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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkmetastudio'")


class MetaStudioAsyncClient(Client):
    def __init__(self):
        super(MetaStudioAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkmetastudio.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "MetaStudioAsyncClient":
                raise TypeError("client type error, support client type is MetaStudioAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_active_code_async(self, request):
        r"""创建激活码

        该接口用于创建激活码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateActiveCode
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateActiveCodeRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateActiveCodeResponse`
        """
        http_info = self._create_active_code_http_info(request)
        return self._call_api(**http_info)

    def create_active_code_async_invoker(self, request):
        http_info = self._create_active_code_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_active_code_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/active-code",
            "request_type": request.__class__.__name__,
            "response_type": "CreateActiveCodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_active_code_async(self, request):
        r"""删除激活码

        该接口用于删除激活码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteActiveCode
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteActiveCodeRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteActiveCodeResponse`
        """
        http_info = self._delete_active_code_http_info(request)
        return self._call_api(**http_info)

    def delete_active_code_async_invoker(self, request):
        http_info = self._delete_active_code_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_active_code_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/active-code/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteActiveCodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_active_code_async(self, request):
        r"""查询激活码列表

        该接口用于查询激活码列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListActiveCode
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListActiveCodeRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListActiveCodeResponse`
        """
        http_info = self._list_active_code_http_info(request)
        return self._call_api(**http_info)

    def list_active_code_async_invoker(self, request):
        http_info = self._list_active_code_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_active_code_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/active-code",
            "request_type": request.__class__.__name__,
            "response_type": "ListActiveCodeResponse"
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
        if 'robot_id' in local_var_params:
            query_params.append(('robot_id', local_var_params['robot_id']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def reset_active_code_async(self, request):
        r"""重置激活码

        该接口用于重置激活码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetActiveCode
        :type request: :class:`huaweicloudsdkmetastudio.v1.ResetActiveCodeRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ResetActiveCodeResponse`
        """
        http_info = self._reset_active_code_http_info(request)
        return self._call_api(**http_info)

    def reset_active_code_async_invoker(self, request):
        http_info = self._reset_active_code_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reset_active_code_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/digital-human-chat/active-code/{active_code_id}/reset",
            "request_type": request.__class__.__name__,
            "response_type": "ResetActiveCodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'active_code_id' in local_var_params:
            path_params['active_code_id'] = local_var_params['active_code_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_active_code_async(self, request):
        r"""查询激活码详情

        该接口用于查询激活码详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowActiveCode
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowActiveCodeRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowActiveCodeResponse`
        """
        http_info = self._show_active_code_http_info(request)
        return self._call_api(**http_info)

    def show_active_code_async_invoker(self, request):
        http_info = self._show_active_code_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_active_code_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/active-code/{active_code_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowActiveCodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'active_code_id' in local_var_params:
            path_params['active_code_id'] = local_var_params['active_code_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_active_code_async(self, request):
        r"""修改激活码

        该接口用于修改激活码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateActiveCode
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateActiveCodeRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateActiveCodeResponse`
        """
        http_info = self._update_active_code_http_info(request)
        return self._call_api(**http_info)

    def update_active_code_async_invoker(self, request):
        http_info = self._update_active_code_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_active_code_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/digital-human-chat/active-code/{active_code_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateActiveCodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'active_code_id' in local_var_params:
            path_params['active_code_id'] = local_var_params['active_code_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_agency_with_role_type_async(self, request):
        r"""创建委托

        该接口用于创建委托。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAgencyWithRoleType
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateAgencyWithRoleTypeRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateAgencyWithRoleTypeResponse`
        """
        http_info = self._create_agency_with_role_type_http_info(request)
        return self._call_api(**http_info)

    def create_agency_with_role_type_async_invoker(self, request):
        http_info = self._create_agency_with_role_type_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_agency_with_role_type_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/agency/{role_type}",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAgencyWithRoleTypeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'role_type' in local_var_params:
            path_params['role_type'] = local_var_params['role_type']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_agency_with_role_type_async(self, request):
        r"""删除委托

        该接口用于删除项目下委托。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAgencyWithRoleType
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteAgencyWithRoleTypeRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteAgencyWithRoleTypeResponse`
        """
        http_info = self._delete_agency_with_role_type_http_info(request)
        return self._call_api(**http_info)

    def delete_agency_with_role_type_async_invoker(self, request):
        http_info = self._delete_agency_with_role_type_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_agency_with_role_type_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/digital-human-chat/agency/{role_type}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAgencyWithRoleTypeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'role_type' in local_var_params:
            path_params['role_type'] = local_var_params['role_type']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_agency_async(self, request):
        r"""查询委托

        该接口用于查询项目下委托
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAgency
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowAgencyRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowAgencyResponse`
        """
        http_info = self._show_agency_http_info(request)
        return self._call_api(**http_info)

    def show_agency_async_invoker(self, request):
        http_info = self._show_agency_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_agency_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/agency",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAgencyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'role_type' in local_var_params:
            query_params.append(('role_type', local_var_params['role_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_asr_vocabulary_async(self, request):
        r"""创建热词表

        该接口用于创建热词表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAsrVocabulary
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateAsrVocabularyRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateAsrVocabularyResponse`
        """
        http_info = self._create_asr_vocabulary_http_info(request)
        return self._call_api(**http_info)

    def create_asr_vocabulary_async_invoker(self, request):
        http_info = self._create_asr_vocabulary_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_asr_vocabulary_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/asr-vocabulary",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAsrVocabularyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_asr_vocabulary_async(self, request):
        r"""删除热词表

        该接口用于删除热词表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAsrVocabulary
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteAsrVocabularyRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteAsrVocabularyResponse`
        """
        http_info = self._delete_asr_vocabulary_http_info(request)
        return self._call_api(**http_info)

    def delete_asr_vocabulary_async_invoker(self, request):
        http_info = self._delete_asr_vocabulary_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_asr_vocabulary_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/digital-human-chat/asr-vocabulary/{asr_vocabulary_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAsrVocabularyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asr_vocabulary_id' in local_var_params:
            path_params['asr_vocabulary_id'] = local_var_params['asr_vocabulary_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_asr_vocabulary_async(self, request):
        r"""查询热词表列表

        该接口用于查询热词表列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAsrVocabulary
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListAsrVocabularyRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListAsrVocabularyResponse`
        """
        http_info = self._list_asr_vocabulary_http_info(request)
        return self._call_api(**http_info)

    def list_asr_vocabulary_async_invoker(self, request):
        http_info = self._list_asr_vocabulary_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_asr_vocabulary_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/asr-vocabulary",
            "request_type": request.__class__.__name__,
            "response_type": "ListAsrVocabularyResponse"
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
        if 'vocabulary_type' in local_var_params:
            query_params.append(('vocabulary_type', local_var_params['vocabulary_type']))
        if 'language' in local_var_params:
            query_params.append(('language', local_var_params['language']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_asr_vocabulary_async(self, request):
        r"""查询热词表详情

        该接口用于查询热词表详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAsrVocabulary
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowAsrVocabularyRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowAsrVocabularyResponse`
        """
        http_info = self._show_asr_vocabulary_http_info(request)
        return self._call_api(**http_info)

    def show_asr_vocabulary_async_invoker(self, request):
        http_info = self._show_asr_vocabulary_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_asr_vocabulary_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/asr-vocabulary/{asr_vocabulary_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAsrVocabularyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asr_vocabulary_id' in local_var_params:
            path_params['asr_vocabulary_id'] = local_var_params['asr_vocabulary_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_asr_vocabulary_association_async(self, request):
        r"""查询热词表关联详情

        该接口用于查询热词表关联详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAsrVocabularyAssociation
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowAsrVocabularyAssociationRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowAsrVocabularyAssociationResponse`
        """
        http_info = self._show_asr_vocabulary_association_http_info(request)
        return self._call_api(**http_info)

    def show_asr_vocabulary_association_async_invoker(self, request):
        http_info = self._show_asr_vocabulary_association_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_asr_vocabulary_association_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/asr-vocabulary/association/{asr_vocabulary_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAsrVocabularyAssociationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asr_vocabulary_id' in local_var_params:
            path_params['asr_vocabulary_id'] = local_var_params['asr_vocabulary_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_asr_vocabulary_async(self, request):
        r"""修改热词表

        该接口用于修改热词表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAsrVocabulary
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateAsrVocabularyRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateAsrVocabularyResponse`
        """
        http_info = self._update_asr_vocabulary_http_info(request)
        return self._call_api(**http_info)

    def update_asr_vocabulary_async_invoker(self, request):
        http_info = self._update_asr_vocabulary_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_asr_vocabulary_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/digital-human-chat/asr-vocabulary/{asr_vocabulary_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAsrVocabularyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asr_vocabulary_id' in local_var_params:
            path_params['asr_vocabulary_id'] = local_var_params['asr_vocabulary_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_task_async(self, request):
        r"""删除导入导出任务

        删除导入导出任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTask
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteTaskRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteTaskResponse`
        """
        http_info = self._delete_task_http_info(request)
        return self._call_api(**http_info)

    def delete_task_async_invoker(self, request):
        http_info = self._delete_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_task_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/ies/task/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTaskResponse"
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

    def download_result_file_async(self, request):
        r"""下载导入或导出的结果文件

        下载导入或者导出结果文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadResultFile
        :type request: :class:`huaweicloudsdkmetastudio.v1.DownloadResultFileRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DownloadResultFileResponse`
        """
        http_info = self._download_result_file_http_info(request)
        return self._call_api(**http_info)

    def download_result_file_async_invoker(self, request):
        http_info = self._download_result_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_result_file_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/ies/result/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadResultFileResponse"
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

    def download_template_async(self, request):
        r"""下载信息导入模板

        下载导入模板，返回导入模板文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadTemplate
        :type request: :class:`huaweicloudsdkmetastudio.v1.DownloadTemplateRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DownloadTemplateResponse`
        """
        http_info = self._download_template_http_info(request)
        return self._call_api(**http_info)

    def download_template_async_invoker(self, request):
        http_info = self._download_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/ies/import/{resource}/template",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource' in local_var_params:
            path_params['resource'] = local_var_params['resource']

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

    def export_resource_async(self, request):
        r"""导出文件

        导出文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportResource
        :type request: :class:`huaweicloudsdkmetastudio.v1.ExportResourceRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ExportResourceResponse`
        """
        http_info = self._export_resource_http_info(request)
        return self._call_api(**http_info)

    def export_resource_async_invoker(self, request):
        http_info = self._export_resource_http_info(request)
        return AsyncInvoker(self, http_info)

    def _export_resource_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ies/export/{resource}",
            "request_type": request.__class__.__name__,
            "response_type": "ExportResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource' in local_var_params:
            path_params['resource'] = local_var_params['resource']

        query_params = []
        if 'business_id' in local_var_params:
            query_params.append(('business_id', local_var_params['business_id']))

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

    def import_resource_async(self, request):
        r"""导入文件

        导入文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportResource
        :type request: :class:`huaweicloudsdkmetastudio.v1.ImportResourceRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ImportResourceResponse`
        """
        http_info = self._import_resource_http_info(request)
        return self._call_api(**http_info)

    def import_resource_async_invoker(self, request):
        http_info = self._import_resource_http_info(request)
        return AsyncInvoker(self, http_info)

    def _import_resource_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ies/import/{resource}",
            "request_type": request.__class__.__name__,
            "response_type": "ImportResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource' in local_var_params:
            path_params['resource'] = local_var_params['resource']

        query_params = []
        if 'business_id' in local_var_params:
            query_params.append(('business_id', local_var_params['business_id']))

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

    def search_task_async(self, request):
        r"""分页查询导入导出任务列表

        分页查询导入导出任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SearchTask
        :type request: :class:`huaweicloudsdkmetastudio.v1.SearchTaskRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.SearchTaskResponse`
        """
        http_info = self._search_task_http_info(request)
        return self._call_api(**http_info)

    def search_task_async_invoker(self, request):
        http_info = self._search_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _search_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/ies/task",
            "request_type": request.__class__.__name__,
            "response_type": "SearchTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'resource' in local_var_params:
            query_params.append(('resource', local_var_params['resource']))
            collection_formats['resource'] = 'csv'
        if 'business_id' in local_var_params:
            query_params.append(('business_id', local_var_params['business_id']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

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

    def show_task_async(self, request):
        r"""查询导入导出任务详情

        查询导入导出任务详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTask
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowTaskRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowTaskResponse`
        """
        http_info = self._show_task_http_info(request)
        return self._call_api(**http_info)

    def show_task_async_invoker(self, request):
        http_info = self._show_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/ies/task/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTaskResponse"
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

    def create_dialog_url_async(self, request):
        r"""创建对话链接

        该接口用于创建对话链接。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDialogUrl
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateDialogUrlRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateDialogUrlResponse`
        """
        http_info = self._create_dialog_url_http_info(request)
        return self._call_api(**http_info)

    def create_dialog_url_async_invoker(self, request):
        http_info = self._create_dialog_url_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_dialog_url_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/create-dialog-url",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDialogUrlResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_smart_chat_job_async(self, request):
        r"""查询数字人智能交互任务列表

        该接口用于查询数字人智能交互任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSmartChatJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListSmartChatJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListSmartChatJobResponse`
        """
        http_info = self._list_smart_chat_job_http_info(request)
        return self._call_api(**http_info)

    def list_smart_chat_job_async_invoker(self, request):
        http_info = self._list_smart_chat_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_smart_chat_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/smart-chat-rooms/{room_id}/smart-chat-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListSmartChatJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']

        query_params = []
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_smart_chat_job_async(self, request):
        r"""查询数字人智能交互任务

        该接口用于查询数字人智能交互任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSmartChatJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowSmartChatJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowSmartChatJobResponse`
        """
        http_info = self._show_smart_chat_job_http_info(request)
        return self._call_api(**http_info)

    def show_smart_chat_job_async_invoker(self, request):
        http_info = self._show_smart_chat_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_smart_chat_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/smart-chat-rooms/{room_id}/smart-chat-jobs/{job_id}/state",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSmartChatJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def start_smart_chat_job_async(self, request):
        r"""启动数字人智能交互任务

        该接口用于启动数字人智能交互任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartSmartChatJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.StartSmartChatJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.StartSmartChatJobResponse`
        """
        http_info = self._start_smart_chat_job_http_info(request)
        return self._call_api(**http_info)

    def start_smart_chat_job_async_invoker(self, request):
        http_info = self._start_smart_chat_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_smart_chat_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/smart-chat-rooms/{room_id}/smart-chat-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "StartSmartChatJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']

        query_params = []
        if 'robot_id' in local_var_params:
            query_params.append(('robot_id', local_var_params['robot_id']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def stop_smart_chat_job_async(self, request):
        r"""结束数字人智能交互任务

        该接口用于结束数字人智能交互任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopSmartChatJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.StopSmartChatJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.StopSmartChatJobResponse`
        """
        http_info = self._stop_smart_chat_job_http_info(request)
        return self._call_api(**http_info)

    def stop_smart_chat_job_async_invoker(self, request):
        http_info = self._stop_smart_chat_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_smart_chat_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/smart-chat-rooms/{room_id}/smart-chat-jobs/{job_id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopSmartChatJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_dialog_report_config_async(self, request):
        r"""创建对话结果上报配置

        该接口用于创建对话结果上报配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDialogReportConfig
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateDialogReportConfigRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateDialogReportConfigResponse`
        """
        http_info = self._create_dialog_report_config_http_info(request)
        return self._call_api(**http_info)

    def create_dialog_report_config_async_invoker(self, request):
        http_info = self._create_dialog_report_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_dialog_report_config_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/dialog-report-config",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDialogReportConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_dialog_report_config_async(self, request):
        r"""删除对话结果上报配置

        该接口用于删除对话结果上报配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDialogReportConfig
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteDialogReportConfigRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteDialogReportConfigResponse`
        """
        http_info = self._delete_dialog_report_config_http_info(request)
        return self._call_api(**http_info)

    def delete_dialog_report_config_async_invoker(self, request):
        http_info = self._delete_dialog_report_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_dialog_report_config_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/digital-human-chat/dialog-report-config",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDialogReportConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_dialog_report_config_async(self, request):
        r"""查询对话结果上报配置

        该接口用于查询对话结果上报配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDialogReportConfig
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowDialogReportConfigRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowDialogReportConfigResponse`
        """
        http_info = self._show_dialog_report_config_http_info(request)
        return self._call_api(**http_info)

    def show_dialog_report_config_async_invoker(self, request):
        http_info = self._show_dialog_report_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_dialog_report_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/dialog-report-config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDialogReportConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_dialog_report_config_async(self, request):
        r"""修改对话结果上报配置

        该接口用于修改对话结果上报配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDialogReportConfig
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateDialogReportConfigRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateDialogReportConfigResponse`
        """
        http_info = self._update_dialog_report_config_http_info(request)
        return self._call_api(**http_info)

    def update_dialog_report_config_async_invoker(self, request):
        http_info = self._update_dialog_report_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_dialog_report_config_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/digital-human-chat/dialog-report-config",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDialogReportConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_execute_asset_action_async(self, request):
        r"""批量资产操作

        该接口用批量资产操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchExecuteAssetAction
        :type request: :class:`huaweicloudsdkmetastudio.v1.BatchExecuteAssetActionRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.BatchExecuteAssetActionResponse`
        """
        http_info = self._batch_execute_asset_action_http_info(request)
        return self._call_api(**http_info)

    def batch_execute_asset_action_async_invoker(self, request):
        http_info = self._batch_execute_asset_action_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_execute_asset_action_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-assets/batch-action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchExecuteAssetActionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_asset_by_replication_info_async(self, request):
        r"""复制资产

        该接口用于在Region B复制Region A的指定资产。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAssetByReplicationInfo
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateAssetByReplicationInfoRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateAssetByReplicationInfoResponse`
        """
        http_info = self._create_asset_by_replication_info_http_info(request)
        return self._call_api(**http_info)

    def create_asset_by_replication_info_async_invoker(self, request):
        http_info = self._create_asset_by_replication_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_asset_by_replication_info_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-assets-by-replication-info",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAssetByReplicationInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_digital_asset_async(self, request):
        r"""创建资产

        该接口用于在资产库中添加上传新的媒体资产。可上传的资产类型包括：分身数字人模型、背景图片、素材图片、素材视频、PPT等。
        &gt; 上传的图片、视频和背景图片，如果需要在视频制作素材中可见，需要设置system_properties。
        &gt; - 资产类型是IMAGE时，通过system_properties来区分背景图片（BACKGROUND_IMG）、素材图片（MATERIAL_IMG）。
        &gt; - 资产类型是VIDEO时，通过system_properties来区分素材视频（MATERIAL_VIDEO）、名片视频（BUSSINESS_CARD_VIDEO）。
        &gt; MetaStudio平台生成的视频，system_properties带CREATED_BY_PLATFORM。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDigitalAsset
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateDigitalAssetRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateDigitalAssetResponse`
        """
        http_info = self._create_digital_asset_http_info(request)
        return self._call_api(**http_info)

    def create_digital_asset_async_invoker(self, request):
        http_info = self._create_digital_asset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_digital_asset_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-assets",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDigitalAssetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']
        if 'x_mss_authorization' in local_var_params:
            header_params['X-MSS-Authorization'] = local_var_params['x_mss_authorization']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_asset_async(self, request):
        r"""删除资产

        该接口用于删除资产库中的媒体资产。调用该接口删除媒体资产时，媒体资产会放入回收站中，不会彻底删除。如需彻底删除资产，需增加“mode&#x3D;force”参数配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAsset
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteAssetRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteAssetResponse`
        """
        http_info = self._delete_asset_http_info(request)
        return self._call_api(**http_info)

    def delete_asset_async_invoker(self, request):
        http_info = self._delete_asset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_asset_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/digital-assets/{asset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAssetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

        query_params = []
        if 'mode' in local_var_params:
            query_params.append(('mode', local_var_params['mode']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_asset_summary_async(self, request):
        r"""查询资产概要

        该接口用于查询媒体资产库中指定的多个资产的概要信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAssetSummary
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListAssetSummaryRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListAssetSummaryResponse`
        """
        http_info = self._list_asset_summary_http_info(request)
        return self._call_api(**http_info)

    def list_asset_summary_async_invoker(self, request):
        http_info = self._list_asset_summary_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_asset_summary_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-assets/summarys",
            "request_type": request.__class__.__name__,
            "response_type": "ListAssetSummaryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_assets_async(self, request):
        r"""查询资产列表

        该接口用于查询资产库中的媒体资产列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAssets
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListAssetsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListAssetsResponse`
        """
        http_info = self._list_assets_http_info(request)
        return self._call_api(**http_info)

    def list_assets_async_invoker(self, request):
        http_info = self._list_assets_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_assets_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-assets",
            "request_type": request.__class__.__name__,
            "response_type": "ListAssetsResponse"
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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))
        if 'tag_combination_type' in local_var_params:
            query_params.append(('tag_combination_type', local_var_params['tag_combination_type']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'asset_type' in local_var_params:
            query_params.append(('asset_type', local_var_params['asset_type']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'asset_source' in local_var_params:
            query_params.append(('asset_source', local_var_params['asset_source']))
        if 'asset_state' in local_var_params:
            query_params.append(('asset_state', local_var_params['asset_state']))
        if 'style_id' in local_var_params:
            query_params.append(('style_id', local_var_params['style_id']))
        if 'accurate_query_field' in local_var_params:
            query_params.append(('accurate_query_field', local_var_params['accurate_query_field']))
            collection_formats['accurate_query_field'] = 'csv'
        if 'asset_id' in local_var_params:
            query_params.append(('asset_id', local_var_params['asset_id']))
            collection_formats['asset_id'] = 'csv'
        if 'sex' in local_var_params:
            query_params.append(('sex', local_var_params['sex']))
        if 'language' in local_var_params:
            query_params.append(('language', local_var_params['language']))
        if 'system_property' in local_var_params:
            query_params.append(('system_property', local_var_params['system_property']))
        if 'action_editable' in local_var_params:
            query_params.append(('action_editable', local_var_params['action_editable']))
        if 'is_with_action_library' in local_var_params:
            query_params.append(('is_with_action_library', local_var_params['is_with_action_library']))
        if 'is_movable' in local_var_params:
            query_params.append(('is_movable', local_var_params['is_movable']))
        if 'voice_provider' in local_var_params:
            query_params.append(('voice_provider', local_var_params['voice_provider']))
        if 'role' in local_var_params:
            query_params.append(('role', local_var_params['role']))
        if 'is_realtime_voice' in local_var_params:
            query_params.append(('is_realtime_voice', local_var_params['is_realtime_voice']))
        if 'human_model_2d_version' in local_var_params:
            query_params.append(('human_model_2d_version', local_var_params['human_model_2d_version']))
        if 'include_device_name' in local_var_params:
            query_params.append(('include_device_name', local_var_params['include_device_name']))
        if 'exclude_device_name' in local_var_params:
            query_params.append(('exclude_device_name', local_var_params['exclude_device_name']))
        if 'supported_service' in local_var_params:
            query_params.append(('supported_service', local_var_params['supported_service']))
        if 'app_user_id' in local_var_params:
            query_params.append(('app_user_id', local_var_params['app_user_id']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def restore_asset_async(self, request):
        r"""恢复被删除的资产

        该接口用于恢复被删除至回收站的媒体资产。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestoreAsset
        :type request: :class:`huaweicloudsdkmetastudio.v1.RestoreAssetRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.RestoreAssetResponse`
        """
        http_info = self._restore_asset_http_info(request)
        return self._call_api(**http_info)

    def restore_asset_async_invoker(self, request):
        http_info = self._restore_asset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _restore_asset_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-assets/{asset_id}/restore",
            "request_type": request.__class__.__name__,
            "response_type": "RestoreAssetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_asset_async(self, request):
        r"""查询资产详情

        该接口用于查询资产库中指定媒体资产的详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAsset
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowAssetRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowAssetResponse`
        """
        http_info = self._show_asset_http_info(request)
        return self._call_api(**http_info)

    def show_asset_async_invoker(self, request):
        http_info = self._show_asset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_asset_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-assets/{asset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAssetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_asset_replication_info_async(self, request):
        r"""查询资产复制信息

        当需要将资产从A Region复制到B Region时，先要在A Region调用该接口用于查询资产复制信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAssetReplicationInfo
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowAssetReplicationInfoRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowAssetReplicationInfoResponse`
        """
        http_info = self._show_asset_replication_info_http_info(request)
        return self._call_api(**http_info)

    def show_asset_replication_info_async_invoker(self, request):
        http_info = self._show_asset_replication_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_asset_replication_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-assets/{asset_id}/replication-info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAssetReplicationInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_digital_asset_async(self, request):
        r"""更新资产

        该接口用于更新资产库中的媒体资产信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDigitalAsset
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateDigitalAssetRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateDigitalAssetResponse`
        """
        http_info = self._update_digital_asset_http_info(request)
        return self._call_api(**http_info)

    def update_digital_asset_async_invoker(self, request):
        http_info = self._update_digital_asset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_digital_asset_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/digital-assets/{asset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDigitalAssetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_digital_human_business_card_async(self, request):
        r"""创建数字人名片制作

        该接口用于数字人名片制作任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDigitalHumanBusinessCard
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateDigitalHumanBusinessCardRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateDigitalHumanBusinessCardResponse`
        """
        http_info = self._create_digital_human_business_card_http_info(request)
        return self._call_api(**http_info)

    def create_digital_human_business_card_async_invoker(self, request):
        http_info = self._create_digital_human_business_card_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_digital_human_business_card_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-business-cards",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDigitalHumanBusinessCardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_digital_human_business_card_async(self, request):
        r"""删除数字人名片制作任务

        该接口用于删除数字人名片制作任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDigitalHumanBusinessCard
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteDigitalHumanBusinessCardRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteDigitalHumanBusinessCardResponse`
        """
        http_info = self._delete_digital_human_business_card_http_info(request)
        return self._call_api(**http_info)

    def delete_digital_human_business_card_async_invoker(self, request):
        http_info = self._delete_digital_human_business_card_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_digital_human_business_card_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/digital-human-business-cards/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDigitalHumanBusinessCardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_digital_human_business_card_async(self, request):
        r"""查询数字人名片制作任务列表

        该接口用于查询数字人名片制作任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDigitalHumanBusinessCard
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListDigitalHumanBusinessCardRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListDigitalHumanBusinessCardResponse`
        """
        http_info = self._list_digital_human_business_card_http_info(request)
        return self._call_api(**http_info)

    def list_digital_human_business_card_async_invoker(self, request):
        http_info = self._list_digital_human_business_card_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_digital_human_business_card_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-business-cards",
            "request_type": request.__class__.__name__,
            "response_type": "ListDigitalHumanBusinessCardResponse"
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
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'create_until' in local_var_params:
            query_params.append(('create_until', local_var_params['create_until']))
        if 'create_since' in local_var_params:
            query_params.append(('create_since', local_var_params['create_since']))
        if 'video_asset_name' in local_var_params:
            query_params.append(('video_asset_name', local_var_params['video_asset_name']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_digital_human_business_card_async(self, request):
        r"""查询数字人名片制作任务详情

        该接口用于查询数字人名片制作任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDigitalHumanBusinessCard
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowDigitalHumanBusinessCardRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowDigitalHumanBusinessCardResponse`
        """
        http_info = self._show_digital_human_business_card_http_info(request)
        return self._call_api(**http_info)

    def show_digital_human_business_card_async_invoker(self, request):
        http_info = self._show_digital_human_business_card_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_digital_human_business_card_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-business-cards/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDigitalHumanBusinessCardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_digital_human_business_card_async(self, request):
        r"""更新数字人名片制作

        该接口用于更新数字人名片制作任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDigitalHumanBusinessCard
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateDigitalHumanBusinessCardRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateDigitalHumanBusinessCardResponse`
        """
        http_info = self._update_digital_human_business_card_http_info(request)
        return self._call_api(**http_info)

    def update_digital_human_business_card_async_invoker(self, request):
        http_info = self._update_digital_human_business_card_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_digital_human_business_card_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/digital-human-business-cards/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDigitalHumanBusinessCardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_digital_human_video_async(self, request):
        r"""查询视频制作任务列表

        该接口用于查询视频制作任务列表。可查询分身数字人视频制作列表，照片数字人视频制作列表等。
        &gt; - 默认查询最近一个月任务记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDigitalHumanVideo
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListDigitalHumanVideoRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListDigitalHumanVideoResponse`
        """
        http_info = self._list_digital_human_video_http_info(request)
        return self._call_api(**http_info)

    def list_digital_human_video_async_invoker(self, request):
        http_info = self._list_digital_human_video_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_digital_human_video_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-videos",
            "request_type": request.__class__.__name__,
            "response_type": "ListDigitalHumanVideoResponse"
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
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'create_until' in local_var_params:
            query_params.append(('create_until', local_var_params['create_until']))
        if 'create_since' in local_var_params:
            query_params.append(('create_since', local_var_params['create_since']))
        if 'fuzzy_query_field' in local_var_params:
            query_params.append(('fuzzy_query_field', local_var_params['fuzzy_query_field']))
            collection_formats['fuzzy_query_field'] = 'csv'
        if 'script_id' in local_var_params:
            query_params.append(('script_id', local_var_params['script_id']))
        if 'asset_name' in local_var_params:
            query_params.append(('asset_name', local_var_params['asset_name']))
        if 'job_type' in local_var_params:
            query_params.append(('job_type', local_var_params['job_type']))
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))
        if 'job_ids' in local_var_params:
            query_params.append(('job_ids', local_var_params['job_ids']))
            collection_formats['job_ids'] = 'csv'

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def cancel2_d_digital_human_video_async(self, request):
        r"""取消等待中的分身数字人视频制作任务

        该接口用于取消等待中的分身数字人视频制作任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for Cancel2DDigitalHumanVideo
        :type request: :class:`huaweicloudsdkmetastudio.v1.Cancel2DDigitalHumanVideoRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.Cancel2DDigitalHumanVideoResponse`
        """
        http_info = self._cancel2_d_digital_human_video_http_info(request)
        return self._call_api(**http_info)

    def cancel2_d_digital_human_video_async_invoker(self, request):
        http_info = self._cancel2_d_digital_human_video_http_info(request)
        return AsyncInvoker(self, http_info)

    def _cancel2_d_digital_human_video_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/2d-digital-human-videos/{job_id}/cancel",
            "request_type": request.__class__.__name__,
            "response_type": "Cancel2DDigitalHumanVideoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create2_d_digital_human_video_async(self, request):
        r"""创建分身数字人视频制作任务

        该接口用于创建分身数字人视频制作任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for Create2DDigitalHumanVideo
        :type request: :class:`huaweicloudsdkmetastudio.v1.Create2DDigitalHumanVideoRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.Create2DDigitalHumanVideoResponse`
        """
        http_info = self._create2_d_digital_human_video_http_info(request)
        return self._call_api(**http_info)

    def create2_d_digital_human_video_async_invoker(self, request):
        http_info = self._create2_d_digital_human_video_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create2_d_digital_human_video_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/2d-digital-human-videos",
            "request_type": request.__class__.__name__,
            "response_type": "Create2DDigitalHumanVideoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show2_d_digital_human_video_async(self, request):
        r"""查询分身数字人视频制作任务详情

        该接口用于查询分身数字人视频制作任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for Show2DDigitalHumanVideo
        :type request: :class:`huaweicloudsdkmetastudio.v1.Show2DDigitalHumanVideoRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.Show2DDigitalHumanVideoResponse`
        """
        http_info = self._show2_d_digital_human_video_http_info(request)
        return self._call_api(**http_info)

    def show2_d_digital_human_video_async_invoker(self, request):
        http_info = self._show2_d_digital_human_video_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show2_d_digital_human_video_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/2d-digital-human-videos/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "Show2DDigitalHumanVideoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'show_script' in local_var_params:
            query_params.append(('show_script', local_var_params['show_script']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def cancel_photo_digital_human_video_async(self, request):
        r"""取消等待中的照片分身数字人视频制作任务

        该接口用于取消等待中的照片分身数字人视频制作任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CancelPhotoDigitalHumanVideo
        :type request: :class:`huaweicloudsdkmetastudio.v1.CancelPhotoDigitalHumanVideoRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CancelPhotoDigitalHumanVideoResponse`
        """
        http_info = self._cancel_photo_digital_human_video_http_info(request)
        return self._call_api(**http_info)

    def cancel_photo_digital_human_video_async_invoker(self, request):
        http_info = self._cancel_photo_digital_human_video_http_info(request)
        return AsyncInvoker(self, http_info)

    def _cancel_photo_digital_human_video_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/photo-digital-human-videos/{job_id}/cancel",
            "request_type": request.__class__.__name__,
            "response_type": "CancelPhotoDigitalHumanVideoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_photo_detection_async(self, request):
        r"""创建照片检测任务

        该接口用于创建照片检测任务，检测照片是否满足制作照片数字人的要求。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePhotoDetection
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreatePhotoDetectionRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreatePhotoDetectionResponse`
        """
        http_info = self._create_photo_detection_http_info(request)
        return self._call_api(**http_info)

    def create_photo_detection_async_invoker(self, request):
        http_info = self._create_photo_detection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_photo_detection_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/photo-detection",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePhotoDetectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_photo_digital_human_video_async(self, request):
        r"""创建照片分身数字人视频制作任务

        该接口用于创建照片分身数字人视频制作任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePhotoDigitalHumanVideo
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreatePhotoDigitalHumanVideoRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreatePhotoDigitalHumanVideoResponse`
        """
        http_info = self._create_photo_digital_human_video_http_info(request)
        return self._call_api(**http_info)

    def create_photo_digital_human_video_async_invoker(self, request):
        http_info = self._create_photo_digital_human_video_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_photo_digital_human_video_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/photo-digital-human-videos",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePhotoDigitalHumanVideoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_photo_detection_async(self, request):
        r"""查询照片检测任务详情

        该接口用于查询照片检测任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPhotoDetection
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowPhotoDetectionRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowPhotoDetectionResponse`
        """
        http_info = self._show_photo_detection_http_info(request)
        return self._call_api(**http_info)

    def show_photo_detection_async_invoker(self, request):
        http_info = self._show_photo_detection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_photo_detection_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/photo-detection/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPhotoDetectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_photo_digital_human_video_async(self, request):
        r"""查询照片分身数字人视频制作任务详情

        该接口用于查询照片分身数字人视频制作任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPhotoDigitalHumanVideo
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowPhotoDigitalHumanVideoRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowPhotoDigitalHumanVideoResponse`
        """
        http_info = self._show_photo_digital_human_video_http_info(request)
        return self._call_api(**http_info)

    def show_photo_digital_human_video_async_invoker(self, request):
        http_info = self._show_photo_digital_human_video_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_photo_digital_human_video_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/photo-digital-human-videos/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPhotoDigitalHumanVideoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'show_script' in local_var_params:
            query_params.append(('show_script', local_var_params['show_script']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_document_async(self, request):
        r"""上传文档

        该接口用于上传文档。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDocument
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateDocumentRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateDocumentResponse`
        """
        http_info = self._create_document_http_info(request)
        return self._call_api(**http_info)

    def create_document_async_invoker(self, request):
        http_info = self._create_document_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_document_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/wise-brain-manager/document",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDocumentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'knowledge_library_id' in local_var_params:
            query_params.append(('knowledge_library_id', local_var_params['knowledge_library_id']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def delete_document_async(self, request):
        r"""批量删除文档

        该接口用于批量删除文档。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDocument
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteDocumentRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteDocumentResponse`
        """
        http_info = self._delete_document_http_info(request)
        return self._call_api(**http_info)

    def delete_document_async_invoker(self, request):
        http_info = self._delete_document_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_document_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/wise-brain-manager/document/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDocumentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def download_document_async(self, request):
        r"""下载文档

        该接口用于下载文档。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadDocument
        :type request: :class:`huaweicloudsdkmetastudio.v1.DownloadDocumentRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DownloadDocumentResponse`
        """
        http_info = self._download_document_http_info(request)
        return self._call_api(**http_info)

    def download_document_async_invoker(self, request):
        http_info = self._download_document_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_document_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/wise-brain-manager/document/{document_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadDocumentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'document_id' in local_var_params:
            path_params['document_id'] = local_var_params['document_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_document_info_async(self, request):
        r"""查询文档列表

        该接口用于分页查询文档列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDocumentInfo
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListDocumentInfoRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListDocumentInfoResponse`
        """
        http_info = self._list_document_info_http_info(request)
        return self._call_api(**http_info)

    def list_document_info_async_invoker(self, request):
        http_info = self._list_document_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_document_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/wise-brain-manager/document",
            "request_type": request.__class__.__name__,
            "response_type": "ListDocumentInfoResponse"
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
        if 'knowledge_library_id' in local_var_params:
            query_params.append(('knowledge_library_id', local_var_params['knowledge_library_id']))
        if 'file_name' in local_var_params:
            query_params.append(('file_name', local_var_params['file_name']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_document_info_async(self, request):
        r"""查询文档详情

        该接口用于查询文档详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDocumentInfo
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowDocumentInfoRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowDocumentInfoResponse`
        """
        http_info = self._show_document_info_http_info(request)
        return self._call_api(**http_info)

    def show_document_info_async_invoker(self, request):
        http_info = self._show_document_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_document_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/wise-brain-manager/document/detail/{document_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDocumentInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'document_id' in local_var_params:
            path_params['document_id'] = local_var_params['document_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_document_async(self, request):
        r"""修改文档

        该接口用于修改文档
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDocument
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateDocumentRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateDocumentResponse`
        """
        http_info = self._update_document_http_info(request)
        return self._call_api(**http_info)

    def update_document_async_invoker(self, request):
        http_info = self._update_document_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_document_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/wise-brain-manager/document/update/{document_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDocumentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'document_id' in local_var_params:
            path_params['document_id'] = local_var_params['document_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def list_document_segment_async(self, request):
        r"""分页查询文档分段信息

        该接口用于分页查询文档分段信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDocumentSegment
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListDocumentSegmentRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListDocumentSegmentResponse`
        """
        http_info = self._list_document_segment_http_info(request)
        return self._call_api(**http_info)

    def list_document_segment_async_invoker(self, request):
        http_info = self._list_document_segment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_document_segment_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/wise-brain-manager/document-segment/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListDocumentSegmentResponse"
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
        if 'document_id' in local_var_params:
            query_params.append(('document_id', local_var_params['document_id']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def preview_document_segment_async(self, request):
        r"""文档分段效果预览

        该接口用于文档分段效果预览。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PreviewDocumentSegment
        :type request: :class:`huaweicloudsdkmetastudio.v1.PreviewDocumentSegmentRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.PreviewDocumentSegmentResponse`
        """
        http_info = self._preview_document_segment_http_info(request)
        return self._call_api(**http_info)

    def preview_document_segment_async_invoker(self, request):
        http_info = self._preview_document_segment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _preview_document_segment_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/wise-brain-manager/document-segment/preview",
            "request_type": request.__class__.__name__,
            "response_type": "PreviewDocumentSegmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'document_id' in local_var_params:
            query_params.append(('document_id', local_var_params['document_id']))
        if 'preview_lines' in local_var_params:
            query_params.append(('preview_lines', local_var_params['preview_lines']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def start_document_segment_async(self, request):
        r"""开始文档分段

        该接口用于开始文档分段任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartDocumentSegment
        :type request: :class:`huaweicloudsdkmetastudio.v1.StartDocumentSegmentRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.StartDocumentSegmentResponse`
        """
        http_info = self._start_document_segment_http_info(request)
        return self._call_api(**http_info)

    def start_document_segment_async_invoker(self, request):
        http_info = self._start_document_segment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_document_segment_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/wise-brain-manager/document-segment/segment",
            "request_type": request.__class__.__name__,
            "response_type": "StartDocumentSegmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_document_segment_info_async(self, request):
        r"""修改文档分段内容

        该接口用于文档分段内容。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDocumentSegmentInfo
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateDocumentSegmentInfoRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateDocumentSegmentInfoResponse`
        """
        http_info = self._update_document_segment_info_http_info(request)
        return self._call_api(**http_info)

    def update_document_segment_info_async_invoker(self, request):
        http_info = self._update_document_segment_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_document_segment_info_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/wise-brain-manager/document-segment/update",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDocumentSegmentInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_document_segment_param_async(self, request):
        r"""更新文档分段配置

        该接口用于更新文档分段配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDocumentSegmentParam
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateDocumentSegmentParamRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateDocumentSegmentParamResponse`
        """
        http_info = self._update_document_segment_param_http_info(request)
        return self._call_api(**http_info)

    def update_document_segment_param_async_invoker(self, request):
        http_info = self._update_document_segment_param_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_document_segment_param_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/wise-brain-manager/document-segment/{document_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDocumentSegmentParamResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'document_id' in local_var_params:
            path_params['document_id'] = local_var_params['document_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def confirm_file_upload_async(self, request):
        r"""确认文件已上传

        资产文件上传完毕后，通过该接口确认上传完成。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ConfirmFileUpload
        :type request: :class:`huaweicloudsdkmetastudio.v1.ConfirmFileUploadRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ConfirmFileUploadResponse`
        """
        http_info = self._confirm_file_upload_http_info(request)
        return self._call_api(**http_info)

    def confirm_file_upload_async_invoker(self, request):
        http_info = self._confirm_file_upload_http_info(request)
        return AsyncInvoker(self, http_info)

    def _confirm_file_upload_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/files/{file_id}/complete",
            "request_type": request.__class__.__name__,
            "response_type": "ConfirmFileUploadResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'file_id' in local_var_params:
            path_params['file_id'] = local_var_params['file_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_file_async(self, request):
        r"""创建文件并获取上传URL

        该接口用于创建文件并获取上传URL。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateFile
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateFileRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateFileResponse`
        """
        http_info = self._create_file_http_info(request)
        return self._call_api(**http_info)

    def create_file_async_invoker(self, request):
        http_info = self._create_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_file_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/files",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_large_file_async(self, request):
        r"""创建大文件

        该接口用于创建大文件（超过5G），获取分段上传URL。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateLargeFile
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateLargeFileRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateLargeFileResponse`
        """
        http_info = self._create_large_file_http_info(request)
        return self._call_api(**http_info)

    def create_large_file_async_invoker(self, request):
        http_info = self._create_large_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_large_file_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/large-files",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLargeFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_file_async(self, request):
        r"""删除文件

        该接口用于删除媒体资产库中指定的文件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteFile
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteFileRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteFileResponse`
        """
        http_info = self._delete_file_http_info(request)
        return self._call_api(**http_info)

    def delete_file_async_invoker(self, request):
        http_info = self._delete_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_file_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/files/{file_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'file_id' in local_var_params:
            path_params['file_id'] = local_var_params['file_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_hot_question_async(self, request):
        r"""创建热点问题

        该接口用于创建热点问题。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateHotQuestion
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateHotQuestionRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateHotQuestionResponse`
        """
        http_info = self._create_hot_question_http_info(request)
        return self._call_api(**http_info)

    def create_hot_question_async_invoker(self, request):
        http_info = self._create_hot_question_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_hot_question_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/hot-question",
            "request_type": request.__class__.__name__,
            "response_type": "CreateHotQuestionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_hot_question_async(self, request):
        r"""删除热点问题

        该接口用于删除热点问题。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteHotQuestion
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteHotQuestionRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteHotQuestionResponse`
        """
        http_info = self._delete_hot_question_http_info(request)
        return self._call_api(**http_info)

    def delete_hot_question_async_invoker(self, request):
        http_info = self._delete_hot_question_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_hot_question_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/hot-question/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteHotQuestionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_hot_question_async(self, request):
        r"""查询热点问题列表

        该接口用于查询热点问题列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHotQuestion
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListHotQuestionRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListHotQuestionResponse`
        """
        http_info = self._list_hot_question_http_info(request)
        return self._call_api(**http_info)

    def list_hot_question_async_invoker(self, request):
        http_info = self._list_hot_question_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_hot_question_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/hot-question",
            "request_type": request.__class__.__name__,
            "response_type": "ListHotQuestionResponse"
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
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'robot_id' in local_var_params:
            query_params.append(('robot_id', local_var_params['robot_id']))
        if 'language' in local_var_params:
            query_params.append(('language', local_var_params['language']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_hot_question_async(self, request):
        r"""查询热点问题详情

        该接口用于查询热点问题详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHotQuestion
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowHotQuestionRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowHotQuestionResponse`
        """
        http_info = self._show_hot_question_http_info(request)
        return self._call_api(**http_info)

    def show_hot_question_async_invoker(self, request):
        http_info = self._show_hot_question_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_hot_question_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/hot-question/{hot_question_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHotQuestionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'hot_question_id' in local_var_params:
            path_params['hot_question_id'] = local_var_params['hot_question_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_hot_question_async(self, request):
        r"""修改热点问题

        该接口用于修改热点问题。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateHotQuestion
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateHotQuestionRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateHotQuestionResponse`
        """
        http_info = self._update_hot_question_http_info(request)
        return self._call_api(**http_info)

    def update_hot_question_async_invoker(self, request):
        http_info = self._update_hot_question_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_hot_question_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/digital-human-chat/hot-question/{hot_question_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHotQuestionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'hot_question_id' in local_var_params:
            path_params['hot_question_id'] = local_var_params['hot_question_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_hot_words_async(self, request):
        r"""创建热词记录

        该接口用于创建热词记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateHotWords
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateHotWordsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateHotWordsResponse`
        """
        http_info = self._create_hot_words_http_info(request)
        return self._call_api(**http_info)

    def create_hot_words_async_invoker(self, request):
        http_info = self._create_hot_words_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_hot_words_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/hot-words",
            "request_type": request.__class__.__name__,
            "response_type": "CreateHotWordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_hot_words_async(self, request):
        r"""删除热词记录

        该接口用于删除热词记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteHotWords
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteHotWordsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteHotWordsResponse`
        """
        http_info = self._delete_hot_words_http_info(request)
        return self._call_api(**http_info)

    def delete_hot_words_async_invoker(self, request):
        http_info = self._delete_hot_words_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_hot_words_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/digital-human-chat/hot-words/{hot_words_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteHotWordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'hot_words_id' in local_var_params:
            path_params['hot_words_id'] = local_var_params['hot_words_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_hot_words_async(self, request):
        r"""查询热词记录列表

        该接口用于查询热词记录列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHotWords
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListHotWordsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListHotWordsResponse`
        """
        http_info = self._list_hot_words_http_info(request)
        return self._call_api(**http_info)

    def list_hot_words_async_invoker(self, request):
        http_info = self._list_hot_words_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_hot_words_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/hot-words",
            "request_type": request.__class__.__name__,
            "response_type": "ListHotWordsResponse"
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
        if 'robot_id' in local_var_params:
            query_params.append(('robot_id', local_var_params['robot_id']))
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
        if 'language' in local_var_params:
            query_params.append(('language', local_var_params['language']))
        if 'hot_words_type' in local_var_params:
            query_params.append(('hot_words_type', local_var_params['hot_words_type']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_hot_words_async(self, request):
        r"""查询配置热词记录详情

        该接口用于查询热词记录详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHotWords
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowHotWordsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowHotWordsResponse`
        """
        http_info = self._show_hot_words_http_info(request)
        return self._call_api(**http_info)

    def show_hot_words_async_invoker(self, request):
        http_info = self._show_hot_words_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_hot_words_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/hot-words/{hot_words_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHotWordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'hot_words_id' in local_var_params:
            path_params['hot_words_id'] = local_var_params['hot_words_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_hot_words_switch_async(self, request):
        r"""查询热词功能开关

        该接口用于查询热词功能开关。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHotWordsSwitch
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowHotWordsSwitchRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowHotWordsSwitchResponse`
        """
        http_info = self._show_hot_words_switch_http_info(request)
        return self._call_api(**http_info)

    def show_hot_words_switch_async_invoker(self, request):
        http_info = self._show_hot_words_switch_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_hot_words_switch_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/hot-words-switch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHotWordsSwitchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'robot_id' in local_var_params:
            query_params.append(('robot_id', local_var_params['robot_id']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_hot_words_async(self, request):
        r"""修改热词记录

        该接口用于修改热词记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateHotWords
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateHotWordsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateHotWordsResponse`
        """
        http_info = self._update_hot_words_http_info(request)
        return self._call_api(**http_info)

    def update_hot_words_async_invoker(self, request):
        http_info = self._update_hot_words_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_hot_words_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/digital-human-chat/hot-words/{hot_words_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHotWordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'hot_words_id' in local_var_params:
            path_params['hot_words_id'] = local_var_params['hot_words_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_hot_words_switch_async(self, request):
        r"""修改热词功能开关

        该接口用于修改热词功能开关。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateHotWordsSwitch
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateHotWordsSwitchRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateHotWordsSwitchResponse`
        """
        http_info = self._update_hot_words_switch_http_info(request)
        return self._call_api(**http_info)

    def update_hot_words_switch_async_invoker(self, request):
        http_info = self._update_hot_words_switch_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_hot_words_switch_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/hot-words-switch",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHotWordsSwitchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_instruction_library_async(self, request):
        r"""创建指令集

        该接口用于创建指令集。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInstructionLibrary
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateInstructionLibraryRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateInstructionLibraryResponse`
        """
        http_info = self._create_instruction_library_http_info(request)
        return self._call_api(**http_info)

    def create_instruction_library_async_invoker(self, request):
        http_info = self._create_instruction_library_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_instruction_library_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/wise-brain-manager/instruction-library",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstructionLibraryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_instruction_library_async(self, request):
        r"""删除指令集

        该接口用于删除指令集。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteInstructionLibrary
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteInstructionLibraryRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteInstructionLibraryResponse`
        """
        http_info = self._delete_instruction_library_http_info(request)
        return self._call_api(**http_info)

    def delete_instruction_library_async_invoker(self, request):
        http_info = self._delete_instruction_library_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_instruction_library_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/wise-brain-manager/instruction-library/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstructionLibraryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_instruction_library_async(self, request):
        r"""查询指令集列表

        该接口用于查询指令集列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstructionLibrary
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListInstructionLibraryRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListInstructionLibraryResponse`
        """
        http_info = self._list_instruction_library_http_info(request)
        return self._call_api(**http_info)

    def list_instruction_library_async_invoker(self, request):
        http_info = self._list_instruction_library_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instruction_library_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/wise-brain-manager/instruction-library",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstructionLibraryResponse"
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
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_instruction_library_async(self, request):
        r"""查询指令集详情

        该接口用于查询指令集详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstructionLibrary
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowInstructionLibraryRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowInstructionLibraryResponse`
        """
        http_info = self._show_instruction_library_http_info(request)
        return self._call_api(**http_info)

    def show_instruction_library_async_invoker(self, request):
        http_info = self._show_instruction_library_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_instruction_library_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/wise-brain-manager/instruction-library/{instruction_library_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstructionLibraryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instruction_library_id' in local_var_params:
            path_params['instruction_library_id'] = local_var_params['instruction_library_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_instruction_library_async(self, request):
        r"""修改指令集

        该接口用于修改指令集。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstructionLibrary
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateInstructionLibraryRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateInstructionLibraryResponse`
        """
        http_info = self._update_instruction_library_http_info(request)
        return self._call_api(**http_info)

    def update_instruction_library_async_invoker(self, request):
        http_info = self._update_instruction_library_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_instruction_library_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/wise-brain-manager/instruction-library/{instruction_library_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstructionLibraryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instruction_library_id' in local_var_params:
            path_params['instruction_library_id'] = local_var_params['instruction_library_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_instruction_async(self, request):
        r"""创建指令

        该接口用于创建指令。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInstruction
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateInstructionRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateInstructionResponse`
        """
        http_info = self._create_instruction_http_info(request)
        return self._call_api(**http_info)

    def create_instruction_async_invoker(self, request):
        http_info = self._create_instruction_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_instruction_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/wise-brain-manager/instruction",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstructionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_instruction_async(self, request):
        r"""删除指令

        该接口用于删除指令。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteInstruction
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteInstructionRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteInstructionResponse`
        """
        http_info = self._delete_instruction_http_info(request)
        return self._call_api(**http_info)

    def delete_instruction_async_invoker(self, request):
        http_info = self._delete_instruction_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_instruction_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/wise-brain-manager/instruction/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstructionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_instruction_async(self, request):
        r"""查询指令列表

        该接口用于查询指令列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstruction
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListInstructionRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListInstructionResponse`
        """
        http_info = self._list_instruction_http_info(request)
        return self._call_api(**http_info)

    def list_instruction_async_invoker(self, request):
        http_info = self._list_instruction_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instruction_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/wise-brain-manager/instruction",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstructionResponse"
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
        if 'instruction_library_id' in local_var_params:
            query_params.append(('instruction_library_id', local_var_params['instruction_library_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_instruction_async(self, request):
        r"""查询指令详情

        该接口用于查询指令详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstruction
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowInstructionRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowInstructionResponse`
        """
        http_info = self._show_instruction_http_info(request)
        return self._call_api(**http_info)

    def show_instruction_async_invoker(self, request):
        http_info = self._show_instruction_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_instruction_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/wise-brain-manager/instruction/{instruction_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstructionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instruction_id' in local_var_params:
            path_params['instruction_id'] = local_var_params['instruction_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_instruction_async(self, request):
        r"""修改指令

        该接口用于修改指令。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstruction
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateInstructionRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateInstructionResponse`
        """
        http_info = self._update_instruction_http_info(request)
        return self._call_api(**http_info)

    def update_instruction_async_invoker(self, request):
        http_info = self._update_instruction_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_instruction_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/wise-brain-manager/instruction/{instruction_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstructionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instruction_id' in local_var_params:
            path_params['instruction_id'] = local_var_params['instruction_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_interaction_rule_group_async(self, request):
        r"""创建智能直播间互动规则库

        该接口用于创建智能直播间互动规则库。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInteractionRuleGroup
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateInteractionRuleGroupRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateInteractionRuleGroupResponse`
        """
        http_info = self._create_interaction_rule_group_http_info(request)
        return self._call_api(**http_info)

    def create_interaction_rule_group_async_invoker(self, request):
        http_info = self._create_interaction_rule_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_interaction_rule_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/smart-live-interaction-rule-groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInteractionRuleGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_interaction_rule_group_async(self, request):
        r"""删除智能直播间互动规则库

        该接口用于删除智能直播间互动规则库。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteInteractionRuleGroup
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteInteractionRuleGroupRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteInteractionRuleGroupResponse`
        """
        http_info = self._delete_interaction_rule_group_http_info(request)
        return self._call_api(**http_info)

    def delete_interaction_rule_group_async_invoker(self, request):
        http_info = self._delete_interaction_rule_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_interaction_rule_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/smart-live-interaction-rule-groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInteractionRuleGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_interaction_rule_groups_async(self, request):
        r"""查询智能直播间互动规则库列表

        该接口用于智能直播间互动规则库列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInteractionRuleGroups
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListInteractionRuleGroupsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListInteractionRuleGroupsResponse`
        """
        http_info = self._list_interaction_rule_groups_http_info(request)
        return self._call_api(**http_info)

    def list_interaction_rule_groups_async_invoker(self, request):
        http_info = self._list_interaction_rule_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_interaction_rule_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/smart-live-interaction-rule-groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListInteractionRuleGroupsResponse"
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
        if 'create_since' in local_var_params:
            query_params.append(('create_since', local_var_params['create_since']))
        if 'create_until' in local_var_params:
            query_params.append(('create_until', local_var_params['create_until']))
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_interaction_rule_group_async(self, request):
        r"""更新智能直播间互动规则库

        该接口用于更新智能直播间互动规则库。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInteractionRuleGroup
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateInteractionRuleGroupRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateInteractionRuleGroupResponse`
        """
        http_info = self._update_interaction_rule_group_http_info(request)
        return self._call_api(**http_info)

    def update_interaction_rule_group_async_invoker(self, request):
        http_info = self._update_interaction_rule_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_interaction_rule_group_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/smart-live-interaction-rule-groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInteractionRuleGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_interactive_chat_async(self, request):
        r"""交互助手对话

        该接口用于交互助手对话。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInteractiveChat
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateInteractiveChatRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateInteractiveChatResponse`
        """
        http_info = self._create_interactive_chat_http_info(request)
        return self._call_api(**http_info)

    def create_interactive_chat_async_invoker(self, request):
        http_info = self._create_interactive_chat_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_interactive_chat_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/wise-brain-manager/chat",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInteractiveChatResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_intent_and_question_async(self, request):
        r"""创建知识库意图和问法

        该接口用于创建知识库意图和问法。一个意图包含一个主题，一个答案，若干个问法等。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateIntentAndQuestion
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateIntentAndQuestionRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateIntentAndQuestionResponse`
        """
        http_info = self._create_intent_and_question_http_info(request)
        return self._call_api(**http_info)

    def create_intent_and_question_async_invoker(self, request):
        http_info = self._create_intent_and_question_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_intent_and_question_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/knowledge/intent-question",
            "request_type": request.__class__.__name__,
            "response_type": "CreateIntentAndQuestionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_knowledge_intent_async(self, request):
        r"""创建知识库意图

        该接口用于创建知识库意图。一个意图包含一个主题，一个答案，若干个问法等。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateKnowledgeIntent
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateKnowledgeIntentRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateKnowledgeIntentResponse`
        """
        http_info = self._create_knowledge_intent_http_info(request)
        return self._call_api(**http_info)

    def create_knowledge_intent_async_invoker(self, request):
        http_info = self._create_knowledge_intent_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_knowledge_intent_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/knowledge/intent",
            "request_type": request.__class__.__name__,
            "response_type": "CreateKnowledgeIntentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_knowledge_intent_async(self, request):
        r"""删除知识库意图

        该接口用于删除知识库意图。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteKnowledgeIntent
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteKnowledgeIntentRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteKnowledgeIntentResponse`
        """
        http_info = self._delete_knowledge_intent_http_info(request)
        return self._call_api(**http_info)

    def delete_knowledge_intent_async_invoker(self, request):
        http_info = self._delete_knowledge_intent_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_knowledge_intent_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/knowledge/intent/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteKnowledgeIntentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_knowledge_intent_async(self, request):
        r"""查询知识库意图列表

        该接口用于查询知识库意图列表。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKnowledgeIntent
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListKnowledgeIntentRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListKnowledgeIntentResponse`
        """
        http_info = self._list_knowledge_intent_http_info(request)
        return self._call_api(**http_info)

    def list_knowledge_intent_async_invoker(self, request):
        http_info = self._list_knowledge_intent_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_knowledge_intent_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/knowledge/intent",
            "request_type": request.__class__.__name__,
            "response_type": "ListKnowledgeIntentResponse"
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
        if 'skill_id' in local_var_params:
            query_params.append(('skill_id', local_var_params['skill_id']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_knowledge_intent_async(self, request):
        r"""查询知识库意图详情

        该接口用于查询知识库意图详情。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowKnowledgeIntent
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowKnowledgeIntentRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowKnowledgeIntentResponse`
        """
        http_info = self._show_knowledge_intent_http_info(request)
        return self._call_api(**http_info)

    def show_knowledge_intent_async_invoker(self, request):
        http_info = self._show_knowledge_intent_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_knowledge_intent_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/knowledge/intent/{intent_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowKnowledgeIntentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'intent_id' in local_var_params:
            path_params['intent_id'] = local_var_params['intent_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_knowledge_intent_async(self, request):
        r"""修改知识库意图

        该接口用于修改知识库意图。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateKnowledgeIntent
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateKnowledgeIntentRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateKnowledgeIntentResponse`
        """
        http_info = self._update_knowledge_intent_http_info(request)
        return self._call_api(**http_info)

    def update_knowledge_intent_async_invoker(self, request):
        http_info = self._update_knowledge_intent_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_knowledge_intent_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/digital-human-chat/knowledge/intent/{intent_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateKnowledgeIntentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'intent_id' in local_var_params:
            path_params['intent_id'] = local_var_params['intent_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def check_recall_knowledge_library_async(self, request):
        r"""知识库召回测试

        该接口用于知识库召回测试。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckRecallKnowledgeLibrary
        :type request: :class:`huaweicloudsdkmetastudio.v1.CheckRecallKnowledgeLibraryRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CheckRecallKnowledgeLibraryResponse`
        """
        http_info = self._check_recall_knowledge_library_http_info(request)
        return self._call_api(**http_info)

    def check_recall_knowledge_library_async_invoker(self, request):
        http_info = self._check_recall_knowledge_library_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_recall_knowledge_library_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/wise-brain-manager/knowledge-library/recall",
            "request_type": request.__class__.__name__,
            "response_type": "CheckRecallKnowledgeLibraryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_knowledge_library_async(self, request):
        r"""创建知识库

        该接口用于创建知识库。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateKnowledgeLibrary
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateKnowledgeLibraryRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateKnowledgeLibraryResponse`
        """
        http_info = self._create_knowledge_library_http_info(request)
        return self._call_api(**http_info)

    def create_knowledge_library_async_invoker(self, request):
        http_info = self._create_knowledge_library_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_knowledge_library_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/wise-brain-manager/knowledge-library",
            "request_type": request.__class__.__name__,
            "response_type": "CreateKnowledgeLibraryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_knowledge_library_async(self, request):
        r"""删除知识库

        该接口用于删除知识库。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteKnowledgeLibrary
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteKnowledgeLibraryRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteKnowledgeLibraryResponse`
        """
        http_info = self._delete_knowledge_library_http_info(request)
        return self._call_api(**http_info)

    def delete_knowledge_library_async_invoker(self, request):
        http_info = self._delete_knowledge_library_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_knowledge_library_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/wise-brain-manager/knowledge-library/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteKnowledgeLibraryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_knowledge_library_async(self, request):
        r"""查询知识库列表

        该接口用于查询知识库列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKnowledgeLibrary
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListKnowledgeLibraryRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListKnowledgeLibraryResponse`
        """
        http_info = self._list_knowledge_library_http_info(request)
        return self._call_api(**http_info)

    def list_knowledge_library_async_invoker(self, request):
        http_info = self._list_knowledge_library_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_knowledge_library_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/wise-brain-manager/knowledge-library",
            "request_type": request.__class__.__name__,
            "response_type": "ListKnowledgeLibraryResponse"
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
        if 'language' in local_var_params:
            query_params.append(('language', local_var_params['language']))
        if 'knowledge_type' in local_var_params:
            query_params.append(('knowledge_type', local_var_params['knowledge_type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_knowledge_library_async(self, request):
        r"""查询知识库详情

        该接口用于查询知识库详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowKnowledgeLibrary
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowKnowledgeLibraryRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowKnowledgeLibraryResponse`
        """
        http_info = self._show_knowledge_library_http_info(request)
        return self._call_api(**http_info)

    def show_knowledge_library_async_invoker(self, request):
        http_info = self._show_knowledge_library_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_knowledge_library_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/wise-brain-manager/knowledge-library/{knowledge_library_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowKnowledgeLibraryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'knowledge_library_id' in local_var_params:
            path_params['knowledge_library_id'] = local_var_params['knowledge_library_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_knowledge_library_async(self, request):
        r"""修改知识库

        该接口用于修改知识库。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateKnowledgeLibrary
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateKnowledgeLibraryRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateKnowledgeLibraryResponse`
        """
        http_info = self._update_knowledge_library_http_info(request)
        return self._call_api(**http_info)

    def update_knowledge_library_async_invoker(self, request):
        http_info = self._update_knowledge_library_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_knowledge_library_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/wise-brain-manager/knowledge-library/{knowledge_library_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateKnowledgeLibraryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'knowledge_library_id' in local_var_params:
            path_params['knowledge_library_id'] = local_var_params['knowledge_library_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_batch_knowledge_question_async(self, request):
        r"""批量创建知识库问法

        该接口用于批量创建知识库问法。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateBatchKnowledgeQuestion
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateBatchKnowledgeQuestionRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateBatchKnowledgeQuestionResponse`
        """
        http_info = self._create_batch_knowledge_question_http_info(request)
        return self._call_api(**http_info)

    def create_batch_knowledge_question_async_invoker(self, request):
        http_info = self._create_batch_knowledge_question_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_batch_knowledge_question_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/knowledge/question-batch",
            "request_type": request.__class__.__name__,
            "response_type": "CreateBatchKnowledgeQuestionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_knowledge_question_async(self, request):
        r"""创建知识库问法

        该接口用于创建知识库问法。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateKnowledgeQuestion
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateKnowledgeQuestionRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateKnowledgeQuestionResponse`
        """
        http_info = self._create_knowledge_question_http_info(request)
        return self._call_api(**http_info)

    def create_knowledge_question_async_invoker(self, request):
        http_info = self._create_knowledge_question_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_knowledge_question_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/knowledge/question",
            "request_type": request.__class__.__name__,
            "response_type": "CreateKnowledgeQuestionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_knowledge_question_async(self, request):
        r"""删除知识库问法

        该接口用于删除知识库问法。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteKnowledgeQuestion
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteKnowledgeQuestionRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteKnowledgeQuestionResponse`
        """
        http_info = self._delete_knowledge_question_http_info(request)
        return self._call_api(**http_info)

    def delete_knowledge_question_async_invoker(self, request):
        http_info = self._delete_knowledge_question_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_knowledge_question_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/knowledge/question/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteKnowledgeQuestionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_knowledge_question_async(self, request):
        r"""查询知识库问法列表

        该接口用于查询知识库问法列表。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKnowledgeQuestion
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListKnowledgeQuestionRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListKnowledgeQuestionResponse`
        """
        http_info = self._list_knowledge_question_http_info(request)
        return self._call_api(**http_info)

    def list_knowledge_question_async_invoker(self, request):
        http_info = self._list_knowledge_question_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_knowledge_question_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/knowledge/question",
            "request_type": request.__class__.__name__,
            "response_type": "ListKnowledgeQuestionResponse"
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
        if 'intent_id' in local_var_params:
            query_params.append(('intent_id', local_var_params['intent_id']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_knowledge_question_async(self, request):
        r"""查询知识库问法详情

        该接口用于查询知识库问法详情。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowKnowledgeQuestion
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowKnowledgeQuestionRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowKnowledgeQuestionResponse`
        """
        http_info = self._show_knowledge_question_http_info(request)
        return self._call_api(**http_info)

    def show_knowledge_question_async_invoker(self, request):
        http_info = self._show_knowledge_question_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_knowledge_question_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/knowledge/question/{question_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowKnowledgeQuestionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'question_id' in local_var_params:
            path_params['question_id'] = local_var_params['question_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_batch_knowledge_question_async(self, request):
        r"""批量修改知识库问法

        该接口用于批量修改知识库问法。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateBatchKnowledgeQuestion
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateBatchKnowledgeQuestionRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateBatchKnowledgeQuestionResponse`
        """
        http_info = self._update_batch_knowledge_question_http_info(request)
        return self._call_api(**http_info)

    def update_batch_knowledge_question_async_invoker(self, request):
        http_info = self._update_batch_knowledge_question_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_batch_knowledge_question_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/digital-human-chat/knowledge/question-batch",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateBatchKnowledgeQuestionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_knowledge_question_async(self, request):
        r"""修改知识库问法

        该接口用于修改知识库问法。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateKnowledgeQuestion
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateKnowledgeQuestionRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateKnowledgeQuestionResponse`
        """
        http_info = self._update_knowledge_question_http_info(request)
        return self._call_api(**http_info)

    def update_knowledge_question_async_invoker(self, request):
        http_info = self._update_knowledge_question_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_knowledge_question_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/digital-human-chat/knowledge/question/{question_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateKnowledgeQuestionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'question_id' in local_var_params:
            path_params['question_id'] = local_var_params['question_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_knowledge_skill_async(self, request):
        r"""创建知识库技能

        该接口用于创建知识库技能。一个技能用于特定场景的交互问答，包含若干个意图等。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateKnowledgeSkill
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateKnowledgeSkillRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateKnowledgeSkillResponse`
        """
        http_info = self._create_knowledge_skill_http_info(request)
        return self._call_api(**http_info)

    def create_knowledge_skill_async_invoker(self, request):
        http_info = self._create_knowledge_skill_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_knowledge_skill_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/knowledge/skill",
            "request_type": request.__class__.__name__,
            "response_type": "CreateKnowledgeSkillResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_knowledge_skill_async(self, request):
        r"""删除知识库技能

        该接口用于删除知识库技能。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteKnowledgeSkill
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteKnowledgeSkillRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteKnowledgeSkillResponse`
        """
        http_info = self._delete_knowledge_skill_http_info(request)
        return self._call_api(**http_info)

    def delete_knowledge_skill_async_invoker(self, request):
        http_info = self._delete_knowledge_skill_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_knowledge_skill_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/knowledge/skill/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteKnowledgeSkillResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def export_knowledge_skill_async(self, request):
        r"""导出知识库技能

        该接口用于导出知识库技能。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportKnowledgeSkill
        :type request: :class:`huaweicloudsdkmetastudio.v1.ExportKnowledgeSkillRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ExportKnowledgeSkillResponse`
        """
        http_info = self._export_knowledge_skill_http_info(request)
        return self._call_api(**http_info)

    def export_knowledge_skill_async_invoker(self, request):
        http_info = self._export_knowledge_skill_http_info(request)
        return AsyncInvoker(self, http_info)

    def _export_knowledge_skill_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/knowledge/skill/{skill_id}/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportKnowledgeSkillResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'skill_id' in local_var_params:
            path_params['skill_id'] = local_var_params['skill_id']

        query_params = []
        if 'export_type' in local_var_params:
            query_params.append(('export_type', local_var_params['export_type']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_knowledge_skill_async(self, request):
        r"""查询知识库技能列表

        该接口用于查询知识库技能列表。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKnowledgeSkill
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListKnowledgeSkillRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListKnowledgeSkillResponse`
        """
        http_info = self._list_knowledge_skill_http_info(request)
        return self._call_api(**http_info)

    def list_knowledge_skill_async_invoker(self, request):
        http_info = self._list_knowledge_skill_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_knowledge_skill_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/knowledge/skill",
            "request_type": request.__class__.__name__,
            "response_type": "ListKnowledgeSkillResponse"
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
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_knowledge_skill_async(self, request):
        r"""查询知识库技能详情

        该接口用于查询知识库技能详情。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowKnowledgeSkill
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowKnowledgeSkillRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowKnowledgeSkillResponse`
        """
        http_info = self._show_knowledge_skill_http_info(request)
        return self._call_api(**http_info)

    def show_knowledge_skill_async_invoker(self, request):
        http_info = self._show_knowledge_skill_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_knowledge_skill_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/knowledge/skill/{skill_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowKnowledgeSkillResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'skill_id' in local_var_params:
            path_params['skill_id'] = local_var_params['skill_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_knowledge_skill_async(self, request):
        r"""修改知识库技能

        该接口用于修改知识库技能。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateKnowledgeSkill
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateKnowledgeSkillRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateKnowledgeSkillResponse`
        """
        http_info = self._update_knowledge_skill_http_info(request)
        return self._call_api(**http_info)

    def update_knowledge_skill_async_invoker(self, request):
        http_info = self._update_knowledge_skill_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_knowledge_skill_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/digital-human-chat/knowledge/skill/{skill_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateKnowledgeSkillResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'skill_id' in local_var_params:
            path_params['skill_id'] = local_var_params['skill_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_live_platform_async(self, request):
        r"""创建第三方直播平台

        该接口用于创建第三方直播平台。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateLivePlatform
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateLivePlatformRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateLivePlatformResponse`
        """
        http_info = self._create_live_platform_http_info(request)
        return self._call_api(**http_info)

    def create_live_platform_async_invoker(self, request):
        http_info = self._create_live_platform_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_live_platform_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/live-platforms/platforms",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLivePlatformResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_live_platform_async(self, request):
        r"""删除第三方直播平台信息

        该接口用于删除第三方直播平台信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteLivePlatform
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteLivePlatformRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteLivePlatformResponse`
        """
        http_info = self._delete_live_platform_http_info(request)
        return self._call_api(**http_info)

    def delete_live_platform_async_invoker(self, request):
        http_info = self._delete_live_platform_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_live_platform_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/live-platforms/platforms/{platform_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLivePlatformResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'platform_id' in local_var_params:
            path_params['platform_id'] = local_var_params['platform_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_live_platform_products_async(self, request):
        r"""查询第三方直播平台商品列表

        该接口用于查询第三方直播平台商品列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLivePlatformProducts
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListLivePlatformProductsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListLivePlatformProductsResponse`
        """
        http_info = self._list_live_platform_products_http_info(request)
        return self._call_api(**http_info)

    def list_live_platform_products_async_invoker(self, request):
        http_info = self._list_live_platform_products_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_live_platform_products_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/live-platforms/products",
            "request_type": request.__class__.__name__,
            "response_type": "ListLivePlatformProductsResponse"
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
        if 'platform_id' in local_var_params:
            query_params.append(('platform_id', local_var_params['platform_id']))
        if 'live_id' in local_var_params:
            query_params.append(('live_id', local_var_params['live_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_live_platforms_async(self, request):
        r"""查询直播平台列表

        该接口用于查询直播平台列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLivePlatforms
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListLivePlatformsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListLivePlatformsResponse`
        """
        http_info = self._list_live_platforms_http_info(request)
        return self._call_api(**http_info)

    def list_live_platforms_async_invoker(self, request):
        http_info = self._list_live_platforms_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_live_platforms_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/live-platforms/platforms",
            "request_type": request.__class__.__name__,
            "response_type": "ListLivePlatformsResponse"
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
        if 'access_type' in local_var_params:
            query_params.append(('access_type', local_var_params['access_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_live_platform_async(self, request):
        r"""查询第三方直播平台信息

        该接口用于查询第三方直播平台信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowLivePlatform
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowLivePlatformRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowLivePlatformResponse`
        """
        http_info = self._show_live_platform_http_info(request)
        return self._call_api(**http_info)

    def show_live_platform_async_invoker(self, request):
        http_info = self._show_live_platform_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_live_platform_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/live-platforms/platforms/{platform_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLivePlatformResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'platform_id' in local_var_params:
            path_params['platform_id'] = local_var_params['platform_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_live_platform_async(self, request):
        r"""更新第三方直播平台信息

        该接口用于更新第三方直播平台信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateLivePlatform
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateLivePlatformRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateLivePlatformResponse`
        """
        http_info = self._update_live_platform_http_info(request)
        return self._call_api(**http_info)

    def update_live_platform_async_invoker(self, request):
        http_info = self._update_live_platform_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_live_platform_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/live-platforms/platforms/{platform_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLivePlatformResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'platform_id' in local_var_params:
            path_params['platform_id'] = local_var_params['platform_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_llm_config_async(self, request):
        r"""创建大语言模型配置

        该接口用于创建大语言模型配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateLlmConfig
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateLlmConfigRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateLlmConfigResponse`
        """
        http_info = self._create_llm_config_http_info(request)
        return self._call_api(**http_info)

    def create_llm_config_async_invoker(self, request):
        http_info = self._create_llm_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_llm_config_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/wise-brain-manager/llm-config",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLlmConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_llm_config_async(self, request):
        r"""删除大语言模型配置

        该接口用于删除大语言模型配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteLlmConfig
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteLlmConfigRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteLlmConfigResponse`
        """
        http_info = self._delete_llm_config_http_info(request)
        return self._call_api(**http_info)

    def delete_llm_config_async_invoker(self, request):
        http_info = self._delete_llm_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_llm_config_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/wise-brain-manager/llm-config/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLlmConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_llm_config_async(self, request):
        r"""查询大语言模型配置列表

        该接口用于查询大语言模型配置列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLlmConfig
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListLlmConfigRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListLlmConfigResponse`
        """
        http_info = self._list_llm_config_http_info(request)
        return self._call_api(**http_info)

    def list_llm_config_async_invoker(self, request):
        http_info = self._list_llm_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_llm_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/wise-brain-manager/llm-config",
            "request_type": request.__class__.__name__,
            "response_type": "ListLlmConfigResponse"
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
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_llm_config_async(self, request):
        r"""查询大语言模型配置详情

        该接口用于查询大语言模型配置详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowLlmConfig
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowLlmConfigRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowLlmConfigResponse`
        """
        http_info = self._show_llm_config_http_info(request)
        return self._call_api(**http_info)

    def show_llm_config_async_invoker(self, request):
        http_info = self._show_llm_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_llm_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/wise-brain-manager/llm-config/{llm_config_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLlmConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'llm_config_id' in local_var_params:
            path_params['llm_config_id'] = local_var_params['llm_config_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_llm_config_async(self, request):
        r"""修改大语言模型配置

        该接口用于修改大语言模型配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateLlmConfig
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateLlmConfigRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateLlmConfigResponse`
        """
        http_info = self._update_llm_config_http_info(request)
        return self._call_api(**http_info)

    def update_llm_config_async_invoker(self, request):
        http_info = self._update_llm_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_llm_config_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/wise-brain-manager/llm-config/{llm_config_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLlmConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'llm_config_id' in local_var_params:
            path_params['llm_config_id'] = local_var_params['llm_config_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_mcp_server_async(self, request):
        r"""创建MCP服务端对接配置

        该接口用于创建MCP服务端对接配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMcpServer
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateMcpServerRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateMcpServerResponse`
        """
        http_info = self._create_mcp_server_http_info(request)
        return self._call_api(**http_info)

    def create_mcp_server_async_invoker(self, request):
        http_info = self._create_mcp_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_mcp_server_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/wise-brain-manager/mcp-server",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMcpServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_mcp_server_async(self, request):
        r"""删除MCP服务端对接配置

        该接口用于删除MCP服务端对接配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteMcpServer
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteMcpServerRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteMcpServerResponse`
        """
        http_info = self._delete_mcp_server_http_info(request)
        return self._call_api(**http_info)

    def delete_mcp_server_async_invoker(self, request):
        http_info = self._delete_mcp_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_mcp_server_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/wise-brain-manager/mcp-server/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMcpServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_mcp_server_async(self, request):
        r"""查询MCP服务端对接配置列表

        该接口用于查询MCP服务端对接配置列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMcpServer
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListMcpServerRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListMcpServerResponse`
        """
        http_info = self._list_mcp_server_http_info(request)
        return self._call_api(**http_info)

    def list_mcp_server_async_invoker(self, request):
        http_info = self._list_mcp_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_mcp_server_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/wise-brain-manager/mcp-server",
            "request_type": request.__class__.__name__,
            "response_type": "ListMcpServerResponse"
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
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_mcp_server_async(self, request):
        r"""查询MCP服务端对接配置详情

        该接口用于查询MCP服务端对接配置详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMcpServer
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowMcpServerRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowMcpServerResponse`
        """
        http_info = self._show_mcp_server_http_info(request)
        return self._call_api(**http_info)

    def show_mcp_server_async_invoker(self, request):
        http_info = self._show_mcp_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_mcp_server_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/wise-brain-manager/mcp-server/{mcp_server_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMcpServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'mcp_server_id' in local_var_params:
            path_params['mcp_server_id'] = local_var_params['mcp_server_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_mcp_server_async(self, request):
        r"""修改MCP服务端对接配置

        该接口用于修改MCP服务端对接配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMcpServer
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateMcpServerRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateMcpServerResponse`
        """
        http_info = self._update_mcp_server_http_info(request)
        return self._call_api(**http_info)

    def update_mcp_server_async_invoker(self, request):
        http_info = self._update_mcp_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_mcp_server_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/wise-brain-manager/mcp-server/{mcp_server_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMcpServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'mcp_server_id' in local_var_params:
            path_params['mcp_server_id'] = local_var_params['mcp_server_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_once_code_async(self, request):
        r"""创建一次性鉴权码

        该接口用于创建一次性鉴权码，有效期5分钟，鉴权码只能使用一次，每次使用后需要重新获取。
        &gt; 接口只能通过第三方后台调用，不能在浏览器前台直接调用，否则会有跨域问题。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateOnceCode
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateOnceCodeRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateOnceCodeResponse`
        """
        http_info = self._create_once_code_http_info(request)
        return self._call_api(**http_info)

    def create_once_code_async_invoker(self, request):
        http_info = self._create_once_code_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_once_code_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/once-code",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOnceCodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_meta_studio_orders_async(self, request):
        r"""订购metastudio云服务产品

        该接口用于订购MetaStudio服务的包周期,一次性,按需套餐包产品
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMetaStudioOrders
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateMetaStudioOrdersRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateMetaStudioOrdersResponse`
        """
        http_info = self._create_meta_studio_orders_http_info(request)
        return self._call_api(**http_info)

    def create_meta_studio_orders_async_invoker(self, request):
        http_info = self._create_meta_studio_orders_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_meta_studio_orders_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/mss/public/orders",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMetaStudioOrdersResponse"
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

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_pacify_words_async(self, request):
        r"""批量删除安抚话术

        该接口用于批量删除安抚话术。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeletePacifyWords
        :type request: :class:`huaweicloudsdkmetastudio.v1.BatchDeletePacifyWordsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.BatchDeletePacifyWordsResponse`
        """
        http_info = self._batch_delete_pacify_words_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_pacify_words_async_invoker(self, request):
        http_info = self._batch_delete_pacify_words_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_pacify_words_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/pacify-words/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeletePacifyWordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_pacify_words_async(self, request):
        r"""创建安抚话术

        该接口用于创建安抚话术。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePacifyWords
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreatePacifyWordsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreatePacifyWordsResponse`
        """
        http_info = self._create_pacify_words_http_info(request)
        return self._call_api(**http_info)

    def create_pacify_words_async_invoker(self, request):
        http_info = self._create_pacify_words_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_pacify_words_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/pacify-words",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePacifyWordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_pacify_words_async(self, request):
        r"""删除安抚话术

        该接口用于删除安抚话术。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePacifyWords
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeletePacifyWordsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeletePacifyWordsResponse`
        """
        http_info = self._delete_pacify_words_http_info(request)
        return self._call_api(**http_info)

    def delete_pacify_words_async_invoker(self, request):
        http_info = self._delete_pacify_words_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_pacify_words_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/digital-human-chat/pacify-words/{pacify_words_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePacifyWordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pacify_words_id' in local_var_params:
            path_params['pacify_words_id'] = local_var_params['pacify_words_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_pacify_words_async(self, request):
        r"""查询安抚话术列表

        该接口用于查询安抚话术列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPacifyWords
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListPacifyWordsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListPacifyWordsResponse`
        """
        http_info = self._list_pacify_words_http_info(request)
        return self._call_api(**http_info)

    def list_pacify_words_async_invoker(self, request):
        http_info = self._list_pacify_words_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_pacify_words_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/pacify-words",
            "request_type": request.__class__.__name__,
            "response_type": "ListPacifyWordsResponse"
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
        if 'robot_id' in local_var_params:
            query_params.append(('robot_id', local_var_params['robot_id']))
        if 'language' in local_var_params:
            query_params.append(('language', local_var_params['language']))
        if 'pacify_words_type' in local_var_params:
            query_params.append(('pacify_words_type', local_var_params['pacify_words_type']))
        if 'intent' in local_var_params:
            query_params.append(('intent', local_var_params['intent']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_pacify_words_async(self, request):
        r"""查询安抚话术详情

        该接口用于查询安抚话术详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPacifyWords
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowPacifyWordsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowPacifyWordsResponse`
        """
        http_info = self._show_pacify_words_http_info(request)
        return self._call_api(**http_info)

    def show_pacify_words_async_invoker(self, request):
        http_info = self._show_pacify_words_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_pacify_words_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/pacify-words/{pacify_words_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPacifyWordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pacify_words_id' in local_var_params:
            path_params['pacify_words_id'] = local_var_params['pacify_words_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_pacify_words_intent_async(self, request):
        r"""查询安抚话术意图

        该接口用于查询安抚话术意图。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPacifyWordsIntent
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowPacifyWordsIntentRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowPacifyWordsIntentResponse`
        """
        http_info = self._show_pacify_words_intent_http_info(request)
        return self._call_api(**http_info)

    def show_pacify_words_intent_async_invoker(self, request):
        http_info = self._show_pacify_words_intent_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_pacify_words_intent_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/pacify-words-intent",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPacifyWordsIntentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'robot_id' in local_var_params:
            query_params.append(('robot_id', local_var_params['robot_id']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_pacify_words_switch_async(self, request):
        r"""查询安抚话术功能开关

        该接口用于查询安抚话术功能开关。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPacifyWordsSwitch
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowPacifyWordsSwitchRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowPacifyWordsSwitchResponse`
        """
        http_info = self._show_pacify_words_switch_http_info(request)
        return self._call_api(**http_info)

    def show_pacify_words_switch_async_invoker(self, request):
        http_info = self._show_pacify_words_switch_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_pacify_words_switch_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/pacify-words-switch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPacifyWordsSwitchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'robot_id' in local_var_params:
            query_params.append(('robot_id', local_var_params['robot_id']))
        if 'language' in local_var_params:
            query_params.append(('language', local_var_params['language']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_pacify_words_trigger_time_async(self, request):
        r"""查询安抚话术等待触发时长

        该接口用于查询等待触发时长。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPacifyWordsTriggerTime
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowPacifyWordsTriggerTimeRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowPacifyWordsTriggerTimeResponse`
        """
        http_info = self._show_pacify_words_trigger_time_http_info(request)
        return self._call_api(**http_info)

    def show_pacify_words_trigger_time_async_invoker(self, request):
        http_info = self._show_pacify_words_trigger_time_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_pacify_words_trigger_time_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/pacify-words-time",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPacifyWordsTriggerTimeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'robot_id' in local_var_params:
            query_params.append(('robot_id', local_var_params['robot_id']))
        if 'language' in local_var_params:
            query_params.append(('language', local_var_params['language']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_pacify_words_async(self, request):
        r"""修改安抚话术

        该接口用于修改安抚话术。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePacifyWords
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdatePacifyWordsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdatePacifyWordsResponse`
        """
        http_info = self._update_pacify_words_http_info(request)
        return self._call_api(**http_info)

    def update_pacify_words_async_invoker(self, request):
        http_info = self._update_pacify_words_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_pacify_words_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/digital-human-chat/pacify-words/{pacify_words_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePacifyWordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pacify_words_id' in local_var_params:
            path_params['pacify_words_id'] = local_var_params['pacify_words_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_pacify_words_switch_async(self, request):
        r"""修改安抚话术功能开关

        该接口用于修改安抚话术功能开关。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePacifyWordsSwitch
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdatePacifyWordsSwitchRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdatePacifyWordsSwitchResponse`
        """
        http_info = self._update_pacify_words_switch_http_info(request)
        return self._call_api(**http_info)

    def update_pacify_words_switch_async_invoker(self, request):
        http_info = self._update_pacify_words_switch_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_pacify_words_switch_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/digital-human-chat/pacify-words-switch",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePacifyWordsSwitchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_pacify_words_trigger_time_async(self, request):
        r"""修改安抚话术等待触发时长

        该接口用于修改安抚话术等待触发时长。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePacifyWordsTriggerTime
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdatePacifyWordsTriggerTimeRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdatePacifyWordsTriggerTimeResponse`
        """
        http_info = self._update_pacify_words_trigger_time_http_info(request)
        return self._call_api(**http_info)

    def update_pacify_words_trigger_time_async_invoker(self, request):
        http_info = self._update_pacify_words_trigger_time_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_pacify_words_trigger_time_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/digital-human-chat/pacify-words-time",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePacifyWordsTriggerTimeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_picture_modeling_by_url_job_async(self, request):
        r"""基于图片URL创建照片建模任务

        该接口用于从URL中获取图片进行照片建模任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePictureModelingByUrlJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreatePictureModelingByUrlJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreatePictureModelingByUrlJobResponse`
        """
        http_info = self._create_picture_modeling_by_url_job_http_info(request)
        return self._call_api(**http_info)

    def create_picture_modeling_by_url_job_async_invoker(self, request):
        http_info = self._create_picture_modeling_by_url_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_picture_modeling_by_url_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human/stylized/picture-modelings-by-url",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePictureModelingByUrlJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_picture_modeling_job_async(self, request):
        r"""创建照片建模任务

        该接口用于创建风格化照片建模任务。通过上传照片，生成风格化数字人模型。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePictureModelingJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreatePictureModelingJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreatePictureModelingJobResponse`
        """
        http_info = self._create_picture_modeling_job_http_info(request)
        return self._call_api(**http_info)

    def create_picture_modeling_job_async_invoker(self, request):
        http_info = self._create_picture_modeling_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_picture_modeling_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human/stylized/picture-modelings",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePictureModelingJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']
        if 'style_id' in local_var_params:
            form_params['style_id'] = local_var_params['style_id']
        if 'name' in local_var_params:
            form_params['name'] = local_var_params['name']
        if 'notify_url' in local_var_params:
            form_params['notify_url'] = local_var_params['notify_url']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def list_picture_modeling_jobs_async(self, request):
        r"""照片建模任务列表查询

        该接口用于查询风格化照片建模任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPictureModelingJobs
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListPictureModelingJobsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListPictureModelingJobsResponse`
        """
        http_info = self._list_picture_modeling_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_picture_modeling_jobs_async_invoker(self, request):
        http_info = self._list_picture_modeling_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_picture_modeling_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human/stylized/picture-modelings",
            "request_type": request.__class__.__name__,
            "response_type": "ListPictureModelingJobsResponse"
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
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'create_until' in local_var_params:
            query_params.append(('create_until', local_var_params['create_until']))
        if 'create_since' in local_var_params:
            query_params.append(('create_since', local_var_params['create_since']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_picture_modeling_job_async(self, request):
        r"""照片建模任务详情查询

        该接口用于风格化查询照片建模任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPictureModelingJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowPictureModelingJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowPictureModelingJobResponse`
        """
        http_info = self._show_picture_modeling_job_http_info(request)
        return self._call_api(**http_info)

    def show_picture_modeling_job_async_invoker(self, request):
        http_info = self._show_picture_modeling_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_picture_modeling_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human/stylized/picture-modelings/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPictureModelingJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_plugin_config_async(self, request):
        r"""创建插件配置

        该接口用于创建插件配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePluginConfig
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreatePluginConfigRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreatePluginConfigResponse`
        """
        http_info = self._create_plugin_config_http_info(request)
        return self._call_api(**http_info)

    def create_plugin_config_async_invoker(self, request):
        http_info = self._create_plugin_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_plugin_config_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/wise-brain-manager/plugin-config",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePluginConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_plugin_config_async(self, request):
        r"""删除插件配置

        该接口用于删除插件配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePluginConfig
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeletePluginConfigRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeletePluginConfigResponse`
        """
        http_info = self._delete_plugin_config_http_info(request)
        return self._call_api(**http_info)

    def delete_plugin_config_async_invoker(self, request):
        http_info = self._delete_plugin_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_plugin_config_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/wise-brain-manager/plugin-config/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePluginConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_plugin_config_async(self, request):
        r"""查询插件配置列表

        该接口用于查询插件配置列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPluginConfig
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListPluginConfigRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListPluginConfigResponse`
        """
        http_info = self._list_plugin_config_http_info(request)
        return self._call_api(**http_info)

    def list_plugin_config_async_invoker(self, request):
        http_info = self._list_plugin_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_plugin_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/wise-brain-manager/plugin-config",
            "request_type": request.__class__.__name__,
            "response_type": "ListPluginConfigResponse"
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
        if 'plugin_provider' in local_var_params:
            query_params.append(('plugin_provider', local_var_params['plugin_provider']))
        if 'plugin_type' in local_var_params:
            query_params.append(('plugin_type', local_var_params['plugin_type']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_plugin_config_async(self, request):
        r"""查询插件配置详情

        该接口用于查询插件配置详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPluginConfig
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowPluginConfigRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowPluginConfigResponse`
        """
        http_info = self._show_plugin_config_http_info(request)
        return self._call_api(**http_info)

    def show_plugin_config_async_invoker(self, request):
        http_info = self._show_plugin_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_plugin_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/wise-brain-manager/plugin-config/{plugin_config_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPluginConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'plugin_config_id' in local_var_params:
            path_params['plugin_config_id'] = local_var_params['plugin_config_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_plugin_config_default_info_async(self, request):
        r"""查询插件配置默认信息

        该接口用于查询插件配置默认信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPluginConfigDefaultInfo
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowPluginConfigDefaultInfoRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowPluginConfigDefaultInfoResponse`
        """
        http_info = self._show_plugin_config_default_info_http_info(request)
        return self._call_api(**http_info)

    def show_plugin_config_default_info_async_invoker(self, request):
        http_info = self._show_plugin_config_default_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_plugin_config_default_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/wise-brain-manager/plugin-config-default",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPluginConfigDefaultInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_plugin_config_async(self, request):
        r"""修改插件配置

        该接口用于修改插件配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePluginConfig
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdatePluginConfigRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdatePluginConfigResponse`
        """
        http_info = self._update_plugin_config_http_info(request)
        return self._call_api(**http_info)

    def update_plugin_config_async_invoker(self, request):
        http_info = self._update_plugin_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_plugin_config_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/wise-brain-manager/plugin-config/{plugin_config_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePluginConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'plugin_config_id' in local_var_params:
            path_params['plugin_config_id'] = local_var_params['plugin_config_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_product_async(self, request):
        r"""创建商品

        Create product
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateProduct
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateProductRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateProductResponse`
        """
        http_info = self._create_product_http_info(request)
        return self._call_api(**http_info)

    def create_product_async_invoker(self, request):
        http_info = self._create_product_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_product_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/products",
            "request_type": request.__class__.__name__,
            "response_type": "CreateProductResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_product_async(self, request):
        r"""删除商品

        删除商品
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteProduct
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteProductRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteProductResponse`
        """
        http_info = self._delete_product_http_info(request)
        return self._call_api(**http_info)

    def delete_product_async_invoker(self, request):
        http_info = self._delete_product_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_product_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/products/{product_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteProductResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'product_id' in local_var_params:
            path_params['product_id'] = local_var_params['product_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_products_async(self, request):
        r"""查询商品列表

        查询商品列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProducts
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListProductsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListProductsResponse`
        """
        http_info = self._list_products_http_info(request)
        return self._call_api(**http_info)

    def list_products_async_invoker(self, request):
        http_info = self._list_products_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_products_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/products",
            "request_type": request.__class__.__name__,
            "response_type": "ListProductsResponse"
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
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'create_until' in local_var_params:
            query_params.append(('create_until', local_var_params['create_until']))
        if 'create_since' in local_var_params:
            query_params.append(('create_since', local_var_params['create_since']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def set_product_asset_async(self, request):
        r"""商品资产组合配置

        商品资产组合配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetProductAsset
        :type request: :class:`huaweicloudsdkmetastudio.v1.SetProductAssetRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.SetProductAssetResponse`
        """
        http_info = self._set_product_asset_http_info(request)
        return self._call_api(**http_info)

    def set_product_asset_async_invoker(self, request):
        http_info = self._set_product_asset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _set_product_asset_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/products/{product_id}/assets",
            "request_type": request.__class__.__name__,
            "response_type": "SetProductAssetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'product_id' in local_var_params:
            path_params['product_id'] = local_var_params['product_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_product_async(self, request):
        r"""查询商品详情

        Show product
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProduct
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowProductRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowProductResponse`
        """
        http_info = self._show_product_http_info(request)
        return self._call_api(**http_info)

    def show_product_async_invoker(self, request):
        http_info = self._show_product_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_product_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/products/{product_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProductResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'product_id' in local_var_params:
            path_params['product_id'] = local_var_params['product_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_product_async(self, request):
        r"""更新商品

        Update product
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateProduct
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateProductRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateProductResponse`
        """
        http_info = self._update_product_http_info(request)
        return self._call_api(**http_info)

    def update_product_async_invoker(self, request):
        http_info = self._update_product_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_product_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/products/{product_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProductResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'product_id' in local_var_params:
            path_params['product_id'] = local_var_params['product_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_question_answer_async(self, request):
        r"""创建问答对

        该接口用于创建问答对。一个问答对包含一个标准问题，一个答案，若干个相似问题等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateQuestionAnswer
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateQuestionAnswerRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateQuestionAnswerResponse`
        """
        http_info = self._create_question_answer_http_info(request)
        return self._call_api(**http_info)

    def create_question_answer_async_invoker(self, request):
        http_info = self._create_question_answer_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_question_answer_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/wise-brain-manager/question-answer",
            "request_type": request.__class__.__name__,
            "response_type": "CreateQuestionAnswerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_question_answer_async(self, request):
        r"""删除问答对

        该接口用于删除问答对。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteQuestionAnswer
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteQuestionAnswerRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteQuestionAnswerResponse`
        """
        http_info = self._delete_question_answer_http_info(request)
        return self._call_api(**http_info)

    def delete_question_answer_async_invoker(self, request):
        http_info = self._delete_question_answer_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_question_answer_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/wise-brain-manager/question-answer/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteQuestionAnswerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_question_answer_async(self, request):
        r"""查询问答对列表

        该接口用于查询问答对列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListQuestionAnswer
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListQuestionAnswerRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListQuestionAnswerResponse`
        """
        http_info = self._list_question_answer_http_info(request)
        return self._call_api(**http_info)

    def list_question_answer_async_invoker(self, request):
        http_info = self._list_question_answer_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_question_answer_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/wise-brain-manager/question-answer",
            "request_type": request.__class__.__name__,
            "response_type": "ListQuestionAnswerResponse"
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
        if 'knowledge_library_id' in local_var_params:
            query_params.append(('knowledge_library_id', local_var_params['knowledge_library_id']))
        if 'question' in local_var_params:
            query_params.append(('question', local_var_params['question']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_question_answer_async(self, request):
        r"""查询问答对详情

        该接口用于查询问答对详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowQuestionAnswer
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowQuestionAnswerRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowQuestionAnswerResponse`
        """
        http_info = self._show_question_answer_http_info(request)
        return self._call_api(**http_info)

    def show_question_answer_async_invoker(self, request):
        http_info = self._show_question_answer_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_question_answer_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/wise-brain-manager/question-answer/{question_answer_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowQuestionAnswerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'question_answer_id' in local_var_params:
            path_params['question_answer_id'] = local_var_params['question_answer_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_question_answer_async(self, request):
        r"""修改问答对

        该接口用于修改问答对。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateQuestionAnswer
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateQuestionAnswerRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateQuestionAnswerResponse`
        """
        http_info = self._update_question_answer_http_info(request)
        return self._call_api(**http_info)

    def update_question_answer_async_invoker(self, request):
        http_info = self._update_question_answer_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_question_answer_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/wise-brain-manager/question-answer/{question_answer_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateQuestionAnswerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'question_answer_id' in local_var_params:
            path_params['question_answer_id'] = local_var_params['question_answer_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_robot_async(self, request):
        r"""创建应用

        该接口用于创建应用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRobot
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateRobotRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateRobotResponse`
        """
        http_info = self._create_robot_http_info(request)
        return self._call_api(**http_info)

    def create_robot_async_invoker(self, request):
        http_info = self._create_robot_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_robot_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/robot",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRobotResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_robot_async(self, request):
        r"""删除应用

        该接口用于删除应用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRobot
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteRobotRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteRobotResponse`
        """
        http_info = self._delete_robot_http_info(request)
        return self._call_api(**http_info)

    def delete_robot_async_invoker(self, request):
        http_info = self._delete_robot_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_robot_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/robot/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRobotResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_robot_async(self, request):
        r"""查询应用列表

        该接口用于查询应用列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRobot
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListRobotRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListRobotResponse`
        """
        http_info = self._list_robot_http_info(request)
        return self._call_api(**http_info)

    def list_robot_async_invoker(self, request):
        http_info = self._list_robot_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_robot_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/robot",
            "request_type": request.__class__.__name__,
            "response_type": "ListRobotResponse"
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
        if 'room_id' in local_var_params:
            query_params.append(('room_id', local_var_params['room_id']))
        if 'robot_type' in local_var_params:
            query_params.append(('robot_type', local_var_params['robot_type']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_robot_async(self, request):
        r"""查询应用详情

        该接口用于查询应用详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRobot
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowRobotRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowRobotResponse`
        """
        http_info = self._show_robot_http_info(request)
        return self._call_api(**http_info)

    def show_robot_async_invoker(self, request):
        http_info = self._show_robot_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_robot_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/robot/{robot_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRobotResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'robot_id' in local_var_params:
            path_params['robot_id'] = local_var_params['robot_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_robot_async(self, request):
        r"""修改应用

        该接口用于修改应用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRobot
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateRobotRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateRobotResponse`
        """
        http_info = self._update_robot_http_info(request)
        return self._call_api(**http_info)

    def update_robot_async_invoker(self, request):
        http_info = self._update_robot_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_robot_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/digital-human-chat/robot/{robot_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRobotResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'robot_id' in local_var_params:
            path_params['robot_id'] = local_var_params['robot_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def validate_robot_async(self, request):
        r"""校验应用

        该接口用于校验应用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ValidateRobot
        :type request: :class:`huaweicloudsdkmetastudio.v1.ValidateRobotRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ValidateRobotResponse`
        """
        http_info = self._validate_robot_http_info(request)
        return self._call_api(**http_info)

    def validate_robot_async_invoker(self, request):
        http_info = self._validate_robot_http_info(request)
        return AsyncInvoker(self, http_info)

    def _validate_robot_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/robot/validate",
            "request_type": request.__class__.__name__,
            "response_type": "ValidateRobotResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_role_async(self, request):
        r"""创建角色

        该接口用于创建角色。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRole
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateRoleRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateRoleResponse`
        """
        http_info = self._create_role_http_info(request)
        return self._call_api(**http_info)

    def create_role_async_invoker(self, request):
        http_info = self._create_role_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_role_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/wise-brain-manager/role",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRoleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_role_async(self, request):
        r"""删除角色

        该接口用于删除角色。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRole
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteRoleRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteRoleResponse`
        """
        http_info = self._delete_role_http_info(request)
        return self._call_api(**http_info)

    def delete_role_async_invoker(self, request):
        http_info = self._delete_role_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_role_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/wise-brain-manager/role/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRoleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_role_async(self, request):
        r"""查询角色列表

        该接口用于查询角色列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRole
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListRoleRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListRoleResponse`
        """
        http_info = self._list_role_http_info(request)
        return self._call_api(**http_info)

    def list_role_async_invoker(self, request):
        http_info = self._list_role_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_role_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/wise-brain-manager/role",
            "request_type": request.__class__.__name__,
            "response_type": "ListRoleResponse"
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
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_role_async(self, request):
        r"""查询角色详情

        该接口用于查询角色详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRole
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowRoleRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowRoleResponse`
        """
        http_info = self._show_role_http_info(request)
        return self._call_api(**http_info)

    def show_role_async_invoker(self, request):
        http_info = self._show_role_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_role_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/wise-brain-manager/role/{role_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRoleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_role_async(self, request):
        r"""修改角色

        该接口用于修改角色。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRole
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateRoleRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateRoleResponse`
        """
        http_info = self._update_role_http_info(request)
        return self._call_api(**http_info)

    def update_role_async_invoker(self, request):
        http_info = self._update_role_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_role_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/wise-brain-manager/role/{role_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRoleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_smart_chat_room_async(self, request):
        r"""创建智能交互对话

        该接口用于创建智能交互对话。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSmartChatRoom
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateSmartChatRoomRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateSmartChatRoomResponse`
        """
        http_info = self._create_smart_chat_room_http_info(request)
        return self._call_api(**http_info)

    def create_smart_chat_room_async_invoker(self, request):
        http_info = self._create_smart_chat_room_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_smart_chat_room_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/smart-chat-rooms",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSmartChatRoomResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_smart_chat_room_async(self, request):
        r"""删除智能交互对话

        该接口用于删除智能交互对话。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSmartChatRoom
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteSmartChatRoomRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteSmartChatRoomResponse`
        """
        http_info = self._delete_smart_chat_room_http_info(request)
        return self._call_api(**http_info)

    def delete_smart_chat_room_async_invoker(self, request):
        http_info = self._delete_smart_chat_room_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_smart_chat_room_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/smart-chat-rooms/{room_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSmartChatRoomResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_smart_chat_rooms_async(self, request):
        r"""查询智能交互对话列表

        该接口用于智能交互对话列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSmartChatRooms
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListSmartChatRoomsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListSmartChatRoomsResponse`
        """
        http_info = self._list_smart_chat_rooms_http_info(request)
        return self._call_api(**http_info)

    def list_smart_chat_rooms_async_invoker(self, request):
        http_info = self._list_smart_chat_rooms_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_smart_chat_rooms_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/smart-chat-rooms",
            "request_type": request.__class__.__name__,
            "response_type": "ListSmartChatRoomsResponse"
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
        if 'room_name' in local_var_params:
            query_params.append(('room_name', local_var_params['room_name']))
        if 'model_name' in local_var_params:
            query_params.append(('model_name', local_var_params['model_name']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_smart_chat_room_async(self, request):
        r"""查询智能交互对话详情

        该接口用于查询智能交互对话详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSmartChatRoom
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowSmartChatRoomRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowSmartChatRoomResponse`
        """
        http_info = self._show_smart_chat_room_http_info(request)
        return self._call_api(**http_info)

    def show_smart_chat_room_async_invoker(self, request):
        http_info = self._show_smart_chat_room_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_smart_chat_room_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/smart-chat-rooms/{room_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSmartChatRoomResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_smart_chat_room_async(self, request):
        r"""更新智能交互对话信息

        该接口用于智能交互对话信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSmartChatRoom
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateSmartChatRoomRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateSmartChatRoomResponse`
        """
        http_info = self._update_smart_chat_room_http_info(request)
        return self._call_api(**http_info)

    def update_smart_chat_room_async_invoker(self, request):
        http_info = self._update_smart_chat_room_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_smart_chat_room_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/smart-chat-rooms/{room_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSmartChatRoomResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_confirm_live_commands_async(self, request):
        r"""批量确认命令

        该接口用于批量确认命令列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchConfirmLiveCommands
        :type request: :class:`huaweicloudsdkmetastudio.v1.BatchConfirmLiveCommandsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.BatchConfirmLiveCommandsResponse`
        """
        http_info = self._batch_confirm_live_commands_http_info(request)
        return self._call_api(**http_info)

    def batch_confirm_live_commands_async_invoker(self, request):
        http_info = self._batch_confirm_live_commands_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_confirm_live_commands_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/smart-live-rooms/{room_id}/smart-live-jobs/{job_id}/batch-commands-confirm",
            "request_type": request.__class__.__name__,
            "response_type": "BatchConfirmLiveCommandsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def execute_smart_live_command_async(self, request):
        r"""控制数字人直播过程

        该接口用于控制数字人直播过程。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteSmartLiveCommand
        :type request: :class:`huaweicloudsdkmetastudio.v1.ExecuteSmartLiveCommandRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ExecuteSmartLiveCommandResponse`
        """
        http_info = self._execute_smart_live_command_http_info(request)
        return self._call_api(**http_info)

    def execute_smart_live_command_async_invoker(self, request):
        http_info = self._execute_smart_live_command_http_info(request)
        return AsyncInvoker(self, http_info)

    def _execute_smart_live_command_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/smart-live-rooms/{room_id}/smart-live-jobs/{job_id}/command",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteSmartLiveCommandResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_smart_live_async(self, request):
        r"""查询某个智能直播间下直播任务列表

        该接口用于查询某个智能直播间的直播任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSmartLive
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListSmartLiveRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListSmartLiveResponse`
        """
        http_info = self._list_smart_live_http_info(request)
        return self._call_api(**http_info)

    def list_smart_live_async_invoker(self, request):
        http_info = self._list_smart_live_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_smart_live_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/smart-live-rooms/{room_id}/smart-live-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListSmartLiveResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'create_since' in local_var_params:
            query_params.append(('create_since', local_var_params['create_since']))
        if 'create_until' in local_var_params:
            query_params.append(('create_until', local_var_params['create_until']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_smart_live_jobs_async(self, request):
        r"""查询租户所有数字人直播任务列表

        该接口用于查询租户所有数字人智能直播任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSmartLiveJobs
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListSmartLiveJobsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListSmartLiveJobsResponse`
        """
        http_info = self._list_smart_live_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_smart_live_jobs_async_invoker(self, request):
        http_info = self._list_smart_live_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_smart_live_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/smart-live-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListSmartLiveJobsResponse"
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
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'create_since' in local_var_params:
            query_params.append(('create_since', local_var_params['create_since']))
        if 'create_until' in local_var_params:
            query_params.append(('create_until', local_var_params['create_until']))
        if 'room_name' in local_var_params:
            query_params.append(('room_name', local_var_params['room_name']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_smart_live_rule_commands_async(self, request):
        r"""查询租户未确认的互动规则命令列表

        该接口用于查询租户未确认的互动规则命令列表，仅限于需要做二次确认的特定用户使用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSmartLiveRuleCommands
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListSmartLiveRuleCommandsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListSmartLiveRuleCommandsResponse`
        """
        http_info = self._list_smart_live_rule_commands_http_info(request)
        return self._call_api(**http_info)

    def list_smart_live_rule_commands_async_invoker(self, request):
        http_info = self._list_smart_live_rule_commands_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_smart_live_rule_commands_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/smart-live-command/rule-commands",
            "request_type": request.__class__.__name__,
            "response_type": "ListSmartLiveRuleCommandsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_smart_live_script_commands_async(self, request):
        r"""查询租户未确认的剧本命令列表

        该接口用于查询租户未确认的剧本命令列表，仅限于需要做二次确认的特定用户使用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSmartLiveScriptCommands
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListSmartLiveScriptCommandsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListSmartLiveScriptCommandsResponse`
        """
        http_info = self._list_smart_live_script_commands_http_info(request)
        return self._call_api(**http_info)

    def list_smart_live_script_commands_async_invoker(self, request):
        http_info = self._list_smart_live_script_commands_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_smart_live_script_commands_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/smart-live-command/script-commands",
            "request_type": request.__class__.__name__,
            "response_type": "ListSmartLiveScriptCommandsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def live_event_report_async(self, request):
        r"""上报直播间事件

        该接口用于上报直播间事件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for LiveEventReport
        :type request: :class:`huaweicloudsdkmetastudio.v1.LiveEventReportRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LiveEventReportResponse`
        """
        http_info = self._live_event_report_http_info(request)
        return self._call_api(**http_info)

    def live_event_report_async_invoker(self, request):
        http_info = self._live_event_report_http_info(request)
        return AsyncInvoker(self, http_info)

    def _live_event_report_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/smart-live-rooms/{room_id}/smart-live-jobs/{job_id}/live-event-report",
            "request_type": request.__class__.__name__,
            "response_type": "LiveEventReportResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'auth_key' in local_var_params:
            query_params.append(('auth_key', local_var_params['auth_key']))
        if 'expires_time' in local_var_params:
            query_params.append(('expires_time', local_var_params['expires_time']))
        if 'refresh_url' in local_var_params:
            query_params.append(('refresh_url', local_var_params['refresh_url']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']
        if 'x_mss_auth_key' in local_var_params:
            header_params['x-mss-auth-key'] = local_var_params['x_mss_auth_key']
        if 'x_mss_expires_time' in local_var_params:
            header_params['x-mss-expires-time'] = local_var_params['x_mss_expires_time']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_smart_live_async(self, request):
        r"""查询数字人智能直播任务详情

        该接口用于查询数字人智能直播任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSmartLive
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowSmartLiveRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowSmartLiveResponse`
        """
        http_info = self._show_smart_live_http_info(request)
        return self._call_api(**http_info)

    def show_smart_live_async_invoker(self, request):
        http_info = self._show_smart_live_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_smart_live_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/smart-live-rooms/{room_id}/smart-live-jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSmartLiveResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def start_smart_live_async(self, request):
        r"""启动数字人智能直播任务

        该接口用于启动数字人智能直播任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartSmartLive
        :type request: :class:`huaweicloudsdkmetastudio.v1.StartSmartLiveRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.StartSmartLiveResponse`
        """
        http_info = self._start_smart_live_http_info(request)
        return self._call_api(**http_info)

    def start_smart_live_async_invoker(self, request):
        http_info = self._start_smart_live_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_smart_live_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/smart-live-rooms/{room_id}/smart-live-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "StartSmartLiveResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def stop_smart_live_async(self, request):
        r"""结束数字人智能直播任务

        该接口用于结束数字人智能直播任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopSmartLive
        :type request: :class:`huaweicloudsdkmetastudio.v1.StopSmartLiveRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.StopSmartLiveResponse`
        """
        http_info = self._stop_smart_live_http_info(request)
        return self._call_api(**http_info)

    def stop_smart_live_async_invoker(self, request):
        http_info = self._stop_smart_live_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_smart_live_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/smart-live-rooms/{room_id}/smart-live-jobs/{job_id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopSmartLiveResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def confirm_smar_live_room_async(self, request):
        r"""直播间确认

        该接口用直播间二次确认
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ConfirmSmarLiveRoom
        :type request: :class:`huaweicloudsdkmetastudio.v1.ConfirmSmarLiveRoomRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ConfirmSmarLiveRoomResponse`
        """
        http_info = self._confirm_smar_live_room_http_info(request)
        return self._call_api(**http_info)

    def confirm_smar_live_room_async_invoker(self, request):
        http_info = self._confirm_smar_live_room_http_info(request)
        return AsyncInvoker(self, http_info)

    def _confirm_smar_live_room_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/smart-live-rooms/{room_id}/confirm",
            "request_type": request.__class__.__name__,
            "response_type": "ConfirmSmarLiveRoomResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_smart_live_room_async(self, request):
        r"""创建智能直播间

        该接口用于创建智能直播间。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSmartLiveRoom
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateSmartLiveRoomRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateSmartLiveRoomResponse`
        """
        http_info = self._create_smart_live_room_http_info(request)
        return self._call_api(**http_info)

    def create_smart_live_room_async_invoker(self, request):
        http_info = self._create_smart_live_room_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_smart_live_room_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/smart-live-rooms",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSmartLiveRoomResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_smart_live_room_async(self, request):
        r"""删除智能直播间

        该接口用于删除智能直播间。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSmartLiveRoom
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteSmartLiveRoomRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteSmartLiveRoomResponse`
        """
        http_info = self._delete_smart_live_room_http_info(request)
        return self._call_api(**http_info)

    def delete_smart_live_room_async_invoker(self, request):
        http_info = self._delete_smart_live_room_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_smart_live_room_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/smart-live-rooms/{room_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSmartLiveRoomResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_smart_live_rooms_async(self, request):
        r"""查询智能直播间列表

        该接口用于智能直播间列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSmartLiveRooms
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListSmartLiveRoomsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListSmartLiveRoomsResponse`
        """
        http_info = self._list_smart_live_rooms_http_info(request)
        return self._call_api(**http_info)

    def list_smart_live_rooms_async_invoker(self, request):
        http_info = self._list_smart_live_rooms_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_smart_live_rooms_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/smart-live-rooms",
            "request_type": request.__class__.__name__,
            "response_type": "ListSmartLiveRoomsResponse"
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
        if 'room_name' in local_var_params:
            query_params.append(('room_name', local_var_params['room_name']))
        if 'dh_id' in local_var_params:
            query_params.append(('dh_id', local_var_params['dh_id']))
        if 'model_name' in local_var_params:
            query_params.append(('model_name', local_var_params['model_name']))
        if 'live_state' in local_var_params:
            query_params.append(('live_state', local_var_params['live_state']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'room_type' in local_var_params:
            query_params.append(('room_type', local_var_params['room_type']))
        if 'template_own_type' in local_var_params:
            query_params.append(('template_own_type', local_var_params['template_own_type']))
        if 'confirm_state' in local_var_params:
            query_params.append(('confirm_state', local_var_params['confirm_state']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_smart_live_room_async(self, request):
        r"""查询智能直播间剧本详情

        该接口用于查询智能直播间剧本详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSmartLiveRoom
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowSmartLiveRoomRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowSmartLiveRoomResponse`
        """
        http_info = self._show_smart_live_room_http_info(request)
        return self._call_api(**http_info)

    def show_smart_live_room_async_invoker(self, request):
        http_info = self._show_smart_live_room_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_smart_live_room_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/smart-live-rooms/{room_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSmartLiveRoomResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_smart_live_room_async(self, request):
        r"""更新智能直播间信息

        该接口用于智能直播间信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSmartLiveRoom
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateSmartLiveRoomRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateSmartLiveRoomResponse`
        """
        http_info = self._update_smart_live_room_http_info(request)
        return self._call_api(**http_info)

    def update_smart_live_room_async_invoker(self, request):
        http_info = self._update_smart_live_room_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_smart_live_room_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/smart-live-rooms/{room_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSmartLiveRoomResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_styles_async(self, request):
        r"""查询数字人风格列表

        查询数字人风格列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListStyles
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListStylesRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListStylesResponse`
        """
        http_info = self._list_styles_http_info(request)
        return self._call_api(**http_info)

    def list_styles_async_invoker(self, request):
        http_info = self._list_styles_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_styles_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/styles",
            "request_type": request.__class__.__name__,
            "response_type": "ListStylesResponse"
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
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'create_until' in local_var_params:
            query_params.append(('create_until', local_var_params['create_until']))
        if 'create_since' in local_var_params:
            query_params.append(('create_since', local_var_params['create_since']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_subtitle_file_async(self, request):
        r"""创建分身数字人视频字幕文件

        该接口用于创建分身数字人视频字幕文件任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSubtitleFile
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateSubtitleFileRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateSubtitleFileResponse`
        """
        http_info = self._create_subtitle_file_http_info(request)
        return self._call_api(**http_info)

    def create_subtitle_file_async_invoker(self, request):
        http_info = self._create_subtitle_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_subtitle_file_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/subtitle-files",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSubtitleFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_subtitle_file_async(self, request):
        r"""查询分身数字人视频字幕文件任务详情

        该接口用于查询分身数字人视频字幕文件任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSubtitleFile
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowSubtitleFileRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowSubtitleFileResponse`
        """
        http_info = self._show_subtitle_file_http_info(request)
        return self._call_api(**http_info)

    def show_subtitle_file_async_invoker(self, request):
        http_info = self._show_subtitle_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_subtitle_file_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/subtitle-files/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSubtitleFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_facial_animations_async(self, request):
        r"""创建语音驱动表情动画任务

        该接口用于创建驱动数字人表情的任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateFacialAnimations
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateFacialAnimationsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateFacialAnimationsResponse`
        """
        http_info = self._create_facial_animations_http_info(request)
        return self._call_api(**http_info)

    def create_facial_animations_async_invoker(self, request):
        http_info = self._create_facial_animations_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_facial_animations_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/ttsa/fas",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFacialAnimationsResponse"
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

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_ttsa_async(self, request):
        r"""创建语音驱动任务

        该接口用于创建驱动数字人表情、动作及语音的任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTtsa
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateTtsaRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateTtsaResponse`
        """
        http_info = self._create_ttsa_http_info(request)
        return self._call_api(**http_info)

    def create_ttsa_async_invoker(self, request):
        http_info = self._create_ttsa_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_ttsa_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/ttsa-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTtsaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_facial_animations_data_async(self, request):
        r"""获取语音驱动表情数据

        该接口用于获取生成的数字人表情驱动数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFacialAnimationsData
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListFacialAnimationsDataRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListFacialAnimationsDataResponse`
        """
        http_info = self._list_facial_animations_data_http_info(request)
        return self._call_api(**http_info)

    def list_facial_animations_data_async_invoker(self, request):
        http_info = self._list_facial_animations_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_facial_animations_data_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/fas-jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListFacialAnimationsDataResponse"
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_ttsa_data_async(self, request):
        r"""获取语音驱动数据

        该接口用于获取生成的数字人驱动数据，包括语音、表情、动作等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTtsaData
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListTtsaDataRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListTtsaDataResponse`
        """
        http_info = self._list_ttsa_data_http_info(request)
        return self._call_api(**http_info)

    def list_ttsa_data_async_invoker(self, request):
        http_info = self._list_ttsa_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ttsa_data_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/ttsa-jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListTtsaDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_ttsa_jobs_async(self, request):
        r"""获取语音驱动任务列表

        该接口用于查询驱动数字人表情、动作及语音的任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTtsaJobs
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListTtsaJobsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListTtsaJobsResponse`
        """
        http_info = self._list_ttsa_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_ttsa_jobs_async_invoker(self, request):
        http_info = self._list_ttsa_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ttsa_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/ttsa-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListTtsaJobsResponse"
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
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def count_tenant_resources_async(self, request):
        r"""统计时间段内过期的资源数量

        统计指定时间段内即将过期的包周期与一次性资源数量。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CountTenantResources
        :type request: :class:`huaweicloudsdkmetastudio.v1.CountTenantResourcesRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CountTenantResourcesResponse`
        """
        http_info = self._count_tenant_resources_http_info(request)
        return self._call_api(**http_info)

    def count_tenant_resources_async_invoker(self, request):
        http_info = self._count_tenant_resources_http_info(request)
        return AsyncInvoker(self, http_info)

    def _count_tenant_resources_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/tenants/resources-count",
            "request_type": request.__class__.__name__,
            "response_type": "CountTenantResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'business' in local_var_params:
            query_params.append(('business', local_var_params['business']))
        if 'resource_expire_start_time' in local_var_params:
            query_params.append(('resource_expire_start_time', local_var_params['resource_expire_start_time']))
        if 'resource_expire_end_time' in local_var_params:
            query_params.append(('resource_expire_end_time', local_var_params['resource_expire_end_time']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_tenant_resources_async(self, request):
        r"""查看租户资源列表

        查看租户资源列表。
         &gt; 按需套餐包用量本接口无法查询，需要调用CBC接口查询，详见[按需套餐包用量查询](https://cbc.huaweicloud.com/bm/support/api-apidt/CBCInterface_0001239.html)和[查询资源包信息](https://cbc.huaweicloud.com/bm/support/api-apidt/CBCInterface_0000511.html)。
        &gt; 各种资源的计费方式请参考[计费说明](https://support.huaweicloud.com/productdesc-metastudio/metastudio_01_0006.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTenantResources
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListTenantResourcesRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListTenantResourcesResponse`
        """
        http_info = self._list_tenant_resources_http_info(request)
        return self._call_api(**http_info)

    def list_tenant_resources_async_invoker(self, request):
        http_info = self._list_tenant_resources_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tenant_resources_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/tenants/resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListTenantResourcesResponse"
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
        if 'resource' in local_var_params:
            query_params.append(('resource', local_var_params['resource']))
        if 'business' in local_var_params:
            query_params.append(('business', local_var_params['business']))
        if 'resource_source' in local_var_params:
            query_params.append(('resource_source', local_var_params['resource_source']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'order_id' in local_var_params:
            query_params.append(('order_id', local_var_params['order_id']))
        if 'charging_mode' in local_var_params:
            query_params.append(('charging_mode', local_var_params['charging_mode']))
        if 'resource_expire_start_time' in local_var_params:
            query_params.append(('resource_expire_start_time', local_var_params['resource_expire_start_time']))
        if 'resource_expire_end_time' in local_var_params:
            query_params.append(('resource_expire_end_time', local_var_params['resource_expire_end_time']))
        if 'sub_resource' in local_var_params:
            query_params.append(('sub_resource', local_var_params['sub_resource']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_resource_usage_async(self, request):
        r"""查看租户资源用量信息

        查询租户一次性和包周期（包年/包月）资源用量信息。
        &gt; 按需套餐包用量本接口无法查询，需要调用CBC接口查询，详见[按需套餐包用量查询](https://cbc.huaweicloud.com/bm/support/api-apidt/CBCInterface_0001239.html)和[查询资源包信息](https://cbc.huaweicloud.com/bm/support/api-apidt/CBCInterface_0000511.html)。
        &gt; 各种资源的计费方式请参考[计费说明](https://support.huaweicloud.com/productdesc-metastudio/metastudio_01_0006.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourceUsage
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowResourceUsageRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowResourceUsageResponse`
        """
        http_info = self._show_resource_usage_http_info(request)
        return self._call_api(**http_info)

    def show_resource_usage_async_invoker(self, request):
        http_info = self._show_resource_usage_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_resource_usage_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/tenants/resources-usage",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourceUsageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'resource' in local_var_params:
            query_params.append(('resource', local_var_params['resource']))
        if 'business' in local_var_params:
            query_params.append(('business', local_var_params['business']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def commit_voice_training_job_async(self, request):
        r"""提交语音训练任务

        提交训练任务,执行该接口后,任务会进入审核状态,审核完成后会等待训练。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CommitVoiceTrainingJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.CommitVoiceTrainingJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CommitVoiceTrainingJobResponse`
        """
        http_info = self._commit_voice_training_job_http_info(request)
        return self._call_api(**http_info)

    def commit_voice_training_job_async_invoker(self, request):
        http_info = self._commit_voice_training_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _commit_voice_training_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/voice-training-manage/user/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CommitVoiceTrainingJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def confirm_training_segment_async(self, request):
        r"""确认在线录音结果

        确认在线录音结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ConfirmTrainingSegment
        :type request: :class:`huaweicloudsdkmetastudio.v1.ConfirmTrainingSegmentRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ConfirmTrainingSegmentResponse`
        """
        http_info = self._confirm_training_segment_http_info(request)
        return self._call_api(**http_info)

    def confirm_training_segment_async_invoker(self, request):
        http_info = self._confirm_training_segment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _confirm_training_segment_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/voice-training-manage/user/training-segment",
            "request_type": request.__class__.__name__,
            "response_type": "ConfirmTrainingSegmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))
        if 'index' in local_var_params:
            query_params.append(('index', local_var_params['index']))

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

    def create_training_advance_job_async(self, request):
        r"""创建高级版语音训练任务

        用户创建语音训练高级版任务，该接口会返回一个obs上传地址，用于上传语音文件。
        
        语音文件为一段WAV格式的长音频文件，仅支持将语音文件打包成zip压缩格式上传。
        
        文件上传后，调用“提交语音训练任务”接口，启动审核和训练。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTrainingAdvanceJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateTrainingAdvanceJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateTrainingAdvanceJobResponse`
        """
        http_info = self._create_training_advance_job_http_info(request)
        return self._call_api(**http_info)

    def create_training_advance_job_async_invoker(self, request):
        http_info = self._create_training_advance_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_training_advance_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/voice-training-manage/user/advance-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTrainingAdvanceJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def create_training_basic_job_async(self, request):
        r"""创建基础版语音训练任务

        用户创建语音训练基础版任务，该接口会返回一个obs上传地址，用于上传语音文件。
        
        支持2种方式上传语音文件：
        * 语音文件和文本文件打包成zip上传：语音文件已经切分成20个wav文件，每个语音文件对应一个txt文本文件，所有文件打包成zip文件。语音文件命名规则：0.wav~19.wav；文本文件命名规则：0.txt~19.txt。
        * 语音文件和文本文件逐句上传：每次上传一句语料的语音文件和文本文件，再调用“确认在线录音结果”接口确认语音和文本内容是否一致。确认成功后再上传和确认下一句。
        
        文件上传后，调用“提交语音训练任务”接口，启动审核和训练。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTrainingBasicJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateTrainingBasicJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateTrainingBasicJobResponse`
        """
        http_info = self._create_training_basic_job_http_info(request)
        return self._call_api(**http_info)

    def create_training_basic_job_async_invoker(self, request):
        http_info = self._create_training_basic_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_training_basic_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/voice-training-manage/user/basic-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTrainingBasicJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def create_training_middle_job_async(self, request):
        r"""创建进阶版语音训练任务

        用户创建语音训练进阶版任务，该接口会返回一个obs上传地址，用于上传语音文件。
        
        支持2种方式上传语音文件：
        * 语音文件和文本文件打包成zip上传：语音文件已经切分成100个wav文件，每个语音文件对应一个txt文本文件，所有文件打包成zip文件。语音文件命名规则：0.wav~99.wav；文本文件命名规则：0.txt~99.txt。
        * 语音文件和文本文件逐句上传：每次上传一句语料的语音文件和文本文件，再调用“确认在线录音结果”接口确认语音和文本内容是否一致。确认成功后再上传和确认下一句。
        
        文件上传后，调用“提交语音训练任务”接口，启动审核和训练。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTrainingMiddleJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateTrainingMiddleJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateTrainingMiddleJobResponse`
        """
        http_info = self._create_training_middle_job_http_info(request)
        return self._call_api(**http_info)

    def create_training_middle_job_async_invoker(self, request):
        http_info = self._create_training_middle_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_training_middle_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/voice-training-manage/user/middle-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTrainingMiddleJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def delete_voice_training_job_async(self, request):
        r"""删除语音训练任务

        删除语音训练任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteVoiceTrainingJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteVoiceTrainingJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteVoiceTrainingJobResponse`
        """
        http_info = self._delete_voice_training_job_http_info(request)
        return self._call_api(**http_info)

    def delete_voice_training_job_async_invoker(self, request):
        http_info = self._delete_voice_training_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_voice_training_job_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/voice-training-manage/user/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVoiceTrainingJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def list_job_operation_log_async(self, request):
        r"""查询任务操作日志

        查询任务操作日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListJobOperationLog
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListJobOperationLogRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListJobOperationLogResponse`
        """
        http_info = self._list_job_operation_log_http_info(request)
        return self._call_api(**http_info)

    def list_job_operation_log_async_invoker(self, request):
        http_info = self._list_job_operation_log_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_job_operation_log_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/voice-training-manage/user/jobs/{job_id}/op-logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListJobOperationLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def list_voice_training_job_async(self, request):
        r"""查询语音训练任务列表

        查询语音训练任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVoiceTrainingJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListVoiceTrainingJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListVoiceTrainingJobResponse`
        """
        http_info = self._list_voice_training_job_http_info(request)
        return self._call_api(**http_info)

    def list_voice_training_job_async_invoker(self, request):
        http_info = self._list_voice_training_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_voice_training_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/voice-training-manage/user/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListVoiceTrainingJobResponse"
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
        if 'create_until' in local_var_params:
            query_params.append(('create_until', local_var_params['create_until']))
        if 'create_since' in local_var_params:
            query_params.append(('create_since', local_var_params['create_since']))
        if 'update_until' in local_var_params:
            query_params.append(('update_until', local_var_params['update_until']))
        if 'update_since' in local_var_params:
            query_params.append(('update_since', local_var_params['update_since']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))
        if 'voice_name' in local_var_params:
            query_params.append(('voice_name', local_var_params['voice_name']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))
        if 'job_type' in local_var_params:
            query_params.append(('job_type', local_var_params['job_type']))
        if 'batch_name' in local_var_params:
            query_params.append(('batch_name', local_var_params['batch_name']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'is_ondemand_resource' in local_var_params:
            query_params.append(('is_ondemand_resource', local_var_params['is_ondemand_resource']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def set_job_batch_name_async(self, request):
        r"""设置任务批次

        用户设置任务批次，该接口用于批量任务管理场景，设置任务的批次
        * 需要开通NA租户权限后才能正常调用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetJobBatchName
        :type request: :class:`huaweicloudsdkmetastudio.v1.SetJobBatchNameRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.SetJobBatchNameResponse`
        """
        http_info = self._set_job_batch_name_http_info(request)
        return self._call_api(**http_info)

    def set_job_batch_name_async_invoker(self, request):
        http_info = self._set_job_batch_name_http_info(request)
        return AsyncInvoker(self, http_info)

    def _set_job_batch_name_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/voice-training-manage/user/batch",
            "request_type": request.__class__.__name__,
            "response_type": "SetJobBatchNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def show_job_audit_result_async(self, request):
        r"""获取语音训练任务审核结果

        获取语音训练任务审核结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobAuditResult
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowJobAuditResultRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowJobAuditResultResponse`
        """
        http_info = self._show_job_audit_result_http_info(request)
        return self._call_api(**http_info)

    def show_job_audit_result_async_invoker(self, request):
        http_info = self._show_job_audit_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_audit_result_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/voice-training-manage/user/jobs/{job_id}/audit-result",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobAuditResultResponse"
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_job_uploading_address_async(self, request):
        r"""获取语音文件上传地址

        获取语音文件上传地址
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobUploadingAddress
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowJobUploadingAddressRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowJobUploadingAddressResponse`
        """
        http_info = self._show_job_uploading_address_http_info(request)
        return self._call_api(**http_info)

    def show_job_uploading_address_async_invoker(self, request):
        http_info = self._show_job_uploading_address_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_uploading_address_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/voice-training-manage/user/jobs/{job_id}/uploading-address-url",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobUploadingAddressResponse"
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_tenant_duration_cfg_async(self, request):
        r"""查询用户配置的个性化音频时长

        查询用户配置的个性化音频时长
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTenantDurationCfg
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowTenantDurationCfgRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowTenantDurationCfgResponse`
        """
        http_info = self._show_tenant_duration_cfg_http_info(request)
        return self._call_api(**http_info)

    def show_tenant_duration_cfg_async_invoker(self, request):
        http_info = self._show_tenant_duration_cfg_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_tenant_duration_cfg_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/voice-training-manage/user/tenant-duration-cfg",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTenantDurationCfgResponse"
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

    def show_training_segment_info_async(self, request):
        r"""获取在线录音确认结果

        获取在线录音确认结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTrainingSegmentInfo
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowTrainingSegmentInfoRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowTrainingSegmentInfoResponse`
        """
        http_info = self._show_training_segment_info_http_info(request)
        return self._call_api(**http_info)

    def show_training_segment_info_async_invoker(self, request):
        http_info = self._show_training_segment_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_training_segment_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/voice-training-manage/user/training-segment",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTrainingSegmentInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_voice_training_job_async(self, request):
        r"""查询语音训练任务详情

        查询语音训练任务详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVoiceTrainingJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowVoiceTrainingJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowVoiceTrainingJobResponse`
        """
        http_info = self._show_voice_training_job_http_info(request)
        return self._call_api(**http_info)

    def show_voice_training_job_async_invoker(self, request):
        http_info = self._show_voice_training_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_voice_training_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/voice-training-manage/user/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVoiceTrainingJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def create2d_model_training_job_async(self, request):
        r"""创建分身数字人模型训练任务

        该接口用于创建分身数字人模型训练任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for Create2dModelTrainingJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.Create2dModelTrainingJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.Create2dModelTrainingJobResponse`
        """
        http_info = self._create2d_model_training_job_http_info(request)
        return self._call_api(**http_info)

    def create2d_model_training_job_async_invoker(self, request):
        http_info = self._create2d_model_training_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create2d_model_training_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-training-manage/user/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "Create2dModelTrainingJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete2d_model_training_job_async(self, request):
        r"""删除分身数字人模型训练任务

        该接口用于删除分身数字人模型训练任务。同时需要删除训练任务相关的训练视频、身份证照片、授权文件、模型资产等。
        &gt; * 该接口应当在任务处于以下状态时调用：WAIT_FILE_UPLOAD、AUTO_VERIFY_FAILED、MANUAL_VERIFYING、MANUAL_VERIFY_FAILED、TRAINING_DATA_PREPROCESS_FAILED、TRAIN_FAILED、INFERENCE_DATA_PREPROCESS_FAILED、JOB_SUCCESS、WAIT_USER_CONFIRM、JOB_REJECT、JOB_FINISH
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for Delete2dModelTrainingJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.Delete2dModelTrainingJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.Delete2dModelTrainingJobResponse`
        """
        http_info = self._delete2d_model_training_job_http_info(request)
        return self._call_api(**http_info)

    def delete2d_model_training_job_async_invoker(self, request):
        http_info = self._delete2d_model_training_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete2d_model_training_job_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/digital-human-training-manage/user/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "Delete2dModelTrainingJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def execute2d_model_training_command_by_user_async(self, request):
        r"""租户执行分身数字人模型训练任务命令

        该接口用于租户执行分身数字人模型训练任务命令，如提交训练审核等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for Execute2dModelTrainingCommandByUser
        :type request: :class:`huaweicloudsdkmetastudio.v1.Execute2dModelTrainingCommandByUserRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.Execute2dModelTrainingCommandByUserResponse`
        """
        http_info = self._execute2d_model_training_command_by_user_http_info(request)
        return self._call_api(**http_info)

    def execute2d_model_training_command_by_user_async_invoker(self, request):
        http_info = self._execute2d_model_training_command_by_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _execute2d_model_training_command_by_user_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-training-manage/user/jobs/{job_id}/command",
            "request_type": request.__class__.__name__,
            "response_type": "Execute2dModelTrainingCommandByUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list2d_model_training_job_async(self, request):
        r"""查询分身数字人模型训练任务列表

        该接口用于查询分身数字人模型训练任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for List2dModelTrainingJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.List2dModelTrainingJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.List2dModelTrainingJobResponse`
        """
        http_info = self._list2d_model_training_job_http_info(request)
        return self._call_api(**http_info)

    def list2d_model_training_job_async_invoker(self, request):
        http_info = self._list2d_model_training_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list2d_model_training_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-training-manage/user/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "List2dModelTrainingJobResponse"
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
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'create_until' in local_var_params:
            query_params.append(('create_until', local_var_params['create_until']))
        if 'create_since' in local_var_params:
            query_params.append(('create_since', local_var_params['create_since']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'query_project_id' in local_var_params:
            query_params.append(('query_project_id', local_var_params['query_project_id']))
        if 'batch_name' in local_var_params:
            query_params.append(('batch_name', local_var_params['batch_name']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'model_resolution' in local_var_params:
            query_params.append(('model_resolution', local_var_params['model_resolution']))
        if 'is_flexus' in local_var_params:
            query_params.append(('is_flexus', local_var_params['is_flexus']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show2d_model_training_job_async(self, request):
        r"""查询分身数字人模型训练任务详情

        该接口用于查询分身数字人模型训练任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for Show2dModelTrainingJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.Show2dModelTrainingJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.Show2dModelTrainingJobResponse`
        """
        http_info = self._show2d_model_training_job_http_info(request)
        return self._call_api(**http_info)

    def show2d_model_training_job_async_invoker(self, request):
        http_info = self._show2d_model_training_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show2d_model_training_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-training-manage/user/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "Show2dModelTrainingJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update2d_model_training_job_async(self, request):
        r"""更新分身数字人模型训练任务

        该接口用于更新分身数字人模型训练任务。用于在自动审核或者人工审核不通过情况下，更新训练视频、身份证照片等。
        &gt; * 该接口只能在AUTO_VERIFY_FAILED或者MANUAL_VERIFY_FAILED状态下调用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for Update2dModelTrainingJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.Update2dModelTrainingJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.Update2dModelTrainingJobResponse`
        """
        http_info = self._update2d_model_training_job_http_info(request)
        return self._call_api(**http_info)

    def update2d_model_training_job_async_invoker(self, request):
        http_info = self._update2d_model_training_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update2d_model_training_job_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/digital-human-training-manage/user/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "Update2dModelTrainingJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def check_voice_asset_async(self, request):
        r"""校验音色模型是否可用（自研和第三方音色）

        该接口用于校验音色模型是否可用，模型可用返回模型信息，不可用返回具体不可用的原因
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckVoiceAsset
        :type request: :class:`huaweicloudsdkmetastudio.v1.CheckVoiceAssetRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CheckVoiceAssetResponse`
        """
        http_info = self._check_voice_asset_http_info(request)
        return self._call_api(**http_info)

    def check_voice_asset_async_invoker(self, request):
        http_info = self._check_voice_asset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_voice_asset_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/ttsc/check-voice-asset/{voice_asset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CheckVoiceAssetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'voice_asset_id' in local_var_params:
            path_params['voice_asset_id'] = local_var_params['voice_asset_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def show_tts_job_async(self, request):
        r"""获取TTS语音合成任务记录

        该接口用于获取TTS语音合成任务记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTtsJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowTtsJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowTtsJobResponse`
        """
        http_info = self._show_tts_job_http_info(request)
        return self._call_api(**http_info)

    def show_tts_job_async_invoker(self, request):
        http_info = self._show_tts_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_tts_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/ttsc/tts-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTtsJobResponse"
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
        if 'create_since' in local_var_params:
            query_params.append(('create_since', local_var_params['create_since']))
        if 'create_until' in local_var_params:
            query_params.append(('create_until', local_var_params['create_until']))
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))
        if 'job_type' in local_var_params:
            query_params.append(('job_type', local_var_params['job_type']))
        if 'tts_service_enum' in local_var_params:
            query_params.append(('tts_service_enum', local_var_params['tts_service_enum']))
        if 'business_type' in local_var_params:
            query_params.append(('business_type', local_var_params['business_type']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def show_tts_phonetic_symbol_async(self, request):
        r"""获取英文单词音标

        根据英文单词返回对应音标列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTtsPhoneticSymbol
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowTtsPhoneticSymbolRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowTtsPhoneticSymbolResponse`
        """
        http_info = self._show_tts_phonetic_symbol_http_info(request)
        return self._call_api(**http_info)

    def show_tts_phonetic_symbol_async_invoker(self, request):
        http_info = self._show_tts_phonetic_symbol_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_tts_phonetic_symbol_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/ttsc/phonetic-symbol",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTtsPhoneticSymbolResponse"
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
        if 'word' in local_var_params:
            query_params.append(('word', local_var_params['word']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def create_async_tts_job_async(self, request):
        r"""创建TTS异步任务

        该接口用于对外生成音频文件。每个预置音色的计费标准详见[预置音色计费标准](metastudio_02_0060.xml)。
        
        &gt; 使用本接口前，需要在MetaStudio控制台服务概览页面，开通“声音合成”的按需计费。
        &gt; 详细操作为：单击“声音合成”卡片中的“去开通”，在弹出的“开通按需计费服务提示”对话框中，勾选同意协议。单击“确定”，开通按需计费。
        &gt; 如需使用第三方声音进行语音合成，请购买出门问问声音套餐，操作请参考《用户指南》的“购买出门问问声音套餐”章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAsyncTtsJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateAsyncTtsJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateAsyncTtsJobResponse`
        """
        http_info = self._create_async_tts_job_http_info(request)
        return self._call_api(**http_info)

    def create_async_tts_job_async_invoker(self, request):
        http_info = self._create_async_tts_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_async_tts_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/ttsc/async-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAsyncTtsJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def create_tts_audition_async(self, request):
        r"""创建TTS试听任务

        该接口用于创建生成播报内容的语音试听文件任务。
        
        [第三方音色试听需要收费，收费标准参考：https://marketplace.huaweicloud.com/product/OFFI919400645308506112#productid&#x3D;OFFI919400645308506112](tag:hc)
        
        [第三方音色试听需要收费，收费标准参考：https://marketplace.huaweicloud.com/intl/contents/939bf377-3005-472b-a4e2-383911e6102f](tag:hk)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTtsAudition
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateTtsAuditionRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateTtsAuditionResponse`
        """
        http_info = self._create_tts_audition_http_info(request)
        return self._call_api(**http_info)

    def create_tts_audition_async_invoker(self, request):
        http_info = self._create_tts_audition_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_tts_audition_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/ttsc/audition",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTtsAuditionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def show_async_tts_job_async(self, request):
        r"""获取TTS异步任务

        该接口用于获取TTS音频文件下载链接。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAsyncTtsJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowAsyncTtsJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowAsyncTtsJobResponse`
        """
        http_info = self._show_async_tts_job_http_info(request)
        return self._call_api(**http_info)

    def show_async_tts_job_async_invoker(self, request):
        http_info = self._show_async_tts_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_async_tts_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/ttsc/async-jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAsyncTtsJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def show_tts_audition_file_async(self, request):
        r"""获取TTS试听文件

        该接口用于获取TTS试听文件下载链接，返回List中包含当前已生产的试听文件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTtsAuditionFile
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowTtsAuditionFileRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowTtsAuditionFileResponse`
        """
        http_info = self._show_tts_audition_file_http_info(request)
        return self._call_api(**http_info)

    def show_tts_audition_file_async_invoker(self, request):
        http_info = self._show_tts_audition_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_tts_audition_file_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/ttsc/audition-file/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTtsAuditionFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def create_ttsc_vocabulary_configs_async(self, request):
        r"""设置TTS租户级自定义读法配置

        该接口用于设置TTS租户级自定义读法配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTtscVocabularyConfigs
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateTtscVocabularyConfigsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateTtscVocabularyConfigsResponse`
        """
        http_info = self._create_ttsc_vocabulary_configs_http_info(request)
        return self._call_api(**http_info)

    def create_ttsc_vocabulary_configs_async_invoker(self, request):
        http_info = self._create_ttsc_vocabulary_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_ttsc_vocabulary_configs_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/ttsc/vocabulary-configs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTtscVocabularyConfigsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def create_ttsc_vocabulary_groups_async(self, request):
        r"""设置TTS租户级词表分组配置

        该接口用于设置TTS租户级词表分组配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTtscVocabularyGroups
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateTtscVocabularyGroupsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateTtscVocabularyGroupsResponse`
        """
        http_info = self._create_ttsc_vocabulary_groups_http_info(request)
        return self._call_api(**http_info)

    def create_ttsc_vocabulary_groups_async_invoker(self, request):
        http_info = self._create_ttsc_vocabulary_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_ttsc_vocabulary_groups_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/ttsc/vocabulary-groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTtscVocabularyGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def delete_ttsc_vocabulary_configs_async(self, request):
        r"""删除TTS租户级自定义读法配置

        该接口用于删除TTS租户级自定义读法配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTtscVocabularyConfigs
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteTtscVocabularyConfigsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteTtscVocabularyConfigsResponse`
        """
        http_info = self._delete_ttsc_vocabulary_configs_http_info(request)
        return self._call_api(**http_info)

    def delete_ttsc_vocabulary_configs_async_invoker(self, request):
        http_info = self._delete_ttsc_vocabulary_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_ttsc_vocabulary_configs_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/ttsc/vocabulary-configs",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTtscVocabularyConfigsResponse"
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
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def delete_ttsc_vocabulary_groups_async(self, request):
        r"""删除TTS租户级词表分组

        该接口用于删除TTS租户级词表分组配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTtscVocabularyGroups
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteTtscVocabularyGroupsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteTtscVocabularyGroupsResponse`
        """
        http_info = self._delete_ttsc_vocabulary_groups_http_info(request)
        return self._call_api(**http_info)

    def delete_ttsc_vocabulary_groups_async_invoker(self, request):
        http_info = self._delete_ttsc_vocabulary_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_ttsc_vocabulary_groups_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/ttsc/vocabulary-groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTtscVocabularyGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def list_ttsc_vocabulary_configs_async(self, request):
        r"""获取TTS租户级自定义读法配置

        该接口用于获取TTS租户级自定义读法配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTtscVocabularyConfigs
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListTtscVocabularyConfigsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListTtscVocabularyConfigsResponse`
        """
        http_info = self._list_ttsc_vocabulary_configs_http_info(request)
        return self._call_api(**http_info)

    def list_ttsc_vocabulary_configs_async_invoker(self, request):
        http_info = self._list_ttsc_vocabulary_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ttsc_vocabulary_configs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/ttsc/vocabulary-configs",
            "request_type": request.__class__.__name__,
            "response_type": "ListTtscVocabularyConfigsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'tts_service_name' in local_var_params:
            query_params.append(('tts_service_name', local_var_params['tts_service_name']))
        if 'is_vocabulary_config_enable' in local_var_params:
            query_params.append(('is_vocabulary_config_enable', local_var_params['is_vocabulary_config_enable']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'asset_id' in local_var_params:
            query_params.append(('asset_id', local_var_params['asset_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'search_key' in local_var_params:
            query_params.append(('search_key', local_var_params['search_key']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def list_ttsc_vocabulary_groups_async(self, request):
        r"""获取TTS租户级词表分组列表

        该接口用于获取TTS租户级词表分组列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTtscVocabularyGroups
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListTtscVocabularyGroupsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListTtscVocabularyGroupsResponse`
        """
        http_info = self._list_ttsc_vocabulary_groups_http_info(request)
        return self._call_api(**http_info)

    def list_ttsc_vocabulary_groups_async_invoker(self, request):
        http_info = self._list_ttsc_vocabulary_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ttsc_vocabulary_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/ttsc/vocabulary-groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListTtscVocabularyGroupsResponse"
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
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def save_ttsc_tenant_configs_async(self, request):
        r"""设置租户级配置

        该接口用于设置租户级配置，当前用于租户级自定义读法配置的全局开关。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SaveTtscTenantConfigs
        :type request: :class:`huaweicloudsdkmetastudio.v1.SaveTtscTenantConfigsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.SaveTtscTenantConfigsResponse`
        """
        http_info = self._save_ttsc_tenant_configs_http_info(request)
        return self._call_api(**http_info)

    def save_ttsc_tenant_configs_async_invoker(self, request):
        http_info = self._save_ttsc_tenant_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _save_ttsc_tenant_configs_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/ttsc/tenant-configs",
            "request_type": request.__class__.__name__,
            "response_type": "SaveTtscTenantConfigsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def save_ttsc_vocabulary_configs_async(self, request):
        r"""修改TTS租户级自定义读法配置

        该接口用于修改TTS租户级自定义读法配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SaveTtscVocabularyConfigs
        :type request: :class:`huaweicloudsdkmetastudio.v1.SaveTtscVocabularyConfigsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.SaveTtscVocabularyConfigsResponse`
        """
        http_info = self._save_ttsc_vocabulary_configs_http_info(request)
        return self._call_api(**http_info)

    def save_ttsc_vocabulary_configs_async_invoker(self, request):
        http_info = self._save_ttsc_vocabulary_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _save_ttsc_vocabulary_configs_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/ttsc/vocabulary-configs/{vocabulary_id}",
            "request_type": request.__class__.__name__,
            "response_type": "SaveTtscVocabularyConfigsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vocabulary_id' in local_var_params:
            path_params['vocabulary_id'] = local_var_params['vocabulary_id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def set_ttsc_group_assets_async(self, request):
        r"""设置TTS租户级词表分组的资产列表

        该接口用于设置TTS租户级词表分组的资产列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetTtscGroupAssets
        :type request: :class:`huaweicloudsdkmetastudio.v1.SetTtscGroupAssetsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.SetTtscGroupAssetsResponse`
        """
        http_info = self._set_ttsc_group_assets_http_info(request)
        return self._call_api(**http_info)

    def set_ttsc_group_assets_async_invoker(self, request):
        http_info = self._set_ttsc_group_assets_http_info(request)
        return AsyncInvoker(self, http_info)

    def _set_ttsc_group_assets_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/ttsc/group-assets/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "SetTtscGroupAssetsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def show_vocabulary_switch_configs_async(self, request):
        r"""获取租户级全局配置

        该接口用于获取租户级全局配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVocabularySwitchConfigs
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowVocabularySwitchConfigsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowVocabularySwitchConfigsResponse`
        """
        http_info = self._show_vocabulary_switch_configs_http_info(request)
        return self._call_api(**http_info)

    def show_vocabulary_switch_configs_async_invoker(self, request):
        http_info = self._show_vocabulary_switch_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_vocabulary_switch_configs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/ttsc/tenant-configs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVocabularySwitchConfigsResponse"
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
        if 'key' in local_var_params:
            query_params.append(('key', local_var_params['key']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def update_ttsc_vocabulary_groups_async(self, request):
        r"""TTS租户级词表分组重命名

        该接口用于对TTS租户级词表分组重命名。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTtscVocabularyGroups
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateTtscVocabularyGroupsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateTtscVocabularyGroupsResponse`
        """
        http_info = self._update_ttsc_vocabulary_groups_http_info(request)
        return self._call_api(**http_info)

    def update_ttsc_vocabulary_groups_async_invoker(self, request):
        http_info = self._update_ttsc_vocabulary_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_ttsc_vocabulary_groups_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/ttsc/vocabulary-groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTtscVocabularyGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def create_video_motion_capture_job_async(self, request):
        r"""创建视频驱动任务

        该接口用于创建视频驱动任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVideoMotionCaptureJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateVideoMotionCaptureJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateVideoMotionCaptureJobResponse`
        """
        http_info = self._create_video_motion_capture_job_http_info(request)
        return self._call_api(**http_info)

    def create_video_motion_capture_job_async_invoker(self, request):
        http_info = self._create_video_motion_capture_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_video_motion_capture_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/video-motion-capture-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVideoMotionCaptureJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']
        if 'x_user_privilege' in local_var_params:
            header_params['X-User-Privilege'] = local_var_params['x_user_privilege']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def execute_video_motion_capture_command_async(self, request):
        r"""控制数字人驱动

        该接口用于控制数字人驱动。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteVideoMotionCaptureCommand
        :type request: :class:`huaweicloudsdkmetastudio.v1.ExecuteVideoMotionCaptureCommandRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ExecuteVideoMotionCaptureCommandResponse`
        """
        http_info = self._execute_video_motion_capture_command_http_info(request)
        return self._call_api(**http_info)

    def execute_video_motion_capture_command_async_invoker(self, request):
        http_info = self._execute_video_motion_capture_command_http_info(request)
        return AsyncInvoker(self, http_info)

    def _execute_video_motion_capture_command_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/video-motion-capture-jobs/{job_id}/command",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteVideoMotionCaptureCommandResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_video_motion_capture_jobs_async(self, request):
        r"""查询视频驱动任务列表

        该接口用于查询视频驱动任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVideoMotionCaptureJobs
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListVideoMotionCaptureJobsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListVideoMotionCaptureJobsResponse`
        """
        http_info = self._list_video_motion_capture_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_video_motion_capture_jobs_async_invoker(self, request):
        http_info = self._list_video_motion_capture_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_video_motion_capture_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/video-motion-capture-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListVideoMotionCaptureJobsResponse"
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
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_video_motion_capture_job_async(self, request):
        r"""查询视频驱动任务详情

        该接口用于查询视频驱动任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVideoMotionCaptureJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowVideoMotionCaptureJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowVideoMotionCaptureJobResponse`
        """
        http_info = self._show_video_motion_capture_job_http_info(request)
        return self._call_api(**http_info)

    def show_video_motion_capture_job_async_invoker(self, request):
        http_info = self._show_video_motion_capture_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_video_motion_capture_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/video-motion-capture-jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVideoMotionCaptureJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def stop_video_motion_capture_job_async(self, request):
        r"""停止视频驱动任务

        该接口用于停止视频驱动任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopVideoMotionCaptureJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.StopVideoMotionCaptureJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.StopVideoMotionCaptureJobResponse`
        """
        http_info = self._stop_video_motion_capture_job_http_info(request)
        return self._call_api(**http_info)

    def stop_video_motion_capture_job_async_invoker(self, request):
        http_info = self._stop_video_motion_capture_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_video_motion_capture_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/video-motion-capture-jobs/{job_id}/finish",
            "request_type": request.__class__.__name__,
            "response_type": "StopVideoMotionCaptureJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def copy_video_scripts_async(self, request):
        r"""复制视频制作剧本

        该接口用于复制视频制作剧本。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CopyVideoScripts
        :type request: :class:`huaweicloudsdkmetastudio.v1.CopyVideoScriptsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CopyVideoScriptsResponse`
        """
        http_info = self._copy_video_scripts_http_info(request)
        return self._call_api(**http_info)

    def copy_video_scripts_async_invoker(self, request):
        http_info = self._copy_video_scripts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _copy_video_scripts_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-video-scripts/{script_id}/copy",
            "request_type": request.__class__.__name__,
            "response_type": "CopyVideoScriptsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_id' in local_var_params:
            path_params['script_id'] = local_var_params['script_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_video_scripts_async(self, request):
        r"""创建视频制作剧本

        该接口用于创建视频制作剧本。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVideoScripts
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateVideoScriptsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateVideoScriptsResponse`
        """
        http_info = self._create_video_scripts_http_info(request)
        return self._call_api(**http_info)

    def create_video_scripts_async_invoker(self, request):
        http_info = self._create_video_scripts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_video_scripts_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-video-scripts",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVideoScriptsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_video_script_async(self, request):
        r"""删除视频制作剧本

        该接口用于删除视频制作剧本。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteVideoScript
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteVideoScriptRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteVideoScriptResponse`
        """
        http_info = self._delete_video_script_http_info(request)
        return self._call_api(**http_info)

    def delete_video_script_async_invoker(self, request):
        http_info = self._delete_video_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_video_script_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/digital-human-video-scripts/{script_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVideoScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_id' in local_var_params:
            path_params['script_id'] = local_var_params['script_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_video_scripts_async(self, request):
        r"""查询视频制作剧本列表

        该接口用于查询视频制作剧本列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVideoScripts
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListVideoScriptsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListVideoScriptsResponse`
        """
        http_info = self._list_video_scripts_http_info(request)
        return self._call_api(**http_info)

    def list_video_scripts_async_invoker(self, request):
        http_info = self._list_video_scripts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_video_scripts_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-video-scripts",
            "request_type": request.__class__.__name__,
            "response_type": "ListVideoScriptsResponse"
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
        if 'script_catalog' in local_var_params:
            query_params.append(('script_catalog', local_var_params['script_catalog']))
        if 'view_mode' in local_var_params:
            query_params.append(('view_mode', local_var_params['view_mode']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_video_script_async(self, request):
        r"""查询视频制作剧本详情

        该接口用于查询视频制作剧本详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVideoScript
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowVideoScriptRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowVideoScriptResponse`
        """
        http_info = self._show_video_script_http_info(request)
        return self._call_api(**http_info)

    def show_video_script_async_invoker(self, request):
        http_info = self._show_video_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_video_script_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-video-scripts/{script_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVideoScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_id' in local_var_params:
            path_params['script_id'] = local_var_params['script_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_video_script_async(self, request):
        r"""更新视频制作剧本

        该接口用于更新视频制作剧本。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateVideoScript
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateVideoScriptRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateVideoScriptResponse`
        """
        http_info = self._update_video_script_http_info(request)
        return self._call_api(**http_info)

    def update_video_script_async_invoker(self, request):
        http_info = self._update_video_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_video_script_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/digital-human-video-scripts/{script_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateVideoScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_id' in local_var_params:
            path_params['script_id'] = local_var_params['script_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_welcome_speech_async(self, request):
        r"""创建欢迎词

        该接口用于创建欢迎词。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWelcomeSpeech
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateWelcomeSpeechRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateWelcomeSpeechResponse`
        """
        http_info = self._create_welcome_speech_http_info(request)
        return self._call_api(**http_info)

    def create_welcome_speech_async_invoker(self, request):
        http_info = self._create_welcome_speech_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_welcome_speech_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/welcome-speech",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWelcomeSpeechResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_welcome_speech_async(self, request):
        r"""删除欢迎词

        该接口用于删除欢迎词。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteWelcomeSpeech
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteWelcomeSpeechRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteWelcomeSpeechResponse`
        """
        http_info = self._delete_welcome_speech_http_info(request)
        return self._call_api(**http_info)

    def delete_welcome_speech_async_invoker(self, request):
        http_info = self._delete_welcome_speech_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_welcome_speech_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/welcome-speech/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteWelcomeSpeechResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_welcome_speech_async(self, request):
        r"""查询欢迎词列表

        该接口用于查询欢迎词列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWelcomeSpeech
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListWelcomeSpeechRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListWelcomeSpeechResponse`
        """
        http_info = self._list_welcome_speech_http_info(request)
        return self._call_api(**http_info)

    def list_welcome_speech_async_invoker(self, request):
        http_info = self._list_welcome_speech_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_welcome_speech_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/welcome-speech",
            "request_type": request.__class__.__name__,
            "response_type": "ListWelcomeSpeechResponse"
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
        if 'robot_id' in local_var_params:
            query_params.append(('robot_id', local_var_params['robot_id']))
        if 'language' in local_var_params:
            query_params.append(('language', local_var_params['language']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_welcome_speech_async(self, request):
        r"""查询欢迎词详情

        该接口用于查询欢迎词详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWelcomeSpeech
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowWelcomeSpeechRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowWelcomeSpeechResponse`
        """
        http_info = self._show_welcome_speech_http_info(request)
        return self._call_api(**http_info)

    def show_welcome_speech_async_invoker(self, request):
        http_info = self._show_welcome_speech_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_welcome_speech_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/welcome-speech/{welcome_speech_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWelcomeSpeechResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'welcome_speech_id' in local_var_params:
            path_params['welcome_speech_id'] = local_var_params['welcome_speech_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_welcome_speech_switch_async(self, request):
        r"""查询欢迎词功能开关

        该接口用于查询欢迎词功能开关。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWelcomeSpeechSwitch
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowWelcomeSpeechSwitchRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowWelcomeSpeechSwitchResponse`
        """
        http_info = self._show_welcome_speech_switch_http_info(request)
        return self._call_api(**http_info)

    def show_welcome_speech_switch_async_invoker(self, request):
        http_info = self._show_welcome_speech_switch_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_welcome_speech_switch_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/welcome-speech-switch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWelcomeSpeechSwitchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'robot_id' in local_var_params:
            query_params.append(('robot_id', local_var_params['robot_id']))
        if 'language' in local_var_params:
            query_params.append(('language', local_var_params['language']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_welcome_speech_async(self, request):
        r"""修改欢迎词

        该接口用于修改欢迎词。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateWelcomeSpeech
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateWelcomeSpeechRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateWelcomeSpeechResponse`
        """
        http_info = self._update_welcome_speech_http_info(request)
        return self._call_api(**http_info)

    def update_welcome_speech_async_invoker(self, request):
        http_info = self._update_welcome_speech_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_welcome_speech_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/digital-human-chat/welcome-speech/{welcome_speech_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateWelcomeSpeechResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'welcome_speech_id' in local_var_params:
            path_params['welcome_speech_id'] = local_var_params['welcome_speech_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_welcome_speech_switch_async(self, request):
        r"""修改欢迎词功能开关

        该接口用于修改欢迎词功能开关。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateWelcomeSpeechSwitch
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateWelcomeSpeechSwitchRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateWelcomeSpeechSwitchResponse`
        """
        http_info = self._update_welcome_speech_switch_http_info(request)
        return self._call_api(**http_info)

    def update_welcome_speech_switch_async_invoker(self, request):
        http_info = self._update_welcome_speech_switch_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_welcome_speech_switch_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/welcome-speech-switch",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateWelcomeSpeechSwitchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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
