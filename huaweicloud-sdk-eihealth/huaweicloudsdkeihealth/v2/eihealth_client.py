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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkeihealth'")


class EiHealthClient(Client):
    def __init__(self):
        super().__init__()
        self.model_package = importlib.import_module("huaweicloudsdkeihealth.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "EiHealthClient":
                raise TypeError("client type error, support client type is EiHealthClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def show_drug_job_statistics(self, request):
        r"""统计药物作业数量和调用次数

        统计药物作业数量和调用次数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDrugJobStatistics
        :type request: :class:`huaweicloudsdkeihealth.v2.ShowDrugJobStatisticsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v2.ShowDrugJobStatisticsResponse`
        """
        http_info = self._show_drug_job_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_drug_job_statistics_invoker(self, request):
        http_info = self._show_drug_job_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_drug_job_statistics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eihealth-projects/drug-jobs/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDrugJobStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

    def create_message_feedback(self, request):
        r"""创建问答内容反馈

        创建问答内容反馈。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateMessageFeedback
        :type request: :class:`huaweicloudsdkeihealth.v2.CreateMessageFeedbackRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v2.CreateMessageFeedbackResponse`
        """
        http_info = self._create_message_feedback_http_info(request)
        return self._call_api(**http_info)

    def create_message_feedback_invoker(self, request):
        http_info = self._create_message_feedback_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_message_feedback_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/chats/{chat_id}/messages/{message_id}/feedback",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMessageFeedbackResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'chat_id' in local_var_params:
            path_params['chat_id'] = local_var_params['chat_id']
        if 'message_id' in local_var_params:
            path_params['message_id'] = local_var_params['message_id']

        query_params = []

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

    def create_assistant_model(self, request):
        r"""创建助手模型

        创建助手模型。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAssistantModel
        :type request: :class:`huaweicloudsdkeihealth.v2.CreateAssistantModelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v2.CreateAssistantModelResponse`
        """
        http_info = self._create_assistant_model_http_info(request)
        return self._call_api(**http_info)

    def create_assistant_model_invoker(self, request):
        http_info = self._create_assistant_model_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_assistant_model_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/model-vendors/{vendor_id}/models",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAssistantModelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vendor_id' in local_var_params:
            path_params['vendor_id'] = local_var_params['vendor_id']

        query_params = []

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

    def delete_assistant_model(self, request):
        r"""删除助手模型

        删除助手模型。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAssistantModel
        :type request: :class:`huaweicloudsdkeihealth.v2.DeleteAssistantModelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v2.DeleteAssistantModelResponse`
        """
        http_info = self._delete_assistant_model_http_info(request)
        return self._call_api(**http_info)

    def delete_assistant_model_invoker(self, request):
        http_info = self._delete_assistant_model_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_assistant_model_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/model-vendors/{vendor_id}/models/{model_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAssistantModelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vendor_id' in local_var_params:
            path_params['vendor_id'] = local_var_params['vendor_id']
        if 'model_id' in local_var_params:
            path_params['model_id'] = local_var_params['model_id']

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

    def list_all_assistant_models(self, request):
        r"""获取模型列表

        获取模型列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAllAssistantModels
        :type request: :class:`huaweicloudsdkeihealth.v2.ListAllAssistantModelsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v2.ListAllAssistantModelsResponse`
        """
        http_info = self._list_all_assistant_models_http_info(request)
        return self._call_api(**http_info)

    def list_all_assistant_models_invoker(self, request):
        http_info = self._list_all_assistant_models_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_all_assistant_models_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/assistant-models",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllAssistantModelsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'chain_of_thought' in local_var_params:
            query_params.append(('chain_of_thought', local_var_params['chain_of_thought']))
        if 'function_of_call' in local_var_params:
            query_params.append(('function_of_call', local_var_params['function_of_call']))
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_assistant_models(self, request):
        r"""获取供应商模型列表

        获取供应商模型列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAssistantModels
        :type request: :class:`huaweicloudsdkeihealth.v2.ListAssistantModelsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v2.ListAssistantModelsResponse`
        """
        http_info = self._list_assistant_models_http_info(request)
        return self._call_api(**http_info)

    def list_assistant_models_invoker(self, request):
        http_info = self._list_assistant_models_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_assistant_models_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/model-vendors/{vendor_id}/models",
            "request_type": request.__class__.__name__,
            "response_type": "ListAssistantModelsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vendor_id' in local_var_params:
            path_params['vendor_id'] = local_var_params['vendor_id']

        query_params = []
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_assistant_model(self, request):
        r"""更新助手模型

        更新助手模型。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAssistantModel
        :type request: :class:`huaweicloudsdkeihealth.v2.UpdateAssistantModelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v2.UpdateAssistantModelResponse`
        """
        http_info = self._update_assistant_model_http_info(request)
        return self._call_api(**http_info)

    def update_assistant_model_invoker(self, request):
        http_info = self._update_assistant_model_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_assistant_model_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/model-vendors/{vendor_id}/models/{model_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAssistantModelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vendor_id' in local_var_params:
            path_params['vendor_id'] = local_var_params['vendor_id']
        if 'model_id' in local_var_params:
            path_params['model_id'] = local_var_params['model_id']

        query_params = []

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

    def create_model_vendor(self, request):
        r"""创建模型供应商

        创建模型供应商。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateModelVendor
        :type request: :class:`huaweicloudsdkeihealth.v2.CreateModelVendorRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v2.CreateModelVendorResponse`
        """
        http_info = self._create_model_vendor_http_info(request)
        return self._call_api(**http_info)

    def create_model_vendor_invoker(self, request):
        http_info = self._create_model_vendor_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_model_vendor_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/model-vendors",
            "request_type": request.__class__.__name__,
            "response_type": "CreateModelVendorResponse"
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

    def delete_model_vendor(self, request):
        r"""删除模型供应商

        删除模型供应商。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteModelVendor
        :type request: :class:`huaweicloudsdkeihealth.v2.DeleteModelVendorRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v2.DeleteModelVendorResponse`
        """
        http_info = self._delete_model_vendor_http_info(request)
        return self._call_api(**http_info)

    def delete_model_vendor_invoker(self, request):
        http_info = self._delete_model_vendor_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_model_vendor_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/model-vendors/{vendor_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteModelVendorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vendor_id' in local_var_params:
            path_params['vendor_id'] = local_var_params['vendor_id']

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

    def list_model_vendors(self, request):
        r"""获取模型供应商列表

        获取模型供应商列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListModelVendors
        :type request: :class:`huaweicloudsdkeihealth.v2.ListModelVendorsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v2.ListModelVendorsResponse`
        """
        http_info = self._list_model_vendors_http_info(request)
        return self._call_api(**http_info)

    def list_model_vendors_invoker(self, request):
        http_info = self._list_model_vendors_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_model_vendors_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/model-vendors",
            "request_type": request.__class__.__name__,
            "response_type": "ListModelVendorsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_model_vendor(self, request):
        r"""更新模型供应商

        更新模型供应商。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateModelVendor
        :type request: :class:`huaweicloudsdkeihealth.v2.UpdateModelVendorRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v2.UpdateModelVendorResponse`
        """
        http_info = self._update_model_vendor_http_info(request)
        return self._call_api(**http_info)

    def update_model_vendor_invoker(self, request):
        http_info = self._update_model_vendor_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_model_vendor_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/model-vendors/{vendor_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateModelVendorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vendor_id' in local_var_params:
            path_params['vendor_id'] = local_var_params['vendor_id']

        query_params = []

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
