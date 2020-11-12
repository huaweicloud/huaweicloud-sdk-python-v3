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


class BssAsyncClient(Client):
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
        super(BssAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkbss.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @staticmethod
    def new_builder(clazz):
        return ClientBuilder(clazz, "GlobalCredentials")

    def batch_set_sub_customer_discount_async(self, request):
        """设置伙伴折扣

        功能描述：设置伙伴折扣

        :param BatchSetSubCustomerDiscountRequest request
        :return: BatchSetSubCustomerDiscountResponse
        """
        return self.batch_set_sub_customer_discount_with_http_info(request)

    def batch_set_sub_customer_discount_with_http_info(self, request):
        """设置伙伴折扣

        功能描述：设置伙伴折扣

        :param BatchSetSubCustomerDiscountRequest request
        :return: BatchSetSubCustomerDiscountResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/partners/discounts',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchSetSubCustomerDiscountResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def change_enterprise_realname_authentication_async(self, request):
        """实名认证变更申请

        功能描述：实名认证变更申请

        :param ChangeEnterpriseRealnameAuthenticationRequest request
        :return: ChangeEnterpriseRealnameAuthenticationResponse
        """
        return self.change_enterprise_realname_authentication_with_http_info(request)

    def change_enterprise_realname_authentication_with_http_info(self, request):
        """实名认证变更申请

        功能描述：实名认证变更申请

        :param ChangeEnterpriseRealnameAuthenticationRequest request
        :return: ChangeEnterpriseRealnameAuthenticationResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/customers/realname-auths/enterprise',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ChangeEnterpriseRealnameAuthenticationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def check_user_identity_async(self, request):
        """校验客户的注册信息

        功能描述：校验客户的注册信息

        :param CheckUserIdentityRequest request
        :return: CheckUserIdentityResponse
        """
        return self.check_user_identity_with_http_info(request)

    def check_user_identity_with_http_info(self, request):
        """校验客户的注册信息

        功能描述：校验客户的注册信息

        :param CheckUserIdentityRequest request
        :return: CheckUserIdentityResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/partners/sub-customers/users/check-identity',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CheckUserIdentityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_enterprise_project_auth_async(self, request):
        """开通企业项目

        功能描述：客户开通自身的企业项目功能

        :param CreateEnterpriseProjectAuthRequest request
        :return: CreateEnterpriseProjectAuthResponse
        """
        return self.create_enterprise_project_auth_with_http_info(request)

    def create_enterprise_project_auth_with_http_info(self, request):
        """开通企业项目

        功能描述：客户开通自身的企业项目功能

        :param CreateEnterpriseProjectAuthRequest request
        :return: CreateEnterpriseProjectAuthResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/enterprises/enterprise-projects/authority',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateEnterpriseProjectAuthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_enterprise_realname_authentication_async(self, request):
        """企业实名认证申请

        功能描述：企业实名认证申请V2

        :param CreateEnterpriseRealnameAuthenticationRequest request
        :return: CreateEnterpriseRealnameAuthenticationResponse
        """
        return self.create_enterprise_realname_authentication_with_http_info(request)

    def create_enterprise_realname_authentication_with_http_info(self, request):
        """企业实名认证申请

        功能描述：企业实名认证申请V2

        :param CreateEnterpriseRealnameAuthenticationRequest request
        :return: CreateEnterpriseRealnameAuthenticationResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/customers/realname-auths/enterprise',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateEnterpriseRealnameAuthenticationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_partner_coupons_async(self, request):
        """伙伴给子客户发券

        功能描述：伙伴给子客户发券

        :param CreatePartnerCouponsRequest request
        :return: CreatePartnerCouponsResponse
        """
        return self.create_partner_coupons_with_http_info(request)

    def create_partner_coupons_with_http_info(self, request):
        """伙伴给子客户发券

        功能描述：伙伴给子客户发券

        :param CreatePartnerCouponsRequest request
        :return: CreatePartnerCouponsResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/promotions/benefits/partner-coupons',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreatePartnerCouponsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_personal_realname_auth_async(self, request):
        """个人实名认证申请

        功能描述：个人实名认证申请

        :param CreatePersonalRealnameAuthRequest request
        :return: CreatePersonalRealnameAuthResponse
        """
        return self.create_personal_realname_auth_with_http_info(request)

    def create_personal_realname_auth_with_http_info(self, request):
        """个人实名认证申请

        功能描述：个人实名认证申请

        :param CreatePersonalRealnameAuthRequest request
        :return: CreatePersonalRealnameAuthResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/customers/realname-auths/individual',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreatePersonalRealnameAuthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_sub_customer_async(self, request):
        """创建客户（V2）

        功能描述：在伙伴销售平台创建客户时同步创建华为云账号，并将客户在伙伴销售平台上的账号与华为云账号进行映射。同时，创建的华为云账号与伙伴账号关联绑定。

        :param CreateSubCustomerRequest request
        :return: CreateSubCustomerResponse
        """
        return self.create_sub_customer_with_http_info(request)

    def create_sub_customer_with_http_info(self, request):
        """创建客户（V2）

        功能描述：在伙伴销售平台创建客户时同步创建华为云账号，并将客户在伙伴销售平台上的账号与华为云账号进行映射。同时，创建的华为云账号与伙伴账号关联绑定。

        :param CreateSubCustomerRequest request
        :return: CreateSubCustomerResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/partners/sub-customers',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateSubCustomerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_sub_enterprise_account_async(self, request):
        """创建企业子账号

        功能描述：创建企业子账号

        :param CreateSubEnterpriseAccountRequest request
        :return: CreateSubEnterpriseAccountResponse
        """
        return self.create_sub_enterprise_account_with_http_info(request)

    def create_sub_enterprise_account_with_http_info(self, request):
        """创建企业子账号

        功能描述：创建企业子账号

        :param CreateSubEnterpriseAccountRequest request
        :return: CreateSubEnterpriseAccountResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/enterprises/multi-accounts/sub-customers',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateSubEnterpriseAccountResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_cities_async(self, request):
        """根据省份查询城市信息

        功能描述：根据省份查询城市列表

        :param ListCitiesRequest request
        :return: ListCitiesResponse
        """
        return self.list_cities_with_http_info(request)

    def list_cities_with_http_info(self, request):
        """根据省份查询城市信息

        功能描述：根据省份查询城市列表

        :param ListCitiesRequest request
        :return: ListCitiesResponse
        """

        all_params = ['province_code', 'x_language', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'province_code' in local_var_params:
            query_params.append(('province_code', local_var_params['province_code']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/systems/configs/cities',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCitiesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_counties_async(self, request):
        """根据城市查询区县信息

        功能描述：根据城市查询区县列表

        :param ListCountiesRequest request
        :return: ListCountiesResponse
        """
        return self.list_counties_with_http_info(request)

    def list_counties_with_http_info(self, request):
        """根据城市查询区县信息

        功能描述：根据城市查询区县列表

        :param ListCountiesRequest request
        :return: ListCountiesResponse
        """

        all_params = ['city_code', 'x_language', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'city_code' in local_var_params:
            query_params.append(('city_code', local_var_params['city_code']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/systems/configs/counties',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCountiesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_coupon_quotas_records_async(self, request):
        """查询优惠券额度发放回收记录

        功能描述：查询优惠券额度发放回收记录

        :param ListCouponQuotasRecordsRequest request
        :return: ListCouponQuotasRecordsResponse
        """
        return self.list_coupon_quotas_records_with_http_info(request)

    def list_coupon_quotas_records_with_http_info(self, request):
        """查询优惠券额度发放回收记录

        功能描述：查询优惠券额度发放回收记录

        :param ListCouponQuotasRecordsRequest request
        :return: ListCouponQuotasRecordsResponse
        """

        all_params = ['indirect_partner_id', 'quota_id', 'operation_time_begin', 'operation_time_end', 'parent_quota_id', 'operation_type', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'indirect_partner_id' in local_var_params:
            query_params.append(('indirect_partner_id', local_var_params['indirect_partner_id']))
        if 'quota_id' in local_var_params:
            query_params.append(('quota_id', local_var_params['quota_id']))
        if 'operation_time_begin' in local_var_params:
            query_params.append(('operation_time_begin', local_var_params['operation_time_begin']))
        if 'operation_time_end' in local_var_params:
            query_params.append(('operation_time_end', local_var_params['operation_time_end']))
        if 'parent_quota_id' in local_var_params:
            query_params.append(('parent_quota_id', local_var_params['parent_quota_id']))
        if 'operation_type' in local_var_params:
            query_params.append(('operation_type', local_var_params['operation_type']))
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


        auth_settings = []

        return self.call_api(
            resource_path='/v2/partners/coupon-quotas/records',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCouponQuotasRecordsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_customer_bills_fee_records_async(self, request):
        """查询流水账单

        功能描述：客户在客户自建平台查询自己的流水账单

        :param ListCustomerBillsFeeRecordsRequest request
        :return: ListCustomerBillsFeeRecordsResponse
        """
        return self.list_customer_bills_fee_records_with_http_info(request)

    def list_customer_bills_fee_records_with_http_info(self, request):
        """查询流水账单

        功能描述：客户在客户自建平台查询自己的流水账单

        :param ListCustomerBillsFeeRecordsRequest request
        :return: ListCustomerBillsFeeRecordsResponse
        """

        all_params = ['bill_cycle', 'x_language', 'provider_type', 'service_type_code', 'resource_type_code', 'region_code', 'charging_mode', 'bill_type', 'trade_id', 'enterprise_project_id', 'include_zero_record', 'status', 'method', 'sub_customer_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bill_cycle' in local_var_params:
            query_params.append(('bill_cycle', local_var_params['bill_cycle']))
        if 'provider_type' in local_var_params:
            query_params.append(('provider_type', local_var_params['provider_type']))
        if 'service_type_code' in local_var_params:
            query_params.append(('service_type_code', local_var_params['service_type_code']))
        if 'resource_type_code' in local_var_params:
            query_params.append(('resource_type_code', local_var_params['resource_type_code']))
        if 'region_code' in local_var_params:
            query_params.append(('region_code', local_var_params['region_code']))
        if 'charging_mode' in local_var_params:
            query_params.append(('charging_mode', local_var_params['charging_mode']))
        if 'bill_type' in local_var_params:
            query_params.append(('bill_type', local_var_params['bill_type']))
        if 'trade_id' in local_var_params:
            query_params.append(('trade_id', local_var_params['trade_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'include_zero_record' in local_var_params:
            query_params.append(('include_zero_record', local_var_params['include_zero_record']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'method' in local_var_params:
            query_params.append(('method', local_var_params['method']))
        if 'sub_customer_id' in local_var_params:
            query_params.append(('sub_customer_id', local_var_params['sub_customer_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/bills/customer-bills/fee-records',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCustomerBillsFeeRecordsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_customer_on_demand_resources_async(self, request):
        """查询客户按需资源列表

        功能描述：查询客户按需资源列表

        :param ListCustomerOnDemandResourcesRequest request
        :return: ListCustomerOnDemandResourcesResponse
        """
        return self.list_customer_on_demand_resources_with_http_info(request)

    def list_customer_on_demand_resources_with_http_info(self, request):
        """查询客户按需资源列表

        功能描述：查询客户按需资源列表

        :param ListCustomerOnDemandResourcesRequest request
        :return: ListCustomerOnDemandResourcesResponse
        """

        all_params = ['req', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v2/partners/sub-customers/on-demand-resources/query',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCustomerOnDemandResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_customers_balances_detail_async(self, request):
        """批量查询伙伴子客户账户余额

        功能描述：批量查询伙伴子客户账户余额

        :param ListCustomersBalancesDetailRequest request
        :return: ListCustomersBalancesDetailResponse
        """
        return self.list_customers_balances_detail_with_http_info(request)

    def list_customers_balances_detail_with_http_info(self, request):
        """批量查询伙伴子客户账户余额

        功能描述：批量查询伙伴子客户账户余额

        :param ListCustomersBalancesDetailRequest request
        :return: ListCustomersBalancesDetailResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/accounts/customer-accounts/balances/batch-query',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCustomersBalancesDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_customerself_resource_record_details_async(self, request):
        """查询资源详单V2（客户）

        功能描述：客户在客户自建平台查询自己的资源详单，用于反映各类资源的消耗情况。资源详单数据有延迟，最大延迟24小时。

        :param ListCustomerselfResourceRecordDetailsRequest request
        :return: ListCustomerselfResourceRecordDetailsResponse
        """
        return self.list_customerself_resource_record_details_with_http_info(request)

    def list_customerself_resource_record_details_with_http_info(self, request):
        """查询资源详单V2（客户）

        功能描述：客户在客户自建平台查询自己的资源详单，用于反映各类资源的消耗情况。资源详单数据有延迟，最大延迟24小时。

        :param ListCustomerselfResourceRecordDetailsRequest request
        :return: ListCustomerselfResourceRecordDetailsResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/bills/customer-bills/res-records/query',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCustomerselfResourceRecordDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_customerself_resource_records_async(self, request):
        """查询资源消费记录（客户）

        功能描述：查询资源消费记录（客户）

        :param ListCustomerselfResourceRecordsRequest request
        :return: ListCustomerselfResourceRecordsResponse
        """
        return self.list_customerself_resource_records_with_http_info(request)

    def list_customerself_resource_records_with_http_info(self, request):
        """查询资源消费记录（客户）

        功能描述：查询资源消费记录（客户）

        :param ListCustomerselfResourceRecordsRequest request
        :return: ListCustomerselfResourceRecordsResponse
        """

        all_params = ['cycle', 'charge_mode', 'x_language', 'cloud_service_type', 'region', 'bill_type', 'offset', 'limit', 'resource_id', 'enterprise_project_id', 'include_zero_record', 'method', 'sub_customer_id', 'trade_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cycle' in local_var_params:
            query_params.append(('cycle', local_var_params['cycle']))
        if 'cloud_service_type' in local_var_params:
            query_params.append(('cloud_service_type', local_var_params['cloud_service_type']))
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
        if 'charge_mode' in local_var_params:
            query_params.append(('charge_mode', local_var_params['charge_mode']))
        if 'bill_type' in local_var_params:
            query_params.append(('bill_type', local_var_params['bill_type']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'include_zero_record' in local_var_params:
            query_params.append(('include_zero_record', local_var_params['include_zero_record']))
        if 'method' in local_var_params:
            query_params.append(('method', local_var_params['method']))
        if 'sub_customer_id' in local_var_params:
            query_params.append(('sub_customer_id', local_var_params['sub_customer_id']))
        if 'trade_id' in local_var_params:
            query_params.append(('trade_id', local_var_params['trade_id']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/bills/customer-bills/res-fee-records',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCustomerselfResourceRecordsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_enterprise_multi_account_async(self, request):
        """查询企业子可回收余额

        功能描述：查询企业子可回收余额

        :param ListEnterpriseMultiAccountRequest request
        :return: ListEnterpriseMultiAccountResponse
        """
        return self.list_enterprise_multi_account_with_http_info(request)

    def list_enterprise_multi_account_with_http_info(self, request):
        """查询企业子可回收余额

        功能描述：查询企业子可回收余额

        :param ListEnterpriseMultiAccountRequest request
        :return: ListEnterpriseMultiAccountResponse
        """

        all_params = ['sub_customer_id', 'balance_type', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sub_customer_id' in local_var_params:
            query_params.append(('sub_customer_id', local_var_params['sub_customer_id']))
        if 'balance_type' in local_var_params:
            query_params.append(('balance_type', local_var_params['balance_type']))
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


        auth_settings = []

        return self.call_api(
            resource_path='/v2/enterprises/multi-accounts/retrieve-amount',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListEnterpriseMultiAccountResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_enterprise_organizations_async(self, request):
        """查询企业组织结构

        功能描述：企业主账号在客户自建平台查询企业组织结构

        :param ListEnterpriseOrganizationsRequest request
        :return: ListEnterpriseOrganizationsResponse
        """
        return self.list_enterprise_organizations_with_http_info(request)

    def list_enterprise_organizations_with_http_info(self, request):
        """查询企业组织结构

        功能描述：企业主账号在客户自建平台查询企业组织结构

        :param ListEnterpriseOrganizationsRequest request
        :return: ListEnterpriseOrganizationsResponse
        """

        all_params = ['recursive_query', 'parent_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'recursive_query' in local_var_params:
            query_params.append(('recursive_query', local_var_params['recursive_query']))
        if 'parent_id' in local_var_params:
            query_params.append(('parent_id', local_var_params['parent_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/enterprises/multi-accounts/enterprise-organizations',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListEnterpriseOrganizationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_enterprise_sub_customers_async(self, request):
        """查询企业子账号列表

        功能描述：企业主账号在客户自建平台查询企业子账号信息列表

        :param ListEnterpriseSubCustomersRequest request
        :return: ListEnterpriseSubCustomersResponse
        """
        return self.list_enterprise_sub_customers_with_http_info(request)

    def list_enterprise_sub_customers_with_http_info(self, request):
        """查询企业子账号列表

        功能描述：企业主账号在客户自建平台查询企业子账号信息列表

        :param ListEnterpriseSubCustomersRequest request
        :return: ListEnterpriseSubCustomersResponse
        """

        all_params = ['sub_customer_account_name', 'sub_customer_display_name', 'fuzzy_query', 'offset', 'limit', 'org_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sub_customer_account_name' in local_var_params:
            query_params.append(('sub_customer_account_name', local_var_params['sub_customer_account_name']))
        if 'sub_customer_display_name' in local_var_params:
            query_params.append(('sub_customer_display_name', local_var_params['sub_customer_display_name']))
        if 'fuzzy_query' in local_var_params:
            query_params.append(('fuzzy_query', local_var_params['fuzzy_query']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'org_id' in local_var_params:
            query_params.append(('org_id', local_var_params['org_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/enterprises/multi-accounts/sub-customers',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListEnterpriseSubCustomersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_indirect_partners_async(self, request):
        """查询精英服务商列表

        功能描述：查询精英服务商列表

        :param ListIndirectPartnersRequest request
        :return: ListIndirectPartnersResponse
        """
        return self.list_indirect_partners_with_http_info(request)

    def list_indirect_partners_with_http_info(self, request):
        """查询精英服务商列表

        功能描述：查询精英服务商列表

        :param ListIndirectPartnersRequest request
        :return: ListIndirectPartnersResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/partners/indirect-partners/query',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListIndirectPartnersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_issued_coupon_quotas_async(self, request):
        """查询已发放优惠券额度

        功能描述：一级经销商查询发给二级经销商的额度

        :param ListIssuedCouponQuotasRequest request
        :return: ListIssuedCouponQuotasResponse
        """
        return self.list_issued_coupon_quotas_with_http_info(request)

    def list_issued_coupon_quotas_with_http_info(self, request):
        """查询已发放优惠券额度

        功能描述：一级经销商查询发给二级经销商的额度

        :param ListIssuedCouponQuotasRequest request
        :return: ListIssuedCouponQuotasResponse
        """

        all_params = ['quota_id', 'indirect_partner_id', 'parent_quota_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'quota_id' in local_var_params:
            query_params.append(('quota_id', local_var_params['quota_id']))
        if 'indirect_partner_id' in local_var_params:
            query_params.append(('indirect_partner_id', local_var_params['indirect_partner_id']))
        if 'parent_quota_id' in local_var_params:
            query_params.append(('parent_quota_id', local_var_params['parent_quota_id']))
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


        auth_settings = []

        return self.call_api(
            resource_path='/v2/partners/issued-coupon-quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListIssuedCouponQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_issued_partner_coupons_async(self, request):
        """查询已发放的优惠券列表

        功能描述：查询已发放的优惠券列表

        :param ListIssuedPartnerCouponsRequest request
        :return: ListIssuedPartnerCouponsResponse
        """
        return self.list_issued_partner_coupons_with_http_info(request)

    def list_issued_partner_coupons_with_http_info(self, request):
        """查询已发放的优惠券列表

        功能描述：查询已发放的优惠券列表

        :param ListIssuedPartnerCouponsRequest request
        :return: ListIssuedPartnerCouponsResponse
        """

        all_params = ['coupon_id', 'customer_id', 'order_id', 'coupon_type', 'status', 'create_time_begin', 'create_time_end', 'effective_time_begin', 'effective_time_end', 'expire_time_begin', 'expire_time_end', 'offset', 'limit', 'indirect_partner_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'coupon_id' in local_var_params:
            query_params.append(('coupon_id', local_var_params['coupon_id']))
        if 'customer_id' in local_var_params:
            query_params.append(('customer_id', local_var_params['customer_id']))
        if 'order_id' in local_var_params:
            query_params.append(('order_id', local_var_params['order_id']))
        if 'coupon_type' in local_var_params:
            query_params.append(('coupon_type', local_var_params['coupon_type']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'create_time_begin' in local_var_params:
            query_params.append(('create_time_begin', local_var_params['create_time_begin']))
        if 'create_time_end' in local_var_params:
            query_params.append(('create_time_end', local_var_params['create_time_end']))
        if 'effective_time_begin' in local_var_params:
            query_params.append(('effective_time_begin', local_var_params['effective_time_begin']))
        if 'effective_time_end' in local_var_params:
            query_params.append(('effective_time_end', local_var_params['effective_time_end']))
        if 'expire_time_begin' in local_var_params:
            query_params.append(('expire_time_begin', local_var_params['expire_time_begin']))
        if 'expire_time_end' in local_var_params:
            query_params.append(('expire_time_end', local_var_params['expire_time_end']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'indirect_partner_id' in local_var_params:
            query_params.append(('indirect_partner_id', local_var_params['indirect_partner_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/promotions/benefits/partner-coupons',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListIssuedPartnerCouponsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_on_demand_resource_ratings_async(self, request):
        """查询按需产品价格

        功能描述：按需资源询价

        :param ListOnDemandResourceRatingsRequest request
        :return: ListOnDemandResourceRatingsResponse
        """
        return self.list_on_demand_resource_ratings_with_http_info(request)

    def list_on_demand_resource_ratings_with_http_info(self, request):
        """查询按需产品价格

        功能描述：按需资源询价

        :param ListOnDemandResourceRatingsRequest request
        :return: ListOnDemandResourceRatingsResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/bills/ratings/on-demand-resources',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListOnDemandResourceRatingsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_partner_adjust_records_async(self, request):
        """查询调账回收记录

        功能描述：查询调账回收记录

        :param ListPartnerAdjustRecordsRequest request
        :return: ListPartnerAdjustRecordsResponse
        """
        return self.list_partner_adjust_records_with_http_info(request)

    def list_partner_adjust_records_with_http_info(self, request):
        """查询调账回收记录

        功能描述：查询调账回收记录

        :param ListPartnerAdjustRecordsRequest request
        :return: ListPartnerAdjustRecordsResponse
        """

        all_params = ['customer_id', 'operation_type', 'operation_time_begin', 'operation_time_end', 'trans_id', 'offset', 'limit', 'indirect_partner_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'customer_id' in local_var_params:
            query_params.append(('customer_id', local_var_params['customer_id']))
        if 'operation_type' in local_var_params:
            query_params.append(('operation_type', local_var_params['operation_type']))
        if 'operation_time_begin' in local_var_params:
            query_params.append(('operation_time_begin', local_var_params['operation_time_begin']))
        if 'operation_time_end' in local_var_params:
            query_params.append(('operation_time_end', local_var_params['operation_time_end']))
        if 'trans_id' in local_var_params:
            query_params.append(('trans_id', local_var_params['trans_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'indirect_partner_id' in local_var_params:
            query_params.append(('indirect_partner_id', local_var_params['indirect_partner_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/accounts/partner-accounts/adjust-records',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPartnerAdjustRecordsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_partner_balances_async(self, request):
        """查询账户余额

        功能描述：查询伙伴账户余额

        :param ListPartnerBalancesRequest request
        :return: ListPartnerBalancesResponse
        """
        return self.list_partner_balances_with_http_info(request)

    def list_partner_balances_with_http_info(self, request):
        """查询账户余额

        功能描述：查询伙伴账户余额

        :param ListPartnerBalancesRequest request
        :return: ListPartnerBalancesResponse
        """

        all_params = ['indirect_partner_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'indirect_partner_id' in local_var_params:
            query_params.append(('indirect_partner_id', local_var_params['indirect_partner_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/accounts/partner-accounts/balances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPartnerBalancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_partner_coupons_record_async(self, request):
        """查询优惠券的发放回收记录

        功能描述：查询优惠券的发放回收记录

        :param ListPartnerCouponsRecordRequest request
        :return: ListPartnerCouponsRecordResponse
        """
        return self.list_partner_coupons_record_with_http_info(request)

    def list_partner_coupons_record_with_http_info(self, request):
        """查询优惠券的发放回收记录

        功能描述：查询优惠券的发放回收记录

        :param ListPartnerCouponsRecordRequest request
        :return: ListPartnerCouponsRecordResponse
        """

        all_params = ['operation_types', 'quota_id', 'quota_type', 'coupon_ids', 'customer_id', 'operation_time_begin', 'operation_time_end', 'result', 'offset', 'limit', 'indirect_partner_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'operation_types' in local_var_params:
            query_params.append(('operation_types', local_var_params['operation_types']))
            collection_formats['operation_types'] = 'multi'
        if 'quota_id' in local_var_params:
            query_params.append(('quota_id', local_var_params['quota_id']))
        if 'quota_type' in local_var_params:
            query_params.append(('quota_type', local_var_params['quota_type']))
        if 'coupon_ids' in local_var_params:
            query_params.append(('coupon_ids', local_var_params['coupon_ids']))
            collection_formats['coupon_ids'] = 'multi'
        if 'customer_id' in local_var_params:
            query_params.append(('customer_id', local_var_params['customer_id']))
        if 'operation_time_begin' in local_var_params:
            query_params.append(('operation_time_begin', local_var_params['operation_time_begin']))
        if 'operation_time_end' in local_var_params:
            query_params.append(('operation_time_end', local_var_params['operation_time_end']))
        if 'result' in local_var_params:
            query_params.append(('result', local_var_params['result']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'indirect_partner_id' in local_var_params:
            query_params.append(('indirect_partner_id', local_var_params['indirect_partner_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/promotions/benefits/partner-coupons/records/query',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPartnerCouponsRecordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_partner_pay_orders_async(self, request):
        """查询伙伴代付订单列表

        功能描述：查询伙伴代付订单列表

        :param ListPartnerPayOrdersRequest request
        :return: ListPartnerPayOrdersResponse
        """
        return self.list_partner_pay_orders_with_http_info(request)

    def list_partner_pay_orders_with_http_info(self, request):
        """查询伙伴代付订单列表

        功能描述：查询伙伴代付订单列表

        :param ListPartnerPayOrdersRequest request
        :return: ListPartnerPayOrdersResponse
        """

        all_params = ['order_id', 'customer_id', 'limit', 'offset', 'status', 'indirect_partner_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_id' in local_var_params:
            query_params.append(('order_id', local_var_params['order_id']))
        if 'customer_id' in local_var_params:
            query_params.append(('customer_id', local_var_params['customer_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'indirect_partner_id' in local_var_params:
            query_params.append(('indirect_partner_id', local_var_params['indirect_partner_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/orders/customer-orders/partner-pay-orders',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPartnerPayOrdersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_provinces_async(self, request):
        """根据国家查询省份信息

        功能描述：根据国家查询省份列表

        :param ListProvincesRequest request
        :return: ListProvincesResponse
        """
        return self.list_provinces_with_http_info(request)

    def list_provinces_with_http_info(self, request):
        """根据国家查询省份信息

        功能描述：根据国家查询省份列表

        :param ListProvincesRequest request
        :return: ListProvincesResponse
        """

        all_params = ['x_language', 'offset', 'limit']
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

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/systems/configs/provinces',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListProvincesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_quota_coupons_async(self, request):
        """查询优惠券额度列表

        功能描述：查询优惠券额度列表

        :param ListQuotaCouponsRequest request
        :return: ListQuotaCouponsResponse
        """
        return self.list_quota_coupons_with_http_info(request)

    def list_quota_coupons_with_http_info(self, request):
        """查询优惠券额度列表

        功能描述：查询优惠券额度列表

        :param ListQuotaCouponsRequest request
        :return: ListQuotaCouponsResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/partners/coupon-quotas/query',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListQuotaCouponsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_rate_on_period_detail_async(self, request):
        """包周期资源订购询价

        功能描述：包周期资源订购询价

        :param ListRateOnPeriodDetailRequest request
        :return: ListRateOnPeriodDetailResponse
        """
        return self.list_rate_on_period_detail_with_http_info(request)

    def list_rate_on_period_detail_with_http_info(self, request):
        """包周期资源订购询价

        功能描述：包周期资源订购询价

        :param ListRateOnPeriodDetailRequest request
        :return: ListRateOnPeriodDetailResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/bills/ratings/period-resources/subscribe-rate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRateOnPeriodDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_sku_inventories_async(self, request):
        """库存查询

        功能描述：查询硬件库存

        :param ListSkuInventoriesRequest request
        :return: ListSkuInventoriesResponse
        """
        return self.list_sku_inventories_with_http_info(request)

    def list_sku_inventories_with_http_info(self, request):
        """库存查询

        功能描述：查询硬件库存

        :param ListSkuInventoriesRequest request
        :return: ListSkuInventoriesResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/orders/inventories/sku-inventories/query',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSkuInventoriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_sub_customer_coupons_async(self, request):
        """查询优惠券列表

        功能描述：查询优惠券列表

        :param ListSubCustomerCouponsRequest request
        :return: ListSubCustomerCouponsResponse
        """
        return self.list_sub_customer_coupons_with_http_info(request)

    def list_sub_customer_coupons_with_http_info(self, request):
        """查询优惠券列表

        功能描述：查询优惠券列表

        :param ListSubCustomerCouponsRequest request
        :return: ListSubCustomerCouponsResponse
        """

        all_params = ['coupon_id', 'order_id', 'promotion_plan_id', 'coupon_type', 'status', 'active_start_time', 'active_end_time', 'offset', 'limit', 'source_id', 'indirect_partner_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'coupon_id' in local_var_params:
            query_params.append(('coupon_id', local_var_params['coupon_id']))
        if 'order_id' in local_var_params:
            query_params.append(('order_id', local_var_params['order_id']))
        if 'promotion_plan_id' in local_var_params:
            query_params.append(('promotion_plan_id', local_var_params['promotion_plan_id']))
        if 'coupon_type' in local_var_params:
            query_params.append(('coupon_type', local_var_params['coupon_type']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'active_start_time' in local_var_params:
            query_params.append(('active_start_time', local_var_params['active_start_time']))
        if 'active_end_time' in local_var_params:
            query_params.append(('active_end_time', local_var_params['active_end_time']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'source_id' in local_var_params:
            query_params.append(('source_id', local_var_params['source_id']))
        if 'indirect_partner_id' in local_var_params:
            query_params.append(('indirect_partner_id', local_var_params['indirect_partner_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/promotions/benefits/coupons',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSubCustomerCouponsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_sub_customer_discounts_async(self, request):
        """查询伙伴折扣

        功能描述：查询伙伴折扣

        :param ListSubCustomerDiscountsRequest request
        :return: ListSubCustomerDiscountsResponse
        """
        return self.list_sub_customer_discounts_with_http_info(request)

    def list_sub_customer_discounts_with_http_info(self, request):
        """查询伙伴折扣

        功能描述：查询伙伴折扣

        :param ListSubCustomerDiscountsRequest request
        :return: ListSubCustomerDiscountsResponse
        """

        all_params = ['customer_id', 'indirect_partner_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'customer_id' in local_var_params:
            query_params.append(('customer_id', local_var_params['customer_id']))
        if 'indirect_partner_id' in local_var_params:
            query_params.append(('indirect_partner_id', local_var_params['indirect_partner_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/partners/discounts',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSubCustomerDiscountsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_sub_customer_res_fee_records_async(self, request):
        """查询客户消费记录

        功能描述：查询客户消费记录

        :param ListSubCustomerResFeeRecordsRequest request
        :return: ListSubCustomerResFeeRecordsResponse
        """
        return self.list_sub_customer_res_fee_records_with_http_info(request)

    def list_sub_customer_res_fee_records_with_http_info(self, request):
        """查询客户消费记录

        功能描述：查询客户消费记录

        :param ListSubCustomerResFeeRecordsRequest request
        :return: ListSubCustomerResFeeRecordsResponse
        """

        all_params = ['customer_id', 'cycle', 'charge_mode', 'cloud_service_type', 'region', 'bill_type', 'offset', 'limit', 'resource_id', 'include_zero_record', 'indirect_partner_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'customer_id' in local_var_params:
            query_params.append(('customer_id', local_var_params['customer_id']))
        if 'cycle' in local_var_params:
            query_params.append(('cycle', local_var_params['cycle']))
        if 'cloud_service_type' in local_var_params:
            query_params.append(('cloud_service_type', local_var_params['cloud_service_type']))
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
        if 'charge_mode' in local_var_params:
            query_params.append(('charge_mode', local_var_params['charge_mode']))
        if 'bill_type' in local_var_params:
            query_params.append(('bill_type', local_var_params['bill_type']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'include_zero_record' in local_var_params:
            query_params.append(('include_zero_record', local_var_params['include_zero_record']))
        if 'indirect_partner_id' in local_var_params:
            query_params.append(('indirect_partner_id', local_var_params['indirect_partner_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/bills/partner-bills/subcustomer-bills/res-fee-records',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSubCustomerResFeeRecordsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_sub_customers_async(self, request):
        """查询客户列表

        功能描述：查询客户列表

        :param ListSubCustomersRequest request
        :return: ListSubCustomersResponse
        """
        return self.list_sub_customers_with_http_info(request)

    def list_sub_customers_with_http_info(self, request):
        """查询客户列表

        功能描述：查询客户列表

        :param ListSubCustomersRequest request
        :return: ListSubCustomersResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/partners/sub-customers/query',
            method='POST',
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


    def list_subcustomer_monthly_bills_async(self, request):
        """查询客户月度消费账单（V2）

        功能描述：合作伙伴可查询客户的消费汇总账单，消费按月汇总

        :param ListSubcustomerMonthlyBillsRequest request
        :return: ListSubcustomerMonthlyBillsResponse
        """
        return self.list_subcustomer_monthly_bills_with_http_info(request)

    def list_subcustomer_monthly_bills_with_http_info(self, request):
        """查询客户月度消费账单（V2）

        功能描述：合作伙伴可查询客户的消费汇总账单，消费按月汇总

        :param ListSubcustomerMonthlyBillsRequest request
        :return: ListSubcustomerMonthlyBillsResponse
        """

        all_params = ['cycle', 'charge_mode', 'customer_id', 'cloud_service_type', 'offset', 'limit', 'bill_type', 'indirect_partner_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'customer_id' in local_var_params:
            query_params.append(('customer_id', local_var_params['customer_id']))
        if 'cycle' in local_var_params:
            query_params.append(('cycle', local_var_params['cycle']))
        if 'cloud_service_type' in local_var_params:
            query_params.append(('cloud_service_type', local_var_params['cloud_service_type']))
        if 'charge_mode' in local_var_params:
            query_params.append(('charge_mode', local_var_params['charge_mode']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'bill_type' in local_var_params:
            query_params.append(('bill_type', local_var_params['bill_type']))
        if 'indirect_partner_id' in local_var_params:
            query_params.append(('indirect_partner_id', local_var_params['indirect_partner_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/bills/partner-bills/subcustomer-bills/monthly-sum',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSubcustomerMonthlyBillsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def reclaim_coupon_quotas_async(self, request):
        """回收优惠券额度

        功能描述：一级经销商给二级经销商回收额度

        :param ReclaimCouponQuotasRequest request
        :return: ReclaimCouponQuotasResponse
        """
        return self.reclaim_coupon_quotas_with_http_info(request)

    def reclaim_coupon_quotas_with_http_info(self, request):
        """回收优惠券额度

        功能描述：一级经销商给二级经销商回收额度

        :param ReclaimCouponQuotasRequest request
        :return: ReclaimCouponQuotasResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/partners/coupon-quotas/indirect-partner-reclaim',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ReclaimCouponQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def reclaim_indirect_partner_account_async(self, request):
        """回收精英服务商账户拨款

        功能描述：合作伙伴可以回收二级渠道账户余额

        :param ReclaimIndirectPartnerAccountRequest request
        :return: ReclaimIndirectPartnerAccountResponse
        """
        return self.reclaim_indirect_partner_account_with_http_info(request)

    def reclaim_indirect_partner_account_with_http_info(self, request):
        """回收精英服务商账户拨款

        功能描述：合作伙伴可以回收二级渠道账户余额

        :param ReclaimIndirectPartnerAccountRequest request
        :return: ReclaimIndirectPartnerAccountResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/accounts/partner-accounts/indirect-partner-reclaim',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ReclaimIndirectPartnerAccountResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def reclaim_partner_coupons_async(self, request):
        """伙伴回收子客户优惠券

        功能描述：伙伴回收子客户优惠券

        :param ReclaimPartnerCouponsRequest request
        :return: ReclaimPartnerCouponsResponse
        """
        return self.reclaim_partner_coupons_with_http_info(request)

    def reclaim_partner_coupons_with_http_info(self, request):
        """伙伴回收子客户优惠券

        功能描述：伙伴回收子客户优惠券

        :param ReclaimPartnerCouponsRequest request
        :return: ReclaimPartnerCouponsResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/promotions/benefits/partner-coupons/reclaim',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ReclaimPartnerCouponsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def reclaim_sub_enterprise_amount_async(self, request):
        """企业主账号从企业子账号回收拨款

        功能描述：企业主账号从企业子账号回收拨款

        :param ReclaimSubEnterpriseAmountRequest request
        :return: ReclaimSubEnterpriseAmountResponse
        """
        return self.reclaim_sub_enterprise_amount_with_http_info(request)

    def reclaim_sub_enterprise_amount_with_http_info(self, request):
        """企业主账号从企业子账号回收拨款

        功能描述：企业主账号从企业子账号回收拨款

        :param ReclaimSubEnterpriseAmountRequest request
        :return: ReclaimSubEnterpriseAmountResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/enterprises/multi-accounts/retrieve-amount',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ReclaimSubEnterpriseAmountResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def reclaim_to_partner_account_async(self, request):
        """回收子客户余额（支持一级回收二级的子客户余额）

        功能描述：回收子客户余额（支持一级回收二级的子客户余额）

        :param ReclaimToPartnerAccountRequest request
        :return: ReclaimToPartnerAccountResponse
        """
        return self.reclaim_to_partner_account_with_http_info(request)

    def reclaim_to_partner_account_with_http_info(self, request):
        """回收子客户余额（支持一级回收二级的子客户余额）

        功能描述：回收子客户余额（支持一级回收二级的子客户余额）

        :param ReclaimToPartnerAccountRequest request
        :return: ReclaimToPartnerAccountResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/accounts/partner-accounts/reclaim',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ReclaimToPartnerAccountResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def send_sms_verification_code_async(self, request):
        """发送短信验证码

        功能描述：发送短信验证码

        :param SendSmsVerificationCodeRequest request
        :return: SendSmsVerificationCodeResponse
        """
        return self.send_sms_verification_code_with_http_info(request)

    def send_sms_verification_code_with_http_info(self, request):
        """发送短信验证码

        功能描述：发送短信验证码

        :param SendSmsVerificationCodeRequest request
        :return: SendSmsVerificationCodeResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/enterprises/multi-accounts/sm-verification-code',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SendSmsVerificationCodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def send_verification_message_code_async(self, request):
        """短信验证码

        功能描述：发送验证码

        :param SendVerificationMessageCodeRequest request
        :return: SendVerificationMessageCodeResponse
        """
        return self.send_verification_message_code_with_http_info(request)

    def send_verification_message_code_with_http_info(self, request):
        """短信验证码

        功能描述：发送验证码

        :param SendVerificationMessageCodeRequest request
        :return: SendVerificationMessageCodeResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/bases/verificationcode/send',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SendVerificationMessageCodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_cusotmer_account_balances_async(self, request):
        """查询客户账户余额

        功能描述：查询客户账户余额

        :param ShowCusotmerAccountBalancesRequest request
        :return: ShowCusotmerAccountBalancesResponse
        """
        return self.show_cusotmer_account_balances_with_http_info(request)

    def show_cusotmer_account_balances_with_http_info(self, request):
        """查询客户账户余额

        功能描述：查询客户账户余额

        :param ShowCusotmerAccountBalancesRequest request
        :return: ShowCusotmerAccountBalancesResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/accounts/customer-accounts/balances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCusotmerAccountBalancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_customer_monthly_sum_async(self, request):
        """查询客户消费汇总

        功能描述：客户可以查询自身的消费汇总单的功能，消费按月汇总。每天刷新一次，更新前一天的数据。

        :param ShowCustomerMonthlySumRequest request
        :return: ShowCustomerMonthlySumResponse
        """
        return self.show_customer_monthly_sum_with_http_info(request)

    def show_customer_monthly_sum_with_http_info(self, request):
        """查询客户消费汇总

        功能描述：客户可以查询自身的消费汇总单的功能，消费按月汇总。每天刷新一次，更新前一天的数据。

        :param ShowCustomerMonthlySumRequest request
        :return: ShowCustomerMonthlySumResponse
        """

        all_params = ['bill_cycle', 'service_type_code', 'enterprise_project_id', 'offset', 'limit', 'method', 'sub_customer_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bill_cycle' in local_var_params:
            query_params.append(('bill_cycle', local_var_params['bill_cycle']))
        if 'service_type_code' in local_var_params:
            query_params.append(('service_type_code', local_var_params['service_type_code']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'method' in local_var_params:
            query_params.append(('method', local_var_params['method']))
        if 'sub_customer_id' in local_var_params:
            query_params.append(('sub_customer_id', local_var_params['sub_customer_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/bills/customer-bills/monthly-sum',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCustomerMonthlySumResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_multi_account_transfer_amount_async(self, request):
        """查询企业主的可拨款余额

        功能描述：查询企业主的可拨款余额

        :param ShowMultiAccountTransferAmountRequest request
        :return: ShowMultiAccountTransferAmountResponse
        """
        return self.show_multi_account_transfer_amount_with_http_info(request)

    def show_multi_account_transfer_amount_with_http_info(self, request):
        """查询企业主的可拨款余额

        功能描述：查询企业主的可拨款余额

        :param ShowMultiAccountTransferAmountRequest request
        :return: ShowMultiAccountTransferAmountResponse
        """

        all_params = ['balance_type', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'balance_type' in local_var_params:
            query_params.append(('balance_type', local_var_params['balance_type']))
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


        auth_settings = []

        return self.call_api(
            resource_path='/v2/enterprises/multi-accounts/transfer-amount',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMultiAccountTransferAmountResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_realname_authentication_review_result_async(self, request):
        """查询实名认证审核结果

        功能描述：查询实名认证审核结果

        :param ShowRealnameAuthenticationReviewResultRequest request
        :return: ShowRealnameAuthenticationReviewResultResponse
        """
        return self.show_realname_authentication_review_result_with_http_info(request)

    def show_realname_authentication_review_result_with_http_info(self, request):
        """查询实名认证审核结果

        功能描述：查询实名认证审核结果

        :param ShowRealnameAuthenticationReviewResultRequest request
        :return: ShowRealnameAuthenticationReviewResultResponse
        """

        all_params = ['customer_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'customer_id' in local_var_params:
            query_params.append(('customer_id', local_var_params['customer_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/customers/realname-auths/result',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRealnameAuthenticationReviewResultResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_coupon_quotas_async(self, request):
        """向精英服务商发放代金券额度

        功能描述：向精英服务商发放代金券额度

        :param UpdateCouponQuotasRequest request
        :return: UpdateCouponQuotasResponse
        """
        return self.update_coupon_quotas_with_http_info(request)

    def update_coupon_quotas_with_http_info(self, request):
        """向精英服务商发放代金券额度

        功能描述：向精英服务商发放代金券额度

        :param UpdateCouponQuotasRequest request
        :return: UpdateCouponQuotasResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/partners/coupon-quotas/indirect-partner-adjust',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateCouponQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_customer_account_amount_async(self, request):
        """调账

        功能描述：从伙伴账户调账给子客户

        :param UpdateCustomerAccountAmountRequest request
        :return: UpdateCustomerAccountAmountResponse
        """
        return self.update_customer_account_amount_with_http_info(request)

    def update_customer_account_amount_with_http_info(self, request):
        """调账

        功能描述：从伙伴账户调账给子客户

        :param UpdateCustomerAccountAmountRequest request
        :return: UpdateCustomerAccountAmountResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/accounts/partner-accounts/adjust-amount',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateCustomerAccountAmountResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_indirect_partner_account_async(self, request):
        """向二级渠道账户拨款

        功能描述：从伙伴账户调账给二级渠道

        :param UpdateIndirectPartnerAccountRequest request
        :return: UpdateIndirectPartnerAccountResponse
        """
        return self.update_indirect_partner_account_with_http_info(request)

    def update_indirect_partner_account_with_http_info(self, request):
        """向二级渠道账户拨款

        功能描述：从伙伴账户调账给二级渠道

        :param UpdateIndirectPartnerAccountRequest request
        :return: UpdateIndirectPartnerAccountResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/accounts/partner-accounts/indirect-partner-adjust',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateIndirectPartnerAccountResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_sub_enterprise_amount_async(self, request):
        """企业主账号向企业子账号拨款

        功能描述：企业主账号向企业子账号拨款

        :param UpdateSubEnterpriseAmountRequest request
        :return: UpdateSubEnterpriseAmountResponse
        """
        return self.update_sub_enterprise_amount_with_http_info(request)

    def update_sub_enterprise_amount_with_http_info(self, request):
        """企业主账号向企业子账号拨款

        功能描述：企业主账号向企业子账号拨款

        :param UpdateSubEnterpriseAmountRequest request
        :return: UpdateSubEnterpriseAmountResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/enterprises/multi-accounts/transfer-amount',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateSubEnterpriseAmountResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def auto_renewal_resources_async(self, request):
        """设置包年包月资源自动续费

        功能描述：设置包周期资源自动续费

        :param AutoRenewalResourcesRequest request
        :return: AutoRenewalResourcesResponse
        """
        return self.auto_renewal_resources_with_http_info(request)

    def auto_renewal_resources_with_http_info(self, request):
        """设置包年包月资源自动续费

        功能描述：设置包周期资源自动续费

        :param AutoRenewalResourcesRequest request
        :return: AutoRenewalResourcesResponse
        """

        all_params = ['resource_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/orders/subscriptions/resources/autorenew/{resource_id}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AutoRenewalResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def cancel_auto_renewal_resources_async(self, request):
        """取消包年包月资源自动续费

        功能描述：取消包年/包月资源自动续费

        :param CancelAutoRenewalResourcesRequest request
        :return: CancelAutoRenewalResourcesResponse
        """
        return self.cancel_auto_renewal_resources_with_http_info(request)

    def cancel_auto_renewal_resources_with_http_info(self, request):
        """取消包年包月资源自动续费

        功能描述：取消包年/包月资源自动续费

        :param CancelAutoRenewalResourcesRequest request
        :return: CancelAutoRenewalResourcesResponse
        """

        all_params = ['resource_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/orders/subscriptions/resources/autorenew/{resource_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CancelAutoRenewalResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def cancel_customer_order_async(self, request):
        """取消包周期订单

        功能描述：取消包周期订单

        :param CancelCustomerOrderRequest request
        :return: CancelCustomerOrderResponse
        """
        return self.cancel_customer_order_with_http_info(request)

    def cancel_customer_order_with_http_info(self, request):
        """取消包周期订单

        功能描述：取消包周期订单

        :param CancelCustomerOrderRequest request
        :return: CancelCustomerOrderResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/orders/customer-orders/cancel',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CancelCustomerOrderResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def cancel_resources_subscription_async(self, request):
        """退订包周期资源

        功能描述：退订包周期资源

        :param CancelResourcesSubscriptionRequest request
        :return: CancelResourcesSubscriptionResponse
        """
        return self.cancel_resources_subscription_with_http_info(request)

    def cancel_resources_subscription_with_http_info(self, request):
        """退订包周期资源

        功能描述：退订包周期资源

        :param CancelResourcesSubscriptionRequest request
        :return: CancelResourcesSubscriptionResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/orders/subscriptions/resources/unsubscribe',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CancelResourcesSubscriptionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_customer_orders_async(self, request):
        """查询订单列表V2

        功能描述：查询订单列表

        :param ListCustomerOrdersRequest request
        :return: ListCustomerOrdersResponse
        """
        return self.list_customer_orders_with_http_info(request)

    def list_customer_orders_with_http_info(self, request):
        """查询订单列表V2

        功能描述：查询订单列表

        :param ListCustomerOrdersRequest request
        :return: ListCustomerOrdersResponse
        """

        all_params = ['order_id', 'customer_id', 'create_time_begin', 'create_time_end', 'service_type_code', 'status', 'order_type', 'limit', 'offset', 'order_by', 'payment_time_begin', 'payment_time_end', 'indirect_partner_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_id' in local_var_params:
            query_params.append(('order_id', local_var_params['order_id']))
        if 'customer_id' in local_var_params:
            query_params.append(('customer_id', local_var_params['customer_id']))
        if 'create_time_begin' in local_var_params:
            query_params.append(('create_time_begin', local_var_params['create_time_begin']))
        if 'create_time_end' in local_var_params:
            query_params.append(('create_time_end', local_var_params['create_time_end']))
        if 'service_type_code' in local_var_params:
            query_params.append(('service_type_code', local_var_params['service_type_code']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'order_type' in local_var_params:
            query_params.append(('order_type', local_var_params['order_type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'payment_time_begin' in local_var_params:
            query_params.append(('payment_time_begin', local_var_params['payment_time_begin']))
        if 'payment_time_end' in local_var_params:
            query_params.append(('payment_time_end', local_var_params['payment_time_end']))
        if 'indirect_partner_id' in local_var_params:
            query_params.append(('indirect_partner_id', local_var_params['indirect_partner_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/orders/customer-orders',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCustomerOrdersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_order_coupons_by_order_id_async(self, request):
        """查询订单可用优惠券

        功能描述：查询订单详情

        :param ListOrderCouponsByOrderIdRequest request
        :return: ListOrderCouponsByOrderIdResponse
        """
        return self.list_order_coupons_by_order_id_with_http_info(request)

    def list_order_coupons_by_order_id_with_http_info(self, request):
        """查询订单可用优惠券

        功能描述：查询订单详情

        :param ListOrderCouponsByOrderIdRequest request
        :return: ListOrderCouponsByOrderIdResponse
        """

        all_params = ['order_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_id' in local_var_params:
            query_params.append(('order_id', local_var_params['order_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/orders/customer-orders/order-coupons',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListOrderCouponsByOrderIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_pay_per_use_customer_resources_async(self, request):
        """查询客户包年包月资源列表

        功能描述：查询客户包年/包月资源列表

        :param ListPayPerUseCustomerResourcesRequest request
        :return: ListPayPerUseCustomerResourcesResponse
        """
        return self.list_pay_per_use_customer_resources_with_http_info(request)

    def list_pay_per_use_customer_resources_with_http_info(self, request):
        """查询客户包年包月资源列表

        功能描述：查询客户包年/包月资源列表

        :param ListPayPerUseCustomerResourcesRequest request
        :return: ListPayPerUseCustomerResourcesResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/orders/suscriptions/resources/query',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPayPerUseCustomerResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_resource_usages_async(self, request):
        """查询套餐内使用量

        功能描述：查询套餐内使用量

        :param ListResourceUsagesRequest request
        :return: ListResourceUsagesResponse
        """
        return self.list_resource_usages_with_http_info(request)

    def list_resource_usages_with_http_info(self, request):
        """查询套餐内使用量

        功能描述：查询套餐内使用量

        :param ListResourceUsagesRequest request
        :return: ListResourceUsagesResponse
        """

        all_params = ['x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/payments/free-resources/usages/query',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListResourceUsagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def pay_orders_async(self, request):
        """支付包周期订单

        功能描述：支付包周期订单

        :param PayOrdersRequest request
        :return: PayOrdersResponse
        """
        return self.pay_orders_with_http_info(request)

    def pay_orders_with_http_info(self, request):
        """支付包周期订单

        功能描述：支付包周期订单

        :param PayOrdersRequest request
        :return: PayOrdersResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/orders/customer-orders/pay',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='PayOrdersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def renewal_resources_async(self, request):
        """续订包周期资源

        功能描述：续订包周期资源

        :param RenewalResourcesRequest request
        :return: RenewalResourcesResponse
        """
        return self.renewal_resources_with_http_info(request)

    def renewal_resources_with_http_info(self, request):
        """续订包周期资源

        功能描述：续订包周期资源

        :param RenewalResourcesRequest request
        :return: RenewalResourcesResponse
        """

        all_params = ['req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/orders/subscriptions/resources/renew',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RenewalResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_customer_order_details_async(self, request):
        """查询订单详情V2

        功能描述：查询订单详情

        :param ShowCustomerOrderDetailsRequest request
        :return: ShowCustomerOrderDetailsResponse
        """
        return self.show_customer_order_details_with_http_info(request)

    def show_customer_order_details_with_http_info(self, request):
        """查询订单详情V2

        功能描述：查询订单详情

        :param ShowCustomerOrderDetailsRequest request
        :return: ShowCustomerOrderDetailsResponse
        """

        all_params = ['order_id', 'limit', 'offset', 'indirect_partner_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'order_id' in local_var_params:
            path_params['order_id'] = local_var_params['order_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'indirect_partner_id' in local_var_params:
            query_params.append(('indirect_partner_id', local_var_params['indirect_partner_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/orders/customer-orders/details/{order_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCustomerOrderDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_refund_order_details_async(self, request):
        """查询退款订单的金额详情V2

        功能描述：查询退款订单的金额详情

        :param ShowRefundOrderDetailsRequest request
        :return: ShowRefundOrderDetailsResponse
        """
        return self.show_refund_order_details_with_http_info(request)

    def show_refund_order_details_with_http_info(self, request):
        """查询退款订单的金额详情V2

        功能描述：查询退款订单的金额详情

        :param ShowRefundOrderDetailsRequest request
        :return: ShowRefundOrderDetailsResponse
        """

        all_params = ['order_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_id' in local_var_params:
            query_params.append(('order_id', local_var_params['order_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/orders/customer-orders/refund-orders',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRefundOrderDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_postal_async(self, request):
        """新增邮寄地址

        功能描述：新增邮寄地址

        :param CreatePostalRequest request
        :return: CreatePostalResponse
        """
        return self.create_postal_with_http_info(request)

    def create_postal_with_http_info(self, request):
        """新增邮寄地址

        功能描述：新增邮寄地址

        :param CreatePostalRequest request
        :return: CreatePostalResponse
        """

        all_params = ['req', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v2/customers/postal-addresses',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreatePostalResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_postal_async(self, request):
        """删除邮寄地址

        功能描述：删除邮寄地址

        :param DeletePostalRequest request
        :return: DeletePostalResponse
        """
        return self.delete_postal_with_http_info(request)

    def delete_postal_with_http_info(self, request):
        """删除邮寄地址

        功能描述：删除邮寄地址

        :param DeletePostalRequest request
        :return: DeletePostalResponse
        """

        all_params = ['address_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'address_id' in local_var_params:
            path_params['address_id'] = local_var_params['address_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/customers/postal-addresses/{address_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeletePostalResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_postal_address_async(self, request):
        """查询邮寄地址

        功能描述：查询邮寄地址

        :param ListPostalAddressRequest request
        :return: ListPostalAddressResponse
        """
        return self.list_postal_address_with_http_info(request)

    def list_postal_address_with_http_info(self, request):
        """查询邮寄地址

        功能描述：查询邮寄地址

        :param ListPostalAddressRequest request
        :return: ListPostalAddressResponse
        """

        all_params = ['offset', 'limit']
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

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/customers/postal-addresses',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPostalAddressResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_resource_types_async(self, request):
        """查询资源类型

        功能描述：查询资源类型

        :param ListResourceTypesRequest request
        :return: ListResourceTypesResponse
        """
        return self.list_resource_types_with_http_info(request)

    def list_resource_types_with_http_info(self, request):
        """查询资源类型

        功能描述：查询资源类型

        :param ListResourceTypesRequest request
        :return: ListResourceTypesResponse
        """

        all_params = ['x_language', 'resource_type_code']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'resource_type_code' in local_var_params:
            query_params.append(('resource_type_code', local_var_params['resource_type_code']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/bases/resource-types',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListResourceTypesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_service_resources_async(self, request):
        """根据云服务类型查询资源列表

        功能描述：根据云服务类型查询资源列表

        :param ListServiceResourcesRequest request
        :return: ListServiceResourcesResponse
        """
        return self.list_service_resources_with_http_info(request)

    def list_service_resources_with_http_info(self, request):
        """根据云服务类型查询资源列表

        功能描述：根据云服务类型查询资源列表

        :param ListServiceResourcesRequest request
        :return: ListServiceResourcesResponse
        """

        all_params = ['service_type_code', 'x_language', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'service_type_code' in local_var_params:
            query_params.append(('service_type_code', local_var_params['service_type_code']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/products/service-resources',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListServiceResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_service_types_async(self, request):
        """查询云服务类型列表

        功能描述：查询云服务类型列表

        :param ListServiceTypesRequest request
        :return: ListServiceTypesResponse
        """
        return self.list_service_types_with_http_info(request)

    def list_service_types_with_http_info(self, request):
        """查询云服务类型列表

        功能描述：查询云服务类型列表

        :param ListServiceTypesRequest request
        :return: ListServiceTypesResponse
        """

        all_params = ['x_language', 'service_type_code']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'service_type_code' in local_var_params:
            query_params.append(('service_type_code', local_var_params['service_type_code']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/bases/service-types',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListServiceTypesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_postal_async(self, request):
        """修改邮寄地址

        功能描述：修改邮寄地址

        :param UpdatePostalRequest request
        :return: UpdatePostalResponse
        """
        return self.update_postal_with_http_info(request)

    def update_postal_with_http_info(self, request):
        """修改邮寄地址

        功能描述：修改邮寄地址

        :param UpdatePostalRequest request
        :return: UpdatePostalResponse
        """

        all_params = ['req', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = []

        return self.call_api(
            resource_path='/v2/customers/postal-addresses',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePostalResponse',
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
