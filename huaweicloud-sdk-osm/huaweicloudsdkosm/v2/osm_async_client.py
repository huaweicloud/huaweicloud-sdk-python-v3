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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkosm'")


class OsmAsyncClient(Client):
    def __init__(self):
        super(OsmAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkosm.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials")
        else:
            if clazz.__name__ != "OsmAsyncClient":
                raise TypeError("client type error, support client type is OsmAsyncClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials")

        

        return client_builder

    def check_hosts_async(self, request):
        """验证授权主机

        验证授权主机密码是否正确
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckHosts
        :type request: :class:`huaweicloudsdkosm.v2.CheckHostsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CheckHostsResponse`
        """
        http_info = self._check_hosts_http_info(request)
        return self._call_api(**http_info)

    def check_hosts_async_invoker(self, request):
        http_info = self._check_hosts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_hosts_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/servicerequest/authorizations/authorization-details/{authorization_detail_id}/verify-host",
            "request_type": request.__class__.__name__,
            "response_type": "CheckHostsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'authorization_detail_id' in local_var_params:
            path_params['authorization_detail_id'] = local_var_params['authorization_detail_id']

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def check_need_verify_async(self, request):
        """是否需要验证

        是否需要验证
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckNeedVerify
        :type request: :class:`huaweicloudsdkosm.v2.CheckNeedVerifyRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CheckNeedVerifyResponse`
        """
        http_info = self._check_need_verify_http_info(request)
        return self._call_api(**http_info)

    def check_need_verify_async_invoker(self, request):
        http_info = self._check_need_verify_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_need_verify_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/verifycodes/need-verify",
            "request_type": request.__class__.__name__,
            "response_type": "CheckNeedVerifyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'contact_value' in local_var_params:
            query_params.append(('contact_value', local_var_params['contact_value']))
        if 'contact_way' in local_var_params:
            query_params.append(('contact_way', local_var_params['contact_way']))
        if 'area_code' in local_var_params:
            query_params.append(('area_code', local_var_params['area_code']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def check_verify_codes_async(self, request):
        """验证联系方式

        验证联系方式
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckVerifyCodes
        :type request: :class:`huaweicloudsdkosm.v2.CheckVerifyCodesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CheckVerifyCodesResponse`
        """
        http_info = self._check_verify_codes_http_info(request)
        return self._call_api(**http_info)

    def check_verify_codes_async_invoker(self, request):
        http_info = self._check_verify_codes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_verify_codes_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/servicerequest/verifycodes",
            "request_type": request.__class__.__name__,
            "response_type": "CheckVerifyCodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def confirm_authorizations_async(self, request):
        """租户确认授权

        租户确认授权
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ConfirmAuthorizations
        :type request: :class:`huaweicloudsdkosm.v2.ConfirmAuthorizationsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ConfirmAuthorizationsResponse`
        """
        http_info = self._confirm_authorizations_http_info(request)
        return self._call_api(**http_info)

    def confirm_authorizations_async_invoker(self, request):
        http_info = self._confirm_authorizations_http_info(request)
        return AsyncInvoker(self, http_info)

    def _confirm_authorizations_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/servicerequest/authorizations/{authorization_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ConfirmAuthorizationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'authorization_id' in local_var_params:
            path_params['authorization_id'] = local_var_params['authorization_id']

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def create_ask_question_async(self, request):
        """语料提问

        基于语料的一次问答
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAskQuestion
        :type request: :class:`huaweicloudsdkosm.v2.CreateAskQuestionRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CreateAskQuestionResponse`
        """
        http_info = self._create_ask_question_http_info(request)
        return self._call_api(**http_info)

    def create_ask_question_async_invoker(self, request):
        http_info = self._create_ask_question_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_ask_question_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/irobot/qapairs/ask",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAskQuestionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_service_key' in local_var_params:
            header_params['x-service-key'] = local_var_params['x_service_key']
        if 'x_site' in local_var_params:
            header_params['x-site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

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

    def create_case_extends_param_async(self, request):
        """提交工单扩展参数

        提交工单扩展参数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCaseExtendsParam
        :type request: :class:`huaweicloudsdkosm.v2.CreateCaseExtendsParamRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CreateCaseExtendsParamResponse`
        """
        http_info = self._create_case_extends_param_http_info(request)
        return self._call_api(**http_info)

    def create_case_extends_param_async_invoker(self, request):
        http_info = self._create_case_extends_param_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_case_extends_param_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/servicerequest/cases/{case_id}/extends-param",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCaseExtendsParamResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def create_case_labels_async(self, request):
        """添加工单关联标签接口

        添加工单关联标签接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCaseLabels
        :type request: :class:`huaweicloudsdkosm.v2.CreateCaseLabelsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CreateCaseLabelsResponse`
        """
        http_info = self._create_case_labels_http_info(request)
        return self._call_api(**http_info)

    def create_case_labels_async_invoker(self, request):
        http_info = self._create_case_labels_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_case_labels_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/servicerequest/cases/{case_id}/labels",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCaseLabelsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']

        query_params = []
        if 'label_ids' in local_var_params:
            query_params.append(('label_ids', local_var_params['label_ids']))
            collection_formats['label_ids'] = 'csv'

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def create_cases_async(self, request):
        """创建工单

        创建工单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCases
        :type request: :class:`huaweicloudsdkosm.v2.CreateCasesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CreateCasesResponse`
        """
        http_info = self._create_cases_http_info(request)
        return self._call_api(**http_info)

    def create_cases_async_invoker(self, request):
        http_info = self._create_cases_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_cases_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/servicerequest/cases",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCasesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']
        if 'x_phone_verifiedid' in local_var_params:
            header_params['x-phone-verifiedid'] = local_var_params['x_phone_verifiedid']
        if 'x_email_verifiedid' in local_var_params:
            header_params['x-email-verifiedid'] = local_var_params['x_email_verifiedid']

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

    def create_diagnose_feedback_async(self, request):
        """用户反馈是否有帮助

        用户反馈是否有帮助
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDiagnoseFeedback
        :type request: :class:`huaweicloudsdkosm.v2.CreateDiagnoseFeedbackRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CreateDiagnoseFeedbackResponse`
        """
        http_info = self._create_diagnose_feedback_http_info(request)
        return self._call_api(**http_info)

    def create_diagnose_feedback_async_invoker(self, request):
        http_info = self._create_diagnose_feedback_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_diagnose_feedback_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/servicerequest/diagnose/feedback",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDiagnoseFeedbackResponse"
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

    def create_diagnose_job_async(self, request):
        """开始一键诊断

        开始一键诊断
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDiagnoseJob
        :type request: :class:`huaweicloudsdkosm.v2.CreateDiagnoseJobRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CreateDiagnoseJobResponse`
        """
        http_info = self._create_diagnose_job_http_info(request)
        return self._call_api(**http_info)

    def create_diagnose_job_async_invoker(self, request):
        http_info = self._create_diagnose_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_diagnose_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/servicerequest/diagnose/job/start",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDiagnoseJobResponse"
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

    def create_evaluate_async(self, request):
        """问答满意度评价

        一次问答完毕后, 针对这一次问答提交满意度评价
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEvaluate
        :type request: :class:`huaweicloudsdkosm.v2.CreateEvaluateRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CreateEvaluateResponse`
        """
        http_info = self._create_evaluate_http_info(request)
        return self._call_api(**http_info)

    def create_evaluate_async_invoker(self, request):
        http_info = self._create_evaluate_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_evaluate_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/irobot/sessions/{session_id}/{request_id}/evaluate",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEvaluateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'session_id' in local_var_params:
            path_params['session_id'] = local_var_params['session_id']
        if 'request_id' in local_var_params:
            path_params['request_id'] = local_var_params['request_id']

        query_params = []

        header_params = {}
        if 'x_service_key' in local_var_params:
            header_params['x-service-key'] = local_var_params['x_service_key']
        if 'x_site' in local_var_params:
            header_params['x-site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

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

    def create_feedback_async(self, request):
        """创建举报反馈

        创建举报反馈
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateFeedback
        :type request: :class:`huaweicloudsdkosm.v2.CreateFeedbackRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CreateFeedbackResponse`
        """
        http_info = self._create_feedback_http_info(request)
        return self._call_api(**http_info)

    def create_feedback_async_invoker(self, request):
        http_info = self._create_feedback_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_feedback_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/servicerequest/feedbacks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFeedbackResponse"
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

    def create_labels_async(self, request):
        """创建标签

        创建标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateLabels
        :type request: :class:`huaweicloudsdkosm.v2.CreateLabelsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CreateLabelsResponse`
        """
        http_info = self._create_labels_http_info(request)
        return self._call_api(**http_info)

    def create_labels_async_invoker(self, request):
        http_info = self._create_labels_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_labels_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/servicerequest/labels",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLabelsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def create_messages_async(self, request):
        """提交留言

        提交留言
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMessages
        :type request: :class:`huaweicloudsdkosm.v2.CreateMessagesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CreateMessagesResponse`
        """
        http_info = self._create_messages_http_info(request)
        return self._call_api(**http_info)

    def create_messages_async_invoker(self, request):
        http_info = self._create_messages_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_messages_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/servicerequest/cases/{case_id}/message",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMessagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def create_privileges_async(self, request):
        """创建授权

        创建授权
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePrivileges
        :type request: :class:`huaweicloudsdkosm.v2.CreatePrivilegesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CreatePrivilegesResponse`
        """
        http_info = self._create_privileges_http_info(request)
        return self._call_api(**http_info)

    def create_privileges_async_invoker(self, request):
        http_info = self._create_privileges_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_privileges_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/servicerequest/privileges",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePrivilegesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def create_qa_ask_async(self, request):
        """新问答接口

        支持多轮流程问答接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateQaAsk
        :type request: :class:`huaweicloudsdkosm.v2.CreateQaAskRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CreateQaAskResponse`
        """
        http_info = self._create_qa_ask_http_info(request)
        return self._call_api(**http_info)

    def create_qa_ask_async_invoker(self, request):
        http_info = self._create_qa_ask_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_qa_ask_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/irobot/ask",
            "request_type": request.__class__.__name__,
            "response_type": "CreateQaAskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_service_key' in local_var_params:
            header_params['x-service-key'] = local_var_params['x_service_key']
        if 'x_site' in local_var_params:
            header_params['x-site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

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

    def create_qa_feedbacks_async(self, request):
        """反馈评价

        提交/取消反馈评价
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateQaFeedbacks
        :type request: :class:`huaweicloudsdkosm.v2.CreateQaFeedbacksRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CreateQaFeedbacksResponse`
        """
        http_info = self._create_qa_feedbacks_http_info(request)
        return self._call_api(**http_info)

    def create_qa_feedbacks_async_invoker(self, request):
        http_info = self._create_qa_feedbacks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_qa_feedbacks_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/irobot/feedbacks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateQaFeedbacksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'feedback_type' in local_var_params:
            query_params.append(('feedback_type', local_var_params['feedback_type']))

        header_params = {}
        if 'x_service_key' in local_var_params:
            header_params['x-service-key'] = local_var_params['x_service_key']
        if 'x_site' in local_var_params:
            header_params['x-site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

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

    def create_question_in_session_async(self, request):
        """提问（在制定的会话中）

        提问（在制定的会话中）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateQuestionInSession
        :type request: :class:`huaweicloudsdkosm.v2.CreateQuestionInSessionRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CreateQuestionInSessionResponse`
        """
        http_info = self._create_question_in_session_http_info(request)
        return self._call_api(**http_info)

    def create_question_in_session_async_invoker(self, request):
        http_info = self._create_question_in_session_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_question_in_session_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/irobot/sessions/{session_id}/ask",
            "request_type": request.__class__.__name__,
            "response_type": "CreateQuestionInSessionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'session_id' in local_var_params:
            path_params['session_id'] = local_var_params['session_id']

        query_params = []

        header_params = {}
        if 'x_service_key' in local_var_params:
            header_params['x-service-key'] = local_var_params['x_service_key']
        if 'x_site' in local_var_params:
            header_params['x-site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

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

    def create_relations_async(self, request):
        """创建关联

        创建关联，一个工单最多支持3个关联
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRelations
        :type request: :class:`huaweicloudsdkosm.v2.CreateRelationsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CreateRelationsResponse`
        """
        http_info = self._create_relations_http_info(request)
        return self._call_api(**http_info)

    def create_relations_async_invoker(self, request):
        http_info = self._create_relations_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_relations_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/servicerequest/cases/{case_id}/relations",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRelationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def create_scores_async(self, request):
        """提交评分

        提交评分
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateScores
        :type request: :class:`huaweicloudsdkosm.v2.CreateScoresRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CreateScoresResponse`
        """
        http_info = self._create_scores_http_info(request)
        return self._call_api(**http_info)

    def create_scores_async_invoker(self, request):
        http_info = self._create_scores_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_scores_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/servicerequest/cases/{case_id}/score",
            "request_type": request.__class__.__name__,
            "response_type": "CreateScoresResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def create_session_async(self, request):
        """创建问答会话

        用于创建问答会话, 创建会话后可开始问答
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSession
        :type request: :class:`huaweicloudsdkosm.v2.CreateSessionRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CreateSessionResponse`
        """
        http_info = self._create_session_http_info(request)
        return self._call_api(**http_info)

    def create_session_async_invoker(self, request):
        http_info = self._create_session_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_session_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/irobot/sessions",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSessionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_service_key' in local_var_params:
            header_params['x-service-key'] = local_var_params['x_service_key']
        if 'x_site' in local_var_params:
            header_params['x-site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

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

    def delete_accessories_async(self, request):
        """删除附件

        删除附件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAccessories
        :type request: :class:`huaweicloudsdkosm.v2.DeleteAccessoriesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.DeleteAccessoriesResponse`
        """
        http_info = self._delete_accessories_http_info(request)
        return self._call_api(**http_info)

    def delete_accessories_async_invoker(self, request):
        http_info = self._delete_accessories_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_accessories_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/servicerequest/accessorys/{accessory_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAccessoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'accessory_id' in local_var_params:
            path_params['accessory_id'] = local_var_params['accessory_id']

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def delete_case_labels_async(self, request):
        """删除工单关联标签接口

        删除指定工单关联标签接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCaseLabels
        :type request: :class:`huaweicloudsdkosm.v2.DeleteCaseLabelsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.DeleteCaseLabelsResponse`
        """
        http_info = self._delete_case_labels_http_info(request)
        return self._call_api(**http_info)

    def delete_case_labels_async_invoker(self, request):
        http_info = self._delete_case_labels_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_case_labels_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/servicerequest/cases/{case_id}/labels",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCaseLabelsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']

        query_params = []
        if 'label_ids' in local_var_params:
            query_params.append(('label_ids', local_var_params['label_ids']))
            collection_formats['label_ids'] = 'csv'

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def delete_labels_async(self, request):
        """删除标签

        删除标签，同时会删除工单与标签关联关系
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteLabels
        :type request: :class:`huaweicloudsdkosm.v2.DeleteLabelsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.DeleteLabelsResponse`
        """
        http_info = self._delete_labels_http_info(request)
        return self._call_api(**http_info)

    def delete_labels_async_invoker(self, request):
        http_info = self._delete_labels_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_labels_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/servicerequest/labels/{label_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLabelsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'label_id' in local_var_params:
            path_params['label_id'] = local_var_params['label_id']

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def delete_relation_async(self, request):
        """删除关联

        删除关联
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRelation
        :type request: :class:`huaweicloudsdkosm.v2.DeleteRelationRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.DeleteRelationResponse`
        """
        http_info = self._delete_relation_http_info(request)
        return self._call_api(**http_info)

    def delete_relation_async_invoker(self, request):
        http_info = self._delete_relation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_relation_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/servicerequest/cases/{case_id}/relations",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRelationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def download_accessories_async(self, request):
        """下载附件

        下载附件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadAccessories
        :type request: :class:`huaweicloudsdkosm.v2.DownloadAccessoriesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.DownloadAccessoriesResponse`
        """
        http_info = self._download_accessories_http_info(request)
        return self._call_api(**http_info)

    def download_accessories_async_invoker(self, request):
        http_info = self._download_accessories_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_accessories_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/accessorys/{accessory_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadAccessoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'accessory_id' in local_var_params:
            path_params['accessory_id'] = local_var_params['accessory_id']

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def download_cases_async(self, request):
        """工单导出

        工单导出
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadCases
        :type request: :class:`huaweicloudsdkosm.v2.DownloadCasesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.DownloadCasesResponse`
        """
        http_info = self._download_cases_http_info(request)
        return self._call_api(**http_info)

    def download_cases_async_invoker(self, request):
        http_info = self._download_cases_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_cases_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/cases/export",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadCasesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'language' in local_var_params:
            query_params.append(('language', local_var_params['language']))
        if 'timezone' in local_var_params:
            query_params.append(('timezone', local_var_params['timezone']))
        if 'incident_id' in local_var_params:
            query_params.append(('incident_id', local_var_params['incident_id']))
        if 'query_start_time' in local_var_params:
            query_params.append(('query_start_time', local_var_params['query_start_time']))
        if 'query_end_time' in local_var_params:
            query_params.append(('query_end_time', local_var_params['query_end_time']))
        if 'x_customer_name' in local_var_params:
            query_params.append(('x_customer_name', local_var_params['x_customer_name']))
        if 'search_key' in local_var_params:
            query_params.append(('search_key', local_var_params['search_key']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'customer_id' in local_var_params:
            query_params.append(('customer_id', local_var_params['customer_id']))
        if 'tenant_source_id_list' in local_var_params:
            query_params.append(('tenant_source_id_list', local_var_params['tenant_source_id_list']))
            collection_formats['tenant_source_id_list'] = 'csv'
        if 'sub_customer_id' in local_var_params:
            query_params.append(('sub_customer_id', local_var_params['sub_customer_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def download_images_async(self, request):
        """图片展示

        返回图片内容，用于页面直接展示
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadImages
        :type request: :class:`huaweicloudsdkosm.v2.DownloadImagesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.DownloadImagesResponse`
        """
        http_info = self._download_images_http_info(request)
        return self._call_api(**http_info)

    def download_images_async_invoker(self, request):
        http_info = self._download_images_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_images_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/accessorys/{accessory_id}/image",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadImagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'accessory_id' in local_var_params:
            path_params['accessory_id'] = local_var_params['accessory_id']

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_accessory_access_urls_async(self, request):
        """租户批量获取下载链接

        租户批量获取下载链接
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAccessoryAccessUrls
        :type request: :class:`huaweicloudsdkosm.v2.ListAccessoryAccessUrlsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListAccessoryAccessUrlsResponse`
        """
        http_info = self._list_accessory_access_urls_http_info(request)
        return self._call_api(**http_info)

    def list_accessory_access_urls_async_invoker(self, request):
        http_info = self._list_accessory_access_urls_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_accessory_access_urls_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/accessorys/access-urls",
            "request_type": request.__class__.__name__,
            "response_type": "ListAccessoryAccessUrlsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'accessory_ids' in local_var_params:
            query_params.append(('accessory_ids', local_var_params['accessory_ids']))
            collection_formats['accessory_ids'] = 'csv'

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_agencies_async(self, request):
        """查询委托

        查询委托
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAgencies
        :type request: :class:`huaweicloudsdkosm.v2.ListAgenciesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListAgenciesResponse`
        """
        http_info = self._list_agencies_http_info(request)
        return self._call_api(**http_info)

    def list_agencies_async_invoker(self, request):
        http_info = self._list_agencies_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_agencies_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/agencies",
            "request_type": request.__class__.__name__,
            "response_type": "ListAgenciesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_area_codes_async(self, request):
        """查询国家码

        查询国家码，用于提交工单页面填写联系方式使用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAreaCodes
        :type request: :class:`huaweicloudsdkosm.v2.ListAreaCodesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListAreaCodesResponse`
        """
        http_info = self._list_area_codes_http_info(request)
        return self._call_api(**http_info)

    def list_area_codes_async_invoker(self, request):
        http_info = self._list_area_codes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_area_codes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/config/area-codes",
            "request_type": request.__class__.__name__,
            "response_type": "ListAreaCodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_articles_async(self, request):
        """查询案例

        查询满足指定条件的案例列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListArticles
        :type request: :class:`huaweicloudsdkosm.v2.ListArticlesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListArticlesResponse`
        """
        http_info = self._list_articles_http_info(request)
        return self._call_api(**http_info)

    def list_articles_async_invoker(self, request):
        http_info = self._list_articles_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_articles_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/irobot/articles/search",
            "request_type": request.__class__.__name__,
            "response_type": "ListArticlesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search_type' in local_var_params:
            query_params.append(('search_type', local_var_params['search_type']))

        header_params = {}
        if 'x_service_key' in local_var_params:
            header_params['x-service-key'] = local_var_params['x_service_key']
        if 'x_site' in local_var_params:
            header_params['x-site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

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

    def list_authorizations_async(self, request):
        """查看授权列表

        查询授权列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAuthorizations
        :type request: :class:`huaweicloudsdkosm.v2.ListAuthorizationsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListAuthorizationsResponse`
        """
        http_info = self._list_authorizations_http_info(request)
        return self._call_api(**http_info)

    def list_authorizations_async_invoker(self, request):
        http_info = self._list_authorizations_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_authorizations_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/authorizations",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuthorizationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sub_customer_name' in local_var_params:
            query_params.append(('sub_customer_name', local_var_params['sub_customer_name']))
        if 'incident_id' in local_var_params:
            query_params.append(('incident_id', local_var_params['incident_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'simple_description' in local_var_params:
            query_params.append(('simple_description', local_var_params['simple_description']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_case_categories_async(self, request):
        """查询工单类目列表

        查询工单类目列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCaseCategories
        :type request: :class:`huaweicloudsdkosm.v2.ListCaseCategoriesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListCaseCategoriesResponse`
        """
        http_info = self._list_case_categories_http_info(request)
        return self._call_api(**http_info)

    def list_case_categories_async_invoker(self, request):
        http_info = self._list_case_categories_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_case_categories_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/config/categories",
            "request_type": request.__class__.__name__,
            "response_type": "ListCaseCategoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_case_cc_emails_async(self, request):
        """查询工单抄送邮箱

        查询工单抄送邮箱
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCaseCcEmails
        :type request: :class:`huaweicloudsdkosm.v2.ListCaseCcEmailsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListCaseCcEmailsResponse`
        """
        http_info = self._list_case_cc_emails_http_info(request)
        return self._call_api(**http_info)

    def list_case_cc_emails_async_invoker(self, request):
        http_info = self._list_case_cc_emails_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_case_cc_emails_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/carbon-copy-emails",
            "request_type": request.__class__.__name__,
            "response_type": "ListCaseCcEmailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_case_counts_async(self, request):
        """统计各状态工单数量

        统计各状态工单数量
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCaseCounts
        :type request: :class:`huaweicloudsdkosm.v2.ListCaseCountsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListCaseCountsResponse`
        """
        http_info = self._list_case_counts_http_info(request)
        return self._call_api(**http_info)

    def list_case_counts_async_invoker(self, request):
        http_info = self._list_case_counts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_case_counts_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/cases/count",
            "request_type": request.__class__.__name__,
            "response_type": "ListCaseCountsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_case_labels_async(self, request):
        """查询工单关联标签接口

        查询工单关联标签接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCaseLabels
        :type request: :class:`huaweicloudsdkosm.v2.ListCaseLabelsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListCaseLabelsResponse`
        """
        http_info = self._list_case_labels_http_info(request)
        return self._call_api(**http_info)

    def list_case_labels_async_invoker(self, request):
        http_info = self._list_case_labels_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_case_labels_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/cases/{case_id}/labels",
            "request_type": request.__class__.__name__,
            "response_type": "ListCaseLabelsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_case_limits_async(self, request):
        """查询工单限制，比如抄送邮箱个数等

        查询工单限制，比如抄送邮箱个数等
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCaseLimits
        :type request: :class:`huaweicloudsdkosm.v2.ListCaseLimitsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListCaseLimitsResponse`
        """
        http_info = self._list_case_limits_http_info(request)
        return self._call_api(**http_info)

    def list_case_limits_async_invoker(self, request):
        http_info = self._list_case_limits_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_case_limits_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/config/limits",
            "request_type": request.__class__.__name__,
            "response_type": "ListCaseLimitsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_case_operate_logs_async(self, request):
        """查询工单操作日志

        查询工单操作日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCaseOperateLogs
        :type request: :class:`huaweicloudsdkosm.v2.ListCaseOperateLogsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListCaseOperateLogsResponse`
        """
        http_info = self._list_case_operate_logs_http_info(request)
        return self._call_api(**http_info)

    def list_case_operate_logs_async_invoker(self, request):
        http_info = self._list_case_operate_logs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_case_operate_logs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/cases/{case_id}/operate-logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListCaseOperateLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_case_quotas_async(self, request):
        """查询工单配额

        查询工单配额
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCaseQuotas
        :type request: :class:`huaweicloudsdkosm.v2.ListCaseQuotasRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListCaseQuotasResponse`
        """
        http_info = self._list_case_quotas_http_info(request)
        return self._call_api(**http_info)

    def list_case_quotas_async_invoker(self, request):
        http_info = self._list_case_quotas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_case_quotas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ListCaseQuotasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_category_id' in local_var_params:
            query_params.append(('product_category_id', local_var_params['product_category_id']))
        if 'business_type_id' in local_var_params:
            query_params.append(('business_type_id', local_var_params['business_type_id']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_case_templates_async(self, request):
        """查询问题类型对应模板

        查询问题类型对应模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCaseTemplates
        :type request: :class:`huaweicloudsdkosm.v2.ListCaseTemplatesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListCaseTemplatesResponse`
        """
        http_info = self._list_case_templates_http_info(request)
        return self._call_api(**http_info)

    def list_case_templates_async_invoker(self, request):
        http_info = self._list_case_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_case_templates_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/config/templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListCaseTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'business_type_id' in local_var_params:
            query_params.append(('business_type_id', local_var_params['business_type_id']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_cases_async(self, request):
        """查询工单列表接口

        查询工单列表接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCases
        :type request: :class:`huaweicloudsdkosm.v2.ListCasesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListCasesResponse`
        """
        http_info = self._list_cases_http_info(request)
        return self._call_api(**http_info)

    def list_cases_async_invoker(self, request):
        http_info = self._list_cases_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cases_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/cases",
            "request_type": request.__class__.__name__,
            "response_type": "ListCasesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search_key' in local_var_params:
            query_params.append(('search_key', local_var_params['search_key']))
            collection_formats['search_key'] = 'csv'
        if 'label_id_list' in local_var_params:
            query_params.append(('label_id_list', local_var_params['label_id_list']))
            collection_formats['label_id_list'] = 'csv'
        if 'app_key' in local_var_params:
            query_params.append(('app_key', local_var_params['app_key']))
        if 'incident_id' in local_var_params:
            query_params.append(('incident_id', local_var_params['incident_id']))
        if 'query_start_time' in local_var_params:
            query_params.append(('query_start_time', local_var_params['query_start_time']))
        if 'query_end_time' in local_var_params:
            query_params.append(('query_end_time', local_var_params['query_end_time']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'incident_status' in local_var_params:
            query_params.append(('incident_status', local_var_params['incident_status']))
        if 'x_customer_id' in local_var_params:
            query_params.append(('x_customer_id', local_var_params['x_customer_id']))
        if 'x_customer_name' in local_var_params:
            query_params.append(('x_customer_name', local_var_params['x_customer_name']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_customers_regions_async(self, request):
        """查询用户关联的region

        查询用户关联的region
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCustomersRegions
        :type request: :class:`huaweicloudsdkosm.v2.ListCustomersRegionsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListCustomersRegionsResponse`
        """
        http_info = self._list_customers_regions_http_info(request)
        return self._call_api(**http_info)

    def list_customers_regions_async_invoker(self, request):
        http_info = self._list_customers_regions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_customers_regions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/customers/regions",
            "request_type": request.__class__.__name__,
            "response_type": "ListCustomersRegionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_diagnose_items_async(self, request):
        """根据itemIds查询指定的诊断检查项执行结果

        根据itemIds查询指定的诊断检查项执行结果
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDiagnoseItems
        :type request: :class:`huaweicloudsdkosm.v2.ListDiagnoseItemsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListDiagnoseItemsResponse`
        """
        http_info = self._list_diagnose_items_http_info(request)
        return self._call_api(**http_info)

    def list_diagnose_items_async_invoker(self, request):
        http_info = self._list_diagnose_items_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_diagnose_items_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/servicerequest/diagnose/job/show-items",
            "request_type": request.__class__.__name__,
            "response_type": "ListDiagnoseItemsResponse"
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

    def list_diagnose_job_async(self, request):
        """查询诊断任务执行结果

        查询诊断任务执行结果
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDiagnoseJob
        :type request: :class:`huaweicloudsdkosm.v2.ListDiagnoseJobRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListDiagnoseJobResponse`
        """
        http_info = self._list_diagnose_job_http_info(request)
        return self._call_api(**http_info)

    def list_diagnose_job_async_invoker(self, request):
        http_info = self._list_diagnose_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_diagnose_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/servicerequest/diagnose/job",
            "request_type": request.__class__.__name__,
            "response_type": "ListDiagnoseJobResponse"
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

    def list_diagnose_records_async(self, request):
        """查询诊断历史记录列表

        查询诊断历史记录列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDiagnoseRecords
        :type request: :class:`huaweicloudsdkosm.v2.ListDiagnoseRecordsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListDiagnoseRecordsResponse`
        """
        http_info = self._list_diagnose_records_http_info(request)
        return self._call_api(**http_info)

    def list_diagnose_records_async_invoker(self, request):
        http_info = self._list_diagnose_records_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_diagnose_records_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/servicerequest/diagnose/records",
            "request_type": request.__class__.__name__,
            "response_type": "ListDiagnoseRecordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'page_no' in local_var_params:
            query_params.append(('page_no', local_var_params['page_no']))
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

    def list_diagnose_resources_async(self, request):
        """获取资源信息

        获取资源信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDiagnoseResources
        :type request: :class:`huaweicloudsdkosm.v2.ListDiagnoseResourcesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListDiagnoseResourcesResponse`
        """
        http_info = self._list_diagnose_resources_http_info(request)
        return self._call_api(**http_info)

    def list_diagnose_resources_async_invoker(self, request):
        http_info = self._list_diagnose_resources_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_diagnose_resources_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/servicerequest/diagnose/job/vm/resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListDiagnoseResourcesResponse"
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

    def list_extends_params_async(self, request):
        """查询附加参数

        提单时，根据不同的产品或者问题类型，会存在不同的一些附加参数填写
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListExtendsParams
        :type request: :class:`huaweicloudsdkosm.v2.ListExtendsParamsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListExtendsParamsResponse`
        """
        http_info = self._list_extends_params_http_info(request)
        return self._call_api(**http_info)

    def list_extends_params_async_invoker(self, request):
        http_info = self._list_extends_params_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_extends_params_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/config/extends-map",
            "request_type": request.__class__.__name__,
            "response_type": "ListExtendsParamsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'business_type_id' in local_var_params:
            query_params.append(('business_type_id', local_var_params['business_type_id']))
        if 'incident_sub_type_id' in local_var_params:
            query_params.append(('incident_sub_type_id', local_var_params['incident_sub_type_id']))
        if 'product_category_id' in local_var_params:
            query_params.append(('product_category_id', local_var_params['product_category_id']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_feedback_option_async(self, request):
        """查询反馈选项

        查询符合条件的反馈选项
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFeedbackOption
        :type request: :class:`huaweicloudsdkosm.v2.ListFeedbackOptionRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListFeedbackOptionResponse`
        """
        http_info = self._list_feedback_option_http_info(request)
        return self._call_api(**http_info)

    def list_feedback_option_async_invoker(self, request):
        http_info = self._list_feedback_option_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_feedback_option_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/irobot/feedbacks/options",
            "request_type": request.__class__.__name__,
            "response_type": "ListFeedbackOptionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'feedback_source' in local_var_params:
            query_params.append(('feedback_source', local_var_params['feedback_source']))

        header_params = {}
        if 'x_service_key' in local_var_params:
            header_params['x-service-key'] = local_var_params['x_service_key']
        if 'x_site' in local_var_params:
            header_params['x-site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

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

    def list_has_verified_contacts_async(self, request):
        """查询已验证的列表

        查询已验证的列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHasVerifiedContacts
        :type request: :class:`huaweicloudsdkosm.v2.ListHasVerifiedContactsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListHasVerifiedContactsResponse`
        """
        http_info = self._list_has_verified_contacts_http_info(request)
        return self._call_api(**http_info)

    def list_has_verified_contacts_async_invoker(self, request):
        http_info = self._list_has_verified_contacts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_has_verified_contacts_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/verifycodes/has-verified",
            "request_type": request.__class__.__name__,
            "response_type": "ListHasVerifiedContactsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'contact_way' in local_var_params:
            query_params.append(('contact_way', local_var_params['contact_way']))
        if 'customer_id' in local_var_params:
            query_params.append(('customer_id', local_var_params['customer_id']))
        if 'sub_customer_id' in local_var_params:
            query_params.append(('sub_customer_id', local_var_params['sub_customer_id']))
        if 'expired_time' in local_var_params:
            query_params.append(('expired_time', local_var_params['expired_time']))
        if 'verified_id' in local_var_params:
            query_params.append(('verified_id', local_var_params['verified_id']))
        if 'contact_value' in local_var_params:
            query_params.append(('contact_value', local_var_params['contact_value']))
        if 'area_code' in local_var_params:
            query_params.append(('area_code', local_var_params['area_code']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_history_operate_logs_async(self, request):
        """查询堡垒机历史操作记录

        查询堡垒机历史操作记录
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHistoryOperateLogs
        :type request: :class:`huaweicloudsdkosm.v2.ListHistoryOperateLogsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListHistoryOperateLogsResponse`
        """
        http_info = self._list_history_operate_logs_http_info(request)
        return self._call_api(**http_info)

    def list_history_operate_logs_async_invoker(self, request):
        http_info = self._list_history_operate_logs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_history_operate_logs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/authorizations/{authorization_id}/authorization-details/{authorization_detail_id}/sessions/{session_id}/operation-logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListHistoryOperateLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'authorization_id' in local_var_params:
            path_params['authorization_id'] = local_var_params['authorization_id']
        if 'authorization_detail_id' in local_var_params:
            path_params['authorization_detail_id'] = local_var_params['authorization_detail_id']
        if 'session_id' in local_var_params:
            path_params['session_id'] = local_var_params['session_id']

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_history_sessions_async(self, request):
        """查询堡垒机历史会话列表

        查询堡垒机历史会话列
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHistorySessions
        :type request: :class:`huaweicloudsdkosm.v2.ListHistorySessionsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListHistorySessionsResponse`
        """
        http_info = self._list_history_sessions_http_info(request)
        return self._call_api(**http_info)

    def list_history_sessions_async_invoker(self, request):
        http_info = self._list_history_sessions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_history_sessions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/authorizations/{authorization_id}/authorization-details/{authorization_detail_id}/history-sessions",
            "request_type": request.__class__.__name__,
            "response_type": "ListHistorySessionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'authorization_id' in local_var_params:
            path_params['authorization_id'] = local_var_params['authorization_id']
        if 'authorization_detail_id' in local_var_params:
            path_params['authorization_detail_id'] = local_var_params['authorization_detail_id']

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_labels_async(self, request):
        """查询标签

        查询标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLabels
        :type request: :class:`huaweicloudsdkosm.v2.ListLabelsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListLabelsResponse`
        """
        http_info = self._list_labels_http_info(request)
        return self._call_api(**http_info)

    def list_labels_async_invoker(self, request):
        http_info = self._list_labels_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_labels_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/labels",
            "request_type": request.__class__.__name__,
            "response_type": "ListLabelsResponse"
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
        if 'label_id' in local_var_params:
            query_params.append(('label_id', local_var_params['label_id']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_messages_async(self, request):
        """查询留言

        查询留言
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMessages
        :type request: :class:`huaweicloudsdkosm.v2.ListMessagesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListMessagesResponse`
        """
        http_info = self._list_messages_http_info(request)
        return self._call_api(**http_info)

    def list_messages_async_invoker(self, request):
        http_info = self._list_messages_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_messages_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/cases/{case_id}/messages",
            "request_type": request.__class__.__name__,
            "response_type": "ListMessagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_more_instant_messages_async(self, request):
        """查询更多留言

        查询更多留言
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMoreInstantMessages
        :type request: :class:`huaweicloudsdkosm.v2.ListMoreInstantMessagesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListMoreInstantMessagesResponse`
        """
        http_info = self._list_more_instant_messages_http_info(request)
        return self._call_api(**http_info)

    def list_more_instant_messages_async_invoker(self, request):
        http_info = self._list_more_instant_messages_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_more_instant_messages_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/cases/{case_id}/instant-messages/more",
            "request_type": request.__class__.__name__,
            "response_type": "ListMoreInstantMessagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']

        query_params = []
        if 'create_time' in local_var_params:
            query_params.append(('create_time', local_var_params['create_time']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_new_instant_messages_async(self, request):
        """轮询查询即时消息

        轮询查询即时消息接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNewInstantMessages
        :type request: :class:`huaweicloudsdkosm.v2.ListNewInstantMessagesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListNewInstantMessagesResponse`
        """
        http_info = self._list_new_instant_messages_http_info(request)
        return self._call_api(**http_info)

    def list_new_instant_messages_async_invoker(self, request):
        http_info = self._list_new_instant_messages_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_new_instant_messages_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/cases/instant-messages",
            "request_type": request.__class__.__name__,
            "response_type": "ListNewInstantMessagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'case_ids' in local_var_params:
            query_params.append(('case_ids', local_var_params['case_ids']))
            collection_formats['case_ids'] = 'csv'
        if 'last_message_time_id' in local_var_params:
            query_params.append(('last_message_time_id', local_var_params['last_message_time_id']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_notices_async(self, request):
        """查询公告

        查询满足指定条件的公告列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNotices
        :type request: :class:`huaweicloudsdkosm.v2.ListNoticesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListNoticesResponse`
        """
        http_info = self._list_notices_http_info(request)
        return self._call_api(**http_info)

    def list_notices_async_invoker(self, request):
        http_info = self._list_notices_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_notices_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/irobot/notices/search",
            "request_type": request.__class__.__name__,
            "response_type": "ListNoticesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_service_key' in local_var_params:
            header_params['x-service-key'] = local_var_params['x_service_key']
        if 'x_site' in local_var_params:
            header_params['x-site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

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

    def list_order_incident_async(self, request):
        """工单列表

        工单列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOrderIncident
        :type request: :class:`huaweicloudsdkosm.v2.ListOrderIncidentRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListOrderIncidentResponse`
        """
        http_info = self._list_order_incident_http_info(request)
        return self._call_api(**http_info)

    def list_order_incident_async_invoker(self, request):
        http_info = self._list_order_incident_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_order_incident_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/osm/incidentservice/api/v1/queryincident",
            "request_type": request.__class__.__name__,
            "response_type": "ListOrderIncidentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
            collection_formats['searchKey'] = 'multi'
        if 'label_id_list' in local_var_params:
            query_params.append(('labelIdList', local_var_params['label_id_list']))
            collection_formats['labelIdList'] = 'multi'
        if 'app_key' in local_var_params:
            query_params.append(('appKey', local_var_params['app_key']))
        if 'incident_id' in local_var_params:
            query_params.append(('incidentId', local_var_params['incident_id']))
        if 'query_start_time' in local_var_params:
            query_params.append(('queryStartTime', local_var_params['query_start_time']))
        if 'query_end_time' in local_var_params:
            query_params.append(('queryEndTime', local_var_params['query_end_time']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'incident_status' in local_var_params:
            query_params.append(('incidentStatus', local_var_params['incident_status']))
        if 'x_customer_name' in local_var_params:
            query_params.append(('xCustomerName', local_var_params['x_customer_name']))
        if 'group_id' in local_var_params:
            query_params.append(('groupId', local_var_params['group_id']))
        if 'product_category_id' in local_var_params:
            query_params.append(('productCategoryId', local_var_params['product_category_id']))
        if 'business_type_id' in local_var_params:
            query_params.append(('businessTypeId', local_var_params['business_type_id']))
        if 'page_no' in local_var_params:
            query_params.append(('pageNo', local_var_params['page_no']))
        if 'page_size' in local_var_params:
            query_params.append(('pageSize', local_var_params['page_size']))
        if 'x_customer_id' in local_var_params:
            query_params.append(('xCustomerId', local_var_params['x_customer_id']))

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

    def list_privileges_async(self, request):
        """查询工单权限

        查询工单权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPrivileges
        :type request: :class:`huaweicloudsdkosm.v2.ListPrivilegesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListPrivilegesResponse`
        """
        http_info = self._list_privileges_http_info(request)
        return self._call_api(**http_info)

    def list_privileges_async_invoker(self, request):
        http_info = self._list_privileges_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_privileges_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/privileges",
            "request_type": request.__class__.__name__,
            "response_type": "ListPrivilegesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'privilege' in local_var_params:
            query_params.append(('privilege', local_var_params['privilege']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_problem_types_async(self, request):
        """查询问题类型列表

        提交工单时，选择产品类型之后选择对应的问题列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProblemTypes
        :type request: :class:`huaweicloudsdkosm.v2.ListProblemTypesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListProblemTypesResponse`
        """
        http_info = self._list_problem_types_http_info(request)
        return self._call_api(**http_info)

    def list_problem_types_async_invoker(self, request):
        http_info = self._list_problem_types_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_problem_types_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/config/problems",
            "request_type": request.__class__.__name__,
            "response_type": "ListProblemTypesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_category_id' in local_var_params:
            query_params.append(('product_category_id', local_var_params['product_category_id']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_product_categories_async(self, request):
        """查询产品类型列表

        查询产品类型列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProductCategories
        :type request: :class:`huaweicloudsdkosm.v2.ListProductCategoriesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListProductCategoriesResponse`
        """
        http_info = self._list_product_categories_http_info(request)
        return self._call_api(**http_info)

    def list_product_categories_async_invoker(self, request):
        http_info = self._list_product_categories_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_product_categories_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/config/product-categories",
            "request_type": request.__class__.__name__,
            "response_type": "ListProductCategoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_category_name' in local_var_params:
            query_params.append(('product_category_name', local_var_params['product_category_name']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_recommend_words_async(self, request):
        """查询推荐热词

        查询指定条件的推荐热词
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRecommendWords
        :type request: :class:`huaweicloudsdkosm.v2.ListRecommendWordsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListRecommendWordsResponse`
        """
        http_info = self._list_recommend_words_http_info(request)
        return self._call_api(**http_info)

    def list_recommend_words_async_invoker(self, request):
        http_info = self._list_recommend_words_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_recommend_words_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/irobot/recommend-words",
            "request_type": request.__class__.__name__,
            "response_type": "ListRecommendWordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'recommend_word_id' in local_var_params:
            query_params.append(('recommend_word_id', local_var_params['recommend_word_id']))
        if 'level_value' in local_var_params:
            query_params.append(('level_value', local_var_params['level_value']))
        if 'theme_name' in local_var_params:
            query_params.append(('theme_name', local_var_params['theme_name']))

        header_params = {}
        if 'x_service_key' in local_var_params:
            header_params['x-service-key'] = local_var_params['x_service_key']
        if 'x_site' in local_var_params:
            header_params['x-site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

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

    def list_regions_async(self, request):
        """查询区域列表

        查询区域列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRegions
        :type request: :class:`huaweicloudsdkosm.v2.ListRegionsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListRegionsResponse`
        """
        http_info = self._list_regions_http_info(request)
        return self._call_api(**http_info)

    def list_regions_async_invoker(self, request):
        http_info = self._list_regions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_regions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/config/regions",
            "request_type": request.__class__.__name__,
            "response_type": "ListRegionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_relation_async(self, request):
        """查询关联工单

        查询工单的关联，返回关联工单的简要信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRelation
        :type request: :class:`huaweicloudsdkosm.v2.ListRelationRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListRelationResponse`
        """
        http_info = self._list_relation_http_info(request)
        return self._call_api(**http_info)

    def list_relation_async_invoker(self, request):
        http_info = self._list_relation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_relation_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/cases/{case_id}/relations",
            "request_type": request.__class__.__name__,
            "response_type": "ListRelationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_satisfaction_dimensions_async(self, request):
        """工单满意度分类列表

        工单满意度分类列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSatisfactionDimensions
        :type request: :class:`huaweicloudsdkosm.v2.ListSatisfactionDimensionsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListSatisfactionDimensionsResponse`
        """
        http_info = self._list_satisfaction_dimensions_http_info(request)
        return self._call_api(**http_info)

    def list_satisfaction_dimensions_async_invoker(self, request):
        http_info = self._list_satisfaction_dimensions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_satisfaction_dimensions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/config/satisfaction-dimensions",
            "request_type": request.__class__.__name__,
            "response_type": "ListSatisfactionDimensionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_severities_async(self, request):
        """查询问题严重性列表

        查询问题严重性列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSeverities
        :type request: :class:`huaweicloudsdkosm.v2.ListSeveritiesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListSeveritiesResponse`
        """
        http_info = self._list_severities_http_info(request)
        return self._call_api(**http_info)

    def list_severities_async_invoker(self, request):
        http_info = self._list_severities_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_severities_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/config/severities",
            "request_type": request.__class__.__name__,
            "response_type": "ListSeveritiesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_category_id' in local_var_params:
            query_params.append(('product_category_id', local_var_params['product_category_id']))
        if 'business_type_id' in local_var_params:
            query_params.append(('business_type_id', local_var_params['business_type_id']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_sub_customers_async(self, request):
        """查询子用户信息

        查询子用户信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSubCustomers
        :type request: :class:`huaweicloudsdkosm.v2.ListSubCustomersRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListSubCustomersResponse`
        """
        http_info = self._list_sub_customers_http_info(request)
        return self._call_api(**http_info)

    def list_sub_customers_async_invoker(self, request):
        http_info = self._list_sub_customers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_sub_customers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/customers/sub-customers",
            "request_type": request.__class__.__name__,
            "response_type": "ListSubCustomersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sub_customer_name' in local_var_params:
            query_params.append(('sub_customer_name', local_var_params['sub_customer_name']))
        if 'sub_customer_id' in local_var_params:
            query_params.append(('sub_customer_id', local_var_params['sub_customer_id']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_tools_async(self, request):
        """查询工具

        查询满足指定条件的工具列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTools
        :type request: :class:`huaweicloudsdkosm.v2.ListToolsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListToolsResponse`
        """
        http_info = self._list_tools_http_info(request)
        return self._call_api(**http_info)

    def list_tools_async_invoker(self, request):
        http_info = self._list_tools_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tools_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/irobot/tools/search",
            "request_type": request.__class__.__name__,
            "response_type": "ListToolsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_service_key' in local_var_params:
            header_params['x-service-key'] = local_var_params['x_service_key']
        if 'x_site' in local_var_params:
            header_params['x-site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

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

    def list_transport_histories_async(self, request):
        """查询堡垒机文件传输记录

        查询堡垒机文件传输记录
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTransportHistories
        :type request: :class:`huaweicloudsdkosm.v2.ListTransportHistoriesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListTransportHistoriesResponse`
        """
        http_info = self._list_transport_histories_http_info(request)
        return self._call_api(**http_info)

    def list_transport_histories_async_invoker(self, request):
        http_info = self._list_transport_histories_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_transport_histories_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/authorizations/{authorization_id}/authorization-details/{authorization_detail_id}/sessions/{session_id}/operation-file-logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListTransportHistoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'authorization_id' in local_var_params:
            path_params['authorization_id'] = local_var_params['authorization_id']
        if 'authorization_detail_id' in local_var_params:
            path_params['authorization_detail_id'] = local_var_params['authorization_detail_id']
        if 'session_id' in local_var_params:
            path_params['session_id'] = local_var_params['session_id']

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def list_unread_new_instant_messages_async(self, request):
        """查询未读消息

        查询未读消息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUnreadNewInstantMessages
        :type request: :class:`huaweicloudsdkosm.v2.ListUnreadNewInstantMessagesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListUnreadNewInstantMessagesResponse`
        """
        http_info = self._list_unread_new_instant_messages_http_info(request)
        return self._call_api(**http_info)

    def list_unread_new_instant_messages_async_invoker(self, request):
        http_info = self._list_unread_new_instant_messages_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_unread_new_instant_messages_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/cases/instant-messages/unread",
            "request_type": request.__class__.__name__,
            "response_type": "ListUnreadNewInstantMessagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'case_ids' in local_var_params:
            query_params.append(('case_ids', local_var_params['case_ids']))
            collection_formats['case_ids'] = 'csv'
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def revoke_message_async(self, request):
        """撤回留言

        撤回留言
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RevokeMessage
        :type request: :class:`huaweicloudsdkosm.v2.RevokeMessageRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.RevokeMessageResponse`
        """
        http_info = self._revoke_message_http_info(request)
        return self._call_api(**http_info)

    def revoke_message_async_invoker(self, request):
        http_info = self._revoke_message_http_info(request)
        return AsyncInvoker(self, http_info)

    def _revoke_message_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/servicerequest/cases/{case_id}/instant-messages/{message_id}/withdraw",
            "request_type": request.__class__.__name__,
            "response_type": "RevokeMessageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']
        if 'message_id' in local_var_params:
            path_params['message_id'] = local_var_params['message_id']

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def send_verify_codes_async(self, request):
        """获取验证码

        获取验证码
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SendVerifyCodes
        :type request: :class:`huaweicloudsdkosm.v2.SendVerifyCodesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.SendVerifyCodesResponse`
        """
        http_info = self._send_verify_codes_http_info(request)
        return self._call_api(**http_info)

    def send_verify_codes_async_invoker(self, request):
        http_info = self._send_verify_codes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _send_verify_codes_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/servicerequest/verifycodes/send",
            "request_type": request.__class__.__name__,
            "response_type": "SendVerifyCodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def show_accessory_limits_async(self, request):
        """附件限制

        查询附件的一下限制，比如大小，数量，文件类型
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAccessoryLimits
        :type request: :class:`huaweicloudsdkosm.v2.ShowAccessoryLimitsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ShowAccessoryLimitsResponse`
        """
        http_info = self._show_accessory_limits_http_info(request)
        return self._call_api(**http_info)

    def show_accessory_limits_async_invoker(self, request):
        http_info = self._show_accessory_limits_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_accessory_limits_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/accessorys/limits",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAccessoryLimitsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def show_associated_questions_async(self, request):
        """查询联想问题

        根据当前输入, 联想相关的问题
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAssociatedQuestions
        :type request: :class:`huaweicloudsdkosm.v2.ShowAssociatedQuestionsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ShowAssociatedQuestionsResponse`
        """
        http_info = self._show_associated_questions_http_info(request)
        return self._call_api(**http_info)

    def show_associated_questions_async_invoker(self, request):
        http_info = self._show_associated_questions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_associated_questions_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/irobot/qapairs/associate",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAssociatedQuestionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_service_key' in local_var_params:
            header_params['x-service-key'] = local_var_params['x_service_key']
        if 'x_site' in local_var_params:
            header_params['x-site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

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

    def show_authorization_detail_async(self, request):
        """查询授权详情

        查询授权详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAuthorizationDetail
        :type request: :class:`huaweicloudsdkosm.v2.ShowAuthorizationDetailRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ShowAuthorizationDetailResponse`
        """
        http_info = self._show_authorization_detail_http_info(request)
        return self._call_api(**http_info)

    def show_authorization_detail_async_invoker(self, request):
        http_info = self._show_authorization_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_authorization_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/authorizations/{authorization_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuthorizationDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'authorization_id' in local_var_params:
            path_params['authorization_id'] = local_var_params['authorization_id']

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def show_case_detail_async(self, request):
        """查询工单详情

        查询工单详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCaseDetail
        :type request: :class:`huaweicloudsdkosm.v2.ShowCaseDetailRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ShowCaseDetailResponse`
        """
        http_info = self._show_case_detail_http_info(request)
        return self._call_api(**http_info)

    def show_case_detail_async_invoker(self, request):
        http_info = self._show_case_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_case_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/cases/{case_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCaseDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def show_case_extends_param_async(self, request):
        """查询工单扩展参数

        查询工单扩展参数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCaseExtendsParam
        :type request: :class:`huaweicloudsdkosm.v2.ShowCaseExtendsParamRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ShowCaseExtendsParamResponse`
        """
        http_info = self._show_case_extends_param_http_info(request)
        return self._call_api(**http_info)

    def show_case_extends_param_async_invoker(self, request):
        http_info = self._show_case_extends_param_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_case_extends_param_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/cases/{case_id}/extends-param",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCaseExtendsParamResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def show_case_status_async(self, request):
        """查询某个工单状态

        查询某个工单状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCaseStatus
        :type request: :class:`huaweicloudsdkosm.v2.ShowCaseStatusRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ShowCaseStatusResponse`
        """
        http_info = self._show_case_status_http_info(request)
        return self._call_api(**http_info)

    def show_case_status_async_invoker(self, request):
        http_info = self._show_case_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_case_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/cases/{case_id}/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCaseStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def show_configuration_async(self, request):
        """查询配置

        查询配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowConfiguration
        :type request: :class:`huaweicloudsdkosm.v2.ShowConfigurationRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ShowConfigurationResponse`
        """
        http_info = self._show_configuration_http_info(request)
        return self._call_api(**http_info)

    def show_configuration_async_invoker(self, request):
        http_info = self._show_configuration_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_configuration_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/configurations/{config_key}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'config_key' in local_var_params:
            path_params['config_key'] = local_var_params['config_key']

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

    def show_customer_privilege_policy_async(self, request):
        """查询提单权限

        查询提单权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCustomerPrivilegePolicy
        :type request: :class:`huaweicloudsdkosm.v2.ShowCustomerPrivilegePolicyRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ShowCustomerPrivilegePolicyResponse`
        """
        http_info = self._show_customer_privilege_policy_http_info(request)
        return self._call_api(**http_info)

    def show_customer_privilege_policy_async_invoker(self, request):
        http_info = self._show_customer_privilege_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_customer_privilege_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/privileges/privilege-policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCustomerPrivilegePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def show_download_accessory_url_async(self, request):
        """附件下载地址

        附件下载地址
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDownloadAccessoryUrl
        :type request: :class:`huaweicloudsdkosm.v2.ShowDownloadAccessoryUrlRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ShowDownloadAccessoryUrlResponse`
        """
        http_info = self._show_download_accessory_url_http_info(request)
        return self._call_api(**http_info)

    def show_download_accessory_url_async_invoker(self, request):
        http_info = self._show_download_accessory_url_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_download_accessory_url_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/accessorys/{accessory_id}/access-url",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDownloadAccessoryUrlResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'accessory_id' in local_var_params:
            path_params['accessory_id'] = local_var_params['accessory_id']

        query_params = []
        if 'relation_type' in local_var_params:
            query_params.append(('relation_type', local_var_params['relation_type']))
        if 'relation_id' in local_var_params:
            query_params.append(('relation_id', local_var_params['relation_id']))
        if 'incident_id' in local_var_params:
            query_params.append(('incident_id', local_var_params['incident_id']))

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

    def show_latest_published_agreement_async(self, request):
        """查看最新发布版本协议详情

        查看最新发布版本协议详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowLatestPublishedAgreement
        :type request: :class:`huaweicloudsdkosm.v2.ShowLatestPublishedAgreementRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ShowLatestPublishedAgreementResponse`
        """
        http_info = self._show_latest_published_agreement_http_info(request)
        return self._call_api(**http_info)

    def show_latest_published_agreement_async_invoker(self, request):
        http_info = self._show_latest_published_agreement_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_latest_published_agreement_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/agreements/published-agreement",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLatestPublishedAgreementResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'agreement_type' in local_var_params:
            query_params.append(('agreement_type', local_var_params['agreement_type']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def show_login_type_async(self, request):
        """查询登录类型

        查询登录类型
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowLoginType
        :type request: :class:`huaweicloudsdkosm.v2.ShowLoginTypeRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ShowLoginTypeResponse`
        """
        http_info = self._show_login_type_http_info(request)
        return self._call_api(**http_info)

    def show_login_type_async_invoker(self, request):
        http_info = self._show_login_type_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_login_type_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/authorizations/login-type",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLoginTypeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def show_partners_cases_privilege_async(self, request):
        """查询伙伴工单权限

        查询伙伴工单权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPartnersCasesPrivilege
        :type request: :class:`huaweicloudsdkosm.v2.ShowPartnersCasesPrivilegeRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ShowPartnersCasesPrivilegeResponse`
        """
        http_info = self._show_partners_cases_privilege_http_info(request)
        return self._call_api(**http_info)

    def show_partners_cases_privilege_async_invoker(self, request):
        http_info = self._show_partners_cases_privilege_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_partners_cases_privilege_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/cases/partners/privilege/cases-processing",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPartnersCasesPrivilegeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def show_partners_service_info_async(self, request):
        """查询关联伙伴服务信息

        查询关联伙伴服务信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPartnersServiceInfo
        :type request: :class:`huaweicloudsdkosm.v2.ShowPartnersServiceInfoRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ShowPartnersServiceInfoResponse`
        """
        http_info = self._show_partners_service_info_http_info(request)
        return self._call_api(**http_info)

    def show_partners_service_info_async_invoker(self, request):
        http_info = self._show_partners_service_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_partners_service_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/cases/partners/service-info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPartnersServiceInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'case_sub_type_id' in local_var_params:
            query_params.append(('case_sub_type_id', local_var_params['case_sub_type_id']))
        if 'product_id' in local_var_params:
            query_params.append(('product_id', local_var_params['product_id']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def show_qa_pair_detail_async(self, request):
        """查询语料详情

        查询指定语料的详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowQaPairDetail
        :type request: :class:`huaweicloudsdkosm.v2.ShowQaPairDetailRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ShowQaPairDetailResponse`
        """
        http_info = self._show_qa_pair_detail_http_info(request)
        return self._call_api(**http_info)

    def show_qa_pair_detail_async_invoker(self, request):
        http_info = self._show_qa_pair_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_qa_pair_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/irobot/qapairs/{qa_pair_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowQaPairDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'qa_pair_id' in local_var_params:
            path_params['qa_pair_id'] = local_var_params['qa_pair_id']

        query_params = []

        header_params = {}
        if 'x_service_key' in local_var_params:
            header_params['x-service-key'] = local_var_params['x_service_key']
        if 'x_site' in local_var_params:
            header_params['x-site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

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

    def show_qa_pairs_async(self, request):
        """查询语料

        查询满足指定条件的语料列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowQaPairs
        :type request: :class:`huaweicloudsdkosm.v2.ShowQaPairsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ShowQaPairsResponse`
        """
        http_info = self._show_qa_pairs_http_info(request)
        return self._call_api(**http_info)

    def show_qa_pairs_async_invoker(self, request):
        http_info = self._show_qa_pairs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_qa_pairs_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/irobot/qapairs/search",
            "request_type": request.__class__.__name__,
            "response_type": "ShowQaPairsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search_type' in local_var_params:
            query_params.append(('search_type', local_var_params['search_type']))

        header_params = {}
        if 'x_service_key' in local_var_params:
            header_params['x-service-key'] = local_var_params['x_service_key']
        if 'x_site' in local_var_params:
            header_params['x-site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

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

    def show_signed_latest_published_agreement_async(self, request):
        """查询用户是否签署最新协议

        查询用户是否签署最新协议
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSignedLatestPublishedAgreement
        :type request: :class:`huaweicloudsdkosm.v2.ShowSignedLatestPublishedAgreementRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ShowSignedLatestPublishedAgreementResponse`
        """
        http_info = self._show_signed_latest_published_agreement_http_info(request)
        return self._call_api(**http_info)

    def show_signed_latest_published_agreement_async_invoker(self, request):
        http_info = self._show_signed_latest_published_agreement_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_signed_latest_published_agreement_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/servicerequest/agreements/signed-latest",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSignedLatestPublishedAgreementResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'agreement_type' in local_var_params:
            query_params.append(('agreement_type', local_var_params['agreement_type']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def show_theme_async(self, request):
        """产品类型转为主题

        产品类型转为主题
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTheme
        :type request: :class:`huaweicloudsdkosm.v2.ShowThemeRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ShowThemeResponse`
        """
        http_info = self._show_theme_http_info(request)
        return self._call_api(**http_info)

    def show_theme_async_invoker(self, request):
        http_info = self._show_theme_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_theme_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/irobot/themes/convert",
            "request_type": request.__class__.__name__,
            "response_type": "ShowThemeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_type_id' in local_var_params:
            query_params.append(('product_type_id', local_var_params['product_type_id']))
        if 'product_type_name' in local_var_params:
            query_params.append(('product_type_name', local_var_params['product_type_name']))
        if 'product_type_short_name' in local_var_params:
            query_params.append(('product_type_short_name', local_var_params['product_type_short_name']))

        header_params = {}
        if 'x_service_key' in local_var_params:
            header_params['x-service-key'] = local_var_params['x_service_key']
        if 'x_site' in local_var_params:
            header_params['x-site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

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

    def sign_published_agreement_async(self, request):
        """签署协议

        签署协议
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SignPublishedAgreement
        :type request: :class:`huaweicloudsdkosm.v2.SignPublishedAgreementRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.SignPublishedAgreementResponse`
        """
        http_info = self._sign_published_agreement_http_info(request)
        return self._call_api(**http_info)

    def sign_published_agreement_async_invoker(self, request):
        http_info = self._sign_published_agreement_http_info(request)
        return AsyncInvoker(self, http_info)

    def _sign_published_agreement_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/servicerequest/agreements/{id}/signed",
            "request_type": request.__class__.__name__,
            "response_type": "SignPublishedAgreementResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def update_authorizations_async(self, request):
        """拒绝|撤销授权

        拒绝|撤销授权
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAuthorizations
        :type request: :class:`huaweicloudsdkosm.v2.UpdateAuthorizationsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.UpdateAuthorizationsResponse`
        """
        http_info = self._update_authorizations_http_info(request)
        return self._call_api(**http_info)

    def update_authorizations_async_invoker(self, request):
        http_info = self._update_authorizations_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_authorizations_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/servicerequest/authorizations/{authorization_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAuthorizationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'authorization_id' in local_var_params:
            path_params['authorization_id'] = local_var_params['authorization_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def update_case_contact_info_async(self, request):
        """修改联系方式

        修改联系方式
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCaseContactInfo
        :type request: :class:`huaweicloudsdkosm.v2.UpdateCaseContactInfoRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.UpdateCaseContactInfoResponse`
        """
        http_info = self._update_case_contact_info_http_info(request)
        return self._call_api(**http_info)

    def update_case_contact_info_async_invoker(self, request):
        http_info = self._update_case_contact_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_case_contact_info_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/servicerequest/cases/{case_id}/contact-info",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCaseContactInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def update_cases_async(self, request):
        """工单操作

        工单操作
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCases
        :type request: :class:`huaweicloudsdkosm.v2.UpdateCasesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.UpdateCasesResponse`
        """
        http_info = self._update_cases_http_info(request)
        return self._call_api(**http_info)

    def update_cases_async_invoker(self, request):
        http_info = self._update_cases_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_cases_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/servicerequest/cases/{case_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCasesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def update_labels_async(self, request):
        """修改标签

        修改标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateLabels
        :type request: :class:`huaweicloudsdkosm.v2.UpdateLabelsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.UpdateLabelsResponse`
        """
        http_info = self._update_labels_http_info(request)
        return self._call_api(**http_info)

    def update_labels_async_invoker(self, request):
        http_info = self._update_labels_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_labels_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/servicerequest/labels/{label_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLabelsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'label_id' in local_var_params:
            path_params['label_id'] = local_var_params['label_id']

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def update_new_instant_messages_read_async(self, request):
        """设置消息已读

        设置消息已读
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateNewInstantMessagesRead
        :type request: :class:`huaweicloudsdkosm.v2.UpdateNewInstantMessagesReadRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.UpdateNewInstantMessagesReadResponse`
        """
        http_info = self._update_new_instant_messages_read_http_info(request)
        return self._call_api(**http_info)

    def update_new_instant_messages_read_async_invoker(self, request):
        http_info = self._update_new_instant_messages_read_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_new_instant_messages_read_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/servicerequest/cases/{case_id}/instant-messages/unread",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNewInstantMessagesReadResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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

    def upload_json_accessories_async(self, request):
        """上传附件

        上传附件给SDK使用，上传附件需要满足\&quot;附件限制\&quot;返回的关于大小等限制
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UploadJsonAccessories
        :type request: :class:`huaweicloudsdkosm.v2.UploadJsonAccessoriesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.UploadJsonAccessoriesResponse`
        """
        http_info = self._upload_json_accessories_http_info(request)
        return self._call_api(**http_info)

    def upload_json_accessories_async_invoker(self, request):
        http_info = self._upload_json_accessories_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upload_json_accessories_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/servicerequest/accessorys/json-format-content",
            "request_type": request.__class__.__name__,
            "response_type": "UploadJsonAccessoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_site' in local_var_params:
            header_params['X-Site'] = local_var_params['x_site']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_time_zone' in local_var_params:
            header_params['X-Time-Zone'] = local_var_params['x_time_zone']

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
