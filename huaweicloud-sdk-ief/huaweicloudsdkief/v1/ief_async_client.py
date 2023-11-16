# coding: utf-8

from __future__ import absolute_import

import importlib
import warnings

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest
try:
    from huaweicloudsdkcore.invoker.invoker import AsyncInvoker
except ImportError as e:
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkief'")


class IefAsyncClient(Client):
    def __init__(self):
        super(IefAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkief.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "IefAsyncClient":
                raise TypeError("client type error, support client type is IefAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

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
        http_info = self._batch_add_delete_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_add_delete_tags_async_invoker(self, request):
        http_info = self._batch_add_delete_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_add_delete_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAddDeleteTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_app_async(self, request):
        """创建应用模板

        该API用于创建一个应用模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateApp
        :type request: :class:`huaweicloudsdkief.v1.CreateAppRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateAppResponse`
        """
        http_info = self._create_app_http_info(request)
        return self._call_api(**http_info)

    def create_app_async_invoker(self, request):
        http_info = self._create_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_app_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edgemgr/apps",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_app_versions_async(self, request):
        """创建应用模板版本

        创建一个应用模板版本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAppVersions
        :type request: :class:`huaweicloudsdkief.v1.CreateAppVersionsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateAppVersionsResponse`
        """
        http_info = self._create_app_versions_http_info(request)
        return self._call_api(**http_info)

    def create_app_versions_async_invoker(self, request):
        http_info = self._create_app_versions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_app_versions_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edgemgr/apps/{app_id}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAppVersionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_batch_job_async(self, request):
        """创建批量处理任务

        创建批量处理作业。该API用于创建批量处理作业，当前支持：批量节点升级、批量应用部署、批量应用升级
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateBatchJob
        :type request: :class:`huaweicloudsdkief.v1.CreateBatchJobRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateBatchJobResponse`
        """
        http_info = self._create_batch_job_http_info(request)
        return self._call_api(**http_info)

    def create_batch_job_async_invoker(self, request):
        http_info = self._create_batch_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_batch_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/productmgr/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateBatchJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_config_map_async(self, request):
        """创建配置项

        创建配置项
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateConfigMap
        :type request: :class:`huaweicloudsdkief.v1.CreateConfigMapRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateConfigMapResponse`
        """
        http_info = self._create_config_map_http_info(request)
        return self._call_api(**http_info)

    def create_config_map_async_invoker(self, request):
        http_info = self._create_config_map_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_config_map_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edgemgr/configmaps",
            "request_type": request.__class__.__name__,
            "response_type": "CreateConfigMapResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_deployments_async(self, request):
        """创建部署

        创建部署
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDeployments
        :type request: :class:`huaweicloudsdkief.v1.CreateDeploymentsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateDeploymentsResponse`
        """
        http_info = self._create_deployments_http_info(request)
        return self._call_api(**http_info)

    def create_deployments_async_invoker(self, request):
        http_info = self._create_deployments_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_deployments_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/edgemgr/deployments",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDeploymentsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_device_async(self, request):
        """注册终端设备

        注册终端设备。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDevice
        :type request: :class:`huaweicloudsdkief.v1.CreateDeviceRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateDeviceResponse`
        """
        http_info = self._create_device_http_info(request)
        return self._call_api(**http_info)

    def create_device_async_invoker(self, request):
        http_info = self._create_device_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_device_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edgemgr/devices",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_device_template_async(self, request):
        """创建终端设备模板

        创建一个终端设备模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDeviceTemplate
        :type request: :class:`huaweicloudsdkief.v1.CreateDeviceTemplateRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateDeviceTemplateResponse`
        """
        http_info = self._create_device_template_http_info(request)
        return self._call_api(**http_info)

    def create_device_template_async_invoker(self, request):
        http_info = self._create_device_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_device_template_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edgemgr/device-templates",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDeviceTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_edge_group_async(self, request):
        """边缘节点组管理

        创建边缘节点组。该API只能在铂金版实例中使用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEdgeGroup
        :type request: :class:`huaweicloudsdkief.v1.CreateEdgeGroupRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateEdgeGroupResponse`
        """
        http_info = self._create_edge_group_http_info(request)
        return self._call_api(**http_info)

    def create_edge_group_async_invoker(self, request):
        http_info = self._create_edge_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_edge_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edgemgr/groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEdgeGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_edge_group_cert_async(self, request):
        """创建边缘节点组证书

        创建边缘节点组证书。边缘节点组证书.tar.gz文件仅在调用该API时提供压缩包下载，请及时下载证书文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEdgeGroupCert
        :type request: :class:`huaweicloudsdkief.v1.CreateEdgeGroupCertRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateEdgeGroupCertResponse`
        """
        http_info = self._create_edge_group_cert_http_info(request)
        return self._call_api(**http_info)

    def create_edge_group_cert_async_invoker(self, request):
        http_info = self._create_edge_group_cert_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_edge_group_cert_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edgemgr/groups/{group_id}/certs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEdgeGroupCertResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_edge_node_async(self, request):
        """注册边缘节点

        该API用于注册一个边缘节点。接口调用成功后，您可以将响应消息体中node.package字段使用base64解码成tar.gz文件，并在控制台下载边缘核心软件，然后纳管边缘节点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEdgeNode
        :type request: :class:`huaweicloudsdkief.v1.CreateEdgeNodeRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateEdgeNodeResponse`
        """
        http_info = self._create_edge_node_http_info(request)
        return self._call_api(**http_info)

    def create_edge_node_async_invoker(self, request):
        http_info = self._create_edge_node_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_edge_node_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edgemgr/nodes",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEdgeNodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_edge_node_certs_async(self, request):
        """创建节点证书

        创建边缘节点上的应用证书和设备证书。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEdgeNodeCerts
        :type request: :class:`huaweicloudsdkief.v1.CreateEdgeNodeCertsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateEdgeNodeCertsResponse`
        """
        http_info = self._create_edge_node_certs_http_info(request)
        return self._call_api(**http_info)

    def create_edge_node_certs_async_invoker(self, request):
        http_info = self._create_edge_node_certs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_edge_node_certs_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edgemgr/nodes/{node_id}/certs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEdgeNodeCertsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_encryptdatas_async(self, request):
        """新增加密数据

        新增加密数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEncryptdatas
        :type request: :class:`huaweicloudsdkief.v1.CreateEncryptdatasRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateEncryptdatasResponse`
        """
        http_info = self._create_encryptdatas_http_info(request)
        return self._call_api(**http_info)

    def create_encryptdatas_async_invoker(self, request):
        http_info = self._create_encryptdatas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_encryptdatas_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edm/encryptdatas",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEncryptdatasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_endpoint_async(self, request):
        """创建端点

        创建一个端点
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEndpoint
        :type request: :class:`huaweicloudsdkief.v1.CreateEndpointRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateEndpointResponse`
        """
        http_info = self._create_endpoint_http_info(request)
        return self._call_api(**http_info)

    def create_endpoint_async_invoker(self, request):
        http_info = self._create_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_endpoint_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/routemgr/endpoints",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_node_encryptdatas_async(self, request):
        """加密数据绑定边缘节点

        加密数据绑定边缘节点
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateNodeEncryptdatas
        :type request: :class:`huaweicloudsdkief.v1.CreateNodeEncryptdatasRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateNodeEncryptdatasResponse`
        """
        http_info = self._create_node_encryptdatas_http_info(request)
        return self._call_api(**http_info)

    def create_node_encryptdatas_async_invoker(self, request):
        http_info = self._create_node_encryptdatas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_node_encryptdatas_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edm/nodes/{node_id}/encryptdatas",
            "request_type": request.__class__.__name__,
            "response_type": "CreateNodeEncryptdatasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_product_async(self, request):
        """创建批量节点注册作业

        创建批量节点注册作业。接口调用成功后，您可以将响应消息体中product.package字段使用base64解码成tar.gz产品证书文件，并在控制台下载边缘注册软件edge-register和edge-installer，使用该产品证书批量纳管边缘节点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateProduct
        :type request: :class:`huaweicloudsdkief.v1.CreateProductRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateProductResponse`
        """
        http_info = self._create_product_http_info(request)
        return self._call_api(**http_info)

    def create_product_async_invoker(self, request):
        http_info = self._create_product_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_product_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/productmgr/products",
            "request_type": request.__class__.__name__,
            "response_type": "CreateProductResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_rule_async(self, request):
        """创建规则

        创建一条规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRule
        :type request: :class:`huaweicloudsdkief.v1.CreateRuleRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateRuleResponse`
        """
        http_info = self._create_rule_http_info(request)
        return self._call_api(**http_info)

    def create_rule_async_invoker(self, request):
        http_info = self._create_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/routemgr/rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_secret_async(self, request):
        """创建密钥

        创建密钥
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSecret
        :type request: :class:`huaweicloudsdkief.v1.CreateSecretRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateSecretResponse`
        """
        http_info = self._create_secret_http_info(request)
        return self._call_api(**http_info)

    def create_secret_async_invoker(self, request):
        http_info = self._create_secret_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_secret_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edgemgr/secrets",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSecretResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_service_async(self, request):
        """创建服务

        创建一个服务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateService
        :type request: :class:`huaweicloudsdkief.v1.CreateServiceRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateServiceResponse`
        """
        http_info = self._create_service_http_info(request)
        return self._call_api(**http_info)

    def create_service_async_invoker(self, request):
        http_info = self._create_service_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_service_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edgemgr/services",
            "request_type": request.__class__.__name__,
            "response_type": "CreateServiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_system_event_async(self, request):
        """创建系统订阅

        创建系统订阅
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSystemEvent
        :type request: :class:`huaweicloudsdkief.v1.CreateSystemEventRequest`
        :rtype: :class:`huaweicloudsdkief.v1.CreateSystemEventResponse`
        """
        http_info = self._create_system_event_http_info(request)
        return self._call_api(**http_info)

    def create_system_event_async_invoker(self, request):
        http_info = self._create_system_event_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_system_event_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/routemgr/exchanger/systemevents",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSystemEventResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

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
        http_info = self._create_tag_http_info(request)
        return self._call_api(**http_info)

    def create_tag_async_invoker(self, request):
        http_info = self._create_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTagResponse"
            }

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
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_app_async(self, request):
        """删除应用模板

        删除应用模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteApp
        :type request: :class:`huaweicloudsdkief.v1.DeleteAppRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteAppResponse`
        """
        http_info = self._delete_app_http_info(request)
        return self._call_api(**http_info)

    def delete_app_async_invoker(self, request):
        http_info = self._delete_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_app_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/edgemgr/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_app_version_async(self, request):
        """删除应用版本

        删除应用版本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAppVersion
        :type request: :class:`huaweicloudsdkief.v1.DeleteAppVersionRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteAppVersionResponse`
        """
        http_info = self._delete_app_version_http_info(request)
        return self._call_api(**http_info)

    def delete_app_version_async_invoker(self, request):
        http_info = self._delete_app_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_app_version_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/edgemgr/apps/{app_id}/versions/{version_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAppVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_batch_job_async(self, request):
        """删除批量处理作业

        删除批量处理作业
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBatchJob
        :type request: :class:`huaweicloudsdkief.v1.DeleteBatchJobRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteBatchJobResponse`
        """
        http_info = self._delete_batch_job_http_info(request)
        return self._call_api(**http_info)

    def delete_batch_job_async_invoker(self, request):
        http_info = self._delete_batch_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_batch_job_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/productmgr/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBatchJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_config_map_async(self, request):
        """删除配置项

        删除配置项
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteConfigMap
        :type request: :class:`huaweicloudsdkief.v1.DeleteConfigMapRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteConfigMapResponse`
        """
        http_info = self._delete_config_map_http_info(request)
        return self._call_api(**http_info)

    def delete_config_map_async_invoker(self, request):
        http_info = self._delete_config_map_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_config_map_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/edgemgr/configmaps/{configmap_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteConfigMapResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_deployment_async(self, request):
        """删除部署

        删除应用部署
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDeployment
        :type request: :class:`huaweicloudsdkief.v1.DeleteDeploymentRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteDeploymentResponse`
        """
        http_info = self._delete_deployment_http_info(request)
        return self._call_api(**http_info)

    def delete_deployment_async_invoker(self, request):
        http_info = self._delete_deployment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_deployment_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/edgemgr/deployments/{deployment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDeploymentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_device_async(self, request):
        """删除终端设备

        该API用于删除终端设备。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDevice
        :type request: :class:`huaweicloudsdkief.v1.DeleteDeviceRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteDeviceResponse`
        """
        http_info = self._delete_device_http_info(request)
        return self._call_api(**http_info)

    def delete_device_async_invoker(self, request):
        http_info = self._delete_device_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_device_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/edgemgr/devices/{device_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_device_template_async(self, request):
        """删除终端设备模板

        删除终端设备模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDeviceTemplate
        :type request: :class:`huaweicloudsdkief.v1.DeleteDeviceTemplateRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteDeviceTemplateResponse`
        """
        http_info = self._delete_device_template_http_info(request)
        return self._call_api(**http_info)

    def delete_device_template_async_invoker(self, request):
        http_info = self._delete_device_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_device_template_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/edgemgr/device-templates/{device_template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDeviceTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_edge_group_async(self, request):
        """删除边缘节点组

        删除边缘节点组。该API只能在铂金版实例中使用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEdgeGroup
        :type request: :class:`huaweicloudsdkief.v1.DeleteEdgeGroupRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteEdgeGroupResponse`
        """
        http_info = self._delete_edge_group_http_info(request)
        return self._call_api(**http_info)

    def delete_edge_group_async_invoker(self, request):
        http_info = self._delete_edge_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_edge_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/edgemgr/groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEdgeGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_edge_group_cert_async(self, request):
        """删除边缘节点组证书

        删除边缘节点组证书
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEdgeGroupCert
        :type request: :class:`huaweicloudsdkief.v1.DeleteEdgeGroupCertRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteEdgeGroupCertResponse`
        """
        http_info = self._delete_edge_group_cert_http_info(request)
        return self._call_api(**http_info)

    def delete_edge_group_cert_async_invoker(self, request):
        http_info = self._delete_edge_group_cert_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_edge_group_cert_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/edgemgr/groups/{group_id}/certs/{group_cert_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEdgeGroupCertResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_edge_node_async(self, request):
        """删除边缘节点

        删除边缘节点
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEdgeNode
        :type request: :class:`huaweicloudsdkief.v1.DeleteEdgeNodeRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteEdgeNodeResponse`
        """
        http_info = self._delete_edge_node_http_info(request)
        return self._call_api(**http_info)

    def delete_edge_node_async_invoker(self, request):
        http_info = self._delete_edge_node_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_edge_node_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/edgemgr/nodes/{node_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEdgeNodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_edge_node_certs_async(self, request):
        """删除节点证书

        删除边缘节点上的证书（目前只支持删除应用证书和设备证书）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEdgeNodeCerts
        :type request: :class:`huaweicloudsdkief.v1.DeleteEdgeNodeCertsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteEdgeNodeCertsResponse`
        """
        http_info = self._delete_edge_node_certs_http_info(request)
        return self._call_api(**http_info)

    def delete_edge_node_certs_async_invoker(self, request):
        http_info = self._delete_edge_node_certs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_edge_node_certs_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/edgemgr/nodes/{node_id}/certs/{cert_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEdgeNodeCertsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_encryptdatas_async(self, request):
        """删除加密数据

        删除加密数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEncryptdatas
        :type request: :class:`huaweicloudsdkief.v1.DeleteEncryptdatasRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteEncryptdatasResponse`
        """
        http_info = self._delete_encryptdatas_http_info(request)
        return self._call_api(**http_info)

    def delete_encryptdatas_async_invoker(self, request):
        http_info = self._delete_encryptdatas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_encryptdatas_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/edm/encryptdatas/{encryptdata_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEncryptdatasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_end_point_async(self, request):
        """删除一个端点

        删除一个端点
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEndPoint
        :type request: :class:`huaweicloudsdkief.v1.DeleteEndPointRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteEndPointResponse`
        """
        http_info = self._delete_end_point_http_info(request)
        return self._call_api(**http_info)

    def delete_end_point_async_invoker(self, request):
        http_info = self._delete_end_point_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_end_point_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/routemgr/endpoints/{endpoint_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEndPointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_node_encryptdatas_async(self, request):
        """解绑边缘节点的加密数据

        解绑边缘节点的加密数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteNodeEncryptdatas
        :type request: :class:`huaweicloudsdkief.v1.DeleteNodeEncryptdatasRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteNodeEncryptdatasResponse`
        """
        http_info = self._delete_node_encryptdatas_http_info(request)
        return self._call_api(**http_info)

    def delete_node_encryptdatas_async_invoker(self, request):
        http_info = self._delete_node_encryptdatas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_node_encryptdatas_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/edm/nodes/{node_id}/encryptdatas/{encryptdata_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNodeEncryptdatasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_product_async(self, request):
        """删除批量节点注册作业

        删除批量节点注册作业。接口调用成功后，与该批量注册任务关联的批量注册凭证将会失效
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteProduct
        :type request: :class:`huaweicloudsdkief.v1.DeleteProductRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteProductResponse`
        """
        http_info = self._delete_product_http_info(request)
        return self._call_api(**http_info)

    def delete_product_async_invoker(self, request):
        http_info = self._delete_product_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_product_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/productmgr/products/{product_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteProductResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_resource_tag_async(self, request):
        """删除资源标签

        删除资源标签。删除时不对标签字符集做校验，调用前必须要做encodeURI，服务端需要对接口uri做decodeURI。删除的key不存在报404，Key不能为空或者空字符串。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteResourceTag
        :type request: :class:`huaweicloudsdkief.v1.DeleteResourceTagRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteResourceTagResponse`
        """
        http_info = self._delete_resource_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_resource_tag_async_invoker(self, request):
        http_info = self._delete_resource_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_resource_tag_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/tags/{key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteResourceTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_rule_async(self, request):
        """删除规则

        删除一条规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRule
        :type request: :class:`huaweicloudsdkief.v1.DeleteRuleRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteRuleResponse`
        """
        http_info = self._delete_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_rule_async_invoker(self, request):
        http_info = self._delete_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/routemgr/rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_secret_async(self, request):
        """删除密钥

        删除密钥
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSecret
        :type request: :class:`huaweicloudsdkief.v1.DeleteSecretRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteSecretResponse`
        """
        http_info = self._delete_secret_http_info(request)
        return self._call_api(**http_info)

    def delete_secret_async_invoker(self, request):
        http_info = self._delete_secret_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_secret_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/edgemgr/secrets/{secret_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSecretResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_service_async(self, request):
        """删除服务

        删除一个服务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteService
        :type request: :class:`huaweicloudsdkief.v1.DeleteServiceRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteServiceResponse`
        """
        http_info = self._delete_service_http_info(request)
        return self._call_api(**http_info)

    def delete_service_async_invoker(self, request):
        http_info = self._delete_service_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_service_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/edgemgr/services/{service_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteServiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_system_event_async(self, request):
        """删除系统订阅列表

        删除系统订阅列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSystemEvent
        :type request: :class:`huaweicloudsdkief.v1.DeleteSystemEventRequest`
        :rtype: :class:`huaweicloudsdkief.v1.DeleteSystemEventResponse`
        """
        http_info = self._delete_system_event_http_info(request)
        return self._call_api(**http_info)

    def delete_system_event_async_invoker(self, request):
        http_info = self._delete_system_event_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_system_event_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/routemgr/exchanger/systemevents/{event_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSystemEventResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def enable_disable_edge_nodes_async(self, request):
        """启用停用边缘节点

        启用停用边缘节点。被停用的边缘节点将无法连接到云端服务，可用该URI启用边缘节点恢复连接。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableDisableEdgeNodes
        :type request: :class:`huaweicloudsdkief.v1.EnableDisableEdgeNodesRequest`
        :rtype: :class:`huaweicloudsdkief.v1.EnableDisableEdgeNodesResponse`
        """
        http_info = self._enable_disable_edge_nodes_http_info(request)
        return self._call_api(**http_info)

    def enable_disable_edge_nodes_async_invoker(self, request):
        http_info = self._enable_disable_edge_nodes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _enable_disable_edge_nodes_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edgemgr/nodes/{node_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "EnableDisableEdgeNodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_app_versions_async(self, request):
        """查询应用模板版本列表

        查询应用模板版本列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppVersions
        :type request: :class:`huaweicloudsdkief.v1.ListAppVersionsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListAppVersionsResponse`
        """
        http_info = self._list_app_versions_http_info(request)
        return self._call_api(**http_info)

    def list_app_versions_async_invoker(self, request):
        http_info = self._list_app_versions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_app_versions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edgemgr/apps/{app_id}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppVersionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_apps_async(self, request):
        """查询应用模板列表

        查询应用模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApps
        :type request: :class:`huaweicloudsdkief.v1.ListAppsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListAppsResponse`
        """
        http_info = self._list_apps_http_info(request)
        return self._call_api(**http_info)

    def list_apps_async_invoker(self, request):
        http_info = self._list_apps_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_apps_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edgemgr/apps",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_batch_job_async(self, request):
        """查询批量处理作业列表

        查询批量处理作业列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBatchJob
        :type request: :class:`huaweicloudsdkief.v1.ListBatchJobRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListBatchJobResponse`
        """
        http_info = self._list_batch_job_http_info(request)
        return self._call_api(**http_info)

    def list_batch_job_async_invoker(self, request):
        http_info = self._list_batch_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_batch_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/productmgr/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListBatchJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_config_maps_async(self, request):
        """查询配置项列表

        查询配置项列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConfigMaps
        :type request: :class:`huaweicloudsdkief.v1.ListConfigMapsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListConfigMapsResponse`
        """
        http_info = self._list_config_maps_http_info(request)
        return self._call_api(**http_info)

    def list_config_maps_async_invoker(self, request):
        http_info = self._list_config_maps_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_config_maps_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edgemgr/configmaps",
            "request_type": request.__class__.__name__,
            "response_type": "ListConfigMapsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_deployments_async(self, request):
        """查询部署列表

        查询部署列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDeployments
        :type request: :class:`huaweicloudsdkief.v1.ListDeploymentsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListDeploymentsResponse`
        """
        http_info = self._list_deployments_http_info(request)
        return self._call_api(**http_info)

    def list_deployments_async_invoker(self, request):
        http_info = self._list_deployments_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_deployments_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/edgemgr/deployments",
            "request_type": request.__class__.__name__,
            "response_type": "ListDeploymentsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_device_templates_async(self, request):
        """查询终端设备模板列表

        查询终端设备模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDeviceTemplates
        :type request: :class:`huaweicloudsdkief.v1.ListDeviceTemplatesRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListDeviceTemplatesResponse`
        """
        http_info = self._list_device_templates_http_info(request)
        return self._call_api(**http_info)

    def list_device_templates_async_invoker(self, request):
        http_info = self._list_device_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_device_templates_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edgemgr/device-templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListDeviceTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_devices_async(self, request):
        """查询终端设备列表

        该API用于查询终端设备列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDevices
        :type request: :class:`huaweicloudsdkief.v1.ListDevicesRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListDevicesResponse`
        """
        http_info = self._list_devices_http_info(request)
        return self._call_api(**http_info)

    def list_devices_async_invoker(self, request):
        http_info = self._list_devices_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_devices_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edgemgr/devices",
            "request_type": request.__class__.__name__,
            "response_type": "ListDevicesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_edge_group_certs_async(self, request):
        """查询边缘节点组证书列表

        查询边缘节点组证书列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEdgeGroupCerts
        :type request: :class:`huaweicloudsdkief.v1.ListEdgeGroupCertsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListEdgeGroupCertsResponse`
        """
        http_info = self._list_edge_group_certs_http_info(request)
        return self._call_api(**http_info)

    def list_edge_group_certs_async_invoker(self, request):
        http_info = self._list_edge_group_certs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_edge_group_certs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edgemgr/groups/{group_id}/certs",
            "request_type": request.__class__.__name__,
            "response_type": "ListEdgeGroupCertsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_edge_groups_async(self, request):
        """查询边缘节点组列表

        查询边缘节点组列表。该API只能在铂金版实例中使用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEdgeGroups
        :type request: :class:`huaweicloudsdkief.v1.ListEdgeGroupsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListEdgeGroupsResponse`
        """
        http_info = self._list_edge_groups_http_info(request)
        return self._call_api(**http_info)

    def list_edge_groups_async_invoker(self, request):
        http_info = self._list_edge_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_edge_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edgemgr/groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListEdgeGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_edge_node_certs_async(self, request):
        """查询节点证书

        查询边缘节点上的应用证书和设备证书。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEdgeNodeCerts
        :type request: :class:`huaweicloudsdkief.v1.ListEdgeNodeCertsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListEdgeNodeCertsResponse`
        """
        http_info = self._list_edge_node_certs_http_info(request)
        return self._call_api(**http_info)

    def list_edge_node_certs_async_invoker(self, request):
        http_info = self._list_edge_node_certs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_edge_node_certs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edgemgr/nodes/{node_id}/certs",
            "request_type": request.__class__.__name__,
            "response_type": "ListEdgeNodeCertsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

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
        http_info = self._list_edge_nodes_http_info(request)
        return self._call_api(**http_info)

    def list_edge_nodes_async_invoker(self, request):
        http_info = self._list_edge_nodes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_edge_nodes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edgemgr/nodes",
            "request_type": request.__class__.__name__,
            "response_type": "ListEdgeNodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_encryptdata_nodes_async(self, request):
        """获取加密数据绑定的边缘节点

        获取加密数据绑定的边缘节点
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEncryptdataNodes
        :type request: :class:`huaweicloudsdkief.v1.ListEncryptdataNodesRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListEncryptdataNodesResponse`
        """
        http_info = self._list_encryptdata_nodes_http_info(request)
        return self._call_api(**http_info)

    def list_encryptdata_nodes_async_invoker(self, request):
        http_info = self._list_encryptdata_nodes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_encryptdata_nodes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edm/encryptdatas/{encryptdata_id}/nodes",
            "request_type": request.__class__.__name__,
            "response_type": "ListEncryptdataNodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_encryptdatas_async(self, request):
        """获取加密数据列表

        获取加密数据列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEncryptdatas
        :type request: :class:`huaweicloudsdkief.v1.ListEncryptdatasRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListEncryptdatasResponse`
        """
        http_info = self._list_encryptdatas_http_info(request)
        return self._call_api(**http_info)

    def list_encryptdatas_async_invoker(self, request):
        http_info = self._list_encryptdatas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_encryptdatas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edm/encryptdatas",
            "request_type": request.__class__.__name__,
            "response_type": "ListEncryptdatasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

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
        http_info = self._list_endpoints_http_info(request)
        return self._call_api(**http_info)

    def list_endpoints_async_invoker(self, request):
        http_info = self._list_endpoints_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_endpoints_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/routemgr/endpoints",
            "request_type": request.__class__.__name__,
            "response_type": "ListEndpointsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_node_encryptdatas_async(self, request):
        """获取边缘节点绑定的加密数据

        获取边缘节点绑定的加密数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNodeEncryptdatas
        :type request: :class:`huaweicloudsdkief.v1.ListNodeEncryptdatasRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListNodeEncryptdatasResponse`
        """
        http_info = self._list_node_encryptdatas_http_info(request)
        return self._call_api(**http_info)

    def list_node_encryptdatas_async_invoker(self, request):
        http_info = self._list_node_encryptdatas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_node_encryptdatas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edm/nodes/{node_id}/encryptdatas",
            "request_type": request.__class__.__name__,
            "response_type": "ListNodeEncryptdatasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_pods_async(self, request):
        """查询应用实例列表

        查询应用实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPods
        :type request: :class:`huaweicloudsdkief.v1.ListPodsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListPodsResponse`
        """
        http_info = self._list_pods_http_info(request)
        return self._call_api(**http_info)

    def list_pods_async_invoker(self, request):
        http_info = self._list_pods_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_pods_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/edgemgr/pods",
            "request_type": request.__class__.__name__,
            "response_type": "ListPodsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        if 'plugin_instance_name' in local_var_params:
            query_params.append(('plugin_instance_name', local_var_params['plugin_instance_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_products_async(self, request):
        """查询批量节点注册作业列表

        查询批量节点注册作业列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProducts
        :type request: :class:`huaweicloudsdkief.v1.ListProductsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListProductsResponse`
        """
        http_info = self._list_products_http_info(request)
        return self._call_api(**http_info)

    def list_products_async_invoker(self, request):
        http_info = self._list_products_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_products_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/productmgr/products",
            "request_type": request.__class__.__name__,
            "response_type": "ListProductsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_resource_by_tags_async(self, request):
        """查询资源实例

        使用标签过滤实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResourceByTags
        :type request: :class:`huaweicloudsdkief.v1.ListResourceByTagsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListResourceByTagsResponse`
        """
        http_info = self._list_resource_by_tags_http_info(request)
        return self._call_api(**http_info)

    def list_resource_by_tags_async_invoker(self, request):
        http_info = self._list_resource_by_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_resource_by_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{resource_type}/resource_instances/action",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceByTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_rule_errors_async(self, request):
        """查询规则错误列表

        查询特定规则下的所有错误列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRuleErrors
        :type request: :class:`huaweicloudsdkief.v1.ListRuleErrorsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListRuleErrorsResponse`
        """
        http_info = self._list_rule_errors_http_info(request)
        return self._call_api(**http_info)

    def list_rule_errors_async_invoker(self, request):
        http_info = self._list_rule_errors_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_rule_errors_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/routemgr/rules/{rule_id}/errors",
            "request_type": request.__class__.__name__,
            "response_type": "ListRuleErrorsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_rules_async(self, request):
        """查询规则列表

        查询到所有的规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRules
        :type request: :class:`huaweicloudsdkief.v1.ListRulesRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListRulesResponse`
        """
        http_info = self._list_rules_http_info(request)
        return self._call_api(**http_info)

    def list_rules_async_invoker(self, request):
        http_info = self._list_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/routemgr/rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_secrets_async(self, request):
        """查询密钥列表

        查询密钥列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSecrets
        :type request: :class:`huaweicloudsdkief.v1.ListSecretsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListSecretsResponse`
        """
        http_info = self._list_secrets_http_info(request)
        return self._call_api(**http_info)

    def list_secrets_async_invoker(self, request):
        http_info = self._list_secrets_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_secrets_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edgemgr/secrets",
            "request_type": request.__class__.__name__,
            "response_type": "ListSecretsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_services_async(self, request):
        """查询服务列表

        获取所有的服务详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServices
        :type request: :class:`huaweicloudsdkief.v1.ListServicesRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListServicesResponse`
        """
        http_info = self._list_services_http_info(request)
        return self._call_api(**http_info)

    def list_services_async_invoker(self, request):
        http_info = self._list_services_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_services_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edgemgr/services",
            "request_type": request.__class__.__name__,
            "response_type": "ListServicesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_system_events_async(self, request):
        """查询系统订阅列表

        查询系统订阅列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSystemEvents
        :type request: :class:`huaweicloudsdkief.v1.ListSystemEventsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListSystemEventsResponse`
        """
        http_info = self._list_system_events_http_info(request)
        return self._call_api(**http_info)

    def list_system_events_async_invoker(self, request):
        http_info = self._list_system_events_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_system_events_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/routemgr/exchanger/systemevents",
            "request_type": request.__class__.__name__,
            "response_type": "ListSystemEventsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_tags_async(self, request):
        """查询资源标签

        查询指定实例的标签信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTags
        :type request: :class:`huaweicloudsdkief.v1.ListTagsRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListTagsResponse`
        """
        http_info = self._list_tags_http_info(request)
        return self._call_api(**http_info)

    def list_tags_async_invoker(self, request):
        http_info = self._list_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListTagsResponse"
            }

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
        if 'ief_instance_id' in local_var_params:
            header_params['ief-instance-id'] = local_var_params['ief_instance_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_tags_by_resource_type_async(self, request):
        """查询项目标签

        查询指定项目中实例类型的所有资源标签集合
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTagsByResourceType
        :type request: :class:`huaweicloudsdkief.v1.ListTagsByResourceTypeRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ListTagsByResourceTypeResponse`
        """
        http_info = self._list_tags_by_resource_type_http_info(request)
        return self._call_api(**http_info)

    def list_tags_by_resource_type_async_invoker(self, request):
        http_info = self._list_tags_by_resource_type_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tags_by_resource_type_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/{resource_type}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListTagsByResourceTypeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def restart_deployments_pod_async(self, request):
        """容器应用实例重启

        重启部署下的应用实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestartDeploymentsPod
        :type request: :class:`huaweicloudsdkief.v1.RestartDeploymentsPodRequest`
        :rtype: :class:`huaweicloudsdkief.v1.RestartDeploymentsPodResponse`
        """
        http_info = self._restart_deployments_pod_http_info(request)
        return self._call_api(**http_info)

    def restart_deployments_pod_async_invoker(self, request):
        http_info = self._restart_deployments_pod_http_info(request)
        return AsyncInvoker(self, http_info)

    def _restart_deployments_pod_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/edgemgr/deployments/{deployment_id}/pods/{pod_name}/restart",
            "request_type": request.__class__.__name__,
            "response_type": "RestartDeploymentsPodResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def restore_batch_job_async(self, request):
        """继续批量处理作业

        继续执行批量处理作业。该API只对停止的批量处理作业生效
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestoreBatchJob
        :type request: :class:`huaweicloudsdkief.v1.RestoreBatchJobRequest`
        :rtype: :class:`huaweicloudsdkief.v1.RestoreBatchJobResponse`
        """
        http_info = self._restore_batch_job_http_info(request)
        return self._call_api(**http_info)

    def restore_batch_job_async_invoker(self, request):
        http_info = self._restore_batch_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _restore_batch_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/productmgr/jobs/{job_id}/restore",
            "request_type": request.__class__.__name__,
            "response_type": "RestoreBatchJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def retry_batch_job_async(self, request):
        """重试批量处理作业

        重试批量处理作业。该API仅对执行状态失败的批量处理作业生效
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RetryBatchJob
        :type request: :class:`huaweicloudsdkief.v1.RetryBatchJobRequest`
        :rtype: :class:`huaweicloudsdkief.v1.RetryBatchJobResponse`
        """
        http_info = self._retry_batch_job_http_info(request)
        return self._call_api(**http_info)

    def retry_batch_job_async_invoker(self, request):
        http_info = self._retry_batch_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _retry_batch_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/productmgr/jobs/{job_id}/retry",
            "request_type": request.__class__.__name__,
            "response_type": "RetryBatchJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_app_detail_async(self, request):
        """查询应用模板详情

        查询应用模板详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAppDetail
        :type request: :class:`huaweicloudsdkief.v1.ShowAppDetailRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowAppDetailResponse`
        """
        http_info = self._show_app_detail_http_info(request)
        return self._call_api(**http_info)

    def show_app_detail_async_invoker(self, request):
        http_info = self._show_app_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_app_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edgemgr/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_app_version_detail_async(self, request):
        """查询应用模板版本详情

        查询应用模板版本详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAppVersionDetail
        :type request: :class:`huaweicloudsdkief.v1.ShowAppVersionDetailRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowAppVersionDetailResponse`
        """
        http_info = self._show_app_version_detail_http_info(request)
        return self._call_api(**http_info)

    def show_app_version_detail_async_invoker(self, request):
        http_info = self._show_app_version_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_app_version_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edgemgr/apps/{app_id}/versions/{version_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppVersionDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_batch_job_async(self, request):
        """查询批量处理作业详情

        查询批量处理作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBatchJob
        :type request: :class:`huaweicloudsdkief.v1.ShowBatchJobRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowBatchJobResponse`
        """
        http_info = self._show_batch_job_http_info(request)
        return self._call_api(**http_info)

    def show_batch_job_async_invoker(self, request):
        http_info = self._show_batch_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_batch_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/productmgr/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBatchJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_config_map_async(self, request):
        """查询配置项详情

        查询一个配置项详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowConfigMap
        :type request: :class:`huaweicloudsdkief.v1.ShowConfigMapRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowConfigMapResponse`
        """
        http_info = self._show_config_map_http_info(request)
        return self._call_api(**http_info)

    def show_config_map_async_invoker(self, request):
        http_info = self._show_config_map_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_config_map_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edgemgr/configmaps/{configmap_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConfigMapResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_deployment_async(self, request):
        """查询应用部署

        查询应用部署
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDeployment
        :type request: :class:`huaweicloudsdkief.v1.ShowDeploymentRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowDeploymentResponse`
        """
        http_info = self._show_deployment_http_info(request)
        return self._call_api(**http_info)

    def show_deployment_async_invoker(self, request):
        http_info = self._show_deployment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_deployment_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/edgemgr/deployments/{deployment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeploymentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_device_async(self, request):
        """查询终端设备详情

        该API用于查询终端设备详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDevice
        :type request: :class:`huaweicloudsdkief.v1.ShowDeviceRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowDeviceResponse`
        """
        http_info = self._show_device_http_info(request)
        return self._call_api(**http_info)

    def show_device_async_invoker(self, request):
        http_info = self._show_device_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_device_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edgemgr/devices/{device_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_device_template_async(self, request):
        """查询终端设备模板

        查询一个终端设备模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDeviceTemplate
        :type request: :class:`huaweicloudsdkief.v1.ShowDeviceTemplateRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowDeviceTemplateResponse`
        """
        http_info = self._show_device_template_http_info(request)
        return self._call_api(**http_info)

    def show_device_template_async_invoker(self, request):
        http_info = self._show_device_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_device_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edgemgr/device-templates/{device_template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeviceTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_device_twin_async(self, request):
        """查询终端设备孪生

        该API用于查询终端设备孪生。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDeviceTwin
        :type request: :class:`huaweicloudsdkief.v1.ShowDeviceTwinRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowDeviceTwinResponse`
        """
        http_info = self._show_device_twin_http_info(request)
        return self._call_api(**http_info)

    def show_device_twin_async_invoker(self, request):
        http_info = self._show_device_twin_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_device_twin_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edgemgr/devices/{device_id}/twin",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeviceTwinResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_edge_group_cert_detail_async(self, request):
        """查询边缘节点组证书详情

        查询边缘节点组证书详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEdgeGroupCertDetail
        :type request: :class:`huaweicloudsdkief.v1.ShowEdgeGroupCertDetailRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowEdgeGroupCertDetailResponse`
        """
        http_info = self._show_edge_group_cert_detail_http_info(request)
        return self._call_api(**http_info)

    def show_edge_group_cert_detail_async_invoker(self, request):
        http_info = self._show_edge_group_cert_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_edge_group_cert_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edgemgr/groups/{group_id}/certs/{group_cert_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEdgeGroupCertDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_edge_group_detail_async(self, request):
        """查询边缘节点组详情

        查询边缘节点组详情。该API只能在铂金版实例中使用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEdgeGroupDetail
        :type request: :class:`huaweicloudsdkief.v1.ShowEdgeGroupDetailRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowEdgeGroupDetailResponse`
        """
        http_info = self._show_edge_group_detail_http_info(request)
        return self._call_api(**http_info)

    def show_edge_group_detail_async_invoker(self, request):
        http_info = self._show_edge_group_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_edge_group_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edgemgr/groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEdgeGroupDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_edge_node_detail_async(self, request):
        """查询边缘节点详情

        查询边缘节点详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEdgeNodeDetail
        :type request: :class:`huaweicloudsdkief.v1.ShowEdgeNodeDetailRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowEdgeNodeDetailResponse`
        """
        http_info = self._show_edge_node_detail_http_info(request)
        return self._call_api(**http_info)

    def show_edge_node_detail_async_invoker(self, request):
        http_info = self._show_edge_node_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_edge_node_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edgemgr/nodes/{node_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEdgeNodeDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_encryptdatas_async(self, request):
        """查询加密数据详情

        查询加密数据详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEncryptdatas
        :type request: :class:`huaweicloudsdkief.v1.ShowEncryptdatasRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowEncryptdatasResponse`
        """
        http_info = self._show_encryptdatas_http_info(request)
        return self._call_api(**http_info)

    def show_encryptdatas_async_invoker(self, request):
        http_info = self._show_encryptdatas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_encryptdatas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edm/encryptdatas/{encryptdata_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEncryptdatasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_end_point_detail_async(self, request):
        """查询端点详情

        查询一个端点的详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEndPointDetail
        :type request: :class:`huaweicloudsdkief.v1.ShowEndPointDetailRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowEndPointDetailResponse`
        """
        http_info = self._show_end_point_detail_http_info(request)
        return self._call_api(**http_info)

    def show_end_point_detail_async_invoker(self, request):
        http_info = self._show_end_point_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_end_point_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/routemgr/endpoints/{endpoint_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEndPointDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_product_detail_async(self, request):
        """查询批量节点注册作业详情

        查询批量节点注册作业详情。该接口无法查询产品证书文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProductDetail
        :type request: :class:`huaweicloudsdkief.v1.ShowProductDetailRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowProductDetailResponse`
        """
        http_info = self._show_product_detail_http_info(request)
        return self._call_api(**http_info)

    def show_product_detail_async_invoker(self, request):
        http_info = self._show_product_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_product_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/productmgr/products/{product_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProductDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_quota_async(self, request):
        """查询IEF服务下的资源配额

        查询IEF服务下的资源配额
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowQuota
        :type request: :class:`huaweicloudsdkief.v1.ShowQuotaRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowQuotaResponse`
        """
        http_info = self._show_quota_http_info(request)
        return self._call_api(**http_info)

    def show_quota_async_invoker(self, request):
        http_info = self._show_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edgemgr/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowQuotaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'types' in local_var_params:
            query_params.append(('types', local_var_params['types']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_rule_detail_async(self, request):
        """查询规则详情

        获取一条规则的详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRuleDetail
        :type request: :class:`huaweicloudsdkief.v1.ShowRuleDetailRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowRuleDetailResponse`
        """
        http_info = self._show_rule_detail_http_info(request)
        return self._call_api(**http_info)

    def show_rule_detail_async_invoker(self, request):
        http_info = self._show_rule_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_rule_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/routemgr/rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRuleDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_secret_async(self, request):
        """查询密钥详情

        查询一个密钥详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSecret
        :type request: :class:`huaweicloudsdkief.v1.ShowSecretRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowSecretResponse`
        """
        http_info = self._show_secret_http_info(request)
        return self._call_api(**http_info)

    def show_secret_async_invoker(self, request):
        http_info = self._show_secret_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_secret_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edgemgr/secrets/{secret_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSecretResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_service_detail_async(self, request):
        """查询服务详情

        查询一个服务的详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServiceDetail
        :type request: :class:`huaweicloudsdkief.v1.ShowServiceDetailRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowServiceDetailResponse`
        """
        http_info = self._show_service_detail_http_info(request)
        return self._call_api(**http_info)

    def show_service_detail_async_invoker(self, request):
        http_info = self._show_service_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_service_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edgemgr/services/{service_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowServiceDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_system_event_detail_async(self, request):
        """查询系统订阅列表

        查询系统订阅列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSystemEventDetail
        :type request: :class:`huaweicloudsdkief.v1.ShowSystemEventDetailRequest`
        :rtype: :class:`huaweicloudsdkief.v1.ShowSystemEventDetailResponse`
        """
        http_info = self._show_system_event_detail_http_info(request)
        return self._call_api(**http_info)

    def show_system_event_detail_async_invoker(self, request):
        http_info = self._show_system_event_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_system_event_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/routemgr/exchanger/systemevents/{event_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSystemEventDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def start_rule_async(self, request):
        """启用规则

        启用一条规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartRule
        :type request: :class:`huaweicloudsdkief.v1.StartRuleRequest`
        :rtype: :class:`huaweicloudsdkief.v1.StartRuleResponse`
        """
        http_info = self._start_rule_http_info(request)
        return self._call_api(**http_info)

    def start_rule_async_invoker(self, request):
        http_info = self._start_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/routemgr/rules/{rule_id}/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def start_system_event_async(self, request):
        """启用系统订阅

        启用系统订阅
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartSystemEvent
        :type request: :class:`huaweicloudsdkief.v1.StartSystemEventRequest`
        :rtype: :class:`huaweicloudsdkief.v1.StartSystemEventResponse`
        """
        http_info = self._start_system_event_http_info(request)
        return self._call_api(**http_info)

    def start_system_event_async_invoker(self, request):
        http_info = self._start_system_event_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_system_event_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/routemgr/exchanger/systemevents/{event_id}/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartSystemEventResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def stop_batch_job_async(self, request):
        """停止批量处理作业

        停止批量处理作业。该API仅对运行中的批量处理作业生效
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopBatchJob
        :type request: :class:`huaweicloudsdkief.v1.StopBatchJobRequest`
        :rtype: :class:`huaweicloudsdkief.v1.StopBatchJobResponse`
        """
        http_info = self._stop_batch_job_http_info(request)
        return self._call_api(**http_info)

    def stop_batch_job_async_invoker(self, request):
        http_info = self._stop_batch_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_batch_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/productmgr/jobs/{job_id}/pause",
            "request_type": request.__class__.__name__,
            "response_type": "StopBatchJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def stop_rule_async(self, request):
        """停用规则

        停用一条规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopRule
        :type request: :class:`huaweicloudsdkief.v1.StopRuleRequest`
        :rtype: :class:`huaweicloudsdkief.v1.StopRuleResponse`
        """
        http_info = self._stop_rule_http_info(request)
        return self._call_api(**http_info)

    def stop_rule_async_invoker(self, request):
        http_info = self._stop_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/routemgr/rules/{rule_id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def stop_system_event_async(self, request):
        """停用系统订阅

        停用系统订阅
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopSystemEvent
        :type request: :class:`huaweicloudsdkief.v1.StopSystemEventRequest`
        :rtype: :class:`huaweicloudsdkief.v1.StopSystemEventResponse`
        """
        http_info = self._stop_system_event_http_info(request)
        return self._call_api(**http_info)

    def stop_system_event_async_invoker(self, request):
        http_info = self._stop_system_event_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_system_event_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/routemgr/exchanger/systemevents/{event_id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopSystemEventResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_app_async(self, request):
        """更新应用模板

        更新一个应用模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateApp
        :type request: :class:`huaweicloudsdkief.v1.UpdateAppRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateAppResponse`
        """
        http_info = self._update_app_http_info(request)
        return self._call_api(**http_info)

    def update_app_async_invoker(self, request):
        http_info = self._update_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_app_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/edgemgr/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_app_version_async(self, request):
        """更新应用模板版本

        更新一个应用模板版本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAppVersion
        :type request: :class:`huaweicloudsdkief.v1.UpdateAppVersionRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateAppVersionResponse`
        """
        http_info = self._update_app_version_http_info(request)
        return self._call_api(**http_info)

    def update_app_version_async_invoker(self, request):
        http_info = self._update_app_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_app_version_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/edgemgr/apps/{app_id}/versions/{version_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAppVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_config_map_async(self, request):
        """更新配置项

        更新一个配置项
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateConfigMap
        :type request: :class:`huaweicloudsdkief.v1.UpdateConfigMapRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateConfigMapResponse`
        """
        http_info = self._update_config_map_http_info(request)
        return self._call_api(**http_info)

    def update_config_map_async_invoker(self, request):
        http_info = self._update_config_map_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_config_map_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/edgemgr/configmaps/{configmap_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateConfigMapResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_deployment_async(self, request):
        """更新应用部署

        修改应用部署
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDeployment
        :type request: :class:`huaweicloudsdkief.v1.UpdateDeploymentRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateDeploymentResponse`
        """
        http_info = self._update_deployment_http_info(request)
        return self._call_api(**http_info)

    def update_deployment_async_invoker(self, request):
        http_info = self._update_deployment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_deployment_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/edgemgr/deployments/{deployment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDeploymentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_device_async(self, request):
        """更新终端设备

        更新一个终端设备。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDevice
        :type request: :class:`huaweicloudsdkief.v1.UpdateDeviceRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateDeviceResponse`
        """
        http_info = self._update_device_http_info(request)
        return self._call_api(**http_info)

    def update_device_async_invoker(self, request):
        http_info = self._update_device_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_device_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/edgemgr/devices/{device_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_device_template_by_id_async(self, request):
        """更新终端设备模板

        更新一个终端设备模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDeviceTemplateById
        :type request: :class:`huaweicloudsdkief.v1.UpdateDeviceTemplateByIdRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateDeviceTemplateByIdResponse`
        """
        http_info = self._update_device_template_by_id_http_info(request)
        return self._call_api(**http_info)

    def update_device_template_by_id_async_invoker(self, request):
        http_info = self._update_device_template_by_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_device_template_by_id_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/edgemgr/device-templates/{device_template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDeviceTemplateByIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_device_twin_async(self, request):
        """更新终端设备孪生

        该API用于更新终端设备孪生。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDeviceTwin
        :type request: :class:`huaweicloudsdkief.v1.UpdateDeviceTwinRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateDeviceTwinResponse`
        """
        http_info = self._update_device_twin_http_info(request)
        return self._call_api(**http_info)

    def update_device_twin_async_invoker(self, request):
        http_info = self._update_device_twin_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_device_twin_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/edgemgr/devices/{device_id}/twin",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDeviceTwinResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_edge_group_async(self, request):
        """更新边缘节点组

        更新边缘节点组描述。该API只能在铂金版实例中使用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEdgeGroup
        :type request: :class:`huaweicloudsdkief.v1.UpdateEdgeGroupRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateEdgeGroupResponse`
        """
        http_info = self._update_edge_group_http_info(request)
        return self._call_api(**http_info)

    def update_edge_group_async_invoker(self, request):
        http_info = self._update_edge_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_edge_group_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/edgemgr/groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEdgeGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_edge_group_node_binding_async(self, request):
        """绑定或解绑边缘节点

        边缘节点组绑定或解绑边缘节点。该API只能在铂金版实例中使用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEdgeGroupNodeBinding
        :type request: :class:`huaweicloudsdkief.v1.UpdateEdgeGroupNodeBindingRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateEdgeGroupNodeBindingResponse`
        """
        http_info = self._update_edge_group_node_binding_http_info(request)
        return self._call_api(**http_info)

    def update_edge_group_node_binding_async_invoker(self, request):
        http_info = self._update_edge_group_node_binding_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_edge_group_node_binding_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/edgemgr/groups/{group_id}/nodes",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEdgeGroupNodeBindingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_edge_node_async(self, request):
        """更新边缘节点

        该API用于更新边缘节点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEdgeNode
        :type request: :class:`huaweicloudsdkief.v1.UpdateEdgeNodeRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateEdgeNodeResponse`
        """
        http_info = self._update_edge_node_http_info(request)
        return self._call_api(**http_info)

    def update_edge_node_async_invoker(self, request):
        http_info = self._update_edge_node_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_edge_node_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/edgemgr/nodes/{node_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEdgeNodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_edge_node_device_async(self, request):
        """更新边缘节点的终端设备

        添加或删除边缘节点的终端设备
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEdgeNodeDevice
        :type request: :class:`huaweicloudsdkief.v1.UpdateEdgeNodeDeviceRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateEdgeNodeDeviceResponse`
        """
        http_info = self._update_edge_node_device_http_info(request)
        return self._call_api(**http_info)

    def update_edge_node_device_async_invoker(self, request):
        http_info = self._update_edge_node_device_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_edge_node_device_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/edgemgr/nodes/{node_id}/devices",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEdgeNodeDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_encryptdatas_async(self, request):
        """更新加密数据

        更新加密数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEncryptdatas
        :type request: :class:`huaweicloudsdkief.v1.UpdateEncryptdatasRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateEncryptdatasResponse`
        """
        http_info = self._update_encryptdatas_http_info(request)
        return self._call_api(**http_info)

    def update_encryptdatas_async_invoker(self, request):
        http_info = self._update_encryptdatas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_encryptdatas_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/edm/encryptdatas/{encryptdata_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEncryptdatasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_node_by_device_id_async(self, request):
        """更新终端设备的边缘节点

        该API用于更新终端设备的边缘节点。功能与更新边缘节点的终端设备相同，推荐使用更新边缘节点的终端设备。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateNodeByDeviceId
        :type request: :class:`huaweicloudsdkief.v1.UpdateNodeByDeviceIdRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateNodeByDeviceIdResponse`
        """
        http_info = self._update_node_by_device_id_http_info(request)
        return self._call_api(**http_info)

    def update_node_by_device_id_async_invoker(self, request):
        http_info = self._update_node_by_device_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_node_by_device_id_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/edgemgr/devices/{device_id}/nodes",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNodeByDeviceIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_secret_async(self, request):
        """更新密钥

        更新一个密钥
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSecret
        :type request: :class:`huaweicloudsdkief.v1.UpdateSecretRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateSecretResponse`
        """
        http_info = self._update_secret_http_info(request)
        return self._call_api(**http_info)

    def update_secret_async_invoker(self, request):
        http_info = self._update_secret_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_secret_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/edgemgr/secrets/{secret_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSecretResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_service_async(self, request):
        """更新服务

        更新一个服务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateService
        :type request: :class:`huaweicloudsdkief.v1.UpdateServiceRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpdateServiceResponse`
        """
        http_info = self._update_service_http_info(request)
        return self._call_api(**http_info)

    def update_service_async_invoker(self, request):
        http_info = self._update_service_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_service_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/edgemgr/services/{service_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateServiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def upgrade_edge_node_async(self, request):
        """升级边缘节点

        该API用于升级边缘节点。边缘节点将自动升级到最新的可用版本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpgradeEdgeNode
        :type request: :class:`huaweicloudsdkief.v1.UpgradeEdgeNodeRequest`
        :rtype: :class:`huaweicloudsdkief.v1.UpgradeEdgeNodeResponse`
        """
        http_info = self._upgrade_edge_node_http_info(request)
        return self._call_api(**http_info)

    def upgrade_edge_node_async_invoker(self, request):
        http_info = self._upgrade_edge_node_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upgrade_edge_node_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edgemgr/nodes/{node_id}/upgrade",
            "request_type": request.__class__.__name__,
            "response_type": "UpgradeEdgeNodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def _call_api(self, **kwargs):
        try:
            kwargs["async_request"] = True
            return self.do_http_request(**kwargs)
        except TypeError:
            import inspect
            params = inspect.signature(self.do_http_request).parameters
            http_info = {param_name: kwargs.get(param_name) for param_name in params if param_name in kwargs}
            return self.do_http_request(**http_info)

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
