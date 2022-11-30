# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

import six

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class NlpClient(Client):
    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def __init__(self):
        super(NlpClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdknlp.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "NlpClient":
            raise TypeError("client type error, support client type is NlpClient")

        return ClientBuilder(clazz)

    def run_aspect_sentiment(self, request):
        """属性级情感分析

        属性级情感分析，针对手机领域的用户评论进行属性级情感分析。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunAspectSentiment
        :type request: :class:`huaweicloudsdknlp.v2.RunAspectSentimentRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunAspectSentimentResponse`
        """
        return self.run_aspect_sentiment_with_http_info(request)

    def run_aspect_sentiment_with_http_info(self, request):
        all_params = ['post_aspect_sentiment_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/nlu/aspect-sentiment',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunAspectSentimentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_aspect_sentiment_advance(self, request):
        """属性级情感分析（高级版）

        属性级情感分析（高级版），针对手机、汽车领域的用户评论进行属性级情感分析。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunAspectSentimentAdvance
        :type request: :class:`huaweicloudsdknlp.v2.RunAspectSentimentAdvanceRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunAspectSentimentAdvanceResponse`
        """
        return self.run_aspect_sentiment_advance_with_http_info(request)

    def run_aspect_sentiment_advance_with_http_info(self, request):
        all_params = ['post_aspect_sentiment_advance_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/nlu/aspect-sentiment/advance',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunAspectSentimentAdvanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_classification(self, request):
        """文本分类

        针对广告领域的自动分类，判断是否是广告。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunClassification
        :type request: :class:`huaweicloudsdknlp.v2.RunClassificationRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunClassificationResponse`
        """
        return self.run_classification_with_http_info(request)

    def run_classification_with_http_info(self, request):
        all_params = ['post_classification_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/nlu/classification',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunClassificationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_constituency_parser(self, request):
        """成分句法分析

        识别句子中的成分以及成分之间的层次包含关系。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunConstituencyParser
        :type request: :class:`huaweicloudsdknlp.v2.RunConstituencyParserRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunConstituencyParserResponse`
        """
        return self.run_constituency_parser_with_http_info(request)

    def run_constituency_parser_with_http_info(self, request):
        all_params = ['constituency_parser_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/nlp-fundamental/constituency-parser',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunConstituencyParserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_dependency_parser(self, request):
        """依存句法分析

        识别句子中词汇与词汇之间的相互依存关系。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunDependencyParser
        :type request: :class:`huaweicloudsdknlp.v2.RunDependencyParserRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunDependencyParserResponse`
        """
        return self.run_dependency_parser_with_http_info(request)

    def run_dependency_parser_with_http_info(self, request):
        all_params = ['dependency_parser_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/nlp-fundamental/dependency-parser',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunDependencyParserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_doc_classification(self, request):
        """文档分类

        文档分类接口，输入文档内容，输出文档的标签和置信度，支持多个标签。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunDocClassification
        :type request: :class:`huaweicloudsdknlp.v2.RunDocClassificationRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunDocClassificationResponse`
        """
        return self.run_doc_classification_with_http_info(request)

    def run_doc_classification_with_http_info(self, request):
        all_params = ['post_document_classification_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/nlu/doc-classification',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunDocClassificationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_domain_sentiment(self, request):
        """情感分析（领域版）

        领域情感分析，针对未知领域，电商，汽车领域的用户评论进行情感分析。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunDomainSentiment
        :type request: :class:`huaweicloudsdknlp.v2.RunDomainSentimentRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunDomainSentimentResponse`
        """
        return self.run_domain_sentiment_with_http_info(request)

    def run_domain_sentiment_with_http_info(self, request):
        all_params = ['post_domain_sentiment_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/nlu/sentiment/domain',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunDomainSentimentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_entity_linking(self, request):
        """实体链接

        针对通用领域的文本进行实体链接分析，识别出其中的实体，并返回实体相关信息。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunEntityLinking
        :type request: :class:`huaweicloudsdknlp.v2.RunEntityLinkingRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunEntityLinkingResponse`
        """
        return self.run_entity_linking_with_http_info(request)

    def run_entity_linking_with_http_info(self, request):
        all_params = ['post_entity_linking_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/nlp-fundamental/entity-linking',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunEntityLinkingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_entity_sentiment(self, request):
        """实体级情感分析

        实体级情感分析，本产品适用于金融方面公司实体正负面新闻的分析。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunEntitySentiment
        :type request: :class:`huaweicloudsdknlp.v2.RunEntitySentimentRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunEntitySentimentResponse`
        """
        return self.run_entity_sentiment_with_http_info(request)

    def run_entity_sentiment_with_http_info(self, request):
        all_params = ['post_entity_sentiment_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/nlu/entity-sentiment',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunEntitySentimentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_event_extraction(self, request):
        """事件抽取

        事件抽取是指从自然语言文本中抽取指定类型的事件以及相关实体信息，并形成结构化数据输出的文本处理技术。
        目前只支持金融公告中会议召开、聘任、辞职、股票增持、股票减持5类事件以及相关要素的抽取。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunEventExtraction
        :type request: :class:`huaweicloudsdknlp.v2.RunEventExtractionRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunEventExtractionResponse`
        """
        return self.run_event_extraction_with_http_info(request)

    def run_event_extraction_with_http_info(self, request):
        all_params = ['event_extraction_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/nlp-fundamental/event-extraction',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunEventExtractionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_file_translation(self, request):
        """文档翻译

        文档翻译接口，用于翻译文档格式文件。由于文档翻译会需要较长的时间，因此识别是异步的，也即接口分为创建翻译任务和查询任务状态两个接口。创建翻译任务接口创建任务完成后返回，然后用户通过调用查询任务状态接口来获得翻译状态和临时URL。 用户可以使用临时URL下载翻译好的文件，每个临时URL有效期为10分种。翻译结果会保存24小时（从翻译完成的时间算起）。24小时后如果再访问，将会返回 \\\&quot;task id is not found\\\&quot;错误。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunFileTranslation
        :type request: :class:`huaweicloudsdknlp.v2.RunFileTranslationRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunFileTranslationResponse`
        """
        return self.run_file_translation_with_http_info(request)

    def run_file_translation_with_http_info(self, request):
        all_params = ['file_translation_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/machine-translation/file-translation/jobs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunFileTranslationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_get_file_translation_result(self, request):
        """文档翻译状态查询

        该接口用于获取文档翻译识别状态以及临时url，临时url可以用与获取翻译后的文档，每个临时url有效期为十分钟。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunGetFileTranslationResult
        :type request: :class:`huaweicloudsdknlp.v2.RunGetFileTranslationResultRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunGetFileTranslationResultResponse`
        """
        return self.run_get_file_translation_result_with_http_info(request)

    def run_get_file_translation_result_with_http_info(self, request):
        all_params = ['job_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/machine-translation/file-translation/jobs/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunGetFileTranslationResultResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_keyword_extract(self, request):
        """关键词抽取

        给定一段文本，抽取其中最能够反映文本主题或者意思的词汇。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunKeywordExtract
        :type request: :class:`huaweicloudsdknlp.v2.RunKeywordExtractRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunKeywordExtractResponse`
        """
        return self.run_keyword_extract_with_http_info(request)

    def run_keyword_extract_with_http_info(self, request):
        all_params = ['keyword_extract_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/nlp-fundamental/keyword-extraction',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunKeywordExtractResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_language_detection(self, request):
        """语种识别

        对于用户输入的文本，返回识别出的所属语种。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunLanguageDetection
        :type request: :class:`huaweicloudsdknlp.v2.RunLanguageDetectionRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunLanguageDetectionResponse`
        """
        return self.run_language_detection_with_http_info(request)

    def run_language_detection_with_http_info(self, request):
        all_params = ['language_detection_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/machine-translation/language-detection',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunLanguageDetectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_multi_grained_segment(self, request):
        """多粒度分词

        多粒度分词：给定一个句子输入，输出不同粒度的所有单词的层次结构。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunMultiGrainedSegment
        :type request: :class:`huaweicloudsdknlp.v2.RunMultiGrainedSegmentRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunMultiGrainedSegmentResponse`
        """
        return self.run_multi_grained_segment_with_http_info(request)

    def run_multi_grained_segment_with_http_info(self, request):
        all_params = ['post_multi_grained_segment_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/nlp-fundamental/multi-grained-segment',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunMultiGrainedSegmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_ner(self, request):
        """命名实体识别（基础版）

        基础版命名实体识别，对文本进行命名实体识别分析，目前支持人名、地名、时间、组织机构类实体的识别。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunNer
        :type request: :class:`huaweicloudsdknlp.v2.RunNerRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunNerResponse`
        """
        return self.run_ner_with_http_info(request)

    def run_ner_with_http_info(self, request):
        all_params = ['post_ner_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/nlp-fundamental/ner',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunNerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_ner_domain(self, request):
        """命名实体识别（领域版）

        领域版本命名实体识别，对文本进行命名实体识别分析，目前支持人名、地名、组织机构、时间点、日期、百分比、货币额度、序数词、计量规格词、民族、职业、邮箱12类实体的识别。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunNerDomain
        :type request: :class:`huaweicloudsdknlp.v2.RunNerDomainRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunNerDomainResponse`
        """
        return self.run_ner_domain_with_http_info(request)

    def run_ner_domain_with_http_info(self, request):
        all_params = ['post_ner_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/nlp-fundamental/ner/domain',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunNerDomainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_poem(self, request):
        """诗歌生成

        根据用户的输入生成诗歌。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunPoem
        :type request: :class:`huaweicloudsdknlp.v2.RunPoemRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunPoemResponse`
        """
        return self.run_poem_with_http_info(request)

    def run_poem_with_http_info(self, request):
        all_params = ['create_poem']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/nlg/poem',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunPoemResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_segment(self, request):
        """分词

        对文本进行分词和词性标注处理。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunSegment
        :type request: :class:`huaweicloudsdknlp.v2.RunSegmentRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunSegmentResponse`
        """
        return self.run_segment_with_http_info(request)

    def run_segment_with_http_info(self, request):
        all_params = ['post_segment_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/nlp-fundamental/segment',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunSegmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_semantic_parser(self, request):
        """意图理解

        针对天气、报时、新闻、笑话、翻译、提醒、闹钟、音乐8个领域进行意图理解，对用户的问题进行领域识别并提取领域内的参数。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunSemanticParser
        :type request: :class:`huaweicloudsdknlp.v2.RunSemanticParserRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunSemanticParserResponse`
        """
        return self.run_semantic_parser_with_http_info(request)

    def run_semantic_parser_with_http_info(self, request):
        all_params = ['intent_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/nlu/semantic-parser',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunSemanticParserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_sentence_embedding(self, request):
        """句向量

        输入句子，返回对应的句向量。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunSentenceEmbedding
        :type request: :class:`huaweicloudsdknlp.v2.RunSentenceEmbeddingRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunSentenceEmbeddingResponse`
        """
        return self.run_sentence_embedding_with_http_info(request)

    def run_sentence_embedding_with_http_info(self, request):
        all_params = ['post_sentence_embedding_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/nlp-fundamental/sentence-embedding',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunSentenceEmbeddingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_sentiment(self, request):
        """情感分析（基础版）

        通用情感分析，针对通用领域的用户评论进行情感分析。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunSentiment
        :type request: :class:`huaweicloudsdknlp.v2.RunSentimentRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunSentimentResponse`
        """
        return self.run_sentiment_with_http_info(request)

    def run_sentiment_with_http_info(self, request):
        all_params = ['post_general_sentiment_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/nlu/sentiment',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunSentimentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_summary(self, request):
        """文本摘要（基础版）

        对文本生成摘要。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunSummary
        :type request: :class:`huaweicloudsdknlp.v2.RunSummaryRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunSummaryResponse`
        """
        return self.run_summary_with_http_info(request)

    def run_summary_with_http_info(self, request):
        all_params = ['summary_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/nlg/summarization',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunSummaryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_summary_domain(self, request):
        """文本摘要（领域版）

        对文本生成摘要。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunSummaryDomain
        :type request: :class:`huaweicloudsdknlp.v2.RunSummaryDomainRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunSummaryDomainResponse`
        """
        return self.run_summary_domain_with_http_info(request)

    def run_summary_domain_with_http_info(self, request):
        all_params = ['summary_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/nlg/summarization/domain',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunSummaryDomainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_text_similarity(self, request):
        """文本相似度（基础版）

        文本相似度服务，对文本对进行相似度计算。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunTextSimilarity
        :type request: :class:`huaweicloudsdknlp.v2.RunTextSimilarityRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunTextSimilarityResponse`
        """
        return self.run_text_similarity_with_http_info(request)

    def run_text_similarity_with_http_info(self, request):
        all_params = ['post_text_similarity_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/nlp-fundamental/text-similarity',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunTextSimilarityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_text_similarity_advance(self, request):
        """文本相似度（高级版）

        文本相似度服务高级版，对文本对进行相似度计算。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunTextSimilarityAdvance
        :type request: :class:`huaweicloudsdknlp.v2.RunTextSimilarityAdvanceRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunTextSimilarityAdvanceResponse`
        """
        return self.run_text_similarity_advance_with_http_info(request)

    def run_text_similarity_advance_with_http_info(self, request):
        all_params = ['post_text_similarity_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/nlp-fundamental/text-similarity/advance',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunTextSimilarityAdvanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_text_translation(self, request):
        """文本翻译

        对于用户输入原始语种的文本，转换为目标语种的文本。
        在使用本API之前， 需要您完成服务申请， 具体操作流程请参见[申请服务](https://support.huaweicloud.com/api-nlp/nlp_03_0004.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunTextTranslation
        :type request: :class:`huaweicloudsdknlp.v2.RunTextTranslationRequest`
        :rtype: :class:`huaweicloudsdknlp.v2.RunTextTranslationResponse`
        """
        return self.run_text_translation_with_http_info(request)

    def run_text_translation_with_http_info(self, request):
        all_params = ['text_translation_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/machine-translation/text-translation',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunTextTranslationResponse',
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
