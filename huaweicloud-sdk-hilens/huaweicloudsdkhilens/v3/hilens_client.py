# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class HiLensClient(Client):
    def __init__(self):
        super(HiLensClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkhilens.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "HiLensClient":
                raise TypeError("client type error, support client type is HiLensClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_deployment_nodes(self, request):
        """批量部署

        通过指定设备id列表或者设备标签将应用部署下发到多个设备上。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddDeploymentNodes
        :type request: :class:`huaweicloudsdkhilens.v3.AddDeploymentNodesRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.AddDeploymentNodesResponse`
        """
        return self._add_deployment_nodes_with_http_info(request)

    def _add_deployment_nodes_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

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
            resource_path='/v3/{project_id}/ai-mgr/deployments/{deployment_id}/nodes',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddDeploymentNodesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_create_node_tags(self, request):
        """批量添加节点标签

        专业版HiLens控制台标签管理，用户选择多个设备，批量添加多个标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateNodeTags
        :type request: :class:`huaweicloudsdkhilens.v3.BatchCreateNodeTagsRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.BatchCreateNodeTagsResponse`
        """
        return self._batch_create_node_tags_with_http_info(request)

    def _batch_create_node_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def create_config_map(self, request):
        """创建配置项

        创建配置项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateConfigMap
        :type request: :class:`huaweicloudsdkhilens.v3.CreateConfigMapRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.CreateConfigMapResponse`
        """
        return self._create_config_map_with_http_info(request)

    def _create_config_map_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def create_deployment(self, request):
        """创建应用部署

        创建应用部署。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDeployment
        :type request: :class:`huaweicloudsdkhilens.v3.CreateDeploymentRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.CreateDeploymentResponse`
        """
        return self._create_deployment_with_http_info(request)

    def _create_deployment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'provider' in local_var_params:
            query_params.append(('provider', local_var_params['provider']))

        header_params = {}
        if 'x_expired_time' in local_var_params:
            header_params['X-Expired-Time'] = local_var_params['x_expired_time']

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
            resource_path='/v3/{project_id}/ai-mgr/deployments',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDeploymentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_node(self, request):
        """注册设备

        填写设备信息，将设备注册到HiLens专业版控制台上。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateNode
        :type request: :class:`huaweicloudsdkhilens.v3.CreateNodeRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.CreateNodeResponse`
        """
        return self._create_node_with_http_info(request)

    def _create_node_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def create_order_form(self, request):
        """创建免费技能订单

        创建免费技能订单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateOrderForm
        :type request: :class:`huaweicloudsdkhilens.v3.CreateOrderFormRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.CreateOrderFormResponse`
        """
        return self._create_order_form_with_http_info(request)

    def _create_order_form_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def create_resource_tags(self, request):
        """添加资源标签

        专业版HiLens控制台标签管理，添加对应资源的标签列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateResourceTags
        :type request: :class:`huaweicloudsdkhilens.v3.CreateResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.CreateResourceTagsResponse`
        """
        return self._create_resource_tags_with_http_info(request)

    def _create_resource_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def create_secret(self, request):
        """创建密钥

        创建密钥
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSecret
        :type request: :class:`huaweicloudsdkhilens.v3.CreateSecretRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.CreateSecretResponse`
        """
        return self._create_secret_with_http_info(request)

    def _create_secret_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def create_task(self, request):
        """创建作业

        创建作业。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTask
        :type request: :class:`huaweicloudsdkhilens.v3.CreateTaskRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.CreateTaskResponse`
        """
        return self._create_task_with_http_info(request)

    def _create_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def create_work_space(self, request):
        """创建工作空间

        创建一个工作空间，其中工作空间名不能与已有的重复
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateWorkSpace
        :type request: :class:`huaweicloudsdkhilens.v3.CreateWorkSpaceRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.CreateWorkSpaceResponse`
        """
        return self._create_work_space_with_http_info(request)

    def _create_work_space_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def delete_config_map(self, request):
        """删除配置项

        根据配置项id删除某个配置项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteConfigMap
        :type request: :class:`huaweicloudsdkhilens.v3.DeleteConfigMapRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.DeleteConfigMapResponse`
        """
        return self._delete_config_map_with_http_info(request)

    def _delete_config_map_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def delete_deployment(self, request):
        """删除应用部署

        删除指定应用部署。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDeployment
        :type request: :class:`huaweicloudsdkhilens.v3.DeleteDeploymentRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.DeleteDeploymentResponse`
        """
        return self._delete_deployment_with_http_info(request)

    def _delete_deployment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def delete_node(self, request):
        """删除设备

        删除专业版HiLens控制台上的设备，并与端侧的设备进行解绑。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteNode
        :type request: :class:`huaweicloudsdkhilens.v3.DeleteNodeRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.DeleteNodeResponse`
        """
        return self._delete_node_with_http_info(request)

    def _delete_node_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def delete_pod(self, request):
        """删除应用实例

        删除指定实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePod
        :type request: :class:`huaweicloudsdkhilens.v3.DeletePodRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.DeletePodResponse`
        """
        return self._delete_pod_with_http_info(request)

    def _delete_pod_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']
        if 'pod_id' in local_var_params:
            path_params['pod_id'] = local_var_params['pod_id']

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
            resource_path='/v3/{project_id}/ai-mgr/deployments/{deployment_id}/{pod_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePodResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_resource_tag(self, request):
        """删除资源标签

        专业版HiLens控制台标签管理，删除对应资源的标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteResourceTag
        :type request: :class:`huaweicloudsdkhilens.v3.DeleteResourceTagRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.DeleteResourceTagResponse`
        """
        return self._delete_resource_tag_with_http_info(request)

    def _delete_resource_tag_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def delete_secret(self, request):
        """删除密钥

        删除密钥
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSecret
        :type request: :class:`huaweicloudsdkhilens.v3.DeleteSecretRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.DeleteSecretResponse`
        """
        return self._delete_secret_with_http_info(request)

    def _delete_secret_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def delete_task(self, request):
        """删除作业

        删除作业。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTask
        :type request: :class:`huaweicloudsdkhilens.v3.DeleteTaskRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.DeleteTaskResponse`
        """
        return self._delete_task_with_http_info(request)

    def _delete_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def delete_work_space(self, request):
        """删除工作空间

        删除指定ID的工作空间，如果该工作空间下仍有资源，则删除会失败
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteWorkSpace
        :type request: :class:`huaweicloudsdkhilens.v3.DeleteWorkSpaceRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.DeleteWorkSpaceResponse`
        """
        return self._delete_work_space_with_http_info(request)

    def _delete_work_space_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def freeze_node(self, request):
        """将激活订单与设备解绑

        将激活订单与设备解绑。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for FreezeNode
        :type request: :class:`huaweicloudsdkhilens.v3.FreezeNodeRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.FreezeNodeResponse`
        """
        return self._freeze_node_with_http_info(request)

    def _freeze_node_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_config_maps(self, request):
        """查询配置项列表

        获取配置项详情，以列表形式返回。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConfigMaps
        :type request: :class:`huaweicloudsdkhilens.v3.ListConfigMapsRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ListConfigMapsResponse`
        """
        return self._list_config_maps_with_http_info(request)

    def _list_config_maps_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_firmwares(self, request):
        """查询固件列表

        查看指定固件历史版本信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFirmwares
        :type request: :class:`huaweicloudsdkhilens.v3.ListFirmwaresRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ListFirmwaresResponse`
        """
        return self._list_firmwares_with_http_info(request)

    def _list_firmwares_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'device_type' in local_var_params:
            query_params.append(('device_type', local_var_params['device_type']))
        if 'arch' in local_var_params:
            query_params.append(('arch', local_var_params['arch']))
        if 'os_name' in local_var_params:
            query_params.append(('os_name', local_var_params['os_name']))
        if 'os_version' in local_var_params:
            query_params.append(('os_version', local_var_params['os_version']))
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
            resource_path='/v3/ai-mgr/firmwares',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFirmwaresResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_platform_manager(self, request):
        """获取运行服务费订单列表

        获取平台管理费列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPlatformManager
        :type request: :class:`huaweicloudsdkhilens.v3.ListPlatformManagerRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ListPlatformManagerResponse`
        """
        return self._list_platform_manager_with_http_info(request)

    def _list_platform_manager_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'device_type' in local_var_params:
            query_params.append(('device_type', local_var_params['device_type']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
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
            resource_path='/v1/{project_id}/platform-manager/orders',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPlatformManagerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_resource_tags(self, request):
        """查询某资源类型的标签

        专业版HiLens控制台标签管理，查询某种资源类型的所有标签，返回标签列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceTags
        :type request: :class:`huaweicloudsdkhilens.v3.ListResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ListResourceTagsResponse`
        """
        return self._list_resource_tags_with_http_info(request)

    def _list_resource_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_secrets(self, request):
        """查询密钥列表

        专业版HiLens控制台密钥管理，根据用户请求条件筛选，查询用户创建的 密钥信息，以列表形式返回。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSecrets
        :type request: :class:`huaweicloudsdkhilens.v3.ListSecretsRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ListSecretsResponse`
        """
        return self._list_secrets_with_http_info(request)

    def _list_secrets_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_tasks(self, request):
        """查询作业列表

        查询当前部署下所有作业，返回详情列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTasks
        :type request: :class:`huaweicloudsdkhilens.v3.ListTasksRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ListTasksResponse`
        """
        return self._list_tasks_with_http_info(request)

    def _list_tasks_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

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

    def list_work_spaces(self, request):
        """获取工作空间列表

        查询用户名下的所有工作空间信息，并返回列表和总条目数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWorkSpaces
        :type request: :class:`huaweicloudsdkhilens.v3.ListWorkSpacesRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ListWorkSpacesResponse`
        """
        return self._list_work_spaces_with_http_info(request)

    def _list_work_spaces_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'iam_user_id' in local_var_params:
            query_params.append(('iam_user_id', local_var_params['iam_user_id']))
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

    def set_default_order_form(self, request):
        """设置默认订单

        设置默认订单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetDefaultOrderForm
        :type request: :class:`huaweicloudsdkhilens.v3.SetDefaultOrderFormRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.SetDefaultOrderFormResponse`
        """
        return self._set_default_order_form_with_http_info(request)

    def _set_default_order_form_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_config_map(self, request):
        """查询配置项详情

        根据配置项id查询某个配置项详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowConfigMap
        :type request: :class:`huaweicloudsdkhilens.v3.ShowConfigMapRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowConfigMapResponse`
        """
        return self._show_config_map_with_http_info(request)

    def _show_config_map_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_deployment(self, request):
        """查询应用部署详情

        获取部署的详情信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeployment
        :type request: :class:`huaweicloudsdkhilens.v3.ShowDeploymentRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowDeploymentResponse`
        """
        return self._show_deployment_with_http_info(request)

    def _show_deployment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

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
            resource_path='/v3/{project_id}/ai-mgr/deployments/{deployment_id}',
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

    def show_deployment_pods(self, request):
        """查询应用实例列表

        获取用户实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeploymentPods
        :type request: :class:`huaweicloudsdkhilens.v3.ShowDeploymentPodsRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowDeploymentPodsResponse`
        """
        return self._show_deployment_pods_with_http_info(request)

    def _show_deployment_pods_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_deployments(self, request):
        """查询应用部署列表

        获取部署列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeployments
        :type request: :class:`huaweicloudsdkhilens.v3.ShowDeploymentsRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowDeploymentsResponse`
        """
        return self._show_deployments_with_http_info(request)

    def _show_deployments_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v3/{project_id}/ai-mgr/deployments',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDeploymentsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_node(self, request):
        """查询设备详情

        支持查询HiLens专业版控制台上的设备详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNode
        :type request: :class:`huaweicloudsdkhilens.v3.ShowNodeRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowNodeResponse`
        """
        return self._show_node_with_http_info(request)

    def _show_node_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_node_activation_records(self, request):
        """获取激活记录列表

        获取激活记录列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNodeActivationRecords
        :type request: :class:`huaweicloudsdkhilens.v3.ShowNodeActivationRecordsRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowNodeActivationRecordsResponse`
        """
        return self._show_node_activation_records_with_http_info(request)

    def _show_node_activation_records_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_nodes(self, request):
        """查询设备列表

        专业版HiLens控制台设备管理，根据用户请求条件筛选，查询用户注册的设备信息，以列表形式返回。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNodes
        :type request: :class:`huaweicloudsdkhilens.v3.ShowNodesRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowNodesResponse`
        """
        return self._show_nodes_with_http_info(request)

    def _show_nodes_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_resource_tags(self, request):
        """查询资源标签

        专业版HiLens控制台标签管理，查询具体资源的标签，返回标签列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowResourceTags
        :type request: :class:`huaweicloudsdkhilens.v3.ShowResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowResourceTagsResponse`
        """
        return self._show_resource_tags_with_http_info(request)

    def _show_resource_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_secret(self, request):
        """查询密钥详情

        查询密钥详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSecret
        :type request: :class:`huaweicloudsdkhilens.v3.ShowSecretRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowSecretResponse`
        """
        return self._show_secret_with_http_info(request)

    def _show_secret_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_skill_info(self, request):
        """获取技能详情

        获取技能详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSkillInfo
        :type request: :class:`huaweicloudsdkhilens.v3.ShowSkillInfoRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowSkillInfoResponse`
        """
        return self._show_skill_info_with_http_info(request)

    def _show_skill_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_skill_list(self, request):
        """查询技能列表

        获取技能列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSkillList
        :type request: :class:`huaweicloudsdkhilens.v3.ShowSkillListRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowSkillListResponse`
        """
        return self._show_skill_list_with_http_info(request)

    def _show_skill_list_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_skill_order_info(self, request):
        """查询订单详情

        获取订单详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSkillOrderInfo
        :type request: :class:`huaweicloudsdkhilens.v3.ShowSkillOrderInfoRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowSkillOrderInfoResponse`
        """
        return self._show_skill_order_info_with_http_info(request)

    def _show_skill_order_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_skill_order_list(self, request):
        """查询订单列表

        获取订单列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSkillOrderList
        :type request: :class:`huaweicloudsdkhilens.v3.ShowSkillOrderListRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowSkillOrderListResponse`
        """
        return self._show_skill_order_list_with_http_info(request)

    def _show_skill_order_list_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_task(self, request):
        """查询作业详情

        通过作业ID查询作业详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTask
        :type request: :class:`huaweicloudsdkhilens.v3.ShowTaskRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowTaskResponse`
        """
        return self._show_task_with_http_info(request)

    def _show_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_upgrade_progress(self, request):
        """获取设备固件升级进度

        获取设备固件升级进度。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUpgradeProgress
        :type request: :class:`huaweicloudsdkhilens.v3.ShowUpgradeProgressRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowUpgradeProgressResponse`
        """
        return self._show_upgrade_progress_with_http_info(request)

    def _show_upgrade_progress_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_work_space(self, request):
        """获取工作空间详情

        获取指定workspace_id的工作空间详情，包括创建时间，描述，创建者等信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowWorkSpace
        :type request: :class:`huaweicloudsdkhilens.v3.ShowWorkSpaceRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.ShowWorkSpaceResponse`
        """
        return self._show_work_space_with_http_info(request)

    def _show_work_space_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def start_and_stop_deployment(self, request):
        """暂停、继续部署负载

        启动/暂停应用部署。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartAndStopDeployment
        :type request: :class:`huaweicloudsdkhilens.v3.StartAndStopDeploymentRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.StartAndStopDeploymentResponse`
        """
        return self._start_and_stop_deployment_with_http_info(request)

    def _start_and_stop_deployment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']
        if 'action' in local_var_params:
            path_params['action'] = local_var_params['action']

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
            resource_path='/v3/{project_id}/ai-mgr/deployments/{deployment_id}/action/{action}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StartAndStopDeploymentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_and_stop_deployment_pod(self, request):
        """启动/停止部署下的指定实例

        启动/停止部署下的指定实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartAndStopDeploymentPod
        :type request: :class:`huaweicloudsdkhilens.v3.StartAndStopDeploymentPodRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.StartAndStopDeploymentPodResponse`
        """
        return self._start_and_stop_deployment_pod_with_http_info(request)

    def _start_and_stop_deployment_pod_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']
        if 'pod_id' in local_var_params:
            path_params['pod_id'] = local_var_params['pod_id']
        if 'action' in local_var_params:
            path_params['action'] = local_var_params['action']

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
            resource_path='/v3/{project_id}/ai-mgr/deployments/{deployment_id}/{pod_id}/action/{action}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StartAndStopDeploymentPodResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def switch_node_connection(self, request):
        """启停设备

        该API用于启用停用设备。被停用的设备将无法连接到云端服务，重新启用设备恢复连接。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchNodeConnection
        :type request: :class:`huaweicloudsdkhilens.v3.SwitchNodeConnectionRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.SwitchNodeConnectionResponse`
        """
        return self._switch_node_connection_with_http_info(request)

    def _switch_node_connection_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def unfreeze_node(self, request):
        """使用运行服务费激活设备

        使用运行服务费激活设备。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UnfreezeNode
        :type request: :class:`huaweicloudsdkhilens.v3.UnfreezeNodeRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.UnfreezeNodeResponse`
        """
        return self._unfreeze_node_with_http_info(request)

    def _unfreeze_node_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def update_config_map(self, request):
        """更新配置项

        根据配置项id更新配置项信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateConfigMap
        :type request: :class:`huaweicloudsdkhilens.v3.UpdateConfigMapRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.UpdateConfigMapResponse`
        """
        return self._update_config_map_with_http_info(request)

    def _update_config_map_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def update_deployment(self, request):
        """更新应用部署

        更新应用部署相关信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDeployment
        :type request: :class:`huaweicloudsdkhilens.v3.UpdateDeploymentRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.UpdateDeploymentResponse`
        """
        return self._update_deployment_with_http_info(request)

    def _update_deployment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

        query_params = []
        if 'provider' in local_var_params:
            query_params.append(('provider', local_var_params['provider']))

        header_params = {}
        if 'x_expired_time' in local_var_params:
            header_params['X-Expired-Time'] = local_var_params['x_expired_time']

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

    def update_deployment_using_patch(self, request):
        """部分更新应用部署

        更新应用部署部分信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDeploymentUsingPatch
        :type request: :class:`huaweicloudsdkhilens.v3.UpdateDeploymentUsingPatchRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.UpdateDeploymentUsingPatchResponse`
        """
        return self._update_deployment_using_patch_with_http_info(request)

    def _update_deployment_using_patch_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def update_node(self, request):
        """更新设备信息

        更新设备日志配置，标签以及描述。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateNode
        :type request: :class:`huaweicloudsdkhilens.v3.UpdateNodeRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.UpdateNodeResponse`
        """
        return self._update_node_with_http_info(request)

    def _update_node_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def update_node_cert(self, request):
        """更新设备证书

        设备出现离线或者证书过期时，可通过该接口更新证书，重新让设备连接到云端
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateNodeCert
        :type request: :class:`huaweicloudsdkhilens.v3.UpdateNodeCertRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.UpdateNodeCertResponse`
        """
        return self._update_node_cert_with_http_info(request)

    def _update_node_cert_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def update_node_firmware(self, request):
        """升级设备固件

        升级设备固件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateNodeFirmware
        :type request: :class:`huaweicloudsdkhilens.v3.UpdateNodeFirmwareRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.UpdateNodeFirmwareResponse`
        """
        return self._update_node_firmware_with_http_info(request)

    def _update_node_firmware_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def update_secret(self, request):
        """更新密钥

        更新密钥
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSecret
        :type request: :class:`huaweicloudsdkhilens.v3.UpdateSecretRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.UpdateSecretResponse`
        """
        return self._update_secret_with_http_info(request)

    def _update_secret_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def update_task(self, request):
        """编辑作业

        编辑作业。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTask
        :type request: :class:`huaweicloudsdkhilens.v3.UpdateTaskRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.UpdateTaskResponse`
        """
        return self._update_task_with_http_info(request)

    def _update_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def update_work_space(self, request):
        """修改工作空间

        更改工作空间信息，暂时只能更改描述
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateWorkSpace
        :type request: :class:`huaweicloudsdkhilens.v3.UpdateWorkSpaceRequest`
        :rtype: :class:`huaweicloudsdkhilens.v3.UpdateWorkSpaceResponse`
        """
        return self._update_work_space_with_http_info(request)

    def _update_work_space_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :param header_params: Header parameters to be placed in the request header.
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
            request_type=request_type)
