# coding: utf-8
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkiotda.v5 import *


def addDeviceGroup(client):
    try:
        description = "GroupA1"
        name = "GroupA2"
        body = AddDeviceGroupDTO(description=description, name=name)
        request = AddDeviceGroupRequest(body=body)
        response = client.add_device_group(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def queryDeviceGroup(client):
    try:
        group_id = "62dcc817-06ad-44f2-aa3a-9760283047b9"
        request = ShowDeviceGroupRequest(group_id=group_id)
        response = client.show_device_group(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def queryDeviceGroupList(client):
    try:
        request = ListDeviceGroupsRequest(instance_id="1a7ffc5c-d89c-44dd-8265-b1653d951bbb")
        response = client.list_device_groups(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def updateDeviceGroup(client):
    try:
        group_id = "62dcc817-06ad-44f2-aa3a-9760283047b9"
        description = "1aaaa"
        name = "1bbbb"
        body = UpdateDeviceGroupDTO(description=description, name=name)
        request = UpdateDeviceGroupRequest(group_id=group_id, body=body)
        response = client.update_device_group(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def deleteDeviceGroup(client):
    try:
        groupId = "62dcc817-06ad-44f2-aa3a-9760283047b9"
        request = DeleteDeviceGroupRequest(group_id=groupId)
        response = client.delete_device_group(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def manageDevicesInGroup(client):
    try:
        groupId = "62dcc817-06ad-44f2-aa3a-9760283047b9"
        actionId = "addDevice"
        deviceId = "5e19ca2b16b09003ca4dbd98_test003"
        request = CreateOrDeleteDeviceInGroupRequest(group_id=groupId, action_id=actionId, device_id=deviceId)
        response = client.create_or_delete_device_in_group(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def queryDevicesInGroup(client):
    try:
        groupId = "62dcc817-06ad-44f2-aa3a-9760283047b9"
        request = ShowDevicesInGroupRequest(group_id=groupId)
        response = client.show_devices_in_group(request)
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

    addDeviceGroup(iotda_client)
    queryDeviceGroup(iotda_client)
    queryDeviceGroupList(iotda_client)
    updateDeviceGroup(iotda_client)
    deleteDeviceGroup(iotda_client)
    manageDevicesInGroup(iotda_client)
    queryDevicesInGroup(iotda_client)
