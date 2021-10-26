import boto3
from botocore.exceptions import ClientError

from service.exceptions import S3Exception


def create_presigned_url(
    bucket_name: str, object_name: str, expiration: int = 3600
) -> dict:
    """
    Generate a presigned URL to share an S3 object
    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """

    s3_client = boto3.client("s3")
    try:
        response = s3_client.generate_presigned_url(
            "put_object",
            ExpiresIn=expiration,
            Params={"Bucket": bucket_name, "Key": object_name},
            HttpMethod="PUT",
        )
    except ClientError as e:
        print(e)
        raise S3Exception("Problem when creating s3 presigned url")

    return response
