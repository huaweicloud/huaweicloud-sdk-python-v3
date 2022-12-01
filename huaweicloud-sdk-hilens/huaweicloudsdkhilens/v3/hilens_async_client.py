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


class HiLensAsyncClient(Client):
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
        super(HiLensAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkhilens.v3.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "HiLensClient":
            raise TypeError("client type error, support client type is HiLensClient")

        return ClientBuilder(clazz)

    def batch_create_node_tags_async(self, request):
        """批量添加节点标签

        专业版HiLens控制台标签管理，用户选择多个设备，批量添加多个标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateNodeTags
        :type request: :class:`huaweicloudsdkhilens.v3.BatchCreateNodeTagsRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.BatchCreateNodeTagsResponse`
        """
        return self.batch_create_node_tags_with_http_info(request)

    def batch_create_node_tags_with_http_info(self, request):
        all_params = ['multi_resources_multi_tags']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

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
            resource_path='/v3/{project_id}/tag-mgr/node-tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreateNodeTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_config_map_async(self, request):
        """创建配置项

        创建配置项
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateConfigMap
        :type request: :class:`huaweicloudsdkhilens.v3.CreateConfigMapRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.CreateConfigMapResponse`
        """
        return self.create_config_map_with_http_info(request)

    def create_config_map_with_http_info(self, request):
        all_params = ['config_map_model_box_dto', 'provider']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'provider' in local_var_params:
            query_params.append(('provider', local_var_params['provider']))

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
            resource_path='/v3/{project_id}/ai-mgr/configmaps',
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

    def create_node_async(self, request):
        """注册设备

        填写设备信息，将设备注册到HiLens专业版控制台上。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateNode
        :type request: :class:`huaweicloudsdkhilens.v3.CreateNodeRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.CreateNodeResponse`
        """
        return self.create_node_with_http_info(request)

    def create_node_with_http_info(self, request):
        all_params = ['node_request', 'provider']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'provider' in local_var_params:
            query_params.append(('provider', local_var_params['provider']))

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
            resource_path='/v3/{project_id}/ai-mgr/nodes',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_order_form_async(self, request):
        """创建免费技能订单

        创建免费技能订单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateOrderForm
        :type request: :class:`huaweicloudsdkhilens.v3.CreateOrderFormRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.CreateOrderFormResponse`
        """
        return self.create_order_form_with_http_info(request)

    def create_order_form_with_http_info(self, request):
        all_params = ['create_skill_oder']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

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
            resource_path='/v1/{project_id}/skill-market/skill-order',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateOrderFormResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_resource_tags_async(self, request):
        """添加资源标签

        专业版HiLens控制台标签管理，添加对应资源的标签列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateResourceTags
        :type request: :class:`huaweicloudsdkhilens.v3.CreateResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.CreateResourceTagsResponse`
        """
        return self.create_resource_tags_with_http_info(request)

    def create_resource_tags_with_http_info(self, request):
        all_params = ['resource_id', 'resource_type', 'tag_requeste_body']
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
            resource_path='/v3/{project_id}/{resource_type}/{resource_id}/tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateResourceTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_secret_async(self, request):
        """创建密钥

        创建密钥
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSecret
        :type request: :class:`huaweicloudsdkhilens.v3.CreateSecretRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.CreateSecretResponse`
        """
        return self.create_secret_with_http_info(request)

    def create_secret_with_http_info(self, request):
        all_params = ['secret_model_box_dto', 'provider']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'provider' in local_var_params:
            query_params.append(('provider', local_var_params['provider']))

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
            resource_path='/v3/{project_id}/ai-mgr/secrets',
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

    def create_task_async(self, request):
        """创建作业

        创建作业。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTask
        :type request: :class:`huaweicloudsdkhilens.v3.CreateTaskRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.CreateTaskResponse`
        """
        return self.create_task_with_http_info(request)

    def create_task_with_http_info(self, request):
        all_params = ['deployment_id', 'task_request']
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
            resource_path='/v3/{project_id}/ai-mgr/deployments/{deployment_id}/tasks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_work_space_async(self, request):
        """创建工作空间

        创建一个工作空间，其中工作空间名不能与已有的重复
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWorkSpace
        :type request: :class:`huaweicloudsdkhilens.v3.CreateWorkSpaceRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.CreateWorkSpaceResponse`
        """
        return self.create_work_space_with_http_info(request)

    def create_work_space_with_http_info(self, request):
        all_params = ['request_workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

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
            resource_path='/v3/{project_id}/ai-mgr/workspaces',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateWorkSpaceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_config_map_async(self, request):
        """删除配置项

        根据配置项id删除某个配置项
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteConfigMap
        :type request: :class:`huaweicloudsdkhilens.v3.DeleteConfigMapRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.DeleteConfigMapResponse`
        """
        return self.delete_config_map_with_http_info(request)

    def delete_config_map_with_http_info(self, request):
        all_params = ['config_map_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'config_map_id' in local_var_params:
            path_params['config_map_id'] = local_var_params['config_map_id']

        query_params = []

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
            resource_path='/v3/{project_id}/ai-mgr/configmaps/{config_map_id}',
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
        """删除应用部署

        删除指定应用部署。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDeployment
        :type request: :class:`huaweicloudsdkhilens.v3.DeleteDeploymentRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.DeleteDeploymentResponse`
        """
        return self.delete_deployment_with_http_info(request)

    def delete_deployment_with_http_info(self, request):
        all_params = ['deployment_id', 'force_delete', 'provider', 'x_expired_time']
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
        if 'provider' in local_var_params:
            query_params.append(('provider', local_var_params['provider']))

        header_params = {}
        if 'x_expired_time' in local_var_params:
            header_params['X-Expired-Time'] = local_var_params['x_expired_time']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/ai-mgr/deployments/{deployment_id}',
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

    def delete_node_async(self, request):
        """删除设备

        删除专业版HiLens控制台上的设备，并与端侧的设备进行解绑。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteNode
        :type request: :class:`huaweicloudsdkhilens.v3.DeleteNodeRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.DeleteNodeResponse`
        """
        return self.delete_node_with_http_info(request)

    def delete_node_with_http_info(self, request):
        all_params = ['node_id', 'force_delete']
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
        if 'force_delete' in local_var_params:
            query_params.append(('force_delete', local_var_params['force_delete']))

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
            resource_path='/v3/{project_id}/ai-mgr/nodes/{node_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_resource_tag_async(self, request):
        """删除资源标签

        专业版HiLens控制台标签管理，删除对应资源的标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteResourceTag
        :type request: :class:`huaweicloudsdkhilens.v3.DeleteResourceTagRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.DeleteResourceTagResponse`
        """
        return self.delete_resource_tag_with_http_info(request)

    def delete_resource_tag_with_http_info(self, request):
        all_params = ['resource_id', 'resource_type', 'key']
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
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']

        query_params = []

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
            resource_path='/v3/{project_id}/{resource_type}/{resource_id}/tags/{key}',
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

    def delete_secret_async(self, request):
        """删除密钥

        删除密钥
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSecret
        :type request: :class:`huaweicloudsdkhilens.v3.DeleteSecretRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.DeleteSecretResponse`
        """
        return self.delete_secret_with_http_info(request)

    def delete_secret_with_http_info(self, request):
        all_params = ['secret_id']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/ai-mgr/secrets/{secret_id}',
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

    def delete_task_async(self, request):
        """删除作业

        删除作业。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTask
        :type request: :class:`huaweicloudsdkhilens.v3.DeleteTaskRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.DeleteTaskResponse`
        """
        return self.delete_task_with_http_info(request)

    def delete_task_with_http_info(self, request):
        all_params = ['deployment_id', 'task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

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
            resource_path='/v3/{project_id}/ai-mgr/deployments/{deployment_id}/tasks/{task_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_work_space_async(self, request):
        """删除工作空间

        删除指定ID的工作空间，如果该工作空间下仍有资源，则删除会失败
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteWorkSpace
        :type request: :class:`huaweicloudsdkhilens.v3.DeleteWorkSpaceRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.DeleteWorkSpaceResponse`
        """
        return self.delete_work_space_with_http_info(request)

    def delete_work_space_with_http_info(self, request):
        all_params = ['workspace_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

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
            resource_path='/v3/{project_id}/ai-mgr/workspaces/{workspace_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteWorkSpaceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def freeze_node_async(self, request):
        """将激活订单与设备解绑

        将激活订单与设备解绑。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for FreezeNode
        :type request: :class:`huaweicloudsdkhilens.v3.FreezeNodeRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.FreezeNodeResponse`
        """
        return self.freeze_node_with_http_info(request)

    def freeze_node_with_http_info(self, request):
        all_params = ['node_id']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/ai-mgr/nodes/{node_id}/deactivate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='FreezeNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_config_maps_async(self, request):
        """查询配置项列表

        获取配置项详情，以列表形式返回。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConfigMaps
        :type request: :class:`huaweicloudsdkhilens.v3.ListConfigMapsRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ListConfigMapsResponse`
        """
        return self.list_config_maps_with_http_info(request)

    def list_config_maps_with_http_info(self, request):
        all_params = ['provider', 'name', 'workspace_id', 'limit', 'offset', 'sort', 'tag_key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'provider' in local_var_params:
            query_params.append(('provider', local_var_params['provider']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'tag_key' in local_var_params:
            query_params.append(('tag_key', local_var_params['tag_key']))

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
            resource_path='/v3/{project_id}/ai-mgr/configmaps',
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

    def list_resource_tags_async(self, request):
        """查询某资源类型的标签

        专业版HiLens控制台标签管理，查询某种资源类型的所有标签，返回标签列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResourceTags
        :type request: :class:`huaweicloudsdkhilens.v3.ListResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ListResourceTagsResponse`
        """
        return self.list_resource_tags_with_http_info(request)

    def list_resource_tags_with_http_info(self, request):
        all_params = ['resource_type']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/tag-mgr/{resource_type}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListResourceTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_secrets_async(self, request):
        """查询密钥列表

        专业版HiLens控制台密钥管理，根据用户请求条件筛选，查询用户创建的 密钥信息，以列表形式返回。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSecrets
        :type request: :class:`huaweicloudsdkhilens.v3.ListSecretsRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ListSecretsResponse`
        """
        return self.list_secrets_with_http_info(request)

    def list_secrets_with_http_info(self, request):
        all_params = ['offset', 'limit', 'name', 'workspace_id', 'tags', 'provider', 'sort']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'provider' in local_var_params:
            query_params.append(('provider', local_var_params['provider']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))

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
            resource_path='/v3/{project_id}/ai-mgr/secrets',
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

    def list_tasks_async(self, request):
        """查询作业列表

        查询当前部署下所有作业，返回详情列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTasks
        :type request: :class:`huaweicloudsdkhilens.v3.ListTasksRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ListTasksResponse`
        """
        return self.list_tasks_with_http_info(request)

    def list_tasks_with_http_info(self, request):
        all_params = ['deployment_id']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/ai-mgr/deployments/{deployment_id}/tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_work_spaces_async(self, request):
        """获取工作空间列表

        查询用户名下的所有工作空间信息，并返回列表和总条目数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWorkSpaces
        :type request: :class:`huaweicloudsdkhilens.v3.ListWorkSpacesRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ListWorkSpacesResponse`
        """
        return self.list_work_spaces_with_http_info(request)

    def list_work_spaces_with_http_info(self, request):
        all_params = ['iam_user_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'iam_user_id' in local_var_params:
            query_params.append(('iam_user_id', local_var_params['iam_user_id']))

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
            resource_path='/v3/{project_id}/ai-mgr/workspaces',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListWorkSpacesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_default_order_form_async(self, request):
        """设置默认订单

        设置默认订单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetDefaultOrderForm
        :type request: :class:`huaweicloudsdkhilens.v3.SetDefaultOrderFormRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.SetDefaultOrderFormResponse`
        """
        return self.set_default_order_form_with_http_info(request)

    def set_default_order_form_with_http_info(self, request):
        all_params = ['order_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'order_id' in local_var_params:
            path_params['order_id'] = local_var_params['order_id']

        query_params = []

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
            resource_path='/v1/{project_id}/skill-market/skill-order/{order_id}/default',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SetDefaultOrderFormResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_config_map_async(self, request):
        """查询配置项详情

        根据配置项id查询某个配置项详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowConfigMap
        :type request: :class:`huaweicloudsdkhilens.v3.ShowConfigMapRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowConfigMapResponse`
        """
        return self.show_config_map_with_http_info(request)

    def show_config_map_with_http_info(self, request):
        all_params = ['config_map_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'config_map_id' in local_var_params:
            path_params['config_map_id'] = local_var_params['config_map_id']

        query_params = []

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
            resource_path='/v3/{project_id}/ai-mgr/configmaps/{config_map_id}',
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

    def show_deployment_pods_async(self, request):
        """查询应用实例列表

        获取用户实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDeploymentPods
        :type request: :class:`huaweicloudsdkhilens.v3.ShowDeploymentPodsRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowDeploymentPodsResponse`
        """
        return self.show_deployment_pods_with_http_info(request)

    def show_deployment_pods_with_http_info(self, request):
        all_params = ['cluster_id', 'node_id', 'provider', 'deployment_id', 'workspace_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'provider' in local_var_params:
            query_params.append(('provider', local_var_params['provider']))
        if 'deployment_id' in local_var_params:
            query_params.append(('deployment_id', local_var_params['deployment_id']))
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))

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
            resource_path='/v3/{project_id}/ai-mgr/pods',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDeploymentPodsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_node_async(self, request):
        """查询设备详情

        支持查询HiLens专业版控制台上的设备详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNode
        :type request: :class:`huaweicloudsdkhilens.v3.ShowNodeRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowNodeResponse`
        """
        return self.show_node_with_http_info(request)

    def show_node_with_http_info(self, request):
        all_params = ['node_id']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/ai-mgr/nodes/{node_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_node_activation_records_async(self, request):
        """获取激活记录列表

        获取激活记录列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNodeActivationRecords
        :type request: :class:`huaweicloudsdkhilens.v3.ShowNodeActivationRecordsRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowNodeActivationRecordsResponse`
        """
        return self.show_node_activation_records_with_http_info(request)

    def show_node_activation_records_with_http_info(self, request):
        all_params = ['node_id', 'offset', 'limit']
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v3/{project_id}/ai-mgr/nodes/{node_id}/activation/records',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowNodeActivationRecordsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_nodes_async(self, request):
        """查询设备列表

        专业版HiLens控制台设备管理，根据用户请求条件筛选，查询用户注册的设备信息，以列表形式返回。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNodes
        :type request: :class:`huaweicloudsdkhilens.v3.ShowNodesRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowNodesResponse`
        """
        return self.show_nodes_with_http_info(request)

    def show_nodes_with_http_info(self, request):
        all_params = ['offset', 'limit', 'name', 'workspace_id', 'app_name', 'tags', 'provider', 'cluster_id', 'status', 'active_status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'provider' in local_var_params:
            query_params.append(('provider', local_var_params['provider']))
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'active_status' in local_var_params:
            query_params.append(('active_status', local_var_params['active_status']))

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
            resource_path='/v3/{project_id}/ai-mgr/nodes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowNodesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_resource_tags_async(self, request):
        """查询资源标签

        专业版HiLens控制台标签管理，查询具体资源的标签，返回标签列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourceTags
        :type request: :class:`huaweicloudsdkhilens.v3.ShowResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowResourceTagsResponse`
        """
        return self.show_resource_tags_with_http_info(request)

    def show_resource_tags_with_http_info(self, request):
        all_params = ['resource_id', 'resource_type']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/{resource_type}/{resource_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowResourceTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_secret_async(self, request):
        """查询密钥详情

        查询密钥详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSecret
        :type request: :class:`huaweicloudsdkhilens.v3.ShowSecretRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowSecretResponse`
        """
        return self.show_secret_with_http_info(request)

    def show_secret_with_http_info(self, request):
        all_params = ['secret_id']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/ai-mgr/secrets/{secret_id}',
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

    def show_skill_info_async(self, request):
        """获取技能详情

        获取技能详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSkillInfo
        :type request: :class:`huaweicloudsdkhilens.v3.ShowSkillInfoRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowSkillInfoResponse`
        """
        return self.show_skill_info_with_http_info(request)

    def show_skill_info_with_http_info(self, request):
        all_params = ['skill_id', 'status', 'version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'skill_id' in local_var_params:
            path_params['skill_id'] = local_var_params['skill_id']

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/skill-market/skills/{skill_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSkillInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_skill_list_async(self, request):
        """查询技能列表

        获取技能列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSkillList
        :type request: :class:`huaweicloudsdkhilens.v3.ShowSkillListRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowSkillListResponse`
        """
        return self.show_skill_list_with_http_info(request)

    def show_skill_list_with_http_info(self, request):
        all_params = ['limit', 'offset', 'skill_name', 'skill_form', 'permission', 'template_source', 'status', 'charge_model', 'platform', 'chip', 'type', 'charge_models', 'device_types', 'scenes']
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
        if 'skill_name' in local_var_params:
            query_params.append(('skill_name', local_var_params['skill_name']))
        if 'skill_form' in local_var_params:
            query_params.append(('skill_form', local_var_params['skill_form']))
        if 'permission' in local_var_params:
            query_params.append(('permission', local_var_params['permission']))
        if 'template_source' in local_var_params:
            query_params.append(('template_source', local_var_params['template_source']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'charge_model' in local_var_params:
            query_params.append(('charge_model', local_var_params['charge_model']))
        if 'platform' in local_var_params:
            query_params.append(('platform', local_var_params['platform']))
        if 'chip' in local_var_params:
            query_params.append(('chip', local_var_params['chip']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'charge_models' in local_var_params:
            query_params.append(('charge_models', local_var_params['charge_models']))
        if 'device_types' in local_var_params:
            query_params.append(('device_types', local_var_params['device_types']))
        if 'scenes' in local_var_params:
            query_params.append(('scenes', local_var_params['scenes']))

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
            resource_path='/v1/skill-market/skills',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSkillListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_skill_order_info_async(self, request):
        """查询订单详情

        获取订单详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSkillOrderInfo
        :type request: :class:`huaweicloudsdkhilens.v3.ShowSkillOrderInfoRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowSkillOrderInfoResponse`
        """
        return self.show_skill_order_info_with_http_info(request)

    def show_skill_order_info_with_http_info(self, request):
        all_params = ['order_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'order_id' in local_var_params:
            path_params['order_id'] = local_var_params['order_id']

        query_params = []

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
            resource_path='/v1/{project_id}/skill-market/skill-order/{order_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSkillOrderInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_skill_order_list_async(self, request):
        """查询订单列表

        获取订单列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSkillOrderList
        :type request: :class:`huaweicloudsdkhilens.v3.ShowSkillOrderListRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowSkillOrderListResponse`
        """
        return self.show_skill_order_list_with_http_info(request)

    def show_skill_order_list_with_http_info(self, request):
        all_params = ['limit', 'offset', 'skill_name', 'skill_form']
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
        if 'skill_name' in local_var_params:
            query_params.append(('skill_name', local_var_params['skill_name']))
        if 'skill_form' in local_var_params:
            query_params.append(('skill_form', local_var_params['skill_form']))

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
            resource_path='/v1/{project_id}/skill-market/skill-order',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSkillOrderListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_task_async(self, request):
        """查询作业详情

        通过作业ID查询作业详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTask
        :type request: :class:`huaweicloudsdkhilens.v3.ShowTaskRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowTaskResponse`
        """
        return self.show_task_with_http_info(request)

    def show_task_with_http_info(self, request):
        all_params = ['deployment_id', 'task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

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
            resource_path='/v3/{project_id}/ai-mgr/deployments/{deployment_id}/tasks/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_upgrade_progress_async(self, request):
        """获取设备固件升级进度

        获取设备固件升级进度。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowUpgradeProgress
        :type request: :class:`huaweicloudsdkhilens.v3.ShowUpgradeProgressRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowUpgradeProgressResponse`
        """
        return self.show_upgrade_progress_with_http_info(request)

    def show_upgrade_progress_with_http_info(self, request):
        all_params = ['node_id']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/node-manager/node/{node_id}/firmware/upgrade-progress',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowUpgradeProgressResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_work_space_async(self, request):
        """获取工作空间详情

        获取指定workspace_id的工作空间详情，包括创建时间，描述，创建者等信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWorkSpace
        :type request: :class:`huaweicloudsdkhilens.v3.ShowWorkSpaceRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowWorkSpaceResponse`
        """
        return self.show_work_space_with_http_info(request)

    def show_work_space_with_http_info(self, request):
        all_params = ['workspace_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

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
            resource_path='/v3/{project_id}/ai-mgr/workspaces/{workspace_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowWorkSpaceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def switch_node_connection_async(self, request):
        """启停设备

        该API用于启用停用设备。被停用的设备将无法连接到云端服务，重新启用设备恢复连接。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SwitchNodeConnection
        :type request: :class:`huaweicloudsdkhilens.v3.SwitchNodeConnectionRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.SwitchNodeConnectionResponse`
        """
        return self.switch_node_connection_with_http_info(request)

    def switch_node_connection_with_http_info(self, request):
        all_params = ['node_id', 'action', 'provider']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']
        if 'action' in local_var_params:
            path_params['action'] = local_var_params['action']

        query_params = []
        if 'provider' in local_var_params:
            query_params.append(('provider', local_var_params['provider']))

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
            resource_path='/v3/{project_id}/ai-mgr/nodes/{node_id}/action/{action}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SwitchNodeConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def unfreeze_node_async(self, request):
        """使用运行服务费激活设备

        使用运行服务费激活设备。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UnfreezeNode
        :type request: :class:`huaweicloudsdkhilens.v3.UnfreezeNodeRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.UnfreezeNodeResponse`
        """
        return self.unfreeze_node_with_http_info(request)

    def unfreeze_node_with_http_info(self, request):
        all_params = ['node_id', 'activate_node']
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
            resource_path='/v3/{project_id}/ai-mgr/nodes/{node_id}/activate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UnfreezeNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_config_map_async(self, request):
        """更新配置项

        根据配置项id更新配置项信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateConfigMap
        :type request: :class:`huaweicloudsdkhilens.v3.UpdateConfigMapRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.UpdateConfigMapResponse`
        """
        return self.update_config_map_with_http_info(request)

    def update_config_map_with_http_info(self, request):
        all_params = ['config_map_id', 'config_map_model_box_dto']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'config_map_id' in local_var_params:
            path_params['config_map_id'] = local_var_params['config_map_id']

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
            resource_path='/v3/{project_id}/ai-mgr/configmaps/{config_map_id}',
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

    def update_deployment_using_patch_async(self, request):
        """部分更新应用部署

        更新应用部署部分信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDeploymentUsingPatch
        :type request: :class:`huaweicloudsdkhilens.v3.UpdateDeploymentUsingPatchRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.UpdateDeploymentUsingPatchResponse`
        """
        return self.update_deployment_using_patch_with_http_info(request)

    def update_deployment_using_patch_with_http_info(self, request):
        all_params = ['deployment_id', 'patch']
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
            resource_path='/v3/{project_id}/ai-mgr/deployments/{deployment_id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDeploymentUsingPatchResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_node_async(self, request):
        """更新设备信息

        更新设备日志配置，标签以及描述。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateNode
        :type request: :class:`huaweicloudsdkhilens.v3.UpdateNodeRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.UpdateNodeResponse`
        """
        return self.update_node_with_http_info(request)

    def update_node_with_http_info(self, request):
        all_params = ['node_id', 'update_node_request']
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
            resource_path='/v3/{project_id}/ai-mgr/nodes/{node_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_node_cert_async(self, request):
        """更新设备证书

        设备出现离线或者证书过期时，可通过该接口更新证书，重新让设备连接到云端
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateNodeCert
        :type request: :class:`huaweicloudsdkhilens.v3.UpdateNodeCertRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.UpdateNodeCertResponse`
        """
        return self.update_node_cert_with_http_info(request)

    def update_node_cert_with_http_info(self, request):
        all_params = ['node_id']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/ai-mgr/nodes/{node_id}/cert',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateNodeCertResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_node_firmware_async(self, request):
        """升级设备固件

        升级设备固件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateNodeFirmware
        :type request: :class:`huaweicloudsdkhilens.v3.UpdateNodeFirmwareRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.UpdateNodeFirmwareResponse`
        """
        return self.update_node_firmware_with_http_info(request)

    def update_node_firmware_with_http_info(self, request):
        all_params = ['node_id', 'firmware_id', 'x_expired_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']
        if 'firmware_id' in local_var_params:
            path_params['firmware_id'] = local_var_params['firmware_id']

        query_params = []

        header_params = {}
        if 'x_expired_time' in local_var_params:
            header_params['X-Expired-Time'] = local_var_params['x_expired_time']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["firmware_name", "firmware_id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/node-manager/node/{node_id}/firmware/{firmware_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateNodeFirmwareResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_secret_async(self, request):
        """更新密钥

        更新密钥
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSecret
        :type request: :class:`huaweicloudsdkhilens.v3.UpdateSecretRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.UpdateSecretResponse`
        """
        return self.update_secret_with_http_info(request)

    def update_secret_with_http_info(self, request):
        all_params = ['secret_id', 'secret_model_box_dto']
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
            resource_path='/v3/{project_id}/ai-mgr/secrets/{secret_id}',
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

    def update_task_async(self, request):
        """编辑作业

        编辑作业。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTask
        :type request: :class:`huaweicloudsdkhilens.v3.UpdateTaskRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.UpdateTaskResponse`
        """
        return self.update_task_with_http_info(request)

    def update_task_with_http_info(self, request):
        all_params = ['deployment_id', 'task_id', 'task_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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
            resource_path='/v3/{project_id}/ai-mgr/deployments/{deployment_id}/task/{task_id}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_work_space_async(self, request):
        """修改工作空间

        更改工作空间信息，暂时只能更改描述
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateWorkSpace
        :type request: :class:`huaweicloudsdkhilens.v3.UpdateWorkSpaceRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.UpdateWorkSpaceResponse`
        """
        return self.update_work_space_with_http_info(request)

    def update_work_space_with_http_info(self, request):
        all_params = ['workspace_id', 'update_workspace_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

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
            resource_path='/v3/{project_id}/ai-mgr/workspaces/{workspace_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateWorkSpaceResponse',
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
