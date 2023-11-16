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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkgsl'")


class GslClient(Client):
    def __init__(self):
        super(GslClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkgsl.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "GslClient":
                raise TypeError("client type error, support client type is GslClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_set_attributes(self, request):
        """批量设置自定义属性接口

        批量设置自定义属性接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchSetAttributes
        :type request: :class:`huaweicloudsdkgsl.v3.BatchSetAttributesRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.BatchSetAttributesResponse`
        """
        http_info = self._batch_set_attributes_http_info(request)
        return self._call_api(**http_info)

    def batch_set_attributes_invoker(self, request):
        http_info = self._batch_set_attributes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_set_attributes_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/sim-cards/attributes/batch-set",
            "request_type": request.__class__.__name__,
            "response_type": "BatchSetAttributesResponse"
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

    def create_attribute(self, request):
        """用户新增自定义属性接口

        用户新增自定义属性接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAttribute
        :type request: :class:`huaweicloudsdkgsl.v3.CreateAttributeRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.CreateAttributeResponse`
        """
        http_info = self._create_attribute_http_info(request)
        return self._call_api(**http_info)

    def create_attribute_invoker(self, request):
        http_info = self._create_attribute_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_attribute_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/attributes",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAttributeResponse"
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

    def disable_attribute(self, request):
        """停用自定义属性接口

        停用自定义属性接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisableAttribute
        :type request: :class:`huaweicloudsdkgsl.v3.DisableAttributeRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.DisableAttributeResponse`
        """
        http_info = self._disable_attribute_http_info(request)
        return self._call_api(**http_info)

    def disable_attribute_invoker(self, request):
        http_info = self._disable_attribute_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disable_attribute_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/attributes/{attribute_id}/disable",
            "request_type": request.__class__.__name__,
            "response_type": "DisableAttributeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'attribute_id' in local_var_params:
            path_params['attribute_id'] = local_var_params['attribute_id']

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

    def enable_attribute(self, request):
        """启用自定义属性接口

        启用自定义属性接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableAttribute
        :type request: :class:`huaweicloudsdkgsl.v3.EnableAttributeRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.EnableAttributeResponse`
        """
        http_info = self._enable_attribute_http_info(request)
        return self._call_api(**http_info)

    def enable_attribute_invoker(self, request):
        http_info = self._enable_attribute_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_attribute_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/attributes/{attribute_id}/enable",
            "request_type": request.__class__.__name__,
            "response_type": "EnableAttributeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'attribute_id' in local_var_params:
            path_params['attribute_id'] = local_var_params['attribute_id']

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

    def list_attributes(self, request):
        """查询自定义属性列表接口

        查询自定义属性列表接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAttributes
        :type request: :class:`huaweicloudsdkgsl.v3.ListAttributesRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ListAttributesResponse`
        """
        http_info = self._list_attributes_http_info(request)
        return self._call_api(**http_info)

    def list_attributes_invoker(self, request):
        http_info = self._list_attributes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_attributes_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/attributes",
            "request_type": request.__class__.__name__,
            "response_type": "ListAttributesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cust_attr_name' in local_var_params:
            query_params.append(('cust_attr_name', local_var_params['cust_attr_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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

    def update_attribute(self, request):
        """修改自定义属性接口

        修改自定义属性接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAttribute
        :type request: :class:`huaweicloudsdkgsl.v3.UpdateAttributeRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.UpdateAttributeResponse`
        """
        http_info = self._update_attribute_http_info(request)
        return self._call_api(**http_info)

    def update_attribute_invoker(self, request):
        http_info = self._update_attribute_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_attribute_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/attributes/{attribute_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAttributeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'attribute_id' in local_var_params:
            path_params['attribute_id'] = local_var_params['attribute_id']

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

    def list_back_pool_members(self, request):
        """查询后向流量池成员列表

        查询后向流量池成员列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBackPoolMembers
        :type request: :class:`huaweicloudsdkgsl.v3.ListBackPoolMembersRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ListBackPoolMembersResponse`
        """
        http_info = self._list_back_pool_members_http_info(request)
        return self._call_api(**http_info)

    def list_back_pool_members_invoker(self, request):
        http_info = self._list_back_pool_members_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_back_pool_members_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/back-pools/{back_pool_id}/members",
            "request_type": request.__class__.__name__,
            "response_type": "ListBackPoolMembersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'back_pool_id' in local_var_params:
            path_params['back_pool_id'] = local_var_params['back_pool_id']

        query_params = []
        if 'cid' in local_var_params:
            query_params.append(('cid', local_var_params['cid']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'billing_cycle' in local_var_params:
            query_params.append(('billing_cycle', local_var_params['billing_cycle']))

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

    def list_back_pools(self, request):
        """查询后向流量池列表

        查询后向流量池列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBackPools
        :type request: :class:`huaweicloudsdkgsl.v3.ListBackPoolsRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ListBackPoolsResponse`
        """
        http_info = self._list_back_pools_http_info(request)
        return self._call_api(**http_info)

    def list_back_pools_invoker(self, request):
        http_info = self._list_back_pools_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_back_pools_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/back-pools",
            "request_type": request.__class__.__name__,
            "response_type": "ListBackPoolsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'pool_name' in local_var_params:
            query_params.append(('pool_name', local_var_params['pool_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'billing_cycle' in local_var_params:
            query_params.append(('billing_cycle', local_var_params['billing_cycle']))
        if 'all_billing_cycle' in local_var_params:
            query_params.append(('all_billing_cycle', local_var_params['all_billing_cycle']))

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

    def list_pro_price_plans(self, request):
        """查询套餐列表信息

        查询套餐列表信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProPricePlans
        :type request: :class:`huaweicloudsdkgsl.v3.ListProPricePlansRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ListProPricePlansResponse`
        """
        http_info = self._list_pro_price_plans_http_info(request)
        return self._call_api(**http_info)

    def list_pro_price_plans_invoker(self, request):
        http_info = self._list_pro_price_plans_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_pro_price_plans_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/price-plans",
            "request_type": request.__class__.__name__,
            "response_type": "ListProPricePlansResponse"
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
        if 'main_search_key' in local_var_params:
            query_params.append(('main_search_key', local_var_params['main_search_key']))
        if 'flow_total' in local_var_params:
            query_params.append(('flow_total', local_var_params['flow_total']))
        if 'network_type' in local_var_params:
            query_params.append(('network_type', local_var_params['network_type']))
        if 'location_type' in local_var_params:
            query_params.append(('location_type', local_var_params['location_type']))
        if 'carrier_type' in local_var_params:
            query_params.append(('carrier_type', local_var_params['carrier_type']))
        if 'country_type' in local_var_params:
            query_params.append(('country_type', local_var_params['country_type']))

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

    def delete_real_name(self, request):
        """清除实名认证信息

        清除实名认证信息，接口仅支持中国电信卡调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRealName
        :type request: :class:`huaweicloudsdkgsl.v3.DeleteRealNameRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.DeleteRealNameResponse`
        """
        http_info = self._delete_real_name_http_info(request)
        return self._call_api(**http_info)

    def delete_real_name_invoker(self, request):
        http_info = self._delete_real_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_real_name_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/sim-cards/{sim_card_id}/clear-real-name",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRealNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sim_card_id' in local_var_params:
            path_params['sim_card_id'] = local_var_params['sim_card_id']

        query_params = []
        if 'iccid' in local_var_params:
            query_params.append(('iccid', local_var_params['iccid']))

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

    def enable_sim_card(self, request):
        """激活实体卡

        创建激活实体卡申请，返回业务受理单号。1~2个工作日完成激活操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableSimCard
        :type request: :class:`huaweicloudsdkgsl.v3.EnableSimCardRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.EnableSimCardResponse`
        """
        http_info = self._enable_sim_card_http_info(request)
        return self._call_api(**http_info)

    def enable_sim_card_invoker(self, request):
        http_info = self._enable_sim_card_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_sim_card_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/sim-cards/{sim_card_id}/enable",
            "request_type": request.__class__.__name__,
            "response_type": "EnableSimCardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sim_card_id' in local_var_params:
            path_params['sim_card_id'] = local_var_params['sim_card_id']

        query_params = []
        if 'iccid' in local_var_params:
            query_params.append(('iccid', local_var_params['iccid']))

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

    def list_sim_cards(self, request):
        """查询SIM卡列表

        查询SIM卡列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSimCards
        :type request: :class:`huaweicloudsdkgsl.v3.ListSimCardsRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ListSimCardsResponse`
        """
        http_info = self._list_sim_cards_http_info(request)
        return self._call_api(**http_info)

    def list_sim_cards_invoker(self, request):
        http_info = self._list_sim_cards_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sim_cards_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/sim-cards",
            "request_type": request.__class__.__name__,
            "response_type": "ListSimCardsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'main_search_type' in local_var_params:
            query_params.append(('main_search_type', local_var_params['main_search_type']))
        if 'main_search_key' in local_var_params:
            query_params.append(('main_search_key', local_var_params['main_search_key']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sim_status' in local_var_params:
            query_params.append(('sim_status', local_var_params['sim_status']))
        if 'device_status' in local_var_params:
            query_params.append(('device_status', local_var_params['device_status']))
        if 'tag_id' in local_var_params:
            query_params.append(('tag_id', local_var_params['tag_id']))
            collection_formats['tag_id'] = 'multi'
        if 'sim_type' in local_var_params:
            query_params.append(('sim_type', local_var_params['sim_type']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'msisdn' in local_var_params:
            query_params.append(('msisdn', local_var_params['msisdn']))
        if 'customer_attribute1' in local_var_params:
            query_params.append(('customer_attribute1', local_var_params['customer_attribute1']))
        if 'customer_attribute2' in local_var_params:
            query_params.append(('customer_attribute2', local_var_params['customer_attribute2']))
        if 'customer_attribute3' in local_var_params:
            query_params.append(('customer_attribute3', local_var_params['customer_attribute3']))
        if 'customer_attribute4' in local_var_params:
            query_params.append(('customer_attribute4', local_var_params['customer_attribute4']))
        if 'customer_attribute5' in local_var_params:
            query_params.append(('customer_attribute5', local_var_params['customer_attribute5']))
        if 'customer_attribute6' in local_var_params:
            query_params.append(('customer_attribute6', local_var_params['customer_attribute6']))
        if 'min_used_flow' in local_var_params:
            query_params.append(('min_used_flow', local_var_params['min_used_flow']))
        if 'max_used_flow' in local_var_params:
            query_params.append(('max_used_flow', local_var_params['max_used_flow']))
        if 'min_left_flow' in local_var_params:
            query_params.append(('min_left_flow', local_var_params['min_left_flow']))
        if 'max_left_flow' in local_var_params:
            query_params.append(('max_left_flow', local_var_params['max_left_flow']))
        if 'real_named' in local_var_params:
            query_params.append(('real_named', local_var_params['real_named']))
        if 'order_id' in local_var_params:
            query_params.append(('order_id', local_var_params['order_id']))
        if 'filter_downtime_period' in local_var_params:
            query_params.append(('filter_downtime_period', local_var_params['filter_downtime_period']))
        if 'order_ids' in local_var_params:
            query_params.append(('order_ids', local_var_params['order_ids']))
            collection_formats['order_ids'] = 'multi'
        if 'price_plan_id' in local_var_params:
            query_params.append(('price_plan_id', local_var_params['price_plan_id']))
            collection_formats['price_plan_id'] = 'multi'

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

    def register_imei(self, request):
        """SIM卡机卡重绑

        支持固定机卡重绑(需要上传IMEI，将SIM卡绑定到指定IMEI的设备)和普通机卡重绑(会清除之前绑定的设备,将SIM卡绑定到正在使用的设备)，接口仅支持中国电信卡，中国移动卡调用。中国电信卡单卡每月只允许重绑2次，中国移动卡仅支持普通机卡重绑。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RegisterImei
        :type request: :class:`huaweicloudsdkgsl.v3.RegisterImeiRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.RegisterImeiResponse`
        """
        http_info = self._register_imei_http_info(request)
        return self._call_api(**http_info)

    def register_imei_invoker(self, request):
        http_info = self._register_imei_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _register_imei_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/sim-cards/{sim_card_id}/bind-device",
            "request_type": request.__class__.__name__,
            "response_type": "RegisterImeiResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sim_card_id' in local_var_params:
            path_params['sim_card_id'] = local_var_params['sim_card_id']

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

    def reset_sim_card(self, request):
        """SIM卡单卡复机

        创建复机申请，返回业务受理单号。1~2个工作日完成复机操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetSimCard
        :type request: :class:`huaweicloudsdkgsl.v3.ResetSimCardRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ResetSimCardResponse`
        """
        http_info = self._reset_sim_card_http_info(request)
        return self._call_api(**http_info)

    def reset_sim_card_invoker(self, request):
        http_info = self._reset_sim_card_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_sim_card_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/sim-cards/{sim_card_id}/reset",
            "request_type": request.__class__.__name__,
            "response_type": "ResetSimCardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sim_card_id' in local_var_params:
            path_params['sim_card_id'] = local_var_params['sim_card_id']

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

    def set_exceed_cut_net(self, request):
        """SIM卡达量断网/取消达量断网

        SIM卡达量断网/取消达量断网，接口仅支持中国电信的卡以及中国联通、中国移动的组池卡调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetExceedCutNet
        :type request: :class:`huaweicloudsdkgsl.v3.SetExceedCutNetRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.SetExceedCutNetResponse`
        """
        http_info = self._set_exceed_cut_net_http_info(request)
        return self._call_api(**http_info)

    def set_exceed_cut_net_invoker(self, request):
        http_info = self._set_exceed_cut_net_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_exceed_cut_net_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/sim-cards/{sim_card_id}/exceed-cut-net",
            "request_type": request.__class__.__name__,
            "response_type": "SetExceedCutNetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sim_card_id' in local_var_params:
            path_params['sim_card_id'] = local_var_params['sim_card_id']

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

    def set_speed_value(self, request):
        """实体卡限速

        实体卡限速接口，接口仅支持中国电信和中国联通实体卡调用。中国联通卡需要个人实名认证后才能使用限速功能。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetSpeedValue
        :type request: :class:`huaweicloudsdkgsl.v3.SetSpeedValueRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.SetSpeedValueResponse`
        """
        http_info = self._set_speed_value_http_info(request)
        return self._call_api(**http_info)

    def set_speed_value_invoker(self, request):
        http_info = self._set_speed_value_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_speed_value_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/sim-cards/{sim_card_id}/speed-limit",
            "request_type": request.__class__.__name__,
            "response_type": "SetSpeedValueResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sim_card_id' in local_var_params:
            path_params['sim_card_id'] = local_var_params['sim_card_id']

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

    def show_month_usages(self, request):
        """月用量统计

        设备月用量统计
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMonthUsages
        :type request: :class:`huaweicloudsdkgsl.v3.ShowMonthUsagesRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ShowMonthUsagesResponse`
        """
        http_info = self._show_month_usages_http_info(request)
        return self._call_api(**http_info)

    def show_month_usages_invoker(self, request):
        http_info = self._show_month_usages_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_month_usages_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/sim-cards/month-usages",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMonthUsagesResponse"
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

    def show_real_named(self, request):
        """查询SIM卡实名认证信息

        实时查询SIM卡实名认证信息，接口仅支持查询中国大陆运营商卡片的实名认证信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRealNamed
        :type request: :class:`huaweicloudsdkgsl.v3.ShowRealNamedRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ShowRealNamedResponse`
        """
        http_info = self._show_real_named_http_info(request)
        return self._call_api(**http_info)

    def show_real_named_invoker(self, request):
        http_info = self._show_real_named_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_real_named_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/sim-cards/{sim_card_id}/real-named",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRealNamedResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sim_card_id' in local_var_params:
            path_params['sim_card_id'] = local_var_params['sim_card_id']

        query_params = []
        if 'iccid' in local_var_params:
            query_params.append(('iccid', local_var_params['iccid']))

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

    def show_sim_card(self, request):
        """查询SIM卡详情

        查询SIM卡详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSimCard
        :type request: :class:`huaweicloudsdkgsl.v3.ShowSimCardRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ShowSimCardResponse`
        """
        http_info = self._show_sim_card_http_info(request)
        return self._call_api(**http_info)

    def show_sim_card_invoker(self, request):
        http_info = self._show_sim_card_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sim_card_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/sim-cards/{sim_card_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSimCardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sim_card_id' in local_var_params:
            path_params['sim_card_id'] = local_var_params['sim_card_id']

        query_params = []
        if 'iccid' in local_var_params:
            query_params.append(('iccid', local_var_params['iccid']))

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

    def start_stop_net(self, request):
        """SIM卡申请断网/恢复在用

        SIM卡申请断网/恢复在用，接口仅支持中国电信卡调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartStopNet
        :type request: :class:`huaweicloudsdkgsl.v3.StartStopNetRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.StartStopNetResponse`
        """
        http_info = self._start_stop_net_http_info(request)
        return self._call_api(**http_info)

    def start_stop_net_invoker(self, request):
        http_info = self._start_stop_net_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_stop_net_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/sim-cards/{sim_card_id}/cut-net",
            "request_type": request.__class__.__name__,
            "response_type": "StartStopNetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sim_card_id' in local_var_params:
            path_params['sim_card_id'] = local_var_params['sim_card_id']

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

    def stop_sim_card(self, request):
        """SIM卡单卡停机

        创建停机申请，返回业务受理单号。1~2个工作日完成停机操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopSimCard
        :type request: :class:`huaweicloudsdkgsl.v3.StopSimCardRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.StopSimCardResponse`
        """
        http_info = self._stop_sim_card_http_info(request)
        return self._call_api(**http_info)

    def stop_sim_card_invoker(self, request):
        http_info = self._stop_sim_card_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_sim_card_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/sim-cards/{sim_card_id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopSimCardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sim_card_id' in local_var_params:
            path_params['sim_card_id'] = local_var_params['sim_card_id']

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

    def list_sim_pool_members(self, request):
        """查询流量池成员列表

        查询流量池成员列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSimPoolMembers
        :type request: :class:`huaweicloudsdkgsl.v3.ListSimPoolMembersRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ListSimPoolMembersResponse`
        """
        http_info = self._list_sim_pool_members_http_info(request)
        return self._call_api(**http_info)

    def list_sim_pool_members_invoker(self, request):
        http_info = self._list_sim_pool_members_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sim_pool_members_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/sim-pools/{sim_pool_id}/members",
            "request_type": request.__class__.__name__,
            "response_type": "ListSimPoolMembersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sim_pool_id' in local_var_params:
            path_params['sim_pool_id'] = local_var_params['sim_pool_id']

        query_params = []
        if 'cid' in local_var_params:
            query_params.append(('cid', local_var_params['cid']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'billing_cycle' in local_var_params:
            query_params.append(('billing_cycle', local_var_params['billing_cycle']))

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

    def list_sim_pools(self, request):
        """查询流量池列表

        查询流量池列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSimPools
        :type request: :class:`huaweicloudsdkgsl.v3.ListSimPoolsRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ListSimPoolsResponse`
        """
        http_info = self._list_sim_pools_http_info(request)
        return self._call_api(**http_info)

    def list_sim_pools_invoker(self, request):
        http_info = self._list_sim_pools_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sim_pools_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/sim-pools",
            "request_type": request.__class__.__name__,
            "response_type": "ListSimPoolsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'pool_name' in local_var_params:
            query_params.append(('pool_name', local_var_params['pool_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'billing_cycle' in local_var_params:
            query_params.append(('billing_cycle', local_var_params['billing_cycle']))
        if 'all_billing_cycle' in local_var_params:
            query_params.append(('all_billing_cycle', local_var_params['all_billing_cycle']))

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

    def list_flow_by_sim_cards(self, request):
        """批量查询实体卡流量

        批量查询实体卡流量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFlowBySimCards
        :type request: :class:`huaweicloudsdkgsl.v3.ListFlowBySimCardsRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ListFlowBySimCardsResponse`
        """
        http_info = self._list_flow_by_sim_cards_http_info(request)
        return self._call_api(**http_info)

    def list_flow_by_sim_cards_invoker(self, request):
        http_info = self._list_flow_by_sim_cards_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_flow_by_sim_cards_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/sim-price-plans/usage/batch-query",
            "request_type": request.__class__.__name__,
            "response_type": "ListFlowBySimCardsResponse"
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

    def list_sim_price_plans(self, request):
        """sim卡套餐列表查询

        SIM卡套餐列表查询，实体卡只会有一个套餐，eSIM/vSIM可能会有多个套餐
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSimPricePlans
        :type request: :class:`huaweicloudsdkgsl.v3.ListSimPricePlansRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ListSimPricePlansResponse`
        """
        http_info = self._list_sim_price_plans_http_info(request)
        return self._call_api(**http_info)

    def list_sim_price_plans_invoker(self, request):
        http_info = self._list_sim_price_plans_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sim_price_plans_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/sim-price-plans",
            "request_type": request.__class__.__name__,
            "response_type": "ListSimPricePlansResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sim_card_id' in local_var_params:
            query_params.append(('sim_card_id', local_var_params['sim_card_id']))
        if 'iccid' in local_var_params:
            query_params.append(('iccid', local_var_params['iccid']))
        if 'real_time' in local_var_params:
            query_params.append(('real_time', local_var_params['real_time']))
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

    def list_sms_details(self, request):
        """短信发送详情

        短信发送详情，接口仅支持开通短信套餐的中国移动与中国电信卡调用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSmsDetails
        :type request: :class:`huaweicloudsdkgsl.v3.ListSmsDetailsRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ListSmsDetailsResponse`
        """
        http_info = self._list_sms_details_http_info(request)
        return self._call_api(**http_info)

    def list_sms_details_invoker(self, request):
        http_info = self._list_sms_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sms_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/sms-send-infos/details",
            "request_type": request.__class__.__name__,
            "response_type": "ListSmsDetailsResponse"
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
        if 'cid' in local_var_params:
            query_params.append(('cid', local_var_params['cid']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
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

    def send_sms(self, request):
        """发送短信

        发送短信，接口仅支持开通短信套餐的中国移动与中国电信卡调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SendSms
        :type request: :class:`huaweicloudsdkgsl.v3.SendSmsRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.SendSmsResponse`
        """
        http_info = self._send_sms_http_info(request)
        return self._call_api(**http_info)

    def send_sms_invoker(self, request):
        http_info = self._send_sms_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _send_sms_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/sms-send-infos",
            "request_type": request.__class__.__name__,
            "response_type": "SendSmsResponse"
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

    def batch_set_tags(self, request):
        """批量设置/取消设置标签接口

        批量设置/取消设置标签接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchSetTags
        :type request: :class:`huaweicloudsdkgsl.v3.BatchSetTagsRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.BatchSetTagsResponse`
        """
        http_info = self._batch_set_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_set_tags_invoker(self, request):
        http_info = self._batch_set_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_set_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/sim-tags/batch-set",
            "request_type": request.__class__.__name__,
            "response_type": "BatchSetTagsResponse"
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

    def create_tag(self, request):
        """用户添加标签

        添加标签接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTag
        :type request: :class:`huaweicloudsdkgsl.v3.CreateTagRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.CreateTagResponse`
        """
        http_info = self._create_tag_http_info(request)
        return self._call_api(**http_info)

    def create_tag_invoker(self, request):
        http_info = self._create_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_tag_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTagResponse"
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

    def delete_tag(self, request):
        """删除标签

        删除标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTag
        :type request: :class:`huaweicloudsdkgsl.v3.DeleteTagRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.DeleteTagResponse`
        """
        http_info = self._delete_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_tag_invoker(self, request):
        http_info = self._delete_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_tag_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/tags/{tag_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tag_id' in local_var_params:
            path_params['tag_id'] = local_var_params['tag_id']

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

    def list_tags(self, request):
        """查询标签列表

        查询标签列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTags
        :type request: :class:`huaweicloudsdkgsl.v3.ListTagsRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ListTagsResponse`
        """
        http_info = self._list_tags_http_info(request)
        return self._call_api(**http_info)

    def list_tags_invoker(self, request):
        http_info = self._list_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tag_name' in local_var_params:
            query_params.append(('tag_name', local_var_params['tag_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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

    def list_work_order_details(self, request):
        """分页查询业务受理明细

        分页查询业务受理明细
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWorkOrderDetails
        :type request: :class:`huaweicloudsdkgsl.v3.ListWorkOrderDetailsRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ListWorkOrderDetailsResponse`
        """
        http_info = self._list_work_order_details_http_info(request)
        return self._call_api(**http_info)

    def list_work_order_details_invoker(self, request):
        http_info = self._list_work_order_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_work_order_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/work-orders/{work_order_id}/details",
            "request_type": request.__class__.__name__,
            "response_type": "ListWorkOrderDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'work_order_id' in local_var_params:
            path_params['work_order_id'] = local_var_params['work_order_id']

        query_params = []
        if 'main_search_key' in local_var_params:
            query_params.append(('main_search_key', local_var_params['main_search_key']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sim_type' in local_var_params:
            query_params.append(('sim_type', local_var_params['sim_type']))
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

    def list_work_orders(self, request):
        """分页查询业务受理单

        分页查询业务受理单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWorkOrders
        :type request: :class:`huaweicloudsdkgsl.v3.ListWorkOrdersRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ListWorkOrdersResponse`
        """
        http_info = self._list_work_orders_http_info(request)
        return self._call_api(**http_info)

    def list_work_orders_invoker(self, request):
        http_info = self._list_work_orders_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_work_orders_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/work-orders",
            "request_type": request.__class__.__name__,
            "response_type": "ListWorkOrdersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'main_search_key' in local_var_params:
            query_params.append(('main_search_key', local_var_params['main_search_key']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sim_type' in local_var_params:
            query_params.append(('sim_type', local_var_params['sim_type']))
        if 'work_order_type' in local_var_params:
            query_params.append(('work_order_type', local_var_params['work_order_type']))
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
