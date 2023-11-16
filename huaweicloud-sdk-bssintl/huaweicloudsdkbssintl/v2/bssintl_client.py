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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkbssintl'")


class BssintlClient(Client):
    def __init__(self):
        super(BssintlClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkbssintl.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials")
        else:
            if clazz.__name__ != "BssintlClient":
                raise TypeError("client type error, support client type is BssintlClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials")

        

        return client_builder

    def list_conversions(self, request):
        """查询使用量单位进制

        功能描述：伙伴在伙伴销售平台上查询使用量单位的进制转换信息，用于不同度量单位之间的转换。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConversions
        :type request: :class:`huaweicloudsdkbssintl.v2.ListConversionsRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ListConversionsResponse`
        """
        http_info = self._list_conversions_http_info(request)
        return self._call_api(**http_info)

    def list_conversions_invoker(self, request):
        http_info = self._list_conversions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_conversions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/bases/conversions",
            "request_type": request.__class__.__name__,
            "response_type": "ListConversionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'measure_type' in local_var_params:
            query_params.append(('measure_type', local_var_params['measure_type']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_costs(self, request):
        """查询成本数据

        客户在自建平台查询成本分析数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCosts
        :type request: :class:`huaweicloudsdkbssintl.v2.ListCostsRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ListCostsResponse`
        """
        http_info = self._list_costs_http_info(request)
        return self._call_api(**http_info)

    def list_costs_invoker(self, request):
        http_info = self._list_costs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_costs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/costs/cost-analysed-bills/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListCostsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_free_resource_usages(self, request):
        """查询资源内使用量

        功能描述：客户在自建平台查询客户自己的资源包列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFreeResourceUsages
        :type request: :class:`huaweicloudsdkbssintl.v2.ListFreeResourceUsagesRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ListFreeResourceUsagesResponse`
        """
        http_info = self._list_free_resource_usages_http_info(request)
        return self._call_api(**http_info)

    def list_free_resource_usages_invoker(self, request):
        http_info = self._list_free_resource_usages_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_free_resource_usages_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/payments/free-resources/usages/details/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListFreeResourceUsagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_free_resources_usage_records(self, request):
        """查询资源包使用明细

        客户在自建平台查询资源包使用明细。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFreeResourcesUsageRecords
        :type request: :class:`huaweicloudsdkbssintl.v2.ListFreeResourcesUsageRecordsRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ListFreeResourcesUsageRecordsResponse`
        """
        http_info = self._list_free_resources_usage_records_http_info(request)
        return self._call_api(**http_info)

    def list_free_resources_usage_records_invoker(self, request):
        http_info = self._list_free_resources_usage_records_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_free_resources_usage_records_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/bills/customer-bills/free-resources-usage-records",
            "request_type": request.__class__.__name__,
            "response_type": "ListFreeResourcesUsageRecordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'free_resource_id' in local_var_params:
            query_params.append(('free_resource_id', local_var_params['free_resource_id']))
        if 'product_id' in local_var_params:
            query_params.append(('product_id', local_var_params['product_id']))
        if 'resource_type_code' in local_var_params:
            query_params.append(('resource_type_code', local_var_params['resource_type_code']))
        if 'deduct_time_begin' in local_var_params:
            query_params.append(('deduct_time_begin', local_var_params['deduct_time_begin']))
        if 'deduct_time_end' in local_var_params:
            query_params.append(('deduct_time_end', local_var_params['deduct_time_end']))
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

    def list_measure_units(self, request):
        """查询使用量单位列表

        功能描述：伙伴在伙伴销售平台上查询资源使用量的度量单位及名称，度量单位类型等。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMeasureUnits
        :type request: :class:`huaweicloudsdkbssintl.v2.ListMeasureUnitsRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ListMeasureUnitsResponse`
        """
        http_info = self._list_measure_units_http_info(request)
        return self._call_api(**http_info)

    def list_measure_units_invoker(self, request):
        http_info = self._list_measure_units_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_measure_units_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/bases/measurements",
            "request_type": request.__class__.__name__,
            "response_type": "ListMeasureUnitsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_resource_types(self, request):
        """查询资源类型列表

        伙伴在伙伴销售平台查询资源类型的列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceTypes
        :type request: :class:`huaweicloudsdkbssintl.v2.ListResourceTypesRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ListResourceTypesResponse`
        """
        http_info = self._list_resource_types_http_info(request)
        return self._call_api(**http_info)

    def list_resource_types_invoker(self, request):
        http_info = self._list_resource_types_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_resource_types_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/products/resource-types",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceTypesResponse"
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
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_service_types(self, request):
        """查询云服务类型列表

        伙伴在伙伴销售平台查询云服务类型的列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListServiceTypes
        :type request: :class:`huaweicloudsdkbssintl.v2.ListServiceTypesRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ListServiceTypesResponse`
        """
        http_info = self._list_service_types_http_info(request)
        return self._call_api(**http_info)

    def list_service_types_invoker(self, request):
        http_info = self._list_service_types_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_service_types_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/products/service-types",
            "request_type": request.__class__.__name__,
            "response_type": "ListServiceTypesResponse"
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
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def change_enterprise_realname_authentication(self, request):
        """申请实名认证变更

        功能描述：客户可以进行实名认证变更申请。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeEnterpriseRealnameAuthentication
        :type request: :class:`huaweicloudsdkbssintl.v2.ChangeEnterpriseRealnameAuthenticationRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ChangeEnterpriseRealnameAuthenticationResponse`
        """
        http_info = self._change_enterprise_realname_authentication_http_info(request)
        return self._call_api(**http_info)

    def change_enterprise_realname_authentication_invoker(self, request):
        http_info = self._change_enterprise_realname_authentication_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_enterprise_realname_authentication_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/customers/realname-auths/enterprise",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeEnterpriseRealnameAuthenticationResponse"
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

    def check_user_identity(self, request):
        """校验客户注册信息

        功能描述：客户注册时可检查客户的登录名称、手机号或者邮箱是否可以用于注册。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckUserIdentity
        :type request: :class:`huaweicloudsdkbssintl.v2.CheckUserIdentityRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.CheckUserIdentityResponse`
        """
        http_info = self._check_user_identity_http_info(request)
        return self._call_api(**http_info)

    def check_user_identity_invoker(self, request):
        http_info = self._check_user_identity_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_user_identity_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/partners/sub-customers/users/check-identity",
            "request_type": request.__class__.__name__,
            "response_type": "CheckUserIdentityResponse"
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

    def create_enterprise_realname_authentication(self, request):
        """申请企业实名认证

        功能描述：企业客户可以进行企业实名认证申请。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEnterpriseRealnameAuthentication
        :type request: :class:`huaweicloudsdkbssintl.v2.CreateEnterpriseRealnameAuthenticationRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.CreateEnterpriseRealnameAuthenticationResponse`
        """
        http_info = self._create_enterprise_realname_authentication_http_info(request)
        return self._call_api(**http_info)

    def create_enterprise_realname_authentication_invoker(self, request):
        http_info = self._create_enterprise_realname_authentication_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_enterprise_realname_authentication_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/customers/realname-auths/enterprise",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEnterpriseRealnameAuthenticationResponse"
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

    def create_personal_realname_auth(self, request):
        """申请个人实名认证

        功能描述：个人客户可以进行个人实名认证申请。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePersonalRealnameAuth
        :type request: :class:`huaweicloudsdkbssintl.v2.CreatePersonalRealnameAuthRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.CreatePersonalRealnameAuthResponse`
        """
        http_info = self._create_personal_realname_auth_http_info(request)
        return self._call_api(**http_info)

    def create_personal_realname_auth_invoker(self, request):
        http_info = self._create_personal_realname_auth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_personal_realname_auth_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/customers/realname-auths/individual",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePersonalRealnameAuthResponse"
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

    def create_sub_customer(self, request):
        """创建客户

        功能描述：在伙伴销售平台创建客户时同步创建华为云账号，并将客户在伙伴销售平台上的账号与华为云账号进行映射。同时，创建的华为云账号与伙伴账号关联绑定。华为云伙伴能力中心（一级经销商）可以注册精英服务商伙伴（二级经销商）的子客户。注册完成后，子客户可以自动和精英服务商伙伴绑定。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSubCustomer
        :type request: :class:`huaweicloudsdkbssintl.v2.CreateSubCustomerRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.CreateSubCustomerResponse`
        """
        http_info = self._create_sub_customer_http_info(request)
        return self._call_api(**http_info)

    def create_sub_customer_invoker(self, request):
        http_info = self._create_sub_customer_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_sub_customer_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/partners/sub-customers",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSubCustomerResponse"
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

    def freeze_sub_customers(self, request):
        """冻结客户账号

        功能描述：冻结伙伴子客户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for FreezeSubCustomers
        :type request: :class:`huaweicloudsdkbssintl.v2.FreezeSubCustomersRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.FreezeSubCustomersResponse`
        """
        http_info = self._freeze_sub_customers_http_info(request)
        return self._call_api(**http_info)

    def freeze_sub_customers_invoker(self, request):
        http_info = self._freeze_sub_customers_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _freeze_sub_customers_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/partners/sub-customers/freeze",
            "request_type": request.__class__.__name__,
            "response_type": "FreezeSubCustomersResponse"
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

    def list_customer_on_demand_resources(self, request):
        """查询客户按需资源列表

        功能描述：客户在伙伴销售平台查询已开通的按需资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCustomerOnDemandResources
        :type request: :class:`huaweicloudsdkbssintl.v2.ListCustomerOnDemandResourcesRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ListCustomerOnDemandResourcesResponse`
        """
        http_info = self._list_customer_on_demand_resources_http_info(request)
        return self._call_api(**http_info)

    def list_customer_on_demand_resources_invoker(self, request):
        http_info = self._list_customer_on_demand_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_customer_on_demand_resources_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/partners/sub-customers/on-demand-resources/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListCustomerOnDemandResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_customerself_resource_record_details(self, request):
        """查询资源详单

        功能描述：客户在客户自建平台查询自己的资源详单，用于反映各类资源的消耗情况。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCustomerselfResourceRecordDetails
        :type request: :class:`huaweicloudsdkbssintl.v2.ListCustomerselfResourceRecordDetailsRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ListCustomerselfResourceRecordDetailsResponse`
        """
        http_info = self._list_customerself_resource_record_details_http_info(request)
        return self._call_api(**http_info)

    def list_customerself_resource_record_details_invoker(self, request):
        http_info = self._list_customerself_resource_record_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_customerself_resource_record_details_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/bills/customer-bills/res-records/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListCustomerselfResourceRecordDetailsResponse"
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

    def list_customerself_resource_records(self, request):
        """查询资源消费记录

        功能描述：客户在客户自建平台查询每个资源的消费明细数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCustomerselfResourceRecords
        :type request: :class:`huaweicloudsdkbssintl.v2.ListCustomerselfResourceRecordsRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ListCustomerselfResourceRecordsResponse`
        """
        http_info = self._list_customerself_resource_records_http_info(request)
        return self._call_api(**http_info)

    def list_customerself_resource_records_invoker(self, request):
        http_info = self._list_customerself_resource_records_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_customerself_resource_records_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/bills/customer-bills/res-fee-records",
            "request_type": request.__class__.__name__,
            "response_type": "ListCustomerselfResourceRecordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
        if 'bill_date_begin' in local_var_params:
            query_params.append(('bill_date_begin', local_var_params['bill_date_begin']))
        if 'bill_date_end' in local_var_params:
            query_params.append(('bill_date_end', local_var_params['bill_date_end']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_free_resource_infos(self, request):
        """查询资源包列表

        功能描述：客户在自建平台查询资源包列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFreeResourceInfos
        :type request: :class:`huaweicloudsdkbssintl.v2.ListFreeResourceInfosRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ListFreeResourceInfosResponse`
        """
        http_info = self._list_free_resource_infos_http_info(request)
        return self._call_api(**http_info)

    def list_free_resource_infos_invoker(self, request):
        http_info = self._list_free_resource_infos_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_free_resource_infos_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/payments/free-resources/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListFreeResourceInfosResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_indirect_partners(self, request):
        """查询云经销商列表

        华为云总经销商（一级经销商）可以查询云经销商（二级经销商）列表。
        
        一级经销商在伙伴中心查询二级经销商列表的方式请参见[这里](https://support.huaweicloud.com/usermanual-bpconsole/dp_120210.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIndirectPartners
        :type request: :class:`huaweicloudsdkbssintl.v2.ListIndirectPartnersRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ListIndirectPartnersResponse`
        """
        http_info = self._list_indirect_partners_http_info(request)
        return self._call_api(**http_info)

    def list_indirect_partners_invoker(self, request):
        http_info = self._list_indirect_partners_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_indirect_partners_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/partners/indirect-partners/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListIndirectPartnersResponse"
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

    def list_invoices(self, request):
        """查询发票列表

        功能描述：查询发票列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInvoices
        :type request: :class:`huaweicloudsdkbssintl.v2.ListInvoicesRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ListInvoicesResponse`
        """
        http_info = self._list_invoices_http_info(request)
        return self._call_api(**http_info)

    def list_invoices_invoker(self, request):
        http_info = self._list_invoices_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_invoices_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{domain_id}/payments/intl-invoices",
            "request_type": request.__class__.__name__,
            "response_type": "ListInvoicesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
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

    def list_monthly_expenditures(self, request):
        """查询消费汇总(客户)

        功能描述：客户可以查询自身的消费汇总单的功能，消费按月汇总。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMonthlyExpenditures
        :type request: :class:`huaweicloudsdkbssintl.v2.ListMonthlyExpendituresRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ListMonthlyExpendituresResponse`
        """
        http_info = self._list_monthly_expenditures_http_info(request)
        return self._call_api(**http_info)

    def list_monthly_expenditures_invoker(self, request):
        http_info = self._list_monthly_expenditures_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_monthly_expenditures_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{domain_id}/customer/account-mgr/bill/monthly-sum",
            "request_type": request.__class__.__name__,
            "response_type": "ListMonthlyExpendituresResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cycle' in local_var_params:
            query_params.append(('cycle', local_var_params['cycle']))
        if 'cloud_service_type_code' in local_var_params:
            query_params.append(('cloud_service_type_code', local_var_params['cloud_service_type_code']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterpriseProjectId', local_var_params['enterprise_project_id']))

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

    def list_on_demand_resource_ratings(self, request):
        """查询按需产品价格

        功能描述：按需资源询价
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOnDemandResourceRatings
        :type request: :class:`huaweicloudsdkbssintl.v2.ListOnDemandResourceRatingsRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ListOnDemandResourceRatingsResponse`
        """
        http_info = self._list_on_demand_resource_ratings_http_info(request)
        return self._call_api(**http_info)

    def list_on_demand_resource_ratings_invoker(self, request):
        http_info = self._list_on_demand_resource_ratings_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_on_demand_resource_ratings_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/bills/ratings/on-demand-resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListOnDemandResourceRatingsResponse"
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

    def list_order_discounts(self, request):
        """查询订单可用折扣

        功能描述：功能介绍客户在伙伴销售平台支付待支付订单时，查询可使用的折扣。只返回商务合同折扣和伙伴授权折扣客户在客户自建平台查看订单可用的优惠券列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOrderDiscounts
        :type request: :class:`huaweicloudsdkbssintl.v2.ListOrderDiscountsRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ListOrderDiscountsResponse`
        """
        http_info = self._list_order_discounts_http_info(request)
        return self._call_api(**http_info)

    def list_order_discounts_invoker(self, request):
        http_info = self._list_order_discounts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_order_discounts_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/orders/customer-orders/order-discounts",
            "request_type": request.__class__.__name__,
            "response_type": "ListOrderDiscountsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_id' in local_var_params:
            query_params.append(('order_id', local_var_params['order_id']))

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

    def list_postpaid_bill_sum(self, request):
        """查询伙伴月度消费账单

        功能描述：伙伴可以查询伙伴月度消费账单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPostpaidBillSum
        :type request: :class:`huaweicloudsdkbssintl.v2.ListPostpaidBillSumRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ListPostpaidBillSumResponse`
        """
        http_info = self._list_postpaid_bill_sum_http_info(request)
        return self._call_api(**http_info)

    def list_postpaid_bill_sum_invoker(self, request):
        http_info = self._list_postpaid_bill_sum_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_postpaid_bill_sum_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/bills/partner-bills/postpaid-bill-summary",
            "request_type": request.__class__.__name__,
            "response_type": "ListPostpaidBillSumResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bill_cycle' in local_var_params:
            query_params.append(('bill_cycle', local_var_params['bill_cycle']))

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

    def list_rate_on_period_detail(self, request):
        """查询包年/包月产品价格

        功能描述：客户在自建平台按照条件查询包年/包月产品开通时候的价格
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRateOnPeriodDetail
        :type request: :class:`huaweicloudsdkbssintl.v2.ListRateOnPeriodDetailRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ListRateOnPeriodDetailResponse`
        """
        http_info = self._list_rate_on_period_detail_http_info(request)
        return self._call_api(**http_info)

    def list_rate_on_period_detail_invoker(self, request):
        http_info = self._list_rate_on_period_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_rate_on_period_detail_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/bills/ratings/period-resources/subscribe-rate",
            "request_type": request.__class__.__name__,
            "response_type": "ListRateOnPeriodDetailResponse"
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

    def list_renew_rate_on_period(self, request):
        """查询待续订包年包月资源的续订金额

        功能描述：客户在自建平台按照条件查询待续订包年/包月资源续订时候的续订金额
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRenewRateOnPeriod
        :type request: :class:`huaweicloudsdkbssintl.v2.ListRenewRateOnPeriodRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ListRenewRateOnPeriodResponse`
        """
        http_info = self._list_renew_rate_on_period_http_info(request)
        return self._call_api(**http_info)

    def list_renew_rate_on_period_invoker(self, request):
        http_info = self._list_renew_rate_on_period_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_renew_rate_on_period_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/bills/ratings/period-resources/renew-rate",
            "request_type": request.__class__.__name__,
            "response_type": "ListRenewRateOnPeriodResponse"
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

    def list_service_resources(self, request):
        """根据云服务类型查询资源列表

        功能描述：伙伴在伙伴销售平台根据云服务类型查询关联的资源类型编码和名称，用于查询按需产品的价格或包年/包月产品的价格。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListServiceResources
        :type request: :class:`huaweicloudsdkbssintl.v2.ListServiceResourcesRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ListServiceResourcesResponse`
        """
        http_info = self._list_service_resources_http_info(request)
        return self._call_api(**http_info)

    def list_service_resources_invoker(self, request):
        http_info = self._list_service_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_service_resources_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/products/service-resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListServiceResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'service_type_code' in local_var_params:
            query_params.append(('service_type_code', local_var_params['service_type_code']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_sub_customer_coupons(self, request):
        """查询优惠券列表

        功能描述：伙伴/客户可以查询自身的优惠券信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSubCustomerCoupons
        :type request: :class:`huaweicloudsdkbssintl.v2.ListSubCustomerCouponsRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ListSubCustomerCouponsResponse`
        """
        http_info = self._list_sub_customer_coupons_http_info(request)
        return self._call_api(**http_info)

    def list_sub_customer_coupons_invoker(self, request):
        http_info = self._list_sub_customer_coupons_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sub_customer_coupons_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/promotions/benefits/coupons",
            "request_type": request.__class__.__name__,
            "response_type": "ListSubCustomerCouponsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

    def list_sub_customers(self, request):
        """查询客户列表

        功能描述：伙伴可以查询合作伙伴的客户信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSubCustomers
        :type request: :class:`huaweicloudsdkbssintl.v2.ListSubCustomersRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ListSubCustomersResponse`
        """
        http_info = self._list_sub_customers_http_info(request)
        return self._call_api(**http_info)

    def list_sub_customers_invoker(self, request):
        http_info = self._list_sub_customers_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sub_customers_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/partners/sub-customers/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListSubCustomersResponse"
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

    def list_usage_types(self, request):
        """查询使用量类型列表

        功能描述：伙伴在伙伴销售平台查询资源的使用量类型列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUsageTypes
        :type request: :class:`huaweicloudsdkbssintl.v2.ListUsageTypesRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ListUsageTypesResponse`
        """
        http_info = self._list_usage_types_http_info(request)
        return self._call_api(**http_info)

    def list_usage_types_invoker(self, request):
        http_info = self._list_usage_types_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_usage_types_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/products/usage-types",
            "request_type": request.__class__.__name__,
            "response_type": "ListUsageTypesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'resource_type_code' in local_var_params:
            query_params.append(('resource_type_code', local_var_params['resource_type_code']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def send_verification_message_code(self, request):
        """发送验证码

        功能描述：客户注册时，如果填写了邮箱，可以向对应的邮箱发送注册验证码，校验信息的正确性。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SendVerificationMessageCode
        :type request: :class:`huaweicloudsdkbssintl.v2.SendVerificationMessageCodeRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.SendVerificationMessageCodeResponse`
        """
        http_info = self._send_verification_message_code_http_info(request)
        return self._call_api(**http_info)

    def send_verification_message_code_invoker(self, request):
        http_info = self._send_verification_message_code_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _send_verification_message_code_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/bases/verificationcode/send",
            "request_type": request.__class__.__name__,
            "response_type": "SendVerificationMessageCodeResponse"
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

    def show_customer_account_balances(self, request):
        """查询账户余额

        功能描述：客户可以查询自身的账户余额。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCustomerAccountBalances
        :type request: :class:`huaweicloudsdkbssintl.v2.ShowCustomerAccountBalancesRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ShowCustomerAccountBalancesResponse`
        """
        http_info = self._show_customer_account_balances_http_info(request)
        return self._call_api(**http_info)

    def show_customer_account_balances_invoker(self, request):
        http_info = self._show_customer_account_balances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_customer_account_balances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/accounts/customer-accounts/balances",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCustomerAccountBalancesResponse"
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

    def show_realname_authentication_review_result(self, request):
        """查询实名认证审核结果

        功能描述：如果实名认证申请或实名认证变更申请的响应中，显示需要人工审核，使用该接口查询审核结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRealnameAuthenticationReviewResult
        :type request: :class:`huaweicloudsdkbssintl.v2.ShowRealnameAuthenticationReviewResultRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ShowRealnameAuthenticationReviewResultResponse`
        """
        http_info = self._show_realname_authentication_review_result_http_info(request)
        return self._call_api(**http_info)

    def show_realname_authentication_review_result_invoker(self, request):
        http_info = self._show_realname_authentication_review_result_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_realname_authentication_review_result_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/customers/realname-auths/result",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRealnameAuthenticationReviewResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'customer_id' in local_var_params:
            query_params.append(('customer_id', local_var_params['customer_id']))

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

    def show_sub_customer_budget(self, request):
        """查询客户预算

        功能描述：查询客户预算
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSubCustomerBudget
        :type request: :class:`huaweicloudsdkbssintl.v2.ShowSubCustomerBudgetRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ShowSubCustomerBudgetResponse`
        """
        http_info = self._show_sub_customer_budget_http_info(request)
        return self._call_api(**http_info)

    def show_sub_customer_budget_invoker(self, request):
        http_info = self._show_sub_customer_budget_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sub_customer_budget_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/partners/sub-customers/budget",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSubCustomerBudgetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'customer_id' in local_var_params:
            query_params.append(('customer_id', local_var_params['customer_id']))
        if 'indirect_partner_id' in local_var_params:
            query_params.append(('indirect_partner_id', local_var_params['indirect_partner_id']))

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

    def unfreeze_sub_customers(self, request):
        """解冻客户账号

        功能描述：解冻伙伴子客户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UnfreezeSubCustomers
        :type request: :class:`huaweicloudsdkbssintl.v2.UnfreezeSubCustomersRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.UnfreezeSubCustomersResponse`
        """
        http_info = self._unfreeze_sub_customers_http_info(request)
        return self._call_api(**http_info)

    def unfreeze_sub_customers_invoker(self, request):
        http_info = self._unfreeze_sub_customers_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _unfreeze_sub_customers_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/partners/sub-customers/unfreeze",
            "request_type": request.__class__.__name__,
            "response_type": "UnfreezeSubCustomersResponse"
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

    def update_period_to_on_demand(self, request):
        """设置或者取消包年/包月资源到期转按需

        功能描述：客户可以设置包年/包月资源到期后转为按需资源计费。包年/包月计费模式到期后，按需的计费模式即生效
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePeriodToOnDemand
        :type request: :class:`huaweicloudsdkbssintl.v2.UpdatePeriodToOnDemandRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.UpdatePeriodToOnDemandResponse`
        """
        http_info = self._update_period_to_on_demand_http_info(request)
        return self._call_api(**http_info)

    def update_period_to_on_demand_invoker(self, request):
        http_info = self._update_period_to_on_demand_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_period_to_on_demand_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/orders/subscriptions/resources/to-on-demand",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePeriodToOnDemandResponse"
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

    def update_sub_customer_budget(self, request):
        """设置客户预算

        功能描述：设置客户预算
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSubCustomerBudget
        :type request: :class:`huaweicloudsdkbssintl.v2.UpdateSubCustomerBudgetRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.UpdateSubCustomerBudgetResponse`
        """
        http_info = self._update_sub_customer_budget_http_info(request)
        return self._call_api(**http_info)

    def update_sub_customer_budget_invoker(self, request):
        http_info = self._update_sub_customer_budget_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_sub_customer_budget_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/partners/sub-customers/budget",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSubCustomerBudgetResponse"
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

    def auto_renewal_resources(self, request):
        """设置包年/包月资源自动续费

        功能描述：客户可以设置包年/包月资源到期后转为按需资源计费
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AutoRenewalResources
        :type request: :class:`huaweicloudsdkbssintl.v2.AutoRenewalResourcesRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.AutoRenewalResourcesResponse`
        """
        http_info = self._auto_renewal_resources_http_info(request)
        return self._call_api(**http_info)

    def auto_renewal_resources_invoker(self, request):
        http_info = self._auto_renewal_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _auto_renewal_resources_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/orders/subscriptions/resources/autorenew/{resource_id}",
            "request_type": request.__class__.__name__,
            "response_type": "AutoRenewalResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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

    def cancel_auto_renewal_resources(self, request):
        """取消包年/包月资源自动续费

        功能描述：取消包年/包月资源自动续费
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelAutoRenewalResources
        :type request: :class:`huaweicloudsdkbssintl.v2.CancelAutoRenewalResourcesRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.CancelAutoRenewalResourcesResponse`
        """
        http_info = self._cancel_auto_renewal_resources_http_info(request)
        return self._call_api(**http_info)

    def cancel_auto_renewal_resources_invoker(self, request):
        http_info = self._cancel_auto_renewal_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_auto_renewal_resources_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/orders/subscriptions/resources/autorenew/{resource_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CancelAutoRenewalResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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

    def cancel_customer_order(self, request):
        """取消待支付订单

        功能描述：客户可以对待支付的订单进行取消操作
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelCustomerOrder
        :type request: :class:`huaweicloudsdkbssintl.v2.CancelCustomerOrderRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.CancelCustomerOrderResponse`
        """
        http_info = self._cancel_customer_order_http_info(request)
        return self._call_api(**http_info)

    def cancel_customer_order_invoker(self, request):
        http_info = self._cancel_customer_order_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_customer_order_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/orders/customer-orders/cancel",
            "request_type": request.__class__.__name__,
            "response_type": "CancelCustomerOrderResponse"
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

    def cancel_resources_subscription(self, request):
        """退订包年/包月资源

        功能描述：客户购买包年/包月资源后，支持客户退订包年/包月实例。退订资源实例包括资源续费部分和当前正在使用的部分，退订后资源将无法使用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelResourcesSubscription
        :type request: :class:`huaweicloudsdkbssintl.v2.CancelResourcesSubscriptionRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.CancelResourcesSubscriptionResponse`
        """
        http_info = self._cancel_resources_subscription_http_info(request)
        return self._call_api(**http_info)

    def cancel_resources_subscription_invoker(self, request):
        http_info = self._cancel_resources_subscription_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_resources_subscription_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/orders/subscriptions/resources/unsubscribe",
            "request_type": request.__class__.__name__,
            "response_type": "CancelResourcesSubscriptionResponse"
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

    def list_customer_orders(self, request):
        """查询订单列表

        功能描述：客户购买包年包月资源后，可以查看待审核、处理中、已取消、已完成和待支付等状态的订单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCustomerOrders
        :type request: :class:`huaweicloudsdkbssintl.v2.ListCustomerOrdersRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ListCustomerOrdersResponse`
        """
        http_info = self._list_customer_orders_http_info(request)
        return self._call_api(**http_info)

    def list_customer_orders_invoker(self, request):
        http_info = self._list_customer_orders_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_customer_orders_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/orders/customer-orders",
            "request_type": request.__class__.__name__,
            "response_type": "ListCustomerOrdersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

    def list_pay_per_use_customer_resources(self, request):
        """查询客户包年/包月资源列表

        功能描述：客户在客户自建平台查询某个或所有的包年/包月资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPayPerUseCustomerResources
        :type request: :class:`huaweicloudsdkbssintl.v2.ListPayPerUseCustomerResourcesRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ListPayPerUseCustomerResourcesResponse`
        """
        http_info = self._list_pay_per_use_customer_resources_http_info(request)
        return self._call_api(**http_info)

    def list_pay_per_use_customer_resources_invoker(self, request):
        http_info = self._list_pay_per_use_customer_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_pay_per_use_customer_resources_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/orders/suscriptions/resources/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListPayPerUseCustomerResourcesResponse"
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

    def pay_orders(self, request):
        """支付包年/包月产品订单

        客户可以对待支付状态的包年/包月产品订单进行支付
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PayOrders
        :type request: :class:`huaweicloudsdkbssintl.v2.PayOrdersRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.PayOrdersResponse`
        """
        http_info = self._pay_orders_http_info(request)
        return self._call_api(**http_info)

    def pay_orders_invoker(self, request):
        http_info = self._pay_orders_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _pay_orders_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/orders/customer-orders/pay",
            "request_type": request.__class__.__name__,
            "response_type": "PayOrdersResponse"
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

    def renewal_resources(self, request):
        """续订包年/包月资源

        功能描述：客户的包年包/月资源即将到期时，可进行包年/包月资源的续订
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RenewalResources
        :type request: :class:`huaweicloudsdkbssintl.v2.RenewalResourcesRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.RenewalResourcesResponse`
        """
        http_info = self._renewal_resources_http_info(request)
        return self._call_api(**http_info)

    def renewal_resources_invoker(self, request):
        http_info = self._renewal_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _renewal_resources_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/orders/subscriptions/resources/renew",
            "request_type": request.__class__.__name__,
            "response_type": "RenewalResourcesResponse"
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

    def show_customer_order_details(self, request):
        """查询订单详情

        功能描述：客户可以查看订单详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCustomerOrderDetails
        :type request: :class:`huaweicloudsdkbssintl.v2.ShowCustomerOrderDetailsRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ShowCustomerOrderDetailsResponse`
        """
        http_info = self._show_customer_order_details_http_info(request)
        return self._call_api(**http_info)

    def show_customer_order_details_invoker(self, request):
        http_info = self._show_customer_order_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_customer_order_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/orders/customer-orders/details/{order_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCustomerOrderDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def show_refund_order_details(self, request):
        """查询退款订单的金额详情

        功能描述：客户在伙伴销售平台查询某次退订订单或者降配订单的退款金额来自哪些资源和对应订单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRefundOrderDetails
        :type request: :class:`huaweicloudsdkbssintl.v2.ShowRefundOrderDetailsRequest`
        :rtype: :class:`huaweicloudsdkbssintl.v2.ShowRefundOrderDetailsResponse`
        """
        http_info = self._show_refund_order_details_http_info(request)
        return self._call_api(**http_info)

    def show_refund_order_details_invoker(self, request):
        http_info = self._show_refund_order_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_refund_order_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/orders/customer-orders/refund-orders",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRefundOrderDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_id' in local_var_params:
            query_params.append(('order_id', local_var_params['order_id']))

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
