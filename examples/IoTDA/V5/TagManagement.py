# coding: utf-8
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkiotda.v5 import *


def getResourcesByTags(client):
    try:
        resource_type = "device"
        tags = [
            {
                "tag_key": "testTagName",
                "tag_value": "testTagValue"
            }
        ]
        body = QueryResourceByTagsDTO(resource_type=resource_type, tags=tags)
        request = ListResourcesByTagsRequest(body=body)
        response = client.list_resources_by_tags(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def bindTagsToResource(client):
    try:
        resource_id = "5e25d39a3b7c24fa3638804b_nb_0403_1"
        resource_type = "device"
        tags = [
            {
                "tag_key": "testTagName",
                "tag_value": "testTagValue"
            }
        ]
        body = BindTagsDTO(resource_id=resource_id, resource_type=resource_type, tags=tags)
        request = TagDeviceRequest(body=body)
        response = client.tag_device(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def unbindTagsToResource(client):
    try:
        resource_id = "5e25d39a3b7c24fa3638804b_nb_0403_1"
        resource_type = "device"
        tag_keys = ["testTagName"]
        body = UnbindTagsDTO(resource_id=resource_id, resource_type=resource_type, tag_keys=tag_keys)
        request = UntagDeviceRequest(body=body)
        response = client.untag_device(request)
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

    getResourcesByTags(iotda_client)
    bindTagsToResource(iotda_client)
    unbindTagsToResource(iotda_client)
