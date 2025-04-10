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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkmsgsms'")


class MsgsmsClient(Client):
    def __init__(self):
        super(MsgsmsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkmsgsms.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "MsgsmsClient":
                raise TypeError("client type error, support client type is MsgsmsClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_app(self, request):
        r"""创建短信应用

        该接口用于用户创建应用信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateApp
        :type request: :class:`huaweicloudsdkmsgsms.v2.CreateAppRequest`
        :rtype: :class:`huaweicloudsdkmsgsms.v2.CreateAppResponse`
        """
        http_info = self._create_app_http_info(request)
        return self._call_api(**http_info)

    def create_app_invoker(self, request):
        http_info = self._create_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_app_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/msgsms/apps",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAppResponse"
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

    def list_app_details(self, request):
        r"""查询短信应用

        该接口用于用户查询已创建的应用信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAppDetails
        :type request: :class:`huaweicloudsdkmsgsms.v2.ListAppDetailsRequest`
        :rtype: :class:`huaweicloudsdkmsgsms.v2.ListAppDetailsResponse`
        """
        http_info = self._list_app_details_http_info(request)
        return self._call_api(**http_info)

    def list_app_details_invoker(self, request):
        http_info = self._list_app_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_app_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/msgsms/apps",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
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

    def show_app(self, request):
        r"""获取应用详情

        该接口用于用户查询应用详情信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApp
        :type request: :class:`huaweicloudsdkmsgsms.v2.ShowAppRequest`
        :rtype: :class:`huaweicloudsdkmsgsms.v2.ShowAppResponse`
        """
        http_info = self._show_app_http_info(request)
        return self._call_api(**http_info)

    def show_app_invoker(self, request):
        http_info = self._show_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_app_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/msgsms/apps/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppResponse"
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

    def show_app_count(self, request):
        r"""查询应用数量

        该接口用于用户查询应用使用的数量信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAppCount
        :type request: :class:`huaweicloudsdkmsgsms.v2.ShowAppCountRequest`
        :rtype: :class:`huaweicloudsdkmsgsms.v2.ShowAppCountResponse`
        """
        http_info = self._show_app_count_http_info(request)
        return self._call_api(**http_info)

    def show_app_count_invoker(self, request):
        http_info = self._show_app_count_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_app_count_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/msgsms/apps-count",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppCountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))

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

    def update_app(self, request):
        r"""修改短信应用

        该接口用于用户修改应用信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateApp
        :type request: :class:`huaweicloudsdkmsgsms.v2.UpdateAppRequest`
        :rtype: :class:`huaweicloudsdkmsgsms.v2.UpdateAppResponse`
        """
        http_info = self._update_app_http_info(request)
        return self._call_api(**http_info)

    def update_app_invoker(self, request):
        http_info = self._update_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_app_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/msgsms/apps/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAppResponse"
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

    def create_signature(self, request):
        r"""创建短信签名

        该接口用于用户创建签名。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSignature
        :type request: :class:`huaweicloudsdkmsgsms.v2.CreateSignatureRequest`
        :rtype: :class:`huaweicloudsdkmsgsms.v2.CreateSignatureResponse`
        """
        http_info = self._create_signature_http_info(request)
        return self._call_api(**http_info)

    def create_signature_invoker(self, request):
        http_info = self._create_signature_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_signature_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/msgsms/signatures",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSignatureResponse"
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

    def delete_signature(self, request):
        r"""删除短信签名

        该接口用于用户删除已创建的签名信息息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSignature
        :type request: :class:`huaweicloudsdkmsgsms.v2.DeleteSignatureRequest`
        :rtype: :class:`huaweicloudsdkmsgsms.v2.DeleteSignatureResponse`
        """
        http_info = self._delete_signature_http_info(request)
        return self._call_api(**http_info)

    def delete_signature_invoker(self, request):
        http_info = self._delete_signature_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_signature_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/msgsms/signatures/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSignatureResponse"
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

    def enable_signature(self, request):
        r"""申请激活签名

        该接口用于用户申请激活签名信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableSignature
        :type request: :class:`huaweicloudsdkmsgsms.v2.EnableSignatureRequest`
        :rtype: :class:`huaweicloudsdkmsgsms.v2.EnableSignatureResponse`
        """
        http_info = self._enable_signature_http_info(request)
        return self._call_api(**http_info)

    def enable_signature_invoker(self, request):
        http_info = self._enable_signature_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_signature_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/msgsms/signatures/{id}/active",
            "request_type": request.__class__.__name__,
            "response_type": "EnableSignatureResponse"
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

    def list_signature_details(self, request):
        r"""查询签名信息

        该接口用于用户查询已创建的短信签名信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSignatureDetails
        :type request: :class:`huaweicloudsdkmsgsms.v2.ListSignatureDetailsRequest`
        :rtype: :class:`huaweicloudsdkmsgsms.v2.ListSignatureDetailsResponse`
        """
        http_info = self._list_signature_details_http_info(request)
        return self._call_api(**http_info)

    def list_signature_details_invoker(self, request):
        http_info = self._list_signature_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_signature_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/msgsms/signatures",
            "request_type": request.__class__.__name__,
            "response_type": "ListSignatureDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'signature_id' in local_var_params:
            query_params.append(('signature_id', local_var_params['signature_id']))
        if 'signature_name' in local_var_params:
            query_params.append(('signature_name', local_var_params['signature_name']))
        if 'signature_type' in local_var_params:
            query_params.append(('signature_type', local_var_params['signature_type']))
        if 'site' in local_var_params:
            query_params.append(('site', local_var_params['site']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
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

    def show_signature(self, request):
        r"""获取签名详情

        该接口用于用户查询签名详情信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSignature
        :type request: :class:`huaweicloudsdkmsgsms.v2.ShowSignatureRequest`
        :rtype: :class:`huaweicloudsdkmsgsms.v2.ShowSignatureResponse`
        """
        http_info = self._show_signature_http_info(request)
        return self._call_api(**http_info)

    def show_signature_invoker(self, request):
        http_info = self._show_signature_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_signature_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/msgsms/signatures/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSignatureResponse"
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

    def show_signature_file(self, request):
        r"""查询申请文件

        该接口用于用户查询上传的文件信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSignatureFile
        :type request: :class:`huaweicloudsdkmsgsms.v2.ShowSignatureFileRequest`
        :rtype: :class:`huaweicloudsdkmsgsms.v2.ShowSignatureFileResponse`
        """
        http_info = self._show_signature_file_http_info(request)
        return self._call_api(**http_info)

    def show_signature_file_invoker(self, request):
        http_info = self._show_signature_file_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_signature_file_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/msgsms/upload-files",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSignatureFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'file_id' in local_var_params:
            query_params.append(('file_id', local_var_params['file_id']))

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

    def update_signature(self, request):
        r"""修改短信签名

        该接口用于用户更新签名信息，目前仅支持审核不通过的短信签名重新修改。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSignature
        :type request: :class:`huaweicloudsdkmsgsms.v2.UpdateSignatureRequest`
        :rtype: :class:`huaweicloudsdkmsgsms.v2.UpdateSignatureResponse`
        """
        http_info = self._update_signature_http_info(request)
        return self._call_api(**http_info)

    def update_signature_invoker(self, request):
        http_info = self._update_signature_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_signature_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/msgsms/signatures/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSignatureResponse"
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

    def upload_signature_file(self, request):
        r"""上传申请文件

        该接口用于用户上传文件信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadSignatureFile
        :type request: :class:`huaweicloudsdkmsgsms.v2.UploadSignatureFileRequest`
        :rtype: :class:`huaweicloudsdkmsgsms.v2.UploadSignatureFileResponse`
        """
        http_info = self._upload_signature_file_http_info(request)
        return self._call_api(**http_info)

    def upload_signature_file_invoker(self, request):
        http_info = self._upload_signature_file_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upload_signature_file_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/msgsms/upload-files",
            "request_type": request.__class__.__name__,
            "response_type": "UploadSignatureFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'file_desc' in local_var_params:
            query_params.append(('file_desc', local_var_params['file_desc']))

        header_params = {}

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

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

    def create_template(self, request):
        r"""创建短信模板

        该接口用于用户创建模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTemplate
        :type request: :class:`huaweicloudsdkmsgsms.v2.CreateTemplateRequest`
        :rtype: :class:`huaweicloudsdkmsgsms.v2.CreateTemplateResponse`
        """
        http_info = self._create_template_http_info(request)
        return self._call_api(**http_info)

    def create_template_invoker(self, request):
        http_info = self._create_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_template_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/msgsms/templates",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTemplateResponse"
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

    def delete_template(self, request):
        r"""删除短信模板

        该接口用于用户删除已创建的模板信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTemplate
        :type request: :class:`huaweicloudsdkmsgsms.v2.DeleteTemplateRequest`
        :rtype: :class:`huaweicloudsdkmsgsms.v2.DeleteTemplateResponse`
        """
        http_info = self._delete_template_http_info(request)
        return self._call_api(**http_info)

    def delete_template_invoker(self, request):
        http_info = self._delete_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_template_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/msgsms/templates/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTemplateResponse"
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

    def list_send_country_details(self, request):
        r"""查询发送国家

        该接口用于用户查询短信发送的国家信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSendCountryDetails
        :type request: :class:`huaweicloudsdkmsgsms.v2.ListSendCountryDetailsRequest`
        :rtype: :class:`huaweicloudsdkmsgsms.v2.ListSendCountryDetailsResponse`
        """
        http_info = self._list_send_country_details_http_info(request)
        return self._call_api(**http_info)

    def list_send_country_details_invoker(self, request):
        http_info = self._list_send_country_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_send_country_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/msgsms/country",
            "request_type": request.__class__.__name__,
            "response_type": "ListSendCountryDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'country_name_en' in local_var_params:
            query_params.append(('country_name_en', local_var_params['country_name_en']))
        if 'country_name_zh' in local_var_params:
            query_params.append(('country_name_zh', local_var_params['country_name_zh']))

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

    def list_template_details(self, request):
        r"""查询短信模板

        该接口用于用户查询已创建的模板信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTemplateDetails
        :type request: :class:`huaweicloudsdkmsgsms.v2.ListTemplateDetailsRequest`
        :rtype: :class:`huaweicloudsdkmsgsms.v2.ListTemplateDetailsResponse`
        """
        http_info = self._list_template_details_http_info(request)
        return self._call_api(**http_info)

    def list_template_details_invoker(self, request):
        http_info = self._list_template_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_template_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/msgsms/templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListTemplateDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'app_key' in local_var_params:
            query_params.append(('app_key', local_var_params['app_key']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'flow_status' in local_var_params:
            query_params.append(('flow_status', local_var_params['flow_status']))
        if 'has_variable' in local_var_params:
            query_params.append(('has_variable', local_var_params['has_variable']))
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
        if 'sign_name' in local_var_params:
            query_params.append(('sign_name', local_var_params['sign_name']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))
        if 'template_name' in local_var_params:
            query_params.append(('template_name', local_var_params['template_name']))
        if 'template_type' in local_var_params:
            query_params.append(('template_type', local_var_params['template_type']))

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

    def list_template_varilable_details(self, request):
        r"""查询模板变量

        该接口用于用户查询模板参数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTemplateVarilableDetails
        :type request: :class:`huaweicloudsdkmsgsms.v2.ListTemplateVarilableDetailsRequest`
        :rtype: :class:`huaweicloudsdkmsgsms.v2.ListTemplateVarilableDetailsResponse`
        """
        http_info = self._list_template_varilable_details_http_info(request)
        return self._call_api(**http_info)

    def list_template_varilable_details_invoker(self, request):
        http_info = self._list_template_varilable_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_template_varilable_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/msgsms/templates/{id}/varilable",
            "request_type": request.__class__.__name__,
            "response_type": "ListTemplateVarilableDetailsResponse"
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

    def show_template(self, request):
        r"""获取模板详情

        该接口用于用户查询已创建的模板详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTemplate
        :type request: :class:`huaweicloudsdkmsgsms.v2.ShowTemplateRequest`
        :rtype: :class:`huaweicloudsdkmsgsms.v2.ShowTemplateResponse`
        """
        http_info = self._show_template_http_info(request)
        return self._call_api(**http_info)

    def show_template_invoker(self, request):
        http_info = self._show_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/msgsms/templates/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTemplateResponse"
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

    def update_template(self, request):
        r"""修改短信模板

        该接口用于用户修改模板信息，目前仅支持审核不通过的短信模板重新修改
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTemplate
        :type request: :class:`huaweicloudsdkmsgsms.v2.UpdateTemplateRequest`
        :rtype: :class:`huaweicloudsdkmsgsms.v2.UpdateTemplateResponse`
        """
        http_info = self._update_template_http_info(request)
        return self._call_api(**http_info)

    def update_template_invoker(self, request):
        http_info = self._update_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_template_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/msgsms/templates/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTemplateResponse"
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
