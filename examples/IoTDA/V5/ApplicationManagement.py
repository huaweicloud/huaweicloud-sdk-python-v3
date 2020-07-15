# coding: utf-8
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkiotda.v5 import *


def getApplications(client):
    try:
        request = ShowApplicationsRequest()
        response = client.show_applications(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def deleteApplication(client):
    try:
        app_id = "e5b55cb2489f40a8af0e0feaae491188"
        request = DeleteApplicationRequest(app_id=app_id)
        response = client.delete_application(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)

def getApplication(client):
    try:
        app_id = "21f57f68bbe342908a915232fbf88ad9"
        request = ShowApplicationRequest(app_id=app_id)
        response = client.show_application(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def addApplication(client):
    try:
        app_name = "testApp2"
        body = AddApplication(app_name=app_name)
        request = AddApplicationRequest(body=body)
        response = client.add_application(request)
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

    getApplications(iotda_client)
    getApplication(iotda_client)
    deleteApplication(iotda_client)
    addApplication(iotda_client)
