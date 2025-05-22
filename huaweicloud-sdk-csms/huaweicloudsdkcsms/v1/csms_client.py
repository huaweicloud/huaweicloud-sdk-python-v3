# coding: utf-8

from __future__ import absolute_import

import importlib
import warnings

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest

try:
    from huaweicloudsdkcore.invoker.invoker import SyncInvoker
except ImportError as e:
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcsms'")


class CsmsClient(Client):
    def __init__(self):
        super(CsmsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcsms.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CsmsClient":
                raise TypeError("client type error, support client type is CsmsClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_create_or_delete_tags(self, request):
        r"""批量添加或删除凭据标签

        - 功能介绍：批量添加或删除凭据标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateOrDeleteTags
        :type request: :class:`huaweicloudsdkcsms.v1.BatchCreateOrDeleteTagsRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.BatchCreateOrDeleteTagsResponse`
        """
        http_info = self._batch_create_or_delete_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_or_delete_tags_invoker(self, request):
        http_info = self._batch_create_or_delete_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_or_delete_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/csms/{secret_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateOrDeleteTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_id' in local_var_params:
            path_params['secret_id'] = local_var_params['secret_id']

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

    def batch_import_secrets(self, request):
        r"""批量导入凭据

        批量导入凭据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchImportSecrets
        :type request: :class:`huaweicloudsdkcsms.v1.BatchImportSecretsRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.BatchImportSecretsResponse`
        """
        http_info = self._batch_import_secrets_http_info(request)
        return self._call_api(**http_info)

    def batch_import_secrets_invoker(self, request):
        http_info = self._batch_import_secrets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_import_secrets_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/secrets/batch-import",
            "request_type": request.__class__.__name__,
            "response_type": "BatchImportSecretsResponse"
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

    def check_secrets(self, request):
        r"""检测传入凭据的凭据强度

        检测传入的凭据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckSecrets
        :type request: :class:`huaweicloudsdkcsms.v1.CheckSecretsRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.CheckSecretsResponse`
        """
        http_info = self._check_secrets_http_info(request)
        return self._call_api(**http_info)

    def check_secrets_invoker(self, request):
        http_info = self._check_secrets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_secrets_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/secrets/checker/check",
            "request_type": request.__class__.__name__,
            "response_type": "CheckSecretsResponse"
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

    def create_agency(self, request):
        r"""创建服务委托

        创建服务委托。用于创建凭据管理服务相关委托和函数工作流相关委托。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAgency
        :type request: :class:`huaweicloudsdkcsms.v1.CreateAgencyRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.CreateAgencyResponse`
        """
        http_info = self._create_agency_http_info(request)
        return self._call_api(**http_info)

    def create_agency_invoker(self, request):
        http_info = self._create_agency_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_agency_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/csms/agencies",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAgencyResponse"
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

    def create_grants(self, request):
        r"""授权操作

        授权操作
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateGrants
        :type request: :class:`huaweicloudsdkcsms.v1.CreateGrantsRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.CreateGrantsResponse`
        """
        http_info = self._create_grants_http_info(request)
        return self._call_api(**http_info)

    def create_grants_invoker(self, request):
        http_info = self._create_grants_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_grants_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/csms/grants",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGrantsResponse"
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

    def create_secret(self, request):
        r"""创建凭据

        创建新的凭据，并将凭据值存入凭据的初始版本。
        
        凭据管理服务将凭据值加密后，存储在凭据对象下的版本中。每个版本可与多个凭据版本状态相关联，凭据版本状态用于标识凭据版本处于的阶段，没有版本状态标记的版本视为已弃用，可用凭据管理服务自动删除。
        
        初始版本的状态被标记为SYSCURRENT。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSecret
        :type request: :class:`huaweicloudsdkcsms.v1.CreateSecretRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.CreateSecretResponse`
        """
        http_info = self._create_secret_http_info(request)
        return self._call_api(**http_info)

    def create_secret_invoker(self, request):
        http_info = self._create_secret_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_secret_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/secrets",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSecretResponse"
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

    def create_secret_event(self, request):
        r"""创建事件

        创建事件，事件可配置在一个或多个凭据对象上。当事件为启用状态且包含的基础事件类型在凭据对象上触发时，云服务会将对应的事件通知发送至事件指定的通知主题上。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSecretEvent
        :type request: :class:`huaweicloudsdkcsms.v1.CreateSecretEventRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.CreateSecretEventResponse`
        """
        http_info = self._create_secret_event_http_info(request)
        return self._call_api(**http_info)

    def create_secret_event_invoker(self, request):
        http_info = self._create_secret_event_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_secret_event_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/csms/events",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSecretEventResponse"
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

    def create_secret_tag(self, request):
        r"""添加凭据标签

        添加凭据标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSecretTag
        :type request: :class:`huaweicloudsdkcsms.v1.CreateSecretTagRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.CreateSecretTagResponse`
        """
        http_info = self._create_secret_tag_http_info(request)
        return self._call_api(**http_info)

    def create_secret_tag_invoker(self, request):
        http_info = self._create_secret_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_secret_tag_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/csms/{secret_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSecretTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_id' in local_var_params:
            path_params['secret_id'] = local_var_params['secret_id']

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

    def create_secret_version(self, request):
        r"""创建凭据版本

        在指定的凭据中，创建一个新的凭据版本，用于加密保管新的凭据值。默认情况下，新创建的凭据版本被标记为SYSCURRENT状态，而SYSCURRENT标记的前一个凭据版本被标记为SYSPREVIOUS状态。您可以通过指定VersionStage参数来覆盖默认行为。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSecretVersion
        :type request: :class:`huaweicloudsdkcsms.v1.CreateSecretVersionRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.CreateSecretVersionResponse`
        """
        http_info = self._create_secret_version_http_info(request)
        return self._call_api(**http_info)

    def create_secret_version_invoker(self, request):
        http_info = self._create_secret_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_secret_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/secrets/{secret_name}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSecretVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_name' in local_var_params:
            path_params['secret_name'] = local_var_params['secret_name']

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

    def delete_grant(self, request):
        r"""删除授权

        删除授权
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteGrant
        :type request: :class:`huaweicloudsdkcsms.v1.DeleteGrantRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.DeleteGrantResponse`
        """
        http_info = self._delete_grant_http_info(request)
        return self._call_api(**http_info)

    def delete_grant_invoker(self, request):
        http_info = self._delete_grant_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_grant_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/csms/grants",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGrantResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'grantee_user' in local_var_params:
            query_params.append(('grantee_user', local_var_params['grantee_user']))
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

    def delete_secret(self, request):
        r"""立即删除凭据

        立即删除指定的凭据，且无法恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSecret
        :type request: :class:`huaweicloudsdkcsms.v1.DeleteSecretRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.DeleteSecretResponse`
        """
        http_info = self._delete_secret_http_info(request)
        return self._call_api(**http_info)

    def delete_secret_invoker(self, request):
        http_info = self._delete_secret_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_secret_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/secrets/{secret_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSecretResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_name' in local_var_params:
            path_params['secret_name'] = local_var_params['secret_name']

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

    def delete_secret_event(self, request):
        r"""立即删除事件

        立即删除指定的事件，且无法恢复。如事件存在凭据引用，则无法删除，请先解除关联。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSecretEvent
        :type request: :class:`huaweicloudsdkcsms.v1.DeleteSecretEventRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.DeleteSecretEventResponse`
        """
        http_info = self._delete_secret_event_http_info(request)
        return self._call_api(**http_info)

    def delete_secret_event_invoker(self, request):
        http_info = self._delete_secret_event_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_secret_event_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/csms/events/{event_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSecretEventResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'event_name' in local_var_params:
            path_params['event_name'] = local_var_params['event_name']

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

    def delete_secret_for_schedule(self, request):
        r"""创建凭据的定时删除任务

        指定延迟删除时间，创建删除凭据的定时任务，可设置7~30天的的延迟删除时间。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSecretForSchedule
        :type request: :class:`huaweicloudsdkcsms.v1.DeleteSecretForScheduleRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.DeleteSecretForScheduleResponse`
        """
        http_info = self._delete_secret_for_schedule_http_info(request)
        return self._call_api(**http_info)

    def delete_secret_for_schedule_invoker(self, request):
        http_info = self._delete_secret_for_schedule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_secret_for_schedule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/secrets/{secret_name}/scheduled-deleted-tasks/create",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSecretForScheduleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_name' in local_var_params:
            path_params['secret_name'] = local_var_params['secret_name']

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

    def delete_secret_stage(self, request):
        r"""删除凭据的版本状态

        删除指定的凭据版本状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSecretStage
        :type request: :class:`huaweicloudsdkcsms.v1.DeleteSecretStageRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.DeleteSecretStageResponse`
        """
        http_info = self._delete_secret_stage_http_info(request)
        return self._call_api(**http_info)

    def delete_secret_stage_invoker(self, request):
        http_info = self._delete_secret_stage_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_secret_stage_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/secrets/{secret_name}/stages/{stage_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSecretStageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_name' in local_var_params:
            path_params['secret_name'] = local_var_params['secret_name']
        if 'stage_name' in local_var_params:
            path_params['stage_name'] = local_var_params['stage_name']

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

    def delete_secret_tag(self, request):
        r"""删除凭据标签

        删除凭据标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSecretTag
        :type request: :class:`huaweicloudsdkcsms.v1.DeleteSecretTagRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.DeleteSecretTagResponse`
        """
        http_info = self._delete_secret_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_secret_tag_invoker(self, request):
        http_info = self._delete_secret_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_secret_tag_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/csms/{secret_id}/tags/{key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSecretTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_id' in local_var_params:
            path_params['secret_id'] = local_var_params['secret_id']
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']

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

    def download_secret_blob(self, request):
        r"""下载凭据备份

        下载指定凭据的备份文件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadSecretBlob
        :type request: :class:`huaweicloudsdkcsms.v1.DownloadSecretBlobRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.DownloadSecretBlobResponse`
        """
        http_info = self._download_secret_blob_http_info(request)
        return self._call_api(**http_info)

    def download_secret_blob_invoker(self, request):
        http_info = self._download_secret_blob_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_secret_blob_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/secrets/{secret_name}/backup",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadSecretBlobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_name' in local_var_params:
            path_params['secret_name'] = local_var_params['secret_name']

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

    def generate_random_password(self, request):
        r"""generate_random_password

        生成随机密码
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GenerateRandomPassword
        :type request: :class:`huaweicloudsdkcsms.v1.GenerateRandomPasswordRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.GenerateRandomPasswordResponse`
        """
        http_info = self._generate_random_password_http_info(request)
        return self._call_api(**http_info)

    def generate_random_password_invoker(self, request):
        http_info = self._generate_random_password_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _generate_random_password_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/csms/generate-password",
            "request_type": request.__class__.__name__,
            "response_type": "GenerateRandomPasswordResponse"
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

    def list_grants(self, request):
        r"""授权列表

        授权列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGrants
        :type request: :class:`huaweicloudsdkcsms.v1.ListGrantsRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.ListGrantsResponse`
        """
        http_info = self._list_grants_http_info(request)
        return self._call_api(**http_info)

    def list_grants_invoker(self, request):
        http_info = self._list_grants_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_grants_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/csms/grants",
            "request_type": request.__class__.__name__,
            "response_type": "ListGrantsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

    def list_notification_records(self, request):
        r"""查询已触发的事件通知记录

        查询三个月内所有已触发的事件通知记录。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNotificationRecords
        :type request: :class:`huaweicloudsdkcsms.v1.ListNotificationRecordsRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.ListNotificationRecordsResponse`
        """
        http_info = self._list_notification_records_http_info(request)
        return self._call_api(**http_info)

    def list_notification_records_invoker(self, request):
        http_info = self._list_notification_records_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_notification_records_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/csms/notification-records",
            "request_type": request.__class__.__name__,
            "response_type": "ListNotificationRecordsResponse"
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

    def list_project_secrets_tags(self, request):
        r"""查询项目标签

        查询用户在指定项目下的所有凭据标签集合。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectSecretsTags
        :type request: :class:`huaweicloudsdkcsms.v1.ListProjectSecretsTagsRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.ListProjectSecretsTagsResponse`
        """
        http_info = self._list_project_secrets_tags_http_info(request)
        return self._call_api(**http_info)

    def list_project_secrets_tags_invoker(self, request):
        http_info = self._list_project_secrets_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_project_secrets_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/csms/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectSecretsTagsResponse"
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

    def list_resource_instances(self, request):
        r"""查询凭据实例

        查询凭据实例。通过标签过滤，筛选用户凭据，返回凭据列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceInstances
        :type request: :class:`huaweicloudsdkcsms.v1.ListResourceInstancesRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.ListResourceInstancesResponse`
        """
        http_info = self._list_resource_instances_http_info(request)
        return self._call_api(**http_info)

    def list_resource_instances_invoker(self, request):
        http_info = self._list_resource_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_resource_instances_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/csms/{resource_instances}/action",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_instances' in local_var_params:
            path_params['resource_instances'] = local_var_params['resource_instances']

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

    def list_secret_events(self, request):
        r"""查询事件列表

        查询当前用户在本项目下创建的所有事件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSecretEvents
        :type request: :class:`huaweicloudsdkcsms.v1.ListSecretEventsRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.ListSecretEventsResponse`
        """
        http_info = self._list_secret_events_http_info(request)
        return self._call_api(**http_info)

    def list_secret_events_invoker(self, request):
        http_info = self._list_secret_events_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_secret_events_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/csms/events",
            "request_type": request.__class__.__name__,
            "response_type": "ListSecretEventsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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

    def list_secret_tags(self, request):
        r"""查询凭据标签

        查询凭据标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSecretTags
        :type request: :class:`huaweicloudsdkcsms.v1.ListSecretTagsRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.ListSecretTagsResponse`
        """
        http_info = self._list_secret_tags_http_info(request)
        return self._call_api(**http_info)

    def list_secret_tags_invoker(self, request):
        http_info = self._list_secret_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_secret_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/csms/{secret_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListSecretTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_id' in local_var_params:
            path_params['secret_id'] = local_var_params['secret_id']

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

    def list_secret_task(self, request):
        r"""查询任务列表

        查询任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSecretTask
        :type request: :class:`huaweicloudsdkcsms.v1.ListSecretTaskRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.ListSecretTaskResponse`
        """
        http_info = self._list_secret_task_http_info(request)
        return self._call_api(**http_info)

    def list_secret_task_invoker(self, request):
        http_info = self._list_secret_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_secret_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/csms/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListSecretTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'secret_name' in local_var_params:
            query_params.append(('secret_name', local_var_params['secret_name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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

    def list_secret_versions(self, request):
        r"""查询凭据的版本列表

        查询指定凭据下的版本列表信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSecretVersions
        :type request: :class:`huaweicloudsdkcsms.v1.ListSecretVersionsRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.ListSecretVersionsResponse`
        """
        http_info = self._list_secret_versions_http_info(request)
        return self._call_api(**http_info)

    def list_secret_versions_invoker(self, request):
        http_info = self._list_secret_versions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_secret_versions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/secrets/{secret_name}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "ListSecretVersionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_name' in local_var_params:
            path_params['secret_name'] = local_var_params['secret_name']

        query_params = []
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

    def list_secrets(self, request):
        r"""查询凭据列表

        查询当前用户在本项目下创建的所有凭据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSecrets
        :type request: :class:`huaweicloudsdkcsms.v1.ListSecretsRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.ListSecretsResponse`
        """
        http_info = self._list_secrets_http_info(request)
        return self._call_api(**http_info)

    def list_secrets_invoker(self, request):
        http_info = self._list_secrets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_secrets_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/secrets",
            "request_type": request.__class__.__name__,
            "response_type": "ListSecretsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'event_name' in local_var_params:
            query_params.append(('event_name', local_var_params['event_name']))

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

    def list_users(self, request):
        r"""查询用户列表

        查询用户列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUsers
        :type request: :class:`huaweicloudsdkcsms.v1.ListUsersRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.ListUsersResponse`
        """
        http_info = self._list_users_http_info(request)
        return self._call_api(**http_info)

    def list_users_invoker(self, request):
        http_info = self._list_users_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_users_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/csms/users",
            "request_type": request.__class__.__name__,
            "response_type": "ListUsersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'org_id' in local_var_params:
            query_params.append(('org_id', local_var_params['org_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'user_info' in local_var_params:
            query_params.append(('user_info', local_var_params['user_info']))

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

    def restore_secret(self, request):
        r"""取消凭据的定时删除任务

        取消凭据的定时删除任务，凭据对象恢复可使用状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestoreSecret
        :type request: :class:`huaweicloudsdkcsms.v1.RestoreSecretRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.RestoreSecretResponse`
        """
        http_info = self._restore_secret_http_info(request)
        return self._call_api(**http_info)

    def restore_secret_invoker(self, request):
        http_info = self._restore_secret_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restore_secret_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/secrets/{secret_name}/scheduled-deleted-tasks/cancel",
            "request_type": request.__class__.__name__,
            "response_type": "RestoreSecretResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_name' in local_var_params:
            path_params['secret_name'] = local_var_params['secret_name']

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

    def rotate_secret(self, request):
        r"""轮转凭据

        立即执行轮转凭据。在指定的凭据中，创建一个新的凭据版本，用于加密存储后台随机产生的凭据值。同时将新创建的凭据版本标记为SYSCURRENT状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RotateSecret
        :type request: :class:`huaweicloudsdkcsms.v1.RotateSecretRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.RotateSecretResponse`
        """
        http_info = self._rotate_secret_http_info(request)
        return self._call_api(**http_info)

    def rotate_secret_invoker(self, request):
        http_info = self._rotate_secret_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _rotate_secret_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/secrets/{secret_name}/rotate",
            "request_type": request.__class__.__name__,
            "response_type": "RotateSecretResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_name' in local_var_params:
            path_params['secret_name'] = local_var_params['secret_name']

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

    def show_agency(self, request):
        r"""查看是否有服务委托

        查看是否有服务委托
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAgency
        :type request: :class:`huaweicloudsdkcsms.v1.ShowAgencyRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.ShowAgencyResponse`
        """
        http_info = self._show_agency_http_info(request)
        return self._call_api(**http_info)

    def show_agency_invoker(self, request):
        http_info = self._show_agency_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_agency_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/csms/agencies",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAgencyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'secret_type' in local_var_params:
            query_params.append(('secret_type', local_var_params['secret_type']))

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

    def show_secret(self, request):
        r"""查询凭据

        查询指定凭据的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSecret
        :type request: :class:`huaweicloudsdkcsms.v1.ShowSecretRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.ShowSecretResponse`
        """
        http_info = self._show_secret_http_info(request)
        return self._call_api(**http_info)

    def show_secret_invoker(self, request):
        http_info = self._show_secret_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_secret_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/secrets/{secret_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSecretResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_name' in local_var_params:
            path_params['secret_name'] = local_var_params['secret_name']

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

    def show_secret_event(self, request):
        r"""查询事件

        查询指定事件的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSecretEvent
        :type request: :class:`huaweicloudsdkcsms.v1.ShowSecretEventRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.ShowSecretEventResponse`
        """
        http_info = self._show_secret_event_http_info(request)
        return self._call_api(**http_info)

    def show_secret_event_invoker(self, request):
        http_info = self._show_secret_event_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_secret_event_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/csms/events/{event_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSecretEventResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'event_name' in local_var_params:
            path_params['event_name'] = local_var_params['event_name']

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

    def show_secret_function_templates(self, request):
        r"""获取凭据轮转函数模板

        获取凭据轮转函数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSecretFunctionTemplates
        :type request: :class:`huaweicloudsdkcsms.v1.ShowSecretFunctionTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.ShowSecretFunctionTemplatesResponse`
        """
        http_info = self._show_secret_function_templates_http_info(request)
        return self._call_api(**http_info)

    def show_secret_function_templates_invoker(self, request):
        http_info = self._show_secret_function_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_secret_function_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/csms/function-templates",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSecretFunctionTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'secret_type' in local_var_params:
            query_params.append(('secret_type', local_var_params['secret_type']))
        if 'secret_sub_type' in local_var_params:
            query_params.append(('secret_sub_type', local_var_params['secret_sub_type']))
        if 'engine' in local_var_params:
            query_params.append(('engine', local_var_params['engine']))

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

    def show_secret_stage(self, request):
        r"""查询凭据的版本状态

        查询指定凭据版本状态标记的版本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSecretStage
        :type request: :class:`huaweicloudsdkcsms.v1.ShowSecretStageRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.ShowSecretStageResponse`
        """
        http_info = self._show_secret_stage_http_info(request)
        return self._call_api(**http_info)

    def show_secret_stage_invoker(self, request):
        http_info = self._show_secret_stage_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_secret_stage_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/secrets/{secret_name}/stages/{stage_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSecretStageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_name' in local_var_params:
            path_params['secret_name'] = local_var_params['secret_name']
        if 'stage_name' in local_var_params:
            path_params['stage_name'] = local_var_params['stage_name']

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

    def show_secret_version(self, request):
        r"""查询凭据的版本与凭据值

        查询指定凭据版本的信息和版本中的明文凭据值，只能查询ENABLED状态的凭据。
        通过/v1/{project_id}/secrets/{secret_name}/versions/latest （即将当前接口URL中的{version_id}赋值为latest）可访问凭据最新版本的凭据值。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSecretVersion
        :type request: :class:`huaweicloudsdkcsms.v1.ShowSecretVersionRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.ShowSecretVersionResponse`
        """
        http_info = self._show_secret_version_http_info(request)
        return self._call_api(**http_info)

    def show_secret_version_invoker(self, request):
        http_info = self._show_secret_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_secret_version_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/secrets/{secret_name}/versions/{version_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSecretVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_name' in local_var_params:
            path_params['secret_name'] = local_var_params['secret_name']
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

    def show_secrets_config(self, request):
        r"""获取租户的凭据检测配置

        获取租户的凭据检测配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSecretsConfig
        :type request: :class:`huaweicloudsdkcsms.v1.ShowSecretsConfigRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.ShowSecretsConfigResponse`
        """
        http_info = self._show_secrets_config_http_info(request)
        return self._call_api(**http_info)

    def show_secrets_config_invoker(self, request):
        http_info = self._show_secrets_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_secrets_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/secrets/checker/config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSecretsConfigResponse"
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

    def show_user_detail(self, request):
        r"""获取用户详情

        根据用户id查询用户详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUserDetail
        :type request: :class:`huaweicloudsdkcsms.v1.ShowUserDetailRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.ShowUserDetailResponse`
        """
        http_info = self._show_user_detail_http_info(request)
        return self._call_api(**http_info)

    def show_user_detail_invoker(self, request):
        http_info = self._show_user_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_user_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/csms/users/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUserDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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

    def update_grant(self, request):
        r"""更新授权

        更新授权
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateGrant
        :type request: :class:`huaweicloudsdkcsms.v1.UpdateGrantRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.UpdateGrantResponse`
        """
        http_info = self._update_grant_http_info(request)
        return self._call_api(**http_info)

    def update_grant_invoker(self, request):
        http_info = self._update_grant_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_grant_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/csms/grants",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGrantResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))

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

    def update_secret(self, request):
        r"""更新凭据

        更新指定凭据的元数据信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSecret
        :type request: :class:`huaweicloudsdkcsms.v1.UpdateSecretRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.UpdateSecretResponse`
        """
        http_info = self._update_secret_http_info(request)
        return self._call_api(**http_info)

    def update_secret_invoker(self, request):
        http_info = self._update_secret_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_secret_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/secrets/{secret_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSecretResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_name' in local_var_params:
            path_params['secret_name'] = local_var_params['secret_name']

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

    def update_secret_event(self, request):
        r"""更新事件

        更新指定事件的元数据信息。支持更新的元数据包含事件启用状态、基础类型列表、通知主题。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSecretEvent
        :type request: :class:`huaweicloudsdkcsms.v1.UpdateSecretEventRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.UpdateSecretEventResponse`
        """
        http_info = self._update_secret_event_http_info(request)
        return self._call_api(**http_info)

    def update_secret_event_invoker(self, request):
        http_info = self._update_secret_event_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_secret_event_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/csms/events/{event_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSecretEventResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'event_name' in local_var_params:
            path_params['event_name'] = local_var_params['event_name']

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

    def update_secret_stage(self, request):
        r"""更新凭据的版本状态

        更新凭据的版本状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSecretStage
        :type request: :class:`huaweicloudsdkcsms.v1.UpdateSecretStageRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.UpdateSecretStageResponse`
        """
        http_info = self._update_secret_stage_http_info(request)
        return self._call_api(**http_info)

    def update_secret_stage_invoker(self, request):
        http_info = self._update_secret_stage_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_secret_stage_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/secrets/{secret_name}/stages/{stage_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSecretStageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_name' in local_var_params:
            path_params['secret_name'] = local_var_params['secret_name']
        if 'stage_name' in local_var_params:
            path_params['stage_name'] = local_var_params['stage_name']

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

    def update_secrets_config(self, request):
        r"""更改获取租户的凭据检测配置

        更改获取租户的凭据检测配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSecretsConfig
        :type request: :class:`huaweicloudsdkcsms.v1.UpdateSecretsConfigRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.UpdateSecretsConfigResponse`
        """
        http_info = self._update_secrets_config_http_info(request)
        return self._call_api(**http_info)

    def update_secrets_config_invoker(self, request):
        http_info = self._update_secrets_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_secrets_config_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/secrets/checker/config",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSecretsConfigResponse"
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

    def update_user_password(self, request):
        r"""修改用户密码

        修改用户密码
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateUserPassword
        :type request: :class:`huaweicloudsdkcsms.v1.UpdateUserPasswordRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.UpdateUserPasswordResponse`
        """
        http_info = self._update_user_password_http_info(request)
        return self._call_api(**http_info)

    def update_user_password_invoker(self, request):
        http_info = self._update_user_password_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_user_password_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/csms/users/change-password",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateUserPasswordResponse"
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

    def update_version(self, request):
        r"""更新凭据版本

        当前支持更新指定凭据版本的有效期，只能更新ENABLED状态的凭据。在关联订阅的事件包含“版本过期”基础事件类型时，每次更新版本有效期后仅会触发一次事件通知。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateVersion
        :type request: :class:`huaweicloudsdkcsms.v1.UpdateVersionRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.UpdateVersionResponse`
        """
        http_info = self._update_version_http_info(request)
        return self._call_api(**http_info)

    def update_version_invoker(self, request):
        http_info = self._update_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_version_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/secrets/{secret_name}/versions/{version_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_name' in local_var_params:
            path_params['secret_name'] = local_var_params['secret_name']
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
            ['application/json;charset=UTF-8'])

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

    def upload_secret_blob(self, request):
        r"""恢复凭据对象

        通过上传凭据备份文件，恢复凭据对象
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadSecretBlob
        :type request: :class:`huaweicloudsdkcsms.v1.UploadSecretBlobRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.UploadSecretBlobResponse`
        """
        http_info = self._upload_secret_blob_http_info(request)
        return self._call_api(**http_info)

    def upload_secret_blob_invoker(self, request):
        http_info = self._upload_secret_blob_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upload_secret_blob_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/secrets/restore",
            "request_type": request.__class__.__name__,
            "response_type": "UploadSecretBlobResponse"
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
