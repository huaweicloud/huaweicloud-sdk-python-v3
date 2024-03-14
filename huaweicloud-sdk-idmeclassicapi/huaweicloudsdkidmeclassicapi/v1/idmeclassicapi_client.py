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

    def batch_checkin(self, request):
        """批量检入M-V模型数据实例

        根据主对象ID批量检入M-V模型数据实例。已检入的数据实例会生成一个新的迭代版本，并将数据存储至系统中。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCheckin
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchCheckinRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchCheckinResponse`
        """
        http_info = self._batch_checkin_http_info(request)
        return self._call_api(**http_info)

    def batch_checkin_invoker(self, request):
        http_info = self._batch_checkin_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_checkin_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchCheckin",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCheckinResponse"
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

    def batch_checkout(self, request):
        """批量检出M-V模型数据实例

        根据主对象ID批量检出M-V模型数据实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCheckout
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchCheckoutRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchCheckoutResponse`
        """
        http_info = self._batch_checkout_http_info(request)
        return self._call_api(**http_info)

    def batch_checkout_invoker(self, request):
        http_info = self._batch_checkout_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_checkout_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchCheckout",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCheckoutResponse"
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

    def batch_checkout_and_update(self, request):
        """批量检出并更新M-V模型

        根据主对象ID批量检出并更新M-V模型数据实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCheckoutAndUpdate
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchCheckoutAndUpdateRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchCheckoutAndUpdateResponse`
        """
        http_info = self._batch_checkout_and_update_http_info(request)
        return self._call_api(**http_info)

    def batch_checkout_and_update_invoker(self, request):
        http_info = self._batch_checkout_and_update_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_checkout_and_update_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchCheckoutAndUpdate",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCheckoutAndUpdateResponse"
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

    def batch_checkout_undo(self, request):
        """批量撤销检出M-V模型数据实例

        通过此接口批量撤销指定M-V模型实例的检出，将实例数据批量还原至检出前的内容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCheckoutUndo
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchCheckoutUndoRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchCheckoutUndoResponse`
        """
        http_info = self._batch_checkout_undo_http_info(request)
        return self._call_api(**http_info)

    def batch_checkout_undo_invoker(self, request):
        http_info = self._batch_checkout_undo_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_checkout_undo_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchUndoCheckout",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCheckoutUndoResponse"
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

    def batch_checkout_undo_by_admin(self, request):
        """管理员批量撤销检出M-V模型数据实例

        管理员通过此接口批量撤销指定M-V模型实例的检出，将实例数据批量还原至检出前的内容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCheckoutUndoByAdmin
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchCheckoutUndoByAdminRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchCheckoutUndoByAdminResponse`
        """
        http_info = self._batch_checkout_undo_by_admin_http_info(request)
        return self._call_api(**http_info)

    def batch_checkout_undo_by_admin_invoker(self, request):
        http_info = self._batch_checkout_undo_by_admin_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_checkout_undo_by_admin_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchUndoCheckoutByAdmin",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCheckoutUndoByAdminResponse"
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

    def batch_create_using_post(self, request):
        """批量创建实例

        批量创建指定数据模型的数据实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchCreateUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchCreateUsingPostResponse`
        """
        http_info = self._batch_create_using_post_http_info(request)
        return self._call_api(**http_info)

    def batch_create_using_post_invoker(self, request):
        http_info = self._batch_create_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchCreate",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateUsingPostResponse"
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

    def batch_delete_branch(self, request):
        """批量删除最新大版本下的所有小版本

        根据主对象ID和父模型ID，批量软删除最新大版本下的所有小版本。请您谨慎使用删除操作，删除后该数据将无法恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteBranch
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchDeleteBranchRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchDeleteBranchResponse`
        """
        http_info = self._batch_delete_branch_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_branch_invoker(self, request):
        http_info = self._batch_delete_branch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_branch_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchDeleteBranch",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteBranchResponse"
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

    def batch_delete_logical_branch(self, request):
        """批量软删除最新大版本下的所有小版本

        根据主对象ID，批量软删除最新大版本下的所有小版本。通过此接口进行删除操作时，系统会将当前删除的实例数据转存至XDM应用的XDMLogicDeleteData内置模型中。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteLogicalBranch
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchDeleteLogicalBranchRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchDeleteLogicalBranchResponse`
        """
        http_info = self._batch_delete_logical_branch_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_logical_branch_invoker(self, request):
        http_info = self._batch_delete_logical_branch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_logical_branch_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchLogicalDeleteBranch",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteLogicalBranchResponse"
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

    def batch_delete_logical_using_post(self, request):
        """批量软删除实例

        根据数据实例的唯一编码，批量软删除指定数据模型中的多个数据实例。
        
        通过此接口进行删除操作时，系统会将当前删除的实例转存至XDM应用的XDMLogicDeleteData内置模型中。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteLogicalUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchDeleteLogicalUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchDeleteLogicalUsingPostResponse`
        """
        http_info = self._batch_delete_logical_using_post_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_logical_using_post_invoker(self, request):
        http_info = self._batch_delete_logical_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_logical_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchLogicalDelete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteLogicalUsingPostResponse"
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

    def batch_delete_using_post(self, request):
        """批量删除实例

        根据数据实例的唯一编码，批量删除指定数据模型中的多个数据实例。
        
        请您谨慎使用删除操作，实例删除后将无法恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchDeleteUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchDeleteUsingPostResponse`
        """
        http_info = self._batch_delete_using_post_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_using_post_invoker(self, request):
        http_info = self._batch_delete_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchDelete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteUsingPostResponse"
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

    def batch_execute_revise(self, request):
        """批量修订M-V模型数据实例

        通过此接口批量修订指定M-V模型实例。修订后，实例的“version.修订版本”会更新为新的修订版本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchExecuteRevise
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchExecuteReviseRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchExecuteReviseResponse`
        """
        http_info = self._batch_execute_revise_http_info(request)
        return self._call_api(**http_info)

    def batch_execute_revise_invoker(self, request):
        http_info = self._batch_execute_revise_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_execute_revise_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchRevise",
            "request_type": request.__class__.__name__,
            "response_type": "BatchExecuteReviseResponse"
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

    def batch_show_get_using_post(self, request):
        """批量查询实例

        根据多个数据实例的唯一编码，批量查询实例的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchShowGetUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchShowGetUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchShowGetUsingPostResponse`
        """
        http_info = self._batch_show_get_using_post_http_info(request)
        return self._call_api(**http_info)

    def batch_show_get_using_post_invoker(self, request):
        http_info = self._batch_show_get_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_show_get_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchGet",
            "request_type": request.__class__.__name__,
            "response_type": "BatchShowGetUsingPostResponse"
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

    def batch_update_and_checkin(self, request):
        """批量更新并检入M-V模型数据实例

        通过此接口批量更新指定M-V模型实例，并检入这些实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateAndCheckin
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchUpdateAndCheckinRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchUpdateAndCheckinResponse`
        """
        http_info = self._batch_update_and_checkin_http_info(request)
        return self._call_api(**http_info)

    def batch_update_and_checkin_invoker(self, request):
        http_info = self._batch_update_and_checkin_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_update_and_checkin_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchUpdateAndCheckin",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateAndCheckinResponse"
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

    def batch_update_and_revise(self, request):
        """批量修订并更新M-V模型数据实例

        根据主对象ID批量修订并更新M-V模型数据实例，即修订后实例的“version.修订版本”更新为新的修订版本，并同时更新该实例的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateAndRevise
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchUpdateAndReviseRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchUpdateAndReviseResponse`
        """
        http_info = self._batch_update_and_revise_http_info(request)
        return self._call_api(**http_info)

    def batch_update_and_revise_invoker(self, request):
        http_info = self._batch_update_and_revise_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_update_and_revise_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchReviseAndUpdate",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateAndReviseResponse"
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

    def batch_update_by_admin(self, request):
        """管理员批量更新M-V模型数据实例

        管理员通过此接口批量更新指定M-V模型的指定实例数据。如果某个实例的唯一编码不存在，则不做任何更新操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateByAdmin
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchUpdateByAdminRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchUpdateByAdminResponse`
        """
        http_info = self._batch_update_by_admin_http_info(request)
        return self._call_api(**http_info)

    def batch_update_by_admin_invoker(self, request):
        http_info = self._batch_update_by_admin_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_update_by_admin_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchUpdateByAdmin",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateByAdminResponse"
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

    def batch_update_using_post(self, request):
        """批量更新实例

        批量更新指定数据模型中的多个实例数据。如果某个实例的唯一编码不存在，该实例不做任何更新操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchUpdateUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchUpdateUsingPostResponse`
        """
        http_info = self._batch_update_using_post_http_info(request)
        return self._call_api(**http_info)

    def batch_update_using_post_invoker(self, request):
        http_info = self._batch_update_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_update_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchUpdate",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateUsingPostResponse"
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

    def batch_update_version(self, request):
        """批量升级M-V模型实例的版本号

        根据M-V模型实体的唯一编码，批量将该实体下实例的版本号更新至最新版本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateVersion
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchUpdateVersionRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchUpdateVersionResponse`
        """
        http_info = self._batch_update_version_http_info(request)
        return self._call_api(**http_info)

    def batch_update_version_invoker(self, request):
        http_info = self._batch_update_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_update_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchUpdateVersion",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateVersionResponse"
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

    def checkin(self, request):
        """检入M-V模型数据实例

        根据主对象ID检入M-V模型数据实例。已检入的数据实例会生成一个新的迭代版本，并将数据存储至系统中。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for Checkin
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.CheckinRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.CheckinResponse`
        """
        http_info = self._checkin_http_info(request)
        return self._call_api(**http_info)

    def checkin_invoker(self, request):
        http_info = self._checkin_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _checkin_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/checkin",
            "request_type": request.__class__.__name__,
            "response_type": "CheckinResponse"
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

    def checkout(self, request):
        """检出M-V模型数据实例

        根据主对象ID检出M-V模型数据实例，检出后会生成一个新的数据实例，该实例会完全复制原实例现有的信息，且状态修改为已检出。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for Checkout
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.CheckoutRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.CheckoutResponse`
        """
        http_info = self._checkout_http_info(request)
        return self._call_api(**http_info)

    def checkout_invoker(self, request):
        http_info = self._checkout_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _checkout_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/checkout",
            "request_type": request.__class__.__name__,
            "response_type": "CheckoutResponse"
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

    def checkout_and_update(self, request):
        """检出并更新M-V模型

        根据主对象ID检出并更新M-V模型数据实例，即检出后生成一个新的数据实例的同时，更新该新实例的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckoutAndUpdate
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.CheckoutAndUpdateRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.CheckoutAndUpdateResponse`
        """
        http_info = self._checkout_and_update_http_info(request)
        return self._call_api(**http_info)

    def checkout_and_update_invoker(self, request):
        http_info = self._checkout_and_update_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _checkout_and_update_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/checkoutAndUpdate",
            "request_type": request.__class__.__name__,
            "response_type": "CheckoutAndUpdateResponse"
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

    def checkout_undo(self, request):
        """撤销检出M-V模型数据实例

        通过此接口撤销指定M-V模型实例的检出，将实例数据还原至检出前的内容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckoutUndo
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.CheckoutUndoRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.CheckoutUndoResponse`
        """
        http_info = self._checkout_undo_http_info(request)
        return self._call_api(**http_info)

    def checkout_undo_invoker(self, request):
        http_info = self._checkout_undo_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _checkout_undo_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/undoCheckout",
            "request_type": request.__class__.__name__,
            "response_type": "CheckoutUndoResponse"
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

    def checkout_undo_by_admin(self, request):
        """管理员撤销检出M-V模型数据实例

        管理员通过此接口撤销指定M-V模型实例的检出，将实例数据还原至检出前的内容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckoutUndoByAdmin
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.CheckoutUndoByAdminRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.CheckoutUndoByAdminResponse`
        """
        http_info = self._checkout_undo_by_admin_http_info(request)
        return self._call_api(**http_info)

    def checkout_undo_by_admin_invoker(self, request):
        http_info = self._checkout_undo_by_admin_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _checkout_undo_by_admin_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/undoCheckoutByAdmin",
            "request_type": request.__class__.__name__,
            "response_type": "CheckoutUndoByAdminResponse"
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

    def compare_business_version(self, request):
        """对比M-V模型实例

        通过此接口可以对比某个M-V模型数据实例的不同版本的属性和关系。建议使用数据建模引擎（xDM Foundation，简称xDM-F）新增的差异对比功能，即使用instance-attrs-comparison和instance-relation-comparison接口，更多内容可在应用运行态的“数据服务管理 &gt; 全量数据服务 &gt; 系统管理API &gt; 属性对比API”中查看。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CompareBusinessVersion
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.CompareBusinessVersionRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.CompareBusinessVersionResponse`
        """
        http_info = self._compare_business_version_http_info(request)
        return self._call_api(**http_info)

    def compare_business_version_invoker(self, request):
        http_info = self._compare_business_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _compare_business_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/compareBusinessVersion",
            "request_type": request.__class__.__name__,
            "response_type": "CompareBusinessVersionResponse"
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

    def count_using_post(self, request):
        """统计指定数据模型的实例总数

        根据指定的查询条件，统计指定数据模型中的实例总数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.CountUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.CountUsingPostResponse`
        """
        http_info = self._count_using_post_http_info(request)
        return self._call_api(**http_info)

    def count_using_post_invoker(self, request):
        http_info = self._count_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _count_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/count",
            "request_type": request.__class__.__name__,
            "response_type": "CountUsingPostResponse"
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

    def create_using_post(self, request):
        """创建实例

        创建指定数据模型的数据实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.CreateUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.CreateUsingPostResponse`
        """
        http_info = self._create_using_post_http_info(request)
        return self._call_api(**http_info)

    def create_using_post_invoker(self, request):
        http_info = self._create_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateUsingPostResponse"
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

    def delete_branch(self, request):
        """删除最新大版本下的所有小版本

        根据父模型ID和版本对象，删除最新大版本下的所有小版本。请您谨慎使用删除操作，删除后该数据将无法恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBranch
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteBranchRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteBranchResponse`
        """
        http_info = self._delete_branch_http_info(request)
        return self._call_api(**http_info)

    def delete_branch_invoker(self, request):
        http_info = self._delete_branch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_branch_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/deleteBranch",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBranchResponse"
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

    def delete_by_condition_using_post(self, request):
        """根据指定条件删除实例

        通过此接口，删除指定条件查询返回的实例。
        
        请您谨慎使用删除操作，实例删除后将无法恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteByConditionUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteByConditionUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteByConditionUsingPostResponse`
        """
        http_info = self._delete_by_condition_using_post_http_info(request)
        return self._call_api(**http_info)

    def delete_by_condition_using_post_invoker(self, request):
        http_info = self._delete_by_condition_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_by_condition_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/deleteByCondition",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteByConditionUsingPostResponse"
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

    def delete_latest_version(self, request):
        """删除版本对象下最新分支的最新版本实例数据

        根据主对象ID，删除版本对象下最新分支的最新版本实例数据。请您谨慎使用删除操作，删除后该数据将无法恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteLatestVersion
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteLatestVersionRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteLatestVersionResponse`
        """
        http_info = self._delete_latest_version_http_info(request)
        return self._call_api(**http_info)

    def delete_latest_version_invoker(self, request):
        http_info = self._delete_latest_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_latest_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/deleteLatestVersion",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLatestVersionResponse"
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

    def delete_logical_branch(self, request):
        """软删除M-V模型实例下最新分支的所有小版本数据

        根据父模型ID和版本对象，软删除M-V模型实例下最新分支的所有小版本数据。通过此接口进行删除操作时，系统会将当前删除的实例数据转存至XDM应用的XDMLogicDeleteData内置模型中。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteLogicalBranch
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteLogicalBranchRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteLogicalBranchResponse`
        """
        http_info = self._delete_logical_branch_http_info(request)
        return self._call_api(**http_info)

    def delete_logical_branch_invoker(self, request):
        http_info = self._delete_logical_branch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_logical_branch_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/logicalDeleteBranch",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLogicalBranchResponse"
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

    def delete_logical_latest_version(self, request):
        """软删除版本对象下最新分支的最新版本实例数据

        根据主对象ID，软删除版本对象下最新分支的最新版本实例数据。通过此接口进行删除操作时，系统会将当前删除的实例数据转存至XDM应用的XDMLogicDeleteData内置模型中。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteLogicalLatestVersion
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteLogicalLatestVersionRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteLogicalLatestVersionResponse`
        """
        http_info = self._delete_logical_latest_version_http_info(request)
        return self._call_api(**http_info)

    def delete_logical_latest_version_invoker(self, request):
        http_info = self._delete_logical_latest_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_logical_latest_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/logicalDeleteLatestVersion",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLogicalLatestVersionResponse"
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

    def delete_using_post(self, request):
        """删除实例

        根据数据实例的唯一编码，删除指定数据模型中的一个数据实例。
        
        请您谨慎使用删除操作，实例删除后将无法恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteUsingPostResponse`
        """
        http_info = self._delete_using_post_http_info(request)
        return self._call_api(**http_info)

    def delete_using_post_invoker(self, request):
        http_info = self._delete_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteUsingPostResponse"
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

    def execute_revise(self, request):
        """修订M-V模型数据实例

        通过此接口修订指定M-V模型实例。修订后，该实例的“version.修订版本”会更新为新的修订版本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteRevise
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ExecuteReviseRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ExecuteReviseResponse`
        """
        http_info = self._execute_revise_http_info(request)
        return self._call_api(**http_info)

    def execute_revise_invoker(self, request):
        http_info = self._execute_revise_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_revise_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/revise",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteReviseResponse"
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

    def list_all_versions(self, request):
        """获取指定M-V模型实例的版本列表

        根据主对象ID，获取对应M-V模型实例的所有版本信息（包含对应版本下的属性信息）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAllVersions
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ListAllVersionsRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ListAllVersionsResponse`
        """
        http_info = self._list_all_versions_http_info(request)
        return self._call_api(**http_info)

    def list_all_versions_invoker(self, request):
        http_info = self._list_all_versions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_all_versions_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/getAllVersions/{pageSizePath}/{curPagePath}",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllVersionsResponse"
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

    def list_query_using_post(self, request):
        """根据“列表属性”为“是”的属性查询实例

        当数据模型中存在“列表属性”为“是”的属性时，可通过此接口查询数据模型中的实例数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQueryUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ListQueryUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ListQueryUsingPostResponse`
        """
        http_info = self._list_query_using_post_http_info(request)
        return self._call_api(**http_info)

    def list_query_using_post_invoker(self, request):
        http_info = self._list_query_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_query_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/query/{pageSizePath}/{curPagePath}",
            "request_type": request.__class__.__name__,
            "response_type": "ListQueryUsingPostResponse"
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

    def list_select_using_post(self, request):
        """查询实例的指定属性

        根据查询条件及指定属性分页返回（不支持扩展属性作为选定属性列）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSelectUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ListSelectUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ListSelectUsingPostResponse`
        """
        http_info = self._list_select_using_post_http_info(request)
        return self._call_api(**http_info)

    def list_select_using_post_invoker(self, request):
        http_info = self._list_select_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_select_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/select/{pageSizePath}/{curPagePath}",
            "request_type": request.__class__.__name__,
            "response_type": "ListSelectUsingPostResponse"
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

    def list_using_post(self, request):
        """查询实例的基础属性

        根据查询条件分页返回模型基本属性信息且不级联查询（不支持扩展属性作为查询条件）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ListUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ListUsingPostResponse`
        """
        http_info = self._list_using_post_http_info(request)
        return self._call_api(**http_info)

    def list_using_post_invoker(self, request):
        http_info = self._list_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/list/{pageSizePath}/{curPagePath}",
            "request_type": request.__class__.__name__,
            "response_type": "ListUsingPostResponse"
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

    def save_all_using_post(self, request):
        """根据唯一键为“是”的属性更新实例数据

        当数据模型中存在“唯一键”为“是”的属性时，可根据该属性的英文名称更新该数据模型中实例的所有字段数据。如果更新的实例不存在，系统将自动创建该实例数据。
        
        调用此接口时，建议传入该实例的所有字段信息。如果未传入某个字段，该字段的数据将更新为空值。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SaveAllUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.SaveAllUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.SaveAllUsingPostResponse`
        """
        http_info = self._save_all_using_post_http_info(request)
        return self._call_api(**http_info)

    def save_all_using_post_invoker(self, request):
        http_info = self._save_all_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _save_all_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/saveAll",
            "request_type": request.__class__.__name__,
            "response_type": "SaveAllUsingPostResponse"
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

    def save_as_using_post(self, request):
        """另存版本对象的实例数据

        版本对象的另存为接口（saveAs）用于创建一条与原版本对象实例数据相同的数据实例。该实例数据会完全复制原实例现有的数据，包括与其关联的主对象和分支对象，且新实例数据的版本号从初始值开始计算。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SaveAsUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.SaveAsUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.SaveAsUsingPostResponse`
        """
        http_info = self._save_as_using_post_http_info(request)
        return self._call_api(**http_info)

    def save_as_using_post_invoker(self, request):
        http_info = self._save_as_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _save_as_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/saveAs",
            "request_type": request.__class__.__name__,
            "response_type": "SaveAsUsingPostResponse"
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

    def save_using_post(self, request):
        """根据唯一键为“是”的属性更新实例的指定字段

        当数据模型中存在“唯一键”为“是”的属性时，可根据该属性的英文名称更新该数据模型中实例的指定字段数据。
        
        如果更新的实例不存在，系统将自动创建该实例数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SaveUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.SaveUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.SaveUsingPostResponse`
        """
        http_info = self._save_using_post_http_info(request)
        return self._call_api(**http_info)

    def save_using_post_invoker(self, request):
        http_info = self._save_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _save_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/save",
            "request_type": request.__class__.__name__,
            "response_type": "SaveUsingPostResponse"
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

    def show_get_by_unique_key(self, request):
        """根据唯一键为“是”的属性查询实例

        当数据模型中存在“唯一键”为“是”的属性时，可根据该属性查询实例数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGetByUniqueKey
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowGetByUniqueKeyRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowGetByUniqueKeyResponse`
        """
        http_info = self._show_get_by_unique_key_http_info(request)
        return self._call_api(**http_info)

    def show_get_by_unique_key_invoker(self, request):
        http_info = self._show_get_by_unique_key_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_get_by_unique_key_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/{getUniqueFieldMethod}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGetByUniqueKeyResponse"
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

    def show_version_by_master(self, request):
        """获取指定版本的M-V模型实例数据

        根据主对象ID、迭代版本和版本号，查询M-V模型实例的详细版本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVersionByMaster
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowVersionByMasterRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowVersionByMasterResponse`
        """
        http_info = self._show_version_by_master_http_info(request)
        return self._call_api(**http_info)

    def show_version_by_master_invoker(self, request):
        http_info = self._show_version_by_master_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_version_by_master_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/getVersionByMaster",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVersionByMasterResponse"
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

    def update_and_checkin(self, request):
        """更新并检入M-V模型数据实例

        通过此接口更新指定M-V模型实例，并检入该实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAndCheckin
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.UpdateAndCheckinRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.UpdateAndCheckinResponse`
        """
        http_info = self._update_and_checkin_http_info(request)
        return self._call_api(**http_info)

    def update_and_checkin_invoker(self, request):
        http_info = self._update_and_checkin_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_and_checkin_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/updateAndCheckin",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAndCheckinResponse"
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

    def update_and_revise(self, request):
        """修订并更新M-V模型数据实例

        根据主对象ID修订并更新M-V模型数据实例，即修订后实例的“version.修订版本”更新为新的修订版本，并同时更新该实例的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAndRevise
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.UpdateAndReviseRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.UpdateAndReviseResponse`
        """
        http_info = self._update_and_revise_http_info(request)
        return self._call_api(**http_info)

    def update_and_revise_invoker(self, request):
        http_info = self._update_and_revise_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_and_revise_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/reviseAndUpdate",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAndReviseResponse"
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

    def update_by_admin(self, request):
        """管理员更新M-V模型数据实例

        管理员通过此接口更新指定M-V模型的指定实例数据。如果实例的唯一编码不存在，则不做任何更新操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateByAdmin
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.UpdateByAdminRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.UpdateByAdminResponse`
        """
        http_info = self._update_by_admin_http_info(request)
        return self._call_api(**http_info)

    def update_by_admin_invoker(self, request):
        http_info = self._update_by_admin_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_by_admin_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/updateByAdmin",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateByAdminResponse"
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

    def update_by_condition_using_post(self, request):
        """根据指定条件更新实例

        根据指定条件更新指定模型的实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateByConditionUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.UpdateByConditionUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.UpdateByConditionUsingPostResponse`
        """
        http_info = self._update_by_condition_using_post_http_info(request)
        return self._call_api(**http_info)

    def update_by_condition_using_post_invoker(self, request):
        http_info = self._update_by_condition_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_by_condition_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/updateByCondition",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateByConditionUsingPostResponse"
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

    def update_using_post(self, request):
        """更新实例

        更新指定数据模型中的一个实例数据。如果实例的唯一编码不存在，则不做任何更新操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.UpdateUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.UpdateUsingPostResponse`
        """
        http_info = self._update_using_post_http_info(request)
        return self._call_api(**http_info)

    def update_using_post_invoker(self, request):
        http_info = self._update_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/update",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateUsingPostResponse"
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
