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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkaidatalake'")


class AIDataLakeAsyncClient(Client):
    def __init__(self):
        super().__init__()
        self.model_package = importlib.import_module("huaweicloudsdkaidatalake.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "AIDataLakeAsyncClient":
                raise TypeError("client type error, support client type is AIDataLakeAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_v2_tenant_image_version_async(self, request):
        r"""添加自定义镜像版本

        为已有镜像添加新版本。用户通过该接口为已注册的镜像添加新的版本。此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddV2TenantImageVersion
        :type request: :class:`huaweicloudsdkaidatalake.v2.AddV2TenantImageVersionRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.AddV2TenantImageVersionResponse`
        """
        http_info = self._add_v2_tenant_image_version_http_info(request)
        return self._call_api(**http_info)

    def add_v2_tenant_image_version_async_invoker(self, request):
        http_info = self._add_v2_tenant_image_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_v2_tenant_image_version_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/images/{image_id}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "AddV2TenantImageVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

        query_params = []

        header_params = {}

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

    def attach_v2_agency_policy_async(self, request):
        r"""附加策略

        为委托附加策略。此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AttachV2AgencyPolicy
        :type request: :class:`huaweicloudsdkaidatalake.v2.AttachV2AgencyPolicyRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.AttachV2AgencyPolicyResponse`
        """
        http_info = self._attach_v2_agency_policy_http_info(request)
        return self._call_api(**http_info)

    def attach_v2_agency_policy_async_invoker(self, request):
        http_info = self._attach_v2_agency_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _attach_v2_agency_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/agencies/{agency_name}/policies",
            "request_type": request.__class__.__name__,
            "response_type": "AttachV2AgencyPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agency_name' in local_var_params:
            path_params['agency_name'] = local_var_params['agency_name']

        query_params = []

        header_params = {}

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

    def create_v2_agency_async(self, request):
        r"""创建服务委托

        创建服务委托，将指定权限策略授权给AI DataLake服务。用户可通过传入支持的委托权限策略，选择性地授予相应权限。此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateV2Agency
        :type request: :class:`huaweicloudsdkaidatalake.v2.CreateV2AgencyRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.CreateV2AgencyResponse`
        """
        http_info = self._create_v2_agency_http_info(request)
        return self._call_api(**http_info)

    def create_v2_agency_async_invoker(self, request):
        http_info = self._create_v2_agency_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_v2_agency_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/agencies",
            "request_type": request.__class__.__name__,
            "response_type": "CreateV2AgencyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def create_v2_compute_async(self, request):
        r"""创建计算资源

        创建计算资源。此接口为异步接口，可通过[查询计算资源操作记录列表](ListV2ComputeVersions.xml)接口获取操作结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateV2Compute
        :type request: :class:`huaweicloudsdkaidatalake.v2.CreateV2ComputeRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.CreateV2ComputeResponse`
        """
        http_info = self._create_v2_compute_http_info(request)
        return self._call_api(**http_info)

    def create_v2_compute_async_invoker(self, request):
        http_info = self._create_v2_compute_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_v2_compute_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/computes",
            "request_type": request.__class__.__name__,
            "response_type": "CreateV2ComputeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

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

    def create_v2_endpoint_async(self, request):
        r"""创建端点

        在工作空间下创建端点。此接口为异步接口，可通过[查询端点详情](ShowV2Endpoint.xml)接口获取操作结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateV2Endpoint
        :type request: :class:`huaweicloudsdkaidatalake.v2.CreateV2EndpointRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.CreateV2EndpointResponse`
        """
        http_info = self._create_v2_endpoint_http_info(request)
        return self._call_api(**http_info)

    def create_v2_endpoint_async_invoker(self, request):
        http_info = self._create_v2_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_v2_endpoint_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/endpoints",
            "request_type": request.__class__.__name__,
            "response_type": "CreateV2EndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

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

    def create_v2_network_async(self, request):
        r"""创建网络配置

        创建网络配置，该工作空间下的资源都将使用该网络配置。此接口是同步接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateV2Network
        :type request: :class:`huaweicloudsdkaidatalake.v2.CreateV2NetworkRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.CreateV2NetworkResponse`
        """
        http_info = self._create_v2_network_http_info(request)
        return self._call_api(**http_info)

    def create_v2_network_async_invoker(self, request):
        http_info = self._create_v2_network_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_v2_network_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/networks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateV2NetworkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

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

    def create_v2_tenant_image_snapshot_async(self, request):
        r"""创建镜像快照

        为指定镜像版本创建快照。此接口为异步接口，一个镜像版本最多创建一个快照，创建后状态为Creating，可通过[查询镜像快照列表](ListV2TenantImageSnapshots.xml)获得镜像快照创建结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateV2TenantImageSnapshot
        :type request: :class:`huaweicloudsdkaidatalake.v2.CreateV2TenantImageSnapshotRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.CreateV2TenantImageSnapshotResponse`
        """
        http_info = self._create_v2_tenant_image_snapshot_http_info(request)
        return self._call_api(**http_info)

    def create_v2_tenant_image_snapshot_async_invoker(self, request):
        http_info = self._create_v2_tenant_image_snapshot_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_v2_tenant_image_snapshot_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/images/{image_id}/versions/{version_id}/image-snapshots",
            "request_type": request.__class__.__name__,
            "response_type": "CreateV2TenantImageSnapshotResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []

        header_params = {}

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

    def create_v2_workspace_async(self, request):
        r"""创建工作空间

        创建工作空间。创建工作空间接口存在同名校验，不支持创建重复名称的工作空间，并且同一账户下最多可创建5个工作空间。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateV2Workspace
        :type request: :class:`huaweicloudsdkaidatalake.v2.CreateV2WorkspaceRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.CreateV2WorkspaceResponse`
        """
        http_info = self._create_v2_workspace_http_info(request)
        return self._call_api(**http_info)

    def create_v2_workspace_async_invoker(self, request):
        http_info = self._create_v2_workspace_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_v2_workspace_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces",
            "request_type": request.__class__.__name__,
            "response_type": "CreateV2WorkspaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def delete_v2_agency_async(self, request):
        r"""删除服务委托

        取消授权给AI DataLake服务的委托。此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteV2Agency
        :type request: :class:`huaweicloudsdkaidatalake.v2.DeleteV2AgencyRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.DeleteV2AgencyResponse`
        """
        http_info = self._delete_v2_agency_http_info(request)
        return self._call_api(**http_info)

    def delete_v2_agency_async_invoker(self, request):
        http_info = self._delete_v2_agency_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_v2_agency_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/agencies/{agency_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteV2AgencyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agency_name' in local_var_params:
            path_params['agency_name'] = local_var_params['agency_name']

        query_params = []

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

    def delete_v2_agreement_async(self, request):
        r"""删除用户签署协议

        删除用户签署的协议。此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteV2Agreement
        :type request: :class:`huaweicloudsdkaidatalake.v2.DeleteV2AgreementRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.DeleteV2AgreementResponse`
        """
        http_info = self._delete_v2_agreement_http_info(request)
        return self._call_api(**http_info)

    def delete_v2_agreement_async_invoker(self, request):
        http_info = self._delete_v2_agreement_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_v2_agreement_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/agreement",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteV2AgreementResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

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

    def delete_v2_compute_async(self, request):
        r"""删除计算资源

        删除计算资源，通过输入计算资源ID，返回操作结果。此接口为异步接口，可通过[查询计算资源操作记录列表](ListV2ComputeVersions.xml)接口获取操作结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteV2Compute
        :type request: :class:`huaweicloudsdkaidatalake.v2.DeleteV2ComputeRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.DeleteV2ComputeResponse`
        """
        http_info = self._delete_v2_compute_http_info(request)
        return self._call_api(**http_info)

    def delete_v2_compute_async_invoker(self, request):
        http_info = self._delete_v2_compute_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_v2_compute_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/workspaces/{workspace_id}/computes/{compute_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteV2ComputeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'compute_id' in local_var_params:
            path_params['compute_id'] = local_var_params['compute_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def delete_v2_endpoint_async(self, request):
        r"""删除端点

        删除端点。此接口为异步接口，可通过[查询端点详情](ShowV2Endpoint.xml)接口获取操作结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteV2Endpoint
        :type request: :class:`huaweicloudsdkaidatalake.v2.DeleteV2EndpointRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.DeleteV2EndpointResponse`
        """
        http_info = self._delete_v2_endpoint_http_info(request)
        return self._call_api(**http_info)

    def delete_v2_endpoint_async_invoker(self, request):
        http_info = self._delete_v2_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_v2_endpoint_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/workspaces/{workspace_id}/endpoints/{endpoint_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteV2EndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'endpoint_id' in local_var_params:
            path_params['endpoint_id'] = local_var_params['endpoint_id']

        query_params = []
        if 'force' in local_var_params:
            query_params.append(('force', local_var_params['force']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def delete_v2_tenant_image_async(self, request):
        r"""删除镜像下所有版本

        删除指定镜像下的所有版本。此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteV2TenantImage
        :type request: :class:`huaweicloudsdkaidatalake.v2.DeleteV2TenantImageRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.DeleteV2TenantImageResponse`
        """
        http_info = self._delete_v2_tenant_image_http_info(request)
        return self._call_api(**http_info)

    def delete_v2_tenant_image_async_invoker(self, request):
        http_info = self._delete_v2_tenant_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_v2_tenant_image_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/images/{image_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteV2TenantImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

        query_params = []

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

    def delete_v2_tenant_image_snapshot_async(self, request):
        r"""删除镜像快照

        删除指定的镜像快照。创建中的快照不允许删除。此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteV2TenantImageSnapshot
        :type request: :class:`huaweicloudsdkaidatalake.v2.DeleteV2TenantImageSnapshotRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.DeleteV2TenantImageSnapshotResponse`
        """
        http_info = self._delete_v2_tenant_image_snapshot_http_info(request)
        return self._call_api(**http_info)

    def delete_v2_tenant_image_snapshot_async_invoker(self, request):
        http_info = self._delete_v2_tenant_image_snapshot_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_v2_tenant_image_snapshot_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/images/{image_id}/versions/{version_id}/image-snapshots/{image_snapshot_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteV2TenantImageSnapshotResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']
        if 'image_snapshot_id' in local_var_params:
            path_params['image_snapshot_id'] = local_var_params['image_snapshot_id']

        query_params = []

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

    def delete_v2_tenant_image_version_async(self, request):
        r"""删除指定镜像版本

        删除指定镜像版本。此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteV2TenantImageVersion
        :type request: :class:`huaweicloudsdkaidatalake.v2.DeleteV2TenantImageVersionRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.DeleteV2TenantImageVersionResponse`
        """
        http_info = self._delete_v2_tenant_image_version_http_info(request)
        return self._call_api(**http_info)

    def delete_v2_tenant_image_version_async_invoker(self, request):
        http_info = self._delete_v2_tenant_image_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_v2_tenant_image_version_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/images/{image_id}/versions/{version_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteV2TenantImageVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def delete_v2_workspace_async(self, request):
        r"""删除工作空间

        删除工作空间。此接口为同步接口，无配套使用接口。在该工作空间下存在计算资源、端点以及App的情况下无法删除，需要先清除该工作空间下创建的各种资源后才能删除。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteV2Workspace
        :type request: :class:`huaweicloudsdkaidatalake.v2.DeleteV2WorkspaceRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.DeleteV2WorkspaceResponse`
        """
        http_info = self._delete_v2_workspace_http_info(request)
        return self._call_api(**http_info)

    def delete_v2_workspace_async_invoker(self, request):
        http_info = self._delete_v2_workspace_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_v2_workspace_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/workspaces/{workspace_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteV2WorkspaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def detach_v2_agency_policy_async(self, request):
        r"""移除策略

        为委托移除关联策略。此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetachV2AgencyPolicy
        :type request: :class:`huaweicloudsdkaidatalake.v2.DetachV2AgencyPolicyRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.DetachV2AgencyPolicyResponse`
        """
        http_info = self._detach_v2_agency_policy_http_info(request)
        return self._call_api(**http_info)

    def detach_v2_agency_policy_async_invoker(self, request):
        http_info = self._detach_v2_agency_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _detach_v2_agency_policy_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/agencies/{agency_name}/policies/{policy_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DetachV2AgencyPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agency_name' in local_var_params:
            path_params['agency_name'] = local_var_params['agency_name']
        if 'policy_name' in local_var_params:
            path_params['policy_name'] = local_var_params['policy_name']

        query_params = []

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

    def list_v2_agreement_rule_async(self, request):
        r"""查询系统协议

        查询系统内置的租户协议内容列表，用户可从中了解协议名称、版本等信息。该接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListV2AgreementRule
        :type request: :class:`huaweicloudsdkaidatalake.v2.ListV2AgreementRuleRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ListV2AgreementRuleResponse`
        """
        http_info = self._list_v2_agreement_rule_http_info(request)
        return self._call_api(**http_info)

    def list_v2_agreement_rule_async_invoker(self, request):
        http_info = self._list_v2_agreement_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_v2_agreement_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/agreement/rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListV2AgreementRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

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

    def list_v2_all_endpoints_async(self, request):
        r"""查询所有端点列表

        列举该租户所有端点列表。此接口为同步接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListV2AllEndpoints
        :type request: :class:`huaweicloudsdkaidatalake.v2.ListV2AllEndpointsRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ListV2AllEndpointsResponse`
        """
        http_info = self._list_v2_all_endpoints_http_info(request)
        return self._call_api(**http_info)

    def list_v2_all_endpoints_async_invoker(self, request):
        http_info = self._list_v2_all_endpoints_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_v2_all_endpoints_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/endpoints",
            "request_type": request.__class__.__name__,
            "response_type": "ListV2AllEndpointsResponse"
            }

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
        if 'engine_types' in local_var_params:
            query_params.append(('engine_types', local_var_params['engine_types']))
            collection_formats['engine_types'] = 'multi'
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
            collection_formats['tags'] = 'multi'

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

    def list_v2_compute_versions_async(self, request):
        r"""查询计算资源操作记录列表

        查询计算资源操作记录列表。此接口为同步接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListV2ComputeVersions
        :type request: :class:`huaweicloudsdkaidatalake.v2.ListV2ComputeVersionsRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ListV2ComputeVersionsResponse`
        """
        http_info = self._list_v2_compute_versions_http_info(request)
        return self._call_api(**http_info)

    def list_v2_compute_versions_async_invoker(self, request):
        http_info = self._list_v2_compute_versions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_v2_compute_versions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/computes/versions",
            "request_type": request.__class__.__name__,
            "response_type": "ListV2ComputeVersionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'compute_id' in local_var_params:
            query_params.append(('compute_id', local_var_params['compute_id']))
        if 'operation_result' in local_var_params:
            query_params.append(('operation_result', local_var_params['operation_result']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_v2_computes_async(self, request):
        r"""查询计算资源列表

        查询工作空间下的计算资源列表。此接口为同步接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListV2Computes
        :type request: :class:`huaweicloudsdkaidatalake.v2.ListV2ComputesRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ListV2ComputesResponse`
        """
        http_info = self._list_v2_computes_http_info(request)
        return self._call_api(**http_info)

    def list_v2_computes_async_invoker(self, request):
        http_info = self._list_v2_computes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_v2_computes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/computes",
            "request_type": request.__class__.__name__,
            "response_type": "ListV2ComputesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'compute_id' in local_var_params:
            query_params.append(('compute_id', local_var_params['compute_id']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
            collection_formats['tags'] = 'multi'

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

    def list_v2_endpoints_async(self, request):
        r"""查询端点列表

        列举工作空间下的端点列表。用户可使用该接口列举指定工作空间下的端点列表，支持输入名称、id等参数过滤，支持分页查询。此接口为同步接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListV2Endpoints
        :type request: :class:`huaweicloudsdkaidatalake.v2.ListV2EndpointsRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ListV2EndpointsResponse`
        """
        http_info = self._list_v2_endpoints_http_info(request)
        return self._call_api(**http_info)

    def list_v2_endpoints_async_invoker(self, request):
        http_info = self._list_v2_endpoints_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_v2_endpoints_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/endpoints",
            "request_type": request.__class__.__name__,
            "response_type": "ListV2EndpointsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'engine_types' in local_var_params:
            query_params.append(('engine_types', local_var_params['engine_types']))
            collection_formats['engine_types'] = 'multi'
        if 'compute_id' in local_var_params:
            query_params.append(('compute_id', local_var_params['compute_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'storage_id' in local_var_params:
            query_params.append(('storage_id', local_var_params['storage_id']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
            collection_formats['tags'] = 'multi'

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

    def list_v2_networks_async(self, request):
        r"""查询网络配置列表

        查询工作空间下的网络配置列表。接口支持分页查询。此接口为同步接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListV2Networks
        :type request: :class:`huaweicloudsdkaidatalake.v2.ListV2NetworksRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ListV2NetworksResponse`
        """
        http_info = self._list_v2_networks_http_info(request)
        return self._call_api(**http_info)

    def list_v2_networks_async_invoker(self, request):
        http_info = self._list_v2_networks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_v2_networks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/networks",
            "request_type": request.__class__.__name__,
            "response_type": "ListV2NetworksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_v2_tenant_image_snapshots_async(self, request):
        r"""查询镜像快照列表

        查询当前租户下的全部镜像快照列表。此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListV2TenantImageSnapshots
        :type request: :class:`huaweicloudsdkaidatalake.v2.ListV2TenantImageSnapshotsRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ListV2TenantImageSnapshotsResponse`
        """
        http_info = self._list_v2_tenant_image_snapshots_http_info(request)
        return self._call_api(**http_info)

    def list_v2_tenant_image_snapshots_async_invoker(self, request):
        http_info = self._list_v2_tenant_image_snapshots_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_v2_tenant_image_snapshots_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/image-snapshots",
            "request_type": request.__class__.__name__,
            "response_type": "ListV2TenantImageSnapshotsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_v2_tenant_image_versions_async(self, request):
        r"""查询自定义镜像版本列表

        查询自定义镜像版本列表。用户可查询指定镜像下的所有版本信息。此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListV2TenantImageVersions
        :type request: :class:`huaweicloudsdkaidatalake.v2.ListV2TenantImageVersionsRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ListV2TenantImageVersionsResponse`
        """
        http_info = self._list_v2_tenant_image_versions_http_info(request)
        return self._call_api(**http_info)

    def list_v2_tenant_image_versions_async_invoker(self, request):
        http_info = self._list_v2_tenant_image_versions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_v2_tenant_image_versions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/images/{image_id}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "ListV2TenantImageVersionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'architectures' in local_var_params:
            query_params.append(('architectures', local_var_params['architectures']))
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))
        if 'endpoint_id' in local_var_params:
            query_params.append(('endpoint_id', local_var_params['endpoint_id']))
        if 'sort_by' in local_var_params:
            query_params.append(('sort_by', local_var_params['sort_by']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'tenant_id' in local_var_params:
            query_params.append(('tenantId', local_var_params['tenant_id']))

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

    def list_v2_tenant_images_async(self, request):
        r"""查询自定义镜像列表。

        查询自定义镜像列表。用户可查询已创建的自定义镜像列表。此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListV2TenantImages
        :type request: :class:`huaweicloudsdkaidatalake.v2.ListV2TenantImagesRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ListV2TenantImagesResponse`
        """
        http_info = self._list_v2_tenant_images_http_info(request)
        return self._call_api(**http_info)

    def list_v2_tenant_images_async_invoker(self, request):
        http_info = self._list_v2_tenant_images_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_v2_tenant_images_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/images",
            "request_type": request.__class__.__name__,
            "response_type": "ListV2TenantImagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_by' in local_var_params:
            query_params.append(('sort_by', local_var_params['sort_by']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'visibility' in local_var_params:
            query_params.append(('visibility', local_var_params['visibility']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_v2_workspaces_async(self, request):
        r"""查询工作空间列表

        查询工作空间列表。此接口为同步接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListV2Workspaces
        :type request: :class:`huaweicloudsdkaidatalake.v2.ListV2WorkspacesRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ListV2WorkspacesResponse`
        """
        http_info = self._list_v2_workspaces_http_info(request)
        return self._call_api(**http_info)

    def list_v2_workspaces_async_invoker(self, request):
        http_info = self._list_v2_workspaces_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_v2_workspaces_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces",
            "request_type": request.__class__.__name__,
            "response_type": "ListV2WorkspacesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
            collection_formats['tags'] = 'multi'

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def register_v2_tenant_image_async(self, request):
        r"""注册自定义镜像

        注册自定义镜像。用户通过该接口将外部镜像仓库中的镜像注册到租户中，以便后续使用。与[添加自定义镜像版本](AddV2ImageVersion.xml)接口配合完成镜像版本的添加。此接口为同步接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RegisterV2TenantImage
        :type request: :class:`huaweicloudsdkaidatalake.v2.RegisterV2TenantImageRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.RegisterV2TenantImageResponse`
        """
        http_info = self._register_v2_tenant_image_http_info(request)
        return self._call_api(**http_info)

    def register_v2_tenant_image_async_invoker(self, request):
        http_info = self._register_v2_tenant_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _register_v2_tenant_image_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/images",
            "request_type": request.__class__.__name__,
            "response_type": "RegisterV2TenantImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_v2_agency_async(self, request):
        r"""查询服务委托

        查询授权给AI DataLake服务的委托。用户调用该接口查询已授权给AI DataLake的委托，以及委托中具体的权限内容。此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowV2Agency
        :type request: :class:`huaweicloudsdkaidatalake.v2.ShowV2AgencyRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowV2AgencyResponse`
        """
        http_info = self._show_v2_agency_http_info(request)
        return self._call_api(**http_info)

    def show_v2_agency_async_invoker(self, request):
        http_info = self._show_v2_agency_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_v2_agency_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/agencies/{agency_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowV2AgencyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agency_name' in local_var_params:
            path_params['agency_name'] = local_var_params['agency_name']

        query_params = []

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

    def show_v2_agreement_async(self, request):
        r"""查询用户是否签署协议

        查询用户是否签署协议。此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowV2Agreement
        :type request: :class:`huaweicloudsdkaidatalake.v2.ShowV2AgreementRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowV2AgreementResponse`
        """
        http_info = self._show_v2_agreement_http_info(request)
        return self._call_api(**http_info)

    def show_v2_agreement_async_invoker(self, request):
        http_info = self._show_v2_agreement_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_v2_agreement_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/agreement",
            "request_type": request.__class__.__name__,
            "response_type": "ShowV2AgreementResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

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

    def show_v2_compute_async(self, request):
        r"""查看计算资源详情

        查看指定计算资源的详细信息。此接口为同步接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowV2Compute
        :type request: :class:`huaweicloudsdkaidatalake.v2.ShowV2ComputeRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowV2ComputeResponse`
        """
        http_info = self._show_v2_compute_http_info(request)
        return self._call_api(**http_info)

    def show_v2_compute_async_invoker(self, request):
        http_info = self._show_v2_compute_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_v2_compute_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/computes/{compute_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowV2ComputeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'compute_id' in local_var_params:
            path_params['compute_id'] = local_var_params['compute_id']

        query_params = []

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

    def show_v2_computes_metrics_async(self, request):
        r"""查询资源池监控

        查询资源池监控CPU、MEM、NPU、GPU数据。此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowV2ComputesMetrics
        :type request: :class:`huaweicloudsdkaidatalake.v2.ShowV2ComputesMetricsRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowV2ComputesMetricsResponse`
        """
        http_info = self._show_v2_computes_metrics_http_info(request)
        return self._call_api(**http_info)

    def show_v2_computes_metrics_async_invoker(self, request):
        http_info = self._show_v2_computes_metrics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_v2_computes_metrics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/computes/metrics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowV2ComputesMetricsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'step' in local_var_params:
            query_params.append(('step', local_var_params['step']))
        if 'metric_name' in local_var_params:
            query_params.append(('metric_name', local_var_params['metric_name']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'compute_ids' in local_var_params:
            query_params.append(('compute_ids', local_var_params['compute_ids']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_v2_endpoint_async(self, request):
        r"""查询端点详情

        列举工作空间下的端点详情。此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowV2Endpoint
        :type request: :class:`huaweicloudsdkaidatalake.v2.ShowV2EndpointRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowV2EndpointResponse`
        """
        http_info = self._show_v2_endpoint_http_info(request)
        return self._call_api(**http_info)

    def show_v2_endpoint_async_invoker(self, request):
        http_info = self._show_v2_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_v2_endpoint_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/endpoints/{endpoint_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowV2EndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'endpoint_id' in local_var_params:
            path_params['endpoint_id'] = local_var_params['endpoint_id']

        query_params = []

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

    def show_v2_endpoint_resource_limit_async(self, request):
        r"""查询端点配置限制

        查询指定资源池各规格的端点配置限制。此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowV2EndpointResourceLimit
        :type request: :class:`huaweicloudsdkaidatalake.v2.ShowV2EndpointResourceLimitRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowV2EndpointResourceLimitResponse`
        """
        http_info = self._show_v2_endpoint_resource_limit_http_info(request)
        return self._call_api(**http_info)

    def show_v2_endpoint_resource_limit_async_invoker(self, request):
        http_info = self._show_v2_endpoint_resource_limit_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_v2_endpoint_resource_limit_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/endpoint-limit",
            "request_type": request.__class__.__name__,
            "response_type": "ShowV2EndpointResourceLimitResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'compute_id' in local_var_params:
            query_params.append(('compute_id', local_var_params['compute_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_v2_endpoints_metrics_async(self, request):
        r"""查询端点监控

        查询端点CPU、MEM、NPU、GPU监控数据。此接口为同步接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowV2EndpointsMetrics
        :type request: :class:`huaweicloudsdkaidatalake.v2.ShowV2EndpointsMetricsRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowV2EndpointsMetricsResponse`
        """
        http_info = self._show_v2_endpoints_metrics_http_info(request)
        return self._call_api(**http_info)

    def show_v2_endpoints_metrics_async_invoker(self, request):
        http_info = self._show_v2_endpoints_metrics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_v2_endpoints_metrics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/endpoints/{endpoint_id}/metrics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowV2EndpointsMetricsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'endpoint_id' in local_var_params:
            path_params['endpoint_id'] = local_var_params['endpoint_id']

        query_params = []
        if 'step' in local_var_params:
            query_params.append(('step', local_var_params['step']))
        if 'metric_name' in local_var_params:
            query_params.append(('metric_name', local_var_params['metric_name']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_v2_tenant_image_async(self, request):
        r"""查询镜像详情

        查询指定镜像的详细信息。此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowV2TenantImage
        :type request: :class:`huaweicloudsdkaidatalake.v2.ShowV2TenantImageRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowV2TenantImageResponse`
        """
        http_info = self._show_v2_tenant_image_http_info(request)
        return self._call_api(**http_info)

    def show_v2_tenant_image_async_invoker(self, request):
        http_info = self._show_v2_tenant_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_v2_tenant_image_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/images/{image_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowV2TenantImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

        query_params = []

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

    def show_v2_tenant_image_version_async(self, request):
        r"""查询自定义镜像版本

        查询自定义镜像版本。用户可查询指定镜像版本的详细信息。此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowV2TenantImageVersion
        :type request: :class:`huaweicloudsdkaidatalake.v2.ShowV2TenantImageVersionRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowV2TenantImageVersionResponse`
        """
        http_info = self._show_v2_tenant_image_version_http_info(request)
        return self._call_api(**http_info)

    def show_v2_tenant_image_version_async_invoker(self, request):
        http_info = self._show_v2_tenant_image_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_v2_tenant_image_version_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/images/{image_id}/versions/{version_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowV2TenantImageVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []

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

    def show_v2_workspace_async(self, request):
        r"""查询工作空间详细信息

        查询工作空间详细信息。用户可通过该接口查询某工作空间详情，输入为工作空间ID，返回对应工作空间详情。此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowV2Workspace
        :type request: :class:`huaweicloudsdkaidatalake.v2.ShowV2WorkspaceRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowV2WorkspaceResponse`
        """
        http_info = self._show_v2_workspace_http_info(request)
        return self._call_api(**http_info)

    def show_v2_workspace_async_invoker(self, request):
        http_info = self._show_v2_workspace_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_v2_workspace_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowV2WorkspaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def sign_v2_agreement_async(self, request):
        r"""签署租户协议

        签署租户协议，用户通过该接口签署租户协议。此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SignV2Agreement
        :type request: :class:`huaweicloudsdkaidatalake.v2.SignV2AgreementRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.SignV2AgreementResponse`
        """
        http_info = self._sign_v2_agreement_http_info(request)
        return self._call_api(**http_info)

    def sign_v2_agreement_async_invoker(self, request):
        http_info = self._sign_v2_agreement_http_info(request)
        return AsyncInvoker(self, http_info)

    def _sign_v2_agreement_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/agreement",
            "request_type": request.__class__.__name__,
            "response_type": "SignV2AgreementResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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

    def update_v2_compute_async(self, request):
        r"""更新计算资源

        更新指定计算资源的配置信息。此接口为异步接口，可通过[查询计算资源操作记录列表](ListV2ComputeVersions.xml)接口获取操作结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateV2Compute
        :type request: :class:`huaweicloudsdkaidatalake.v2.UpdateV2ComputeRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.UpdateV2ComputeResponse`
        """
        http_info = self._update_v2_compute_http_info(request)
        return self._call_api(**http_info)

    def update_v2_compute_async_invoker(self, request):
        http_info = self._update_v2_compute_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_v2_compute_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/workspaces/{workspace_id}/computes/{compute_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateV2ComputeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'compute_id' in local_var_params:
            path_params['compute_id'] = local_var_params['compute_id']

        query_params = []

        header_params = {}

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

    def update_v2_endpoint_async(self, request):
        r"""更新端点

        更新端点。此接口为异步接口，可通过[查询端点详情](ShowV2Endpoint.xml)接口获取操作结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateV2Endpoint
        :type request: :class:`huaweicloudsdkaidatalake.v2.UpdateV2EndpointRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.UpdateV2EndpointResponse`
        """
        http_info = self._update_v2_endpoint_http_info(request)
        return self._call_api(**http_info)

    def update_v2_endpoint_async_invoker(self, request):
        http_info = self._update_v2_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_v2_endpoint_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/workspaces/{workspace_id}/endpoints/{endpoint_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateV2EndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'endpoint_id' in local_var_params:
            path_params['endpoint_id'] = local_var_params['endpoint_id']

        query_params = []

        header_params = {}

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

    def update_v2_tenant_image_version_async(self, request):
        r"""更新自定义镜像版本

        更新自定义镜像版本信息。用户通过该接口更新指定镜像版本的描述、架构、容器软件、分类等信息。与[注册自定义镜像](RegisterV2Image.xml)接口配合完成镜像版本管理。此接口为同步接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateV2TenantImageVersion
        :type request: :class:`huaweicloudsdkaidatalake.v2.UpdateV2TenantImageVersionRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.UpdateV2TenantImageVersionResponse`
        """
        http_info = self._update_v2_tenant_image_version_http_info(request)
        return self._call_api(**http_info)

    def update_v2_tenant_image_version_async_invoker(self, request):
        http_info = self._update_v2_tenant_image_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_v2_tenant_image_version_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/images/{image_id}/versions/{version_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateV2TenantImageVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def update_v2_workspace_async(self, request):
        r"""更新工作空间

        更新工作空间。此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateV2Workspace
        :type request: :class:`huaweicloudsdkaidatalake.v2.UpdateV2WorkspaceRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.UpdateV2WorkspaceResponse`
        """
        http_info = self._update_v2_workspace_http_info(request)
        return self._call_api(**http_info)

    def update_v2_workspace_async_invoker(self, request):
        http_info = self._update_v2_workspace_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_v2_workspace_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/workspaces/{workspace_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateV2WorkspaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def cancel_aura_dataframe_job_async(self, request):
        r"""取消Aura Dataframe Job

        取消正在运行中的Dataframe Job。
        此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CancelAuraDataframeJob
        :type request: :class:`huaweicloudsdkaidatalake.v2.CancelAuraDataframeJobRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.CancelAuraDataframeJobResponse`
        """
        http_info = self._cancel_aura_dataframe_job_http_info(request)
        return self._call_api(**http_info)

    def cancel_aura_dataframe_job_async_invoker(self, request):
        http_info = self._cancel_aura_dataframe_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _cancel_aura_dataframe_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/aura-dataframe-jobs/{job_id}/cancel",
            "request_type": request.__class__.__name__,
            "response_type": "CancelAuraDataframeJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def create_aura_dataframe_job_async(self, request):
        r"""创建Aura Dataframe Job

        创建Dataframe Job。
        用户通过此接口在指定端点创建Dataframe Job。
        此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAuraDataframeJob
        :type request: :class:`huaweicloudsdkaidatalake.v2.CreateAuraDataframeJobRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.CreateAuraDataframeJobResponse`
        """
        http_info = self._create_aura_dataframe_job_http_info(request)
        return self._call_api(**http_info)

    def create_aura_dataframe_job_async_invoker(self, request):
        http_info = self._create_aura_dataframe_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_aura_dataframe_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/aura-dataframe-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAuraDataframeJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_aura_dataframe_job_async(self, request):
        r"""查看Aura Dataframe Job列表

        查询Aura Dataframe Job列表。
        此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAuraDataframeJob
        :type request: :class:`huaweicloudsdkaidatalake.v2.ListAuraDataframeJobRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ListAuraDataframeJobResponse`
        """
        http_info = self._list_aura_dataframe_job_http_info(request)
        return self._call_api(**http_info)

    def list_aura_dataframe_job_async_invoker(self, request):
        http_info = self._list_aura_dataframe_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_aura_dataframe_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/aura-dataframe-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuraDataframeJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'endpoint_id' in local_var_params:
            query_params.append(('endpoint_id', local_var_params['endpoint_id']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

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

    def show_aura_dataframe_job_async(self, request):
        r"""查看Aura Dataframe Job详情

        查询Aura Dataframe Job信息。
        此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAuraDataframeJob
        :type request: :class:`huaweicloudsdkaidatalake.v2.ShowAuraDataframeJobRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowAuraDataframeJobResponse`
        """
        http_info = self._show_aura_dataframe_job_http_info(request)
        return self._call_api(**http_info)

    def show_aura_dataframe_job_async_invoker(self, request):
        http_info = self._show_aura_dataframe_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_aura_dataframe_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/aura-dataframe-jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuraDataframeJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

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

    def cancel_aura_sql_statement_async(self, request):
        r"""取消SQL执行

        取消SQL语句执行。 用户可通过该接口取消SQL语句执行，输入为SQL Session id、statement id，返回操作结果。 此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CancelAuraSqlStatement
        :type request: :class:`huaweicloudsdkaidatalake.v2.CancelAuraSqlStatementRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.CancelAuraSqlStatementResponse`
        """
        http_info = self._cancel_aura_sql_statement_http_info(request)
        return self._call_api(**http_info)

    def cancel_aura_sql_statement_async_invoker(self, request):
        http_info = self._cancel_aura_sql_statement_http_info(request)
        return AsyncInvoker(self, http_info)

    def _cancel_aura_sql_statement_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/aura-sessions/{session_id}/statements/{statement_id}/cancel",
            "request_type": request.__class__.__name__,
            "response_type": "CancelAuraSqlStatementResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'session_id' in local_var_params:
            path_params['session_id'] = local_var_params['session_id']
        if 'statement_id' in local_var_params:
            path_params['statement_id'] = local_var_params['statement_id']

        query_params = []

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

    def close_aura_sql_session_async(self, request):
        r"""关闭Session

        关闭SQL Session。
        用户可通过此接口关闭SQL Session，输入为Session id，返回操作结果。
        此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CloseAuraSqlSession
        :type request: :class:`huaweicloudsdkaidatalake.v2.CloseAuraSqlSessionRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.CloseAuraSqlSessionResponse`
        """
        http_info = self._close_aura_sql_session_http_info(request)
        return self._call_api(**http_info)

    def close_aura_sql_session_async_invoker(self, request):
        http_info = self._close_aura_sql_session_http_info(request)
        return AsyncInvoker(self, http_info)

    def _close_aura_sql_session_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/workspaces/{workspace_id}/aura-sessions/{session_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CloseAuraSqlSessionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'session_id' in local_var_params:
            path_params['session_id'] = local_var_params['session_id']

        query_params = []

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

    def create_aura_sql_session_async(self, request):
        r"""创建Session

        创建SQL Session。
        用户通过此接口在指定端点创建SQL Session，通过输入端点id、LakeFormation配置，返回Session信息。
        此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAuraSqlSession
        :type request: :class:`huaweicloudsdkaidatalake.v2.CreateAuraSqlSessionRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.CreateAuraSqlSessionResponse`
        """
        http_info = self._create_aura_sql_session_http_info(request)
        return self._call_api(**http_info)

    def create_aura_sql_session_async_invoker(self, request):
        http_info = self._create_aura_sql_session_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_aura_sql_session_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/aura-sessions",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAuraSqlSessionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def execute_aura_sql_statement_async(self, request):
        r"""在指定Session中执行SQL

        在指定的Session下执行SQL语句。
        用户可通过此接口执行SQL语句，输入为SQL语句、SQL Session id、绑定参数等信息，返回语句执行结果或statement id。
        此接口支持异步和同步两种执行模式，由入参is_sync参数决定。如果是异步执行，配套使用[查看SQL执行结果](ShowAuraV2SqlStatementResult.xml)接口查询语句结果。
        如果是同步执行，接口会等待一段时间接收结果，如果执行完毕会返回执行结果，如果没有执行完毕，会返回一个运行中状态，后续可以使用[查看SQL执行结果](ShowAuraV2SqlStatementResult.xml)接口查询语句结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteAuraSqlStatement
        :type request: :class:`huaweicloudsdkaidatalake.v2.ExecuteAuraSqlStatementRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ExecuteAuraSqlStatementResponse`
        """
        http_info = self._execute_aura_sql_statement_http_info(request)
        return self._call_api(**http_info)

    def execute_aura_sql_statement_async_invoker(self, request):
        http_info = self._execute_aura_sql_statement_http_info(request)
        return AsyncInvoker(self, http_info)

    def _execute_aura_sql_statement_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/aura-sessions/statements",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteAuraSqlStatementResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

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

    def list_aura_session_statement_records_async(self, request):
        r"""查看指定Session下的SQL执行记录

        查询指定Session下的SQL执行记录。
        输入workspace_id，session_id，statement_id（可选），status（可选），分页查询参数limit和marker；输出此会话下SQL执行记录。
        此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAuraSessionStatementRecords
        :type request: :class:`huaweicloudsdkaidatalake.v2.ListAuraSessionStatementRecordsRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ListAuraSessionStatementRecordsResponse`
        """
        http_info = self._list_aura_session_statement_records_http_info(request)
        return self._call_api(**http_info)

    def list_aura_session_statement_records_async_invoker(self, request):
        http_info = self._list_aura_session_statement_records_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_aura_session_statement_records_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/aura-sessions/{session_id}/statements",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuraSessionStatementRecordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'session_id' in local_var_params:
            path_params['session_id'] = local_var_params['session_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'statement_id' in local_var_params:
            query_params.append(('statement_id', local_var_params['statement_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

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

    def list_aura_sql_sessions_async(self, request):
        r"""查看Session列表

        查询SQL Session列表。
        输入workspace_id，endpoint_name（可选），status（可选），session_id（可选），start_time（可选），end_time（可选）,分页查询参数limit和marker；输出SQL会话列表，包含会话id、会话创建时间、结束时间、会话状态等信息。
        此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAuraSqlSessions
        :type request: :class:`huaweicloudsdkaidatalake.v2.ListAuraSqlSessionsRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ListAuraSqlSessionsResponse`
        """
        http_info = self._list_aura_sql_sessions_http_info(request)
        return self._call_api(**http_info)

    def list_aura_sql_sessions_async_invoker(self, request):
        http_info = self._list_aura_sql_sessions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_aura_sql_sessions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/aura-sessions",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuraSqlSessionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'endpoint_id' in local_var_params:
            query_params.append(('endpoint_id', local_var_params['endpoint_id']))
        if 'endpoint_name' in local_var_params:
            query_params.append(('endpoint_name', local_var_params['endpoint_name']))
        if 'session_id' in local_var_params:
            query_params.append(('session_id', local_var_params['session_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_aura_statement_records_async(self, request):
        r"""查看SQL执行记录

        查询SQL执行记录。 查询指定Session下的SQL执行记录。 输入workspace_id，session_id，statement_id（可选），status（可选），分页查询参数limit和marker；输出此会话下SQL执行记录。 此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAuraStatementRecords
        :type request: :class:`huaweicloudsdkaidatalake.v2.ListAuraStatementRecordsRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ListAuraStatementRecordsResponse`
        """
        http_info = self._list_aura_statement_records_http_info(request)
        return self._call_api(**http_info)

    def list_aura_statement_records_async_invoker(self, request):
        http_info = self._list_aura_statement_records_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_aura_statement_records_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/aura-statement-records",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuraStatementRecordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'endpoint_id' in local_var_params:
            query_params.append(('endpoint_id', local_var_params['endpoint_id']))
        if 'endpoint_name' in local_var_params:
            query_params.append(('endpoint_name', local_var_params['endpoint_name']))
        if 'session_id' in local_var_params:
            query_params.append(('session_id', local_var_params['session_id']))
        if 'statement_id' in local_var_params:
            query_params.append(('statement_id', local_var_params['statement_id']))
        if 'source' in local_var_params:
            query_params.append(('source', local_var_params['source']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def show_aura_sql_session_async(self, request):
        r"""查看Session详情

        查询SQL Session信息。
        用户可通过此接口查询SQL Session信息，输入为Session id，返回操作结果。
        此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAuraSqlSession
        :type request: :class:`huaweicloudsdkaidatalake.v2.ShowAuraSqlSessionRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowAuraSqlSessionResponse`
        """
        http_info = self._show_aura_sql_session_http_info(request)
        return self._call_api(**http_info)

    def show_aura_sql_session_async_invoker(self, request):
        http_info = self._show_aura_sql_session_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_aura_sql_session_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/aura-sessions/{session_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuraSqlSessionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'session_id' in local_var_params:
            path_params['session_id'] = local_var_params['session_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_aura_sql_statement_result_async(self, request):
        r"""查看SQL执行结果

        查询SQL语句执行结果。
        用户可通过该接口查询SQL语句执行结果，输入为SQL Session id、statement id，返回执行结果。
        此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAuraSqlStatementResult
        :type request: :class:`huaweicloudsdkaidatalake.v2.ShowAuraSqlStatementResultRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowAuraSqlStatementResultResponse`
        """
        http_info = self._show_aura_sql_statement_result_http_info(request)
        return self._call_api(**http_info)

    def show_aura_sql_statement_result_async_invoker(self, request):
        http_info = self._show_aura_sql_statement_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_aura_sql_statement_result_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/aura-sessions/{session_id}/statements/{statement_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuraSqlStatementResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'session_id' in local_var_params:
            path_params['session_id'] = local_var_params['session_id']
        if 'statement_id' in local_var_params:
            path_params['statement_id'] = local_var_params['statement_id']

        query_params = []
        if 'page_num' in local_var_params:
            query_params.append(('page_num', local_var_params['page_num']))
        if 'is_enable_obs_path' in local_var_params:
            query_params.append(('is_enable_obs_path', local_var_params['is_enable_obs_path']))

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

    def show_aura_statement_operator_metrics_async(self, request):
        r"""查看SQL执行算子监控记录

        查看SQL执行算子监控记录。 用户可通过该接口查看SQL执行算子监控记录，输入为SQL Session id、statement id，返回操作结果。 此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAuraStatementOperatorMetrics
        :type request: :class:`huaweicloudsdkaidatalake.v2.ShowAuraStatementOperatorMetricsRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowAuraStatementOperatorMetricsResponse`
        """
        http_info = self._show_aura_statement_operator_metrics_http_info(request)
        return self._call_api(**http_info)

    def show_aura_statement_operator_metrics_async_invoker(self, request):
        http_info = self._show_aura_statement_operator_metrics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_aura_statement_operator_metrics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/aura-sessions/{session_id}/statements/{statement_id}/operator-metrics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuraStatementOperatorMetricsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'session_id' in local_var_params:
            path_params['session_id'] = local_var_params['session_id']
        if 'statement_id' in local_var_params:
            path_params['statement_id'] = local_var_params['statement_id']

        query_params = []

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

    def show_aura_statement_query_metrics_async(self, request):
        r"""查看语句监控详情

        查询语句监控详情信息。
        输入workspace_id，session_id，statement_id，输出此会话下SQL监控数据。
        此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAuraStatementQueryMetrics
        :type request: :class:`huaweicloudsdkaidatalake.v2.ShowAuraStatementQueryMetricsRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowAuraStatementQueryMetricsResponse`
        """
        http_info = self._show_aura_statement_query_metrics_http_info(request)
        return self._call_api(**http_info)

    def show_aura_statement_query_metrics_async_invoker(self, request):
        http_info = self._show_aura_statement_query_metrics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_aura_statement_query_metrics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/aura-sessions/{session_id}/statements/{statement_id}/query-metrics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuraStatementQueryMetricsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'session_id' in local_var_params:
            path_params['session_id'] = local_var_params['session_id']
        if 'statement_id' in local_var_params:
            path_params['statement_id'] = local_var_params['statement_id']

        query_params = []

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

    def list_flink_job_autoscaling_histories_async(self, request):
        r"""查询Flink作业自动调优历史

        查询Flink作业自动调优历史记录，包含每次扩缩容操作的详细信息。此接口为同步接口，支持分页查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFlinkJobAutoscalingHistories
        :type request: :class:`huaweicloudsdkaidatalake.v2.ListFlinkJobAutoscalingHistoriesRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ListFlinkJobAutoscalingHistoriesResponse`
        """
        http_info = self._list_flink_job_autoscaling_histories_http_info(request)
        return self._call_api(**http_info)

    def list_flink_job_autoscaling_histories_async_invoker(self, request):
        http_info = self._list_flink_job_autoscaling_histories_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_flink_job_autoscaling_histories_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/flink-jobs/{job_id}/autoscaling-histories",
            "request_type": request.__class__.__name__,
            "response_type": "ListFlinkJobAutoscalingHistoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def show_flink_job_autoscaling_policy_async(self, request):
        r"""查询Flink作业自动调优配置

        查询Flink作业当前的自动调优配置。此接口为同步接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowFlinkJobAutoscalingPolicy
        :type request: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkJobAutoscalingPolicyRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkJobAutoscalingPolicyResponse`
        """
        http_info = self._show_flink_job_autoscaling_policy_http_info(request)
        return self._call_api(**http_info)

    def show_flink_job_autoscaling_policy_async_invoker(self, request):
        http_info = self._show_flink_job_autoscaling_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_flink_job_autoscaling_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/flink-jobs/{job_id}/autoscaling-policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFlinkJobAutoscalingPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

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

    def update_flink_job_autoscaling_policy_async(self, request):
        r"""热更新Flink作业自动调优配置

        热更新Flink作业自动调优配置。此接口为异步接口，作业运行中时配置将自动应用，无需重启作业。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateFlinkJobAutoscalingPolicy
        :type request: :class:`huaweicloudsdkaidatalake.v2.UpdateFlinkJobAutoscalingPolicyRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.UpdateFlinkJobAutoscalingPolicyResponse`
        """
        http_info = self._update_flink_job_autoscaling_policy_http_info(request)
        return self._call_api(**http_info)

    def update_flink_job_autoscaling_policy_async_invoker(self, request):
        http_info = self._update_flink_job_autoscaling_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_flink_job_autoscaling_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/workspaces/{workspace_id}/flink-jobs/{job_id}/autoscaling-policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateFlinkJobAutoscalingPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}

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

    def cancel_flink_job_async(self, request):
        r"""取消Flink作业执行

        取消Flink作业。此接口为异步接口，响应仅表示取消请求已接收，作业实际停止状态可通过[查询Flink作业状态](ShowFlinkJobState.xml)接口查询。
        支持多种停止策略：
        - NONE：立即停止不保存状态。
        - STOP_WITH_SAVEPOINT：停止前创建快照。
        - STOP_WITH_DRAIN：Drain模式停止，触发窗口计算后再创建快照停止。
        - FORCE_CANCEL：强制取消，仅当作业已处于CANCELLING状态时可再次触发取消。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CancelFlinkJob
        :type request: :class:`huaweicloudsdkaidatalake.v2.CancelFlinkJobRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.CancelFlinkJobResponse`
        """
        http_info = self._cancel_flink_job_http_info(request)
        return self._call_api(**http_info)

    def cancel_flink_job_async_invoker(self, request):
        http_info = self._cancel_flink_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _cancel_flink_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/flink-jobs/{job_id}/cancel",
            "request_type": request.__class__.__name__,
            "response_type": "CancelFlinkJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}

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

    def list_flink_job_events_async(self, request):
        r"""查询Flink作业事件详情列表

        查询Flink作业的运行事件列表。此接口为同步接口，响应中包含作业运行期间产生的事件详情，可用于问题定位和运行状态追踪。
        可通过[查看Flink作业详情](ShowFlinkJob.xml)接口获取作业完整信息，或通过[查询Flink作业状态](ShowFlinkJobState.xml)接口获取作业当前运行状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFlinkJobEvents
        :type request: :class:`huaweicloudsdkaidatalake.v2.ListFlinkJobEventsRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ListFlinkJobEventsResponse`
        """
        http_info = self._list_flink_job_events_http_info(request)
        return self._call_api(**http_info)

    def list_flink_job_events_async_invoker(self, request):
        http_info = self._list_flink_job_events_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_flink_job_events_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/flink-jobs/{job_id}/events",
            "request_type": request.__class__.__name__,
            "response_type": "ListFlinkJobEventsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'create_time_after' in local_var_params:
            query_params.append(('create_time_after', local_var_params['create_time_after']))
        if 'create_time_before' in local_var_params:
            query_params.append(('create_time_before', local_var_params['create_time_before']))

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

    def list_flink_jobs_async(self, request):
        r"""查询Flink作业列表

        查询工作空间下Flink作业列表。此接口为同步接口，响应中包含作业的概要信息，支持分页查询和多条件筛选。
        可通过[查看Flink作业详情](ShowFlinkJob.xml)接口获取指定作业的完整信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFlinkJobs
        :type request: :class:`huaweicloudsdkaidatalake.v2.ListFlinkJobsRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ListFlinkJobsResponse`
        """
        http_info = self._list_flink_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_flink_jobs_async_invoker(self, request):
        http_info = self._list_flink_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_flink_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/flink-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListFlinkJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'create_time_after' in local_var_params:
            query_params.append(('create_time_after', local_var_params['create_time_after']))
        if 'create_time_before' in local_var_params:
            query_params.append(('create_time_before', local_var_params['create_time_before']))
        if 'endpoint_id' in local_var_params:
            query_params.append(('endpoint_id', local_var_params['endpoint_id']))
        if 'endpoint_name' in local_var_params:
            query_params.append(('endpoint_name', local_var_params['endpoint_name']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))
        if 'deployment_id' in local_var_params:
            query_params.append(('deployment_id', local_var_params['deployment_id']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
            collection_formats['state'] = 'multi'
        if 'job_type' in local_var_params:
            query_params.append(('job_type', local_var_params['job_type']))
        if 'execution_mode' in local_var_params:
            query_params.append(('execution_mode', local_var_params['execution_mode']))
        if 'create_user_id' in local_var_params:
            query_params.append(('create_user_id', local_var_params['create_user_id']))
        if 'labels' in local_var_params:
            query_params.append(('labels', local_var_params['labels']))
            collection_formats['labels'] = 'multi'

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

    def run_flink_job_async(self, request):
        r"""创建Flink作业

        创建并启动Flink作业实例。此接口为异步接口，响应仅表示作业创建请求已接收，作业实际运行状态可通过[查询Flink作业状态](ShowFlinkJobState.xml)接口查询。
        支持多种作业类型：
        - FLINK_SQL_JOB：SQL作业。
        - FLINK_JAR_JOB：JAR作业。
        - FLINK_SQL_GATEWAY：SQL Gateway作业。
        - FLINK_PYTHON_JOB：Python作业。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunFlinkJob
        :type request: :class:`huaweicloudsdkaidatalake.v2.RunFlinkJobRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.RunFlinkJobResponse`
        """
        http_info = self._run_flink_job_http_info(request)
        return self._call_api(**http_info)

    def run_flink_job_async_invoker(self, request):
        http_info = self._run_flink_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_flink_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/flink-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "RunFlinkJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'x_client_token' in local_var_params:
            header_params['X-Client-Token'] = local_var_params['x_client_token']

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

    def show_flink_job_async(self, request):
        r"""查看Flink作业详情

        获取Flink作业实例的详细信息。此接口为同步接口，响应中包含作业的完整配置和运行状态信息。
        可通过[查询Flink作业事件详情列表](ListFlinkJobEvents.xml)接口获取作业运行事件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowFlinkJob
        :type request: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkJobRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkJobResponse`
        """
        http_info = self._show_flink_job_http_info(request)
        return self._call_api(**http_info)

    def show_flink_job_async_invoker(self, request):
        http_info = self._show_flink_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_flink_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/flink-jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFlinkJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

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

    def show_flink_job_state_async(self, request):
        r"""查询Flink作业状态

        查询Flink作业的运行状态。此接口为同步接口，响应中包含作业当前状态。
        可通过[查看Flink作业详情](ShowFlinkJob.xml)接口获取作业完整信息，或通过[查询Flink作业事件详情列表](ListFlinkJobEvents.xml)接口获取作业运行事件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowFlinkJobState
        :type request: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkJobStateRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkJobStateResponse`
        """
        http_info = self._show_flink_job_state_http_info(request)
        return self._call_api(**http_info)

    def show_flink_job_state_async_invoker(self, request):
        http_info = self._show_flink_job_state_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_flink_job_state_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/flink-jobs/{job_id}/state",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFlinkJobStateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

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

    def create_flink_savepoint_async(self, request):
        r"""创建Flink作业Savepoint

        为运行中的Flink作业触发Savepoint，用于保存作业当前状态。此接口为异步接口，响应仅表示快照创建请求已接收，快照实际生成状态可通过[查询Flink作业Savepoint列表](ListFlinkSavepoint.xml)接口查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateFlinkSavepoint
        :type request: :class:`huaweicloudsdkaidatalake.v2.CreateFlinkSavepointRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.CreateFlinkSavepointResponse`
        """
        http_info = self._create_flink_savepoint_http_info(request)
        return self._call_api(**http_info)

    def create_flink_savepoint_async_invoker(self, request):
        http_info = self._create_flink_savepoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_flink_savepoint_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/flink-jobs/{job_id}/flink-savepoints",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFlinkSavepointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}

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

    def delete_flink_savepoint_async(self, request):
        r"""删除Flink作业Savepoint

        删除指定Savepoint的元数据记录，不影响OBS中的实际Savepoint数据。该接口为同步接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteFlinkSavepoint
        :type request: :class:`huaweicloudsdkaidatalake.v2.DeleteFlinkSavepointRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.DeleteFlinkSavepointResponse`
        """
        http_info = self._delete_flink_savepoint_http_info(request)
        return self._call_api(**http_info)

    def delete_flink_savepoint_async_invoker(self, request):
        http_info = self._delete_flink_savepoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_flink_savepoint_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/workspaces/{workspace_id}/flink-jobs/{job_id}/flink-savepoints/{savepoint_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteFlinkSavepointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'savepoint_id' in local_var_params:
            path_params['savepoint_id'] = local_var_params['savepoint_id']

        query_params = []

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

    def list_flink_savepoint_async(self, request):
        r"""查询Flink作业Savepoint列表

        查询指定Flink作业的Savepoint记录，返回分页列表。此接口为同步接口，响应中包含Savepoint的详细信息。
        可通过[查询Flink作业Savepoint详情](ShowFlinkSavepoint.xml)接口获取指定Savepoint的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFlinkSavepoint
        :type request: :class:`huaweicloudsdkaidatalake.v2.ListFlinkSavepointRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ListFlinkSavepointResponse`
        """
        http_info = self._list_flink_savepoint_http_info(request)
        return self._call_api(**http_info)

    def list_flink_savepoint_async_invoker(self, request):
        http_info = self._list_flink_savepoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_flink_savepoint_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/flink-jobs/{job_id}/flink-savepoints",
            "request_type": request.__class__.__name__,
            "response_type": "ListFlinkSavepointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'create_time_after' in local_var_params:
            query_params.append(('create_time_after', local_var_params['create_time_after']))
        if 'create_time_before' in local_var_params:
            query_params.append(('create_time_before', local_var_params['create_time_before']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'trigger_type' in local_var_params:
            query_params.append(('trigger_type', local_var_params['trigger_type']))

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

    def show_flink_savepoint_async(self, request):
        r"""查询Flink作业Savepoint详情

        获取指定Savepoint的详细信息。此接口为同步接口，响应中包含Savepoint的完整状态和配置信息。
        可通过[查询Flink作业Savepoint列表](ListFlinkSavepoint.xml)接口获取Savepoint列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowFlinkSavepoint
        :type request: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkSavepointRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkSavepointResponse`
        """
        http_info = self._show_flink_savepoint_http_info(request)
        return self._call_api(**http_info)

    def show_flink_savepoint_async_invoker(self, request):
        http_info = self._show_flink_savepoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_flink_savepoint_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/flink-jobs/{job_id}/flink-savepoints/{savepoint_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFlinkSavepointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'savepoint_id' in local_var_params:
            path_params['savepoint_id'] = local_var_params['savepoint_id']

        query_params = []

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

    def create_v2_ray_federation_async(self, request):
        r"""创建Ray联邦端点

        创建Ray联邦端点。此接口为同步接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateV2RayFederation
        :type request: :class:`huaweicloudsdkaidatalake.v2.CreateV2RayFederationRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.CreateV2RayFederationResponse`
        """
        http_info = self._create_v2_ray_federation_http_info(request)
        return self._call_api(**http_info)

    def create_v2_ray_federation_async_invoker(self, request):
        http_info = self._create_v2_ray_federation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_v2_ray_federation_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/ray-federations",
            "request_type": request.__class__.__name__,
            "response_type": "CreateV2RayFederationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

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

    def delete_v2_ray_federation_async(self, request):
        r"""删除Ray联邦端点

        删除Ray联邦端点。此接口为同步接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteV2RayFederation
        :type request: :class:`huaweicloudsdkaidatalake.v2.DeleteV2RayFederationRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.DeleteV2RayFederationResponse`
        """
        http_info = self._delete_v2_ray_federation_http_info(request)
        return self._call_api(**http_info)

    def delete_v2_ray_federation_async_invoker(self, request):
        http_info = self._delete_v2_ray_federation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_v2_ray_federation_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/workspaces/{workspace_id}/ray-federations/{ray_federation_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteV2RayFederationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'ray_federation_id' in local_var_params:
            path_params['ray_federation_id'] = local_var_params['ray_federation_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_v2_ray_federations_async(self, request):
        r"""查询Ray联邦端点列表

        查询工作空间下的Ray联邦端点列表。此接口为同步接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListV2RayFederations
        :type request: :class:`huaweicloudsdkaidatalake.v2.ListV2RayFederationsRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ListV2RayFederationsResponse`
        """
        http_info = self._list_v2_ray_federations_http_info(request)
        return self._call_api(**http_info)

    def list_v2_ray_federations_async_invoker(self, request):
        http_info = self._list_v2_ray_federations_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_v2_ray_federations_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/ray-federations",
            "request_type": request.__class__.__name__,
            "response_type": "ListV2RayFederationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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

    def show_v2_ray_federation_async(self, request):
        r"""查询Ray联邦端点详情

        查询Ray联邦端点详情。此接口为同步接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowV2RayFederation
        :type request: :class:`huaweicloudsdkaidatalake.v2.ShowV2RayFederationRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowV2RayFederationResponse`
        """
        http_info = self._show_v2_ray_federation_http_info(request)
        return self._call_api(**http_info)

    def show_v2_ray_federation_async_invoker(self, request):
        http_info = self._show_v2_ray_federation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_v2_ray_federation_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/ray-federations/{ray_federation_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowV2RayFederationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'ray_federation_id' in local_var_params:
            path_params['ray_federation_id'] = local_var_params['ray_federation_id']

        query_params = []

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

    def update_v2_ray_federation_async(self, request):
        r"""更新Ray联邦端点

        更新Ray联邦端点。此接口为同步接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateV2RayFederation
        :type request: :class:`huaweicloudsdkaidatalake.v2.UpdateV2RayFederationRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.UpdateV2RayFederationResponse`
        """
        http_info = self._update_v2_ray_federation_http_info(request)
        return self._call_api(**http_info)

    def update_v2_ray_federation_async_invoker(self, request):
        http_info = self._update_v2_ray_federation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_v2_ray_federation_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/workspaces/{workspace_id}/ray-federations/{ray_federation_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateV2RayFederationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'ray_federation_id' in local_var_params:
            path_params['ray_federation_id'] = local_var_params['ray_federation_id']

        query_params = []

        header_params = {}

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

    def cancel_ray_job_async(self, request):
        r"""取消作业运行

        取消作业运行。主要使用于取消运行Ray Job场景。本接口为异步接口，当前取消作业运行请求下发成功后会返回job_id，此时取消作业运行并没有立即完成，需要通过调用[查看Ray作业详情](ShowRayJob.xml)查询Job状态，当Job状态为CANCELED时代表取消作业运行成功。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CancelRayJob
        :type request: :class:`huaweicloudsdkaidatalake.v2.CancelRayJobRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.CancelRayJobResponse`
        """
        http_info = self._cancel_ray_job_http_info(request)
        return self._call_api(**http_info)

    def cancel_ray_job_async_invoker(self, request):
        http_info = self._cancel_ray_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _cancel_ray_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/ray-jobs/{job_id}/cancel",
            "request_type": request.__class__.__name__,
            "response_type": "CancelRayJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

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

    def list_ray_jobs_async(self, request):
        r"""查询Ray作业列表

        列举所有Ray作业。列举工作空间下的作业，分页返回。本接口为同步接口，当前列举所有Ray作业请求下发后会返回结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRayJobs
        :type request: :class:`huaweicloudsdkaidatalake.v2.ListRayJobsRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ListRayJobsResponse`
        """
        http_info = self._list_ray_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_ray_jobs_async_invoker(self, request):
        http_info = self._list_ray_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ray_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/ray-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListRayJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'endpoint_name' in local_var_params:
            query_params.append(('endpoint_name', local_var_params['endpoint_name']))
        if 'federation_name' in local_var_params:
            query_params.append(('federation_name', local_var_params['federation_name']))
        if 'create_time_before' in local_var_params:
            query_params.append(('create_time_before', local_var_params['create_time_before']))
        if 'create_time_after' in local_var_params:
            query_params.append(('create_time_after', local_var_params['create_time_after']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'multi'

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

    def run_ray_job_async(self, request):
        r"""运行作业

        运行Ray作业。本接口为异步接口，当前运行作业请求下发成功后会返回job_id，此时运行作业并没有立即完成，需要通过调用[查看Ray作业详情](ShowRayJob.xml)查询Job状态，当Job状态为SUCCEEDED时代表运行作业成功。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunRayJob
        :type request: :class:`huaweicloudsdkaidatalake.v2.RunRayJobRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.RunRayJobResponse`
        """
        http_info = self._run_ray_job_http_info(request)
        return self._call_api(**http_info)

    def run_ray_job_async_invoker(self, request):
        http_info = self._run_ray_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_ray_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/ray-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "RunRayJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'x_client_token' in local_var_params:
            header_params['X-Client-Token'] = local_var_params['x_client_token']

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

    def show_ray_job_async(self, request):
        r"""查看Ray作业详情

        查看Ray作业详情。本接口为同步接口，当前查看Ray作业详情请求下发成功后会返回结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRayJob
        :type request: :class:`huaweicloudsdkaidatalake.v2.ShowRayJobRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowRayJobResponse`
        """
        http_info = self._show_ray_job_http_info(request)
        return self._call_api(**http_info)

    def show_ray_job_async_invoker(self, request):
        http_info = self._show_ray_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ray_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/ray-jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRayJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

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

    def close_ray_session_async(self, request):
        r"""关闭交互式会话

        关闭一个已存在的交互式会话，将会话状态设置为成功。本接口为同步接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CloseRaySession
        :type request: :class:`huaweicloudsdkaidatalake.v2.CloseRaySessionRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.CloseRaySessionResponse`
        """
        http_info = self._close_ray_session_http_info(request)
        return self._call_api(**http_info)

    def close_ray_session_async_invoker(self, request):
        http_info = self._close_ray_session_http_info(request)
        return AsyncInvoker(self, http_info)

    def _close_ray_session_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/workspaces/{workspace_id}/ray-sessions/{session_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CloseRaySessionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'session_id' in local_var_params:
            path_params['session_id'] = local_var_params['session_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def create_ray_session_async(self, request):
        r"""创建交互式会话

        创建一个交互式会话。本接口为同步接口，用于Notebook等交互式工具连接Ray集群。联邦用户认证场景下，会返回含联邦用户身份对应的凭据名称。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRaySession
        :type request: :class:`huaweicloudsdkaidatalake.v2.CreateRaySessionRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.CreateRaySessionResponse`
        """
        http_info = self._create_ray_session_http_info(request)
        return self._call_api(**http_info)

    def create_ray_session_async_invoker(self, request):
        http_info = self._create_ray_session_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_ray_session_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/ray-sessions",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRaySessionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def cancel_spark_job_async(self, request):
        r"""取消Spark作业执行

        取消正在执行的Spark作业，此接口为同步接口。调用成功后，作业将被终止执行，直接返回取消结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CancelSparkJob
        :type request: :class:`huaweicloudsdkaidatalake.v2.CancelSparkJobRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.CancelSparkJobResponse`
        """
        http_info = self._cancel_spark_job_http_info(request)
        return self._call_api(**http_info)

    def cancel_spark_job_async_invoker(self, request):
        http_info = self._cancel_spark_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _cancel_spark_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/spark-jobs/{job_id}/cancel",
            "request_type": request.__class__.__name__,
            "response_type": "CancelSparkJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

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

    def list_spark_jobs_async(self, request):
        r"""查询Spark作业列表

        查询工作空间下Spark作业列表，此接口为同步接口。支持按作业ID、作业名称、作业状态、作业类型、创建时间等条件过滤查询，支持分页查询，调用成功后直接返回作业列表数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSparkJobs
        :type request: :class:`huaweicloudsdkaidatalake.v2.ListSparkJobsRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ListSparkJobsResponse`
        """
        http_info = self._list_spark_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_spark_jobs_async_invoker(self, request):
        http_info = self._list_spark_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_spark_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/spark-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListSparkJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'create_time_after' in local_var_params:
            query_params.append(('create_time_after', local_var_params['create_time_after']))
        if 'create_time_before' in local_var_params:
            query_params.append(('create_time_before', local_var_params['create_time_before']))
        if 'endpoint_name' in local_var_params:
            query_params.append(('endpoint_name', local_var_params['endpoint_name']))
        if 'states' in local_var_params:
            query_params.append(('states', local_var_params['states']))
            collection_formats['states'] = 'multi'
        if 'job_type' in local_var_params:
            query_params.append(('job_type', local_var_params['job_type']))
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))
        if 'create_user_id' in local_var_params:
            query_params.append(('create_user_id', local_var_params['create_user_id']))
        if 'create_user_name' in local_var_params:
            query_params.append(('create_user_name', local_var_params['create_user_name']))
        if 'labels' in local_var_params:
            query_params.append(('labels', local_var_params['labels']))

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

    def run_spark_job_async(self, request):
        r"""启动Spark作业

        启动Spark作业，此接口为异步接口。支持Spark Jar作业、Python作业和SQL Script作业。调用该接口后，作业将提交到队列等待执行，返回作业ID后需通过查询作业状态接口确认作业是否成功启动。查询作业状态请参见[查询Spark作业的状态](ShowSparkJobState.xml)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunSparkJob
        :type request: :class:`huaweicloudsdkaidatalake.v2.RunSparkJobRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.RunSparkJobResponse`
        """
        http_info = self._run_spark_job_http_info(request)
        return self._call_api(**http_info)

    def run_spark_job_async_invoker(self, request):
        http_info = self._run_spark_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_spark_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/spark-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "RunSparkJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'x_client_token' in local_var_params:
            header_params['X-Client-Token'] = local_var_params['x_client_token']

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

    def show_spark_job_async(self, request):
        r"""查看Spark作业详情

        查看指定Spark作业的详细信息，此接口为同步接口。包括作业ID、作业名称、作业状态、作业配置、资源配置、镜像配置等完整信息，调用成功后直接返回作业详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSparkJob
        :type request: :class:`huaweicloudsdkaidatalake.v2.ShowSparkJobRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowSparkJobResponse`
        """
        http_info = self._show_spark_job_http_info(request)
        return self._call_api(**http_info)

    def show_spark_job_async_invoker(self, request):
        http_info = self._show_spark_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_spark_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/spark-jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSparkJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

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

    def show_spark_job_state_async(self, request):
        r"""查询Spark作业的状态

        查询Spark作业的状态，此接口为同步接口。可通过作业ID查询Spark作业的当前执行状态，包括排队中、运行中、已成功、已失败等状态，调用后立即返回作业当前状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSparkJobState
        :type request: :class:`huaweicloudsdkaidatalake.v2.ShowSparkJobStateRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowSparkJobStateResponse`
        """
        http_info = self._show_spark_job_state_http_info(request)
        return self._call_api(**http_info)

    def show_spark_job_state_async_invoker(self, request):
        http_info = self._show_spark_job_state_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_spark_job_state_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/spark-jobs/{job_id}/state",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSparkJobStateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

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

    def show_spark_operator_state_async(self, request):
        r"""查询Spark异步操作状态

        查询Spark异步操作的执行状态，用于获取异步操作（如重启集群等）的当前状态和执行结果。该接口为同步接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSparkOperatorState
        :type request: :class:`huaweicloudsdkaidatalake.v2.ShowSparkOperatorStateRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowSparkOperatorStateResponse`
        """
        http_info = self._show_spark_operator_state_http_info(request)
        return self._call_api(**http_info)

    def show_spark_operator_state_async_invoker(self, request):
        http_info = self._show_spark_operator_state_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_spark_operator_state_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/spark-operators/{operation_id}/show-state",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSparkOperatorStateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'operation_id' in local_var_params:
            path_params['operation_id'] = local_var_params['operation_id']

        query_params = []

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

    def cancel_spark_sql_async(self, request):
        r"""取消SparkSql作业执行

        取消正在运行或排队中的SparkSql作业，此接口为同步接口。只能取消处于QUEUED或RUNNING状态的作业，调用成功后直接返回取消结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CancelSparkSql
        :type request: :class:`huaweicloudsdkaidatalake.v2.CancelSparkSqlRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.CancelSparkSqlResponse`
        """
        http_info = self._cancel_spark_sql_http_info(request)
        return self._call_api(**http_info)

    def cancel_spark_sql_async_invoker(self, request):
        http_info = self._cancel_spark_sql_http_info(request)
        return AsyncInvoker(self, http_info)

    def _cancel_spark_sql_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/spark-sqls/{statement_id}/cancel",
            "request_type": request.__class__.__name__,
            "response_type": "CancelSparkSqlResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'statement_id' in local_var_params:
            path_params['statement_id'] = local_var_params['statement_id']

        query_params = []

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

    def list_spark_sqls_async(self, request):
        r"""查询SparkSql作业列表

        查询工作空间下SparkSql作业列表，此接口为同步接口。支持按作业状态、创建时间、SQL片段等条件进行过滤查询，调用成功后直接返回作业列表数据。可通过[查看SparkSql作业详情](ShowSparkSql.xml)接口查看作业详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSparkSqls
        :type request: :class:`huaweicloudsdkaidatalake.v2.ListSparkSqlsRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ListSparkSqlsResponse`
        """
        http_info = self._list_spark_sqls_http_info(request)
        return self._call_api(**http_info)

    def list_spark_sqls_async_invoker(self, request):
        http_info = self._list_spark_sqls_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_spark_sqls_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/spark-sqls",
            "request_type": request.__class__.__name__,
            "response_type": "ListSparkSqlsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'endpoint_name' in local_var_params:
            query_params.append(('endpoint_name', local_var_params['endpoint_name']))
        if 'statement' in local_var_params:
            query_params.append(('statement', local_var_params['statement']))
        if 'create_time_after' in local_var_params:
            query_params.append(('create_time_after', local_var_params['create_time_after']))
        if 'create_time_before' in local_var_params:
            query_params.append(('create_time_before', local_var_params['create_time_before']))
        if 'states' in local_var_params:
            query_params.append(('states', local_var_params['states']))
            collection_formats['states'] = 'multi'
        if 'statement_types' in local_var_params:
            query_params.append(('statement_types', local_var_params['statement_types']))
            collection_formats['statement_types'] = 'multi'
        if 'statement_id' in local_var_params:
            query_params.append(('statement_id', local_var_params['statement_id']))
        if 'create_user_id' in local_var_params:
            query_params.append(('create_user_id', local_var_params['create_user_id']))
        if 'create_user_name' in local_var_params:
            query_params.append(('create_user_name', local_var_params['create_user_name']))
        if 'labels' in local_var_params:
            query_params.append(('labels', local_var_params['labels']))

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

    def preview_spark_sql_result_async(self, request):
        r"""预览SparkSql作业查询结果

        预览SparkSql作业的查询结果，此接口为同步接口。仅适用于执行成功的DQL类型作业，可查看作业返回的数据内容，调用成功后直接返回查询结果数据。可通过[查看SparkSql作业详情](ShowSparkSql.xml)接口查看作业详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PreviewSparkSqlResult
        :type request: :class:`huaweicloudsdkaidatalake.v2.PreviewSparkSqlResultRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.PreviewSparkSqlResultResponse`
        """
        http_info = self._preview_spark_sql_result_http_info(request)
        return self._call_api(**http_info)

    def preview_spark_sql_result_async_invoker(self, request):
        http_info = self._preview_spark_sql_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _preview_spark_sql_result_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/spark-sqls/{statement_id}/preview",
            "request_type": request.__class__.__name__,
            "response_type": "PreviewSparkSqlResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'statement_id' in local_var_params:
            path_params['statement_id'] = local_var_params['statement_id']

        query_params = []

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

    def restart_spark_sql_cluster_async(self, request):
        r"""重启SparkSql集群

        重启SparkSql集群，该接口为异步接口，接口调用成功后会返回操作ID（operation_id），您可以通过查询Spark异步操作状态接口查询操作执行结果，详情请参见[查询Spark异步操作状态](ShowSparkOperatorState.xml)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestartSparkSqlCluster
        :type request: :class:`huaweicloudsdkaidatalake.v2.RestartSparkSqlClusterRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.RestartSparkSqlClusterResponse`
        """
        http_info = self._restart_spark_sql_cluster_http_info(request)
        return self._call_api(**http_info)

    def restart_spark_sql_cluster_async_invoker(self, request):
        http_info = self._restart_spark_sql_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _restart_spark_sql_cluster_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/endpoints/{endpoint_name}/spark-sqls/restart-cluster",
            "request_type": request.__class__.__name__,
            "response_type": "RestartSparkSqlClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'endpoint_name' in local_var_params:
            path_params['endpoint_name'] = local_var_params['endpoint_name']

        query_params = []

        header_params = {}

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

    def run_spark_sql_async(self, request):
        r"""执行SparkSql作业

        执行SparkSql作业，此接口为异步接口。接口调用成功后会返回作业ID（statement_id）,您可以通过查询作业状态接口查询作业执行结果，详情请参见[查询SparkSql作业的状态](ShowSparkSqlState.xml)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunSparkSql
        :type request: :class:`huaweicloudsdkaidatalake.v2.RunSparkSqlRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.RunSparkSqlResponse`
        """
        http_info = self._run_spark_sql_http_info(request)
        return self._call_api(**http_info)

    def run_spark_sql_async_invoker(self, request):
        http_info = self._run_spark_sql_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_spark_sql_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/spark-sqls",
            "request_type": request.__class__.__name__,
            "response_type": "RunSparkSqlResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'x_client_token' in local_var_params:
            header_params['X-Client-Token'] = local_var_params['x_client_token']

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

    def show_spark_sql_async(self, request):
        r"""查看SparkSql作业详情

        查看SparkSql作业的详细信息，此接口为同步接口。包括作业状态、SQL内容、执行参数等，调用成功后直接返回作业详细信息。可通过[执行SparkSql作业](RunSparkSql.xml)接口创建作业，通过[查询SparkSql作业列表](ListSparkSqls.xml)接口查询作业列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSparkSql
        :type request: :class:`huaweicloudsdkaidatalake.v2.ShowSparkSqlRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowSparkSqlResponse`
        """
        http_info = self._show_spark_sql_http_info(request)
        return self._call_api(**http_info)

    def show_spark_sql_async_invoker(self, request):
        http_info = self._show_spark_sql_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_spark_sql_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/spark-sqls/{statement_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSparkSqlResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'statement_id' in local_var_params:
            path_params['statement_id'] = local_var_params['statement_id']

        query_params = []

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

    def show_spark_sql_state_async(self, request):
        r"""查询SparkSql作业的状态

        查询SparkSql作业的状态，此接口为同步接口。可通过查询SparkSql作业列表接口获取statement_id，调用成功后直接返回作业当前状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSparkSqlState
        :type request: :class:`huaweicloudsdkaidatalake.v2.ShowSparkSqlStateRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowSparkSqlStateResponse`
        """
        http_info = self._show_spark_sql_state_http_info(request)
        return self._call_api(**http_info)

    def show_spark_sql_state_async_invoker(self, request):
        http_info = self._show_spark_sql_state_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_spark_sql_state_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/spark-sqls/{statement_id}/state",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSparkSqlStateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'statement_id' in local_var_params:
            path_params['statement_id'] = local_var_params['statement_id']

        query_params = []

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

    def batch_create_v2_resource_tags_async(self, request):
        r"""批量添加资源标签

        资源批量添加标签。此接口为同步接口，无配套使用接口。创建时，不允许设置重复key数据，如果数据库已存在该key，就覆盖value的值。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateV2ResourceTags
        :type request: :class:`huaweicloudsdkaidatalake.v2.BatchCreateV2ResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.BatchCreateV2ResourceTagsResponse`
        """
        http_info = self._batch_create_v2_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_v2_resource_tags_async_invoker(self, request):
        http_info = self._batch_create_v2_resource_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_v2_resource_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateV2ResourceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []

        header_params = {}

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

    def batch_delete_v2_resource_tags_async(self, request):
        r"""批量删除资源标签

        标签资源批量删除标签。此接口为同步接口，无配套使用接口。删除时，如果删除的标签不存在，默认处理成功，删除时不对标签字符集范围做校验。删除时tags结构体不能缺失，key不能为空或者空字符串。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteV2ResourceTags
        :type request: :class:`huaweicloudsdkaidatalake.v2.BatchDeleteV2ResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.BatchDeleteV2ResourceTagsResponse`
        """
        http_info = self._batch_delete_v2_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_v2_resource_tags_async_invoker(self, request):
        http_info = self._batch_delete_v2_resource_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_v2_resource_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteV2ResourceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []

        header_params = {}

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

    def count_v2_tag_resources_async(self, request):
        r"""查询资源实例数量

        通过标签查询资源实例数量。此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CountV2TagResources
        :type request: :class:`huaweicloudsdkaidatalake.v2.CountV2TagResourcesRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.CountV2TagResourcesResponse`
        """
        http_info = self._count_v2_tag_resources_http_info(request)
        return self._call_api(**http_info)

    def count_v2_tag_resources_async_invoker(self, request):
        http_info = self._count_v2_tag_resources_http_info(request)
        return AsyncInvoker(self, http_info)

    def _count_v2_tag_resources_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{resource_type}/resource-instances/count",
            "request_type": request.__class__.__name__,
            "response_type": "CountV2TagResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

        query_params = []
        if 'engine_types' in local_var_params:
            query_params.append(('engine_types', local_var_params['engine_types']))
            collection_formats['engine_types'] = 'multi'

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_v2_project_tags_async(self, request):
        r"""查询项目标签

        查询指定项目关联的标签列表。此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListV2ProjectTags
        :type request: :class:`huaweicloudsdkaidatalake.v2.ListV2ProjectTagsRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ListV2ProjectTagsResponse`
        """
        http_info = self._list_v2_project_tags_http_info(request)
        return self._call_api(**http_info)

    def list_v2_project_tags_async_invoker(self, request):
        http_info = self._list_v2_project_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_v2_project_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/{resource_type}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListV2ProjectTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

        query_params = []
        if 'use_predefine_tags' in local_var_params:
            query_params.append(('use_predefine_tags', local_var_params['use_predefine_tags']))
        if 'engine_types' in local_var_params:
            query_params.append(('engine_types', local_var_params['engine_types']))
            collection_formats['engine_types'] = 'multi'
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_v2_resource_tags_async(self, request):
        r"""查询资源标签

        查询资源的标签。用于查询资源的标签，返回对应资源的标签。此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListV2ResourceTags
        :type request: :class:`huaweicloudsdkaidatalake.v2.ListV2ResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ListV2ResourceTagsResponse`
        """
        http_info = self._list_v2_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def list_v2_resource_tags_async_invoker(self, request):
        http_info = self._list_v2_resource_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_v2_resource_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListV2ResourceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_v2_tag_resources_async(self, request):
        r"""查询资源实例列表

        通过标签查询资源列表。此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListV2TagResources
        :type request: :class:`huaweicloudsdkaidatalake.v2.ListV2TagResourcesRequest`
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ListV2TagResourcesResponse`
        """
        http_info = self._list_v2_tag_resources_http_info(request)
        return self._call_api(**http_info)

    def list_v2_tag_resources_async_invoker(self, request):
        http_info = self._list_v2_tag_resources_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_v2_tag_resources_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{resource_type}/resource-instances/filter",
            "request_type": request.__class__.__name__,
            "response_type": "ListV2TagResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

        query_params = []
        if 'engine_types' in local_var_params:
            query_params.append(('engine_types', local_var_params['engine_types']))
            collection_formats['engine_types'] = 'multi'
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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
