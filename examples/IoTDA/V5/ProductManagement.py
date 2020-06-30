# coding: utf-8
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkiotda.v5 import *


def queryProduct(client):
    try:
        product_id = "5ea4f9fdda687b03370ad348"
        request = ShowProductRequest(product_id=product_id)
        response = client.show_product(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def queryProducts(client):
    try:
        request = ListProductsRequest()
        response = client.list_products(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def addProduct(client):
    try:
        app_id = "vWT2abBX135ioL_D028b7NRYJfYa"
        data_format = "binary"
        description = "this is a thermometer produced by Huawei"
        device_type = "Thermometer"
        name = "Thermometer"
        protocol_type = "CoAP"
        service_capabilities = [
            {
                "commands": [
                    {
                        "command_name": "reboot",
                        "paras": [
                            {
                                "data_type": "string",
                                "max": 100,
                                "max_length": 100,
                                "min": 1,
                                "para_name": "force",
                                "step": 0.1,
                                "unit": "km/h"
                            }
                        ],
                        "responses": [
                            {
                                "paras": [
                                    {
                                        "data_type": "string",
                                        "max": 100,
                                        "max_length": 100,
                                        "min": 1,
                                        "para_name": "force",
                                        "step": 0.1,
                                        "unit": "km/h"
                                    }
                                ],
                                "response_name": "ACK"
                            }
                        ]
                    }
                ],
                "description": "temperature",
                "events": [
                    {
                        "event_type": "reboot",
                        "paras": [
                            {
                                "data_type": "string",
                                "description": "force",
                                "max": 100,
                                "max_length": 100,
                                "min": 1,
                                "para_name": "force",
                                "step": 0.1,
                                "unit": "km/h"
                            }
                        ]
                    }
                ],
                "option": "Mandatory",
                "properties": [
                    {
                        "data_type": "decimal",
                        "default": {
                            "color": "red",
                            "size": 1
                        },
                        "description": "force",
                        "max": 100,
                        "max_length": 100,
                        "method": "R",
                        "min": 1,
                        "property_name": "temperature",
                        "step": 0.1,
                        "unit": "centigrade"
                    }
                ],
                "service_id": "temperature",
                "service_type": "temperature"
            }
        ]
        body = AddProduct(app_id=app_id, data_format=data_format, description=description, device_type=device_type,
                          name=name, protocol_type=protocol_type, service_capabilities=service_capabilities)
        request = CreateProductRequest(body=body)
        response = client.create_product(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def deleteProduct(client):
    try:
        product_id = "5ea4f9fdda687b03370ad348"
        request = DeleteProductRequest(product_id=product_id)
        response = client.delete_product(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def updateProduct(client):
    try:
        app_id = "vWT2abBX135ioL_D028b7NRYJfYa"
        data_format = "binary",
        description = "this is a thermometer produced by Huawei"
        device_type = "Thermometer"
        name = "Thermometer"
        protocol_type = "CoAP"
        service_capabilities = [
            {
                "commands": [
                    {
                        "command_name": "reboot",
                        "paras": [
                            {
                                "data_type": "int",
                                "max": 100,
                                "max_length": 100,
                                "min": 1,
                                "para_name": "force",
                                "step": 0.1,
                                "unit": "km/h"
                            }
                        ],
                        "responses": [
                            {
                                "paras": [
                                    {
                                        "data_type": "string",
                                        "max": 100,
                                        "max_length": 100,
                                        "min": 1,
                                        "para_name": "force",
                                        "step": 0.1,
                                        "unit": "km/h"
                                    }
                                ],
                                "response_name": "ACK"
                            }
                        ]
                    }
                ],
                "description": "temperature",
                "events": [
                    {
                        "event_type": "reboot",
                        "paras": [
                            {
                                "data_type": "string",
                                "description": "force",
                                "max": 100,
                                "max_length": 100,
                                "min": 1,
                                "para_name": "force",
                                "step": 0.1,
                                "unit": "km/h"
                            }
                        ]
                    }
                ],
                "option": "Mandatory",
                "properties": [
                    {
                        "data_type": "decimal",
                        "default": {
                            "color": "red",
                            "size": 1
                        },
                        "description": "force",
                        "max": 100,
                        "max_length": 100,
                        "method": "RW",
                        "min": 1,
                        "property_name": "temperature",
                        "step": 0.1,
                        "unit": "centigrade"
                    }
                ],
                "service_id": "temperature",
                "service_type": "temperature"
            }
        ]
        body = UpdateProduct(app_id=app_id, data_format=data_format, description=description, device_type=device_type,
                             name=name,
                             protocol_type=protocol_type, service_capabilities=service_capabilities)
        product_id = "5ea4f9fdda687b03370ad348"
        request = UpdateProductRequest(product_id=product_id, body=body)
        response = client.update_product(request)
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

    queryProduct(iotda_client)
    queryProducts(iotda_client)
    addProduct(iotda_client)
    deleteProduct(iotda_client)
    updateProduct(iotda_client)
