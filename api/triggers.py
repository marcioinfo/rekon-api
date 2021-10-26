from usecases.blobs import recognize_image, send_callback_url_data


def trigger_rekognition(event: dict, context: dict) -> dict:
    """
    trigger rekognition
    call rekognition for s3 image after s3 put
    :param event: lambda event
    :param context: lambda context
    """
    print(event)

    blob_id = event["Records"][0]["s3"]["object"]["key"]
    recognize_image(blob_id)


def trigger_callback_url(event: dict, context: dict) -> None:
    """
    trigger callback_url
    used to send data to callback_url after blob update in dynamodb
    :param event: lambda event
    :param context: lambda context
    """
    print(event)
    event_name = event["Records"][0]["eventName"]

    # send request only for modification operations
    if event_name == "MODIFY":

        # get dynamodb new image from stream
        data = event["Records"][0]["dynamodb"]["NewImage"]
        send_callback_url_data(data)
