# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class GslClient(Client):
    def __init__(self):
        super(GslClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkgsl.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "GslClient":
            raise TypeError("client type error, support client type is GslClient")

        return ClientBuilder(clazz)

    def batch_set_attributes(self, request):
        """批量设置自定义属性接口

        批量设置自定义属性接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchSetAttributes
        :type request: :class:`huaweicloudsdkgsl.v3.BatchSetAttributesRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.BatchSetAttributesResponse`
        """
        return self._batch_set_attributes_with_http_info(request)

    def _batch_set_attributes_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1/sim-cards/attributes/batch-set',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchSetAttributesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_attribute(self, request):
        """用户新增自定义属性接口

        用户新增自定义属性接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAttribute
        :type request: :class:`huaweicloudsdkgsl.v3.CreateAttributeRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.CreateAttributeResponse`
        """
        return self._create_attribute_with_http_info(request)

    def _create_attribute_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1/attributes',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAttributeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disable_attribute(self, request):
        """停用自定义属性接口

        停用自定义属性接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisableAttribute
        :type request: :class:`huaweicloudsdkgsl.v3.DisableAttributeRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.DisableAttributeResponse`
        """
        return self._disable_attribute_with_http_info(request)

    def _disable_attribute_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'attribute_id' in local_var_params:
            path_params['attribute_id'] = local_var_params['attribute_id']

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
            resource_path='/v1/attributes/{attribute_id}/disable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisableAttributeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def enable_attribute(self, request):
        """启用自定义属性接口

        启用自定义属性接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableAttribute
        :type request: :class:`huaweicloudsdkgsl.v3.EnableAttributeRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.EnableAttributeResponse`
        """
        return self._enable_attribute_with_http_info(request)

    def _enable_attribute_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'attribute_id' in local_var_params:
            path_params['attribute_id'] = local_var_params['attribute_id']

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
            resource_path='/v1/attributes/{attribute_id}/enable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='EnableAttributeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_attributes(self, request):
        """查询自定义属性列表接口

        查询自定义属性列表接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAttributes
        :type request: :class:`huaweicloudsdkgsl.v3.ListAttributesRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ListAttributesResponse`
        """
        return self._list_attributes_with_http_info(request)

    def _list_attributes_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/attributes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAttributesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_attribute(self, request):
        """修改自定义属性接口

        修改自定义属性接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAttribute
        :type request: :class:`huaweicloudsdkgsl.v3.UpdateAttributeRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.UpdateAttributeResponse`
        """
        return self._update_attribute_with_http_info(request)

    def _update_attribute_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'attribute_id' in local_var_params:
            path_params['attribute_id'] = local_var_params['attribute_id']

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
            resource_path='/v1/attributes/{attribute_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAttributeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_back_pool_members(self, request):
        """查询后向流量池成员列表

        查询后向流量池成员列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBackPoolMembers
        :type request: :class:`huaweicloudsdkgsl.v3.ListBackPoolMembersRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ListBackPoolMembersResponse`
        """
        return self._list_back_pool_members_with_http_info(request)

    def _list_back_pool_members_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/back-pools/{back_pool_id}/members',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBackPoolMembersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_back_pools(self, request):
        """查询后向流量池列表

        查询后向流量池列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBackPools
        :type request: :class:`huaweicloudsdkgsl.v3.ListBackPoolsRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ListBackPoolsResponse`
        """
        return self._list_back_pools_with_http_info(request)

    def _list_back_pools_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/back-pools',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBackPoolsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_pro_price_plans(self, request):
        """查询套餐列表信息

        查询套餐列表信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProPricePlans
        :type request: :class:`huaweicloudsdkgsl.v3.ListProPricePlansRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ListProPricePlansResponse`
        """
        return self._list_pro_price_plans_with_http_info(request)

    def _list_pro_price_plans_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/price-plans',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProPricePlansResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_real_name(self, request):
        """清除实名认证信息

        清除实名认证信息，接口仅支持中国电信卡调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRealName
        :type request: :class:`huaweicloudsdkgsl.v3.DeleteRealNameRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.DeleteRealNameResponse`
        """
        return self._delete_real_name_with_http_info(request)

    def _delete_real_name_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/sim-cards/{sim_card_id}/clear-real-name',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteRealNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def enable_sim_card(self, request):
        """激活实体卡

        创建激活实体卡申请，返回业务受理单号。1~2个工作日完成激活操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableSimCard
        :type request: :class:`huaweicloudsdkgsl.v3.EnableSimCardRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.EnableSimCardResponse`
        """
        return self._enable_sim_card_with_http_info(request)

    def _enable_sim_card_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/sim-cards/{sim_card_id}/enable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='EnableSimCardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_sim_cards(self, request):
        """查询SIM卡列表

        查询SIM卡列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSimCards
        :type request: :class:`huaweicloudsdkgsl.v3.ListSimCardsRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ListSimCardsResponse`
        """
        return self._list_sim_cards_with_http_info(request)

    def _list_sim_cards_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/sim-cards',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSimCardsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def register_imei(self, request):
        """SIM卡机卡重绑

        支持固定机卡重绑(需要上传IMEI，将SIM卡绑定到指定IMEI的设备)和普通机卡重绑(会清除之前绑定的设备,将SIM卡绑定到正在使用的设备)，接口仅支持中国电信卡，中国移动卡调用。中国电信卡单卡每月只允许重绑2次，中国移动卡仅支持普通机卡重绑。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RegisterImei
        :type request: :class:`huaweicloudsdkgsl.v3.RegisterImeiRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.RegisterImeiResponse`
        """
        return self._register_imei_with_http_info(request)

    def _register_imei_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sim_card_id' in local_var_params:
            path_params['sim_card_id'] = local_var_params['sim_card_id']

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
            resource_path='/v1/sim-cards/{sim_card_id}/bind-device',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RegisterImeiResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reset_sim_card(self, request):
        """SIM卡单卡复机

        创建复机申请，返回业务受理单号。1~2个工作日完成复机操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetSimCard
        :type request: :class:`huaweicloudsdkgsl.v3.ResetSimCardRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ResetSimCardResponse`
        """
        return self._reset_sim_card_with_http_info(request)

    def _reset_sim_card_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sim_card_id' in local_var_params:
            path_params['sim_card_id'] = local_var_params['sim_card_id']

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
            resource_path='/v1/sim-cards/{sim_card_id}/reset',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResetSimCardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_exceed_cut_net(self, request):
        """SIM卡达量断网/取消达量断网

        SIM卡达量断网/取消达量断网，接口仅支持中国电信的卡以及中国联通、中国移动的组池卡调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetExceedCutNet
        :type request: :class:`huaweicloudsdkgsl.v3.SetExceedCutNetRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.SetExceedCutNetResponse`
        """
        return self._set_exceed_cut_net_with_http_info(request)

    def _set_exceed_cut_net_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sim_card_id' in local_var_params:
            path_params['sim_card_id'] = local_var_params['sim_card_id']

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
            resource_path='/v1/sim-cards/{sim_card_id}/exceed-cut-net',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SetExceedCutNetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_speed_value(self, request):
        """实体卡限速

        实体卡限速接口，接口仅支持中国电信和中国联通实体卡调用。中国联通卡需要个人实名认证后才能使用限速功能。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetSpeedValue
        :type request: :class:`huaweicloudsdkgsl.v3.SetSpeedValueRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.SetSpeedValueResponse`
        """
        return self._set_speed_value_with_http_info(request)

    def _set_speed_value_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sim_card_id' in local_var_params:
            path_params['sim_card_id'] = local_var_params['sim_card_id']

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
            resource_path='/v1/sim-cards/{sim_card_id}/speed-limit',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SetSpeedValueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_month_usages(self, request):
        """月用量统计

        设备月用量统计
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMonthUsages
        :type request: :class:`huaweicloudsdkgsl.v3.ShowMonthUsagesRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ShowMonthUsagesResponse`
        """
        return self._show_month_usages_with_http_info(request)

    def _show_month_usages_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1/sim-cards/month-usages',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowMonthUsagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_real_named(self, request):
        """查询SIM卡实名认证信息

        实时查询SIM卡实名认证信息，接口仅支持查询中国大陆运营商卡片的实名认证信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRealNamed
        :type request: :class:`huaweicloudsdkgsl.v3.ShowRealNamedRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ShowRealNamedResponse`
        """
        return self._show_real_named_with_http_info(request)

    def _show_real_named_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/sim-cards/{sim_card_id}/real-named',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowRealNamedResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_sim_card(self, request):
        """查询SIM卡详情

        查询SIM卡详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSimCard
        :type request: :class:`huaweicloudsdkgsl.v3.ShowSimCardRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ShowSimCardResponse`
        """
        return self._show_sim_card_with_http_info(request)

    def _show_sim_card_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/sim-cards/{sim_card_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSimCardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_stop_net(self, request):
        """SIM卡申请断网/恢复在用

        SIM卡申请断网/恢复在用，接口仅支持中国电信卡调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartStopNet
        :type request: :class:`huaweicloudsdkgsl.v3.StartStopNetRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.StartStopNetResponse`
        """
        return self._start_stop_net_with_http_info(request)

    def _start_stop_net_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sim_card_id' in local_var_params:
            path_params['sim_card_id'] = local_var_params['sim_card_id']

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
            resource_path='/v1/sim-cards/{sim_card_id}/cut-net',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StartStopNetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_sim_card(self, request):
        """SIM卡单卡停机

        创建停机申请，返回业务受理单号。1~2个工作日完成停机操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopSimCard
        :type request: :class:`huaweicloudsdkgsl.v3.StopSimCardRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.StopSimCardResponse`
        """
        return self._stop_sim_card_with_http_info(request)

    def _stop_sim_card_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sim_card_id' in local_var_params:
            path_params['sim_card_id'] = local_var_params['sim_card_id']

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
            resource_path='/v1/sim-cards/{sim_card_id}/stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopSimCardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_sim_pool_members(self, request):
        """查询流量池成员列表

        查询流量池成员列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSimPoolMembers
        :type request: :class:`huaweicloudsdkgsl.v3.ListSimPoolMembersRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ListSimPoolMembersResponse`
        """
        return self._list_sim_pool_members_with_http_info(request)

    def _list_sim_pool_members_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/sim-pools/{sim_pool_id}/members',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSimPoolMembersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_sim_pools(self, request):
        """查询流量池列表

        查询流量池列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSimPools
        :type request: :class:`huaweicloudsdkgsl.v3.ListSimPoolsRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ListSimPoolsResponse`
        """
        return self._list_sim_pools_with_http_info(request)

    def _list_sim_pools_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/sim-pools',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSimPoolsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_flow_by_sim_cards(self, request):
        """批量查询实体卡流量

        批量查询实体卡流量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFlowBySimCards
        :type request: :class:`huaweicloudsdkgsl.v3.ListFlowBySimCardsRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ListFlowBySimCardsResponse`
        """
        return self._list_flow_by_sim_cards_with_http_info(request)

    def _list_flow_by_sim_cards_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1/sim-price-plans/usage/batch-query',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFlowBySimCardsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_sim_price_plans(self, request):
        """sim卡套餐列表查询

        SIM卡套餐列表查询，实体卡只会有一个套餐，eSIM/vSIM可能会有多个套餐
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSimPricePlans
        :type request: :class:`huaweicloudsdkgsl.v3.ListSimPricePlansRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ListSimPricePlansResponse`
        """
        return self._list_sim_price_plans_with_http_info(request)

    def _list_sim_price_plans_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/sim-price-plans',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSimPricePlansResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_sms_details(self, request):
        """短信发送详情

        短信发送详情，接口仅支持开通短信套餐的中国移动与中国电信卡调用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSmsDetails
        :type request: :class:`huaweicloudsdkgsl.v3.ListSmsDetailsRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ListSmsDetailsResponse`
        """
        return self._list_sms_details_with_http_info(request)

    def _list_sms_details_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/sms-send-infos/details',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSmsDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def send_sms(self, request):
        """发送短信

        发送短信，接口仅支持开通短信套餐的中国移动与中国电信卡调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SendSms
        :type request: :class:`huaweicloudsdkgsl.v3.SendSmsRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.SendSmsResponse`
        """
        return self._send_sms_with_http_info(request)

    def _send_sms_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1/sms-send-infos',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SendSmsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_set_tags(self, request):
        """批量设置/取消设置标签接口

        批量设置/取消设置标签接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchSetTags
        :type request: :class:`huaweicloudsdkgsl.v3.BatchSetTagsRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.BatchSetTagsResponse`
        """
        return self._batch_set_tags_with_http_info(request)

    def _batch_set_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1/sim-tags/batch-set',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchSetTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_tag(self, request):
        """用户添加标签

        添加标签接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTag
        :type request: :class:`huaweicloudsdkgsl.v3.CreateTagRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.CreateTagResponse`
        """
        return self._create_tag_with_http_info(request)

    def _create_tag_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1/tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_tag(self, request):
        """删除标签

        删除标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTag
        :type request: :class:`huaweicloudsdkgsl.v3.DeleteTagRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.DeleteTagResponse`
        """
        return self._delete_tag_with_http_info(request)

    def _delete_tag_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tag_id' in local_var_params:
            path_params['tag_id'] = local_var_params['tag_id']

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
            resource_path='/v1/tags/{tag_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_tags(self, request):
        """查询标签列表

        查询标签列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTags
        :type request: :class:`huaweicloudsdkgsl.v3.ListTagsRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ListTagsResponse`
        """
        return self._list_tags_with_http_info(request)

    def _list_tags_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_work_order_details(self, request):
        """分页查询业务受理明细

        分页查询业务受理明细
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWorkOrderDetails
        :type request: :class:`huaweicloudsdkgsl.v3.ListWorkOrderDetailsRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ListWorkOrderDetailsResponse`
        """
        return self._list_work_order_details_with_http_info(request)

    def _list_work_order_details_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/work-orders/{work_order_id}/details',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListWorkOrderDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_work_orders(self, request):
        """分页查询业务受理单

        分页查询业务受理单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWorkOrders
        :type request: :class:`huaweicloudsdkgsl.v3.ListWorkOrdersRequest`
        :rtype: :class:`huaweicloudsdkgsl.v3.ListWorkOrdersResponse`
        """
        return self._list_work_orders_with_http_info(request)

    def _list_work_orders_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/work-orders',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListWorkOrdersResponse',
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
