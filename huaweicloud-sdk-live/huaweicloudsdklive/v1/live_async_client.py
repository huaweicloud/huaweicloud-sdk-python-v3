# coding: utf-8

from __future__ import absolute_import

import importlib
import warnings

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest
try:
    from huaweicloudsdkcore.invoker.invoker import AsyncInvoker
except ImportError as e:
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdklive'")


class LiveAsyncClient(Client):
    def __init__(self):
        super(LiveAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdklive.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "LiveAsyncClient":
                raise TypeError("client type error, support client type is LiveAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_show_ip_belongs_async(self, request):
        """查询IP归属信息

        查询IP归属信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchShowIpBelongs
        :type request: :class:`huaweicloudsdklive.v1.BatchShowIpBelongsRequest`
        :rtype: :class:`huaweicloudsdklive.v1.BatchShowIpBelongsResponse`
        """
        http_info = self._batch_show_ip_belongs_http_info(request)
        return self._call_api(**http_info)

    def batch_show_ip_belongs_async_invoker(self, request):
        http_info = self._batch_show_ip_belongs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_show_ip_belongs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cdn/ip-info",
            "request_type": request.__class__.__name__,
            "response_type": "BatchShowIpBelongsResponse"
            }

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

    def create_domain_async(self, request):
        """创建直播域名

        可单独创建直播播放域名或推流域名，每个租户最多可配置64条域名记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDomain
        :type request: :class:`huaweicloudsdklive.v1.CreateDomainRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateDomainResponse`
        """
        http_info = self._create_domain_http_info(request)
        return self._call_api(**http_info)

    def create_domain_async_invoker(self, request):
        http_info = self._create_domain_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_domain_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/domain",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDomainResponse"
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
            ['application/json; charset=UTF-8'])

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

    def create_domain_mapping_async(self, request):
        """域名映射

        将用户已创建的播放域名和推流域名建立域名映射关系
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDomainMapping
        :type request: :class:`huaweicloudsdklive.v1.CreateDomainMappingRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateDomainMappingResponse`
        """
        http_info = self._create_domain_mapping_http_info(request)
        return self._call_api(**http_info)

    def create_domain_mapping_async_invoker(self, request):
        http_info = self._create_domain_mapping_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_domain_mapping_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/domains_mapping",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDomainMappingResponse"
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
            ['application/json; charset=UTF-8'])

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

    def create_record_callback_config_async(self, request):
        """创建录制回调配置

        创建录制回调配置接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRecordCallbackConfig
        :type request: :class:`huaweicloudsdklive.v1.CreateRecordCallbackConfigRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateRecordCallbackConfigResponse`
        """
        http_info = self._create_record_callback_config_http_info(request)
        return self._call_api(**http_info)

    def create_record_callback_config_async_invoker(self, request):
        http_info = self._create_record_callback_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_record_callback_config_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/record/callbacks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRecordCallbackConfigResponse"
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
            ['application/json; charset=UTF-8'])

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

    def create_record_index_async(self, request):
        """创建录制视频索引文件

        Create Record Index
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRecordIndex
        :type request: :class:`huaweicloudsdklive.v1.CreateRecordIndexRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateRecordIndexResponse`
        """
        http_info = self._create_record_index_http_info(request)
        return self._call_api(**http_info)

    def create_record_index_async_invoker(self, request):
        http_info = self._create_record_index_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_record_index_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/record/indexes",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRecordIndexResponse"
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

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

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

    def create_record_rule_async(self, request):
        """创建录制规则

        创建录制规则接口，录制规则对新推送的流生效，对已经推送中的流不生效
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRecordRule
        :type request: :class:`huaweicloudsdklive.v1.CreateRecordRuleRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateRecordRuleResponse`
        """
        http_info = self._create_record_rule_http_info(request)
        return self._call_api(**http_info)

    def create_record_rule_async_invoker(self, request):
        http_info = self._create_record_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_record_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/record/rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRecordRuleResponse"
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
            ['application/json; charset=UTF-8'])

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

    def create_snapshot_config_async(self, request):
        """创建直播截图配置

        创建直播截图配置接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSnapshotConfig
        :type request: :class:`huaweicloudsdklive.v1.CreateSnapshotConfigRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateSnapshotConfigResponse`
        """
        http_info = self._create_snapshot_config_http_info(request)
        return self._call_api(**http_info)

    def create_snapshot_config_async_invoker(self, request):
        http_info = self._create_snapshot_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_snapshot_config_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/stream/snapshot",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSnapshotConfigResponse"
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
            ['application/json; charset=UTF-8'])

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

    def create_stream_forbidden_async(self, request):
        """禁止直播推流

        禁止直播推流
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateStreamForbidden
        :type request: :class:`huaweicloudsdklive.v1.CreateStreamForbiddenRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateStreamForbiddenResponse`
        """
        http_info = self._create_stream_forbidden_http_info(request)
        return self._call_api(**http_info)

    def create_stream_forbidden_async_invoker(self, request):
        http_info = self._create_stream_forbidden_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_stream_forbidden_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/stream/blocks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateStreamForbiddenResponse"
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
            ['application/json; charset=UTF-8'])

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

    def create_transcodings_template_async(self, request):
        """创建直播转码模板

        创建直播转码模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTranscodingsTemplate
        :type request: :class:`huaweicloudsdklive.v1.CreateTranscodingsTemplateRequest`
        :rtype: :class:`huaweicloudsdklive.v1.CreateTranscodingsTemplateResponse`
        """
        http_info = self._create_transcodings_template_http_info(request)
        return self._call_api(**http_info)

    def create_transcodings_template_async_invoker(self, request):
        http_info = self._create_transcodings_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_transcodings_template_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/template/transcodings",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTranscodingsTemplateResponse"
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
            ['application/json; charset=UTF-8'])

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

    def delete_domain_async(self, request):
        """删除直播域名

        删除域名。只有在域名停用（off）状态时才能删除。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDomain
        :type request: :class:`huaweicloudsdklive.v1.DeleteDomainRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteDomainResponse`
        """
        http_info = self._delete_domain_http_info(request)
        return self._call_api(**http_info)

    def delete_domain_async_invoker(self, request):
        http_info = self._delete_domain_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_domain_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/domain",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDomainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

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

    def delete_domain_key_chain_async(self, request):
        """删除指定域名的Key防盗链配置

        删除指定域名的Key防盗链配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDomainKeyChain
        :type request: :class:`huaweicloudsdklive.v1.DeleteDomainKeyChainRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteDomainKeyChainResponse`
        """
        http_info = self._delete_domain_key_chain_http_info(request)
        return self._call_api(**http_info)

    def delete_domain_key_chain_async_invoker(self, request):
        http_info = self._delete_domain_key_chain_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_domain_key_chain_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/guard/key-chain",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDomainKeyChainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

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

    def delete_domain_mapping_async(self, request):
        """删除直播域名映射关系

        将播放域名和推流域名的域名映射关系删除
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDomainMapping
        :type request: :class:`huaweicloudsdklive.v1.DeleteDomainMappingRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteDomainMappingResponse`
        """
        http_info = self._delete_domain_mapping_http_info(request)
        return self._call_api(**http_info)

    def delete_domain_mapping_async_invoker(self, request):
        http_info = self._delete_domain_mapping_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_domain_mapping_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/domains_mapping",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDomainMappingResponse"
            }

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

    def delete_record_callback_config_async(self, request):
        """删除录制回调配置

        删除录制回调配置接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRecordCallbackConfig
        :type request: :class:`huaweicloudsdklive.v1.DeleteRecordCallbackConfigRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteRecordCallbackConfigResponse`
        """
        http_info = self._delete_record_callback_config_http_info(request)
        return self._call_api(**http_info)

    def delete_record_callback_config_async_invoker(self, request):
        http_info = self._delete_record_callback_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_record_callback_config_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/record/callbacks/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRecordCallbackConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def delete_record_rule_async(self, request):
        """删除录制规则

        删除录制规则接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRecordRule
        :type request: :class:`huaweicloudsdklive.v1.DeleteRecordRuleRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteRecordRuleResponse`
        """
        http_info = self._delete_record_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_record_rule_async_invoker(self, request):
        http_info = self._delete_record_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_record_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/record/rules/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRecordRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def delete_snapshot_config_async(self, request):
        """删除直播截图配置

        删除直播截图配置接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSnapshotConfig
        :type request: :class:`huaweicloudsdklive.v1.DeleteSnapshotConfigRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteSnapshotConfigResponse`
        """
        http_info = self._delete_snapshot_config_http_info(request)
        return self._call_api(**http_info)

    def delete_snapshot_config_async_invoker(self, request):
        http_info = self._delete_snapshot_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_snapshot_config_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/stream/snapshot",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSnapshotConfigResponse"
            }

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

    def delete_stream_forbidden_async(self, request):
        """禁推恢复

        恢复直播推流接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteStreamForbidden
        :type request: :class:`huaweicloudsdklive.v1.DeleteStreamForbiddenRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteStreamForbiddenResponse`
        """
        http_info = self._delete_stream_forbidden_http_info(request)
        return self._call_api(**http_info)

    def delete_stream_forbidden_async_invoker(self, request):
        http_info = self._delete_stream_forbidden_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_stream_forbidden_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/stream/blocks",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteStreamForbiddenResponse"
            }

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

    def delete_transcodings_template_async(self, request):
        """删除直播转码模板

        删除直播转码模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTranscodingsTemplate
        :type request: :class:`huaweicloudsdklive.v1.DeleteTranscodingsTemplateRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteTranscodingsTemplateResponse`
        """
        http_info = self._delete_transcodings_template_http_info(request)
        return self._call_api(**http_info)

    def delete_transcodings_template_async_invoker(self, request):
        http_info = self._delete_transcodings_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_transcodings_template_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/template/transcodings",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTranscodingsTemplateResponse"
            }

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

    def list_live_sample_logs_async(self, request):
        """获取直播播放日志

        获取直播播放日志，基于域名以5分钟粒度进行打包，日志内容以 \&quot;|\&quot; 进行分隔。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLiveSampleLogs
        :type request: :class:`huaweicloudsdklive.v1.ListLiveSampleLogsRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListLiveSampleLogsResponse`
        """
        http_info = self._list_live_sample_logs_http_info(request)
        return self._call_api(**http_info)

    def list_live_sample_logs_async_invoker(self, request):
        http_info = self._list_live_sample_logs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_live_sample_logs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListLiveSampleLogsResponse"
            }

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

    def list_live_streams_online_async(self, request):
        """查询直播中的流信息

        查询直播中的流信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLiveStreamsOnline
        :type request: :class:`huaweicloudsdklive.v1.ListLiveStreamsOnlineRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListLiveStreamsOnlineResponse`
        """
        http_info = self._list_live_streams_online_http_info(request)
        return self._call_api(**http_info)

    def list_live_streams_online_async_invoker(self, request):
        http_info = self._list_live_streams_online_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_live_streams_online_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/realtime/streams",
            "request_type": request.__class__.__name__,
            "response_type": "ListLiveStreamsOnlineResponse"
            }

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

    def list_record_callback_configs_async(self, request):
        """查询录制回调配置列表

        查询录制回调配置列表接口。通过指定条件，查询满足条件的配置列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRecordCallbackConfigs
        :type request: :class:`huaweicloudsdklive.v1.ListRecordCallbackConfigsRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListRecordCallbackConfigsResponse`
        """
        http_info = self._list_record_callback_configs_http_info(request)
        return self._call_api(**http_info)

    def list_record_callback_configs_async_invoker(self, request):
        http_info = self._list_record_callback_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_record_callback_configs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/record/callbacks",
            "request_type": request.__class__.__name__,
            "response_type": "ListRecordCallbackConfigsResponse"
            }

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

    def list_record_contents_async(self, request):
        """录制完成内容的查询

        录制完成的内容查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRecordContents
        :type request: :class:`huaweicloudsdklive.v1.ListRecordContentsRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListRecordContentsResponse`
        """
        http_info = self._list_record_contents_http_info(request)
        return self._call_api(**http_info)

    def list_record_contents_async_invoker(self, request):
        http_info = self._list_record_contents_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_record_contents_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/record/contents",
            "request_type": request.__class__.__name__,
            "response_type": "ListRecordContentsResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def list_record_rules_async(self, request):
        """查询录制规则列表

        查询录制规则列表接口，通过指定条件，查询满足条件的录制规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRecordRules
        :type request: :class:`huaweicloudsdklive.v1.ListRecordRulesRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListRecordRulesResponse`
        """
        http_info = self._list_record_rules_http_info(request)
        return self._call_api(**http_info)

    def list_record_rules_async_invoker(self, request):
        http_info = self._list_record_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_record_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/record/rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListRecordRulesResponse"
            }

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

    def list_snapshot_configs_async(self, request):
        """查询直播截图配置

        查询直播截图配置接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSnapshotConfigs
        :type request: :class:`huaweicloudsdklive.v1.ListSnapshotConfigsRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListSnapshotConfigsResponse`
        """
        http_info = self._list_snapshot_configs_http_info(request)
        return self._call_api(**http_info)

    def list_snapshot_configs_async_invoker(self, request):
        http_info = self._list_snapshot_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_snapshot_configs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/stream/snapshot",
            "request_type": request.__class__.__name__,
            "response_type": "ListSnapshotConfigsResponse"
            }

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

    def list_stream_forbidden_async(self, request):
        """查询禁止直播推流列表

        查询禁播黑名单列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListStreamForbidden
        :type request: :class:`huaweicloudsdklive.v1.ListStreamForbiddenRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ListStreamForbiddenResponse`
        """
        http_info = self._list_stream_forbidden_http_info(request)
        return self._call_api(**http_info)

    def list_stream_forbidden_async_invoker(self, request):
        http_info = self._list_stream_forbidden_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_stream_forbidden_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/stream/blocks",
            "request_type": request.__class__.__name__,
            "response_type": "ListStreamForbiddenResponse"
            }

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

    def run_record_async(self, request):
        """提交录制控制命令

        对单条流的实时录制控制接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunRecord
        :type request: :class:`huaweicloudsdklive.v1.RunRecordRequest`
        :rtype: :class:`huaweicloudsdklive.v1.RunRecordResponse`
        """
        http_info = self._run_record_http_info(request)
        return self._call_api(**http_info)

    def run_record_async_invoker(self, request):
        http_info = self._run_record_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_record_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/record/control",
            "request_type": request.__class__.__name__,
            "response_type": "RunRecordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

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

    def show_domain_async(self, request):
        """查询直播域名

        查询直播域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDomain
        :type request: :class:`huaweicloudsdklive.v1.ShowDomainRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ShowDomainResponse`
        """
        http_info = self._show_domain_http_info(request)
        return self._call_api(**http_info)

    def show_domain_async_invoker(self, request):
        http_info = self._show_domain_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_domain_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/domain",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainResponse"
            }

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

    def show_domain_key_chain_async(self, request):
        """查询指定域名的Key防盗链配置

        查询指定域名的Key防盗链配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDomainKeyChain
        :type request: :class:`huaweicloudsdklive.v1.ShowDomainKeyChainRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ShowDomainKeyChainResponse`
        """
        http_info = self._show_domain_key_chain_http_info(request)
        return self._call_api(**http_info)

    def show_domain_key_chain_async_invoker(self, request):
        http_info = self._show_domain_key_chain_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_domain_key_chain_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/guard/key-chain",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainKeyChainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

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

    def show_record_callback_config_async(self, request):
        """查询录制回调配置

        查询录制回调配置接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRecordCallbackConfig
        :type request: :class:`huaweicloudsdklive.v1.ShowRecordCallbackConfigRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ShowRecordCallbackConfigResponse`
        """
        http_info = self._show_record_callback_config_http_info(request)
        return self._call_api(**http_info)

    def show_record_callback_config_async_invoker(self, request):
        http_info = self._show_record_callback_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_record_callback_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/record/callbacks/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRecordCallbackConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def show_record_rule_async(self, request):
        """查询录制规则配置

        查询录制规则接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRecordRule
        :type request: :class:`huaweicloudsdklive.v1.ShowRecordRuleRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ShowRecordRuleResponse`
        """
        http_info = self._show_record_rule_http_info(request)
        return self._call_api(**http_info)

    def show_record_rule_async_invoker(self, request):
        http_info = self._show_record_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_record_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/record/rules/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRecordRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def show_transcodings_template_async(self, request):
        """查询直播转码模板

        查询直播转码模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTranscodingsTemplate
        :type request: :class:`huaweicloudsdklive.v1.ShowTranscodingsTemplateRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ShowTranscodingsTemplateResponse`
        """
        http_info = self._show_transcodings_template_http_info(request)
        return self._call_api(**http_info)

    def show_transcodings_template_async_invoker(self, request):
        http_info = self._show_transcodings_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_transcodings_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/template/transcodings",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTranscodingsTemplateResponse"
            }

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

    def update_domain_async(self, request):
        """修改直播域名

        修改直播播放、RTMP推流加速域名相关信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDomain
        :type request: :class:`huaweicloudsdklive.v1.UpdateDomainRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateDomainResponse`
        """
        http_info = self._update_domain_http_info(request)
        return self._call_api(**http_info)

    def update_domain_async_invoker(self, request):
        http_info = self._update_domain_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_domain_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/domain",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDomainResponse"
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
            ['application/json; charset=UTF-8'])

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

    def update_domain_ip6_switch_async(self, request):
        """配置域名IPV6开关

        配置IPV6开关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDomainIp6Switch
        :type request: :class:`huaweicloudsdklive.v1.UpdateDomainIp6SwitchRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateDomainIp6SwitchResponse`
        """
        http_info = self._update_domain_ip6_switch_http_info(request)
        return self._call_api(**http_info)

    def update_domain_ip6_switch_async_invoker(self, request):
        http_info = self._update_domain_ip6_switch_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_domain_ip6_switch_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/domain/ipv6-switch",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDomainIp6SwitchResponse"
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
            ['application/json; charset=UTF-8'])

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

    def update_domain_key_chain_async(self, request):
        """更新指定域名的Key防盗链配置

        更新指定域名的Key防盗链配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDomainKeyChain
        :type request: :class:`huaweicloudsdklive.v1.UpdateDomainKeyChainRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateDomainKeyChainResponse`
        """
        http_info = self._update_domain_key_chain_http_info(request)
        return self._call_api(**http_info)

    def update_domain_key_chain_async_invoker(self, request):
        http_info = self._update_domain_key_chain_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_domain_key_chain_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/guard/key-chain",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDomainKeyChainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

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

    def update_record_callback_config_async(self, request):
        """修改录制回调配置

        修改录制回调配置接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRecordCallbackConfig
        :type request: :class:`huaweicloudsdklive.v1.UpdateRecordCallbackConfigRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateRecordCallbackConfigResponse`
        """
        http_info = self._update_record_callback_config_http_info(request)
        return self._call_api(**http_info)

    def update_record_callback_config_async_invoker(self, request):
        http_info = self._update_record_callback_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_record_callback_config_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/record/callbacks/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRecordCallbackConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            ['application/json; charset=UTF-8'])

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

    def update_record_rule_async(self, request):
        """修改录制规则

        修改录制规则接口，如果规则修改后，修改后的规则对正在录制的流无效，对新的流有效。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRecordRule
        :type request: :class:`huaweicloudsdklive.v1.UpdateRecordRuleRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateRecordRuleResponse`
        """
        http_info = self._update_record_rule_http_info(request)
        return self._call_api(**http_info)

    def update_record_rule_async_invoker(self, request):
        http_info = self._update_record_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_record_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/record/rules/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRecordRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            ['application/json; charset=UTF-8'])

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

    def update_snapshot_config_async(self, request):
        """修改直播截图配置

        修改直播截图配置接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSnapshotConfig
        :type request: :class:`huaweicloudsdklive.v1.UpdateSnapshotConfigRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateSnapshotConfigResponse`
        """
        http_info = self._update_snapshot_config_http_info(request)
        return self._call_api(**http_info)

    def update_snapshot_config_async_invoker(self, request):
        http_info = self._update_snapshot_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_snapshot_config_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/stream/snapshot",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSnapshotConfigResponse"
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
            ['application/json; charset=UTF-8'])

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

    def update_stream_forbidden_async(self, request):
        """修改禁推属性

        修改禁推属性
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateStreamForbidden
        :type request: :class:`huaweicloudsdklive.v1.UpdateStreamForbiddenRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateStreamForbiddenResponse`
        """
        http_info = self._update_stream_forbidden_http_info(request)
        return self._call_api(**http_info)

    def update_stream_forbidden_async_invoker(self, request):
        http_info = self._update_stream_forbidden_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_stream_forbidden_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/stream/blocks",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateStreamForbiddenResponse"
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
            ['application/json; charset=UTF-8'])

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

    def update_transcodings_template_async(self, request):
        """配置直播转码模板

        修改直播转码模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTranscodingsTemplate
        :type request: :class:`huaweicloudsdklive.v1.UpdateTranscodingsTemplateRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateTranscodingsTemplateResponse`
        """
        http_info = self._update_transcodings_template_http_info(request)
        return self._call_api(**http_info)

    def update_transcodings_template_async_invoker(self, request):
        http_info = self._update_transcodings_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_transcodings_template_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/template/transcodings",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTranscodingsTemplateResponse"
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
            ['application/json; charset=UTF-8'])

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

    def delete_domain_https_cert_async(self, request):
        """删除指定域名的https证书配置

        删除指定域名的https证书配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDomainHttpsCert
        :type request: :class:`huaweicloudsdklive.v1.DeleteDomainHttpsCertRequest`
        :rtype: :class:`huaweicloudsdklive.v1.DeleteDomainHttpsCertResponse`
        """
        http_info = self._delete_domain_https_cert_http_info(request)
        return self._call_api(**http_info)

    def delete_domain_https_cert_async_invoker(self, request):
        http_info = self._delete_domain_https_cert_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_domain_https_cert_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/guard/https-cert",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDomainHttpsCertResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

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

    def show_domain_https_cert_async(self, request):
        """查询指定域名的https证书配置

        查询指定域名的https证书配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDomainHttpsCert
        :type request: :class:`huaweicloudsdklive.v1.ShowDomainHttpsCertRequest`
        :rtype: :class:`huaweicloudsdklive.v1.ShowDomainHttpsCertResponse`
        """
        http_info = self._show_domain_https_cert_http_info(request)
        return self._call_api(**http_info)

    def show_domain_https_cert_async_invoker(self, request):
        http_info = self._show_domain_https_cert_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_domain_https_cert_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/guard/https-cert",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainHttpsCertResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

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

    def update_domain_https_cert_async(self, request):
        """修改指定域名的https证书配置

        修改指定域名的https证书配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDomainHttpsCert
        :type request: :class:`huaweicloudsdklive.v1.UpdateDomainHttpsCertRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateDomainHttpsCertResponse`
        """
        http_info = self._update_domain_https_cert_http_info(request)
        return self._call_api(**http_info)

    def update_domain_https_cert_async_invoker(self, request):
        http_info = self._update_domain_https_cert_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_domain_https_cert_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/guard/https-cert",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDomainHttpsCertResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

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

    def update_obs_bucket_authority_public_async(self, request):
        """OBS桶授权及取消授权

        OBS桶授权及取消授权
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateObsBucketAuthorityPublic
        :type request: :class:`huaweicloudsdklive.v1.UpdateObsBucketAuthorityPublicRequest`
        :rtype: :class:`huaweicloudsdklive.v1.UpdateObsBucketAuthorityPublicResponse`
        """
        http_info = self._update_obs_bucket_authority_public_http_info(request)
        return self._call_api(**http_info)

    def update_obs_bucket_authority_public_async_invoker(self, request):
        http_info = self._update_obs_bucket_authority_public_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_obs_bucket_authority_public_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/obs/authority",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateObsBucketAuthorityPublicResponse"
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
            ['application/json; charset=UTF-8'])

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
            kwargs["async_request"] = True
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
        :param header_params: Header parameters to be
            placed in the request header.
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
            request_type=request_type,
	        async_request=True)
