# coding: utf-8
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkiotda.v5 import *


def createSubscription(client):
    try:
        callbackurl = "https://10.10.10.10:443/deviceActivate"
        channel = "http"
        subject = {
            "event": "activate",
            "resource": "device"
        }
        body = CreateSubReq(callbackurl=callbackurl, channel=channel, subject=subject)
        request = CreateSubscriptionRequest(body=body)
        response = client.create_subscription(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def deleteOneSubscription(client):
    try:
        subscription_id = "7eaed2d9-fc12-48ef-94f5-31e3db761124"
        request = DeleteSubscriptionRequest(subscription_id=subscription_id)
        response = client.delete_subscription(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def findOneSubscription(client):
    try:
        subscription_id = "7eaed2d9-fc12-48ef-94f5-31e3db761124"
        request = ShowSubscriptionRequest(subscription_id=subscription_id)
        response = client.show_subscription(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def findSubscriptions(client):
    try:
        request = ListSubscriptionsRequest()
        response = client.list_subscriptions(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def updateSubscription(client):
    try:
        subscription_id = "1568ad27-bf8e-4be3-8fd4-b56ccb468458"
        callbackurl = "https://0.0.0.0:443/deviceActivate"
        body = UpdateSubReq(callbackurl=callbackurl)
        request = UpdateSubscriptionRequest(subscription_id=subscription_id, body=body)
        response = client.update_subscription(request)
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

    createSubscription(iotda_client)
    deleteOneSubscription(iotda_client)
    findOneSubscription(iotda_client)
    findSubscriptions(iotda_client)
    updateSubscription(iotda_client)
