class BlobException(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__()


class S3Exception(BlobException):
    def __str__(self) -> str:
        return f"S3 Error: {self.message}"


class DynamodbException(BlobException):
    def __str__(self) -> str:
        return f"DynamoDB Error: {self.message}"


class RekognitionException(BlobException):
    def __str__(self) -> str:
        return f"Rekognition Error: {self.message}"
