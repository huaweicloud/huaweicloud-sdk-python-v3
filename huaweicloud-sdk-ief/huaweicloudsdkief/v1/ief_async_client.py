# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

import six

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class IefAsyncClient(Client):
    """
    :param configuration: .Configuration object for this client
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def __init__(self):
        super(IefAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkief.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "IefClient":
            raise TypeError("client type error, support client type is IefClient")

        return ClientBuilder(clazz)

    def batch_add_delete_tags_async(self, request):
        """批量添加删除资源标签

        为指定实例批量添加或删除标签。 一个资源上最多有20个标签。  说明： - 此接口为幂等接口，创建时如果请求体中存在重复key则报错。 - 创建时不允许设置重复key数据,如果数据库已存在该key，就覆盖value的值。 - 删除时不对标签字符集范围做校验，如果删除的标签不存在，默认处理成功。删除时tags结构体不能缺失，key不能为空，或者空字符串。

        :param BatchAddDeleteTagsRequest request
        :return: BatchAddDeleteTagsResponse
        """
        return self.batch_add_delete_tags_with_http_info(request)

    def batch_add_delete_tags_with_http_info(self, request):
        """批量添加删除资源标签

        为指定实例批量添加或删除标签。 一个资源上最多有20个标签。  说明： - 此接口为幂等接口，创建时如果请求体中存在重复key则报错。 - 创建时不允许设置重复key数据,如果数据库已存在该key，就覆盖value的值。 - 删除时不对标签字符集范围做校验，如果删除的标签不存在，默认处理成功。删除时tags结构体不能缺失，key不能为空，或者空字符串。

        :param BatchAddDeleteTagsRequest request
        :return: BatchAddDeleteTagsResponse
        """

        all_params = ['resource_type', 'resource_id', 'ief_instance_id', 'tags']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/{resource_type}/{resource_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchAddDeleteTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_app_async(self, request):
        """创建应用模板

        该API用于创建一个应用模板。

        :param CreateAppRequest request
        :return: CreateAppResponse
        """
        return self.create_app_with_http_info(request)

    def create_app_with_http_info(self, request):
        """创建应用模板

        该API用于创建一个应用模板。

        :param CreateAppRequest request
        :return: CreateAppResponse
        """

        all_params = ['app', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/apps',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_app_versions_async(self, request):
        """创建应用模板版本

        创建一个应用模板版本

        :param CreateAppVersionsRequest request
        :return: CreateAppVersionsResponse
        """
        return self.create_app_versions_with_http_info(request)

    def create_app_versions_with_http_info(self, request):
        """创建应用模板版本

        创建一个应用模板版本

        :param CreateAppVersionsRequest request
        :return: CreateAppVersionsResponse
        """

        all_params = ['app_id', 'version', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/apps/{app_id}/versions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAppVersionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_config_map_async(self, request):
        """创建配置项

        创建配置项

        :param CreateConfigMapRequest request
        :return: CreateConfigMapResponse
        """
        return self.create_config_map_with_http_info(request)

    def create_config_map_with_http_info(self, request):
        """创建配置项

        创建配置项

        :param CreateConfigMapRequest request
        :return: CreateConfigMapResponse
        """

        all_params = ['create_config_map', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/configmaps',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateConfigMapResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_deployments_async(self, request):
        """创建部署

        创建部署

        :param CreateDeploymentsRequest request
        :return: CreateDeploymentsResponse
        """
        return self.create_deployments_with_http_info(request)

    def create_deployments_with_http_info(self, request):
        """创建部署

        创建部署

        :param CreateDeploymentsRequest request
        :return: CreateDeploymentsResponse
        """

        all_params = ['create_deployments', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/edgemgr/deployments',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateDeploymentsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_device_async(self, request):
        """注册终端设备

        该API用于注册一个终端设备。

        :param CreateDeviceRequest request
        :return: CreateDeviceResponse
        """
        return self.create_device_with_http_info(request)

    def create_device_with_http_info(self, request):
        """注册终端设备

        该API用于注册一个终端设备。

        :param CreateDeviceRequest request
        :return: CreateDeviceResponse
        """

        all_params = ['create_device', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/devices',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_device_template_async(self, request):
        """创建终端设备模板

        创建一个终端设备模板

        :param CreateDeviceTemplateRequest request
        :return: CreateDeviceTemplateResponse
        """
        return self.create_device_template_with_http_info(request)

    def create_device_template_with_http_info(self, request):
        """创建终端设备模板

        创建一个终端设备模板

        :param CreateDeviceTemplateRequest request
        :return: CreateDeviceTemplateResponse
        """

        all_params = ['device_template', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/device-templates',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateDeviceTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_edge_node_async(self, request):
        """注册边缘节点

        该API用于注册一个边缘节点。接口调用成功后，您可以将响应消息体中node.package字段使用base64解码成tar.gz文件，并在控制台下载边缘核心软件，然后纳管边缘节点。

        :param CreateEdgeNodeRequest request
        :return: CreateEdgeNodeResponse
        """
        return self.create_edge_node_with_http_info(request)

    def create_edge_node_with_http_info(self, request):
        """注册边缘节点

        该API用于注册一个边缘节点。接口调用成功后，您可以将响应消息体中node.package字段使用base64解码成tar.gz文件，并在控制台下载边缘核心软件，然后纳管边缘节点。

        :param CreateEdgeNodeRequest request
        :return: CreateEdgeNodeResponse
        """

        all_params = ['create_edge_node', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/nodes',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateEdgeNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_edge_node_certs_async(self, request):
        """创建节点证书

        创建边缘节点上的应用证书和设备证书。

        :param CreateEdgeNodeCertsRequest request
        :return: CreateEdgeNodeCertsResponse
        """
        return self.create_edge_node_certs_with_http_info(request)

    def create_edge_node_certs_with_http_info(self, request):
        """创建节点证书

        创建边缘节点上的应用证书和设备证书。

        :param CreateEdgeNodeCertsRequest request
        :return: CreateEdgeNodeCertsResponse
        """

        all_params = ['node_id', 'create_edge_node_certs', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/nodes/{node_id}/certs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateEdgeNodeCertsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_endpoint_async(self, request):
        """创建端点

        创建一个端点

        :param CreateEndpointRequest request
        :return: CreateEndpointResponse
        """
        return self.create_endpoint_with_http_info(request)

    def create_endpoint_with_http_info(self, request):
        """创建端点

        创建一个端点

        :param CreateEndpointRequest request
        :return: CreateEndpointResponse
        """

        all_params = ['create_endpoint', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/routemgr/endpoints',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateEndpointResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_rule_async(self, request):
        """创建规则

        创建一条规则

        :param CreateRuleRequest request
        :return: CreateRuleResponse
        """
        return self.create_rule_with_http_info(request)

    def create_rule_with_http_info(self, request):
        """创建规则

        创建一条规则

        :param CreateRuleRequest request
        :return: CreateRuleResponse
        """

        all_params = ['ief_instance_id', 'create_rule']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/routemgr/rules',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_secret_async(self, request):
        """创建密钥

        创建密钥

        :param CreateSecretRequest request
        :return: CreateSecretResponse
        """
        return self.create_secret_with_http_info(request)

    def create_secret_with_http_info(self, request):
        """创建密钥

        创建密钥

        :param CreateSecretRequest request
        :return: CreateSecretResponse
        """

        all_params = ['create_secret', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/secrets',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateSecretResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_service_async(self, request):
        """创建服务

        创建一个服务

        :param CreateServiceRequest request
        :return: CreateServiceResponse
        """
        return self.create_service_with_http_info(request)

    def create_service_with_http_info(self, request):
        """创建服务

        创建一个服务

        :param CreateServiceRequest request
        :return: CreateServiceResponse
        """

        all_params = ['ief_instance_id', 'create_service']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/services',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateServiceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_tag_async(self, request):
        """添加资源标签

        为资源添加标签。 一个资源上最多有20个标签。 此接口为幂等接口，创建时，如果创建的标签已经存在（key相同），则覆盖。

        :param CreateTagRequest request
        :return: CreateTagResponse
        """
        return self.create_tag_with_http_info(request)

    def create_tag_with_http_info(self, request):
        """添加资源标签

        为资源添加标签。 一个资源上最多有20个标签。 此接口为幂等接口，创建时，如果创建的标签已经存在（key相同），则覆盖。

        :param CreateTagRequest request
        :return: CreateTagResponse
        """

        all_params = ['resource_id', 'resource_type', 'tag', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/{resource_type}/{resource_id}/tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_app_async(self, request):
        """删除应用模板

        删除应用模板

        :param DeleteAppRequest request
        :return: DeleteAppResponse
        """
        return self.delete_app_with_http_info(request)

    def delete_app_with_http_info(self, request):
        """删除应用模板

        删除应用模板

        :param DeleteAppRequest request
        :return: DeleteAppResponse
        """

        all_params = ['app_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/apps/{app_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_app_version_async(self, request):
        """删除应用版本

        删除应用版本

        :param DeleteAppVersionRequest request
        :return: DeleteAppVersionResponse
        """
        return self.delete_app_version_with_http_info(request)

    def delete_app_version_with_http_info(self, request):
        """删除应用版本

        删除应用版本

        :param DeleteAppVersionRequest request
        :return: DeleteAppVersionResponse
        """

        all_params = ['app_id', 'version_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/apps/{app_id}/versions/{version_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteAppVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_config_map_async(self, request):
        """删除配置项

        删除配置项

        :param DeleteConfigMapRequest request
        :return: DeleteConfigMapResponse
        """
        return self.delete_config_map_with_http_info(request)

    def delete_config_map_with_http_info(self, request):
        """删除配置项

        删除配置项

        :param DeleteConfigMapRequest request
        :return: DeleteConfigMapResponse
        """

        all_params = ['configmap_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'configmap_id' in local_var_params:
            path_params['configmap_id'] = local_var_params['configmap_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/configmaps/{configmap_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteConfigMapResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_deployment_async(self, request):
        """删除部署

        删除应用部署

        :param DeleteDeploymentRequest request
        :return: DeleteDeploymentResponse
        """
        return self.delete_deployment_with_http_info(request)

    def delete_deployment_with_http_info(self, request):
        """删除部署

        删除应用部署

        :param DeleteDeploymentRequest request
        :return: DeleteDeploymentResponse
        """

        all_params = ['deployment_id', 'ief_instance_id', 'force_delete']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

        query_params = []
        if 'force_delete' in local_var_params:
            query_params.append(('force_delete', local_var_params['force_delete']))

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/edgemgr/deployments/{deployment_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteDeploymentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_device_async(self, request):
        """删除终端设备

        该API用于删除终端设备。

        :param DeleteDeviceRequest request
        :return: DeleteDeviceResponse
        """
        return self.delete_device_with_http_info(request)

    def delete_device_with_http_info(self, request):
        """删除终端设备

        该API用于删除终端设备。

        :param DeleteDeviceRequest request
        :return: DeleteDeviceResponse
        """

        all_params = ['device_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/devices/{device_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_device_template_async(self, request):
        """删除终端设备模板

        删除终端设备模板

        :param DeleteDeviceTemplateRequest request
        :return: DeleteDeviceTemplateResponse
        """
        return self.delete_device_template_with_http_info(request)

    def delete_device_template_with_http_info(self, request):
        """删除终端设备模板

        删除终端设备模板

        :param DeleteDeviceTemplateRequest request
        :return: DeleteDeviceTemplateResponse
        """

        all_params = ['device_template_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_template_id' in local_var_params:
            path_params['device_template_id'] = local_var_params['device_template_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/device-templates/{device_template_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteDeviceTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_edge_node_async(self, request):
        """删除边缘节点

        删除边缘节点

        :param DeleteEdgeNodeRequest request
        :return: DeleteEdgeNodeResponse
        """
        return self.delete_edge_node_with_http_info(request)

    def delete_edge_node_with_http_info(self, request):
        """删除边缘节点

        删除边缘节点

        :param DeleteEdgeNodeRequest request
        :return: DeleteEdgeNodeResponse
        """

        all_params = ['node_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/nodes/{node_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteEdgeNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_edge_node_certs_async(self, request):
        """删除节点证书

        删除边缘节点上的证书（目前只支持删除应用证书和设备证书）

        :param DeleteEdgeNodeCertsRequest request
        :return: DeleteEdgeNodeCertsResponse
        """
        return self.delete_edge_node_certs_with_http_info(request)

    def delete_edge_node_certs_with_http_info(self, request):
        """删除节点证书

        删除边缘节点上的证书（目前只支持删除应用证书和设备证书）

        :param DeleteEdgeNodeCertsRequest request
        :return: DeleteEdgeNodeCertsResponse
        """

        all_params = ['node_id', 'cert_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']
        if 'cert_id' in local_var_params:
            path_params['cert_id'] = local_var_params['cert_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/nodes/{node_id}/certs/{cert_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteEdgeNodeCertsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_end_point_async(self, request):
        """删除一个端点

        删除一个端点

        :param DeleteEndPointRequest request
        :return: DeleteEndPointResponse
        """
        return self.delete_end_point_with_http_info(request)

    def delete_end_point_with_http_info(self, request):
        """删除一个端点

        删除一个端点

        :param DeleteEndPointRequest request
        :return: DeleteEndPointResponse
        """

        all_params = ['endpoint_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'endpoint_id' in local_var_params:
            path_params['endpoint_id'] = local_var_params['endpoint_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/routemgr/endpoints/{endpoint_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteEndPointResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_resource_tag_async(self, request):
        """删除资源标签

        删除资源标签。删除时不对标签字符集做校验，调用前必须要做encodeURI，服务端需要对接口uri做decodeURI。删除的key不存在报404，Key不能为空或者空字符串。

        :param DeleteResourceTagRequest request
        :return: DeleteResourceTagResponse
        """
        return self.delete_resource_tag_with_http_info(request)

    def delete_resource_tag_with_http_info(self, request):
        """删除资源标签

        删除资源标签。删除时不对标签字符集做校验，调用前必须要做encodeURI，服务端需要对接口uri做decodeURI。删除的key不存在报404，Key不能为空或者空字符串。

        :param DeleteResourceTagRequest request
        :return: DeleteResourceTagResponse
        """

        all_params = ['resource_type', 'resource_id', 'key', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/{resource_type}/{resource_id}/tags/{key}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteResourceTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_rule_async(self, request):
        """删除规则

        删除一条规则

        :param DeleteRuleRequest request
        :return: DeleteRuleResponse
        """
        return self.delete_rule_with_http_info(request)

    def delete_rule_with_http_info(self, request):
        """删除规则

        删除一条规则

        :param DeleteRuleRequest request
        :return: DeleteRuleResponse
        """

        all_params = ['rule_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/routemgr/rules/{rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_secret_async(self, request):
        """删除密钥

        删除密钥

        :param DeleteSecretRequest request
        :return: DeleteSecretResponse
        """
        return self.delete_secret_with_http_info(request)

    def delete_secret_with_http_info(self, request):
        """删除密钥

        删除密钥

        :param DeleteSecretRequest request
        :return: DeleteSecretResponse
        """

        all_params = ['secret_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'secret_id' in local_var_params:
            path_params['secret_id'] = local_var_params['secret_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/secrets/{secret_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteSecretResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_service_async(self, request):
        """删除服务

        删除一个服务

        :param DeleteServiceRequest request
        :return: DeleteServiceResponse
        """
        return self.delete_service_with_http_info(request)

    def delete_service_with_http_info(self, request):
        """删除服务

        删除一个服务

        :param DeleteServiceRequest request
        :return: DeleteServiceResponse
        """

        all_params = ['service_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/services/{service_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteServiceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def enable_disable_edge_nodes_async(self, request):
        """启用停用边缘节点

        该API用于启用停用边缘节点。被停用的边缘节点将无法连接到云端服务，可用该URI启用边缘节点恢复连接。

        :param EnableDisableEdgeNodesRequest request
        :return: EnableDisableEdgeNodesResponse
        """
        return self.enable_disable_edge_nodes_with_http_info(request)

    def enable_disable_edge_nodes_with_http_info(self, request):
        """启用停用边缘节点

        该API用于启用停用边缘节点。被停用的边缘节点将无法连接到云端服务，可用该URI启用边缘节点恢复连接。

        :param EnableDisableEdgeNodesRequest request
        :return: EnableDisableEdgeNodesResponse
        """

        all_params = ['node_id', 'node', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/nodes/{node_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='EnableDisableEdgeNodesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_app_versions_async(self, request):
        """查询应用模板版本列表

        查询应用模板版本列表

        :param ListAppVersionsRequest request
        :return: ListAppVersionsResponse
        """
        return self.list_app_versions_with_http_info(request)

    def list_app_versions_with_http_info(self, request):
        """查询应用模板版本列表

        查询应用模板版本列表

        :param ListAppVersionsRequest request
        :return: ListAppVersionsResponse
        """

        all_params = ['app_id', 'ief_instance_id', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/apps/{app_id}/versions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAppVersionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_apps_async(self, request):
        """查询应用模板列表

        查询应用模板列表

        :param ListAppsRequest request
        :return: ListAppsResponse
        """
        return self.list_apps_with_http_info(request)

    def list_apps_with_http_info(self, request):
        """查询应用模板列表

        查询应用模板列表

        :param ListAppsRequest request
        :return: ListAppsResponse
        """

        all_params = ['ief_instance_id', 'name', 'limit', 'offset', 'alias', 'visibility']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'alias' in local_var_params:
            query_params.append(('alias', local_var_params['alias']))
        if 'visibility' in local_var_params:
            query_params.append(('visibility', local_var_params['visibility']))

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/apps',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAppsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_config_maps_async(self, request):
        """查询配置项列表

        查询配置项列表

        :param ListConfigMapsRequest request
        :return: ListConfigMapsResponse
        """
        return self.list_config_maps_with_http_info(request)

    def list_config_maps_with_http_info(self, request):
        """查询配置项列表

        查询配置项列表

        :param ListConfigMapsRequest request
        :return: ListConfigMapsResponse
        """

        all_params = ['ief_instance_id', 'name', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/configmaps',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListConfigMapsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_deployments_async(self, request):
        """查询部署列表

        查询部署列表

        :param ListDeploymentsRequest request
        :return: ListDeploymentsResponse
        """
        return self.list_deployments_with_http_info(request)

    def list_deployments_with_http_info(self, request):
        """查询部署列表

        查询部署列表

        :param ListDeploymentsRequest request
        :return: ListDeploymentsResponse
        """

        all_params = ['ief_instance_id', 'limit', 'offset', 'sort', 'name', 'node_id', 'group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/edgemgr/deployments',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListDeploymentsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_device_templates_async(self, request):
        """查询终端设备模板列表

        查询终端设备模板列表

        :param ListDeviceTemplatesRequest request
        :return: ListDeviceTemplatesResponse
        """
        return self.list_device_templates_with_http_info(request)

    def list_device_templates_with_http_info(self, request):
        """查询终端设备模板列表

        查询终端设备模板列表

        :param ListDeviceTemplatesRequest request
        :return: ListDeviceTemplatesResponse
        """

        all_params = ['ief_instance_id', 'name', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/device-templates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListDeviceTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_devices_async(self, request):
        """查询终端设备列表

        该API用于查询终端设备列表。

        :param ListDevicesRequest request
        :return: ListDevicesResponse
        """
        return self.list_devices_with_http_info(request)

    def list_devices_with_http_info(self, request):
        """查询终端设备列表

        该API用于查询终端设备列表。

        :param ListDevicesRequest request
        :return: ListDevicesResponse
        """

        all_params = ['ief_instance_id', 'name', 'node_id', 'limit', 'offset', 'is_binding', 'tags']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'is_binding' in local_var_params:
            query_params.append(('is_binding', local_var_params['is_binding']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/devices',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListDevicesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_edge_node_certs_async(self, request):
        """查询节点证书

        查询边缘节点上的应用证书和设备证书。

        :param ListEdgeNodeCertsRequest request
        :return: ListEdgeNodeCertsResponse
        """
        return self.list_edge_node_certs_with_http_info(request)

    def list_edge_node_certs_with_http_info(self, request):
        """查询节点证书

        查询边缘节点上的应用证书和设备证书。

        :param ListEdgeNodeCertsRequest request
        :return: ListEdgeNodeCertsResponse
        """

        all_params = ['node_id', 'ief_instance_id', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/nodes/{node_id}/certs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListEdgeNodeCertsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_edge_nodes_async(self, request):
        """查询边缘节点列表

        该API用于查询边缘节点。 - 如果不携带任何检索参数，将返回该租户的所有边缘节点信息。 - app_name和tags不支持复合查询，如果同时存在则返回tags查询结果，可以同时携带多个其他检索参数，可同时生效。

        :param ListEdgeNodesRequest request
        :return: ListEdgeNodesResponse
        """
        return self.list_edge_nodes_with_http_info(request)

    def list_edge_nodes_with_http_info(self, request):
        """查询边缘节点列表

        该API用于查询边缘节点。 - 如果不携带任何检索参数，将返回该租户的所有边缘节点信息。 - app_name和tags不支持复合查询，如果同时存在则返回tags查询结果，可以同时携带多个其他检索参数，可同时生效。

        :param ListEdgeNodesRequest request
        :return: ListEdgeNodesResponse
        """

        all_params = ['name', 'limit', 'offset', 'device_id', 'device_name', 'app_name', 'tags', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'device_id' in local_var_params:
            query_params.append(('device_id', local_var_params['device_id']))
        if 'device_name' in local_var_params:
            query_params.append(('device_name', local_var_params['device_name']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/nodes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListEdgeNodesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_endpoints_async(self, request):
        """查询端点列表

        获取所有的端点详情。 如果不携带任何检索参数，将返回该租户的所有端点信息和系统中所有的共享端点。 如果同时指定is_shared=true和其他参数，同样还会对name、type进行过滤。

        :param ListEndpointsRequest request
        :return: ListEndpointsResponse
        """
        return self.list_endpoints_with_http_info(request)

    def list_endpoints_with_http_info(self, request):
        """查询端点列表

        获取所有的端点详情。 如果不携带任何检索参数，将返回该租户的所有端点信息和系统中所有的共享端点。 如果同时指定is_shared=true和其他参数，同样还会对name、type进行过滤。

        :param ListEndpointsRequest request
        :return: ListEndpointsResponse
        """

        all_params = ['ief_instance_id', 'name', 'type', 'is_shared', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'is_shared' in local_var_params:
            query_params.append(('is_shared', local_var_params['is_shared']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/routemgr/endpoints',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListEndpointsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_pods_async(self, request):
        """查询应用实例列表

        查询应用实例列表

        :param ListPodsRequest request
        :return: ListPodsResponse
        """
        return self.list_pods_with_http_info(request)

    def list_pods_with_http_info(self, request):
        """查询应用实例列表

        查询应用实例列表

        :param ListPodsRequest request
        :return: ListPodsResponse
        """

        all_params = ['node_id', 'group_id', 'deployment_id', 'deployment_ids', 'limit', 'offset', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'deployment_id' in local_var_params:
            query_params.append(('deployment_id', local_var_params['deployment_id']))
        if 'deployment_ids' in local_var_params:
            query_params.append(('deployment_ids', local_var_params['deployment_ids']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/edgemgr/pods',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPodsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_resource_by_tags_async(self, request):
        """查询资源实例

        使用标签过滤实例

        :param ListResourceByTagsRequest request
        :return: ListResourceByTagsResponse
        """
        return self.list_resource_by_tags_with_http_info(request)

    def list_resource_by_tags_with_http_info(self, request):
        """查询资源实例

        使用标签过滤实例

        :param ListResourceByTagsRequest request
        :return: ListResourceByTagsResponse
        """

        all_params = ['resource_type', 'list_resource_by_tags', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/{resource_type}/resource_instances/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListResourceByTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_rule_errors_async(self, request):
        """查询规则错误列表

        查询特定规则下的所有错误列表

        :param ListRuleErrorsRequest request
        :return: ListRuleErrorsResponse
        """
        return self.list_rule_errors_with_http_info(request)

    def list_rule_errors_with_http_info(self, request):
        """查询规则错误列表

        查询特定规则下的所有错误列表

        :param ListRuleErrorsRequest request
        :return: ListRuleErrorsResponse
        """

        all_params = ['rule_id', 'ief_instance_id', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/routemgr/rules/{rule_id}/errors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRuleErrorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_rules_async(self, request):
        """查询规则列表

        查询到所有的规则

        :param ListRulesRequest request
        :return: ListRulesResponse
        """
        return self.list_rules_with_http_info(request)

    def list_rules_with_http_info(self, request):
        """查询规则列表

        查询到所有的规则

        :param ListRulesRequest request
        :return: ListRulesResponse
        """

        all_params = ['ief_instance_id', 'name', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/routemgr/rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_secrets_async(self, request):
        """查询密钥列表

        查询密钥列表

        :param ListSecretsRequest request
        :return: ListSecretsResponse
        """
        return self.list_secrets_with_http_info(request)

    def list_secrets_with_http_info(self, request):
        """查询密钥列表

        查询密钥列表

        :param ListSecretsRequest request
        :return: ListSecretsResponse
        """

        all_params = ['ief_instance_id', 'name', 'limit', 'offset', 'sort']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/secrets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSecretsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_services_async(self, request):
        """查询服务列表

        获取所有的服务详情

        :param ListServicesRequest request
        :return: ListServicesResponse
        """
        return self.list_services_with_http_info(request)

    def list_services_with_http_info(self, request):
        """查询服务列表

        获取所有的服务详情

        :param ListServicesRequest request
        :return: ListServicesResponse
        """

        all_params = ['ief_instance_id', 'limit', 'offset', 'sorted', 'name', 'app']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sorted' in local_var_params:
            query_params.append(('sorted', local_var_params['sorted']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/services',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListServicesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_tags_async(self, request):
        """查询资源标签

        查询指定实例的标签信息

        :param ListTagsRequest request
        :return: ListTagsResponse
        """
        return self.list_tags_with_http_info(request)

    def list_tags_with_http_info(self, request):
        """查询资源标签

        查询指定实例的标签信息

        :param ListTagsRequest request
        :return: ListTagsResponse
        """

        all_params = ['resource_id', 'resource_type', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/{resource_type}/{resource_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_tags_by_resource_type_async(self, request):
        """查询项目标签

        查询指定项目中实例类型的所有资源标签集合

        :param ListTagsByResourceTypeRequest request
        :return: ListTagsByResourceTypeResponse
        """
        return self.list_tags_by_resource_type_with_http_info(request)

    def list_tags_by_resource_type_with_http_info(self, request):
        """查询项目标签

        查询指定项目中实例类型的所有资源标签集合

        :param ListTagsByResourceTypeRequest request
        :return: ListTagsByResourceTypeResponse
        """

        all_params = ['resource_type', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/{resource_type}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTagsByResourceTypeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_app_detail_async(self, request):
        """查询应用模板详情

        查询应用模板详情。

        :param ShowAppDetailRequest request
        :return: ShowAppDetailResponse
        """
        return self.show_app_detail_with_http_info(request)

    def show_app_detail_with_http_info(self, request):
        """查询应用模板详情

        查询应用模板详情。

        :param ShowAppDetailRequest request
        :return: ShowAppDetailResponse
        """

        all_params = ['app_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/apps/{app_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowAppDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_app_version_detail_async(self, request):
        """查询应用模板版本详情

        查询应用模板版本详情

        :param ShowAppVersionDetailRequest request
        :return: ShowAppVersionDetailResponse
        """
        return self.show_app_version_detail_with_http_info(request)

    def show_app_version_detail_with_http_info(self, request):
        """查询应用模板版本详情

        查询应用模板版本详情

        :param ShowAppVersionDetailRequest request
        :return: ShowAppVersionDetailResponse
        """

        all_params = ['app_id', 'version_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/apps/{app_id}/versions/{version_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowAppVersionDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_config_map_async(self, request):
        """查询配置项详情

        查询一个配置项详情

        :param ShowConfigMapRequest request
        :return: ShowConfigMapResponse
        """
        return self.show_config_map_with_http_info(request)

    def show_config_map_with_http_info(self, request):
        """查询配置项详情

        查询一个配置项详情

        :param ShowConfigMapRequest request
        :return: ShowConfigMapResponse
        """

        all_params = ['configmap_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'configmap_id' in local_var_params:
            path_params['configmap_id'] = local_var_params['configmap_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/configmaps/{configmap_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowConfigMapResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_deployment_async(self, request):
        """查询应用部署

        查询应用部署

        :param ShowDeploymentRequest request
        :return: ShowDeploymentResponse
        """
        return self.show_deployment_with_http_info(request)

    def show_deployment_with_http_info(self, request):
        """查询应用部署

        查询应用部署

        :param ShowDeploymentRequest request
        :return: ShowDeploymentResponse
        """

        all_params = ['deployment_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/edgemgr/deployments/{deployment_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDeploymentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_device_async(self, request):
        """查询终端设备详情

        该API用于查询终端设备详情。

        :param ShowDeviceRequest request
        :return: ShowDeviceResponse
        """
        return self.show_device_with_http_info(request)

    def show_device_with_http_info(self, request):
        """查询终端设备详情

        该API用于查询终端设备详情。

        :param ShowDeviceRequest request
        :return: ShowDeviceResponse
        """

        all_params = ['device_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/devices/{device_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_device_template_async(self, request):
        """查询终端设备模板

        查询一个终端设备模板

        :param ShowDeviceTemplateRequest request
        :return: ShowDeviceTemplateResponse
        """
        return self.show_device_template_with_http_info(request)

    def show_device_template_with_http_info(self, request):
        """查询终端设备模板

        查询一个终端设备模板

        :param ShowDeviceTemplateRequest request
        :return: ShowDeviceTemplateResponse
        """

        all_params = ['device_template_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_template_id' in local_var_params:
            path_params['device_template_id'] = local_var_params['device_template_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/device-templates/{device_template_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDeviceTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_device_twin_async(self, request):
        """查询终端设备孪生

        该API用于查询终端设备孪生。

        :param ShowDeviceTwinRequest request
        :return: ShowDeviceTwinResponse
        """
        return self.show_device_twin_with_http_info(request)

    def show_device_twin_with_http_info(self, request):
        """查询终端设备孪生

        该API用于查询终端设备孪生。

        :param ShowDeviceTwinRequest request
        :return: ShowDeviceTwinResponse
        """

        all_params = ['device_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/devices/{device_id}/twin',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDeviceTwinResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_edge_node_detail_async(self, request):
        """查询边缘节点详情

        该API用于查询边缘节点详情。

        :param ShowEdgeNodeDetailRequest request
        :return: ShowEdgeNodeDetailResponse
        """
        return self.show_edge_node_detail_with_http_info(request)

    def show_edge_node_detail_with_http_info(self, request):
        """查询边缘节点详情

        该API用于查询边缘节点详情。

        :param ShowEdgeNodeDetailRequest request
        :return: ShowEdgeNodeDetailResponse
        """

        all_params = ['node_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/nodes/{node_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowEdgeNodeDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_end_point_detail_async(self, request):
        """查询端点详情

        查询一个端点的详情

        :param ShowEndPointDetailRequest request
        :return: ShowEndPointDetailResponse
        """
        return self.show_end_point_detail_with_http_info(request)

    def show_end_point_detail_with_http_info(self, request):
        """查询端点详情

        查询一个端点的详情

        :param ShowEndPointDetailRequest request
        :return: ShowEndPointDetailResponse
        """

        all_params = ['endpoint_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'endpoint_id' in local_var_params:
            path_params['endpoint_id'] = local_var_params['endpoint_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/routemgr/endpoints/{endpoint_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowEndPointDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_rule_detail_async(self, request):
        """查询规则详情

        获取一条规则的详情

        :param ShowRuleDetailRequest request
        :return: ShowRuleDetailResponse
        """
        return self.show_rule_detail_with_http_info(request)

    def show_rule_detail_with_http_info(self, request):
        """查询规则详情

        获取一条规则的详情

        :param ShowRuleDetailRequest request
        :return: ShowRuleDetailResponse
        """

        all_params = ['rule_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/routemgr/rules/{rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRuleDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_secret_async(self, request):
        """查询密钥详情

        查询一个密钥详情

        :param ShowSecretRequest request
        :return: ShowSecretResponse
        """
        return self.show_secret_with_http_info(request)

    def show_secret_with_http_info(self, request):
        """查询密钥详情

        查询一个密钥详情

        :param ShowSecretRequest request
        :return: ShowSecretResponse
        """

        all_params = ['secret_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'secret_id' in local_var_params:
            path_params['secret_id'] = local_var_params['secret_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/secrets/{secret_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowSecretResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_service_detail_async(self, request):
        """查询服务详情

        查询一个服务的详情

        :param ShowServiceDetailRequest request
        :return: ShowServiceDetailResponse
        """
        return self.show_service_detail_with_http_info(request)

    def show_service_detail_with_http_info(self, request):
        """查询服务详情

        查询一个服务的详情

        :param ShowServiceDetailRequest request
        :return: ShowServiceDetailResponse
        """

        all_params = ['service_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/services/{service_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowServiceDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def start_rule_async(self, request):
        """启用规则

        启用一条规则

        :param StartRuleRequest request
        :return: StartRuleResponse
        """
        return self.start_rule_with_http_info(request)

    def start_rule_with_http_info(self, request):
        """启用规则

        启用一条规则

        :param StartRuleRequest request
        :return: StartRuleResponse
        """

        all_params = ['rule_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/routemgr/rules/{rule_id}/start',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StartRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def stop_rule_async(self, request):
        """停用规则

        停用一条规则

        :param StopRuleRequest request
        :return: StopRuleResponse
        """
        return self.stop_rule_with_http_info(request)

    def stop_rule_with_http_info(self, request):
        """停用规则

        停用一条规则

        :param StopRuleRequest request
        :return: StopRuleResponse
        """

        all_params = ['rule_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/routemgr/rules/{rule_id}/stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StopRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_app_async(self, request):
        """更新应用模板

        更新一个应用模板。

        :param UpdateAppRequest request
        :return: UpdateAppResponse
        """
        return self.update_app_with_http_info(request)

    def update_app_with_http_info(self, request):
        """更新应用模板

        更新一个应用模板。

        :param UpdateAppRequest request
        :return: UpdateAppResponse
        """

        all_params = ['app_id', 'update_app', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/apps/{app_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_app_version_async(self, request):
        """更新应用模板版本

        更新一个应用模板版本

        :param UpdateAppVersionRequest request
        :return: UpdateAppVersionResponse
        """
        return self.update_app_version_with_http_info(request)

    def update_app_version_with_http_info(self, request):
        """更新应用模板版本

        更新一个应用模板版本

        :param UpdateAppVersionRequest request
        :return: UpdateAppVersionResponse
        """

        all_params = ['app_id', 'version_id', 'version', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/apps/{app_id}/versions/{version_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateAppVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_config_map_async(self, request):
        """更新配置项

        更新一个配置项

        :param UpdateConfigMapRequest request
        :return: UpdateConfigMapResponse
        """
        return self.update_config_map_with_http_info(request)

    def update_config_map_with_http_info(self, request):
        """更新配置项

        更新一个配置项

        :param UpdateConfigMapRequest request
        :return: UpdateConfigMapResponse
        """

        all_params = ['configmap_id', 'update_config_map', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'configmap_id' in local_var_params:
            path_params['configmap_id'] = local_var_params['configmap_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/configmaps/{configmap_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateConfigMapResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_deployment_async(self, request):
        """更新应用部署

        修改应用部署

        :param UpdateDeploymentRequest request
        :return: UpdateDeploymentResponse
        """
        return self.update_deployment_with_http_info(request)

    def update_deployment_with_http_info(self, request):
        """更新应用部署

        修改应用部署

        :param UpdateDeploymentRequest request
        :return: UpdateDeploymentResponse
        """

        all_params = ['deployment_id', 'update_deployment', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/edgemgr/deployments/{deployment_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateDeploymentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_device_async(self, request):
        """更新终端设备

        更新一个终端设备。

        :param UpdateDeviceRequest request
        :return: UpdateDeviceResponse
        """
        return self.update_device_with_http_info(request)

    def update_device_with_http_info(self, request):
        """更新终端设备

        更新一个终端设备。

        :param UpdateDeviceRequest request
        :return: UpdateDeviceResponse
        """

        all_params = ['device_id', 'device', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/devices/{device_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_device_template_by_id_async(self, request):
        """更新终端设备模板

        更新一个终端设备模板。

        :param UpdateDeviceTemplateByIdRequest request
        :return: UpdateDeviceTemplateByIdResponse
        """
        return self.update_device_template_by_id_with_http_info(request)

    def update_device_template_by_id_with_http_info(self, request):
        """更新终端设备模板

        更新一个终端设备模板。

        :param UpdateDeviceTemplateByIdRequest request
        :return: UpdateDeviceTemplateByIdResponse
        """

        all_params = ['device_template_id', 'device_template', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_template_id' in local_var_params:
            path_params['device_template_id'] = local_var_params['device_template_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/device-templates/{device_template_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateDeviceTemplateByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_device_twin_async(self, request):
        """更新终端设备孪生

        该API用于更新终端设备孪生。

        :param UpdateDeviceTwinRequest request
        :return: UpdateDeviceTwinResponse
        """
        return self.update_device_twin_with_http_info(request)

    def update_device_twin_with_http_info(self, request):
        """更新终端设备孪生

        该API用于更新终端设备孪生。

        :param UpdateDeviceTwinRequest request
        :return: UpdateDeviceTwinResponse
        """

        all_params = ['device_id', 'ief_instance_id', 'update_device_twin']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/devices/{device_id}/twin',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateDeviceTwinResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_edge_node_async(self, request):
        """更新边缘节点

        该API用于更新边缘节点。

        :param UpdateEdgeNodeRequest request
        :return: UpdateEdgeNodeResponse
        """
        return self.update_edge_node_with_http_info(request)

    def update_edge_node_with_http_info(self, request):
        """更新边缘节点

        该API用于更新边缘节点。

        :param UpdateEdgeNodeRequest request
        :return: UpdateEdgeNodeResponse
        """

        all_params = ['node_id', 'ief_instance_id', 'node']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/nodes/{node_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateEdgeNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_edge_node_device_async(self, request):
        """更新边缘节点的终端设备

        添加或删除边缘节点的终端设备

        :param UpdateEdgeNodeDeviceRequest request
        :return: UpdateEdgeNodeDeviceResponse
        """
        return self.update_edge_node_device_with_http_info(request)

    def update_edge_node_device_with_http_info(self, request):
        """更新边缘节点的终端设备

        添加或删除边缘节点的终端设备

        :param UpdateEdgeNodeDeviceRequest request
        :return: UpdateEdgeNodeDeviceResponse
        """

        all_params = ['node_id', 'devices', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/nodes/{node_id}/devices',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateEdgeNodeDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_node_by_device_id_async(self, request):
        """更新终端设备的边缘节点

        该API用于更新终端设备的边缘节点。功能与更新边缘节点的终端设备相同，推荐使用更新边缘节点的终端设备。

        :param UpdateNodeByDeviceIdRequest request
        :return: UpdateNodeByDeviceIdResponse
        """
        return self.update_node_by_device_id_with_http_info(request)

    def update_node_by_device_id_with_http_info(self, request):
        """更新终端设备的边缘节点

        该API用于更新终端设备的边缘节点。功能与更新边缘节点的终端设备相同，推荐使用更新边缘节点的终端设备。

        :param UpdateNodeByDeviceIdRequest request
        :return: UpdateNodeByDeviceIdResponse
        """

        all_params = ['device_id', 'node']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/devices/{device_id}/nodes',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateNodeByDeviceIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_secret_async(self, request):
        """更新密钥

        更新一个密钥

        :param UpdateSecretRequest request
        :return: UpdateSecretResponse
        """
        return self.update_secret_with_http_info(request)

    def update_secret_with_http_info(self, request):
        """更新密钥

        更新一个密钥

        :param UpdateSecretRequest request
        :return: UpdateSecretResponse
        """

        all_params = ['secret_id', 'update_secret', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'secret_id' in local_var_params:
            path_params['secret_id'] = local_var_params['secret_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/secrets/{secret_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateSecretResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_service_async(self, request):
        """更新服务

        更新一个服务

        :param UpdateServiceRequest request
        :return: UpdateServiceResponse
        """
        return self.update_service_with_http_info(request)

    def update_service_with_http_info(self, request):
        """更新服务

        更新一个服务

        :param UpdateServiceRequest request
        :return: UpdateServiceResponse
        """

        all_params = ['service_id', 'ief_instance_id', 'service']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/services/{service_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateServiceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response_type: Response data type.
        :param response_headers: Header should be added to response data.
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param request_type: Request data type.
        :return:
            Return the response directly.
        """
        return self.do_http_request(
            method=method,
            resource_path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
            post_params=post_params,
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type,
	    async_request=True)
