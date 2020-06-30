# coding: utf-8
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkiotda.v5 import *


def createBatchTask(client):
    try:
        app_id = "vWT2abBX135ioL_D028b7NRYJfYa"
        document = {
            "package_id": "24381244be486f8b3a89ad07"
        }
        targets = [
            "5e19ca2b16b09003ca4dbd98_test003"
        ]
        task_name = "BatchCommandTask"
        task_type = "softwareUpgrade"
        body = CreateBatchTask(app_id=app_id, document=document, targets=targets, task_name=task_name,
                               task_type=task_type)
        request = CreateBatchTaskRequest(body=body)
        response = client.create_batch_task(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def queryBatchTask(client):
    try:
        request = ShowBatchTaskRequest(taskId="5ea53331251c3e02075b1499")
        response = client.show_batch_task(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def queryBatchTasks(client):
    try:
        request = ListBatchTasksRequest(task_type="softwareUpgrade", marker="ffffffffffffffffffffffff")
        response = client.list_batch_tasks(request)
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

    createBatchTask(iotda_client)
    queryBatchTask(iotda_client)
    queryBatchTasks(iotda_client)
