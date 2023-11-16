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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkbss'")


class BssClient(Client):
    def __init__(self):
        super(BssClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkbss.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials")
        else:
            if clazz.__name__ != "BssClient":
                raise TypeError("client type error, support client type is BssClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials")

        

        return client_builder

    def list_conversions(self, request):
        """查询度量单位进制

        伙伴在伙伴销售平台上查询度量单位的进制转换信息，用于不同度量单位之间的转换。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConversions
        :type request: :class:`huaweicloudsdkbss.v2.ListConversionsRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListConversionsResponse`
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
        :type request: :class:`huaweicloudsdkbss.v2.ListCostsRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListCostsResponse`
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

    def list_customer_bills_monthly_break_down(self, request):
        """查询月度成本

        客户可以查询指定月份的月度摊销成本。当前仅支持查询近18个月的摊销成本。摊销成本计算规则请参见[成本摊销规则](https://support.huaweicloud.com/usermanual-cost/costcenter_000002_01.html)。
        
        客户可查询的数据范围同成本中心提供的[数据范围](https://support.huaweicloud.com/usermanual-cost/costcenter_0000004.html)一致。
        
        客户登录成本中心导出成本明细请参见[导出成本明细数据](https://support.huaweicloud.com/usermanual-cost/costcenter_000002_03.html)。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;该接口仅面向已开通成本中心的客户开放。如何开启成本中心请参见[这里](https://support.huaweicloud.com/usermanual-cost/costcenter_000004.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCustomerBillsMonthlyBreakDown
        :type request: :class:`huaweicloudsdkbss.v2.ListCustomerBillsMonthlyBreakDownRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListCustomerBillsMonthlyBreakDownResponse`
        """
        http_info = self._list_customer_bills_monthly_break_down_http_info(request)
        return self._call_api(**http_info)

    def list_customer_bills_monthly_break_down_invoker(self, request):
        http_info = self._list_customer_bills_monthly_break_down_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_customer_bills_monthly_break_down_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/costs/cost-analysed-bills/monthly-breakdown",
            "request_type": request.__class__.__name__,
            "response_type": "ListCustomerBillsMonthlyBreakDownResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'shared_month' in local_var_params:
            query_params.append(('shared_month', local_var_params['shared_month']))
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'resource_name' in local_var_params:
            query_params.append(('resource_name', local_var_params['resource_name']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'method' in local_var_params:
            query_params.append(('method', local_var_params['method']))
        if 'sub_customer_id' in local_var_params:
            query_params.append(('sub_customer_id', local_var_params['sub_customer_id']))

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

        客户在伙伴销售平台查询客户的资源包列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFreeResourceInfos
        :type request: :class:`huaweicloudsdkbss.v2.ListFreeResourceInfosRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListFreeResourceInfosResponse`
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

    def list_free_resource_usages(self, request):
        """查询资源包使用量

        客户在伙伴销售平台根据资源项维度查询客户的资源包使用量。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFreeResourceUsages
        :type request: :class:`huaweicloudsdkbss.v2.ListFreeResourceUsagesRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListFreeResourceUsagesResponse`
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
        :type request: :class:`huaweicloudsdkbss.v2.ListFreeResourcesUsageRecordsRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListFreeResourcesUsageRecordsResponse`
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

    def list_incentive_discount_policies(self, request):
        """查询产品的折扣和激励策略

        伙伴在伙伴销售平台上查询产品的折扣和激励策略。
        
        伙伴登录合作伙伴中心查看产品的折扣和激励策略请参见[这里](https://support.huaweicloud.com/usermanual-bpconsole/dp_120400.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIncentiveDiscountPolicies
        :type request: :class:`huaweicloudsdkbss.v2.ListIncentiveDiscountPoliciesRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListIncentiveDiscountPoliciesResponse`
        """
        http_info = self._list_incentive_discount_policies_http_info(request)
        return self._call_api(**http_info)

    def list_incentive_discount_policies_invoker(self, request):
        http_info = self._list_incentive_discount_policies_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_incentive_discount_policies_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/products/incentive-discount-policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListIncentiveDiscountPoliciesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'time' in local_var_params:
            query_params.append(('time', local_var_params['time']))
        if 'service_type_code' in local_var_params:
            query_params.append(('service_type_code', local_var_params['service_type_code']))
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
        """查询度量单位列表

        伙伴在伙伴销售平台上查询资源使用量，包年包月资源的时长及金额的度量单位及名称，度量单位类型等。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMeasureUnits
        :type request: :class:`huaweicloudsdkbss.v2.ListMeasureUnitsRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListMeasureUnitsResponse`
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

    def list_partner_account_change_records(self, request):
        """查询收支明细

        伙伴在伙伴销售平台上查询自身的收支明细情况。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPartnerAccountChangeRecords
        :type request: :class:`huaweicloudsdkbss.v2.ListPartnerAccountChangeRecordsRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListPartnerAccountChangeRecordsResponse`
        """
        http_info = self._list_partner_account_change_records_http_info(request)
        return self._call_api(**http_info)

    def list_partner_account_change_records_invoker(self, request):
        http_info = self._list_partner_account_change_records_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_partner_account_change_records_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/accounts/partner-accounts/account-change-records",
            "request_type": request.__class__.__name__,
            "response_type": "ListPartnerAccountChangeRecordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'balance_type' in local_var_params:
            query_params.append(('balance_type', local_var_params['balance_type']))
        if 'trade_type' in local_var_params:
            query_params.append(('trade_type', local_var_params['trade_type']))
        if 'trade_time_begin' in local_var_params:
            query_params.append(('trade_time_begin', local_var_params['trade_time_begin']))
        if 'trade_time_end' in local_var_params:
            query_params.append(('trade_time_end', local_var_params['trade_time_end']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
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

    def list_resource_types(self, request):
        """查询资源类型列表

        伙伴在伙伴销售平台查询资源类型的列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceTypes
        :type request: :class:`huaweicloudsdkbss.v2.ListResourceTypesRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListResourceTypesResponse`
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
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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

    def list_resource_usage(self, request):
        """查询95计费资源用量明细

        客户在自建平台查询自己的资源使用量明细。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;当前仅支持查询CDN、OBS、IEC和VPC四种云服务类型的资源用量明细，仅针对95计费场景。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceUsage
        :type request: :class:`huaweicloudsdkbss.v2.ListResourceUsageRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListResourceUsageResponse`
        """
        http_info = self._list_resource_usage_http_info(request)
        return self._call_api(**http_info)

    def list_resource_usage_invoker(self, request):
        http_info = self._list_resource_usage_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_resource_usage_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/bills/customer-bills/resources/usage/details",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceUsageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bill_cycle' in local_var_params:
            query_params.append(('bill_cycle', local_var_params['bill_cycle']))
        if 'service_type_code' in local_var_params:
            query_params.append(('service_type_code', local_var_params['service_type_code']))
        if 'resource_type_code' in local_var_params:
            query_params.append(('resource_type_code', local_var_params['resource_type_code']))
        if 'usage_type' in local_var_params:
            query_params.append(('usage_type', local_var_params['usage_type']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
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

    def list_resource_usage_summary(self, request):
        """查询95计费资源用量汇总

        客户在自建平台查询自己的资源使用量汇总。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;-   当前仅支持查询CDN、OBS、IEC和VPC四种云服务类型的资源用量汇总，仅针对95计费场景。
        &gt;-   使用量汇总列表只包含月汇总金额和资源ID，若要查询具体某个资源的用量明细，请调用[查询资源用量明细](https://support.huaweicloud.com/api-oce/zh-cn_topic_0000001190606757.html)接口获取。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceUsageSummary
        :type request: :class:`huaweicloudsdkbss.v2.ListResourceUsageSummaryRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListResourceUsageSummaryResponse`
        """
        http_info = self._list_resource_usage_summary_http_info(request)
        return self._call_api(**http_info)

    def list_resource_usage_summary_invoker(self, request):
        http_info = self._list_resource_usage_summary_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_resource_usage_summary_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/bills/customer-bills/resources/usage/summary",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceUsageSummaryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bill_cycle' in local_var_params:
            query_params.append(('bill_cycle', local_var_params['bill_cycle']))
        if 'service_type_code' in local_var_params:
            query_params.append(('service_type_code', local_var_params['service_type_code']))
        if 'resource_type_code' in local_var_params:
            query_params.append(('resource_type_code', local_var_params['resource_type_code']))
        if 'usage_type' in local_var_params:
            query_params.append(('usage_type', local_var_params['usage_type']))
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
        :type request: :class:`huaweicloudsdkbss.v2.ListServiceTypesRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListServiceTypesResponse`
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
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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

    def list_stored_value_cards(self, request):
        """查询储值卡列表

        客户可以查询已购买的储值卡列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStoredValueCards
        :type request: :class:`huaweicloudsdkbss.v2.ListStoredValueCardsRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListStoredValueCardsResponse`
        """
        http_info = self._list_stored_value_cards_http_info(request)
        return self._call_api(**http_info)

    def list_stored_value_cards_invoker(self, request):
        http_info = self._list_stored_value_cards_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_stored_value_cards_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/promotions/benefits/stored-value-cards",
            "request_type": request.__class__.__name__,
            "response_type": "ListStoredValueCardsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'card_id' in local_var_params:
            query_params.append(('card_id', local_var_params['card_id']))
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

    def list_sub_customer_new_tag(self, request):
        """查询客户新客标签

        伙伴通过该接口可以查询客户的新客标签。
        
        &gt;![](public_sys-resources/icon-caution.gif) **注意：** 
        &gt;-   新客标签失效后，new\\_customer\\_tag会变成N，且有效期过期。
        &gt;-   客户如果没有实名认证，则新客标签为空。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSubCustomerNewTag
        :type request: :class:`huaweicloudsdkbss.v2.ListSubCustomerNewTagRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListSubCustomerNewTagResponse`
        """
        http_info = self._list_sub_customer_new_tag_http_info(request)
        return self._call_api(**http_info)

    def list_sub_customer_new_tag_invoker(self, request):
        http_info = self._list_sub_customer_new_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sub_customer_new_tag_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/partners/sub-customers/new-customers-tags/batch-query",
            "request_type": request.__class__.__name__,
            "response_type": "ListSubCustomerNewTagResponse"
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

    def change_enterprise_realname_authentication(self, request):
        """申请实名认证变更

        客户可以进行实名认证变更申请。
        
        个人客户登录帐号中心通过实名认证变更为企业帐号的方式及流程请参见[这里](https://support.huaweicloud.com/usermanual-account/zh-cn_topic_0103532632.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeEnterpriseRealnameAuthentication
        :type request: :class:`huaweicloudsdkbss.v2.ChangeEnterpriseRealnameAuthenticationRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ChangeEnterpriseRealnameAuthenticationResponse`
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

        客户注册时可检查客户的登录名称、手机号或者邮箱是否可以用于注册。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;针对校验手机号场景，目前仅支持校验手机号注册数量是否超过上限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckUserIdentity
        :type request: :class:`huaweicloudsdkbss.v2.CheckUserIdentityRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.CheckUserIdentityResponse`
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

    def claim_enterprise_multi_account_coupon(self, request):
        """企业主账号向企业子账号拨款优惠券

        企业主账号在自建平台向企业子账号拨款优惠券。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;-   仅支持华为发放的测试类、商务类、活动类代金券。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ClaimEnterpriseMultiAccountCoupon
        :type request: :class:`huaweicloudsdkbss.v2.ClaimEnterpriseMultiAccountCouponRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ClaimEnterpriseMultiAccountCouponResponse`
        """
        http_info = self._claim_enterprise_multi_account_coupon_http_info(request)
        return self._call_api(**http_info)

    def claim_enterprise_multi_account_coupon_invoker(self, request):
        http_info = self._claim_enterprise_multi_account_coupon_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _claim_enterprise_multi_account_coupon_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/enterprises/multi-accounts/transfer-coupon",
            "request_type": request.__class__.__name__,
            "response_type": "ClaimEnterpriseMultiAccountCouponResponse"
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

    def create_enterprise_project_auth(self, request):
        """开通客户企业项目权限

        客户在自建平台开通客户企业项目权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEnterpriseProjectAuth
        :type request: :class:`huaweicloudsdkbss.v2.CreateEnterpriseProjectAuthRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.CreateEnterpriseProjectAuthResponse`
        """
        http_info = self._create_enterprise_project_auth_http_info(request)
        return self._call_api(**http_info)

    def create_enterprise_project_auth_invoker(self, request):
        http_info = self._create_enterprise_project_auth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_enterprise_project_auth_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/enterprises/enterprise-projects/authority",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEnterpriseProjectAuthResponse"
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

    def create_enterprise_realname_authentication(self, request):
        """申请企业实名认证

        企业客户可以进行企业实名认证申请。
        
        客户登录帐号中心进行企业实名认证的方式及流程请参见[这里](https://support.huaweicloud.com/usermanual-account/zh-cn_topic_0077914253.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEnterpriseRealnameAuthentication
        :type request: :class:`huaweicloudsdkbss.v2.CreateEnterpriseRealnameAuthenticationRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.CreateEnterpriseRealnameAuthenticationResponse`
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

    def create_partner_coupons(self, request):
        """发放优惠券

        合作伙伴可以在拥有的代金券额度范围内为客户下发优惠券。
        
        伙伴登录合作伙伴中心为客户发放代金券请参见[这里](https://support.huaweicloud.com/usermanual-bpconsole/espp_050502.html)。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;只能给代售子客户发放优惠券。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePartnerCoupons
        :type request: :class:`huaweicloudsdkbss.v2.CreatePartnerCouponsRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.CreatePartnerCouponsResponse`
        """
        http_info = self._create_partner_coupons_http_info(request)
        return self._call_api(**http_info)

    def create_partner_coupons_invoker(self, request):
        http_info = self._create_partner_coupons_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_partner_coupons_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/promotions/benefits/partner-coupons",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePartnerCouponsResponse"
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

        个人客户可以进行个人实名认证申请。
        
        客户登录帐号中心进行个人实名认证的方式及流程请参见[这里](https://support.huaweicloud.com/usermanual-account/zh-cn_topic_0077914254.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePersonalRealnameAuth
        :type request: :class:`huaweicloudsdkbss.v2.CreatePersonalRealnameAuthRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.CreatePersonalRealnameAuthResponse`
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

        在伙伴销售平台创建客户时同步创建华为云账号，并将客户在伙伴销售平台上的账号与华为云账号进行映射。同时，创建的华为云账号与伙伴账号关联绑定。
        
        华为云总经销商（一级经销商）可以注册云经销商（二级经销商）的子客户。注册完成后，子客户可以自动和云经销商绑定。
        
        &gt;![](public_sys-resources/icon-caution.gif) **注意：** 
        &gt;-   调用该接口为客户创建华为云账号后，如果想从合作伙伴销售平台跳转至华为云官网，还需要进行SAML认证，具体请参见“[Web UI方式](https://support.huaweicloud.com/api-bpconsole/jac_00001.html)”中的“SAML认证”。
        &gt;-   如果创建的时候不输入手机号，那么客户将无法收到华为云发出的任何提醒短信，需要客户自己登录到华为云平台补充手机号。
        &gt;-   调用“创建客户”接口时，华为云会同步创建华为云客户账号，将客户ID及账号名返回给伙伴平台，然后华为云异步完成客户与伙伴的关联。伙伴与客户的关联结果可通过“[查询客户列表](https://support.huaweicloud.com/api-bpconsole/mc_00021.html)”查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSubCustomer
        :type request: :class:`huaweicloudsdkbss.v2.CreateSubCustomerRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.CreateSubCustomerResponse`
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

    def create_sub_enterprise_account(self, request):
        """创建企业子账号

        企业主账号在自建平台创建企业子账号。
        
        企业主账号创建企业子账号请参见[这里](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0104194162.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSubEnterpriseAccount
        :type request: :class:`huaweicloudsdkbss.v2.CreateSubEnterpriseAccountRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.CreateSubEnterpriseAccountResponse`
        """
        http_info = self._create_sub_enterprise_account_http_info(request)
        return self._call_api(**http_info)

    def create_sub_enterprise_account_invoker(self, request):
        http_info = self._create_sub_enterprise_account_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_sub_enterprise_account_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/enterprises/multi-accounts/sub-customers",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSubEnterpriseAccountResponse"
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

    def list_cities(self, request):
        """查询城市信息

        伙伴在伙伴销售平台上查询城市信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCities
        :type request: :class:`huaweicloudsdkbss.v2.ListCitiesRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListCitiesResponse`
        """
        http_info = self._list_cities_http_info(request)
        return self._call_api(**http_info)

    def list_cities_invoker(self, request):
        http_info = self._list_cities_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_cities_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/systems/configs/cities",
            "request_type": request.__class__.__name__,
            "response_type": "ListCitiesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

    def list_consume_sub_customers(self, request):
        """查询伙伴消费子客户列表

        伙伴在伙伴销售平台可实时查询消费账期内的子客户列表，可以用于查询子客户的消费记录。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;若当前子客户与伙伴无关联关系，仍可查询账期内处于关联状态且有消费的子客户列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConsumeSubCustomers
        :type request: :class:`huaweicloudsdkbss.v2.ListConsumeSubCustomersRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListConsumeSubCustomersResponse`
        """
        http_info = self._list_consume_sub_customers_http_info(request)
        return self._call_api(**http_info)

    def list_consume_sub_customers_invoker(self, request):
        http_info = self._list_consume_sub_customers_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_consume_sub_customers_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/bills/subcustomer-bills/res-fee-records/sub-customers/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListConsumeSubCustomersResponse"
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

    def list_counties(self, request):
        """查询区县信息

        伙伴在伙伴销售平台上查询区县信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCounties
        :type request: :class:`huaweicloudsdkbss.v2.ListCountiesRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListCountiesResponse`
        """
        http_info = self._list_counties_http_info(request)
        return self._call_api(**http_info)

    def list_counties_invoker(self, request):
        http_info = self._list_counties_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_counties_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/systems/configs/counties",
            "request_type": request.__class__.__name__,
            "response_type": "ListCountiesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

    def list_coupon_quotas_records(self, request):
        """查询代金券额度的发放回收记录

        华为云总经销商（一级经销商）可以查看给云经销商（二级经销商）发放或回收代金券额度的操作记录。
        
        一级经销商可以登录伙伴中心，进入“客户业务** **\\&gt; 代金券管理”，选择“代金券额度”页签，单击“操作记录”查看代金券额度的发放和回收记录。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;伙伴也可以单击代金券额度所在行的“操作记录”，查看该代金券额度对应的操作记录日志。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCouponQuotasRecords
        :type request: :class:`huaweicloudsdkbss.v2.ListCouponQuotasRecordsRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListCouponQuotasRecordsResponse`
        """
        http_info = self._list_coupon_quotas_records_http_info(request)
        return self._call_api(**http_info)

    def list_coupon_quotas_records_invoker(self, request):
        http_info = self._list_coupon_quotas_records_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_coupon_quotas_records_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/partners/coupon-quotas/records",
            "request_type": request.__class__.__name__,
            "response_type": "ListCouponQuotasRecordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

    def list_customer_account_change_records(self, request):
        """查询收支明细(客户)

        功能描述：客户可以查询自身的收支明细情况(此接口不适用于伙伴的代售类、转售类客户。)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCustomerAccountChangeRecords
        :type request: :class:`huaweicloudsdkbss.v2.ListCustomerAccountChangeRecordsRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListCustomerAccountChangeRecordsResponse`
        """
        http_info = self._list_customer_account_change_records_http_info(request)
        return self._call_api(**http_info)

    def list_customer_account_change_records_invoker(self, request):
        http_info = self._list_customer_account_change_records_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_customer_account_change_records_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/accounts/customer-accounts/account-change-records",
            "request_type": request.__class__.__name__,
            "response_type": "ListCustomerAccountChangeRecordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'balance_type' in local_var_params:
            query_params.append(('balance_type', local_var_params['balance_type']))
        if 'revenue_expense_type' in local_var_params:
            query_params.append(('revenue_expense_type', local_var_params['revenue_expense_type']))
        if 'trade_type' in local_var_params:
            query_params.append(('trade_type', local_var_params['trade_type']))
        if 'trade_time_begin' in local_var_params:
            query_params.append(('trade_time_begin', local_var_params['trade_time_begin']))
        if 'trade_time_end' in local_var_params:
            query_params.append(('trade_time_end', local_var_params['trade_time_end']))
        if 'trade_id' in local_var_params:
            query_params.append(('trade_id', local_var_params['trade_id']))
        if 'payment_channel_id' in local_var_params:
            query_params.append(('payment_channel_id', local_var_params['payment_channel_id']))
        if 'payment_channel_no' in local_var_params:
            query_params.append(('payment_channel_no', local_var_params['payment_channel_no']))
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

    def list_customer_bills_fee_records(self, request):
        """查询流水账单

        客户在自建平台查询自己的消费流水账单。
        
        客户登录费用中心查询自己的消费流水账单请参见[这里](https://support.huaweicloud.com/usermanual-billing/bills-topic_80000001.html#bills-topic_80000001__zh-cn_topic_0000001162496407_s716e04d5d0ba4e9d9a76a8bcbfbcfe73)的“**查看流水账单**”。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCustomerBillsFeeRecords
        :type request: :class:`huaweicloudsdkbss.v2.ListCustomerBillsFeeRecordsRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListCustomerBillsFeeRecordsResponse`
        """
        http_info = self._list_customer_bills_fee_records_http_info(request)
        return self._call_api(**http_info)

    def list_customer_bills_fee_records_invoker(self, request):
        http_info = self._list_customer_bills_fee_records_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_customer_bills_fee_records_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/bills/customer-bills/fee-records",
            "request_type": request.__class__.__name__,
            "response_type": "ListCustomerBillsFeeRecordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

    def list_customer_on_demand_resources(self, request):
        """查询客户按需资源列表

        合作伙伴可以查询关联的代售类客户已开通的按需资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCustomerOnDemandResources
        :type request: :class:`huaweicloudsdkbss.v2.ListCustomerOnDemandResourcesRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListCustomerOnDemandResourcesResponse`
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

    def list_customers_balances_detail(self, request):
        """查询客户账户余额

        合作伙伴可以查询关联的代售类客户的账户余额。
        
        伙伴登录伙伴中心查询客户余额请参见[这里](https://support.huaweicloud.com/usermanual-bpconsole/zh-cn_topic_0072435115.html)。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;顾问销售类客户是客户在华为云充值，合作伙伴无法调用此接口查询其账户余额。代售类客户的账户由合作伙伴拨款，所以可以查询到。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCustomersBalancesDetail
        :type request: :class:`huaweicloudsdkbss.v2.ListCustomersBalancesDetailRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListCustomersBalancesDetailResponse`
        """
        http_info = self._list_customers_balances_detail_http_info(request)
        return self._call_api(**http_info)

    def list_customers_balances_detail_invoker(self, request):
        http_info = self._list_customers_balances_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_customers_balances_detail_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/accounts/customer-accounts/balances/batch-query",
            "request_type": request.__class__.__name__,
            "response_type": "ListCustomersBalancesDetailResponse"
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

    def list_customerself_resource_record_details(self, request):
        """查询资源详单

        客户在自建平台查询自己的资源详单，用于反映各类资源的消耗情况。
        
        客户登录费用中心查询资源详单请参见[这里](https://support.huaweicloud.com/usermanual-billing/bills_topic_100000063.html)。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;由于资源消费呈现的是资源维度的8位小数原始消费金额，实际从账户扣费时按2位小数进行扣费（即扣到分），会存在精度差异，所以，不推荐消费汇总和资源消费直接对账。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCustomerselfResourceRecordDetails
        :type request: :class:`huaweicloudsdkbss.v2.ListCustomerselfResourceRecordDetailsRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListCustomerselfResourceRecordDetailsResponse`
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

        客户在自建平台查询每个资源的消费明细数据。
        
        客户登录费用中心查询资源消费记录请参见[这里](https://support.huaweicloud.com/usermanual-billing/bills_topic_100000061.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCustomerselfResourceRecords
        :type request: :class:`huaweicloudsdkbss.v2.ListCustomerselfResourceRecordsRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListCustomerselfResourceRecordsResponse`
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

    def list_enterprise_multi_account(self, request):
        """查询企业子账号可回收余额

        企业主账号在自建平台查询企业子账号的可回收余额。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEnterpriseMultiAccount
        :type request: :class:`huaweicloudsdkbss.v2.ListEnterpriseMultiAccountRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListEnterpriseMultiAccountResponse`
        """
        http_info = self._list_enterprise_multi_account_http_info(request)
        return self._call_api(**http_info)

    def list_enterprise_multi_account_invoker(self, request):
        http_info = self._list_enterprise_multi_account_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_enterprise_multi_account_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/enterprises/multi-accounts/retrieve-amount",
            "request_type": request.__class__.__name__,
            "response_type": "ListEnterpriseMultiAccountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

    def list_enterprise_organizations(self, request):
        """查询企业组织结构

        企业主账号在自建平台查询企业组织结构。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEnterpriseOrganizations
        :type request: :class:`huaweicloudsdkbss.v2.ListEnterpriseOrganizationsRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListEnterpriseOrganizationsResponse`
        """
        http_info = self._list_enterprise_organizations_http_info(request)
        return self._call_api(**http_info)

    def list_enterprise_organizations_invoker(self, request):
        http_info = self._list_enterprise_organizations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_enterprise_organizations_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/enterprises/multi-accounts/enterprise-organizations",
            "request_type": request.__class__.__name__,
            "response_type": "ListEnterpriseOrganizationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'recursive_query' in local_var_params:
            query_params.append(('recursive_query', local_var_params['recursive_query']))
        if 'parent_id' in local_var_params:
            query_params.append(('parent_id', local_var_params['parent_id']))

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

    def list_enterprise_sub_customers(self, request):
        """查询企业子账号列表

        企业主账号在自建平台查询企业子账号信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEnterpriseSubCustomers
        :type request: :class:`huaweicloudsdkbss.v2.ListEnterpriseSubCustomersRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListEnterpriseSubCustomersResponse`
        """
        http_info = self._list_enterprise_sub_customers_http_info(request)
        return self._call_api(**http_info)

    def list_enterprise_sub_customers_invoker(self, request):
        http_info = self._list_enterprise_sub_customers_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_enterprise_sub_customers_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/enterprises/multi-accounts/sub-customers",
            "request_type": request.__class__.__name__,
            "response_type": "ListEnterpriseSubCustomersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

    def list_indirect_partners(self, request):
        """查询云经销商列表

        华为云总经销商（一级经销商）可以查询云经销商（二级经销商）列表。
        
        一级经销商在伙伴中心查询二级经销商列表的方式请参见[这里](https://support.huaweicloud.com/usermanual-bpconsole/dp_120210.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIndirectPartners
        :type request: :class:`huaweicloudsdkbss.v2.ListIndirectPartnersRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListIndirectPartnersResponse`
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

    def list_issued_coupon_quotas(self, request):
        """查询已发放的代金券额度

        华为云总经销商（一级经销商）可以查看发放给云经销商（二级经销商）的代金券额度列表。
        
        一级经销商登录伙伴中心，进入“客户业务** **\\&gt; 代金券管理”，选择“已发放代金券额度”可查看代金券额度列表。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;调用该接口之前，需通过客户经理联系华为运营人员，为合作伙伴设置代金券发放额度。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIssuedCouponQuotas
        :type request: :class:`huaweicloudsdkbss.v2.ListIssuedCouponQuotasRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListIssuedCouponQuotasResponse`
        """
        http_info = self._list_issued_coupon_quotas_http_info(request)
        return self._call_api(**http_info)

    def list_issued_coupon_quotas_invoker(self, request):
        http_info = self._list_issued_coupon_quotas_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_issued_coupon_quotas_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/partners/issued-coupon-quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ListIssuedCouponQuotasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

    def list_issued_partner_coupons(self, request):
        """查询已发放的优惠券

        合作伙伴可以查询已发放的优惠券列表。
        
        伙伴登录伙伴中心，进入“客户业务** **\\&gt; 代金券管理”，选择“已发放代金券”页签，即可查询已发放的代金券。
        
        伙伴登录伙伴中心，进入“客户业务 \\&gt; 现金券管理”，选择“已发放现金券”页签，即可查询已发放的现金券。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;-   只可查到失效时间在12个月内的代金/现金劵。
        &gt;-   在API只可以查询代售子客户已发放的代金/现金劵，在伙伴中心可以查询代售和顾问销售已发放的代金/现金劵，对比一致性时需要注意关联模式是否一致。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIssuedPartnerCoupons
        :type request: :class:`huaweicloudsdkbss.v2.ListIssuedPartnerCouponsRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListIssuedPartnerCouponsResponse`
        """
        http_info = self._list_issued_partner_coupons_http_info(request)
        return self._call_api(**http_info)

    def list_issued_partner_coupons_invoker(self, request):
        http_info = self._list_issued_partner_coupons_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_issued_partner_coupons_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/promotions/benefits/partner-coupons",
            "request_type": request.__class__.__name__,
            "response_type": "ListIssuedPartnerCouponsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

    def list_multi_account_retrieve_coupons(self, request):
        """查询企业子账号可回收优惠券列表

        企业主账号在自建平台查询企业子账号的可回收优惠券。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;-   仅支持华为发放的测试类、商务类、活动类代金券。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMultiAccountRetrieveCoupons
        :type request: :class:`huaweicloudsdkbss.v2.ListMultiAccountRetrieveCouponsRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListMultiAccountRetrieveCouponsResponse`
        """
        http_info = self._list_multi_account_retrieve_coupons_http_info(request)
        return self._call_api(**http_info)

    def list_multi_account_retrieve_coupons_invoker(self, request):
        http_info = self._list_multi_account_retrieve_coupons_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_multi_account_retrieve_coupons_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/enterprises/multi-accounts/retrieve-coupons",
            "request_type": request.__class__.__name__,
            "response_type": "ListMultiAccountRetrieveCouponsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sub_customer_id' in local_var_params:
            query_params.append(('sub_customer_id', local_var_params['sub_customer_id']))
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

    def list_multi_account_transfer_coupons(self, request):
        """查询企业主账号可拨款优惠券列表

        企业主账号在自建平台查询自己的可拨款优惠券列表。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;-   仅支持华为发放的测试类、商务类、活动类代金券。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMultiAccountTransferCoupons
        :type request: :class:`huaweicloudsdkbss.v2.ListMultiAccountTransferCouponsRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListMultiAccountTransferCouponsResponse`
        """
        http_info = self._list_multi_account_transfer_coupons_http_info(request)
        return self._call_api(**http_info)

    def list_multi_account_transfer_coupons_invoker(self, request):
        http_info = self._list_multi_account_transfer_coupons_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_multi_account_transfer_coupons_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/enterprises/multi-accounts/transfer-coupons",
            "request_type": request.__class__.__name__,
            "response_type": "ListMultiAccountTransferCouponsResponse"
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

        伙伴在销售平台按照条件查询按需产品的价格。
        
        如果购买该产品的租户享受折扣，可以在查询结果中返回折扣金额以及扣除折扣后的最后成交价。
        
        如果该租户享受多种折扣，系统会优先返回客户享受的商务折扣的折扣金额和最终成交价。
        
        &gt;![](public_sys-resources/icon-caution.gif) **注意：** 
        &gt;华为云根据云服务类型、资源类型、云服务区和资源规格四个条件来查询产品，查询时请确认这4个查询条件均输入正确，否则该接口会返回无法找到产品的错误。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOnDemandResourceRatings
        :type request: :class:`huaweicloudsdkbss.v2.ListOnDemandResourceRatingsRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListOnDemandResourceRatingsResponse`
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

        客户在伙伴销售平台支付待支付订单时，查询可使用的折扣信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOrderDiscounts
        :type request: :class:`huaweicloudsdkbss.v2.ListOrderDiscountsRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListOrderDiscountsResponse`
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

    def list_partner_adjust_records(self, request):
        """查询调账记录

        伙伴在伙伴销售平台查询向客户及关联的云经销商（二级经销商）拨款或回收的调账记录。
        
        伙伴登录伙伴中心，在“拨款”或“回收”页面，单击“调账记录”，可以查看一级经销商为二级经销商调账的记录。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPartnerAdjustRecords
        :type request: :class:`huaweicloudsdkbss.v2.ListPartnerAdjustRecordsRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListPartnerAdjustRecordsResponse`
        """
        http_info = self._list_partner_adjust_records_http_info(request)
        return self._call_api(**http_info)

    def list_partner_adjust_records_invoker(self, request):
        http_info = self._list_partner_adjust_records_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_partner_adjust_records_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/accounts/partner-accounts/adjust-records",
            "request_type": request.__class__.__name__,
            "response_type": "ListPartnerAdjustRecordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

    def list_partner_balances(self, request):
        """查询云经销商账户余额

        华为云总经销商（一级经销商）可以查询关联的云经销商（二级经销商）的账户余额；云经销商伙伴可以查询自己的账户余额。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPartnerBalances
        :type request: :class:`huaweicloudsdkbss.v2.ListPartnerBalancesRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListPartnerBalancesResponse`
        """
        http_info = self._list_partner_balances_http_info(request)
        return self._call_api(**http_info)

    def list_partner_balances_invoker(self, request):
        http_info = self._list_partner_balances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_partner_balances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/accounts/partner-accounts/balances",
            "request_type": request.__class__.__name__,
            "response_type": "ListPartnerBalancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

    def list_partner_coupons_record(self, request):
        """查询优惠券的发放回收记录

        合作伙伴可查看给客户发放和回收优惠券的操作记录。
        
        合作伙伴登录伙伴中心查看、导出代金券操作日志请参见[这里](https://support.huaweicloud.com/usermanual-bpconsole/zh-cn_topic_0072435103.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPartnerCouponsRecord
        :type request: :class:`huaweicloudsdkbss.v2.ListPartnerCouponsRecordRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListPartnerCouponsRecordResponse`
        """
        http_info = self._list_partner_coupons_record_http_info(request)
        return self._call_api(**http_info)

    def list_partner_coupons_record_invoker(self, request):
        http_info = self._list_partner_coupons_record_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_partner_coupons_record_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/promotions/benefits/partner-coupons/records/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListPartnerCouponsRecordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

    def list_provinces(self, request):
        """查询省份信息

        伙伴在伙伴销售平台上查询省份信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProvinces
        :type request: :class:`huaweicloudsdkbss.v2.ListProvincesRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListProvincesResponse`
        """
        http_info = self._list_provinces_http_info(request)
        return self._call_api(**http_info)

    def list_provinces_invoker(self, request):
        http_info = self._list_provinces_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_provinces_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/systems/configs/provinces",
            "request_type": request.__class__.__name__,
            "response_type": "ListProvincesResponse"
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

    def list_quota_coupons(self, request):
        """查询优惠券额度

        合作伙伴可以查看所拥有的优惠劵额度。
        
        伙伴登录合作伙伴中心查看所拥有的代金券额度请参见[这里](https://support.huaweicloud.com/usermanual-bpconsole/zh-cn_topic_0072435100.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQuotaCoupons
        :type request: :class:`huaweicloudsdkbss.v2.ListQuotaCouponsRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListQuotaCouponsResponse`
        """
        http_info = self._list_quota_coupons_http_info(request)
        return self._call_api(**http_info)

    def list_quota_coupons_invoker(self, request):
        http_info = self._list_quota_coupons_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_quota_coupons_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/partners/coupon-quotas/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListQuotaCouponsResponse"
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

    def list_rate_on_period_detail(self, request):
        """查询包年/包月产品价格

        伙伴在销售平台按照条件查询包年/包月产品开通时候的价格。
        
        如果购买该产品的客户享受折扣，可以在查询结果中返回折扣金额以及扣除折扣后的最后成交价。
        
        如果该客户享受多种折扣，系统会返回每种折扣的批价结果。如果客户在下单的时候选择自动支付，则系统会优先应用商务折扣的批价结果。
        
        &gt;![](public_sys-resources/icon-caution.gif) **注意：** 
        &gt;华为云根据云服务类型、资源类型、云服务区和资源规格四个条件来查询产品，查询时请确认这4个查询条件均输入正确，否则该接口会返回无法找到产品的错误。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRateOnPeriodDetail
        :type request: :class:`huaweicloudsdkbss.v2.ListRateOnPeriodDetailRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListRateOnPeriodDetailResponse`
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
        :type request: :class:`huaweicloudsdkbss.v2.ListRenewRateOnPeriodRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListRenewRateOnPeriodResponse`
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

        伙伴在伙伴销售平台根据云服务类型查询关联的资源类型编码和名称，用于查询按需产品的价格或包年/包月产品的价格。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListServiceResources
        :type request: :class:`huaweicloudsdkbss.v2.ListServiceResourcesRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListServiceResourcesResponse`
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
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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

    def list_sub_customer_bill_detail(self, request):
        """查询伙伴子客户消费记录

        伙伴在伙伴销售平台可实时查询子客户的消费记录，了解客户的资源消耗情况。
        
        伙伴在伙伴中心查询客户消费明细请参见[这里](https://support.huaweicloud.com/usermanual-bpconsole/zh-cn_topic_0072435155.html)。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;-   消费记录支持查询18个月内的记录。
        &gt;-   如果是客户经理主管来查询，只支持按照单个客户经理查询，必须输入客户经理ID。
        &gt;-   目前支持伙伴查询所有子客户（包含代售类和顾问销售类）的消费记录。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSubCustomerBillDetail
        :type request: :class:`huaweicloudsdkbss.v2.ListSubCustomerBillDetailRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListSubCustomerBillDetailResponse`
        """
        http_info = self._list_sub_customer_bill_detail_http_info(request)
        return self._call_api(**http_info)

    def list_sub_customer_bill_detail_invoker(self, request):
        http_info = self._list_sub_customer_bill_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sub_customer_bill_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/bills/subcustomer-bills/res-fee-records",
            "request_type": request.__class__.__name__,
            "response_type": "ListSubCustomerBillDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bill_cycle' in local_var_params:
            query_params.append(('bill_cycle', local_var_params['bill_cycle']))
        if 'customer_id' in local_var_params:
            query_params.append(('customer_id', local_var_params['customer_id']))
        if 'service_type_code' in local_var_params:
            query_params.append(('service_type_code', local_var_params['service_type_code']))
        if 'region_code' in local_var_params:
            query_params.append(('region_code', local_var_params['region_code']))
        if 'charging_mode' in local_var_params:
            query_params.append(('charging_mode', local_var_params['charging_mode']))
        if 'bill_detail_type' in local_var_params:
            query_params.append(('bill_detail_type', local_var_params['bill_detail_type']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'resource_name' in local_var_params:
            query_params.append(('resource_name', local_var_params['resource_name']))
        if 'trade_id' in local_var_params:
            query_params.append(('trade_id', local_var_params['trade_id']))
        if 'account_manager_id' in local_var_params:
            query_params.append(('account_manager_id', local_var_params['account_manager_id']))
        if 'association_type' in local_var_params:
            query_params.append(('association_type', local_var_params['association_type']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'indirect_partner_id' in local_var_params:
            query_params.append(('indirect_partner_id', local_var_params['indirect_partner_id']))
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

    def list_sub_customer_coupons(self, request):
        """查询优惠券列表

        伙伴可以查询自身的优惠券信息。
        
        伙伴登录伙伴中心查询已发放代金券列表请参见[这里](https://support.huaweicloud.com/usermanual-bpconsole/zh-cn_topic_0072435101.html)，查看已下发代金券的内容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSubCustomerCoupons
        :type request: :class:`huaweicloudsdkbss.v2.ListSubCustomerCouponsRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListSubCustomerCouponsResponse`
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

    def list_sub_customers(self, request):
        """查询客户列表

        伙伴可以查询合作伙伴的客户信息列表。
        
        伙伴登录合作伙伴中心查询客户信息列表请参见[这里](https://support.huaweicloud.com/usermanual-bpconsole/zh-cn_topic_0072435115.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSubCustomers
        :type request: :class:`huaweicloudsdkbss.v2.ListSubCustomersRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListSubCustomersResponse`
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

    def list_subcustomer_monthly_bills(self, request):
        """查询客户月度消费账单

        合作伙伴可查询客户的消费汇总账单，消费按月汇总。
        
        伙伴在伙伴中心查询客户月度消费账单请参见[这里](https://support.huaweicloud.com/usermanual-bpconsole/zh-cn_topic_0072435154.html)。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;消费汇总数据仅包含前一天24点前的数据。每天刷新一次，更新前一天的数据。
        &gt;该接口用于合作伙伴查询其代售类客户在华为的消费情况，如果输入某个客户ID，则是查询单个客户的，否则是查询该伙伴下所有使用伙伴拨款消费的客户的消费记录（包括退订记录）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSubcustomerMonthlyBills
        :type request: :class:`huaweicloudsdkbss.v2.ListSubcustomerMonthlyBillsRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListSubcustomerMonthlyBillsResponse`
        """
        http_info = self._list_subcustomer_monthly_bills_http_info(request)
        return self._call_api(**http_info)

    def list_subcustomer_monthly_bills_invoker(self, request):
        http_info = self._list_subcustomer_monthly_bills_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_subcustomer_monthly_bills_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/bills/partner-bills/subcustomer-bills/monthly-sum",
            "request_type": request.__class__.__name__,
            "response_type": "ListSubcustomerMonthlyBillsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

    def list_usage_types(self, request):
        """查询使用量类型列表

        伙伴在伙伴销售平台查询资源的使用量类型列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUsageTypes
        :type request: :class:`huaweicloudsdkbss.v2.ListUsageTypesRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListUsageTypesResponse`
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

    def reclaim_coupon_quotas(self, request):
        """回收云经销商的代金券额度

        华为云总经销商（一级经销商）可以回收已发放给云经销商（二级经销商）的代金券额度。
        
        一级经销商在伙伴中心回收已发放给二级经销商的代金券额度请参见[这里](https://support.huaweicloud.com/usermanual-bpconsole/dp_120206.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ReclaimCouponQuotas
        :type request: :class:`huaweicloudsdkbss.v2.ReclaimCouponQuotasRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ReclaimCouponQuotasResponse`
        """
        http_info = self._reclaim_coupon_quotas_http_info(request)
        return self._call_api(**http_info)

    def reclaim_coupon_quotas_invoker(self, request):
        http_info = self._reclaim_coupon_quotas_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reclaim_coupon_quotas_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/partners/coupon-quotas/indirect-partner-reclaim",
            "request_type": request.__class__.__name__,
            "response_type": "ReclaimCouponQuotasResponse"
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

    def reclaim_enterprise_multi_account_coupon(self, request):
        """企业主账号从企业子账号回收优惠券

        企业主账号在自建平台回收给企业子账号的拨款优惠券。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;-   仅支持华为发放的测试类、商务类、活动类代金券。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ReclaimEnterpriseMultiAccountCoupon
        :type request: :class:`huaweicloudsdkbss.v2.ReclaimEnterpriseMultiAccountCouponRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ReclaimEnterpriseMultiAccountCouponResponse`
        """
        http_info = self._reclaim_enterprise_multi_account_coupon_http_info(request)
        return self._call_api(**http_info)

    def reclaim_enterprise_multi_account_coupon_invoker(self, request):
        http_info = self._reclaim_enterprise_multi_account_coupon_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reclaim_enterprise_multi_account_coupon_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/enterprises/multi-accounts/retrieve-coupon",
            "request_type": request.__class__.__name__,
            "response_type": "ReclaimEnterpriseMultiAccountCouponResponse"
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

    def reclaim_indirect_partner_account(self, request):
        """回收云经销商账户拨款

        华为云总经销商（一级经销商）可以回收云经销商（二级经销商）的账户余额。
        
        一级经销商在伙伴中心回收二级经销商账户拨款请参见[这里](https://support.huaweicloud.com/usermanual-bpconsole/dp_120205.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ReclaimIndirectPartnerAccount
        :type request: :class:`huaweicloudsdkbss.v2.ReclaimIndirectPartnerAccountRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ReclaimIndirectPartnerAccountResponse`
        """
        http_info = self._reclaim_indirect_partner_account_http_info(request)
        return self._call_api(**http_info)

    def reclaim_indirect_partner_account_invoker(self, request):
        http_info = self._reclaim_indirect_partner_account_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reclaim_indirect_partner_account_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/accounts/partner-accounts/indirect-partner-reclaim",
            "request_type": request.__class__.__name__,
            "response_type": "ReclaimIndirectPartnerAccountResponse"
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

    def reclaim_partner_coupons(self, request):
        """回收优惠券

        对于合作伙伴已经下发给客户的优惠券，如遇发错或其他特殊情况，合作伙伴有回收的权利。优惠券回收后，客户将不再拥有该优惠券。
        
        伙伴登录合作伙伴中心回收为客户发放的代金券请参见[这里](https://support.huaweicloud.com/usermanual-bpconsole/espp_050503.html)。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;只能回收代售类子客户的优惠券。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ReclaimPartnerCoupons
        :type request: :class:`huaweicloudsdkbss.v2.ReclaimPartnerCouponsRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ReclaimPartnerCouponsResponse`
        """
        http_info = self._reclaim_partner_coupons_http_info(request)
        return self._call_api(**http_info)

    def reclaim_partner_coupons_invoker(self, request):
        http_info = self._reclaim_partner_coupons_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reclaim_partner_coupons_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/promotions/benefits/partner-coupons/reclaim",
            "request_type": request.__class__.__name__,
            "response_type": "ReclaimPartnerCouponsResponse"
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

    def reclaim_sub_enterprise_amount(self, request):
        """企业主账号从企业子账号回收拨款

        企业主账号在自建平台回收给企业子账号的拨款。
        
        如果回收的是企业子账户的信用账户，可以回收所有额度；如果回收金额大于子账户信用余额的时候，可能会导致子账户欠费，请慎重选择。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ReclaimSubEnterpriseAmount
        :type request: :class:`huaweicloudsdkbss.v2.ReclaimSubEnterpriseAmountRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ReclaimSubEnterpriseAmountResponse`
        """
        http_info = self._reclaim_sub_enterprise_amount_http_info(request)
        return self._call_api(**http_info)

    def reclaim_sub_enterprise_amount_invoker(self, request):
        http_info = self._reclaim_sub_enterprise_amount_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reclaim_sub_enterprise_amount_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/enterprises/multi-accounts/retrieve-amount",
            "request_type": request.__class__.__name__,
            "response_type": "ReclaimSubEnterpriseAmountResponse"
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

    def reclaim_to_partner_account(self, request):
        """回收客户账户余额

        当客户不再使用华为云产品时，合作伙伴可以回收代售类客户账户余额。
        
        伙伴登录伙伴中心回收代售类客户账户余额请参见[这里](https://support.huaweicloud.com/usermanual-bpconsole/zh-cn_topic_0072435147.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ReclaimToPartnerAccount
        :type request: :class:`huaweicloudsdkbss.v2.ReclaimToPartnerAccountRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ReclaimToPartnerAccountResponse`
        """
        http_info = self._reclaim_to_partner_account_http_info(request)
        return self._call_api(**http_info)

    def reclaim_to_partner_account_invoker(self, request):
        http_info = self._reclaim_to_partner_account_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reclaim_to_partner_account_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/accounts/partner-accounts/reclaim",
            "request_type": request.__class__.__name__,
            "response_type": "ReclaimToPartnerAccountResponse"
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

    def send_sms_verification_code(self, request):
        """发送短信验证码

        企业主账号在自建平台发送短信验证码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SendSmsVerificationCode
        :type request: :class:`huaweicloudsdkbss.v2.SendSmsVerificationCodeRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.SendSmsVerificationCodeResponse`
        """
        http_info = self._send_sms_verification_code_http_info(request)
        return self._call_api(**http_info)

    def send_sms_verification_code_invoker(self, request):
        http_info = self._send_sms_verification_code_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _send_sms_verification_code_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/enterprises/multi-accounts/sm-verification-code",
            "request_type": request.__class__.__name__,
            "response_type": "SendSmsVerificationCodeResponse"
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

    def send_verification_message_code(self, request):
        """发送验证码

        客户注册时，如果填写了手机号，可以向对应的手机发送注册验证码，校验信息的正确性。使用个人银行卡方式进行实名认证时，通过该接口向指定的手机发送验证码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SendVerificationMessageCode
        :type request: :class:`huaweicloudsdkbss.v2.SendVerificationMessageCodeRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.SendVerificationMessageCodeResponse`
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

        客户可以查询自身的账户余额。
        
        客户可以登录费用中心进入“[总览](https://account.huaweicloud.com/usercenter/#/userindex/allview)”页面，在“可用额度”区域可以查询自身的账户余额。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCustomerAccountBalances
        :type request: :class:`huaweicloudsdkbss.v2.ShowCustomerAccountBalancesRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ShowCustomerAccountBalancesResponse`
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

    def show_customer_monthly_sum(self, request):
        """查询汇总账单

        客户在自建平台查询自身的消费汇总账单，此账单按月汇总消费数据。
        
        客户登录费用中心查询自身的消费汇总账单请参见[这里](https://support.huaweicloud.com/usermanual-billing/bills-topic_80000001.html#bills-topic_80000001__zh-cn_topic_0000001162496407_s620ce713baf04899a416d781d1817931)的“**查看汇总**”。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;当前支持查看2019/01月份至今的费用账单。企业主账号展示的费用账单，包含关联的统一还款企业子账号的消费数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCustomerMonthlySum
        :type request: :class:`huaweicloudsdkbss.v2.ShowCustomerMonthlySumRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ShowCustomerMonthlySumResponse`
        """
        http_info = self._show_customer_monthly_sum_http_info(request)
        return self._call_api(**http_info)

    def show_customer_monthly_sum_invoker(self, request):
        http_info = self._show_customer_monthly_sum_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_customer_monthly_sum_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/bills/customer-bills/monthly-sum",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCustomerMonthlySumResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

    def show_multi_account_transfer_amount(self, request):
        """查询企业主账号可拨款余额

        企业主账号在自建平台查询自己的可拨款余额。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMultiAccountTransferAmount
        :type request: :class:`huaweicloudsdkbss.v2.ShowMultiAccountTransferAmountRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ShowMultiAccountTransferAmountResponse`
        """
        http_info = self._show_multi_account_transfer_amount_http_info(request)
        return self._call_api(**http_info)

    def show_multi_account_transfer_amount_invoker(self, request):
        http_info = self._show_multi_account_transfer_amount_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_multi_account_transfer_amount_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/enterprises/multi-accounts/transfer-amount",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMultiAccountTransferAmountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        如果实名认证申请或实名认证变更申请的响应中，显示需要人工审核，使用该接口查询审核结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRealnameAuthenticationReviewResult
        :type request: :class:`huaweicloudsdkbss.v2.ShowRealnameAuthenticationReviewResultRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ShowRealnameAuthenticationReviewResultResponse`
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

    def update_coupon_quotas(self, request):
        """向云经销商发放代金券额度

        华为云总经销商（一级经销商）可以向云经销商（二级经销商）发放代金券额度。
        
        一级经销商在伙伴中心向二级经销商发放代金券额度请参见[这里](https://support.huaweicloud.com/usermanual-bpconsole/dp_120206.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCouponQuotas
        :type request: :class:`huaweicloudsdkbss.v2.UpdateCouponQuotasRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.UpdateCouponQuotasResponse`
        """
        http_info = self._update_coupon_quotas_http_info(request)
        return self._call_api(**http_info)

    def update_coupon_quotas_invoker(self, request):
        http_info = self._update_coupon_quotas_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_coupon_quotas_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/partners/coupon-quotas/indirect-partner-adjust",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCouponQuotasResponse"
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

    def update_customer_account_amount(self, request):
        """向客户账户拨款

        合作伙伴可以为代售类客户账户拨款。
        
        伙伴登录伙伴中心为代售类客户账户拨款请参见[这里](https://support.huaweicloud.com/usermanual-bpconsole/zh-cn_topic_0072435147.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCustomerAccountAmount
        :type request: :class:`huaweicloudsdkbss.v2.UpdateCustomerAccountAmountRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.UpdateCustomerAccountAmountResponse`
        """
        http_info = self._update_customer_account_amount_http_info(request)
        return self._call_api(**http_info)

    def update_customer_account_amount_invoker(self, request):
        http_info = self._update_customer_account_amount_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_customer_account_amount_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/accounts/partner-accounts/adjust-amount",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCustomerAccountAmountResponse"
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

    def update_indirect_partner_account(self, request):
        """向云经销商账户拨款

        华为云总经销商（一级经销商）可以向云经销商（二级经销商）账户拨款。
        
        一级经销商在伙伴中心向二级经销商拨款请参见[这里](https://support.huaweicloud.com/usermanual-bpconsole/dp_120205.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateIndirectPartnerAccount
        :type request: :class:`huaweicloudsdkbss.v2.UpdateIndirectPartnerAccountRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.UpdateIndirectPartnerAccountResponse`
        """
        http_info = self._update_indirect_partner_account_http_info(request)
        return self._call_api(**http_info)

    def update_indirect_partner_account_invoker(self, request):
        http_info = self._update_indirect_partner_account_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_indirect_partner_account_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/accounts/partner-accounts/indirect-partner-adjust",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateIndirectPartnerAccountResponse"
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
        """设置或取消包年/包月资源到期转按需

        客户可以设置包年/包月资源到期后转为按需资源计费。包年/包月计费模式到期后，按需的计费模式即生效。
        
        客户在费用中心设置包年包月资源到期转按需请参见[这里](https://support.huaweicloud.com/usermanual-billing/renewals_topic_50000003.html)。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;-   客户需要成功支付包年/包月资源订单后，才能设置资源的到期转按需。
        &gt;-   目前解决方案组合产品、按需套餐包不支持到期转按需。
        &gt;-   在调用本接口前，您可以调用“[查询客户包年/包月资源列表](https://support.huaweicloud.com/api-oce/api_order_00021.html)”接口获取资源ID、资源过期时间以及资源过期后的扣费策略等信息。
        &gt;-   设置包年/包月资源到期转按需后，包年/包月资源到期后将自动变成按需计费。
        &gt;-   取消包年/包月资源到期转按需的前提是已经调用“[设置或取消包年/包月资源到期转按需](https://support.huaweicloud.com/api-oce/api_order_00024.html)”接口设置包年/包月资源的到期转按需或在调用“[续订包年/包月资源](https://support.huaweicloud.com/api-oce/api_order_00018.html)”接口时设置到期策略为到期转按需。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePeriodToOnDemand
        :type request: :class:`huaweicloudsdkbss.v2.UpdatePeriodToOnDemandRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.UpdatePeriodToOnDemandResponse`
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

    def update_sub_enterprise_amount(self, request):
        """企业主账号向企业子账号拨款

        企业主账号在自建平台向企业子账号拨款。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSubEnterpriseAmount
        :type request: :class:`huaweicloudsdkbss.v2.UpdateSubEnterpriseAmountRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.UpdateSubEnterpriseAmountResponse`
        """
        http_info = self._update_sub_enterprise_amount_http_info(request)
        return self._call_api(**http_info)

    def update_sub_enterprise_amount_invoker(self, request):
        http_info = self._update_sub_enterprise_amount_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_sub_enterprise_amount_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/enterprises/multi-accounts/transfer-amount",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSubEnterpriseAmountResponse"
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

        为防止资源到期被删除，客户可为长期使用的包年/包月资源开通自动续费。
        
        客户在费用中心开通自动续费请参见[这里](https://support.huaweicloud.com/usermanual-billing/renewals_topic_20000003.html)。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;-   首先要客户成功支付包年/包月资源订单，才能进行自动续费的开通。
        &gt;-   目前支持设置自动续费的包年/包月产品请参见[自动续费规则说明](https://support.huaweicloud.com/usermanual-billing/renewals_topic_20000002.html)。
        &gt;-   在调用本接口前，您可以调用“[查询客户包年/包月资源列表](https://support.huaweicloud.com/api-oce/api_order_00021.html)”接口获取资源ID、资源过期时间以及资源过期后扣费策略等信息。
        &gt;-   自动续费将于产品到期前7天的凌晨3:00开始扣款，请保持账户余额充足。若由于账户中余额不足等原因导致第一次未扣费成功，系统将每天凌晨3:00尝试进行一次扣款，直到扣款成功或保留产品资源的最后一天。
        &gt;-   续费周期与原资源的购买周期一致。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AutoRenewalResources
        :type request: :class:`huaweicloudsdkbss.v2.AutoRenewalResourcesRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.AutoRenewalResourcesResponse`
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

        客户设置自动续费后，还可以执行取消自动续费的操作。关闭自动续费后，资源到期将不会被自动续费。
        
        客户在费用中心取消包年/包月资源自动续费请参见[这里](https://support.huaweicloud.com/usermanual-billing/renewals_topic_20000005.html)。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;-   前提是已经调用“[设置包年/包月资源自动续费](https://support.huaweicloud.com/api-oce/api_order_00022.html)”接口设置自动续费或在调用“[续订包年/包月资源](https://support.huaweicloud.com/api-oce/api_order_00018.html)”接口时设置到期策略为自动续订。
        &gt;-   目前支持取消自动续费的包年/包月产品同支持自动续费的包年/包月产品。
        &gt;-   在调用本接口前，您可以调用“[查询客户包年/包月资源列表](https://support.huaweicloud.com/api-bpconsole/api_order_00021.html)”接口获取资源ID、资源过期时间以及资源过期后扣费策略等信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelAutoRenewalResources
        :type request: :class:`huaweicloudsdkbss.v2.CancelAutoRenewalResourcesRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.CancelAutoRenewalResourcesResponse`
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

        客户可以对待支付的订单进行取消操作。
        
        客户登录费用中心取消包年包月产品的待支付订单请单击[这里](https://support.huaweicloud.com/usermanual-billing/zh-cn_topic_0031465730.html)。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;只有订单状态是“待支付”的时候，才能取消订单。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelCustomerOrder
        :type request: :class:`huaweicloudsdkbss.v2.CancelCustomerOrderRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.CancelCustomerOrderResponse`
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

        客户购买包年/包月资源后，支持客户退订包年/包月实例。退订资源实例包括资源续费部分和当前正在使用的部分，退订后资源将无法使用。
        
        客户在费用中心退订已购买的包年包月资源请参见[这里](https://support.huaweicloud.com/usermanual-billing/zh-cn_topic_0083138805.html)。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;-   首先要成功支付包年/包月产品，产生一条开通成功的包年/包月资源，才能进行退订。
        &gt;-   调用接口后，如果某个主资源有对应的从资源，系统会将主资源和从资源一起退订，主资源的从资源信息可以通过调用[查询客户包年/包月资源列表](https://support.huaweicloud.com/api-oce/api_order_00021.html)接口获取。
        &gt;-   注意：如ECS主机挂载新购的云硬盘，但此硬盘不是该ECS主资源的从资源，主从资源信息必须以调用[查询客户包年/包月资源列表](https://support.huaweicloud.com/api-oce/api_order_00021.html)接口获取的信息为准。
        &gt;-   调用该接口后，您还可以调用“[查询退款订单的金额详情](查询退款订单的金额详情.md)”接口查询退订订单对应的金额来自哪些订单。
        &gt;-   该接口支持5天无理由全额退订，具体规则请参见“[退订规则说明](https://support.huaweicloud.com/usermanual-billing/unsubscription_topic_20000081.html)”。
        &gt;-   您正在退订使用中的资源，请仔细确认资源信息和退款信息。未放入回收站的资源退订后无法恢复，若您要保留资源，仅退订未使用的续费周期，请退订续费周期。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelResourcesSubscription
        :type request: :class:`huaweicloudsdkbss.v2.CancelResourcesSubscriptionRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.CancelResourcesSubscriptionResponse`
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

        客户购买包年/包月资源后，可以查看待审核、处理中、已取消、已完成和待支付等状态的订单。
        
        伙伴登录伙伴中心查看客户订单请单击[这里](https://support.huaweicloud.com/usermanual-bpconsole/zh-cn_topic_0076200001.html)。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;如果想查询某条订单下的资源信息，在调用本接口获取订单ID后，请调用“[查询客户包年/包月资源列表](https://support.huaweicloud.com/api-oce/api_order_00021.html)”接口在请求参数输入订单号进行查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCustomerOrders
        :type request: :class:`huaweicloudsdkbss.v2.ListCustomerOrdersRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListCustomerOrdersResponse`
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

    def list_order_coupons_by_order_id(self, request):
        """查询订单可用优惠券

        客户在伙伴销售平台支付待支付订单时，查询可使用的优惠券列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOrderCouponsByOrderId
        :type request: :class:`huaweicloudsdkbss.v2.ListOrderCouponsByOrderIdRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListOrderCouponsByOrderIdResponse`
        """
        http_info = self._list_order_coupons_by_order_id_http_info(request)
        return self._call_api(**http_info)

    def list_order_coupons_by_order_id_invoker(self, request):
        http_info = self._list_order_coupons_by_order_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_order_coupons_by_order_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/orders/customer-orders/order-coupons",
            "request_type": request.__class__.__name__,
            "response_type": "ListOrderCouponsByOrderIdResponse"
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

    def list_pay_per_use_customer_resources(self, request):
        """查询客户包年/包月资源列表

        客户在伙伴销售平台查询某个或所有的包年/包月资源。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;成功调用本接口后，如果您需要对已生效状态的资源进行续订，您可以调用“[查询包年/包月产品价格](https://support.huaweicloud.com/api-bpconsole/bcloud_01002.html)”接口对查询到的包年/包月资源进行续订询价，然后再调用“[续订包年/包月资源](https://support.huaweicloud.com/api-bpconsole/api_order_00018.html)”接口进行续订。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPayPerUseCustomerResources
        :type request: :class:`huaweicloudsdkbss.v2.ListPayPerUseCustomerResourcesRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ListPayPerUseCustomerResourcesResponse`
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

        客户可以对待支付状态的包年/包月产品订单进行支付。
        
        客户登录费用中心支付包年包月产品的待支付订单请单击[这里](https://support.huaweicloud.com/usermanual-billing/zh-cn_topic_0031512547.html)。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;-   API支持月度结算和余额支付两种支付方式，月度结算优先。
        &gt;-   余额支付包括现金账户和信用账户两种支付方式，如果两个账户都有余额，则优先现金账户支付。
        &gt;-   同时使用订单折扣和优惠券的互斥规则如下：
        &gt;    -   如果优惠券的限制属性上存在simultaneousUseWithEmpowerDiscount字段，并且值为0，则折扣和优惠券不能同时使用。
        &gt;    -   如果优惠券的限制属性上存在minConsumeDiscount字段，当折扣ID包含的所有订单项上的折扣率discount\\_ratio都小于minConsumeDiscount字段时，则折扣ID和优惠券不能同时使用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PayOrders
        :type request: :class:`huaweicloudsdkbss.v2.PayOrdersRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.PayOrdersResponse`
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

        客户的包年/包月资源即将到期时，可进行包年/包月资源的续订。
        
        客户在费用中心执行续订操作请参见[这里](https://support.huaweicloud.com/usermanual-billing/renewals_topic_10000003.html)。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;-   调用接口后，如果某个主资源有对应的从资源，系统会将主资源和从资源一起续订，主资源的从资源信息可以通过调用[查询客户包年/包月资源列表](https://support.huaweicloud.com/api-oce/api_order_00021.html)接口获取。
        &gt;-   注意：如ECS主机挂载新购的云硬盘，但此硬盘不是该ECS主资源的从资源，主从资源信息必须以调用[查询客户包年/包月资源列表](https://support.huaweicloud.com/api-oce/api_order_00021.html)接口获取的信息为准。
        &gt;-   本接口支持自动支付，支付时使用折扣或优惠券的说明，请参见[支付使用折扣或优惠券说明](https://support.huaweicloud.com/api-oce/appendix_00001.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RenewalResources
        :type request: :class:`huaweicloudsdkbss.v2.RenewalResourcesRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.RenewalResourcesResponse`
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

        客户可以在伙伴销售平台查看订单详情。
        
        客户登录费用中心查看订单详情请单击[这里](https://support.huaweicloud.com/usermanual-billing/order_topic_9000001.html)。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;如果想查询某条订单下的资源信息，请调用“[查询客户包年/包月资源列表](https://support.huaweicloud.com/api-oce/api_order_00021.html)”接口在请求参数输入订单号进行查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCustomerOrderDetails
        :type request: :class:`huaweicloudsdkbss.v2.ShowCustomerOrderDetailsRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ShowCustomerOrderDetailsResponse`
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

        客户在伙伴销售平台查询某次退订订单或者降配订单的退款金额来自哪些资源和对应订单。
        
        &gt;![](public_sys-resources/icon-note.gif) **说明：** 
        &gt;-   可以在调用完“[退订包年/包月资源](https://support.huaweicloud.com/api-oce/api_order_00019.html)”接口生成退订订单ID后，调用该接口查询退订订单对应的金额所属资源和订单。例如，调用“[退订包年/包月资源](https://support.huaweicloud.com/api-oce/api_order_00019.html)”接口退订资源及其已续费周期后，您可以调用本小节的接口查询到退订金额归属的原开通订单ID和原续费订单ID。
        &gt;-   2018年5月份之后退订的订单才能查询到归属的原订单ID。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRefundOrderDetails
        :type request: :class:`huaweicloudsdkbss.v2.ShowRefundOrderDetailsRequest`
        :rtype: :class:`huaweicloudsdkbss.v2.ShowRefundOrderDetailsResponse`
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
