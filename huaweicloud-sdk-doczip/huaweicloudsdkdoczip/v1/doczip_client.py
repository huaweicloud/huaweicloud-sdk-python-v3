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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkdoczip'")


class DocZipClient(Client):
    def __init__(self):
        super().__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdoczip.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "DocZipClient":
                raise TypeError("client type error, support client type is DocZipClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_application(self, request):
        r"""创建应用

        租户可通过该接口创建应用，每个租户允许创建应用个数可以通过“获取允许创建的资源数量”接口获取。其中租户ID就是用户的账号ID。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateApplication
        :type request: :class:`huaweicloudsdkdoczip.v1.CreateApplicationRequest`
        :rtype: :class:`huaweicloudsdkdoczip.v1.CreateApplicationResponse`
        """
        http_info = self._create_application_http_info(request)
        return self._call_api(**http_info)

    def create_application_invoker(self, request):
        http_info = self._create_application_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_application_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/tenants/application",
            "request_type": request.__class__.__name__,
            "response_type": "CreateApplicationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'tenant_id' in local_var_params:
            header_params['tenant_id'] = local_var_params['tenant_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Trace-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_application(self, request):
        r"""删除应用

        租户可通过该接口删除应用，应用被删除后，将不能被恢复。其中租户ID就是用户的账号ID。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApplication
        :type request: :class:`huaweicloudsdkdoczip.v1.DeleteApplicationRequest`
        :rtype: :class:`huaweicloudsdkdoczip.v1.DeleteApplicationResponse`
        """
        http_info = self._delete_application_http_info(request)
        return self._call_api(**http_info)

    def delete_application_invoker(self, request):
        http_info = self._delete_application_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_application_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/tenants/application/{application_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteApplicationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []

        header_params = {}
        if 'tenant_id' in local_var_params:
            header_params['tenant_id'] = local_var_params['tenant_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Trace-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_application_details(self, request):
        r"""获取应用详情

        租户通过该接口可以查询某个租户的详细信息，配合query_type字段查询应用的基本信息，系统配置信息，文档块信息，也可以查询全部信息。其中租户ID就是用户的账号ID。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApplicationDetails
        :type request: :class:`huaweicloudsdkdoczip.v1.ListApplicationDetailsRequest`
        :rtype: :class:`huaweicloudsdkdoczip.v1.ListApplicationDetailsResponse`
        """
        http_info = self._list_application_details_http_info(request)
        return self._call_api(**http_info)

    def list_application_details_invoker(self, request):
        http_info = self._list_application_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_application_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/tenants/application/detail/{application_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListApplicationDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []
        if 'query_type' in local_var_params:
            query_params.append(('query_type', local_var_params['query_type']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'tenant_id' in local_var_params:
            header_params['tenant_id'] = local_var_params['tenant_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Trace-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_applications(self, request):
        r"""获取应用列表

        租户可通过该接口获取租户下所有应用的信息列表。其中租户ID就是用户的账号ID。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApplications
        :type request: :class:`huaweicloudsdkdoczip.v1.ListApplicationsRequest`
        :rtype: :class:`huaweicloudsdkdoczip.v1.ListApplicationsResponse`
        """
        http_info = self._list_applications_http_info(request)
        return self._call_api(**http_info)

    def list_applications_invoker(self, request):
        http_info = self._list_applications_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_applications_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/tenants/application/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListApplicationsResponse"
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
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'application_name' in local_var_params:
            query_params.append(('application_name', local_var_params['application_name']))

        header_params = {}
        if 'tenant_id' in local_var_params:
            header_params['tenant_id'] = local_var_params['tenant_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Trace-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def publish_application(self, request):
        r"""发布应用

        租户可通过该接口发布应用，应用发布后，才可以被使用。其中租户ID就是用户的账号ID。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PublishApplication
        :type request: :class:`huaweicloudsdkdoczip.v1.PublishApplicationRequest`
        :rtype: :class:`huaweicloudsdkdoczip.v1.PublishApplicationResponse`
        """
        http_info = self._publish_application_http_info(request)
        return self._call_api(**http_info)

    def publish_application_invoker(self, request):
        http_info = self._publish_application_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _publish_application_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/tenants/application/{application_id}/release",
            "request_type": request.__class__.__name__,
            "response_type": "PublishApplicationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []

        header_params = {}
        if 'tenant_id' in local_var_params:
            header_params['tenant_id'] = local_var_params['tenant_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Trace-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_app_resource_limit(self, request):
        r"""获取允许创建的应用上限

        租户可通过该接口获取允许创建的应用数量上限，每个租户允许创建的租户数量不能超过配置的被允许创建的应用数量。其中租户ID就是用户的账号ID。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAppResourceLimit
        :type request: :class:`huaweicloudsdkdoczip.v1.ShowAppResourceLimitRequest`
        :rtype: :class:`huaweicloudsdkdoczip.v1.ShowAppResourceLimitResponse`
        """
        http_info = self._show_app_resource_limit_http_info(request)
        return self._call_api(**http_info)

    def show_app_resource_limit_invoker(self, request):
        http_info = self._show_app_resource_limit_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_app_resource_limit_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/tenants/resource/limit",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppResourceLimitResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}
        if 'tenant_id' in local_var_params:
            header_params['tenant_id'] = local_var_params['tenant_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Trace-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_app_secret_key(self, request):
        r"""获取应用密钥

        租户可通过该接口获取应用密钥。租户可通过application_id和应用密钥完成租户认证。其中租户ID就是用户的账号ID。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAppSecretKey
        :type request: :class:`huaweicloudsdkdoczip.v1.ShowAppSecretKeyRequest`
        :rtype: :class:`huaweicloudsdkdoczip.v1.ShowAppSecretKeyResponse`
        """
        http_info = self._show_app_secret_key_http_info(request)
        return self._call_api(**http_info)

    def show_app_secret_key_invoker(self, request):
        http_info = self._show_app_secret_key_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_app_secret_key_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/tenants/application/secret-key/{application_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppSecretKeyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []

        header_params = {}
        if 'tenant_id' in local_var_params:
            header_params['tenant_id'] = local_var_params['tenant_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Trace-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_blocks(self, request):
        r"""获取应用文档块信息

        租户可通过该接口获取当前租户下支持的所有文档块信息，在“创建应用”接口中，可根据业务需求为不同的应用选择不同的文档块数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBlocks
        :type request: :class:`huaweicloudsdkdoczip.v1.ShowBlocksRequest`
        :rtype: :class:`huaweicloudsdkdoczip.v1.ShowBlocksResponse`
        """
        http_info = self._show_blocks_http_info(request)
        return self._call_api(**http_info)

    def show_blocks_invoker(self, request):
        http_info = self._show_blocks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_blocks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/tenants/application/block",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBlocksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'tenant_id' in local_var_params:
            header_params['tenant_id'] = local_var_params['tenant_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Trace-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_application(self, request):
        r"""修改应用

        租户可通过该接口修改某个应用的名称，系统设置等信息。其中租户ID就是用户的账号ID。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateApplication
        :type request: :class:`huaweicloudsdkdoczip.v1.UpdateApplicationRequest`
        :rtype: :class:`huaweicloudsdkdoczip.v1.UpdateApplicationResponse`
        """
        http_info = self._update_application_http_info(request)
        return self._call_api(**http_info)

    def update_application_invoker(self, request):
        http_info = self._update_application_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_application_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/tenants/application/{application_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateApplicationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []

        header_params = {}
        if 'tenant_id' in local_var_params:
            header_params['tenant_id'] = local_var_params['tenant_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Trace-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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
