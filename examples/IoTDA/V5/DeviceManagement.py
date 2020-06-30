# coding: utf-8
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkiotda.v5 import *


def addDevice(client):
    try:
        node_id = "gf"
        product_id = "5e25d39a3b7c24fa3638804b"
        body = AddDevice(node_id=node_id, product_id=product_id)
        request = AddDeviceRequest(body=body)
        response = client.add_device(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def queryDevices(client):
    try:
        request = ListDevicesRequest()
        response = client.list_devices(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def queryDevice(client):
    try:
        device_id = "5e25d39a3b7c24fa3638804b_nb_0403_1"
        request = ShowDeviceRequest(device_id=device_id)
        response = client.show_device(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def deleteDevice(client):
    try:
        device_id = "5e25d39a3b7c24fa3638804b_nb_0403_1"
        request = DeleteDeviceRequest(device_id=device_id)
        response = client.delete_device(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def updateDevice(client):
    try:
        device_id = "5e25d39a3b7c24fa3638804b_nb_0403_1"
        device_name = "gf"
        description = "5e25d39a3b7c24fa3638804b"
        extension_info = {"aaa": "xxx", "bbb": 0}
        auth_info = {
            "secure_access": "true",
            "timeout": 0
        }
        body = UpdateDevice(device_name=device_name, description=description, extension_info=extension_info,
                            auth_info=auth_info)
        request = UpdateDeviceRequest(device_id=device_id, body=body)
        response = client.update_device(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def resetDeviceSecret(client):
    try:
        device_id = "5e25d39a3b7c24fa3638804b_nb_0403_1"
        actionId = "resetSecret"
        secret = "12345678910"
        body = ResetDeviceSecret(secret=secret)
        request = ResetDeviceSecretRequest(device_id=device_id, action_id=actionId, body=body)
        response = client.reset_device_secret(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def freezeDevice(client):
    try:
        device_id = "5e25d39a3b7c24fa3638804b_nb_0403_1"
        request = FreezeDeviceRequest(device_id=device_id)
        response = client.freeze_device(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def unfreezeDevice(client):
    try:
        device_id = "5e25d39a3b7c24fa3638804b_nb_0403_1"
        request = UnfreezeDeviceRequest(device_id=device_id)
        response = client.unfreeze_device(request)
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

    addDevice(iotda_client)
    queryDevices(iotda_client)
    queryDevice(iotda_client)
    deleteDevice(iotda_client)
    updateDevice(iotda_client)
    resetDeviceSecret(iotda_client)
