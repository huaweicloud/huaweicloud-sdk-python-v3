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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdknat'")


class NatAsyncClient(Client):
    def __init__(self):
        super(NatAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdknat.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "NatAsyncClient":
                raise TypeError("client type error, support client type is NatAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_create_nat_gateway_dnat_rules_async(self, request):
        r"""批量创建DNAT规则

        批量创建DNAT规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateNatGatewayDnatRules
        :type request: :class:`huaweicloudsdknat.v2.BatchCreateNatGatewayDnatRulesRequest`
        :rtype: :class:`huaweicloudsdknat.v2.BatchCreateNatGatewayDnatRulesResponse`
        """
        http_info = self._batch_create_nat_gateway_dnat_rules_http_info(request)
        return self._call_api(**http_info)

    def batch_create_nat_gateway_dnat_rules_async_invoker(self, request):
        http_info = self._batch_create_nat_gateway_dnat_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_nat_gateway_dnat_rules_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/dnat_rules/batch",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateNatGatewayDnatRulesResponse"
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

    def create_nat_gateway_dnat_rule_async(self, request):
        r"""创建DNAT规则

        创建DNAT规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateNatGatewayDnatRule
        :type request: :class:`huaweicloudsdknat.v2.CreateNatGatewayDnatRuleRequest`
        :rtype: :class:`huaweicloudsdknat.v2.CreateNatGatewayDnatRuleResponse`
        """
        http_info = self._create_nat_gateway_dnat_rule_http_info(request)
        return self._call_api(**http_info)

    def create_nat_gateway_dnat_rule_async_invoker(self, request):
        http_info = self._create_nat_gateway_dnat_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_nat_gateway_dnat_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/dnat_rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateNatGatewayDnatRuleResponse"
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

    def create_private_dnat_async(self, request):
        r"""创建DNAT规则

        创建DNAT规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePrivateDnat
        :type request: :class:`huaweicloudsdknat.v2.CreatePrivateDnatRequest`
        :rtype: :class:`huaweicloudsdknat.v2.CreatePrivateDnatResponse`
        """
        http_info = self._create_private_dnat_http_info(request)
        return self._call_api(**http_info)

    def create_private_dnat_async_invoker(self, request):
        http_info = self._create_private_dnat_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_private_dnat_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/private-nat/dnat-rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePrivateDnatResponse"
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

    def delete_nat_gateway_dnat_rule_async(self, request):
        r"""删除DNAT规则

        删除指定的DNAT规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteNatGatewayDnatRule
        :type request: :class:`huaweicloudsdknat.v2.DeleteNatGatewayDnatRuleRequest`
        :rtype: :class:`huaweicloudsdknat.v2.DeleteNatGatewayDnatRuleResponse`
        """
        http_info = self._delete_nat_gateway_dnat_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_nat_gateway_dnat_rule_async_invoker(self, request):
        http_info = self._delete_nat_gateway_dnat_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_nat_gateway_dnat_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/nat_gateways/{nat_gateway_id}/dnat_rules/{dnat_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNatGatewayDnatRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'nat_gateway_id' in local_var_params:
            path_params['nat_gateway_id'] = local_var_params['nat_gateway_id']
        if 'dnat_rule_id' in local_var_params:
            path_params['dnat_rule_id'] = local_var_params['dnat_rule_id']

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

    def delete_private_dnat_async(self, request):
        r"""删除DNAT规则

        删除指定的DNAT规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePrivateDnat
        :type request: :class:`huaweicloudsdknat.v2.DeletePrivateDnatRequest`
        :rtype: :class:`huaweicloudsdknat.v2.DeletePrivateDnatResponse`
        """
        http_info = self._delete_private_dnat_http_info(request)
        return self._call_api(**http_info)

    def delete_private_dnat_async_invoker(self, request):
        http_info = self._delete_private_dnat_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_private_dnat_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/private-nat/dnat-rules/{dnat_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePrivateDnatResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dnat_rule_id' in local_var_params:
            path_params['dnat_rule_id'] = local_var_params['dnat_rule_id']

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

    def list_nat_gateway_dnat_rules_async(self, request):
        r"""查询DNAT规则列表

        查询DNAT规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNatGatewayDnatRules
        :type request: :class:`huaweicloudsdknat.v2.ListNatGatewayDnatRulesRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ListNatGatewayDnatRulesResponse`
        """
        http_info = self._list_nat_gateway_dnat_rules_http_info(request)
        return self._call_api(**http_info)

    def list_nat_gateway_dnat_rules_async_invoker(self, request):
        http_info = self._list_nat_gateway_dnat_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_nat_gateway_dnat_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/dnat_rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListNatGatewayDnatRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'external_service_port' in local_var_params:
            query_params.append(('external_service_port', local_var_params['external_service_port']))
        if 'floating_ip_address' in local_var_params:
            query_params.append(('floating_ip_address', local_var_params['floating_ip_address']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'csv'
        if 'floating_ip_id' in local_var_params:
            query_params.append(('floating_ip_id', local_var_params['floating_ip_id']))
        if 'internal_service_port' in local_var_params:
            query_params.append(('internal_service_port', local_var_params['internal_service_port']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'created_at' in local_var_params:
            query_params.append(('created_at', local_var_params['created_at']))
        if 'nat_gateway_id' in local_var_params:
            query_params.append(('nat_gateway_id', local_var_params['nat_gateway_id']))
            collection_formats['nat_gateway_id'] = 'csv'
        if 'port_id' in local_var_params:
            query_params.append(('port_id', local_var_params['port_id']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
            collection_formats['protocol'] = 'csv'
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

    def list_private_dnats_async(self, request):
        r"""查询DNAT规则列表

        查询DNAT规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPrivateDnats
        :type request: :class:`huaweicloudsdknat.v2.ListPrivateDnatsRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ListPrivateDnatsResponse`
        """
        http_info = self._list_private_dnats_http_info(request)
        return self._call_api(**http_info)

    def list_private_dnats_async_invoker(self, request):
        http_info = self._list_private_dnats_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_private_dnats_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/private-nat/dnat-rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListPrivateDnatsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'csv'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'csv'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'csv'
        if 'gateway_id' in local_var_params:
            query_params.append(('gateway_id', local_var_params['gateway_id']))
            collection_formats['gateway_id'] = 'csv'
        if 'transit_ip_id' in local_var_params:
            query_params.append(('transit_ip_id', local_var_params['transit_ip_id']))
            collection_formats['transit_ip_id'] = 'csv'
        if 'external_ip_address' in local_var_params:
            query_params.append(('external_ip_address', local_var_params['external_ip_address']))
            collection_formats['external_ip_address'] = 'csv'
        if 'network_interface_id' in local_var_params:
            query_params.append(('network_interface_id', local_var_params['network_interface_id']))
            collection_formats['network_interface_id'] = 'csv'
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'csv'
        if 'private_ip_address' in local_var_params:
            query_params.append(('private_ip_address', local_var_params['private_ip_address']))
            collection_formats['private_ip_address'] = 'csv'

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

    def show_nat_gateway_dnat_rule_async(self, request):
        r"""查询指定的DNAT规则详情

        查询指定的DNAT规则详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNatGatewayDnatRule
        :type request: :class:`huaweicloudsdknat.v2.ShowNatGatewayDnatRuleRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ShowNatGatewayDnatRuleResponse`
        """
        http_info = self._show_nat_gateway_dnat_rule_http_info(request)
        return self._call_api(**http_info)

    def show_nat_gateway_dnat_rule_async_invoker(self, request):
        http_info = self._show_nat_gateway_dnat_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_nat_gateway_dnat_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/dnat_rules/{dnat_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNatGatewayDnatRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dnat_rule_id' in local_var_params:
            path_params['dnat_rule_id'] = local_var_params['dnat_rule_id']

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

    def show_private_dnat_async(self, request):
        r"""查询指定的DNAT规则详情

        查询指定的DNAT规则详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPrivateDnat
        :type request: :class:`huaweicloudsdknat.v2.ShowPrivateDnatRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ShowPrivateDnatResponse`
        """
        http_info = self._show_private_dnat_http_info(request)
        return self._call_api(**http_info)

    def show_private_dnat_async_invoker(self, request):
        http_info = self._show_private_dnat_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_private_dnat_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/private-nat/dnat-rules/{dnat_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPrivateDnatResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dnat_rule_id' in local_var_params:
            path_params['dnat_rule_id'] = local_var_params['dnat_rule_id']

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

    def update_nat_gateway_dnat_rule_async(self, request):
        r"""更新DNAT规则

        更新指定的DNAT规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateNatGatewayDnatRule
        :type request: :class:`huaweicloudsdknat.v2.UpdateNatGatewayDnatRuleRequest`
        :rtype: :class:`huaweicloudsdknat.v2.UpdateNatGatewayDnatRuleResponse`
        """
        http_info = self._update_nat_gateway_dnat_rule_http_info(request)
        return self._call_api(**http_info)

    def update_nat_gateway_dnat_rule_async_invoker(self, request):
        http_info = self._update_nat_gateway_dnat_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_nat_gateway_dnat_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/dnat_rules/{dnat_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNatGatewayDnatRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dnat_rule_id' in local_var_params:
            path_params['dnat_rule_id'] = local_var_params['dnat_rule_id']

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

    def update_private_dnat_async(self, request):
        r"""更新DNAT规则

        更新指定的DNAT规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePrivateDnat
        :type request: :class:`huaweicloudsdknat.v2.UpdatePrivateDnatRequest`
        :rtype: :class:`huaweicloudsdknat.v2.UpdatePrivateDnatResponse`
        """
        http_info = self._update_private_dnat_http_info(request)
        return self._call_api(**http_info)

    def update_private_dnat_async_invoker(self, request):
        http_info = self._update_private_dnat_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_private_dnat_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/private-nat/dnat-rules/{dnat_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePrivateDnatResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dnat_rule_id' in local_var_params:
            path_params['dnat_rule_id'] = local_var_params['dnat_rule_id']

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

    def batch_create_delete_transit_ip_tags_async(self, request):
        r"""批量添加删除中转IP标签

        - 为指定中转IP实例批量添加或删除标签
        - 标签管理服务需要使用该接口批量管理中转IP实例的标签。
        - 一个中转IP上最多有10个标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateDeleteTransitIpTags
        :type request: :class:`huaweicloudsdknat.v2.BatchCreateDeleteTransitIpTagsRequest`
        :rtype: :class:`huaweicloudsdknat.v2.BatchCreateDeleteTransitIpTagsResponse`
        """
        http_info = self._batch_create_delete_transit_ip_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_delete_transit_ip_tags_async_invoker(self, request):
        http_info = self._batch_create_delete_transit_ip_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_delete_transit_ip_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/transit-ips/{resource_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateDeleteTransitIpTagsResponse"
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

    def create_transit_ip_tag_async(self, request):
        r"""添加中转IP标签

        - 一个中转IP上最多有10个标签。
        - 此接口为幂等接口：
        - 创建时，如果创建的标签已经存在（key相同），则覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTransitIpTag
        :type request: :class:`huaweicloudsdknat.v2.CreateTransitIpTagRequest`
        :rtype: :class:`huaweicloudsdknat.v2.CreateTransitIpTagResponse`
        """
        http_info = self._create_transit_ip_tag_http_info(request)
        return self._call_api(**http_info)

    def create_transit_ip_tag_async_invoker(self, request):
        http_info = self._create_transit_ip_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_transit_ip_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/transit-ips/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTransitIpTagResponse"
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

    def delete_transit_ip_tag_async(self, request):
        r"""删除中转IP标签

        - 幂等接口：
        - 删除时，不对标签字符集做校验，调用接口前必须要做encodeURI，服务端需要对接口uri做decodeURI。删除的key不存在报404，key不能为空或者空字符串。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTransitIpTag
        :type request: :class:`huaweicloudsdknat.v2.DeleteTransitIpTagRequest`
        :rtype: :class:`huaweicloudsdknat.v2.DeleteTransitIpTagResponse`
        """
        http_info = self._delete_transit_ip_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_transit_ip_tag_async_invoker(self, request):
        http_info = self._delete_transit_ip_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_transit_ip_tag_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/transit-ips/{resource_id}/tags/{key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTransitIpTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']
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

    def list_transit_ip_tags_async(self, request):
        r"""查询中转IP项目标签

        - 查询租户在指定Project和实例类型的所有中转IP标签集合。
        - 标签管理服务需要能够列出当前租户全部已使用的中转IP标签集合，为打中转IP标签和过滤中转IP实例时提供标签联想功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTransitIpTags
        :type request: :class:`huaweicloudsdknat.v2.ListTransitIpTagsRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ListTransitIpTagsResponse`
        """
        http_info = self._list_transit_ip_tags_http_info(request)
        return self._call_api(**http_info)

    def list_transit_ip_tags_async_invoker(self, request):
        http_info = self._list_transit_ip_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_transit_ip_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/transit-ips/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListTransitIpTagsResponse"
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

    def list_transit_ips_by_tags_async(self, request):
        r"""查询中转IP实例

        - 使用标签过滤中转IP实例。
        - 标签管理服务需要提供按标签过滤中转IP服务实例并汇总显示在列表中，需要中转IP服务提供查询能力。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTransitIpsByTags
        :type request: :class:`huaweicloudsdknat.v2.ListTransitIpsByTagsRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ListTransitIpsByTagsResponse`
        """
        http_info = self._list_transit_ips_by_tags_http_info(request)
        return self._call_api(**http_info)

    def list_transit_ips_by_tags_async_invoker(self, request):
        http_info = self._list_transit_ips_by_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_transit_ips_by_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/transit-ips/resource_instances/action",
            "request_type": request.__class__.__name__,
            "response_type": "ListTransitIpsByTagsResponse"
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

    def show_transit_ip_tags_async(self, request):
        r"""查询中转IP标签

        - 查询指定中转IP实例的标签信息。
        - 标签管理服务需要使用该接口查询指定中转IP实例的全部标签数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTransitIpTags
        :type request: :class:`huaweicloudsdknat.v2.ShowTransitIpTagsRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ShowTransitIpTagsResponse`
        """
        http_info = self._show_transit_ip_tags_http_info(request)
        return self._call_api(**http_info)

    def show_transit_ip_tags_async_invoker(self, request):
        http_info = self._show_transit_ip_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_transit_ip_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/transit-ips/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTransitIpTagsResponse"
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

    def batch_create_delete_nat_gateway_tag_async(self, request):
        r"""批量添加/删除公网NAT网关资源标签

        - 为指定公网NAT网关实例批量添加或删除标签。 
        - 标签管理服务需要使用该接口批量管理实例的标签。 
        - 一个资源上最多有10个标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateDeleteNatGatewayTag
        :type request: :class:`huaweicloudsdknat.v2.BatchCreateDeleteNatGatewayTagRequest`
        :rtype: :class:`huaweicloudsdknat.v2.BatchCreateDeleteNatGatewayTagResponse`
        """
        http_info = self._batch_create_delete_nat_gateway_tag_http_info(request)
        return self._call_api(**http_info)

    def batch_create_delete_nat_gateway_tag_async_invoker(self, request):
        http_info = self._batch_create_delete_nat_gateway_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_delete_nat_gateway_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/nat_gateways/{nat_gateway_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateDeleteNatGatewayTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'nat_gateway_id' in local_var_params:
            path_params['nat_gateway_id'] = local_var_params['nat_gateway_id']

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

    def batch_create_delete_private_nat_tags_async(self, request):
        r"""批量添加删除私网NAT网关标签

        - 为指定私网NAT网关实例批量添加或删除标签
        - 标签管理服务需要使用该接口批量管理私网NAT网关实例的标签。
        - 一个私网NAT网关上最多有10个标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateDeletePrivateNatTags
        :type request: :class:`huaweicloudsdknat.v2.BatchCreateDeletePrivateNatTagsRequest`
        :rtype: :class:`huaweicloudsdknat.v2.BatchCreateDeletePrivateNatTagsResponse`
        """
        http_info = self._batch_create_delete_private_nat_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_delete_private_nat_tags_async_invoker(self, request):
        http_info = self._batch_create_delete_private_nat_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_delete_private_nat_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/private-nat-gateways/{resource_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateDeletePrivateNatTagsResponse"
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

    def create_nat_gateway_async(self, request):
        r"""创建公网NAT网关

        创建公网NAT网关实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateNatGateway
        :type request: :class:`huaweicloudsdknat.v2.CreateNatGatewayRequest`
        :rtype: :class:`huaweicloudsdknat.v2.CreateNatGatewayResponse`
        """
        http_info = self._create_nat_gateway_http_info(request)
        return self._call_api(**http_info)

    def create_nat_gateway_async_invoker(self, request):
        http_info = self._create_nat_gateway_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_nat_gateway_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/nat_gateways",
            "request_type": request.__class__.__name__,
            "response_type": "CreateNatGatewayResponse"
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

    def create_nat_gateway_tag_async(self, request):
        r"""添加公网NAT网关资源标签

        - 添加公网NAT网关资源标签。一个资源上最多有10个标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateNatGatewayTag
        :type request: :class:`huaweicloudsdknat.v2.CreateNatGatewayTagRequest`
        :rtype: :class:`huaweicloudsdknat.v2.CreateNatGatewayTagResponse`
        """
        http_info = self._create_nat_gateway_tag_http_info(request)
        return self._call_api(**http_info)

    def create_nat_gateway_tag_async_invoker(self, request):
        http_info = self._create_nat_gateway_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_nat_gateway_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/nat_gateways/{nat_gateway_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreateNatGatewayTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'nat_gateway_id' in local_var_params:
            path_params['nat_gateway_id'] = local_var_params['nat_gateway_id']

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

    def create_private_nat_async(self, request):
        r"""创建私网NAT网关

        创建私网NAT网关实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePrivateNat
        :type request: :class:`huaweicloudsdknat.v2.CreatePrivateNatRequest`
        :rtype: :class:`huaweicloudsdknat.v2.CreatePrivateNatResponse`
        """
        http_info = self._create_private_nat_http_info(request)
        return self._call_api(**http_info)

    def create_private_nat_async_invoker(self, request):
        http_info = self._create_private_nat_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_private_nat_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/private-nat/gateways",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePrivateNatResponse"
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

    def create_private_nat_tag_async(self, request):
        r"""添加私网NAT网关标签

        - 一个私网NAT网关上最多有10个标签。
        - 此接口为幂等接口：
        - 创建时，如果创建的标签已经存在（key相同），则覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePrivateNatTag
        :type request: :class:`huaweicloudsdknat.v2.CreatePrivateNatTagRequest`
        :rtype: :class:`huaweicloudsdknat.v2.CreatePrivateNatTagResponse`
        """
        http_info = self._create_private_nat_tag_http_info(request)
        return self._call_api(**http_info)

    def create_private_nat_tag_async_invoker(self, request):
        http_info = self._create_private_nat_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_private_nat_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/private-nat-gateways/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePrivateNatTagResponse"
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

    def delete_nat_gateway_async(self, request):
        r"""删除公网NAT网关

        删除公网NAT网关实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteNatGateway
        :type request: :class:`huaweicloudsdknat.v2.DeleteNatGatewayRequest`
        :rtype: :class:`huaweicloudsdknat.v2.DeleteNatGatewayResponse`
        """
        http_info = self._delete_nat_gateway_http_info(request)
        return self._call_api(**http_info)

    def delete_nat_gateway_async_invoker(self, request):
        http_info = self._delete_nat_gateway_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_nat_gateway_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/nat_gateways/{nat_gateway_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNatGatewayResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'nat_gateway_id' in local_var_params:
            path_params['nat_gateway_id'] = local_var_params['nat_gateway_id']

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

    def delete_nat_gateway_tag_async(self, request):
        r"""删除公网NAT网关资源标签

        - 删除指定公网NAT网关资源实例的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteNatGatewayTag
        :type request: :class:`huaweicloudsdknat.v2.DeleteNatGatewayTagRequest`
        :rtype: :class:`huaweicloudsdknat.v2.DeleteNatGatewayTagResponse`
        """
        http_info = self._delete_nat_gateway_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_nat_gateway_tag_async_invoker(self, request):
        http_info = self._delete_nat_gateway_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_nat_gateway_tag_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/nat_gateways/{nat_gateway_id}/tags/{key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNatGatewayTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'nat_gateway_id' in local_var_params:
            path_params['nat_gateway_id'] = local_var_params['nat_gateway_id']
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

    def delete_private_nat_async(self, request):
        r"""删除私网NAT网关

        删除私网NAT网关实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePrivateNat
        :type request: :class:`huaweicloudsdknat.v2.DeletePrivateNatRequest`
        :rtype: :class:`huaweicloudsdknat.v2.DeletePrivateNatResponse`
        """
        http_info = self._delete_private_nat_http_info(request)
        return self._call_api(**http_info)

    def delete_private_nat_async_invoker(self, request):
        http_info = self._delete_private_nat_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_private_nat_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/private-nat/gateways/{gateway_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePrivateNatResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']

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

    def delete_private_nat_tag_async(self, request):
        r"""删除私网NAT网关标签

        - 幂等接口：
        - 删除时，不对标签字符集做校验，调用接口前必须要做encodeURI，服务端需要对接口uri做decodeURI。删除的key不存在报404，key不能为空或者空字符串。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePrivateNatTag
        :type request: :class:`huaweicloudsdknat.v2.DeletePrivateNatTagRequest`
        :rtype: :class:`huaweicloudsdknat.v2.DeletePrivateNatTagResponse`
        """
        http_info = self._delete_private_nat_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_private_nat_tag_async_invoker(self, request):
        http_info = self._delete_private_nat_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_private_nat_tag_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/private-nat-gateways/{resource_id}/tags/{key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePrivateNatTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']
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

    def list_nat_gateway_by_tag_async(self, request):
        r"""查询公网NAT网关资源实例

        - 使用标签过滤公网NAT网关资源实例。
        - 标签管理服务需要提供按标签过滤公网NAT网关服务实例并汇总显示在列表中，需要公网NAT网关服务提供查询能力。
        - 资源默认按照创建时间倒序，资源tag也按照创建时间倒序。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNatGatewayByTag
        :type request: :class:`huaweicloudsdknat.v2.ListNatGatewayByTagRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ListNatGatewayByTagResponse`
        """
        http_info = self._list_nat_gateway_by_tag_http_info(request)
        return self._call_api(**http_info)

    def list_nat_gateway_by_tag_async_invoker(self, request):
        http_info = self._list_nat_gateway_by_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_nat_gateway_by_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/nat_gateways/resource_instances/action",
            "request_type": request.__class__.__name__,
            "response_type": "ListNatGatewayByTagResponse"
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

    def list_nat_gateway_tag_async(self, request):
        r"""查询公网NAT网关项目标签

        - 查询租户在指定项目和公网NAT网关实例类型的所有标签集合。
        - 标签管理服务需要能够列出当前租户全部已使用的标签集合，为各服务Console打标签和过滤实例时提供标签联想功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNatGatewayTag
        :type request: :class:`huaweicloudsdknat.v2.ListNatGatewayTagRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ListNatGatewayTagResponse`
        """
        http_info = self._list_nat_gateway_tag_http_info(request)
        return self._call_api(**http_info)

    def list_nat_gateway_tag_async_invoker(self, request):
        http_info = self._list_nat_gateway_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_nat_gateway_tag_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/nat_gateways/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListNatGatewayTagResponse"
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

    def list_nat_gateways_async(self, request):
        r"""查询公网NAT网关列表

        查询公网NAT网关实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNatGateways
        :type request: :class:`huaweicloudsdknat.v2.ListNatGatewaysRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ListNatGatewaysResponse`
        """
        http_info = self._list_nat_gateways_http_info(request)
        return self._call_api(**http_info)

    def list_nat_gateways_async_invoker(self, request):
        http_info = self._list_nat_gateways_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_nat_gateways_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/nat_gateways",
            "request_type": request.__class__.__name__,
            "response_type": "ListNatGatewaysResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'created_at' in local_var_params:
            query_params.append(('created_at', local_var_params['created_at']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'csv'
        if 'spec' in local_var_params:
            query_params.append(('spec', local_var_params['spec']))
            collection_formats['spec'] = 'csv'
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'internal_network_id' in local_var_params:
            query_params.append(('internal_network_id', local_var_params['internal_network_id']))
        if 'router_id' in local_var_params:
            query_params.append(('router_id', local_var_params['router_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
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

    def list_private_nat_tags_async(self, request):
        r"""查询私网NAT网关项目标签

        - 查询租户在指定Project和实例类型的所有私网NAT网关标签集合。
        - 标签管理服务需要能够列出当前租户全部已使用的私网NAT网关标签集合，为打私网NAT网关标签和过滤私网NAT网关实例时提供标签联想功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPrivateNatTags
        :type request: :class:`huaweicloudsdknat.v2.ListPrivateNatTagsRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ListPrivateNatTagsResponse`
        """
        http_info = self._list_private_nat_tags_http_info(request)
        return self._call_api(**http_info)

    def list_private_nat_tags_async_invoker(self, request):
        http_info = self._list_private_nat_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_private_nat_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/private-nat-gateways/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListPrivateNatTagsResponse"
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

    def list_private_nats_async(self, request):
        r"""查询私网NAT网关列表

        查询私网NAT网关实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPrivateNats
        :type request: :class:`huaweicloudsdknat.v2.ListPrivateNatsRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ListPrivateNatsResponse`
        """
        http_info = self._list_private_nats_http_info(request)
        return self._call_api(**http_info)

    def list_private_nats_async_invoker(self, request):
        http_info = self._list_private_nats_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_private_nats_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/private-nat/gateways",
            "request_type": request.__class__.__name__,
            "response_type": "ListPrivateNatsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'csv'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'csv'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'csv'
        if 'spec' in local_var_params:
            query_params.append(('spec', local_var_params['spec']))
            collection_formats['spec'] = 'csv'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'csv'
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
            collection_formats['vpc_id'] = 'csv'
        if 'virsubnet_id' in local_var_params:
            query_params.append(('virsubnet_id', local_var_params['virsubnet_id']))
            collection_formats['virsubnet_id'] = 'csv'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'csv'

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

    def list_private_nats_by_tags_async(self, request):
        r"""查询私网NAT网关实例

        - 使用标签过滤私网NAT网关实例。
        - 标签管理服务需要提供按标签过滤私网NAT网关服务实例并汇总显示在列表中，需要私网NAT网关服务提供查询能力。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPrivateNatsByTags
        :type request: :class:`huaweicloudsdknat.v2.ListPrivateNatsByTagsRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ListPrivateNatsByTagsResponse`
        """
        http_info = self._list_private_nats_by_tags_http_info(request)
        return self._call_api(**http_info)

    def list_private_nats_by_tags_async_invoker(self, request):
        http_info = self._list_private_nats_by_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_private_nats_by_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/private-nat-gateways/resource_instances/action",
            "request_type": request.__class__.__name__,
            "response_type": "ListPrivateNatsByTagsResponse"
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

    def show_nat_gateway_async(self, request):
        r"""查询指定的公网NAT网关详情

        查询指定的公网NAT网关实例详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNatGateway
        :type request: :class:`huaweicloudsdknat.v2.ShowNatGatewayRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ShowNatGatewayResponse`
        """
        http_info = self._show_nat_gateway_http_info(request)
        return self._call_api(**http_info)

    def show_nat_gateway_async_invoker(self, request):
        http_info = self._show_nat_gateway_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_nat_gateway_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/nat_gateways/{nat_gateway_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNatGatewayResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'nat_gateway_id' in local_var_params:
            path_params['nat_gateway_id'] = local_var_params['nat_gateway_id']

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

    def show_nat_gateway_tag_async(self, request):
        r"""查询公网NAT网关资源标签

        - 查询指定公网NAT网关实例的标签信息。
        - 标签管理服务需要使用该接口查询指定公网NAT网关实例的全部标签数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNatGatewayTag
        :type request: :class:`huaweicloudsdknat.v2.ShowNatGatewayTagRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ShowNatGatewayTagResponse`
        """
        http_info = self._show_nat_gateway_tag_http_info(request)
        return self._call_api(**http_info)

    def show_nat_gateway_tag_async_invoker(self, request):
        http_info = self._show_nat_gateway_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_nat_gateway_tag_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/nat_gateways/{nat_gateway_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNatGatewayTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'nat_gateway_id' in local_var_params:
            path_params['nat_gateway_id'] = local_var_params['nat_gateway_id']

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

    def show_private_nat_async(self, request):
        r"""查询指定的私网NAT网关详情

        查询指定的私网NAT网关实例详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPrivateNat
        :type request: :class:`huaweicloudsdknat.v2.ShowPrivateNatRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ShowPrivateNatResponse`
        """
        http_info = self._show_private_nat_http_info(request)
        return self._call_api(**http_info)

    def show_private_nat_async_invoker(self, request):
        http_info = self._show_private_nat_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_private_nat_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/private-nat/gateways/{gateway_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPrivateNatResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']

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

    def show_private_nat_tags_async(self, request):
        r"""查询私网NAT网关标签

        - 查询指定私网NAT网关实例的标签信息。
        - 标签管理服务需要使用该接口查询指定私网NAT网关实例的全部标签数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPrivateNatTags
        :type request: :class:`huaweicloudsdknat.v2.ShowPrivateNatTagsRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ShowPrivateNatTagsResponse`
        """
        http_info = self._show_private_nat_tags_http_info(request)
        return self._call_api(**http_info)

    def show_private_nat_tags_async_invoker(self, request):
        http_info = self._show_private_nat_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_private_nat_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/private-nat-gateways/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPrivateNatTagsResponse"
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

    def update_nat_gateway_async(self, request):
        r"""更新公网NAT网关

        更新公网NAT网关实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateNatGateway
        :type request: :class:`huaweicloudsdknat.v2.UpdateNatGatewayRequest`
        :rtype: :class:`huaweicloudsdknat.v2.UpdateNatGatewayResponse`
        """
        http_info = self._update_nat_gateway_http_info(request)
        return self._call_api(**http_info)

    def update_nat_gateway_async_invoker(self, request):
        http_info = self._update_nat_gateway_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_nat_gateway_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/nat_gateways/{nat_gateway_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNatGatewayResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'nat_gateway_id' in local_var_params:
            path_params['nat_gateway_id'] = local_var_params['nat_gateway_id']

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

    def update_private_nat_async(self, request):
        r"""更新私网NAT网关

        更新私网NAT网关实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePrivateNat
        :type request: :class:`huaweicloudsdknat.v2.UpdatePrivateNatRequest`
        :rtype: :class:`huaweicloudsdknat.v2.UpdatePrivateNatResponse`
        """
        http_info = self._update_private_nat_http_info(request)
        return self._call_api(**http_info)

    def update_private_nat_async_invoker(self, request):
        http_info = self._update_private_nat_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_private_nat_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/private-nat/gateways/{gateway_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePrivateNatResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']

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

    def create_transit_ip_async(self, request):
        r"""创建中转IP

        创建中转IP。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTransitIp
        :type request: :class:`huaweicloudsdknat.v2.CreateTransitIpRequest`
        :rtype: :class:`huaweicloudsdknat.v2.CreateTransitIpResponse`
        """
        http_info = self._create_transit_ip_http_info(request)
        return self._call_api(**http_info)

    def create_transit_ip_async_invoker(self, request):
        http_info = self._create_transit_ip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_transit_ip_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/private-nat/transit-ips",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTransitIpResponse"
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

    def delete_transit_ip_async(self, request):
        r"""删除中转IP

        删除中转IP。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTransitIp
        :type request: :class:`huaweicloudsdknat.v2.DeleteTransitIpRequest`
        :rtype: :class:`huaweicloudsdknat.v2.DeleteTransitIpResponse`
        """
        http_info = self._delete_transit_ip_http_info(request)
        return self._call_api(**http_info)

    def delete_transit_ip_async_invoker(self, request):
        http_info = self._delete_transit_ip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_transit_ip_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/private-nat/transit-ips/{transit_ip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTransitIpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'transit_ip_id' in local_var_params:
            path_params['transit_ip_id'] = local_var_params['transit_ip_id']

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

    def list_transit_ips_async(self, request):
        r"""查询中转IP列表

        查询中转IP列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTransitIps
        :type request: :class:`huaweicloudsdknat.v2.ListTransitIpsRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ListTransitIpsResponse`
        """
        http_info = self._list_transit_ips_http_info(request)
        return self._call_api(**http_info)

    def list_transit_ips_async_invoker(self, request):
        http_info = self._list_transit_ips_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_transit_ips_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/private-nat/transit-ips",
            "request_type": request.__class__.__name__,
            "response_type": "ListTransitIpsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'csv'
        if 'network_interface_id' in local_var_params:
            query_params.append(('network_interface_id', local_var_params['network_interface_id']))
            collection_formats['network_interface_id'] = 'csv'
        if 'ip_address' in local_var_params:
            query_params.append(('ip_address', local_var_params['ip_address']))
            collection_formats['ip_address'] = 'csv'
        if 'gateway_id' in local_var_params:
            query_params.append(('gateway_id', local_var_params['gateway_id']))
            collection_formats['gateway_id'] = 'csv'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'csv'
        if 'virsubnet_id' in local_var_params:
            query_params.append(('virsubnet_id', local_var_params['virsubnet_id']))
            collection_formats['virsubnet_id'] = 'csv'

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

    def show_transit_ip_async(self, request):
        r"""查询指定的中转IP详情

        查询中转IP详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTransitIp
        :type request: :class:`huaweicloudsdknat.v2.ShowTransitIpRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ShowTransitIpResponse`
        """
        http_info = self._show_transit_ip_http_info(request)
        return self._call_api(**http_info)

    def show_transit_ip_async_invoker(self, request):
        http_info = self._show_transit_ip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_transit_ip_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/private-nat/transit-ips/{transit_ip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTransitIpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'transit_ip_id' in local_var_params:
            path_params['transit_ip_id'] = local_var_params['transit_ip_id']

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

    def create_nat_gateway_snat_rule_async(self, request):
        r"""创建SNAT规则

        创建SNAT规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateNatGatewaySnatRule
        :type request: :class:`huaweicloudsdknat.v2.CreateNatGatewaySnatRuleRequest`
        :rtype: :class:`huaweicloudsdknat.v2.CreateNatGatewaySnatRuleResponse`
        """
        http_info = self._create_nat_gateway_snat_rule_http_info(request)
        return self._call_api(**http_info)

    def create_nat_gateway_snat_rule_async_invoker(self, request):
        http_info = self._create_nat_gateway_snat_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_nat_gateway_snat_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/snat_rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateNatGatewaySnatRuleResponse"
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

    def create_private_snat_async(self, request):
        r"""创建SNAT规则

        创建SNAT规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePrivateSnat
        :type request: :class:`huaweicloudsdknat.v2.CreatePrivateSnatRequest`
        :rtype: :class:`huaweicloudsdknat.v2.CreatePrivateSnatResponse`
        """
        http_info = self._create_private_snat_http_info(request)
        return self._call_api(**http_info)

    def create_private_snat_async_invoker(self, request):
        http_info = self._create_private_snat_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_private_snat_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/private-nat/snat-rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePrivateSnatResponse"
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

    def delete_nat_gateway_snat_rule_async(self, request):
        r"""删除SNAT规则

        删除指定的SNAT规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteNatGatewaySnatRule
        :type request: :class:`huaweicloudsdknat.v2.DeleteNatGatewaySnatRuleRequest`
        :rtype: :class:`huaweicloudsdknat.v2.DeleteNatGatewaySnatRuleResponse`
        """
        http_info = self._delete_nat_gateway_snat_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_nat_gateway_snat_rule_async_invoker(self, request):
        http_info = self._delete_nat_gateway_snat_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_nat_gateway_snat_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/nat_gateways/{nat_gateway_id}/snat_rules/{snat_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNatGatewaySnatRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'nat_gateway_id' in local_var_params:
            path_params['nat_gateway_id'] = local_var_params['nat_gateway_id']
        if 'snat_rule_id' in local_var_params:
            path_params['snat_rule_id'] = local_var_params['snat_rule_id']

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

    def delete_private_snat_async(self, request):
        r"""删除SNAT规则

        删除指定的SNAT规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePrivateSnat
        :type request: :class:`huaweicloudsdknat.v2.DeletePrivateSnatRequest`
        :rtype: :class:`huaweicloudsdknat.v2.DeletePrivateSnatResponse`
        """
        http_info = self._delete_private_snat_http_info(request)
        return self._call_api(**http_info)

    def delete_private_snat_async_invoker(self, request):
        http_info = self._delete_private_snat_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_private_snat_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/private-nat/snat-rules/{snat_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePrivateSnatResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'snat_rule_id' in local_var_params:
            path_params['snat_rule_id'] = local_var_params['snat_rule_id']

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

    def list_nat_gateway_snat_rules_async(self, request):
        r"""查询SNAT规则列表

        查询SNAT规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNatGatewaySnatRules
        :type request: :class:`huaweicloudsdknat.v2.ListNatGatewaySnatRulesRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ListNatGatewaySnatRulesResponse`
        """
        http_info = self._list_nat_gateway_snat_rules_http_info(request)
        return self._call_api(**http_info)

    def list_nat_gateway_snat_rules_async_invoker(self, request):
        http_info = self._list_nat_gateway_snat_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_nat_gateway_snat_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/snat_rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListNatGatewaySnatRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'cidr' in local_var_params:
            query_params.append(('cidr', local_var_params['cidr']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'floating_ip_address' in local_var_params:
            query_params.append(('floating_ip_address', local_var_params['floating_ip_address']))
            collection_formats['floating_ip_address'] = 'csv'
        if 'floating_ip_id' in local_var_params:
            query_params.append(('floating_ip_id', local_var_params['floating_ip_id']))
            collection_formats['floating_ip_id'] = 'csv'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'created_at' in local_var_params:
            query_params.append(('created_at', local_var_params['created_at']))
        if 'nat_gateway_id' in local_var_params:
            query_params.append(('nat_gateway_id', local_var_params['nat_gateway_id']))
            collection_formats['nat_gateway_id'] = 'csv'
        if 'network_id' in local_var_params:
            query_params.append(('network_id', local_var_params['network_id']))
        if 'source_type' in local_var_params:
            query_params.append(('source_type', local_var_params['source_type']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
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

    def list_private_snats_async(self, request):
        r"""查询SNAT规则列表

        查询SNAT规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPrivateSnats
        :type request: :class:`huaweicloudsdknat.v2.ListPrivateSnatsRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ListPrivateSnatsResponse`
        """
        http_info = self._list_private_snats_http_info(request)
        return self._call_api(**http_info)

    def list_private_snats_async_invoker(self, request):
        http_info = self._list_private_snats_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_private_snats_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/private-nat/snat-rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListPrivateSnatsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'csv'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'csv'
        if 'gateway_id' in local_var_params:
            query_params.append(('gateway_id', local_var_params['gateway_id']))
            collection_formats['gateway_id'] = 'csv'
        if 'cidr' in local_var_params:
            query_params.append(('cidr', local_var_params['cidr']))
            collection_formats['cidr'] = 'csv'
        if 'virsubnet_id' in local_var_params:
            query_params.append(('virsubnet_id', local_var_params['virsubnet_id']))
            collection_formats['virsubnet_id'] = 'csv'
        if 'transit_ip_id' in local_var_params:
            query_params.append(('transit_ip_id', local_var_params['transit_ip_id']))
            collection_formats['transit_ip_id'] = 'csv'
        if 'transit_ip_address' in local_var_params:
            query_params.append(('transit_ip_address', local_var_params['transit_ip_address']))
            collection_formats['transit_ip_address'] = 'csv'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'csv'

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

    def show_nat_gateway_snat_rule_async(self, request):
        r"""查询指定的SNAT规则详情

        查询指定的SNAT规则详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNatGatewaySnatRule
        :type request: :class:`huaweicloudsdknat.v2.ShowNatGatewaySnatRuleRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ShowNatGatewaySnatRuleResponse`
        """
        http_info = self._show_nat_gateway_snat_rule_http_info(request)
        return self._call_api(**http_info)

    def show_nat_gateway_snat_rule_async_invoker(self, request):
        http_info = self._show_nat_gateway_snat_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_nat_gateway_snat_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/snat_rules/{snat_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNatGatewaySnatRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'snat_rule_id' in local_var_params:
            path_params['snat_rule_id'] = local_var_params['snat_rule_id']

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

    def show_private_snat_async(self, request):
        r"""查询指定的SNAT规则详情

        查询指定的SNAT规则详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPrivateSnat
        :type request: :class:`huaweicloudsdknat.v2.ShowPrivateSnatRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ShowPrivateSnatResponse`
        """
        http_info = self._show_private_snat_http_info(request)
        return self._call_api(**http_info)

    def show_private_snat_async_invoker(self, request):
        http_info = self._show_private_snat_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_private_snat_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/private-nat/snat-rules/{snat_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPrivateSnatResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'snat_rule_id' in local_var_params:
            path_params['snat_rule_id'] = local_var_params['snat_rule_id']

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

    def update_nat_gateway_snat_rule_async(self, request):
        r"""更新SNAT规则

        更新指定的SNAT规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateNatGatewaySnatRule
        :type request: :class:`huaweicloudsdknat.v2.UpdateNatGatewaySnatRuleRequest`
        :rtype: :class:`huaweicloudsdknat.v2.UpdateNatGatewaySnatRuleResponse`
        """
        http_info = self._update_nat_gateway_snat_rule_http_info(request)
        return self._call_api(**http_info)

    def update_nat_gateway_snat_rule_async_invoker(self, request):
        http_info = self._update_nat_gateway_snat_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_nat_gateway_snat_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/snat_rules/{snat_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNatGatewaySnatRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'snat_rule_id' in local_var_params:
            path_params['snat_rule_id'] = local_var_params['snat_rule_id']

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

    def update_private_snat_async(self, request):
        r"""更新SNAT规则

        更新指定的SNAT规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePrivateSnat
        :type request: :class:`huaweicloudsdknat.v2.UpdatePrivateSnatRequest`
        :rtype: :class:`huaweicloudsdknat.v2.UpdatePrivateSnatResponse`
        """
        http_info = self._update_private_snat_http_info(request)
        return self._call_api(**http_info)

    def update_private_snat_async_invoker(self, request):
        http_info = self._update_private_snat_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_private_snat_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/private-nat/snat-rules/{snat_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePrivateSnatResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'snat_rule_id' in local_var_params:
            path_params['snat_rule_id'] = local_var_params['snat_rule_id']

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
