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


class GslAsyncClient(Client):
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
        super(GslAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkgsl.v3.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "GslClient":
            raise TypeError("client type error, support client type is GslClient")

        return ClientBuilder(clazz)

    def list_pro_price_plans_async(self, request):
        """查询套餐列表信息

        查询套餐列表信息

        :param ListProPricePlansRequest request
        :return: ListProPricePlansResponse
        """
        return self.list_pro_price_plans_with_http_info(request)

    def list_pro_price_plans_with_http_info(self, request):
        """查询套餐列表信息

        查询套餐列表信息

        :param ListProPricePlansRequest request
        :return: ListProPricePlansResponse
        """

        all_params = ['limit', 'offset', 'main_search_key', 'flow_total', 'network_type', 'location_type', 'carrier_type', 'country_type', 'sim_card_id', 'partner', 'package_type', 'sim_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
        if 'sim_card_id' in local_var_params:
            query_params.append(('sim_card_id', local_var_params['sim_card_id']))
        if 'partner' in local_var_params:
            query_params.append(('partner', local_var_params['partner']))
        if 'package_type' in local_var_params:
            query_params.append(('package_type', local_var_params['package_type']))
        if 'sim_type' in local_var_params:
            query_params.append(('sim_type', local_var_params['sim_type']))

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
            response_type='ListProPricePlansResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_real_name_async(self, request):
        """清除实名认证信息

        清除实名认证信息，接口只支持电信卡调用

        :param DeleteRealNameRequest request
        :return: DeleteRealNameResponse
        """
        return self.delete_real_name_with_http_info(request)

    def delete_real_name_with_http_info(self, request):
        """清除实名认证信息

        清除实名认证信息，接口只支持电信卡调用

        :param DeleteRealNameRequest request
        :return: DeleteRealNameResponse
        """

        all_params = ['sim_card_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'sim_card_id' in local_var_params:
            path_params['sim_card_id'] = local_var_params['sim_card_id']

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
            resource_path='/v1/sim-cards/{sim_card_id}/clear-real-name',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteRealNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def enable_sim_card_async(self, request):
        """激活实体卡

        创建激活实体卡申请，返回业务受理单号。1~2个工作日完成激活操作。

        :param EnableSimCardRequest request
        :return: EnableSimCardResponse
        """
        return self.enable_sim_card_with_http_info(request)

    def enable_sim_card_with_http_info(self, request):
        """激活实体卡

        创建激活实体卡申请，返回业务受理单号。1~2个工作日完成激活操作。

        :param EnableSimCardRequest request
        :return: EnableSimCardResponse
        """

        all_params = ['sim_card_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'sim_card_id' in local_var_params:
            path_params['sim_card_id'] = local_var_params['sim_card_id']

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
            resource_path='/v1/sim-cards/{sim_card_id}/enable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='EnableSimCardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_sim_cards_async(self, request):
        """查询SIM卡列表

        查询SIM卡列表

        :param ListSimCardsRequest request
        :return: ListSimCardsResponse
        """
        return self.list_sim_cards_with_http_info(request)

    def list_sim_cards_with_http_info(self, request):
        """查询SIM卡列表

        查询SIM卡列表

        :param ListSimCardsRequest request
        :return: ListSimCardsResponse
        """

        all_params = ['main_search_type', 'main_search_key', 'limit', 'offset', 'sim_status', 'device_status', 'tag_id', 'sim_type', 'order', 'sort', 'msisdn', 'customer_attribute1', 'customer_attribute2', 'customer_attribute3', 'customer_attribute4', 'customer_attribute5', 'customer_attribute6', 'real_named']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            collection_formats['tag_id'] = 'csv'
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
        if 'real_named' in local_var_params:
            query_params.append(('real_named', local_var_params['real_named']))

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
            response_type='ListSimCardsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def register_imei_async(self, request):
        """SIM卡机卡重绑

        支持固定机卡重绑(需要上传IMEI，将SIM卡绑定到指定IMEI的设备)和普通机卡重绑(会清除之前绑定的设备,将SIM卡绑定到正在使用的设备)，单卡每月只允许重绑2次，接口只支持电信卡调用。

        :param RegisterImeiRequest request
        :return: RegisterImeiResponse
        """
        return self.register_imei_with_http_info(request)

    def register_imei_with_http_info(self, request):
        """SIM卡机卡重绑

        支持固定机卡重绑(需要上传IMEI，将SIM卡绑定到指定IMEI的设备)和普通机卡重绑(会清除之前绑定的设备,将SIM卡绑定到正在使用的设备)，单卡每月只允许重绑2次，接口只支持电信卡调用。

        :param RegisterImeiRequest request
        :return: RegisterImeiResponse
        """

        all_params = ['sim_card_id', 'register_imei_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='RegisterImeiResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def reset_sim_card_async(self, request):
        """SIM卡单卡复机

        创建复机申请，返回业务受理单号。1~2个工作日完成复机操作。

        :param ResetSimCardRequest request
        :return: ResetSimCardResponse
        """
        return self.reset_sim_card_with_http_info(request)

    def reset_sim_card_with_http_info(self, request):
        """SIM卡单卡复机

        创建复机申请，返回业务受理单号。1~2个工作日完成复机操作。

        :param ResetSimCardRequest request
        :return: ResetSimCardResponse
        """

        all_params = ['sim_card_id', 'reset_sim_card_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ResetSimCardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def set_exceed_cut_net_async(self, request):
        """SIM卡达量断网/恢复在用

        SIM卡达量断网/恢复在用,只支持电信卡。

        :param SetExceedCutNetRequest request
        :return: SetExceedCutNetResponse
        """
        return self.set_exceed_cut_net_with_http_info(request)

    def set_exceed_cut_net_with_http_info(self, request):
        """SIM卡达量断网/恢复在用

        SIM卡达量断网/恢复在用,只支持电信卡。

        :param SetExceedCutNetRequest request
        :return: SetExceedCutNetResponse
        """

        all_params = ['sim_card_id', 'set_exceed_cut_net_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='SetExceedCutNetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def set_speed_value_async(self, request):
        """实体卡限速

        实体卡限速接口,支持电信和联通实体卡调用。

        :param SetSpeedValueRequest request
        :return: SetSpeedValueResponse
        """
        return self.set_speed_value_with_http_info(request)

    def set_speed_value_with_http_info(self, request):
        """实体卡限速

        实体卡限速接口,支持电信和联通实体卡调用。

        :param SetSpeedValueRequest request
        :return: SetSpeedValueResponse
        """

        all_params = ['sim_card_id', 'set_speed_value_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='SetSpeedValueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_real_named_async(self, request):
        """查询SIM卡实名认证信息

        实时查询SIM卡实名认证信息。

        :param ShowRealNamedRequest request
        :return: ShowRealNamedResponse
        """
        return self.show_real_named_with_http_info(request)

    def show_real_named_with_http_info(self, request):
        """查询SIM卡实名认证信息

        实时查询SIM卡实名认证信息。

        :param ShowRealNamedRequest request
        :return: ShowRealNamedResponse
        """

        all_params = ['sim_card_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'sim_card_id' in local_var_params:
            path_params['sim_card_id'] = local_var_params['sim_card_id']

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
            resource_path='/v1/sim-cards/{sim_card_id}/real-named',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRealNamedResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_sim_card_async(self, request):
        """查询SIM卡详情

        查询SIM卡详情

        :param ShowSimCardRequest request
        :return: ShowSimCardResponse
        """
        return self.show_sim_card_with_http_info(request)

    def show_sim_card_with_http_info(self, request):
        """查询SIM卡详情

        查询SIM卡详情

        :param ShowSimCardRequest request
        :return: ShowSimCardResponse
        """

        all_params = ['sim_card_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'sim_card_id' in local_var_params:
            path_params['sim_card_id'] = local_var_params['sim_card_id']

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
            resource_path='/v1/sim-cards/{sim_card_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowSimCardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def start_stop_net_async(self, request):
        """SIM卡申请断网/恢复在用

        SIM卡申请断网/恢复在用,只支持电信卡。

        :param StartStopNetRequest request
        :return: StartStopNetResponse
        """
        return self.start_stop_net_with_http_info(request)

    def start_stop_net_with_http_info(self, request):
        """SIM卡申请断网/恢复在用

        SIM卡申请断网/恢复在用,只支持电信卡。

        :param StartStopNetRequest request
        :return: StartStopNetResponse
        """

        all_params = ['sim_card_id', 'start_stop_net_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='StartStopNetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def stop_sim_card_async(self, request):
        """SIM卡单卡停机

        创建停机申请，返回业务受理单号。1~2个工作日完成停机操作。

        :param StopSimCardRequest request
        :return: StopSimCardResponse
        """
        return self.stop_sim_card_with_http_info(request)

    def stop_sim_card_with_http_info(self, request):
        """SIM卡单卡停机

        创建停机申请，返回业务受理单号。1~2个工作日完成停机操作。

        :param StopSimCardRequest request
        :return: StopSimCardResponse
        """

        all_params = ['sim_card_id', 'stop_sim_card_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='StopSimCardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_sim_pool_members_async(self, request):
        """查询流量池成员列表

        查询流量池成员列表

        :param ListSimPoolMembersRequest request
        :return: ListSimPoolMembersResponse
        """
        return self.list_sim_pool_members_with_http_info(request)

    def list_sim_pool_members_with_http_info(self, request):
        """查询流量池成员列表

        查询流量池成员列表

        :param ListSimPoolMembersRequest request
        :return: ListSimPoolMembersResponse
        """

        all_params = ['sim_pool_id', 'billing_cycle', 'cid', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ListSimPoolMembersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_sim_pools_async(self, request):
        """查询流量池列表

        查询流量池列表

        :param ListSimPoolsRequest request
        :return: ListSimPoolsResponse
        """
        return self.list_sim_pools_with_http_info(request)

    def list_sim_pools_with_http_info(self, request):
        """查询流量池列表

        查询流量池列表

        :param ListSimPoolsRequest request
        :return: ListSimPoolsResponse
        """

        all_params = ['pool_name', 'limit', 'offset', 'billing_cycle']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ListSimPoolsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_flow_by_sim_cards_async(self, request):
        """批量查询实体卡流量

        批量查询实体卡流量

        :param ListFlowBySimCardsRequest request
        :return: ListFlowBySimCardsResponse
        """
        return self.list_flow_by_sim_cards_with_http_info(request)

    def list_flow_by_sim_cards_with_http_info(self, request):
        """批量查询实体卡流量

        批量查询实体卡流量

        :param ListFlowBySimCardsRequest request
        :return: ListFlowBySimCardsResponse
        """

        all_params = ['list_flow_by_sim_cards_request_body']
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
            resource_path='/v1/sim-price-plans/usage/batch-query',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListFlowBySimCardsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_sim_price_plans_async(self, request):
        """sim卡套餐列表查询

        SIM卡套餐列表查询，实体卡只会有一个套餐，eSIM/vSIM可能会有多个套餐

        :param ListSimPricePlansRequest request
        :return: ListSimPricePlansResponse
        """
        return self.list_sim_price_plans_with_http_info(request)

    def list_sim_price_plans_with_http_info(self, request):
        """sim卡套餐列表查询

        SIM卡套餐列表查询，实体卡只会有一个套餐，eSIM/vSIM可能会有多个套餐

        :param ListSimPricePlansRequest request
        :return: ListSimPricePlansResponse
        """

        all_params = ['sim_card_id', 'sim_price_plan_id', 'real_time', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sim_card_id' in local_var_params:
            query_params.append(('sim_card_id', local_var_params['sim_card_id']))
        if 'sim_price_plan_id' in local_var_params:
            query_params.append(('sim_price_plan_id', local_var_params['sim_price_plan_id']))
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
            response_type='ListSimPricePlansResponse',
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
