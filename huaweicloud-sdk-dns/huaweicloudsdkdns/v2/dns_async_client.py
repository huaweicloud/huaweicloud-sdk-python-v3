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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkdns'")


class DnsAsyncClient(Client):
    def __init__(self):
        super(DnsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdns.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "DnsAsyncClient":
                raise TypeError("client type error, support client type is DnsAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def associate_endpoint_ipaddress_async(self, request):
        r"""终端节点绑定IP地址

        终端节点绑定IP地址。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateEndpointIpaddress
        :type request: :class:`huaweicloudsdkdns.v2.AssociateEndpointIpaddressRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.AssociateEndpointIpaddressResponse`
        """
        http_info = self._associate_endpoint_ipaddress_http_info(request)
        return self._call_api(**http_info)

    def associate_endpoint_ipaddress_async_invoker(self, request):
        http_info = self._associate_endpoint_ipaddress_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_endpoint_ipaddress_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.1/endpoints/{endpoint_id}/ipaddresses",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateEndpointIpaddressResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_id' in local_var_params:
            path_params['endpoint_id'] = local_var_params['endpoint_id']

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

    def associate_resolver_rule_router_async(self, request):
        r"""解析器转发规则关联VPC

        解析器转发规则关联VPC。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateResolverRuleRouter
        :type request: :class:`huaweicloudsdkdns.v2.AssociateResolverRuleRouterRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.AssociateResolverRuleRouterResponse`
        """
        http_info = self._associate_resolver_rule_router_http_info(request)
        return self._call_api(**http_info)

    def associate_resolver_rule_router_async_invoker(self, request):
        http_info = self._associate_resolver_rule_router_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_resolver_rule_router_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.1/resolverrules/{resolverrule_id}/associaterouter",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateResolverRuleRouterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resolverrule_id' in local_var_params:
            path_params['resolverrule_id'] = local_var_params['resolverrule_id']

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

    def associate_router_async(self, request):
        r"""在内网域名上关联VPC

        当您的内网域名创建完成后，可以通过调用此接口为内网域名关联新的VPC。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateRouter
        :type request: :class:`huaweicloudsdkdns.v2.AssociateRouterRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.AssociateRouterResponse`
        """
        http_info = self._associate_router_http_info(request)
        return self._call_api(**http_info)

    def associate_router_async_invoker(self, request):
        http_info = self._associate_router_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_router_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/zones/{zone_id}/associaterouter",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateRouterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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

    def batch_create_tag_async(self, request):
        r"""为指定实例批量添加或删除标签

        为指定实例批量添加或删除标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateTag
        :type request: :class:`huaweicloudsdkdns.v2.BatchCreateTagRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.BatchCreateTagResponse`
        """
        http_info = self._batch_create_tag_http_info(request)
        return self._call_api(**http_info)

    def batch_create_tag_async_invoker(self, request):
        http_info = self._batch_create_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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

    def batch_delete_ptr_records_async(self, request):
        r"""批量删除反向解析

        批量删除反向解析。本接口为原子操作，所有记录应全部删除成功或全部失败。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeletePtrRecords
        :type request: :class:`huaweicloudsdkdns.v2.BatchDeletePtrRecordsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.BatchDeletePtrRecordsResponse`
        """
        http_info = self._batch_delete_ptr_records_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_ptr_records_async_invoker(self, request):
        http_info = self._batch_delete_ptr_records_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_ptr_records_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.1/reverse/floatingips",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeletePtrRecordsResponse"
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

    def batch_delete_record_set_with_line_async(self, request):
        r"""批量删除域名下的记录集

        批量删除域名下的记录集，当删除的资源不存在时，则默认删除成功。
        响应结果中只包含本次实际删除的资源。
        支持公网域名和内网域名。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteRecordSetWithLine
        :type request: :class:`huaweicloudsdkdns.v2.BatchDeleteRecordSetWithLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.BatchDeleteRecordSetWithLineResponse`
        """
        http_info = self._batch_delete_record_set_with_line_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_record_set_with_line_async_invoker(self, request):
        http_info = self._batch_delete_record_set_with_line_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_record_set_with_line_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.1/zones/{zone_id}/recordsets",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteRecordSetWithLineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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

    def batch_delete_record_sets_async(self, request):
        r"""批量删除记录集

        批量删除记录集。
        响应结果中只包含本次实际删除的记录集。
        支持批量删除公网域名和内网域名的记录集。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteRecordSets
        :type request: :class:`huaweicloudsdkdns.v2.BatchDeleteRecordSetsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.BatchDeleteRecordSetsResponse`
        """
        http_info = self._batch_delete_record_sets_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_record_sets_async_invoker(self, request):
        http_info = self._batch_delete_record_sets_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_record_sets_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.1/recordsets",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteRecordSetsResponse"
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

    def batch_delete_zones_async(self, request):
        r"""批量删除域名

        批量删除域名。
        本接口为原子操作，所有记录应全部删除成功或全部失败。
        支持公网域名、内网域名。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteZones
        :type request: :class:`huaweicloudsdkdns.v2.BatchDeleteZonesRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.BatchDeleteZonesResponse`
        """
        http_info = self._batch_delete_zones_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_zones_async_invoker(self, request):
        http_info = self._batch_delete_zones_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_zones_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.1/zones",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteZonesResponse"
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

    def batch_set_record_sets_status_async(self, request):
        r"""批量设置记录集状态

        批量设置记录集状态。
        响应结果中只包含本次实际更新的记录集。
        支持公网域名和内网域名的记录集。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchSetRecordSetsStatus
        :type request: :class:`huaweicloudsdkdns.v2.BatchSetRecordSetsStatusRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.BatchSetRecordSetsStatusResponse`
        """
        http_info = self._batch_set_record_sets_status_http_info(request)
        return self._call_api(**http_info)

    def batch_set_record_sets_status_async_invoker(self, request):
        http_info = self._batch_set_record_sets_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_set_record_sets_status_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.1/recordsets/statuses",
            "request_type": request.__class__.__name__,
            "response_type": "BatchSetRecordSetsStatusResponse"
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

    def batch_set_zones_status_async(self, request):
        r"""批量设置域名状态

        批量设置域名状态。
        响应结果中只包含本次实际更新的域名。
        支持公网域名、内网域名。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchSetZonesStatus
        :type request: :class:`huaweicloudsdkdns.v2.BatchSetZonesStatusRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.BatchSetZonesStatusResponse`
        """
        http_info = self._batch_set_zones_status_http_info(request)
        return self._call_api(**http_info)

    def batch_set_zones_status_async_invoker(self, request):
        http_info = self._batch_set_zones_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_set_zones_status_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.1/zones/statuses",
            "request_type": request.__class__.__name__,
            "response_type": "BatchSetZonesStatusResponse"
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

    def batch_update_record_set_with_line_async(self, request):
        r"""批量修改记录集

        批量修改记录集。属于原子性操作，请求记录集将全部完成修改，或不做任何修改。
        仅公网域名支持。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchUpdateRecordSetWithLine
        :type request: :class:`huaweicloudsdkdns.v2.BatchUpdateRecordSetWithLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.BatchUpdateRecordSetWithLineResponse`
        """
        http_info = self._batch_update_record_set_with_line_http_info(request)
        return self._call_api(**http_info)

    def batch_update_record_set_with_line_async_invoker(self, request):
        http_info = self._batch_update_record_set_with_line_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_update_record_set_with_line_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.1/zones/{zone_id}/recordsets",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateRecordSetWithLineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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

    def create_custom_line_async(self, request):
        r"""创建自定义线路

        创建自定义线路。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCustomLine
        :type request: :class:`huaweicloudsdkdns.v2.CreateCustomLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreateCustomLineResponse`
        """
        http_info = self._create_custom_line_http_info(request)
        return self._call_api(**http_info)

    def create_custom_line_async_invoker(self, request):
        http_info = self._create_custom_line_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_custom_line_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.1/customlines",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCustomLineResponse"
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

    def create_endpoint_async(self, request):
        r"""创建终端节点

        创建终端节点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEndpoint
        :type request: :class:`huaweicloudsdkdns.v2.CreateEndpointRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreateEndpointResponse`
        """
        http_info = self._create_endpoint_http_info(request)
        return self._call_api(**http_info)

    def create_endpoint_async_invoker(self, request):
        http_info = self._create_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_endpoint_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.1/endpoints",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEndpointResponse"
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

    def create_line_group_async(self, request):
        r"""创建线路分组

        创建线路分组。该接口部分区域未上线，如需使用请提交工单申请开通。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateLineGroup
        :type request: :class:`huaweicloudsdkdns.v2.CreateLineGroupRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreateLineGroupResponse`
        """
        http_info = self._create_line_group_http_info(request)
        return self._call_api(**http_info)

    def create_line_group_async_invoker(self, request):
        http_info = self._create_line_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_line_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.1/linegroups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLineGroupResponse"
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

    def create_private_zone_async(self, request):
        r"""创建内网域名

        内网域名是指在VPC中生效的域名，内网域名创建后，用户可以将其与私网IP地址相关联，为云服务提供VPC内的内网域名解析服务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePrivateZone
        :type request: :class:`huaweicloudsdkdns.v2.CreatePrivateZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreatePrivateZoneResponse`
        """
        http_info = self._create_private_zone_http_info(request)
        return self._call_api(**http_info)

    def create_private_zone_async_invoker(self, request):
        http_info = self._create_private_zone_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_private_zone_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/zones",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePrivateZoneResponse"
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

    def create_public_zone_async(self, request):
        r"""创建公网域名

        您在使用华为云云解析服务为自己注册的域名配置DNS解析之前，需要先将域名添加至云解析服务控制台。
        
        **[公网域名为全局资源，请选择“华北-北京四（cn-north-4）”区域调用。](tag:hws)**
        **[公网域名为全局资源，请选择“亚太-新加坡（ap-southeast-3）”区域调用。](tag:hws_hk)**
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePublicZone
        :type request: :class:`huaweicloudsdkdns.v2.CreatePublicZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreatePublicZoneResponse`
        """
        http_info = self._create_public_zone_http_info(request)
        return self._call_api(**http_info)

    def create_public_zone_async_invoker(self, request):
        http_info = self._create_public_zone_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_public_zone_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/zones",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePublicZoneResponse"
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

    def create_record_set_with_batch_lines_async(self, request):
        r"""批量线路创建记录集

        批量线路创建记录集。属于原子性操作，如果存在一个参数校验不通过，则创建失败。仅公网域名支持。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRecordSetWithBatchLines
        :type request: :class:`huaweicloudsdkdns.v2.CreateRecordSetWithBatchLinesRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreateRecordSetWithBatchLinesResponse`
        """
        http_info = self._create_record_set_with_batch_lines_http_info(request)
        return self._call_api(**http_info)

    def create_record_set_with_batch_lines_async_invoker(self, request):
        http_info = self._create_record_set_with_batch_lines_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_record_set_with_batch_lines_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.1/zones/{zone_id}/recordsets/batch/lines",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRecordSetWithBatchLinesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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

    def create_resolver_rule_async(self, request):
        r"""创建解析器转发规则

        创建解析器转发规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateResolverRule
        :type request: :class:`huaweicloudsdkdns.v2.CreateResolverRuleRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreateResolverRuleResponse`
        """
        http_info = self._create_resolver_rule_http_info(request)
        return self._call_api(**http_info)

    def create_resolver_rule_async_invoker(self, request):
        http_info = self._create_resolver_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_resolver_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.1/resolverrules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateResolverRuleResponse"
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

    def create_tag_async(self, request):
        r"""为指定实例添加标签

        为指定实例添加标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTag
        :type request: :class:`huaweicloudsdkdns.v2.CreateTagRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreateTagResponse`
        """
        http_info = self._create_tag_http_info(request)
        return self._call_api(**http_info)

    def create_tag_async_invoker(self, request):
        http_info = self._create_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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

    def delete_custom_line_async(self, request):
        r"""删除自定义线路

        删除自定义线路。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCustomLine
        :type request: :class:`huaweicloudsdkdns.v2.DeleteCustomLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeleteCustomLineResponse`
        """
        http_info = self._delete_custom_line_http_info(request)
        return self._call_api(**http_info)

    def delete_custom_line_async_invoker(self, request):
        http_info = self._delete_custom_line_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_custom_line_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.1/customlines/{line_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCustomLineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'line_id' in local_var_params:
            path_params['line_id'] = local_var_params['line_id']

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

    def delete_endpoint_async(self, request):
        r"""删除终端节点

        删除终端节点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEndpoint
        :type request: :class:`huaweicloudsdkdns.v2.DeleteEndpointRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeleteEndpointResponse`
        """
        http_info = self._delete_endpoint_http_info(request)
        return self._call_api(**http_info)

    def delete_endpoint_async_invoker(self, request):
        http_info = self._delete_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_endpoint_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.1/endpoints/{endpoint_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_id' in local_var_params:
            path_params['endpoint_id'] = local_var_params['endpoint_id']

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

    def delete_line_group_async(self, request):
        r"""删除线路分组

        删除线路分组。该接口部分区域未上线，如需使用请提交工单申请开通。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteLineGroup
        :type request: :class:`huaweicloudsdkdns.v2.DeleteLineGroupRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeleteLineGroupResponse`
        """
        http_info = self._delete_line_group_http_info(request)
        return self._call_api(**http_info)

    def delete_line_group_async_invoker(self, request):
        http_info = self._delete_line_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_line_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.1/linegroups/{linegroup_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLineGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'linegroup_id' in local_var_params:
            path_params['linegroup_id'] = local_var_params['linegroup_id']

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

    def delete_private_zone_async(self, request):
        r"""删除内网域名

        当您的内网域名不再使用时，您可以通过调用此接口将其删除。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePrivateZone
        :type request: :class:`huaweicloudsdkdns.v2.DeletePrivateZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeletePrivateZoneResponse`
        """
        http_info = self._delete_private_zone_http_info(request)
        return self._call_api(**http_info)

    def delete_private_zone_async_invoker(self, request):
        http_info = self._delete_private_zone_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_private_zone_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/zones/{zone_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePrivateZoneResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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

    def delete_public_zone_async(self, request):
        r"""删除公网域名

        当您的公网域名不再使用时，您可以通过调用此接口将其删除。
        
        **[公网域名为全局资源，请选择“华北-北京四（cn-north-4）”区域调用。](tag:hws)**
        **[公网域名为全局资源，请选择“亚太-新加坡（ap-southeast-3）”区域调用。](tag:hws_hk)**
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePublicZone
        :type request: :class:`huaweicloudsdkdns.v2.DeletePublicZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeletePublicZoneResponse`
        """
        http_info = self._delete_public_zone_http_info(request)
        return self._call_api(**http_info)

    def delete_public_zone_async_invoker(self, request):
        http_info = self._delete_public_zone_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_public_zone_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/zones/{zone_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePublicZoneResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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

    def delete_resolver_rule_async(self, request):
        r"""删除解析器转发规则

        删除解析器转发规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteResolverRule
        :type request: :class:`huaweicloudsdkdns.v2.DeleteResolverRuleRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeleteResolverRuleResponse`
        """
        http_info = self._delete_resolver_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_resolver_rule_async_invoker(self, request):
        http_info = self._delete_resolver_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_resolver_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.1/resolverrules/{resolverrule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteResolverRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resolverrule_id' in local_var_params:
            path_params['resolverrule_id'] = local_var_params['resolverrule_id']

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

    def delete_tag_async(self, request):
        r"""删除资源标签

        删除资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTag
        :type request: :class:`huaweicloudsdkdns.v2.DeleteTagRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeleteTagResponse`
        """
        http_info = self._delete_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_tag_async_invoker(self, request):
        http_info = self._delete_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_tag_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/tags/{key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']

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

    def disassociate_endpoint_ipaddress_async(self, request):
        r"""终端节点解绑IP地址

        终端节点解绑IP地址。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateEndpointIpaddress
        :type request: :class:`huaweicloudsdkdns.v2.DisassociateEndpointIpaddressRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DisassociateEndpointIpaddressResponse`
        """
        http_info = self._disassociate_endpoint_ipaddress_http_info(request)
        return self._call_api(**http_info)

    def disassociate_endpoint_ipaddress_async_invoker(self, request):
        http_info = self._disassociate_endpoint_ipaddress_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disassociate_endpoint_ipaddress_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.1/endpoints/{endpoint_id}/ipaddresses/{ipaddress_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateEndpointIpaddressResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_id' in local_var_params:
            path_params['endpoint_id'] = local_var_params['endpoint_id']
        if 'ipaddress_id' in local_var_params:
            path_params['ipaddress_id'] = local_var_params['ipaddress_id']

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

    def disassociate_resolver_rule_router_async(self, request):
        r"""解析器转发规则解关联VPC

        解析器转发规则解关联VPC。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateResolverRuleRouter
        :type request: :class:`huaweicloudsdkdns.v2.DisassociateResolverRuleRouterRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DisassociateResolverRuleRouterResponse`
        """
        http_info = self._disassociate_resolver_rule_router_http_info(request)
        return self._call_api(**http_info)

    def disassociate_resolver_rule_router_async_invoker(self, request):
        http_info = self._disassociate_resolver_rule_router_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disassociate_resolver_rule_router_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.1/resolverrules/{resolverrule_id}/disassociaterouter",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateResolverRuleRouterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resolverrule_id' in local_var_params:
            path_params['resolverrule_id'] = local_var_params['resolverrule_id']

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

    def disassociate_router_async(self, request):
        r"""在内网域名上解关联VPC

        当您的内网域名创建完成后，可以通过调用此接口为内网域名解除已关联的VPC。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateRouter
        :type request: :class:`huaweicloudsdkdns.v2.DisassociateRouterRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DisassociateRouterResponse`
        """
        http_info = self._disassociate_router_http_info(request)
        return self._call_api(**http_info)

    def disassociate_router_async_invoker(self, request):
        http_info = self._disassociate_router_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disassociate_router_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/zones/{zone_id}/disassociaterouter",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateRouterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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

    def list_api_versions_async(self, request):
        r"""查询API版本信息列表

        查询云解析服务支持的所有API版本信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApiVersions
        :type request: :class:`huaweicloudsdkdns.v2.ListApiVersionsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListApiVersionsResponse`
        """
        http_info = self._list_api_versions_http_info(request)
        return self._call_api(**http_info)

    def list_api_versions_async_invoker(self, request):
        http_info = self._list_api_versions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_api_versions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/",
            "request_type": request.__class__.__name__,
            "response_type": "ListApiVersionsResponse"
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

    def list_custom_line_async(self, request):
        r"""查询自定义线路

        查询自定义线路。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCustomLine
        :type request: :class:`huaweicloudsdkdns.v2.ListCustomLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListCustomLineResponse`
        """
        http_info = self._list_custom_line_http_info(request)
        return self._call_api(**http_info)

    def list_custom_line_async_invoker(self, request):
        http_info = self._list_custom_line_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_custom_line_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.1/customlines",
            "request_type": request.__class__.__name__,
            "response_type": "ListCustomLineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'line_id' in local_var_params:
            query_params.append(('line_id', local_var_params['line_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'show_detail' in local_var_params:
            query_params.append(('show_detail', local_var_params['show_detail']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))

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

    def list_endpoint_ipaddresses_async(self, request):
        r"""查询IP地址列表

        查询终端节点下的IP地址列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEndpointIpaddresses
        :type request: :class:`huaweicloudsdkdns.v2.ListEndpointIpaddressesRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListEndpointIpaddressesResponse`
        """
        http_info = self._list_endpoint_ipaddresses_http_info(request)
        return self._call_api(**http_info)

    def list_endpoint_ipaddresses_async_invoker(self, request):
        http_info = self._list_endpoint_ipaddresses_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_endpoint_ipaddresses_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.1/endpoints/{endpoint_id}/ipaddresses",
            "request_type": request.__class__.__name__,
            "response_type": "ListEndpointIpaddressesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_id' in local_var_params:
            path_params['endpoint_id'] = local_var_params['endpoint_id']

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

    def list_endpoint_vpcs_async(self, request):
        r"""查询终端节点VPC列表

        查询终端节点VPC列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEndpointVpcs
        :type request: :class:`huaweicloudsdkdns.v2.ListEndpointVpcsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListEndpointVpcsResponse`
        """
        http_info = self._list_endpoint_vpcs_http_info(request)
        return self._call_api(**http_info)

    def list_endpoint_vpcs_async_invoker(self, request):
        http_info = self._list_endpoint_vpcs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_endpoint_vpcs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.1/vpcs",
            "request_type": request.__class__.__name__,
            "response_type": "ListEndpointVpcsResponse"
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
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))

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

    def list_endpoints_async(self, request):
        r"""查询终端节点列表

        查询终端节点列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEndpoints
        :type request: :class:`huaweicloudsdkdns.v2.ListEndpointsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListEndpointsResponse`
        """
        http_info = self._list_endpoints_http_info(request)
        return self._call_api(**http_info)

    def list_endpoints_async_invoker(self, request):
        http_info = self._list_endpoints_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_endpoints_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.1/endpoints",
            "request_type": request.__class__.__name__,
            "response_type": "ListEndpointsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'direction' in local_var_params:
            query_params.append(('direction', local_var_params['direction']))
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
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

    def list_line_groups_async(self, request):
        r"""查询线路分组列表

        查询线路分组列表。该接口部分区域未上线，如需使用请提交工单申请开通。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLineGroups
        :type request: :class:`huaweicloudsdkdns.v2.ListLineGroupsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListLineGroupsResponse`
        """
        http_info = self._list_line_groups_http_info(request)
        return self._call_api(**http_info)

    def list_line_groups_async_invoker(self, request):
        http_info = self._list_line_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_line_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.1/linegroups",
            "request_type": request.__class__.__name__,
            "response_type": "ListLineGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'line_id' in local_var_params:
            query_params.append(('line_id', local_var_params['line_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
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

    def list_name_servers_async(self, request):
        r"""查询名称服务器列表

        查询名称服务器列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNameServers
        :type request: :class:`huaweicloudsdkdns.v2.ListNameServersRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListNameServersResponse`
        """
        http_info = self._list_name_servers_http_info(request)
        return self._call_api(**http_info)

    def list_name_servers_async_invoker(self, request):
        http_info = self._list_name_servers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_name_servers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/nameservers",
            "request_type": request.__class__.__name__,
            "response_type": "ListNameServersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))

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

    def list_private_zones_async(self, request):
        r"""查询内网域名列表

        当您的内网域名创建成功后，您可以通过调用此接口查询单个内网域名信息，包括域名、ID、状态、记录集个数、企业项目、标签、TTL、创建时间、修改时间、描述等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPrivateZones
        :type request: :class:`huaweicloudsdkdns.v2.ListPrivateZonesRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListPrivateZonesResponse`
        """
        http_info = self._list_private_zones_http_info(request)
        return self._call_api(**http_info)

    def list_private_zones_async_invoker(self, request):
        http_info = self._list_private_zones_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_private_zones_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/zones",
            "request_type": request.__class__.__name__,
            "response_type": "ListPrivateZonesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'search_mode' in local_var_params:
            query_params.append(('search_mode', local_var_params['search_mode']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'router_id' in local_var_params:
            query_params.append(('router_id', local_var_params['router_id']))

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

    def list_public_zones_async(self, request):
        r"""查询公网域名列表

        当您的公网域名创建成功后，您可以通过调用此接口查询所有公网域名信息，包括域名、ID、状态、记录集个数、企业项目、标签、TTL、创建时间、修改时间、描述等。
        
        **[公网域名为全局资源，请选择“华北-北京四（cn-north-4）”区域调用。](tag:hws)**
        **[公网域名为全局资源，请选择“亚太-新加坡（ap-southeast-3）”区域调用。](tag:hws_hk)**
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPublicZones
        :type request: :class:`huaweicloudsdkdns.v2.ListPublicZonesRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListPublicZonesResponse`
        """
        http_info = self._list_public_zones_http_info(request)
        return self._call_api(**http_info)

    def list_public_zones_async_invoker(self, request):
        http_info = self._list_public_zones_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_public_zones_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/zones",
            "request_type": request.__class__.__name__,
            "response_type": "ListPublicZonesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'search_mode' in local_var_params:
            query_params.append(('search_mode', local_var_params['search_mode']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
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

    def list_resolver_rules_async(self, request):
        r"""查询解析器转发规则列表

        查询解析器转发规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResolverRules
        :type request: :class:`huaweicloudsdkdns.v2.ListResolverRulesRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListResolverRulesResponse`
        """
        http_info = self._list_resolver_rules_http_info(request)
        return self._call_api(**http_info)

    def list_resolver_rules_async_invoker(self, request):
        http_info = self._list_resolver_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_resolver_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.1/resolverrules",
            "request_type": request.__class__.__name__,
            "response_type": "ListResolverRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'endpoint_id' in local_var_params:
            query_params.append(('endpoint_id', local_var_params['endpoint_id']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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

    def list_tag_async(self, request):
        r"""使用标签查询资源实例

        使用标签查询资源实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTag
        :type request: :class:`huaweicloudsdkdns.v2.ListTagRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListTagResponse`
        """
        http_info = self._list_tag_http_info(request)
        return self._call_api(**http_info)

    def list_tag_async_invoker(self, request):
        http_info = self._list_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{resource_type}/resource_instances/action",
            "request_type": request.__class__.__name__,
            "response_type": "ListTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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

    def list_tags_async(self, request):
        r"""查询指定实例类型的所有标签集合

        查询指定实例类型的所有标签集合
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTags
        :type request: :class:`huaweicloudsdkdns.v2.ListTagsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListTagsResponse`
        """
        http_info = self._list_tags_http_info(request)
        return self._call_api(**http_info)

    def list_tags_async_invoker(self, request):
        http_info = self._list_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/{resource_type}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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

    def set_private_zone_proxy_pattern_async(self, request):
        r"""设置内网域名的子域名递归解析代理

        当您的内网域名创建成功后，您可以通过调用此接口设置开启或者关闭内网域名的子域名递归解析代理。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetPrivateZoneProxyPattern
        :type request: :class:`huaweicloudsdkdns.v2.SetPrivateZoneProxyPatternRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.SetPrivateZoneProxyPatternResponse`
        """
        http_info = self._set_private_zone_proxy_pattern_http_info(request)
        return self._call_api(**http_info)

    def set_private_zone_proxy_pattern_async_invoker(self, request):
        http_info = self._set_private_zone_proxy_pattern_http_info(request)
        return AsyncInvoker(self, http_info)

    def _set_private_zone_proxy_pattern_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/zones/{zone_id}/actions/set-proxy-pattern",
            "request_type": request.__class__.__name__,
            "response_type": "SetPrivateZoneProxyPatternResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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

    def show_api_info_async(self, request):
        r"""查询指定版本号的API版本信息

        查询指定版本号的云解析服务API版本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowApiInfo
        :type request: :class:`huaweicloudsdkdns.v2.ShowApiInfoRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowApiInfoResponse`
        """
        http_info = self._show_api_info_http_info(request)
        return self._call_api(**http_info)

    def show_api_info_async_invoker(self, request):
        http_info = self._show_api_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_api_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/{version}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApiInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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

    def show_domain_quota_async(self, request):
        r"""查询租户配额

        查询租户在DNS服务下的资源配额，包括公网域名配额、内网域名配额、记录集配额、反向解析配额、自定义线路配额、线路分组配额、入站终端节点配额、出站终端节点配额、转发规则配额等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDomainQuota
        :type request: :class:`huaweicloudsdkdns.v2.ShowDomainQuotaRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowDomainQuotaResponse`
        """
        http_info = self._show_domain_quota_http_info(request)
        return self._call_api(**http_info)

    def show_domain_quota_async_invoker(self, request):
        http_info = self._show_domain_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_domain_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/quotamg/dns/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainQuotaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain_id' in local_var_params:
            query_params.append(('domain_id', local_var_params['domain_id']))

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

    def show_endpoint_async(self, request):
        r"""查询终端节点

        查询终端节点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEndpoint
        :type request: :class:`huaweicloudsdkdns.v2.ShowEndpointRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowEndpointResponse`
        """
        http_info = self._show_endpoint_http_info(request)
        return self._call_api(**http_info)

    def show_endpoint_async_invoker(self, request):
        http_info = self._show_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_endpoint_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.1/endpoints/{endpoint_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_id' in local_var_params:
            path_params['endpoint_id'] = local_var_params['endpoint_id']

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

    def show_line_group_async(self, request):
        r"""查询线路分组

        查询线路分组。该接口部分区域未上线，如需使用请提交工单申请开通。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowLineGroup
        :type request: :class:`huaweicloudsdkdns.v2.ShowLineGroupRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowLineGroupResponse`
        """
        http_info = self._show_line_group_http_info(request)
        return self._call_api(**http_info)

    def show_line_group_async_invoker(self, request):
        http_info = self._show_line_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_line_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.1/linegroups/{linegroup_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLineGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'linegroup_id' in local_var_params:
            path_params['linegroup_id'] = local_var_params['linegroup_id']

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

    def show_private_zone_async(self, request):
        r"""查询内网域名

        当您的内网域名创建成功后，您可以通过调用此接口查询单个内网域名信息，包括域名、ID、状态、记录集个数、企业项目、标签、TTL、创建时间、修改时间、描述等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPrivateZone
        :type request: :class:`huaweicloudsdkdns.v2.ShowPrivateZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowPrivateZoneResponse`
        """
        http_info = self._show_private_zone_http_info(request)
        return self._call_api(**http_info)

    def show_private_zone_async_invoker(self, request):
        http_info = self._show_private_zone_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_private_zone_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/zones/{zone_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPrivateZoneResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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

    def show_private_zone_name_server_async(self, request):
        r"""查询内网域名的名称服务器

        当您的内网域名创建成功后，您可以通过调用此接口查询内网域名的名称服务器信息，包括优先级、DNS服务器地址等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPrivateZoneNameServer
        :type request: :class:`huaweicloudsdkdns.v2.ShowPrivateZoneNameServerRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowPrivateZoneNameServerResponse`
        """
        http_info = self._show_private_zone_name_server_http_info(request)
        return self._call_api(**http_info)

    def show_private_zone_name_server_async_invoker(self, request):
        http_info = self._show_private_zone_name_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_private_zone_name_server_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/zones/{zone_id}/nameservers",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPrivateZoneNameServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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

    def show_public_zone_async(self, request):
        r"""查询公网域名

        当您的公网域名创建成功后，您可以通过调用此接口查询单个公网域名信息，包括域名、ID、状态、记录集个数、企业项目、标签、TTL、创建时间、修改时间、描述等。
        
        **[公网域名为全局资源，请选择“华北-北京四（cn-north-4）”区域调用。](tag:hws)**
        **[公网域名为全局资源，请选择“亚太-新加坡（ap-southeast-3）”区域调用。](tag:hws_hk)**
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPublicZone
        :type request: :class:`huaweicloudsdkdns.v2.ShowPublicZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowPublicZoneResponse`
        """
        http_info = self._show_public_zone_http_info(request)
        return self._call_api(**http_info)

    def show_public_zone_async_invoker(self, request):
        http_info = self._show_public_zone_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_public_zone_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/zones/{zone_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPublicZoneResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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

    def show_public_zone_name_server_async(self, request):
        r"""查询公网域名的名称服务器

        当您的公网域名创建成功后，您可以通过调用此接口查询公网域名的名称服务器信息，包括主机名、优先级等。
        
        **[公网域名为全局资源，请选择“华北-北京四（cn-north-4）”区域调用。](tag:hws)**
        **[公网域名为全局资源，请选择“亚太-新加坡（ap-southeast-3）”区域调用。](tag:hws_hk)**
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPublicZoneNameServer
        :type request: :class:`huaweicloudsdkdns.v2.ShowPublicZoneNameServerRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowPublicZoneNameServerResponse`
        """
        http_info = self._show_public_zone_name_server_http_info(request)
        return self._call_api(**http_info)

    def show_public_zone_name_server_async_invoker(self, request):
        http_info = self._show_public_zone_name_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_public_zone_name_server_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/zones/{zone_id}/nameservers",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPublicZoneNameServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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

    def show_resolver_rule_async(self, request):
        r"""查询解析器转发规则

        查询解析器转发规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResolverRule
        :type request: :class:`huaweicloudsdkdns.v2.ShowResolverRuleRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowResolverRuleResponse`
        """
        http_info = self._show_resolver_rule_http_info(request)
        return self._call_api(**http_info)

    def show_resolver_rule_async_invoker(self, request):
        http_info = self._show_resolver_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_resolver_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.1/resolverrules/{resolverrule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResolverRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resolverrule_id' in local_var_params:
            path_params['resolverrule_id'] = local_var_params['resolverrule_id']

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

    def show_resource_tag_async(self, request):
        r"""查询指定实例的标签信息

        查询指定实例的标签信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourceTag
        :type request: :class:`huaweicloudsdkdns.v2.ShowResourceTagRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowResourceTagResponse`
        """
        http_info = self._show_resource_tag_http_info(request)
        return self._call_api(**http_info)

    def show_resource_tag_async_invoker(self, request):
        http_info = self._show_resource_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_resource_tag_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourceTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
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

    def update_custom_line_async(self, request):
        r"""修改自定义线路

        修改自定义线路。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCustomLine
        :type request: :class:`huaweicloudsdkdns.v2.UpdateCustomLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdateCustomLineResponse`
        """
        http_info = self._update_custom_line_http_info(request)
        return self._call_api(**http_info)

    def update_custom_line_async_invoker(self, request):
        http_info = self._update_custom_line_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_custom_line_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.1/customlines/{line_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCustomLineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'line_id' in local_var_params:
            path_params['line_id'] = local_var_params['line_id']

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

    def update_endpoint_async(self, request):
        r"""修改终端节点

        修改终端节点
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEndpoint
        :type request: :class:`huaweicloudsdkdns.v2.UpdateEndpointRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdateEndpointResponse`
        """
        http_info = self._update_endpoint_http_info(request)
        return self._call_api(**http_info)

    def update_endpoint_async_invoker(self, request):
        http_info = self._update_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_endpoint_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.1/endpoints/{endpoint_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_id' in local_var_params:
            path_params['endpoint_id'] = local_var_params['endpoint_id']

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

    def update_line_groups_async(self, request):
        r"""修改线路分组

        修改线路分组。该接口部分区域未上线，如需使用请提交工单申请开通。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateLineGroups
        :type request: :class:`huaweicloudsdkdns.v2.UpdateLineGroupsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdateLineGroupsResponse`
        """
        http_info = self._update_line_groups_http_info(request)
        return self._call_api(**http_info)

    def update_line_groups_async_invoker(self, request):
        http_info = self._update_line_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_line_groups_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.1/linegroups/{linegroup_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLineGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'linegroup_id' in local_var_params:
            path_params['linegroup_id'] = local_var_params['linegroup_id']

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

    def update_private_zone_async(self, request):
        r"""修改内网域名

        当您的内网域名创建成功后，您可以通过调用此接口修改内网域名的基本信息，包括TTL、描述等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePrivateZone
        :type request: :class:`huaweicloudsdkdns.v2.UpdatePrivateZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdatePrivateZoneResponse`
        """
        http_info = self._update_private_zone_http_info(request)
        return self._call_api(**http_info)

    def update_private_zone_async_invoker(self, request):
        http_info = self._update_private_zone_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_private_zone_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v2/zones/{zone_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePrivateZoneResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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

    def update_private_zone_status_async(self, request):
        r"""设置内网域名状态

        当您的内网域名创建成功后，您可以通过调用此接口设置内网域名的状态，包括暂停、启用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePrivateZoneStatus
        :type request: :class:`huaweicloudsdkdns.v2.UpdatePrivateZoneStatusRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdatePrivateZoneStatusResponse`
        """
        http_info = self._update_private_zone_status_http_info(request)
        return self._call_api(**http_info)

    def update_private_zone_status_async_invoker(self, request):
        http_info = self._update_private_zone_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_private_zone_status_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/zones/{zone_id}/statuses",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePrivateZoneStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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

    def update_public_zone_async(self, request):
        r"""修改公网域名

        当您的公网域名创建成功后，您可以通过调用此接口修改公网域名的基本信息，包括TTL、描述等。
        
        **[公网域名为全局资源，请选择“华北-北京四（cn-north-4）”区域调用。](tag:hws)**
        **[公网域名为全局资源，请选择“亚太-新加坡（ap-southeast-3）”区域调用。](tag:hws_hk)**
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePublicZone
        :type request: :class:`huaweicloudsdkdns.v2.UpdatePublicZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdatePublicZoneResponse`
        """
        http_info = self._update_public_zone_http_info(request)
        return self._call_api(**http_info)

    def update_public_zone_async_invoker(self, request):
        http_info = self._update_public_zone_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_public_zone_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v2/zones/{zone_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePublicZoneResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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

    def update_public_zone_status_async(self, request):
        r"""设置公网域名状态

        当您的公网域名创建成功后，您可以通过调用此接口设置公网域名的状态，包括暂停、启用。
        
        **[公网域名为全局资源，请选择“华北-北京四（cn-north-4）”区域调用。](tag:hws)**
        **[公网域名为全局资源，请选择“亚太-新加坡（ap-southeast-3）”区域调用。](tag:hws_hk)**
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePublicZoneStatus
        :type request: :class:`huaweicloudsdkdns.v2.UpdatePublicZoneStatusRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdatePublicZoneStatusResponse`
        """
        http_info = self._update_public_zone_status_http_info(request)
        return self._call_api(**http_info)

    def update_public_zone_status_async_invoker(self, request):
        http_info = self._update_public_zone_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_public_zone_status_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/zones/{zone_id}/statuses",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePublicZoneStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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

    def update_resolver_rule_async(self, request):
        r"""修改解析器转发规则

        修改解析器转发规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateResolverRule
        :type request: :class:`huaweicloudsdkdns.v2.UpdateResolverRuleRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdateResolverRuleResponse`
        """
        http_info = self._update_resolver_rule_http_info(request)
        return self._call_api(**http_info)

    def update_resolver_rule_async_invoker(self, request):
        http_info = self._update_resolver_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_resolver_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.1/resolverrules/{resolverrule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateResolverRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resolverrule_id' in local_var_params:
            path_params['resolverrule_id'] = local_var_params['resolverrule_id']

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

    def disable_dnssec_config_async(self, request):
        r"""关闭DNSSEC

        关闭公网域名的DNSSEC。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisableDnssecConfig
        :type request: :class:`huaweicloudsdkdns.v2.DisableDnssecConfigRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DisableDnssecConfigResponse`
        """
        http_info = self._disable_dnssec_config_http_info(request)
        return self._call_api(**http_info)

    def disable_dnssec_config_async_invoker(self, request):
        http_info = self._disable_dnssec_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disable_dnssec_config_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/zones/{zone_id}/disable-dnssec",
            "request_type": request.__class__.__name__,
            "response_type": "DisableDnssecConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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

    def enable_dnssec_config_async(self, request):
        r"""开启DNSSEC

        开启公网域名的DNSSEC。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableDnssecConfig
        :type request: :class:`huaweicloudsdkdns.v2.EnableDnssecConfigRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.EnableDnssecConfigResponse`
        """
        http_info = self._enable_dnssec_config_http_info(request)
        return self._call_api(**http_info)

    def enable_dnssec_config_async_invoker(self, request):
        http_info = self._enable_dnssec_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _enable_dnssec_config_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/zones/{zone_id}/enable-dnssec",
            "request_type": request.__class__.__name__,
            "response_type": "EnableDnssecConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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

    def show_dnssec_config_async(self, request):
        r"""查询DNSSEC

        查询公网域名的DNSSEC。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDnssecConfig
        :type request: :class:`huaweicloudsdkdns.v2.ShowDnssecConfigRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowDnssecConfigResponse`
        """
        http_info = self._show_dnssec_config_http_info(request)
        return self._call_api(**http_info)

    def show_dnssec_config_async_invoker(self, request):
        http_info = self._show_dnssec_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_dnssec_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/zones/{zone_id}/dnssec",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDnssecConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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

    def create_eip_record_set_async(self, request):
        r"""设置弹性公网IP的反向解析记录

        设置弹性公网IP的反向解析记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEipRecordSet
        :type request: :class:`huaweicloudsdkdns.v2.CreateEipRecordSetRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreateEipRecordSetResponse`
        """
        http_info = self._create_eip_record_set_http_info(request)
        return self._call_api(**http_info)

    def create_eip_record_set_async_invoker(self, request):
        http_info = self._create_eip_record_set_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_eip_record_set_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v2/reverse/floatingips/{region}:{floatingip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEipRecordSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'region' in local_var_params:
            path_params['region'] = local_var_params['region']
        if 'floatingip_id' in local_var_params:
            path_params['floatingip_id'] = local_var_params['floatingip_id']

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

    def create_record_set_async(self, request):
        r"""创建记录集

        记录集是指一组资源记录的集合，这些资源记录属于同一域名，用于定义域名支持的解析类型以及解析值。您的域名创建完成后，可以通过调用此接口为域名添加不同类型的记录集。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRecordSet
        :type request: :class:`huaweicloudsdkdns.v2.CreateRecordSetRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreateRecordSetResponse`
        """
        http_info = self._create_record_set_http_info(request)
        return self._call_api(**http_info)

    def create_record_set_async_invoker(self, request):
        http_info = self._create_record_set_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_record_set_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/zones/{zone_id}/recordsets",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRecordSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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

    def delete_record_set_async(self, request):
        r"""删除记录集

        当您的记录集不再使用时，您可以通过调用此接口将其删除。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRecordSet
        :type request: :class:`huaweicloudsdkdns.v2.DeleteRecordSetRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeleteRecordSetResponse`
        """
        http_info = self._delete_record_set_http_info(request)
        return self._call_api(**http_info)

    def delete_record_set_async_invoker(self, request):
        http_info = self._delete_record_set_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_record_set_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/zones/{zone_id}/recordsets/{recordset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRecordSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']
        if 'recordset_id' in local_var_params:
            path_params['recordset_id'] = local_var_params['recordset_id']

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

    def list_ptr_records_async(self, request):
        r"""查询弹性公网IP的反向解析记录列表

        查询弹性公网IP的反向解析记录列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPtrRecords
        :type request: :class:`huaweicloudsdkdns.v2.ListPtrRecordsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListPtrRecordsResponse`
        """
        http_info = self._list_ptr_records_http_info(request)
        return self._call_api(**http_info)

    def list_ptr_records_async_invoker(self, request):
        http_info = self._list_ptr_records_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ptr_records_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/reverse/floatingips",
            "request_type": request.__class__.__name__,
            "response_type": "ListPtrRecordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
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

    def list_record_sets_async(self, request):
        r"""查询租户记录集列表

        当您的记录集创建成功后，您可以通过调用此接口查询指定域名下的所有记录集信息，包括名称、ID、状态、所属域名、解析记录值、标签、TTL、创建时间、修改时间、描述等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRecordSets
        :type request: :class:`huaweicloudsdkdns.v2.ListRecordSetsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListRecordSetsResponse`
        """
        http_info = self._list_record_sets_http_info(request)
        return self._call_api(**http_info)

    def list_record_sets_async_invoker(self, request):
        http_info = self._list_record_sets_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_record_sets_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/recordsets",
            "request_type": request.__class__.__name__,
            "response_type": "ListRecordSetsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'zone_type' in local_var_params:
            query_params.append(('zone_type', local_var_params['zone_type']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'search_mode' in local_var_params:
            query_params.append(('search_mode', local_var_params['search_mode']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'records' in local_var_params:
            query_params.append(('records', local_var_params['records']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

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

    def list_record_sets_by_zone_async(self, request):
        r"""查询域名下的记录集列表

        当您的记录集创建成功后，您可以通过调用此接口查询指定域名下的所有记录集信息，包括名称、ID、状态、所属域名、解析记录值、标签、TTL、创建时间、修改时间、描述等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRecordSetsByZone
        :type request: :class:`huaweicloudsdkdns.v2.ListRecordSetsByZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListRecordSetsByZoneResponse`
        """
        http_info = self._list_record_sets_by_zone_http_info(request)
        return self._call_api(**http_info)

    def list_record_sets_by_zone_async_invoker(self, request):
        http_info = self._list_record_sets_by_zone_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_record_sets_by_zone_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/zones/{zone_id}/recordsets",
            "request_type": request.__class__.__name__,
            "response_type": "ListRecordSetsByZoneResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

        query_params = []
        if 'search_mode' in local_var_params:
            query_params.append(('search_mode', local_var_params['search_mode']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

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

    def restore_ptr_record_async(self, request):
        r"""将弹性公网IP的反向解析记录恢复为默认值

        将弹性公网IP的反向解析记录恢复为默认值。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestorePtrRecord
        :type request: :class:`huaweicloudsdkdns.v2.RestorePtrRecordRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.RestorePtrRecordResponse`
        """
        http_info = self._restore_ptr_record_http_info(request)
        return self._call_api(**http_info)

    def restore_ptr_record_async_invoker(self, request):
        http_info = self._restore_ptr_record_http_info(request)
        return AsyncInvoker(self, http_info)

    def _restore_ptr_record_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v2/reverse/floatingips/{region}:{floatingip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "RestorePtrRecordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'region' in local_var_params:
            path_params['region'] = local_var_params['region']
        if 'floatingip_id' in local_var_params:
            path_params['floatingip_id'] = local_var_params['floatingip_id']

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

    def show_ptr_record_set_async(self, request):
        r"""查询弹性公网IP的反向解析记录

        查询弹性公网IP的反向解析记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPtrRecordSet
        :type request: :class:`huaweicloudsdkdns.v2.ShowPtrRecordSetRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowPtrRecordSetResponse`
        """
        http_info = self._show_ptr_record_set_http_info(request)
        return self._call_api(**http_info)

    def show_ptr_record_set_async_invoker(self, request):
        http_info = self._show_ptr_record_set_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ptr_record_set_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/reverse/floatingips/{region}:{floatingip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPtrRecordSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'region' in local_var_params:
            path_params['region'] = local_var_params['region']
        if 'floatingip_id' in local_var_params:
            path_params['floatingip_id'] = local_var_params['floatingip_id']

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

    def show_record_set_async(self, request):
        r"""查询记录集

        当您的记录集创建成功后，您可以通过调用此接口查询指定域名下的所有记录集信息，包括名称、ID、状态、所属域名、解析记录值、标签、TTL、创建时间、修改时间、描述等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRecordSet
        :type request: :class:`huaweicloudsdkdns.v2.ShowRecordSetRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowRecordSetResponse`
        """
        http_info = self._show_record_set_http_info(request)
        return self._call_api(**http_info)

    def show_record_set_async_invoker(self, request):
        http_info = self._show_record_set_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_record_set_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/zones/{zone_id}/recordsets/{recordset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRecordSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']
        if 'recordset_id' in local_var_params:
            path_params['recordset_id'] = local_var_params['recordset_id']

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

    def update_ptr_record_async(self, request):
        r"""修改弹性公网IP的反向解析记录

        修改弹性公网IP的反向解析记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePtrRecord
        :type request: :class:`huaweicloudsdkdns.v2.UpdatePtrRecordRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdatePtrRecordResponse`
        """
        http_info = self._update_ptr_record_http_info(request)
        return self._call_api(**http_info)

    def update_ptr_record_async_invoker(self, request):
        http_info = self._update_ptr_record_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_ptr_record_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v2/reverse/floatingips/{region}:{floatingip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePtrRecordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'region' in local_var_params:
            path_params['region'] = local_var_params['region']
        if 'floatingip_id' in local_var_params:
            path_params['floatingip_id'] = local_var_params['floatingip_id']

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

    def update_record_set_async(self, request):
        r"""修改记录集

        当您的记录集创建成功后，您可以通过调用此接口修改记录集的信息，包括域名、类型、记录值、TTL、描述等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRecordSet
        :type request: :class:`huaweicloudsdkdns.v2.UpdateRecordSetRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdateRecordSetResponse`
        """
        http_info = self._update_record_set_http_info(request)
        return self._call_api(**http_info)

    def update_record_set_async_invoker(self, request):
        http_info = self._update_record_set_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_record_set_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/zones/{zone_id}/recordsets/{recordset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRecordSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']
        if 'recordset_id' in local_var_params:
            path_params['recordset_id'] = local_var_params['recordset_id']

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

    def create_ptr_async(self, request):
        r"""创建弹性公网IP的反向解析记录

        创建弹性公网IP的反向解析记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePtr
        :type request: :class:`huaweicloudsdkdns.v2.CreatePtrRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreatePtrResponse`
        """
        http_info = self._create_ptr_http_info(request)
        return self._call_api(**http_info)

    def create_ptr_async_invoker(self, request):
        http_info = self._create_ptr_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_ptr_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.1/ptrs",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePtrResponse"
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

    def create_record_set_with_line_async(self, request):
        r"""创建记录集

        记录集是指一组资源记录的集合，这些资源记录属于同一域名，用于定义域名支持的解析类型以及解析值。您的域名创建完成后，可以通过调用此接口为域名添加不同类型的记录集。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRecordSetWithLine
        :type request: :class:`huaweicloudsdkdns.v2.CreateRecordSetWithLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreateRecordSetWithLineResponse`
        """
        http_info = self._create_record_set_with_line_http_info(request)
        return self._call_api(**http_info)

    def create_record_set_with_line_async_invoker(self, request):
        http_info = self._create_record_set_with_line_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_record_set_with_line_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.1/zones/{zone_id}/recordsets",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRecordSetWithLineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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

    def delete_ptr_async(self, request):
        r"""将弹性公网IP的反向解析记录恢复为默认值

        将弹性公网IP的反向解析记录恢复为默认值。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePtr
        :type request: :class:`huaweicloudsdkdns.v2.DeletePtrRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeletePtrResponse`
        """
        http_info = self._delete_ptr_http_info(request)
        return self._call_api(**http_info)

    def delete_ptr_async_invoker(self, request):
        http_info = self._delete_ptr_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_ptr_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.1/ptrs/{ptr_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePtrResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ptr_id' in local_var_params:
            path_params['ptr_id'] = local_var_params['ptr_id']

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

    def delete_record_sets_async(self, request):
        r"""删除记录集

        当您的记录集不再使用时，您可以通过调用此接口将其删除。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRecordSets
        :type request: :class:`huaweicloudsdkdns.v2.DeleteRecordSetsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeleteRecordSetsResponse`
        """
        http_info = self._delete_record_sets_http_info(request)
        return self._call_api(**http_info)

    def delete_record_sets_async_invoker(self, request):
        http_info = self._delete_record_sets_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_record_sets_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.1/zones/{zone_id}/recordsets/{recordset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRecordSetsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']
        if 'recordset_id' in local_var_params:
            path_params['recordset_id'] = local_var_params['recordset_id']

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

    def list_ptrs_async(self, request):
        r"""查询弹性公网IP的反向解析记录列表

        查询弹性公网IP的反向解析记录列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPtrs
        :type request: :class:`huaweicloudsdkdns.v2.ListPtrsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListPtrsResponse`
        """
        http_info = self._list_ptrs_http_info(request)
        return self._call_api(**http_info)

    def list_ptrs_async_invoker(self, request):
        http_info = self._list_ptrs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ptrs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.1/ptrs",
            "request_type": request.__class__.__name__,
            "response_type": "ListPtrsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))

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

    def list_public_zone_lines_async(self, request):
        r"""查询公网域名的线路列表

        公网域名支持设置线路解析，当您的公网域名创建完成并添加记录集时，可通过调用此接口查询公网域名的所有解析线路。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPublicZoneLines
        :type request: :class:`huaweicloudsdkdns.v2.ListPublicZoneLinesRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListPublicZoneLinesResponse`
        """
        http_info = self._list_public_zone_lines_http_info(request)
        return self._call_api(**http_info)

    def list_public_zone_lines_async_invoker(self, request):
        http_info = self._list_public_zone_lines_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_public_zone_lines_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.1/zones/{zone_id}/lines",
            "request_type": request.__class__.__name__,
            "response_type": "ListPublicZoneLinesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

        query_params = []
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

    def list_record_sets_with_line_async(self, request):
        r"""查询租户记录集列表

        当您的记录集创建成功后，您可以通过调用此接口查询单个记录集信息，包括名称、ID、状态、所属域名、解析记录值、标签、TTL、创建时间、修改时间、描述等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRecordSetsWithLine
        :type request: :class:`huaweicloudsdkdns.v2.ListRecordSetsWithLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListRecordSetsWithLineResponse`
        """
        http_info = self._list_record_sets_with_line_http_info(request)
        return self._call_api(**http_info)

    def list_record_sets_with_line_async_invoker(self, request):
        http_info = self._list_record_sets_with_line_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_record_sets_with_line_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.1/recordsets",
            "request_type": request.__class__.__name__,
            "response_type": "ListRecordSetsWithLineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'zone_type' in local_var_params:
            query_params.append(('zone_type', local_var_params['zone_type']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'zone_id' in local_var_params:
            query_params.append(('zone_id', local_var_params['zone_id']))
        if 'line_id' in local_var_params:
            query_params.append(('line_id', local_var_params['line_id']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'records' in local_var_params:
            query_params.append(('records', local_var_params['records']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'health_check_id' in local_var_params:
            query_params.append(('health_check_id', local_var_params['health_check_id']))
        if 'search_mode' in local_var_params:
            query_params.append(('search_mode', local_var_params['search_mode']))

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

    def set_record_sets_status_async(self, request):
        r"""设置记录集状态

        当您的内网域名创建成功后，您可以通过调用此接口设置记录集的状态，包括暂停、启用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetRecordSetsStatus
        :type request: :class:`huaweicloudsdkdns.v2.SetRecordSetsStatusRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.SetRecordSetsStatusResponse`
        """
        http_info = self._set_record_sets_status_http_info(request)
        return self._call_api(**http_info)

    def set_record_sets_status_async_invoker(self, request):
        http_info = self._set_record_sets_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _set_record_sets_status_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.1/recordsets/{recordset_id}/statuses/set",
            "request_type": request.__class__.__name__,
            "response_type": "SetRecordSetsStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'recordset_id' in local_var_params:
            path_params['recordset_id'] = local_var_params['recordset_id']

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

    def show_ptr_async(self, request):
        r"""查询弹性公网IP的反向解析记录

        查询弹性公网IP的反向解析记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPtr
        :type request: :class:`huaweicloudsdkdns.v2.ShowPtrRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowPtrResponse`
        """
        http_info = self._show_ptr_http_info(request)
        return self._call_api(**http_info)

    def show_ptr_async_invoker(self, request):
        http_info = self._show_ptr_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ptr_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.1/ptrs/{ptr_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPtrResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ptr_id' in local_var_params:
            path_params['ptr_id'] = local_var_params['ptr_id']

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

    def show_record_set_by_zone_async(self, request):
        r"""查询域名下的记录集列表

        当您的记录集创建成功后，您可以通过调用此接口查询单个记录集信息，包括名称、ID、状态、所属域名、解析记录值、标签、TTL、创建时间、修改时间、描述等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRecordSetByZone
        :type request: :class:`huaweicloudsdkdns.v2.ShowRecordSetByZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowRecordSetByZoneResponse`
        """
        http_info = self._show_record_set_by_zone_http_info(request)
        return self._call_api(**http_info)

    def show_record_set_by_zone_async_invoker(self, request):
        http_info = self._show_record_set_by_zone_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_record_set_by_zone_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.1/zones/{zone_id}/recordsets",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRecordSetByZoneResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'line_id' in local_var_params:
            query_params.append(('line_id', local_var_params['line_id']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'search_mode' in local_var_params:
            query_params.append(('search_mode', local_var_params['search_mode']))

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

    def show_record_set_with_line_async(self, request):
        r"""查询记录集

        当您的记录集创建成功后，您可以通过调用此接口查询单个记录集信息，包括名称、ID、状态、所属域名、解析记录值、标签、TTL、创建时间、修改时间、描述等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRecordSetWithLine
        :type request: :class:`huaweicloudsdkdns.v2.ShowRecordSetWithLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowRecordSetWithLineResponse`
        """
        http_info = self._show_record_set_with_line_http_info(request)
        return self._call_api(**http_info)

    def show_record_set_with_line_async_invoker(self, request):
        http_info = self._show_record_set_with_line_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_record_set_with_line_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.1/zones/{zone_id}/recordsets/{recordset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRecordSetWithLineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']
        if 'recordset_id' in local_var_params:
            path_params['recordset_id'] = local_var_params['recordset_id']

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

    def update_ptr_async(self, request):
        r"""修改弹性公网IP的反向解析记录

        修改弹性公网IP的反向解析记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePtr
        :type request: :class:`huaweicloudsdkdns.v2.UpdatePtrRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdatePtrResponse`
        """
        http_info = self._update_ptr_http_info(request)
        return self._call_api(**http_info)

    def update_ptr_async_invoker(self, request):
        http_info = self._update_ptr_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_ptr_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.1/ptrs/{ptr_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePtrResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ptr_id' in local_var_params:
            path_params['ptr_id'] = local_var_params['ptr_id']

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

    def update_record_sets_async(self, request):
        r"""修改记录集

        当您的记录集创建成功后，您可以通过调用此接口修改记录集的信息，包括域名、类型、记录值、TTL、描述等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRecordSets
        :type request: :class:`huaweicloudsdkdns.v2.UpdateRecordSetsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdateRecordSetsResponse`
        """
        http_info = self._update_record_sets_http_info(request)
        return self._call_api(**http_info)

    def update_record_sets_async_invoker(self, request):
        http_info = self._update_record_sets_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_record_sets_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.1/zones/{zone_id}/recordsets/{recordset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRecordSetsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']
        if 'recordset_id' in local_var_params:
            path_params['recordset_id'] = local_var_params['recordset_id']

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
