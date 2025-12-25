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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkversatile'")


class VersatileClient(Client):
    def __init__(self):
        super().__init__()
        self.model_package = importlib.import_module("huaweicloudsdkversatile.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "VersatileClient":
                raise TypeError("client type error, support client type is VersatileClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def search_knowledge_base(self, request):
        r"""知识库检索

        提供多知识库并行检索能力，支持语义、关键词、混合及FAQ四种检索模式，并允许自定义相似度阈值与返回结果数量，实现精准高效的信息匹配。
        
        **适用场景**：
        - 同时从多个知识库或文档集合中搜索相关内容。
        - 在预设的问答列表中快速定位最相关的答案（FAQ检索）。
        - 通过混合模式或调整阈值，兼顾搜索结果的准确性和全面性。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchKnowledgeBase
        :type request: :class:`huaweicloudsdkversatile.v1.SearchKnowledgeBaseRequest`
        :rtype: :class:`huaweicloudsdkversatile.v1.SearchKnowledgeBaseResponse`
        """
        http_info = self._search_knowledge_base_http_info(request)
        return self._call_api(**http_info)

    def search_knowledge_base_invoker(self, request):
        http_info = self._search_knowledge_base_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_knowledge_base_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/knowledge-bases/retrieve",
            "request_type": request.__class__.__name__,
            "response_type": "SearchKnowledgeBaseResponse"
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

    def run_agent(self, request):
        r"""运行一个智能体

        运行一个智能体，支持流式和非流式
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunAgent
        :type request: :class:`huaweicloudsdkversatile.v1.RunAgentRequest`
        :rtype: :class:`huaweicloudsdkversatile.v1.RunAgentResponse`
        """
        http_info = self._run_agent_http_info(request)
        return self._call_api(**http_info)

    def run_agent_invoker(self, request):
        http_info = self._run_agent_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_agent_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/agents/{agent_id}/conversations/{conversation_id}",
            "request_type": request.__class__.__name__,
            "response_type": "RunAgentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agent_id' in local_var_params:
            path_params['agent_id'] = local_var_params['agent_id']
        if 'conversation_id' in local_var_params:
            path_params['conversation_id'] = local_var_params['conversation_id']

        query_params = []
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}
        if 'stream' in local_var_params:
            header_params['stream'] = local_var_params['stream']

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

    def run_workflow(self, request):
        r"""运行一个工作流

        运行一个工作流，支持流式和非流式
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunWorkflow
        :type request: :class:`huaweicloudsdkversatile.v1.RunWorkflowRequest`
        :rtype: :class:`huaweicloudsdkversatile.v1.RunWorkflowResponse`
        """
        http_info = self._run_workflow_http_info(request)
        return self._call_api(**http_info)

    def run_workflow_invoker(self, request):
        http_info = self._run_workflow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_workflow_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workflows/{workflow_id}/conversations/{conversation_id}",
            "request_type": request.__class__.__name__,
            "response_type": "RunWorkflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']
        if 'conversation_id' in local_var_params:
            path_params['conversation_id'] = local_var_params['conversation_id']

        query_params = []
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))

        header_params = {}
        if 'stream' in local_var_params:
            header_params['stream'] = local_var_params['stream']

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

    def upload_agent_file(self, request):
        r"""上传文件

        上传文件，以供agent或者工作流使用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadAgentFile
        :type request: :class:`huaweicloudsdkversatile.v1.UploadAgentFileRequest`
        :rtype: :class:`huaweicloudsdkversatile.v1.UploadAgentFileResponse`
        """
        http_info = self._upload_agent_file_http_info(request)
        return self._call_api(**http_info)

    def upload_agent_file_invoker(self, request):
        http_info = self._upload_agent_file_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upload_agent_file_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/agent-runtime/upload-file",
            "request_type": request.__class__.__name__,
            "response_type": "UploadAgentFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))
        if 'expires' in local_var_params:
            query_params.append(('expires', local_var_params['expires']))
        if 'is_image' in local_var_params:
            query_params.append(('is_image', local_var_params['is_image']))

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
