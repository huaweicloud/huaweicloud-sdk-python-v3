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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkworkspaceapp'")


class WorkspaceAppAsyncClient(Client):
    def __init__(self):
        super(WorkspaceAppAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkworkspaceapp.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "WorkspaceAppAsyncClient":
                raise TypeError("client type error, support client type is WorkspaceAppAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def authorize_obs_async(self, request):
        r"""获取上传至OBS桶的临时ak/sk

        获取上传至OBS桶的临时ak/sk。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AuthorizeObs
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.AuthorizeObsRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.AuthorizeObsResponse`
        """
        http_info = self._authorize_obs_http_info(request)
        return self._call_api(**http_info)

    def authorize_obs_async_invoker(self, request):
        http_info = self._authorize_obs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _authorize_obs_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-warehouse/action/authorize",
            "request_type": request.__class__.__name__,
            "response_type": "AuthorizeObsResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_warehouse_app_async(self, request):
        r"""批量删除应用仓库中的指定应用

        批量删除应用仓库中的指定应用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteWarehouseApp
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchDeleteWarehouseAppRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchDeleteWarehouseAppResponse`
        """
        http_info = self._batch_delete_warehouse_app_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_warehouse_app_async_invoker(self, request):
        http_info = self._batch_delete_warehouse_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_warehouse_app_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-warehouse/actions/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteWarehouseAppResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def bind_app_warehouse_bucket_async(self, request):
        r"""添加用户应用仓库桶及桶授权

        添加用户应用仓库桶及桶授权。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BindAppWarehouseBucket
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BindAppWarehouseBucketRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BindAppWarehouseBucketResponse`
        """
        http_info = self._bind_app_warehouse_bucket_http_info(request)
        return self._call_api(**http_info)

    def bind_app_warehouse_bucket_async_invoker(self, request):
        http_info = self._bind_app_warehouse_bucket_http_info(request)
        return AsyncInvoker(self, http_info)

    def _bind_app_warehouse_bucket_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-warehouse/bucket",
            "request_type": request.__class__.__name__,
            "response_type": "BindAppWarehouseBucketResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_bucket_or_acl_async(self, request):
        r"""添加桶或者桶授权

        添加桶或者桶授权。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateBucketOrAcl
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CreateBucketOrAclRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CreateBucketOrAclResponse`
        """
        http_info = self._create_bucket_or_acl_http_info(request)
        return self._call_api(**http_info)

    def create_bucket_or_acl_async_invoker(self, request):
        http_info = self._create_bucket_or_acl_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_bucket_or_acl_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-warehouse/bucket-and-acl/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateBucketOrAclResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_warehouse_app_async(self, request):
        r"""在应用仓库中新增应用

        在应用仓库中新增应用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWarehouseApp
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CreateWarehouseAppRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CreateWarehouseAppResponse`
        """
        http_info = self._create_warehouse_app_http_info(request)
        return self._call_api(**http_info)

    def create_warehouse_app_async_invoker(self, request):
        http_info = self._create_warehouse_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_warehouse_app_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-warehouse/apps",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWarehouseAppResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_warehouse_app_async(self, request):
        r"""删除应用仓库中的指定应用

        删除应用仓库中的指定应用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteWarehouseApp
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.DeleteWarehouseAppRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DeleteWarehouseAppResponse`
        """
        http_info = self._delete_warehouse_app_http_info(request)
        return self._call_api(**http_info)

    def delete_warehouse_app_async_invoker(self, request):
        http_info = self._delete_warehouse_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_warehouse_app_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/app-warehouse/apps/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteWarehouseAppResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_warehouse_apps_async(self, request):
        r"""查询租户应用仓库中的应用列表

        查询租户应用仓库中的应用列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWarehouseApps
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListWarehouseAppsRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListWarehouseAppsResponse`
        """
        http_info = self._list_warehouse_apps_http_info(request)
        return self._call_api(**http_info)

    def list_warehouse_apps_async_invoker(self, request):
        http_info = self._list_warehouse_apps_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_warehouse_apps_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-warehouse/apps",
            "request_type": request.__class__.__name__,
            "response_type": "ListWarehouseAppsResponse"
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
        if 'verify_status' in local_var_params:
            query_params.append(('verify_status', local_var_params['verify_status']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'app_category' in local_var_params:
            query_params.append(('app_category', local_var_params['app_category']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_app_warehouse_bucket_async(self, request):
        r"""查询用户应用仓库桶

        查询用户应用仓库桶
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAppWarehouseBucket
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ShowAppWarehouseBucketRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ShowAppWarehouseBucketResponse`
        """
        http_info = self._show_app_warehouse_bucket_http_info(request)
        return self._call_api(**http_info)

    def show_app_warehouse_bucket_async_invoker(self, request):
        http_info = self._show_app_warehouse_bucket_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_app_warehouse_bucket_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-warehouse/bucket",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppWarehouseBucketResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_warehouse_app_async(self, request):
        r"""修改应用仓库中的指定应用信息

        修改应用仓库中的指定应用信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateWarehouseApp
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.UpdateWarehouseAppRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UpdateWarehouseAppResponse`
        """
        http_info = self._update_warehouse_app_http_info(request)
        return self._call_api(**http_info)

    def update_warehouse_app_async_invoker(self, request):
        http_info = self._update_warehouse_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_warehouse_app_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/app-warehouse/apps/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateWarehouseAppResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def upload_warehouse_app_icon_async(self, request):
        r"""在应用仓库中上传图标文件

        在应用仓库中上传图标文件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UploadWarehouseAppIcon
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.UploadWarehouseAppIconRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UploadWarehouseAppIconResponse`
        """
        http_info = self._upload_warehouse_app_icon_http_info(request)
        return self._call_api(**http_info)

    def upload_warehouse_app_icon_async_invoker(self, request):
        http_info = self._upload_warehouse_app_icon_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upload_warehouse_app_icon_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-warehouse/apps/icon",
            "request_type": request.__class__.__name__,
            "response_type": "UploadWarehouseAppIconResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}
        if 'data' in local_var_params:
            form_params['data'] = local_var_params['data']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_disable_app_async(self, request):
        r"""批量禁用应用

        批量禁用应用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDisableApp
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchDisableAppRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchDisableAppResponse`
        """
        http_info = self._batch_disable_app_http_info(request)
        return self._call_api(**http_info)

    def batch_disable_app_async_invoker(self, request):
        http_info = self._batch_disable_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_disable_app_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-groups/{app_group_id}/apps/actions/disable",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDisableAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_group_id' in local_var_params:
            path_params['app_group_id'] = local_var_params['app_group_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_enable_app_async(self, request):
        r"""批量启用应用

        批量启用应用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchEnableApp
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchEnableAppRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchEnableAppResponse`
        """
        http_info = self._batch_enable_app_http_info(request)
        return self._call_api(**http_info)

    def batch_enable_app_async_invoker(self, request):
        http_info = self._batch_enable_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_enable_app_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-groups/{app_group_id}/apps/actions/enable",
            "request_type": request.__class__.__name__,
            "response_type": "BatchEnableAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_group_id' in local_var_params:
            path_params['app_group_id'] = local_var_params['app_group_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_app_icon_async(self, request):
        r"""删除自定义应用图标

        删除自定义应用应用图标，恢复使用默认应用图标，重复执行会按照成功处理(响应200)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAppIcon
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.DeleteAppIconRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DeleteAppIconResponse`
        """
        http_info = self._delete_app_icon_http_info(request)
        return self._call_api(**http_info)

    def delete_app_icon_async_invoker(self, request):
        http_info = self._delete_app_icon_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_app_icon_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/app-groups/{app_group_id}/apps/{app_id}/icon",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAppIconResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_group_id' in local_var_params:
            path_params['app_group_id'] = local_var_params['app_group_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_published_app_async(self, request):
        r"""查询已发布应用

        查询已发布的应用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPublishedApp
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListPublishedAppRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListPublishedAppResponse`
        """
        http_info = self._list_published_app_http_info(request)
        return self._call_api(**http_info)

    def list_published_app_async_invoker(self, request):
        http_info = self._list_published_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_published_app_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-groups/{app_group_id}/apps",
            "request_type": request.__class__.__name__,
            "response_type": "ListPublishedAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_group_id' in local_var_params:
            path_params['app_group_id'] = local_var_params['app_group_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def publish_app_async(self, request):
        r"""发布应用

        批量发布应用，不允许发布同名的应用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PublishApp
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.PublishAppRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PublishAppResponse`
        """
        http_info = self._publish_app_http_info(request)
        return self._call_api(**http_info)

    def publish_app_async_invoker(self, request):
        http_info = self._publish_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _publish_app_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-groups/{app_group_id}/apps",
            "request_type": request.__class__.__name__,
            "response_type": "PublishAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_group_id' in local_var_params:
            path_params['app_group_id'] = local_var_params['app_group_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

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
        r"""查询应用详细信息

        查询应用详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAppDetail
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ShowAppDetailRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ShowAppDetailResponse`
        """
        http_info = self._show_app_detail_http_info(request)
        return self._call_api(**http_info)

    def show_app_detail_async_invoker(self, request):
        http_info = self._show_app_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_app_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-groups/{app_group_id}/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_group_id' in local_var_params:
            path_params['app_group_id'] = local_var_params['app_group_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_publishable_app_async(self, request):
        r"""可发布应用列表

        查询应用组下可发布的应用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPublishableApp
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ShowPublishableAppRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ShowPublishableAppResponse`
        """
        http_info = self._show_publishable_app_http_info(request)
        return self._call_api(**http_info)

    def show_publishable_app_async_invoker(self, request):
        http_info = self._show_publishable_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_publishable_app_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-groups/{app_group_id}/publishable-app",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPublishableAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_group_id' in local_var_params:
            path_params['app_group_id'] = local_var_params['app_group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def unpublish_app_async(self, request):
        r"""批量取消应用发布

        批量取消应用发布。
        &gt; - 批量取消应用组下已经发布的应用，应用对应的授权会一起删除，重复执行会按照成功处理(响应200)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UnpublishApp
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.UnpublishAppRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UnpublishAppResponse`
        """
        http_info = self._unpublish_app_http_info(request)
        return self._call_api(**http_info)

    def unpublish_app_async_invoker(self, request):
        http_info = self._unpublish_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _unpublish_app_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-groups/{app_group_id}/apps/batch-unpublish",
            "request_type": request.__class__.__name__,
            "response_type": "UnpublishAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_group_id' in local_var_params:
            path_params['app_group_id'] = local_var_params['app_group_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

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
        r"""修改应用信息

        编辑修改应用信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateApp
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.UpdateAppRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UpdateAppResponse`
        """
        http_info = self._update_app_http_info(request)
        return self._call_api(**http_info)

    def update_app_async_invoker(self, request):
        http_info = self._update_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_app_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/app-groups/{app_group_id}/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_group_id' in local_var_params:
            path_params['app_group_id'] = local_var_params['app_group_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_pre_boot_policy_async(self, request):
        r"""批量设置应用预启动

        批量设置应用预启动。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePreBootPolicy
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.UpdatePreBootPolicyRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UpdatePreBootPolicyResponse`
        """
        http_info = self._update_pre_boot_policy_http_info(request)
        return self._call_api(**http_info)

    def update_pre_boot_policy_async_invoker(self, request):
        http_info = self._update_pre_boot_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_pre_boot_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-groups/{app_group_id}/apps/pre-boot-policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePreBootPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_group_id' in local_var_params:
            path_params['app_group_id'] = local_var_params['app_group_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def upload_app_icon_async(self, request):
        r"""修改自定义应用图标

        修改自定义应用图标。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UploadAppIcon
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.UploadAppIconRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UploadAppIconResponse`
        """
        http_info = self._upload_app_icon_http_info(request)
        return self._call_api(**http_info)

    def upload_app_icon_async_invoker(self, request):
        http_info = self._upload_app_icon_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upload_app_icon_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-groups/{app_group_id}/apps/{app_id}/icon",
            "request_type": request.__class__.__name__,
            "response_type": "UploadAppIconResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_group_id' in local_var_params:
            path_params['app_group_id'] = local_var_params['app_group_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}

        form_params = {}
        if 'data' in local_var_params:
            form_params['data'] = local_var_params['data']
        if 'icon_url' in local_var_params:
            form_params['icon_url'] = local_var_params['icon_url']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def initialize_tenant_async(self, request):
        r"""租户服务激活、初始化

        租户服务激活。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for InitializeTenant
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.InitializeTenantRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.InitializeTenantResponse`
        """
        http_info = self._initialize_tenant_http_info(request)
        return self._call_api(**http_info)

    def initialize_tenant_async_invoker(self, request):
        http_info = self._initialize_tenant_http_info(request)
        return AsyncInvoker(self, http_info)

    def _initialize_tenant_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/tenant/action/active",
            "request_type": request.__class__.__name__,
            "response_type": "InitializeTenantResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_corp_config_info_async(self, request):
        r"""查询企业系统配置

        配置加载顺序： 查询企业级配置--&gt; 查不到则赋默认阿波罗配置--&gt; 阿波罗没有则不返回。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCorpConfigInfo
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListCorpConfigInfoRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListCorpConfigInfoResponse`
        """
        http_info = self._list_corp_config_info_http_info(request)
        return self._call_api(**http_info)

    def list_corp_config_info_async_invoker(self, request):
        http_info = self._list_corp_config_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_corp_config_info_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/bundles/batch-query-config-info",
            "request_type": request.__class__.__name__,
            "response_type": "ListCorpConfigInfoResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_tenant_profile_async(self, request):
        r"""查询租户信息

        查询租户信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTenantProfile
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListTenantProfileRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListTenantProfileResponse`
        """
        http_info = self._list_tenant_profile_http_info(request)
        return self._call_api(**http_info)

    def list_tenant_profile_async_invoker(self, request):
        http_info = self._list_tenant_profile_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tenant_profile_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/tenant/profile",
            "request_type": request.__class__.__name__,
            "response_type": "ListTenantProfileResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_app_group_async(self, request):
        r"""批量删除应用组

        批量删除应用组,重复执行会按照成功处理(响应200)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteAppGroup
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchDeleteAppGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchDeleteAppGroupResponse`
        """
        http_info = self._batch_delete_app_group_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_app_group_async_invoker(self, request):
        http_info = self._batch_delete_app_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_app_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-groups/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteAppGroupResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def check_app_group_async(self, request):
        r"""校验应用组

        校验应用组是否符合指定的规则。
        1. 校验应用组名称是否符合规则。
        2. 校验应用组名称是否重复。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckAppGroup
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CheckAppGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CheckAppGroupResponse`
        """
        http_info = self._check_app_group_http_info(request)
        return self._call_api(**http_info)

    def check_app_group_async_invoker(self, request):
        http_info = self._check_app_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_app_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-groups/rules/validate",
            "request_type": request.__class__.__name__,
            "response_type": "CheckAppGroupResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_app_group_async(self, request):
        r"""创建应用组

        该API用于创建应用组。
        &gt; - 应用服务器中安装了不同的应用，这些应用可以组成不同的应用组，进行集中的管理和维护，向用户(组)发布。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAppGroup
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CreateAppGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CreateAppGroupResponse`
        """
        http_info = self._create_app_group_http_info(request)
        return self._call_api(**http_info)

    def create_app_group_async_invoker(self, request):
        http_info = self._create_app_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_app_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAppGroupResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_app_group_async(self, request):
        r"""应用组删除

        删除指定的应用组,重复执行会按照成功处理(响应200)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAppGroup
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.DeleteAppGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DeleteAppGroupResponse`
        """
        http_info = self._delete_app_group_http_info(request)
        return self._call_api(**http_info)

    def delete_app_group_async_invoker(self, request):
        http_info = self._delete_app_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_app_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/app-groups/{app_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAppGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_group_id' in local_var_params:
            path_params['app_group_id'] = local_var_params['app_group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def disassociate_app_group_async(self, request):
        r"""解除服务组关联的所有应用组

        解除服务组关联的所有应用组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateAppGroup
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.DisassociateAppGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DisassociateAppGroupResponse`
        """
        http_info = self._disassociate_app_group_http_info(request)
        return self._call_api(**http_info)

    def disassociate_app_group_async_invoker(self, request):
        http_info = self._disassociate_app_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disassociate_app_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-groups/actions/disassociate-app-group",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateAppGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'server_group_id' in local_var_params:
            query_params.append(('server_group_id', local_var_params['server_group_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_app_group_async(self, request):
        r"""查询应用组

        查询用户创建的应用组，按照名称、授权类型分页查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppGroup
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListAppGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListAppGroupResponse`
        """
        http_info = self._list_app_group_http_info(request)
        return self._call_api(**http_info)

    def list_app_group_async_invoker(self, request):
        http_info = self._list_app_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_app_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppGroupResponse"
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
        if 'app_server_group_id' in local_var_params:
            query_params.append(('app_server_group_id', local_var_params['app_server_group_id']))
        if 'app_group_id' in local_var_params:
            query_params.append(('app_group_id', local_var_params['app_group_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'authorization_type' in local_var_params:
            query_params.append(('authorization_type', local_var_params['authorization_type']))
        if 'app_type' in local_var_params:
            query_params.append(('app_type', local_var_params['app_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_app_group_detail_async(self, request):
        r"""查询应用组详情

        查询应用组详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAppGroupDetail
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ShowAppGroupDetailRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ShowAppGroupDetailResponse`
        """
        http_info = self._show_app_group_detail_http_info(request)
        return self._call_api(**http_info)

    def show_app_group_detail_async_invoker(self, request):
        http_info = self._show_app_group_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_app_group_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-groups/{app_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppGroupDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_group_id' in local_var_params:
            path_params['app_group_id'] = local_var_params['app_group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_app_group_async(self, request):
        r"""修改应用组

        修改应用组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAppGroup
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.UpdateAppGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UpdateAppGroupResponse`
        """
        http_info = self._update_app_group_http_info(request)
        return self._call_api(**http_info)

    def update_app_group_async_invoker(self, request):
        http_info = self._update_app_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_app_group_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/app-groups/{app_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAppGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_group_id' in local_var_params:
            path_params['app_group_id'] = local_var_params['app_group_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_order_async(self, request):
        r"""创建订单

        创建订单。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateOrder
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CreateOrderRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CreateOrderResponse`
        """
        http_info = self._create_order_http_info(request)
        return self._call_api(**http_info)

    def create_order_async_invoker(self, request):
        http_info = self._create_order_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_order_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/bundles/subscribe/order",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOrderResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_product_async(self, request):
        r"""查询云应用套餐

        查询云应用套餐，按照条件过滤。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProduct
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListProductRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListProductResponse`
        """
        http_info = self._list_product_http_info(request)
        return self._call_api(**http_info)

    def list_product_async_invoker(self, request):
        http_info = self._list_product_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_product_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/product",
            "request_type": request.__class__.__name__,
            "response_type": "ListProductResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_id' in local_var_params:
            query_params.append(('product_id', local_var_params['product_id']))
        if 'flavor_id' in local_var_params:
            query_params.append(('flavor_id', local_var_params['flavor_id']))
        if 'availability_zone' in local_var_params:
            query_params.append(('availability_zone', local_var_params['availability_zone']))
        if 'os_type' in local_var_params:
            query_params.append(('os_type', local_var_params['os_type']))
        if 'charge_mode' in local_var_params:
            query_params.append(('charge_mode', local_var_params['charge_mode']))
        if 'architecture' in local_var_params:
            query_params.append(('architecture', local_var_params['architecture']))
        if 'package_type' in local_var_params:
            query_params.append(('package_type', local_var_params['package_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_session_type_async(self, request):
        r"""查询会话套餐列表

        该接口用于查询会话套餐列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSessionType
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListSessionTypeRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListSessionTypeResponse`
        """
        http_info = self._list_session_type_http_info(request)
        return self._call_api(**http_info)

    def list_session_type_async_invoker(self, request):
        http_info = self._list_session_type_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_session_type_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/session-type",
            "request_type": request.__class__.__name__,
            "response_type": "ListSessionTypeResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_session_types_async(self, request):
        r"""查询会话套餐列表（已废弃）

        该接口用于查询会话套餐列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSessionTypes
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ShowSessionTypesRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ShowSessionTypesResponse`
        """
        http_info = self._show_session_types_http_info(request)
        return self._call_api(**http_info)

    def show_session_types_async_invoker(self, request):
        http_info = self._show_session_types_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_session_types_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/session-type",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSessionTypesResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def add_app_group_authorization_async(self, request):
        r"""增加应用组授权

        应用组添加用户授权，授权后用户就获得应用组下所有已发布应用的权限访问。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddAppGroupAuthorization
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.AddAppGroupAuthorizationRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.AddAppGroupAuthorizationResponse`
        """
        http_info = self._add_app_group_authorization_http_info(request)
        return self._call_api(**http_info)

    def add_app_group_authorization_async_invoker(self, request):
        http_info = self._add_app_group_authorization_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_app_group_authorization_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-groups/authorizations",
            "request_type": request.__class__.__name__,
            "response_type": "AddAppGroupAuthorizationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_app_group_authorization_async(self, request):
        r"""移除应用组授权

        移除应用组内的指定用户的授权，用户授权删除后，用户将没有权限访问应用组内的任何应用。注意：重复执行会按照操作成功处理。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteAppGroupAuthorization
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchDeleteAppGroupAuthorizationRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchDeleteAppGroupAuthorizationResponse`
        """
        http_info = self._batch_delete_app_group_authorization_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_app_group_authorization_async_invoker(self, request):
        http_info = self._batch_delete_app_group_authorization_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_app_group_authorization_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-groups/actions/batch-delete-authorization",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteAppGroupAuthorizationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_app_group_authorization_async(self, request):
        r"""查询应用组授权记录

        查询应用内已授权的用户列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppGroupAuthorization
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListAppGroupAuthorizationRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListAppGroupAuthorizationResponse`
        """
        http_info = self._list_app_group_authorization_http_info(request)
        return self._call_api(**http_info)

    def list_app_group_authorization_async_invoker(self, request):
        http_info = self._list_app_group_authorization_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_app_group_authorization_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-groups/actions/list-authorizations",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppGroupAuthorizationResponse"
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
        if 'app_group_id' in local_var_params:
            query_params.append(('app_group_id', local_var_params['app_group_id']))
        if 'account_id' in local_var_params:
            query_params.append(('account_id', local_var_params['account_id']))
        if 'account' in local_var_params:
            query_params.append(('account', local_var_params['account']))
        if 'account_type' in local_var_params:
            query_params.append(('account_type', local_var_params['account_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_availability_zone_async(self, request):
        r"""查询可用分区列表

        该接口用于查询支持的可用分区列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAvailabilityZone
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListAvailabilityZoneRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListAvailabilityZoneResponse`
        """
        http_info = self._list_availability_zone_http_info(request)
        return self._call_api(**http_info)

    def list_availability_zone_async_invoker(self, request):
        http_info = self._list_availability_zone_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_availability_zone_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/availability-zone",
            "request_type": request.__class__.__name__,
            "response_type": "ListAvailabilityZoneResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_az_async(self, request):
        r"""查询可用分区列表

        [该接口用于查询支持的可用分区列表，按站点分类。](tag:HW)[该接口用于查询支持的可用分区列表。](tag:HCS)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAz
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListAzRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListAzResponse`
        """
        http_info = self._list_az_http_info(request)
        return self._call_api(**http_info)

    def list_az_async_invoker(self, request):
        http_info = self._list_az_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_az_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/availability-zone/summary",
            "request_type": request.__class__.__name__,
            "response_type": "ListAzResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_cloud_storage_async(self, request):
        r"""批量删除云存储

        批量删除云存储。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteCloudStorage
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchDeleteCloudStorageRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchDeleteCloudStorageResponse`
        """
        http_info = self._batch_delete_cloud_storage_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_cloud_storage_async_invoker(self, request):
        http_info = self._batch_delete_cloud_storage_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_cloud_storage_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloud-storages/actions/batch-delete-cloud-storages",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteCloudStorageResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_cloud_storage_async(self, request):
        r"""创建项目配置关联

        创建项目配置关联，目前仅支持关联项目配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCloudStorage
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CreateCloudStorageRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CreateCloudStorageResponse`
        """
        http_info = self._create_cloud_storage_http_info(request)
        return self._call_api(**http_info)

    def create_cloud_storage_async_invoker(self, request):
        http_info = self._create_cloud_storage_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_cloud_storage_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloud-storages",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCloudStorageResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_user_folder_assignment_async(self, request):
        r"""创建个人文件夹

        创建个人文件夹，已存在对应目录时，仅更新策略不会重复创建目录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateUserFolderAssignment
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CreateUserFolderAssignmentRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CreateUserFolderAssignmentResponse`
        """
        http_info = self._create_user_folder_assignment_http_info(request)
        return self._call_api(**http_info)

    def create_user_folder_assignment_async_invoker(self, request):
        http_info = self._create_user_folder_assignment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_user_folder_assignment_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloud-storages/{storage_id}/actions/create-folder",
            "request_type": request.__class__.__name__,
            "response_type": "CreateUserFolderAssignmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'storage_id' in local_var_params:
            path_params['storage_id'] = local_var_params['storage_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_cloud_storage_async(self, request):
        r"""删除云存储

        删除共享存储，只会解除NAS与项目配置之间的关联关系。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCloudStorage
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.DeleteCloudStorageRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DeleteCloudStorageResponse`
        """
        http_info = self._delete_cloud_storage_http_info(request)
        return self._call_api(**http_info)

    def delete_cloud_storage_async_invoker(self, request):
        http_info = self._delete_cloud_storage_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_cloud_storage_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/cloud-storages/{storage_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCloudStorageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_cloud_storage_attachment_async(self, request):
        r"""删除个人文件夹

        删除个人存储目录，个人目录中的数据也将永久删除且无法恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCloudStorageAttachment
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.DeleteCloudStorageAttachmentRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DeleteCloudStorageAttachmentResponse`
        """
        http_info = self._delete_cloud_storage_attachment_http_info(request)
        return self._call_api(**http_info)

    def delete_cloud_storage_attachment_async_invoker(self, request):
        http_info = self._delete_cloud_storage_attachment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_cloud_storage_attachment_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloud-storages/{storage_id}/actions/delete-folder",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCloudStorageAttachmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'storage_id' in local_var_params:
            path_params['storage_id'] = local_var_params['storage_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_cloud_storage_async(self, request):
        r"""查询云存储

        查询云存储。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCloudStorage
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListCloudStorageRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListCloudStorageResponse`
        """
        http_info = self._list_cloud_storage_http_info(request)
        return self._call_api(**http_info)

    def list_cloud_storage_async_invoker(self, request):
        http_info = self._list_cloud_storage_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cloud_storage_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloud-storages",
            "request_type": request.__class__.__name__,
            "response_type": "ListCloudStorageResponse"
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
        if 'storage_id' in local_var_params:
            query_params.append(('storage_id', local_var_params['storage_id']))
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_cloud_storage_assignment_async(self, request):
        r"""查询个人文件夹列表

        查询个人文件夹列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCloudStorageAssignment
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListCloudStorageAssignmentRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListCloudStorageAssignmentResponse`
        """
        http_info = self._list_cloud_storage_assignment_http_info(request)
        return self._call_api(**http_info)

    def list_cloud_storage_assignment_async_invoker(self, request):
        http_info = self._list_cloud_storage_assignment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cloud_storage_assignment_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloud-storages/actions/list-folders",
            "request_type": request.__class__.__name__,
            "response_type": "ListCloudStorageAssignmentResponse"
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
        if 'storage_id' in local_var_params:
            query_params.append(('storage_id', local_var_params['storage_id']))
        if 'claim_mode' in local_var_params:
            query_params.append(('claim_mode', local_var_params['claim_mode']))
        if 'attach' in local_var_params:
            query_params.append(('attach', local_var_params['attach']))
        if 'attach_names' in local_var_params:
            query_params.append(('attach_names', local_var_params['attach_names']))
            collection_formats['attach_names'] = 'csv'
        if 'capacity_filter' in local_var_params:
            query_params.append(('capacity_filter', local_var_params['capacity_filter']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_folders_and_files_async(self, request):
        r"""查询文件夹和文件信息

        查询指定目录下文件夹和文件信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFoldersAndFiles
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListFoldersAndFilesRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListFoldersAndFilesResponse`
        """
        http_info = self._list_folders_and_files_http_info(request)
        return self._call_api(**http_info)

    def list_folders_and_files_async_invoker(self, request):
        http_info = self._list_folders_and_files_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_folders_and_files_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloud-storages/actions/list-folder-files",
            "request_type": request.__class__.__name__,
            "response_type": "ListFoldersAndFilesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'cloud_storage_assignment_id' in local_var_params:
            query_params.append(('cloud_storage_assignment_id', local_var_params['cloud_storage_assignment_id']))
        if 'folder_url' in local_var_params:
            query_params.append(('folder_url', local_var_params['folder_url']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'max_keys' in local_var_params:
            query_params.append(('max_keys', local_var_params['max_keys']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_project_configs_async(self, request):
        r"""查询项目配置列表

        查询项目配置列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectConfigs
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListProjectConfigsRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListProjectConfigsResponse`
        """
        http_info = self._list_project_configs_http_info(request)
        return self._call_api(**http_info)

    def list_project_configs_async_invoker(self, request):
        http_info = self._list_project_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_project_configs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloud-storages/actions/list-project-configs",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectConfigsResponse"
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

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def reset_user_profile_async(self, request):
        r"""重置userprofile

        重置userprofile，初始化或重置并备份userprofile。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetUserProfile
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ResetUserProfileRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ResetUserProfileResponse`
        """
        http_info = self._reset_user_profile_http_info(request)
        return self._call_api(**http_info)

    def reset_user_profile_async_invoker(self, request):
        http_info = self._reset_user_profile_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reset_user_profile_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloud-storages/actions/reset-userprofile",
            "request_type": request.__class__.__name__,
            "response_type": "ResetUserProfileResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_project_config_async(self, request):
        r"""查询项目配置信息

        查询项目配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProjectConfig
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ShowProjectConfigRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ShowProjectConfigResponse`
        """
        http_info = self._show_project_config_http_info(request)
        return self._call_api(**http_info)

    def show_project_config_async_invoker(self, request):
        http_info = self._show_project_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_project_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloud-storages/actions/project-config/{cloud_storage_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cloud_storage_id' in local_var_params:
            path_params['cloud_storage_id'] = local_var_params['cloud_storage_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def transfer_file_async(self, request):
        r"""文件流转

        云存储文件流转与分享
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for TransferFile
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.TransferFileRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.TransferFileResponse`
        """
        http_info = self._transfer_file_http_info(request)
        return self._call_api(**http_info)

    def transfer_file_async_invoker(self, request):
        http_info = self._transfer_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _transfer_file_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloud-storages/actions/transfer-file",
            "request_type": request.__class__.__name__,
            "response_type": "TransferFileResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def transfer_file_pre_async(self, request):
        r"""文件预流转

        文件预流转，在接收方接收文件前返回可用的文件路径
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for TransferFilePre
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.TransferFilePreRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.TransferFilePreResponse`
        """
        http_info = self._transfer_file_pre_http_info(request)
        return self._call_api(**http_info)

    def transfer_file_pre_async_invoker(self, request):
        http_info = self._transfer_file_pre_http_info(request)
        return AsyncInvoker(self, http_info)

    def _transfer_file_pre_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloud-storages/actions/pre-transfer-file",
            "request_type": request.__class__.__name__,
            "response_type": "TransferFilePreResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_cloud_user_folder_assignment_async(self, request):
        r"""修改个人文件夹

        创建个人文件夹。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCloudUserFolderAssignment
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.UpdateCloudUserFolderAssignmentRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UpdateCloudUserFolderAssignmentResponse`
        """
        http_info = self._update_cloud_user_folder_assignment_http_info(request)
        return self._call_api(**http_info)

    def update_cloud_user_folder_assignment_async_invoker(self, request):
        http_info = self._update_cloud_user_folder_assignment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_cloud_user_folder_assignment_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/cloud-storages/{storage_id}/actions/update-folder/{cloud_assignment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCloudUserFolderAssignmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'storage_id' in local_var_params:
            path_params['storage_id'] = local_var_params['storage_id']
        if 'cloud_assignment_id' in local_var_params:
            path_params['cloud_assignment_id'] = local_var_params['cloud_assignment_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def attach_image_server_app_async(self, request):
        r"""分发软件信息至镜像实例

        分发应用软件信息至镜像实例，管理员可以按需下载并安装应用软件。
        * 目前只支持来自云应用仓库的软件信息。
        * 只允许对状态为 &#x60;实例正常运行&#x60;、&#x60;镜像任务结束&#x60; 的实例分发软件信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AttachImageServerApp
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.AttachImageServerAppRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.AttachImageServerAppResponse`
        """
        http_info = self._attach_image_server_app_http_info(request)
        return self._call_api(**http_info)

    def attach_image_server_app_async_invoker(self, request):
        http_info = self._attach_image_server_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _attach_image_server_app_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/image-servers/{server_id}/actions/attach-app",
            "request_type": request.__class__.__name__,
            "response_type": "AttachImageServerAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_image_server_async(self, request):
        r"""批量删除镜像实例

        批量删除镜像实例。
        * 忽略不存在的镜像实例，响应正常。
        * 不允许操作状态为 &#x60;创建中&#x60;、&#x60;镜像创建中&#x60;的实例，响应异常。
        * 不支持资源关联发生变化后，请求删除镜像实例关联资源，任务响应异常。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteImageServer
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchDeleteImageServerRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchDeleteImageServerResponse`
        """
        http_info = self._batch_delete_image_server_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_image_server_async_invoker(self, request):
        http_info = self._batch_delete_image_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_image_server_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/image-servers/actions/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteImageServerResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_image_server_async(self, request):
        r"""创建镜像实例

        创建镜像实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateImageServer
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CreateImageServerRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CreateImageServerResponse`
        """
        http_info = self._create_image_server_http_info(request)
        return self._call_api(**http_info)

    def create_image_server_async_invoker(self, request):
        http_info = self._create_image_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_image_server_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/image-servers",
            "request_type": request.__class__.__name__,
            "response_type": "CreateImageServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'service_transaction_id' in local_var_params:
            header_params['Service-Transaction-Id'] = local_var_params['service_transaction_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_image_servers_async(self, request):
        r"""查询镜像实例列表

        查询镜像实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListImageServers
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListImageServersRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListImageServersResponse`
        """
        http_info = self._list_image_servers_http_info(request)
        return self._call_api(**http_info)

    def list_image_servers_async_invoker(self, request):
        http_info = self._list_image_servers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_image_servers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/image-servers",
            "request_type": request.__class__.__name__,
            "response_type": "ListImageServersResponse"
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
        if 'server_name' in local_var_params:
            query_params.append(('server_name', local_var_params['server_name']))
        if 'server_id' in local_var_params:
            query_params.append(('server_id', local_var_params['server_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_latest_attached_server_app_async(self, request):
        r"""查询最近一次分发软件信息列表

        查询最近一次分发软件信息列表，返回ID列表，不包含具体信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLatestAttachedServerApp
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListLatestAttachedServerAppRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListLatestAttachedServerAppResponse`
        """
        http_info = self._list_latest_attached_server_app_http_info(request)
        return self._call_api(**http_info)

    def list_latest_attached_server_app_async_invoker(self, request):
        http_info = self._list_latest_attached_server_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_latest_attached_server_app_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/image-servers/{server_id}/actions/latest-attached-app",
            "request_type": request.__class__.__name__,
            "response_type": "ListLatestAttachedServerAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def recreate_server_image_async(self, request):
        r"""构建云应用镜像

        构建云应用镜像。
        * 只允许对状态为 &#x60;实例正常运行&#x60;、&#x60;镜像任务结束&#x60; 的实例构建云应用镜像。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RecreateServerImage
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.RecreateServerImageRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.RecreateServerImageResponse`
        """
        http_info = self._recreate_server_image_http_info(request)
        return self._call_api(**http_info)

    def recreate_server_image_async_invoker(self, request):
        http_info = self._recreate_server_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _recreate_server_image_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/image-servers/{server_id}/actions/recreate-image",
            "request_type": request.__class__.__name__,
            "response_type": "RecreateServerImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_image_server_async(self, request):
        r"""查询指定镜像实例

        查询指定的镜像实例当前这个接口的查询数据和list查询的一致。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowImageServer
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ShowImageServerRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ShowImageServerResponse`
        """
        http_info = self._show_image_server_http_info(request)
        return self._call_api(**http_info)

    def show_image_server_async_invoker(self, request):
        http_info = self._show_image_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_image_server_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/image-servers/{server_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowImageServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_image_server_async(self, request):
        r"""修改镜像实例

        修改镜像实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateImageServer
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.UpdateImageServerRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UpdateImageServerResponse`
        """
        http_info = self._update_image_server_http_info(request)
        return self._call_api(**http_info)

    def update_image_server_async_invoker(self, request):
        http_info = self._update_image_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_image_server_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/image-servers/{server_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateImageServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_app_sub_jobs_async(self, request):
        r"""批量删除子任务

        批量删除子任务，忽略不存在的服务器并且返回成功响应。
        只能删除以下的两种状态：
        - SUCCESS：成功。
        - FAILED：失败。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteAppSubJobs
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchDeleteAppSubJobsRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchDeleteAppSubJobsResponse`
        """
        http_info = self._batch_delete_app_sub_jobs_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_app_sub_jobs_async_invoker(self, request):
        http_info = self._batch_delete_app_sub_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_app_sub_jobs_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-server-sub-jobs/actions/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteAppSubJobsResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_image_sub_jobs_async(self, request):
        r"""批量删除镜像子任务

        批量删除子任务，忽略不存在的服务器并且返回成功响应。
        只能删除以下的两种状态 SUCCESS：成功。 FAILED：失败
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteImageSubJobs
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchDeleteImageSubJobsRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchDeleteImageSubJobsResponse`
        """
        http_info = self._batch_delete_image_sub_jobs_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_image_sub_jobs_async_invoker(self, request):
        http_info = self._batch_delete_image_sub_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_image_sub_jobs_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/image-server-sub-jobs/actions/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteImageSubJobsResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def count_image_sub_jobs_async(self, request):
        r"""镜像子任务数量查询

        该接口用于查询异步子任务数量,job_type未传递时,
        则查询JobType为CREATE_SERVER|DELETE_SERVER|REJOIN_DOMAIN|CHANGE_SERVER_IMAGE|REINSTALL_OS的子任务总数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CountImageSubJobs
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CountImageSubJobsRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CountImageSubJobsResponse`
        """
        http_info = self._count_image_sub_jobs_http_info(request)
        return self._call_api(**http_info)

    def count_image_sub_jobs_async_invoker(self, request):
        http_info = self._count_image_sub_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _count_image_sub_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/image-server-sub-jobs/actions/count",
            "request_type": request.__class__.__name__,
            "response_type": "CountImageSubJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'job_type' in local_var_params:
            query_params.append(('job_type', local_var_params['job_type']))
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def count_sub_jobs_async(self, request):
        r"""子任务数量查询

        该接口用于查询异步子任务数量。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CountSubJobs
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CountSubJobsRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CountSubJobsResponse`
        """
        http_info = self._count_sub_jobs_http_info(request)
        return self._call_api(**http_info)

    def count_sub_jobs_async_invoker(self, request):
        http_info = self._count_sub_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _count_sub_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-server-sub-jobs/actions/count",
            "request_type": request.__class__.__name__,
            "response_type": "CountSubJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'job_type' in local_var_params:
            query_params.append(('job_type', local_var_params['job_type']))
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_image_jobs_async(self, request):
        r"""查询租户的镜像任务列表

        该接口用于查询租户的异步任务执行情况。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListImageJobs
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListImageJobsRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListImageJobsResponse`
        """
        http_info = self._list_image_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_image_jobs_async_invoker(self, request):
        http_info = self._list_image_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_image_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/image-server-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListImageJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'job_type' in local_var_params:
            query_params.append(('job_type', local_var_params['job_type']))
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_image_sub_jobs_async(self, request):
        r"""镜像子任务查询

        该接口用于查询异步子任务执行情况,sub_job_ids非空时offset和limit不会生效。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListImageSubJobs
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListImageSubJobsRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListImageSubJobsResponse`
        """
        http_info = self._list_image_sub_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_image_sub_jobs_async_invoker(self, request):
        http_info = self._list_image_sub_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_image_sub_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/image-server-sub-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListImageSubJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'job_type' in local_var_params:
            query_params.append(('job_type', local_var_params['job_type']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_sub_jobs_async(self, request):
        r"""子任务查询

        该接口用于查询异步子任务执行情况,sub_job_ids非空时offset和limit不会生效。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSubJobs
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListSubJobsRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListSubJobsResponse`
        """
        http_info = self._list_sub_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_sub_jobs_async_invoker(self, request):
        http_info = self._list_sub_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_sub_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-server-sub-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListSubJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'job_type' in local_var_params:
            query_params.append(('job_type', local_var_params['job_type']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_image_job_async(self, request):
        r"""查询镜像任务详情

        该接口用于查询异步任务的执行情况，比如查询创建镜像实例任务的执行状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowImageJob
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ShowImageJobRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ShowImageJobResponse`
        """
        http_info = self._show_image_job_http_info(request)
        return self._call_api(**http_info)

    def show_image_job_async_invoker(self, request):
        http_info = self._show_image_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_image_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/image-server-jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowImageJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_job_async(self, request):
        r"""查询任务的执行状态（已废弃）

        查询Job的执行状态。
        
        对于创建云应用服务器命令下发后会返回job_id，通过job_id可以查询任务的执行状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJob
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ShowJobRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ShowJobResponse`
        """
        http_info = self._show_job_http_info(request)
        return self._call_api(**http_info)

    def show_job_async_invoker(self, request):
        http_info = self._show_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/job/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_job_detail_async(self, request):
        r"""查询任务的执行状态详情

        查询Job的执行状态。
        
        对于创建云服务器、删除云服务器、重建镜像等异步API，下发命令后会返回job_id，通过job_id可以查询任务的执行状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobDetail
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ShowJobDetailRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ShowJobDetailResponse`
        """
        http_info = self._show_job_detail_http_info(request)
        return self._call_api(**http_info)

    def show_job_detail_async_invoker(self, request):
        http_info = self._show_job_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/job/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_authorization_mail_record_async(self, request):
        r"""查询应用组授权邮件发送记录

        查询应用组授权邮件发送记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAuthorizationMailRecord
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListAuthorizationMailRecordRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListAuthorizationMailRecordResponse`
        """
        http_info = self._list_authorization_mail_record_http_info(request)
        return self._call_api(**http_info)

    def list_authorization_mail_record_async_invoker(self, request):
        http_info = self._list_authorization_mail_record_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_authorization_mail_record_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/mails",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuthorizationMailRecordResponse"
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
        if 'app_group_id' in local_var_params:
            query_params.append(('app_group_id', local_var_params['app_group_id']))
        if 'account' in local_var_params:
            query_params.append(('account', local_var_params['account']))
        if 'mail_send_type' in local_var_params:
            query_params.append(('mail_send_type', local_var_params['mail_send_type']))
        if 'mail_send_result' in local_var_params:
            query_params.append(('mail_send_result', local_var_params['mail_send_result']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def send_authorization_mail_async(self, request):
        r"""重发应用组授权邮件（根据授权邮件记录）

        重发应用组授权邮件（根据授权邮件记录）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SendAuthorizationMail
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.SendAuthorizationMailRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.SendAuthorizationMailResponse`
        """
        http_info = self._send_authorization_mail_http_info(request)
        return self._call_api(**http_info)

    def send_authorization_mail_async_invoker(self, request):
        http_info = self._send_authorization_mail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _send_authorization_mail_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/mails/actions/send",
            "request_type": request.__class__.__name__,
            "response_type": "SendAuthorizationMailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def send_authorized_mail_async(self, request):
        r"""重发应用组授权邮件（根据授权记录）

        重发应用组授权邮件（根据授权记录）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SendAuthorizedMail
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.SendAuthorizedMailRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.SendAuthorizedMailResponse`
        """
        http_info = self._send_authorized_mail_http_info(request)
        return self._call_api(**http_info)

    def send_authorized_mail_async_invoker(self, request):
        http_info = self._send_authorized_mail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _send_authorized_mail_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/mails/actions/send-by-authorization",
            "request_type": request.__class__.__name__,
            "response_type": "SendAuthorizedMailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_persistent_storage_async(self, request):
        r"""批量删除WKS存储

        批量删除WKS存储。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeletePersistentStorage
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchDeletePersistentStorageRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchDeletePersistentStorageResponse`
        """
        http_info = self._batch_delete_persistent_storage_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_persistent_storage_async_invoker(self, request):
        http_info = self._batch_delete_persistent_storage_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_persistent_storage_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/persistent-storages/actions/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeletePersistentStorageResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_or_update_storage_policy_statement_async(self, request):
        r"""新增或更新存储目录访问权限自定义策略

        新增或更新存储目录访问权限自定义策略(已存在自定义策略时会对已有策略更新)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateOrUpdateStoragePolicyStatement
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CreateOrUpdateStoragePolicyStatementRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CreateOrUpdateStoragePolicyStatementResponse`
        """
        http_info = self._create_or_update_storage_policy_statement_http_info(request)
        return self._call_api(**http_info)

    def create_or_update_storage_policy_statement_async_invoker(self, request):
        http_info = self._create_or_update_storage_policy_statement_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_or_update_storage_policy_statement_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/storages-policy/actions/create-statements",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOrUpdateStoragePolicyStatementResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_persistent_storage_async(self, request):
        r"""创建WKS存储

        创建WKS存储，目前仅支持创建 SFS3.0 容量型文件系统。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePersistentStorage
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CreatePersistentStorageRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CreatePersistentStorageResponse`
        """
        http_info = self._create_persistent_storage_http_info(request)
        return self._call_api(**http_info)

    def create_persistent_storage_async_invoker(self, request):
        http_info = self._create_persistent_storage_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_persistent_storage_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/persistent-storages",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePersistentStorageResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_share_folder_async(self, request):
        r"""创建共享存储目录

        创建共享存储目录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateShareFolder
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CreateShareFolderRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CreateShareFolderResponse`
        """
        http_info = self._create_share_folder_http_info(request)
        return self._call_api(**http_info)

    def create_share_folder_async_invoker(self, request):
        http_info = self._create_share_folder_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_share_folder_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/persistent-storages/{storage_id}/actions/create-share-folder",
            "request_type": request.__class__.__name__,
            "response_type": "CreateShareFolderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'storage_id' in local_var_params:
            path_params['storage_id'] = local_var_params['storage_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_persistent_storage_async(self, request):
        r"""删除WKS存储

        删除共享存储，只会解除NAS与文件系统之间的关联关系，不会删除文件系统和文件系统中的数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePersistentStorage
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.DeletePersistentStorageRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DeletePersistentStorageResponse`
        """
        http_info = self._delete_persistent_storage_http_info(request)
        return self._call_api(**http_info)

    def delete_persistent_storage_async_invoker(self, request):
        http_info = self._delete_persistent_storage_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_persistent_storage_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/persistent-storages/{storage_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePersistentStorageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_storage_claim_async(self, request):
        r"""删除共享目录

        删除共享存储目录。
        &gt; 需要删除绑定的用户及用户组，才能删除共享文目录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteStorageClaim
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.DeleteStorageClaimRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DeleteStorageClaimResponse`
        """
        http_info = self._delete_storage_claim_http_info(request)
        return self._call_api(**http_info)

    def delete_storage_claim_async_invoker(self, request):
        http_info = self._delete_storage_claim_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_storage_claim_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/persistent-storages/{storage_id}/actions/delete-storage-claim",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteStorageClaimResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'storage_id' in local_var_params:
            path_params['storage_id'] = local_var_params['storage_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_user_storage_attachment_async(self, request):
        r"""删除个人存储目录

        删除个人存储目录，个人目录中的数据也将永久删除且无法恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteUserStorageAttachment
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.DeleteUserStorageAttachmentRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DeleteUserStorageAttachmentResponse`
        """
        http_info = self._delete_user_storage_attachment_http_info(request)
        return self._call_api(**http_info)

    def delete_user_storage_attachment_async_invoker(self, request):
        http_info = self._delete_user_storage_attachment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_user_storage_attachment_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/persistent-storages/{storage_id}/actions/delete-user-attachment",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteUserStorageAttachmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'storage_id' in local_var_params:
            path_params['storage_id'] = local_var_params['storage_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_persistent_storage_async(self, request):
        r"""查询WKS存储

        查询WKS存储。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPersistentStorage
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListPersistentStorageRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListPersistentStorageResponse`
        """
        http_info = self._list_persistent_storage_http_info(request)
        return self._call_api(**http_info)

    def list_persistent_storage_async_invoker(self, request):
        http_info = self._list_persistent_storage_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_persistent_storage_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/persistent-storages",
            "request_type": request.__class__.__name__,
            "response_type": "ListPersistentStorageResponse"
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
        if 'storage_id' in local_var_params:
            query_params.append(('storage_id', local_var_params['storage_id']))
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_sfs3_storage_async(self, request):
        r"""查询SFS3.0存储

        查询SFS3.0存储。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSfs3Storage
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListSfs3StorageRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListSfs3StorageResponse`
        """
        http_info = self._list_sfs3_storage_http_info(request)
        return self._call_api(**http_info)

    def list_sfs3_storage_async_invoker(self, request):
        http_info = self._list_sfs3_storage_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_sfs3_storage_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/persistent-storages/actions/list-sfs-storages",
            "request_type": request.__class__.__name__,
            "response_type": "ListSfs3StorageResponse"
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

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_share_folder_async(self, request):
        r"""查询共享存储目录

        查询共享存储目录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListShareFolder
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListShareFolderRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListShareFolderResponse`
        """
        http_info = self._list_share_folder_http_info(request)
        return self._call_api(**http_info)

    def list_share_folder_async_invoker(self, request):
        http_info = self._list_share_folder_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_share_folder_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/persistent-storages/actions/list-share-folders",
            "request_type": request.__class__.__name__,
            "response_type": "ListShareFolderResponse"
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
        if 'storage_id' in local_var_params:
            query_params.append(('storage_id', local_var_params['storage_id']))
        if 'storage_claim_id' in local_var_params:
            query_params.append(('storage_claim_id', local_var_params['storage_claim_id']))
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_storage_assignment_async(self, request):
        r"""查询个人存储目录

        查询个人存储目录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListStorageAssignment
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListStorageAssignmentRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListStorageAssignmentResponse`
        """
        http_info = self._list_storage_assignment_http_info(request)
        return self._call_api(**http_info)

    def list_storage_assignment_async_invoker(self, request):
        http_info = self._list_storage_assignment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_storage_assignment_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/persistent-storages/actions/list-attachments",
            "request_type": request.__class__.__name__,
            "response_type": "ListStorageAssignmentResponse"
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
        if 'storage_id' in local_var_params:
            query_params.append(('storage_id', local_var_params['storage_id']))
        if 'claim_mode' in local_var_params:
            query_params.append(('claim_mode', local_var_params['claim_mode']))
        if 'storage_claim_id' in local_var_params:
            query_params.append(('storage_claim_id', local_var_params['storage_claim_id']))
        if 'attach' in local_var_params:
            query_params.append(('attach', local_var_params['attach']))
        if 'attach_type' in local_var_params:
            query_params.append(('attach_type', local_var_params['attach_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_storage_policy_statement_async(self, request):
        r"""查询存储目录访问权限策略

        查询存储目录访问权限策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListStoragePolicyStatement
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListStoragePolicyStatementRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListStoragePolicyStatementResponse`
        """
        http_info = self._list_storage_policy_statement_http_info(request)
        return self._call_api(**http_info)

    def list_storage_policy_statement_async_invoker(self, request):
        http_info = self._list_storage_policy_statement_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_storage_policy_statement_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/storages-policy/actions/list-statements",
            "request_type": request.__class__.__name__,
            "response_type": "ListStoragePolicyStatementResponse"
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

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_share_folder_assignment_async(self, request):
        r"""修改共享目录成员

        批量添加或者移除共享目录成员。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateShareFolderAssignment
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.UpdateShareFolderAssignmentRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UpdateShareFolderAssignmentResponse`
        """
        http_info = self._update_share_folder_assignment_http_info(request)
        return self._call_api(**http_info)

    def update_share_folder_assignment_async_invoker(self, request):
        http_info = self._update_share_folder_assignment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_share_folder_assignment_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/persistent-storages/{storage_id}/actions/assign-share-folder",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateShareFolderAssignmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'storage_id' in local_var_params:
            path_params['storage_id'] = local_var_params['storage_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_user_folder_assignment_async(self, request):
        r"""创建个人存储目录

        创建个人存储目录，已存在对应目录时，仅更新策略不会重复创建目录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateUserFolderAssignment
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.UpdateUserFolderAssignmentRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UpdateUserFolderAssignmentResponse`
        """
        http_info = self._update_user_folder_assignment_http_info(request)
        return self._call_api(**http_info)

    def update_user_folder_assignment_async_invoker(self, request):
        http_info = self._update_user_folder_assignment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_user_folder_assignment_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/persistent-storages/{storage_id}/actions/assign-folder",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateUserFolderAssignmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'storage_id' in local_var_params:
            path_params['storage_id'] = local_var_params['storage_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_policy_group_async(self, request):
        r"""新增策略组

        新增策略组，通过策略组能灵活的控制客户端访问与接入策略，如：文件、剪切板、会话等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePolicyGroup
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CreatePolicyGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CreatePolicyGroupResponse`
        """
        http_info = self._create_policy_group_http_info(request)
        return self._call_api(**http_info)

    def create_policy_group_async_invoker(self, request):
        http_info = self._create_policy_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_policy_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/policy-groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePolicyGroupResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_policy_template_async(self, request):
        r"""新增策略模板

        新增策略模板。策略模板创建好后，用户在创建策略组的时候，就可以根据已有策略模板按需调整配置，快速完成策略组的创建。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePolicyTemplate
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CreatePolicyTemplateRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CreatePolicyTemplateResponse`
        """
        http_info = self._create_policy_template_http_info(request)
        return self._call_api(**http_info)

    def create_policy_template_async_invoker(self, request):
        http_info = self._create_policy_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_policy_template_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/policy-templates",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePolicyTemplateResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_policy_group_async(self, request):
        r"""删除策略组

        删除指定策略组，包含策略组对应的策略信息以及应用对象信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePolicyGroup
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.DeletePolicyGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DeletePolicyGroupResponse`
        """
        http_info = self._delete_policy_group_http_info(request)
        return self._call_api(**http_info)

    def delete_policy_group_async_invoker(self, request):
        http_info = self._delete_policy_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_policy_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/policy-groups/{policy_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePolicyGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_group_id' in local_var_params:
            path_params['policy_group_id'] = local_var_params['policy_group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_policy_template_async(self, request):
        r"""删除策略模板

        删除指定策略模板，包含策略模板对应的策略信息以及应用对象信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePolicyTemplate
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.DeletePolicyTemplateRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DeletePolicyTemplateResponse`
        """
        http_info = self._delete_policy_template_http_info(request)
        return self._call_api(**http_info)

    def delete_policy_template_async_invoker(self, request):
        http_info = self._delete_policy_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_policy_template_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/policy-templates/{policy_template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePolicyTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_template_id' in local_var_params:
            path_params['policy_template_id'] = local_var_params['policy_template_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_policy_group_async(self, request):
        r"""查询策略组列表

        查询策略组概要信息列表,包括应用对象和详细策略项。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPolicyGroup
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListPolicyGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListPolicyGroupResponse`
        """
        http_info = self._list_policy_group_http_info(request)
        return self._call_api(**http_info)

    def list_policy_group_async_invoker(self, request):
        http_info = self._list_policy_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_policy_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/policy-groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListPolicyGroupResponse"
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
        if 'policy_group_name' in local_var_params:
            query_params.append(('policy_group_name', local_var_params['policy_group_name']))
        if 'policy_group_type' in local_var_params:
            query_params.append(('policy_group_type', local_var_params['policy_group_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_policy_group_detail_info_async(self, request):
        r"""查询策略组详情列表

        包含策略信息以及应用对象的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPolicyGroupDetailInfo
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListPolicyGroupDetailInfoRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListPolicyGroupDetailInfoResponse`
        """
        http_info = self._list_policy_group_detail_info_http_info(request)
        return self._call_api(**http_info)

    def list_policy_group_detail_info_async_invoker(self, request):
        http_info = self._list_policy_group_detail_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_policy_group_detail_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/policy-groups/show/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ListPolicyGroupDetailInfoResponse"
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
        if 'policy_group_name' in local_var_params:
            query_params.append(('policy_group_name', local_var_params['policy_group_name']))
        if 'policy_group_type' in local_var_params:
            query_params.append(('policy_group_type', local_var_params['policy_group_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_policy_of_policy_group_async(self, request):
        r"""查询策略组中的策略项

        查询指定策略组内的策略项。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPolicyOfPolicyGroup
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListPolicyOfPolicyGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListPolicyOfPolicyGroupResponse`
        """
        http_info = self._list_policy_of_policy_group_http_info(request)
        return self._call_api(**http_info)

    def list_policy_of_policy_group_async_invoker(self, request):
        http_info = self._list_policy_of_policy_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_policy_of_policy_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/policy-groups/{policy_group_id}/policy",
            "request_type": request.__class__.__name__,
            "response_type": "ListPolicyOfPolicyGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_group_id' in local_var_params:
            path_params['policy_group_id'] = local_var_params['policy_group_id']

        query_params = []
        if 'policy_type' in local_var_params:
            query_params.append(('policy_type', local_var_params['policy_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_policy_template_async(self, request):
        r"""查询策略模板列表

        查询策略模板概要信息列表，包含策略信息以及应用对象信息。用户在创建策略组的时候，可以根据已有策略模板按需调整配置，快速完成策略组的创建。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPolicyTemplate
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListPolicyTemplateRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListPolicyTemplateResponse`
        """
        http_info = self._list_policy_template_http_info(request)
        return self._call_api(**http_info)

    def list_policy_template_async_invoker(self, request):
        http_info = self._list_policy_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_policy_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/policy-templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListPolicyTemplateResponse"
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
        if 'policy_group_name' in local_var_params:
            query_params.append(('policy_group_name', local_var_params['policy_group_name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_targets_of_policy_group_async(self, request):
        r"""查询策略组应用对象

        查询指定策略组所应用的对象。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTargetsOfPolicyGroup
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListTargetsOfPolicyGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListTargetsOfPolicyGroupResponse`
        """
        http_info = self._list_targets_of_policy_group_http_info(request)
        return self._call_api(**http_info)

    def list_targets_of_policy_group_async_invoker(self, request):
        http_info = self._list_targets_of_policy_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_targets_of_policy_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/policy-groups/{policy_group_id}/target",
            "request_type": request.__class__.__name__,
            "response_type": "ListTargetsOfPolicyGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_group_id' in local_var_params:
            path_params['policy_group_id'] = local_var_params['policy_group_id']

        query_params = []
        if 'target_type' in local_var_params:
            query_params.append(('target_type', local_var_params['target_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_original_policy_info_async(self, request):
        r"""查询初始策略项

        查询初始策略项，初始策略项是所有协议策略配置项的默认配置，用户可以在初始策略项的基础上根据需求修改指定的配置，创建新的策略组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOriginalPolicyInfo
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ShowOriginalPolicyInfoRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ShowOriginalPolicyInfoResponse`
        """
        http_info = self._show_original_policy_info_http_info(request)
        return self._call_api(**http_info)

    def show_original_policy_info_async_invoker(self, request):
        http_info = self._show_original_policy_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_original_policy_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/policy-groups/actions/list-original-policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOriginalPolicyInfoResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_policy_group_async(self, request):
        r"""查询策略组详情

        根据策略组ID查询策略组详细信息，包含策略信息以及应用对象信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPolicyGroup
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ShowPolicyGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ShowPolicyGroupResponse`
        """
        http_info = self._show_policy_group_http_info(request)
        return self._call_api(**http_info)

    def show_policy_group_async_invoker(self, request):
        http_info = self._show_policy_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_policy_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/policy-groups/{policy_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPolicyGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_group_id' in local_var_params:
            path_params['policy_group_id'] = local_var_params['policy_group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_policy_group_async(self, request):
        r"""修改策略组

        修改指定策略组的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePolicyGroup
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.UpdatePolicyGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UpdatePolicyGroupResponse`
        """
        http_info = self._update_policy_group_http_info(request)
        return self._call_api(**http_info)

    def update_policy_group_async_invoker(self, request):
        http_info = self._update_policy_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_policy_group_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/policy-groups/{policy_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePolicyGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_group_id' in local_var_params:
            path_params['policy_group_id'] = local_var_params['policy_group_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_policy_template_async(self, request):
        r"""修改策略模板

        修改指定策略模板的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePolicyTemplate
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.UpdatePolicyTemplateRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UpdatePolicyTemplateResponse`
        """
        http_info = self._update_policy_template_http_info(request)
        return self._call_api(**http_info)

    def update_policy_template_async_invoker(self, request):
        http_info = self._update_policy_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_policy_template_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/policy-templates/{policy_template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePolicyTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_template_id' in local_var_params:
            path_params['policy_template_id'] = local_var_params['policy_template_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_privacy_statement_async(self, request):
        r"""查询最新版本的隐私声明

        查询最新版本的隐私声明。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPrivacyStatement
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ShowPrivacyStatementRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ShowPrivacyStatementResponse`
        """
        http_info = self._show_privacy_statement_http_info(request)
        return self._call_api(**http_info)

    def show_privacy_statement_async_invoker(self, request):
        http_info = self._show_privacy_statement_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_privacy_statement_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/privacy-statement",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPrivacyStatementResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def sign_privacy_statement_async(self, request):
        r"""签署隐私声明

        签署隐私声明。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SignPrivacyStatement
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.SignPrivacyStatementRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.SignPrivacyStatementResponse`
        """
        http_info = self._sign_privacy_statement_http_info(request)
        return self._call_api(**http_info)

    def sign_privacy_statement_async_invoker(self, request):
        http_info = self._sign_privacy_statement_http_info(request)
        return AsyncInvoker(self, http_info)

    def _sign_privacy_statement_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/privacy-statement",
            "request_type": request.__class__.__name__,
            "response_type": "SignPrivacyStatementResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def check_quota_async(self, request):
        r"""配额校验

        配额校验，购买服务器前可用调用该接口，校验本次创建服务器资源是否足够。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckQuota
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CheckQuotaRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CheckQuotaResponse`
        """
        http_info = self._check_quota_http_info(request)
        return self._call_api(**http_info)

    def check_quota_async_invoker(self, request):
        http_info = self._check_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/check/quota",
            "request_type": request.__class__.__name__,
            "response_type": "CheckQuotaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_id' in local_var_params:
            query_params.append(('product_id', local_var_params['product_id']))
        if 'flavor_id' in local_var_params:
            query_params.append(('flavor_id', local_var_params['flavor_id']))
        if 'subscription_num' in local_var_params:
            query_params.append(('subscription_num', local_var_params['subscription_num']))
        if 'disk_size' in local_var_params:
            query_params.append(('disk_size', local_var_params['disk_size']))
        if 'disk_num' in local_var_params:
            query_params.append(('disk_num', local_var_params['disk_num']))
        if 'is_period' in local_var_params:
            query_params.append(('is_period', local_var_params['is_period']))
        if 'deh_id' in local_var_params:
            query_params.append(('deh_id', local_var_params['deh_id']))
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_or_update_scaling_policy_async(self, request):
        r"""新增/修改弹性伸缩策略

        新增/修改弹性伸缩策略,仅按需的服务器支持。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateOrUpdateScalingPolicy
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CreateOrUpdateScalingPolicyRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CreateOrUpdateScalingPolicyResponse`
        """
        http_info = self._create_or_update_scaling_policy_http_info(request)
        return self._call_api(**http_info)

    def create_or_update_scaling_policy_async_invoker(self, request):
        http_info = self._create_or_update_scaling_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_or_update_scaling_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/scaling-policy",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOrUpdateScalingPolicyResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_scaling_policy_async(self, request):
        r"""删除弹性伸缩策略

        删除弹性伸缩策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteScalingPolicy
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.DeleteScalingPolicyRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DeleteScalingPolicyResponse`
        """
        http_info = self._delete_scaling_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_scaling_policy_async_invoker(self, request):
        http_info = self._delete_scaling_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_scaling_policy_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/scaling-policy",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteScalingPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'server_group_id' in local_var_params:
            query_params.append(('server_group_id', local_var_params['server_group_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_scaling_policy_async(self, request):
        r"""查询服务器组弹性伸缩策略

        查询服务器组弹性伸缩策略,如果服务器未配置策略时响应默认策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowScalingPolicy
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ShowScalingPolicyRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ShowScalingPolicyResponse`
        """
        http_info = self._show_scaling_policy_http_info(request)
        return self._call_api(**http_info)

    def show_scaling_policy_async_invoker(self, request):
        http_info = self._show_scaling_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_scaling_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/scaling-policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowScalingPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'server_group_id' in local_var_params:
            query_params.append(('server_group_id', local_var_params['server_group_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_schedule_task_async(self, request):
        r"""批量删除定时任务

        批量删除定时任务，忽略不存在的服务器组并且返回成功响应。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteScheduleTask
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchDeleteScheduleTaskRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchDeleteScheduleTaskResponse`
        """
        http_info = self._batch_delete_schedule_task_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_schedule_task_async_invoker(self, request):
        http_info = self._batch_delete_schedule_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_schedule_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/schedule-task/actions/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteScheduleTaskResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_schedule_task_async(self, request):
        r"""新增定时任务

        新增定时任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateScheduleTask
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CreateScheduleTaskRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CreateScheduleTaskResponse`
        """
        http_info = self._create_schedule_task_http_info(request)
        return self._call_api(**http_info)

    def create_schedule_task_async_invoker(self, request):
        http_info = self._create_schedule_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_schedule_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/schedule-task",
            "request_type": request.__class__.__name__,
            "response_type": "CreateScheduleTaskResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_schedule_task_async(self, request):
        r"""删除任务

        删除任务，忽略不存在的任务并且返回成功响应。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteScheduleTask
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.DeleteScheduleTaskRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DeleteScheduleTaskResponse`
        """
        http_info = self._delete_schedule_task_http_info(request)
        return self._call_api(**http_info)

    def delete_schedule_task_async_invoker(self, request):
        http_info = self._delete_schedule_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_schedule_task_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/schedule-task/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteScheduleTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_future_executions_async(self, request):
        r"""未来执行的具体时间列表

        未来执行的具体时间列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFutureExecutions
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListFutureExecutionsRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListFutureExecutionsResponse`
        """
        http_info = self._list_future_executions_http_info(request)
        return self._call_api(**http_info)

    def list_future_executions_async_invoker(self, request):
        http_info = self._list_future_executions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_future_executions_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/schedule-task/future-executions",
            "request_type": request.__class__.__name__,
            "response_type": "ListFutureExecutionsResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_schedule_tasks_async(self, request):
        r"""查询定时任务列表

        查询定时任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListScheduleTasks
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListScheduleTasksRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListScheduleTasksResponse`
        """
        http_info = self._list_schedule_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_schedule_tasks_async_invoker(self, request):
        http_info = self._list_schedule_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_schedule_tasks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/schedule-task",
            "request_type": request.__class__.__name__,
            "response_type": "ListScheduleTasksResponse"
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
        if 'task_name' in local_var_params:
            query_params.append(('task_name', local_var_params['task_name']))
        if 'task_type' in local_var_params:
            query_params.append(('task_type', local_var_params['task_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_task_execute_detail_async(self, request):
        r"""查询定时任务执行子任务列表

        查询定时任务执行子任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTaskExecuteDetail
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListTaskExecuteDetailRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListTaskExecuteDetailResponse`
        """
        http_info = self._list_task_execute_detail_http_info(request)
        return self._call_api(**http_info)

    def list_task_execute_detail_async_invoker(self, request):
        http_info = self._list_task_execute_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_task_execute_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/schedule-task/{execute_history_id}/execute-detail",
            "request_type": request.__class__.__name__,
            "response_type": "ListTaskExecuteDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'execute_history_id' in local_var_params:
            path_params['execute_history_id'] = local_var_params['execute_history_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_task_execute_history_async(self, request):
        r"""查询定时任务执行列表

        查询定时任务执行列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTaskExecuteHistory
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListTaskExecuteHistoryRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListTaskExecuteHistoryResponse`
        """
        http_info = self._list_task_execute_history_http_info(request)
        return self._call_api(**http_info)

    def list_task_execute_history_async_invoker(self, request):
        http_info = self._list_task_execute_history_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_task_execute_history_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/schedule-task/{task_id}/execute-history",
            "request_type": request.__class__.__name__,
            "response_type": "ListTaskExecuteHistoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_schedule_task_async(self, request):
        r"""查询指定定时任务详情

        查询指定定时任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowScheduleTask
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ShowScheduleTaskRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ShowScheduleTaskResponse`
        """
        http_info = self._show_schedule_task_http_info(request)
        return self._call_api(**http_info)

    def show_schedule_task_async_invoker(self, request):
        http_info = self._show_schedule_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_schedule_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/schedule-task/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowScheduleTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_schedule_task_async(self, request):
        r"""修改定时任务

        修改定时任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateScheduleTask
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.UpdateScheduleTaskRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UpdateScheduleTaskResponse`
        """
        http_info = self._update_schedule_task_http_info(request)
        return self._call_api(**http_info)

    def update_schedule_task_async_invoker(self, request):
        http_info = self._update_schedule_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_schedule_task_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/schedule-task/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateScheduleTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_change_server_image_async(self, request):
        r"""批量修改服务器的镜像

        批量修改服务器的镜像。
        &gt; - 服务器的镜像和服务器组的镜像不一样时，支持服务器的镜像切换为服务器组的镜像，并且仅允许同等镜像进行切换，例如：同操作系统，免费镜像切换，同源同价的付费镜像切换。如果服务器组的镜像和服务器的镜像为非同等镜像，建议您直接购买新的服务器，删除或者退订老的服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchChangeServerImage
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchChangeServerImageRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchChangeServerImageResponse`
        """
        http_info = self._batch_change_server_image_http_info(request)
        return self._call_api(**http_info)

    def batch_change_server_image_async_invoker(self, request):
        http_info = self._batch_change_server_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_change_server_image_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-servers/actions/batch-change-image",
            "request_type": request.__class__.__name__,
            "response_type": "BatchChangeServerImageResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_change_server_maintain_mode_async(self, request):
        r"""标记服务器维护状态

        标记服务器维护状态，处于维护状态中的服务器不再分配流量。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchChangeServerMaintainMode
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchChangeServerMaintainModeRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchChangeServerMaintainModeResponse`
        """
        http_info = self._batch_change_server_maintain_mode_http_info(request)
        return self._call_api(**http_info)

    def batch_change_server_maintain_mode_async_invoker(self, request):
        http_info = self._batch_change_server_maintain_mode_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_change_server_maintain_mode_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/app-servers/actions/batch-maint",
            "request_type": request.__class__.__name__,
            "response_type": "BatchChangeServerMaintainModeResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_server_async(self, request):
        r"""批量删除服务器

        批量删除服务器。
        &gt; - [仅支持删除按需订购的服务器，包周期订购的服务器需要到Console界面进行退订，订单退订成功后服务器将会自动删除。](tag:HW)[批量删除服务器。](tag:HCS)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteServer
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchDeleteServerRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchDeleteServerResponse`
        """
        http_info = self._batch_delete_server_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_server_async_invoker(self, request):
        http_info = self._batch_delete_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_server_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-servers/actions/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteServerResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_migrate_hosts_server_async(self, request):
        r"""迁移云办公主机下面的服务器到目标云办公主机

        迁移云办公主机下面的服务器到目标云办公主机。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchMigrateHostsServer
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchMigrateHostsServerRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchMigrateHostsServerResponse`
        """
        http_info = self._batch_migrate_hosts_server_http_info(request)
        return self._call_api(**http_info)

    def batch_migrate_hosts_server_async_invoker(self, request):
        http_info = self._batch_migrate_hosts_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_migrate_hosts_server_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/app-servers/hosts/batch-migrate",
            "request_type": request.__class__.__name__,
            "response_type": "BatchMigrateHostsServerResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_reboot_server_async(self, request):
        r"""重启服务器

        重启服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchRebootServer
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchRebootServerRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchRebootServerResponse`
        """
        http_info = self._batch_reboot_server_http_info(request)
        return self._call_api(**http_info)

    def batch_reboot_server_async_invoker(self, request):
        http_info = self._batch_reboot_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_reboot_server_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/app-servers/actions/batch-reboot",
            "request_type": request.__class__.__name__,
            "response_type": "BatchRebootServerResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_reinstall_server_async(self, request):
        r"""批量重装服务器

        批量重装服务器。
        &gt; - 使用服务器原有的镜像进行重装，当服务器异常无法恢复时或者服务器运行时间久了，性能下降时，可选择重建服务器。注意：重装时系统盘的数据将会被清理掉。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchReinstallServer
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchReinstallServerRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchReinstallServerResponse`
        """
        http_info = self._batch_reinstall_server_http_info(request)
        return self._call_api(**http_info)

    def batch_reinstall_server_async_invoker(self, request):
        http_info = self._batch_reinstall_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_reinstall_server_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-servers/actions/batch-reinstall",
            "request_type": request.__class__.__name__,
            "response_type": "BatchReinstallServerResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_rejoin_domain_async(self, request):
        r"""批量服务器重新加域

        批量服务器重新加入AD域，一般用于解决服务器脱域的情况使用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchRejoinDomain
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchRejoinDomainRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchRejoinDomainResponse`
        """
        http_info = self._batch_rejoin_domain_http_info(request)
        return self._call_api(**http_info)

    def batch_rejoin_domain_async_invoker(self, request):
        http_info = self._batch_rejoin_domain_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_rejoin_domain_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/app-servers/actions/batch-rejoin-domain",
            "request_type": request.__class__.__name__,
            "response_type": "BatchRejoinDomainResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_start_server_async(self, request):
        r"""启动服务器

        启动服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchStartServer
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchStartServerRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchStartServerResponse`
        """
        http_info = self._batch_start_server_http_info(request)
        return self._call_api(**http_info)

    def batch_start_server_async_invoker(self, request):
        http_info = self._batch_start_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_start_server_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/app-servers/actions/batch-start",
            "request_type": request.__class__.__name__,
            "response_type": "BatchStartServerResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_stop_server_async(self, request):
        r"""关闭服务器

        关闭服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchStopServer
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchStopServerRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchStopServerResponse`
        """
        http_info = self._batch_stop_server_http_info(request)
        return self._call_api(**http_info)

    def batch_stop_server_async_invoker(self, request):
        http_info = self._batch_stop_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_stop_server_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/app-servers/actions/batch-stop",
            "request_type": request.__class__.__name__,
            "response_type": "BatchStopServerResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_update_tsvi_async(self, request):
        r"""批量更新服务器虚拟会话IP配置

        批量更新服务器虚拟会话IP配置，按需重启机器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchUpdateTsvi
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchUpdateTsviRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchUpdateTsviResponse`
        """
        http_info = self._batch_update_tsvi_http_info(request)
        return self._call_api(**http_info)

    def batch_update_tsvi_async_invoker(self, request):
        http_info = self._batch_update_tsvi_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_update_tsvi_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/app-servers/actions/batch-update-tsvi",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateTsviResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_upgrade_hda_version_async(self, request):
        r"""批量升级服务器HDA版本

        批量升级服务器HDA版本。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchUpgradeHdaVersion
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchUpgradeHdaVersionRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchUpgradeHdaVersionResponse`
        """
        http_info = self._batch_upgrade_hda_version_http_info(request)
        return self._call_api(**http_info)

    def batch_upgrade_hda_version_async_invoker(self, request):
        http_info = self._batch_upgrade_hda_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_upgrade_hda_version_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/app-servers/access-agent/actions/upgrade",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpgradeHdaVersionResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def change_server_image_async(self, request):
        r"""修改服务器的镜像

        修改服务器的镜像。
        &gt; - 服务器的镜像和服务器组的镜像不一样时，支持服务器的镜像切换为服务器组的镜像，并且仅允许同等镜像进行切换，例如：同操作系统，免费镜像切换，同源同价的付费镜像切换。如果服务器组的镜像和服务器的镜像为非同等镜像，建议您直接购买新的服务器，删除或者退订老的服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeServerImage
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ChangeServerImageRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ChangeServerImageResponse`
        """
        http_info = self._change_server_image_http_info(request)
        return self._call_api(**http_info)

    def change_server_image_async_invoker(self, request):
        http_info = self._change_server_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_server_image_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-servers/{server_id}/actions/change-image",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeServerImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_app_servers_async(self, request):
        r"""创建云服务器

        创建云服务器接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAppServers
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CreateAppServersRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CreateAppServersResponse`
        """
        http_info = self._create_app_servers_http_info(request)
        return self._call_api(**http_info)

    def create_app_servers_async_invoker(self, request):
        http_info = self._create_app_servers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_app_servers_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-servers/actions/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAppServersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_linked_id' in local_var_params:
            header_params['X-Linked-Id'] = local_var_params['x_linked_id']
        if 'service_transaction_id' in local_var_params:
            header_params['Service-Transaction-Id'] = local_var_params['service_transaction_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_server_async(self, request):
        r"""删除服务器

        删除服务器，忽略不存在的服务器并且返回成功响应。订单退订成功后调用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteServer
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.DeleteServerRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DeleteServerResponse`
        """
        http_info = self._delete_server_http_info(request)
        return self._call_api(**http_info)

    def delete_server_async_invoker(self, request):
        http_info = self._delete_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_server_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/app-servers/{server_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_access_agent_latest_version_async(self, request):
        r"""查询租户的所有HDA最新版本

        查询租户的所有HDA最新版本。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAccessAgentLatestVersion
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListAccessAgentLatestVersionRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListAccessAgentLatestVersionResponse`
        """
        http_info = self._list_access_agent_latest_version_http_info(request)
        return self._call_api(**http_info)

    def list_access_agent_latest_version_async_invoker(self, request):
        http_info = self._list_access_agent_latest_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_access_agent_latest_version_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-servers/access-agent/actions/show-latest-version",
            "request_type": request.__class__.__name__,
            "response_type": "ListAccessAgentLatestVersionResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_server_hda_details_async(self, request):
        r"""查询服务器的HDA相关信息

        查询服务器的HDA相关信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServerHdaDetails
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListServerHdaDetailsRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListServerHdaDetailsResponse`
        """
        http_info = self._list_server_hda_details_http_info(request)
        return self._call_api(**http_info)

    def list_server_hda_details_async_invoker(self, request):
        http_info = self._list_server_hda_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_server_hda_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-servers/access-agent/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListServerHdaDetailsResponse"
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
        if 'server_group_id' in local_var_params:
            query_params.append(('server_group_id', local_var_params['server_group_id']))
        if 'server_name' in local_var_params:
            query_params.append(('server_name', local_var_params['server_name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_server_hda_upgrade_records_async(self, request):
        r"""查询服务器的HDA升级跟踪记录

        查询服务器的HDA升级跟踪记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServerHdaUpgradeRecords
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListServerHdaUpgradeRecordsRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListServerHdaUpgradeRecordsResponse`
        """
        http_info = self._list_server_hda_upgrade_records_http_info(request)
        return self._call_api(**http_info)

    def list_server_hda_upgrade_records_async_invoker(self, request):
        http_info = self._list_server_hda_upgrade_records_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_server_hda_upgrade_records_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-servers/access-agent/upgrade-record",
            "request_type": request.__class__.__name__,
            "response_type": "ListServerHdaUpgradeRecordsResponse"
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

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_server_metric_data_async(self, request):
        r"""查询指定时间范围指定指标的指定粒度的监控数据

        查询指定时间范围指定指标的指定粒度的监控数据，可以通过参数指定需要查询的数据维度。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServerMetricData
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListServerMetricDataRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListServerMetricDataResponse`
        """
        http_info = self._list_server_metric_data_http_info(request)
        return self._call_api(**http_info)

    def list_server_metric_data_async_invoker(self, request):
        http_info = self._list_server_metric_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_server_metric_data_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-servers/server-metric-data/{server_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListServerMetricDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'metric_name' in local_var_params:
            query_params.append(('metric_name', local_var_params['metric_name']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))
        if 'period' in local_var_params:
            query_params.append(('period', local_var_params['period']))
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_servers_async(self, request):
        r"""查询服务器列表

        查询服务器列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServers
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListServersRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListServersResponse`
        """
        http_info = self._list_servers_http_info(request)
        return self._call_api(**http_info)

    def list_servers_async_invoker(self, request):
        http_info = self._list_servers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_servers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-servers",
            "request_type": request.__class__.__name__,
            "response_type": "ListServersResponse"
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
        if 'server_group_id' in local_var_params:
            query_params.append(('server_group_id', local_var_params['server_group_id']))
        if 'server_name' in local_var_params:
            query_params.append(('server_name', local_var_params['server_name']))
        if 'machine_name' in local_var_params:
            query_params.append(('machine_name', local_var_params['machine_name']))
        if 'ip_addr' in local_var_params:
            query_params.append(('ip_addr', local_var_params['ip_addr']))
        if 'server_id' in local_var_params:
            query_params.append(('server_id', local_var_params['server_id']))
        if 'maintain_status' in local_var_params:
            query_params.append(('maintain_status', local_var_params['maintain_status']))
        if 'scaling_auto_create' in local_var_params:
            query_params.append(('scaling_auto_create', local_var_params['scaling_auto_create']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def reinstall_server_async(self, request):
        r"""重装服务器

        重装服务器。
        &gt; - 使用服务器原有的镜像进行重装，当服务器异常无法恢复时或者服务器运行时间久了，性能下降时，可选择重建服务器。注意：重装时系统盘的数据将会被清理掉。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ReinstallServer
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ReinstallServerRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ReinstallServerResponse`
        """
        http_info = self._reinstall_server_http_info(request)
        return self._call_api(**http_info)

    def reinstall_server_async_invoker(self, request):
        http_info = self._reinstall_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reinstall_server_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-servers/{server_id}/actions/reinstall",
            "request_type": request.__class__.__name__,
            "response_type": "ReinstallServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_access_agent_latest_version_async(self, request):
        r"""查询租户的HDA最新版本

        查询租户的HDA最新版本。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAccessAgentLatestVersion
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ShowAccessAgentLatestVersionRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ShowAccessAgentLatestVersionResponse`
        """
        http_info = self._show_access_agent_latest_version_http_info(request)
        return self._call_api(**http_info)

    def show_access_agent_latest_version_async_invoker(self, request):
        http_info = self._show_access_agent_latest_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_access_agent_latest_version_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-servers/access-agent/latest-version",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAccessAgentLatestVersionResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_hda_upgrade_flag_async(self, request):
        r"""查询HDA升级提醒标识

        查询HDA升级提醒标识(仅内部访问使用)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHdaUpgradeFlag
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ShowHdaUpgradeFlagRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ShowHdaUpgradeFlagResponse`
        """
        http_info = self._show_hda_upgrade_flag_http_info(request)
        return self._call_api(**http_info)

    def show_hda_upgrade_flag_async_invoker(self, request):
        http_info = self._show_hda_upgrade_flag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_hda_upgrade_flag_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-servers/access-agent/upgrade-flag",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHdaUpgradeFlagResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_server_async(self, request):
        r"""查询指定服务器

        查询指定的服务器当前这个接口的查询数据和list查询的一致。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServer
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ShowServerRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ShowServerResponse`
        """
        http_info = self._show_server_http_info(request)
        return self._call_api(**http_info)

    def show_server_async_invoker(self, request):
        http_info = self._show_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_server_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-servers/{server_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_server_metric_data_async(self, request):
        r"""查询云应用服务器监控信息

        该接口可获取某一计算机在一段时间段(范围：1小时到30天)的数据信息（例如CPU占用率、内存占用率、用户的在线时间段等），最长数据保存时间不能超过180天。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServerMetricData
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ShowServerMetricDataRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ShowServerMetricDataResponse`
        """
        http_info = self._show_server_metric_data_http_info(request)
        return self._call_api(**http_info)

    def show_server_metric_data_async_invoker(self, request):
        http_info = self._show_server_metric_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_server_metric_data_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-servers/metric-data/{server_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowServerMetricDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'metric_name' in local_var_params:
            query_params.append(('metric_name', local_var_params['metric_name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_server_vnc_async(self, request):
        r"""获取VNC远程登录地址

        获取VNC远程登录地址。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServerVnc
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ShowServerVncRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ShowServerVncResponse`
        """
        http_info = self._show_server_vnc_http_info(request)
        return self._call_api(**http_info)

    def show_server_vnc_async_invoker(self, request):
        http_info = self._show_server_vnc_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_server_vnc_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-servers/{server_id}/actions/vnc",
            "request_type": request.__class__.__name__,
            "response_type": "ShowServerVncResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_server_async(self, request):
        r"""修改服务器

        修改服务器。
        &gt; - 服务器的状态修改为维护模式后，用户打开应用，选择可用的服务器进行接入的时候，会过滤掉处于维护模式的服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateServer
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.UpdateServerRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UpdateServerResponse`
        """
        http_info = self._update_server_http_info(request)
        return self._call_api(**http_info)

    def update_server_async_invoker(self, request):
        http_info = self._update_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_server_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/app-servers/{server_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_server_group_async(self, request):
        r"""创建服务器组

        创建服务器组。
        &gt; - 服务器组是一组相同配置的服务器集合，服务器组内的服务器使用同一镜像创建，配置相同，运行相同的应用程序。用户在打开云应用时，会根据调度规则选取组内的一台可用服务器进行连接。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateServerGroup
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CreateServerGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CreateServerGroupResponse`
        """
        http_info = self._create_server_group_http_info(request)
        return self._call_api(**http_info)

    def create_server_group_async_invoker(self, request):
        http_info = self._create_server_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_server_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-server-groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateServerGroupResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_server_groups_async(self, request):
        r"""删除服务器组

        删除服务器组。
        - &gt; 删除服务器组之前，需要先删除服务器组内的所有服务器。如果传服务器组已被删除，重复执行删除，则返回成功响应。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteServerGroups
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.DeleteServerGroupsRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DeleteServerGroupsResponse`
        """
        http_info = self._delete_server_groups_http_info(request)
        return self._call_api(**http_info)

    def delete_server_groups_async_invoker(self, request):
        http_info = self._delete_server_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_server_groups_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/app-server-groups/{server_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteServerGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_group_id' in local_var_params:
            path_params['server_group_id'] = local_var_params['server_group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_server_groups_async(self, request):
        r"""查询服务器组列表

        查询服务器组列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServerGroups
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListServerGroupsRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListServerGroupsResponse`
        """
        http_info = self._list_server_groups_http_info(request)
        return self._call_api(**http_info)

    def list_server_groups_async_invoker(self, request):
        http_info = self._list_server_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_server_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-server-groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListServerGroupsResponse"
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
        if 'server_group_name' in local_var_params:
            query_params.append(('server_group_name', local_var_params['server_group_name']))
        if 'server_group_id' in local_var_params:
            query_params.append(('server_group_id', local_var_params['server_group_id']))
        if 'app_type' in local_var_params:
            query_params.append(('app_type', local_var_params['app_type']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'is_secondary_server_group' in local_var_params:
            query_params.append(('is_secondary_server_group', local_var_params['is_secondary_server_group']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_tenant_server_groups_async(self, request):
        r"""查询租户服务器组基础信息列表

        查询租户服务器组基础信息列表(用于创建应用组时绑定服务器组)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTenantServerGroups
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListTenantServerGroupsRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListTenantServerGroupsResponse`
        """
        http_info = self._list_tenant_server_groups_http_info(request)
        return self._call_api(**http_info)

    def list_tenant_server_groups_async_invoker(self, request):
        http_info = self._list_tenant_server_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tenant_server_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-server-groups/actions/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListTenantServerGroupsResponse"
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
        if 'sever_group_name' in local_var_params:
            query_params.append(('sever_group_name', local_var_params['sever_group_name']))
        if 'app_type' in local_var_params:
            query_params.append(('app_type', local_var_params['app_type']))
        if 'is_secondary_server_group' in local_var_params:
            query_params.append(('is_secondary_server_group', local_var_params['is_secondary_server_group']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_server_group_async(self, request):
        r"""查询指定服务器组

        查询指定的服务器组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServerGroup
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ShowServerGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ShowServerGroupResponse`
        """
        http_info = self._show_server_group_http_info(request)
        return self._call_api(**http_info)

    def show_server_group_async_invoker(self, request):
        http_info = self._show_server_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_server_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-server-groups/{server_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowServerGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_group_id' in local_var_params:
            path_params['server_group_id'] = local_var_params['server_group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_server_group_restrict_async(self, request):
        r"""指定租户服务器组限制查询

        指定租户服务器组限制查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServerGroupRestrict
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ShowServerGroupRestrictRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ShowServerGroupRestrictResponse`
        """
        http_info = self._show_server_group_restrict_http_info(request)
        return self._call_api(**http_info)

    def show_server_group_restrict_async_invoker(self, request):
        http_info = self._show_server_group_restrict_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_server_group_restrict_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-server-groups/resources/restrict",
            "request_type": request.__class__.__name__,
            "response_type": "ShowServerGroupRestrictResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_server_group_state_async(self, request):
        r"""查询指定服务器组内服务器状态

        查询指定的服务器组内服务器状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServerGroupState
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ShowServerGroupStateRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ShowServerGroupStateResponse`
        """
        http_info = self._show_server_group_state_http_info(request)
        return self._call_api(**http_info)

    def show_server_group_state_async_invoker(self, request):
        http_info = self._show_server_group_state_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_server_group_state_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/app-server-groups/{server_group_id}/state",
            "request_type": request.__class__.__name__,
            "response_type": "ShowServerGroupStateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_group_id' in local_var_params:
            path_params['server_group_id'] = local_var_params['server_group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_server_group_async(self, request):
        r"""修改服务器组

        修改服务器组。
        - &gt; 修改服务器组的镜像，系统盘大小，OU信息后，已创建的服务器配置不变，新添加的服务器会使用新的配置创建。修改最大会话数后，用户接入服务器组时，会按照最新的配置进行路由计算。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateServerGroup
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.UpdateServerGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UpdateServerGroupResponse`
        """
        http_info = self._update_server_group_http_info(request)
        return self._call_api(**http_info)

    def update_server_group_async_invoker(self, request):
        http_info = self._update_server_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_server_group_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/app-server-groups/{server_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateServerGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_group_id' in local_var_params:
            path_params['server_group_id'] = local_var_params['server_group_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def validate_server_group_async(self, request):
        r"""校验服务器组

        校验服务器组是否符合指定的规则。
        1. 校验服务器组名称是否符合规则。
        2. 校验服务器组名称是否重复。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ValidateServerGroup
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ValidateServerGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ValidateServerGroupResponse`
        """
        http_info = self._validate_server_group_http_info(request)
        return self._call_api(**http_info)

    def validate_server_group_async_invoker(self, request):
        http_info = self._validate_server_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _validate_server_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/app-server-groups/rules/validate",
            "request_type": request.__class__.__name__,
            "response_type": "ValidateServerGroupResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def export_app_connection_async(self, request):
        r"""导出应用使用记录

        导出应用使用记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportAppConnection
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ExportAppConnectionRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ExportAppConnectionResponse`
        """
        http_info = self._export_app_connection_http_info(request)
        return self._call_api(**http_info)

    def export_app_connection_async_invoker(self, request):
        http_info = self._export_app_connection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _export_app_connection_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/session/app-connection/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportAppConnectionResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def export_sessions_async(self, request):
        r"""导出用户会话列表

        导出用户会话列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportSessions
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ExportSessionsRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ExportSessionsResponse`
        """
        http_info = self._export_sessions_http_info(request)
        return self._call_api(**http_info)

    def export_sessions_async_invoker(self, request):
        http_info = self._export_sessions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _export_sessions_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/session/list-sessions/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportSessionsResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def export_user_connection_async(self, request):
        r"""导出用户登录记录

        导出用户登录记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportUserConnection
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ExportUserConnectionRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ExportUserConnectionResponse`
        """
        http_info = self._export_user_connection_http_info(request)
        return self._call_api(**http_info)

    def export_user_connection_async_invoker(self, request):
        http_info = self._export_user_connection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _export_user_connection_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/session/user-connection/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportUserConnectionResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_app_connection_async(self, request):
        r"""查询应用使用记录

        查询应用使用记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppConnection
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListAppConnectionRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListAppConnectionResponse`
        """
        http_info = self._list_app_connection_http_info(request)
        return self._call_api(**http_info)

    def list_app_connection_async_invoker(self, request):
        http_info = self._list_app_connection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_app_connection_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/session/app-connection",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppConnectionResponse"
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
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_session_by_user_name_async(self, request):
        r"""根据用户名查询当前会话

        根据用户名查询当前会话。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSessionByUserName
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListSessionByUserNameRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListSessionByUserNameResponse`
        """
        http_info = self._list_session_by_user_name_http_info(request)
        return self._call_api(**http_info)

    def list_session_by_user_name_async_invoker(self, request):
        http_info = self._list_session_by_user_name_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_session_by_user_name_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/session/user-session-info",
            "request_type": request.__class__.__name__,
            "response_type": "ListSessionByUserNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_sessions_async(self, request):
        r"""查询用户会话列表

        查询用户会话列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSessions
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListSessionsRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListSessionsResponse`
        """
        http_info = self._list_sessions_http_info(request)
        return self._call_api(**http_info)

    def list_sessions_async_invoker(self, request):
        http_info = self._list_sessions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_sessions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/session/list-sessions",
            "request_type": request.__class__.__name__,
            "response_type": "ListSessionsResponse"
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
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'query_begin_time' in local_var_params:
            query_params.append(('query_begin_time', local_var_params['query_begin_time']))
        if 'query_end_time' in local_var_params:
            query_params.append(('query_end_time', local_var_params['query_end_time']))
        if 'app_server_group_id' in local_var_params:
            query_params.append(('app_server_group_id', local_var_params['app_server_group_id']))
        if 'vm_ip' in local_var_params:
            query_params.append(('vm_ip', local_var_params['vm_ip']))
        if 'public_ip' in local_var_params:
            query_params.append(('public_ip', local_var_params['public_ip']))
        if 'machine_name' in local_var_params:
            query_params.append(('machine_name', local_var_params['machine_name']))
        if 'session_state' in local_var_params:
            query_params.append(('session_state', local_var_params['session_state']))
        if 'is_success' in local_var_params:
            query_params.append(('is_success', local_var_params['is_success']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_user_connection_async(self, request):
        r"""查询用户登录记录

        查询用户登录记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUserConnection
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListUserConnectionRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListUserConnectionResponse`
        """
        http_info = self._list_user_connection_http_info(request)
        return self._call_api(**http_info)

    def list_user_connection_async_invoker(self, request):
        http_info = self._list_user_connection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_user_connection_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/session/user-connection",
            "request_type": request.__class__.__name__,
            "response_type": "ListUserConnectionResponse"
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
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def logoff_user_session_async(self, request):
        r"""用户会话注销

        用户会话注销。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for LogoffUserSession
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.LogoffUserSessionRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.LogoffUserSessionResponse`
        """
        http_info = self._logoff_user_session_http_info(request)
        return self._call_api(**http_info)

    def logoff_user_session_async_invoker(self, request):
        http_info = self._logoff_user_session_http_info(request)
        return AsyncInvoker(self, http_info)

    def _logoff_user_session_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/session/logoff",
            "request_type": request.__class__.__name__,
            "response_type": "LogoffUserSessionResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_create_server_group_tags_async(self, request):
        r"""批量添加服务器组标签

        此接口为幂等接口：
        同时对多个服务器组批量添加标签，最大支持100个服务器组，每个服务器组最大20个标签
        创建时如果请求体中存在重复key则报错。        
        创建时，不允许设置重复key数据,如果数据库已存在该key，就覆盖value的值。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateServerGroupTags
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchCreateServerGroupTagsRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchCreateServerGroupTagsResponse`
        """
        http_info = self._batch_create_server_group_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_server_group_tags_async_invoker(self, request):
        http_info = self._batch_create_server_group_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_server_group_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/server-group/tags/batch-create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateServerGroupTagsResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_server_group_tags_async(self, request):
        r"""批量删除服务器组标签

        此接口为幂等接口：
        同时对多个服务器组批量删除标签，最大支持100个服务器组，每个服务器组最大20个标签。
        删除时，如果删除的标签不存在，默认处理成功，删除时不对标签字符集范围做校验。
        删除时tags结构体不能缺失，key不能为空，或者空字符串。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteServerGroupTags
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchDeleteServerGroupTagsRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchDeleteServerGroupTagsResponse`
        """
        http_info = self._batch_delete_server_group_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_server_group_tags_async_invoker(self, request):
        http_info = self._batch_delete_server_group_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_server_group_tags_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/server-group/tags/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteServerGroupTagsResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_server_group_tags_async(self, request):
        r"""添加服务器组标签

        此接口为幂等接口：
        创建时如果请求体中存在重复key则报错。
        创建时，不允许设置重复key数据,如果数据库已存在该key，就覆盖value的值。
        一个服务器组上最多有20个标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateServerGroupTags
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CreateServerGroupTagsRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CreateServerGroupTagsResponse`
        """
        http_info = self._create_server_group_tags_http_info(request)
        return self._call_api(**http_info)

    def create_server_group_tags_async_invoker(self, request):
        http_info = self._create_server_group_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_server_group_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/server-group/{server_group_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateServerGroupTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_group_id' in local_var_params:
            path_params['server_group_id'] = local_var_params['server_group_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_server_group_tags_async(self, request):
        r"""删除服务器组标签

        此接口为幂等接口：
        删除时，如果删除的标签不存在，默认处理成功,删除时不对标签字符集范围做校验。
        删除时tags结构体不能缺失，key不能为空，或者空字符串。
        支持最多每次删除20个标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteServerGroupTags
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.DeleteServerGroupTagsRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DeleteServerGroupTagsResponse`
        """
        http_info = self._delete_server_group_tags_http_info(request)
        return self._call_api(**http_info)

    def delete_server_group_tags_async_invoker(self, request):
        http_info = self._delete_server_group_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_server_group_tags_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/server-group/{server_group_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteServerGroupTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_group_id' in local_var_params:
            path_params['server_group_id'] = local_var_params['server_group_id']

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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_server_group_tag_async(self, request):
        r"""查询租户在所有服务器组上的标签

        查询租户在所有服务器组上的资源标签集合。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServerGroupTag
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListServerGroupTagRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListServerGroupTagResponse`
        """
        http_info = self._list_server_group_tag_http_info(request)
        return self._call_api(**http_info)

    def list_server_group_tag_async_invoker(self, request):
        http_info = self._list_server_group_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_server_group_tag_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/server-group/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListServerGroupTagResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_server_group_tag_async(self, request):
        r"""查询服务器组的标签

        查询指定服务器组的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServerGroupTag
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ShowServerGroupTagRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ShowServerGroupTagResponse`
        """
        http_info = self._show_server_group_tag_http_info(request)
        return self._call_api(**http_info)

    def show_server_group_tag_async_invoker(self, request):
        http_info = self._show_server_group_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_server_group_tag_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/server-group/{server_group_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowServerGroupTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_group_id' in local_var_params:
            path_params['server_group_id'] = local_var_params['server_group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_volume_type_async(self, request):
        r"""查询可用磁盘类型

        该接口用于查询可用磁盘类型。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVolumeType
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListVolumeTypeRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListVolumeTypeResponse`
        """
        http_info = self._list_volume_type_http_info(request)
        return self._call_api(**http_info)

    def list_volume_type_async_invoker(self, request):
        http_info = self._list_volume_type_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_volume_type_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/volume-type",
            "request_type": request.__class__.__name__,
            "response_type": "ListVolumeTypeResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

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
