import json

from service import utils
from usecases import blobs


def blob_post(event: dict, context: dict) -> dict:
    """
    Blob POST method
    :param event: lambda event data
    :param context: lambda context data
    :return: dict
    """
    print(event)

    body = json.loads(event["body"])
    callback_url = body.get("callback_url", None)

    data = blobs.create_blob_process(callback_url)

    return {"statusCode": 200, "body": json.dumps(data, cls=utils.CustomEncoder)}


def blob_get(event: dict, context: dict) -> dict:
    """
    Blob GET method
    :param event: lambda event data
    :param context: lambda context data
    :return: dict
    """
    print(event)

    blob_id = event["pathParameters"]["blob_id"]
    data = blobs.get_blob_from_database(blob_id)

    if not data:
        return {"statusCode": 404}

    return {"statusCode": 200, "body": json.dumps(data, cls=utils.CustomEncoder)}
