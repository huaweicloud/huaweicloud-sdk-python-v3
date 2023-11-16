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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkvpc'")


class VpcClient(Client):
    def __init__(self):
        super(VpcClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkvpc.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "VpcClient":
                raise TypeError("client type error, support client type is VpcClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def accept_vpc_peering(self, request):
        """接受对等连接请求

        租户A名下的VPC申请和租户B的VPC建立对等连接，需要等待租户B接受该请求。此接口用于租户接受其他租户发起的对等连接请求。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AcceptVpcPeering
        :type request: :class:`huaweicloudsdkvpc.v2.AcceptVpcPeeringRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.AcceptVpcPeeringResponse`
        """
        http_info = self._accept_vpc_peering_http_info(request)
        return self._call_api(**http_info)

    def accept_vpc_peering_invoker(self, request):
        http_info = self._accept_vpc_peering_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _accept_vpc_peering_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.0/vpc/peerings/{peering_id}/accept",
            "request_type": request.__class__.__name__,
            "response_type": "AcceptVpcPeeringResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'peering_id' in local_var_params:
            path_params['peering_id'] = local_var_params['peering_id']

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

    def associate_route_table(self, request):
        """子网关联路由表

        路由表关联子网。子网关联路由表A后，再关联B，不需要先跟路由表A解关联再关联路由表B
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateRouteTable
        :type request: :class:`huaweicloudsdkvpc.v2.AssociateRouteTableRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.AssociateRouteTableResponse`
        """
        http_info = self._associate_route_table_http_info(request)
        return self._call_api(**http_info)

    def associate_route_table_invoker(self, request):
        http_info = self._associate_route_table_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _associate_route_table_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/routetables/{routetable_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateRouteTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_create_subnet_tags(self, request):
        """批量创建子网资源标签

        为指定的子网资源实例批量添加标签。
        此接口为幂等接口：创建时如果请求体中存在重复key则报错。创建时，不允许设置重复key数据，如果数据库已存在该key，就覆盖value的值。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateSubnetTags
        :type request: :class:`huaweicloudsdkvpc.v2.BatchCreateSubnetTagsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.BatchCreateSubnetTagsResponse`
        """
        http_info = self._batch_create_subnet_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_subnet_tags_invoker(self, request):
        http_info = self._batch_create_subnet_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_subnet_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/subnets/{subnet_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateSubnetTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_subnet_tags(self, request):
        """批量删除子网资源标签

        为指定的子网资源实例批量删除标签
        此接口为幂等接口：删除时，如果删除的标签不存在，默认处理成功；删除时不对标签字符集范围做校验。删除时tags结构体不能缺失，key不能为空，或者空字符串。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteSubnetTags
        :type request: :class:`huaweicloudsdkvpc.v2.BatchDeleteSubnetTagsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.BatchDeleteSubnetTagsResponse`
        """
        http_info = self._batch_delete_subnet_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_subnet_tags_invoker(self, request):
        http_info = self._batch_delete_subnet_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_subnet_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/subnets/{subnet_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteSubnetTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_flow_log(self, request):
        """创建流日志

        创建流日志。
        流日志功能可以记录虚拟私有云中的流量信息，帮助您检查和优化安全组和网络ACL防火墙控制规则、监控网络流量、进行网络攻击分析等。
        VPC流日志功能需要与云日志服务LTS结合使用，请先在云日志服务中创建日志组和日志主题，然后再创建VPC流日志。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFlowLog
        :type request: :class:`huaweicloudsdkvpc.v2.CreateFlowLogRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.CreateFlowLogResponse`
        """
        http_info = self._create_flow_log_http_info(request)
        return self._call_api(**http_info)

    def create_flow_log_invoker(self, request):
        http_info = self._create_flow_log_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_flow_log_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/fl/flow_logs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFlowLogResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_port(self, request):
        """创建端口

        创建端口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePort
        :type request: :class:`huaweicloudsdkvpc.v2.CreatePortRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.CreatePortResponse`
        """
        http_info = self._create_port_http_info(request)
        return self._call_api(**http_info)

    def create_port_invoker(self, request):
        http_info = self._create_port_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_port_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/ports",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePortResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_route_table(self, request):
        """创建路由表

        创建路由表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRouteTable
        :type request: :class:`huaweicloudsdkvpc.v2.CreateRouteTableRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.CreateRouteTableResponse`
        """
        http_info = self._create_route_table_http_info(request)
        return self._call_api(**http_info)

    def create_route_table_invoker(self, request):
        http_info = self._create_route_table_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_route_table_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/routetables",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRouteTableResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_security_group(self, request):
        """创建安全组

        创建安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSecurityGroup
        :type request: :class:`huaweicloudsdkvpc.v2.CreateSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.CreateSecurityGroupResponse`
        """
        http_info = self._create_security_group_http_info(request)
        return self._call_api(**http_info)

    def create_security_group_invoker(self, request):
        http_info = self._create_security_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_security_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/security-groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSecurityGroupResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_security_group_rule(self, request):
        """创建安全组规则

        创建安全组规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSecurityGroupRule
        :type request: :class:`huaweicloudsdkvpc.v2.CreateSecurityGroupRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.CreateSecurityGroupRuleResponse`
        """
        http_info = self._create_security_group_rule_http_info(request)
        return self._call_api(**http_info)

    def create_security_group_rule_invoker(self, request):
        http_info = self._create_security_group_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_security_group_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/security-group-rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSecurityGroupRuleResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_subnet(self, request):
        """创建子网

        创建子网。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSubnet
        :type request: :class:`huaweicloudsdkvpc.v2.CreateSubnetRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.CreateSubnetResponse`
        """
        http_info = self._create_subnet_http_info(request)
        return self._call_api(**http_info)

    def create_subnet_invoker(self, request):
        http_info = self._create_subnet_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_subnet_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/subnets",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSubnetResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_subnet_tag(self, request):
        """创建子网资源标签

        给指定子网资源实例增加标签信息。
        此接口为幂等接口：创建时，如果创建的标签已经存在（key相同），则覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSubnetTag
        :type request: :class:`huaweicloudsdkvpc.v2.CreateSubnetTagRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.CreateSubnetTagResponse`
        """
        http_info = self._create_subnet_tag_http_info(request)
        return self._call_api(**http_info)

    def create_subnet_tag_invoker(self, request):
        http_info = self._create_subnet_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_subnet_tag_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/subnets/{subnet_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSubnetTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_vpc_peering(self, request):
        """创建对等连接

        创建对等连接。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateVpcPeering
        :type request: :class:`huaweicloudsdkvpc.v2.CreateVpcPeeringRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.CreateVpcPeeringResponse`
        """
        http_info = self._create_vpc_peering_http_info(request)
        return self._call_api(**http_info)

    def create_vpc_peering_invoker(self, request):
        http_info = self._create_vpc_peering_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_vpc_peering_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/vpc/peerings",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVpcPeeringResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_flow_log(self, request):
        """删除流日志

        删除流日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteFlowLog
        :type request: :class:`huaweicloudsdkvpc.v2.DeleteFlowLogRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.DeleteFlowLogResponse`
        """
        http_info = self._delete_flow_log_http_info(request)
        return self._call_api(**http_info)

    def delete_flow_log_invoker(self, request):
        http_info = self._delete_flow_log_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_flow_log_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/fl/flow_logs/{flowlog_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteFlowLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'flowlog_id' in local_var_params:
            path_params['flowlog_id'] = local_var_params['flowlog_id']

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

    def delete_port(self, request):
        """删除端口

        删除端口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePort
        :type request: :class:`huaweicloudsdkvpc.v2.DeletePortRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.DeletePortResponse`
        """
        http_info = self._delete_port_http_info(request)
        return self._call_api(**http_info)

    def delete_port_invoker(self, request):
        http_info = self._delete_port_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_port_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/ports/{port_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePortResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

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

    def delete_route_table(self, request):
        """删除路由表

        删除路由表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRouteTable
        :type request: :class:`huaweicloudsdkvpc.v2.DeleteRouteTableRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.DeleteRouteTableResponse`
        """
        http_info = self._delete_route_table_http_info(request)
        return self._call_api(**http_info)

    def delete_route_table_invoker(self, request):
        http_info = self._delete_route_table_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_route_table_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/routetables/{routetable_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRouteTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

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

    def delete_security_group(self, request):
        """删除安全组

        删除安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSecurityGroup
        :type request: :class:`huaweicloudsdkvpc.v2.DeleteSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.DeleteSecurityGroupResponse`
        """
        http_info = self._delete_security_group_http_info(request)
        return self._call_api(**http_info)

    def delete_security_group_invoker(self, request):
        http_info = self._delete_security_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_security_group_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/security-groups/{security_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSecurityGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_group_id' in local_var_params:
            path_params['security_group_id'] = local_var_params['security_group_id']

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

    def delete_security_group_rule(self, request):
        """删除安全组规则

        删除安全组规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSecurityGroupRule
        :type request: :class:`huaweicloudsdkvpc.v2.DeleteSecurityGroupRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.DeleteSecurityGroupRuleResponse`
        """
        http_info = self._delete_security_group_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_security_group_rule_invoker(self, request):
        http_info = self._delete_security_group_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_security_group_rule_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/security-group-rules/{security_group_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSecurityGroupRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_group_rule_id' in local_var_params:
            path_params['security_group_rule_id'] = local_var_params['security_group_rule_id']

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

    def delete_subnet(self, request):
        """删除子网

        删除子网
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSubnet
        :type request: :class:`huaweicloudsdkvpc.v2.DeleteSubnetRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.DeleteSubnetResponse`
        """
        http_info = self._delete_subnet_http_info(request)
        return self._call_api(**http_info)

    def delete_subnet_invoker(self, request):
        http_info = self._delete_subnet_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_subnet_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/vpcs/{vpc_id}/subnets/{subnet_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSubnetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

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

    def delete_subnet_tag(self, request):
        """删除子网资源标签

        删除指定子网资源实例的标签信息。
        该接口为幂等接口：删除的key不存在报404，Key不能为空或者空字符串
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSubnetTag
        :type request: :class:`huaweicloudsdkvpc.v2.DeleteSubnetTagRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.DeleteSubnetTagResponse`
        """
        http_info = self._delete_subnet_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_subnet_tag_invoker(self, request):
        http_info = self._delete_subnet_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_subnet_tag_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/{project_id}/subnets/{subnet_id}/tags/{key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSubnetTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']
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

    def delete_vpc_peering(self, request):
        """删除对等连接

        删除对等连接。
        可以在在本端或对端任何一端删除对等连接。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteVpcPeering
        :type request: :class:`huaweicloudsdkvpc.v2.DeleteVpcPeeringRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.DeleteVpcPeeringResponse`
        """
        http_info = self._delete_vpc_peering_http_info(request)
        return self._call_api(**http_info)

    def delete_vpc_peering_invoker(self, request):
        http_info = self._delete_vpc_peering_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_vpc_peering_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/vpc/peerings/{peering_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVpcPeeringResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'peering_id' in local_var_params:
            path_params['peering_id'] = local_var_params['peering_id']

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

    def disassociate_route_table(self, request):
        """子网解关联路由表

        子网解关联路由表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisassociateRouteTable
        :type request: :class:`huaweicloudsdkvpc.v2.DisassociateRouteTableRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.DisassociateRouteTableResponse`
        """
        http_info = self._disassociate_route_table_http_info(request)
        return self._call_api(**http_info)

    def disassociate_route_table_invoker(self, request):
        http_info = self._disassociate_route_table_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disassociate_route_table_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/routetables/{routetable_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateRouteTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_flow_logs(self, request):
        """查询流日志列表

        查询提交请求的租户的所有流日志列表，并根据过滤条件进行过滤
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFlowLogs
        :type request: :class:`huaweicloudsdkvpc.v2.ListFlowLogsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ListFlowLogsResponse`
        """
        http_info = self._list_flow_logs_http_info(request)
        return self._call_api(**http_info)

    def list_flow_logs_invoker(self, request):
        http_info = self._list_flow_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_flow_logs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/fl/flow_logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListFlowLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'tenant_id' in local_var_params:
            query_params.append(('tenant_id', local_var_params['tenant_id']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'traffic_type' in local_var_params:
            query_params.append(('traffic_type', local_var_params['traffic_type']))
        if 'log_group_id' in local_var_params:
            query_params.append(('log_group_id', local_var_params['log_group_id']))
        if 'log_topic_id' in local_var_params:
            query_params.append(('log_topic_id', local_var_params['log_topic_id']))
        if 'log_store_type' in local_var_params:
            query_params.append(('log_store_type', local_var_params['log_store_type']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
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

    def list_ports(self, request):
        """查询端口列表

        查询提交请求的租户的所有端口，单次查询最多返回2000条数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPorts
        :type request: :class:`huaweicloudsdkvpc.v2.ListPortsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ListPortsResponse`
        """
        http_info = self._list_ports_http_info(request)
        return self._call_api(**http_info)

    def list_ports_invoker(self, request):
        http_info = self._list_ports_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ports_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/ports",
            "request_type": request.__class__.__name__,
            "response_type": "ListPortsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'network_id' in local_var_params:
            query_params.append(('network_id', local_var_params['network_id']))
        if 'mac_address' in local_var_params:
            query_params.append(('mac_address', local_var_params['mac_address']))
        if 'device_id' in local_var_params:
            query_params.append(('device_id', local_var_params['device_id']))
        if 'device_owner' in local_var_params:
            query_params.append(('device_owner', local_var_params['device_owner']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'security_groups' in local_var_params:
            query_params.append(('security_groups', local_var_params['security_groups']))
            collection_formats['security_groups'] = 'multi'
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'fixed_ips' in local_var_params:
            query_params.append(('fixed_ips', local_var_params['fixed_ips']))
            collection_formats['fixed_ips'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'enable_efi' in local_var_params:
            query_params.append(('enable_efi', local_var_params['enable_efi']))

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

    def list_route_tables(self, request):
        """查询路由表列表

        查询提交请求的帐户的所有路由表列表，并根据过滤条件进行过滤
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRouteTables
        :type request: :class:`huaweicloudsdkvpc.v2.ListRouteTablesRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ListRouteTablesResponse`
        """
        http_info = self._list_route_tables_http_info(request)
        return self._call_api(**http_info)

    def list_route_tables_invoker(self, request):
        http_info = self._list_route_tables_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_route_tables_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/routetables",
            "request_type": request.__class__.__name__,
            "response_type": "ListRouteTablesResponse"
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
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
        if 'subnet_id' in local_var_params:
            query_params.append(('subnet_id', local_var_params['subnet_id']))

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

    def list_security_group_rules(self, request):
        """查询安全组规则列表

        查询安全组规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSecurityGroupRules
        :type request: :class:`huaweicloudsdkvpc.v2.ListSecurityGroupRulesRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ListSecurityGroupRulesResponse`
        """
        http_info = self._list_security_group_rules_http_info(request)
        return self._call_api(**http_info)

    def list_security_group_rules_invoker(self, request):
        http_info = self._list_security_group_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_security_group_rules_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/security-group-rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListSecurityGroupRulesResponse"
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
        if 'security_group_id' in local_var_params:
            query_params.append(('security_group_id', local_var_params['security_group_id']))
        if 'remote_ip_prefix' in local_var_params:
            query_params.append(('remote_ip_prefix', local_var_params['remote_ip_prefix']))

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

    def list_security_groups(self, request):
        """查询安全组列表

        查询安全组列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSecurityGroups
        :type request: :class:`huaweicloudsdkvpc.v2.ListSecurityGroupsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ListSecurityGroupsResponse`
        """
        http_info = self._list_security_groups_http_info(request)
        return self._call_api(**http_info)

    def list_security_groups_invoker(self, request):
        http_info = self._list_security_groups_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_security_groups_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/security-groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListSecurityGroupsResponse"
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
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
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

    def list_subnet_tags(self, request):
        """查询子网项目标签

        查询租户在指定区域和实例类型的所有标签集合
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSubnetTags
        :type request: :class:`huaweicloudsdkvpc.v2.ListSubnetTagsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ListSubnetTagsResponse`
        """
        http_info = self._list_subnet_tags_http_info(request)
        return self._call_api(**http_info)

    def list_subnet_tags_invoker(self, request):
        http_info = self._list_subnet_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_subnet_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/subnets/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListSubnetTagsResponse"
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

    def list_subnets(self, request):
        """查询子网列表

        查询子网列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSubnets
        :type request: :class:`huaweicloudsdkvpc.v2.ListSubnetsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ListSubnetsResponse`
        """
        http_info = self._list_subnets_http_info(request)
        return self._call_api(**http_info)

    def list_subnets_invoker(self, request):
        http_info = self._list_subnets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_subnets_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/subnets",
            "request_type": request.__class__.__name__,
            "response_type": "ListSubnetsResponse"
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

    def list_subnets_by_tags(self, request):
        """查询子网资源实例

        使用标签过滤实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSubnetsByTags
        :type request: :class:`huaweicloudsdkvpc.v2.ListSubnetsByTagsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ListSubnetsByTagsResponse`
        """
        http_info = self._list_subnets_by_tags_http_info(request)
        return self._call_api(**http_info)

    def list_subnets_by_tags_invoker(self, request):
        http_info = self._list_subnets_by_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_subnets_by_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/subnets/resource_instances/action",
            "request_type": request.__class__.__name__,
            "response_type": "ListSubnetsByTagsResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_vpc_peerings(self, request):
        """查询对等连接列表

        查询提交请求的租户的所有对等连接。根据过滤条件进行过滤。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVpcPeerings
        :type request: :class:`huaweicloudsdkvpc.v2.ListVpcPeeringsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ListVpcPeeringsResponse`
        """
        http_info = self._list_vpc_peerings_http_info(request)
        return self._call_api(**http_info)

    def list_vpc_peerings_invoker(self, request):
        http_info = self._list_vpc_peerings_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_vpc_peerings_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/vpc/peerings",
            "request_type": request.__class__.__name__,
            "response_type": "ListVpcPeeringsResponse"
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
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'tenant_id' in local_var_params:
            query_params.append(('tenant_id', local_var_params['tenant_id']))
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

    def reject_vpc_peering(self, request):
        """拒绝对等连接请求

        租户A名下的VPC申请和租户B的VPC建立对等连接，需要等待租户B接受该请求。此接口用于租户拒绝其他租户发起的对等连接请求。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RejectVpcPeering
        :type request: :class:`huaweicloudsdkvpc.v2.RejectVpcPeeringRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.RejectVpcPeeringResponse`
        """
        http_info = self._reject_vpc_peering_http_info(request)
        return self._call_api(**http_info)

    def reject_vpc_peering_invoker(self, request):
        http_info = self._reject_vpc_peering_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reject_vpc_peering_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.0/vpc/peerings/{peering_id}/reject",
            "request_type": request.__class__.__name__,
            "response_type": "RejectVpcPeeringResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'peering_id' in local_var_params:
            path_params['peering_id'] = local_var_params['peering_id']

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

    def show_flow_log(self, request):
        """查询流日志

        查询流日志详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFlowLog
        :type request: :class:`huaweicloudsdkvpc.v2.ShowFlowLogRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ShowFlowLogResponse`
        """
        http_info = self._show_flow_log_http_info(request)
        return self._call_api(**http_info)

    def show_flow_log_invoker(self, request):
        http_info = self._show_flow_log_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_flow_log_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/fl/flow_logs/{flowlog_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFlowLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'flowlog_id' in local_var_params:
            path_params['flowlog_id'] = local_var_params['flowlog_id']

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

    def show_port(self, request):
        """查询端口

        查询单个端口详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPort
        :type request: :class:`huaweicloudsdkvpc.v2.ShowPortRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ShowPortResponse`
        """
        http_info = self._show_port_http_info(request)
        return self._call_api(**http_info)

    def show_port_invoker(self, request):
        http_info = self._show_port_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_port_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/ports/{port_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPortResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

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

    def show_quota(self, request):
        """查询配额

        查询单租户在VPC服务下的网络资源配额，包括vpc配额、子网配额、安全组配额、安全组规则配额、弹性公网IP配额，vpn配额等。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowQuota
        :type request: :class:`huaweicloudsdkvpc.v2.ShowQuotaRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ShowQuotaResponse`
        """
        http_info = self._show_quota_http_info(request)
        return self._call_api(**http_info)

    def show_quota_invoker(self, request):
        http_info = self._show_quota_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_quota_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowQuotaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

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

    def show_route_table(self, request):
        """查询路由表

        查询路由表详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRouteTable
        :type request: :class:`huaweicloudsdkvpc.v2.ShowRouteTableRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ShowRouteTableResponse`
        """
        http_info = self._show_route_table_http_info(request)
        return self._call_api(**http_info)

    def show_route_table_invoker(self, request):
        http_info = self._show_route_table_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_route_table_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/routetables/{routetable_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRouteTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

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

    def show_security_group(self, request):
        """查询安全组

        查询单个安全组详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSecurityGroup
        :type request: :class:`huaweicloudsdkvpc.v2.ShowSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ShowSecurityGroupResponse`
        """
        http_info = self._show_security_group_http_info(request)
        return self._call_api(**http_info)

    def show_security_group_invoker(self, request):
        http_info = self._show_security_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_security_group_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/security-groups/{security_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSecurityGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_group_id' in local_var_params:
            path_params['security_group_id'] = local_var_params['security_group_id']

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

    def show_security_group_rule(self, request):
        """查询安全组规则

        查询单个安全组规则详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSecurityGroupRule
        :type request: :class:`huaweicloudsdkvpc.v2.ShowSecurityGroupRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ShowSecurityGroupRuleResponse`
        """
        http_info = self._show_security_group_rule_http_info(request)
        return self._call_api(**http_info)

    def show_security_group_rule_invoker(self, request):
        http_info = self._show_security_group_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_security_group_rule_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/security-group-rules/{security_group_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSecurityGroupRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_group_rule_id' in local_var_params:
            path_params['security_group_rule_id'] = local_var_params['security_group_rule_id']

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

    def show_subnet(self, request):
        """查询子网

        查询子网详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSubnet
        :type request: :class:`huaweicloudsdkvpc.v2.ShowSubnetRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ShowSubnetResponse`
        """
        http_info = self._show_subnet_http_info(request)
        return self._call_api(**http_info)

    def show_subnet_invoker(self, request):
        http_info = self._show_subnet_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_subnet_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/subnets/{subnet_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSubnetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

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

    def show_subnet_tags(self, request):
        """查询子网资源标签

        查询指定子网实例的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSubnetTags
        :type request: :class:`huaweicloudsdkvpc.v2.ShowSubnetTagsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ShowSubnetTagsResponse`
        """
        http_info = self._show_subnet_tags_http_info(request)
        return self._call_api(**http_info)

    def show_subnet_tags_invoker(self, request):
        http_info = self._show_subnet_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_subnet_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/subnets/{subnet_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSubnetTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

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

    def show_vpc_peering(self, request):
        """查询对等连接

        查询对等连接详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVpcPeering
        :type request: :class:`huaweicloudsdkvpc.v2.ShowVpcPeeringRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ShowVpcPeeringResponse`
        """
        http_info = self._show_vpc_peering_http_info(request)
        return self._call_api(**http_info)

    def show_vpc_peering_invoker(self, request):
        http_info = self._show_vpc_peering_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_vpc_peering_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/vpc/peerings/{peering_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVpcPeeringResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'peering_id' in local_var_params:
            path_params['peering_id'] = local_var_params['peering_id']

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

    def update_flow_log(self, request):
        """更新流日志

        更新流日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateFlowLog
        :type request: :class:`huaweicloudsdkvpc.v2.UpdateFlowLogRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.UpdateFlowLogResponse`
        """
        http_info = self._update_flow_log_http_info(request)
        return self._call_api(**http_info)

    def update_flow_log_invoker(self, request):
        http_info = self._update_flow_log_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_flow_log_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/fl/flow_logs/{flowlog_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateFlowLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'flowlog_id' in local_var_params:
            path_params['flowlog_id'] = local_var_params['flowlog_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_port(self, request):
        """更新端口

        更新端口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePort
        :type request: :class:`huaweicloudsdkvpc.v2.UpdatePortRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.UpdatePortResponse`
        """
        http_info = self._update_port_http_info(request)
        return self._call_api(**http_info)

    def update_port_invoker(self, request):
        http_info = self._update_port_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_port_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/ports/{port_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePortResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_route_table(self, request):
        """更新路由表

        更新路由表，包括可以更新路由表的名称，描述，以及新增、更新、删除路由条目
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRouteTable
        :type request: :class:`huaweicloudsdkvpc.v2.UpdateRouteTableRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.UpdateRouteTableResponse`
        """
        http_info = self._update_route_table_http_info(request)
        return self._call_api(**http_info)

    def update_route_table_invoker(self, request):
        http_info = self._update_route_table_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_route_table_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/routetables/{routetable_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRouteTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_subnet(self, request):
        """更新子网

        更新子网。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSubnet
        :type request: :class:`huaweicloudsdkvpc.v2.UpdateSubnetRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.UpdateSubnetResponse`
        """
        http_info = self._update_subnet_http_info(request)
        return self._call_api(**http_info)

    def update_subnet_invoker(self, request):
        http_info = self._update_subnet_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_subnet_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/vpcs/{vpc_id}/subnets/{subnet_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSubnetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_vpc_peering(self, request):
        """更新对等连接

        更新对等连接。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateVpcPeering
        :type request: :class:`huaweicloudsdkvpc.v2.UpdateVpcPeeringRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.UpdateVpcPeeringResponse`
        """
        http_info = self._update_vpc_peering_http_info(request)
        return self._call_api(**http_info)

    def update_vpc_peering_invoker(self, request):
        http_info = self._update_vpc_peering_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_vpc_peering_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.0/vpc/peerings/{peering_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateVpcPeeringResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'peering_id' in local_var_params:
            path_params['peering_id'] = local_var_params['peering_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_privateip(self, request):
        """申请私有IP

        申请私有IP。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePrivateip
        :type request: :class:`huaweicloudsdkvpc.v2.CreatePrivateipRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.CreatePrivateipResponse`
        """
        http_info = self._create_privateip_http_info(request)
        return self._call_api(**http_info)

    def create_privateip_invoker(self, request):
        http_info = self._create_privateip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_privateip_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/privateips",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePrivateipResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_privateip(self, request):
        """删除私有IP

        删除私有IP。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePrivateip
        :type request: :class:`huaweicloudsdkvpc.v2.DeletePrivateipRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.DeletePrivateipResponse`
        """
        http_info = self._delete_privateip_http_info(request)
        return self._call_api(**http_info)

    def delete_privateip_invoker(self, request):
        http_info = self._delete_privateip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_privateip_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/privateips/{privateip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePrivateipResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'privateip_id' in local_var_params:
            path_params['privateip_id'] = local_var_params['privateip_id']

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

    def list_privateips(self, request):
        """查询私有IP列表

        查询指定子网下的私有IP列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPrivateips
        :type request: :class:`huaweicloudsdkvpc.v2.ListPrivateipsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ListPrivateipsResponse`
        """
        http_info = self._list_privateips_http_info(request)
        return self._call_api(**http_info)

    def list_privateips_invoker(self, request):
        http_info = self._list_privateips_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_privateips_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/subnets/{subnet_id}/privateips",
            "request_type": request.__class__.__name__,
            "response_type": "ListPrivateipsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

        query_params = []
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

    def show_network_ip_availabilities(self, request):
        """查询网络IP使用情况

        显示一个指定网络中的IPv4地址使用情况。
        包括此网络中的IP总数以及已用IP总数，以及网络下每一个子网的IP地址总数和可用IP地址总数。
        
        &gt; 须知
        
        - 系统预留地址指的是子网的第1个以及最后4个地址，一般用于网关、DHCP等服务。
        - 这里以及下文描述的IP地址总数、已用IP地址总数不包含系统预留地址。
        - 在分配IP时，用户可以指定系统预留的IP地址。但是不论IP是如何分配的，只要是处于系统预留IP地址段的IP均不会被统计到已用IP地址数目和IP地址总数中。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNetworkIpAvailabilities
        :type request: :class:`huaweicloudsdkvpc.v2.ShowNetworkIpAvailabilitiesRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ShowNetworkIpAvailabilitiesResponse`
        """
        http_info = self._show_network_ip_availabilities_http_info(request)
        return self._call_api(**http_info)

    def show_network_ip_availabilities_invoker(self, request):
        http_info = self._show_network_ip_availabilities_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_network_ip_availabilities_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/network-ip-availabilities/{network_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNetworkIpAvailabilitiesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'network_id' in local_var_params:
            path_params['network_id'] = local_var_params['network_id']

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

    def show_privateip(self, request):
        """查询私有IP

        指定ID查询私有IP。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPrivateip
        :type request: :class:`huaweicloudsdkvpc.v2.ShowPrivateipRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ShowPrivateipResponse`
        """
        http_info = self._show_privateip_http_info(request)
        return self._call_api(**http_info)

    def show_privateip_invoker(self, request):
        http_info = self._show_privateip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_privateip_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/privateips/{privateip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPrivateipResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'privateip_id' in local_var_params:
            path_params['privateip_id'] = local_var_params['privateip_id']

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

    def neutron_add_router_interface(self, request):
        """路由器添加接口

        添加路由器接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronAddRouterInterface
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronAddRouterInterfaceRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronAddRouterInterfaceResponse`
        """
        http_info = self._neutron_add_router_interface_http_info(request)
        return self._call_api(**http_info)

    def neutron_add_router_interface_invoker(self, request):
        http_info = self._neutron_add_router_interface_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_add_router_interface_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.0/routers/{router_id}/add_router_interface",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronAddRouterInterfaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'router_id' in local_var_params:
            path_params['router_id'] = local_var_params['router_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def neutron_create_network(self, request):
        """创建网络

        创建网络
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronCreateNetwork
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronCreateNetworkRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronCreateNetworkResponse`
        """
        http_info = self._neutron_create_network_http_info(request)
        return self._call_api(**http_info)

    def neutron_create_network_invoker(self, request):
        http_info = self._neutron_create_network_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_create_network_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/networks",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronCreateNetworkResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def neutron_create_port(self, request):
        """创建端口

        创建端口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronCreatePort
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronCreatePortRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronCreatePortResponse`
        """
        http_info = self._neutron_create_port_http_info(request)
        return self._call_api(**http_info)

    def neutron_create_port_invoker(self, request):
        http_info = self._neutron_create_port_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_create_port_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/ports",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronCreatePortResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def neutron_create_router(self, request):
        """创建路由器

        创建路由器。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronCreateRouter
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronCreateRouterRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronCreateRouterResponse`
        """
        http_info = self._neutron_create_router_http_info(request)
        return self._call_api(**http_info)

    def neutron_create_router_invoker(self, request):
        http_info = self._neutron_create_router_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_create_router_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/routers",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronCreateRouterResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def neutron_create_security_group(self, request):
        """创建安全组

        创建安全组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronCreateSecurityGroup
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronCreateSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronCreateSecurityGroupResponse`
        """
        http_info = self._neutron_create_security_group_http_info(request)
        return self._call_api(**http_info)

    def neutron_create_security_group_invoker(self, request):
        http_info = self._neutron_create_security_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_create_security_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/security-groups",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronCreateSecurityGroupResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def neutron_create_security_group_rule(self, request):
        """创建安全组规则

        创建安全组规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronCreateSecurityGroupRule
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronCreateSecurityGroupRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronCreateSecurityGroupRuleResponse`
        """
        http_info = self._neutron_create_security_group_rule_http_info(request)
        return self._call_api(**http_info)

    def neutron_create_security_group_rule_invoker(self, request):
        http_info = self._neutron_create_security_group_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_create_security_group_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/security-group-rules",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronCreateSecurityGroupRuleResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def neutron_create_subnet(self, request):
        """创建子网

        创建子网。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronCreateSubnet
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronCreateSubnetRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronCreateSubnetResponse`
        """
        http_info = self._neutron_create_subnet_http_info(request)
        return self._call_api(**http_info)

    def neutron_create_subnet_invoker(self, request):
        http_info = self._neutron_create_subnet_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_create_subnet_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/subnets",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronCreateSubnetResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def neutron_delete_network(self, request):
        """删除网络

        删除网络
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronDeleteNetwork
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronDeleteNetworkRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronDeleteNetworkResponse`
        """
        http_info = self._neutron_delete_network_http_info(request)
        return self._call_api(**http_info)

    def neutron_delete_network_invoker(self, request):
        http_info = self._neutron_delete_network_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_delete_network_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/networks/{network_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronDeleteNetworkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'network_id' in local_var_params:
            path_params['network_id'] = local_var_params['network_id']

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

    def neutron_delete_port(self, request):
        """删除端口

        删除端口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronDeletePort
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronDeletePortRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronDeletePortResponse`
        """
        http_info = self._neutron_delete_port_http_info(request)
        return self._call_api(**http_info)

    def neutron_delete_port_invoker(self, request):
        http_info = self._neutron_delete_port_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_delete_port_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/ports/{port_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronDeletePortResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

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

    def neutron_delete_router(self, request):
        """删除路由器

        删除路由器
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronDeleteRouter
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronDeleteRouterRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronDeleteRouterResponse`
        """
        http_info = self._neutron_delete_router_http_info(request)
        return self._call_api(**http_info)

    def neutron_delete_router_invoker(self, request):
        http_info = self._neutron_delete_router_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_delete_router_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/routers/{router_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronDeleteRouterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'router_id' in local_var_params:
            path_params['router_id'] = local_var_params['router_id']

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

    def neutron_delete_security_group(self, request):
        """删除安全组

        删除安全组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronDeleteSecurityGroup
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronDeleteSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronDeleteSecurityGroupResponse`
        """
        http_info = self._neutron_delete_security_group_http_info(request)
        return self._call_api(**http_info)

    def neutron_delete_security_group_invoker(self, request):
        http_info = self._neutron_delete_security_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_delete_security_group_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/security-groups/{security_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronDeleteSecurityGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_group_id' in local_var_params:
            path_params['security_group_id'] = local_var_params['security_group_id']

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

    def neutron_delete_security_group_rule(self, request):
        """删除安全组规则

        删除安全组规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronDeleteSecurityGroupRule
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronDeleteSecurityGroupRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronDeleteSecurityGroupRuleResponse`
        """
        http_info = self._neutron_delete_security_group_rule_http_info(request)
        return self._call_api(**http_info)

    def neutron_delete_security_group_rule_invoker(self, request):
        http_info = self._neutron_delete_security_group_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_delete_security_group_rule_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/security-group-rules/{security_group_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronDeleteSecurityGroupRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_group_rule_id' in local_var_params:
            path_params['security_group_rule_id'] = local_var_params['security_group_rule_id']

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

    def neutron_delete_subnet(self, request):
        """删除子网

        删除子网
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronDeleteSubnet
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronDeleteSubnetRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronDeleteSubnetResponse`
        """
        http_info = self._neutron_delete_subnet_http_info(request)
        return self._call_api(**http_info)

    def neutron_delete_subnet_invoker(self, request):
        http_info = self._neutron_delete_subnet_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_delete_subnet_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/subnets/{subnet_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronDeleteSubnetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

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

    def neutron_list_networks(self, request):
        """查询网络列表

        查询提交请求的租户的所有网络，单次查询最多返回2000条数据，超过2000后会返回分页标记。分页查询请参考分页查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronListNetworks
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronListNetworksRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronListNetworksResponse`
        """
        http_info = self._neutron_list_networks_http_info(request)
        return self._call_api(**http_info)

    def neutron_list_networks_invoker(self, request):
        http_info = self._neutron_list_networks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_list_networks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/networks",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronListNetworksResponse"
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
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'shared' in local_var_params:
            query_params.append(('shared', local_var_params['shared']))
        if 'routerexternal' in local_var_params:
            query_params.append(('router:external', local_var_params['routerexternal']))
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'providernetwork_type' in local_var_params:
            query_params.append(('provider:network_type', local_var_params['providernetwork_type']))
        if 'tenant_id' in local_var_params:
            query_params.append(('tenant_id', local_var_params['tenant_id']))

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

    def neutron_list_ports(self, request):
        """查询端口列表

        查询提交请求的租户的所有端口，单次查询最多返回2000条数据，超过2000后会返回分页标记。分页查询请参考分页查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronListPorts
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronListPortsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronListPortsResponse`
        """
        http_info = self._neutron_list_ports_http_info(request)
        return self._call_api(**http_info)

    def neutron_list_ports_invoker(self, request):
        http_info = self._neutron_list_ports_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_list_ports_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/ports",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronListPortsResponse"
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
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'network_id' in local_var_params:
            query_params.append(('network_id', local_var_params['network_id']))
        if 'mac_address' in local_var_params:
            query_params.append(('mac_address', local_var_params['mac_address']))
        if 'device_id' in local_var_params:
            query_params.append(('device_id', local_var_params['device_id']))
        if 'device_owner' in local_var_params:
            query_params.append(('device_owner', local_var_params['device_owner']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'security_groups' in local_var_params:
            query_params.append(('security_groups', local_var_params['security_groups']))
            collection_formats['security_groups'] = 'multi'
        if 'fixed_ips' in local_var_params:
            query_params.append(('fixed_ips', local_var_params['fixed_ips']))
            collection_formats['fixed_ips'] = 'multi'
        if 'tenant_id' in local_var_params:
            query_params.append(('tenant_id', local_var_params['tenant_id']))

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

    def neutron_list_routers(self, request):
        """查询路由器列表

        查询提交请求的租户有权限操作的所有路由器信息，单次查询最多返回2000条数据，超过2000后会返回分页标记。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronListRouters
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronListRoutersRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronListRoutersResponse`
        """
        http_info = self._neutron_list_routers_http_info(request)
        return self._call_api(**http_info)

    def neutron_list_routers_invoker(self, request):
        http_info = self._neutron_list_routers_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_list_routers_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/routers",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronListRoutersResponse"
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
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'tenant_id' in local_var_params:
            query_params.append(('tenant_id', local_var_params['tenant_id']))
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))

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

    def neutron_list_security_group_rules(self, request):
        """查询安全组规则列表

        查询提交请求的租户有权限查看的所有安全组规则。单次查询最多返回2000条数据，超过2000后会返回分页标记。分页查询请参考分页查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronListSecurityGroupRules
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronListSecurityGroupRulesRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronListSecurityGroupRulesResponse`
        """
        http_info = self._neutron_list_security_group_rules_http_info(request)
        return self._call_api(**http_info)

    def neutron_list_security_group_rules_invoker(self, request):
        http_info = self._neutron_list_security_group_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_list_security_group_rules_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/security-group-rules",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronListSecurityGroupRulesResponse"
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
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'direction' in local_var_params:
            query_params.append(('direction', local_var_params['direction']))
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
        if 'ethertype' in local_var_params:
            query_params.append(('ethertype', local_var_params['ethertype']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'remote_ip_prefix' in local_var_params:
            query_params.append(('remote_ip_prefix', local_var_params['remote_ip_prefix']))
        if 'remote_group_id' in local_var_params:
            query_params.append(('remote_group_id', local_var_params['remote_group_id']))
        if 'security_group_id' in local_var_params:
            query_params.append(('security_group_id', local_var_params['security_group_id']))
        if 'port_range_max' in local_var_params:
            query_params.append(('port_range_max', local_var_params['port_range_max']))
        if 'port_range_min' in local_var_params:
            query_params.append(('port_range_min', local_var_params['port_range_min']))
        if 'tenant_id' in local_var_params:
            query_params.append(('tenant_id', local_var_params['tenant_id']))

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

    def neutron_list_security_groups(self, request):
        """查询安全组列表

        查询提交请求租户的所有安全组，单次查询最多返回2000条数据，超过2000后会返回分页标记。分页查询请参考分页查询 。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronListSecurityGroups
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronListSecurityGroupsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronListSecurityGroupsResponse`
        """
        http_info = self._neutron_list_security_groups_http_info(request)
        return self._call_api(**http_info)

    def neutron_list_security_groups_invoker(self, request):
        http_info = self._neutron_list_security_groups_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_list_security_groups_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/security-groups",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronListSecurityGroupsResponse"
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
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'tenant_id' in local_var_params:
            query_params.append(('tenant_id', local_var_params['tenant_id']))

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

    def neutron_list_subnets(self, request):
        """查询子网列表

        查询提交请求租户的所有子网，单次查询最多返回2000条数据，超过2000后会返回分页标记。分页查询请参考分页查询 。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronListSubnets
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronListSubnetsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronListSubnetsResponse`
        """
        http_info = self._neutron_list_subnets_http_info(request)
        return self._call_api(**http_info)

    def neutron_list_subnets_invoker(self, request):
        http_info = self._neutron_list_subnets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_list_subnets_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/subnets",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronListSubnetsResponse"
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
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'cidr' in local_var_params:
            query_params.append(('cidr', local_var_params['cidr']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'enable_dhcp' in local_var_params:
            query_params.append(('enable_dhcp', local_var_params['enable_dhcp']))
        if 'network_id' in local_var_params:
            query_params.append(('network_id', local_var_params['network_id']))
        if 'ip_version' in local_var_params:
            query_params.append(('ip_version', local_var_params['ip_version']))
        if 'gateway_ip' in local_var_params:
            query_params.append(('gateway_ip', local_var_params['gateway_ip']))
        if 'tenant_id' in local_var_params:
            query_params.append(('tenant_id', local_var_params['tenant_id']))

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

    def neutron_remove_router_interface(self, request):
        """路由器删除接口

        删除路由器接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronRemoveRouterInterface
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronRemoveRouterInterfaceRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronRemoveRouterInterfaceResponse`
        """
        http_info = self._neutron_remove_router_interface_http_info(request)
        return self._call_api(**http_info)

    def neutron_remove_router_interface_invoker(self, request):
        http_info = self._neutron_remove_router_interface_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_remove_router_interface_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.0/routers/{router_id}/remove_router_interface",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronRemoveRouterInterfaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'router_id' in local_var_params:
            path_params['router_id'] = local_var_params['router_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def neutron_show_network(self, request):
        """查询网络

        查询指定的网络详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronShowNetwork
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronShowNetworkRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronShowNetworkResponse`
        """
        http_info = self._neutron_show_network_http_info(request)
        return self._call_api(**http_info)

    def neutron_show_network_invoker(self, request):
        http_info = self._neutron_show_network_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_show_network_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/networks/{network_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronShowNetworkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'network_id' in local_var_params:
            path_params['network_id'] = local_var_params['network_id']

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

    def neutron_show_port(self, request):
        """查询端口

        查询端口详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronShowPort
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronShowPortRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronShowPortResponse`
        """
        http_info = self._neutron_show_port_http_info(request)
        return self._call_api(**http_info)

    def neutron_show_port_invoker(self, request):
        http_info = self._neutron_show_port_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_show_port_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/ports/{port_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronShowPortResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

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

    def neutron_show_router(self, request):
        """查询路由器

        查询路由器详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronShowRouter
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronShowRouterRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronShowRouterResponse`
        """
        http_info = self._neutron_show_router_http_info(request)
        return self._call_api(**http_info)

    def neutron_show_router_invoker(self, request):
        http_info = self._neutron_show_router_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_show_router_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/routers/{router_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronShowRouterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'router_id' in local_var_params:
            path_params['router_id'] = local_var_params['router_id']

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

    def neutron_show_security_group(self, request):
        """查询安全组

        查询安全组详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronShowSecurityGroup
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronShowSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronShowSecurityGroupResponse`
        """
        http_info = self._neutron_show_security_group_http_info(request)
        return self._call_api(**http_info)

    def neutron_show_security_group_invoker(self, request):
        http_info = self._neutron_show_security_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_show_security_group_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/security-groups/{security_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronShowSecurityGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_group_id' in local_var_params:
            path_params['security_group_id'] = local_var_params['security_group_id']

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

    def neutron_show_security_group_rule(self, request):
        """查询安全组规则

        查询安全组规则详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronShowSecurityGroupRule
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronShowSecurityGroupRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronShowSecurityGroupRuleResponse`
        """
        http_info = self._neutron_show_security_group_rule_http_info(request)
        return self._call_api(**http_info)

    def neutron_show_security_group_rule_invoker(self, request):
        http_info = self._neutron_show_security_group_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_show_security_group_rule_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/security-group-rules/{security_group_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronShowSecurityGroupRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_group_rule_id' in local_var_params:
            path_params['security_group_rule_id'] = local_var_params['security_group_rule_id']

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

    def neutron_show_subnet(self, request):
        """查询子网

        查询子网详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronShowSubnet
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronShowSubnetRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronShowSubnetResponse`
        """
        http_info = self._neutron_show_subnet_http_info(request)
        return self._call_api(**http_info)

    def neutron_show_subnet_invoker(self, request):
        http_info = self._neutron_show_subnet_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_show_subnet_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/subnets/{subnet_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronShowSubnetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

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

    def neutron_update_network(self, request):
        """更新网络

        更新网络
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronUpdateNetwork
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronUpdateNetworkRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronUpdateNetworkResponse`
        """
        http_info = self._neutron_update_network_http_info(request)
        return self._call_api(**http_info)

    def neutron_update_network_invoker(self, request):
        http_info = self._neutron_update_network_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_update_network_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.0/networks/{network_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronUpdateNetworkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'network_id' in local_var_params:
            path_params['network_id'] = local_var_params['network_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def neutron_update_port(self, request):
        """更新端口

        更新端口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronUpdatePort
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronUpdatePortRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronUpdatePortResponse`
        """
        http_info = self._neutron_update_port_http_info(request)
        return self._call_api(**http_info)

    def neutron_update_port_invoker(self, request):
        http_info = self._neutron_update_port_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_update_port_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.0/ports/{port_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronUpdatePortResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def neutron_update_router(self, request):
        """更新路由器

        更新路由器。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronUpdateRouter
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronUpdateRouterRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronUpdateRouterResponse`
        """
        http_info = self._neutron_update_router_http_info(request)
        return self._call_api(**http_info)

    def neutron_update_router_invoker(self, request):
        http_info = self._neutron_update_router_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_update_router_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.0/routers/{router_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronUpdateRouterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'router_id' in local_var_params:
            path_params['router_id'] = local_var_params['router_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def neutron_update_security_group(self, request):
        """更新安全组

        更新安全组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronUpdateSecurityGroup
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronUpdateSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronUpdateSecurityGroupResponse`
        """
        http_info = self._neutron_update_security_group_http_info(request)
        return self._call_api(**http_info)

    def neutron_update_security_group_invoker(self, request):
        http_info = self._neutron_update_security_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_update_security_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.0/security-groups/{security_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronUpdateSecurityGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_group_id' in local_var_params:
            path_params['security_group_id'] = local_var_params['security_group_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def neutron_update_subnet(self, request):
        """更新子网

        更新子网
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronUpdateSubnet
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronUpdateSubnetRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronUpdateSubnetResponse`
        """
        http_info = self._neutron_update_subnet_http_info(request)
        return self._call_api(**http_info)

    def neutron_update_subnet_invoker(self, request):
        http_info = self._neutron_update_subnet_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_update_subnet_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.0/subnets/{subnet_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronUpdateSubnetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def neutron_add_firewall_rule(self, request):
        """插入网络ACL规则

        插入一条网络ACL规则到某一网络ACL策略中。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronAddFirewallRule
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronAddFirewallRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronAddFirewallRuleResponse`
        """
        http_info = self._neutron_add_firewall_rule_http_info(request)
        return self._call_api(**http_info)

    def neutron_add_firewall_rule_invoker(self, request):
        http_info = self._neutron_add_firewall_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_add_firewall_rule_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.0/fwaas/firewall_policies/{firewall_policy_id}/insert_rule",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronAddFirewallRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_policy_id' in local_var_params:
            path_params['firewall_policy_id'] = local_var_params['firewall_policy_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def neutron_create_firewall_group(self, request):
        """创建网络ACL组

        创建网络ACL组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronCreateFirewallGroup
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronCreateFirewallGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronCreateFirewallGroupResponse`
        """
        http_info = self._neutron_create_firewall_group_http_info(request)
        return self._call_api(**http_info)

    def neutron_create_firewall_group_invoker(self, request):
        http_info = self._neutron_create_firewall_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_create_firewall_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/fwaas/firewall_groups",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronCreateFirewallGroupResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def neutron_create_firewall_policy(self, request):
        """创建网络ACL策略

        创建网络ACL策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronCreateFirewallPolicy
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronCreateFirewallPolicyRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronCreateFirewallPolicyResponse`
        """
        http_info = self._neutron_create_firewall_policy_http_info(request)
        return self._call_api(**http_info)

    def neutron_create_firewall_policy_invoker(self, request):
        http_info = self._neutron_create_firewall_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_create_firewall_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/fwaas/firewall_policies",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronCreateFirewallPolicyResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def neutron_create_firewall_rule(self, request):
        """创建网络ACL规则

        创建网络ACL规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronCreateFirewallRule
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronCreateFirewallRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronCreateFirewallRuleResponse`
        """
        http_info = self._neutron_create_firewall_rule_http_info(request)
        return self._call_api(**http_info)

    def neutron_create_firewall_rule_invoker(self, request):
        http_info = self._neutron_create_firewall_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_create_firewall_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/fwaas/firewall_rules",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronCreateFirewallRuleResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def neutron_delete_firewall_group(self, request):
        """删除网络ACL组

        删除网络ACL组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronDeleteFirewallGroup
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronDeleteFirewallGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronDeleteFirewallGroupResponse`
        """
        http_info = self._neutron_delete_firewall_group_http_info(request)
        return self._call_api(**http_info)

    def neutron_delete_firewall_group_invoker(self, request):
        http_info = self._neutron_delete_firewall_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_delete_firewall_group_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/fwaas/firewall_groups/{firewall_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronDeleteFirewallGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_group_id' in local_var_params:
            path_params['firewall_group_id'] = local_var_params['firewall_group_id']

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

    def neutron_delete_firewall_policy(self, request):
        """删除网络ACL策略

        删除网络ACL策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronDeleteFirewallPolicy
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronDeleteFirewallPolicyRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronDeleteFirewallPolicyResponse`
        """
        http_info = self._neutron_delete_firewall_policy_http_info(request)
        return self._call_api(**http_info)

    def neutron_delete_firewall_policy_invoker(self, request):
        http_info = self._neutron_delete_firewall_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_delete_firewall_policy_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/fwaas/firewall_policies/{firewall_policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronDeleteFirewallPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_policy_id' in local_var_params:
            path_params['firewall_policy_id'] = local_var_params['firewall_policy_id']

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

    def neutron_delete_firewall_rule(self, request):
        """删除网络ACL规则

        删除网络ACL规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronDeleteFirewallRule
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronDeleteFirewallRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronDeleteFirewallRuleResponse`
        """
        http_info = self._neutron_delete_firewall_rule_http_info(request)
        return self._call_api(**http_info)

    def neutron_delete_firewall_rule_invoker(self, request):
        http_info = self._neutron_delete_firewall_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_delete_firewall_rule_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/fwaas/firewall_rules/{firewall_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronDeleteFirewallRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_rule_id' in local_var_params:
            path_params['firewall_rule_id'] = local_var_params['firewall_rule_id']

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

    def neutron_list_firewall_groups(self, request):
        """查询所有网络ACL组

        查询提交请求的租户有权限操作的所有网络ACL组信息。单次查询最多返回2000条数据，超过2000后会返回分页标记。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronListFirewallGroups
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronListFirewallGroupsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronListFirewallGroupsResponse`
        """
        http_info = self._neutron_list_firewall_groups_http_info(request)
        return self._call_api(**http_info)

    def neutron_list_firewall_groups_invoker(self, request):
        http_info = self._neutron_list_firewall_groups_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_list_firewall_groups_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/fwaas/firewall_groups",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronListFirewallGroupsResponse"
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
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'ingress_firewall_policy_id' in local_var_params:
            query_params.append(('ingress_firewall_policy_id', local_var_params['ingress_firewall_policy_id']))
        if 'egress_firewall_policy_id' in local_var_params:
            query_params.append(('egress_firewall_policy_id', local_var_params['egress_firewall_policy_id']))

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

    def neutron_list_firewall_policies(self, request):
        """查询所有网络ACL策略

        查询提交请求的租户有权限操作的所有网络ACL策略信息。单次查询最多返回2000条数据，超过2000后会返回分页标记。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronListFirewallPolicies
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronListFirewallPoliciesRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronListFirewallPoliciesResponse`
        """
        http_info = self._neutron_list_firewall_policies_http_info(request)
        return self._call_api(**http_info)

    def neutron_list_firewall_policies_invoker(self, request):
        http_info = self._neutron_list_firewall_policies_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_list_firewall_policies_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/fwaas/firewall_policies",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronListFirewallPoliciesResponse"
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
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'tenant_id' in local_var_params:
            query_params.append(('tenant_id', local_var_params['tenant_id']))

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

    def neutron_list_firewall_rules(self, request):
        """查询所有网络ACL规则

        查询提交请求的租户有权限操作的所有网络ACL规则信息。单次查询最多返回2000条数据，超过2000后会返回分页标记。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronListFirewallRules
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronListFirewallRulesRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronListFirewallRulesResponse`
        """
        http_info = self._neutron_list_firewall_rules_http_info(request)
        return self._call_api(**http_info)

    def neutron_list_firewall_rules_invoker(self, request):
        http_info = self._neutron_list_firewall_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_list_firewall_rules_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/fwaas/firewall_rules",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronListFirewallRulesResponse"
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
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))
        if 'tenant_id' in local_var_params:
            query_params.append(('tenant_id', local_var_params['tenant_id']))

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

    def neutron_remove_firewall_rule(self, request):
        """移除网络ACL规则

        从某一网络ACL策略中移除一条网络ACL规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronRemoveFirewallRule
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronRemoveFirewallRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronRemoveFirewallRuleResponse`
        """
        http_info = self._neutron_remove_firewall_rule_http_info(request)
        return self._call_api(**http_info)

    def neutron_remove_firewall_rule_invoker(self, request):
        http_info = self._neutron_remove_firewall_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_remove_firewall_rule_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.0/fwaas/firewall_policies/{firewall_policy_id}/remove_rule",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronRemoveFirewallRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_policy_id' in local_var_params:
            path_params['firewall_policy_id'] = local_var_params['firewall_policy_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def neutron_show_firewall_group(self, request):
        """查询特定网络ACL组详情

        查询特定网络ACL组详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronShowFirewallGroup
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronShowFirewallGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronShowFirewallGroupResponse`
        """
        http_info = self._neutron_show_firewall_group_http_info(request)
        return self._call_api(**http_info)

    def neutron_show_firewall_group_invoker(self, request):
        http_info = self._neutron_show_firewall_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_show_firewall_group_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/fwaas/firewall_groups/{firewall_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronShowFirewallGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_group_id' in local_var_params:
            path_params['firewall_group_id'] = local_var_params['firewall_group_id']

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

    def neutron_show_firewall_policy(self, request):
        """查询特定网络ACL策略详情

        查询特定网络ACL策略详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronShowFirewallPolicy
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronShowFirewallPolicyRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronShowFirewallPolicyResponse`
        """
        http_info = self._neutron_show_firewall_policy_http_info(request)
        return self._call_api(**http_info)

    def neutron_show_firewall_policy_invoker(self, request):
        http_info = self._neutron_show_firewall_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_show_firewall_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/fwaas/firewall_policies/{firewall_policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronShowFirewallPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_policy_id' in local_var_params:
            path_params['firewall_policy_id'] = local_var_params['firewall_policy_id']

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

    def neutron_show_firewall_rule(self, request):
        """查询特定网络ACL规则

        查询特定网络ACL规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronShowFirewallRule
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronShowFirewallRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronShowFirewallRuleResponse`
        """
        http_info = self._neutron_show_firewall_rule_http_info(request)
        return self._call_api(**http_info)

    def neutron_show_firewall_rule_invoker(self, request):
        http_info = self._neutron_show_firewall_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_show_firewall_rule_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/fwaas/firewall_rules/{firewall_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronShowFirewallRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_rule_id' in local_var_params:
            path_params['firewall_rule_id'] = local_var_params['firewall_rule_id']

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

    def neutron_update_firewall_group(self, request):
        """更新网络ACL组

        更新网络ACL组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronUpdateFirewallGroup
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronUpdateFirewallGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronUpdateFirewallGroupResponse`
        """
        http_info = self._neutron_update_firewall_group_http_info(request)
        return self._call_api(**http_info)

    def neutron_update_firewall_group_invoker(self, request):
        http_info = self._neutron_update_firewall_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_update_firewall_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.0/fwaas/firewall_groups/{firewall_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronUpdateFirewallGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_group_id' in local_var_params:
            path_params['firewall_group_id'] = local_var_params['firewall_group_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def neutron_update_firewall_policy(self, request):
        """更新网络ACL策略

        更新网络ACL策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronUpdateFirewallPolicy
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronUpdateFirewallPolicyRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronUpdateFirewallPolicyResponse`
        """
        http_info = self._neutron_update_firewall_policy_http_info(request)
        return self._call_api(**http_info)

    def neutron_update_firewall_policy_invoker(self, request):
        http_info = self._neutron_update_firewall_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_update_firewall_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.0/fwaas/firewall_policies/{firewall_policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronUpdateFirewallPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_policy_id' in local_var_params:
            path_params['firewall_policy_id'] = local_var_params['firewall_policy_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def neutron_update_firewall_rule(self, request):
        """更新网络ACL规则

        更新网络ACL规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NeutronUpdateFirewallRule
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronUpdateFirewallRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronUpdateFirewallRuleResponse`
        """
        http_info = self._neutron_update_firewall_rule_http_info(request)
        return self._call_api(**http_info)

    def neutron_update_firewall_rule_invoker(self, request):
        http_info = self._neutron_update_firewall_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _neutron_update_firewall_rule_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.0/fwaas/firewall_rules/{firewall_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "NeutronUpdateFirewallRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_rule_id' in local_var_params:
            path_params['firewall_rule_id'] = local_var_params['firewall_rule_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_api_version(self, request):
        """查询API版本信息列表

        返回当前API所有可用的版本（仅针对OpenStack原生接口）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApiVersion
        :type request: :class:`huaweicloudsdkvpc.v2.ListApiVersionRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ListApiVersionResponse`
        """
        http_info = self._list_api_version_http_info(request)
        return self._call_api(**http_info)

    def list_api_version_invoker(self, request):
        http_info = self._list_api_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_api_version_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/",
            "request_type": request.__class__.__name__,
            "response_type": "ListApiVersionResponse"
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

    def batch_create_vpc_tags(self, request):
        """批量创建VPC资源标签

        为指定的VPC资源实例批量添加标签。
        此接口为幂等接口：创建时如果请求体中存在重复key则报错。创建时，不允许设置重复key数据，如果数据库已存在该key，就覆盖value的值。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateVpcTags
        :type request: :class:`huaweicloudsdkvpc.v2.BatchCreateVpcTagsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.BatchCreateVpcTagsResponse`
        """
        http_info = self._batch_create_vpc_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_vpc_tags_invoker(self, request):
        http_info = self._batch_create_vpc_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_vpc_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/vpcs/{vpc_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateVpcTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_vpc_tags(self, request):
        """批量删除VPC资源标签

        为指定的VPC资源实例批量删除标签。
        此接口为幂等接口：删除时，如果删除的标签不存在，默认处理成功；删除时不对标签字符集范围做校验。删除时tags结构体不能缺失，key不能为空，或者空字符串。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteVpcTags
        :type request: :class:`huaweicloudsdkvpc.v2.BatchDeleteVpcTagsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.BatchDeleteVpcTagsResponse`
        """
        http_info = self._batch_delete_vpc_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_vpc_tags_invoker(self, request):
        http_info = self._batch_delete_vpc_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_vpc_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/vpcs/{vpc_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteVpcTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_vpc(self, request):
        """创建VPC

        创建虚拟私有云。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateVpc
        :type request: :class:`huaweicloudsdkvpc.v2.CreateVpcRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.CreateVpcResponse`
        """
        http_info = self._create_vpc_http_info(request)
        return self._call_api(**http_info)

    def create_vpc_invoker(self, request):
        http_info = self._create_vpc_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_vpc_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/vpcs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVpcResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_vpc_resource_tag(self, request):
        """创建VPC资源标签

        给指定VPC资源实例增加标签信息
        此接口为幂等接口：创建时，如果创建的标签已经存在（key相同），则覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateVpcResourceTag
        :type request: :class:`huaweicloudsdkvpc.v2.CreateVpcResourceTagRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.CreateVpcResourceTagResponse`
        """
        http_info = self._create_vpc_resource_tag_http_info(request)
        return self._call_api(**http_info)

    def create_vpc_resource_tag_invoker(self, request):
        http_info = self._create_vpc_resource_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_vpc_resource_tag_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/vpcs/{vpc_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVpcResourceTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_vpc_route(self, request):
        """创建VPC路由

        创建路由
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateVpcRoute
        :type request: :class:`huaweicloudsdkvpc.v2.CreateVpcRouteRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.CreateVpcRouteResponse`
        """
        http_info = self._create_vpc_route_http_info(request)
        return self._call_api(**http_info)

    def create_vpc_route_invoker(self, request):
        http_info = self._create_vpc_route_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_vpc_route_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/vpc/routes",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVpcRouteResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_vpc(self, request):
        """删除VPC

        删除虚拟私有云。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteVpc
        :type request: :class:`huaweicloudsdkvpc.v2.DeleteVpcRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.DeleteVpcResponse`
        """
        http_info = self._delete_vpc_http_info(request)
        return self._call_api(**http_info)

    def delete_vpc_invoker(self, request):
        http_info = self._delete_vpc_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_vpc_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/vpcs/{vpc_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVpcResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']

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

    def delete_vpc_route(self, request):
        """删除VPC路由

        删除路由
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteVpcRoute
        :type request: :class:`huaweicloudsdkvpc.v2.DeleteVpcRouteRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.DeleteVpcRouteResponse`
        """
        http_info = self._delete_vpc_route_http_info(request)
        return self._call_api(**http_info)

    def delete_vpc_route_invoker(self, request):
        http_info = self._delete_vpc_route_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_vpc_route_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/vpc/routes/{route_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVpcRouteResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'route_id' in local_var_params:
            path_params['route_id'] = local_var_params['route_id']

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

    def delete_vpc_tag(self, request):
        """删除VPC资源标签

        删除指定VPC资源实例的标签信息
        该接口为幂等接口：删除的key不存在报404，Key不能为空或者空字符串
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteVpcTag
        :type request: :class:`huaweicloudsdkvpc.v2.DeleteVpcTagRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.DeleteVpcTagResponse`
        """
        http_info = self._delete_vpc_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_vpc_tag_invoker(self, request):
        http_info = self._delete_vpc_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_vpc_tag_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/{project_id}/vpcs/{vpc_id}/tags/{key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVpcTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']
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

    def list_vpc_routes(self, request):
        """查询VPC路由列表

        查询提交请求的租户的所有路由列表，并根据过滤条件进行过滤。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVpcRoutes
        :type request: :class:`huaweicloudsdkvpc.v2.ListVpcRoutesRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ListVpcRoutesResponse`
        """
        http_info = self._list_vpc_routes_http_info(request)
        return self._call_api(**http_info)

    def list_vpc_routes_invoker(self, request):
        http_info = self._list_vpc_routes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_vpc_routes_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/vpc/routes",
            "request_type": request.__class__.__name__,
            "response_type": "ListVpcRoutesResponse"
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
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
        if 'destination' in local_var_params:
            query_params.append(('destination', local_var_params['destination']))
        if 'tenant_id' in local_var_params:
            query_params.append(('tenant_id', local_var_params['tenant_id']))

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

    def list_vpc_tags(self, request):
        """查询VPC项目标签

        查询租户在指定区域和实例类型的所有标签集合
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVpcTags
        :type request: :class:`huaweicloudsdkvpc.v2.ListVpcTagsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ListVpcTagsResponse`
        """
        http_info = self._list_vpc_tags_http_info(request)
        return self._call_api(**http_info)

    def list_vpc_tags_invoker(self, request):
        http_info = self._list_vpc_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_vpc_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/vpcs/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListVpcTagsResponse"
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

    def list_vpcs(self, request):
        """查询VPC列表

        查询虚拟私有云列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVpcs
        :type request: :class:`huaweicloudsdkvpc.v2.ListVpcsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ListVpcsResponse`
        """
        http_info = self._list_vpcs_http_info(request)
        return self._call_api(**http_info)

    def list_vpcs_invoker(self, request):
        http_info = self._list_vpcs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_vpcs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/vpcs",
            "request_type": request.__class__.__name__,
            "response_type": "ListVpcsResponse"
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
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
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

    def list_vpcs_by_tags(self, request):
        """查询VPC资源实例

        使用标签过滤实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVpcsByTags
        :type request: :class:`huaweicloudsdkvpc.v2.ListVpcsByTagsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ListVpcsByTagsResponse`
        """
        http_info = self._list_vpcs_by_tags_http_info(request)
        return self._call_api(**http_info)

    def list_vpcs_by_tags_invoker(self, request):
        http_info = self._list_vpcs_by_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_vpcs_by_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/vpcs/resource_instances/action",
            "request_type": request.__class__.__name__,
            "response_type": "ListVpcsByTagsResponse"
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_vpc(self, request):
        """查询VPC

        查询虚拟私有云。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVpc
        :type request: :class:`huaweicloudsdkvpc.v2.ShowVpcRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ShowVpcResponse`
        """
        http_info = self._show_vpc_http_info(request)
        return self._call_api(**http_info)

    def show_vpc_invoker(self, request):
        http_info = self._show_vpc_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_vpc_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/vpcs/{vpc_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVpcResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']

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

    def show_vpc_route(self, request):
        """查询VPC路由

        查询路由详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVpcRoute
        :type request: :class:`huaweicloudsdkvpc.v2.ShowVpcRouteRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ShowVpcRouteResponse`
        """
        http_info = self._show_vpc_route_http_info(request)
        return self._call_api(**http_info)

    def show_vpc_route_invoker(self, request):
        http_info = self._show_vpc_route_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_vpc_route_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/vpc/routes/{route_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVpcRouteResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'route_id' in local_var_params:
            path_params['route_id'] = local_var_params['route_id']

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

    def show_vpc_tags(self, request):
        """查询VPC资源标签

        查询指定VPC实例的标签信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVpcTags
        :type request: :class:`huaweicloudsdkvpc.v2.ShowVpcTagsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ShowVpcTagsResponse`
        """
        http_info = self._show_vpc_tags_http_info(request)
        return self._call_api(**http_info)

    def show_vpc_tags_invoker(self, request):
        http_info = self._show_vpc_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_vpc_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/vpcs/{vpc_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVpcTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']

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

    def update_vpc(self, request):
        """更新VPC

        更新虚拟私有云。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateVpc
        :type request: :class:`huaweicloudsdkvpc.v2.UpdateVpcRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.UpdateVpcResponse`
        """
        http_info = self._update_vpc_http_info(request)
        return self._call_api(**http_info)

    def update_vpc_invoker(self, request):
        http_info = self._update_vpc_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_vpc_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/vpcs/{vpc_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateVpcResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

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
