# coding: utf-8
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkiotda.v5 import *


def changeRuleStatus(client):
    try:
        rule_id = "5ea8ebe75d6efc01e5a022c8"
        status = "active"
        body = RuleStatus(status=status)
        request = ChangeRuleStatusRequest(rule_id=rule_id, body=body)
        response = client.change_rule_status(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def createRule(client):
    try:
        actions = [
            {
                "addition": [
                    "88cce89f943646cfbda057aed55c4841"
                ],
                "iota_forwarding": {
                    "project_id": "88cce89f943646cfbda057aed55c4841",
                    "region_name": "cn-north-7"
                },
                "type": "IoTA_FORWARDING"
            }
        ]
        condition_group = {
            "conditions": [
                {

                    "device_property_condition": {
                        "filters": [
                            {
                                "operator": ">",
                                "path": "Meter/signalStrength",
                                "value": "0"
                            }
                        ]
                    },
                    "type": "DEVICE_DATA"
                }
            ],
            "time_range": {
                "end_time": "12:02",
                "start_time": "12:00"
            }
        }
        name = "test_createRule_Success"
        rule_type = "DATA_FORWARDING"
        status = "inactive"
        body = Rule(actions=actions, condition_group=condition_group, name=name, rule_type=rule_type, status=status)
        request = CreateRuleRequest(body=body)
        response = client.create_rule(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def deleteRule(client):
    try:
        rule_id = "5ea8ebe75d6efc01e5a022c8"
        request = DeleteRuleRequest(rule_id=rule_id)
        response = client.delete_rule(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def findRule(client):
    try:
        request = ListRulesRequest();
        response = client.list_rules(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def getRuleById(client):
    try:
        rule_id = "5ea8ebe75d6efc01e5a022c8"
        request = ShowRuleRequest(rule_id=rule_id)
        response = client.show_rule(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def updateRule(client):
    try:
        rule_id = "5ea8ebe75d6efc01e5a022c8"
        actions = [
            {
                "addition": [
                    "88cce89f943646cfbda057aed55c4841"
                ],
                "iota_forwarding": {
                    "project_id": "88cce89f943646cfbda057aed55c4841",
                    "region_name": "update"
                },
                "type": "IoTA_FORWARDING"
            }
        ]
        condition_group = {
            "conditions": [
                {

                    "device_property_condition": {
                        "filters": [
                            {
                                "operator": ">",
                                "path": "Meter/signalStrength",
                                "value": "0"
                            }
                        ]
                    },
                    "type": "DEVICE_DATA"
                }
            ],
            "time_range": {
                "end_time": "12:02",
                "start_time": "12:00"
            }
        }
        name = "test_createRule_Success"
        rule_type = "DATA_FORWARDING"
        status = "inactive"
        body = Rule(actions=actions, condition_group=condition_group, name=name, rule_type=rule_type, status=status)
        request = UpdateRuleRequest(rule_id=rule_id, body=body)
        response = client.update_rule(request)
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

    changeRuleStatus(iotda_client)
    createRule(iotda_client)
    deleteRule(iotda_client)
    findRule(iotda_client)
    getRuleById(iotda_client)
    updateRule(iotda_client)
