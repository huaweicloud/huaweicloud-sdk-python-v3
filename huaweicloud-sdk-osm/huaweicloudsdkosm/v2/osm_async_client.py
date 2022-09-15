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


class OsmAsyncClient(Client):
    """
    :param configuration: .Configuration object for this client
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

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
        super(OsmAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkosm.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls, "GlobalCredentials")

        if clazz.__name__ != "OsmClient":
            raise TypeError("client type error, support client type is OsmClient")

        return ClientBuilder(clazz, "GlobalCredentials")

    def check_hosts_async(self, request):
        """验证授权主机

        验证授权主机密码是否正确
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CheckHosts
        :type request: :class:`huaweicloudsdkosm.v2.CheckHostsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CheckHostsResponse`
        """
        return self.check_hosts_with_http_info(request)

    def check_hosts_with_http_info(self, request):
        all_params = ['authorization_detail_id', 'x_site', 'x_language', 'x_time_zone', 'check_hosts_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/servicerequest/authorizations/authorization-details/{authorization_detail_id}/verify-host',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CheckHostsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_need_verify_async(self, request):
        """是否需要验证

        是否需要验证
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CheckNeedVerify
        :type request: :class:`huaweicloudsdkosm.v2.CheckNeedVerifyRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CheckNeedVerifyResponse`
        """
        return self.check_need_verify_with_http_info(request)

    def check_need_verify_with_http_info(self, request):
        all_params = ['contact_value', 'contact_way', 'area_code', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/verifycodes/need-verify',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CheckNeedVerifyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_verify_codes_async(self, request):
        """验证联系方式

        验证联系方式
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CheckVerifyCodes
        :type request: :class:`huaweicloudsdkosm.v2.CheckVerifyCodesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CheckVerifyCodesResponse`
        """
        return self.check_verify_codes_with_http_info(request)

    def check_verify_codes_with_http_info(self, request):
        all_params = ['x_site', 'x_language', 'x_time_zone', 'check_verify_codes_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/servicerequest/verifycodes',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CheckVerifyCodesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def confirm_authorizations_async(self, request):
        """租户确认授权

        租户确认授权
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ConfirmAuthorizations
        :type request: :class:`huaweicloudsdkosm.v2.ConfirmAuthorizationsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ConfirmAuthorizationsResponse`
        """
        return self.confirm_authorizations_with_http_info(request)

    def confirm_authorizations_with_http_info(self, request):
        all_params = ['authorization_id', 'x_site', 'x_language', 'x_time_zone', 'confirm_authorizations_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/servicerequest/authorizations/{authorization_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ConfirmAuthorizationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_case_extends_param_async(self, request):
        """提交工单扩展参数

        提交工单扩展参数
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateCaseExtendsParam
        :type request: :class:`huaweicloudsdkosm.v2.CreateCaseExtendsParamRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CreateCaseExtendsParamResponse`
        """
        return self.create_case_extends_param_with_http_info(request)

    def create_case_extends_param_with_http_info(self, request):
        all_params = ['case_id', 'create_case_extends_param_request_body', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/servicerequest/cases/{case_id}/extends-param',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateCaseExtendsParamResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_case_labels_async(self, request):
        """添加工单关联标签接口

        添加工单关联标签接口
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateCaseLabels
        :type request: :class:`huaweicloudsdkosm.v2.CreateCaseLabelsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CreateCaseLabelsResponse`
        """
        return self.create_case_labels_with_http_info(request)

    def create_case_labels_with_http_info(self, request):
        all_params = ['case_id', 'label_ids', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/cases/{case_id}/labels',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateCaseLabelsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_cases_async(self, request):
        """创建工单

        创建工单
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateCases
        :type request: :class:`huaweicloudsdkosm.v2.CreateCasesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CreateCasesResponse`
        """
        return self.create_cases_with_http_info(request)

    def create_cases_with_http_info(self, request):
        all_params = ['x_site', 'x_language', 'x_time_zone', 'x_phone_verifiedid', 'x_email_verifiedid', 'create_cases_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/servicerequest/cases',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateCasesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_labels_async(self, request):
        """创建标签

        创建标签
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateLabels
        :type request: :class:`huaweicloudsdkosm.v2.CreateLabelsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CreateLabelsResponse`
        """
        return self.create_labels_with_http_info(request)

    def create_labels_with_http_info(self, request):
        all_params = ['create_labels_request_body', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/servicerequest/labels',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateLabelsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_messages_async(self, request):
        """提交留言

        提交留言
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateMessages
        :type request: :class:`huaweicloudsdkosm.v2.CreateMessagesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CreateMessagesResponse`
        """
        return self.create_messages_with_http_info(request)

    def create_messages_with_http_info(self, request):
        all_params = ['case_id', 'x_site', 'x_language', 'x_time_zone', 'create_messages_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/servicerequest/cases/{case_id}/message',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateMessagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_privileges_async(self, request):
        """创建授权

        创建授权
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreatePrivileges
        :type request: :class:`huaweicloudsdkosm.v2.CreatePrivilegesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CreatePrivilegesResponse`
        """
        return self.create_privileges_with_http_info(request)

    def create_privileges_with_http_info(self, request):
        all_params = ['x_site', 'x_language', 'x_time_zone', 'create_privileges_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/servicerequest/privileges',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreatePrivilegesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_relations_async(self, request):
        """创建关联

        创建关联，一个工单最多支持3个关联
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateRelations
        :type request: :class:`huaweicloudsdkosm.v2.CreateRelationsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CreateRelationsResponse`
        """
        return self.create_relations_with_http_info(request)

    def create_relations_with_http_info(self, request):
        all_params = ['case_id', 'create_relations_request_body', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/servicerequest/cases/{case_id}/relations',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateRelationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_scores_async(self, request):
        """提交评分

        提交评分
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateScores
        :type request: :class:`huaweicloudsdkosm.v2.CreateScoresRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.CreateScoresResponse`
        """
        return self.create_scores_with_http_info(request)

    def create_scores_with_http_info(self, request):
        all_params = ['case_id', 'x_site', 'x_language', 'x_time_zone', 'create_scores_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/servicerequest/cases/{case_id}/score',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateScoresResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_accessories_async(self, request):
        """删除附件

        删除附件
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteAccessories
        :type request: :class:`huaweicloudsdkosm.v2.DeleteAccessoriesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.DeleteAccessoriesResponse`
        """
        return self.delete_accessories_with_http_info(request)

    def delete_accessories_with_http_info(self, request):
        all_params = ['accessory_id', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/accessorys/{accessory_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteAccessoriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_case_labels_async(self, request):
        """删除工单关联标签接口

        删除指定工单关联标签接口
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteCaseLabels
        :type request: :class:`huaweicloudsdkosm.v2.DeleteCaseLabelsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.DeleteCaseLabelsResponse`
        """
        return self.delete_case_labels_with_http_info(request)

    def delete_case_labels_with_http_info(self, request):
        all_params = ['case_id', 'label_ids', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/cases/{case_id}/labels',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteCaseLabelsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_labels_async(self, request):
        """删除标签

        删除标签，同时会删除工单与标签关联关系
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteLabels
        :type request: :class:`huaweicloudsdkosm.v2.DeleteLabelsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.DeleteLabelsResponse`
        """
        return self.delete_labels_with_http_info(request)

    def delete_labels_with_http_info(self, request):
        all_params = ['label_id', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/labels/{label_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteLabelsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_relation_async(self, request):
        """删除关联

        删除关联
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteRelation
        :type request: :class:`huaweicloudsdkosm.v2.DeleteRelationRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.DeleteRelationResponse`
        """
        return self.delete_relation_with_http_info(request)

    def delete_relation_with_http_info(self, request):
        all_params = ['case_id', 'delete_relation_request_body', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/servicerequest/cases/{case_id}/relations',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteRelationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def download_accessories_async(self, request):
        """下载附件

        下载附件
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DownloadAccessories
        :type request: :class:`huaweicloudsdkosm.v2.DownloadAccessoriesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.DownloadAccessoriesResponse`
        """
        return self.download_accessories_with_http_info(request)

    def download_accessories_with_http_info(self, request):
        all_params = ['accessory_id', 'group_id', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/accessorys/{accessory_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DownloadAccessoriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def download_cases_async(self, request):
        """工单导出

        工单导出
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DownloadCases
        :type request: :class:`huaweicloudsdkosm.v2.DownloadCasesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.DownloadCasesResponse`
        """
        return self.download_cases_with_http_info(request)

    def download_cases_with_http_info(self, request):
        all_params = ['language', 'timezone', 'incident_id', 'query_start_time', 'query_end_time', 'x_customer_name', 'search_key', 'status', 'customer_id', 'tenant_source_id_list', 'sub_customer_id', 'offset', 'limit', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/cases/export',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DownloadCasesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def download_images_async(self, request):
        """图片展示

        返回图片内容，用于页面直接展示
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DownloadImages
        :type request: :class:`huaweicloudsdkosm.v2.DownloadImagesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.DownloadImagesResponse`
        """
        return self.download_images_with_http_info(request)

    def download_images_with_http_info(self, request):
        all_params = ['accessory_id', 'group_id', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/accessorys/{accessory_id}/image',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DownloadImagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_accessory_access_urls_async(self, request):
        """租户批量获取下载链接

        租户批量获取下载链接
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListAccessoryAccessUrls
        :type request: :class:`huaweicloudsdkosm.v2.ListAccessoryAccessUrlsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListAccessoryAccessUrlsResponse`
        """
        return self.list_accessory_access_urls_with_http_info(request)

    def list_accessory_access_urls_with_http_info(self, request):
        all_params = ['group_id', 'accessory_ids', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/accessorys/access-urls',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAccessoryAccessUrlsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_agencies_async(self, request):
        """查询委托

        查询委托
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListAgencies
        :type request: :class:`huaweicloudsdkosm.v2.ListAgenciesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListAgenciesResponse`
        """
        return self.list_agencies_with_http_info(request)

    def list_agencies_with_http_info(self, request):
        all_params = ['x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/agencies',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAgenciesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_area_codes_async(self, request):
        """查询国家码

        查询国家码，用于提交工单页面填写联系方式使用
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListAreaCodes
        :type request: :class:`huaweicloudsdkosm.v2.ListAreaCodesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListAreaCodesResponse`
        """
        return self.list_area_codes_with_http_info(request)

    def list_area_codes_with_http_info(self, request):
        all_params = ['x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/config/area-codes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAreaCodesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_authorizations_async(self, request):
        """查看授权列表

        查询授权列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListAuthorizations
        :type request: :class:`huaweicloudsdkosm.v2.ListAuthorizationsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListAuthorizationsResponse`
        """
        return self.list_authorizations_with_http_info(request)

    def list_authorizations_with_http_info(self, request):
        all_params = ['sub_customer_name', 'incident_id', 'status', 'simple_description', 'offset', 'limit', 'group_id', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/authorizations',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAuthorizationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_case_categories_async(self, request):
        """查询工单类目列表

        查询工单类目列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListCaseCategories
        :type request: :class:`huaweicloudsdkosm.v2.ListCaseCategoriesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListCaseCategoriesResponse`
        """
        return self.list_case_categories_with_http_info(request)

    def list_case_categories_with_http_info(self, request):
        all_params = ['x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/config/categories',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCaseCategoriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_case_cc_emails_async(self, request):
        """查询工单抄送邮箱

        查询工单抄送邮箱
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListCaseCcEmails
        :type request: :class:`huaweicloudsdkosm.v2.ListCaseCcEmailsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListCaseCcEmailsResponse`
        """
        return self.list_case_cc_emails_with_http_info(request)

    def list_case_cc_emails_with_http_info(self, request):
        all_params = ['x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/carbon-copy-emails',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCaseCcEmailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_case_counts_async(self, request):
        """统计各状态工单数量

        统计各状态工单数量
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListCaseCounts
        :type request: :class:`huaweicloudsdkosm.v2.ListCaseCountsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListCaseCountsResponse`
        """
        return self.list_case_counts_with_http_info(request)

    def list_case_counts_with_http_info(self, request):
        all_params = ['status', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/cases/count',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCaseCountsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_case_labels_async(self, request):
        """查询工单关联标签接口

        查询工单关联标签接口
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListCaseLabels
        :type request: :class:`huaweicloudsdkosm.v2.ListCaseLabelsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListCaseLabelsResponse`
        """
        return self.list_case_labels_with_http_info(request)

    def list_case_labels_with_http_info(self, request):
        all_params = ['case_id', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/cases/{case_id}/labels',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCaseLabelsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_case_limits_async(self, request):
        """查询工单限制，比如抄送邮箱个数等

        查询工单限制，比如抄送邮箱个数等
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListCaseLimits
        :type request: :class:`huaweicloudsdkosm.v2.ListCaseLimitsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListCaseLimitsResponse`
        """
        return self.list_case_limits_with_http_info(request)

    def list_case_limits_with_http_info(self, request):
        all_params = ['x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/config/limits',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCaseLimitsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_case_operate_logs_async(self, request):
        """查询工单操作日志

        查询工单操作日志
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListCaseOperateLogs
        :type request: :class:`huaweicloudsdkosm.v2.ListCaseOperateLogsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListCaseOperateLogsResponse`
        """
        return self.list_case_operate_logs_with_http_info(request)

    def list_case_operate_logs_with_http_info(self, request):
        all_params = ['case_id', 'group_id', 'offset', 'limit', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/cases/{case_id}/operate-logs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCaseOperateLogsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_case_quotas_async(self, request):
        """查询工单配额

        查询工单配额
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListCaseQuotas
        :type request: :class:`huaweicloudsdkosm.v2.ListCaseQuotasRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListCaseQuotasResponse`
        """
        return self.list_case_quotas_with_http_info(request)

    def list_case_quotas_with_http_info(self, request):
        all_params = ['business_type_id', 'product_category_id', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCaseQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_case_templates_async(self, request):
        """查询问题类型对应模板

        查询问题类型对应模板
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListCaseTemplates
        :type request: :class:`huaweicloudsdkosm.v2.ListCaseTemplatesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListCaseTemplatesResponse`
        """
        return self.list_case_templates_with_http_info(request)

    def list_case_templates_with_http_info(self, request):
        all_params = ['business_type_id', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/config/templates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCaseTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_cases_async(self, request):
        """查询工单列表接口

        查询工单列表接口
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListCases
        :type request: :class:`huaweicloudsdkosm.v2.ListCasesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListCasesResponse`
        """
        return self.list_cases_with_http_info(request)

    def list_cases_with_http_info(self, request):
        all_params = ['search_key', 'label_id_list', 'app_key', 'incident_id', 'query_start_time', 'query_end_time', 'status', 'incident_status', 'x_customer_id', 'x_customer_name', 'group_id', 'offset', 'limit', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/cases',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCasesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_customers_regions_async(self, request):
        """查询用户关联的region

        查询用户关联的region
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListCustomersRegions
        :type request: :class:`huaweicloudsdkosm.v2.ListCustomersRegionsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListCustomersRegionsResponse`
        """
        return self.list_customers_regions_with_http_info(request)

    def list_customers_regions_with_http_info(self, request):
        all_params = ['x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/customers/regions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCustomersRegionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_extends_params_async(self, request):
        """查询附加参数

        提单时，根据不同的产品或者问题类型，会存在不同的一些附加参数填写
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListExtendsParams
        :type request: :class:`huaweicloudsdkosm.v2.ListExtendsParamsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListExtendsParamsResponse`
        """
        return self.list_extends_params_with_http_info(request)

    def list_extends_params_with_http_info(self, request):
        all_params = ['business_type_id', 'incident_sub_type_id', 'product_category_id', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/config/extends-map',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListExtendsParamsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_has_verified_contacts_async(self, request):
        """查询已验证的列表

        查询已验证的列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListHasVerifiedContacts
        :type request: :class:`huaweicloudsdkosm.v2.ListHasVerifiedContactsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListHasVerifiedContactsResponse`
        """
        return self.list_has_verified_contacts_with_http_info(request)

    def list_has_verified_contacts_with_http_info(self, request):
        all_params = ['contact_way', 'customer_id', 'sub_customer_id', 'expired_time', 'verified_id', 'contact_value', 'area_code', 'offset', 'limit', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/verifycodes/has-verified',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListHasVerifiedContactsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_history_operate_logs_async(self, request):
        """查询堡垒机历史操作记录

        查询堡垒机历史操作记录
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListHistoryOperateLogs
        :type request: :class:`huaweicloudsdkosm.v2.ListHistoryOperateLogsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListHistoryOperateLogsResponse`
        """
        return self.list_history_operate_logs_with_http_info(request)

    def list_history_operate_logs_with_http_info(self, request):
        all_params = ['authorization_id', 'authorization_detail_id', 'session_id', 'group_id', 'sort', 'offset', 'limit', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/authorizations/{authorization_id}/authorization-details/{authorization_detail_id}/sessions/{session_id}/operation-logs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListHistoryOperateLogsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_history_sessions_async(self, request):
        """查询堡垒机历史会话列表

        查询堡垒机历史会话列
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListHistorySessions
        :type request: :class:`huaweicloudsdkosm.v2.ListHistorySessionsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListHistorySessionsResponse`
        """
        return self.list_history_sessions_with_http_info(request)

    def list_history_sessions_with_http_info(self, request):
        all_params = ['authorization_id', 'authorization_detail_id', 'group_id', 'offset', 'limit', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/authorizations/{authorization_id}/authorization-details/{authorization_detail_id}/history-sessions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListHistorySessionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_labels_async(self, request):
        """查询标签

        查询标签
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListLabels
        :type request: :class:`huaweicloudsdkosm.v2.ListLabelsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListLabelsResponse`
        """
        return self.list_labels_with_http_info(request)

    def list_labels_with_http_info(self, request):
        all_params = ['offset', 'limit', 'name', 'label_id', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/labels',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListLabelsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_messages_async(self, request):
        """查询留言

        查询留言
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListMessages
        :type request: :class:`huaweicloudsdkosm.v2.ListMessagesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListMessagesResponse`
        """
        return self.list_messages_with_http_info(request)

    def list_messages_with_http_info(self, request):
        all_params = ['case_id', 'group_id', 'offset', 'limit', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/cases/{case_id}/messages',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListMessagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_more_instant_messages_async(self, request):
        """查询更多留言

        查询更多留言
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListMoreInstantMessages
        :type request: :class:`huaweicloudsdkosm.v2.ListMoreInstantMessagesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListMoreInstantMessagesResponse`
        """
        return self.list_more_instant_messages_with_http_info(request)

    def list_more_instant_messages_with_http_info(self, request):
        all_params = ['case_id', 'create_time', 'type', 'limit', 'group_id', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/cases/{case_id}/instant-messages/more',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListMoreInstantMessagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_new_instant_messages_async(self, request):
        """轮询查询即时消息

        轮询查询即时消息接口
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListNewInstantMessages
        :type request: :class:`huaweicloudsdkosm.v2.ListNewInstantMessagesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListNewInstantMessagesResponse`
        """
        return self.list_new_instant_messages_with_http_info(request)

    def list_new_instant_messages_with_http_info(self, request):
        all_params = ['case_ids', 'last_message_time_id', 'group_id', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/cases/instant-messages',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListNewInstantMessagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_privileges_async(self, request):
        """查询工单权限

        查询工单权限
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListPrivileges
        :type request: :class:`huaweicloudsdkosm.v2.ListPrivilegesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListPrivilegesResponse`
        """
        return self.list_privileges_with_http_info(request)

    def list_privileges_with_http_info(self, request):
        all_params = ['privilege', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/privileges',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPrivilegesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_problem_types_async(self, request):
        """查询问题类型列表

        提交工单时，选择产品类型之后选择对应的问题列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListProblemTypes
        :type request: :class:`huaweicloudsdkosm.v2.ListProblemTypesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListProblemTypesResponse`
        """
        return self.list_problem_types_with_http_info(request)

    def list_problem_types_with_http_info(self, request):
        all_params = ['product_category_id', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/config/problems',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListProblemTypesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_product_categories_async(self, request):
        """查询产品类型列表

        查询产品类型列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListProductCategories
        :type request: :class:`huaweicloudsdkosm.v2.ListProductCategoriesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListProductCategoriesResponse`
        """
        return self.list_product_categories_with_http_info(request)

    def list_product_categories_with_http_info(self, request):
        all_params = ['product_category_name', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/config/product-categories',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListProductCategoriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_regions_async(self, request):
        """查询区域列表

        查询区域列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListRegions
        :type request: :class:`huaweicloudsdkosm.v2.ListRegionsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListRegionsResponse`
        """
        return self.list_regions_with_http_info(request)

    def list_regions_with_http_info(self, request):
        all_params = ['x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/config/regions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRegionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_relation_async(self, request):
        """查询关联工单

        查询工单的关联，返回关联工单的简要信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListRelation
        :type request: :class:`huaweicloudsdkosm.v2.ListRelationRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListRelationResponse`
        """
        return self.list_relation_with_http_info(request)

    def list_relation_with_http_info(self, request):
        all_params = ['case_id', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/cases/{case_id}/relations',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRelationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_satisfaction_dimensions_async(self, request):
        """工单满意度分类列表

        工单满意度分类列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListSatisfactionDimensions
        :type request: :class:`huaweicloudsdkosm.v2.ListSatisfactionDimensionsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListSatisfactionDimensionsResponse`
        """
        return self.list_satisfaction_dimensions_with_http_info(request)

    def list_satisfaction_dimensions_with_http_info(self, request):
        all_params = ['x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/config/satisfaction-dimensions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSatisfactionDimensionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_severities_async(self, request):
        """查询问题严重性列表

        查询问题严重性列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListSeverities
        :type request: :class:`huaweicloudsdkosm.v2.ListSeveritiesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListSeveritiesResponse`
        """
        return self.list_severities_with_http_info(request)

    def list_severities_with_http_info(self, request):
        all_params = ['product_category_id', 'business_type_id', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/config/severities',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSeveritiesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_sub_customers_async(self, request):
        """查询子用户信息

        查询子用户信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListSubCustomers
        :type request: :class:`huaweicloudsdkosm.v2.ListSubCustomersRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListSubCustomersResponse`
        """
        return self.list_sub_customers_with_http_info(request)

    def list_sub_customers_with_http_info(self, request):
        all_params = ['sub_customer_name', 'sub_customer_id', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/customers/sub-customers',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSubCustomersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_transport_histories_async(self, request):
        """查询堡垒机文件传输记录

        查询堡垒机文件传输记录
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListTransportHistories
        :type request: :class:`huaweicloudsdkosm.v2.ListTransportHistoriesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListTransportHistoriesResponse`
        """
        return self.list_transport_histories_with_http_info(request)

    def list_transport_histories_with_http_info(self, request):
        all_params = ['authorization_id', 'authorization_detail_id', 'session_id', 'group_id', 'sort', 'offset', 'limit', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/authorizations/{authorization_id}/authorization-details/{authorization_detail_id}/sessions/{session_id}/operation-file-logs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTransportHistoriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_unread_new_instant_messages_async(self, request):
        """查询未读消息

        查询未读消息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListUnreadNewInstantMessages
        :type request: :class:`huaweicloudsdkosm.v2.ListUnreadNewInstantMessagesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ListUnreadNewInstantMessagesResponse`
        """
        return self.list_unread_new_instant_messages_with_http_info(request)

    def list_unread_new_instant_messages_with_http_info(self, request):
        all_params = ['case_ids', 'group_id', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/cases/instant-messages/unread',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListUnreadNewInstantMessagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def send_verify_codes_async(self, request):
        """获取验证码

        获取验证码
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SendVerifyCodes
        :type request: :class:`huaweicloudsdkosm.v2.SendVerifyCodesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.SendVerifyCodesResponse`
        """
        return self.send_verify_codes_with_http_info(request)

    def send_verify_codes_with_http_info(self, request):
        all_params = ['x_site', 'x_language', 'x_time_zone', 'send_verify_codes_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/servicerequest/verifycodes/send',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SendVerifyCodesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_accessory_limits_async(self, request):
        """附件限制

        查询附件的一下限制，比如大小，数量，文件类型
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowAccessoryLimits
        :type request: :class:`huaweicloudsdkosm.v2.ShowAccessoryLimitsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ShowAccessoryLimitsResponse`
        """
        return self.show_accessory_limits_with_http_info(request)

    def show_accessory_limits_with_http_info(self, request):
        all_params = ['x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/accessorys/limits',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowAccessoryLimitsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_authorization_detail_async(self, request):
        """查询授权详情

        查询授权详情
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowAuthorizationDetail
        :type request: :class:`huaweicloudsdkosm.v2.ShowAuthorizationDetailRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ShowAuthorizationDetailResponse`
        """
        return self.show_authorization_detail_with_http_info(request)

    def show_authorization_detail_with_http_info(self, request):
        all_params = ['authorization_id', 'group_id', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/authorizations/{authorization_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowAuthorizationDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_case_detail_async(self, request):
        """查询工单详情

        查询工单详情
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowCaseDetail
        :type request: :class:`huaweicloudsdkosm.v2.ShowCaseDetailRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ShowCaseDetailResponse`
        """
        return self.show_case_detail_with_http_info(request)

    def show_case_detail_with_http_info(self, request):
        all_params = ['case_id', 'group_id', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/cases/{case_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCaseDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_case_extends_param_async(self, request):
        """查询工单扩展参数

        查询工单扩展参数
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowCaseExtendsParam
        :type request: :class:`huaweicloudsdkosm.v2.ShowCaseExtendsParamRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ShowCaseExtendsParamResponse`
        """
        return self.show_case_extends_param_with_http_info(request)

    def show_case_extends_param_with_http_info(self, request):
        all_params = ['group_id', 'case_id', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/cases/{case_id}/extends-param',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCaseExtendsParamResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_case_status_async(self, request):
        """查询某个工单状态

        查询某个工单状态
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowCaseStatus
        :type request: :class:`huaweicloudsdkosm.v2.ShowCaseStatusRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ShowCaseStatusResponse`
        """
        return self.show_case_status_with_http_info(request)

    def show_case_status_with_http_info(self, request):
        all_params = ['case_id', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/cases/{case_id}/status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCaseStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_customer_privilege_policy_async(self, request):
        """查询提单权限

        查询提单权限
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowCustomerPrivilegePolicy
        :type request: :class:`huaweicloudsdkosm.v2.ShowCustomerPrivilegePolicyRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ShowCustomerPrivilegePolicyResponse`
        """
        return self.show_customer_privilege_policy_with_http_info(request)

    def show_customer_privilege_policy_with_http_info(self, request):
        all_params = ['x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/privileges/privilege-policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCustomerPrivilegePolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_latest_published_agreement_async(self, request):
        """查看最新发布版本协议详情

        查看最新发布版本协议详情
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowLatestPublishedAgreement
        :type request: :class:`huaweicloudsdkosm.v2.ShowLatestPublishedAgreementRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ShowLatestPublishedAgreementResponse`
        """
        return self.show_latest_published_agreement_with_http_info(request)

    def show_latest_published_agreement_with_http_info(self, request):
        all_params = ['agreement_type', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/agreements/published-agreement',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowLatestPublishedAgreementResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_partners_cases_privilege_async(self, request):
        """查询伙伴工单权限

        查询伙伴工单权限
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowPartnersCasesPrivilege
        :type request: :class:`huaweicloudsdkosm.v2.ShowPartnersCasesPrivilegeRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ShowPartnersCasesPrivilegeResponse`
        """
        return self.show_partners_cases_privilege_with_http_info(request)

    def show_partners_cases_privilege_with_http_info(self, request):
        all_params = ['x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/cases/partners/privilege/cases-processing',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPartnersCasesPrivilegeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_partners_service_info_async(self, request):
        """查询关联伙伴服务信息

        查询关联伙伴服务信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowPartnersServiceInfo
        :type request: :class:`huaweicloudsdkosm.v2.ShowPartnersServiceInfoRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ShowPartnersServiceInfoResponse`
        """
        return self.show_partners_service_info_with_http_info(request)

    def show_partners_service_info_with_http_info(self, request):
        all_params = ['case_sub_type_id', 'product_id', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/cases/partners/service-info',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPartnersServiceInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_signed_latest_published_agreement_async(self, request):
        """查询用户是否签署最新协议

        查询用户是否签署最新协议
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowSignedLatestPublishedAgreement
        :type request: :class:`huaweicloudsdkosm.v2.ShowSignedLatestPublishedAgreementRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.ShowSignedLatestPublishedAgreementResponse`
        """
        return self.show_signed_latest_published_agreement_with_http_info(request)

    def show_signed_latest_published_agreement_with_http_info(self, request):
        all_params = ['agreement_type', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/servicerequest/agreements/signed-latest',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowSignedLatestPublishedAgreementResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def sign_published_agreement_async(self, request):
        """签署协议

        签署协议
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SignPublishedAgreement
        :type request: :class:`huaweicloudsdkosm.v2.SignPublishedAgreementRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.SignPublishedAgreementResponse`
        """
        return self.sign_published_agreement_with_http_info(request)

    def sign_published_agreement_with_http_info(self, request):
        all_params = ['id', 'x_site', 'x_language', 'x_time_zone', 'sign_published_agreement_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/servicerequest/agreements/{id}/signed',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SignPublishedAgreementResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_authorizations_async(self, request):
        """拒绝|撤销授权

        拒绝|撤销授权
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateAuthorizations
        :type request: :class:`huaweicloudsdkosm.v2.UpdateAuthorizationsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.UpdateAuthorizationsResponse`
        """
        return self.update_authorizations_with_http_info(request)

    def update_authorizations_with_http_info(self, request):
        all_params = ['authorization_id', 'action_id', 'x_site', 'x_language', 'x_time_zone', 'update_authorizations_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/servicerequest/authorizations/{authorization_id}/action',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateAuthorizationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_case_contact_info_async(self, request):
        """修改联系方式

        修改联系方式
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateCaseContactInfo
        :type request: :class:`huaweicloudsdkosm.v2.UpdateCaseContactInfoRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.UpdateCaseContactInfoResponse`
        """
        return self.update_case_contact_info_with_http_info(request)

    def update_case_contact_info_with_http_info(self, request):
        all_params = ['case_id', 'update_case_contact_info_request_body', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/servicerequest/cases/{case_id}/contact-info',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateCaseContactInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_cases_async(self, request):
        """工单操作

        工单操作
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateCases
        :type request: :class:`huaweicloudsdkosm.v2.UpdateCasesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.UpdateCasesResponse`
        """
        return self.update_cases_with_http_info(request)

    def update_cases_with_http_info(self, request):
        all_params = ['case_id', 'action_id', 'x_site', 'x_language', 'x_time_zone', 'update_cases_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/servicerequest/cases/{case_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateCasesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_labels_async(self, request):
        """修改标签

        修改标签
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateLabels
        :type request: :class:`huaweicloudsdkosm.v2.UpdateLabelsRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.UpdateLabelsResponse`
        """
        return self.update_labels_with_http_info(request)

    def update_labels_with_http_info(self, request):
        all_params = ['label_id', 'update_labels_request_body', 'x_site', 'x_language', 'x_time_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/servicerequest/labels/{label_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateLabelsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_new_instant_messages_read_async(self, request):
        """设置消息已读

        设置消息已读
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateNewInstantMessagesRead
        :type request: :class:`huaweicloudsdkosm.v2.UpdateNewInstantMessagesReadRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.UpdateNewInstantMessagesReadResponse`
        """
        return self.update_new_instant_messages_read_with_http_info(request)

    def update_new_instant_messages_read_with_http_info(self, request):
        all_params = ['case_id', 'x_site', 'x_language', 'x_time_zone', 'update_new_instant_messages_read_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/servicerequest/cases/{case_id}/instant-messages/unread',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateNewInstantMessagesReadResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def upload_json_accessories_async(self, request):
        """上传附件

        上传附件给SDK使用
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UploadJsonAccessories
        :type request: :class:`huaweicloudsdkosm.v2.UploadJsonAccessoriesRequest`
        :rtype: :class:`huaweicloudsdkosm.v2.UploadJsonAccessoriesResponse`
        """
        return self.upload_json_accessories_with_http_info(request)

    def upload_json_accessories_with_http_info(self, request):
        all_params = ['x_site', 'x_language', 'x_time_zone', 'upload_json_accessories_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/servicerequest/accessorys/json-format-content',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UploadJsonAccessoriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
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
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type,
	    async_request=True)
