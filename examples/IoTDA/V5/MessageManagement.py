# coding: utf-8
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkiotda.v5 import *


def createMessage(client):
    try:
        message_id = "1a7ffc5c-d89c-44dd-8265-b1653d951ce3",
        name = "ON_OFF",
        message = {
            "value": "1"
        }
        body = DeviceMessageRequest(message_id=message_id, message=message, name=name)
        device_id = "5eec67a68dd70c048a18dd31_wq_0620"
        request = CreateMessageRequest(body=body, device_id=device_id)
        response = client.create_message(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def listDeviceMessages(client):
    try:
        device_id = "5eec67a68dd70c048a18dd31_wq_0620"
        request = ListDeviceMessagesRequest(device_id=device_id)
        response = client.list_device_messages(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def showDeviceMessage(client):
    try:
        device_id = "5eec67a68dd70c048a18dd31_wq_0620"
        message_id = "1a7ffc5c-d89c-44dd-8265-b1653d951ce3"
        request = ShowDeviceMessageRequest(device_id=device_id, message_id=message_id)
        response = client.show_device_message(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


if __name__ == '__main__':
    ak = "{your ak string}"
    sk = "{your sk string}"
    endpoint = "{your endpoint}"
    project_id = "{your project id}"

    config = HttpConfig.get_default_config()
    config.ignore_ssl_verification = True
    credentials = BasicCredentials(ak, sk, project_id)

    iotda_client = IoTDAClient().new_builder(IoTDAClient) \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_endpoint(endpoint) \
        .build()

    showDeviceMessage(iotda_client)
    listDeviceMessages(iotda_client)
    createMessage(iotda_client)
