import json
import urllib
import uuid
from decimal import Decimal

from service import http_client, utils
from service.aws import dynamodb_handler, rekognition_handler, s3_handler
from service.config import DYNAMODB_TABLE, S3_BUCKET
from service.exceptions import BlobException


def create_blob_process(callback_url: str = None) -> dict:
    """
    usecase that create a blob process
    :param callback_url: callback url used to notify client
    :return: dict
    """
    try:
        # generate blob_id
        blob_id = str(uuid.uuid4())

        # create s3 presigned url
        s3_response = s3_handler.create_presigned_url(S3_BUCKET, blob_id)

        # create dynamodb register
        dynamodb_handler.put(
            table_name=DYNAMODB_TABLE,
            data={
                "pk": blob_id,
                "callback_url": callback_url,
                "labels": None,
            },
        )

    except BlobException as e:
        return {"error": str(e)}

    body = {"blob_id": str(blob_id), "presigned_url": s3_response}

    return body


def get_blob_from_database(blob_id: str) -> dict:
    """
    get blob processed in database
    :param blob_id: blob dynamodb key uuid
    """

    try:
        # get in dynamodb
        data = dynamodb_handler.get(table_name=DYNAMODB_TABLE, search={"pk": blob_id})
        data.pop("pk")
        data.pop("callback_url")

    except BlobException as e:
        return {"error": str(e)}

    return data


def recognize_image(blob_id: str) -> dict:
    """
    recognize image
    :param blob_id: blob id
    """
    try:
        # get rekognition labels
        data = rekognition_handler.detect_labels(S3_BUCKET, blob_id)
        data = json.loads(json.dumps(data), parse_float=Decimal)

        # update dynamodb register
        dynamodb_handler.update(
            table_name=DYNAMODB_TABLE,
            key={"pk": blob_id},
            update_expression="set labels = :data",
            attributes={":data": data},
        )

    except BlobException as e:
        return {"error": str(e)}

    return data


def send_callback_url_data(data: dict) -> None:
    """
    send data to callback_url
    :param data: dynamodb data
    """
    data = utils.unmarshal_dynamodb_json(data)

    # callback url
    callback_url = data.get("callback_url", None)

    if callback_url:

        print("sending data to callback url")
        url = urllib.parse.urlparse(callback_url)

        data["blob_id"] = data.pop("pk")
        data.pop("callback_url")

        response = http_client.post(
            url=url.netloc,
            path=url.path,
            headers={"Content-Type": "application/json"},
            body=data,
        )

        if 200 <= response.getcode() <= 299:
            print("request sent successfully")
        else:
            print("problem when sent data to callback_url")
