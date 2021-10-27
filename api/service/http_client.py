import http.client
import json


def post(*, url: str, path: str, headers: dict, body: dict):
    """
    send http post request
    :param url: url base
    :param path: url path
    :param headers: http headers
    :param body: http body
    :return: http response
    """
    conn = http.client.HTTPSConnection(url)

    json_data = json.dumps(body)
    conn.request("POST", f"{path}", json_data, headers)

    response = conn.getresponse()
    return response
