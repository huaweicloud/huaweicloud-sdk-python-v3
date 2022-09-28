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


class EiHealthClient(Client):
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
        super(EiHealthClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkeihealth.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "EiHealthClient":
            raise TypeError("client type error, support client type is EiHealthClient")

        return ClientBuilder(clazz)

    def batch_import_app(self, request):
        """导入应用

        批量导入应用
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for BatchImportApp
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchImportAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchImportAppResponse`
        """
        return self.batch_import_app_with_http_info(request)

    def batch_import_app_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'import_app_src_dto']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/apps/batch-import',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchImportAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_app(self, request):
        """创建应用

        创建应用
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateApp
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateAppResponse`
        """
        return self.create_app_with_http_info(request)

    def create_app_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'app_dto']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/apps',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_app(self, request):
        """删除应用

        删除应用
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteApp
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteAppResponse`
        """
        return self.delete_app_with_http_info(request)

    def delete_app_with_http_info(self, request):
        all_params = ['app_id', 'eihealth_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/apps/{app_id}',
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

    def list_app(self, request):
        """获取应用列表

        获取应用列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListApp
        :type request: :class:`huaweicloudsdkeihealth.v1.ListAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListAppResponse`
        """
        return self.list_app_with_http_info(request)

    def list_app_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'name', 'version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/apps',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_app(self, request):
        """获取应用详情

        获取应用详情
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowApp
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowAppResponse`
        """
        return self.show_app_with_http_info(request)

    def show_app_with_http_info(self, request):
        all_params = ['app_id', 'eihealth_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/apps/{app_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def subscribe_app(self, request):
        """订阅应用

        订阅应用
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SubscribeApp
        :type request: :class:`huaweicloudsdkeihealth.v1.SubscribeAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.SubscribeAppResponse`
        """
        return self.subscribe_app_with_http_info(request)

    def subscribe_app_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'subscribe_app_dto']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/apps/subscribe',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SubscribeAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_app(self, request):
        """更新应用

        更新应用
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateApp
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateAppResponse`
        """
        return self.update_app_with_http_info(request)

    def update_app_with_http_info(self, request):
        all_params = ['app_id', 'eihealth_project_id', 'app_dto']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/apps/{app_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_asset(self, request):
        """获取资产列表

        获取资产列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListAsset
        :type request: :class:`huaweicloudsdkeihealth.v1.ListAssetRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListAssetResponse`
        """
        return self.list_asset_with_http_info(request)

    def list_asset_with_http_info(self, request):
        all_params = ['scope', 'categories', 'key_word', 'labels', 'limit', 'offset', 'publishers', 'vendor_ids']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'categories' in local_var_params:
            query_params.append(('categories', local_var_params['categories']))
        if 'key_word' in local_var_params:
            query_params.append(('key_word', local_var_params['key_word']))
        if 'labels' in local_var_params:
            query_params.append(('labels', local_var_params['labels']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'publishers' in local_var_params:
            query_params.append(('publishers', local_var_params['publishers']))
        if 'scope' in local_var_params:
            query_params.append(('scope', local_var_params['scope']))
        if 'vendor_ids' in local_var_params:
            query_params.append(('vendor_ids', local_var_params['vendor_ids']))

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
            resource_path='/v1/{project_id}/assets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAssetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_property(self, request):
        """获取属性值列表

        获取属性值列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListProperty
        :type request: :class:`huaweicloudsdkeihealth.v1.ListPropertyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListPropertyResponse`
        """
        return self.list_property_with_http_info(request)

    def list_property_with_http_info(self, request):
        all_params = ['_property']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if '_property' in local_var_params:
            query_params.append(('property', local_var_params['_property']))

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
            resource_path='/v1/{project_id}/assets/properties',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPropertyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_asset(self, request):
        """查询资产详情

        查询资产详情
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowAsset
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowAssetRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowAssetResponse`
        """
        return self.show_asset_with_http_info(request)

    def show_asset_with_http_info(self, request):
        all_params = ['asset_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

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
            resource_path='/v1/{project_id}/assets/{asset_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowAssetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_asset_version(self, request):
        """查询资产版本详情

        查询资产版本详情
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowAssetVersion
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowAssetVersionRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowAssetVersionResponse`
        """
        return self.show_asset_version_with_http_info(request)

    def show_asset_version_with_http_info(self, request):
        all_params = ['asset_id', 'version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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
            resource_path='/v1/{project_id}/assets/{asset_id}/versions/{version}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowAssetVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_auto_job(self, request):
        """创建自动作业模板

        创建自动作业模板
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateAutoJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateAutoJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateAutoJobResponse`
        """
        return self.create_auto_job_with_http_info(request)

    def create_auto_job_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'auto_job_dto']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/auto-jobs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAutoJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_auto_job(self, request):
        """删除自动作业模板

        删除自动作业模板
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteAutoJob
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteAutoJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteAutoJobResponse`
        """
        return self.delete_auto_job_with_http_info(request)

    def delete_auto_job_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'auto_job_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'auto_job_id' in local_var_params:
            path_params['auto_job_id'] = local_var_params['auto_job_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/auto-jobs/{auto_job_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteAutoJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_auto_job(self, request):
        """获取自动作业模板列表

        获取自动作业模板列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListAutoJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ListAutoJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListAutoJobResponse`
        """
        return self.list_auto_job_with_http_info(request)

    def list_auto_job_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'x_language', 'limit', 'offset', 'sort_key', 'sort_dir']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/auto-jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAutoJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_auto_job(self, request):
        """查询自动作业模板

        查询自动作业模板
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowAutoJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowAutoJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowAutoJobResponse`
        """
        return self.show_auto_job_with_http_info(request)

    def show_auto_job_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'auto_job_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'auto_job_id' in local_var_params:
            path_params['auto_job_id'] = local_var_params['auto_job_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/auto-jobs/{auto_job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowAutoJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_auto_job(self, request):
        """启动自动作业

        启动自动作业
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for StartAutoJob
        :type request: :class:`huaweicloudsdkeihealth.v1.StartAutoJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.StartAutoJobResponse`
        """
        return self.start_auto_job_with_http_info(request)

    def start_auto_job_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'auto_job_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'auto_job_id' in local_var_params:
            path_params['auto_job_id'] = local_var_params['auto_job_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/auto-jobs/{auto_job_id}/start',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StartAutoJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_auto_job(self, request):
        """停止自动作业

        停止自动作业
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for StopAutoJob
        :type request: :class:`huaweicloudsdkeihealth.v1.StopAutoJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.StopAutoJobResponse`
        """
        return self.stop_auto_job_with_http_info(request)

    def stop_auto_job_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'auto_job_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'auto_job_id' in local_var_params:
            path_params['auto_job_id'] = local_var_params['auto_job_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/auto-jobs/{auto_job_id}/stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StopAutoJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_auto_job(self, request):
        """更新自动作业模板

        更新自动作业模板
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateAutoJob
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateAutoJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateAutoJobResponse`
        """
        return self.update_auto_job_with_http_info(request)

    def update_auto_job_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'auto_job_id', 'auto_job_dto']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'auto_job_id' in local_var_params:
            path_params['auto_job_id'] = local_var_params['auto_job_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/auto-jobs/{auto_job_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateAutoJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_computing_resource(self, request):
        """购买计算资源

        购买计算资源
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateComputingResource
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateComputingResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateComputingResourceResponse`
        """
        return self.create_computing_resource_with_http_info(request)

    def create_computing_resource_with_http_info(self, request):
        all_params = ['request']
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
            resource_path='/v1/{project_id}/system/computing-resources',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateComputingResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_computing_resource(self, request):
        """删除计算资源

        删除计算资源
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteComputingResource
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteComputingResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteComputingResourceResponse`
        """
        return self.delete_computing_resource_with_http_info(request)

    def delete_computing_resource_with_http_info(self, request):
        all_params = ['id']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/system/computing-resources/{id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteComputingResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_computing_resource_flavors(self, request):
        """查询计算资源规格

        查询计算资源规格
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListComputingResourceFlavors
        :type request: :class:`huaweicloudsdkeihealth.v1.ListComputingResourceFlavorsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListComputingResourceFlavorsResponse`
        """
        return self.list_computing_resource_flavors_with_http_info(request)

    def list_computing_resource_flavors_with_http_info(self, request):
        all_params = ['availability_zone_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'availability_zone_id' in local_var_params:
            query_params.append(('availability_zone_id', local_var_params['availability_zone_id']))

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
            resource_path='/v1/{project_id}/system/computing-resources/flavors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListComputingResourceFlavorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_computing_resources(self, request):
        """查询计算资源

        查询计算资源
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListComputingResources
        :type request: :class:`huaweicloudsdkeihealth.v1.ListComputingResourcesRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListComputingResourcesResponse`
        """
        return self.list_computing_resources_with_http_info(request)

    def list_computing_resources_with_http_info(self, request):
        all_params = ['label', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'label' in local_var_params:
            query_params.append(('label', local_var_params['label']))
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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/system/computing-resources',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListComputingResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reboot_node(self, request):
        """重启计算资源

        重启计算资源
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for RebootNode
        :type request: :class:`huaweicloudsdkeihealth.v1.RebootNodeRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.RebootNodeResponse`
        """
        return self.reboot_node_with_http_info(request)

    def reboot_node_with_http_info(self, request):
        all_params = ['id', 'force']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'force' in local_var_params:
            query_params.append(('force', local_var_params['force']))

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
            resource_path='/v1/{project_id}/system/computing-resources/{id}/reboot',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RebootNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_bms_devices(self, request):
        """查询bms计算资源显卡id列表

        查询bms计算资源显卡id列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowBmsDevices
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowBmsDevicesRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowBmsDevicesResponse`
        """
        return self.show_bms_devices_with_http_info(request)

    def show_bms_devices_with_http_info(self, request):
        all_params = ['id']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/system/computing-resources/{id}/devices',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowBmsDevicesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_evs_quota(self, request):
        """获取EVS配额及使用情况

        获取EVS配额及使用情况
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowEvsQuota
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowEvsQuotaRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowEvsQuotaResponse`
        """
        return self.show_evs_quota_with_http_info(request)

    def show_evs_quota_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/computing-resources/evs-quota',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowEvsQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_left_quota(self, request):
        """获取节点剩余配额

        获取节点剩余配额
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowLeftQuota
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowLeftQuotaRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowLeftQuotaResponse`
        """
        return self.show_left_quota_with_http_info(request)

    def show_left_quota_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/computing-resources/quota',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowLeftQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_schedule(self, request):
        """查询计算资源调度信息

        查询计算资源调度信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowSchedule
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowScheduleRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowScheduleResponse`
        """
        return self.show_schedule_with_http_info(request)

    def show_schedule_with_http_info(self, request):
        all_params = ['id']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/system/computing-resources/{id}/schedule',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowScheduleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_node(self, request):
        """启动计算资源

        启动计算资源
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for StartNode
        :type request: :class:`huaweicloudsdkeihealth.v1.StartNodeRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.StartNodeResponse`
        """
        return self.start_node_with_http_info(request)

    def start_node_with_http_info(self, request):
        all_params = ['id']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/system/computing-resources/{id}/start',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StartNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_node(self, request):
        """关闭计算资源

        关闭计算资源
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for StopNode
        :type request: :class:`huaweicloudsdkeihealth.v1.StopNodeRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.StopNodeResponse`
        """
        return self.stop_node_with_http_info(request)

    def stop_node_with_http_info(self, request):
        all_params = ['id', 'force']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'force' in local_var_params:
            query_params.append(('force', local_var_params['force']))

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
            resource_path='/v1/{project_id}/system/computing-resources/{id}/stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StopNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_schedule(self, request):
        """修改计算资源调度信息

        修改计算资源调度信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateSchedule
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateScheduleRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateScheduleResponse`
        """
        return self.update_schedule_with_http_info(request)

    def update_schedule_with_http_info(self, request):
        all_params = ['id', 'request']
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
            resource_path='/v1/{project_id}/system/computing-resources/{id}/schedule',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateScheduleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_backup(self, request):
        """归档数据

        将需要归档的重要数据拷贝到数据归档桶
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateBackup
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateBackupRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateBackupResponse`
        """
        return self.create_backup_with_http_info(request)

    def create_backup_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/backups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateBackupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_backup(self, request):
        """删除归档

        删除指定的归档
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteBackup
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteBackupRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteBackupResponse`
        """
        return self.delete_backup_with_http_info(request)

    def delete_backup_with_http_info(self, request):
        all_params = ['backup_id', 'eihealth_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/backups/{backup_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteBackupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_backup(self, request):
        """查询归档列表

        分页查询用户管理的项目的所有历史归档记录
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListBackup
        :type request: :class:`huaweicloudsdkeihealth.v1.ListBackupRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListBackupResponse`
        """
        return self.list_backup_with_http_info(request)

    def list_backup_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'limit', 'offset', 'sort_dir', 'sort_key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/backups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListBackupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restore_backup(self, request):
        """恢复归档

        将指定的归档数据拷贝到目标项目的某个目录下
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for RestoreBackup
        :type request: :class:`huaweicloudsdkeihealth.v1.RestoreBackupRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.RestoreBackupResponse`
        """
        return self.restore_backup_with_http_info(request)

    def restore_backup_with_http_info(self, request):
        all_params = ['backup_id', 'eihealth_project_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/backups/{backup_id}/restore',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RestoreBackupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_backup_path(self, request):
        """获取指定归档的全数据清单

        根据归档ID获取该归档的全数据清单
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowBackupPath
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowBackupPathRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowBackupPathResponse`
        """
        return self.show_backup_path_with_http_info(request)

    def show_backup_path_with_http_info(self, request):
        all_params = ['backup_id', 'eihealth_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/backups/{backup_id}/paths',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowBackupPathResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def copy_data(self, request):
        """复制项目数据

        复制项目数据
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CopyData
        :type request: :class:`huaweicloudsdkeihealth.v1.CopyDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CopyDataResponse`
        """
        return self.copy_data_with_http_info(request)

    def copy_data_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/clone',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CopyDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_data(self, request):
        """创建文件夹

        创建文件夹
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateData
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDataResponse`
        """
        return self.create_data_with_http_info(request)

    def create_data_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_data(self, request):
        """批量删除项目数据

        批量删除项目数据
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteData
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteDataResponse`
        """
        return self.delete_data_with_http_info(request)

    def delete_data_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def import_data(self, request):
        """导入项目数据

        导入项目数据
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ImportData
        :type request: :class:`huaweicloudsdkeihealth.v1.ImportDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImportDataResponse`
        """
        return self.import_data_with_http_info(request)

    def import_data_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/import',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ImportDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def import_network_data(self, request):
        """导入网上数据

        导入网上数据
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ImportNetworkData
        :type request: :class:`huaweicloudsdkeihealth.v1.ImportNetworkDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImportNetworkDataResponse`
        """
        return self.import_network_data_with_http_info(request)

    def import_network_data_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/import-from-network',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ImportNetworkDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_bucket(self, request):
        """获取桶列表

        获取桶列表(包含当前项目桶和引用项目桶)
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListBucket
        :type request: :class:`huaweicloudsdkeihealth.v1.ListBucketRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListBucketResponse`
        """
        return self.list_bucket_with_http_info(request)

    def list_bucket_with_http_info(self, request):
        all_params = ['eihealth_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/buckets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListBucketResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_data(self, request):
        """查询数据列表

        查询指定目录下的数据列表，如果不指定默认查询根目录
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListData
        :type request: :class:`huaweicloudsdkeihealth.v1.ListDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListDataResponse`
        """
        return self.list_data_with_http_info(request)

    def list_data_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'limit', 'offset', 'path', 'search_key', 'sort_dir', 'sort_key', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))
        if 'search_key' in local_var_params:
            query_params.append(('search_key', local_var_params['search_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def quote_data(self, request):
        """引用项目数据

        引用项目数据
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for QuoteData
        :type request: :class:`huaweicloudsdkeihealth.v1.QuoteDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.QuoteDataResponse`
        """
        return self.quote_data_with_http_info(request)

    def quote_data_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/quote',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='QuoteDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_bucket_storage(self, request):
        """获取桶存量信息

        获取桶存量信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowBucketStorage
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowBucketStorageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowBucketStorageResponse`
        """
        return self.show_bucket_storage_with_http_info(request)

    def show_bucket_storage_with_http_info(self, request):
        all_params = ['eihealth_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/bucket-storage',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowBucketStorageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_data(self, request):
        """获取指定数据对象

        获取指定数据对象的详细信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowData
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowDataResponse`
        """
        return self.show_data_with_http_info(request)

    def show_data_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'path']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'path' in local_var_params:
            path_params['path'] = local_var_params['path']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/{path}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_data_policy(self, request):
        """查询项目级数据权限控制策略

        查询项目级数据权限控制策略
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDataPolicy
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowDataPolicyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowDataPolicyResponse`
        """
        return self.show_data_policy_with_http_info(request)

    def show_data_policy_with_http_info(self, request):
        all_params = ['eihealth_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDataPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def subscribe_data(self, request):
        """订阅资产市场数据

        订阅资产市场数据
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SubscribeData
        :type request: :class:`huaweicloudsdkeihealth.v1.SubscribeDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.SubscribeDataResponse`
        """
        return self.subscribe_data_with_http_info(request)

    def subscribe_data_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/subscribe',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SubscribeDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_data_policy(self, request):
        """设置项目级权限控制策略

        设置项目级权限控制策略
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateDataPolicy
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateDataPolicyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateDataPolicyResponse`
        """
        return self.update_data_policy_with_http_info(request)

    def update_data_policy_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/policy',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateDataPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def upload_data(self, request):
        """上传数据文件

        上传数据文件
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UploadData
        :type request: :class:`huaweicloudsdkeihealth.v1.UploadDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UploadDataResponse`
        """
        return self.upload_data_with_http_info(request)

    def upload_data_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'file', 'target_folder', 'part_number', 'total_part', 'multipart_id', 'file_name', 'md5']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'target_folder' in local_var_params:
            query_params.append(('target_folder', local_var_params['target_folder']))
        if 'part_number' in local_var_params:
            query_params.append(('part_number', local_var_params['part_number']))
        if 'total_part' in local_var_params:
            query_params.append(('total_part', local_var_params['total_part']))
        if 'multipart_id' in local_var_params:
            query_params.append(('multipart_id', local_var_params['multipart_id']))
        if 'file_name' in local_var_params:
            query_params.append(('file_name', local_var_params['file_name']))
        if 'md5' in local_var_params:
            query_params.append(('md5', local_var_params['md5']))

        header_params = {}

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/upload',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UploadDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cancel_data_job(self, request):
        """取消数据作业

        取消数据作业
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CancelDataJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CancelDataJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CancelDataJobResponse`
        """
        return self.cancel_data_job_with_http_info(request)

    def cancel_data_job_with_http_info(self, request):
        all_params = ['data_job_id', 'eihealth_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'data_job_id' in local_var_params:
            path_params['data_job_id'] = local_var_params['data_job_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/data-jobs/{data_job_id}/cancel',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CancelDataJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_data_job(self, request):
        """删除数据作业

        删除数据作业
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteDataJob
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteDataJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteDataJobResponse`
        """
        return self.delete_data_job_with_http_info(request)

    def delete_data_job_with_http_info(self, request):
        all_params = ['data_job_id', 'eihealth_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'data_job_id' in local_var_params:
            path_params['data_job_id'] = local_var_params['data_job_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/data-jobs/{data_job_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteDataJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def download_data_job_log(self, request):
        """下载数据作业执行日志

        下载数据作业执行日志
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DownloadDataJobLog
        :type request: :class:`huaweicloudsdkeihealth.v1.DownloadDataJobLogRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DownloadDataJobLogResponse`
        """
        return self.download_data_job_log_with_http_info(request)

    def download_data_job_log_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'data_job_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'data_job_id' in local_var_params:
            path_params['data_job_id'] = local_var_params['data_job_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/data-jobs/{data_job_id}/logs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DownloadDataJobLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_checkpoint(self, request):
        """获取数据作业执行日志

        获取数据作业执行日志
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListCheckpoint
        :type request: :class:`huaweicloudsdkeihealth.v1.ListCheckpointRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListCheckpointResponse`
        """
        return self.list_checkpoint_with_http_info(request)

    def list_checkpoint_with_http_info(self, request):
        all_params = ['data_job_id', 'eihealth_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'data_job_id' in local_var_params:
            path_params['data_job_id'] = local_var_params['data_job_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/data-jobs/{data_job_id}/checkpoints',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCheckpointResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_data_job(self, request):
        """获取数据作业列表

        获取数据作业列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListDataJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ListDataJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListDataJobResponse`
        """
        return self.list_data_job_with_http_info(request)

    def list_data_job_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'creator', 'from_time', 'limit', 'name', 'offset', 'status', 'to_time', 'type', 'finish_from_time', 'finish_to_time', 'sort_dir', 'sort_key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'creator' in local_var_params:
            query_params.append(('creator', local_var_params['creator']))
        if 'from_time' in local_var_params:
            query_params.append(('from_time', local_var_params['from_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'to_time' in local_var_params:
            query_params.append(('to_time', local_var_params['to_time']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'finish_from_time' in local_var_params:
            query_params.append(('finish_from_time', local_var_params['finish_from_time']))
        if 'finish_to_time' in local_var_params:
            query_params.append(('finish_to_time', local_var_params['finish_to_time']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/data-jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListDataJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def retry_data_job(self, request):
        """重试数据作业

        重试数据作业
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for RetryDataJob
        :type request: :class:`huaweicloudsdkeihealth.v1.RetryDataJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.RetryDataJobResponse`
        """
        return self.retry_data_job_with_http_info(request)

    def retry_data_job_with_http_info(self, request):
        all_params = ['data_job_id', 'eihealth_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'data_job_id' in local_var_params:
            path_params['data_job_id'] = local_var_params['data_job_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/data-jobs/{data_job_id}/retry',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RetryDataJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_data_job(self, request):
        """获取数据作业详细信息

        获取数据作业详细信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDataJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowDataJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowDataJobResponse`
        """
        return self.show_data_job_with_http_info(request)

    def show_data_job_with_http_info(self, request):
        all_params = ['data_job_id', 'eihealth_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'data_job_id' in local_var_params:
            path_params['data_job_id'] = local_var_params['data_job_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/data-jobs/{data_job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDataJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_database_data(self, request):
        """插入单条数据

        插入单条数据
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateDatabaseData
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDatabaseDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDatabaseDataResponse`
        """
        return self.create_database_data_with_http_info(request)

    def create_database_data_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'database_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'database_id' in local_var_params:
            path_params['database_id'] = local_var_params['database_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases/{database_id}/data/insert',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateDatabaseDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_instance(self, request):
        """创建数据库实例

        创建数据库实例
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateInstance
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateInstanceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateInstanceResponse`
        """
        return self.create_instance_with_http_info(request)

    def create_instance_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_database_data(self, request):
        """删除数据

        删除指定行数据
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteDatabaseData
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteDatabaseDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteDatabaseDataResponse`
        """
        return self.delete_database_data_with_http_info(request)

    def delete_database_data_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'database_id', 'row_num']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'database_id' in local_var_params:
            path_params['database_id'] = local_var_params['database_id']
        if 'row_num' in local_var_params:
            path_params['row_num'] = local_var_params['row_num']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases/{database_id}/data/{row_num}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteDatabaseDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_instance(self, request):
        """删除实例

        删除实例
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteInstance
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteInstanceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteInstanceResponse`
        """
        return self.delete_instance_with_http_info(request)

    def delete_instance_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'database_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'database_id' in local_var_params:
            path_params['database_id'] = local_var_params['database_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases/{database_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def import_database_data(self, request):
        """导入数据

        导入数据
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ImportDatabaseData
        :type request: :class:`huaweicloudsdkeihealth.v1.ImportDatabaseDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImportDatabaseDataResponse`
        """
        return self.import_database_data_with_http_info(request)

    def import_database_data_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'database_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'database_id' in local_var_params:
            path_params['database_id'] = local_var_params['database_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases/{database_id}/data',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ImportDatabaseDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_database_data(self, request):
        """查询数据

        查询数据
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListDatabaseData
        :type request: :class:`huaweicloudsdkeihealth.v1.ListDatabaseDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListDatabaseDataResponse`
        """
        return self.list_database_data_with_http_info(request)

    def list_database_data_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'database_id', 'limit', 'query', 'offset', 'sort_key', 'sort_dir']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'database_id' in local_var_params:
            path_params['database_id'] = local_var_params['database_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'query' in local_var_params:
            query_params.append(('query', local_var_params['query']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases/{database_id}/data',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListDatabaseDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instance(self, request):
        """获取实例列表

        获取实例列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListInstance
        :type request: :class:`huaweicloudsdkeihealth.v1.ListInstanceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListInstanceResponse`
        """
        return self.list_instance_with_http_info(request)

    def list_instance_with_http_info(self, request):
        all_params = ['eihealth_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def quote_instance(self, request):
        """引用数据库实例

        引用数据库实例
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for QuoteInstance
        :type request: :class:`huaweicloudsdkeihealth.v1.QuoteInstanceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.QuoteInstanceResponse`
        """
        return self.quote_instance_with_http_info(request)

    def quote_instance_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases/batch-quote',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='QuoteInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_instance(self, request):
        """查询实例详情

        查询实例详情
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowInstance
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowInstanceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowInstanceResponse`
        """
        return self.show_instance_with_http_info(request)

    def show_instance_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'database_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'database_id' in local_var_params:
            path_params['database_id'] = local_var_params['database_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases/{database_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_database_data(self, request):
        """更新数据

        更新数据
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateDatabaseData
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateDatabaseDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateDatabaseDataResponse`
        """
        return self.update_database_data_with_http_info(request)

    def update_database_data_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'database_id', 'row_num', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'database_id' in local_var_params:
            path_params['database_id'] = local_var_params['database_id']
        if 'row_num' in local_var_params:
            path_params['row_num'] = local_var_params['row_num']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases/{database_id}/data/{row_num}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateDatabaseDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_database_resource(self, request):
        """购买数据库资源

        购买数据库资源
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateDatabaseResource
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDatabaseResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDatabaseResourceResponse`
        """
        return self.create_database_resource_with_http_info(request)

    def create_database_resource_with_http_info(self, request):
        all_params = ['request']
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
            resource_path='/v1/{project_id}/system/database-resources',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateDatabaseResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_database_resource(self, request):
        """删除数据库资源

        删除数据库资源
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteDatabaseResource
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteDatabaseResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteDatabaseResourceResponse`
        """
        return self.delete_database_resource_with_http_info(request)

    def delete_database_resource_with_http_info(self, request):
        all_params = ['id']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/system/database-resources/{id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteDatabaseResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_database_resource(self, request):
        """查询数据库资源

        查询数据库资源
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListDatabaseResource
        :type request: :class:`huaweicloudsdkeihealth.v1.ListDatabaseResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListDatabaseResourceResponse`
        """
        return self.list_database_resource_with_http_info(request)

    def list_database_resource_with_http_info(self, request):
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

        response_headers = ["X-Resource-Mappings"]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/system/database-resources',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListDatabaseResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_database_resource_flavor(self, request):
        """获取数据库资源规格列表

        获取数据库资源规格列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListDatabaseResourceFlavor
        :type request: :class:`huaweicloudsdkeihealth.v1.ListDatabaseResourceFlavorRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListDatabaseResourceFlavorResponse`
        """
        return self.list_database_resource_flavor_with_http_info(request)

    def list_database_resource_flavor_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/database-resources/flavors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListDatabaseResourceFlavorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_tag(self, request):
        """批量删除镜像tag

        批量删除镜像tag
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for BatchDeleteTag
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchDeleteTagRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchDeleteTagResponse`
        """
        return self.batch_delete_tag_with_http_info(request)

    def batch_delete_tag_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'image_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images/{image_id}/tags/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_image(self, request):
        """创建镜像

        创建镜像
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateImage
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateImageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateImageResponse`
        """
        return self.create_image_with_http_info(request)

    def create_image_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_image(self, request):
        """删除镜像仓库

        删除镜像仓库
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteImage
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteImageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteImageResponse`
        """
        return self.delete_image_with_http_info(request)

    def delete_image_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'image_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images/{image_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_tag(self, request):
        """删除指定镜像tag

        删除指定镜像tag
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteTag
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteTagRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteTagResponse`
        """
        return self.delete_tag_with_http_info(request)

    def delete_tag_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'image_id', 'tag']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']
        if 'tag' in local_var_params:
            path_params['tag'] = local_var_params['tag']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images/{image_id}/tags/{tag}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def import_image(self, request):
        """导入镜像

        导入镜像
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ImportImage
        :type request: :class:`huaweicloudsdkeihealth.v1.ImportImageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImportImageResponse`
        """
        return self.import_image_with_http_info(request)

    def import_image_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images/import',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ImportImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_image(self, request):
        """获取镜像列表

        获取镜像列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListImage
        :type request: :class:`huaweicloudsdkeihealth.v1.ListImageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListImageResponse`
        """
        return self.list_image_with_http_info(request)

    def list_image_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'type', 'name', 'show_empty']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'show_empty' in local_var_params:
            query_params.append(('show_empty', local_var_params['show_empty']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_image_tag(self, request):
        """获取指定镜像的tag列表

        获取指定镜像的tag列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListImageTag
        :type request: :class:`huaweicloudsdkeihealth.v1.ListImageTagRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListImageTagResponse`
        """
        return self.list_image_tag_with_http_info(request)

    def list_image_tag_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'image_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images/{image_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListImageTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_docker_login(self, request):
        """获取docker login指令

        获取docker login指令
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDockerLogin
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowDockerLoginRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowDockerLoginResponse`
        """
        return self.show_docker_login_with_http_info(request)

    def show_docker_login_with_http_info(self, request):
        all_params = ['eihealth_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images/docker-login-cmd',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDockerLoginResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def subscribe_image(self, request):
        """订阅镜像

        订阅镜像
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SubscribeImage
        :type request: :class:`huaweicloudsdkeihealth.v1.SubscribeImageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.SubscribeImageResponse`
        """
        return self.subscribe_image_with_http_info(request)

    def subscribe_image_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'subscribe_image_dto']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images/subscribe',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SubscribeImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_image(self, request):
        """更新镜像描述信息或者类型

        更新镜像描述信息或者类型
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateImage
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateImageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateImageResponse`
        """
        return self.update_image_with_http_info(request)

    def update_image_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'image_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images/{image_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job_config(self, request):
        """获取作业配置

        获取作业配置
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowJobConfig
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowJobConfigRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowJobConfigResponse`
        """
        return self.show_job_config_with_http_info(request)

    def show_job_config_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/job-config',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowJobConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_job_config(self, request):
        """设置作业配置

        设置作业配置，目前支持修改保存时长(180天 - 10年)、记录数(1W-500W)
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateJobConfig
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateJobConfigRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateJobConfigResponse`
        """
        return self.update_job_config_with_http_info(request)

    def update_job_config_with_http_info(self, request):
        all_params = ['job_config_dto']
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
            resource_path='/v1/{project_id}/system/job-config',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateJobConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cancel_job(self, request):
        """取消或强制停止作业调度

        取消或强制作业调度
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CancelJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CancelJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CancelJobResponse`
        """
        return self.cancel_job_with_http_info(request)

    def cancel_job_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'job_id', 'terminate_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}/terminate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CancelJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_job(self, request):
        """删除作业

        删除作业
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteJob
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteJobResponse`
        """
        return self.delete_job_with_http_info(request)

    def delete_job_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'job_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_job(self, request):
        """启动作业

        启动作业
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ExecuteJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ExecuteJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ExecuteJobResponse`
        """
        return self.execute_job_with_http_info(request)

    def execute_job_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'job_dto']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ExecuteJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_job(self, request):
        """获取作业列表

        获取作业列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ListJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListJobResponse`
        """
        return self.list_job_with_http_info(request)

    def list_job_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'end_time', 'job_name', 'labels', 'limit', 'offset', 'sort_dir', 'sort_key', 'start_time', 'status', 'tool_name', 'user_name', 'finish_start_time', 'finish_end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'job_name' in local_var_params:
            query_params.append(('job_name', local_var_params['job_name']))
        if 'labels' in local_var_params:
            query_params.append(('labels', local_var_params['labels']))
            collection_formats['labels'] = 'csv'
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'tool_name' in local_var_params:
            query_params.append(('tool_name', local_var_params['tool_name']))
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'finish_start_time' in local_var_params:
            query_params.append(('finish_start_time', local_var_params['finish_start_time']))
        if 'finish_end_time' in local_var_params:
            query_params.append(('finish_end_time', local_var_params['finish_end_time']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def retry_job(self, request):
        """重试作业

        重试作业
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for RetryJob
        :type request: :class:`huaweicloudsdkeihealth.v1.RetryJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.RetryJobResponse`
        """
        return self.retry_job_with_http_info(request)

    def retry_job_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'job_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}/retry',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RetryJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job(self, request):
        """获取作业详情

        获取作业详情
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowJobResponse`
        """
        return self.show_job_with_http_info(request)

    def show_job_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'job_id', 'x_addition_info']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_addition_info' in local_var_params:
            header_params['X-Addition-Info'] = local_var_params['x_addition_info']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job_event(self, request):
        """获取作业事件

        获取作业事件
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowJobEvent
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowJobEventRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowJobEventResponse`
        """
        return self.show_job_event_with_http_info(request)

    def show_job_event_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'job_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}/events',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowJobEventResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job_log(self, request):
        """获取作业日志

        获取作业日志
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowJobLog
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowJobLogRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowJobLogResponse`
        """
        return self.show_job_log_with_http_info(request)

    def show_job_log_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'job_id', 'task_name', 'task_index']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'task_name' in local_var_params:
            query_params.append(('task_name', local_var_params['task_name']))
        if 'task_index' in local_var_params:
            query_params.append(('task_index', local_var_params['task_index']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}/logs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowJobLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_task_events(self, request):
        """获取子任务启动事件

        获取子任务启动事件
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowTaskEvents
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowTaskEventsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowTaskEventsResponse`
        """
        return self.show_task_events_with_http_info(request)

    def show_task_events_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'job_id', 'task_name', 'task_index']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'task_name' in local_var_params:
            path_params['task_name'] = local_var_params['task_name']

        query_params = []
        if 'task_index' in local_var_params:
            query_params.append(('task_index', local_var_params['task_index']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}/tasks/{task_name}/events',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTaskEventsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_task_instance_events(self, request):
        """获取子任务中实例的事件

        获取子任务中实例的事件
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowTaskInstanceEvents
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstanceEventsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstanceEventsResponse`
        """
        return self.show_task_instance_events_with_http_info(request)

    def show_task_instance_events_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'job_id', 'task_name', 'instance_name', 'task_index']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'task_name' in local_var_params:
            path_params['task_name'] = local_var_params['task_name']
        if 'instance_name' in local_var_params:
            path_params['instance_name'] = local_var_params['instance_name']

        query_params = []
        if 'task_index' in local_var_params:
            query_params.append(('task_index', local_var_params['task_index']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}/tasks/{task_name}/instances/{instance_name}/events',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTaskInstanceEventsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_task_instance_pod(self, request):
        """获取子任务中实例的pod信息

        获取子任务中实例的pod信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowTaskInstancePod
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstancePodRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstancePodResponse`
        """
        return self.show_task_instance_pod_with_http_info(request)

    def show_task_instance_pod_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'job_id', 'task_name', 'instance_name', 'task_index']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'task_name' in local_var_params:
            path_params['task_name'] = local_var_params['task_name']
        if 'instance_name' in local_var_params:
            path_params['instance_name'] = local_var_params['instance_name']

        query_params = []
        if 'task_index' in local_var_params:
            query_params.append(('task_index', local_var_params['task_index']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}/tasks/{task_name}/instances/{instance_name}/pod',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTaskInstancePodResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_task_instances(self, request):
        """获取子任务实例信息

        获取子任务实例信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowTaskInstances
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstancesRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstancesResponse`
        """
        return self.show_task_instances_with_http_info(request)

    def show_task_instances_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'job_id', 'task_name', 'task_index']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'task_name' in local_var_params:
            path_params['task_name'] = local_var_params['task_name']

        query_params = []
        if 'task_index' in local_var_params:
            query_params.append(('task_index', local_var_params['task_index']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}/tasks/{task_name}/instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTaskInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_label(self, request):
        """创建标签

        创建标签
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateLabel
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateLabelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateLabelResponse`
        """
        return self.create_label_with_http_info(request)

    def create_label_with_http_info(self, request):
        all_params = ['label']
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
            resource_path='/v1/{project_id}/system/labels',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateLabelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_label(self, request):
        """删除标签

        删除标签
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteLabel
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteLabelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteLabelResponse`
        """
        return self.delete_label_with_http_info(request)

    def delete_label_with_http_info(self, request):
        all_params = ['label_id']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/system/labels/{label_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteLabelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_label(self, request):
        """获取标签列表

        获取标签列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListLabel
        :type request: :class:`huaweicloudsdkeihealth.v1.ListLabelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListLabelResponse`
        """
        return self.list_label_with_http_info(request)

    def list_label_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/labels',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListLabelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_label_page(self, request):
        """创建标签页面

        创建标签页面
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateLabelPage
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateLabelPageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateLabelPageResponse`
        """
        return self.create_label_page_with_http_info(request)

    def create_label_page_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'label_page_dto']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/label-pages',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateLabelPageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_label_page(self, request):
        """删除标签页面

        删除标签页面
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteLabelPage
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteLabelPageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteLabelPageResponse`
        """
        return self.delete_label_page_with_http_info(request)

    def delete_label_page_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'label_page_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'label_page_id' in local_var_params:
            path_params['label_page_id'] = local_var_params['label_page_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/label-pages/{label_page_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteLabelPageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_label_page(self, request):
        """获取标签页面列表

        获取标签页面列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListLabelPage
        :type request: :class:`huaweicloudsdkeihealth.v1.ListLabelPageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListLabelPageResponse`
        """
        return self.list_label_page_with_http_info(request)

    def list_label_page_with_http_info(self, request):
        all_params = ['eihealth_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/label-pages',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListLabelPageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_email_connection(self, request):
        """邮箱连通性测试

        邮箱连通性测试
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CheckEmailConnection
        :type request: :class:`huaweicloudsdkeihealth.v1.CheckEmailConnectionRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CheckEmailConnectionResponse`
        """
        return self.check_email_connection_with_http_info(request)

    def check_email_connection_with_http_info(self, request):
        all_params = ['message_email_config_dto']
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
            resource_path='/v1/{project_id}/messages/email-connection-test',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CheckEmailConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_message_email_config(self, request):
        """删除消息邮件配置

        删除消息邮件配置
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteMessageEmailConfig
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteMessageEmailConfigRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteMessageEmailConfigResponse`
        """
        return self.delete_message_email_config_with_http_info(request)

    def delete_message_email_config_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/messages/email-server-config',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteMessageEmailConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_message(self, request):
        """获取消息列表

        从消息中心获取当前用户有权限查看的消息列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListMessage
        :type request: :class:`huaweicloudsdkeihealth.v1.ListMessageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListMessageResponse`
        """
        return self.list_message_with_http_info(request)

    def list_message_with_http_info(self, request):
        all_params = ['eihealth_project_name', 'limit', 'message_type', 'offset', 'operator', 'resource_type', 'status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'eihealth_project_name' in local_var_params:
            query_params.append(('eihealth_project_name', local_var_params['eihealth_project_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'message_type' in local_var_params:
            query_params.append(('message_type', local_var_params['message_type']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'operator' in local_var_params:
            query_params.append(('operator', local_var_params['operator']))
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))
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
            resource_path='/v1/{project_id}/messages',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListMessageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_message_clear_rule(self, request):
        """获取消息清理规则

        获取消息清理规则
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowMessageClearRule
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowMessageClearRuleRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowMessageClearRuleResponse`
        """
        return self.show_message_clear_rule_with_http_info(request)

    def show_message_clear_rule_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/messages/rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMessageClearRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_message_email_config(self, request):
        """获取消息邮件配置

        获取消息邮件配置
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowMessageEmailConfig
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowMessageEmailConfigRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowMessageEmailConfigResponse`
        """
        return self.show_message_email_config_with_http_info(request)

    def show_message_email_config_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/messages/email-server-config',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMessageEmailConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_message_receive_config(self, request):
        """获取用户邮件配置

        获取用户邮件配置
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowMessageReceiveConfig
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowMessageReceiveConfigRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowMessageReceiveConfigResponse`
        """
        return self.show_message_receive_config_with_http_info(request)

    def show_message_receive_config_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/messages/email-client-config',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMessageReceiveConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_message_clear_rule(self, request):
        """设置消息清理规则

        设置消息清理规则，支持修改保存时长(180天 - 10年)、记录数(1W-500W)
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateMessageClearRule
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateMessageClearRuleRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateMessageClearRuleResponse`
        """
        return self.update_message_clear_rule_with_http_info(request)

    def update_message_clear_rule_with_http_info(self, request):
        all_params = ['message_clear_rules_dto']
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
            resource_path='/v1/{project_id}/messages/rules',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateMessageClearRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_message_email_config(self, request):
        """设置消息邮件配置

        设置消息邮件配置
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateMessageEmailConfig
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateMessageEmailConfigRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateMessageEmailConfigResponse`
        """
        return self.update_message_email_config_with_http_info(request)

    def update_message_email_config_with_http_info(self, request):
        all_params = ['message_email_config_dto']
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
            resource_path='/v1/{project_id}/messages/email-server-config',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateMessageEmailConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_message_receive_config(self, request):
        """设置用户邮件配置

        设置用户邮件配置
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateMessageReceiveConfig
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateMessageReceiveConfigRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateMessageReceiveConfigResponse`
        """
        return self.update_message_receive_config_with_http_info(request)

    def update_message_receive_config_with_http_info(self, request):
        all_params = ['message_receive_config_dto']
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
            resource_path='/v1/{project_id}/messages/email-client-config',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateMessageReceiveConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_update_node_label(self, request):
        """设置节点标签

        设置节点标签
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for BatchUpdateNodeLabel
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchUpdateNodeLabelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchUpdateNodeLabelResponse`
        """
        return self.batch_update_node_label_with_http_info(request)

    def batch_update_node_label_with_http_info(self, request):
        all_params = ['server_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/system/nodes/{server_id}/labels',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchUpdateNodeLabelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_cluster_all_node_label(self, request):
        """获取节点标签集

        获取节点标签集
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListClusterAllNodeLabel
        :type request: :class:`huaweicloudsdkeihealth.v1.ListClusterAllNodeLabelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListClusterAllNodeLabelResponse`
        """
        return self.list_cluster_all_node_label_with_http_info(request)

    def list_cluster_all_node_label_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/cluster/labels',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListClusterAllNodeLabelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_node_label(self, request):
        """获取节点标签集

        获取节点标签集
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListNodeLabel
        :type request: :class:`huaweicloudsdkeihealth.v1.ListNodeLabelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListNodeLabelResponse`
        """
        return self.list_node_label_with_http_info(request)

    def list_node_label_with_http_info(self, request):
        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/system/nodes/{server_id}/labels',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListNodeLabelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_preset_label(self, request):
        """获取预置标签列表

        获取预置标签列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListPresetLabel
        :type request: :class:`huaweicloudsdkeihealth.v1.ListPresetLabelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListPresetLabelResponse`
        """
        return self.list_preset_label_with_http_info(request)

    def list_preset_label_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/preset-labels',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPresetLabelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_notebook(self, request):
        """创建notebook

        创建notebook
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateNotebook
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateNotebookRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateNotebookResponse`
        """
        return self.create_notebook_with_http_info(request)

    def create_notebook_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/notebooks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateNotebookResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_notebook(self, request):
        """删除notebook

        删除notebook
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteNotebook
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteNotebookRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteNotebookResponse`
        """
        return self.delete_notebook_with_http_info(request)

    def delete_notebook_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'notebook_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'notebook_id' in local_var_params:
            path_params['notebook_id'] = local_var_params['notebook_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/notebooks/{notebook_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteNotebookResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_notebook(self, request):
        """获取notebook列表

        获取notebook列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListNotebook
        :type request: :class:`huaweicloudsdkeihealth.v1.ListNotebookRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListNotebookResponse`
        """
        return self.list_notebook_with_http_info(request)

    def list_notebook_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'limit', 'name', 'offset', 'status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/notebooks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListNotebookResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_notebook_tool(self, request):
        """获取notebook工作环境

        获取notebook工作环境
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListNotebookTool
        :type request: :class:`huaweicloudsdkeihealth.v1.ListNotebookToolRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListNotebookToolResponse`
        """
        return self.list_notebook_tool_with_http_info(request)

    def list_notebook_tool_with_http_info(self, request):
        all_params = ['eihealth_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/notebooks/tools',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListNotebookToolResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_notebook(self, request):
        """获取notebook详情

        获取notebook详情
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowNotebook
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowNotebookRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowNotebookResponse`
        """
        return self.show_notebook_with_http_info(request)

    def show_notebook_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'notebook_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'notebook_id' in local_var_params:
            path_params['notebook_id'] = local_var_params['notebook_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/notebooks/{notebook_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowNotebookResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_notebook_token(self, request):
        """获取notebook鉴权信息

        获取notebook鉴权信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowNotebookToken
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowNotebookTokenRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowNotebookTokenResponse`
        """
        return self.show_notebook_token_with_http_info(request)

    def show_notebook_token_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'notebook_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'notebook_id' in local_var_params:
            path_params['notebook_id'] = local_var_params['notebook_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/notebooks/{notebook_id}/token',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowNotebookTokenResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_or_start_notebook(self, request):
        """启停notebook

        启停notebook
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for StopOrStartNotebook
        :type request: :class:`huaweicloudsdkeihealth.v1.StopOrStartNotebookRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.StopOrStartNotebookResponse`
        """
        return self.stop_or_start_notebook_with_http_info(request)

    def stop_or_start_notebook_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'notebook_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'notebook_id' in local_var_params:
            path_params['notebook_id'] = local_var_params['notebook_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/notebooks/{notebook_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StopOrStartNotebookResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_notebook(self, request):
        """更新notebook

        更新notebook
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateNotebook
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateNotebookRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateNotebookResponse`
        """
        return self.update_notebook_with_http_info(request)

    def update_notebook_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'notebook_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'notebook_id' in local_var_params:
            path_params['notebook_id'] = local_var_params['notebook_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/notebooks/{notebook_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateNotebookResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_obs_bucket(self, request):
        """获取用户OBS桶列表

        获取用户OBS桶列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListObsBucket
        :type request: :class:`huaweicloudsdkeihealth.v1.ListObsBucketRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListObsBucketResponse`
        """
        return self.list_obs_bucket_with_http_info(request)

    def list_obs_bucket_with_http_info(self, request):
        all_params = ['type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

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
            resource_path='/v1/{project_id}/customer-buckets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListObsBucketResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_obs_bucket_object(self, request):
        """获取用户OBS桶内对象

        获取用户OBS桶内对象
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListObsBucketObject
        :type request: :class:`huaweicloudsdkeihealth.v1.ListObsBucketObjectRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListObsBucketObjectResponse`
        """
        return self.list_obs_bucket_object_with_http_info(request)

    def list_obs_bucket_object_with_http_info(self, request):
        all_params = ['bucket_name', 'limit', 'offset', 'path']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'bucket_name' in local_var_params:
            path_params['bucket_name'] = local_var_params['bucket_name']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))

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
            resource_path='/v1/{project_id}/customer-buckets/{bucket_name}/objects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListObsBucketObjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_overview(self, request):
        """获取医疗平台信息

        获取医疗平台信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowOverview
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowOverviewRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowOverviewResponse`
        """
        return self.show_overview_with_http_info(request)

    def show_overview_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/overview',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowOverviewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_performance_resource(self, request):
        """购买性能加速资源

        购买性能加速资源
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreatePerformanceResource
        :type request: :class:`huaweicloudsdkeihealth.v1.CreatePerformanceResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreatePerformanceResourceResponse`
        """
        return self.create_performance_resource_with_http_info(request)

    def create_performance_resource_with_http_info(self, request):
        all_params = ['request']
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
            resource_path='/v1/{project_id}/system/performance-resources',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreatePerformanceResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_performance_resource(self, request):
        """删除性能加速资源

        删除性能加速资源
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeletePerformanceResource
        :type request: :class:`huaweicloudsdkeihealth.v1.DeletePerformanceResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeletePerformanceResourceResponse`
        """
        return self.delete_performance_resource_with_http_info(request)

    def delete_performance_resource_with_http_info(self, request):
        all_params = ['id']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/system/performance-resources/{id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeletePerformanceResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_performance_resources(self, request):
        """查询性能加速资源

        查询性能加速资源
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListPerformanceResources
        :type request: :class:`huaweicloudsdkeihealth.v1.ListPerformanceResourcesRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListPerformanceResourcesResponse`
        """
        return self.list_performance_resources_with_http_info(request)

    def list_performance_resources_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/performance-resources',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPerformanceResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_performance_resource(self, request):
        """更新性能加速资源配置

        更新性能加速资源配置
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdatePerformanceResource
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdatePerformanceResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdatePerformanceResourceResponse`
        """
        return self.update_performance_resource_with_http_info(request)

    def update_performance_resource_with_http_info(self, request):
        all_params = ['id', 'request']
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
            resource_path='/v1/{project_id}/system/performance-resources/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePerformanceResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_member(self, request):
        """批量删除项目成员

        批量删除项目成员
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for BatchDeleteMember
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchDeleteMemberRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchDeleteMemberResponse`
        """
        return self.batch_delete_member_with_http_info(request)

    def batch_delete_member_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/members/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_project(self, request):
        """创建项目

        创建项目
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateProject
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateProjectRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateProjectResponse`
        """
        return self.create_project_with_http_info(request)

    def create_project_with_http_info(self, request):
        all_params = ['request']
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
            resource_path='/v1/{project_id}/eihealth-projects',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_member(self, request):
        """移除项目成员

        移除项目成员
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteMember
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteMemberRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteMemberResponse`
        """
        return self.delete_member_with_http_info(request)

    def delete_member_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'user_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/members/{user_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_project(self, request):
        """删除项目

        删除项目
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteProject
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteProjectRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteProjectResponse`
        """
        return self.delete_project_with_http_info(request)

    def delete_project_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'x_delete_now']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []

        header_params = {}
        if 'x_delete_now' in local_var_params:
            header_params['X-Delete-Now'] = local_var_params['x_delete_now']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_project(self, request):
        """获取项目列表

        获取项目列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListProject
        :type request: :class:`huaweicloudsdkeihealth.v1.ListProjectRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListProjectResponse`
        """
        return self.list_project_with_http_info(request)

    def list_project_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/eihealth-projects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_recent_job(self, request):
        """获取最近的作业列表

        获取最近的作业列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListRecentJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ListRecentJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListRecentJobResponse`
        """
        return self.list_recent_job_with_http_info(request)

    def list_recent_job_with_http_info(self, request):
        all_params = ['limit', 'offset']
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
            resource_path='/v1/{project_id}/recent-jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRecentJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_project(self, request):
        """获取项目详情

        获取项目详情
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowProject
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowProjectRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowProjectResponse`
        """
        return self.show_project_with_http_info(request)

    def show_project_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'x_bucket_name', 'x_namespace_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []

        header_params = {}
        if 'x_bucket_name' in local_var_params:
            header_params['X-Bucket-Name'] = local_var_params['x_bucket_name']
        if 'x_namespace_name' in local_var_params:
            header_params['X-Namespace-Name'] = local_var_params['x_namespace_name']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def transfer_project(self, request):
        """转移项目

        转移项目
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for TransferProject
        :type request: :class:`huaweicloudsdkeihealth.v1.TransferProjectRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.TransferProjectResponse`
        """
        return self.transfer_project_with_http_info(request)

    def transfer_project_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/transfer',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='TransferProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_member(self, request):
        """更新或者添加项目成员角色

        更新或者添加项目成员角色
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateMember
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateMemberRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateMemberResponse`
        """
        return self.update_member_with_http_info(request)

    def update_member_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'user_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/members/{user_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_project(self, request):
        """更新项目

        更新项目
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateProject
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateProjectRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateProjectResponse`
        """
        return self.update_project_with_http_info(request)

    def update_project_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def download_data_trace(self, request):
        """下载近一万条审计日志

        下载近一万条审计日志
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DownloadDataTrace
        :type request: :class:`huaweicloudsdkeihealth.v1.DownloadDataTraceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DownloadDataTraceResponse`
        """
        return self.download_data_trace_with_http_info(request)

    def download_data_trace_with_http_info(self, request):
        all_params = ['x_language', 'eihealth_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/data-traces',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DownloadDataTraceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_project_trace(self, request):
        """获取项目审计日志

        获取项目审计日志
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowProjectTrace
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowProjectTraceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowProjectTraceResponse`
        """
        return self.show_project_trace_with_http_info(request)

    def show_project_trace_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'path', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))
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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/project-traces',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowProjectTraceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_project_trace_data(self, request):
        """获取指定审计日志

        获取指定审计日志
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowProjectTraceData
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowProjectTraceDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowProjectTraceDataResponse`
        """
        return self.show_project_trace_data_with_http_info(request)

    def show_project_trace_data_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'path']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'path' in local_var_params:
            path_params['path'] = local_var_params['path']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/project-traces/{path}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowProjectTraceDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_project_tracker(self, request):
        """获取项目审计日志追踪器

        获取项目审计日志追踪器
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowProjectTracker
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowProjectTrackerRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowProjectTrackerResponse`
        """
        return self.show_project_tracker_with_http_info(request)

    def show_project_tracker_with_http_info(self, request):
        all_params = ['eihealth_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/project-tracker',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowProjectTrackerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_project_tracker(self, request):
        """更新项目审计日志追踪器配置

        更新项目审计日志追踪器配置
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateProjectTracker
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateProjectTrackerRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateProjectTrackerResponse`
        """
        return self.update_project_tracker_with_http_info(request)

    def update_project_tracker_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'update_tracker_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/project-tracker',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateProjectTrackerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_resource_metric_data(self, request):
        """获取资源监控数据

        获取资源监控数据
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowResourceMetricData
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowResourceMetricDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowResourceMetricDataResponse`
        """
        return self.show_resource_metric_data_with_http_info(request)

    def show_resource_metric_data_with_http_info(self, request):
        all_params = ['metric_name', 'from_time', 'to_time', 'period', 'method', 'resource_id', 'device_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'from_time' in local_var_params:
            query_params.append(('from_time', local_var_params['from_time']))
        if 'to_time' in local_var_params:
            query_params.append(('to_time', local_var_params['to_time']))
        if 'period' in local_var_params:
            query_params.append(('period', local_var_params['period']))
        if 'method' in local_var_params:
            query_params.append(('method', local_var_params['method']))
        if 'metric_name' in local_var_params:
            query_params.append(('metric_name', local_var_params['metric_name']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'device_id' in local_var_params:
            query_params.append(('device_id', local_var_params['device_id']))

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
            resource_path='/v1/{project_id}/metric-data',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowResourceMetricDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_star(self, request):
        """取消收藏

        取消收藏
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteStar
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteStarRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteStarResponse`
        """
        return self.delete_star_with_http_info(request)

    def delete_star_with_http_info(self, request):
        all_params = ['asset_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

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
            resource_path='/v1/{project_id}/assets/{asset_id}/stars',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteStarResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_star(self, request):
        """获取收藏资产列表

        获取收藏资产列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListStar
        :type request: :class:`huaweicloudsdkeihealth.v1.ListStarRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListStarResponse`
        """
        return self.list_star_with_http_info(request)

    def list_star_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/assets/stars',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListStarResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_star(self, request):
        """收藏资产

        收藏资产
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateStar
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateStarRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateStarResponse`
        """
        return self.update_star_with_http_info(request)

    def update_star_with_http_info(self, request):
        all_params = ['asset_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

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
            resource_path='/v1/{project_id}/assets/{asset_id}/stars',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateStarResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_performance_resource_stat(self, request):
        """获取性能加速资源上统计信息

        获取性能加速资源上统计信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListPerformanceResourceStat
        :type request: :class:`huaweicloudsdkeihealth.v1.ListPerformanceResourceStatRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListPerformanceResourceStatResponse`
        """
        return self.list_performance_resource_stat_with_http_info(request)

    def list_performance_resource_stat_with_http_info(self, request):
        all_params = ['limit', 'offset']
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
            resource_path='/v1/{project_id}/eihealth-projects/performance-resources-statistics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPerformanceResourceStatResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_workflow_statistic(self, request):
        """统计应用、流程、作业数目

        统计应用、流程、作业数目
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListWorkflowStatistic
        :type request: :class:`huaweicloudsdkeihealth.v1.ListWorkflowStatisticRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListWorkflowStatisticResponse`
        """
        return self.list_workflow_statistic_with_http_info(request)

    def list_workflow_statistic_with_http_info(self, request):
        all_params = ['eihealth_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/statistics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListWorkflowStatisticResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_storage_resources(self, request):
        """查询存储资源

        查询存储资源
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListStorageResources
        :type request: :class:`huaweicloudsdkeihealth.v1.ListStorageResourcesRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListStorageResourcesResponse`
        """
        return self.list_storage_resources_with_http_info(request)

    def list_storage_resources_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/storage-resources',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListStorageResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_study(self, request):
        """创建study

        创建study
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateStudy
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateStudyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateStudyResponse`
        """
        return self.create_study_with_http_info(request)

    def create_study_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'create_study_dto']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/studies',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateStudyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_study_job(self, request):
        """创建study作业

        创建study作业
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateStudyJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateStudyJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateStudyJobResponse`
        """
        return self.create_study_job_with_http_info(request)

    def create_study_job_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'study_id', 'record_study_result_dto']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'study_id' in local_var_params:
            path_params['study_id'] = local_var_params['study_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/studies/{study_id}/jobs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateStudyJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_study(self, request):
        """删除study

        删除study
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteStudy
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteStudyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteStudyResponse`
        """
        return self.delete_study_with_http_info(request)

    def delete_study_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'study_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'study_id' in local_var_params:
            path_params['study_id'] = local_var_params['study_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/studies/{study_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteStudyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_study(self, request):
        """列举study

        列举study
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListStudy
        :type request: :class:`huaweicloudsdkeihealth.v1.ListStudyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListStudyResponse`
        """
        return self.list_study_with_http_info(request)

    def list_study_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/studies',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListStudyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_study_job(self, request):
        """列举study所有作业

        列举study所有作业
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListStudyJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ListStudyJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListStudyJobResponse`
        """
        return self.list_study_job_with_http_info(request)

    def list_study_job_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'study_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'study_id' in local_var_params:
            path_params['study_id'] = local_var_params['study_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/studies/{study_id}/jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListStudyJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show3d_structure_content(self, request):
        """获取生成study作业3D结构的内容

        获取生成study作业3D结构的内容
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for Show3dStructureContent
        :type request: :class:`huaweicloudsdkeihealth.v1.Show3dStructureContentRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.Show3dStructureContentResponse`
        """
        return self.show3d_structure_content_with_http_info(request)

    def show3d_structure_content_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'study_id', 'job_id', 'ligand', 'receptor']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'study_id' in local_var_params:
            path_params['study_id'] = local_var_params['study_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'ligand' in local_var_params:
            query_params.append(('ligand', local_var_params['ligand']))
        if 'receptor' in local_var_params:
            query_params.append(('receptor', local_var_params['receptor']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/studies/{study_id}/jobs/{job_id}/3d-structure',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='Show3dStructureContentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_extremum_info(self, request):
        """获取study作业的最值信息

        获取study作业的最值信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowExtremumInfo
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowExtremumInfoRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowExtremumInfoResponse`
        """
        return self.show_extremum_info_with_http_info(request)

    def show_extremum_info_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'study_id', 'job_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'study_id' in local_var_params:
            path_params['study_id'] = local_var_params['study_id']
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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/studies/{study_id}/jobs/{job_id}/extremum',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowExtremumInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_archive_configs(self, request):
        """获取跨域归档配置

        获取跨域归档配置
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListArchiveConfigs
        :type request: :class:`huaweicloudsdkeihealth.v1.ListArchiveConfigsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListArchiveConfigsResponse`
        """
        return self.list_archive_configs_with_http_info(request)

    def list_archive_configs_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/archive-configs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListArchiveConfigsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_env(self, request):
        """查询系统配置列表

        获取系统配置列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowEnv
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowEnvRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowEnvResponse`
        """
        return self.show_env_with_http_info(request)

    def show_env_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/configs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowEnvResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_vendor(self, request):
        """获取供应商配置

        获取供应商配置
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowVendor
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowVendorRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowVendorResponse`
        """
        return self.show_vendor_with_http_info(request)

    def show_vendor_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/vendor-config',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowVendorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_archive_config(self, request):
        """修改跨域归档设置

        修改跨域归档设置
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateArchiveConfig
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateArchiveConfigRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateArchiveConfigResponse`
        """
        return self.update_archive_config_with_http_info(request)

    def update_archive_config_with_http_info(self, request):
        all_params = ['region_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'region_id' in local_var_params:
            path_params['region_id'] = local_var_params['region_id']

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
            resource_path='/v1/{project_id}/system/archive-configs/{region_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateArchiveConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_vendor(self, request):
        """设置供应商配置

        设置供应商配置
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateVendor
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateVendorRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateVendorResponse`
        """
        return self.update_vendor_with_http_info(request)

    def update_vendor_with_http_info(self, request):
        all_params = ['file', 'name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']
        if 'name' in local_var_params:
            form_params['name'] = local_var_params['name']

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/system/vendor-config',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateVendorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_quota(self, request):
        """获取当前系统配额及资源使用情况

        获取当前系统配额及资源使用情况
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListQuota
        :type request: :class:`huaweicloudsdkeihealth.v1.ListQuotaRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListQuotaResponse`
        """
        return self.list_quota_with_http_info(request)

    def list_quota_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_template(self, request):
        """创建模板

        创建模板
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateTemplate
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateTemplateRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateTemplateResponse`
        """
        return self.create_template_with_http_info(request)

    def create_template_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/templates',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_template(self, request):
        """删除模板

        删除模板
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteTemplate
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteTemplateRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteTemplateResponse`
        """
        return self.delete_template_with_http_info(request)

    def delete_template_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'template_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/templates/{template_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def import_template(self, request):
        """从其他项目导入模板

        从其他项目导入模板
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ImportTemplate
        :type request: :class:`huaweicloudsdkeihealth.v1.ImportTemplateRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImportTemplateResponse`
        """
        return self.import_template_with_http_info(request)

    def import_template_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/templates/batch-import',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ImportTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_template(self, request):
        """查询模板列表

        查询模板列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListTemplate
        :type request: :class:`huaweicloudsdkeihealth.v1.ListTemplateRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListTemplateResponse`
        """
        return self.list_template_with_http_info(request)

    def list_template_with_http_info(self, request):
        all_params = ['eihealth_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/templates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_template(self, request):
        """查询模板详情

        查询模板详情
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowTemplate
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowTemplateRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowTemplateResponse`
        """
        return self.show_template_with_http_info(request)

    def show_template_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'template_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/templates/{template_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def upload_template(self, request):
        """上传模板

        上传模板
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UploadTemplate
        :type request: :class:`huaweicloudsdkeihealth.v1.UploadTemplateRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UploadTemplateResponse`
        """
        return self.upload_template_with_http_info(request)

    def upload_template_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'file']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []

        header_params = {}

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/templates/upload',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UploadTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_code(self, request):
        """发送验证码

        发送验证码
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateCode
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateCodeRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateCodeResponse`
        """
        return self.create_code_with_http_info(request)

    def create_code_with_http_info(self, request):
        all_params = ['user_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            resource_path='/v1/{project_id}/users/{user_id}/verification-code',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateCodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_user(self, request):
        """创建用户

        创建用户
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateUser
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateUserRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateUserResponse`
        """
        return self.create_user_with_http_info(request)

    def create_user_with_http_info(self, request):
        all_params = ['request']
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
            resource_path='/v1/{project_id}/users',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_user(self, request):
        """删除用户

        删除用户
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteUser
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteUserRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteUserResponse`
        """
        return self.delete_user_with_http_info(request)

    def delete_user_with_http_info(self, request):
        all_params = ['user_id', 'user_id_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []
        if 'user_id_type' in local_var_params:
            query_params.append(('user_id_type', local_var_params['user_id_type']))

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
            resource_path='/v1/{project_id}/users/{user_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_mfa(self, request):
        """获取可用的认证方法

        获取可用的认证方法
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListMfa
        :type request: :class:`huaweicloudsdkeihealth.v1.ListMfaRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListMfaResponse`
        """
        return self.list_mfa_with_http_info(request)

    def list_mfa_with_http_info(self, request):
        all_params = ['user_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            resource_path='/v1/{project_id}/users/{user_id}/mfa/methods',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListMfaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_user(self, request):
        """获取用户列表

        获取用户列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListUser
        :type request: :class:`huaweicloudsdkeihealth.v1.ListUserRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListUserResponse`
        """
        return self.list_user_with_http_info(request)

    def list_user_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/users',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_token_verification(self, request):
        """校验token

        校验token是否可访问当前环境
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowTokenVerification
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowTokenVerificationRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowTokenVerificationResponse`
        """
        return self.show_token_verification_with_http_info(request)

    def show_token_verification_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/users/token-verification',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTokenVerificationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_user(self, request):
        """获取指定用户详情

        获取指定用户详情
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowUser
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowUserRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowUserResponse`
        """
        return self.show_user_with_http_info(request)

    def show_user_with_http_info(self, request):
        all_params = ['user_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            resource_path='/v1/{project_id}/users/{user_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_user_setting(self, request):
        """查询用户设置

        查询用户设置
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowUserSetting
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowUserSettingRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowUserSettingResponse`
        """
        return self.show_user_setting_with_http_info(request)

    def show_user_setting_with_http_info(self, request):
        all_params = ['user_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            resource_path='/v1/{project_id}/users/{user_id}/settings',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowUserSettingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_init_password(self, request):
        """新用户重置密码

        新用户重置密码
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateInitPassword
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateInitPasswordRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateInitPasswordResponse`
        """
        return self.update_init_password_with_http_info(request)

    def update_init_password_with_http_info(self, request):
        all_params = ['user_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            resource_path='/v1/{project_id}/users/{user_id}/init-password',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateInitPasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_password(self, request):
        """修改密码

        修改密码
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdatePassword
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdatePasswordRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdatePasswordResponse`
        """
        return self.update_password_with_http_info(request)

    def update_password_with_http_info(self, request):
        all_params = ['user_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            resource_path='/v1/{project_id}/users/{user_id}/password',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_user(self, request):
        """修改用户基本信息

        修改用户基本信息（邮箱，手机）
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateUser
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateUserRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateUserResponse`
        """
        return self.update_user_with_http_info(request)

    def update_user_with_http_info(self, request):
        all_params = ['user_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            resource_path='/v1/{project_id}/users/{user_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_user_by_domain(self, request):
        """最终租户修改子用户

        最终租户修改子用户
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateUserByDomain
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateUserByDomainRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateUserByDomainResponse`
        """
        return self.update_user_by_domain_with_http_info(request)

    def update_user_by_domain_with_http_info(self, request):
        all_params = ['user_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            resource_path='/v1/{project_id}/users/{user_id}/domain-change-info',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateUserByDomainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_user_role(self, request):
        """更新用户角色

        更新用户角色
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateUserRole
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateUserRoleRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateUserRoleResponse`
        """
        return self.update_user_role_with_http_info(request)

    def update_user_role_with_http_info(self, request):
        all_params = ['user_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            resource_path='/v1/{project_id}/users/{user_id}/role',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateUserRoleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_user_setting(self, request):
        """更新用户设置

        更新用户设置
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateUserSetting
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateUserSettingRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateUserSettingResponse`
        """
        return self.update_user_setting_with_http_info(request)

    def update_user_setting_with_http_info(self, request):
        all_params = ['user_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            resource_path='/v1/{project_id}/users/{user_id}/settings',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateUserSettingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def validate_code(self, request):
        """预验证

        预验证
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ValidateCode
        :type request: :class:`huaweicloudsdkeihealth.v1.ValidateCodeRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ValidateCodeResponse`
        """
        return self.validate_code_with_http_info(request)

    def validate_code_with_http_info(self, request):
        all_params = ['user_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            resource_path='/v1/{project_id}/users/{user_id}/code-verify',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ValidateCodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_vendor(self, request):
        """获取供应商列表

        获取供应商列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListVendor
        :type request: :class:`huaweicloudsdkeihealth.v1.ListVendorRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListVendorResponse`
        """
        return self.list_vendor_with_http_info(request)

    def list_vendor_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/vendors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListVendorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_workflow(self, request):
        """创建流程

        创建流程
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateWorkflowResponse`
        """
        return self.create_workflow_with_http_info(request)

    def create_workflow_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'workflow_dto']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/workflows',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateWorkflowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_workflow(self, request):
        """删除流程

        删除流程
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteWorkflowResponse`
        """
        return self.delete_workflow_with_http_info(request)

    def delete_workflow_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'workflow_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/workflows/{workflow_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteWorkflowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def import_workflow(self, request):
        """导入流程

        导入流程
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ImportWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.ImportWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImportWorkflowResponse`
        """
        return self.import_workflow_with_http_info(request)

    def import_workflow_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'import_workflow_dto']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/workflows/import',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ImportWorkflowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_workflow(self, request):
        """获取流程列表

        获取流程列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.ListWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListWorkflowResponse`
        """
        return self.list_workflow_with_http_info(request)

    def list_workflow_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'name', 'version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/workflows',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListWorkflowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_workflow(self, request):
        """获取流程详情

        获取流程详情
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowWorkflowResponse`
        """
        return self.show_workflow_with_http_info(request)

    def show_workflow_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'workflow_id', 'show_param_detail']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

        query_params = []

        header_params = {}
        if 'show_param_detail' in local_var_params:
            header_params['Show-Param-Detail'] = local_var_params['show_param_detail']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/workflows/{workflow_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowWorkflowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def subscribe_workflow(self, request):
        """订阅流程

        订阅流程
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SubscribeWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.SubscribeWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.SubscribeWorkflowResponse`
        """
        return self.subscribe_workflow_with_http_info(request)

    def subscribe_workflow_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'subscribe_workflow_dto']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/workflows/subscribe',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SubscribeWorkflowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_workflow(self, request):
        """更新流程

        更新流程
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateWorkflowResponse`
        """
        return self.update_workflow_with_http_info(request)

    def update_workflow_with_http_info(self, request):
        all_params = ['eihealth_project_id', 'workflow_id', 'workflow_dto']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/workflows/{workflow_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateWorkflowResponse',
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
        :param header_params: Header parameters to be placed in the request header.
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
            request_type=request_type)
