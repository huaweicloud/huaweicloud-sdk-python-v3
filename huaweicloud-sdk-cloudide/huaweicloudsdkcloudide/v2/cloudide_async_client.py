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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcloudide'")


class CloudIDEAsyncClient(Client):
    def __init__(self):
        super(CloudIDEAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcloudide.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CloudIDEAsyncClient":
                raise TypeError("client type error, support client type is CloudIDEAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_extension_evaluation_async(self, request):
        r"""添加插件评论

        添加插件评论
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddExtensionEvaluation
        :type request: :class:`huaweicloudsdkcloudide.v2.AddExtensionEvaluationRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.AddExtensionEvaluationResponse`
        """
        http_info = self._add_extension_evaluation_http_info(request)
        return self._call_api(**http_info)

    def add_extension_evaluation_async_invoker(self, request):
        http_info = self._add_extension_evaluation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_extension_evaluation_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/marketplace/extension/evaluation",
            "request_type": request.__class__.__name__,
            "response_type": "AddExtensionEvaluationResponse"
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

    def add_extension_evaluation_reply_async(self, request):
        r"""添加评论回复、回复评论回复

        添加评论回复、回复评论回复
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddExtensionEvaluationReply
        :type request: :class:`huaweicloudsdkcloudide.v2.AddExtensionEvaluationReplyRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.AddExtensionEvaluationReplyResponse`
        """
        http_info = self._add_extension_evaluation_reply_http_info(request)
        return self._call_api(**http_info)

    def add_extension_evaluation_reply_async_invoker(self, request):
        http_info = self._add_extension_evaluation_reply_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_extension_evaluation_reply_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/marketplace/extension/evaluation/reply",
            "request_type": request.__class__.__name__,
            "response_type": "AddExtensionEvaluationReplyResponse"
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

    def add_extension_star_async(self, request):
        r"""添加新评星

        添加新评星
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddExtensionStar
        :type request: :class:`huaweicloudsdkcloudide.v2.AddExtensionStarRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.AddExtensionStarResponse`
        """
        http_info = self._add_extension_star_http_info(request)
        return self._call_api(**http_info)

    def add_extension_star_async_invoker(self, request):
        http_info = self._add_extension_star_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_extension_star_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/marketplace/star",
            "request_type": request.__class__.__name__,
            "response_type": "AddExtensionStarResponse"
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

    def check_malicious_extension_evaluation_async(self, request):
        r"""举报评论,举报回复

        举报评论,举报回复
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckMaliciousExtensionEvaluation
        :type request: :class:`huaweicloudsdkcloudide.v2.CheckMaliciousExtensionEvaluationRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.CheckMaliciousExtensionEvaluationResponse`
        """
        http_info = self._check_malicious_extension_evaluation_http_info(request)
        return self._call_api(**http_info)

    def check_malicious_extension_evaluation_async_invoker(self, request):
        http_info = self._check_malicious_extension_evaluation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_malicious_extension_evaluation_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/marketplace/extension/evaluation/accusation",
            "request_type": request.__class__.__name__,
            "response_type": "CheckMaliciousExtensionEvaluationResponse"
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

    def create_extension_authorization_async(self, request):
        r"""设置ide实例对插件的授权

        设置ide实例对插件的授权。同意、不同意、未知（下次重新询问）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateExtensionAuthorization
        :type request: :class:`huaweicloudsdkcloudide.v2.CreateExtensionAuthorizationRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.CreateExtensionAuthorizationResponse`
        """
        http_info = self._create_extension_authorization_http_info(request)
        return self._call_api(**http_info)

    def create_extension_authorization_async_invoker(self, request):
        http_info = self._create_extension_authorization_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_extension_authorization_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/extension/authorization/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CreateExtensionAuthorizationResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_evaluation_async(self, request):
        r"""删除评论

        删除评论
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEvaluation
        :type request: :class:`huaweicloudsdkcloudide.v2.DeleteEvaluationRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.DeleteEvaluationResponse`
        """
        http_info = self._delete_evaluation_http_info(request)
        return self._call_api(**http_info)

    def delete_evaluation_async_invoker(self, request):
        http_info = self._delete_evaluation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_evaluation_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/marketplace/evaluation/{evaluation_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEvaluationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'evaluation_id' in local_var_params:
            path_params['evaluation_id'] = local_var_params['evaluation_id']

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

    def delete_evaluation_reply_async(self, request):
        r"""删除回复

        删除回复
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEvaluationReply
        :type request: :class:`huaweicloudsdkcloudide.v2.DeleteEvaluationReplyRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.DeleteEvaluationReplyResponse`
        """
        http_info = self._delete_evaluation_reply_http_info(request)
        return self._call_api(**http_info)

    def delete_evaluation_reply_async_invoker(self, request):
        http_info = self._delete_evaluation_reply_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_evaluation_reply_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/marketplace/evaluation/reply/{reply_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEvaluationReplyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'reply_id' in local_var_params:
            path_params['reply_id'] = local_var_params['reply_id']

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

    def list_extensions_async(self, request):
        r"""查询插件列表

        查询插件列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListExtensions
        :type request: :class:`huaweicloudsdkcloudide.v2.ListExtensionsRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.ListExtensionsResponse`
        """
        http_info = self._list_extensions_http_info(request)
        return self._call_api(**http_info)

    def list_extensions_async_invoker(self, request):
        http_info = self._list_extensions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_extensions_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/marketplace/extension/extensionquery",
            "request_type": request.__class__.__name__,
            "response_type": "ListExtensionsResponse"
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

    def list_project_templates_async(self, request):
        r"""查询技术栈模板工程

        查询技术栈模板工程
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectTemplates
        :type request: :class:`huaweicloudsdkcloudide.v2.ListProjectTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.ListProjectTemplatesResponse`
        """
        http_info = self._list_project_templates_http_info(request)
        return self._call_api(**http_info)

    def list_project_templates_async_invoker(self, request):
        http_info = self._list_project_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_project_templates_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'arch' in local_var_params:
            query_params.append(('arch', local_var_params['arch']))
        if 'stack_id' in local_var_params:
            query_params.append(('stack_id', local_var_params['stack_id']))

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

    def list_publisher_async(self, request):
        r"""获取当前用户下的发布商列表

        获取当前用户下的发布商列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPublisher
        :type request: :class:`huaweicloudsdkcloudide.v2.ListPublisherRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.ListPublisherResponse`
        """
        http_info = self._list_publisher_http_info(request)
        return self._call_api(**http_info)

    def list_publisher_async_invoker(self, request):
        http_info = self._list_publisher_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_publisher_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/marketplace/publishers/mine",
            "request_type": request.__class__.__name__,
            "response_type": "ListPublisherResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

    def list_stacks_async(self, request):
        r"""按region获取标签所有技术栈

        按region获取标签所有技术栈
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListStacks
        :type request: :class:`huaweicloudsdkcloudide.v2.ListStacksRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.ListStacksResponse`
        """
        http_info = self._list_stacks_http_info(request)
        return self._call_api(**http_info)

    def list_stacks_async_invoker(self, request):
        http_info = self._list_stacks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_stacks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/stacks/tag",
            "request_type": request.__class__.__name__,
            "response_type": "ListStacksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def publish_extension_async(self, request):
        r"""插件发布

        插件发布
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PublishExtension
        :type request: :class:`huaweicloudsdkcloudide.v2.PublishExtensionRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.PublishExtensionResponse`
        """
        http_info = self._publish_extension_http_info(request)
        return self._call_api(**http_info)

    def publish_extension_async_invoker(self, request):
        http_info = self._publish_extension_http_info(request)
        return AsyncInvoker(self, http_info)

    def _publish_extension_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/marketplace/extension/{task_id}/archiving",
            "request_type": request.__class__.__name__,
            "response_type": "PublishExtensionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}
        if 'x_publisher_token' in local_var_params:
            header_params['x-publisher-token'] = local_var_params['x_publisher_token']

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

    def show_account_status_async(self, request):
        r"""查询当前帐号访问权限

        查询当前帐号访问权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAccountStatus
        :type request: :class:`huaweicloudsdkcloudide.v2.ShowAccountStatusRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.ShowAccountStatusResponse`
        """
        http_info = self._show_account_status_http_info(request)
        return self._call_api(**http_info)

    def show_account_status_async_invoker(self, request):
        http_info = self._show_account_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_account_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/permission/account/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAccountStatusResponse"
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

    def show_category_list_async(self, request):
        r"""查询插件分类

        查询插件分类
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCategoryList
        :type request: :class:`huaweicloudsdkcloudide.v2.ShowCategoryListRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.ShowCategoryListResponse`
        """
        http_info = self._show_category_list_http_info(request)
        return self._call_api(**http_info)

    def show_category_list_async_invoker(self, request):
        http_info = self._show_category_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_category_list_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/marketplace/extension/category",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCategoryListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_num' in local_var_params:
            query_params.append(('page_num', local_var_params['page_num']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'scene_name' in local_var_params:
            query_params.append(('scene_name', local_var_params['scene_name']))
        if 'support_ide' in local_var_params:
            query_params.append(('support_ide', local_var_params['support_ide']))
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_extension_authorization_async(self, request):
        r"""查询ide实例对插件的授权情况

        查询ide实例对插件的授权情况，同意授权的插件能在ide实例内携带登陆用户的token调用第三方服务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowExtensionAuthorization
        :type request: :class:`huaweicloudsdkcloudide.v2.ShowExtensionAuthorizationRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.ShowExtensionAuthorizationResponse`
        """
        http_info = self._show_extension_authorization_http_info(request)
        return self._call_api(**http_info)

    def show_extension_authorization_async_invoker(self, request):
        http_info = self._show_extension_authorization_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_extension_authorization_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/extension/authorization",
            "request_type": request.__class__.__name__,
            "response_type": "ShowExtensionAuthorizationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'extension_version' in local_var_params:
            query_params.append(('extension_version', local_var_params['extension_version']))
        if 'identifier' in local_var_params:
            query_params.append(('identifier', local_var_params['identifier']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))

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

    def show_extension_detail_async(self, request):
        r"""查询插件详细信息

        查询插件详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowExtensionDetail
        :type request: :class:`huaweicloudsdkcloudide.v2.ShowExtensionDetailRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.ShowExtensionDetailResponse`
        """
        http_info = self._show_extension_detail_http_info(request)
        return self._call_api(**http_info)

    def show_extension_detail_async_invoker(self, request):
        http_info = self._show_extension_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_extension_detail_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/marketplace/extension/public/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowExtensionDetailResponse"
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

    def show_extension_evaluation_async(self, request):
        r"""查询插件评价

        查询插件评价
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowExtensionEvaluation
        :type request: :class:`huaweicloudsdkcloudide.v2.ShowExtensionEvaluationRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.ShowExtensionEvaluationResponse`
        """
        http_info = self._show_extension_evaluation_http_info(request)
        return self._call_api(**http_info)

    def show_extension_evaluation_async_invoker(self, request):
        http_info = self._show_extension_evaluation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_extension_evaluation_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/marketplace/feedback/evaluation",
            "request_type": request.__class__.__name__,
            "response_type": "ShowExtensionEvaluationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'extension_id' in local_var_params:
            query_params.append(('extension_id', local_var_params['extension_id']))
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_extension_evaluation_star_async(self, request):
        r"""查询插件评星

        查询插件评星
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowExtensionEvaluationStar
        :type request: :class:`huaweicloudsdkcloudide.v2.ShowExtensionEvaluationStarRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.ShowExtensionEvaluationStarResponse`
        """
        http_info = self._show_extension_evaluation_star_http_info(request)
        return self._call_api(**http_info)

    def show_extension_evaluation_star_async_invoker(self, request):
        http_info = self._show_extension_evaluation_star_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_extension_evaluation_star_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/marketplace/feedback/star",
            "request_type": request.__class__.__name__,
            "response_type": "ShowExtensionEvaluationStarResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'extension_id' in local_var_params:
            query_params.append(('extension_id', local_var_params['extension_id']))
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_extension_testing_result_async(self, request):
        r"""获取插件检测结果

        获取插件检测结果
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowExtensionTestingResult
        :type request: :class:`huaweicloudsdkcloudide.v2.ShowExtensionTestingResultRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.ShowExtensionTestingResultResponse`
        """
        http_info = self._show_extension_testing_result_http_info(request)
        return self._call_api(**http_info)

    def show_extension_testing_result_async_invoker(self, request):
        http_info = self._show_extension_testing_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_extension_testing_result_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/marketplace/extension/{task_id}/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowExtensionTestingResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}
        if 'x_publisher_token' in local_var_params:
            header_params['x-publisher-token'] = local_var_params['x_publisher_token']

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

    def show_price_async(self, request):
        r"""获取技术栈计费信息

        获取技术栈计费信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPrice
        :type request: :class:`huaweicloudsdkcloudide.v2.ShowPriceRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.ShowPriceResponse`
        """
        http_info = self._show_price_http_info(request)
        return self._call_api(**http_info)

    def show_price_async_invoker(self, request):
        http_info = self._show_price_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_price_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/stacks/price",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPriceResponse"
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

    def upload_extension_file_async(self, request):
        r"""上传插件

        上传插件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UploadExtensionFile
        :type request: :class:`huaweicloudsdkcloudide.v2.UploadExtensionFileRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.UploadExtensionFileResponse`
        """
        http_info = self._upload_extension_file_http_info(request)
        return self._call_api(**http_info)

    def upload_extension_file_async_invoker(self, request):
        http_info = self._upload_extension_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upload_extension_file_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/marketplace/file/plugin",
            "request_type": request.__class__.__name__,
            "response_type": "UploadExtensionFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'official' in local_var_params:
            query_params.append(('official', local_var_params['official']))

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

    def upload_file_publisher_async(self, request):
        r"""文件上传归一化

        文件上传归一化
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UploadFilePublisher
        :type request: :class:`huaweicloudsdkcloudide.v2.UploadFilePublisherRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.UploadFilePublisherResponse`
        """
        http_info = self._upload_file_publisher_http_info(request)
        return self._call_api(**http_info)

    def upload_file_publisher_async_invoker(self, request):
        http_info = self._upload_file_publisher_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upload_file_publisher_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/fileservice/file/upload",
            "request_type": request.__class__.__name__,
            "response_type": "UploadFilePublisherResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_publisher_token' in local_var_params:
            header_params['x-publisher-token'] = local_var_params['x_publisher_token']

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']
        if 'publisher_id' in local_var_params:
            form_params['publisher_id'] = local_var_params['publisher_id']
        if 'chunk_index' in local_var_params:
            form_params['chunk_index'] = local_var_params['chunk_index']
        if 'merge' in local_var_params:
            form_params['merge'] = local_var_params['merge']
        if 'total_chunk_num' in local_var_params:
            form_params['total_chunk_num'] = local_var_params['total_chunk_num']
        if 'parent_file_size' in local_var_params:
            form_params['parent_file_size'] = local_var_params['parent_file_size']
        if 'parent_file_name' in local_var_params:
            form_params['parent_file_name'] = local_var_params['parent_file_name']
        if 'override' in local_var_params:
            form_params['override'] = local_var_params['override']
        if 'chunk_md5' in local_var_params:
            form_params['chunk_md5'] = local_var_params['chunk_md5']
        if 'parent_file_sha256' in local_var_params:
            form_params['parent_file_sha256'] = local_var_params['parent_file_sha256']
        if 'task_id' in local_var_params:
            form_params['task_id'] = local_var_params['task_id']

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

    def check_instance_access_async(self, request):
        r"""查询用户是否有权限访问某个IDE实例

        查询用户是否有权限访问某个IDE实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckInstanceAccess
        :type request: :class:`huaweicloudsdkcloudide.v2.CheckInstanceAccessRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.CheckInstanceAccessResponse`
        """
        http_info = self._check_instance_access_http_info(request)
        return self._call_api(**http_info)

    def check_instance_access_async_invoker(self, request):
        http_info = self._check_instance_access_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_instance_access_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/instances/{instance_id}/access",
            "request_type": request.__class__.__name__,
            "response_type": "CheckInstanceAccessResponse"
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def check_name_async(self, request):
        r"""查询IDE实例名是否重复

        查询IDE实例名是否重复
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckName
        :type request: :class:`huaweicloudsdkcloudide.v2.CheckNameRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.CheckNameResponse`
        """
        http_info = self._check_name_http_info(request)
        return self._call_api(**http_info)

    def check_name_async_invoker(self, request):
        http_info = self._check_name_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_name_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/instances/duplicate",
            "request_type": request.__class__.__name__,
            "response_type": "CheckNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'display_name' in local_var_params:
            query_params.append(('display_name', local_var_params['display_name']))

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

    def create_instance_async(self, request):
        r"""创建IDE实例

        创建IDE实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInstance
        :type request: :class:`huaweicloudsdkcloudide.v2.CreateInstanceRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.CreateInstanceResponse`
        """
        http_info = self._create_instance_http_info(request)
        return self._call_api(**http_info)

    def create_instance_async_invoker(self, request):
        http_info = self._create_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{org_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'org_id' in local_var_params:
            path_params['org_id'] = local_var_params['org_id']

        query_params = []

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

    def create_instance_by3rd_async(self, request):
        r"""外部第三方集成商创建IDE实例

        创建IDE实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInstanceBy3rd
        :type request: :class:`huaweicloudsdkcloudide.v2.CreateInstanceBy3rdRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.CreateInstanceBy3rdResponse`
        """
        http_info = self._create_instance_by3rd_http_info(request)
        return self._call_api(**http_info)

    def create_instance_by3rd_async_invoker(self, request):
        http_info = self._create_instance_by3rd_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_instance_by3rd_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/instances",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceBy3rdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_label' in local_var_params:
            query_params.append(('instance_label', local_var_params['instance_label']))

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

    def delete_instance_async(self, request):
        r"""删除IDE实例

        删除IDE实例（同时删除磁盘数据）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteInstance
        :type request: :class:`huaweicloudsdkcloudide.v2.DeleteInstanceRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.DeleteInstanceResponse`
        """
        http_info = self._delete_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_async_invoker(self, request):
        http_info = self._delete_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_instance_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstanceResponse"
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_instances_async(self, request):
        r"""查询IDE实例列表

        查询IDE实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstances
        :type request: :class:`huaweicloudsdkcloudide.v2.ListInstancesRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.ListInstancesResponse`
        """
        http_info = self._list_instances_http_info(request)
        return self._call_api(**http_info)

    def list_instances_async_invoker(self, request):
        http_info = self._list_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instances_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstancesResponse"
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
        if 'is_temporary' in local_var_params:
            query_params.append(('is_temporary', local_var_params['is_temporary']))
        if 'label' in local_var_params:
            query_params.append(('label', local_var_params['label']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_org_instances_async(self, request):
        r"""查询某个租户下的IDE实例列表

        查询某个租户下的IDE实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOrgInstances
        :type request: :class:`huaweicloudsdkcloudide.v2.ListOrgInstancesRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.ListOrgInstancesResponse`
        """
        http_info = self._list_org_instances_http_info(request)
        return self._call_api(**http_info)

    def list_org_instances_async_invoker(self, request):
        http_info = self._list_org_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_org_instances_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{org_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListOrgInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'org_id' in local_var_params:
            path_params['org_id'] = local_var_params['org_id']

        query_params = []
        if 'is_temporary' in local_var_params:
            query_params.append(('is_temporary', local_var_params['is_temporary']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))

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

    def show_instance_async(self, request):
        r"""查询某个IDE实例

        查询某个IDE实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstance
        :type request: :class:`huaweicloudsdkcloudide.v2.ShowInstanceRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.ShowInstanceResponse`
        """
        http_info = self._show_instance_http_info(request)
        return self._call_api(**http_info)

    def show_instance_async_invoker(self, request):
        http_info = self._show_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_instance_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceResponse"
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_instance_status_info_async(self, request):
        r"""查询某个IDE实例的状态

        查询某个IDE实例的状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstanceStatusInfo
        :type request: :class:`huaweicloudsdkcloudide.v2.ShowInstanceStatusInfoRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.ShowInstanceStatusInfoResponse`
        """
        http_info = self._show_instance_status_info_http_info(request)
        return self._call_api(**http_info)

    def show_instance_status_info_async_invoker(self, request):
        http_info = self._show_instance_status_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_instance_status_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/instances/{instance_id}/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceStatusInfoResponse"
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def start_instance_async(self, request):
        r"""启动IDE实例

        启动IDE实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartInstance
        :type request: :class:`huaweicloudsdkcloudide.v2.StartInstanceRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.StartInstanceResponse`
        """
        http_info = self._start_instance_http_info(request)
        return self._call_api(**http_info)

    def start_instance_async_invoker(self, request):
        http_info = self._start_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_instance_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/instances/{instance_id}/runtime",
            "request_type": request.__class__.__name__,
            "response_type": "StartInstanceResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def stop_instance_async(self, request):
        r"""停止IDE实例

        停止IDE实例（不删除磁盘数据）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopInstance
        :type request: :class:`huaweicloudsdkcloudide.v2.StopInstanceRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.StopInstanceResponse`
        """
        http_info = self._stop_instance_http_info(request)
        return self._call_api(**http_info)

    def stop_instance_async_invoker(self, request):
        http_info = self._stop_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_instance_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/instances/{instance_id}/runtime",
            "request_type": request.__class__.__name__,
            "response_type": "StopInstanceResponse"
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_instance_async(self, request):
        r"""修改IDE实例

        修改IDE实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstance
        :type request: :class:`huaweicloudsdkcloudide.v2.UpdateInstanceRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.UpdateInstanceResponse`
        """
        http_info = self._update_instance_http_info(request)
        return self._call_api(**http_info)

    def update_instance_async_invoker(self, request):
        http_info = self._update_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_instance_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_instance_activity_async(self, request):
        r"""刷新IDE实例活跃状态

        刷新IDE实例活跃状态，超过该实例设置的过期时间后实例自动关闭。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstanceActivity
        :type request: :class:`huaweicloudsdkcloudide.v2.UpdateInstanceActivityRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.UpdateInstanceActivityResponse`
        """
        http_info = self._update_instance_activity_http_info(request)
        return self._call_api(**http_info)

    def update_instance_activity_async_invoker(self, request):
        http_info = self._update_instance_activity_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_instance_activity_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/instances/{instance_id}/activity",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceActivityResponse"
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_acceptance_async(self, request):
        r"""CreateAcceptance接口

        create a acceptance
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAcceptance
        :type request: :class:`huaweicloudsdkcloudide.v2.CreateAcceptanceRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.CreateAcceptanceResponse`
        """
        http_info = self._create_acceptance_http_info(request)
        return self._call_api(**http_info)

    def create_acceptance_async_invoker(self, request):
        http_info = self._create_acceptance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_acceptance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/aims/codemodelserver/code-generation/acceptance",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAcceptanceResponse"
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

    def create_apply_async(self, request):
        r"""CreateJoinRequest接口

        create a join-request
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateApply
        :type request: :class:`huaweicloudsdkcloudide.v2.CreateApplyRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.CreateApplyResponse`
        """
        http_info = self._create_apply_http_info(request)
        return self._call_api(**http_info)

    def create_apply_async_invoker(self, request):
        http_info = self._create_apply_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_apply_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/aims/codemodelserver/join-request",
            "request_type": request.__class__.__name__,
            "response_type": "CreateApplyResponse"
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

    def create_event_async(self, request):
        r"""CreateEvent接口

        create an event
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEvent
        :type request: :class:`huaweicloudsdkcloudide.v2.CreateEventRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.CreateEventResponse`
        """
        http_info = self._create_event_http_info(request)
        return self._call_api(**http_info)

    def create_event_async_invoker(self, request):
        http_info = self._create_event_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_event_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/aims/codemodelserver/management/event",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEventResponse"
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

    def create_login_async(self, request):
        r"""CreateLogin接口

        create a login
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateLogin
        :type request: :class:`huaweicloudsdkcloudide.v2.CreateLoginRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.CreateLoginResponse`
        """
        http_info = self._create_login_http_info(request)
        return self._call_api(**http_info)

    def create_login_async_invoker(self, request):
        http_info = self._create_login_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_login_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/aims/codemodelserver/code-generation/login",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLoginResponse"
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

    def create_request_async(self, request):
        r"""Create Request接口

        create a code generation request.
        
        if agent receives a code generation request, it will:
        - record the request into mysql,
        - decompose the request into &#x60;topn&#x60; tasks.
        - send the tasks to kafka.
        
        if agent receives a duplicated code generation request, it will not decompose request and send to kafka.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRequest
        :type request: :class:`huaweicloudsdkcloudide.v2.CreateRequestRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.CreateRequestResponse`
        """
        http_info = self._create_request_http_info(request)
        return self._call_api(**http_info)

    def create_request_async_invoker(self, request):
        http_info = self._create_request_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_request_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/aims/codemodelserver/code-generation/request",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRequestResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'topn' in local_var_params:
            query_params.append(('topn', local_var_params['topn']))
        if 'scenario' in local_var_params:
            query_params.append(('scenario', local_var_params['scenario']))
        if 'resubmit' in local_var_params:
            query_params.append(('resubmit', local_var_params['resubmit']))
        if 'model_id' in local_var_params:
            query_params.append(('model_id', local_var_params['model_id']))
        if 'request_type' in local_var_params:
            query_params.append(('request_type', local_var_params['request_type']))

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

    def show_result_async(self, request):
        r"""Show Result接口

        get the result of the code generation request.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResult
        :type request: :class:`huaweicloudsdkcloudide.v2.ShowResultRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.ShowResultResponse`
        """
        http_info = self._show_result_http_info(request)
        return self._call_api(**http_info)

    def show_result_async_invoker(self, request):
        http_info = self._show_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_result_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/aims/codemodelserver/code-generation/results",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'request_id' in local_var_params:
            query_params.append(('request_id', local_var_params['request_id']))

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

    def start_chat_async(self, request):
        r"""start_chat_codebreezetsbot_v1_devmind_tsbot_start_chat_post接口

        开启对话
        :param data: example: {\&quot;user_type\&quot;: \&quot;IDE\&quot;}
        :return:
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartChat
        :type request: :class:`huaweicloudsdkcloudide.v2.StartChatRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.StartChatResponse`
        """
        http_info = self._start_chat_http_info(request)
        return self._call_api(**http_info)

    def start_chat_async_invoker(self, request):
        http_info = self._start_chat_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_chat_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/codebreezetsbot/devmind/tsbot/start-chat",
            "request_type": request.__class__.__name__,
            "response_type": "StartChatResponse"
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

    def sync_chat_async(self, request):
        r"""async_chat_codebreezetsbot_v1_devmind_tsbot_async_chat_post接口

        异步聊天请求
        :param data: ChatRequestMessage
        :return:
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SyncChat
        :type request: :class:`huaweicloudsdkcloudide.v2.SyncChatRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.SyncChatResponse`
        """
        http_info = self._sync_chat_http_info(request)
        return self._call_api(**http_info)

    def sync_chat_async_invoker(self, request):
        http_info = self._sync_chat_http_info(request)
        return AsyncInvoker(self, http_info)

    def _sync_chat_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/codebreezetsbot/devmind/tsbot/async-chat",
            "request_type": request.__class__.__name__,
            "response_type": "SyncChatResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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

    def sync_get_chat_result_async(self, request):
        r"""async_get_chat_result_codebreezetsbot_v1_devmind_tsbot_async_get_chat_result_post接口

        异步聊天获取结果
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SyncGetChatResult
        :type request: :class:`huaweicloudsdkcloudide.v2.SyncGetChatResultRequest`
        :rtype: :class:`huaweicloudsdkcloudide.v2.SyncGetChatResultResponse`
        """
        http_info = self._sync_get_chat_result_http_info(request)
        return self._call_api(**http_info)

    def sync_get_chat_result_async_invoker(self, request):
        http_info = self._sync_get_chat_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _sync_get_chat_result_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/codebreezetsbot/devmind/tsbot/async-get-chat-result",
            "request_type": request.__class__.__name__,
            "response_type": "SyncGetChatResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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
