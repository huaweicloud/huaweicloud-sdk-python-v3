# coding: utf-8
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkiotda.v5 import *


def createCommand(client):
    try:
        service_id = "APP_STATUS"
        command_name = "reboot"
        paras = {
            "value": "1"
        }
        body = DeviceCommandRequest(paras=paras, service_id=service_id, command_name=command_name)
        device_id = "5eec67a68dd70c048a18dd31_wq_0620"

        request = CreateCommandRequest(device_id=device_id, body=body)
        response = client.create_command(request)
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

    createCommand(iotda_client)
