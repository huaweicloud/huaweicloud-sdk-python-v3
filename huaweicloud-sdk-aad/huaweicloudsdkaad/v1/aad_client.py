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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkaad'")


class AadClient(Client):
    def __init__(self):
        super(AadClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkaad.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials")
        else:
            if clazz.__name__ != "AadClient":
                raise TypeError("client type error, support client type is AadClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials")

        

        return client_builder

    def add_black_white_ip_list(self, request):
        r"""高防实例添加黑白名单

        高防实例添加黑白名单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddBlackWhiteIpList
        :type request: :class:`huaweicloudsdkaad.v1.AddBlackWhiteIpListRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.AddBlackWhiteIpListResponse`
        """
        http_info = self._add_black_white_ip_list_http_info(request)
        return self._call_api(**http_info)

    def add_black_white_ip_list_invoker(self, request):
        http_info = self._add_black_white_ip_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_black_white_ip_list_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/aad/external/bwlist",
            "request_type": request.__class__.__name__,
            "response_type": "AddBlackWhiteIpListResponse"
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

    def add_policy_black_and_white_ip_list(self, request):
        r"""策略添加黑白名单

        策略添加黑白名单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddPolicyBlackAndWhiteIpList
        :type request: :class:`huaweicloudsdkaad.v1.AddPolicyBlackAndWhiteIpListRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.AddPolicyBlackAndWhiteIpListResponse`
        """
        http_info = self._add_policy_black_and_white_ip_list_http_info(request)
        return self._call_api(**http_info)

    def add_policy_black_and_white_ip_list_invoker(self, request):
        http_info = self._add_policy_black_and_white_ip_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_policy_black_and_white_ip_list_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/cnad/policies/{policy_id}/ip-list/add",
            "request_type": request.__class__.__name__,
            "response_type": "AddPolicyBlackAndWhiteIpListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def associate_ip_to_policy(self, request):
        r"""策略绑定防护对象

        策略绑定防护对象
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateIpToPolicy
        :type request: :class:`huaweicloudsdkaad.v1.AssociateIpToPolicyRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.AssociateIpToPolicyResponse`
        """
        http_info = self._associate_ip_to_policy_http_info(request)
        return self._call_api(**http_info)

    def associate_ip_to_policy_invoker(self, request):
        http_info = self._associate_ip_to_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _associate_ip_to_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/cnad/policies/{policy_id}/bind",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateIpToPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def associate_ip_to_policy_and_package(self, request):
        r"""策略和实例绑定防护对象

        策略和实例绑定防护对象
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateIpToPolicyAndPackage
        :type request: :class:`huaweicloudsdkaad.v1.AssociateIpToPolicyAndPackageRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.AssociateIpToPolicyAndPackageResponse`
        """
        http_info = self._associate_ip_to_policy_and_package_http_info(request)
        return self._call_api(**http_info)

    def associate_ip_to_policy_and_package_invoker(self, request):
        http_info = self._associate_ip_to_policy_and_package_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _associate_ip_to_policy_and_package_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/cnad/policies/{policy_id}/bind",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateIpToPolicyAndPackageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def batch_create_instance_ip_rule(self, request):
        r"""批量创建高防实例IP的转发规则

        批量创建高防实例IP的转发规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateInstanceIpRule
        :type request: :class:`huaweicloudsdkaad.v1.BatchCreateInstanceIpRuleRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.BatchCreateInstanceIpRuleResponse`
        """
        http_info = self._batch_create_instance_ip_rule_http_info(request)
        return self._call_api(**http_info)

    def batch_create_instance_ip_rule_invoker(self, request):
        http_info = self._batch_create_instance_ip_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_instance_ip_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/aad/instances/{instance_id}/{ip}/rules/batch-create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateInstanceIpRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'ip' in local_var_params:
            path_params['ip'] = local_var_params['ip']

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

    def batch_delete_instance_ip_rule(self, request):
        r"""批量删除高防实例IP的转发规则

        批量删除高防实例IP的转发规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteInstanceIpRule
        :type request: :class:`huaweicloudsdkaad.v1.BatchDeleteInstanceIpRuleRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.BatchDeleteInstanceIpRuleResponse`
        """
        http_info = self._batch_delete_instance_ip_rule_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_instance_ip_rule_invoker(self, request):
        http_info = self._batch_delete_instance_ip_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_instance_ip_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/aad/instances/{instance_id}/{ip}/rules/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteInstanceIpRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'ip' in local_var_params:
            path_params['ip'] = local_var_params['ip']

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

    def create_aad_domain(self, request):
        r"""创建防护域名

        创建防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAadDomain
        :type request: :class:`huaweicloudsdkaad.v1.CreateAadDomainRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.CreateAadDomainResponse`
        """
        http_info = self._create_aad_domain_http_info(request)
        return self._call_api(**http_info)

    def create_aad_domain_invoker(self, request):
        http_info = self._create_aad_domain_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_aad_domain_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/aad/external/domains",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAadDomainResponse"
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

    def create_policy(self, request):
        r"""创建策略

        创建策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePolicy
        :type request: :class:`huaweicloudsdkaad.v1.CreatePolicyRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.CreatePolicyResponse`
        """
        http_info = self._create_policy_http_info(request)
        return self._call_api(**http_info)

    def create_policy_invoker(self, request):
        http_info = self._create_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/cnad/policies",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePolicyResponse"
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

    def delete_alarm_config(self, request):
        r"""删除告警配置

        删除告警配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAlarmConfig
        :type request: :class:`huaweicloudsdkaad.v1.DeleteAlarmConfigRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.DeleteAlarmConfigResponse`
        """
        http_info = self._delete_alarm_config_http_info(request)
        return self._call_api(**http_info)

    def delete_alarm_config_invoker(self, request):
        http_info = self._delete_alarm_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_alarm_config_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/cnad/alarm-config",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAlarmConfigResponse"
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

    def delete_black_white_ip_list(self, request):
        r"""高防实例删除黑白名单

        高防实例删除黑白名单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBlackWhiteIpList
        :type request: :class:`huaweicloudsdkaad.v1.DeleteBlackWhiteIpListRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.DeleteBlackWhiteIpListResponse`
        """
        http_info = self._delete_black_white_ip_list_http_info(request)
        return self._call_api(**http_info)

    def delete_black_white_ip_list_invoker(self, request):
        http_info = self._delete_black_white_ip_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_black_white_ip_list_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/aad/external/bwlist",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBlackWhiteIpListResponse"
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

    def delete_policy(self, request):
        r"""删除策略

        删除策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePolicy
        :type request: :class:`huaweicloudsdkaad.v1.DeletePolicyRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.DeletePolicyResponse`
        """
        http_info = self._delete_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_policy_invoker(self, request):
        http_info = self._delete_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_policy_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/cnad/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def delete_policy_black_and_white_ip_list(self, request):
        r"""策略删除黑白名单

        策略删除黑白名单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePolicyBlackAndWhiteIpList
        :type request: :class:`huaweicloudsdkaad.v1.DeletePolicyBlackAndWhiteIpListRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.DeletePolicyBlackAndWhiteIpListResponse`
        """
        http_info = self._delete_policy_black_and_white_ip_list_http_info(request)
        return self._call_api(**http_info)

    def delete_policy_black_and_white_ip_list_invoker(self, request):
        http_info = self._delete_policy_black_and_white_ip_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_policy_black_and_white_ip_list_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/cnad/policies/{policy_id}/ip-list/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePolicyBlackAndWhiteIpListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def disassociate_ip_from_policy(self, request):
        r"""策略解绑防护对象

        策略解绑防护对象
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisassociateIpFromPolicy
        :type request: :class:`huaweicloudsdkaad.v1.DisassociateIpFromPolicyRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.DisassociateIpFromPolicyResponse`
        """
        http_info = self._disassociate_ip_from_policy_http_info(request)
        return self._call_api(**http_info)

    def disassociate_ip_from_policy_invoker(self, request):
        http_info = self._disassociate_ip_from_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disassociate_ip_from_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/cnad/policies/{policy_id}/unbind",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateIpFromPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def disassociate_ip_from_policy_and_package(self, request):
        r"""策略和实例解绑防护对象

        策略和实例解绑防护对象
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisassociateIpFromPolicyAndPackage
        :type request: :class:`huaweicloudsdkaad.v1.DisassociateIpFromPolicyAndPackageRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.DisassociateIpFromPolicyAndPackageResponse`
        """
        http_info = self._disassociate_ip_from_policy_and_package_http_info(request)
        return self._call_api(**http_info)

    def disassociate_ip_from_policy_and_package_invoker(self, request):
        http_info = self._disassociate_ip_from_policy_and_package_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disassociate_ip_from_policy_and_package_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/cnad/policies/{policy_id}/unbind",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateIpFromPolicyAndPackageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def list_domain(self, request):
        r"""查询域名列表

        查询域名列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDomain
        :type request: :class:`huaweicloudsdkaad.v1.ListDomainRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.ListDomainResponse`
        """
        http_info = self._list_domain_http_info(request)
        return self._call_api(**http_info)

    def list_domain_invoker(self, request):
        http_info = self._list_domain_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_domain_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/aad/protected-domains",
            "request_type": request.__class__.__name__,
            "response_type": "ListDomainResponse"
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

    def list_instance(self, request):
        r"""查询高防实例列表

        查询高防实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstance
        :type request: :class:`huaweicloudsdkaad.v1.ListInstanceRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.ListInstanceResponse`
        """
        http_info = self._list_instance_http_info(request)
        return self._call_api(**http_info)

    def list_instance_invoker(self, request):
        http_info = self._list_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/aad/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceResponse"
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

    def list_instance_id(self, request):
        r"""查询域名关联的实例ID

        查询域名关联的实例ID
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceId
        :type request: :class:`huaweicloudsdkaad.v1.ListInstanceIdRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.ListInstanceIdResponse`
        """
        http_info = self._list_instance_id_http_info(request)
        return self._call_api(**http_info)

    def list_instance_id_invoker(self, request):
        http_info = self._list_instance_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/aad/protected-domains/{domain_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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

    def list_instance_ip_rule(self, request):
        r"""查询高防实例IP的转发规则列表

        查询高防实例IP的转发规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceIpRule
        :type request: :class:`huaweicloudsdkaad.v1.ListInstanceIpRuleRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.ListInstanceIpRuleResponse`
        """
        http_info = self._list_instance_ip_rule_http_info(request)
        return self._call_api(**http_info)

    def list_instance_ip_rule_invoker(self, request):
        http_info = self._list_instance_ip_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_ip_rule_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/aad/instances/{instance_id}/{ip}/rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceIpRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'ip' in local_var_params:
            path_params['ip'] = local_var_params['ip']

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

    def list_package(self, request):
        r"""查询实例列表

        查询实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPackage
        :type request: :class:`huaweicloudsdkaad.v1.ListPackageRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.ListPackageResponse`
        """
        http_info = self._list_package_http_info(request)
        return self._call_api(**http_info)

    def list_package_invoker(self, request):
        http_info = self._list_package_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_package_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/cnad/packages",
            "request_type": request.__class__.__name__,
            "response_type": "ListPackageResponse"
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

    def list_peak(self, request):
        r"""查询流量峰值、攻击计数

        查询流量峰值、攻击计数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPeak
        :type request: :class:`huaweicloudsdkaad.v1.ListPeakRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.ListPeakResponse`
        """
        http_info = self._list_peak_http_info(request)
        return self._call_api(**http_info)

    def list_peak_invoker(self, request):
        http_info = self._list_peak_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_peak_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/aad/instances/{instance_id}/{ip}/ddos-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ListPeakResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'ip' in local_var_params:
            path_params['ip'] = local_var_params['ip']

        query_params = []
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

    def list_policy(self, request):
        r"""查询策略列表

        查询策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPolicy
        :type request: :class:`huaweicloudsdkaad.v1.ListPolicyRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.ListPolicyResponse`
        """
        http_info = self._list_policy_http_info(request)
        return self._call_api(**http_info)

    def list_policy_invoker(self, request):
        http_info = self._list_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/cnad/policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'policy_name' in local_var_params:
            query_params.append(('policy_name', local_var_params['policy_name']))

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

    def list_protected_ip(self, request):
        r"""查询防护对象列表

        查询防护对象列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProtectedIp
        :type request: :class:`huaweicloudsdkaad.v1.ListProtectedIpRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.ListProtectedIpResponse`
        """
        http_info = self._list_protected_ip_http_info(request)
        return self._call_api(**http_info)

    def list_protected_ip_invoker(self, request):
        http_info = self._list_protected_ip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_protected_ip_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/cnad/protected-ips",
            "request_type": request.__class__.__name__,
            "response_type": "ListProtectedIpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'package_id' in local_var_params:
            query_params.append(('package_id', local_var_params['package_id']))
        if 'policy_id' in local_var_params:
            query_params.append(('policy_id', local_var_params['policy_id']))
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))

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

    def list_source_ips(self, request):
        r"""查询高防回源IP段列表

        查询高防回源IP段列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSourceIps
        :type request: :class:`huaweicloudsdkaad.v1.ListSourceIpsRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.ListSourceIpsResponse`
        """
        http_info = self._list_source_ips_http_info(request)
        return self._call_api(**http_info)

    def list_source_ips_invoker(self, request):
        http_info = self._list_source_ips_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_source_ips_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/aad/external/source-ip",
            "request_type": request.__class__.__name__,
            "response_type": "ListSourceIpsResponse"
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

    def list_unbound_protected_ip(self, request):
        r"""查询可绑定的防护对象列表

        查询可绑定的防护对象列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUnboundProtectedIp
        :type request: :class:`huaweicloudsdkaad.v1.ListUnboundProtectedIpRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.ListUnboundProtectedIpResponse`
        """
        http_info = self._list_unbound_protected_ip_http_info(request)
        return self._call_api(**http_info)

    def list_unbound_protected_ip_invoker(self, request):
        http_info = self._list_unbound_protected_ip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_unbound_protected_ip_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/cnad/packages/{package_id}/unbound-protected-ips",
            "request_type": request.__class__.__name__,
            "response_type": "ListUnboundProtectedIpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'package_id' in local_var_params:
            path_params['package_id'] = local_var_params['package_id']

        query_params = []
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

    def modify_domain_web_switch(self, request):
        r"""修改域名WEB基础防护开关/CC防护开关

        修改域名WEB基础防护开关/CC防护开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyDomainWebSwitch
        :type request: :class:`huaweicloudsdkaad.v1.ModifyDomainWebSwitchRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.ModifyDomainWebSwitchResponse`
        """
        http_info = self._modify_domain_web_switch_http_info(request)
        return self._call_api(**http_info)

    def modify_domain_web_switch_invoker(self, request):
        http_info = self._modify_domain_web_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_domain_web_switch_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/aad/external/domains/switch",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyDomainWebSwitchResponse"
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

    def set_cert_for_domain(self, request):
        r"""上传/修改域名对应证书

        上传/修改域名对应证书
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetCertForDomain
        :type request: :class:`huaweicloudsdkaad.v1.SetCertForDomainRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.SetCertForDomainResponse`
        """
        http_info = self._set_cert_for_domain_http_info(request)
        return self._call_api(**http_info)

    def set_cert_for_domain_invoker(self, request):
        http_info = self._set_cert_for_domain_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_cert_for_domain_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/aad/external/domains/certificate",
            "request_type": request.__class__.__name__,
            "response_type": "SetCertForDomainResponse"
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

    def show_alarm_config(self, request):
        r"""查询告警配置

        查询告警配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAlarmConfig
        :type request: :class:`huaweicloudsdkaad.v1.ShowAlarmConfigRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.ShowAlarmConfigResponse`
        """
        http_info = self._show_alarm_config_http_info(request)
        return self._call_api(**http_info)

    def show_alarm_config_invoker(self, request):
        http_info = self._show_alarm_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_alarm_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/cnad/alarm-config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAlarmConfigResponse"
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

    def show_policy(self, request):
        r"""查询策略详情

        查询策略详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPolicy
        :type request: :class:`huaweicloudsdkaad.v1.ShowPolicyRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.ShowPolicyResponse`
        """
        http_info = self._show_policy_http_info(request)
        return self._call_api(**http_info)

    def show_policy_invoker(self, request):
        http_info = self._show_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/cnad/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def update_alarm_config(self, request):
        r"""设置告警配置

        设置告警配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAlarmConfig
        :type request: :class:`huaweicloudsdkaad.v1.UpdateAlarmConfigRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.UpdateAlarmConfigResponse`
        """
        http_info = self._update_alarm_config_http_info(request)
        return self._call_api(**http_info)

    def update_alarm_config_invoker(self, request):
        http_info = self._update_alarm_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_alarm_config_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/cnad/alarm-config",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAlarmConfigResponse"
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

    def update_domain(self, request):
        r"""更新域名信息

        更新域名源站配置信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDomain
        :type request: :class:`huaweicloudsdkaad.v1.UpdateDomainRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.UpdateDomainResponse`
        """
        http_info = self._update_domain_http_info(request)
        return self._call_api(**http_info)

    def update_domain_invoker(self, request):
        http_info = self._update_domain_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_domain_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/aad/protected-domains/{domain_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDomainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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

    def update_instance_ip_rule(self, request):
        r"""修改高防实例转发配置的源站IP

        修改高防实例转发配置的源站IP
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceIpRule
        :type request: :class:`huaweicloudsdkaad.v1.UpdateInstanceIpRuleRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.UpdateInstanceIpRuleResponse`
        """
        http_info = self._update_instance_ip_rule_http_info(request)
        return self._call_api(**http_info)

    def update_instance_ip_rule_invoker(self, request):
        http_info = self._update_instance_ip_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_ip_rule_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/aad/instances/{instance_id}/{ip}/rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceIpRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'ip' in local_var_params:
            path_params['ip'] = local_var_params['ip']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def update_package_ip(self, request):
        r"""更新实例绑定的全量防护对象

        更新实例绑定的全量防护对象
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePackageIp
        :type request: :class:`huaweicloudsdkaad.v1.UpdatePackageIpRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.UpdatePackageIpResponse`
        """
        http_info = self._update_package_ip_http_info(request)
        return self._call_api(**http_info)

    def update_package_ip_invoker(self, request):
        http_info = self._update_package_ip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_package_ip_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/cnad/packages/{package_id}/protected-ips",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePackageIpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'package_id' in local_var_params:
            path_params['package_id'] = local_var_params['package_id']

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

    def update_package_name(self, request):
        r"""更新实例名字

        更新实例名字
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePackageName
        :type request: :class:`huaweicloudsdkaad.v1.UpdatePackageNameRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.UpdatePackageNameResponse`
        """
        http_info = self._update_package_name_http_info(request)
        return self._call_api(**http_info)

    def update_package_name_invoker(self, request):
        http_info = self._update_package_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_package_name_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/cnad/packages/{package_id}/name",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePackageNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'package_id' in local_var_params:
            path_params['package_id'] = local_var_params['package_id']

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

    def update_policy(self, request):
        r"""更新策略

        更新策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePolicy
        :type request: :class:`huaweicloudsdkaad.v1.UpdatePolicyRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.UpdatePolicyResponse`
        """
        http_info = self._update_policy_http_info(request)
        return self._call_api(**http_info)

    def update_policy_invoker(self, request):
        http_info = self._update_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/cnad/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def update_tag_for_protected_ip(self, request):
        r"""防护对象设置标签

        防护对象设置标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTagForProtectedIp
        :type request: :class:`huaweicloudsdkaad.v1.UpdateTagForProtectedIpRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.UpdateTagForProtectedIpResponse`
        """
        http_info = self._update_tag_for_protected_ip_http_info(request)
        return self._call_api(**http_info)

    def update_tag_for_protected_ip_invoker(self, request):
        http_info = self._update_tag_for_protected_ip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_tag_for_protected_ip_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/cnad/protected-ips/tags",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTagForProtectedIpResponse"
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

    def execute_unblock_ip(self, request):
        r"""解封IP

        解封IP
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteUnblockIp
        :type request: :class:`huaweicloudsdkaad.v1.ExecuteUnblockIpRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.ExecuteUnblockIpResponse`
        """
        http_info = self._execute_unblock_ip_http_info(request)
        return self._call_api(**http_info)

    def execute_unblock_ip_invoker(self, request):
        http_info = self._execute_unblock_ip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_unblock_ip_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/unblockservice/{domain_id}/unblock",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteUnblockIpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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

    def list_block_ips(self, request):
        r"""查询租户封堵列表

        查询租户封堵列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBlockIps
        :type request: :class:`huaweicloudsdkaad.v1.ListBlockIpsRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.ListBlockIpsResponse`
        """
        http_info = self._list_block_ips_http_info(request)
        return self._call_api(**http_info)

    def list_block_ips_invoker(self, request):
        http_info = self._list_block_ips_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_block_ips_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/unblockservice/{domain_id}/block-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListBlockIpsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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

    def list_unblock_quota_statistics(self, request):
        r"""查询解封配额

        查询解封配额
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUnblockQuotaStatistics
        :type request: :class:`huaweicloudsdkaad.v1.ListUnblockQuotaStatisticsRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.ListUnblockQuotaStatisticsResponse`
        """
        http_info = self._list_unblock_quota_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_unblock_quota_statistics_invoker(self, request):
        http_info = self._list_unblock_quota_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_unblock_quota_statistics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/unblockservice/{domain_id}/unblock-quota-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ListUnblockQuotaStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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

    def show_block_statistics(self, request):
        r"""查询封堵统计数据

        查询封堵统计数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBlockStatistics
        :type request: :class:`huaweicloudsdkaad.v1.ShowBlockStatisticsRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.ShowBlockStatisticsResponse`
        """
        http_info = self._show_block_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_block_statistics_invoker(self, request):
        http_info = self._show_block_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_block_statistics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/unblockservice/{domain_id}/block-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBlockStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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

    def show_unblock_record(self, request):
        r"""查询租户解封记录

        查询租户解封记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUnblockRecord
        :type request: :class:`huaweicloudsdkaad.v1.ShowUnblockRecordRequest`
        :rtype: :class:`huaweicloudsdkaad.v1.ShowUnblockRecordResponse`
        """
        http_info = self._show_unblock_record_http_info(request)
        return self._call_api(**http_info)

    def show_unblock_record_invoker(self, request):
        http_info = self._show_unblock_record_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_unblock_record_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/unblockservice/{domain_id}/unblock-record",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUnblockRecordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
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
