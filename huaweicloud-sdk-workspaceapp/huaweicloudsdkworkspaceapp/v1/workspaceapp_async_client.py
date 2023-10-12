# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class WorkspaceAppAsyncClient(Client):
    def __init__(self):
        super(WorkspaceAppAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkworkspaceapp.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "WorkspaceAppClient":
            raise TypeError("client type error, support client type is WorkspaceAppClient")

        return ClientBuilder(clazz)

    def list_published_app_async(self, request):
        """查询已发布应用

        查询已发布的应用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPublishedApp
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListPublishedAppRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListPublishedAppResponse`
        """
        return self._list_published_app_with_http_info(request)

    def _list_published_app_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/app-groups/{app_group_id}/apps',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPublishedAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def publish_app_async(self, request):
        """发布应用

        批量发布应用,不允许发布同名的应用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PublishApp
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.PublishAppRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PublishAppResponse`
        """
        return self._publish_app_with_http_info(request)

    def _publish_app_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_group_id' in local_var_params:
            path_params['app_group_id'] = local_var_params['app_group_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/app-groups/{app_group_id}/apps',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='PublishAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_publishable_app_async(self, request):
        """可发布应用列表

        查询应用组下可发布的应用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPublishableApp
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ShowPublishableAppRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ShowPublishableAppResponse`
        """
        return self._show_publishable_app_with_http_info(request)

    def _show_publishable_app_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_group_id' in local_var_params:
            path_params['app_group_id'] = local_var_params['app_group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/app-groups/{app_group_id}/publishable-app',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPublishableAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def unpublish_app_async(self, request):
        """批量取消应用发布

        批量取消应用发布。
        &gt; - 批量取消应用组下已经发布的应用，应用对应的授权会一起删除，重复执行会按照成功处理(响应200)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UnpublishApp
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.UnpublishAppRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UnpublishAppResponse`
        """
        return self._unpublish_app_with_http_info(request)

    def _unpublish_app_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_group_id' in local_var_params:
            path_params['app_group_id'] = local_var_params['app_group_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/app-groups/{app_group_id}/apps/batch-unpublish',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UnpublishAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_app_async(self, request):
        """修改应用信息

        编辑修改应用信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateApp
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.UpdateAppRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UpdateAppResponse`
        """
        return self._update_app_with_http_info(request)

    def _update_app_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/app-groups/{app_group_id}/apps/{app_id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def upload_app_icon_async(self, request):
        """修改自定义应用图标

        修改自定义应用图标
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UploadAppIcon
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.UploadAppIconRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UploadAppIconResponse`
        """
        return self._upload_app_icon_with_http_info(request)

    def _upload_app_icon_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/app-groups/{app_group_id}/apps/{app_id}/icon',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UploadAppIconResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_app_group_async(self, request):
        """批量删除应用组

        批量删除应用组,重复执行会按照成功处理(响应200)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteAppGroup
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchDeleteAppGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchDeleteAppGroupResponse`
        """
        return self._batch_delete_app_group_with_http_info(request)

    def _batch_delete_app_group_with_http_info(self, request):
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/app-groups/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteAppGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_app_group_async(self, request):
        """创建应用组

        该API用于创建应用组。
        &gt; - 应用服务器中安装了不同的应用，这些应用可以组成不同的应用组，进行集中的管理和维护，向用户(组)发布。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAppGroup
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CreateAppGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CreateAppGroupResponse`
        """
        return self._create_app_group_with_http_info(request)

    def _create_app_group_with_http_info(self, request):
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/app-groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAppGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_app_group_async(self, request):
        """查询应用组

        查询用户创建的应用组，按照名称、授权类型分页查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppGroup
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListAppGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListAppGroupResponse`
        """
        return self._list_app_group_with_http_info(request)

    def _list_app_group_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/app-groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAppGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_app_group_async(self, request):
        """修改应用组

        修改应用组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAppGroup
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.UpdateAppGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UpdateAppGroupResponse`
        """
        return self._update_app_group_with_http_info(request)

    def _update_app_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_group_id' in local_var_params:
            path_params['app_group_id'] = local_var_params['app_group_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/app-groups/{app_group_id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAppGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_product_async(self, request):
        """查询云应用套餐

        查询云应用套餐，按照条件过滤。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProduct
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListProductRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListProductResponse`
        """
        return self._list_product_with_http_info(request)

    def _list_product_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_id' in local_var_params:
            query_params.append(('product_id', local_var_params['product_id']))
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/product',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProductResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_session_type_async(self, request):
        """查询会话套餐列表

        该接口用于查询会话套餐列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSessionType
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListSessionTypeRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListSessionTypeResponse`
        """
        return self._list_session_type_with_http_info(request)

    def _list_session_type_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/session-type',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSessionTypeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_app_group_authorization_async(self, request):
        """增加应用组授权

        应用组添加用户授权，授权后用户就获得应用组下所有已发布应用的权限访问。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddAppGroupAuthorization
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.AddAppGroupAuthorizationRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.AddAppGroupAuthorizationResponse`
        """
        return self._add_app_group_authorization_with_http_info(request)

    def _add_app_group_authorization_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/app-groups/authorizations',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddAppGroupAuthorizationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_app_group_authorization_async(self, request):
        """移除授权

        移除应用组内的指定用户的授权，用户授权删除后，用户将没有权限访问应用组内的任何应用。注意：重复执行会按照操作成功处理。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteAppGroupAuthorization
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchDeleteAppGroupAuthorizationRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchDeleteAppGroupAuthorizationResponse`
        """
        return self._batch_delete_app_group_authorization_with_http_info(request)

    def _batch_delete_app_group_authorization_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/app-groups/actions/batch-delete-authorization',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteAppGroupAuthorizationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_app_group_authorization_async(self, request):
        """查询授权记录

        查询应用内已授权的用户列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppGroupAuthorization
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListAppGroupAuthorizationRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListAppGroupAuthorizationResponse`
        """
        return self._list_app_group_authorization_with_http_info(request)

    def _list_app_group_authorization_with_http_info(self, request):
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

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/app-groups/actions/list-authorizations',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAppGroupAuthorizationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_availability_zone_async(self, request):
        """查询可用分区列表

        该接口用于查询支持的可用分区列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAvailabilityZone
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListAvailabilityZoneRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListAvailabilityZoneResponse`
        """
        return self._list_availability_zone_with_http_info(request)

    def _list_availability_zone_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/availability-zone',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAvailabilityZoneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job_async(self, request):
        """查询任务的执行状态

        查询Job的执行状态。
        
        对于创建云应用服务器命令下发后会返回job_id，通过job_id可以查询任务的执行状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJob
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ShowJobRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ShowJobResponse`
        """
        return self._show_job_with_http_info(request)

    def _show_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/job/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_or_update_storage_policy_statement_async(self, request):
        """新增或更新存储目录访问权限自定义策略

        新增或更新存储目录访问权限自定义策略(已存在自定义策略时会对已有策略更新)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateOrUpdateStoragePolicyStatement
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CreateOrUpdateStoragePolicyStatementRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CreateOrUpdateStoragePolicyStatementResponse`
        """
        return self._create_or_update_storage_policy_statement_with_http_info(request)

    def _create_or_update_storage_policy_statement_with_http_info(self, request):
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/storages-policy/actions/create-statements',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateOrUpdateStoragePolicyStatementResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_persistent_storage_async(self, request):
        """创建WKS存储

        创建WKS存储，目前仅支持创建 SFS3.0 容量型文件系统。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePersistentStorage
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CreatePersistentStorageRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CreatePersistentStorageResponse`
        """
        return self._create_persistent_storage_with_http_info(request)

    def _create_persistent_storage_with_http_info(self, request):
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/persistent-storages',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePersistentStorageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_share_folder_async(self, request):
        """创建共享存储目录

        创建共享存储目录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateShareFolder
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CreateShareFolderRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CreateShareFolderResponse`
        """
        return self._create_share_folder_with_http_info(request)

    def _create_share_folder_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'storage_id' in local_var_params:
            path_params['storage_id'] = local_var_params['storage_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/persistent-storages/{storage_id}/actions/create-share-folder',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateShareFolderResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_persistent_storage_async(self, request):
        """删除WKS存储

        删除共享存储，只会解除NAS与文件系统之间的关联关系，不会删除文件系统和文件系统中的数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePersistentStorage
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.DeletePersistentStorageRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DeletePersistentStorageResponse`
        """
        return self._delete_persistent_storage_with_http_info(request)

    def _delete_persistent_storage_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'storage_id' in local_var_params:
            path_params['storage_id'] = local_var_params['storage_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/persistent-storages/{storage_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePersistentStorageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_storage_claim_async(self, request):
        """删除共享目录

        删除共享存储目录。
        &gt; 需要删除绑定的用户及用户组，才能删除共享文目录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteStorageClaim
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.DeleteStorageClaimRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DeleteStorageClaimResponse`
        """
        return self._delete_storage_claim_with_http_info(request)

    def _delete_storage_claim_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'storage_id' in local_var_params:
            path_params['storage_id'] = local_var_params['storage_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/persistent-storages/{storage_id}/actions/delete-storage-claim',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteStorageClaimResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_user_storage_attachment_async(self, request):
        """删除个人存储目录

        删除个人存储目录，个人目录中的数据也将永久删除且无法恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteUserStorageAttachment
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.DeleteUserStorageAttachmentRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DeleteUserStorageAttachmentResponse`
        """
        return self._delete_user_storage_attachment_with_http_info(request)

    def _delete_user_storage_attachment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'storage_id' in local_var_params:
            path_params['storage_id'] = local_var_params['storage_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/persistent-storages/{storage_id}/actions/delete-user-attachment',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteUserStorageAttachmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_persistent_storage_async(self, request):
        """查询WKS存储

        查询WKS存储
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPersistentStorage
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListPersistentStorageRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListPersistentStorageResponse`
        """
        return self._list_persistent_storage_with_http_info(request)

    def _list_persistent_storage_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/persistent-storages',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPersistentStorageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_share_folder_async(self, request):
        """查询共享存储目录

        查询共享存储目录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListShareFolder
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListShareFolderRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListShareFolderResponse`
        """
        return self._list_share_folder_with_http_info(request)

    def _list_share_folder_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/persistent-storages/actions/list-share-folders',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListShareFolderResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_storage_assignment_async(self, request):
        """查询个人存储目录

        查询个人存储目录
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListStorageAssignment
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListStorageAssignmentRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListStorageAssignmentResponse`
        """
        return self._list_storage_assignment_with_http_info(request)

    def _list_storage_assignment_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/persistent-storages/actions/list-attachments',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListStorageAssignmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_storage_policy_statement_async(self, request):
        """查询存储目录访问权限策略

        查询存储目录访问权限策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListStoragePolicyStatement
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListStoragePolicyStatementRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListStoragePolicyStatementResponse`
        """
        return self._list_storage_policy_statement_with_http_info(request)

    def _list_storage_policy_statement_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/storages-policy/actions/list-statements',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListStoragePolicyStatementResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_share_folder_assignment_async(self, request):
        """修改共享目录成员

        批量添加或者移除共享目录成员
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateShareFolderAssignment
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.UpdateShareFolderAssignmentRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UpdateShareFolderAssignmentResponse`
        """
        return self._update_share_folder_assignment_with_http_info(request)

    def _update_share_folder_assignment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'storage_id' in local_var_params:
            path_params['storage_id'] = local_var_params['storage_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/persistent-storages/{storage_id}/actions/assign-share-folder',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateShareFolderAssignmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_user_folder_assignment_async(self, request):
        """创建个人存储目录

        创建个人存储目录
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateUserFolderAssignment
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.UpdateUserFolderAssignmentRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UpdateUserFolderAssignmentResponse`
        """
        return self._update_user_folder_assignment_with_http_info(request)

    def _update_user_folder_assignment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'storage_id' in local_var_params:
            path_params['storage_id'] = local_var_params['storage_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/persistent-storages/{storage_id}/actions/assign-folder',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateUserFolderAssignmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_policy_group_async(self, request):
        """新增策略组

        新增策略组，通过策略组能灵活的控制客户端访问与接入策略，如：文件、剪切板、会话等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePolicyGroup
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CreatePolicyGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CreatePolicyGroupResponse`
        """
        return self._create_policy_group_with_http_info(request)

    def _create_policy_group_with_http_info(self, request):
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/policy-groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePolicyGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_policy_template_async(self, request):
        """新增策略模板

        新增策略模板。策略模板创建好后，用户在创建策略组的时候，就可以根据已有策略模板按需调整配置，快速完成策略组的创建。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePolicyTemplate
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CreatePolicyTemplateRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CreatePolicyTemplateResponse`
        """
        return self._create_policy_template_with_http_info(request)

    def _create_policy_template_with_http_info(self, request):
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/policy-templates',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePolicyTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_policy_group_async(self, request):
        """删除策略组

        删除指定策略组，包含策略组对应的策略信息以及应用对象信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePolicyGroup
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.DeletePolicyGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DeletePolicyGroupResponse`
        """
        return self._delete_policy_group_with_http_info(request)

    def _delete_policy_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_group_id' in local_var_params:
            path_params['policy_group_id'] = local_var_params['policy_group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/policy-groups/{policy_group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePolicyGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_policy_template_async(self, request):
        """删除策略模板

        删除指定策略模板，包含策略模板对应的策略信息以及应用对象信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePolicyTemplate
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.DeletePolicyTemplateRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DeletePolicyTemplateResponse`
        """
        return self._delete_policy_template_with_http_info(request)

    def _delete_policy_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_template_id' in local_var_params:
            path_params['policy_template_id'] = local_var_params['policy_template_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/policy-templates/{policy_template_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePolicyTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_policy_group_async(self, request):
        """查询策略组列表

        查询策略组概要信息列表,包括应用对象和详细策略项。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPolicyGroup
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListPolicyGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListPolicyGroupResponse`
        """
        return self._list_policy_group_with_http_info(request)

    def _list_policy_group_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/policy-groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPolicyGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_policy_template_async(self, request):
        """查询策略模板列表

        查询策略模板概要信息列表，包含策略信息以及应用对象信息。用户在创建策略组的时候，可以根据已有策略模板按需调整配置，快速完成策略组的创建。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPolicyTemplate
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListPolicyTemplateRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListPolicyTemplateResponse`
        """
        return self._list_policy_template_with_http_info(request)

    def _list_policy_template_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/policy-templates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPolicyTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_targets_of_policy_group_async(self, request):
        """查询策略组应用对象

        查询指定策略组所应用的对象。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTargetsOfPolicyGroup
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListTargetsOfPolicyGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListTargetsOfPolicyGroupResponse`
        """
        return self._list_targets_of_policy_group_with_http_info(request)

    def _list_targets_of_policy_group_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/policy-groups/{policy_group_id}/target',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTargetsOfPolicyGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_original_policy_info_async(self, request):
        """查询初始策略项

        查询初始策略项，初始策略项是所有协议策略配置项的默认配置，用户可以在初始策略项的基础上根据需求修改指定的配置，创建新的策略组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOriginalPolicyInfo
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ShowOriginalPolicyInfoRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ShowOriginalPolicyInfoResponse`
        """
        return self._show_original_policy_info_with_http_info(request)

    def _show_original_policy_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/policy-groups/actions/list-original-policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowOriginalPolicyInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_policy_group_async(self, request):
        """修改策略组

        修改指定策略组的信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePolicyGroup
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.UpdatePolicyGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UpdatePolicyGroupResponse`
        """
        return self._update_policy_group_with_http_info(request)

    def _update_policy_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_group_id' in local_var_params:
            path_params['policy_group_id'] = local_var_params['policy_group_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/policy-groups/{policy_group_id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePolicyGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_policy_template_async(self, request):
        """修改策略模板

        修改指定策略模板的信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePolicyTemplate
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.UpdatePolicyTemplateRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UpdatePolicyTemplateResponse`
        """
        return self._update_policy_template_with_http_info(request)

    def _update_policy_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_template_id' in local_var_params:
            path_params['policy_template_id'] = local_var_params['policy_template_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/policy-templates/{policy_template_id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePolicyTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_quota_async(self, request):
        """配额校验

        配额校验，购买服务器前可用调用该接口，校验本次创建服务器资源是否足够。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckQuota
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CheckQuotaRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CheckQuotaResponse`
        """
        return self._check_quota_with_http_info(request)

    def _check_quota_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_id' in local_var_params:
            query_params.append(('product_id', local_var_params['product_id']))
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/check/quota',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CheckQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_server_async(self, request):
        """批量删除服务器

        批量删除服务器
        &gt; - 仅支持删除按需订购的服务器，包周期订购的服务器需要到Console界面进行退订，订单退订成功后服务器将会自动删除。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteServer
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchDeleteServerRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchDeleteServerResponse`
        """
        return self._batch_delete_server_with_http_info(request)

    def _batch_delete_server_with_http_info(self, request):
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/app-servers/actions/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_migrate_hosts_server_async(self, request):
        """迁移云办公主机下面的服务器到目标云办公主机

        迁移云办公主机下面的服务器到目标云办公主机
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchMigrateHostsServer
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchMigrateHostsServerRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchMigrateHostsServerResponse`
        """
        return self._batch_migrate_hosts_server_with_http_info(request)

    def _batch_migrate_hosts_server_with_http_info(self, request):
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/app-servers/hosts/batch-migrate',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchMigrateHostsServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_reboot_server_async(self, request):
        """重启服务器

        重启服务器
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchRebootServer
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchRebootServerRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchRebootServerResponse`
        """
        return self._batch_reboot_server_with_http_info(request)

    def _batch_reboot_server_with_http_info(self, request):
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/app-servers/actions/batch-reboot',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchRebootServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_rejoin_domain_async(self, request):
        """批量服务器重新加域

        批量服务器重新加入AD域，一般用于解决服务器脱域的情况使用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchRejoinDomain
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchRejoinDomainRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchRejoinDomainResponse`
        """
        return self._batch_rejoin_domain_with_http_info(request)

    def _batch_rejoin_domain_with_http_info(self, request):
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/app-servers/actions/batch-rejoin-domain',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchRejoinDomainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_start_server_async(self, request):
        """启动服务器

        启动服务器
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchStartServer
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchStartServerRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchStartServerResponse`
        """
        return self._batch_start_server_with_http_info(request)

    def _batch_start_server_with_http_info(self, request):
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/app-servers/actions/batch-start',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchStartServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_stop_server_async(self, request):
        """关闭服务器

        关闭服务器
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchStopServer
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchStopServerRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchStopServerResponse`
        """
        return self._batch_stop_server_with_http_info(request)

    def _batch_stop_server_with_http_info(self, request):
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/app-servers/actions/batch-stop',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchStopServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_update_tsvi_async(self, request):
        """批量更新服务器虚拟会话IP配置

        批量更新服务器虚拟会话IP配置，按需重启机器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchUpdateTsvi
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.BatchUpdateTsviRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.BatchUpdateTsviResponse`
        """
        return self._batch_update_tsvi_with_http_info(request)

    def _batch_update_tsvi_with_http_info(self, request):
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/app-servers/actions/batch-update-tsvi',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchUpdateTsviResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_server_image_async(self, request):
        """修改服务器的镜像

        修改服务器的镜像
        &gt; - 服务器的镜像和服务器组的镜像不一样时，支持服务器的镜像切换为服务器组的镜像，并且仅允许同等镜像进行切换，例如：同操作系统，免费镜像切换，同源同价的付费镜像切换。如果服务器组的镜像和服务器的镜像为非同等镜像，建议您直接购买新的服务器，删除或者退订老的服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeServerImage
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ChangeServerImageRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ChangeServerImageResponse`
        """
        return self._change_server_image_with_http_info(request)

    def _change_server_image_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/app-servers/{server_id}/actions/change-image',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeServerImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_app_servers_async(self, request):
        """创建云服务器

        创建云服务器接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAppServers
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CreateAppServersRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CreateAppServersResponse`
        """
        return self._create_app_servers_with_http_info(request)

    def _create_app_servers_with_http_info(self, request):
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/app-servers/actions/create',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAppServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_servers_async(self, request):
        """查询服务器列表

        查询服务器列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServers
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListServersRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListServersResponse`
        """
        return self._list_servers_with_http_info(request)

    def _list_servers_with_http_info(self, request):
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
        if 'server_id' in local_var_params:
            query_params.append(('server_id', local_var_params['server_id']))
        if 'maintain_status' in local_var_params:
            query_params.append(('maintain_status', local_var_params['maintain_status']))
        if 'scaling_auto_create' in local_var_params:
            query_params.append(('scaling_auto_create', local_var_params['scaling_auto_create']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/app-servers',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reinstall_server_async(self, request):
        """重装服务器

        重装服务器。
        &gt; - 使用服务器原有的镜像进行重装，当服务器异常无法恢复时或者服务器运行时间久了，性能下降时，可选择重建服务器。注意：重装时系统盘的数据将会被清理掉。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ReinstallServer
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ReinstallServerRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ReinstallServerResponse`
        """
        return self._reinstall_server_with_http_info(request)

    def _reinstall_server_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/app-servers/{server_id}/actions/reinstall',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ReinstallServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_server_async(self, request):
        """修改服务器

        修改服务器。
        &gt; - 服务器的状态修改为维护模式后，用户打开应用，选择可用的服务器进行接入的时候，会过滤掉处于维护模式的服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateServer
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.UpdateServerRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UpdateServerResponse`
        """
        return self._update_server_with_http_info(request)

    def _update_server_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/app-servers/{server_id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_server_group_async(self, request):
        """创建服务器组

        创建服务器组。
        &gt; - 服务器组是一组相同配置的服务器集合，服务器组内的服务器使用同一镜像创建，配置相同，运行相同的应用程序。用户在打开云应用时，会根据调度规则选取组内的一台可用服务器进行连接。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateServerGroup
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.CreateServerGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CreateServerGroupResponse`
        """
        return self._create_server_group_with_http_info(request)

    def _create_server_group_with_http_info(self, request):
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/app-server-groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateServerGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_server_groups_async(self, request):
        """删除服务器组

        删除服务器组。
        - &gt; 删除服务器组之前，需要先删除服务器组内的所有服务器。如果传服务器组已被删除，重复执行删除，则返回成功响应。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteServerGroups
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.DeleteServerGroupsRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DeleteServerGroupsResponse`
        """
        return self._delete_server_groups_with_http_info(request)

    def _delete_server_groups_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_group_id' in local_var_params:
            path_params['server_group_id'] = local_var_params['server_group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/app-server-groups/{server_group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteServerGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_server_groups_async(self, request):
        """查询服务器组列表

        查询服务器组列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServerGroups
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListServerGroupsRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListServerGroupsResponse`
        """
        return self._list_server_groups_with_http_info(request)

    def _list_server_groups_with_http_info(self, request):
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

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/app-server-groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListServerGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_server_group_async(self, request):
        """修改服务器组

        修改服务器组。
        - &gt; 修改服务器组的镜像，系统盘大小，OU信息后，已创建的服务器配置不变，新添加的服务器会使用新的配置创建。修改最大会话数后，用户接入服务器组时，会按照最新的配置进行路由计算。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateServerGroup
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.UpdateServerGroupRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UpdateServerGroupResponse`
        """
        return self._update_server_group_with_http_info(request)

    def _update_server_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_group_id' in local_var_params:
            path_params['server_group_id'] = local_var_params['server_group_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/app-server-groups/{server_group_id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateServerGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_app_connection_async(self, request):
        """查询应用使用记录

        查询应用使用记录
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppConnection
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListAppConnectionRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListAppConnectionResponse`
        """
        return self._list_app_connection_with_http_info(request)

    def _list_app_connection_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/session/app-connection',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAppConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_session_by_user_name_async(self, request):
        """根据用户名查询当前会话

        根据用户名查询当前会话
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSessionByUserName
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListSessionByUserNameRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListSessionByUserNameResponse`
        """
        return self._list_session_by_user_name_with_http_info(request)

    def _list_session_by_user_name_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/session/user-session-info',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSessionByUserNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_user_connection_async(self, request):
        """查询用户登录记录

        查询用户登录记录
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUserConnection
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListUserConnectionRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListUserConnectionResponse`
        """
        return self._list_user_connection_with_http_info(request)

    def _list_user_connection_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/session/user-connection',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListUserConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def logoff_user_session_async(self, request):
        """用户会话注销

        用户会话注销
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for LogoffUserSession
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.LogoffUserSessionRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.LogoffUserSessionResponse`
        """
        return self._logoff_user_session_with_http_info(request)

    def _logoff_user_session_with_http_info(self, request):
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/session/logoff',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='LogoffUserSessionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_volume_type_async(self, request):
        """查询可用磁盘类型

        该接口用于查询可用磁盘类型。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVolumeType
        :type request: :class:`huaweicloudsdkworkspaceapp.v1.ListVolumeTypeRequest`
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListVolumeTypeResponse`
        """
        return self._list_volume_type_with_http_info(request)

    def _list_volume_type_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/volume-type',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListVolumeTypeResponse',
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
