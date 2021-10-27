import boto3
from botocore.exceptions import ClientError

from service.exceptions import RekognitionException

rekognition = boto3.client("rekognition", region_name="us-east-1")


def detect_labels(
    bucket: str, key: str, max_labels: int = 10, min_confidence: int = 90
) -> dict:
    """
    detect labels from images
    :param bucket: bucket name
    :param key: image key
    :param max_labels: max number of labels
    :param min_confidence: label minimum confidence
    """
    try:
        response = rekognition.detect_labels(
            Image={
                "S3Object": {
                    "Bucket": bucket,
                    "Name": key,
                }
            },
            MaxLabels=max_labels,
            MinConfidence=min_confidence,
        )
        return response["Labels"]

    except ClientError as e:
        print(e)
        raise RekognitionException("Problem when call rekognition service")
