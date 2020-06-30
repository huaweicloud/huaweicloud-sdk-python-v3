# coding: utf-8
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkiotda.v5 import *


def updateDeviceShadow(client):
    try:
        deviceId = "5e25d39a3b7c24fa3638804b_nb_0403_1"
        shadow = [{
            "desired": {
                "aaa": "60",
                "bbb": 10
            },
            "service_id": "serviceId1_s2l0HvEzi8"
        }]
        body = UpdateDesireds(shadow=shadow)
        request = UpdateDeviceShadowDesiredDataRequest(device_id=deviceId, body=body)
        response = client.update_device_shadow_desired_data(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def getDeviceShadow(client):
    try:
        deviceId = "5e25d39a3b7c24fa3638804b_nb_0403_1"
        request = ShowDeviceShadowRequest(device_id=deviceId)
        response = client.show_device_shadow(request)
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

    updateDeviceShadow(iotda_client)
    getDeviceShadow(iotda_client)
