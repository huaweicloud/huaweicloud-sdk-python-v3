# coding: utf-8
import logging

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkvpc.v2 import *


def list_vpc(client):
    try:
        request = ListVpcsRequest()
        response = client.list_vpcs_async(request)
        print(response.result())
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


if __name__ == "__main__":
    ak = "{your ak string}"
    sk = "{your sk string}"
    endpoint = "{your endpoint}"
    project_id = "{your project id}"

    config = HttpConfig.get_default_config()
    config.ignore_ssl_verification = True
    credentials = BasicCredentials(ak, sk, project_id)

    vpc_client = VpcAsyncClient.new_builder(VpcAsyncClient) \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_endpoint(endpoint) \
        .with_file_log(path="vpc.log", log_level=logging.DEBUG) \
        .with_stream_log(log_level=logging.DEBUG) \
        .build()

    list_vpc(vpc_client)
