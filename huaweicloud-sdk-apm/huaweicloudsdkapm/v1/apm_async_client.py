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


class ApmAsyncClient(Client):
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
        super(ApmAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkapm.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "ApmClient":
            raise TypeError("client type error, support client type is ApmClient")

        return ClientBuilder(clazz)

    def create_ak_sk_async(self, request):
        """创建aksk

        创建aksk
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateAkSk
        :type request: :class:`huaweicloudsdkapm.v1.CreateAkSkRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.CreateAkSkResponse`
        """
        return self.create_ak_sk_with_http_info(request)

    def create_ak_sk_with_http_info(self, request):
        all_params = ['create_aksk_model']
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
            resource_path='/v1/apm2/access-keys',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAkSkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_ak_sk_async(self, request):
        """删除aksk

        删除aksk
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteAkSk
        :type request: :class:`huaweicloudsdkapm.v1.DeleteAkSkRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.DeleteAkSkResponse`
        """
        return self.delete_ak_sk_with_http_info(request)

    def delete_ak_sk_with_http_info(self, request):
        all_params = ['ak']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'ak' in local_var_params:
            path_params['ak'] = local_var_params['ak']

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
            resource_path='/v1/apm2/access-keys/{ak}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteAkSkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_ak_sks_async(self, request):
        """查询租户的aksk

        查询租户的aksk
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowAkSks
        :type request: :class:`huaweicloudsdkapm.v1.ShowAkSksRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowAkSksResponse`
        """
        return self.show_ak_sks_with_http_info(request)

    def show_ak_sks_with_http_info(self, request):
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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/access-keys',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowAkSksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_ak_sk_async(self, request):
        """获取ak/sk

        获取该用户创建的ak/sk列表。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListAkSk
        :type request: :class:`huaweicloudsdkapm.v1.ListAkSkRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListAkSkResponse`
        """
        return self.list_ak_sk_with_http_info(request)

    def list_ak_sk_with_http_info(self, request):
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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/systemmng/get-ak-sk-list',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAkSkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_business_async(self, request):
        """查询业务列表

        该接口用于查询对应用户下的业务。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListBusiness
        :type request: :class:`huaweicloudsdkapm.v1.ListBusinessRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListBusinessResponse`
        """
        return self.list_business_with_http_info(request)

    def list_business_with_http_info(self, request):
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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/apm2/openapi/cmdb/business/get-business-list',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListBusinessResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_env_monitor_item_async(self, request):
        """查询监控项列表

        查询监控项列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListEnvMonitorItem
        :type request: :class:`huaweicloudsdkapm.v1.ListEnvMonitorItemRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListEnvMonitorItemResponse`
        """
        return self.list_env_monitor_item_with_http_info(request)

    def list_env_monitor_item_with_http_info(self, request):
        all_params = ['x_business_id', 'get_env_monitor_item_list_param']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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
            resource_path='/v1/apm2/openapi/apm-service/monitor-item-mgr/get-env-monitor-item-list',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListEnvMonitorItemResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def save_monitor_item_config_async(self, request):
        """保存监控项

        保存监控项
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SaveMonitorItemConfig
        :type request: :class:`huaweicloudsdkapm.v1.SaveMonitorItemConfigRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.SaveMonitorItemConfigResponse`
        """
        return self.save_monitor_item_config_with_http_info(request)

    def save_monitor_item_config_with_http_info(self, request):
        all_params = ['x_business_id', 'save_monitor_item_param']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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
            resource_path='/v1/apm2/openapi/apm-service/monitor-item-mgr/save-monitor-item-config',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SaveMonitorItemConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_application_async(self, request):
        """对指定区域下的应用和环境及其探针情况进行搜索

        对指定区域下的应用和环境及其探针情况进行搜索
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SearchApplication
        :type request: :class:`huaweicloudsdkapm.v1.SearchApplicationRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.SearchApplicationResponse`
        """
        return self.search_application_with_http_info(request)

    def search_application_with_http_info(self, request):
        all_params = ['x_business_id', 'app_search_param']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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
            resource_path='/v1/apm2/openapi/apm-service/app-mgr/search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchApplicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_master_address_async(self, request):
        """查询master地址

        根据region名称获取该名称下的master服务podlb地址信息。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowMasterAddress
        :type request: :class:`huaweicloudsdkapm.v1.ShowMasterAddressRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowMasterAddressResponse`
        """
        return self.show_master_address_with_http_info(request)

    def show_master_address_with_http_info(self, request):
        all_params = ['region_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'region_name' in local_var_params:
            query_params.append(('region_name', local_var_params['region_name']))

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
            resource_path='/v1/apm2/openapi/systemmng/get-master-address',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMasterAddressResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_app_async(self, request):
        """根据组件id删除指定的组件

        该接口用于删除指定的组件
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteApp
        :type request: :class:`huaweicloudsdkapm.v1.DeleteAppRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.DeleteAppResponse`
        """
        return self.delete_app_with_http_info(request)

    def delete_app_with_http_info(self, request):
        all_params = ['application_id', 'x_business_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/cmdb/apps/delete-app/{application_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_env_async(self, request):
        """根据环境id删除指定的环境

        该接口用于删除指定的环境
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteEnv
        :type request: :class:`huaweicloudsdkapm.v1.DeleteEnvRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.DeleteEnvResponse`
        """
        return self.delete_env_with_http_info(request)

    def delete_env_with_http_info(self, request):
        all_params = ['env_id', 'x_business_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'env_id' in local_var_params:
            path_params['env_id'] = local_var_params['env_id']

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/cmdb/envs/delete-env/{env_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteEnvResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_app_envs_async(self, request):
        """获取组件下的环境列表

        获取组件下的环境列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListAppEnvs
        :type request: :class:`huaweicloudsdkapm.v1.ListAppEnvsRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListAppEnvsResponse`
        """
        return self.list_app_envs_with_http_info(request)

    def list_app_envs_with_http_info(self, request):
        all_params = ['app_id', 'x_business_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/cmdb/envs/get-app-envs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAppEnvsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apps_async(self, request):
        """获取组件列表

        获取组件列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListApps
        :type request: :class:`huaweicloudsdkapm.v1.ListAppsRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListAppsResponse`
        """
        return self.list_apps_with_http_info(request)

    def list_apps_with_http_info(self, request):
        all_params = ['business_id', 'x_business_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'business_id' in local_var_params:
            query_params.append(('business_id', local_var_params['business_id']))

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/cmdb/apps/get-apps',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAppsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_env_tags_async(self, request):
        """查询环境标签

        查询环境标签接口
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListEnvTags
        :type request: :class:`huaweicloudsdkapm.v1.ListEnvTagsRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListEnvTagsResponse`
        """
        return self.list_env_tags_with_http_info(request)

    def list_env_tags_with_http_info(self, request):
        all_params = ['x_business_id', 'tag_param']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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
            resource_path='/v1/apm2/openapi/cmdb/tag/get-env-tag-list',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListEnvTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_topology_tree_async(self, request):
        """获取业务树

        获取业务树
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowTopologyTree
        :type request: :class:`huaweicloudsdkapm.v1.ShowTopologyTreeRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowTopologyTreeResponse`
        """
        return self.show_topology_tree_with_http_info(request)

    def show_topology_tree_with_http_info(self, request):
        all_params = ['x_business_id', 'region_id', 'business_id', 'env_tag_id', 'env_keyword']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'business_id' in local_var_params:
            query_params.append(('business_id', local_var_params['business_id']))
        if 'env_tag_id' in local_var_params:
            query_params.append(('env_tag_id', local_var_params['env_tag_id']))
        if 'env_keyword' in local_var_params:
            query_params.append(('env_keyword', local_var_params['env_keyword']))

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/cmdb/topology-trees/get-topology-trees',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTopologyTreeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_open_region_async(self, request):
        """查询开通的region

        该接口用于查询用户开通的region信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListOpenRegion
        :type request: :class:`huaweicloudsdkapm.v1.ListOpenRegionRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListOpenRegionResponse`
        """
        return self.list_open_region_with_http_info(request)

    def list_open_region_with_http_info(self, request):
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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/region/get-opened-region',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListOpenRegionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_supported_region_async(self, request):
        """查询所有的支持的region

        查询所有的支持的region信息。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListSupportedRegion
        :type request: :class:`huaweicloudsdkapm.v1.ListSupportedRegionRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListSupportedRegionResponse`
        """
        return self.list_supported_region_with_http_info(request)

    def list_supported_region_with_http_info(self, request):
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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/region/get-all-supported-region',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSupportedRegionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_env_instances_async(self, request):
        """获取实例信息列表

        获取实例信息列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListEnvInstances
        :type request: :class:`huaweicloudsdkapm.v1.ListEnvInstancesRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListEnvInstancesResponse`
        """
        return self.list_env_instances_with_http_info(request)

    def list_env_instances_with_http_info(self, request):
        all_params = ['x_business_id', 'instance_search_param']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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
            resource_path='/v1/apm2/openapi/view/mainview/get-env-instance-list',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListEnvInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_clob_detail_async(self, request):
        """获取原始数据详情

        获取原始数据详情
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowClobDetail
        :type request: :class:`huaweicloudsdkapm.v1.ShowClobDetailRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowClobDetailResponse`
        """
        return self.show_clob_detail_with_http_info(request)

    def show_clob_detail_with_http_info(self, request):
        all_params = ['x_business_id', 'get_clob_detail_param']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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
            resource_path='/v1/apm2/openapi/view/metric/get-clob-detail',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowClobDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_env_monitor_items_async(self, request):
        """show_env_monitor_items

        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowEnvMonitorItems
        :type request: :class:`huaweicloudsdkapm.v1.ShowEnvMonitorItemsRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowEnvMonitorItemsResponse`
        """
        return self.show_env_monitor_items_with_http_info(request)

    def show_env_monitor_items_with_http_info(self, request):
        all_params = ['env_id', 'x_business_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/view/mainview/get-env-monitor-item-list',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowEnvMonitorItemsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_event_detail_async(self, request):
        """获取event的详情

        获取event的详情
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowEventDetail
        :type request: :class:`huaweicloudsdkapm.v1.ShowEventDetailRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowEventDetailResponse`
        """
        return self.show_event_detail_with_http_info(request)

    def show_event_detail_with_http_info(self, request):
        all_params = ['trace_id', 'span_id', 'event_id', 'env_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'trace_id' in local_var_params:
            query_params.append(('trace_id', local_var_params['trace_id']))
        if 'span_id' in local_var_params:
            query_params.append(('span_id', local_var_params['span_id']))
        if 'event_id' in local_var_params:
            query_params.append(('event_id', local_var_params['event_id']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))

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
            resource_path='/v1/apm2/openapi/view/trace/get-event-detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowEventDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_monitor_item_view_config_async(self, request):
        """查询监控项配置信息

        查询监控项配置信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowMonitorItemViewConfig
        :type request: :class:`huaweicloudsdkapm.v1.ShowMonitorItemViewConfigRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowMonitorItemViewConfigResponse`
        """
        return self.show_monitor_item_view_config_with_http_info(request)

    def show_monitor_item_view_config_with_http_info(self, request):
        all_params = ['env_id', 'collector_id', 'x_business_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'collector_id' in local_var_params:
            query_params.append(('collector_id', local_var_params['collector_id']))

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/view/config/get-monitor-item-view-config',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMonitorItemViewConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_raw_table_async(self, request):
        """获取原始数据表格

        获取原始数据表格
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowRawTable
        :type request: :class:`huaweicloudsdkapm.v1.ShowRawTableRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowRawTableResponse`
        """
        return self.show_raw_table_with_http_info(request)

    def show_raw_table_with_http_info(self, request):
        all_params = ['x_business_id', 'raw_table_param']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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
            resource_path='/v1/apm2/openapi/view/metric/raw-table',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRawTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_span_search_async(self, request):
        """查询span数据

        span数据查询接口
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowSpanSearch
        :type request: :class:`huaweicloudsdkapm.v1.ShowSpanSearchRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowSpanSearchResponse`
        """
        return self.show_span_search_with_http_info(request)

    def show_span_search_with_http_info(self, request):
        all_params = ['x_business_id', 'trace_search_param']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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
            resource_path='/v1/apm2/openapi/view/trace/span-search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowSpanSearchResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_sum_table_async(self, request):
        """获取汇总表格数据

        获取汇总表格数据
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowSumTable
        :type request: :class:`huaweicloudsdkapm.v1.ShowSumTableRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowSumTableResponse`
        """
        return self.show_sum_table_with_http_info(request)

    def show_sum_table_with_http_info(self, request):
        all_params = ['x_business_id', 'sum_table_param']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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
            resource_path='/v1/apm2/openapi/view/metric/sum-table',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowSumTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_topology_async(self, request):
        """调用链拓扑图

        调用链拓扑图
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowTopology
        :type request: :class:`huaweicloudsdkapm.v1.ShowTopologyRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowTopologyResponse`
        """
        return self.show_topology_with_http_info(request)

    def show_topology_with_http_info(self, request):
        all_params = ['trace_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'trace_id' in local_var_params:
            query_params.append(('trace_id', local_var_params['trace_id']))

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
            resource_path='/v1/apm2/openapi/view/trace/topology',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTopologyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_trace_events_async(self, request):
        """获取一个trace的所有调用链数据

        获取一个trace的所有调用链数据
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowTraceEvents
        :type request: :class:`huaweicloudsdkapm.v1.ShowTraceEventsRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowTraceEventsResponse`
        """
        return self.show_trace_events_with_http_info(request)

    def show_trace_events_with_http_info(self, request):
        all_params = ['trace_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'trace_id' in local_var_params:
            query_params.append(('trace_id', local_var_params['trace_id']))

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
            resource_path='/v1/apm2/openapi/view/trace/get-trace-events',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTraceEventsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_trend_async(self, request):
        """获取趋势图

        获取趋势图
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowTrend
        :type request: :class:`huaweicloudsdkapm.v1.ShowTrendRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowTrendResponse`
        """
        return self.show_trend_with_http_info(request)

    def show_trend_with_http_info(self, request):
        all_params = ['x_business_id', 'trend_param']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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
            resource_path='/v1/apm2/openapi/view/metric/trend',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTrendResponse',
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
