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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdknlp'")


class NlpAsyncClient(Client):
    def __init__(self):
        super(NlpAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdknlp.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "NlpAsyncClient":
                raise TypeError("client type error, support client type is NlpAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def run_aspect_sentiment_async(self, request):
        """属性级情感分析

        属性级情感分析，针对手机领域的用户评论进行属性级情感分析。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunAspectSentiment
        :type request: :class:`huaweicloudsdknlp.v2.RunAspectSentimentRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunAspectSentimentResponse`
        """
        http_info = self._run_aspect_sentiment_http_info(request)
        return self._call_api(**http_info)

    def run_aspect_sentiment_async_invoker(self, request):
        http_info = self._run_aspect_sentiment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_aspect_sentiment_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/nlu/aspect-sentiment",
            "request_type": request.__class__.__name__,
            "response_type": "RunAspectSentimentResponse"
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

    def run_aspect_sentiment_advance_async(self, request):
        """属性级情感分析（高级版）

        属性级情感分析（高级版），针对手机、汽车领域的用户评论进行属性级情感分析。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunAspectSentimentAdvance
        :type request: :class:`huaweicloudsdknlp.v2.RunAspectSentimentAdvanceRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunAspectSentimentAdvanceResponse`
        """
        http_info = self._run_aspect_sentiment_advance_http_info(request)
        return self._call_api(**http_info)

    def run_aspect_sentiment_advance_async_invoker(self, request):
        http_info = self._run_aspect_sentiment_advance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_aspect_sentiment_advance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/nlu/aspect-sentiment/advance",
            "request_type": request.__class__.__name__,
            "response_type": "RunAspectSentimentAdvanceResponse"
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

    def run_classification_async(self, request):
        """文本分类

        针对广告领域的自动分类，判断是否是广告。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunClassification
        :type request: :class:`huaweicloudsdknlp.v2.RunClassificationRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunClassificationResponse`
        """
        http_info = self._run_classification_http_info(request)
        return self._call_api(**http_info)

    def run_classification_async_invoker(self, request):
        http_info = self._run_classification_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_classification_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/nlu/classification",
            "request_type": request.__class__.__name__,
            "response_type": "RunClassificationResponse"
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

    def run_constituency_parser_async(self, request):
        """成分句法分析

        识别句子中的成分以及成分之间的层次包含关系。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunConstituencyParser
        :type request: :class:`huaweicloudsdknlp.v2.RunConstituencyParserRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunConstituencyParserResponse`
        """
        http_info = self._run_constituency_parser_http_info(request)
        return self._call_api(**http_info)

    def run_constituency_parser_async_invoker(self, request):
        http_info = self._run_constituency_parser_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_constituency_parser_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/nlp-fundamental/constituency-parser",
            "request_type": request.__class__.__name__,
            "response_type": "RunConstituencyParserResponse"
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

    def run_dependency_parser_async(self, request):
        """依存句法分析

        识别句子中词汇与词汇之间的相互依存关系。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunDependencyParser
        :type request: :class:`huaweicloudsdknlp.v2.RunDependencyParserRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunDependencyParserResponse`
        """
        http_info = self._run_dependency_parser_http_info(request)
        return self._call_api(**http_info)

    def run_dependency_parser_async_invoker(self, request):
        http_info = self._run_dependency_parser_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_dependency_parser_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/nlp-fundamental/dependency-parser",
            "request_type": request.__class__.__name__,
            "response_type": "RunDependencyParserResponse"
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

    def run_doc_classification_async(self, request):
        """文档分类

        文档分类接口，输入文档内容，输出文档的标签和置信度，支持多个标签。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunDocClassification
        :type request: :class:`huaweicloudsdknlp.v2.RunDocClassificationRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunDocClassificationResponse`
        """
        http_info = self._run_doc_classification_http_info(request)
        return self._call_api(**http_info)

    def run_doc_classification_async_invoker(self, request):
        http_info = self._run_doc_classification_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_doc_classification_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/nlu/doc-classification",
            "request_type": request.__class__.__name__,
            "response_type": "RunDocClassificationResponse"
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

    def run_domain_sentiment_async(self, request):
        """情感分析（领域版）

        领域情感分析，针对未知领域，电商，汽车领域的用户评论进行情感分析。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunDomainSentiment
        :type request: :class:`huaweicloudsdknlp.v2.RunDomainSentimentRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunDomainSentimentResponse`
        """
        http_info = self._run_domain_sentiment_http_info(request)
        return self._call_api(**http_info)

    def run_domain_sentiment_async_invoker(self, request):
        http_info = self._run_domain_sentiment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_domain_sentiment_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/nlu/sentiment/domain",
            "request_type": request.__class__.__name__,
            "response_type": "RunDomainSentimentResponse"
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

    def run_entity_linking_async(self, request):
        """实体链接

        针对通用领域的文本进行实体链接分析，识别出其中的实体，并返回实体相关信息。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunEntityLinking
        :type request: :class:`huaweicloudsdknlp.v2.RunEntityLinkingRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunEntityLinkingResponse`
        """
        http_info = self._run_entity_linking_http_info(request)
        return self._call_api(**http_info)

    def run_entity_linking_async_invoker(self, request):
        http_info = self._run_entity_linking_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_entity_linking_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/nlp-fundamental/entity-linking",
            "request_type": request.__class__.__name__,
            "response_type": "RunEntityLinkingResponse"
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

    def run_entity_sentiment_async(self, request):
        """实体级情感分析

        实体级情感分析，本产品适用于金融方面公司实体正负面新闻的分析。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunEntitySentiment
        :type request: :class:`huaweicloudsdknlp.v2.RunEntitySentimentRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunEntitySentimentResponse`
        """
        http_info = self._run_entity_sentiment_http_info(request)
        return self._call_api(**http_info)

    def run_entity_sentiment_async_invoker(self, request):
        http_info = self._run_entity_sentiment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_entity_sentiment_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/nlu/entity-sentiment",
            "request_type": request.__class__.__name__,
            "response_type": "RunEntitySentimentResponse"
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

    def run_event_extraction_async(self, request):
        """事件抽取

        事件抽取是指从自然语言文本中抽取指定类型的事件以及相关实体信息，并形成结构化数据输出的文本处理技术。
        目前只支持金融公告中会议召开、聘任、辞职、股票增持、股票减持5类事件以及相关要素的抽取。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunEventExtraction
        :type request: :class:`huaweicloudsdknlp.v2.RunEventExtractionRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunEventExtractionResponse`
        """
        http_info = self._run_event_extraction_http_info(request)
        return self._call_api(**http_info)

    def run_event_extraction_async_invoker(self, request):
        http_info = self._run_event_extraction_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_event_extraction_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/nlp-fundamental/event-extraction",
            "request_type": request.__class__.__name__,
            "response_type": "RunEventExtractionResponse"
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

    def run_file_translation_async(self, request):
        """文档翻译

        文档翻译接口，用于翻译文档格式文件。由于文档翻译会需要较长的时间，因此识别是异步的，也即接口分为创建翻译任务和查询任务状态两个接口。创建翻译任务接口创建任务完成后返回，然后用户通过调用查询任务状态接口来获得翻译状态和临时URL。 用户可以使用临时URL下载翻译好的文件，每个临时URL有效期为10分种。翻译结果会保存24小时（从翻译完成的时间算起）。24小时后如果再访问，将会返回 \\\&quot;task id is not found\\\&quot;错误。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunFileTranslation
        :type request: :class:`huaweicloudsdknlp.v2.RunFileTranslationRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunFileTranslationResponse`
        """
        http_info = self._run_file_translation_http_info(request)
        return self._call_api(**http_info)

    def run_file_translation_async_invoker(self, request):
        http_info = self._run_file_translation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_file_translation_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/machine-translation/file-translation/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "RunFileTranslationResponse"
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

    def run_get_file_translation_result_async(self, request):
        """文档翻译状态查询

        该接口用于获取文档翻译识别状态以及临时url，临时url可以用与获取翻译后的文档，每个临时url有效期为十分钟。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunGetFileTranslationResult
        :type request: :class:`huaweicloudsdknlp.v2.RunGetFileTranslationResultRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunGetFileTranslationResultResponse`
        """
        http_info = self._run_get_file_translation_result_http_info(request)
        return self._call_api(**http_info)

    def run_get_file_translation_result_async_invoker(self, request):
        http_info = self._run_get_file_translation_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_get_file_translation_result_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/machine-translation/file-translation/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "RunGetFileTranslationResultResponse"
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

    def run_keyword_extract_async(self, request):
        """关键词抽取

        给定一段文本，抽取其中最能够反映文本主题或者意思的词汇。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunKeywordExtract
        :type request: :class:`huaweicloudsdknlp.v2.RunKeywordExtractRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunKeywordExtractResponse`
        """
        http_info = self._run_keyword_extract_http_info(request)
        return self._call_api(**http_info)

    def run_keyword_extract_async_invoker(self, request):
        http_info = self._run_keyword_extract_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_keyword_extract_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/nlp-fundamental/keyword-extraction",
            "request_type": request.__class__.__name__,
            "response_type": "RunKeywordExtractResponse"
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

    def run_language_detection_async(self, request):
        """语种识别

        对于用户输入的文本，返回识别出的所属语种。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunLanguageDetection
        :type request: :class:`huaweicloudsdknlp.v2.RunLanguageDetectionRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunLanguageDetectionResponse`
        """
        http_info = self._run_language_detection_http_info(request)
        return self._call_api(**http_info)

    def run_language_detection_async_invoker(self, request):
        http_info = self._run_language_detection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_language_detection_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/machine-translation/language-detection",
            "request_type": request.__class__.__name__,
            "response_type": "RunLanguageDetectionResponse"
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

    def run_multi_grained_segment_async(self, request):
        """多粒度分词

        多粒度分词：给定一个句子输入，输出不同粒度的所有单词的层次结构。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunMultiGrainedSegment
        :type request: :class:`huaweicloudsdknlp.v2.RunMultiGrainedSegmentRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunMultiGrainedSegmentResponse`
        """
        http_info = self._run_multi_grained_segment_http_info(request)
        return self._call_api(**http_info)

    def run_multi_grained_segment_async_invoker(self, request):
        http_info = self._run_multi_grained_segment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_multi_grained_segment_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/nlp-fundamental/multi-grained-segment",
            "request_type": request.__class__.__name__,
            "response_type": "RunMultiGrainedSegmentResponse"
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

    def run_ner_async(self, request):
        """命名实体识别（基础版）

        基础版命名实体识别，对文本进行命名实体识别分析，目前支持人名、地名、时间、组织机构类实体的识别。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunNer
        :type request: :class:`huaweicloudsdknlp.v2.RunNerRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunNerResponse`
        """
        http_info = self._run_ner_http_info(request)
        return self._call_api(**http_info)

    def run_ner_async_invoker(self, request):
        http_info = self._run_ner_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_ner_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/nlp-fundamental/ner",
            "request_type": request.__class__.__name__,
            "response_type": "RunNerResponse"
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

    def run_ner_domain_async(self, request):
        """命名实体识别（领域版）

        领域版本命名实体识别，对文本进行命名实体识别分析，目前支持人名、地名、组织机构、时间点、日期、百分比、货币额度、序数词、计量规格词、民族、职业、邮箱12类实体的识别。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunNerDomain
        :type request: :class:`huaweicloudsdknlp.v2.RunNerDomainRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunNerDomainResponse`
        """
        http_info = self._run_ner_domain_http_info(request)
        return self._call_api(**http_info)

    def run_ner_domain_async_invoker(self, request):
        http_info = self._run_ner_domain_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_ner_domain_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/nlp-fundamental/ner/domain",
            "request_type": request.__class__.__name__,
            "response_type": "RunNerDomainResponse"
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

    def run_poem_async(self, request):
        """诗歌生成

        根据用户的输入生成诗歌。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunPoem
        :type request: :class:`huaweicloudsdknlp.v2.RunPoemRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunPoemResponse`
        """
        http_info = self._run_poem_http_info(request)
        return self._call_api(**http_info)

    def run_poem_async_invoker(self, request):
        http_info = self._run_poem_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_poem_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/nlg/poem",
            "request_type": request.__class__.__name__,
            "response_type": "RunPoemResponse"
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

    def run_segment_async(self, request):
        """分词

        对文本进行分词和词性标注处理。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunSegment
        :type request: :class:`huaweicloudsdknlp.v2.RunSegmentRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunSegmentResponse`
        """
        http_info = self._run_segment_http_info(request)
        return self._call_api(**http_info)

    def run_segment_async_invoker(self, request):
        http_info = self._run_segment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_segment_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/nlp-fundamental/segment",
            "request_type": request.__class__.__name__,
            "response_type": "RunSegmentResponse"
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

    def run_semantic_parser_async(self, request):
        """意图理解

        针对天气、报时、新闻、笑话、翻译、提醒、闹钟、音乐8个领域进行意图理解，对用户的问题进行领域识别并提取领域内的参数。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunSemanticParser
        :type request: :class:`huaweicloudsdknlp.v2.RunSemanticParserRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunSemanticParserResponse`
        """
        http_info = self._run_semantic_parser_http_info(request)
        return self._call_api(**http_info)

    def run_semantic_parser_async_invoker(self, request):
        http_info = self._run_semantic_parser_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_semantic_parser_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/nlu/semantic-parser",
            "request_type": request.__class__.__name__,
            "response_type": "RunSemanticParserResponse"
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

    def run_sentence_embedding_async(self, request):
        """句向量

        输入句子，返回对应的句向量。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunSentenceEmbedding
        :type request: :class:`huaweicloudsdknlp.v2.RunSentenceEmbeddingRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunSentenceEmbeddingResponse`
        """
        http_info = self._run_sentence_embedding_http_info(request)
        return self._call_api(**http_info)

    def run_sentence_embedding_async_invoker(self, request):
        http_info = self._run_sentence_embedding_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_sentence_embedding_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/nlp-fundamental/sentence-embedding",
            "request_type": request.__class__.__name__,
            "response_type": "RunSentenceEmbeddingResponse"
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

    def run_sentiment_async(self, request):
        """情感分析（基础版）

        通用情感分析，针对通用领域的用户评论进行情感分析。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunSentiment
        :type request: :class:`huaweicloudsdknlp.v2.RunSentimentRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunSentimentResponse`
        """
        http_info = self._run_sentiment_http_info(request)
        return self._call_api(**http_info)

    def run_sentiment_async_invoker(self, request):
        http_info = self._run_sentiment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_sentiment_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/nlu/sentiment",
            "request_type": request.__class__.__name__,
            "response_type": "RunSentimentResponse"
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

    def run_summary_async(self, request):
        """文本摘要（基础版）

        对文本生成摘要。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunSummary
        :type request: :class:`huaweicloudsdknlp.v2.RunSummaryRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunSummaryResponse`
        """
        http_info = self._run_summary_http_info(request)
        return self._call_api(**http_info)

    def run_summary_async_invoker(self, request):
        http_info = self._run_summary_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_summary_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/nlg/summarization",
            "request_type": request.__class__.__name__,
            "response_type": "RunSummaryResponse"
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

    def run_summary_domain_async(self, request):
        """文本摘要（领域版）

        对文本生成摘要。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunSummaryDomain
        :type request: :class:`huaweicloudsdknlp.v2.RunSummaryDomainRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunSummaryDomainResponse`
        """
        http_info = self._run_summary_domain_http_info(request)
        return self._call_api(**http_info)

    def run_summary_domain_async_invoker(self, request):
        http_info = self._run_summary_domain_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_summary_domain_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/nlg/summarization/domain",
            "request_type": request.__class__.__name__,
            "response_type": "RunSummaryDomainResponse"
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

    def run_text_similarity_async(self, request):
        """文本相似度（基础版）

        文本相似度服务，对文本对进行相似度计算。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunTextSimilarity
        :type request: :class:`huaweicloudsdknlp.v2.RunTextSimilarityRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunTextSimilarityResponse`
        """
        http_info = self._run_text_similarity_http_info(request)
        return self._call_api(**http_info)

    def run_text_similarity_async_invoker(self, request):
        http_info = self._run_text_similarity_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_text_similarity_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/nlp-fundamental/text-similarity",
            "request_type": request.__class__.__name__,
            "response_type": "RunTextSimilarityResponse"
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

    def run_text_similarity_advance_async(self, request):
        """文本相似度（高级版）

        文本相似度服务高级版，对文本对进行相似度计算。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunTextSimilarityAdvance
        :type request: :class:`huaweicloudsdknlp.v2.RunTextSimilarityAdvanceRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunTextSimilarityAdvanceResponse`
        """
        http_info = self._run_text_similarity_advance_http_info(request)
        return self._call_api(**http_info)

    def run_text_similarity_advance_async_invoker(self, request):
        http_info = self._run_text_similarity_advance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_text_similarity_advance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/nlp-fundamental/text-similarity/advance",
            "request_type": request.__class__.__name__,
            "response_type": "RunTextSimilarityAdvanceResponse"
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

    def run_text_translation_async(self, request):
        """文本翻译

        对于用户输入原始语种的文本，转换为目标语种的文本。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunTextTranslation
        :type request: :class:`huaweicloudsdknlp.v2.RunTextTranslationRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunTextTranslationResponse`
        """
        http_info = self._run_text_translation_http_info(request)
        return self._call_api(**http_info)

    def run_text_translation_async_invoker(self, request):
        http_info = self._run_text_translation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_text_translation_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/machine-translation/text-translation",
            "request_type": request.__class__.__name__,
            "response_type": "RunTextTranslationResponse"
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
