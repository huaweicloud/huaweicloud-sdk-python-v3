# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class LiveClient(Client):
    def __init__(self):
        super(LiveClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdklive.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "LiveClient":
            raise TypeError("client type error, support client type is LiveClient")

        return ClientBuilder(clazz)

    def batch_show_ip_belongs(self, request):
        """查询IP归属信息

        查询IP归属信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchShowIpBelongs
        :type request: :class:`huaweicloudsdklive.v1.BatchShowIpBelongsRequest`
        :rtype: :class:`huaweicloudsdklive.v1.BatchShowIpBelongsResponse`
        """
        return self._batch_show_ip_belongs_with_http_info(request)

    def _batch_show_ip_belongs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))
            collection_formats['ip'] = 'multi'

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
            resource_path='/v1/{project_id}/cdn/ip-info',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchShowIpBelongsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_domain(self, request):
        """创建直播域名

        可单独创建直播播放域名或推流域名，每个租户最多可配置64条域名记录。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDomain
        :type request: :class:`huaweicloudsdklive.v1.CreateDomainRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateDomainResponse`
        """
        return self._create_domain_with_http_info(request)

    def _create_domain_with_http_info(self, request):
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
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/domain',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDomainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_domain_mapping(self, request):
        """域名映射

        将用户已创建的播放域名和推流域名建立域名映射关系
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDomainMapping
        :type request: :class:`huaweicloudsdklive.v1.CreateDomainMappingRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateDomainMappingResponse`
        """
        return self._create_domain_mapping_with_http_info(request)

    def _create_domain_mapping_with_http_info(self, request):
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
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/domains_mapping',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDomainMappingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_record_callback_config(self, request):
        """创建录制回调配置

        创建录制回调配置接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRecordCallbackConfig
        :type request: :class:`huaweicloudsdklive.v1.CreateRecordCallbackConfigRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateRecordCallbackConfigResponse`
        """
        return self._create_record_callback_config_with_http_info(request)

    def _create_record_callback_config_with_http_info(self, request):
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
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/record/callbacks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateRecordCallbackConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_record_index(self, request):
        """创建录制视频索引文件

        Create Record Index
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRecordIndex
        :type request: :class:`huaweicloudsdklive.v1.CreateRecordIndexRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateRecordIndexResponse`
        """
        return self._create_record_index_with_http_info(request)

    def _create_record_index_with_http_info(self, request):
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

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/record/indexes',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateRecordIndexResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_record_rule(self, request):
        """创建录制规则

        创建录制规则接口，录制规则对新推送的流生效，对已经推送中的流不生效
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRecordRule
        :type request: :class:`huaweicloudsdklive.v1.CreateRecordRuleRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateRecordRuleResponse`
        """
        return self._create_record_rule_with_http_info(request)

    def _create_record_rule_with_http_info(self, request):
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
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/record/rules',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateRecordRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_snapshot_config(self, request):
        """创建直播截图配置

        创建直播截图配置接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSnapshotConfig
        :type request: :class:`huaweicloudsdklive.v1.CreateSnapshotConfigRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateSnapshotConfigResponse`
        """
        return self._create_snapshot_config_with_http_info(request)

    def _create_snapshot_config_with_http_info(self, request):
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
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/stream/snapshot',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSnapshotConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_stream_forbidden(self, request):
        """禁止直播推流

        禁止直播推流
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateStreamForbidden
        :type request: :class:`huaweicloudsdklive.v1.CreateStreamForbiddenRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateStreamForbiddenResponse`
        """
        return self._create_stream_forbidden_with_http_info(request)

    def _create_stream_forbidden_with_http_info(self, request):
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
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/stream/blocks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateStreamForbiddenResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_transcodings_template(self, request):
        """创建直播转码模板

        创建直播转码模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTranscodingsTemplate
        :type request: :class:`huaweicloudsdklive.v1.CreateTranscodingsTemplateRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateTranscodingsTemplateResponse`
        """
        return self._create_transcodings_template_with_http_info(request)

    def _create_transcodings_template_with_http_info(self, request):
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
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/transcodings',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTranscodingsTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_domain(self, request):
        """删除直播域名

        删除域名。只有在域名停用（off）状态时才能删除。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDomain
        :type request: :class:`huaweicloudsdklive.v1.DeleteDomainRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteDomainResponse`
        """
        return self._delete_domain_with_http_info(request)

    def _delete_domain_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

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
            resource_path='/v1/{project_id}/domain',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDomainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_domain_key_chain(self, request):
        """删除指定域名的Key防盗链配置

        删除指定域名的Key防盗链配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDomainKeyChain
        :type request: :class:`huaweicloudsdklive.v1.DeleteDomainKeyChainRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteDomainKeyChainResponse`
        """
        return self._delete_domain_key_chain_with_http_info(request)

    def _delete_domain_key_chain_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

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
            resource_path='/v1/{project_id}/guard/key-chain',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDomainKeyChainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_domain_mapping(self, request):
        """删除直播域名映射关系

        将播放域名和推流域名的域名映射关系删除
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDomainMapping
        :type request: :class:`huaweicloudsdklive.v1.DeleteDomainMappingRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteDomainMappingResponse`
        """
        return self._delete_domain_mapping_with_http_info(request)

    def _delete_domain_mapping_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'pull_domain' in local_var_params:
            query_params.append(('pull_domain', local_var_params['pull_domain']))
        if 'push_domain' in local_var_params:
            query_params.append(('push_domain', local_var_params['push_domain']))

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
            resource_path='/v1/{project_id}/domains_mapping',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDomainMappingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_record_callback_config(self, request):
        """删除录制回调配置

        删除录制回调配置接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRecordCallbackConfig
        :type request: :class:`huaweicloudsdklive.v1.DeleteRecordCallbackConfigRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteRecordCallbackConfigResponse`
        """
        return self._delete_record_callback_config_with_http_info(request)

    def _delete_record_callback_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v1/{project_id}/record/callbacks/{id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteRecordCallbackConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_record_rule(self, request):
        """删除录制规则

        删除录制规则接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRecordRule
        :type request: :class:`huaweicloudsdklive.v1.DeleteRecordRuleRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteRecordRuleResponse`
        """
        return self._delete_record_rule_with_http_info(request)

    def _delete_record_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v1/{project_id}/record/rules/{id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteRecordRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_snapshot_config(self, request):
        """删除直播截图配置

        删除直播截图配置接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSnapshotConfig
        :type request: :class:`huaweicloudsdklive.v1.DeleteSnapshotConfigRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteSnapshotConfigResponse`
        """
        return self._delete_snapshot_config_with_http_info(request)

    def _delete_snapshot_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))

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
            resource_path='/v1/{project_id}/stream/snapshot',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSnapshotConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_stream_forbidden(self, request):
        """禁推恢复

        恢复直播推流接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteStreamForbidden
        :type request: :class:`huaweicloudsdklive.v1.DeleteStreamForbiddenRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteStreamForbiddenResponse`
        """
        return self._delete_stream_forbidden_with_http_info(request)

    def _delete_stream_forbidden_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'stream_name' in local_var_params:
            query_params.append(('stream_name', local_var_params['stream_name']))

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
            resource_path='/v1/{project_id}/stream/blocks',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteStreamForbiddenResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_transcodings_template(self, request):
        """删除直播转码模板

        删除直播转码模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTranscodingsTemplate
        :type request: :class:`huaweicloudsdklive.v1.DeleteTranscodingsTemplateRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteTranscodingsTemplateResponse`
        """
        return self._delete_transcodings_template_with_http_info(request)

    def _delete_transcodings_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))

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
            resource_path='/v1/{project_id}/template/transcodings',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTranscodingsTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_live_sample_logs(self, request):
        """获取直播播放日志

        获取直播播放日志，基于域名以5分钟粒度进行打包，日志内容以 \&quot;|\&quot; 进行分隔。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLiveSampleLogs
        :type request: :class:`huaweicloudsdklive.v1.ListLiveSampleLogsRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListLiveSampleLogsResponse`
        """
        return self._list_live_sample_logs_with_http_info(request)

    def _list_live_sample_logs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'play_domain' in local_var_params:
            query_params.append(('play_domain', local_var_params['play_domain']))
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
            resource_path='/v1/{project_id}/logs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListLiveSampleLogsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_live_streams_online(self, request):
        """查询直播中的流信息

        查询直播中的流信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLiveStreamsOnline
        :type request: :class:`huaweicloudsdklive.v1.ListLiveStreamsOnlineRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListLiveStreamsOnlineResponse`
        """
        return self._list_live_streams_online_with_http_info(request)

    def _list_live_streams_online_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'publish_domain' in local_var_params:
            query_params.append(('publish_domain', local_var_params['publish_domain']))
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'stream' in local_var_params:
            query_params.append(('stream', local_var_params['stream']))

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
            resource_path='/v1/{project_id}/realtime/streams',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListLiveStreamsOnlineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_record_callback_configs(self, request):
        """查询录制回调配置列表

        查询录制回调配置列表接口。通过指定条件，查询满足条件的配置列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRecordCallbackConfigs
        :type request: :class:`huaweicloudsdklive.v1.ListRecordCallbackConfigsRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListRecordCallbackConfigsResponse`
        """
        return self._list_record_callback_configs_with_http_info(request)

    def _list_record_callback_configs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'publish_domain' in local_var_params:
            query_params.append(('publish_domain', local_var_params['publish_domain']))
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
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
            resource_path='/v1/{project_id}/record/callbacks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRecordCallbackConfigsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_record_contents(self, request):
        """录制完成内容的查询

        录制完成的内容查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRecordContents
        :type request: :class:`huaweicloudsdklive.v1.ListRecordContentsRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListRecordContentsResponse`
        """
        return self._list_record_contents_with_http_info(request)

    def _list_record_contents_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'publish_domain' in local_var_params:
            query_params.append(('publish_domain', local_var_params['publish_domain']))
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'stream' in local_var_params:
            query_params.append(('stream', local_var_params['stream']))
        if 'record_type' in local_var_params:
            query_params.append(('record_type', local_var_params['record_type']))
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/record/contents',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRecordContentsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_record_rules(self, request):
        """查询录制规则列表

        查询录制规则列表接口，通过指定条件，查询满足条件的录制规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRecordRules
        :type request: :class:`huaweicloudsdklive.v1.ListRecordRulesRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListRecordRulesResponse`
        """
        return self._list_record_rules_with_http_info(request)

    def _list_record_rules_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'publish_domain' in local_var_params:
            query_params.append(('publish_domain', local_var_params['publish_domain']))
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'stream' in local_var_params:
            query_params.append(('stream', local_var_params['stream']))
        if 'record_type' in local_var_params:
            query_params.append(('record_type', local_var_params['record_type']))
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
            resource_path='/v1/{project_id}/record/rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRecordRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_snapshot_configs(self, request):
        """查询直播截图配置

        查询直播截图配置接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSnapshotConfigs
        :type request: :class:`huaweicloudsdklive.v1.ListSnapshotConfigsRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListSnapshotConfigsResponse`
        """
        return self._list_snapshot_configs_with_http_info(request)

    def _list_snapshot_configs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
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
            resource_path='/v1/{project_id}/stream/snapshot',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSnapshotConfigsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_stream_forbidden(self, request):
        """查询禁止直播推流列表

        查询禁播黑名单列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStreamForbidden
        :type request: :class:`huaweicloudsdklive.v1.ListStreamForbiddenRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListStreamForbiddenResponse`
        """
        return self._list_stream_forbidden_with_http_info(request)

    def _list_stream_forbidden_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'stream_name' in local_var_params:
            query_params.append(('stream_name', local_var_params['stream_name']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

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
            resource_path='/v1/{project_id}/stream/blocks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListStreamForbiddenResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_record(self, request):
        """提交录制控制命令

        对单条流的实时录制控制接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunRecord
        :type request: :class:`huaweicloudsdklive.v1.RunRecordRequest`
        :rtype: :class:`huaweicloudsdklive.v1.RunRecordResponse`
        """
        return self._run_record_with_http_info(request)

    def _run_record_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/record/control',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunRecordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_domain(self, request):
        """查询直播域名

        查询直播域名
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomain
        :type request: :class:`huaweicloudsdklive.v1.ShowDomainRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ShowDomainResponse`
        """
        return self._show_domain_with_http_info(request)

    def _show_domain_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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
            resource_path='/v1/{project_id}/domain',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDomainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_domain_key_chain(self, request):
        """查询指定域名的Key防盗链配置

        查询指定域名的Key防盗链配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainKeyChain
        :type request: :class:`huaweicloudsdklive.v1.ShowDomainKeyChainRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ShowDomainKeyChainResponse`
        """
        return self._show_domain_key_chain_with_http_info(request)

    def _show_domain_key_chain_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

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
            resource_path='/v1/{project_id}/guard/key-chain',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDomainKeyChainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_record_callback_config(self, request):
        """查询录制回调配置

        查询录制回调配置接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRecordCallbackConfig
        :type request: :class:`huaweicloudsdklive.v1.ShowRecordCallbackConfigRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ShowRecordCallbackConfigResponse`
        """
        return self._show_record_callback_config_with_http_info(request)

    def _show_record_callback_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v1/{project_id}/record/callbacks/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowRecordCallbackConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_record_rule(self, request):
        """查询录制规则配置

        查询录制规则接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRecordRule
        :type request: :class:`huaweicloudsdklive.v1.ShowRecordRuleRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ShowRecordRuleResponse`
        """
        return self._show_record_rule_with_http_info(request)

    def _show_record_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v1/{project_id}/record/rules/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowRecordRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_transcodings_template(self, request):
        """查询直播转码模板

        查询直播转码模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTranscodingsTemplate
        :type request: :class:`huaweicloudsdklive.v1.ShowTranscodingsTemplateRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ShowTranscodingsTemplateResponse`
        """
        return self._show_transcodings_template_with_http_info(request)

    def _show_transcodings_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

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
            resource_path='/v1/{project_id}/template/transcodings',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTranscodingsTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_domain(self, request):
        """修改直播域名

        修改直播播放、RTMP推流加速域名相关信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDomain
        :type request: :class:`huaweicloudsdklive.v1.UpdateDomainRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateDomainResponse`
        """
        return self._update_domain_with_http_info(request)

    def _update_domain_with_http_info(self, request):
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
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/domain',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDomainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_domain_ip6_switch(self, request):
        """配置域名IPV6开关

        配置IPV6开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDomainIp6Switch
        :type request: :class:`huaweicloudsdklive.v1.UpdateDomainIp6SwitchRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateDomainIp6SwitchResponse`
        """
        return self._update_domain_ip6_switch_with_http_info(request)

    def _update_domain_ip6_switch_with_http_info(self, request):
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
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/domain/ipv6-switch',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDomainIp6SwitchResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_domain_key_chain(self, request):
        """更新指定域名的Key防盗链配置

        更新指定域名的Key防盗链配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDomainKeyChain
        :type request: :class:`huaweicloudsdklive.v1.UpdateDomainKeyChainRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateDomainKeyChainResponse`
        """
        return self._update_domain_key_chain_with_http_info(request)

    def _update_domain_key_chain_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/guard/key-chain',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDomainKeyChainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_record_callback_config(self, request):
        """修改录制回调配置

        修改录制回调配置接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRecordCallbackConfig
        :type request: :class:`huaweicloudsdklive.v1.UpdateRecordCallbackConfigRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateRecordCallbackConfigResponse`
        """
        return self._update_record_callback_config_with_http_info(request)

    def _update_record_callback_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/record/callbacks/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateRecordCallbackConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_record_rule(self, request):
        """修改录制规则

        修改录制规则接口，如果规则修改后，修改后的规则对正在录制的流无效，对新的流有效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRecordRule
        :type request: :class:`huaweicloudsdklive.v1.UpdateRecordRuleRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateRecordRuleResponse`
        """
        return self._update_record_rule_with_http_info(request)

    def _update_record_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/record/rules/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateRecordRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_snapshot_config(self, request):
        """修改直播截图配置

        修改直播截图配置接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSnapshotConfig
        :type request: :class:`huaweicloudsdklive.v1.UpdateSnapshotConfigRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateSnapshotConfigResponse`
        """
        return self._update_snapshot_config_with_http_info(request)

    def _update_snapshot_config_with_http_info(self, request):
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
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/stream/snapshot',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateSnapshotConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_stream_forbidden(self, request):
        """修改禁推属性

        修改禁推属性
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateStreamForbidden
        :type request: :class:`huaweicloudsdklive.v1.UpdateStreamForbiddenRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateStreamForbiddenResponse`
        """
        return self._update_stream_forbidden_with_http_info(request)

    def _update_stream_forbidden_with_http_info(self, request):
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
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/stream/blocks',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateStreamForbiddenResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_transcodings_template(self, request):
        """配置直播转码模板

        修改直播转码模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTranscodingsTemplate
        :type request: :class:`huaweicloudsdklive.v1.UpdateTranscodingsTemplateRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateTranscodingsTemplateResponse`
        """
        return self._update_transcodings_template_with_http_info(request)

    def _update_transcodings_template_with_http_info(self, request):
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
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/transcodings',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateTranscodingsTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_domain_https_cert(self, request):
        """删除指定域名的https证书配置

        删除指定域名的https证书配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDomainHttpsCert
        :type request: :class:`huaweicloudsdklive.v1.DeleteDomainHttpsCertRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteDomainHttpsCertResponse`
        """
        return self._delete_domain_https_cert_with_http_info(request)

    def _delete_domain_https_cert_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

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
            resource_path='/v1/{project_id}/guard/https-cert',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDomainHttpsCertResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_domain_https_cert(self, request):
        """查询指定域名的https证书配置

        查询指定域名的https证书配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainHttpsCert
        :type request: :class:`huaweicloudsdklive.v1.ShowDomainHttpsCertRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ShowDomainHttpsCertResponse`
        """
        return self._show_domain_https_cert_with_http_info(request)

    def _show_domain_https_cert_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

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
            resource_path='/v1/{project_id}/guard/https-cert',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDomainHttpsCertResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_domain_https_cert(self, request):
        """修改指定域名的https证书配置

        修改指定域名的https证书配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDomainHttpsCert
        :type request: :class:`huaweicloudsdklive.v1.UpdateDomainHttpsCertRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateDomainHttpsCertResponse`
        """
        return self._update_domain_https_cert_with_http_info(request)

    def _update_domain_https_cert_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/guard/https-cert',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDomainHttpsCertResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_obs_bucket_authority_public(self, request):
        """OBS桶授权及取消授权

        OBS桶授权及取消授权
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateObsBucketAuthorityPublic
        :type request: :class:`huaweicloudsdklive.v1.UpdateObsBucketAuthorityPublicRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateObsBucketAuthorityPublicResponse`
        """
        return self._update_obs_bucket_authority_public_with_http_info(request)

    def _update_obs_bucket_authority_public_with_http_info(self, request):
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
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/obs/authority',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateObsBucketAuthorityPublicResponse',
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
