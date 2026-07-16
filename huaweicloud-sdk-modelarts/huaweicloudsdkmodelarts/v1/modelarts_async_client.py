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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkmodelarts'")


class ModelArtsAsyncClient(Client):
    def __init__(self):
        super().__init__()
        self.model_package = importlib.import_module("huaweicloudsdkmodelarts.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "ModelArtsAsyncClient":
                raise TypeError("client type error, support client type is ModelArtsAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def accept_scheduled_event_async(self, request):
        r"""计划事件授权

        计划事件授权接口用于为指定的计划事件分配或调整权限。该接口适用于以下场景：当创建新的计划事件、调整现有计划事件的权限设置或变更权限分配时，用户可通过此接口为指定的计划事件授予或修改权限。使用该接口的前提条件是计划事件已存在且用户具有管理员权限。授权操作完成后，计划事件的权限设置将被更新，相关变更将被记录以便审计。若计划事件不存在、用户无权限操作或授权信息格式不正确，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AcceptScheduledEvent
        :type request: :class:`huaweicloudsdkmodelarts.v1.AcceptScheduledEventRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.AcceptScheduledEventResponse`
        """
        http_info = self._accept_scheduled_event_http_info(request)
        return self._call_api(**http_info)

    def accept_scheduled_event_async_invoker(self, request):
        http_info = self._accept_scheduled_event_http_info(request)
        return AsyncInvoker(self, http_info)

    def _accept_scheduled_event_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/scheduled-events/{event_id}/accept",
            "request_type": request.__class__.__name__,
            "response_type": "AcceptScheduledEventResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'event_id' in local_var_params:
            path_params['event_id'] = local_var_params['event_id']

        query_params = []
        if 'workspace_id' in local_var_params:
            query_params.append(('workspaceId', local_var_params['workspace_id']))
        if 'workspace_id2' in local_var_params:
            query_params.append(('workspaceId', local_var_params['workspace_id2']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def attach_dynamic_storage_async(self, request):
        r"""动态挂载Notebook存储

        动态挂载Notebook存储接口支持将存储动态挂载到运行中的Notebook实例的指定文件目录。调用该接口后，系统将在Notebook实例中**异步**挂载指定的存储实例，挂载完成后用户可在容器中以文件系统方式读写存储实例中的文件。若用户无权限访问指定实例或Notebook实例未运行，接口将返回相应的错误信息。
        
        支持的存储类型：
        - **对象存储 OBS**：适合直接使用OBS桶作为持久化存储进行AI开发和探索场景，但小文件频繁读写性能较差，**模型训练，大文件解压等场景慎用，此类场景可能会导致Notebook文件操作卡顿**。
        - **并行文件系统 PFS**：高性能对象存储文件系统，存储成本低，吞吐量大，能够快速处理高性能计算（HPC）工作负载，**但小文件频繁读写较弱。小文件频繁读写场景可能会导致Notebook文件操作卡顿**
        - **高性能弹性文件服务SFS Turbo**：仅支持专属资源池实例挂载，**挂载前需要在资源池网络管理界面中进行网络关联**，支持多个环境使用，可以在多个开发环境、开发环境和训练之间共享。适合探索、实验等非正式生产场景，但不适合重IO读写模型。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AttachDynamicStorage
        :type request: :class:`huaweicloudsdkmodelarts.v1.AttachDynamicStorageRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.AttachDynamicStorageResponse`
        """
        http_info = self._attach_dynamic_storage_http_info(request)
        return self._call_api(**http_info)

    def attach_dynamic_storage_async_invoker(self, request):
        http_info = self._attach_dynamic_storage_http_info(request)
        return AsyncInvoker(self, http_info)

    def _attach_dynamic_storage_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/notebooks/{instance_id}/storage",
            "request_type": request.__class__.__name__,
            "response_type": "AttachDynamicStorageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_bind_infer_api_keys_async(self, request):
        r"""批量绑定应用密钥

        本接口用于将生成的多个apikey与指定服务进行批量绑定，用于访问特定服务。调用此接口前，确保已成功创建服务实例，并获取到有效的apikey。绑定成功后，apikey将作为服务调用时的身份验证凭证，确保仅授权用户能够访问该服务。如果尝试绑定已失效或已绑定当前服务的apikey将返回相应的异常信息，提示用户检查apikey的有效性和绑定状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchBindInferApiKeys
        :type request: :class:`huaweicloudsdkmodelarts.v1.BatchBindInferApiKeysRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.BatchBindInferApiKeysResponse`
        """
        http_info = self._batch_bind_infer_api_keys_http_info(request)
        return self._call_api(**http_info)

    def batch_bind_infer_api_keys_async_invoker(self, request):
        http_info = self._batch_bind_infer_api_keys_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_bind_infer_api_keys_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/services/{service_id}/api-keys/batch-bind",
            "request_type": request.__class__.__name__,
            "response_type": "BatchBindInferApiKeysResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

        query_params = []

        header_params = {}

        form_params = {}
        if 'key_ids' in local_var_params:
            form_params['key_ids'] = local_var_params['key_ids']
            collection_formats['key_ids'] = 'csv'

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/x-www-form-urlencoded'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_bind_pool_nodes_async(self, request):
        r"""批量为节点绑定逻辑子池

        批量为节点绑定逻辑子池接口用于在物理专属池开启节点绑定功能时，对逻辑子池中的节点进行逻辑子池的换绑操作。该接口适用于以下场景：当需要重新分配资源、调整业务负载或优化资源使用效率时，用户可通过此接口将指定节点从当前逻辑子池迁移到另一个逻辑子池。使用该接口的前提条件是物理专属池已开启节点绑定功能，且目标逻辑子池已存在并具备足够的资源容量。绑定操作完成后，节点将从原逻辑子池解绑并绑定到目标逻辑子池，原逻辑子池的节点数减少，目标逻辑子池的节点数增加。若节点未绑定到任何逻辑子池、目标逻辑子池不存在或资源不足，或用户无权限操作，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchBindPoolNodes
        :type request: :class:`huaweicloudsdkmodelarts.v1.BatchBindPoolNodesRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.BatchBindPoolNodesResponse`
        """
        http_info = self._batch_bind_pool_nodes_http_info(request)
        return self._call_api(**http_info)

    def batch_bind_pool_nodes_async_invoker(self, request):
        http_info = self._batch_bind_pool_nodes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_bind_pool_nodes_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/pools/{pool_name}/nodes/batch-bind",
            "request_type": request.__class__.__name__,
            "response_type": "BatchBindPoolNodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']

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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_create_pool_tags_async(self, request):
        r"""批量创建资源池标签

        批量创建资源池标签接口用于为指定资源池添加或更新多个标签信息。该接口适用于以下场景：当需要对资源池进行统一分类管理（如成本归属、环境标识）、批量配置元数据（如项目归属、负责人信息）或更新已有标签值时，管理员可通过此接口一次性操作多个标签。使用该接口的前提条件是目标资源池必须已存在且处于可管理状态，调用者需具备资源池标签管理权限，且提交的标签数据需符合格式规范（如key非空、value长度限制）。操作完成后，系统将为资源池添加新标签或覆盖同名标签的值，且不会影响资源池的其他配置属性。若资源池不存在、用户权限不足、标签格式错误或系统服务异常，接口将返回对应的错误信息（如\&quot;404 Not Found\&quot;、\&quot;403 Forbidden\&quot;、\&quot;400 Bad Request\&quot;或\&quot;503 Service Unavailable\&quot;）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreatePoolTags
        :type request: :class:`huaweicloudsdkmodelarts.v1.BatchCreatePoolTagsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.BatchCreatePoolTagsResponse`
        """
        http_info = self._batch_create_pool_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_pool_tags_async_invoker(self, request):
        http_info = self._batch_create_pool_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_pool_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/pools/{pool_name}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreatePoolTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']

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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_infer_intranet_connections_async(self, request):
        r"""批量删除内网接入

        本接口用于批量删除指定的内网接入点，适用于需要清理多个不再使用的内网接入点的场景。调用此接口前，确保已具备相应的删除权限，并提供一个有效的内网接入点ID列表。删除成功后，所指定的内网接入点将被彻底移除，不再对任何服务生效。如果提供的内网接入点ID列表中包含无效或已删除的ID，将返回相应的异常信息，提示用户检查ID的有效性。此外，如果调用时出现权限不足或其他系统异常，也将返回相应的异常信息，提示用户检查权限或联系技术支持。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteInferIntranetConnections
        :type request: :class:`huaweicloudsdkmodelarts.v1.BatchDeleteInferIntranetConnectionsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.BatchDeleteInferIntranetConnectionsResponse`
        """
        http_info = self._batch_delete_infer_intranet_connections_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_infer_intranet_connections_async_invoker(self, request):
        http_info = self._batch_delete_infer_intranet_connections_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_infer_intranet_connections_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/intranet-connection/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteInferIntranetConnectionsResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_infer_services_async(self, request):
        r"""删除指定服务列表

        删除指定服务列表功能允许用户批量删除多个服务，适用于需要清理资源、释放计算能力或管理多个服务的场景。使用此功能前，请确保您具备删除服务的权限，并提供有效的服务ID列表。成功执行后，指定的服务将被终止运行并释放相关资源。若服务ID无效、权限不足或服务状态不允许删除，将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteInferServices
        :type request: :class:`huaweicloudsdkmodelarts.v1.BatchDeleteInferServicesRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.BatchDeleteInferServicesResponse`
        """
        http_info = self._batch_delete_infer_services_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_infer_services_async_invoker(self, request):
        http_info = self._batch_delete_infer_services_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_infer_services_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/services/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteInferServicesResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_pool_nodes_async(self, request):
        r"""批量删除节点

        批量删除节点接口用于批量删除指定资源池中的节点。该接口适用于以下场景：当需要清理资源池中的冗余节点、重新分配资源或移除故障节点时，用户可通过此接口批量删除指定的节点。使用该接口的前提条件是资源池已创建且处于可用状态，用户具有删除节点的权限，且资源池中至少保留一个节点。删除操作完成后，指定的节点将被永久移除，资源池中剩余的节点将继续提供服务。若资源池不存在、节点不存在、用户无权限操作或资源池中节点不足，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeletePoolNodes
        :type request: :class:`huaweicloudsdkmodelarts.v1.BatchDeletePoolNodesRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.BatchDeletePoolNodesResponse`
        """
        http_info = self._batch_delete_pool_nodes_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_pool_nodes_async_invoker(self, request):
        http_info = self._batch_delete_pool_nodes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_pool_nodes_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/pools/{pool_name}/nodes/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeletePoolNodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']

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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_pool_tags_async(self, request):
        r"""批量删除资源池标签

        批量删除资源标签接口用于移除指定资源上的多个标签信息。该接口适用于以下场景：当需要清理冗余标签（如过期分类、无效元数据）、统一调整资源分类策略或因权限变更需批量移除标签时，管理员可通过此接口一次性删除多个标签。使用该接口的前提条件是目标资源必须已存在且处于可管理状态，调用者需具备资源标签管理权限，且待删除的标签必须已关联至该资源，系统标签管理服务需正常运行。操作完成后，指定标签将从资源中彻底移除，且不会影响资源的其他配置属性。若资源不存在、用户权限不足、标签未关联或系统服务异常，接口将返回对应的错误信息（如\&quot;404 Not Found\&quot;、\&quot;403 Forbidden\&quot;、\&quot;400 Bad Request\&quot;或\&quot;503 Service Unavailable\&quot;）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeletePoolTags
        :type request: :class:`huaweicloudsdkmodelarts.v1.BatchDeletePoolTagsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.BatchDeletePoolTagsResponse`
        """
        http_info = self._batch_delete_pool_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_pool_tags_async_invoker(self, request):
        http_info = self._batch_delete_pool_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_pool_tags_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/pools/{pool_name}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeletePoolTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']

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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_lock_pool_nodes_async(self, request):
        r"""批量对节点功能上锁

        批量对节点功能上锁接口用于批量对指定节点的功能进行上锁操作，被上锁的功能在控制台将无法正常使用。该接口适用于以下场景：当需要临时禁用某些节点的功能以防止误操作、进行系统维护或测试时，用户可通过此接口批量对节点功能进行上锁。使用该接口的前提条件是节点功能已存在且用户具有管理员权限。上锁操作完成后，指定节点的功能将在控制台被禁用，无法进行相关操作。若节点功能不存在、用户无权限操作或请求参数无效，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchLockPoolNodes
        :type request: :class:`huaweicloudsdkmodelarts.v1.BatchLockPoolNodesRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.BatchLockPoolNodesResponse`
        """
        http_info = self._batch_lock_pool_nodes_http_info(request)
        return self._call_api(**http_info)

    def batch_lock_pool_nodes_async_invoker(self, request):
        http_info = self._batch_lock_pool_nodes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_lock_pool_nodes_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/pools/{pool_name}/nodes/batch-lock",
            "request_type": request.__class__.__name__,
            "response_type": "BatchLockPoolNodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']

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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_migrate_pool_nodes_async(self, request):
        r"""批量迁移节点

        批量迁移节点接口用于在资源池之间批量迁移节点，将节点从一个资源池迁移到另一个资源池。该接口适用于以下场景：当资源池的节点分布不均衡、需要进行集群维护或业务扩展时，用户可通过此接口将指定节点从一个资源池迁移到另一个资源池。使用该接口的前提条件是资源池中至少包含两个节点，且目标资源池具备足够的资源容量（如IP地址等）以接收迁移节点。若资源池只有一个节点、目标集群资源不足、节点状态不支持迁移或用户无权限操作，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchMigratePoolNodes
        :type request: :class:`huaweicloudsdkmodelarts.v1.BatchMigratePoolNodesRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.BatchMigratePoolNodesResponse`
        """
        http_info = self._batch_migrate_pool_nodes_http_info(request)
        return self._call_api(**http_info)

    def batch_migrate_pool_nodes_async_invoker(self, request):
        http_info = self._batch_migrate_pool_nodes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_migrate_pool_nodes_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/pools/{pool_name}/nodes/batch-migrate",
            "request_type": request.__class__.__name__,
            "response_type": "BatchMigratePoolNodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']

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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_reboot_pool_nodes_async(self, request):
        r"""批量重启节点

        批量重启节点接口用于批量重启指定资源池中的节点。该接口适用于以下场景：当需要对资源池中的节点进行系统更新、配置变更、故障恢复或维护操作时，用户可通过此接口批量重启指定的节点。使用该接口的前提条件是资源池已创建且处于可用状态，节点属于该资源池且处于运行状态，且用户具有重启节点的权限。重启操作完成后，指定的节点将被重新启动，资源池中的其他节点将继续正常运行。若资源池不存在、节点不在资源池中、节点未处于运行状态或用户无权限操作，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchRebootPoolNodes
        :type request: :class:`huaweicloudsdkmodelarts.v1.BatchRebootPoolNodesRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.BatchRebootPoolNodesResponse`
        """
        http_info = self._batch_reboot_pool_nodes_http_info(request)
        return self._call_api(**http_info)

    def batch_reboot_pool_nodes_async_invoker(self, request):
        http_info = self._batch_reboot_pool_nodes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_reboot_pool_nodes_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/pools/{pool_name}/nodes/batch-reboot",
            "request_type": request.__class__.__name__,
            "response_type": "BatchRebootPoolNodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']

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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_reset_pool_nodes_async(self, request):
        r"""重置节点

        重置节点接口用于将指定节点恢复到初始状态，清除节点上的数据和配置。该接口适用于以下场景：当节点出现故障、配置错误、需要重新部署或进行系统恢复时，用户可通过此接口重置节点，使其恢复到出厂或初始状态。使用该接口的前提条件是节点已存在且用户具有管理员权限。重置操作完成后，节点上的所有数据和配置将被清除，节点将被重新启动并恢复到初始状态。若节点不存在、用户无权限操作或节点处于不可重置状态（如正在运行任务），接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchResetPoolNodes
        :type request: :class:`huaweicloudsdkmodelarts.v1.BatchResetPoolNodesRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.BatchResetPoolNodesResponse`
        """
        http_info = self._batch_reset_pool_nodes_http_info(request)
        return self._call_api(**http_info)

    def batch_reset_pool_nodes_async_invoker(self, request):
        http_info = self._batch_reset_pool_nodes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_reset_pool_nodes_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/pools/{pool_name}/nodes/batch-reset",
            "request_type": request.__class__.__name__,
            "response_type": "BatchResetPoolNodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']

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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_resize_pool_nodes_async(self, request):
        r"""节点规格变更

        节点规格变更接口用于调整指定节点的规格（如步长），例如将节点从8节点超节点扩容到16节点超节点。该接口适用于以下场景：当需要根据业务需求调整节点的资源容量、优化资源利用率或进行系统升级时，用户可通过此接口变更节点的规格。使用该接口的前提条件是节点已创建且处于可变更状态，目标规格在支持范围内，且用户具有管理员权限。规格变更完成后，节点的资源容量将按新规格调整，相关服务和配置将重新加载以适应新的规格。若节点不存在、节点状态不允许变更、目标规格不支持或用户无权限操作，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchResizePoolNodes
        :type request: :class:`huaweicloudsdkmodelarts.v1.BatchResizePoolNodesRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.BatchResizePoolNodesResponse`
        """
        http_info = self._batch_resize_pool_nodes_http_info(request)
        return self._call_api(**http_info)

    def batch_resize_pool_nodes_async_invoker(self, request):
        http_info = self._batch_resize_pool_nodes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_resize_pool_nodes_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/pools/{pool_name}/nodes/batch-resize",
            "request_type": request.__class__.__name__,
            "response_type": "BatchResizePoolNodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']

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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_unbind_infer_api_keys_async(self, request):
        r"""批量解绑应用密钥

        本接口用于将已绑定的apikey从指定服务中批量解绑，适用于需要撤销多个apikey对特定服务的访问权限的场景。调用此接口前，确保已获取到需要解绑的多个apikey，并确认这些apikey当前绑定在指定服务上。解绑成功后，这些apikey将不再对指定服务生效，但仍可继续用于其他服务。如果尝试解绑不存在或未绑定到指定服务的apikey，将返回相应的异常信息，提示用户检查apikey的有效性和绑定状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchUnbindInferApiKeys
        :type request: :class:`huaweicloudsdkmodelarts.v1.BatchUnbindInferApiKeysRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.BatchUnbindInferApiKeysResponse`
        """
        http_info = self._batch_unbind_infer_api_keys_http_info(request)
        return self._call_api(**http_info)

    def batch_unbind_infer_api_keys_async_invoker(self, request):
        http_info = self._batch_unbind_infer_api_keys_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_unbind_infer_api_keys_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/services/{service_id}/api-keys/batch-unbind",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUnbindInferApiKeysResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

        query_params = []

        header_params = {}

        form_params = {}
        if 'key_ids' in local_var_params:
            form_params['key_ids'] = local_var_params['key_ids']
            collection_formats['key_ids'] = 'csv'

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/x-www-form-urlencoded'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_unlock_pool_nodes_async(self, request):
        r"""批量对节点功能解锁

        批量对节点功能解锁接口用于批量解除指定节点功能的锁定状态，使被上锁的功能在控制台恢复正常可用状态。该接口适用于以下场景：当需要恢复被锁定的节点功能以正常使用、完成系统维护或测试后，用户可通过此接口批量对节点功能进行解锁。使用该接口的前提条件是节点功能已被上锁且用户具有管理员权限。解锁操作完成后，指定节点的功能将在控制台恢复正常，用户可以正常使用相关功能。若节点功能未被锁定、用户无权限操作或请求参数无效，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchUnlockPoolNodes
        :type request: :class:`huaweicloudsdkmodelarts.v1.BatchUnlockPoolNodesRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.BatchUnlockPoolNodesResponse`
        """
        http_info = self._batch_unlock_pool_nodes_http_info(request)
        return self._call_api(**http_info)

    def batch_unlock_pool_nodes_async_invoker(self, request):
        http_info = self._batch_unlock_pool_nodes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_unlock_pool_nodes_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/pools/{pool_name}/nodes/batch-unlock",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUnlockPoolNodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']

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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_update_pool_nodes_async(self, request):
        r"""批量更新节点

        批量更新节点接口用于同时修改多个节点的配置或属性，支持批量操作时各节点独立执行更新流程。该接口适用于以下场景：当用户需统一升级节点软件版本、批量处理选中节点的资源标签、调整资源分配策略、应用安全补丁或同步配置变更时，可通过此接口批量更新目标节点，确保每个节点的更新过程互不影响。使用该接口的前提条件包括：目标节点已存在且用户具备管理员权限，节点需处于可操作状态（如非锁定或维护中），批量操作时需提供有效的节点列表及更新参数（如配置项、版本号等）作为输入。操作完成后，指定节点将应用新配置并更新状态为可用，原有配置将被覆盖。若节点不存在、用户权限不足、节点状态异常（如正在维护）、更新参数不合规或输入参数缺失，接口将返回对应错误信息（如404未找到节点、403权限拒绝、400参数校验失败等）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchUpdatePoolNodes
        :type request: :class:`huaweicloudsdkmodelarts.v1.BatchUpdatePoolNodesRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.BatchUpdatePoolNodesResponse`
        """
        http_info = self._batch_update_pool_nodes_http_info(request)
        return self._call_api(**http_info)

    def batch_update_pool_nodes_async_invoker(self, request):
        http_info = self._batch_update_pool_nodes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_update_pool_nodes_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/pools/{pool_name}/nodes/batch-update",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdatePoolNodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']

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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def bind_infer_api_key_async(self, request):
        r"""绑定应用密钥

        本接口用于将生成的apikey与指定服务进行绑定，适用于应用程序需要调用特定服务的场景。调用此接口前，确保已成功创建服务实例，并获取到有效的apikey。绑定成功后，apikey将作为服务调用时的身份验证凭证，确保仅授权用户能够访问该服务。如果尝试绑定已失效的apikey，将返回相应的异常信息，提示用户检查apikey的有效性和绑定状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BindInferApiKey
        :type request: :class:`huaweicloudsdkmodelarts.v1.BindInferApiKeyRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.BindInferApiKeyResponse`
        """
        http_info = self._bind_infer_api_key_http_info(request)
        return self._call_api(**http_info)

    def bind_infer_api_key_async_invoker(self, request):
        http_info = self._bind_infer_api_key_http_info(request)
        return AsyncInvoker(self, http_info)

    def _bind_infer_api_key_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/services/{service_id}/api-keys/{key_id}/bind",
            "request_type": request.__class__.__name__,
            "response_type": "BindInferApiKeyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'key_id' in local_var_params:
            path_params['key_id'] = local_var_params['key_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def cancel_infer_deployment_async(self, request):
        r"""中断服务部署

        中断服务部署接口用于中断处于“升级中”或“部署中”状态的部署，使其快速停止。该接口适用于以下场景：当部署出现严重故障需要立即修复、资源需要快速释放以部署更高优先级的部署，或在测试环境中需要快速迭代时，用户可通过此接口中断指定部署。使用该接口的前提条件是部署当前状态为“升级中”或“部署中”，且用户具有中断部署的权限。若部署为“部署中”状态，执行中断操作，部署状态将变成“停止”，相关资源将被释放，且终端操作将被记录；若部署为“升级中”状态，执行中断操作，部署状态将变成“运行中”。若部署当前状态不是“升级中”或“部署中”，若用户无权限操作，接口将返回相应的错误信息。若部署ID无效、版本号不存在或用户无权限，则返回400 Bad Request或403 Forbidden；
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CancelInferDeployment
        :type request: :class:`huaweicloudsdkmodelarts.v1.CancelInferDeploymentRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CancelInferDeploymentResponse`
        """
        http_info = self._cancel_infer_deployment_http_info(request)
        return self._call_api(**http_info)

    def cancel_infer_deployment_async_invoker(self, request):
        http_info = self._cancel_infer_deployment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _cancel_infer_deployment_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/services/{service_id}/deployments/{deployment_id}/interrupt",
            "request_type": request.__class__.__name__,
            "response_type": "CancelInferDeploymentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def change_algorithm_async(self, request):
        r"""更新算法

        更新算法。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeAlgorithm
        :type request: :class:`huaweicloudsdkmodelarts.v1.ChangeAlgorithmRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ChangeAlgorithmResponse`
        """
        http_info = self._change_algorithm_http_info(request)
        return self._call_api(**http_info)

    def change_algorithm_async_invoker(self, request):
        http_info = self._change_algorithm_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_algorithm_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/algorithms/{algorithm_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeAlgorithmResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'algorithm_id' in local_var_params:
            path_params['algorithm_id'] = local_var_params['algorithm_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def change_training_experiment_async(self, request):
        r"""更新训练实验信息

        通过实验ID更新训练实验信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeTrainingExperiment
        :type request: :class:`huaweicloudsdkmodelarts.v1.ChangeTrainingExperimentRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ChangeTrainingExperimentResponse`
        """
        http_info = self._change_training_experiment_http_info(request)
        return self._call_api(**http_info)

    def change_training_experiment_async_invoker(self, request):
        http_info = self._change_training_experiment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_training_experiment_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/training-experiments/{experiment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeTrainingExperimentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'experiment_id' in local_var_params:
            path_params['experiment_id'] = local_var_params['experiment_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def change_training_job_description_async(self, request):
        r"""更新训练作业描述

        更新训练作业描述。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeTrainingJobDescription
        :type request: :class:`huaweicloudsdkmodelarts.v1.ChangeTrainingJobDescriptionRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ChangeTrainingJobDescriptionResponse`
        """
        http_info = self._change_training_job_description_http_info(request)
        return self._call_api(**http_info)

    def change_training_job_description_async_invoker(self, request):
        http_info = self._change_training_job_description_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_training_job_description_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/training-jobs/{training_job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeTrainingJobDescriptionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'training_job_id' in local_var_params:
            path_params['training_job_id'] = local_var_params['training_job_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def check_training_experiment_async(self, request):
        r"""校验训练实验名称

        校验训练实验名称接口用于新增训练实验前校验训练实验名称是否重复。
        该接口适用于以下场景：当用户需要创建新的训练实验时，可以通过此接口校验定义的实验名称是否已存在。使用该接口的前提条件是用户具有创建实验的权限。查询操作完成后，将返回实验名称是否重复的结果。若用户无权限操作，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckTrainingExperiment
        :type request: :class:`huaweicloudsdkmodelarts.v1.CheckTrainingExperimentRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CheckTrainingExperimentResponse`
        """
        http_info = self._check_training_experiment_http_info(request)
        return self._call_api(**http_info)

    def check_training_experiment_async_invoker(self, request):
        http_info = self._check_training_experiment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_training_experiment_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/training-experiment-names",
            "request_type": request.__class__.__name__,
            "response_type": "CheckTrainingExperimentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))
        if 'experiment_name' in local_var_params:
            query_params.append(('experiment_name', local_var_params['experiment_name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def count_infer_services_by_tags_async(self, request):
        r"""通过标签查询资源数量

        该接口适用于需要统计和获取符合特定标签或资源名称条件的资源数量的场景，例如在资源管理和监控中，用户可以通过指定标签或资源名称进行精确或模糊查询来统计资源数量。通过调用此接口，用户可以基于多个标签或资源名称进行查询，若不传标签则返回所有资源的总数。用户必须具有足够的权限，且目标资源需存在。查询成功后，返回符合条件的资源总数；若失败，返回具体的错误信息。常见异常包括权限验证错误、资源不存在错误和参数验证错误。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CountInferServicesByTags
        :type request: :class:`huaweicloudsdkmodelarts.v1.CountInferServicesByTagsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CountInferServicesByTagsResponse`
        """
        http_info = self._count_infer_services_by_tags_http_info(request)
        return self._call_api(**http_info)

    def count_infer_services_by_tags_async_invoker(self, request):
        http_info = self._count_infer_services_by_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _count_infer_services_by_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/modelarts-service-v2/resource-instances/count",
            "request_type": request.__class__.__name__,
            "response_type": "CountInferServicesByTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))

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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_algorithm_async(self, request):
        r"""创建算法

        创建一个算法。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAlgorithm
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateAlgorithmRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateAlgorithmResponse`
        """
        http_info = self._create_algorithm_http_info(request)
        return self._call_api(**http_info)

    def create_algorithm_async_invoker(self, request):
        http_info = self._create_algorithm_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_algorithm_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/algorithms",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAlgorithmResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_algorithm_version_to_gallery_async(self, request):
        r"""创建发布算法资产

        创建发布算法资产接口用于在算法管理中创建并发布新的算法资产。
        该接口适用于以下场景：当用户开发完成新的算法并希望将其发布为可复用的算法资产时，可以通过此接口创建并发布算法资产。使用该接口的前提条件是用户已登录且具有创建和发布算法资产的权限。创建发布操作完成后，系统将生成新的算法资产，并将其添加到算法资产列表中，用户可以通过算法ID进行管理和调用。若用户无权限操作、算法资产信息不完整或已存在相同名称的算法资产，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAlgorithmVersionToGallery
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateAlgorithmVersionToGalleryRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateAlgorithmVersionToGalleryResponse`
        """
        http_info = self._create_algorithm_version_to_gallery_http_info(request)
        return self._call_api(**http_info)

    def create_algorithm_version_to_gallery_async_invoker(self, request):
        http_info = self._create_algorithm_version_to_gallery_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_algorithm_version_to_gallery_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/gallery-algorithm-publication",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAlgorithmVersionToGalleryResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_authorization_async(self, request):
        r"""配置授权

        配置授权接口用于配置ModelArts的授权。该接口适用于以下场景：当需要为IAM子用户设置访问ModelArts的权限时，管理员可通过此接口配置授权。使用该接口的前提条件是管理员具备IAM系统的Security Administrator权限，并且需要为子用户设置访问密钥。配置完成后，子用户将被授予访问ModelArts资源的权限，从而能够正常使用训练管理、开发环境、数据管理、在线服务等功能。若管理员无权限操作或子用户不存在，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAuthorization
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateAuthorizationRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateAuthorizationResponse`
        """
        http_info = self._create_authorization_http_info(request)
        return self._call_api(**http_info)

    def create_authorization_async_invoker(self, request):
        http_info = self._create_authorization_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_authorization_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/authorizations",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAuthorizationResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_infer_api_key_async(self, request):
        r"""创建应用密钥

        本接口用于在系统中创建一个新的API_KEY，适用于需要为用户或应用程序生成访问凭证的场景。调用此接口前，确保已具备相应的创建权限，并提供必要的参数，如用户ID或应用程序ID。创建成功后，系统将生成一个唯一的API_KEY，并返回该API_KEY的详细信息，包括API_KEY值、创建时间等。如果提供的参数无效或系统中已存在相同的API_KEY，将返回相应的异常信息，提示用户检查输入数据的有效性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInferApiKey
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateInferApiKeyRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateInferApiKeyResponse`
        """
        http_info = self._create_infer_api_key_http_info(request)
        return self._call_api(**http_info)

    def create_infer_api_key_async_invoker(self, request):
        http_info = self._create_infer_api_key_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_infer_api_key_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/services/api-keys",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInferApiKeyResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_infer_deployment_async(self, request):
        r"""添加部署

        将模型部署为在线服务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInferDeployment
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateInferDeploymentRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateInferDeploymentResponse`
        """
        http_info = self._create_infer_deployment_http_info(request)
        return self._call_api(**http_info)

    def create_infer_deployment_async_invoker(self, request):
        http_info = self._create_infer_deployment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_infer_deployment_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/services/{service_id}/deployments",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInferDeploymentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_infer_intranet_connection_async(self, request):
        r"""创建内网接入

        本接口用于在指定Region中创建内网接入点，适用于需要为应用程序或服务配置内网连接的场景。调用此接口前，确保已具备相应的创建权限，并提供必要的参数，如Region ID、内网接入点名称和网络配置信息。创建成功后，系统将生成一个内网接入点，并返回该接入点的详细信息，包括接入点ID、创建时间、状态等。如果提供的参数无效或内网接入配置冲突，将返回相应的异常信息，提示用户检查输入数据的有效性和配置冲突情况。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInferIntranetConnection
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateInferIntranetConnectionRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateInferIntranetConnectionResponse`
        """
        http_info = self._create_infer_intranet_connection_http_info(request)
        return self._call_api(**http_info)

    def create_infer_intranet_connection_async_invoker(self, request):
        http_info = self._create_infer_intranet_connection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_infer_intranet_connection_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/intranet-connection",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInferIntranetConnectionResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_infer_service_async(self, request):
        r"""创建服务

        将模型部署为在线服务，适用于用户在开发或运维过程中需要将训练好的模型部署为在线服务，以便通过API或HTTP接口提供预测或处理能力的场景。调用此接口前，用户必须具有创建服务的权限，并提供合法的模型镜像路径和完整的服务配置信息（如服务名称、模型镜像路径、资源配置、升级配置等）。调用成功后，系统将成功创建并部署服务，服务状态变为“部署中”，并生成服务的唯一ID返回给用户。服务的详细信息（如状态、创建时间、更新时间等）也会记录在系统中。如果用户没有创建服务的权限，或提供的模型镜像路径不合法，或服务配置信息不完整，调用将返回相应的错误信息。如果系统在部署过程中遇到资源不足或其他内部错误，也将返回错误信息并记录日志。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInferService
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateInferServiceRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateInferServiceResponse`
        """
        http_info = self._create_infer_service_http_info(request)
        return self._call_api(**http_info)

    def create_infer_service_async_invoker(self, request):
        http_info = self._create_infer_service_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_infer_service_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/services",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInferServiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_auth_token_provider' in local_var_params:
            header_params['X-Auth-Token-Provider'] = local_var_params['x_auth_token_provider']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_infer_service_tag_async(self, request):
        r"""添加标签

        该接口适用于需要为资源（如模型、数据集、服务等）添加元数据标签的场景，例如在资源管理或分类中，用户可以通过添加标签来标注资源的用途、状态或其他属性。通过调用此接口，用户可以批量添加标签，如果标签key已存在，则更新其value。用户必须具有足够的权限，且目标资源需存在。添加成功后，资源将包含新的标签信息；若失败，返回具体的错误信息。常见异常包括权限验证错误、资源不存在错误和参数验证错误。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInferServiceTag
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateInferServiceTagRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateInferServiceTagResponse`
        """
        http_info = self._create_infer_service_tag_http_info(request)
        return self._call_api(**http_info)

    def create_infer_service_tag_async_invoker(self, request):
        http_info = self._create_infer_service_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_infer_service_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/modelarts-service-v2/{resource_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInferServiceTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_model_arts_agency_async(self, request):
        r"""创建ModelArts委托

        创建ModelArts委托接口用于创建包含OBS、SWR、IEF等依赖服务的ModelArts委托。该接口适用于以下场景：当需要配置ModelArts访问OBS、SWR、IEF等服务的权限时，用户可通过此接口创建委托。使用该接口的前提条件是用户具备创建委托的权限，并且需要在IAM系统中具备相应的权限。创建完成后，ModelArts将被授权访问OBS、SWR、IEF等服务，从而能够正常执行数据存储、镜像拉取、模型部署等功能。若用户无权限创建委托或依赖服务未配置，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateModelArtsAgency
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateModelArtsAgencyRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateModelArtsAgencyResponse`
        """
        http_info = self._create_model_arts_agency_http_info(request)
        return self._call_api(**http_info)

    def create_model_arts_agency_async_invoker(self, request):
        http_info = self._create_model_arts_agency_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_model_arts_agency_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/agency",
            "request_type": request.__class__.__name__,
            "response_type": "CreateModelArtsAgencyResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_network_async(self, request):
        r"""创建网络资源

        创建网络资源接口用于在系统中创建新的网络资源。该接口适用于以下场景：当需要为业务扩展、资源规划或网络架构调整时，用户可通过此接口创建新的网络资源，如虚拟网络、子网或路由等。使用该接口的前提条件是用户具有管理员权限，并且系统中具备足够的资源支持新网络资源的创建。创建操作完成后，新的网络资源将被成功添加到系统中，并可用于后续的业务配置。若用户无权限、资源不足或输入参数有误，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateNetwork
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateNetworkRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateNetworkResponse`
        """
        http_info = self._create_network_http_info(request)
        return self._call_api(**http_info)

    def create_network_async_invoker(self, request):
        http_info = self._create_network_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_network_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/networks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateNetworkResponse"
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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_node_pool_async(self, request):
        r"""创建节点池

        创建节点池接口用于创建新的节点池。该接口适用于以下场景：当需要扩展计算资源、优化资源分配或部署新的服务时，用户可通过此接口创建指定配置的节点池。使用该接口的前提条件是用户具有管理员权限且节点池的配置参数（如节点数量、规格、网络配置等）已正确设置。创建操作完成后，节点池将被成功创建并处于可用状态，相关节点信息将被记录。若用户无权限操作、配置参数错误或系统资源不足，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateNodePool
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateNodePoolRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateNodePoolResponse`
        """
        http_info = self._create_node_pool_http_info(request)
        return self._call_api(**http_info)

    def create_node_pool_async_invoker(self, request):
        http_info = self._create_node_pool_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_node_pool_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/pools/{pool_name}/nodepools",
            "request_type": request.__class__.__name__,
            "response_type": "CreateNodePoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_order_id_async(self, request):
        r"""创建资源池的订单id

        创建资源池订单ID接口用于生成资源池申请的订单标识。该接口适用于以下场景：当用户需要申请新资源池时（如业务扩展、资源不足或临时资源需求），可通过此接口提交按需转包周期订单的创建请求。使用该接口的前提条件是用户需具备资源申请权限，提交的资源池配置参数（如资源类型、容量、周期等）需符合系统校验规则，且当前仅支持按需转包周期订单类型。订单创建成功后，系统将生成唯一订单ID并触发后续资源分配流程，同时记录操作日志。若用户权限不足、配置参数缺失/冲突（如容量超出配额）、订单类型不支持或系统资源不足，接口将返回对应错误码及提示信息，且不会生成订单ID或占用资源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateOrderId
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateOrderIdRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateOrderIdResponse`
        """
        http_info = self._create_order_id_http_info(request)
        return self._call_api(**http_info)

    def create_order_id_async_invoker(self, request):
        http_info = self._create_order_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_order_id_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/pools/{name}/orderid",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOrderIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']

        query_params = []
        if 'action_type' in local_var_params:
            query_params.append(('actionType', local_var_params['action_type']))
        if 'workspace_id' in local_var_params:
            query_params.append(('workspaceId', local_var_params['workspace_id']))

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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_pool_async(self, request):
        r"""创建资源池

        创建资源池接口用于在系统中创建新的资源池。该接口适用于以下场景：当需要为新业务分配资源、优化资源管理或进行资源隔离时，用户可通过此接口创建新的资源池，用于管理计算、存储、网络等资源。使用该接口的前提条件是用户具有管理员权限，并且系统中具备足够的资源支持新资源池的创建。创建操作完成后，新的资源池将被成功添加到系统中，并处于可用状态，可支持后续的资源分配和管理。若用户无权限、系统资源不足或输入参数有误，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePool
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreatePoolRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreatePoolResponse`
        """
        http_info = self._create_pool_http_info(request)
        return self._call_api(**http_info)

    def create_pool_async_invoker(self, request):
        http_info = self._create_pool_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_pool_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/pools",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_model_arts_user_id' in local_var_params:
            header_params['X-ModelArts-User-ID'] = local_var_params['x_model_arts_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_pool_plugin_async(self, request):
        r"""创建插件

        创建插件实例接口用于在系统中创建一个新的插件实例。该接口适用于以下场景：当需要扩展系统功能、部署新的插件、更新现有插件配置或测试插件时，用户可通过此接口创建指定插件的实例。使用该接口的前提条件是插件已存在且用户具有管理员权限或插件管理权限。创建操作完成后，插件实例将被成功创建并处于可用状态，相关配置信息将被记录。若插件不存在、用户无权限操作、配置参数错误或系统资源不足，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePoolPlugin
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreatePoolPluginRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreatePoolPluginResponse`
        """
        http_info = self._create_pool_plugin_http_info(request)
        return self._call_api(**http_info)

    def create_pool_plugin_async_invoker(self, request):
        http_info = self._create_pool_plugin_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_pool_plugin_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/pools/{pool_name}/plugins",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePoolPluginResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_save_image_job_async(self, request):
        r"""创建训练作业镜像保存任务

        创建训练作业镜像保存任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSaveImageJob
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateSaveImageJobRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateSaveImageJobResponse`
        """
        http_info = self._create_save_image_job_http_info(request)
        return self._call_api(**http_info)

    def create_save_image_job_async_invoker(self, request):
        http_info = self._create_save_image_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_save_image_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/training-jobs/{training_job_id}/tasks/{task_id}/save-image-job",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSaveImageJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'training_job_id' in local_var_params:
            path_params['training_job_id'] = local_var_params['training_job_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_train_job_tags_async(self, request):
        r"""创建训练作业标签

        创建训练作业标签，支持批量添加，当添加的标签key已存在，则覆盖该标签的value。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTrainJobTags
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateTrainJobTagsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateTrainJobTagsResponse`
        """
        http_info = self._create_train_job_tags_http_info(request)
        return self._call_api(**http_info)

    def create_train_job_tags_async_invoker(self, request):
        http_info = self._create_train_job_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_train_job_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/modelarts-training-job/{training_job_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTrainJobTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'training_job_id' in local_var_params:
            path_params['training_job_id'] = local_var_params['training_job_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_training_experiment_async(self, request):
        r"""创建训练实验

        创建训练实验接口用于在ModelArts平台上创建新的实验分类。
        该接口适用于以下场景：当用户需要将训练作业放入实验中分类，有序地进行管理，可以通过此接口创建训练实验，常用于多任务的版本管理等场景。使用该接口的前提条件是用户已登录ModelArts平台并具有创建训练实验的权限。创建操作完成后，系统将返回训练实验的详细信息，包括实验ID、当前实验下的训练作业总个数等。若用户无权限操作，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTrainingExperiment
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateTrainingExperimentRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateTrainingExperimentResponse`
        """
        http_info = self._create_training_experiment_http_info(request)
        return self._call_api(**http_info)

    def create_training_experiment_async_invoker(self, request):
        http_info = self._create_training_experiment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_training_experiment_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/training-experiments",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTrainingExperimentResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_training_job_async(self, request):
        r"""创建训练作业

        创建训练作业。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTrainingJob
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateTrainingJobRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateTrainingJobResponse`
        """
        http_info = self._create_training_job_http_info(request)
        return self._call_api(**http_info)

    def create_training_job_async_invoker(self, request):
        http_info = self._create_training_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_training_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/training-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTrainingJobResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_workspace_async(self, request):
        r"""创建工作空间

        创建工作空间（\&quot;default\&quot;为系统预留的默认工作空间名称，不能使用）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWorkspace
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateWorkspaceRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateWorkspaceResponse`
        """
        http_info = self._create_workspace_http_info(request)
        return self._call_api(**http_info)

    def create_workspace_async_invoker(self, request):
        http_info = self._create_workspace_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_workspace_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWorkspaceResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_algorithm_async(self, request):
        r"""删除算法

        删除算法。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAlgorithm
        :type request: :class:`huaweicloudsdkmodelarts.v1.DeleteAlgorithmRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeleteAlgorithmResponse`
        """
        http_info = self._delete_algorithm_http_info(request)
        return self._call_api(**http_info)

    def delete_algorithm_async_invoker(self, request):
        http_info = self._delete_algorithm_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_algorithm_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/algorithms/{algorithm_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAlgorithmResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'algorithm_id' in local_var_params:
            path_params['algorithm_id'] = local_var_params['algorithm_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_authorizations_async(self, request):
        r"""删除授权

        删除授权接口用于删除指定用户的授权或删除全量用户的授权。该接口适用于以下场景：当需要撤销特定用户的访问权限或在系统维护时清理所有用户的授权时，管理员可通过此接口删除指定用户的授权或全量用户的授权。使用该接口的前提条件是管理员具备删除授权的权限，并且需要指定要删除授权的用户或选择删除全量用户的授权。删除操作完成后，指定用户的授权将被移除，或所有用户的授权将被清空，用户将无法再访问相关功能。若用户不存在、管理员无权限操作或删除全量授权时系统检测到无管理员权限，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAuthorizations
        :type request: :class:`huaweicloudsdkmodelarts.v1.DeleteAuthorizationsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeleteAuthorizationsResponse`
        """
        http_info = self._delete_authorizations_http_info(request)
        return self._call_api(**http_info)

    def delete_authorizations_async_invoker(self, request):
        http_info = self._delete_authorizations_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_authorizations_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/authorizations",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAuthorizationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in local_var_params:
            query_params.append(('user_id', local_var_params['user_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_image_async(self, request):
        r"""删除镜像

        删除镜像接口用于删除镜像对象，对于个人私有镜像可以通过参数一并删除SWR镜像内容。该接口适用于以下场景：当镜像不再需要、配置错误或需要清理资源时，用户可通过此接口删除指定的镜像对象。使用该接口的前提条件是镜像已存在且用户具有删除权限。删除操作完成后，镜像对象将被永久移除，相关资源和配置也将被清理。若镜像不存在、用户无权限操作或镜像正在被使用，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteImage
        :type request: :class:`huaweicloudsdkmodelarts.v1.DeleteImageRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeleteImageResponse`
        """
        http_info = self._delete_image_http_info(request)
        return self._call_api(**http_info)

    def delete_image_async_invoker(self, request):
        http_info = self._delete_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_image_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/images/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_image_group_async(self, request):
        r"""删除镜像组

        删除镜像组接口用于删除镜像组内所有的版本对象，对于个人私有镜像可以通过参数一并删除SWR镜像内容。该接口适用于以下场景：当镜像不再需要、配置错误或需要清理资源时，用户可通过此接口删除指定的镜像组对象内所有版本。使用该接口的前提条件是镜像组已存在且用户具有删除权限。删除操作完成后，镜像组内所有版本对象将被永久移除，相关资源和配置也将被清理。若镜像组不存在、用户无权限操作或镜像正在被使用，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteImageGroup
        :type request: :class:`huaweicloudsdkmodelarts.v1.DeleteImageGroupRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeleteImageGroupResponse`
        """
        http_info = self._delete_image_group_http_info(request)
        return self._call_api(**http_info)

    def delete_image_group_async_invoker(self, request):
        http_info = self._delete_image_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_image_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/images/group/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteImageGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_infer_api_key_async(self, request):
        r"""删除应用密钥

        本接口用于删除指定的apikey，适用于管理员需要撤销对某个应用程序或用户的访问权限的场景。调用此接口前，确保已获取到需要删除的apikey，并确认apikey未在其他服务中使用。删除成功后，该apikey将无法再用于访问任何相关服务。如果尝试删除不存在或已删除的apikey，将返回相应的异常信息，提示用户检查apikey的有效性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteInferApiKey
        :type request: :class:`huaweicloudsdkmodelarts.v1.DeleteInferApiKeyRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeleteInferApiKeyResponse`
        """
        http_info = self._delete_infer_api_key_http_info(request)
        return self._call_api(**http_info)

    def delete_infer_api_key_async_invoker(self, request):
        http_info = self._delete_infer_api_key_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_infer_api_key_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/services/api-keys/{key_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInferApiKeyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'key_id' in local_var_params:
            path_params['key_id'] = local_var_params['key_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_infer_deployment_async(self, request):
        r"""删除服务部署

        该接口适用于删除服务的某个部署。若服务ID、部署ID无效、版本号不存在或用户无权限，则返回400 Bad Request或403 Forbidden
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteInferDeployment
        :type request: :class:`huaweicloudsdkmodelarts.v1.DeleteInferDeploymentRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeleteInferDeploymentResponse`
        """
        http_info = self._delete_infer_deployment_http_info(request)
        return self._call_api(**http_info)

    def delete_infer_deployment_async_invoker(self, request):
        http_info = self._delete_infer_deployment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_infer_deployment_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/services/{service_id}/deployments/{deployment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInferDeploymentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_infer_deployment_instance_async(self, request):
        r"""删除服务部署的实例

        本接口用于删除指定的单个部署的实例，适用于需要清理或释放不再使用的部署实例资源的场景。调用此接口前，确保已具备相应的删除权限，并提供有效的服务实例ID、部署ID。删除成功后，指定的服务部署实例将被彻底移除，不再对任何请求生效。如果提供的服务实例ID、部署ID无效、服务实例已删除或权限不足，将返回相应的异常信息，提示用户检查输入数据的有效性和权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteInferDeploymentInstance
        :type request: :class:`huaweicloudsdkmodelarts.v1.DeleteInferDeploymentInstanceRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeleteInferDeploymentInstanceResponse`
        """
        http_info = self._delete_infer_deployment_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_infer_deployment_instance_async_invoker(self, request):
        http_info = self._delete_infer_deployment_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_infer_deployment_instance_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/services/{id}/deployments/{deployment_name}/instances/{name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInferDeploymentInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']
        if 'deployment_name' in local_var_params:
            path_params['deployment_name'] = local_var_params['deployment_name']
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']

        query_params = []
        if 'force' in local_var_params:
            query_params.append(('force', local_var_params['force']))
        if 'operation' in local_var_params:
            query_params.append(('operation', local_var_params['operation']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_infer_deployment_pod_async(self, request):
        r"""删除Pod

        本接口用于删除指定的单个Pod，适用于需要清理或释放不再使用的Pod资源的场景。调用此接口前，确保已具备相应的删除权限，并提供有效的Pod ID。删除成功后，指定的Pod将被彻底移除，不再对任何服务请求生效。如果提供的Pod ID无效、Pod已删除或权限不足，将返回相应的异常信息，提示用户检查输入数据的有效性和权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteInferDeploymentPod
        :type request: :class:`huaweicloudsdkmodelarts.v1.DeleteInferDeploymentPodRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeleteInferDeploymentPodResponse`
        """
        http_info = self._delete_infer_deployment_pod_http_info(request)
        return self._call_api(**http_info)

    def delete_infer_deployment_pod_async_invoker(self, request):
        http_info = self._delete_infer_deployment_pod_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_infer_deployment_pod_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/services/{id}/deployments/{deployment_name}/instances/{instance_name}/pods/{name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInferDeploymentPodResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']
        if 'deployment_name' in local_var_params:
            path_params['deployment_name'] = local_var_params['deployment_name']
        if 'instance_name' in local_var_params:
            path_params['instance_name'] = local_var_params['instance_name']
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']

        query_params = []
        if 'force' in local_var_params:
            query_params.append(('force', local_var_params['force']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_infer_deployment_version_async(self, request):
        r"""删除在线服务部署版本

        此接口用于删除指定服务部署的某个在线版本，适用于需要清理不再使用的版本或优化资源管理的场景。
        请求需包含有效的服务ID、部署ID及版本号。用户必须具有对目标服务部署的管理权限，并且该版本当前未处于活跃状态。
        删除成功后，指定版本将从在线服务部署中移除，相关资源将被释放。
        若服务ID、部署ID无效、版本号不存在或用户无权限，则返回400 Bad Request或403 Forbidden；若版本处于活跃状态或有其他依赖，则返回400 Bad Request。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteInferDeploymentVersion
        :type request: :class:`huaweicloudsdkmodelarts.v1.DeleteInferDeploymentVersionRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeleteInferDeploymentVersionResponse`
        """
        http_info = self._delete_infer_deployment_version_http_info(request)
        return self._call_api(**http_info)

    def delete_infer_deployment_version_async_invoker(self, request):
        http_info = self._delete_infer_deployment_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_infer_deployment_version_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/services/{service_id}/deployments/{deployment_id}/versions/{version}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInferDeploymentVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_infer_service_tag_async(self, request):
        r"""删除资源标签

        该接口适用于需要从资源（如模型、数据集、服务等）中移除特定标签的场景，例如在资源管理或分类中，用户可以通过删除标签来调整或清理资源的元数据。通过调用此接口，用户可以批量删除指定的标签。用户必须具有足够的权限，且目标资源需存在。删除成功后，资源将不再包含指定的标签信息；若失败，返回具体的错误信息。常见异常包括权限验证错误、资源不存在错误和参数验证错误。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteInferServiceTag
        :type request: :class:`huaweicloudsdkmodelarts.v1.DeleteInferServiceTagRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeleteInferServiceTagResponse`
        """
        http_info = self._delete_infer_service_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_infer_service_tag_async_invoker(self, request):
        http_info = self._delete_infer_service_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_infer_service_tag_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/modelarts-service-v2/{resource_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInferServiceTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))

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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_network_async(self, request):
        r"""删除网络资源

        删除网络资源接口用于移除指定的网络资源。该接口适用于以下场景：当网络资源不再需要、配置错误或需要清理资源时，用户可通过此接口删除指定的网络资源。使用该接口的前提条件是网络资源已存在且用户具有管理员权限。删除操作完成后，指定的网络资源将被永久移除，相关配置和关联关系也将被清理。若指定的网络资源不存在、用户无权限操作或资源被其他资源依赖，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteNetwork
        :type request: :class:`huaweicloudsdkmodelarts.v1.DeleteNetworkRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeleteNetworkResponse`
        """
        http_info = self._delete_network_http_info(request)
        return self._call_api(**http_info)

    def delete_network_async_invoker(self, request):
        http_info = self._delete_network_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_network_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/networks/{network_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNetworkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'network_name' in local_var_params:
            path_params['network_name'] = local_var_params['network_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_node_pool_async(self, request):
        r"""删除节点池

        删除节点池接口用于移除已创建的节点池，包周期资源池不支持。该接口适用于以下场景：当节点池完成任务、配置错误或需要清理资源时，用户可通过此接口删除指定的节点池。使用该接口的前提条件是节点池已存在且用户具有管理员权限。删除操作完成后，节点池将被永久移除，相关资源和配置也将被清理。若节点池不存在、用户无权限操作或节点池处于不可删除状态（如包周期资源池或节点池正在使用中），接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteNodePool
        :type request: :class:`huaweicloudsdkmodelarts.v1.DeleteNodePoolRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeleteNodePoolResponse`
        """
        http_info = self._delete_node_pool_http_info(request)
        return self._call_api(**http_info)

    def delete_node_pool_async_invoker(self, request):
        http_info = self._delete_node_pool_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_node_pool_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/pools/{pool_name}/nodepools/{nodepool_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNodePoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']
        if 'nodepool_name' in local_var_params:
            path_params['nodepool_name'] = local_var_params['nodepool_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_pool_async(self, request):
        r"""删除资源池

        删除资源池接口用于移除指定的资源池。该接口适用于以下场景：当资源池不再需要、配置错误或需要清理资源时，用户可通过此接口删除指定的资源池。使用该接口的前提条件是资源池已存在且用户具有管理员权限。删除操作完成后，指定的资源池将被永久移除，相关资源和配置也将被清理。若资源池不存在、用户无权限操作或资源池被其他资源依赖，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePool
        :type request: :class:`huaweicloudsdkmodelarts.v1.DeletePoolRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeletePoolResponse`
        """
        http_info = self._delete_pool_http_info(request)
        return self._call_api(**http_info)

    def delete_pool_async_invoker(self, request):
        http_info = self._delete_pool_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_pool_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/pools/{pool_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']

        query_params = []

        header_params = {}
        if 'x_model_arts_user_id' in local_var_params:
            header_params['X-ModelArts-User-ID'] = local_var_params['x_model_arts_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_train_job_tags_async(self, request):
        r"""删除训练作业标签

        删除训练作业标签，支持批量删除。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTrainJobTags
        :type request: :class:`huaweicloudsdkmodelarts.v1.DeleteTrainJobTagsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeleteTrainJobTagsResponse`
        """
        http_info = self._delete_train_job_tags_http_info(request)
        return self._call_api(**http_info)

    def delete_train_job_tags_async_invoker(self, request):
        http_info = self._delete_train_job_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_train_job_tags_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/modelarts-training-job/{training_job_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTrainJobTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'training_job_id' in local_var_params:
            path_params['training_job_id'] = local_var_params['training_job_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_training_experiment_async(self, request):
        r"""删除训练实验

        删除训练实验接口用于移除已创建的训练实验。
        该接口适用于以下场景：当训练实验完成、配置错误或需要清理资源时，用户可以通过此接口删除指定的训练实验。使用该接口的前提条件是训练实验已存在且用户具有删除该实验的权限。删除操作完成后，训练实验将被永久移除，相关的配置和资源也将被清理。若训练实验不存在或用户无权限操作，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTrainingExperiment
        :type request: :class:`huaweicloudsdkmodelarts.v1.DeleteTrainingExperimentRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeleteTrainingExperimentResponse`
        """
        http_info = self._delete_training_experiment_http_info(request)
        return self._call_api(**http_info)

    def delete_training_experiment_async_invoker(self, request):
        http_info = self._delete_training_experiment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_training_experiment_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/training-experiments/{experiment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTrainingExperimentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'experiment_id' in local_var_params:
            path_params['experiment_id'] = local_var_params['experiment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_training_job_async(self, request):
        r"""删除训练作业

        删除训练作业。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTrainingJob
        :type request: :class:`huaweicloudsdkmodelarts.v1.DeleteTrainingJobRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeleteTrainingJobResponse`
        """
        http_info = self._delete_training_job_http_info(request)
        return self._call_api(**http_info)

    def delete_training_job_async_invoker(self, request):
        http_info = self._delete_training_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_training_job_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/training-jobs/{training_job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTrainingJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'training_job_id' in local_var_params:
            path_params['training_job_id'] = local_var_params['training_job_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_workspace_async(self, request):
        r"""删除工作空间

        删除工作空间。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteWorkspace
        :type request: :class:`huaweicloudsdkmodelarts.v1.DeleteWorkspaceRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeleteWorkspaceResponse`
        """
        http_info = self._delete_workspace_http_info(request)
        return self._call_api(**http_info)

    def delete_workspace_async_invoker(self, request):
        http_info = self._delete_workspace_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_workspace_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteWorkspaceResponse"
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

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def detach_dynamic_storage_async(self, request):
        r"""动态卸载Notebook存储

        动态卸载Notebook存储接口用于从运行中的Notebook实例中卸载已挂载的动态存储实例。
        
        适用场景：用户需要清理或重新组织Notebook实例的挂载资源时，可通过此接口卸载指定的存储实例。使用该接口的前提条件是用户已登录系统并具有访问目标Notebook实例的权限，同时Notebook实例必须处于运行状态且存储实例处于MOUNTED / UNMOUNT_FAILED / MOUNT_FAILED状态。调用该接口后，系统将卸载指定的存储实例，Notebook容器将无法再操作存储中的文件或对象，但存储中的文件或对象保持不变。若用户无权限访问指定实例或Notebook实例未运行，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetachDynamicStorage
        :type request: :class:`huaweicloudsdkmodelarts.v1.DetachDynamicStorageRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DetachDynamicStorageResponse`
        """
        http_info = self._detach_dynamic_storage_http_info(request)
        return self._call_api(**http_info)

    def detach_dynamic_storage_async_invoker(self, request):
        http_info = self._detach_dynamic_storage_http_info(request)
        return AsyncInvoker(self, http_info)

    def _detach_dynamic_storage_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/notebooks/{instance_id}/storage/{storage_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DetachDynamicStorageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'storage_id' in local_var_params:
            path_params['storage_id'] = local_var_params['storage_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_authorizations_async(self, request):
        r"""查看授权列表

        查看授权列表接口用于查看授权信息。该接口适用于以下场景：当用户需要了解当前的授权情况、审核权限分配或管理权限时，可通过此接口查看授权列表。使用该接口的前提条件是用户具备查看授权的权限。查看操作完成后，将返回授权列表，包括被授权的资源、授权类型以及授权内容等信息。若用户无权限查看或授权列表不存在，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetAuthorizations
        :type request: :class:`huaweicloudsdkmodelarts.v1.GetAuthorizationsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.GetAuthorizationsResponse`
        """
        http_info = self._get_authorizations_http_info(request)
        return self._call_api(**http_info)

    def get_authorizations_async_invoker(self, request):
        http_info = self._get_authorizations_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_authorizations_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/authorizations",
            "request_type": request.__class__.__name__,
            "response_type": "GetAuthorizationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sort_by' in local_var_params:
            query_params.append(('sort_by', local_var_params['sort_by']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_hyperinstance_operation_async(self, request):
        r"""查询超节点Operation详情

        查询Operation详情接口用于获取指定Operation的详细信息。该接口适用于以下场景：当用户需要了解某个Operation的具体执行情况和状态，以便进行故障排查或操作审计时，可以通过此接口获取相关信息。使用该接口的前提条件是用户已登录并具有查询Operation详情的权限，且指定的Operation已存在。查询操作完成后，接口将返回指定Operation的详细信息，包括Operation ID、操作类型、执行状态、开始时间、结束时间、操作结果等。若用户无权限操作、指定的Operation不存在或Operation ID无效，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetHyperinstanceOperation
        :type request: :class:`huaweicloudsdkmodelarts.v1.GetHyperinstanceOperationRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.GetHyperinstanceOperationResponse`
        """
        http_info = self._get_hyperinstance_operation_http_info(request)
        return self._call_api(**http_info)

    def get_hyperinstance_operation_async_invoker(self, request):
        http_info = self._get_hyperinstance_operation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_hyperinstance_operation_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dev-servers/hyperinstance/{id}/operation/{operation_id}",
            "request_type": request.__class__.__name__,
            "response_type": "GetHyperinstanceOperationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']
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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_algorithms_async(self, request):
        r"""查询算法列表

        查询算法列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAlgorithms
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListAlgorithmsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListAlgorithmsResponse`
        """
        http_info = self._list_algorithms_http_info(request)
        return self._call_api(**http_info)

    def list_algorithms_async_invoker(self, request):
        http_info = self._list_algorithms_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_algorithms_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/algorithms",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlgorithmsResponse"
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
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'group_by' in local_var_params:
            query_params.append(('group_by', local_var_params['group_by']))
        if 'searches' in local_var_params:
            query_params.append(('searches', local_var_params['searches']))
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_dynamic_storages_async(self, request):
        r"""获取动态挂载存储信息列表

        此接口用于获取指定Notebook实例下挂载的动态存储信息列表。
        适用场景：用户需要获取指定Notebook实例下挂载的动态存储的存储id、存储类型、挂载路径、挂载状态等信息的场景。若挂载失败，会返回相应错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDynamicStorages
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListDynamicStoragesRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListDynamicStoragesResponse`
        """
        http_info = self._list_dynamic_storages_http_info(request)
        return self._call_api(**http_info)

    def list_dynamic_storages_async_invoker(self, request):
        http_info = self._list_dynamic_storages_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_dynamic_storages_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/notebooks/{instance_id}/storage",
            "request_type": request.__class__.__name__,
            "response_type": "ListDynamicStoragesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_event_categories_async(self, request):
        r"""获取事件类型列表

        获取事件类型列表接口用于获取训练管理中支持的事件类型列表。
        该接口适用于以下场景：当用户需要了解训练管理中支持的事件类型，以便在创建或管理训练任务时进行相关配置时，可以通过此接口获取事件类型列表。使用该接口的前提条件是用户已登录且具有访问训练管理的权限。获取操作完成后，响应消息体中将包含所有支持的事件类型及其描述。若用户无权限访问或系统中无事件类型信息，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEventCategories
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListEventCategoriesRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListEventCategoriesResponse`
        """
        http_info = self._list_event_categories_http_info(request)
        return self._call_api(**http_info)

    def list_event_categories_async_invoker(self, request):
        http_info = self._list_event_categories_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_event_categories_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/training-event-categories",
            "request_type": request.__class__.__name__,
            "response_type": "ListEventCategoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'flavor_type' in local_var_params:
            query_params.append(('flavor_type', local_var_params['flavor_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_events_async(self, request):
        r"""查询事件列表

        查询事件列表接口用于获取系统中记录的事件信息。该接口适用于以下场景：当用户需要监控系统状态、排查问题或进行审计时，可通过此接口查询系统中发生的事件记录。使用该接口的前提条件是用户具有相应的权限，并且系统中已存在事件记录。查询操作完成后，接口将返回事件列表，包含事件ID、类型、时间、描述等信息。若用户无权限、事件记录不存在或查询参数有误，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEvents
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListEventsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListEventsResponse`
        """
        http_info = self._list_events_http_info(request)
        return self._call_api(**http_info)

    def list_events_async_invoker(self, request):
        http_info = self._list_events_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_events_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/events",
            "request_type": request.__class__.__name__,
            "response_type": "ListEventsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'resource' in local_var_params:
            query_params.append(('resource', local_var_params['resource']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if '_continue' in local_var_params:
            query_params.append(('continue', local_var_params['_continue']))
        if 'since' in local_var_params:
            query_params.append(('since', local_var_params['since']))
        if 'until' in local_var_params:
            query_params.append(('until', local_var_params['until']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_image_async(self, request):
        r"""查询支持的镜像列表

        查询支持的镜像列表接口用于根据指定条件分页查询满足条件的所有镜像。该接口适用于以下场景：当用户需要查找特定镜像、管理镜像仓库或选择合适的镜像版本进行部署时，可通过此接口获取符合条件的镜像列表。使用该接口的前提条件是镜像仓库已存在且用户具有访问权限。查询操作完成后，将返回满足条件的镜像列表，包括镜像ID、名称、版本、类型、状态、大小和创建时间等详细信息。若镜像仓库不存在、用户无权限访问或查询条件有误，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListImage
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListImageRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListImageResponse`
        """
        http_info = self._list_image_http_info(request)
        return self._call_api(**http_info)

    def list_image_async_invoker(self, request):
        http_info = self._list_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_image_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/images",
            "request_type": request.__class__.__name__,
            "response_type": "ListImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'name_fuzzy_match' in local_var_params:
            query_params.append(('name_fuzzy_match', local_var_params['name_fuzzy_match']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'service_type' in local_var_params:
            query_params.append(('service_type', local_var_params['service_type']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))
        if 'show_name' in local_var_params:
            query_params.append(('show_name', local_var_params['show_name']))
        if 'show_tag' in local_var_params:
            query_params.append(('show_tag', local_var_params['show_tag']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_image_group_async(self, request):
        r"""查询用户镜像列表

        查询用户镜像列表接口用于查询用户镜像信息概览，以镜像名称作为聚合的信息。该接口适用于以下场景：当用户需要管理多个镜像或了解各镜像的基本信息时，可通过此接口获取镜像列表及其概览信息。使用该接口的前提条件是用户具备镜像管理权限，并且镜像已存在。查询操作完成后，将返回用户所有镜像的列表，包括镜像名称、版本、状态等信息。若镜像不存在或用户无权限访问，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListImageGroup
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListImageGroupRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListImageGroupResponse`
        """
        http_info = self._list_image_group_http_info(request)
        return self._call_api(**http_info)

    def list_image_group_async_invoker(self, request):
        http_info = self._list_image_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_image_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/images/group",
            "request_type": request.__class__.__name__,
            "response_type": "ListImageGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'name_fuzzy_match' in local_var_params:
            query_params.append(('name_fuzzy_match', local_var_params['name_fuzzy_match']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'swr_instance_id' in local_var_params:
            query_params.append(('swr_instance_id', local_var_params['swr_instance_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_infer_api_keys_async(self, request):
        r"""查询应用密钥

        本接口用于查询当前系统中的apikey列表，适用于管理员或用户需要查看和管理apikey的场景。调用此接口前，确保已具备相应的查询权限。返回的列表将包含每个apikey的基本信息，如apikey值、创建时间、绑定的服务等。如果当前系统中没有apikey，将返回空列表或相应的异常信息，提示用户检查查询条件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInferApiKeys
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListInferApiKeysRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListInferApiKeysResponse`
        """
        http_info = self._list_infer_api_keys_http_info(request)
        return self._call_api(**http_info)

    def list_infer_api_keys_async_invoker(self, request):
        http_info = self._list_infer_api_keys_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_infer_api_keys_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/services/api-keys",
            "request_type": request.__class__.__name__,
            "response_type": "ListInferApiKeysResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'scope' in local_var_params:
            query_params.append(('scope', local_var_params['scope']))
        if 'service_id' in local_var_params:
            query_params.append(('service_id', local_var_params['service_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'service_name' in local_var_params:
            query_params.append(('service_name', local_var_params['service_name']))
        if 'key_id' in local_var_params:
            query_params.append(('key_id', local_var_params['key_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))
        if 'with_user_scope' in local_var_params:
            query_params.append(('with_user_scope', local_var_params['with_user_scope']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_infer_cluster_flavors_async(self, request):
        r"""查询支持可切换规格列表

        该接口允许用户查询当前资源实例支持的可切换规格列表，适用于需要调整实例资源配置的场景。使用该接口前，用户需确保已登录并拥有查询权限。执行成功后，用户将获得一个包含各种可切换规格的详细列表，包括规格ID、名称、资源配额等信息，可用于后续的实例规格变更操作。如果用户没有相应的查询权限或资源实例ID无效，接口将返回错误信息，如401 Unauthorized或404 Not Found。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInferClusterFlavors
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListInferClusterFlavorsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListInferClusterFlavorsResponse`
        """
        http_info = self._list_infer_cluster_flavors_http_info(request)
        return self._call_api(**http_info)

    def list_infer_cluster_flavors_async_invoker(self, request):
        http_info = self._list_infer_cluster_flavors_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_infer_cluster_flavors_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/services/flavors",
            "request_type": request.__class__.__name__,
            "response_type": "ListInferClusterFlavorsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'flavor_type' in local_var_params:
            query_params.append(('flavor_type', local_var_params['flavor_type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_infer_deployment_instances_async(self, request):
        r"""查询服务部署实例列表

        本接口用于查询当前[租户](tag:hws,hws_hk,fcs,fcs_super)[资源空间](tag:hcs,hcs_sm)的服务部署实例列表，并支持根据服务部署实例的状态进行筛选，包括运行中和已删除状态，同时支持分页和关键词筛选。适用于需要管理和监控服务实例状态的场景。调用此接口前，确保已具备相应的查询权限，并提供可选的筛选条件和分页参数。返回的列表将包含每个服务部署实例的基本信息，如部署名字、最新更新时间、状态等。如果当前租户没有符合条件的服务实例或提供的参数无效，将返回空列表或相应的异常信息，提示用户检查输入数据的有效性和权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInferDeploymentInstances
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListInferDeploymentInstancesRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListInferDeploymentInstancesResponse`
        """
        http_info = self._list_infer_deployment_instances_http_info(request)
        return self._call_api(**http_info)

    def list_infer_deployment_instances_async_invoker(self, request):
        http_info = self._list_infer_deployment_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_infer_deployment_instances_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/services/{id}/deployments/{name}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListInferDeploymentInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'csv'
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'pod_name' in local_var_params:
            query_params.append(('pod_name', local_var_params['pod_name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_infer_deployment_pod_events_async(self, request):
        r"""查询Pod事件

        本接口用于查询指定Pod的Kubernetes事件，适用于需要监控和排查Pod运行状态的场景。调用此接口前，确保已具备相应的查询权限，并提供有效的Pod ID。返回的事件列表将包含每个事件的详细信息，如事件类型、发生次数、事件名称、事件信息、发生时间等。如果提供的Pod ID无效、Pod不存在或权限不足，将返回相应的异常信息，提示用户检查输入数据的有效性和权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInferDeploymentPodEvents
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListInferDeploymentPodEventsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListInferDeploymentPodEventsResponse`
        """
        http_info = self._list_infer_deployment_pod_events_http_info(request)
        return self._call_api(**http_info)

    def list_infer_deployment_pod_events_async_invoker(self, request):
        http_info = self._list_infer_deployment_pod_events_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_infer_deployment_pod_events_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/services/{id}/deployments/{deployment_name}/instances/{instance_name}/pods/{name}/events",
            "request_type": request.__class__.__name__,
            "response_type": "ListInferDeploymentPodEventsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']
        if 'deployment_name' in local_var_params:
            path_params['deployment_name'] = local_var_params['deployment_name']
        if 'instance_name' in local_var_params:
            path_params['instance_name'] = local_var_params['instance_name']
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_infer_deployment_pods_async(self, request):
        r"""查询服务部署的pod的列表

        本接口用于查询指定服务部署的pod列表，并支持选择是否只获取当前运行中的pod。适用于需要管理和监控服务部署pod状态的场景。调用此接口前，确保已具备相应的查询权限，并提供有效的服务ID、部署ID和可选的筛选参数pod status（如是否只获取当前运行中的pod）。返回的列表将包含每个pod的基本信息，如pod名称、pod所在node的IP、pod所在node名字、pod角色、状态、最近更新时间等。如果指定的服务ID无效或当前服务没有pod，将返回空列表或相应的异常信息，提示用户检查输入数据的有效性和权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInferDeploymentPods
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListInferDeploymentPodsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListInferDeploymentPodsResponse`
        """
        http_info = self._list_infer_deployment_pods_http_info(request)
        return self._call_api(**http_info)

    def list_infer_deployment_pods_async_invoker(self, request):
        http_info = self._list_infer_deployment_pods_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_infer_deployment_pods_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/services/{id}/deployments/{deployment_name}/instances/{name}/pods",
            "request_type": request.__class__.__name__,
            "response_type": "ListInferDeploymentPodsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']
        if 'deployment_name' in local_var_params:
            path_params['deployment_name'] = local_var_params['deployment_name']
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'csv'
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'pod_name' in local_var_params:
            query_params.append(('pod_name', local_var_params['pod_name']))
        if 'pod_id' in local_var_params:
            query_params.append(('pod_id', local_var_params['pod_id']))
        if 'pod_node_ip' in local_var_params:
            query_params.append(('pod_node_ip', local_var_params['pod_node_ip']))
        if 'pod_node_name' in local_var_params:
            query_params.append(('pod_node_name', local_var_params['pod_node_name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_infer_deployment_versions_async(self, request):
        r"""查询在线服务部署版本列表

        此接口用于获取指定服务部署的版本列表，适用于需要了解当前服务部署可用版本的场景，例如进行版本选择或确认当前版本信息。请求需包含有效的服务ID、部署ID，也可通过排序参数对列表进行排序。用户必须具有对目标服务部署的查看权限。请求成功后，返回该服务部署的所有在线版本信息，包括版本号、发布时间和状态。若服务ID/部署ID无效或用户无权限，则返回400 Bad Request或403 Forbidden；若服务部署无在线版本，则返回空列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInferDeploymentVersions
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListInferDeploymentVersionsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListInferDeploymentVersionsResponse`
        """
        http_info = self._list_infer_deployment_versions_http_info(request)
        return self._call_api(**http_info)

    def list_infer_deployment_versions_async_invoker(self, request):
        http_info = self._list_infer_deployment_versions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_infer_deployment_versions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/services/{service_id}/deployments/{deployment_id}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "ListInferDeploymentVersionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_infer_deployments_async(self, request):
        r"""查询服务部署列表

        支持分页和筛选，适用于用户在管理控制台或通过API需要查看特定条件下（如服务状态、名称等）的部署列表的情况。调用此接口前，用户必须具有查询部署列表的权限，并提供合法的分页参数（如页码、每页条数）和筛选条件（如部署状态、名称等）。调用成功后，系统将返回符合筛选条件的部署列表，包含指定页码的数据，并返回总页数和总记录数。如果用户没有查询部署列表的权限，或提供的分页参数和筛选条件不合法，调用将返回相应的错误信息。如果系统在查询过程中遇到内部错误，也将返回错误信息并记录日志。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInferDeployments
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListInferDeploymentsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListInferDeploymentsResponse`
        """
        http_info = self._list_infer_deployments_http_info(request)
        return self._call_api(**http_info)

    def list_infer_deployments_async_invoker(self, request):
        http_info = self._list_infer_deployments_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_infer_deployments_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/services/{service_id}/deployments",
            "request_type": request.__class__.__name__,
            "response_type": "ListInferDeploymentsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

        query_params = []
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'delete_after' in local_var_params:
            query_params.append(('delete_after', local_var_params['delete_after']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_infer_intranet_connection_applications_async(self, request):
        r"""查询当前的内网接入申请列表

        本接口用于查询当前所有的内网接入申请记录，适用于需要管理和监控内网接入申请状态的场景。调用此接口前，确保已具备相应的查询权限。返回的列表将包含每个内网接入申请的基本信息，如申请ID、创建时间、状态、Region ID等。如果当前租户没有内网接入申请记录，将返回空列表。如果调用时出现权限不足或其他系统异常，将返回相应的异常信息，提示用户检查权限或联系技术支持。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInferIntranetConnectionApplications
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListInferIntranetConnectionApplicationsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListInferIntranetConnectionApplicationsResponse`
        """
        http_info = self._list_infer_intranet_connection_applications_http_info(request)
        return self._call_api(**http_info)

    def list_infer_intranet_connection_applications_async_invoker(self, request):
        http_info = self._list_infer_intranet_connection_applications_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_infer_intranet_connection_applications_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/intranet-connection/requests",
            "request_type": request.__class__.__name__,
            "response_type": "ListInferIntranetConnectionApplicationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'scene' in local_var_params:
            query_params.append(('scene', local_var_params['scene']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'service_id' in local_var_params:
            query_params.append(('service_id', local_var_params['service_id']))
        if 'service_name' in local_var_params:
            query_params.append(('service_name', local_var_params['service_name']))
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
        if 'vpc_name' in local_var_params:
            query_params.append(('vpc_name', local_var_params['vpc_name']))
        if 'pool_id' in local_var_params:
            query_params.append(('pool_id', local_var_params['pool_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_infer_intranet_connection_reviews_async(self, request):
        r"""查询当前的内网接入审批列表

        本接口用于查询当前所有的内网接入审批记录，适用于需要管理和监控内网接入审批状态的场景。调用此接口前，确保已具备相应的查询权限。返回的列表将包含每个内网接入审批的基本信息，如审批ID、申请时间、状态（如待审批、已批准、已拒绝）、申请者信息、Region ID等。如果当前租户没有内网接入审批记录，将返回空列表。如果调用时出现权限不足或其他系统异常，将返回相应的异常信息，提示用户检查权限或联系技术支持。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInferIntranetConnectionReviews
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListInferIntranetConnectionReviewsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListInferIntranetConnectionReviewsResponse`
        """
        http_info = self._list_infer_intranet_connection_reviews_http_info(request)
        return self._call_api(**http_info)

    def list_infer_intranet_connection_reviews_async_invoker(self, request):
        http_info = self._list_infer_intranet_connection_reviews_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_infer_intranet_connection_reviews_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/intranet-connection/reviews",
            "request_type": request.__class__.__name__,
            "response_type": "ListInferIntranetConnectionReviewsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'scene' in local_var_params:
            query_params.append(('scene', local_var_params['scene']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'applicant_domain_id' in local_var_params:
            query_params.append(('applicant_domain_id', local_var_params['applicant_domain_id']))
        if 'service_id' in local_var_params:
            query_params.append(('service_id', local_var_params['service_id']))
        if 'applicant_user_name' in local_var_params:
            query_params.append(('applicant_user_name', local_var_params['applicant_user_name']))
        if 'service_name' in local_var_params:
            query_params.append(('service_name', local_var_params['service_name']))
        if 'vpc_name' in local_var_params:
            query_params.append(('vpc_name', local_var_params['vpc_name']))
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
        if 'pool_id' in local_var_params:
            query_params.append(('pool_id', local_var_params['pool_id']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_infer_service_events_async(self, request):
        r"""获取在线服务事件列表

        该接口适用于需要监控和管理在线服务事件的场景，例如用户或运维人员需要定期检查服务的日志事件，以及时发现和处理问题。通过调用此接口，用户可以获取当前在线服务的所有事件记录，包括事件类型、事件信息、时间、发生次数等信息。用户必须具有查询服务事件列表的权限，才能成功访问该接口。获取成功后，返回事件列表；若失败，返回具体的错误信息。常见异常包括权限验证错误、服务状态错误和参数验证错误。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInferServiceEvents
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListInferServiceEventsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListInferServiceEventsResponse`
        """
        http_info = self._list_infer_service_events_http_info(request)
        return self._call_api(**http_info)

    def list_infer_service_events_async_invoker(self, request):
        http_info = self._list_infer_service_events_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_infer_service_events_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/services/{service_id}/events",
            "request_type": request.__class__.__name__,
            "response_type": "ListInferServiceEventsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

        query_params = []
        if 'event_type' in local_var_params:
            query_params.append(('event_type', local_var_params['event_type']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'event_info_key' in local_var_params:
            query_params.append(('event_info_key', local_var_params['event_info_key']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_infer_service_tags_async(self, request):
        r"""查询某一类资源下的标签

        该接口适用于需要获取用户当前项目中某一类资源（如指定的Service）的标签信息的场景，例如在资源管理和监控中，用户可以通过查询标签来了解各类资源的分类和属性。通过调用此接口，用户可以获取指定Service在所有工作空间中的标签列表，但无权限的工作空间标签数据将被过滤不返回。用户必须具有足够的权限，且目标资源需存在。查询成功后，返回指定Service的标签列表；若失败，返回具体的错误信息。常见异常包括权限验证错误、资源不存在错误和参数验证错误。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInferServiceTags
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListInferServiceTagsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListInferServiceTagsResponse`
        """
        http_info = self._list_infer_service_tags_http_info(request)
        return self._call_api(**http_info)

    def list_infer_service_tags_async_invoker(self, request):
        http_info = self._list_infer_service_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_infer_service_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/modelarts-service-v2/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListInferServiceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_infer_services_async(self, request):
        r"""查询服务列表

        支持分页和筛选
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInferServices
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListInferServicesRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListInferServicesResponse`
        """
        http_info = self._list_infer_services_http_info(request)
        return self._call_api(**http_info)

    def list_infer_services_async_invoker(self, request):
        http_info = self._list_infer_services_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_infer_services_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/services",
            "request_type": request.__class__.__name__,
            "response_type": "ListInferServicesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'pool_id' in local_var_params:
            query_params.append(('pool_id', local_var_params['pool_id']))
        if 'pool_name' in local_var_params:
            query_params.append(('pool_name', local_var_params['pool_name']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'auth_type' in local_var_params:
            query_params.append(('auth_type', local_var_params['auth_type']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'asset_id' in local_var_params:
            query_params.append(('asset_id', local_var_params['asset_id']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_infer_services_by_tags_async(self, request):
        r"""通过标签反查资源列表

        该接口适用于需要根据标签或资源名称查找相关资源的场景，例如在资源管理和搜索中，用户可以通过指定标签或进行模糊查询来查找符合特定条件的资源。通过调用此接口，用户可以基于多个标签或资源名称进行精确或模糊查询，若不传标签则返回所有资源。用户必须具有足够的权限，且目标资源需存在。查询成功后，返回符合条件的资源列表；若失败，返回具体的错误信息。常见异常包括权限验证错误、资源不存在错误和参数验证错误。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInferServicesByTags
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListInferServicesByTagsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListInferServicesByTagsResponse`
        """
        http_info = self._list_infer_services_by_tags_http_info(request)
        return self._call_api(**http_info)

    def list_infer_services_by_tags_async_invoker(self, request):
        http_info = self._list_infer_services_by_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_infer_services_by_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/modelarts-service-v2/resource-instances/filter",
            "request_type": request.__class__.__name__,
            "response_type": "ListInferServicesByTagsResponse"
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
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))

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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_jobs_async(self, request):
        r"""查询任务列表

        查询任务列表接口用于获取当前用户下的任务列表。该接口适用于以下场景：当需要查看任务状态、管理任务进度或统计任务数量时，用户可通过此接口获取当前用户下所有任务的详细信息。使用该接口的前提条件是用户已登录系统且具有查看任务的权限。调用接口成功后，系统将返回当前用户下的任务列表，包括任务ID、名称、状态、创建时间等信息。若用户未登录、无权限访问或系统中未配置任务，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListJobs
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListJobsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListJobsResponse`
        """
        http_info = self._list_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_jobs_async_invoker(self, request):
        http_info = self._list_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'since' in local_var_params:
            query_params.append(('since', local_var_params['since']))
        if 'until' in local_var_params:
            query_params.append(('until', local_var_params['until']))
        if 'resource' in local_var_params:
            query_params.append(('resource', local_var_params['resource']))
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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_networks_async(self, request):
        r"""查询网络资源列表

        查询网络资源列表接口用于获取系统中已创建的网络资源信息。该接口适用于以下场景：当用户需要监控网络状态、进行资源规划、排查网络问题或进行审计时，可通过此接口查询系统中现有的网络资源列表。使用该接口的前提条件是用户具有相应的权限，并且系统中已存在网络资源。查询操作完成后，接口将返回网络资源列表，包含资源ID、类型、状态、创建时间等详细信息。若用户无权限、系统中无网络资源或查询参数有误，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNetworks
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListNetworksRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListNetworksResponse`
        """
        http_info = self._list_networks_http_info(request)
        return self._call_api(**http_info)

    def list_networks_async_invoker(self, request):
        http_info = self._list_networks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_networks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/networks",
            "request_type": request.__class__.__name__,
            "response_type": "ListNetworksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'label_selector' in local_var_params:
            query_params.append(('labelSelector', local_var_params['label_selector']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if '_continue' in local_var_params:
            query_params.append(('continue', local_var_params['_continue']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_node_pool_nodes_async(self, request):
        r"""查询节点池的节点列表

        查询节点池的节点列表接口用于获取指定节点池中所有节点的详细信息。该接口适用于以下场景：当需要查看节点池的节点状态、资源使用情况或管理节点资源时，用户可通过此接口获取节点池中节点的详细信息。使用该接口的前提条件是节点池已存在且用户具有访问该节点池的权限。调用接口成功后，系统将返回节点池中所有节点的列表，包括节点ID、名称、状态、IP地址、资源使用情况等详细信息。若节点池不存在、用户无权限访问或节点池当前不可用，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNodePoolNodes
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListNodePoolNodesRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListNodePoolNodesResponse`
        """
        http_info = self._list_node_pool_nodes_http_info(request)
        return self._call_api(**http_info)

    def list_node_pool_nodes_async_invoker(self, request):
        http_info = self._list_node_pool_nodes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_node_pool_nodes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/pools/{pool_name}/nodepools/{nodepool_name}/nodes",
            "request_type": request.__class__.__name__,
            "response_type": "ListNodePoolNodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']
        if 'nodepool_name' in local_var_params:
            path_params['nodepool_name'] = local_var_params['nodepool_name']

        query_params = []
        if '_continue' in local_var_params:
            query_params.append(('continue', local_var_params['_continue']))
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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_node_pools_async(self, request):
        r"""查询节点池列表

        查询节点池列表接口用于获取指定节点池的列表信息。该接口适用于以下场景：当需要查看节点池的配置、状态或管理节点池资源时，用户可通过此接口获取节点池的详细信息。使用该接口的前提条件是节点池已存在且用户具有管理员权限。调用接口成功后，系统将返回节点池的列表，包括节点池ID、名称、节点数量、状态等详细信息。若节点池不存在、用户无权限操作或节点池当前不可用，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNodePools
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListNodePoolsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListNodePoolsResponse`
        """
        http_info = self._list_node_pools_http_info(request)
        return self._call_api(**http_info)

    def list_node_pools_async_invoker(self, request):
        http_info = self._list_node_pools_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_node_pools_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/pools/{pool_name}/nodepools",
            "request_type": request.__class__.__name__,
            "response_type": "ListNodePoolsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_plugin_templates_async(self, request):
        r"""查询插件模板列表

        查询插件模板列表接口用于获取插件模板的基本信息列表。该接口适用于以下场景：当需要浏览或管理插件模板时，用户可通过此接口查询所有可用的插件模板信息，以便选择或进一步操作。使用该接口的前提条件是用户具有访问插件模板的权限，且插件模板服务处于正常运行状态。查询操作完成后，用户将获得插件模板的列表信息，包括模板名称、类型、版本等，便于后续的插件开发或管理。若用户无权限访问、插件模板服务不可用或请求参数无效，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPluginTemplates
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListPluginTemplatesRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListPluginTemplatesResponse`
        """
        http_info = self._list_plugin_templates_http_info(request)
        return self._call_api(**http_info)

    def list_plugin_templates_async_invoker(self, request):
        http_info = self._list_plugin_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_plugin_templates_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/plugintemplates",
            "request_type": request.__class__.__name__,
            "response_type": "ListPluginTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'template_name' in local_var_params:
            query_params.append(('templateName', local_var_params['template_name']))
        if 'pool_name' in local_var_params:
            query_params.append(('poolName', local_var_params['pool_name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_pool_nodes_async(self, request):
        r"""查询资源池节点列表

        查询资源池节点列表接口用于获取指定资源池中的节点信息列表。该接口适用于以下场景：当需要了解资源池中节点的分布、状态或资源使用情况时，用户可通过此接口查询资源池中的节点列表，以便进行资源监控、分配或管理。使用该接口的前提条件是资源池已创建且处于可用状态，且用户具有访问资源池的权限。查询操作完成后，用户将获得资源池中节点的详细信息，包括节点ID、状态、资源使用情况等，便于后续的资源管理和优化。若资源池不存在、用户无权限访问或请求参数无效，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPoolNodes
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListPoolNodesRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListPoolNodesResponse`
        """
        http_info = self._list_pool_nodes_http_info(request)
        return self._call_api(**http_info)

    def list_pool_nodes_async_invoker(self, request):
        http_info = self._list_pool_nodes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_pool_nodes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/pools/{pool_name}/nodes",
            "request_type": request.__class__.__name__,
            "response_type": "ListPoolNodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']

        query_params = []
        if '_continue' in local_var_params:
            query_params.append(('continue', local_var_params['_continue']))
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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_pool_plugins_async(self, request):
        r"""查询插件列表

        查询插件实例列表接口用于获取系统中已部署的插件实例信息。该接口适用于以下场景：当用户需要查看系统中已部署的插件实例、监控插件运行状态、管理插件配置或进行故障排查时，可通过此接口获取插件实例的详细信息。使用该接口的前提条件是用户具有查询权限且系统中已部署至少一个插件实例。调用该接口后，系统将返回所有插件实例的列表，包括插件名称、类型、状态、版本及部署环境等信息。若用户无权限访问或系统中未部署任何插件实例，接口将返回相应的错误信息或空列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPoolPlugins
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListPoolPluginsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListPoolPluginsResponse`
        """
        http_info = self._list_pool_plugins_http_info(request)
        return self._call_api(**http_info)

    def list_pool_plugins_async_invoker(self, request):
        http_info = self._list_pool_plugins_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_pool_plugins_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/pools/{pool_name}/plugins",
            "request_type": request.__class__.__name__,
            "response_type": "ListPoolPluginsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_pool_tags_async(self, request):
        r"""查询资源池的所有标签

        查询资源池所有标签接口用于获取用户当前项目下资源池的所有标签信息，默认查询所有工作空间，但无权限的工作空间不会返回标签数据。该接口适用于以下场景：当需要管理、分类或统计资源池的标签信息时，用户可通过此接口获取资源池的标签数据。使用该接口的前提条件是用户具有访问资源池的权限且资源池已存在。调用接口成功后，系统将返回用户当前项目下所有可访问工作空间的资源池标签信息。若用户无权限访问资源池、资源池不存在或项目未创建，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPoolTags
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListPoolTagsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListPoolTagsResponse`
        """
        http_info = self._list_pool_tags_http_info(request)
        return self._call_api(**http_info)

    def list_pool_tags_async_invoker(self, request):
        http_info = self._list_pool_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_pool_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/pools/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListPoolTagsResponse"
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

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_pools_async(self, request):
        r"""查询资源池列表

        查询资源池列表接口用于获取系统中已创建的资源池信息。该接口适用于以下场景：当用户需要监控资源池状态、进行资源规划、管理资源分配或进行审计时，可通过此接口查询系统中现有的资源池列表。使用该接口的前提条件是用户具有相应的权限，并且系统中已存在资源池。查询操作完成后，接口将返回资源池列表，包含资源池ID、名称、类型、状态、资源配额等详细信息。若用户无权限、系统中无资源池或查询参数有误，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPools
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListPoolsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListPoolsResponse`
        """
        http_info = self._list_pools_http_info(request)
        return self._call_api(**http_info)

    def list_pools_async_invoker(self, request):
        http_info = self._list_pools_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_pools_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/pools",
            "request_type": request.__class__.__name__,
            "response_type": "ListPoolsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'workspace_id' in local_var_params:
            query_params.append(('workspaceId', local_var_params['workspace_id']))
        if 'label_selector' in local_var_params:
            query_params.append(('labelSelector', local_var_params['label_selector']))
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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_resource_flavors_async(self, request):
        r"""查询资源规格列表

        查询资源规格列表接口用于获取可用的资源规格信息。该接口适用于以下场景：当需要查看或选择资源规格以创建资源池、分配资源或了解可用资源规格时，用户可通过此接口获取资源规格的详细信息。使用该接口的前提条件是用户具有相应的权限（如管理员权限或资源管理权限）。调用接口成功后，系统将返回资源规格的列表，包括规格ID、名称、CPU核数、内存大小、存储容量等详细信息。若用户无权限访问该接口或系统中未配置资源规格，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResourceFlavors
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListResourceFlavorsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListResourceFlavorsResponse`
        """
        http_info = self._list_resource_flavors_http_info(request)
        return self._call_api(**http_info)

    def list_resource_flavors_async_invoker(self, request):
        http_info = self._list_resource_flavors_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_resource_flavors_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/resourceflavors",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceFlavorsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if '_continue' in local_var_params:
            query_params.append(('continue', local_var_params['_continue']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'label_selector' in local_var_params:
            query_params.append(('labelSelector', local_var_params['label_selector']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_scheduled_events_async(self, request):
        r"""查询计划事件列表

        查询计划事件列表信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListScheduledEvents
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListScheduledEventsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListScheduledEventsResponse`
        """
        http_info = self._list_scheduled_events_http_info(request)
        return self._call_api(**http_info)

    def list_scheduled_events_async_invoker(self, request):
        http_info = self._list_scheduled_events_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_scheduled_events_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/scheduled-events",
            "request_type": request.__class__.__name__,
            "response_type": "ListScheduledEventsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'workspace_id' in local_var_params:
            query_params.append(('workspaceId', local_var_params['workspace_id']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
            collection_formats['state'] = 'csv'
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'csv'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'node_name' in local_var_params:
            query_params.append(('nodeName', local_var_params['node_name']))
        if 'pool_name' in local_var_params:
            query_params.append(('poolName', local_var_params['pool_name']))
        if 'publish_start_time' in local_var_params:
            query_params.append(('publishStartTime', local_var_params['publish_start_time']))
        if 'publish_end_time' in local_var_params:
            query_params.append(('publishEndTime', local_var_params['publish_end_time']))
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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_training_experiments_async(self, request):
        r"""查询训练实验列表

        查询训练实验列表接口用于获取ModelArts平台上用户已创建的训练实验的列表。
        该接口适用于以下场景：当用户需要查看所有或部分训练实验的概要信息，如实验名称、描述、创建时间等时，可以通过此接口查询训练实验列表。使用该接口的前提条件是用户已登录ModelArts平台并具有查看训练实验的权限。查询操作完成后，系统将返回符合条件的训练实验列表。若用户无权限操作或查询条件不合法，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTrainingExperiments
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListTrainingExperimentsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListTrainingExperimentsResponse`
        """
        http_info = self._list_training_experiments_http_info(request)
        return self._call_api(**http_info)

    def list_training_experiments_async_invoker(self, request):
        http_info = self._list_training_experiments_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_training_experiments_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/training-experiments",
            "request_type": request.__class__.__name__,
            "response_type": "ListTrainingExperimentsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_by' in local_var_params:
            query_params.append(('sort_by', local_var_params['sort_by']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_training_job_events_async(self, request):
        r"""获取训练作业事件列表

        获取训练作业事件列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTrainingJobEvents
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListTrainingJobEventsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListTrainingJobEventsResponse`
        """
        http_info = self._list_training_job_events_http_info(request)
        return self._call_api(**http_info)

    def list_training_job_events_async_invoker(self, request):
        http_info = self._list_training_job_events_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_training_job_events_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/training-jobs/{training_job_id}/events",
            "request_type": request.__class__.__name__,
            "response_type": "ListTrainingJobEventsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'training_job_id' in local_var_params:
            path_params['training_job_id'] = local_var_params['training_job_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'level' in local_var_params:
            query_params.append(('level', local_var_params['level']))
        if 'pattern' in local_var_params:
            query_params.append(('pattern', local_var_params['pattern']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_training_job_stages_async(self, request):
        r"""获取训练作业流程阶段信息列表

        获取训练作业流程阶段信息列表接口用于获取ModelArts平台上指定训练作业的流程阶段信息列表。
        该接口适用于以下场景：当用户需要查看特定训练作业的流程阶段记录时，可以通过此接口获取阶段信息列表。使用该接口的前提条件是用户已知训练作业ID，并具有查看阶段信息列表的权限。查询操作完成后，平台将返回包含训练作业的阶段信息记录。若训练作业ID不存在或用户无权限操作，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTrainingJobStages
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListTrainingJobStagesRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListTrainingJobStagesResponse`
        """
        http_info = self._list_training_job_stages_http_info(request)
        return self._call_api(**http_info)

    def list_training_job_stages_async_invoker(self, request):
        http_info = self._list_training_job_stages_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_training_job_stages_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/training-jobs/{training_job_id}/stages",
            "request_type": request.__class__.__name__,
            "response_type": "ListTrainingJobStagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'training_job_id' in local_var_params:
            path_params['training_job_id'] = local_var_params['training_job_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_training_job_tasks_async(self, request):
        r"""查询训练作业的实例历史调度信息

        查询训练作业调度的实例IP、节点IP等信息，可通过schedule_count参数查询具体的某一次调度的实例信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTrainingJobTasks
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListTrainingJobTasksRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListTrainingJobTasksResponse`
        """
        http_info = self._list_training_job_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_training_job_tasks_async_invoker(self, request):
        http_info = self._list_training_job_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_training_job_tasks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/training-jobs/{training_job_id}/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListTrainingJobTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'training_job_id' in local_var_params:
            path_params['training_job_id'] = local_var_params['training_job_id']

        query_params = []
        if 'schedule_count' in local_var_params:
            query_params.append(('schedule_count', local_var_params['schedule_count']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_training_jobs_async(self, request):
        r"""查询训练作业列表

        根据指定查询条件查询用户创建的训练作业列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTrainingJobs
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListTrainingJobsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListTrainingJobsResponse`
        """
        http_info = self._list_training_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_training_jobs_async_invoker(self, request):
        http_info = self._list_training_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_training_jobs_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/training-job-searches",
            "request_type": request.__class__.__name__,
            "response_type": "ListTrainingJobsResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_workloads_async(self, request):
        r"""查询资源池作业列表

        查询专属资源池作业列表接口用于获取指定专属资源池中的作业信息列表。该接口适用于以下场景：当需要监控专属资源池的资源使用情况、查看作业状态或管理资源分配时，用户可通过此接口获取专属资源池中作业的详细信息。使用该接口的前提条件是专属资源池已存在且用户具有相应的权限（如管理员权限或资源管理权限）。调用接口成功后，系统将返回专属资源池中作业的列表，包括作业ID、名称、状态、资源使用情况等详细信息。若专属资源池不存在、用户无权限操作或资源池当前不可用，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWorkloads
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListWorkloadsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListWorkloadsResponse`
        """
        http_info = self._list_workloads_http_info(request)
        return self._call_api(**http_info)

    def list_workloads_async_invoker(self, request):
        http_info = self._list_workloads_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_workloads_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/pools/{pool_name}/workloads",
            "request_type": request.__class__.__name__,
            "response_type": "ListWorkloadsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']

        query_params = []
        if 'hostip' in local_var_params:
            query_params.append(('hostip', local_var_params['hostip']))
            collection_formats['hostip'] = 'csv'
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'ascend' in local_var_params:
            query_params.append(('ascend', local_var_params['ascend']))
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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_workspace_async(self, request):
        r"""查询工作空间列表

        查询工作空间列表，响应消息体中包含详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWorkspace
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListWorkspaceRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListWorkspaceResponse`
        """
        http_info = self._list_workspace_http_info(request)
        return self._call_api(**http_info)

    def list_workspace_async_invoker(self, request):
        http_info = self._list_workspace_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_workspace_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces",
            "request_type": request.__class__.__name__,
            "response_type": "ListWorkspaceResponse"
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
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'filter_accessible' in local_var_params:
            query_params.append(('filter_accessible', local_var_params['filter_accessible']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def modify_infer_intranet_connections_async(self, request):
        r"""修改添加自定义URL申请

        本接口用于修改添加内网自定义URL请求，适用于需要同时更新或者添加多个内网接入点的场景。调用此接口前，确保调用者具备相应的更新权限，提供需要更新的参数，如IP地址、VPC ID、子网ID等。指定的内网接入点将添加新的配置，新的配置将对相关服务生效。如果提供的内网接入点ID列表中包含无效或不存在的ID，接口将返回相应的异常信息，提示用户检查ID的有效性，如果提供的更新参数不符合格式要求（如IP地址格式不正确），接口将返回相应的异常信息，提示用户检查参数的有效性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ModifyInferIntranetConnections
        :type request: :class:`huaweicloudsdkmodelarts.v1.ModifyInferIntranetConnectionsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ModifyInferIntranetConnectionsResponse`
        """
        http_info = self._modify_infer_intranet_connections_http_info(request)
        return self._call_api(**http_info)

    def modify_infer_intranet_connections_async_invoker(self, request):
        http_info = self._modify_infer_intranet_connections_http_info(request)
        return AsyncInvoker(self, http_info)

    def _modify_infer_intranet_connections_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/intranet-connection/{id}/modify",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyInferIntranetConnectionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def notify_training_job_information_async(self, request):
        r"""训练作业事件上报接口

        训练事件上报给业务面
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NotifyTrainingJobInformation
        :type request: :class:`huaweicloudsdkmodelarts.v1.NotifyTrainingJobInformationRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NotifyTrainingJobInformationResponse`
        """
        http_info = self._notify_training_job_information_http_info(request)
        return self._call_api(**http_info)

    def notify_training_job_information_async_invoker(self, request):
        http_info = self._notify_training_job_information_http_info(request)
        return AsyncInvoker(self, http_info)

    def _notify_training_job_information_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/training-jobs/{training_job_id}/tasks/{task_id}/reports/{report_type}",
            "request_type": request.__class__.__name__,
            "response_type": "NotifyTrainingJobInformationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'training_job_id' in local_var_params:
            path_params['training_job_id'] = local_var_params['training_job_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']
        if 'report_type' in local_var_params:
            path_params['report_type'] = local_var_params['report_type']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def patch_network_async(self, request):
        r"""更新网络资源

        更新网络资源接口用于修改指定网络资源的配置信息。该接口适用于以下场景：当需要调整网络资源的属性、修复配置错误或优化资源设置时，用户可通过此接口更新指定网络资源的详细信息。使用该接口的前提条件是网络资源已存在且用户具有管理员权限。更新操作完成后，指定网络资源的配置信息将被成功修改，系统将反映最新的资源状态和属性。若指定的网络资源不存在、用户无权限操作或输入参数有误，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PatchNetwork
        :type request: :class:`huaweicloudsdkmodelarts.v1.PatchNetworkRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PatchNetworkResponse`
        """
        http_info = self._patch_network_http_info(request)
        return self._call_api(**http_info)

    def patch_network_async_invoker(self, request):
        http_info = self._patch_network_http_info(request)
        return AsyncInvoker(self, http_info)

    def _patch_network_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/networks/{network_name}",
            "request_type": request.__class__.__name__,
            "response_type": "PatchNetworkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'network_name' in local_var_params:
            path_params['network_name'] = local_var_params['network_name']

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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def patch_node_pool_async(self, request):
        r"""更新节点池

        更新节点池接口用于修改指定节点池的配置信息。该接口适用于以下场景：当需要扩展节点池容量、调整节点规格、优化资源分配或修复节点池配置时，用户可通过此接口更新节点池的相关信息。使用该接口的前提条件是节点池已存在且用户具有管理员权限。更新操作完成后，节点池的配置将被更新，包括节点数量、规格、网络配置等参数。若节点池不存在、用户无权限操作或配置参数错误，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PatchNodePool
        :type request: :class:`huaweicloudsdkmodelarts.v1.PatchNodePoolRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PatchNodePoolResponse`
        """
        http_info = self._patch_node_pool_http_info(request)
        return self._call_api(**http_info)

    def patch_node_pool_async_invoker(self, request):
        http_info = self._patch_node_pool_http_info(request)
        return AsyncInvoker(self, http_info)

    def _patch_node_pool_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v2/{project_id}/pools/{pool_name}/nodepools/{nodepool_name}",
            "request_type": request.__class__.__name__,
            "response_type": "PatchNodePoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']
        if 'nodepool_name' in local_var_params:
            path_params['nodepool_name'] = local_var_params['nodepool_name']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def patch_pool_async(self, request):
        r"""更新资源池

        更新资源池接口用于修改指定资源池的配置和容量。该接口适用于以下场景：当资源池需要扩展容量、调整配置或优化性能时，用户可通过此接口更新资源池的相关信息。使用该接口的前提条件是资源池已存在且用户具有管理员权限。更新操作完成后，资源池的配置和容量将被更新，相关资源和配置也将被调整。若资源池不存在、用户无权限操作或资源池处于不可更新状态，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PatchPool
        :type request: :class:`huaweicloudsdkmodelarts.v1.PatchPoolRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PatchPoolResponse`
        """
        http_info = self._patch_pool_http_info(request)
        return self._call_api(**http_info)

    def patch_pool_async_invoker(self, request):
        http_info = self._patch_pool_http_info(request)
        return AsyncInvoker(self, http_info)

    def _patch_pool_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v2/{project_id}/pools/{pool_name}",
            "request_type": request.__class__.__name__,
            "response_type": "PatchPoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']

        query_params = []

        header_params = {}
        if 'x_model_arts_user_id' in local_var_params:
            header_params['X-ModelArts-User-ID'] = local_var_params['x_model_arts_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def register_image_async(self, request):
        r"""注册自定义镜像

        注册自定义镜像接口用于将用户自定义的镜像注册到ModelArts镜像管理。该接口适用于以下场景：当用户需要将自己的自定义镜像（如特定算法环境、工具链或配置）集成到ModelArts平台时，可通过此接口将镜像注册到镜像管理中以便后续使用。使用该接口的前提条件是用户具备ModelArts镜像管理权限，并且需要提供有效的镜像地址和符合要求的镜像格式。注册操作完成后，自定义镜像将被成功添加到ModelArts镜像列表中，用户可以在后续任务中选择使用该镜像。若镜像地址无效、镜像格式不符合要求或用户无权限操作，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RegisterImage
        :type request: :class:`huaweicloudsdkmodelarts.v1.RegisterImageRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.RegisterImageResponse`
        """
        http_info = self._register_image_http_info(request)
        return self._call_api(**http_info)

    def register_image_async_invoker(self, request):
        http_info = self._register_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _register_image_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/images",
            "request_type": request.__class__.__name__,
            "response_type": "RegisterImageResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_algorithm_by_uuid_async(self, request):
        r"""查询算法详情

        根据算法id查询指定算法。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAlgorithmByUuid
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowAlgorithmByUuidRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowAlgorithmByUuidResponse`
        """
        http_info = self._show_algorithm_by_uuid_http_info(request)
        return self._call_api(**http_info)

    def show_algorithm_by_uuid_async_invoker(self, request):
        http_info = self._show_algorithm_by_uuid_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_algorithm_by_uuid_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/algorithms/{algorithm_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAlgorithmByUuidResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'algorithm_id' in local_var_params:
            path_params['algorithm_id'] = local_var_params['algorithm_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_authmode_detail_async(self, request):
        r"""查询授权模式

        查询授权模式接口用于获取指定资源或功能的授权方式和权限配置信息。该接口适用于以下场景：当系统管理员需要查看资源的访问权限设置、开发者需要验证授权策略配置是否正确，或安全审计人员需要检查授权配置是否符合安全规范时，可通过此接口查询授权模式的详细信息。使用该接口的前提条件是用户具有查询权限且目标资源或功能的授权模式已配置。调用成功后，接口将返回授权模式的类型、规则及权限范围等详细信息。若用户无权限访问该接口，或目标资源的授权模式未配置，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAuthmodeDetail
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowAuthmodeDetailRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowAuthmodeDetailResponse`
        """
        http_info = self._show_authmode_detail_http_info(request)
        return self._call_api(**http_info)

    def show_authmode_detail_async_invoker(self, request):
        http_info = self._show_authmode_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_authmode_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/auth-mode",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuthmodeDetailResponse"
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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_auto_search_param_analysis_result_path_async(self, request):
        r"""获取某个超参敏感度分析图像的路径

        获取某个超参敏感度分析图像的保存路径。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAutoSearchParamAnalysisResultPath
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowAutoSearchParamAnalysisResultPathRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowAutoSearchParamAnalysisResultPathResponse`
        """
        http_info = self._show_auto_search_param_analysis_result_path_http_info(request)
        return self._call_api(**http_info)

    def show_auto_search_param_analysis_result_path_async_invoker(self, request):
        http_info = self._show_auto_search_param_analysis_result_path_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_auto_search_param_analysis_result_path_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/training-jobs/{training_job_id}/autosearch-parameter-analysis/{parameter_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutoSearchParamAnalysisResultPathResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'parameter_name' in local_var_params:
            path_params['parameter_name'] = local_var_params['parameter_name']
        if 'training_job_id' in local_var_params:
            path_params['training_job_id'] = local_var_params['training_job_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_auto_search_params_analysis_async(self, request):
        r"""获取超参敏感度分析结果

        获取超参敏感度分析结果的汇总表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAutoSearchParamsAnalysis
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowAutoSearchParamsAnalysisRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowAutoSearchParamsAnalysisResponse`
        """
        http_info = self._show_auto_search_params_analysis_http_info(request)
        return self._call_api(**http_info)

    def show_auto_search_params_analysis_async_invoker(self, request):
        http_info = self._show_auto_search_params_analysis_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_auto_search_params_analysis_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/training-jobs/{training_job_id}/autosearch-parameter-analysis",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutoSearchParamsAnalysisResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'training_job_id' in local_var_params:
            path_params['training_job_id'] = local_var_params['training_job_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_auto_search_per_trial_async(self, request):
        r"""查询超参搜索某个trial的结果

        根据传入的trial_id，查询指定trial的搜索结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAutoSearchPerTrial
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowAutoSearchPerTrialRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowAutoSearchPerTrialResponse`
        """
        http_info = self._show_auto_search_per_trial_http_info(request)
        return self._call_api(**http_info)

    def show_auto_search_per_trial_async_invoker(self, request):
        http_info = self._show_auto_search_per_trial_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_auto_search_per_trial_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/training-jobs/{training_job_id}/autosearch-trials/{trial_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutoSearchPerTrialResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'training_job_id' in local_var_params:
            path_params['training_job_id'] = local_var_params['training_job_id']
        if 'trial_id' in local_var_params:
            path_params['trial_id'] = local_var_params['trial_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_auto_search_trial_early_stop_async(self, request):
        r"""提前终止自动化搜索作业的某个trial

        提前终止自动化搜索作业的某个trial。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAutoSearchTrialEarlyStop
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowAutoSearchTrialEarlyStopRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowAutoSearchTrialEarlyStopResponse`
        """
        http_info = self._show_auto_search_trial_early_stop_http_info(request)
        return self._call_api(**http_info)

    def show_auto_search_trial_early_stop_async_invoker(self, request):
        http_info = self._show_auto_search_trial_early_stop_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_auto_search_trial_early_stop_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/training-jobs/{training_job_id}/autosearch-trial-earlystop/{trial_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutoSearchTrialEarlyStopResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'training_job_id' in local_var_params:
            path_params['training_job_id'] = local_var_params['training_job_id']
        if 'trial_id' in local_var_params:
            path_params['trial_id'] = local_var_params['trial_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_auto_search_trials_async(self, request):
        r"""查询超参搜索所有trial的结果

        查询超参搜索所有trial的结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAutoSearchTrials
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowAutoSearchTrialsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowAutoSearchTrialsResponse`
        """
        http_info = self._show_auto_search_trials_http_info(request)
        return self._call_api(**http_info)

    def show_auto_search_trials_async_invoker(self, request):
        http_info = self._show_auto_search_trials_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_auto_search_trials_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/training-jobs/{training_job_id}/autosearch-trials",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutoSearchTrialsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'training_job_id' in local_var_params:
            path_params['training_job_id'] = local_var_params['training_job_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_auto_search_yaml_template_content_async(self, request):
        r"""获取自动化搜索作业yaml模板的内容

        获取自动化搜索作业yaml模板的内容。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAutoSearchYamlTemplateContent
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowAutoSearchYamlTemplateContentRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowAutoSearchYamlTemplateContentResponse`
        """
        http_info = self._show_auto_search_yaml_template_content_http_info(request)
        return self._call_api(**http_info)

    def show_auto_search_yaml_template_content_async_invoker(self, request):
        http_info = self._show_auto_search_yaml_template_content_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_auto_search_yaml_template_content_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/training-jobs/autosearch/yaml-templates/{algorithm_type}/{algorithm_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutoSearchYamlTemplateContentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'algorithm_type' in local_var_params:
            path_params['algorithm_type'] = local_var_params['algorithm_type']
        if 'algorithm_name' in local_var_params:
            path_params['algorithm_name'] = local_var_params['algorithm_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_auto_search_yaml_templates_info_async(self, request):
        r"""获取自动化搜索作业yaml模板的信息

        获取自动化搜索作业yaml模板的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAutoSearchYamlTemplatesInfo
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowAutoSearchYamlTemplatesInfoRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowAutoSearchYamlTemplatesInfoResponse`
        """
        http_info = self._show_auto_search_yaml_templates_info_http_info(request)
        return self._call_api(**http_info)

    def show_auto_search_yaml_templates_info_async_invoker(self, request):
        http_info = self._show_auto_search_yaml_templates_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_auto_search_yaml_templates_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/training-jobs/autosearch/yaml-templates",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutoSearchYamlTemplatesInfoResponse"
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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_dynamic_storage_async(self, request):
        r"""获取动态挂载存储实例详情

        获取动态挂载OBS实例详情接口用于获取已挂载到运行中Notebook实例中的存储实例的详细信息。
        
        适用场景：用户需要查看Notebook实例中已挂载的存储实例的详细信息时，可通过此接口获取。使用该接口的前提条件是用户已登录系统并具有访问目标Notebook实例的权限。调用该接口后，系统将返回指定Notebook实例中挂载的存储实例的详细信息。若用户无权限访问指定实例，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDynamicStorage
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowDynamicStorageRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowDynamicStorageResponse`
        """
        http_info = self._show_dynamic_storage_http_info(request)
        return self._call_api(**http_info)

    def show_dynamic_storage_async_invoker(self, request):
        http_info = self._show_dynamic_storage_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_dynamic_storage_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/notebooks/{instance_id}/storage/{storage_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDynamicStorageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'storage_id' in local_var_params:
            path_params['storage_id'] = local_var_params['storage_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_image_async(self, request):
        r"""查询镜像详情

        查询镜像详情接口用于查询镜像的详细信息。该接口适用于以下场景：当用户需要了解特定镜像的详细信息（如镜像名称、版本、创建时间、大小、状态等）或对镜像执行一些操作时，可通过此接口获取镜像的详细信息。使用该接口的前提条件是用户具备镜像管理权限，并且待查询镜像有效且存在。查询操作完成后，将返回镜像的详细信息，包括镜像ID、名称、版本、创建时间、大小以及状态等。若镜像不存在或用户无权限访问，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowImage
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowImageRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowImageResponse`
        """
        http_info = self._show_image_http_info(request)
        return self._call_api(**http_info)

    def show_image_async_invoker(self, request):
        http_info = self._show_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_image_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/images/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_infer_deployment_async(self, request):
        r"""查询服务部署详情

        通过服务ID、部署ID查询对应的部署详情，调用者可以通过有效的服务ID、部署ID获取部署的名称、状态、服务实例、配置参数等详细信息。调用者需具有足够的权限，且输入的服务ID、部署ID必须有效。查询成功时返回部署详细信息，查询失败时返回特定的错误码和错误信息。若服务ID或者部署ID无效、版本号不存在或用户无权限，则返回400 Bad Request或403 Forbidden；
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInferDeployment
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowInferDeploymentRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowInferDeploymentResponse`
        """
        http_info = self._show_infer_deployment_http_info(request)
        return self._call_api(**http_info)

    def show_infer_deployment_async_invoker(self, request):
        http_info = self._show_infer_deployment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_infer_deployment_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/services/{service_id}/deployments/{deployment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInferDeploymentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_infer_deployment_version_async(self, request):
        r"""查询在线服务部署版本详情

        此接口用于获取指定服务部署版本的详细信息，适用于需要查看特定版本的详细配置和状态的场景，例如确认版本的功能、性能参数或发布历史。请求需包含有效的服务ID、部署ID及版本号。用户必须具有对目标服务部署的查看权限。请求成功后，返回该版本的详细信息，包括版本号、发布时间、配置参数和状态。若服务ID、部署ID无效、版本号不存在或用户无权限，则返回400 Bad Request或403 Forbidden；若服务部署无该版本信息，则返回404 Not Found。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInferDeploymentVersion
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowInferDeploymentVersionRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowInferDeploymentVersionResponse`
        """
        http_info = self._show_infer_deployment_version_http_info(request)
        return self._call_api(**http_info)

    def show_infer_deployment_version_async_invoker(self, request):
        http_info = self._show_infer_deployment_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_infer_deployment_version_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/services/{service_id}/deployments/{deployment_id}/versions/{version}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInferDeploymentVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_infer_service_async(self, request):
        r"""查询服务详情

        通过服务ID查询对应的服务详情，调用者可以通过有效的服务ID获取服务的名称、状态、服务实例、配置参数等详细信息。调用者需具有足够的权限，且输入的服务ID必须有效。查询成功时返回服务详细信息，查询失败时返回特定的错误码和错误信息。若服务ID无效、版本号不存在或用户无权限，则返回400 Bad Request或403 Forbidden。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInferService
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowInferServiceRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowInferServiceResponse`
        """
        http_info = self._show_infer_service_http_info(request)
        return self._call_api(**http_info)

    def show_infer_service_async_invoker(self, request):
        http_info = self._show_infer_service_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_infer_service_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/services/{service_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInferServiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_infer_service_cluster_async(self, request):
        r"""查询纳管资源池详情

        该接口允许用户通过指定资源池的ID来查询纳管资源池的详细信息，包括实例ID、名称、Flavor规格、实例状态和实例可访问的URL。此功能适用于需要监控或管理云资源的用户，使用该接口前，用户需确保已拥有访问权限及正确的资源池ID。执行成功后，用户将获得所需的实例详情，可用于进一步的资源管理和配置。如果资源池ID无效或用户没有相应的访问权限，接口将返回错误信息，如404 Not Found或401 Unauthorized。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInferServiceCluster
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowInferServiceClusterRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowInferServiceClusterResponse`
        """
        http_info = self._show_infer_service_cluster_http_info(request)
        return self._call_api(**http_info)

    def show_infer_service_cluster_async_invoker(self, request):
        http_info = self._show_infer_service_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_infer_service_cluster_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/services/clusters/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInferServiceClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_user_token' in local_var_params:
            header_params['X-User-Token'] = local_var_params['x_user_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_infer_service_tags_async(self, request):
        r"""查询资源标签

        该接口适用于需要获取资源（如模型、数据集、服务等）的标签信息的场景，例如在资源管理或分类中，用户可以通过查询标签来了解资源的用途、状态或其他属性。通过调用此接口，用户可以通过资源ID获取指定资源的所有标签列表。用户必须具有足够的权限，且目标资源需存在。查询成功后，返回资源的标签列表；若失败，返回具体的错误信息。常见异常包括权限验证错误、资源不存在错误和参数验证错误。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInferServiceTags
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowInferServiceTagsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowInferServiceTagsResponse`
        """
        http_info = self._show_infer_service_tags_http_info(request)
        return self._call_api(**http_info)

    def show_infer_service_tags_async_invoker(self, request):
        http_info = self._show_infer_service_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_infer_service_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/modelarts-service-v2/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInferServiceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_network_async(self, request):
        r"""查询网络资源

        查询网络资源接口用于获取指定网络资源的详情信息。该接口适用于以下场景：当用户需要查看特定网络资源的详细配置、状态或属性时，可通过此接口查询指定网络资源的详细信息。使用该接口的前提条件是用户具有相应的权限，并且指定的网络资源已存在于系统中。查询操作完成后，接口将返回指定网络资源的详细信息，包括资源ID、类型、状态、配置参数等。若指定的网络资源不存在、用户无权限操作或输入参数有误，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNetwork
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowNetworkRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowNetworkResponse`
        """
        http_info = self._show_network_http_info(request)
        return self._call_api(**http_info)

    def show_network_async_invoker(self, request):
        http_info = self._show_network_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_network_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/networks/{network_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNetworkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'network_name' in local_var_params:
            path_params['network_name'] = local_var_params['network_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_network_available_ip_async(self, request):
        r"""查询网络可用的IP

        查询网络可用的IP接口用于查找指定网络中未被占用的IP地址。该接口适用于以下场景：在网络规划、资源分配或故障排查时，用户需要快速获取可用的IP地址信息。使用该接口的前提条件是用户具有访问目标网络的权限，并且需要提供有效的网络范围（如子网掩码或IP段）。查询完成后，接口将返回指定网络中未被占用的IP地址列表，用户可以根据结果进行IP地址的分配或进一步操作。若网络不可达、权限不足或网络范围有误，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNetworkAvailableIp
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowNetworkAvailableIpRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowNetworkAvailableIpResponse`
        """
        http_info = self._show_network_available_ip_http_info(request)
        return self._call_api(**http_info)

    def show_network_available_ip_async_invoker(self, request):
        http_info = self._show_network_available_ip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_network_available_ip_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/networks/{network_name}/network-ip-availabilities",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNetworkAvailableIpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'network_name' in local_var_params:
            path_params['network_name'] = local_var_params['network_name']

        query_params = []
        if 'network_id' in local_var_params:
            query_params.append(('network_id', local_var_params['network_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_node_config_template_async(self, request):
        r"""查询节点配置模板

        查询节点配置模板接口用于获取指定节点配置模板的详细信息。该接口适用于以下场景：当用户需要查看节点配置模板的内容、管理节点配置或进行相关操作时，可通过此接口获取指定节点配置模板的详细信息。使用该接口的前提条件是节点配置模板已存在且用户具有相应的访问权限。调用该接口后，系统将返回指定节点配置模板的详细信息，包括模板名称、版本、配置参数及描述等。若节点配置模板不存在或用户无权限访问，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNodeConfigTemplate
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowNodeConfigTemplateRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowNodeConfigTemplateResponse`
        """
        http_info = self._show_node_config_template_http_info(request)
        return self._call_api(**http_info)

    def show_node_config_template_async_invoker(self, request):
        http_info = self._show_node_config_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_node_config_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/nodeconfigtemplates/{nodeconfigtemplate_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNodeConfigTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'nodeconfigtemplate_name' in local_var_params:
            path_params['nodeconfigtemplate_name'] = local_var_params['nodeconfigtemplate_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_node_pool_async(self, request):
        r"""查询指定节点池详情

        查询指定节点池详情接口用于获取指定节点池的详细信息。该接口适用于以下场景：当需要查看节点池的配置、状态、资源使用情况或管理节点池时，用户可通过此接口获取节点池的详细信息。使用该接口的前提条件是节点池已存在且用户具有访问该节点池的权限。调用接口成功后，系统将返回节点池的详细信息，包括节点池ID、名称、节点数量、状态、创建时间、配置参数等。若节点池不存在、用户无权限访问或节点池当前不可用，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNodePool
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowNodePoolRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowNodePoolResponse`
        """
        http_info = self._show_node_pool_http_info(request)
        return self._call_api(**http_info)

    def show_node_pool_async_invoker(self, request):
        http_info = self._show_node_pool_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_node_pool_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/pools/{pool_name}/nodepools/{nodepool_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNodePoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']
        if 'nodepool_name' in local_var_params:
            path_params['nodepool_name'] = local_var_params['nodepool_name']

        query_params = []
        if '_continue' in local_var_params:
            query_params.append(('continue', local_var_params['_continue']))
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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_obs_url_of_training_job_logs_async(self, request):
        r"""查询训练作业指定任务的日志（OBS链接）

        查询训练作业指定任务的日志（OBS临时链接，有效期5分钟），可全量查看或直接下载。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowObsUrlOfTrainingJobLogs
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowObsUrlOfTrainingJobLogsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowObsUrlOfTrainingJobLogsResponse`
        """
        http_info = self._show_obs_url_of_training_job_logs_http_info(request)
        return self._call_api(**http_info)

    def show_obs_url_of_training_job_logs_async_invoker(self, request):
        http_info = self._show_obs_url_of_training_job_logs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_obs_url_of_training_job_logs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/training-jobs/{training_job_id}/tasks/{task_id}/logs/url",
            "request_type": request.__class__.__name__,
            "response_type": "ShowObsUrlOfTrainingJobLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'training_job_id' in local_var_params:
            path_params['training_job_id'] = local_var_params['training_job_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_order_async(self, request):
        r"""查询订单详情

        查询订单详情接口用于获取指定订单的详细信息。该接口适用于以下场景：当需要查看订单的状态、金额、商品信息或处理订单相关问题时，用户可通过此接口获取订单的详细数据。使用该接口的前提条件是订单已存在且用户具有访问该订单的权限。调用接口成功后，系统将返回订单的详细信息，包括订单号、商品列表、金额、支付状态、下单时间等。若订单不存在、用户无权限访问或订单信息未正确配置，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOrder
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowOrderRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowOrderResponse`
        """
        http_info = self._show_order_http_info(request)
        return self._call_api(**http_info)

    def show_order_async_invoker(self, request):
        http_info = self._show_order_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_order_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/orders/{order_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOrderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'order_name' in local_var_params:
            path_params['order_name'] = local_var_params['order_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_os_config_async(self, request):
        r"""查询OS的配置参数

        查询OS的配置参数接口用于获取ModelArts OS服务的配置参数，如网络网段、用户资源配额等。该接口适用于以下场景：当需要了解当前ModelArts OS服务的网络配置、资源分配情况或进行系统管理时，用户可通过此接口查询相关的配置参数。使用该接口的前提条件是用户具有访问ModelArts OS服务的权限，且服务处于正常运行状态。查询操作完成后，用户将获得指定的配置参数信息，便于进行后续的资源规划或系统优化。若用户无权限访问、服务不可用或请求参数无效，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOsConfig
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowOsConfigRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowOsConfigResponse`
        """
        http_info = self._show_os_config_http_info(request)
        return self._call_api(**http_info)

    def show_os_config_async_invoker(self, request):
        http_info = self._show_os_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_os_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/os-user-config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOsConfigResponse"
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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_os_quota_async(self, request):
        r"""查询OS的配额

        查询OS配额接口用于获取ModelArts OS服务中部分资源的配额信息，如资源池配额、网络配额等。该接口适用于以下场景：当需要了解资源池或网络资源的使用限制、规划资源分配或监控资源使用情况时，用户可通过此接口获取相关配额信息。使用该接口的前提条件是ModelArts OS服务已部署且用户具有相应的权限（如管理员权限或资源管理权限）。调用接口成功后，系统将返回资源池配额、网络配额等详细信息，帮助用户更好地进行资源规划和管理。若用户无权限访问该接口、服务不可用或配额信息未配置，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOsQuota
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowOsQuotaRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowOsQuotaResponse`
        """
        http_info = self._show_os_quota_http_info(request)
        return self._call_api(**http_info)

    def show_os_quota_async_invoker(self, request):
        http_info = self._show_os_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_os_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOsQuotaResponse"
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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_plugin_template_async(self, request):
        r"""查询插件模板

        查询插件模板接口用于获取指定插件模板的详细信息。该接口适用于以下场景：当需要了解特定插件模板的配置、功能或使用方式时，用户可通过此接口查询插件模板的详细信息。使用该接口的前提条件是插件模板已存在且用户具有访问权限。查询操作完成后，用户将获得指定插件模板的详细信息，包括模板的配置参数、功能描述等，便于后续的插件开发或配置管理。若插件模板不存在或用户无权限访问，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPluginTemplate
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowPluginTemplateRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowPluginTemplateResponse`
        """
        http_info = self._show_plugin_template_http_info(request)
        return self._call_api(**http_info)

    def show_plugin_template_async_invoker(self, request):
        http_info = self._show_plugin_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_plugin_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/plugintemplates/{plugintemplate_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPluginTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'plugintemplate_name' in local_var_params:
            path_params['plugintemplate_name'] = local_var_params['plugintemplate_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_pool_async(self, request):
        r"""查询资源池

        查询资源池信息接口用于获取指定资源池的详细信息。该接口适用于以下场景：当用户需要查看特定资源池的详细配置、状态、资源使用情况或进行资源管理时，可通过此接口查询指定资源池的详细信息。使用该接口的前提条件是用户具有相应的权限，并且指定的资源池已存在于系统中。查询操作完成后，接口将返回资源池的详细信息，包括资源池ID、名称、类型、状态、资源配额、利用率等。若指定的资源池不存在、用户无权限操作或输入参数有误，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPool
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowPoolRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowPoolResponse`
        """
        http_info = self._show_pool_http_info(request)
        return self._call_api(**http_info)

    def show_pool_async_invoker(self, request):
        http_info = self._show_pool_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_pool_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/pools/{pool_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']

        query_params = []

        header_params = {}
        if 'x_model_arts_user_id' in local_var_params:
            header_params['X-ModelArts-User-ID'] = local_var_params['x_model_arts_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_pool_monitor_async(self, request):
        r"""资源池监控

        资源池监控接口用于获取指定资源池的实时或历史监控信息。该接口适用于以下场景：当需要实时查看资源池的资源使用情况、性能状态或历史数据时，用户可通过此接口获取资源池的监控数据。使用该接口的前提条件是资源池已存在且用户具有管理员权限。调用接口成功后，系统将返回资源池的监控信息，包括资源使用率、性能指标及历史趋势等数据。若资源池不存在、用户无权限操作或资源池当前不可用，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPoolMonitor
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowPoolMonitorRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowPoolMonitorResponse`
        """
        http_info = self._show_pool_monitor_http_info(request)
        return self._call_api(**http_info)

    def show_pool_monitor_async_invoker(self, request):
        http_info = self._show_pool_monitor_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_pool_monitor_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/pools/{pool_name}/monitor",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPoolMonitorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']

        query_params = []
        if 'time_range' in local_var_params:
            query_params.append(('time_range', local_var_params['time_range']))
        if 'statistics' in local_var_params:
            query_params.append(('statistics', local_var_params['statistics']))
        if 'period' in local_var_params:
            query_params.append(('period', local_var_params['period']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_pool_node_async(self, request):
        r"""查询资源池单个节点详情

        查询资源池中的单个节点接口用于获取指定资源池内单个节点的详细信息。该接口适用于以下场景：当用户需要了解节点资源分配、详细信息时，可通过此接口获取节点的类型、状态、配置参数及关联服务等信息。使用该接口的前提条件是目标资源池已存在且用户具备查看权限，同时需提供有效的资源池标识符作为输入参数。接口调用后，系统将返回资源池中单个节点数据；若资源池不存在、用户权限不足或输入参数无效，接口将返回对应的错误信息（如404未找到资源池或403权限拒绝）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPoolNode
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowPoolNodeRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowPoolNodeResponse`
        """
        http_info = self._show_pool_node_http_info(request)
        return self._call_api(**http_info)

    def show_pool_node_async_invoker(self, request):
        http_info = self._show_pool_node_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_pool_node_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/pools/{pool_name}/nodes/{node_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPoolNodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']
        if 'node_name' in local_var_params:
            path_params['node_name'] = local_var_params['node_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_pool_node_config_async(self, request):
        r"""查询资源池节点自定义配置

        查询资源池节点自定义配置接口用于获取指定资源池节点的自定义配置信息。该接口适用于以下场景：当需要查看资源池节点的详细配置、优化资源分配或管理节点资源时，用户可通过此接口获取节点的自定义配置数据。使用该接口的前提条件是资源池节点已存在且用户具有访问该节点的权限。调用接口成功后，系统将返回资源池节点的自定义配置信息，包括硬件规格、软件环境、网络设置等详细参数。若资源池节点不存在、用户无权限访问或节点配置信息未正确配置，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPoolNodeConfig
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowPoolNodeConfigRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowPoolNodeConfigResponse`
        """
        http_info = self._show_pool_node_config_http_info(request)
        return self._call_api(**http_info)

    def show_pool_node_config_async_invoker(self, request):
        http_info = self._show_pool_node_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_pool_node_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/pools/{pool_name}/node-config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPoolNodeConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_pool_node_config_template_async(self, request):
        r"""查询资源池节点自定义配置模板

        查询资源池节点自定义配置模板接口用于获取节点配置模板的结构定义与参数规范。该接口适用于以下场景：当需要了解节点自定义配置的模板结构（如参数字段、校验规则、示例值）、验证配置模板是否符合规范或进行配置模板选型时，用户可通过此接口获取模板的元数据（如参数说明、类型限制、依赖关系等）。使用该接口的前提条件是目标配置模板必须已注册至系统且处于可访问状态，调用者需具备模板查看权限，且系统配置管理服务正常运行。查询操作完成后，系统将返回模板的完整定义信息（如参数列表、版本号、更新时间等），且不会对模板内容或节点配置产生影响。若模板未注册、用户权限不足或系统服务异常，接口将返回对应的错误信息（如\&quot;404 Not Found\&quot;、\&quot;403 Forbidden\&quot;或\&quot;503 Service Unavailable\&quot;）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPoolNodeConfigTemplate
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowPoolNodeConfigTemplateRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowPoolNodeConfigTemplateResponse`
        """
        http_info = self._show_pool_node_config_template_http_info(request)
        return self._call_api(**http_info)

    def show_pool_node_config_template_async_invoker(self, request):
        http_info = self._show_pool_node_config_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_pool_node_config_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/pools/{pool_name}/node-config-template",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPoolNodeConfigTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_pool_runtime_metrics_async(self, request):
        r"""查询资源实时利用率

        查询资源实时利用率接口用于获取当前项目下所有资源池的实时利用率信息。该接口适用于以下场景：当用户需要监控资源使用情况、进行资源优化、容量规划或故障排查时，可通过此接口查询资源池的实时利用率，包括CPU、内存、存储等资源的使用情况。使用该接口的前提条件是用户具有访问该项目的权限，并且资源池已存在且处于运行状态。查询操作完成后，接口将返回资源池的实时利用率数据，包含利用率百分比、资源类型、时间戳等详细信息。若用户无权限、资源池不存在或系统无法获取实时数据，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPoolRuntimeMetrics
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowPoolRuntimeMetricsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowPoolRuntimeMetricsResponse`
        """
        http_info = self._show_pool_runtime_metrics_http_info(request)
        return self._call_api(**http_info)

    def show_pool_runtime_metrics_async_invoker(self, request):
        http_info = self._show_pool_runtime_metrics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_pool_runtime_metrics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/metrics/runtime/pools",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPoolRuntimeMetricsResponse"
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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_pool_statistics_async(self, request):
        r"""资源池统计

        资源池统计接口用于获取指定资源池的统计信息。该接口适用于以下场景：当需要了解资源池的资源使用情况、分配情况或利用率时，用户可通过此接口获取资源池的统计数据。使用该接口的前提条件是资源池已存在且用户具有管理员权限。调用接口成功后，系统将返回资源池的统计信息，包括资源使用总量、已分配量、利用率及资源分配趋势等数据。若资源池不存在、用户无权限操作或资源池当前不可用，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPoolStatistics
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowPoolStatisticsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowPoolStatisticsResponse`
        """
        http_info = self._show_pool_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_pool_statistics_async_invoker(self, request):
        http_info = self._show_pool_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_pool_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/statistics/pools",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPoolStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'workspace_id' in local_var_params:
            query_params.append(('workspaceId', local_var_params['workspace_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_pool_tags_async(self, request):
        r"""查询资源池上的标签

        查询资源池的标签接口用于获取指定资源池的标签信息。该接口适用于以下场景：当需要查看、管理或统计特定资源池的标签信息时，用户可通过此接口获取资源池的标签数据。使用该接口的前提条件是资源池已存在且用户具有访问该资源池的权限。调用接口成功后，系统将返回指定资源池的标签信息，包括标签键和标签值。若资源池不存在、用户无权限访问或资源池未配置标签，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPoolTags
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowPoolTagsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowPoolTagsResponse`
        """
        http_info = self._show_pool_tags_http_info(request)
        return self._call_api(**http_info)

    def show_pool_tags_async_invoker(self, request):
        http_info = self._show_pool_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_pool_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/pools/{pool_name}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPoolTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_save_image_job_async(self, request):
        r"""查询训练作业镜像保存任务

        查询训练作业镜像保存任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSaveImageJob
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowSaveImageJobRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowSaveImageJobResponse`
        """
        http_info = self._show_save_image_job_http_info(request)
        return self._call_api(**http_info)

    def show_save_image_job_async_invoker(self, request):
        http_info = self._show_save_image_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_save_image_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/training-jobs/{training_job_id}/tasks/{task_id}/save-image-job",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSaveImageJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'training_job_id' in local_var_params:
            path_params['training_job_id'] = local_var_params['training_job_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_search_algorithms_async(self, request):
        r"""获取支持的超参搜索算法

        获取支持的超参搜索算法。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSearchAlgorithms
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowSearchAlgorithmsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowSearchAlgorithmsResponse`
        """
        http_info = self._show_search_algorithms_http_info(request)
        return self._call_api(**http_info)

    def show_search_algorithms_async_invoker(self, request):
        http_info = self._show_search_algorithms_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_search_algorithms_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/search-algorithms",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSearchAlgorithmsResponse"
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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_train_job_tags_async(self, request):
        r"""查询训练作业标签

        查询训练作业标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTrainJobTags
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowTrainJobTagsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowTrainJobTagsResponse`
        """
        http_info = self._show_train_job_tags_http_info(request)
        return self._call_api(**http_info)

    def show_train_job_tags_async_invoker(self, request):
        http_info = self._show_train_job_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_train_job_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/modelarts-training-job/{training_job_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTrainJobTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'training_job_id' in local_var_params:
            path_params['training_job_id'] = local_var_params['training_job_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_training_experiment_details_async(self, request):
        r"""查询训练实验详情

        查询训练实验详情接口用于获取指定训练实验的详细信息。
        该接口适用于以下场景：当用户需要查看训练实验的实验名称、描述、创建时间等详细信息时，可以通过此接口获取。使用该接口的前提条件是训练实验已存在且用户具有查看该实验的权限。查询操作完成后，将返回训练实验的详细信息，包括但不限于实验ID、名称、描述、创建时间等。若训练实验不存在或用户无权限操作，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTrainingExperimentDetails
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowTrainingExperimentDetailsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowTrainingExperimentDetailsResponse`
        """
        http_info = self._show_training_experiment_details_http_info(request)
        return self._call_api(**http_info)

    def show_training_experiment_details_async_invoker(self, request):
        http_info = self._show_training_experiment_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_training_experiment_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/training-experiments/{experiment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTrainingExperimentDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'experiment_id' in local_var_params:
            path_params['experiment_id'] = local_var_params['experiment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_training_job_details_async(self, request):
        r"""查询训练作业详情

        查询训练作业详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTrainingJobDetails
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowTrainingJobDetailsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowTrainingJobDetailsResponse`
        """
        http_info = self._show_training_job_details_http_info(request)
        return self._call_api(**http_info)

    def show_training_job_details_async_invoker(self, request):
        http_info = self._show_training_job_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_training_job_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/training-jobs/{training_job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTrainingJobDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'training_job_id' in local_var_params:
            path_params['training_job_id'] = local_var_params['training_job_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_training_job_engines_async(self, request):
        r"""获取训练作业支持的AI预置框架

        获取训练作业支持的AI预置框架。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTrainingJobEngines
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowTrainingJobEnginesRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowTrainingJobEnginesResponse`
        """
        http_info = self._show_training_job_engines_http_info(request)
        return self._call_api(**http_info)

    def show_training_job_engines_async_invoker(self, request):
        http_info = self._show_training_job_engines_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_training_job_engines_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/training-job-engines",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTrainingJobEnginesResponse"
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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_training_job_flavors_async(self, request):
        r"""获取训练作业支持的公共规格

        获取训练作业支持的公共规格。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTrainingJobFlavors
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowTrainingJobFlavorsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowTrainingJobFlavorsResponse`
        """
        http_info = self._show_training_job_flavors_http_info(request)
        return self._call_api(**http_info)

    def show_training_job_flavors_async_invoker(self, request):
        http_info = self._show_training_job_flavors_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_training_job_flavors_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/training-job-flavors",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTrainingJobFlavorsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'flavor_type' in local_var_params:
            query_params.append(('flavor_type', local_var_params['flavor_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_training_job_logs_preview_async(self, request):
        r"""查询训练作业指定任务的日志（预览）

        查询训练作业指定任务的日志（预览）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTrainingJobLogsPreview
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowTrainingJobLogsPreviewRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowTrainingJobLogsPreviewResponse`
        """
        http_info = self._show_training_job_logs_preview_http_info(request)
        return self._call_api(**http_info)

    def show_training_job_logs_preview_async_invoker(self, request):
        http_info = self._show_training_job_logs_preview_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_training_job_logs_preview_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/training-jobs/{training_job_id}/tasks/{task_id}/logs/preview",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTrainingJobLogsPreviewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'training_job_id' in local_var_params:
            path_params['training_job_id'] = local_var_params['training_job_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_training_job_metrics_async(self, request):
        r"""查询训练作业指定任务的运行指标

        查询训练作业指定任务的运行指标。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTrainingJobMetrics
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowTrainingJobMetricsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowTrainingJobMetricsResponse`
        """
        http_info = self._show_training_job_metrics_http_info(request)
        return self._call_api(**http_info)

    def show_training_job_metrics_async_invoker(self, request):
        http_info = self._show_training_job_metrics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_training_job_metrics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/training-jobs/{training_job_id}/metrics/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTrainingJobMetricsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'training_job_id' in local_var_params:
            path_params['training_job_id'] = local_var_params['training_job_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_training_quotas_async(self, request):
        r"""获取训练配额

        获取训练配额接口用于查询用户在ModelArts服务中的训练资源配额信息。
        该接口适用于以下场景：当用户需要了解当前可用的训练资源配额，以便合理规划和管理训练任务时，可以通过此接口获取配额详情。使用该接口的前提条件是用户已登录并具有查看配额的权限。响应消息体中包含用户已创建的训练作业个数、剩余可创建个数等。若用户无权限或配额信息为空，接口将返回相应的错误信息或空列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTrainingQuotas
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowTrainingQuotasRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowTrainingQuotasResponse`
        """
        http_info = self._show_training_quotas_http_info(request)
        return self._call_api(**http_info)

    def show_training_quotas_async_invoker(self, request):
        http_info = self._show_training_quotas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_training_quotas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/training-quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTrainingQuotasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in local_var_params:
            query_params.append(('user_id', local_var_params['user_id']))
        if 'resource' in local_var_params:
            query_params.append(('resource', local_var_params['resource']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_workload_statistics_async(self, request):
        r"""查询专属资源池作业统计信息

        查询专属资源池作业统计信息接口用于获取指定专属资源池中作业的统计信息。该接口适用于以下场景：当需要了解专属资源池中作业的整体运行情况、资源使用效率或作业状态分布时，用户可通过此接口获取统计信息。使用该接口的前提条件是专属资源池已存在且用户具有相应的权限（如管理员权限或资源管理权限）。调用接口成功后，系统将返回专属资源池中作业的统计信息，包括作业总数、运行中作业数、完成作业数、资源使用率等数据。若专属资源池不存在、用户无权限操作或资源池当前不可用，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWorkloadStatistics
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowWorkloadStatisticsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowWorkloadStatisticsResponse`
        """
        http_info = self._show_workload_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_workload_statistics_async_invoker(self, request):
        http_info = self._show_workload_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_workload_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/statistics/pools/{pool_name}/workloads",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWorkloadStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_name' in local_var_params:
            path_params['pool_name'] = local_var_params['pool_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_workspace_async(self, request):
        r"""查询工作空间详情

        查询工作空间详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWorkspace
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowWorkspaceRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowWorkspaceResponse`
        """
        http_info = self._show_workspace_http_info(request)
        return self._call_api(**http_info)

    def show_workspace_async_invoker(self, request):
        http_info = self._show_workspace_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_workspace_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWorkspaceResponse"
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

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_workspace_quotas_async(self, request):
        r"""查询工作空间配额

        查询工作空间配额。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWorkspaceQuotas
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowWorkspaceQuotasRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowWorkspaceQuotasResponse`
        """
        http_info = self._show_workspace_quotas_http_info(request)
        return self._call_api(**http_info)

    def show_workspace_quotas_async_invoker(self, request):
        http_info = self._show_workspace_quotas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_workspace_quotas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWorkspaceQuotasResponse"
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

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def start_infer_deployment_async(self, request):
        r"""启动服务部署

        使部署从“停止”或“失败”状态进入“部署中”状态，适用于用户需要重新启动已停止或启动失败的部署的情况。调用此接口前，部署状态必须为“停止”或“失败”，且用户需具有启动部署的权限。调用成功后，部署状态将变为“部署中”，系统将开始执行部署流程，包括资源准备、配置加载等。如果部署当前状态不是“停止”或“失败”，或用户没有启动部署的权限，调用将返回错误。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartInferDeployment
        :type request: :class:`huaweicloudsdkmodelarts.v1.StartInferDeploymentRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.StartInferDeploymentResponse`
        """
        http_info = self._start_infer_deployment_http_info(request)
        return self._call_api(**http_info)

    def start_infer_deployment_async_invoker(self, request):
        http_info = self._start_infer_deployment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_infer_deployment_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/services/{service_id}/deployments/{deployment_id}/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartInferDeploymentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def start_infer_service_async(self, request):
        r"""启动服务

        使服务从\&quot;停止\&quot;或\&quot;失败\&quot;状态进入\&quot;部署中\&quot;状态，适用于用户需要重新启动已停止或启动失败的服务的情况。调用此接口前，服务状态必须为\&quot;停止\&quot;或\&quot;失败\&quot;，且用户需具有启动服务的权限。调用成功后，服务状态将变为\&quot;部署中\&quot;，系统将开始执行部署流程，包括资源准备、配置加载等。如果服务当前状态不是\&quot;停止\&quot;或\&quot;失败\&quot;，或用户没有启动服务的权限，调用将返回错误。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartInferService
        :type request: :class:`huaweicloudsdkmodelarts.v1.StartInferServiceRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.StartInferServiceResponse`
        """
        http_info = self._start_infer_service_http_info(request)
        return self._call_api(**http_info)

    def start_infer_service_async_invoker(self, request):
        http_info = self._start_infer_service_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_infer_service_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/services/{service_id}/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartInferServiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def stop_infer_deployment_async(self, request):
        r"""停止在线服务部署

        停止在线部署功能允许用户在特定状态下主动终止正在运行或处于其他可操作状态的部署实例。该功能适用于需要维护、升级或检测到异常的服务场景，支持在服务处于\&quot;运行中\&quot;、\&quot;部署中\&quot;、\&quot;失败\&quot;或\&quot;告警\&quot;状态时执行停止操作。使用此功能前，请确保部署实例处于可停止状态，并具备相应的API调用权限。成功执行后，部署将进入停止状态，释放相关资源并停止处理新的请求。若部署不在允许停止的状态、调用权限不足或系统内部出现错误，将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopInferDeployment
        :type request: :class:`huaweicloudsdkmodelarts.v1.StopInferDeploymentRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.StopInferDeploymentResponse`
        """
        http_info = self._stop_infer_deployment_http_info(request)
        return self._call_api(**http_info)

    def stop_infer_deployment_async_invoker(self, request):
        http_info = self._stop_infer_deployment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_infer_deployment_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/services/{service_id}/deployments/{deployment_id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopInferDeploymentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def stop_infer_service_async(self, request):
        r"""停止服务

        使服务从\&quot;运行中\&quot;状态进入\&quot;停止中\&quot;最终变为\&quot;停止\&quot;状态，适用于用户需要停止正在运行的服务以节省资源成本的场景。用户需具有停止服务的权限。调用成功后，服务状态将变为\&quot;停止中\&quot;，系统将开始执行停止流程，包括释放资源、保存状态等。如果用户没有停止服务的权限，调用将返回错误。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopInferService
        :type request: :class:`huaweicloudsdkmodelarts.v1.StopInferServiceRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.StopInferServiceResponse`
        """
        http_info = self._stop_infer_service_http_info(request)
        return self._call_api(**http_info)

    def stop_infer_service_async_invoker(self, request):
        http_info = self._stop_infer_service_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_infer_service_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/services/{service_id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopInferServiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def stop_training_job_async(self, request):
        r"""终止训练作业

        终止训练作业，只可终止创建中、等待中、运行中的作业。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopTrainingJob
        :type request: :class:`huaweicloudsdkmodelarts.v1.StopTrainingJobRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.StopTrainingJobResponse`
        """
        http_info = self._stop_training_job_http_info(request)
        return self._call_api(**http_info)

    def stop_training_job_async_invoker(self, request):
        http_info = self._stop_training_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_training_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/training-jobs/{training_job_id}/actions",
            "request_type": request.__class__.__name__,
            "response_type": "StopTrainingJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'training_job_id' in local_var_params:
            path_params['training_job_id'] = local_var_params['training_job_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def switch_infer_deployment_version_async(self, request):
        r"""切换部署到指定版本

        此接口用于将部署切换到指定版本，适用于需要在不同版本间进行切换以测试或回滚的场景。请求需包含有效的服务ID、部署ID及目标版本号，版本号必须是已发布的有效版本。用户必须具有对目标服务部署的管理权限，并且部署处于运行状态。切换成功后，部署将立即使用新的版本。若服务ID无效、部署ID无效、版本号不存在或用户无权限，则返回400 Bad Request或403 Forbidden；若部署状态不允许切换，则返回400 Bad Request。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SwitchInferDeploymentVersion
        :type request: :class:`huaweicloudsdkmodelarts.v1.SwitchInferDeploymentVersionRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.SwitchInferDeploymentVersionResponse`
        """
        http_info = self._switch_infer_deployment_version_http_info(request)
        return self._call_api(**http_info)

    def switch_infer_deployment_version_async_invoker(self, request):
        http_info = self._switch_infer_deployment_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _switch_infer_deployment_version_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/services/{service_id}/deployments/{deployment_id}/versions/{version}/switch",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchInferDeploymentVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def sync_image_async(self, request):
        r"""同步镜像状态

        同步镜像状态接口用于修正镜像状态的异常情况。该接口适用于以下场景：当镜像状态因误操作、网络问题或系统故障等原因出现异常时，用户可通过此接口同步镜像的最新状态。使用该接口的前提条件是镜像已存在且用户具有相应的操作权限。同步操作完成后，镜像的状态将被更新为最新的正确状态，相关资源和配置也将被同步。若镜像不存在、用户无权限操作或同步过程中出现错误，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SyncImage
        :type request: :class:`huaweicloudsdkmodelarts.v1.SyncImageRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.SyncImageResponse`
        """
        http_info = self._sync_image_http_info(request)
        return self._call_api(**http_info)

    def sync_image_async_invoker(self, request):
        http_info = self._sync_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _sync_image_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/images/{image_id}/sync",
            "request_type": request.__class__.__name__,
            "response_type": "SyncImageResponse"
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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def unbind_infer_api_key_async(self, request):
        r"""解绑应用密钥

        本接口用于将已绑定的apikey从指定服务中解绑，适用于需要撤销某个apikey对特定服务的访问权限的场景。调用此接口前，确保已获取到需要解绑的apikey，并确认该apikey当前绑定在指定服务上。解绑成功后，该apikey将不再对指定服务生效，但仍可继续用于其他服务。如果尝试解绑不存在或未绑定到指定服务的apikey，将返回相应的异常信息，提示用户检查apikey的有效性和绑定状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UnbindInferApiKey
        :type request: :class:`huaweicloudsdkmodelarts.v1.UnbindInferApiKeyRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.UnbindInferApiKeyResponse`
        """
        http_info = self._unbind_infer_api_key_http_info(request)
        return self._call_api(**http_info)

    def unbind_infer_api_key_async_invoker(self, request):
        http_info = self._unbind_infer_api_key_http_info(request)
        return AsyncInvoker(self, http_info)

    def _unbind_infer_api_key_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/services/{service_id}/api-keys/{key_id}/unbind",
            "request_type": request.__class__.__name__,
            "response_type": "UnbindInferApiKeyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'key_id' in local_var_params:
            path_params['key_id'] = local_var_params['key_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_auth_mode_async(self, request):
        r"""更新授权模式

        更新授权模式接口用于修改指定资源或功能的授权方式和权限配置信息。该接口适用于以下场景：当系统管理员需要调整资源的访问权限、开发者需要更新授权策略以适应新的业务需求，或安全审计人员需要修改授权配置以符合新的安全规范时，可通过此接口更新授权模式的详细信息。使用该接口的前提条件是用户具有更新权限且目标资源或功能的授权模式已存在。调用成功后，接口将更新目标资源的授权模式，并返回更新后的授权模式信息。若用户无权限访问该接口，或目标资源的授权模式不存在，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAuthMode
        :type request: :class:`huaweicloudsdkmodelarts.v1.UpdateAuthModeRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.UpdateAuthModeResponse`
        """
        http_info = self._update_auth_mode_http_info(request)
        return self._call_api(**http_info)

    def update_auth_mode_async_invoker(self, request):
        http_info = self._update_auth_mode_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_auth_mode_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/auth-mode",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAuthModeResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_image_group_async(self, request):
        r"""更新镜像组

        更新镜像组接口用于更新镜像组的标签及说明信息。该接口适用于以下场景：当镜像说明需要修改，或者镜像的标签需要修改时，用户可通过此接口修改。使用该接口的前提条件是镜像组已存在且用户具有更新权限。更新操作完成后，镜像组对应的配置文件会。若镜像组不存在、用户无权限操作或镜像正在被使用，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateImageGroup
        :type request: :class:`huaweicloudsdkmodelarts.v1.UpdateImageGroupRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.UpdateImageGroupResponse`
        """
        http_info = self._update_image_group_http_info(request)
        return self._call_api(**http_info)

    def update_image_group_async_invoker(self, request):
        http_info = self._update_image_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_image_group_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/images/group/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateImageGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_infer_deployment_async(self, request):
        r"""更新服务部署配置

        该接口适用于需要动态调整模型服务部署配置的场景
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInferDeployment
        :type request: :class:`huaweicloudsdkmodelarts.v1.UpdateInferDeploymentRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.UpdateInferDeploymentResponse`
        """
        http_info = self._update_infer_deployment_http_info(request)
        return self._call_api(**http_info)

    def update_infer_deployment_async_invoker(self, request):
        http_info = self._update_infer_deployment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_infer_deployment_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/services/{service_id}/deployments/{deployment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInferDeploymentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_infer_deployment_scale_async(self, request):
        r"""手动服务扩缩容

        该接口适用于模型服务实例扩缩容。通过调用此接口，用户可以在原有服务的情况下，对服务进行扩缩容，且不会增加新的版本；包括权限验证错误、服务状态错误和参数验证错误。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInferDeploymentScale
        :type request: :class:`huaweicloudsdkmodelarts.v1.UpdateInferDeploymentScaleRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.UpdateInferDeploymentScaleResponse`
        """
        http_info = self._update_infer_deployment_scale_http_info(request)
        return self._call_api(**http_info)

    def update_infer_deployment_scale_async_invoker(self, request):
        http_info = self._update_infer_deployment_scale_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_infer_deployment_scale_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/services/{service_id}/deployments/{deployment_name}/scale",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInferDeploymentScaleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'deployment_name' in local_var_params:
            path_params['deployment_name'] = local_var_params['deployment_name']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_infer_intranet_connection_async(self, request):
        r"""变更内网申请

        本接口用于对当前租户的内网接入申请进行状态变更操作，支持通过（APPROVE）、拒绝（REJECT）、取消（CANCEL）和重试（RETRY）等操作。适用于需要管理内网接入申请审批流程的场景。调用此接口前，确保已具备相应的变更权限，并提供有效的内网申请ID和所需的操作类型。变更成功后，内网申请的状态将更新为指定的操作结果，并记录相关日志。如果提供的内网申请ID无效、操作类型不支持或权限不足，将返回相应的异常信息，提示用户检查输入数据的有效性和权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInferIntranetConnection
        :type request: :class:`huaweicloudsdkmodelarts.v1.UpdateInferIntranetConnectionRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.UpdateInferIntranetConnectionResponse`
        """
        http_info = self._update_infer_intranet_connection_http_info(request)
        return self._call_api(**http_info)

    def update_infer_intranet_connection_async_invoker(self, request):
        http_info = self._update_infer_intranet_connection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_infer_intranet_connection_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/intranet-connection/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInferIntranetConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_infer_service_async(self, request):
        r"""更新服务配置

        该接口适用于需要动态调整模型服务配置的场景，对模型的性能参数、资源池配置、服务调用配置等进行更新升级。通过调用此接口，用户可以在原有服务的情况下，升级成一个新的服务版本。调用此接口前，服务状态必须为“停止”、“失败”或“运行中”，且用户需具有修改服务的权限。更新成功后，新配置立即生效；若失败，服务保持原有配置并返回错误信息。常见异常包括参数验证错误、权限验证错误和服务状态错误。若服务ID无效、版本号不存在或用户无权限，则返回400 Bad Request或403 Forbidden；若服务状态不允许切换，则返回400 Bad Request。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInferService
        :type request: :class:`huaweicloudsdkmodelarts.v1.UpdateInferServiceRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.UpdateInferServiceResponse`
        """
        http_info = self._update_infer_service_http_info(request)
        return self._call_api(**http_info)

    def update_infer_service_async_invoker(self, request):
        http_info = self._update_infer_service_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_infer_service_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/services/{service_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInferServiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_workspace_async(self, request):
        r"""修改工作空间

        修改工作空间。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateWorkspace
        :type request: :class:`huaweicloudsdkmodelarts.v1.UpdateWorkspaceRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.UpdateWorkspaceResponse`
        """
        http_info = self._update_workspace_http_info(request)
        return self._call_api(**http_info)

    def update_workspace_async_invoker(self, request):
        http_info = self._update_workspace_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_workspace_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateWorkspaceResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_workspace_quotas_async(self, request):
        r"""修改工作空间配额

        修改工作空间配额。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateWorkspaceQuotas
        :type request: :class:`huaweicloudsdkmodelarts.v1.UpdateWorkspaceQuotasRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.UpdateWorkspaceQuotasResponse`
        """
        http_info = self._update_workspace_quotas_http_info(request)
        return self._call_api(**http_info)

    def update_workspace_quotas_async_invoker(self, request):
        http_info = self._update_workspace_quotas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_workspace_quotas_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateWorkspaceQuotasResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def validate_authorization_async(self, request):
        r"""鉴权能否使用当前工作空间资源

        鉴权能否使用当前工作空间资源接口用于验证用户是否有权限访问和使用当前工作空间中的资源。该接口适用于以下场景：当用户尝试访问或操作工作空间中的资源时，系统需要确认用户是否具有相应的权限。使用该接口的前提条件是用户已登录且工作空间已存在。鉴权成功后，用户可以正常访问和使用工作空间资源；若鉴权失败，接口将返回相应的错误信息，如用户无权限或工作空间不存在等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ValidateAuthorization
        :type request: :class:`huaweicloudsdkmodelarts.v1.ValidateAuthorizationRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ValidateAuthorizationResponse`
        """
        http_info = self._validate_authorization_http_info(request)
        return self._call_api(**http_info)

    def validate_authorization_async_invoker(self, request):
        http_info = self._validate_authorization_http_info(request)
        return AsyncInvoker(self, http_info)

    def _validate_authorization_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/auth",
            "request_type": request.__class__.__name__,
            "response_type": "ValidateAuthorizationResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_infer_deployment_hpa_async(self, request):
        r"""创建自动扩缩容策略

        本接口用于在已部署的服务上创建定时扩缩容策略，适用于需要根据业务负载或特定时间自动调整服务实例个数的场景。调用此接口前，确保服务已成功部署并获取了有效的服务ID，并提供详细的扩缩容策略参数，如扩缩容时间、实例个数范围、条件触发器等。创建成功后，系统将根据设定的策略自动调整服务实例个数，确保服务在指定时间内的性能和可用性。如果提供的服务ID无效、参数配置错误或系统资源不足，将返回相应的异常信息，提示用户检查输入数据的有效性或联系技术支持。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInferDeploymentHpa
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateInferDeploymentHpaRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateInferDeploymentHpaResponse`
        """
        http_info = self._create_infer_deployment_hpa_http_info(request)
        return self._call_api(**http_info)

    def create_infer_deployment_hpa_async_invoker(self, request):
        http_info = self._create_infer_deployment_hpa_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_infer_deployment_hpa_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/services/{service_id}/deployments/{deployment_id}/hpa",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInferDeploymentHpaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_infer_deployment_hpa_async(self, request):
        r"""删除自动扩缩容策略

        本接口用于在已部署的服务上删除定时扩缩容策略，适用于需要根据业务负载或特定时间自动删除服务的场景。调用此接口前，确保服务已成功部署并获取了有效的服务ID，部署ID。如果提供的服务ID无效、参数配置错误或系统资源不足，将返回相应的异常信息，提示用户检查输入数据的有效性或联系技术支持。暂时为非开放接口，后端清理服务下的自动扩缩容策略规则使用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteInferDeploymentHpa
        :type request: :class:`huaweicloudsdkmodelarts.v1.DeleteInferDeploymentHpaRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeleteInferDeploymentHpaResponse`
        """
        http_info = self._delete_infer_deployment_hpa_http_info(request)
        return self._call_api(**http_info)

    def delete_infer_deployment_hpa_async_invoker(self, request):
        http_info = self._delete_infer_deployment_hpa_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_infer_deployment_hpa_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/services/{service_id}/deployments/{deployment_id}/hpa",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInferDeploymentHpaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_infer_deployment_hpa_events_async(self, request):
        r"""查看自动扩缩容策略事件

        本接口用于在已部署的服务上查看自动扩缩容策略事件，适用于查看自动扩缩容策略变动历史记录。调用此接口前，确保获取了有效的用户项目ID，服务ID，部署ID。调用成功后，会返回策略事件ID，事件状态，规则执行信息，扩缩容前实例数，扩缩容后实例数，预设目标实例数，执行记录时间。如果提供的服务ID无效、参数配置错误或系统资源不足，将返回相应的异常信息，提示用户检查输入数据的有效性或联系技术支持。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInferDeploymentHpaEvents
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListInferDeploymentHpaEventsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListInferDeploymentHpaEventsResponse`
        """
        http_info = self._list_infer_deployment_hpa_events_http_info(request)
        return self._call_api(**http_info)

    def list_infer_deployment_hpa_events_async_invoker(self, request):
        http_info = self._list_infer_deployment_hpa_events_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_infer_deployment_hpa_events_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/services/{service_id}/deployments/{deployment_id}/hpa/events",
            "request_type": request.__class__.__name__,
            "response_type": "ListInferDeploymentHpaEventsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_infer_deployment_hpa_async(self, request):
        r"""查看自动扩缩容策略

        本接口用于在已部署的服务上查看自动扩缩容策略。调用此接口前，确保服务已成功部署并获取了有效的服务ID。查询成功后，返回服务对应的策略信息，如规则ID，规则名称，扩缩容类型，扩缩容状态，扩缩容cron表达式，目标实例数等。如果提供的服务ID无效、参数配置错误或系统资源不足，将返回相应的异常信息，提示用户检查输入数据的有效性或联系技术支持。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInferDeploymentHpa
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowInferDeploymentHpaRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowInferDeploymentHpaResponse`
        """
        http_info = self._show_infer_deployment_hpa_http_info(request)
        return self._call_api(**http_info)

    def show_infer_deployment_hpa_async_invoker(self, request):
        http_info = self._show_infer_deployment_hpa_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_infer_deployment_hpa_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/services/{service_id}/deployments/{deployment_id}/hpa",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInferDeploymentHpaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_infer_deployment_hpa_async(self, request):
        r"""修改自动扩缩容策略

        本接口用于在已部署的服务上修改定时扩缩容策略，适用于需要根据业务负载或特定时间自动调整服务实例个数的场景。调用此接口前，确保服务已成功部署并获取了有效的服务ID，部署ID，并提供详细的扩缩容策略参数，如扩缩容时间、实例个数范围、条件触发器等。修改成功后，系统将根据设定的策略自动调整服务实例个数，确保服务在指定时间内的性能和可用性。如果提供的服务ID无效、参数配置错误或系统资源不足，将返回相应的异常信息，提示用户检查输入数据的有效性或联系技术支持。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInferDeploymentHpa
        :type request: :class:`huaweicloudsdkmodelarts.v1.UpdateInferDeploymentHpaRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.UpdateInferDeploymentHpaResponse`
        """
        http_info = self._update_infer_deployment_hpa_http_info(request)
        return self._call_api(**http_info)

    def update_infer_deployment_hpa_async_invoker(self, request):
        http_info = self._update_infer_deployment_hpa_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_infer_deployment_hpa_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/services/{service_id}/deployments/{deployment_id}/hpa",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInferDeploymentHpaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_infer_hra_async(self, request):
        r"""创建HRA策略

        本接口用于在已部署且支持HRA策略的服务上创建HRA策略，适用于需要根据业务负载或特定时间自动调整服务实例个数的场景。调用此接口前，确保服务已成功部署并获取了有效的服务ID，并提供详细的hra策略参数，如hra时间、实例个数范围、条件触发器等。创建成功后，系统将根据设定的策略自动调整服务实例个数，确保服务在指定时间内的性能和可用性。如果提供的服务ID无效、参数配置错误或系统资源不足，将返回相应的异常信息，提示用户检查输入数据的有效性或联系技术支持。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInferHra
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateInferHraRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateInferHraResponse`
        """
        http_info = self._create_infer_hra_http_info(request)
        return self._call_api(**http_info)

    def create_infer_hra_async_invoker(self, request):
        http_info = self._create_infer_hra_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_infer_hra_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/services/{service_id}/deployments/{deployment_id}/hra",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInferHraResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_infer_hra_async(self, request):
        r"""获取推理单元配比检测信息

        本接口用于在已部署的服务上查看推理单元配比检测信息。调用此接口前，确保服务已成功部署并获取了有效的服务ID。查询成功后，返回服务对应的策略信息，如规则ID，规则名称，策略状态，HRA结果状态等。如果提供的服务ID无效、参数配置错误或系统资源不足，将返回相应的异常信息，提示用户检查输入数据的有效性或联系技术支持。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInferHra
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowInferHraRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowInferHraResponse`
        """
        http_info = self._show_infer_hra_http_info(request)
        return self._call_api(**http_info)

    def show_infer_hra_async_invoker(self, request):
        http_info = self._show_infer_hra_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_infer_hra_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/services/{service_id}/deployments/{deployment_id}/hra",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInferHraResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_infer_hra_async(self, request):
        r"""修改指定部署的HRA策略配置

        本接口用于在已创建HRA策略的服务上修改指定部署的HRA策略配置，适用于需要根据业务负载或特定时间自动调整服务实例个数的场景。调用此接口前，确保服务已成功部署并获取了有效的服务ID，部署ID，并提供详细的hra策略参数，如HRA规则列表、HRA结果状态、策略状态等。修改成功后，系统将根据设定的策略自动调整服务实例个数，确保服务在指定时间内的性能和可用性。如果提供的服务ID无效、参数配置错误或系统资源不足，将返回相应的异常信息，提示用户检查输入数据的有效性或联系技术支持。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInferHra
        :type request: :class:`huaweicloudsdkmodelarts.v1.UpdateInferHraRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.UpdateInferHraResponse`
        """
        http_info = self._update_infer_hra_http_info(request)
        return self._call_api(**http_info)

    def update_infer_hra_async_invoker(self, request):
        http_info = self._update_infer_hra_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_infer_hra_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/services/{service_id}/deployments/{deployment_id}/hra",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInferHraResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def attach_dev_server_volume_async(self, request):
        r"""Lite Server服务器挂载磁盘

        Lite Server服务器挂载磁盘接口用于将额外的磁盘挂载到Lite Server服务器上。该接口适用于以下场景：当用户需要扩展Lite Server服务器的存储空间以满足更大的数据存储需求时，可以通过此接口将指定的磁盘挂载到服务器上。使用该接口的前提条件是Lite Server服务器已创建且处于运行状态、或者停止状态，用户具有挂载磁盘的权限，且指定的磁盘已存在且未被其他服务器使用。挂载操作完成后，磁盘将成功挂载到Lite Server服务器上，用户可以访问和使用新增的存储空间。若Lite Server服务器不存在、指定的磁盘不存在或已被使用，或用户无权限操作，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AttachDevServerVolume
        :type request: :class:`huaweicloudsdkmodelarts.v1.AttachDevServerVolumeRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.AttachDevServerVolumeResponse`
        """
        http_info = self._attach_dev_server_volume_http_info(request)
        return self._call_api(**http_info)

    def attach_dev_server_volume_async_invoker(self, request):
        http_info = self._attach_dev_server_volume_http_info(request)
        return AsyncInvoker(self, http_info)

    def _attach_dev_server_volume_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dev-servers/{id}/attachvolume",
            "request_type": request.__class__.__name__,
            "response_type": "AttachDevServerVolumeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_dev_servers_action_async(self, request):
        r"""批量操作Lite Server实例

        批量操作Lite Server实例接口用于对多个Lite Server实例进行统一操作，如启动、停止、重启或删除等。该接口适用于以下场景：当需要对多个Lite Server实例进行相同的操作，例如在维护期间批量停止实例、更新配置后批量重启实例或清理不再需要的实例时，用户可通过此接口高效地完成批量操作。使用该接口的前提条件是目标Lite Server实例已存在且用户具有相应的操作权限。操作完成后，所有指定的Lite Server实例将根据请求完成相应的状态变更或被移除，相关资源和配置也将被相应调整或清理。若目标Lite Server实例不存在、用户无权限操作或请求参数不正确，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDevServersAction
        :type request: :class:`huaweicloudsdkmodelarts.v1.BatchDevServersActionRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.BatchDevServersActionResponse`
        """
        http_info = self._batch_dev_servers_action_http_info(request)
        return self._call_api(**http_info)

    def batch_dev_servers_action_async_invoker(self, request):
        http_info = self._batch_dev_servers_action_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_dev_servers_action_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dev-servers/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDevServersActionResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def bind_dev_server_public_ip_async(self, request):
        r"""Lite Server服务器绑定EIP

        Lite Server服务器绑定的EIP接口用于将弹性公网IP（EIP）绑定到Lite Server服务器上。该接口适用于以下场景：当用户需要为Lite Server服务器分配一个固定的公网IP地址，以便从外部网络访问服务器时，可以通过此接口将指定的EIP绑定到服务器上。使用该接口的前提条件是Lite Server服务器已创建且处于运行状态，用户具有绑定EIP的权限，且指定的EIP已存在且未被其他资源使用。绑定操作完成后，EIP将成功绑定到Lite Server服务器上，服务器可以通过该EIP从外部网络访问。若Lite Server服务器不存在、已处于停止状态、指定的EIP不存在或已被使用，或用户无权限操作，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BindDevServerPublicIP
        :type request: :class:`huaweicloudsdkmodelarts.v1.BindDevServerPublicIPRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.BindDevServerPublicIPResponse`
        """
        http_info = self._bind_dev_server_public_ip_http_info(request)
        return self._call_api(**http_info)

    def bind_dev_server_public_ip_async_invoker(self, request):
        http_info = self._bind_dev_server_public_ip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _bind_dev_server_public_ip_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dev-servers/{id}/publicips",
            "request_type": request.__class__.__name__,
            "response_type": "BindDevServerPublicIPResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def change_dev_server_os_async(self, request):
        r"""切换Lite Server服务器操作系统镜像

        切换Lite Server服务器操作系统镜像接口用于更换Lite Server服务器当前使用的操作系统镜像。该接口适用于以下场景：当用户需要更换操作系统以适应不同的开发或测试需求时，可以通过此接口切换指定的Lite Server服务器操作系统镜像。使用该接口的前提条件是Lite Server服务器已存在且处于停止状态，用户具有切换操作系统的权限。切换操作完成后，Lite Server服务器将安装新的操作系统镜像，并重新进入运行状态，若Lite Server服务器不存在、已处于运行状态或用户无权限操作，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeDevServerOS
        :type request: :class:`huaweicloudsdkmodelarts.v1.ChangeDevServerOSRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ChangeDevServerOSResponse`
        """
        http_info = self._change_dev_server_os_http_info(request)
        return self._call_api(**http_info)

    def change_dev_server_os_async_invoker(self, request):
        http_info = self._change_dev_server_os_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_dev_server_os_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dev-servers/{id}/changeos",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeDevServerOSResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def change_hyperinstance_os_async(self, request):
        r"""切换Lite Server超节点服务器操作系统镜像

        切换Lite Server超节点服务器操作系统镜像接口用于更换Lite Server超节点服务器当前使用的操作系统镜像。该接口适用于以下场景：当用户需要更换操作系统以适应不同的开发或测试需求时，可以通过此接口切换指定的Lite Server超节点服务器操作系统镜像。使用该接口的前提条件是Lite Server超节点服务器已存在且处于停止状态，用户具有切换操作系统的权限。切换操作完成后，Lite Server超节点服务器将安装新的操作系统镜像，并重新进入运行状态，若Lite Server超节点服务器不存在、已处于运行状态或用户无权限操作，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeHyperinstanceOS
        :type request: :class:`huaweicloudsdkmodelarts.v1.ChangeHyperinstanceOSRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ChangeHyperinstanceOSResponse`
        """
        http_info = self._change_hyperinstance_os_http_info(request)
        return self._call_api(**http_info)

    def change_hyperinstance_os_async_invoker(self, request):
        http_info = self._change_hyperinstance_os_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_hyperinstance_os_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dev-servers/hyperinstance/{id}/changeos",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeHyperinstanceOSResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_dev_server_async(self, request):
        r"""创建Lite Server

        创建Lite Server接口用于创建LiteServer弹性云服务器、裸金属服务器及超节点服务器。该接口适用于以下场景：用户需要根据业务需求快速部署和配置不同类型的服务器资源。使用该接口的前提条件是用户已登录且具有创建Lite Server的权限，并且需要提供服务器类型、规格、网络配置等必要参数。创建操作完成后，系统将返回新创建的Lite Server实例信息，包括实例ID、状态等。若用户无权限、参数配置错误或资源不足，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDevServer
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateDevServerRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateDevServerResponse`
        """
        http_info = self._create_dev_server_http_info(request)
        return self._call_api(**http_info)

    def create_dev_server_async_invoker(self, request):
        http_info = self._create_dev_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_dev_server_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dev-servers",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDevServerResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_dev_server_job_async(self, request):
        r"""创建Lite Server任务

        创建Lite Server任务接口用于在Lite Server上创建新的任务。该接口适用于以下场景：当用户需要在Lite Server上启动新的开发、测试或部署任务时，可以通过此接口创建并配置任务。使用该接口的前提条件是用户具有创建任务的权限，并且提供的任务配置参数符合要求。创建操作完成后，新的Lite Server任务将被成功创建，并返回任务ID和其他相关信息。若用户无权限操作、提供的参数不正确或系统资源不足，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDevServerJob
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateDevServerJobRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateDevServerJobResponse`
        """
        http_info = self._create_dev_server_job_http_info(request)
        return self._call_api(**http_info)

    def create_dev_server_job_async_invoker(self, request):
        http_info = self._create_dev_server_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_dev_server_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dev-servers/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDevServerJobResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_hyper_cluster_async(self, request):
        r"""创建Hyper Cluster

        创建Hyper Cluster接口用于在系统中创建一个新的Hyper Cluster。该接口适用于以下场景：当用户需要使用超节点网络时，可以通过此接口创建Hyper Cluster。使用该接口的前提条件是用户已登录并具有创建Hyper Cluster的权限，且系统中已配置了必要的资源。创建操作完成后，将生成一个新的超节点网络，并返回超节点网络的详细信息，包括ID、名称、子网信息等。若用户无权限操作、系统中缺少必要的资源或配置参数无效，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateHyperCluster
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateHyperClusterRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateHyperClusterResponse`
        """
        http_info = self._create_hyper_cluster_http_info(request)
        return self._call_api(**http_info)

    def create_hyper_cluster_async_invoker(self, request):
        http_info = self._create_hyper_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_hyper_cluster_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dev-servers/hyper-clusters",
            "request_type": request.__class__.__name__,
            "response_type": "CreateHyperClusterResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_hyperinstance_tags_async(self, request):
        r"""创建Lite Server超节点标签

        创建Lite Server超节点标签接口用于为Lite Server超节点添加自定义标签。该接口适用于以下场景：当用户需要对Lite Server超节点进行分类管理或标记特定信息时，可以通过此接口为指定的超节点创建标签。使用该接口的前提条件是Lite Server超节点已存在，用户具有创建标签的权限。创建操作完成后，标签将被成功添加到指定的超节点上，用户可以通过标签进行快速查找和管理。若Lite Server超节点不存在、标签已存在或用户无权限操作，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateHyperinstanceTags
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateHyperinstanceTagsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateHyperinstanceTagsResponse`
        """
        http_info = self._create_hyperinstance_tags_http_info(request)
        return self._call_api(**http_info)

    def create_hyperinstance_tags_async_invoker(self, request):
        http_info = self._create_hyperinstance_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_hyperinstance_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dev-servers/hyperinstance/{id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateHyperinstanceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_roce_network_async(self, request):
        r"""创建RoCE网络

        创建RoCE网络接口用于在系统中创建一个新的RoCE网络。该接口适用于以下场景：当用户需要为高性能计算或低延迟应用创建专用的RoCE网络时，可以通过此接口创建并配置RoCE网络。使用该接口的前提条件是用户已登录并具有创建RoCE网络的权限，且系统中已配置了必要的网络资源。创建操作完成后，将生成一个新的RoCE网络，并返回网络的详细信息，包括网络ID、子网信息、配置参数等。若用户无权限操作、系统中缺少必要的网络资源或网络配置参数无效，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRoceNetwork
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateRoceNetworkRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateRoceNetworkResponse`
        """
        http_info = self._create_roce_network_http_info(request)
        return self._call_api(**http_info)

    def create_roce_network_async_invoker(self, request):
        http_info = self._create_roce_network_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_roce_network_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dev-servers/networks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRoceNetworkResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_dev_server_async(self, request):
        r"""删除Lite Server实例

        删除Lite Server实例接口用于移除已创建的Lite Server实例。该接口适用于以下场景：当Lite Server按需实例不再需要使用时或者创建失败的实例以及处于ERROR状态时，用户可通过此接口删除指定的Lite Server实例。使用该接口的前提条件是Lite Server实例已存在且用户具有管理员权限。删除操作完成后，Lite Server实例将被永久移除，相关资源也将被清理。若Lite Server实例不存在或用户无权限操作，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDevServer
        :type request: :class:`huaweicloudsdkmodelarts.v1.DeleteDevServerRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeleteDevServerResponse`
        """
        http_info = self._delete_dev_server_http_info(request)
        return self._call_api(**http_info)

    def delete_dev_server_async_invoker(self, request):
        http_info = self._delete_dev_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_dev_server_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/dev-servers/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDevServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_dev_server_jobs_async(self, request):
        r"""批量删除Lite Server Job

        批量删除Lite Server Job接口用于批量移除已创建的Lite Server Job。该接口适用于以下场景：当多个Lite Server Job已完成、配置错误或需要清理资源时，用户可以通过此接口批量删除指定的Lite Server Job。使用该接口的前提条件是目标Lite Server Job已存在且用户具有管理员权限。删除操作完成后，指定的Lite Server Job将被永久移除，相关资源和配置也将被清理。若目标Lite Server Job不存在、用户无权限操作或请求参数不正确，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDevServerJobs
        :type request: :class:`huaweicloudsdkmodelarts.v1.DeleteDevServerJobsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeleteDevServerJobsResponse`
        """
        http_info = self._delete_dev_server_jobs_http_info(request)
        return self._call_api(**http_info)

    def delete_dev_server_jobs_async_invoker(self, request):
        http_info = self._delete_dev_server_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_dev_server_jobs_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/dev-servers/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDevServerJobsResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_hyper_cluster_async(self, request):
        r"""删除Hyper Cluster实例

        删除Hyper Cluster实例接口用于移除已创建的Hyper Cluster。该接口适用于以下场景：当超节点网络配置错误或需要清理资源时，用户可通过此接口删除指定的超节点网络。使用该接口的前提条件是Hyper Cluster实例已存在且用户具有管理员权限。删除操作完成后，超节点网络将被永久移除，相关资源和配置也将被清理。若Hyper Cluster实例不存在或用户无权限操作，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteHyperCluster
        :type request: :class:`huaweicloudsdkmodelarts.v1.DeleteHyperClusterRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeleteHyperClusterResponse`
        """
        http_info = self._delete_hyper_cluster_http_info(request)
        return self._call_api(**http_info)

    def delete_hyper_cluster_async_invoker(self, request):
        http_info = self._delete_hyper_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_hyper_cluster_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/dev-servers/hyper-clusters/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteHyperClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_hyperinstance_async(self, request):
        r"""删除Lite Server超节点实例

        删除Lite Server超节点实例接口用于删除按需超节点实例同时移除处于ERROR状态的Lite Server超节点实例。该接口适用于以下场景：当超节点实例因创建失败、或其他原因进入ERROR状态；按需超节点实例，用户可以通过此接口删除指定的超节点实例。使用该接口的前提条件是用户已登录并具有删除超节点实例的权限，且指定的超节点实例是按需且处于运行状态、或者处于ERROR状态。删除操作完成后，指定的超节点实例将被永久移除，相关资源也将被清理。若指定的超节点实例不存在、未处于ERROR状态或用户无权限操作，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteHyperinstance
        :type request: :class:`huaweicloudsdkmodelarts.v1.DeleteHyperinstanceRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeleteHyperinstanceResponse`
        """
        http_info = self._delete_hyperinstance_http_info(request)
        return self._call_api(**http_info)

    def delete_hyperinstance_async_invoker(self, request):
        http_info = self._delete_hyperinstance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_hyperinstance_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/dev-servers/hyperinstance/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteHyperinstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_hyperinstance_tags_async(self, request):
        r"""删除Lite Server超节点标签

        删除Lite Server超节点标签接口用于移除已创建的Lite Server超节点标签。该接口适用于以下场景：当用户需要清理不再需要的标签或修正标签错误时，可以通过此接口删除指定的超节点标签。使用该接口的前提条件是Lite Server超节点已存在，且该超节点上已存在要删除的标签，用户具有删除标签的权限。删除操作完成后，指定的标签将从超节点上移除，超节点的其他配置和数据保持不变。若Lite Server超节点不存在、标签不存在或用户无权限操作，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteHyperinstanceTags
        :type request: :class:`huaweicloudsdkmodelarts.v1.DeleteHyperinstanceTagsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeleteHyperinstanceTagsResponse`
        """
        http_info = self._delete_hyperinstance_tags_http_info(request)
        return self._call_api(**http_info)

    def delete_hyperinstance_tags_async_invoker(self, request):
        http_info = self._delete_hyperinstance_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_hyperinstance_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dev-servers/hyperinstance/{id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteHyperinstanceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def detach_dev_server_volume_async(self, request):
        r"""Lite Server服务器卸载磁盘

        Lite Server服务器卸载磁盘接口用于从Lite Server服务器上卸载已挂载的磁盘。该接口适用于以下场景：当用户需要释放存储资源或重新分配磁盘时，可以通过此接口卸载指定的磁盘。使用该接口的前提条件是Lite Server服务器已创建且处于运行状态、或者停止状态，用户具有卸载磁盘的权限，且指定的磁盘已挂载到服务器上。卸载操作完成后，磁盘将从Lite Server服务器上成功卸载，用户可以将其挂载到其他服务器或进行其他操作。若Lite Server服务器不存在、指定的磁盘未挂载到服务器上，或用户无权限操作，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetachDevServerVolume
        :type request: :class:`huaweicloudsdkmodelarts.v1.DetachDevServerVolumeRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DetachDevServerVolumeResponse`
        """
        http_info = self._detach_dev_server_volume_http_info(request)
        return self._call_api(**http_info)

    def detach_dev_server_volume_async_invoker(self, request):
        http_info = self._detach_dev_server_volume_http_info(request)
        return AsyncInvoker(self, http_info)

    def _detach_dev_server_volume_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/dev-servers/{id}/detachvolume/{volume_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DetachDevServerVolumeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_dev_server_image_async(self, request):
        r"""查询Lite Server镜像详情

        查询Lite Server镜像详情接口用于获取指定Lite Server镜像的详细信息。该接口适用于以下场景：当用户需要了解某个Lite Server镜像的具体配置和属性，以便在创建或调整Lite Server实例时选择合适的镜像时，可以通过此接口获取相关信息。使用该接口的前提条件是用户已登录并具有查询镜像详情的权限，且指定的镜像已存在。查询操作完成后，接口将返回指定Lite Server镜像的详细信息，包括镜像ID、名称、操作系统、版本、创建时间等。若用户无权限操作、指定的镜像不存在或镜像ID无效，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetDevServerImage
        :type request: :class:`huaweicloudsdkmodelarts.v1.GetDevServerImageRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.GetDevServerImageResponse`
        """
        http_info = self._get_dev_server_image_http_info(request)
        return self._call_api(**http_info)

    def get_dev_server_image_async_invoker(self, request):
        http_info = self._get_dev_server_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_dev_server_image_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dev-servers/images/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "GetDevServerImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_dev_server_job_async(self, request):
        r"""查询Lite Server Job详情

        查询Lite Server Job详情接口用于获取指定Lite Server Job的详细信息。该接口适用于以下场景：当用户需要查看某个Lite Server Job的执行状态、配置参数、日志信息等详细数据时，可以通过此接口获取相关信息。使用该接口的前提条件是目标Lite Server Job已存在且用户具有查看权限。查询操作完成后，接口将返回指定Lite Server Job的详细信息，包括但不限于Job ID、状态、创建时间、执行时间、配置参数和日志等。若目标Lite Server Job不存在或用户无权限操作，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetDevServerJob
        :type request: :class:`huaweicloudsdkmodelarts.v1.GetDevServerJobRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.GetDevServerJobResponse`
        """
        http_info = self._get_dev_server_job_http_info(request)
        return self._call_api(**http_info)

    def get_dev_server_job_async_invoker(self, request):
        http_info = self._get_dev_server_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_dev_server_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dev-servers/jobs/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "GetDevServerJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_dev_server_job_service_async(self, request):
        r"""获取Lite Server 部署服务详情

        根据服务id获取Lite Server部署服务详情。该接口适用于以下场景：当用户需要查看部署服务详情，以便查看已部署服务的状态、api等信息时，可以通过此接口获取服务详情。使用该接口的前提条件是用户具有查看服务的权限。查询操作完成后，接口将返回此部署服务的详细信息，包括名称、状态、描述、所用模型、实例详情等信息。若用户无权限操作或无相应id，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetDevServerJobService
        :type request: :class:`huaweicloudsdkmodelarts.v1.GetDevServerJobServiceRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.GetDevServerJobServiceResponse`
        """
        http_info = self._get_dev_server_job_service_http_info(request)
        return self._call_api(**http_info)

    def get_dev_server_job_service_async_invoker(self, request):
        http_info = self._get_dev_server_job_service_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_dev_server_job_service_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dev-servers/jobs/services/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "GetDevServerJobServiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_dev_server_job_template_async(self, request):
        r"""获取Lite Server Job模板详情

        获取Lite Server Job模板详情接口用于获取指定Lite Server Job模板的详细信息。该接口适用于以下场景：当用户需要查看某个特定Job模板的详细配置，以便了解其参数设置、使用说明等信息时，可以通过此接口获取模板详情。查询操作完成后，接口将返回指定模板的详细信息，包括模板ID、名称、描述、配置参数等。若目标模板不存在，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetDevServerJobTemplate
        :type request: :class:`huaweicloudsdkmodelarts.v1.GetDevServerJobTemplateRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.GetDevServerJobTemplateResponse`
        """
        http_info = self._get_dev_server_job_template_http_info(request)
        return self._call_api(**http_info)

    def get_dev_server_job_template_async_invoker(self, request):
        http_info = self._get_dev_server_job_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_dev_server_job_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dev-servers/jobs/templates/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "GetDevServerJobTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_dev_server_operation_async(self, request):
        r"""查询Operation详情

        查询Operation详情接口用于获取指定Operation的详细信息。该接口适用于以下场景：当用户需要了解某个Operation的具体执行情况和状态，以便进行故障排查或操作审计时，可以通过此接口获取相关信息。使用该接口的前提条件是用户已登录并具有查询Operation详情的权限，且指定的Operation已存在。查询操作完成后，接口将返回指定Operation的详细信息，包括Operation ID、操作类型、执行状态、开始时间、结束时间、操作结果等。若用户无权限操作、指定的Operation不存在或Operation ID无效，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetDevServerOperation
        :type request: :class:`huaweicloudsdkmodelarts.v1.GetDevServerOperationRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.GetDevServerOperationResponse`
        """
        http_info = self._get_dev_server_operation_http_info(request)
        return self._call_api(**http_info)

    def get_dev_server_operation_async_invoker(self, request):
        http_info = self._get_dev_server_operation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_dev_server_operation_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dev-servers/{id}/operation/{operation_id}",
            "request_type": request.__class__.__name__,
            "response_type": "GetDevServerOperationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']
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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_hyper_cluster_async(self, request):
        r"""查询Hyper Cluster实例详情

        查询Hyper Cluster实例详情接口用于获取指定Hyper Cluster实例的详细信息。该接口适用于以下场景：当用户需要了解某个超节点网络的具体配置和状态，以便进行管理和监控时，可以通过此接口获取相关信息。使用该接口的前提条件是用户已登录并具有查询Hyper Cluster详情的权限，且指定的超节点网络已存在。查询操作完成后，接口将返回指定超节点网络的详细信息，包括ID、名称、子网信息等。若用户无权限操作、指定的超节点网络不存在或ID无效，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetHyperCluster
        :type request: :class:`huaweicloudsdkmodelarts.v1.GetHyperClusterRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.GetHyperClusterResponse`
        """
        http_info = self._get_hyper_cluster_http_info(request)
        return self._call_api(**http_info)

    def get_hyper_cluster_async_invoker(self, request):
        http_info = self._get_hyper_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_hyper_cluster_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dev-servers/hyper-clusters/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "GetHyperClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_hyperinstance_async(self, request):
        r"""查询指定超节点实例详情

        查询指定超节点实例详情接口用于获取特定Lite Server超节点实例的详细信息。该接口适用于以下场景：当用户需要查看某个具体超节点实例的配置、状态和使用情况时，可以通过此接口获取相关信息。使用该接口的前提条件是用户已登录并具有查询超节点实例的权限，且指定的超节点实例已存在。查询操作完成后，接口将返回指定超节点实例的详细信息，包括实例ID、操作系统、运行状态、资源使用情况等。若用户无权限操作、指定的超节点实例不存在或实例ID无效，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetHyperinstance
        :type request: :class:`huaweicloudsdkmodelarts.v1.GetHyperinstanceRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.GetHyperinstanceResponse`
        """
        http_info = self._get_hyperinstance_http_info(request)
        return self._call_api(**http_info)

    def get_hyperinstance_async_invoker(self, request):
        http_info = self._get_hyperinstance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_hyperinstance_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dev-servers/hyperinstance/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "GetHyperinstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_scale_evaluations_dev_server_async(self, request):
        r"""查询Lite Server超节点扩缩容支持规格列表及容量测算

        查询Lite Server超节点扩缩容支持规格列表及容量测算接口用于获取Lite Server超节点支持的扩缩容规格列表，并进行容量测算。该接口适用于以下场景：当用户需要了解Lite Server超节点支持的扩缩容选项，以便在调整超节点资源时选择合适的规格，并评估扩缩容后的资源需求时，可以通过此接口获取相关信息。使用该接口的前提条件是用户已登录并具有查询超节点扩缩容规格的权限，且指定的超节点已存在。查询操作完成后，接口将返回支持的扩缩容规格列表及容量测算结果，包括规格ID、CPU、内存、存储等详细配置和扩缩容后的资源使用情况。若用户无权限操作、指定的超节点不存在或系统中没有可用的扩缩容规格，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetScaleEvaluationsDevServer
        :type request: :class:`huaweicloudsdkmodelarts.v1.GetScaleEvaluationsDevServerRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.GetScaleEvaluationsDevServerResponse`
        """
        http_info = self._get_scale_evaluations_dev_server_http_info(request)
        return self._call_api(**http_info)

    def get_scale_evaluations_dev_server_async_invoker(self, request):
        http_info = self._get_scale_evaluations_dev_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_scale_evaluations_dev_server_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dev-servers/hyperinstance/{id}/scale-evaluations",
            "request_type": request.__class__.__name__,
            "response_type": "GetScaleEvaluationsDevServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_topologies_async(self, request):
        r"""查询实例的Tor信息

        查询实例的Tor信息接口用于获取指定实例的Top-of-Rack（Tor）交换机相关信息。该接口适用于以下场景：当用户需要了解实例连接的Tor交换机的详细信息，以便进行网络配置时，可以通过此接口获取相关信息。使用该接口的前提条件是用户已登录并具有查询实例Tor信息的权限，且指定的实例已存在。查询操作完成后，接口将返回指定实例的Tor信息。若用户无权限操作、指定的实例不存在或实例未连接到Tor交换机，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetTopologies
        :type request: :class:`huaweicloudsdkmodelarts.v1.GetTopologiesRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.GetTopologiesResponse`
        """
        http_info = self._get_topologies_http_info(request)
        return self._call_api(**http_info)

    def get_topologies_async_invoker(self, request):
        http_info = self._get_topologies_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_topologies_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dev-servers/instance-physical-topologies",
            "request_type": request.__class__.__name__,
            "response_type": "GetTopologiesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_all_dev_servers_async(self, request):
        r"""查询租户Lite Server列表

        查询租户Lite Server列表接口用于获取指定租户的所有Lite Server实例信息。该接口适用于以下场景：当用户需要查看其租户下所有Lite Server实例的详细信息，以便进行管理和监控时，可以通过此接口获取相关信息。使用该接口的前提条件是用户已登录并具有查询租户Lite Server列表的权限。查询操作完成后，接口将返回租户下所有Lite Server实例的详细信息，包括实例ID、名称、状态、资源配置等。若用户无权限操作或租户下没有Lite Server实例，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAllDevServers
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListAllDevServersRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListAllDevServersResponse`
        """
        http_info = self._list_all_dev_servers_http_info(request)
        return self._call_api(**http_info)

    def list_all_dev_servers_async_invoker(self, request):
        http_info = self._list_all_dev_servers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_all_dev_servers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dev-servers/all",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllDevServersResponse"
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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_all_hyperinstances_async(self, request):
        r"""查询租户Hyperinstance列表

        查询租户Hyperinstance列表接口用于获取指定租户的所有Hyperinstance实例信息。该接口适用于以下场景：当用户需要查看其租户下所有Hyperinstance实例的详细信息，以便进行管理和监控时，可以通过此接口获取相关信息。使用该接口的前提条件是用户已登录并具有查询租户Hyperinstance列表的权限。查询操作完成后，接口将返回租户下所有Hyperinstance实例的详细信息，包括实例ID、名称、状态、资源配置等。若用户无权限操作或租户下没有Hyperinstance实例，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAllHyperinstances
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListAllHyperinstancesRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListAllHyperinstancesResponse`
        """
        http_info = self._list_all_hyperinstances_http_info(request)
        return self._call_api(**http_info)

    def list_all_hyperinstances_async_invoker(self, request):
        http_info = self._list_all_hyperinstances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_all_hyperinstances_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dev-servers/hyperinstance/all",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllHyperinstancesResponse"
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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_dev_server_flavors_async(self, request):
        r"""查询规格列表

        查询规格列表接口用于获取系统中所有可用的资源规格信息。该接口适用于以下场景：当用户需要了解可用的资源规格，以便在创建或调整Lite Server实例时选择合适的配置时，可以通过此接口获取规格列表。使用该接口的前提条件是用户已登录并具有查询规格的权限。查询操作完成后，接口将返回所有可用的资源规格信息，包括规格ID、CPU、内存、存储等详细配置。若用户无权限操作或系统中没有可用的资源规格，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDevServerFlavors
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListDevServerFlavorsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListDevServerFlavorsResponse`
        """
        http_info = self._list_dev_server_flavors_http_info(request)
        return self._call_api(**http_info)

    def list_dev_server_flavors_async_invoker(self, request):
        http_info = self._list_dev_server_flavors_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_dev_server_flavors_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dev-servers/flavors",
            "request_type": request.__class__.__name__,
            "response_type": "ListDevServerFlavorsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'server_type' in local_var_params:
            query_params.append(('server_type', local_var_params['server_type']))
        if 'arch' in local_var_params:
            query_params.append(('arch', local_var_params['arch']))
        if 'charging_mode' in local_var_params:
            query_params.append(('charging_mode', local_var_params['charging_mode']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_dev_server_images_async(self, request):
        r"""查询Lite Server镜像列表

        查询Lite Server镜像列表接口用于获取系统中所有可用的Lite Server镜像信息。该接口适用于以下场景：当用户需要了解可用的Lite Server镜像，以便在创建或调整Lite Server实例时选择合适的镜像时，可以通过此接口获取镜像列表。使用该接口的前提条件是用户已登录并具有查询镜像列表的权限。查询操作完成后，接口将返回所有可用的Lite Server镜像信息，包括镜像ID、名称、架构类型等。若用户无权限操作或系统中没有可用的镜像，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDevServerImages
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListDevServerImagesRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListDevServerImagesResponse`
        """
        http_info = self._list_dev_server_images_http_info(request)
        return self._call_api(**http_info)

    def list_dev_server_images_async_invoker(self, request):
        http_info = self._list_dev_server_images_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_dev_server_images_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dev-servers/images",
            "request_type": request.__class__.__name__,
            "response_type": "ListDevServerImagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'server_type' in local_var_params:
            query_params.append(('server_type', local_var_params['server_type']))
        if 'flavor_name' in local_var_params:
            query_params.append(('flavor_name', local_var_params['flavor_name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_dev_server_job_templates_async(self, request):
        r"""获取Lite Server Job模板列表

        获取Lite Server Job模板列表接口用于获取可用的Lite Server Job模板列表。该接口适用于以下场景：当用户需要查看可用的Job模板，以便选择合适的模板来创建新的Lite Server任务时，可以通过此接口获取模板列表。查询操作完成后，接口将返回所有可用的Lite Server Job模板列表，包括模板ID、名称、描述等信息。若系统中无可用模板，接口将返回相应的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDevServerJobTemplates
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListDevServerJobTemplatesRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListDevServerJobTemplatesResponse`
        """
        http_info = self._list_dev_server_job_templates_http_info(request)
        return self._call_api(**http_info)

    def list_dev_server_job_templates_async_invoker(self, request):
        http_info = self._list_dev_server_job_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_dev_server_job_templates_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dev-servers/jobs/templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListDevServerJobTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_dev_server_jobs_async(self, request):
        r"""查询Lite Server Job列表

        查询Lite Server Job列表接口用于获取Lite Server Job的列表信息，并支持按照状态、ID等相关字段进行过滤。该接口适用于以下场景：当用户需要查看多个Lite Server Job的概要信息，例如在监控作业状态、排查问题或进行日常管理时，可以通过此接口获取符合过滤条件的Job列表。使用该接口的前提条件是用户具有查看权限。查询操作完成后，接口将返回符合条件的Lite Server Job列表，包括每个Job的ID、状态、创建时间等基本信息。若用户无权限操作或请求参数不正确，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDevServerJobs
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListDevServerJobsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListDevServerJobsResponse`
        """
        http_info = self._list_dev_server_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_dev_server_jobs_async_invoker(self, request):
        http_info = self._list_dev_server_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_dev_server_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dev-servers/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListDevServerJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'visible' in local_var_params:
            query_params.append(('visible', local_var_params['visible']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_dev_server_public_ip_async(self, request):
        r"""查询已绑定的EIP

        查询已绑定的EIP接口用于获取已绑定到Lite Server服务器上的弹性公网IP（EIP）信息。该接口适用于以下场景：当用户需要查看Lite Server服务器上已绑定的EIP及其详细信息时，可以通过此接口获取相关信息。使用该接口的前提条件是用户已登录并具有查询EIP的权限，且指定的Lite Server服务器已存在。查询操作完成后，接口将返回已绑定到Lite Server服务器上的EIP的详细信息，包括EIP地址、绑定时间、状态等。若Lite Server服务器不存在、未绑定EIP或用户无权限操作，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDevServerPublicIP
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListDevServerPublicIPRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListDevServerPublicIPResponse`
        """
        http_info = self._list_dev_server_public_ip_http_info(request)
        return self._call_api(**http_info)

    def list_dev_server_public_ip_async_invoker(self, request):
        http_info = self._list_dev_server_public_ip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_dev_server_public_ip_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dev-servers/{id}/publicips",
            "request_type": request.__class__.__name__,
            "response_type": "ListDevServerPublicIPResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_dev_servers_async(self, request):
        r"""查询用户所有Lite Server实例列表

        查询用户所有Lite Server实例列表接口用于获取用户名下所有Lite Server实例的详细信息。该接口适用于以下场景：用户需要查看其所有Lite Server实例的状态、配置等信息，以便进行资源管理和监控。使用该接口的前提条件是用户已登录且具有查看Lite Server实例的权限。调用此接口后，系统将返回用户名下所有Lite Server实例的列表，包括实例ID、名称、状态、创建时间等信息。若用户无权限或未登录，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDevServers
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListDevServersRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListDevServersResponse`
        """
        http_info = self._list_dev_servers_http_info(request)
        return self._call_api(**http_info)

    def list_dev_servers_async_invoker(self, request):
        http_info = self._list_dev_servers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_dev_servers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dev-servers",
            "request_type": request.__class__.__name__,
            "response_type": "ListDevServersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'owner' in local_var_params:
            query_params.append(('owner', local_var_params['owner']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_hyper_cluster_async(self, request):
        r"""查询Hyper Cluster详情列表

        查询Hyper Cluster详情列表接口用于获取所有Hyper Cluster的详细信息。该接口适用于以下场景：当用户需要了解系统中所有超节点网络的配置和状态时，可以通过此接口获取相关信息。使用该接口的前提条件是用户已登录并具有查询Hyper Cluster详情的权限。查询操作完成后，接口将返回所有超节点网络的详细信息，包括ID、名称、子网信息等。若用户无权限操作或系统中没有Hyper Cluster，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHyperCluster
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListHyperClusterRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListHyperClusterResponse`
        """
        http_info = self._list_hyper_cluster_http_info(request)
        return self._call_api(**http_info)

    def list_hyper_cluster_async_invoker(self, request):
        http_info = self._list_hyper_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_hyper_cluster_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dev-servers/hyper-clusters",
            "request_type": request.__class__.__name__,
            "response_type": "ListHyperClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_hyperinstance_clusters_capacity_async(self, request):
        r"""查询超节点hyperinstance-clusters逻辑容量测算结果

        查询超节点hyperinstance-clusters逻辑容量测算结果接口用于获取指定超节点集群的逻辑容量测算结果。该接口适用于以下场景：当用户需要了解超节点集群的资源使用情况和容量规划，以便进行资源管理和优化时，可以通过此接口获取逻辑容量测算结果。使用该接口的前提条件是用户已登录并具有查询超节点集群逻辑容量的权限，且指定的超节点集群已存在。查询操作完成后，接口将返回指定超节点集群的逻辑容量测算结果，包括可用容量信息。若用户无权限操作、指定的超节点集群不存在或集群ID无效，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHyperinstanceClustersCapacity
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListHyperinstanceClustersCapacityRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListHyperinstanceClustersCapacityResponse`
        """
        http_info = self._list_hyperinstance_clusters_capacity_http_info(request)
        return self._call_api(**http_info)

    def list_hyperinstance_clusters_capacity_async_invoker(self, request):
        http_info = self._list_hyperinstance_clusters_capacity_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_hyperinstance_clusters_capacity_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dev-servers/hyperinstance/cluster-capacity-evaluations",
            "request_type": request.__class__.__name__,
            "response_type": "ListHyperinstanceClustersCapacityResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_hyperinstances_async(self, request):
        r"""查询用户所有超节点实例详情

        查询用户所有超节点实例详情接口用于获取用户所有Lite Server超节点实例的详细信息。该接口适用于以下场景：当用户需要查看其所有超节点实例的配置、状态和使用情况时，可以通过此接口获取相关信息。使用该接口的前提条件是用户已登录并具有查询超节点实例的权限。查询操作完成后，接口将返回所有超节点实例的详细信息，包括实例ID、操作系统、运行状态、资源使用情况等。若用户无权限操作或没有超节点实例，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHyperinstances
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListHyperinstancesRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListHyperinstancesResponse`
        """
        http_info = self._list_hyperinstances_http_info(request)
        return self._call_api(**http_info)

    def list_hyperinstances_async_invoker(self, request):
        http_info = self._list_hyperinstances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_hyperinstances_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dev-servers/hyperinstance",
            "request_type": request.__class__.__name__,
            "response_type": "ListHyperinstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def query_hyperinstance_tags_async(self, request):
        r"""查询Lite Server超节点标签

        查询Lite Server超节点标签接口用于获取Lite Server超节点上的所有标签信息。该接口适用于以下场景：当用户需要查看或管理Lite Server超节点的标签时，可以通过此接口查询指定超节点上的所有标签。使用该接口的前提条件是Lite Server超节点已存在，用户具有查询标签的权限。查询操作完成后，接口将返回超节点上的所有标签信息，包括标签名称和相关属性。若Lite Server超节点不存在或用户无权限操作，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for QueryHyperinstanceTags
        :type request: :class:`huaweicloudsdkmodelarts.v1.QueryHyperinstanceTagsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.QueryHyperinstanceTagsResponse`
        """
        http_info = self._query_hyperinstance_tags_http_info(request)
        return self._call_api(**http_info)

    def query_hyperinstance_tags_async_invoker(self, request):
        http_info = self._query_hyperinstance_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _query_hyperinstance_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dev-servers/hyperinstance/{id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "QueryHyperinstanceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def reboot_dev_server_async(self, request):
        r"""重启Lite Server实例

        重启Lite Server实例接口用于重启正在运行的Lite Server实例。该接口适用于以下场景：当用户需要重启实例以应用配置更改、解决运行问题或进行系统维护时，可以通过此接口重启指定的Lite Server实例。使用该接口的前提条件是Lite Server实例已创建且处于运行状态，用户具有重启实例的权限。重启操作完成后，Lite Server实例将重新启动并进入运行状态，用户可以继续使用实例提供的服务。若Lite Server实例不存在、已处于停止状态或用户无权限操作，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RebootDevServer
        :type request: :class:`huaweicloudsdkmodelarts.v1.RebootDevServerRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.RebootDevServerResponse`
        """
        http_info = self._reboot_dev_server_http_info(request)
        return self._call_api(**http_info)

    def reboot_dev_server_async_invoker(self, request):
        http_info = self._reboot_dev_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reboot_dev_server_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/dev-servers/{id}/reboot",
            "request_type": request.__class__.__name__,
            "response_type": "RebootDevServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def reinstall_dev_server_os_async(self, request):
        r"""重装Lite Server服务器操作系统镜像

        重装Lite Server服务器操作系统镜像接口用于重新安装Lite Server服务器的操作系统镜像。该接口适用于以下场景：当用户需要更新操作系统版本、修复系统故障或重新配置系统环境时，可以通过此接口重装指定的Lite Server服务器操作系统镜像。使用该接口的前提条件是Lite Server服务器已存在且处于停止状态，用户具有重装操作系统的权限。重装操作完成后，Lite Server服务器将安装新的操作系统镜像，并重新进入运行状态，若Lite Server服务器不存在、已处于运行状态或用户无权限操作，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ReinstallDevServerOS
        :type request: :class:`huaweicloudsdkmodelarts.v1.ReinstallDevServerOSRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ReinstallDevServerOSResponse`
        """
        http_info = self._reinstall_dev_server_os_http_info(request)
        return self._call_api(**http_info)

    def reinstall_dev_server_os_async_invoker(self, request):
        http_info = self._reinstall_dev_server_os_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reinstall_dev_server_os_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dev-servers/{id}/reinstallos",
            "request_type": request.__class__.__name__,
            "response_type": "ReinstallDevServerOSResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def scale_down_hyperinstance_async(self, request):
        r"""缩容Lite Server超节点

        缩容Lite Server超节点接口用于减少Lite Server超节点的资源容量。该接口适用于以下场景：当用户需要降低Lite Server超节点的资源使用，以节省成本或优化资源分配时，可以通过此接口进行缩容。使用该接口的前提条件是用户已登录并具有缩容超节点的权限，且指定的超节点已存在且处于运行状态。缩容操作完成后，超节点的资源容量将根据指定的规格进行调整，用户可以立即使用减少后的资源。若用户无权限操作、指定的超节点不存在、超节点已处于最小容量或指定的缩容规格无效，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ScaleDownHyperinstance
        :type request: :class:`huaweicloudsdkmodelarts.v1.ScaleDownHyperinstanceRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ScaleDownHyperinstanceResponse`
        """
        http_info = self._scale_down_hyperinstance_http_info(request)
        return self._call_api(**http_info)

    def scale_down_hyperinstance_async_invoker(self, request):
        http_info = self._scale_down_hyperinstance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _scale_down_hyperinstance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dev-servers/hyperinstance/{id}/live-scale-down",
            "request_type": request.__class__.__name__,
            "response_type": "ScaleDownHyperinstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def scale_up_hyperinstance_async(self, request):
        r"""扩容Lite Server超节点

        扩容Lite Server超节点接口用于增加Lite Server超节点的资源容量。该接口适用于以下场景：当用户需要提升Lite Server超节点的性能，以支持更多的负载或更大的数据处理需求时，可以通过此接口进行扩容。使用该接口的前提条件是用户已登录并具有扩容超节点的权限，且指定的超节点已存在且处于运行状态。扩容操作完成后，超节点的资源容量将根据指定的规格进行调整，用户可以立即使用增加的资源。若用户无权限操作、指定的超节点不存在、超节点已处于最大容量或指定的扩容规格无效，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ScaleUpHyperinstance
        :type request: :class:`huaweicloudsdkmodelarts.v1.ScaleUpHyperinstanceRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ScaleUpHyperinstanceResponse`
        """
        http_info = self._scale_up_hyperinstance_http_info(request)
        return self._call_api(**http_info)

    def scale_up_hyperinstance_async_invoker(self, request):
        http_info = self._scale_up_hyperinstance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _scale_up_hyperinstance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dev-servers/hyperinstance/{id}/live-scale-up",
            "request_type": request.__class__.__name__,
            "response_type": "ScaleUpHyperinstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_dev_server_async(self, request):
        r"""查询Lite Server实例详情

        查询Lite Server实例详情接口用于获取指定Lite Server实例的详细信息。该接口适用于以下场景：用户需要查看特定Lite Server实例的配置、状态、网络信息等详细数据，以便进行故障排查、资源管理和监控。使用该接口的前提条件是用户已登录且具有查看Lite Server实例的权限，并且需要提供有效的实例ID。查询操作完成后，系统将返回指定Lite Server实例的详细信息，包括实例ID、名称、状态、配置、网络配置等。若用户无权限、实例ID无效或实例不存在，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDevServer
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowDevServerRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowDevServerResponse`
        """
        http_info = self._show_dev_server_http_info(request)
        return self._call_api(**http_info)

    def show_dev_server_async_invoker(self, request):
        http_info = self._show_dev_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_dev_server_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dev-servers/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDevServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def start_dev_server_async(self, request):
        r"""启动Lite Server实例

        启动Lite Server实例接口用于启动已创建但未运行的Lite Server实例。该接口适用于以下场景：当用户需要开始使用Lite Server实例进行开发或测试时，可以通过此接口启动指定的Lite Server实例。使用该接口的前提条件是Lite Server实例已创建且处于停止状态，用户具有启动实例的权限。若Lite Server实例不存在、已处于运行状态或用户无权限操作，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartDevServer
        :type request: :class:`huaweicloudsdkmodelarts.v1.StartDevServerRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.StartDevServerResponse`
        """
        http_info = self._start_dev_server_http_info(request)
        return self._call_api(**http_info)

    def start_dev_server_async_invoker(self, request):
        http_info = self._start_dev_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_dev_server_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/dev-servers/{id}/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartDevServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def start_hyperinstance_async(self, request):
        r"""启动Lite Server超节点服务器

        启动Lite Server超节点服务器接口用于启动已创建但未运行的Lite Server超节点服务器。该接口适用于以下场景：当用户需要开始使用Lite Server超节点服务器进行开发或测试时，可以通过此接口启动指定的超节点服务器。使用该接口的前提条件是Lite Server超节点服务器已创建且处于停止状态，用户具有启动超节点服务器的权限。启动操作完成后，超节点服务器将进入运行状态，用户可以访问和使用服务器提供的服务。若Lite Server超节点服务器不存在、已处于运行状态或用户无权限操作，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartHyperinstance
        :type request: :class:`huaweicloudsdkmodelarts.v1.StartHyperinstanceRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.StartHyperinstanceResponse`
        """
        http_info = self._start_hyperinstance_http_info(request)
        return self._call_api(**http_info)

    def start_hyperinstance_async_invoker(self, request):
        http_info = self._start_hyperinstance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_hyperinstance_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/dev-servers/hyperinstance/{id}/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartHyperinstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def stop_dev_server_async(self, request):
        r"""停止Lite Server实例

        停止Lite Server实例接口用于停止正在运行的Lite Server实例。该接口适用于以下场景：当用户需要停止Lite Server实例，以节省资源或进行维护时，可以通过此接口停止指定的Lite Server实例。使用该接口的前提条件是Lite Server实例已创建且处于运行状态，用户具有停止实例的权限。若Lite Server实例不存在、已处于停止状态或用户无权限操作，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopDevServer
        :type request: :class:`huaweicloudsdkmodelarts.v1.StopDevServerRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.StopDevServerResponse`
        """
        http_info = self._stop_dev_server_http_info(request)
        return self._call_api(**http_info)

    def stop_dev_server_async_invoker(self, request):
        http_info = self._stop_dev_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_dev_server_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/dev-servers/{id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopDevServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def stop_hyperinstance_async(self, request):
        r"""停止Lite Server超节点服务器

        停止Lite Server超节点服务器接口用于停止正在运行的Lite Server超节点服务器。该接口适用于以下场景：当用户需要暂停使用Lite Server超节点服务器，以节省资源或进行维护时，可以通过此接口停止指定的超节点服务器。使用该接口的前提条件是Lite Server超节点服务器已创建且处于运行状态或者停止失败状态，用户具有停止超节点服务器的权限。停止操作完成后，超节点服务器将进入停止状态，不再提供服务。若Lite Server超节点服务器不存在、已处于停止状态或用户无权限操作，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopHyperinstance
        :type request: :class:`huaweicloudsdkmodelarts.v1.StopHyperinstanceRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.StopHyperinstanceResponse`
        """
        http_info = self._stop_hyperinstance_http_info(request)
        return self._call_api(**http_info)

    def stop_hyperinstance_async_invoker(self, request):
        http_info = self._stop_hyperinstance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_hyperinstance_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/dev-servers/hyperinstance/{id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopHyperinstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def sync_dev_servers_async(self, request):
        r"""实时同步用户指定Lite Server实例状态

        实时同步用户Lite Server实例状态接口用于实时获取并同步用户Lite Server实例的当前状态。该接口适用于以下场景：用户需要实时监控其Lite Server实例的运行状态，确保实例正常运行或及时发现并处理异常情况。使用该接口的前提条件是用户已登录并具有相应的权限，且Lite Server实例已创建并处于运行状态。接口调用成功后，将返回Lite Server实例的最新状态信息，包括但不限于实例ID、运行状态、资源使用情况等。若用户无权限操作或Lite Server实例不存在，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SyncDevServers
        :type request: :class:`huaweicloudsdkmodelarts.v1.SyncDevServersRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.SyncDevServersResponse`
        """
        http_info = self._sync_dev_servers_http_info(request)
        return self._call_api(**http_info)

    def sync_dev_servers_async_invoker(self, request):
        http_info = self._sync_dev_servers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _sync_dev_servers_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/dev-servers/sync",
            "request_type": request.__class__.__name__,
            "response_type": "SyncDevServersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'owner' in local_var_params:
            query_params.append(('owner', local_var_params['owner']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_dev_server_async(self, request):
        r"""修改Lite Server实例名称

        修改DevServer实例名称接口用于更改已创建的DevServer实例的名称。该接口适用于以下场景：当用户需要对DevServer实例进行重命名以更好地反映实例的功能或用途时，或者在实例名称不再符合当前项目命名规范时进行更新。使用该接口的前提条件是DevServer实例已存在且用户具有对该实例的管理权限。修改操作完成后，实例的新名称将立即生效，并在所有相关视图和记录中更新。若DevServer实例不存在、用户无权限操作或新名称不符合命名规则，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDevServer
        :type request: :class:`huaweicloudsdkmodelarts.v1.UpdateDevServerRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.UpdateDevServerResponse`
        """
        http_info = self._update_dev_server_http_info(request)
        return self._call_api(**http_info)

    def update_dev_server_async_invoker(self, request):
        http_info = self._update_dev_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_dev_server_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/dev-servers/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDevServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_image_async(self, request):
        r"""通过运行的实例保存成容器镜像

        通过运行的实例保存成容器镜像接口用于将正在运行的实例保存为容器镜像。该接口适用于以下场景：用户需要保存当前运行环境以便后续使用或开发时，可通过此接口将实例保存为镜像。使用该接口的前提条件是用户已登录系统并具有访问目标实例的权限，同时实例必须处于运行状态。调用该接口后，系统将保存实例的当前状态为容器镜像，包括安装的依赖包和插件。若用户无权限访问指定实例或实例未运行，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateImage
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateImageRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateImageResponse`
        """
        http_info = self._create_image_http_info(request)
        return self._call_api(**http_info)

    def create_image_async_invoker(self, request):
        http_info = self._create_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_image_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/notebooks/{id}/create-image",
            "request_type": request.__class__.__name__,
            "response_type": "CreateImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_notebook_async(self, request):
        r"""创建Notebook实例

        创建Notebook实例接口用于根据指定的参数创建一个新的Notebook实例。该接口适用于以下场景：用户需要为特定任务或项目创建Notebook实例时，可通过此接口指定实例规格、AI引擎镜像和存储配置。使用该接口的前提条件是用户已登录系统并具有创建Notebook实例的权限，同时需提供有效的创建参数。调用该接口后，系统将异步创建Notebook实例，用户可通过查询接口获取实例状态。创建完成后，用户可通过网页或SSH客户端访问Notebook实例。若用户无权限创建实例或参数无效，接口将返回相应的错误信息。异常情况包括：若系统资源不足，或创建操作失败，接口将返回相应的错误提示。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateNotebook
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateNotebookRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateNotebookResponse`
        """
        http_info = self._create_notebook_http_info(request)
        return self._call_api(**http_info)

    def create_notebook_async_invoker(self, request):
        http_info = self._create_notebook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_notebook_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/notebooks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateNotebookResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_notebook_tags_async(self, request):
        r"""添加资源标签

        添加资源标签接口用于为指定的Notebook实例添加标签信息。该接口适用于以下场景：用户需要为Notebook实例添加标签信息，可通过此接口添加一个或多个标签。使用该接口的前提条件是用户已登录系统并具有操作目标Notebook实例的权限。调用该接口后，系统将为指定的Notebook实例添加标签，若标签的key已存在，则覆盖原有的value值。若用户无权限操作指定Notebook实例或输入的参数无效，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateNotebookTags
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateNotebookTagsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateNotebookTagsResponse`
        """
        http_info = self._create_notebook_tags_http_info(request)
        return self._call_api(**http_info)

    def create_notebook_tags_async_invoker(self, request):
        http_info = self._create_notebook_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_notebook_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/notebooks/{resource_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateNotebookTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_notebook_async(self, request):
        r"""删除Notebook实例

        删除Notebook实例接口用于移除已创建的Notebook实例及其相关资源。该接口适用于以下场景：用户需要清理不再使用的Notebook实例时，可通过此接口删除指定的Notebook实例，包括其容器和所有存储资源。使用该接口的前提条件是用户已登录系统并具有操作目标Notebook实例的权限。调用该接口后，系统将删除指定的Notebook实例及其相关资源。若用户无权限操作指定实例或Notebook实例未停止，接口将返回相应的错误信息。异常情况包括：若指定的Notebook实例不存在，或删除操作失败，接口将返回相应的错误提示。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteNotebook
        :type request: :class:`huaweicloudsdkmodelarts.v1.DeleteNotebookRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeleteNotebookResponse`
        """
        http_info = self._delete_notebook_http_info(request)
        return self._call_api(**http_info)

    def delete_notebook_async_invoker(self, request):
        http_info = self._delete_notebook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_notebook_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/notebooks/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNotebookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_notebook_tags_async(self, request):
        r"""删除资源标签

        删除资源标签接口用于移除指定Notebook实例的标签信息。该接口适用于以下场景：用户需要清理或重新组织Notebook实例的标签时，可通过此接口删除单个或多个标签。使用该接口的前提条件是用户已登录系统并具有操作目标Notebook实例的权限。调用该接口后，系统将删除指定的标签，若标签不存在则不进行操作。若用户无权限操作指定Notebook实例或输入的参数无效，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteNotebookTags
        :type request: :class:`huaweicloudsdkmodelarts.v1.DeleteNotebookTagsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeleteNotebookTagsResponse`
        """
        http_info = self._delete_notebook_tags_http_info(request)
        return self._call_api(**http_info)

    def delete_notebook_tags_async_invoker(self, request):
        http_info = self._delete_notebook_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_notebook_tags_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/notebooks/{resource_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNotebookTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))

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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_all_notebooks_async(self, request):
        r"""查询所有Notebook实例列表

        查询所有Notebook实例列表接口用于获取所有已创建的Notebook实例信息。该接口适用于以下场景：用户需要全面了解当前系统中所有Notebook实例的状态、资源使用情况或管理多个Notebook实例时，可通过此接口获取相关信息。使用该接口的前提条件是用户已创建Notebook实例，并且具有相应的查询权限。调用成功后，系统将返回所有Notebook实例的列表，包含实例ID、状态、创建时间等详细信息。若用户无权限访问，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAllNotebooks
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListAllNotebooksRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListAllNotebooksResponse`
        """
        http_info = self._list_all_notebooks_http_info(request)
        return self._call_api(**http_info)

    def list_all_notebooks_async_invoker(self, request):
        http_info = self._list_all_notebooks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_all_notebooks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/notebooks/all",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllNotebooksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'feature' in local_var_params:
            query_params.append(('feature', local_var_params['feature']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'pool_id' in local_var_params:
            query_params.append(('pool_id', local_var_params['pool_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'owner' in local_var_params:
            query_params.append(('owner', local_var_params['owner']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))
        if 'flavor' in local_var_params:
            query_params.append(('flavor', local_var_params['flavor']))
        if 'image_id' in local_var_params:
            query_params.append(('image_id', local_var_params['image_id']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'billing' in local_var_params:
            query_params.append(('billing', local_var_params['billing']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_authoring_clusters_async(self, request):
        r"""查询用户所有Notebook资源池实例详情

        查询用户所有Notebook资源池实例详情接口用于获取用户关联的所有Notebook资源池实例的详细信息。该接口适用于以下场景：当用户创建Notebook示例需要选择资源池时，可通过此接口获取所有资源池实例列表信息。使用该接口的前提条件是用户已注册并登录系统，且具有查看资源池实例的权限。调用成功后，接口将返回包含所有资源池实例的详细信息列表，包括实例名称、状态、节点规格等。若用户未登录、无权限访问或系统内部出现错误，接口将返回相应的错误信息，如未认证、无权限或服务不可用等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAuthoringClusters
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListAuthoringClustersRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListAuthoringClustersResponse`
        """
        http_info = self._list_authoring_clusters_http_info(request)
        return self._call_api(**http_info)

    def list_authoring_clusters_async_invoker(self, request):
        http_info = self._list_authoring_clusters_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_authoring_clusters_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/authoring/clusters",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuthoringClustersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'scope' in local_var_params:
            query_params.append(('scope', local_var_params['scope']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_features_async(self, request):
        r"""查询当前用户指定特性的开关及配额

        查询当前用户指定特性的开关及配额接口用于获取指定特性在当前用户下的开关状态及配额信息。该接口适用于以下场景：当用户需要了解特定特性是否已开启、查看配额限制或监控已使用的资源情况时，可通过此接口查询相关信息。使用该接口的前提条件是用户已登录且具有查询权限，同时指定的特性必须存在。调用该接口后，系统将返回该特性是否已开启、配额总量及已使用的资源情况等详细信息。若用户无权限查询、特性不存在或系统出现异常，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFeatures
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListFeaturesRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListFeaturesResponse`
        """
        http_info = self._list_features_http_info(request)
        return self._call_api(**http_info)

    def list_features_async_invoker(self, request):
        http_info = self._list_features_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_features_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/authoring/features/{feature}",
            "request_type": request.__class__.__name__,
            "response_type": "ListFeaturesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'feature' in local_var_params:
            path_params['feature'] = local_var_params['feature']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_flavors_async(self, request):
        r"""查询Notebook支持的有效规格列表

        查询Notebook支持的有效规格列表接口用于获取运行Notebook实例时可使用的规格选项。该接口适用于以下场景：用户需要了解Notebook实例支持的配置选项时，可通过此接口查询可用的规格列表。使用该接口的前提条件是用户已登录系统并具有访问目标Notebook实例的权限。调用该接口后，系统将返回Notebook实例支持的有效规格列表，包括内存、CPU等配置信息。若用户无权限访问指定实例或Notebook实例未运行，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFlavors
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListFlavorsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListFlavorsResponse`
        """
        http_info = self._list_flavors_http_info(request)
        return self._call_api(**http_info)

    def list_flavors_async_invoker(self, request):
        http_info = self._list_flavors_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_flavors_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/notebooks/flavors",
            "request_type": request.__class__.__name__,
            "response_type": "ListFlavorsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'flavor_type' in local_var_params:
            query_params.append(('flavor_type', local_var_params['flavor_type']))
        if 'feature' in local_var_params:
            query_params.append(('feature', local_var_params['feature']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_notebooks_async(self, request):
        r"""查询Notebook实例列表

        查询Notebook实例列表接口用于获取满足特定条件的Notebook实例信息。该接口适用于以下场景：用户管理多个Notebook实例或查看特定状态的Notebook实例时，可通过此接口获取相关信息。使用该接口的前提条件是用户已创建Notebook实例，并且具有相应的查询权限。调用成功后，系统将返回符合条件的Notebook实例列表，包含实例ID、状态、创建时间等详细信息。若用户无权限访问或查询条件不明确，接口将返回相应的错误信息或空列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNotebooks
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListNotebooksRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListNotebooksResponse`
        """
        http_info = self._list_notebooks_http_info(request)
        return self._call_api(**http_info)

    def list_notebooks_async_invoker(self, request):
        http_info = self._list_notebooks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_notebooks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/notebooks",
            "request_type": request.__class__.__name__,
            "response_type": "ListNotebooksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'feature' in local_var_params:
            query_params.append(('feature', local_var_params['feature']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'pool_id' in local_var_params:
            query_params.append(('pool_id', local_var_params['pool_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'owner' in local_var_params:
            query_params.append(('owner', local_var_params['owner']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))
        if 'flavor' in local_var_params:
            query_params.append(('flavor', local_var_params['flavor']))
        if 'image_id' in local_var_params:
            query_params.append(('image_id', local_var_params['image_id']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'billing' in local_var_params:
            query_params.append(('billing', local_var_params['billing']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def renew_lease_async(self, request):
        r"""Notebook时长续约

        Notebook时长续约接口用于延长运行中的Notebook实例的运行时间。该接口适用于以下场景：用户需要延长Notebook实例的使用时间以完成长时间任务时，可通过此接口延长指定实例的运行时间。使用该接口的前提条件是用户已登录系统并具有操作目标Notebook实例的权限，同时Notebook实例必须处于运行状态。调用该接口后，系统将延长指定Notebook实例的运行时间，用户可继续使用。若用户无权限操作指定实例或Notebook实例未运行，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RenewLease
        :type request: :class:`huaweicloudsdkmodelarts.v1.RenewLeaseRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.RenewLeaseResponse`
        """
        http_info = self._renew_lease_http_info(request)
        return self._call_api(**http_info)

    def renew_lease_async_invoker(self, request):
        http_info = self._renew_lease_http_info(request)
        return AsyncInvoker(self, http_info)

    def _renew_lease_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/notebooks/{id}/lease",
            "request_type": request.__class__.__name__,
            "response_type": "RenewLeaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'duration' in local_var_params:
            query_params.append(('duration', local_var_params['duration']))

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

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_cluster_async(self, request):
        r"""查询Notebook资源池详情

        查询Notebook资源池详情接口用于获取资源池的详细信息。该接口适用于以下场景：当用户需要创建Notebook实例作业时，可通过此接口查询指定集群的详细信息。使用该接口的前提条件是集群已成功纳管且用户具有相应的访问权限。调用该接口后，系统将返回集群的实例ID、名称、Flavor规格、实例状态以及实例可打开的URL等详细信息。若集群不存在、未被纳管或用户无权限访问，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCluster
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowClusterRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowClusterResponse`
        """
        http_info = self._show_cluster_http_info(request)
        return self._call_api(**http_info)

    def show_cluster_async_invoker(self, request):
        http_info = self._show_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_cluster_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/authoring/clusters/{cluster_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_lease_async(self, request):
        r"""查询运行中的Notebook可用时长

        查询运行中的Notebook可用时长接口用于获取正在运行的Notebook实例的剩余可用时间。该接口适用于以下场景：用户需要了解Notebook实例的剩余运行时间以合理安排任务时，可通过此接口查询指定实例的可用时长。使用该接口的前提条件是用户已登录系统并具有访问目标Notebook实例的权限，同时Notebook实例必须处于运行状态。调用该接口后，系统将返回指定Notebook实例的可用时长信息。若用户无权限访问指定实例或Notebook实例未运行，接口将返回相应的错误信息。异常情况包括：若指定的Notebook实例不存在，或查询操作失败，接口将返回相应的错误提示。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowLease
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowLeaseRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowLeaseResponse`
        """
        http_info = self._show_lease_http_info(request)
        return self._call_api(**http_info)

    def show_lease_async_invoker(self, request):
        http_info = self._show_lease_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_lease_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/notebooks/{id}/lease",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLeaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_notebook_async(self, request):
        r"""查询Notebook实例详情

        查询Notebook实例详情接口用于获取指定Notebook实例的详细信息。该接口适用于以下场景：用户需要查看特定Notebook实例的详细配置、运行状态或获取访问链接时，可通过此接口获取相关信息。使用该接口的前提条件是Notebook实例已存在且用户具有相应的查询权限。调用成功后，系统将返回实例ID、名称、规格、镜像、实例状态和实例可打开的URL等详细信息。若实例不存在或用户无权限访问，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNotebook
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowNotebookRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowNotebookResponse`
        """
        http_info = self._show_notebook_http_info(request)
        return self._call_api(**http_info)

    def show_notebook_async_invoker(self, request):
        http_info = self._show_notebook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_notebook_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/notebooks/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNotebookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_notebook_tags_async(self, request):
        r"""查询Notebook资源类型下的标签

        查询Notebook资源类型下的标签接口用于获取用户当前project下Notebook实例的标签信息。该接口适用于以下场景：用户需要管理或统计Notebook资源时，可通过此接口查询特定标签或所有标签的Notebook实例。使用该接口的前提条件是用户已登录系统并具有访问权限，同时可指定工作空间或默认查询所有工作空间。调用该接口后，系统将返回指定Notebook实例的标签列表，包括标签名称、标签值等信息。若用户无权限，则返回相应的异常信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNotebookTags
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowNotebookTagsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowNotebookTagsResponse`
        """
        http_info = self._show_notebook_tags_http_info(request)
        return self._call_api(**http_info)

    def show_notebook_tags_async_invoker(self, request):
        http_info = self._show_notebook_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_notebook_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/notebooks/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNotebookTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_switchable_flavors_async(self, request):
        r"""查询Notebook支持的可切换规格列表

        查询Notebook支持的可切换规格列表接口用于获取创建Notebook实例时可选择的规格选项。该接口适用于以下场景：用户需要了解Notebook实例支持的配置选项时，可通过此接口查询可用的规格列表。使用该接口的前提条件是用户已登录系统并具有创建Notebook实例的权限。调用该接口后，系统将返回Notebook实例支持的可切换规格列表，包括内存、CPU等配置信息。若用户无权限创建Notebook实例，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSwitchableFlavors
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowSwitchableFlavorsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowSwitchableFlavorsResponse`
        """
        http_info = self._show_switchable_flavors_http_info(request)
        return self._call_api(**http_info)

    def show_switchable_flavors_async_invoker(self, request):
        http_info = self._show_switchable_flavors_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_switchable_flavors_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/notebooks/{id}/flavors",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSwitchableFlavorsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def start_notebook_async(self, request):
        r"""启动Notebook实例

        启动Notebook实例接口用于启动已创建的Notebook实例。该接口适用于以下场景：用户需要开始运行Notebook实例以进行数据处理、模型训练或开发时，可通过此接口启动指定的Notebook实例。使用该接口的前提条件是用户已登录系统并具有操作目标Notebook实例的权限，同时Notebook实例必须处于停止状态且配置正确。调用该接口后，系统将启动指定的Notebook实例，用户可开始使用。若用户无权限操作指定实例或Notebook实例未停止，接口将返回相应的错误信息。异常情况包括：若指定的Notebook实例不存在，或启动操作失败，接口将返回相应的错误提示。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartNotebook
        :type request: :class:`huaweicloudsdkmodelarts.v1.StartNotebookRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.StartNotebookResponse`
        """
        http_info = self._start_notebook_http_info(request)
        return self._call_api(**http_info)

    def start_notebook_async_invoker(self, request):
        http_info = self._start_notebook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_notebook_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/notebooks/{id}/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartNotebookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'duration' in local_var_params:
            query_params.append(('duration', local_var_params['duration']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def stop_notebook_async(self, request):
        r"""停止Notebook实例

        停止Notebook实例接口用于停止正在运行的Notebook实例。该接口适用于以下场景：用户需要释放Notebook实例占用的资源或结束当前运行的任务时，可通过此接口停止指定的Notebook实例。使用该接口的前提条件是用户已登录系统并具有操作目标Notebook实例的权限，同时Notebook实例必须处于运行状态。调用该接口后，系统将停止指定的Notebook实例，释放相关资源。若用户无权限操作指定实例或Notebook实例未运行，接口将返回相应的错误信息。异常情况包括：若指定的Notebook实例不存在，或停止操作失败，接口将返回相应的错误提示。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopNotebook
        :type request: :class:`huaweicloudsdkmodelarts.v1.StopNotebookRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.StopNotebookResponse`
        """
        http_info = self._stop_notebook_http_info(request)
        return self._call_api(**http_info)

    def stop_notebook_async_invoker(self, request):
        http_info = self._stop_notebook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_notebook_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/notebooks/{id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopNotebookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_notebook_async(self, request):
        r"""更新Notebook实例

        更新Notebook实例接口用于修改Notebook实例的配置信息，包括名称、描述、规格和镜像等。该接口适用于以下场景：用户需要调整Notebook实例的配置以适应新的需求时，可通过此接口更新实例的详细信息。使用该接口的前提条件是用户已登录系统并具有操作目标Notebook实例的权限，同时Notebook实例必须处于停止状态。调用该接口后，系统将更新指定Notebook实例的配置信息。若用户无权限操作指定实例或Notebook实例未停止，接口将返回相应的错误信息。异常情况包括：若指定的Notebook实例不存在，或更新参数无效，接口将返回相应的错误提示。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateNotebook
        :type request: :class:`huaweicloudsdkmodelarts.v1.UpdateNotebookRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.UpdateNotebookResponse`
        """
        http_info = self._update_notebook_http_info(request)
        return self._call_api(**http_info)

    def update_notebook_async_invoker(self, request):
        http_info = self._update_notebook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_notebook_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/notebooks/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNotebookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_workflow_async(self, request):
        r"""新建Workflow工作流

        创建Workflow工作流。[可参考[如何开发Workflow](https://support.huaweicloud.com/usermanual-standard-modelarts/modelarts_workflow_0292.html)，创建工作流。](tag:hc)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWorkflow
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateWorkflowRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateWorkflowResponse`
        """
        http_info = self._create_workflow_http_info(request)
        return self._call_api(**http_info)

    def create_workflow_async_invoker(self, request):
        http_info = self._create_workflow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_workflow_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workflows",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWorkflowResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_workflow_purchase_pool_async(self, request):
        r"""创建在线服务包

        计费工作流购买资源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWorkflowPurchasePool
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateWorkflowPurchasePoolRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateWorkflowPurchasePoolResponse`
        """
        http_info = self._create_workflow_purchase_pool_http_info(request)
        return self._call_api(**http_info)

    def create_workflow_purchase_pool_async_invoker(self, request):
        http_info = self._create_workflow_purchase_pool_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_workflow_purchase_pool_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workflows/{workflow_id}/service/packages",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWorkflowPurchasePoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_workflow_service_auth_async(self, request):
        r"""在线服务鉴权

        计费工作流在线服务鉴权。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWorkflowServiceAuth
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateWorkflowServiceAuthRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateWorkflowServiceAuthResponse`
        """
        http_info = self._create_workflow_service_auth_http_info(request)
        return self._call_api(**http_info)

    def create_workflow_service_auth_async_invoker(self, request):
        http_info = self._create_workflow_service_auth_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_workflow_service_auth_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workflows/service/auth",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWorkflowServiceAuthResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_workflow_async(self, request):
        r"""删除Workflow工作流

        通过ID删除Workflow工作流。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteWorkflow
        :type request: :class:`huaweicloudsdkmodelarts.v1.DeleteWorkflowRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeleteWorkflowResponse`
        """
        http_info = self._delete_workflow_http_info(request)
        return self._call_api(**http_info)

    def delete_workflow_async_invoker(self, request):
        http_info = self._delete_workflow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_workflow_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/workflows/{workflow_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteWorkflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_workflows_async(self, request):
        r"""获取Workflow工作流列表

        展示Workflow工作流列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWorkflows
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListWorkflowsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListWorkflowsResponse`
        """
        http_info = self._list_workflows_http_info(request)
        return self._call_api(**http_info)

    def list_workflows_async_invoker(self, request):
        http_info = self._list_workflows_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_workflows_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workflows",
            "request_type": request.__class__.__name__,
            "response_type": "ListWorkflowsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'labels' in local_var_params:
            query_params.append(('labels', local_var_params['labels']))
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_by' in local_var_params:
            query_params.append(('sort_by', local_var_params['sort_by']))
        if 'search_type' in local_var_params:
            query_params.append(('search_type', local_var_params['search_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_workflow_async(self, request):
        r"""查询Workflow工作流

        通过ID查询Workflow工作流详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWorkflow
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowWorkflowRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowWorkflowResponse`
        """
        http_info = self._show_workflow_http_info(request)
        return self._call_api(**http_info)

    def show_workflow_async_invoker(self, request):
        http_info = self._show_workflow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_workflow_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workflows/{workflow_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWorkflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

        query_params = []
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_workflow_labels_async(self, request):
        r"""Workflow列表所有标签

        Workflow列表所有标签接口用于获取指定项目下所有工作流的标签信息。
        该接口适用于以下场景：当用户需要了解项目中所有工作流的标签配置，以便进行资源管理和筛选时，可以通过此接口获取标签列表。使用该接口的前提条件是用户已登录并具有查看工作流标签的权限。响应消息体中包含每个工作流的标签信息，如标签键和值。若用户无权限或项目下无工作流，接口将返回相应的错误信息或空列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWorkflowLabels
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowWorkflowLabelsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowWorkflowLabelsResponse`
        """
        http_info = self._show_workflow_labels_http_info(request)
        return self._call_api(**http_info)

    def show_workflow_labels_async_invoker(self, request):
        http_info = self._show_workflow_labels_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_workflow_labels_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workflows/labels",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWorkflowLabelsResponse"
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
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'sort_by' in local_var_params:
            query_params.append(('sort_by', local_var_params['sort_by']))
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_workflows_overview_async(self, request):
        r"""总览Workflow工作流

        获取Workflow工作流统计信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWorkflowsOverview
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowWorkflowsOverviewRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowWorkflowsOverviewResponse`
        """
        http_info = self._show_workflows_overview_http_info(request)
        return self._call_api(**http_info)

    def show_workflows_overview_async_invoker(self, request):
        http_info = self._show_workflows_overview_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_workflows_overview_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workflows/overview",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWorkflowsOverviewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))
        if 'search_type' in local_var_params:
            query_params.append(('search_type', local_var_params['search_type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_workflows_todolist_async(self, request):
        r"""查询Workflow待办事项

        获取Workflow待办列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWorkflowsTodolist
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowWorkflowsTodolistRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowWorkflowsTodolistResponse`
        """
        http_info = self._show_workflows_todolist_http_info(request)
        return self._call_api(**http_info)

    def show_workflows_todolist_async_invoker(self, request):
        http_info = self._show_workflows_todolist_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_workflows_todolist_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workflows/todolist",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWorkflowsTodolistResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_workflow_async(self, request):
        r"""修改Workflow工作流

        更新Workflow工作流信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateWorkflow
        :type request: :class:`huaweicloudsdkmodelarts.v1.UpdateWorkflowRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.UpdateWorkflowResponse`
        """
        http_info = self._update_workflow_http_info(request)
        return self._call_api(**http_info)

    def update_workflow_async_invoker(self, request):
        http_info = self._update_workflow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_workflow_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/workflows/{workflow_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateWorkflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_workflow_execution_async(self, request):
        r"""新建Workflow Execution

        创建Workflow Execution。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWorkflowExecution
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateWorkflowExecutionRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateWorkflowExecutionResponse`
        """
        http_info = self._create_workflow_execution_http_info(request)
        return self._call_api(**http_info)

    def create_workflow_execution_async_invoker(self, request):
        http_info = self._create_workflow_execution_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_workflow_execution_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workflows/{workflow_id}/executions",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWorkflowExecutionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_workflow_executions_actions_async(self, request):
        r"""管理Workflow Execution

        本接口支持对Workflow Execution进行停止或重跑操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWorkflowExecutionsActions
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateWorkflowExecutionsActionsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateWorkflowExecutionsActionsResponse`
        """
        http_info = self._create_workflow_executions_actions_http_info(request)
        return self._call_api(**http_info)

    def create_workflow_executions_actions_async_invoker(self, request):
        http_info = self._create_workflow_executions_actions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_workflow_executions_actions_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workflows/{workflow_id}/executions/{execution_id}/actions",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWorkflowExecutionsActionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']
        if 'execution_id' in local_var_params:
            path_params['execution_id'] = local_var_params['execution_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_workflow_step_executions_actions_async(self, request):
        r"""管理Workflow StepExecution

        本接口支持对Workflow StepExecution进行重试、停止和继续操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWorkflowStepExecutionsActions
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateWorkflowStepExecutionsActionsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateWorkflowStepExecutionsActionsResponse`
        """
        http_info = self._create_workflow_step_executions_actions_http_info(request)
        return self._call_api(**http_info)

    def create_workflow_step_executions_actions_async_invoker(self, request):
        http_info = self._create_workflow_step_executions_actions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_workflow_step_executions_actions_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workflows/{workflow_id}/executions/{execution_id}/step-executions/{step_execution_id}/actions",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWorkflowStepExecutionsActionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']
        if 'execution_id' in local_var_params:
            path_params['execution_id'] = local_var_params['execution_id']
        if 'step_execution_id' in local_var_params:
            path_params['step_execution_id'] = local_var_params['step_execution_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_workflow_execution_async(self, request):
        r"""删除Workflow Execution

        通过ID删除Workflow Execution。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteWorkflowExecution
        :type request: :class:`huaweicloudsdkmodelarts.v1.DeleteWorkflowExecutionRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeleteWorkflowExecutionResponse`
        """
        http_info = self._delete_workflow_execution_http_info(request)
        return self._call_api(**http_info)

    def delete_workflow_execution_async_invoker(self, request):
        http_info = self._delete_workflow_execution_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_workflow_execution_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/workflows/{workflow_id}/executions/{execution_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteWorkflowExecutionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']
        if 'execution_id' in local_var_params:
            path_params['execution_id'] = local_var_params['execution_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_execution_labels_async(self, request):
        r"""获取Workflow Execution列表的所有标签

        获取Workflow Execution列表的所有标签接口用于查询指定工作流执行记录中的所有标签。
        该接口适用于以下场景：当用户需要查看工作流执行记录的标签信息，以便进行分类、筛选或统计时，可以通过此接口获取所有标签的列表。使用该接口的前提条件是用户已登录且具有查看工作流执行记录的权限。接口响应消息体中包含每个标签的详细信息，如标签键和标签值。若用户无权限操作或指定的工作流执行记录不存在，接口将返回相应的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListExecutionLabels
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListExecutionLabelsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListExecutionLabelsResponse`
        """
        http_info = self._list_execution_labels_http_info(request)
        return self._call_api(**http_info)

    def list_execution_labels_async_invoker(self, request):
        http_info = self._list_execution_labels_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_execution_labels_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workflows/{workflow_id}/executions/labels",
            "request_type": request.__class__.__name__,
            "response_type": "ListExecutionLabelsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_workflow_executions_async(self, request):
        r"""获取Execution列表

        查询Workflow下的执行记录列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWorkflowExecutions
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListWorkflowExecutionsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListWorkflowExecutionsResponse`
        """
        http_info = self._list_workflow_executions_http_info(request)
        return self._call_api(**http_info)

    def list_workflow_executions_async_invoker(self, request):
        http_info = self._list_workflow_executions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_workflow_executions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workflows/{workflow_id}/executions",
            "request_type": request.__class__.__name__,
            "response_type": "ListWorkflowExecutionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

        query_params = []
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_by' in local_var_params:
            query_params.append(('sort_by', local_var_params['sort_by']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'labels' in local_var_params:
            query_params.append(('labels', local_var_params['labels']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'scene_id' in local_var_params:
            query_params.append(('scene_id', local_var_params['scene_id']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_workflow_step_execution_async(self, request):
        r"""获取StepExecution列表

        查询指定工作流中各步骤的执行情况。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWorkflowStepExecution
        :type request: :class:`huaweicloudsdkmodelarts.v1.ListWorkflowStepExecutionRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListWorkflowStepExecutionResponse`
        """
        http_info = self._list_workflow_step_execution_http_info(request)
        return self._call_api(**http_info)

    def list_workflow_step_execution_async_invoker(self, request):
        http_info = self._list_workflow_step_execution_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_workflow_step_execution_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workflows/{workflow_id}/step-executions",
            "request_type": request.__class__.__name__,
            "response_type": "ListWorkflowStepExecutionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'sort_by' in local_var_params:
            query_params.append(('sort_by', local_var_params['sort_by']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_workflow_execution_async(self, request):
        r"""查询Workflow Execution

        通过ID查询Workflow Execution详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWorkflowExecution
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowWorkflowExecutionRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowWorkflowExecutionResponse`
        """
        http_info = self._show_workflow_execution_http_info(request)
        return self._call_api(**http_info)

    def show_workflow_execution_async_invoker(self, request):
        http_info = self._show_workflow_execution_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_workflow_execution_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workflows/{workflow_id}/executions/{execution_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWorkflowExecutionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']
        if 'execution_id' in local_var_params:
            path_params['execution_id'] = local_var_params['execution_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_workflow_step_execution_metrics_async(self, request):
        r"""获取Workflow工作流节点度量信息

        获取Workflow工作流节点的度量信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWorkflowStepExecutionMetrics
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowWorkflowStepExecutionMetricsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowWorkflowStepExecutionMetricsResponse`
        """
        http_info = self._show_workflow_step_execution_metrics_http_info(request)
        return self._call_api(**http_info)

    def show_workflow_step_execution_metrics_async_invoker(self, request):
        http_info = self._show_workflow_step_execution_metrics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_workflow_step_execution_metrics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workflows/{workflow_id}/executions/{execution_id}/step-executions/{step_execution_id}/metrics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWorkflowStepExecutionMetricsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']
        if 'execution_id' in local_var_params:
            path_params['execution_id'] = local_var_params['execution_id']
        if 'step_execution_id' in local_var_params:
            path_params['step_execution_id'] = local_var_params['step_execution_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_workflow_execution_async(self, request):
        r"""更新Workflow Execution

        通过ID更新Workflow Exectuion。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateWorkflowExecution
        :type request: :class:`huaweicloudsdkmodelarts.v1.UpdateWorkflowExecutionRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.UpdateWorkflowExecutionResponse`
        """
        http_info = self._update_workflow_execution_http_info(request)
        return self._call_api(**http_info)

    def update_workflow_execution_async_invoker(self, request):
        http_info = self._update_workflow_execution_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_workflow_execution_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/workflows/{workflow_id}/executions/{execution_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateWorkflowExecutionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']
        if 'execution_id' in local_var_params:
            path_params['execution_id'] = local_var_params['execution_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_workflow_schedule_async(self, request):
        r"""创建工作流定时调度

        创建Workflow定时调度。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWorkflowSchedule
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateWorkflowScheduleRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateWorkflowScheduleResponse`
        """
        http_info = self._create_workflow_schedule_http_info(request)
        return self._call_api(**http_info)

    def create_workflow_schedule_async_invoker(self, request):
        http_info = self._create_workflow_schedule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_workflow_schedule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workflows/{workflow_id}/schedules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWorkflowScheduleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_workflow_schedule_id_async(self, request):
        r"""删除工作流定时调度信息

        删除工作流调度信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteWorkflowScheduleId
        :type request: :class:`huaweicloudsdkmodelarts.v1.DeleteWorkflowScheduleIdRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeleteWorkflowScheduleIdResponse`
        """
        http_info = self._delete_workflow_schedule_id_http_info(request)
        return self._call_api(**http_info)

    def delete_workflow_schedule_id_async_invoker(self, request):
        http_info = self._delete_workflow_schedule_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_workflow_schedule_id_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/workflows/{workflow_id}/schedules/{schedule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteWorkflowScheduleIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']
        if 'schedule_id' in local_var_params:
            path_params['schedule_id'] = local_var_params['schedule_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_workflow_schedule_async(self, request):
        r"""查询工作流定时调度详情

        查询工作流调度详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWorkflowSchedule
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowWorkflowScheduleRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowWorkflowScheduleResponse`
        """
        http_info = self._show_workflow_schedule_http_info(request)
        return self._call_api(**http_info)

    def show_workflow_schedule_async_invoker(self, request):
        http_info = self._show_workflow_schedule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_workflow_schedule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workflows/{workflow_id}/schedules/{schedule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWorkflowScheduleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']
        if 'schedule_id' in local_var_params:
            path_params['schedule_id'] = local_var_params['schedule_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_workflow_schedule_list_async(self, request):
        r"""查询工作流定时调度列表

        查询工作流定时调度列表接口用于获取指定项目下所有工作流的定时调度信息。
        该接口适用于以下场景：当用户需要查看项目中所有工作流的定时调度配置，以便进行任务管理和调度优化时，可以通过此接口获取定时调度列表。使用该接口的前提条件是用户已登录并具有查看工作流定时调度的权限。响应消息体中包含每个工作流的定时调度信息，如调度ID、调度时间、状态等。若用户无权限或项目下无工作流定时调度，接口将返回相应的错误信息或空列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWorkflowScheduleList
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowWorkflowScheduleListRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowWorkflowScheduleListResponse`
        """
        http_info = self._show_workflow_schedule_list_http_info(request)
        return self._call_api(**http_info)

    def show_workflow_schedule_list_async_invoker(self, request):
        http_info = self._show_workflow_schedule_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_workflow_schedule_list_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workflows/{workflow_id}/schedules",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWorkflowScheduleListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_workflow_schedule_async(self, request):
        r"""更新工作流定时调度信息

        更新WorkflowSchedule信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateWorkflowSchedule
        :type request: :class:`huaweicloudsdkmodelarts.v1.UpdateWorkflowScheduleRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.UpdateWorkflowScheduleResponse`
        """
        http_info = self._update_workflow_schedule_http_info(request)
        return self._call_api(**http_info)

    def update_workflow_schedule_async_invoker(self, request):
        http_info = self._update_workflow_schedule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_workflow_schedule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/workflows/{workflow_id}/schedules/{schedule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateWorkflowScheduleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']
        if 'schedule_id' in local_var_params:
            path_params['schedule_id'] = local_var_params['schedule_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_workflow_subscriptions_async(self, request):
        r"""新建消息订阅Subscription

        为Workflow工作流添加消息订阅功能。工作流已订阅的事件发生时，会产生消息提醒。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWorkflowSubscriptions
        :type request: :class:`huaweicloudsdkmodelarts.v1.CreateWorkflowSubscriptionsRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateWorkflowSubscriptionsResponse`
        """
        http_info = self._create_workflow_subscriptions_http_info(request)
        return self._call_api(**http_info)

    def create_workflow_subscriptions_async_invoker(self, request):
        http_info = self._create_workflow_subscriptions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_workflow_subscriptions_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/workflows/{workflow_id}/subscriptions",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWorkflowSubscriptionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_workflow_subscription_async(self, request):
        r"""删除消息订阅Subscription

        删除已订阅的消息订阅Subscription。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteWorkflowSubscription
        :type request: :class:`huaweicloudsdkmodelarts.v1.DeleteWorkflowSubscriptionRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeleteWorkflowSubscriptionResponse`
        """
        http_info = self._delete_workflow_subscription_http_info(request)
        return self._call_api(**http_info)

    def delete_workflow_subscription_async_invoker(self, request):
        http_info = self._delete_workflow_subscription_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_workflow_subscription_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/workflows/{workflow_id}/subscriptions/{subscription_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteWorkflowSubscriptionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']
        if 'subscription_id' in local_var_params:
            path_params['subscription_id'] = local_var_params['subscription_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_workflow_subscription_async(self, request):
        r"""查询消息订阅Subscription详情

        查询Workflow工作流已订阅的订阅信息详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWorkflowSubscription
        :type request: :class:`huaweicloudsdkmodelarts.v1.ShowWorkflowSubscriptionRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ShowWorkflowSubscriptionResponse`
        """
        http_info = self._show_workflow_subscription_http_info(request)
        return self._call_api(**http_info)

    def show_workflow_subscription_async_invoker(self, request):
        http_info = self._show_workflow_subscription_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_workflow_subscription_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/workflows/{workflow_id}/subscriptions/{subscription_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWorkflowSubscriptionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']
        if 'subscription_id' in local_var_params:
            path_params['subscription_id'] = local_var_params['subscription_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['ApiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_workflow_subscription_async(self, request):
        r"""更新消息订阅Subscription

        更新Workflow工作流已订阅的订阅信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateWorkflowSubscription
        :type request: :class:`huaweicloudsdkmodelarts.v1.UpdateWorkflowSubscriptionRequest`
        :rtype: :class:`huaweicloudsdkmodelarts.v1.UpdateWorkflowSubscriptionResponse`
        """
        http_info = self._update_workflow_subscription_http_info(request)
        return self._call_api(**http_info)

    def update_workflow_subscription_async_invoker(self, request):
        http_info = self._update_workflow_subscription_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_workflow_subscription_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/workflows/{workflow_id}/subscriptions/{subscription_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateWorkflowSubscriptionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subscription_id' in local_var_params:
            path_params['subscription_id'] = local_var_params['subscription_id']
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = ['ApiTokenAuth']

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
