import boto3
from botocore.exceptions import ClientError

from service.exceptions import DynamodbException

dynamodb = boto3.resource("dynamodb")


def put(*, table_name: str, data: dict) -> dict:
    """
    insert item in dynamodb
    :param table_name: name of dynamodb table
    :param data: dict data
    """
    table = dynamodb.Table(table_name)

    try:
        response = table.put_item(Item=data)
        return response

    except ClientError as e:
        print(e)
        raise DynamodbException(f"Problem when putting data to {table_name}")


def get(*, table_name: str, search: dict) -> dict:
    """
    get from dynamodb
    :param table_name: name of dynamodb table
    :param data: dict filter
    """
    table = dynamodb.Table(table_name)

    try:
        response = table.get_item(Key=search)
        return response.get("Item")

    except ClientError as e:
        print(e)
        raise DynamodbException(f"Problem when getting data from {table_name}")


def update(
    *,
    table_name: str,
    key: dict,
    update_expression: str,
    attributes: dict,
    return_values: str = "UPDATED_NEW",
) -> dict:
    """
    update data in dynamodb
    :param key:
    """
    table = dynamodb.Table(table_name)

    try:
        response = table.update_item(
            Key=key,
            UpdateExpression=update_expression,
            ExpressionAttributeValues=attributes,
            ReturnValues=return_values,
        )
        return response

    except ClientError as e:
        print(e)
        raise DynamodbException(f"Problem when update data in {table_name}")
