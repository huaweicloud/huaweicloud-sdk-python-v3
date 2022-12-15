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

        为指定实例批量添加或删除标签。
        一个资源上最多有20个标签。
        
        说明：
        - 此接口为幂等接口，创建时如果请求体中存在重复key则报错。
        - 创建时不允许设置重复key数据,如果数据库已存在该key，就覆盖value的值。
        - 删除时不对标签字符集范围做校验，如果删除的标签不存在，默认处理成功。删除时tags结构体不能缺失，key不能为空，或者空字符串。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAddDeleteTags
        :type request: :class:`huaweicloudsdkief.v1.BatchAddDeleteTagsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.BatchAddDeleteTagsResponse`
        """
        return self.batch_add_delete_tags_with_http_info(request)

    def batch_add_delete_tags_with_http_info(self, request):
        all_params = ['resource_type', 'resource_id', 'ief_instance_id', 'tags']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='BatchAddDeleteTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_app_async(self, request):
        """创建应用模板

        该API用于创建一个应用模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateApp
        :type request: :class:`huaweicloudsdkief.v1.CreateAppRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateAppResponse`
        """
        return self.create_app_with_http_info(request)

    def create_app_with_http_info(self, request):
        all_params = ['app', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='CreateAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_app_versions_async(self, request):
        """创建应用模板版本

        创建一个应用模板版本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAppVersions
        :type request: :class:`huaweicloudsdkief.v1.CreateAppVersionsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateAppVersionsResponse`
        """
        return self.create_app_versions_with_http_info(request)

    def create_app_versions_with_http_info(self, request):
        all_params = ['app_id', 'version', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='CreateAppVersionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_batch_job_async(self, request):
        """创建批量处理任务

        创建批量处理作业。该API用于创建批量处理作业，当前支持：批量节点升级、批量应用部署、批量应用升级
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateBatchJob
        :type request: :class:`huaweicloudsdkief.v1.CreateBatchJobRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateBatchJobResponse`
        """
        return self.create_batch_job_with_http_info(request)

    def create_batch_job_with_http_info(self, request):
        all_params = ['ief_instance_id', 'create_batch_job_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v2/{project_id}/productmgr/jobs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateBatchJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_config_map_async(self, request):
        """创建配置项

        创建配置项
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateConfigMap
        :type request: :class:`huaweicloudsdkief.v1.CreateConfigMapRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateConfigMapResponse`
        """
        return self.create_config_map_with_http_info(request)

    def create_config_map_with_http_info(self, request):
        all_params = ['create_config_map', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='CreateConfigMapResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_deployments_async(self, request):
        """创建部署

        创建部署
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDeployments
        :type request: :class:`huaweicloudsdkief.v1.CreateDeploymentsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateDeploymentsResponse`
        """
        return self.create_deployments_with_http_info(request)

    def create_deployments_with_http_info(self, request):
        all_params = ['create_deployments', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='CreateDeploymentsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_device_async(self, request):
        """注册终端设备

        注册终端设备。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDevice
        :type request: :class:`huaweicloudsdkief.v1.CreateDeviceRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateDeviceResponse`
        """
        return self.create_device_with_http_info(request)

    def create_device_with_http_info(self, request):
        all_params = ['create_device', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='CreateDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_device_template_async(self, request):
        """创建终端设备模板

        创建一个终端设备模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDeviceTemplate
        :type request: :class:`huaweicloudsdkief.v1.CreateDeviceTemplateRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateDeviceTemplateResponse`
        """
        return self.create_device_template_with_http_info(request)

    def create_device_template_with_http_info(self, request):
        all_params = ['device_template', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='CreateDeviceTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_edge_group_async(self, request):
        """边缘节点组管理

        创建边缘节点组。该API只能在铂金版实例中使用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEdgeGroup
        :type request: :class:`huaweicloudsdkief.v1.CreateEdgeGroupRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateEdgeGroupResponse`
        """
        return self.create_edge_group_with_http_info(request)

    def create_edge_group_with_http_info(self, request):
        all_params = ['ief_instance_id', 'create_edge_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v2/{project_id}/edgemgr/groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateEdgeGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_edge_group_cert_async(self, request):
        """创建边缘节点组证书

        创建边缘节点组证书。边缘节点组证书.tar.gz文件仅在调用该API时提供压缩包下载，请及时下载证书文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEdgeGroupCert
        :type request: :class:`huaweicloudsdkief.v1.CreateEdgeGroupCertRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateEdgeGroupCertResponse`
        """
        return self.create_edge_group_cert_with_http_info(request)

    def create_edge_group_cert_with_http_info(self, request):
        all_params = ['group_id', 'ief_instance_id', 'create_edge_group_cert_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            resource_path='/v2/{project_id}/edgemgr/groups/{group_id}/certs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateEdgeGroupCertResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_edge_node_async(self, request):
        """注册边缘节点

        该API用于注册一个边缘节点。接口调用成功后，您可以将响应消息体中node.package字段使用base64解码成tar.gz文件，并在控制台下载边缘核心软件，然后纳管边缘节点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEdgeNode
        :type request: :class:`huaweicloudsdkief.v1.CreateEdgeNodeRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateEdgeNodeResponse`
        """
        return self.create_edge_node_with_http_info(request)

    def create_edge_node_with_http_info(self, request):
        all_params = ['create_edge_node_request_body', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='CreateEdgeNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_edge_node_certs_async(self, request):
        """创建节点证书

        创建边缘节点上的应用证书和设备证书。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEdgeNodeCerts
        :type request: :class:`huaweicloudsdkief.v1.CreateEdgeNodeCertsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateEdgeNodeCertsResponse`
        """
        return self.create_edge_node_certs_with_http_info(request)

    def create_edge_node_certs_with_http_info(self, request):
        all_params = ['node_id', 'create_edge_node_certs', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='CreateEdgeNodeCertsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_encryptdatas_async(self, request):
        """新增加密数据

        新增加密数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEncryptdatas
        :type request: :class:`huaweicloudsdkief.v1.CreateEncryptdatasRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateEncryptdatasResponse`
        """
        return self.create_encryptdatas_with_http_info(request)

    def create_encryptdatas_with_http_info(self, request):
        all_params = ['create_encryptdatas_request_body', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v2/{project_id}/edm/encryptdatas',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateEncryptdatasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_endpoint_async(self, request):
        """创建端点

        创建一个端点
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEndpoint
        :type request: :class:`huaweicloudsdkief.v1.CreateEndpointRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateEndpointResponse`
        """
        return self.create_endpoint_with_http_info(request)

    def create_endpoint_with_http_info(self, request):
        all_params = ['create_endpoint', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='CreateEndpointResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_node_encryptdatas_async(self, request):
        """加密数据绑定边缘节点

        加密数据绑定边缘节点
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateNodeEncryptdatas
        :type request: :class:`huaweicloudsdkief.v1.CreateNodeEncryptdatasRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateNodeEncryptdatasResponse`
        """
        return self.create_node_encryptdatas_with_http_info(request)

    def create_node_encryptdatas_with_http_info(self, request):
        all_params = ['node_id', 'create_node_encryptdatas_request_body', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v2/{project_id}/edm/nodes/{node_id}/encryptdatas',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateNodeEncryptdatasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_product_async(self, request):
        """创建批量节点注册作业

        创建批量节点注册作业。接口调用成功后，您可以将响应消息体中product.package字段使用base64解码成tar.gz产品证书文件，并在控制台下载边缘注册软件edge-register和edge-installer，使用该产品证书批量纳管边缘节点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateProduct
        :type request: :class:`huaweicloudsdkief.v1.CreateProductRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateProductResponse`
        """
        return self.create_product_with_http_info(request)

    def create_product_with_http_info(self, request):
        all_params = ['ief_instance_id', 'create_product_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v2/{project_id}/productmgr/products',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateProductResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_rule_async(self, request):
        """创建规则

        创建一条规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRule
        :type request: :class:`huaweicloudsdkief.v1.CreateRuleRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateRuleResponse`
        """
        return self.create_rule_with_http_info(request)

    def create_rule_with_http_info(self, request):
        all_params = ['create_rule', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='CreateRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_secret_async(self, request):
        """创建密钥

        创建密钥
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSecret
        :type request: :class:`huaweicloudsdkief.v1.CreateSecretRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateSecretResponse`
        """
        return self.create_secret_with_http_info(request)

    def create_secret_with_http_info(self, request):
        all_params = ['create_secret', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='CreateSecretResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_service_async(self, request):
        """创建服务

        创建一个服务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateService
        :type request: :class:`huaweicloudsdkief.v1.CreateServiceRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateServiceResponse`
        """
        return self.create_service_with_http_info(request)

    def create_service_with_http_info(self, request):
        all_params = ['ief_instance_id', 'create_service']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='CreateServiceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_system_event_async(self, request):
        """创建系统订阅

        创建系统订阅
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSystemEvent
        :type request: :class:`huaweicloudsdkief.v1.CreateSystemEventRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateSystemEventResponse`
        """
        return self.create_system_event_with_http_info(request)

    def create_system_event_with_http_info(self, request):
        all_params = ['ief_instance_id', 'create_system_event_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v2/{project_id}/routemgr/exchanger/systemevents',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSystemEventResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_tag_async(self, request):
        """添加资源标签

        为资源添加标签。
        一个资源上最多有20个标签。
        此接口为幂等接口，创建时，如果创建的标签已经存在（key相同），则覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTag
        :type request: :class:`huaweicloudsdkief.v1.CreateTagRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateTagResponse`
        """
        return self.create_tag_with_http_info(request)

    def create_tag_with_http_info(self, request):
        all_params = ['resource_id', 'resource_type', 'create_tag_request_body', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='CreateTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_app_async(self, request):
        """删除应用模板

        删除应用模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteApp
        :type request: :class:`huaweicloudsdkief.v1.DeleteAppRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteAppResponse`
        """
        return self.delete_app_with_http_info(request)

    def delete_app_with_http_info(self, request):
        all_params = ['app_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='DeleteAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_app_version_async(self, request):
        """删除应用版本

        删除应用版本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAppVersion
        :type request: :class:`huaweicloudsdkief.v1.DeleteAppVersionRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteAppVersionResponse`
        """
        return self.delete_app_version_with_http_info(request)

    def delete_app_version_with_http_info(self, request):
        all_params = ['app_id', 'version_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='DeleteAppVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_batch_job_async(self, request):
        """删除批量处理作业

        删除批量处理作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBatchJob
        :type request: :class:`huaweicloudsdkief.v1.DeleteBatchJobRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteBatchJobResponse`
        """
        return self.delete_batch_job_with_http_info(request)

    def delete_batch_job_with_http_info(self, request):
        all_params = ['job_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v2/{project_id}/productmgr/jobs/{job_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteBatchJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_config_map_async(self, request):
        """删除配置项

        删除配置项
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteConfigMap
        :type request: :class:`huaweicloudsdkief.v1.DeleteConfigMapRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteConfigMapResponse`
        """
        return self.delete_config_map_with_http_info(request)

    def delete_config_map_with_http_info(self, request):
        all_params = ['configmap_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='DeleteConfigMapResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_deployment_async(self, request):
        """删除部署

        删除应用部署
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDeployment
        :type request: :class:`huaweicloudsdkief.v1.DeleteDeploymentRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteDeploymentResponse`
        """
        return self.delete_deployment_with_http_info(request)

    def delete_deployment_with_http_info(self, request):
        all_params = ['deployment_id', 'ief_instance_id', 'force_delete']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='DeleteDeploymentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_device_async(self, request):
        """删除终端设备

        该API用于删除终端设备。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDevice
        :type request: :class:`huaweicloudsdkief.v1.DeleteDeviceRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteDeviceResponse`
        """
        return self.delete_device_with_http_info(request)

    def delete_device_with_http_info(self, request):
        all_params = ['device_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='DeleteDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_device_template_async(self, request):
        """删除终端设备模板

        删除终端设备模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDeviceTemplate
        :type request: :class:`huaweicloudsdkief.v1.DeleteDeviceTemplateRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteDeviceTemplateResponse`
        """
        return self.delete_device_template_with_http_info(request)

    def delete_device_template_with_http_info(self, request):
        all_params = ['device_template_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='DeleteDeviceTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_edge_group_async(self, request):
        """删除边缘节点组

        删除边缘节点组。该API只能在铂金版实例中使用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEdgeGroup
        :type request: :class:`huaweicloudsdkief.v1.DeleteEdgeGroupRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteEdgeGroupResponse`
        """
        return self.delete_edge_group_with_http_info(request)

    def delete_edge_group_with_http_info(self, request):
        all_params = ['group_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            resource_path='/v2/{project_id}/edgemgr/groups/{group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEdgeGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_edge_group_cert_async(self, request):
        """删除边缘节点组证书

        删除边缘节点组证书
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEdgeGroupCert
        :type request: :class:`huaweicloudsdkief.v1.DeleteEdgeGroupCertRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteEdgeGroupCertResponse`
        """
        return self.delete_edge_group_cert_with_http_info(request)

    def delete_edge_group_cert_with_http_info(self, request):
        all_params = ['group_id', 'group_cert_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'group_cert_id' in local_var_params:
            path_params['group_cert_id'] = local_var_params['group_cert_id']

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
            resource_path='/v2/{project_id}/edgemgr/groups/{group_id}/certs/{group_cert_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEdgeGroupCertResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_edge_node_async(self, request):
        """删除边缘节点

        删除边缘节点
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEdgeNode
        :type request: :class:`huaweicloudsdkief.v1.DeleteEdgeNodeRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteEdgeNodeResponse`
        """
        return self.delete_edge_node_with_http_info(request)

    def delete_edge_node_with_http_info(self, request):
        all_params = ['node_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='DeleteEdgeNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_edge_node_certs_async(self, request):
        """删除节点证书

        删除边缘节点上的证书（目前只支持删除应用证书和设备证书）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEdgeNodeCerts
        :type request: :class:`huaweicloudsdkief.v1.DeleteEdgeNodeCertsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteEdgeNodeCertsResponse`
        """
        return self.delete_edge_node_certs_with_http_info(request)

    def delete_edge_node_certs_with_http_info(self, request):
        all_params = ['node_id', 'cert_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='DeleteEdgeNodeCertsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_encryptdatas_async(self, request):
        """删除加密数据

        删除加密数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEncryptdatas
        :type request: :class:`huaweicloudsdkief.v1.DeleteEncryptdatasRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteEncryptdatasResponse`
        """
        return self.delete_encryptdatas_with_http_info(request)

    def delete_encryptdatas_with_http_info(self, request):
        all_params = ['encryptdata_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'encryptdata_id' in local_var_params:
            path_params['encryptdata_id'] = local_var_params['encryptdata_id']

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
            resource_path='/v2/{project_id}/edm/encryptdatas/{encryptdata_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEncryptdatasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_end_point_async(self, request):
        """删除一个端点

        删除一个端点
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEndPoint
        :type request: :class:`huaweicloudsdkief.v1.DeleteEndPointRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteEndPointResponse`
        """
        return self.delete_end_point_with_http_info(request)

    def delete_end_point_with_http_info(self, request):
        all_params = ['endpoint_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='DeleteEndPointResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_node_encryptdatas_async(self, request):
        """解绑边缘节点的加密数据

        解绑边缘节点的加密数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteNodeEncryptdatas
        :type request: :class:`huaweicloudsdkief.v1.DeleteNodeEncryptdatasRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteNodeEncryptdatasResponse`
        """
        return self.delete_node_encryptdatas_with_http_info(request)

    def delete_node_encryptdatas_with_http_info(self, request):
        all_params = ['node_id', 'encryptdata_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']
        if 'encryptdata_id' in local_var_params:
            path_params['encryptdata_id'] = local_var_params['encryptdata_id']

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
            resource_path='/v2/{project_id}/edm/nodes/{node_id}/encryptdatas/{encryptdata_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteNodeEncryptdatasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_product_async(self, request):
        """删除批量节点注册作业

        删除批量节点注册作业。接口调用成功后，与该批量注册任务关联的批量注册凭证将会失效
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteProduct
        :type request: :class:`huaweicloudsdkief.v1.DeleteProductRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteProductResponse`
        """
        return self.delete_product_with_http_info(request)

    def delete_product_with_http_info(self, request):
        all_params = ['product_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'product_id' in local_var_params:
            path_params['product_id'] = local_var_params['product_id']

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
            resource_path='/v2/{project_id}/productmgr/products/{product_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteProductResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_resource_tag_async(self, request):
        """删除资源标签

        删除资源标签。删除时不对标签字符集做校验，调用前必须要做encodeURI，服务端需要对接口uri做decodeURI。删除的key不存在报404，Key不能为空或者空字符串。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteResourceTag
        :type request: :class:`huaweicloudsdkief.v1.DeleteResourceTagRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteResourceTagResponse`
        """
        return self.delete_resource_tag_with_http_info(request)

    def delete_resource_tag_with_http_info(self, request):
        all_params = ['resource_type', 'resource_id', 'key', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='DeleteResourceTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_rule_async(self, request):
        """删除规则

        删除一条规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRule
        :type request: :class:`huaweicloudsdkief.v1.DeleteRuleRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteRuleResponse`
        """
        return self.delete_rule_with_http_info(request)

    def delete_rule_with_http_info(self, request):
        all_params = ['rule_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='DeleteRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_secret_async(self, request):
        """删除密钥

        删除密钥
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSecret
        :type request: :class:`huaweicloudsdkief.v1.DeleteSecretRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteSecretResponse`
        """
        return self.delete_secret_with_http_info(request)

    def delete_secret_with_http_info(self, request):
        all_params = ['secret_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='DeleteSecretResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_service_async(self, request):
        """删除服务

        删除一个服务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteService
        :type request: :class:`huaweicloudsdkief.v1.DeleteServiceRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteServiceResponse`
        """
        return self.delete_service_with_http_info(request)

    def delete_service_with_http_info(self, request):
        all_params = ['service_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='DeleteServiceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_system_event_async(self, request):
        """删除系统订阅列表

        删除系统订阅列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSystemEvent
        :type request: :class:`huaweicloudsdkief.v1.DeleteSystemEventRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteSystemEventResponse`
        """
        return self.delete_system_event_with_http_info(request)

    def delete_system_event_with_http_info(self, request):
        all_params = ['event_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'event_id' in local_var_params:
            path_params['event_id'] = local_var_params['event_id']

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
            resource_path='/v2/{project_id}/routemgr/exchanger/systemevents/{event_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSystemEventResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def enable_disable_edge_nodes_async(self, request):
        """启用停用边缘节点

        启用停用边缘节点。被停用的边缘节点将无法连接到云端服务，可用该URI启用边缘节点恢复连接。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableDisableEdgeNodes
        :type request: :class:`huaweicloudsdkief.v1.EnableDisableEdgeNodesRequest`
        :rtype: :class:`huaweicloudsdkief.v1.EnableDisableEdgeNodesResponse`
        """
        return self.enable_disable_edge_nodes_with_http_info(request)

    def enable_disable_edge_nodes_with_http_info(self, request):
        all_params = ['node_id', 'enable_disable_edge_nodes_request_body', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='EnableDisableEdgeNodesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_app_versions_async(self, request):
        """查询应用模板版本列表

        查询应用模板版本列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppVersions
        :type request: :class:`huaweicloudsdkief.v1.ListAppVersionsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListAppVersionsResponse`
        """
        return self.list_app_versions_with_http_info(request)

    def list_app_versions_with_http_info(self, request):
        all_params = ['app_id', 'ief_instance_id', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListAppVersionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apps_async(self, request):
        """查询应用模板列表

        查询应用模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApps
        :type request: :class:`huaweicloudsdkief.v1.ListAppsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListAppsResponse`
        """
        return self.list_apps_with_http_info(request)

    def list_apps_with_http_info(self, request):
        all_params = ['ief_instance_id', 'name', 'limit', 'offset', 'alias', 'visibility']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListAppsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_batch_job_async(self, request):
        """查询批量处理作业列表

        查询批量处理作业列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBatchJob
        :type request: :class:`huaweicloudsdkief.v1.ListBatchJobRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListBatchJobResponse`
        """
        return self.list_batch_job_with_http_info(request)

    def list_batch_job_with_http_info(self, request):
        all_params = ['job_type', 'limit', 'offset', 'sort', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_type' in local_var_params:
            query_params.append(('job_type', local_var_params['job_type']))
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
            resource_path='/v2/{project_id}/productmgr/jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBatchJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_config_maps_async(self, request):
        """查询配置项列表

        查询配置项列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConfigMaps
        :type request: :class:`huaweicloudsdkief.v1.ListConfigMapsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListConfigMapsResponse`
        """
        return self.list_config_maps_with_http_info(request)

    def list_config_maps_with_http_info(self, request):
        all_params = ['ief_instance_id', 'name', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListConfigMapsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_deployments_async(self, request):
        """查询部署列表

        查询部署列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDeployments
        :type request: :class:`huaweicloudsdkief.v1.ListDeploymentsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListDeploymentsResponse`
        """
        return self.list_deployments_with_http_info(request)

    def list_deployments_with_http_info(self, request):
        all_params = ['ief_instance_id', 'limit', 'offset', 'sort', 'name', 'node_id', 'group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListDeploymentsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_device_templates_async(self, request):
        """查询终端设备模板列表

        查询终端设备模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDeviceTemplates
        :type request: :class:`huaweicloudsdkief.v1.ListDeviceTemplatesRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListDeviceTemplatesResponse`
        """
        return self.list_device_templates_with_http_info(request)

    def list_device_templates_with_http_info(self, request):
        all_params = ['ief_instance_id', 'name', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListDeviceTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_devices_async(self, request):
        """查询终端设备列表

        该API用于查询终端设备列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDevices
        :type request: :class:`huaweicloudsdkief.v1.ListDevicesRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListDevicesResponse`
        """
        return self.list_devices_with_http_info(request)

    def list_devices_with_http_info(self, request):
        all_params = ['ief_instance_id', 'name', 'node_id', 'limit', 'offset', 'is_binding', 'tags']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListDevicesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_edge_group_certs_async(self, request):
        """查询边缘节点组证书列表

        查询边缘节点组证书列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEdgeGroupCerts
        :type request: :class:`huaweicloudsdkief.v1.ListEdgeGroupCertsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListEdgeGroupCertsResponse`
        """
        return self.list_edge_group_certs_with_http_info(request)

    def list_edge_group_certs_with_http_info(self, request):
        all_params = ['group_id', 'ief_instance_id', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            resource_path='/v2/{project_id}/edgemgr/groups/{group_id}/certs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEdgeGroupCertsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_edge_groups_async(self, request):
        """查询边缘节点组列表

        查询边缘节点组列表。该API只能在铂金版实例中使用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEdgeGroups
        :type request: :class:`huaweicloudsdkief.v1.ListEdgeGroupsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListEdgeGroupsResponse`
        """
        return self.list_edge_groups_with_http_info(request)

    def list_edge_groups_with_http_info(self, request):
        all_params = ['ief_instance_id', 'name', 'limit', 'offset', 'sort']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v2/{project_id}/edgemgr/groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEdgeGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_edge_node_certs_async(self, request):
        """查询节点证书

        查询边缘节点上的应用证书和设备证书。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEdgeNodeCerts
        :type request: :class:`huaweicloudsdkief.v1.ListEdgeNodeCertsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListEdgeNodeCertsResponse`
        """
        return self.list_edge_node_certs_with_http_info(request)

    def list_edge_node_certs_with_http_info(self, request):
        all_params = ['node_id', 'ief_instance_id', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListEdgeNodeCertsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_edge_nodes_async(self, request):
        """查询边缘节点列表

        该API用于查询边缘节点。
        - 如果不携带任何检索参数，将返回该租户的所有边缘节点信息。
        - app_name和tags不支持复合查询，如果同时存在则返回tags查询结果，可以同时携带多个其他检索参数，可同时生效。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEdgeNodes
        :type request: :class:`huaweicloudsdkief.v1.ListEdgeNodesRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListEdgeNodesResponse`
        """
        return self.list_edge_nodes_with_http_info(request)

    def list_edge_nodes_with_http_info(self, request):
        all_params = ['ief_instance_id', 'name', 'limit', 'offset', 'sort', 'device_id', 'device_name', 'app_name', 'state', 'tags']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
        if 'device_id' in local_var_params:
            query_params.append(('device_id', local_var_params['device_id']))
        if 'device_name' in local_var_params:
            query_params.append(('device_name', local_var_params['device_name']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
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
            cname=cname,
            response_type='ListEdgeNodesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_encryptdata_nodes_async(self, request):
        """获取加密数据绑定的边缘节点

        获取加密数据绑定的边缘节点
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEncryptdataNodes
        :type request: :class:`huaweicloudsdkief.v1.ListEncryptdataNodesRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListEncryptdataNodesResponse`
        """
        return self.list_encryptdata_nodes_with_http_info(request)

    def list_encryptdata_nodes_with_http_info(self, request):
        all_params = ['encryptdata_id', 'limit', 'ief_instance_id', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'encryptdata_id' in local_var_params:
            path_params['encryptdata_id'] = local_var_params['encryptdata_id']

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
            resource_path='/v2/{project_id}/edm/encryptdatas/{encryptdata_id}/nodes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEncryptdataNodesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_encryptdatas_async(self, request):
        """获取加密数据列表

        获取加密数据列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEncryptdatas
        :type request: :class:`huaweicloudsdkief.v1.ListEncryptdatasRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListEncryptdatasResponse`
        """
        return self.list_encryptdatas_with_http_info(request)

    def list_encryptdatas_with_http_info(self, request):
        all_params = ['name', 'limit', 'offset', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v2/{project_id}/edm/encryptdatas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEncryptdatasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_endpoints_async(self, request):
        """查询端点列表

        获取所有的端点详情。
        如果不携带任何检索参数，将返回该租户的所有端点信息和系统中所有的共享端点。
        如果同时指定is_shared&#x3D;true和其他参数，同样还会对name、type进行过滤。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEndpoints
        :type request: :class:`huaweicloudsdkief.v1.ListEndpointsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListEndpointsResponse`
        """
        return self.list_endpoints_with_http_info(request)

    def list_endpoints_with_http_info(self, request):
        all_params = ['ief_instance_id', 'name', 'type', 'is_shared', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListEndpointsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_node_encryptdatas_async(self, request):
        """获取边缘节点绑定的加密数据

        获取边缘节点绑定的加密数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNodeEncryptdatas
        :type request: :class:`huaweicloudsdkief.v1.ListNodeEncryptdatasRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListNodeEncryptdatasResponse`
        """
        return self.list_node_encryptdatas_with_http_info(request)

    def list_node_encryptdatas_with_http_info(self, request):
        all_params = ['node_id', 'limit', 'offset', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v2/{project_id}/edm/nodes/{node_id}/encryptdatas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListNodeEncryptdatasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_pods_async(self, request):
        """查询应用实例列表

        查询应用实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPods
        :type request: :class:`huaweicloudsdkief.v1.ListPodsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListPodsResponse`
        """
        return self.list_pods_with_http_info(request)

    def list_pods_with_http_info(self, request):
        all_params = ['node_id', 'group_id', 'deployment_id', 'deployment_ids', 'limit', 'offset', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListPodsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_products_async(self, request):
        """查询批量节点注册作业列表

        查询批量节点注册作业列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProducts
        :type request: :class:`huaweicloudsdkief.v1.ListProductsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListProductsResponse`
        """
        return self.list_products_with_http_info(request)

    def list_products_with_http_info(self, request):
        all_params = ['ief_instance_id', 'limit', 'offset', 'sort']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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
            resource_path='/v2/{project_id}/productmgr/products',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProductsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_resource_by_tags_async(self, request):
        """查询资源实例

        使用标签过滤实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResourceByTags
        :type request: :class:`huaweicloudsdkief.v1.ListResourceByTagsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListResourceByTagsResponse`
        """
        return self.list_resource_by_tags_with_http_info(request)

    def list_resource_by_tags_with_http_info(self, request):
        all_params = ['resource_type', 'list_resource_by_tags', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListResourceByTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_rule_errors_async(self, request):
        """查询规则错误列表

        查询特定规则下的所有错误列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRuleErrors
        :type request: :class:`huaweicloudsdkief.v1.ListRuleErrorsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListRuleErrorsResponse`
        """
        return self.list_rule_errors_with_http_info(request)

    def list_rule_errors_with_http_info(self, request):
        all_params = ['rule_id', 'ief_instance_id', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListRuleErrorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_rules_async(self, request):
        """查询规则列表

        查询到所有的规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRules
        :type request: :class:`huaweicloudsdkief.v1.ListRulesRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListRulesResponse`
        """
        return self.list_rules_with_http_info(request)

    def list_rules_with_http_info(self, request):
        all_params = ['ief_instance_id', 'name', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_secrets_async(self, request):
        """查询密钥列表

        查询密钥列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSecrets
        :type request: :class:`huaweicloudsdkief.v1.ListSecretsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListSecretsResponse`
        """
        return self.list_secrets_with_http_info(request)

    def list_secrets_with_http_info(self, request):
        all_params = ['ief_instance_id', 'name', 'limit', 'offset', 'sort']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListSecretsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_services_async(self, request):
        """查询服务列表

        获取所有的服务详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServices
        :type request: :class:`huaweicloudsdkief.v1.ListServicesRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListServicesResponse`
        """
        return self.list_services_with_http_info(request)

    def list_services_with_http_info(self, request):
        all_params = ['ief_instance_id', 'limit', 'offset', 'sorted', 'name', 'app']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListServicesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_system_events_async(self, request):
        """查询系统订阅列表

        查询系统订阅列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSystemEvents
        :type request: :class:`huaweicloudsdkief.v1.ListSystemEventsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListSystemEventsResponse`
        """
        return self.list_system_events_with_http_info(request)

    def list_system_events_with_http_info(self, request):
        all_params = ['ief_instance_id', 'name', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v2/{project_id}/routemgr/exchanger/systemevents',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSystemEventsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_tags_async(self, request):
        """查询资源标签

        查询指定实例的标签信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTags
        :type request: :class:`huaweicloudsdkief.v1.ListTagsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListTagsResponse`
        """
        return self.list_tags_with_http_info(request)

    def list_tags_with_http_info(self, request):
        all_params = ['resource_id', 'resource_type', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_tags_by_resource_type_async(self, request):
        """查询项目标签

        查询指定项目中实例类型的所有资源标签集合
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTagsByResourceType
        :type request: :class:`huaweicloudsdkief.v1.ListTagsByResourceTypeRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListTagsByResourceTypeResponse`
        """
        return self.list_tags_by_resource_type_with_http_info(request)

    def list_tags_by_resource_type_with_http_info(self, request):
        all_params = ['resource_type', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListTagsByResourceTypeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restart_deployments_pod_async(self, request):
        """容器应用实例重启

        重启部署下的应用实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestartDeploymentsPod
        :type request: :class:`huaweicloudsdkief.v1.RestartDeploymentsPodRequest`
        :rtype: :class:`huaweicloudsdkief.v1.RestartDeploymentsPodResponse`
        """
        return self.restart_deployments_pod_with_http_info(request)

    def restart_deployments_pod_with_http_info(self, request):
        all_params = ['deployment_id', 'pod_name', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']
        if 'pod_name' in local_var_params:
            path_params['pod_name'] = local_var_params['pod_name']

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
            resource_path='/v3/{project_id}/edgemgr/deployments/{deployment_id}/pods/{pod_name}/restart',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RestartDeploymentsPodResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restore_batch_job_async(self, request):
        """继续批量处理作业

        继续执行批量处理作业。该API只对停止的批量处理作业生效
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestoreBatchJob
        :type request: :class:`huaweicloudsdkief.v1.RestoreBatchJobRequest`
        :rtype: :class:`huaweicloudsdkief.v1.RestoreBatchJobResponse`
        """
        return self.restore_batch_job_with_http_info(request)

    def restore_batch_job_with_http_info(self, request):
        all_params = ['job_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v2/{project_id}/productmgr/jobs/{job_id}/restore',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RestoreBatchJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def retry_batch_job_async(self, request):
        """重试批量处理作业

        重试批量处理作业。该API仅对执行状态失败的批量处理作业生效
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RetryBatchJob
        :type request: :class:`huaweicloudsdkief.v1.RetryBatchJobRequest`
        :rtype: :class:`huaweicloudsdkief.v1.RetryBatchJobResponse`
        """
        return self.retry_batch_job_with_http_info(request)

    def retry_batch_job_with_http_info(self, request):
        all_params = ['job_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v2/{project_id}/productmgr/jobs/{job_id}/retry',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RetryBatchJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_app_detail_async(self, request):
        """查询应用模板详情

        查询应用模板详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAppDetail
        :type request: :class:`huaweicloudsdkief.v1.ShowAppDetailRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowAppDetailResponse`
        """
        return self.show_app_detail_with_http_info(request)

    def show_app_detail_with_http_info(self, request):
        all_params = ['app_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowAppDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_app_version_detail_async(self, request):
        """查询应用模板版本详情

        查询应用模板版本详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAppVersionDetail
        :type request: :class:`huaweicloudsdkief.v1.ShowAppVersionDetailRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowAppVersionDetailResponse`
        """
        return self.show_app_version_detail_with_http_info(request)

    def show_app_version_detail_with_http_info(self, request):
        all_params = ['app_id', 'version_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowAppVersionDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_batch_job_async(self, request):
        """查询批量处理作业详情

        查询批量处理作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBatchJob
        :type request: :class:`huaweicloudsdkief.v1.ShowBatchJobRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowBatchJobResponse`
        """
        return self.show_batch_job_with_http_info(request)

    def show_batch_job_with_http_info(self, request):
        all_params = ['job_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v2/{project_id}/productmgr/jobs/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowBatchJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_config_map_async(self, request):
        """查询配置项详情

        查询一个配置项详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowConfigMap
        :type request: :class:`huaweicloudsdkief.v1.ShowConfigMapRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowConfigMapResponse`
        """
        return self.show_config_map_with_http_info(request)

    def show_config_map_with_http_info(self, request):
        all_params = ['configmap_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowConfigMapResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_deployment_async(self, request):
        """查询应用部署

        查询应用部署
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDeployment
        :type request: :class:`huaweicloudsdkief.v1.ShowDeploymentRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowDeploymentResponse`
        """
        return self.show_deployment_with_http_info(request)

    def show_deployment_with_http_info(self, request):
        all_params = ['deployment_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowDeploymentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_device_async(self, request):
        """查询终端设备详情

        该API用于查询终端设备详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDevice
        :type request: :class:`huaweicloudsdkief.v1.ShowDeviceRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowDeviceResponse`
        """
        return self.show_device_with_http_info(request)

    def show_device_with_http_info(self, request):
        all_params = ['device_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_device_template_async(self, request):
        """查询终端设备模板

        查询一个终端设备模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDeviceTemplate
        :type request: :class:`huaweicloudsdkief.v1.ShowDeviceTemplateRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowDeviceTemplateResponse`
        """
        return self.show_device_template_with_http_info(request)

    def show_device_template_with_http_info(self, request):
        all_params = ['device_template_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowDeviceTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_device_twin_async(self, request):
        """查询终端设备孪生

        该API用于查询终端设备孪生。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDeviceTwin
        :type request: :class:`huaweicloudsdkief.v1.ShowDeviceTwinRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowDeviceTwinResponse`
        """
        return self.show_device_twin_with_http_info(request)

    def show_device_twin_with_http_info(self, request):
        all_params = ['device_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowDeviceTwinResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_edge_group_cert_detail_async(self, request):
        """查询边缘节点组证书详情

        查询边缘节点组证书详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEdgeGroupCertDetail
        :type request: :class:`huaweicloudsdkief.v1.ShowEdgeGroupCertDetailRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowEdgeGroupCertDetailResponse`
        """
        return self.show_edge_group_cert_detail_with_http_info(request)

    def show_edge_group_cert_detail_with_http_info(self, request):
        all_params = ['group_id', 'group_cert_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'group_cert_id' in local_var_params:
            path_params['group_cert_id'] = local_var_params['group_cert_id']

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
            resource_path='/v2/{project_id}/edgemgr/groups/{group_id}/certs/{group_cert_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEdgeGroupCertDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_edge_group_detail_async(self, request):
        """查询边缘节点组详情

        查询边缘节点组详情。该API只能在铂金版实例中使用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEdgeGroupDetail
        :type request: :class:`huaweicloudsdkief.v1.ShowEdgeGroupDetailRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowEdgeGroupDetailResponse`
        """
        return self.show_edge_group_detail_with_http_info(request)

    def show_edge_group_detail_with_http_info(self, request):
        all_params = ['group_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            resource_path='/v2/{project_id}/edgemgr/groups/{group_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEdgeGroupDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_edge_node_detail_async(self, request):
        """查询边缘节点详情

        查询边缘节点详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEdgeNodeDetail
        :type request: :class:`huaweicloudsdkief.v1.ShowEdgeNodeDetailRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowEdgeNodeDetailResponse`
        """
        return self.show_edge_node_detail_with_http_info(request)

    def show_edge_node_detail_with_http_info(self, request):
        all_params = ['node_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowEdgeNodeDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_encryptdatas_async(self, request):
        """查询加密数据详情

        查询加密数据详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEncryptdatas
        :type request: :class:`huaweicloudsdkief.v1.ShowEncryptdatasRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowEncryptdatasResponse`
        """
        return self.show_encryptdatas_with_http_info(request)

    def show_encryptdatas_with_http_info(self, request):
        all_params = ['encryptdata_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'encryptdata_id' in local_var_params:
            path_params['encryptdata_id'] = local_var_params['encryptdata_id']

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
            resource_path='/v2/{project_id}/edm/encryptdatas/{encryptdata_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEncryptdatasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_end_point_detail_async(self, request):
        """查询端点详情

        查询一个端点的详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEndPointDetail
        :type request: :class:`huaweicloudsdkief.v1.ShowEndPointDetailRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowEndPointDetailResponse`
        """
        return self.show_end_point_detail_with_http_info(request)

    def show_end_point_detail_with_http_info(self, request):
        all_params = ['endpoint_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowEndPointDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_product_detail_async(self, request):
        """查询批量节点注册作业详情

        查询批量节点注册作业详情。该接口无法查询产品证书文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProductDetail
        :type request: :class:`huaweicloudsdkief.v1.ShowProductDetailRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowProductDetailResponse`
        """
        return self.show_product_detail_with_http_info(request)

    def show_product_detail_with_http_info(self, request):
        all_params = ['product_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'product_id' in local_var_params:
            path_params['product_id'] = local_var_params['product_id']

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
            resource_path='/v2/{project_id}/productmgr/products/{product_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowProductDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_quota_async(self, request):
        """查询IEF服务下的资源配额

        查询IEF服务下的资源配额
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowQuota
        :type request: :class:`huaweicloudsdkief.v1.ShowQuotaRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowQuotaResponse`
        """
        return self.show_quota_with_http_info(request)

    def show_quota_with_http_info(self, request):
        all_params = ['types']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'types' in local_var_params:
            query_params.append(('types', local_var_params['types']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edgemgr/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_rule_detail_async(self, request):
        """查询规则详情

        获取一条规则的详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRuleDetail
        :type request: :class:`huaweicloudsdkief.v1.ShowRuleDetailRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowRuleDetailResponse`
        """
        return self.show_rule_detail_with_http_info(request)

    def show_rule_detail_with_http_info(self, request):
        all_params = ['rule_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowRuleDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_secret_async(self, request):
        """查询密钥详情

        查询一个密钥详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSecret
        :type request: :class:`huaweicloudsdkief.v1.ShowSecretRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowSecretResponse`
        """
        return self.show_secret_with_http_info(request)

    def show_secret_with_http_info(self, request):
        all_params = ['secret_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowSecretResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_service_detail_async(self, request):
        """查询服务详情

        查询一个服务的详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServiceDetail
        :type request: :class:`huaweicloudsdkief.v1.ShowServiceDetailRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowServiceDetailResponse`
        """
        return self.show_service_detail_with_http_info(request)

    def show_service_detail_with_http_info(self, request):
        all_params = ['service_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowServiceDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_system_event_detail_async(self, request):
        """查询系统订阅列表

        查询系统订阅列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSystemEventDetail
        :type request: :class:`huaweicloudsdkief.v1.ShowSystemEventDetailRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowSystemEventDetailResponse`
        """
        return self.show_system_event_detail_with_http_info(request)

    def show_system_event_detail_with_http_info(self, request):
        all_params = ['event_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'event_id' in local_var_params:
            path_params['event_id'] = local_var_params['event_id']

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
            resource_path='/v2/{project_id}/routemgr/exchanger/systemevents/{event_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSystemEventDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_rule_async(self, request):
        """启用规则

        启用一条规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartRule
        :type request: :class:`huaweicloudsdkief.v1.StartRuleRequest`
        :rtype: :class:`huaweicloudsdkief.v1.StartRuleResponse`
        """
        return self.start_rule_with_http_info(request)

    def start_rule_with_http_info(self, request):
        all_params = ['rule_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='StartRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_system_event_async(self, request):
        """启用系统订阅

        启用系统订阅
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartSystemEvent
        :type request: :class:`huaweicloudsdkief.v1.StartSystemEventRequest`
        :rtype: :class:`huaweicloudsdkief.v1.StartSystemEventResponse`
        """
        return self.start_system_event_with_http_info(request)

    def start_system_event_with_http_info(self, request):
        all_params = ['event_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'event_id' in local_var_params:
            path_params['event_id'] = local_var_params['event_id']

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
            resource_path='/v2/{project_id}/routemgr/exchanger/systemevents/{event_id}/start',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StartSystemEventResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_batch_job_async(self, request):
        """停止批量处理作业

        停止批量处理作业。该API仅对运行中的批量处理作业生效
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopBatchJob
        :type request: :class:`huaweicloudsdkief.v1.StopBatchJobRequest`
        :rtype: :class:`huaweicloudsdkief.v1.StopBatchJobResponse`
        """
        return self.stop_batch_job_with_http_info(request)

    def stop_batch_job_with_http_info(self, request):
        all_params = ['job_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v2/{project_id}/productmgr/jobs/{job_id}/pause',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopBatchJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_rule_async(self, request):
        """停用规则

        停用一条规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopRule
        :type request: :class:`huaweicloudsdkief.v1.StopRuleRequest`
        :rtype: :class:`huaweicloudsdkief.v1.StopRuleResponse`
        """
        return self.stop_rule_with_http_info(request)

    def stop_rule_with_http_info(self, request):
        all_params = ['rule_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='StopRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_system_event_async(self, request):
        """停用系统订阅

        停用系统订阅
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopSystemEvent
        :type request: :class:`huaweicloudsdkief.v1.StopSystemEventRequest`
        :rtype: :class:`huaweicloudsdkief.v1.StopSystemEventResponse`
        """
        return self.stop_system_event_with_http_info(request)

    def stop_system_event_with_http_info(self, request):
        all_params = ['event_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'event_id' in local_var_params:
            path_params['event_id'] = local_var_params['event_id']

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
            resource_path='/v2/{project_id}/routemgr/exchanger/systemevents/{event_id}/stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopSystemEventResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_app_async(self, request):
        """更新应用模板

        更新一个应用模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateApp
        :type request: :class:`huaweicloudsdkief.v1.UpdateAppRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateAppResponse`
        """
        return self.update_app_with_http_info(request)

    def update_app_with_http_info(self, request):
        all_params = ['app_id', 'update_app_body', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='UpdateAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_app_version_async(self, request):
        """更新应用模板版本

        更新一个应用模板版本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAppVersion
        :type request: :class:`huaweicloudsdkief.v1.UpdateAppVersionRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateAppVersionResponse`
        """
        return self.update_app_version_with_http_info(request)

    def update_app_version_with_http_info(self, request):
        all_params = ['app_id', 'version_id', 'updata_app_version_body', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='UpdateAppVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_config_map_async(self, request):
        """更新配置项

        更新一个配置项
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateConfigMap
        :type request: :class:`huaweicloudsdkief.v1.UpdateConfigMapRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateConfigMapResponse`
        """
        return self.update_config_map_with_http_info(request)

    def update_config_map_with_http_info(self, request):
        all_params = ['configmap_id', 'update_config_map', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='UpdateConfigMapResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_deployment_async(self, request):
        """更新应用部署

        修改应用部署
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDeployment
        :type request: :class:`huaweicloudsdkief.v1.UpdateDeploymentRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateDeploymentResponse`
        """
        return self.update_deployment_with_http_info(request)

    def update_deployment_with_http_info(self, request):
        all_params = ['deployment_id', 'update_deployment', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='UpdateDeploymentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_device_async(self, request):
        """更新终端设备

        更新一个终端设备。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDevice
        :type request: :class:`huaweicloudsdkief.v1.UpdateDeviceRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateDeviceResponse`
        """
        return self.update_device_with_http_info(request)

    def update_device_with_http_info(self, request):
        all_params = ['device_id', 'device', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='UpdateDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_device_template_by_id_async(self, request):
        """更新终端设备模板

        更新一个终端设备模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDeviceTemplateById
        :type request: :class:`huaweicloudsdkief.v1.UpdateDeviceTemplateByIdRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateDeviceTemplateByIdResponse`
        """
        return self.update_device_template_by_id_with_http_info(request)

    def update_device_template_by_id_with_http_info(self, request):
        all_params = ['device_template_id', 'device_template', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='UpdateDeviceTemplateByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_device_twin_async(self, request):
        """更新终端设备孪生

        该API用于更新终端设备孪生。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDeviceTwin
        :type request: :class:`huaweicloudsdkief.v1.UpdateDeviceTwinRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateDeviceTwinResponse`
        """
        return self.update_device_twin_with_http_info(request)

    def update_device_twin_with_http_info(self, request):
        all_params = ['device_id', 'ief_instance_id', 'update_device_twin']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='UpdateDeviceTwinResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_edge_group_async(self, request):
        """更新边缘节点组

        更新边缘节点组描述。该API只能在铂金版实例中使用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEdgeGroup
        :type request: :class:`huaweicloudsdkief.v1.UpdateEdgeGroupRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateEdgeGroupResponse`
        """
        return self.update_edge_group_with_http_info(request)

    def update_edge_group_with_http_info(self, request):
        all_params = ['group_id', 'ief_instance_id', 'update_edge_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            resource_path='/v2/{project_id}/edgemgr/groups/{group_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEdgeGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_edge_group_node_binding_async(self, request):
        """绑定或解绑边缘节点

        边缘节点组绑定或解绑边缘节点。该API只能在铂金版实例中使用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEdgeGroupNodeBinding
        :type request: :class:`huaweicloudsdkief.v1.UpdateEdgeGroupNodeBindingRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateEdgeGroupNodeBindingResponse`
        """
        return self.update_edge_group_node_binding_with_http_info(request)

    def update_edge_group_node_binding_with_http_info(self, request):
        all_params = ['group_id', 'ief_instance_id', 'update_edge_group_node_binding_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            resource_path='/v2/{project_id}/edgemgr/groups/{group_id}/nodes',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEdgeGroupNodeBindingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_edge_node_async(self, request):
        """更新边缘节点

        该API用于更新边缘节点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEdgeNode
        :type request: :class:`huaweicloudsdkief.v1.UpdateEdgeNodeRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateEdgeNodeResponse`
        """
        return self.update_edge_node_with_http_info(request)

    def update_edge_node_with_http_info(self, request):
        all_params = ['node_id', 'ief_instance_id', 'update_edge_node_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='UpdateEdgeNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_edge_node_device_async(self, request):
        """更新边缘节点的终端设备

        添加或删除边缘节点的终端设备
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEdgeNodeDevice
        :type request: :class:`huaweicloudsdkief.v1.UpdateEdgeNodeDeviceRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateEdgeNodeDeviceResponse`
        """
        return self.update_edge_node_device_with_http_info(request)

    def update_edge_node_device_with_http_info(self, request):
        all_params = ['node_id', 'devices', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='UpdateEdgeNodeDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_encryptdatas_async(self, request):
        """更新加密数据

        更新加密数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEncryptdatas
        :type request: :class:`huaweicloudsdkief.v1.UpdateEncryptdatasRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateEncryptdatasResponse`
        """
        return self.update_encryptdatas_with_http_info(request)

    def update_encryptdatas_with_http_info(self, request):
        all_params = ['encryptdata_id', 'update_encryptdatas_request_body', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'encryptdata_id' in local_var_params:
            path_params['encryptdata_id'] = local_var_params['encryptdata_id']

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
            resource_path='/v2/{project_id}/edm/encryptdatas/{encryptdata_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEncryptdatasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_node_by_device_id_async(self, request):
        """更新终端设备的边缘节点

        该API用于更新终端设备的边缘节点。功能与更新边缘节点的终端设备相同，推荐使用更新边缘节点的终端设备。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateNodeByDeviceId
        :type request: :class:`huaweicloudsdkief.v1.UpdateNodeByDeviceIdRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateNodeByDeviceIdResponse`
        """
        return self.update_node_by_device_id_with_http_info(request)

    def update_node_by_device_id_with_http_info(self, request):
        all_params = ['device_id', 'node', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v2/{project_id}/edgemgr/devices/{device_id}/nodes',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateNodeByDeviceIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_secret_async(self, request):
        """更新密钥

        更新一个密钥
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSecret
        :type request: :class:`huaweicloudsdkief.v1.UpdateSecretRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateSecretResponse`
        """
        return self.update_secret_with_http_info(request)

    def update_secret_with_http_info(self, request):
        all_params = ['secret_id', 'update_secret', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='UpdateSecretResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_service_async(self, request):
        """更新服务

        更新一个服务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateService
        :type request: :class:`huaweicloudsdkief.v1.UpdateServiceRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateServiceResponse`
        """
        return self.update_service_with_http_info(request)

    def update_service_with_http_info(self, request):
        all_params = ['service_id', 'ief_instance_id', 'service']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='UpdateServiceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def upgrade_edge_node_async(self, request):
        """升级边缘节点

        该API用于升级边缘节点。边缘节点将自动升级到最新的可用版本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpgradeEdgeNode
        :type request: :class:`huaweicloudsdkief.v1.UpgradeEdgeNodeRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpgradeEdgeNodeResponse`
        """
        return self.upgrade_edge_node_with_http_info(request)

    def upgrade_edge_node_with_http_info(self, request):
        all_params = ['node_id', 'ief_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v2/{project_id}/edgemgr/nodes/{node_id}/upgrade',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpgradeEdgeNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, cname=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param cname: Used for obs endpoint.
        :param auth_settings: Auth Settings names for the request.
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
            cname=cname,
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type,
	    async_request=True)
