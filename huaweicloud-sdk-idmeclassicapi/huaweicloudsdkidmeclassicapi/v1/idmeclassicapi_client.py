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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkidmeclassicapi'")


class IDMEClassicAPIClient(Client):
    def __init__(self):
        super(IDMEClassicAPIClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkidmeclassicapi.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "IDMEClassicAPIClient":
                raise TypeError("client type error, support client type is IDMEClassicAPIClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def show_batch_checkin_using_post(self, request):
        """XDM_批量检入VersionModel

        根据主对象ID批量检入版本对象，小版本升版。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBatchCheckinUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchCheckinUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchCheckinUsingPostResponse`
        """
        http_info = self._show_batch_checkin_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_batch_checkin_using_post_invoker(self, request):
        http_info = self._show_batch_checkin_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_batch_checkin_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchCheckin",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBatchCheckinUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_batch_checkout_and_update_using_post(self, request):
        """XDM_批量检出并更新VersionModel

        根据主对象ID批量检出对象并根据传入字段批量更新版本对象。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBatchCheckoutAndUpdateUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchCheckoutAndUpdateUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchCheckoutAndUpdateUsingPostResponse`
        """
        http_info = self._show_batch_checkout_and_update_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_batch_checkout_and_update_using_post_invoker(self, request):
        http_info = self._show_batch_checkout_and_update_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_batch_checkout_and_update_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchCheckoutAndUpdate",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBatchCheckoutAndUpdateUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_batch_checkout_using_post(self, request):
        """XDM_批量检出VersionModel

        根据主对象ID批量检出版本对象。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBatchCheckoutUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchCheckoutUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchCheckoutUsingPostResponse`
        """
        http_info = self._show_batch_checkout_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_batch_checkout_using_post_invoker(self, request):
        http_info = self._show_batch_checkout_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_batch_checkout_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchCheckout",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBatchCheckoutUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_batch_create_using_post(self, request):
        """批量创建实例

        批量创建指定数据模型的数据实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBatchCreateUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchCreateUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchCreateUsingPostResponse`
        """
        http_info = self._show_batch_create_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_batch_create_using_post_invoker(self, request):
        http_info = self._show_batch_create_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_batch_create_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchCreate",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBatchCreateUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_batch_delete_branch_using_post(self, request):
        """XDM_批量删除VersionModel最新分支版本下所有小版本

        根据主对象ID&amp;业务版本列表，批量删除最新分支版本下的所有小版本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBatchDeleteBranchUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchDeleteBranchUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchDeleteBranchUsingPostResponse`
        """
        http_info = self._show_batch_delete_branch_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_batch_delete_branch_using_post_invoker(self, request):
        http_info = self._show_batch_delete_branch_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_batch_delete_branch_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchDeleteBranch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBatchDeleteBranchUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_batch_delete_using_post(self, request):
        """批量删除实例

        根据数据实例的唯一编码，批量删除指定数据模型中的多个数据实例。
        
        请您谨慎使用删除操作，实例删除后将无法恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBatchDeleteUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchDeleteUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchDeleteUsingPostResponse`
        """
        http_info = self._show_batch_delete_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_batch_delete_using_post_invoker(self, request):
        http_info = self._show_batch_delete_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_batch_delete_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchDelete",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBatchDeleteUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_batch_get_using_post(self, request):
        """批量查询实例

        根据多个数据实例的唯一编码，批量查询实例的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBatchGetUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchGetUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchGetUsingPostResponse`
        """
        http_info = self._show_batch_get_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_batch_get_using_post_invoker(self, request):
        http_info = self._show_batch_get_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_batch_get_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchGet",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBatchGetUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_batch_logical_delete_branch_using_post(self, request):
        """XDM_批量软删除VersionModel最新分支版本下所有小版本

        批量软删除最新分支版本下的所有小版本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBatchLogicalDeleteBranchUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchLogicalDeleteBranchUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchLogicalDeleteBranchUsingPostResponse`
        """
        http_info = self._show_batch_logical_delete_branch_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_batch_logical_delete_branch_using_post_invoker(self, request):
        http_info = self._show_batch_logical_delete_branch_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_batch_logical_delete_branch_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchLogicalDeleteBranch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBatchLogicalDeleteBranchUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_batch_logical_delete_using_post(self, request):
        """批量软删除实例

        根据数据实例的唯一编码，批量软删除指定数据模型中的多个数据实例。
        
        通过此接口进行删除操作时，系统会将当前删除的实例转存至XDM应用的XDMLogicDeleteData内置模型中。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBatchLogicalDeleteUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchLogicalDeleteUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchLogicalDeleteUsingPostResponse`
        """
        http_info = self._show_batch_logical_delete_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_batch_logical_delete_using_post_invoker(self, request):
        http_info = self._show_batch_logical_delete_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_batch_logical_delete_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchLogicalDelete",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBatchLogicalDeleteUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_batch_revise_and_update_using_post(self, request):
        """XDM_批量修订且更新VersionModel。

        根据主对象ID批量修订对象并根据传入字段更新主对象+版本对象。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBatchReviseAndUpdateUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchReviseAndUpdateUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchReviseAndUpdateUsingPostResponse`
        """
        http_info = self._show_batch_revise_and_update_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_batch_revise_and_update_using_post_invoker(self, request):
        http_info = self._show_batch_revise_and_update_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_batch_revise_and_update_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchReviseAndUpdate",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBatchReviseAndUpdateUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_batch_revise_using_post(self, request):
        """XDM_批量修订VersionModel。

        根据主对象ID批量修订对象。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBatchReviseUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchReviseUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchReviseUsingPostResponse`
        """
        http_info = self._show_batch_revise_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_batch_revise_using_post_invoker(self, request):
        http_info = self._show_batch_revise_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_batch_revise_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchRevise",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBatchReviseUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_batch_undo_checkout_by_admin_using_post(self, request):
        """XDM_管理员批量撤销检出VersionModel

        管理员根据主对象ID批量撤销检出版本对象。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBatchUndoCheckoutByAdminUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchUndoCheckoutByAdminUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchUndoCheckoutByAdminUsingPostResponse`
        """
        http_info = self._show_batch_undo_checkout_by_admin_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_batch_undo_checkout_by_admin_using_post_invoker(self, request):
        http_info = self._show_batch_undo_checkout_by_admin_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_batch_undo_checkout_by_admin_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchUndoCheckoutByAdmin",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBatchUndoCheckoutByAdminUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_batch_undo_checkout_using_post(self, request):
        """XDM_批量撤销检出VersionModel

        根据主对象ID批量撤销检出版本对象。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBatchUndoCheckoutUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchUndoCheckoutUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchUndoCheckoutUsingPostResponse`
        """
        http_info = self._show_batch_undo_checkout_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_batch_undo_checkout_using_post_invoker(self, request):
        http_info = self._show_batch_undo_checkout_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_batch_undo_checkout_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchUndoCheckout",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBatchUndoCheckoutUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_batch_update_and_checkin_using_post(self, request):
        """XDM_批量更新并检入VersionModel

        根据传入字段批量更新版本对象并根据主对象ID批量检入对象。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBatchUpdateAndCheckinUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchUpdateAndCheckinUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchUpdateAndCheckinUsingPostResponse`
        """
        http_info = self._show_batch_update_and_checkin_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_batch_update_and_checkin_using_post_invoker(self, request):
        http_info = self._show_batch_update_and_checkin_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_batch_update_and_checkin_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchUpdateAndCheckin",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBatchUpdateAndCheckinUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_batch_update_by_admin_using_post(self, request):
        """XDM_管理员批量更新VersionModel指定属性

        以管理员身份批量更新指定版本实例上的基础信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBatchUpdateByAdminUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchUpdateByAdminUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchUpdateByAdminUsingPostResponse`
        """
        http_info = self._show_batch_update_by_admin_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_batch_update_by_admin_using_post_invoker(self, request):
        http_info = self._show_batch_update_by_admin_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_batch_update_by_admin_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchUpdateByAdmin",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBatchUpdateByAdminUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_batch_update_using_post(self, request):
        """批量更新实例

        批量更新指定数据模型中的多个实例数据。如果某个实例的唯一编码不存在，该实例不做任何更新操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBatchUpdateUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchUpdateUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchUpdateUsingPostResponse`
        """
        http_info = self._show_batch_update_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_batch_update_using_post_invoker(self, request):
        http_info = self._show_batch_update_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_batch_update_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchUpdate",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBatchUpdateUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_batch_update_version_using_post(self, request):
        """XDM_批量升版最新版本对象VersionModel的版本号

        根据ID批量升版最新版本对象数据的版本号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBatchUpdateVersionUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchUpdateVersionUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowBatchUpdateVersionUsingPostResponse`
        """
        http_info = self._show_batch_update_version_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_batch_update_version_using_post_invoker(self, request):
        http_info = self._show_batch_update_version_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_batch_update_version_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchUpdateVersion",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBatchUpdateVersionUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_checkin_using_post(self, request):
        """XDM_检入VersionModel

        根据主对象ID检入版本对象，按照设置的规则生成新的业务版本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCheckinUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowCheckinUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowCheckinUsingPostResponse`
        """
        http_info = self._show_checkin_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_checkin_using_post_invoker(self, request):
        http_info = self._show_checkin_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_checkin_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/checkin",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCheckinUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_checkout_and_update_using_post(self, request):
        """XDM_检出并更新VersionModel

        根据主对象ID检出对象并根据传入字段更新版本对象。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCheckoutAndUpdateUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowCheckoutAndUpdateUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowCheckoutAndUpdateUsingPostResponse`
        """
        http_info = self._show_checkout_and_update_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_checkout_and_update_using_post_invoker(self, request):
        http_info = self._show_checkout_and_update_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_checkout_and_update_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/checkoutAndUpdate",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCheckoutAndUpdateUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_checkout_using_post(self, request):
        """XDM_检出VersionModel

        根据主对象ID检出版本对象，复制生成一条新的版本记录且状态为已检出。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCheckoutUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowCheckoutUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowCheckoutUsingPostResponse`
        """
        http_info = self._show_checkout_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_checkout_using_post_invoker(self, request):
        http_info = self._show_checkout_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_checkout_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/checkout",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCheckoutUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_compare_business_version_using_post(self, request):
        """XDM_VersionModel业务版本对比

        根据主对象id，输入版本号（大版本+小版本）进行版本属性与关系对比。（建议使用新的接口instance-attrs-comparison和\\ instance-relation-comparison比较属性和关系）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCompareBusinessVersionUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowCompareBusinessVersionUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowCompareBusinessVersionUsingPostResponse`
        """
        http_info = self._show_compare_business_version_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_compare_business_version_using_post_invoker(self, request):
        http_info = self._show_compare_business_version_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_compare_business_version_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/compareBusinessVersion",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCompareBusinessVersionUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_count_using_post(self, request):
        """统计指定数据模型的实例总数

        根据指定的查询条件，统计指定数据模型中的实例总数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCountUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowCountUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowCountUsingPostResponse`
        """
        http_info = self._show_count_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_count_using_post_invoker(self, request):
        http_info = self._show_count_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_count_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/count",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCountUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_create_using_post(self, request):
        """创建实例

        创建指定数据模型的数据实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCreateUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowCreateUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowCreateUsingPostResponse`
        """
        http_info = self._show_create_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_create_using_post_invoker(self, request):
        http_info = self._show_create_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_create_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/create",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCreateUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_delete_branch_using_post(self, request):
        """XDM_删除VersionModel最新分支版本下所有小版本

        根据masterid&amp;version删除最新大版本下的所有小版本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeleteBranchUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowDeleteBranchUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowDeleteBranchUsingPostResponse`
        """
        http_info = self._show_delete_branch_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_delete_branch_using_post_invoker(self, request):
        http_info = self._show_delete_branch_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_delete_branch_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/deleteBranch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeleteBranchUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_delete_by_condition_using_post(self, request):
        """根据指定条件删除实例

        通过此接口，删除指定条件查询返回的实例。
        
        请您谨慎使用删除操作，实例删除后将无法恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeleteByConditionUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowDeleteByConditionUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowDeleteByConditionUsingPostResponse`
        """
        http_info = self._show_delete_by_condition_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_delete_by_condition_using_post_invoker(self, request):
        http_info = self._show_delete_by_condition_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_delete_by_condition_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/deleteByCondition",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeleteByConditionUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_delete_latest_version_using_post(self, request):
        """XDM_删除VersionModel最新分支的最新版本

        根据主对象ID入参，删除最新分支的最新版本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeleteLatestVersionUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowDeleteLatestVersionUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowDeleteLatestVersionUsingPostResponse`
        """
        http_info = self._show_delete_latest_version_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_delete_latest_version_using_post_invoker(self, request):
        http_info = self._show_delete_latest_version_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_delete_latest_version_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/deleteLatestVersion",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeleteLatestVersionUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_delete_using_post(self, request):
        """删除实例

        根据数据实例的唯一编码，删除指定数据模型中的一个数据实例。
        
        请您谨慎使用删除操作，实例删除后将无法恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeleteUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowDeleteUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowDeleteUsingPostResponse`
        """
        http_info = self._show_delete_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_delete_using_post_invoker(self, request):
        http_info = self._show_delete_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_delete_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/delete",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeleteUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_find_using_post(self, request):
        """分页查询实例

        分页查询指定数据模型中的所有实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFindUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowFindUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowFindUsingPostResponse`
        """
        http_info = self._show_find_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_find_using_post_invoker(self, request):
        http_info = self._show_find_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_find_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/find/{pageSizePath}/{curPagePath}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFindUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']
        if 'page_size_path' in local_var_params:
            path_params['pageSizePath'] = local_var_params['page_size_path']
        if 'cur_page_path' in local_var_params:
            path_params['curPagePath'] = local_var_params['cur_page_path']

        query_params = []
        if 'cur_page' in local_var_params:
            query_params.append(('curPage', local_var_params['cur_page']))
        if 'end_index' in local_var_params:
            query_params.append(('endIndex', local_var_params['end_index']))
        if 'max_page_size' in local_var_params:
            query_params.append(('maxPageSize', local_var_params['max_page_size']))
        if 'page_size' in local_var_params:
            query_params.append(('pageSize', local_var_params['page_size']))
        if 'start_index' in local_var_params:
            query_params.append(('startIndex', local_var_params['start_index']))
        if 'total_pages' in local_var_params:
            query_params.append(('totalPages', local_var_params['total_pages']))
        if 'total_rows' in local_var_params:
            query_params.append(('totalRows', local_var_params['total_rows']))

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

    def show_get_all_versions_using_post(self, request):
        """XDM_获取VersionModel版本列表

        根据主对象ID，获取全量版本以及对应版本对象list属性。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGetAllVersionsUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowGetAllVersionsUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowGetAllVersionsUsingPostResponse`
        """
        http_info = self._show_get_all_versions_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_get_all_versions_using_post_invoker(self, request):
        http_info = self._show_get_all_versions_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_get_all_versions_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/getAllVersions/{pageSizePath}/{curPagePath}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGetAllVersionsUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']
        if 'cur_page_path' in local_var_params:
            path_params['curPagePath'] = local_var_params['cur_page_path']
        if 'page_size_path' in local_var_params:
            path_params['pageSizePath'] = local_var_params['page_size_path']

        query_params = []
        if 'cur_page' in local_var_params:
            query_params.append(('curPage', local_var_params['cur_page']))
        if 'end_index' in local_var_params:
            query_params.append(('endIndex', local_var_params['end_index']))
        if 'max_page_size' in local_var_params:
            query_params.append(('maxPageSize', local_var_params['max_page_size']))
        if 'page_size' in local_var_params:
            query_params.append(('pageSize', local_var_params['page_size']))
        if 'start_index' in local_var_params:
            query_params.append(('startIndex', local_var_params['start_index']))
        if 'total_pages' in local_var_params:
            query_params.append(('totalPages', local_var_params['total_pages']))
        if 'total_rows' in local_var_params:
            query_params.append(('totalRows', local_var_params['total_rows']))

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

    def show_get_by_unique_key_using_post(self, request):
        """根据唯一键为“是”的属性查询实例

        当数据模型中存在“唯一键”为“是”的属性时，可根据该属性查询实例数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGetByUniqueKeyUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowGetByUniqueKeyUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowGetByUniqueKeyUsingPostResponse`
        """
        http_info = self._show_get_by_unique_key_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_get_by_unique_key_using_post_invoker(self, request):
        http_info = self._show_get_by_unique_key_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_get_by_unique_key_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/{getUniqueFieldMethod}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGetByUniqueKeyUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']
        if 'get_unique_field_method' in local_var_params:
            path_params['getUniqueFieldMethod'] = local_var_params['get_unique_field_method']

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

    def show_get_using_post(self, request):
        """查询实例

        根据一个数据实例的唯一编码，查询实例的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGetUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowGetUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowGetUsingPostResponse`
        """
        http_info = self._show_get_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_get_using_post_invoker(self, request):
        http_info = self._show_get_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_get_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/get",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGetUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_get_version_by_master_using_post(self, request):
        """XDM_获取VersionModel对应版本信息

        根据Masterid和版本号和小版本号，返回对应版本属性，小版本号为空则返回最新小版本属性。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGetVersionByMasterUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowGetVersionByMasterUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowGetVersionByMasterUsingPostResponse`
        """
        http_info = self._show_get_version_by_master_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_get_version_by_master_using_post_invoker(self, request):
        http_info = self._show_get_version_by_master_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_get_version_by_master_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/getVersionByMaster",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGetVersionByMasterUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_list_using_post(self, request):
        """查询实例的基础属性

        根据查询条件分页返回模型基本属性信息且不级联查询（不支持扩展属性作为查询条件）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowListUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowListUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowListUsingPostResponse`
        """
        http_info = self._show_list_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_list_using_post_invoker(self, request):
        http_info = self._show_list_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_list_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/list/{pageSizePath}/{curPagePath}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowListUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']
        if 'page_size_path' in local_var_params:
            path_params['pageSizePath'] = local_var_params['page_size_path']
        if 'cur_page_path' in local_var_params:
            path_params['curPagePath'] = local_var_params['cur_page_path']

        query_params = []
        if 'cur_page' in local_var_params:
            query_params.append(('curPage', local_var_params['cur_page']))
        if 'end_index' in local_var_params:
            query_params.append(('endIndex', local_var_params['end_index']))
        if 'max_page_size' in local_var_params:
            query_params.append(('maxPageSize', local_var_params['max_page_size']))
        if 'page_size' in local_var_params:
            query_params.append(('pageSize', local_var_params['page_size']))
        if 'start_index' in local_var_params:
            query_params.append(('startIndex', local_var_params['start_index']))
        if 'total_pages' in local_var_params:
            query_params.append(('totalPages', local_var_params['total_pages']))
        if 'total_rows' in local_var_params:
            query_params.append(('totalRows', local_var_params['total_rows']))

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

    def show_logical_delete_branch_using_post(self, request):
        """XDM_软删除VersionModel最新分支版本下所有小版本

        软删除最新分支版本下的所有小版本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLogicalDeleteBranchUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowLogicalDeleteBranchUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowLogicalDeleteBranchUsingPostResponse`
        """
        http_info = self._show_logical_delete_branch_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_logical_delete_branch_using_post_invoker(self, request):
        http_info = self._show_logical_delete_branch_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_logical_delete_branch_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/logicalDeleteBranch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLogicalDeleteBranchUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_logical_delete_by_condition_using_post(self, request):
        """根据指定条件软删除实例

        通过此接口，软删除指定条件查询返回的实例。
        
        通过此接口进行删除操作时，系统会将当前删除的实例转存至XDM应用的XDMLogicDeleteData内置模型中。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLogicalDeleteByConditionUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowLogicalDeleteByConditionUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowLogicalDeleteByConditionUsingPostResponse`
        """
        http_info = self._show_logical_delete_by_condition_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_logical_delete_by_condition_using_post_invoker(self, request):
        http_info = self._show_logical_delete_by_condition_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_logical_delete_by_condition_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/logicalDeleteByCondition",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLogicalDeleteByConditionUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_logical_delete_latest_version_using_post(self, request):
        """XDM_软删除VersionModel最新分支的最新版本

        根据主对象ID入参，软删最新分支的最新版本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLogicalDeleteLatestVersionUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowLogicalDeleteLatestVersionUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowLogicalDeleteLatestVersionUsingPostResponse`
        """
        http_info = self._show_logical_delete_latest_version_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_logical_delete_latest_version_using_post_invoker(self, request):
        http_info = self._show_logical_delete_latest_version_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_logical_delete_latest_version_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/logicalDeleteLatestVersion",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLogicalDeleteLatestVersionUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_logical_delete_using_post(self, request):
        """软删除实例

        根据数据实例的唯一编码，软删除指定数据模型中的一个数据实例。
        
        通过此接口进行删除操作时，系统会将当前删除的实例转存至XDM应用的XDMLogicDeleteData内置模型中。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLogicalDeleteUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowLogicalDeleteUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowLogicalDeleteUsingPostResponse`
        """
        http_info = self._show_logical_delete_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_logical_delete_using_post_invoker(self, request):
        http_info = self._show_logical_delete_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_logical_delete_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/logicalDelete",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLogicalDeleteUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_query_using_post(self, request):
        """根据“列表属性”为“是”的属性查询实例

        当数据模型中存在“列表属性”为“是”的属性时，可通过此接口查询数据模型中的实例数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowQueryUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowQueryUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowQueryUsingPostResponse`
        """
        http_info = self._show_query_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_query_using_post_invoker(self, request):
        http_info = self._show_query_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_query_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/query/{pageSizePath}/{curPagePath}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowQueryUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']
        if 'page_size_path' in local_var_params:
            path_params['pageSizePath'] = local_var_params['page_size_path']
        if 'cur_page_path' in local_var_params:
            path_params['curPagePath'] = local_var_params['cur_page_path']

        query_params = []
        if 'cur_page' in local_var_params:
            query_params.append(('curPage', local_var_params['cur_page']))
        if 'end_index' in local_var_params:
            query_params.append(('endIndex', local_var_params['end_index']))
        if 'max_page_size' in local_var_params:
            query_params.append(('maxPageSize', local_var_params['max_page_size']))
        if 'page_size' in local_var_params:
            query_params.append(('pageSize', local_var_params['page_size']))
        if 'start_index' in local_var_params:
            query_params.append(('startIndex', local_var_params['start_index']))
        if 'total_pages' in local_var_params:
            query_params.append(('totalPages', local_var_params['total_pages']))
        if 'total_rows' in local_var_params:
            query_params.append(('totalRows', local_var_params['total_rows']))

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

    def show_revise_and_update_using_post(self, request):
        """XDM_修订且更新VersionModel。

        根据主对象ID修订对象并根据传入字段更新主对象+版本对象。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowReviseAndUpdateUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowReviseAndUpdateUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowReviseAndUpdateUsingPostResponse`
        """
        http_info = self._show_revise_and_update_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_revise_and_update_using_post_invoker(self, request):
        http_info = self._show_revise_and_update_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_revise_and_update_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/reviseAndUpdate",
            "request_type": request.__class__.__name__,
            "response_type": "ShowReviseAndUpdateUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_revise_using_post(self, request):
        """XDM_修订VersionModel

        根据主对象ID修订对象，按照设置的规则生成新的业务版本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowReviseUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowReviseUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowReviseUsingPostResponse`
        """
        http_info = self._show_revise_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_revise_using_post_invoker(self, request):
        http_info = self._show_revise_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_revise_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/revise",
            "request_type": request.__class__.__name__,
            "response_type": "ShowReviseUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_save_all_using_post(self, request):
        """根据唯一键为“是”的属性更新实例数据

        当数据模型中存在“唯一键”为“是”的属性时，可根据该属性的英文名称更新该数据模型中实例的所有字段数据。如果更新的实例不存在，系统将自动创建该实例数据。
        
        调用此接口时，建议传入该实例的所有字段信息。如果未传入某个字段，该字段的数据将更新为空值。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSaveAllUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowSaveAllUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowSaveAllUsingPostResponse`
        """
        http_info = self._show_save_all_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_save_all_using_post_invoker(self, request):
        http_info = self._show_save_all_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_save_all_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/saveAll",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSaveAllUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_save_as_using_post(self, request):
        """另存版本对象的实例数据

        版本对象的另存为接口（saveAs）用于创建一条与原版本对象实例数据相同的数据实例。该实例数据会完全复制原实例现有的数据，包括与其关联的主对象和分支对象，且新实例数据的版本号从初始值开始计算。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSaveAsUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowSaveAsUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowSaveAsUsingPostResponse`
        """
        http_info = self._show_save_as_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_save_as_using_post_invoker(self, request):
        http_info = self._show_save_as_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_save_as_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/saveAs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSaveAsUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_save_using_post(self, request):
        """根据唯一键为“是”的属性更新实例的指定字段

        当数据模型中存在“唯一键”为“是”的属性时，可根据该属性的英文名称更新该数据模型中实例的指定字段数据。
        
        如果更新的实例不存在，系统将自动创建该实例数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSaveUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowSaveUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowSaveUsingPostResponse`
        """
        http_info = self._show_save_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_save_using_post_invoker(self, request):
        http_info = self._show_save_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_save_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/save",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSaveUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_select_using_post(self, request):
        """查询实例的指定属性

        根据查询条件及指定属性分页返回（不支持扩展属性作为选定属性列)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSelectUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowSelectUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowSelectUsingPostResponse`
        """
        http_info = self._show_select_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_select_using_post_invoker(self, request):
        http_info = self._show_select_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_select_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/select/{pageSizePath}/{curPagePath}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSelectUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']
        if 'page_size_path' in local_var_params:
            path_params['pageSizePath'] = local_var_params['page_size_path']
        if 'cur_page_path' in local_var_params:
            path_params['curPagePath'] = local_var_params['cur_page_path']

        query_params = []
        if 'cur_page' in local_var_params:
            query_params.append(('curPage', local_var_params['cur_page']))
        if 'end_index' in local_var_params:
            query_params.append(('endIndex', local_var_params['end_index']))
        if 'max_page_size' in local_var_params:
            query_params.append(('maxPageSize', local_var_params['max_page_size']))
        if 'page_size' in local_var_params:
            query_params.append(('pageSize', local_var_params['page_size']))
        if 'start_index' in local_var_params:
            query_params.append(('startIndex', local_var_params['start_index']))
        if 'total_pages' in local_var_params:
            query_params.append(('totalPages', local_var_params['total_pages']))
        if 'total_rows' in local_var_params:
            query_params.append(('totalRows', local_var_params['total_rows']))

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

    def show_statics_using_post(self, request):
        """查询指定数据模型的实例统计信息

        根据指定函数，统计指定数据模型的实例信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowStaticsUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowStaticsUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowStaticsUsingPostResponse`
        """
        http_info = self._show_statics_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_statics_using_post_invoker(self, request):
        http_info = self._show_statics_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_statics_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/statics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowStaticsUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_undo_checkout_by_admin_using_post(self, request):
        """XDM_管理员撤销检出VersionModel

        管理员根据主对象ID撤销检出版本对象。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUndoCheckoutByAdminUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowUndoCheckoutByAdminUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowUndoCheckoutByAdminUsingPostResponse`
        """
        http_info = self._show_undo_checkout_by_admin_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_undo_checkout_by_admin_using_post_invoker(self, request):
        http_info = self._show_undo_checkout_by_admin_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_undo_checkout_by_admin_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/undoCheckoutByAdmin",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUndoCheckoutByAdminUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_undo_checkout_using_post(self, request):
        """XDM_撤销检出VersionModel

        根据主对象ID撤销检出版本对象，删除新的版本记录且状态为已检入。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUndoCheckoutUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowUndoCheckoutUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowUndoCheckoutUsingPostResponse`
        """
        http_info = self._show_undo_checkout_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_undo_checkout_using_post_invoker(self, request):
        http_info = self._show_undo_checkout_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_undo_checkout_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/undoCheckout",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUndoCheckoutUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_update_and_checkin_using_post(self, request):
        """XDM_更新并检入VersionModel

        根据传入字段更新版本对象并根据主对象ID检入对象。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUpdateAndCheckinUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowUpdateAndCheckinUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowUpdateAndCheckinUsingPostResponse`
        """
        http_info = self._show_update_and_checkin_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_update_and_checkin_using_post_invoker(self, request):
        http_info = self._show_update_and_checkin_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_update_and_checkin_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/updateAndCheckin",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUpdateAndCheckinUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_update_by_admin_using_post(self, request):
        """XDM_管理员更新对象VersionModel指定属性

        以管理员身份更新指定版本实例上的基础信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUpdateByAdminUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowUpdateByAdminUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowUpdateByAdminUsingPostResponse`
        """
        http_info = self._show_update_by_admin_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_update_by_admin_using_post_invoker(self, request):
        http_info = self._show_update_by_admin_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_update_by_admin_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/updateByAdmin",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUpdateByAdminUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_update_by_condition_using_post(self, request):
        """根据指定条件更新实例

        根据指定条件更新指定模型的实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUpdateByConditionUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowUpdateByConditionUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowUpdateByConditionUsingPostResponse`
        """
        http_info = self._show_update_by_condition_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_update_by_condition_using_post_invoker(self, request):
        http_info = self._show_update_by_condition_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_update_by_condition_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/updateByCondition",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUpdateByConditionUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_update_using_post(self, request):
        """更新实例

        更新指定数据模型中的一个实例数据。如果实例的唯一编码不存在，则不做任何更新操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUpdateUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowUpdateUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowUpdateUsingPostResponse`
        """
        http_info = self._show_update_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_update_using_post_invoker(self, request):
        http_info = self._show_update_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_update_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/update",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUpdateUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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
