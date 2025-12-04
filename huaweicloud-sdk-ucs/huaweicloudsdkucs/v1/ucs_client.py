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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkucs'")


class UcsClient(Client):
    def __init__(self):
        super().__init__()
        self.model_package = importlib.import_module("huaweicloudsdkucs.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials")
        else:
            if clazz.__name__ != "UcsClient":
                raise TypeError("client type error, support client type is UcsClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials")

        

        return client_builder

    def create_addon_instance(self, request):
        r"""安装插件实例

        安装插件实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAddonInstance
        :type request: :class:`huaweicloudsdkucs.v1.CreateAddonInstanceRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.CreateAddonInstanceResponse`
        """
        http_info = self._create_addon_instance_http_info(request)
        return self._call_api(**http_info)

    def create_addon_instance_invoker(self, request):
        http_info = self._create_addon_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_addon_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/addons",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAddonInstanceResponse"
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

    def create_cluster_group_policy_instance(self, request):
        r"""创建舰队策略实例

        创建舰队策略实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateClusterGroupPolicyInstance
        :type request: :class:`huaweicloudsdkucs.v1.CreateClusterGroupPolicyInstanceRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.CreateClusterGroupPolicyInstanceResponse`
        """
        http_info = self._create_cluster_group_policy_instance_http_info(request)
        return self._call_api(**http_info)

    def create_cluster_group_policy_instance_invoker(self, request):
        http_info = self._create_cluster_group_policy_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_cluster_group_policy_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/clustergroups/{clustergroupid}/policyinstance",
            "request_type": request.__class__.__name__,
            "response_type": "CreateClusterGroupPolicyInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clustergroupid' in local_var_params:
            path_params['clustergroupid'] = local_var_params['clustergroupid']

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

    def create_config_set(self, request):
        r"""创建配置集合

        创建配置集合
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateConfigSet
        :type request: :class:`huaweicloudsdkucs.v1.CreateConfigSetRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.CreateConfigSetResponse`
        """
        http_info = self._create_config_set_http_info(request)
        return self._call_api(**http_info)

    def create_config_set_invoker(self, request):
        http_info = self._create_config_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_config_set_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/configsets",
            "request_type": request.__class__.__name__,
            "response_type": "CreateConfigSetResponse"
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

    def create_federation_cert(self, request):
        r"""创建联邦网络连接并下载联邦kubeconfig

        舰队开通联邦后，调用此接口，创建vpcep终端节点，连接到联邦apiserver，并下载联邦apiserver的kubeconfig
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFederationCert
        :type request: :class:`huaweicloudsdkucs.v1.CreateFederationCertRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.CreateFederationCertResponse`
        """
        http_info = self._create_federation_cert_http_info(request)
        return self._call_api(**http_info)

    def create_federation_cert_invoker(self, request):
        http_info = self._create_federation_cert_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_federation_cert_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/clustergroups/{clustergroupid}/cert",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFederationCertResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clustergroupid' in local_var_params:
            path_params['clustergroupid'] = local_var_params['clustergroupid']

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

    def create_federation_connection(self, request):
        r"""创建联邦网络连接

        舰队开通联邦后，创建vpcep终端节点连接到联邦apiserver
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFederationConnection
        :type request: :class:`huaweicloudsdkucs.v1.CreateFederationConnectionRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.CreateFederationConnectionResponse`
        """
        http_info = self._create_federation_connection_http_info(request)
        return self._call_api(**http_info)

    def create_federation_connection_invoker(self, request):
        http_info = self._create_federation_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_federation_connection_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/clustergroups/{clustergroupid}/connection",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFederationConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clustergroupid' in local_var_params:
            path_params['clustergroupid'] = local_var_params['clustergroupid']

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

    def create_proxy_united_workload(self, request):
        r"""创建联邦工作负载

        创建联邦工作负载
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateProxyUnitedWorkload
        :type request: :class:`huaweicloudsdkucs.v1.CreateProxyUnitedWorkloadRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.CreateProxyUnitedWorkloadResponse`
        """
        http_info = self._create_proxy_united_workload_http_info(request)
        return self._call_api(**http_info)

    def create_proxy_united_workload_invoker(self, request):
        http_info = self._create_proxy_united_workload_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_proxy_united_workload_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/clustergroups/{clustergroupid}/unitedworkload",
            "request_type": request.__class__.__name__,
            "response_type": "CreateProxyUnitedWorkloadResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clustergroupid' in local_var_params:
            path_params['clustergroupid'] = local_var_params['clustergroupid']

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

    def create_record_set(self, request):
        r"""创建域名解析记录集

        创建域名解析记录集
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRecordSet
        :type request: :class:`huaweicloudsdkucs.v1.CreateRecordSetRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.CreateRecordSetResponse`
        """
        http_info = self._create_record_set_http_info(request)
        return self._call_api(**http_info)

    def create_record_set_invoker(self, request):
        http_info = self._create_record_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_record_set_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/traffic/recordsets",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRecordSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_zone_project_id' in local_var_params:
            header_params['X-Zone-Project-ID'] = local_var_params['x_zone_project_id']
        if 'x_zone_id' in local_var_params:
            header_params['X-Zone-ID'] = local_var_params['x_zone_id']

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

    def create_repo(self, request):
        r"""创建仓库源

        创建仓库源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRepo
        :type request: :class:`huaweicloudsdkucs.v1.CreateRepoRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.CreateRepoResponse`
        """
        http_info = self._create_repo_http_info(request)
        return self._call_api(**http_info)

    def create_repo_invoker(self, request):
        http_info = self._create_repo_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_repo_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/configsets/repos",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRepoResponse"
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

    def create_rule(self, request):
        r"""创建权限策略

        创建权限策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRule
        :type request: :class:`huaweicloudsdkucs.v1.CreateRuleRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.CreateRuleResponse`
        """
        http_info = self._create_rule_http_info(request)
        return self._call_api(**http_info)

    def create_rule_invoker(self, request):
        http_info = self._create_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/permissions/rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}
        if 'metadata' in local_var_params:
            form_params['metadata'] = local_var_params['metadata']
        if 'spec' in local_var_params:
            form_params['spec'] = local_var_params['spec']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/x-www-form-urlencoded'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_addon_instance(self, request):
        r"""卸载插件实例

        卸载插件实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAddonInstance
        :type request: :class:`huaweicloudsdkucs.v1.DeleteAddonInstanceRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.DeleteAddonInstanceResponse`
        """
        http_info = self._delete_addon_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_addon_instance_invoker(self, request):
        http_info = self._delete_addon_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_addon_instance_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/addons/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAddonInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))

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

    def delete_cluster_group(self, request):
        r"""删除容器舰队

        容器舰队删除接口，只有在容器舰队为空时才可以删除该容器舰队，若需删除请先将集群移出容器舰队；传入的cluster ID必须符合k8s UUID的格式规则；同时需要用户有对应集群的操作权限，否则会鉴权失败
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteClusterGroup
        :type request: :class:`huaweicloudsdkucs.v1.DeleteClusterGroupRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.DeleteClusterGroupResponse`
        """
        http_info = self._delete_cluster_group_http_info(request)
        return self._call_api(**http_info)

    def delete_cluster_group_invoker(self, request):
        http_info = self._delete_cluster_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_cluster_group_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/clustergroups/{clustergroupid}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteClusterGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clustergroupid' in local_var_params:
            path_params['clustergroupid'] = local_var_params['clustergroupid']

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

    def delete_config_set(self, request):
        r"""删除配置集合

        仅删除配置集合，不删除仓库源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteConfigSet
        :type request: :class:`huaweicloudsdkucs.v1.DeleteConfigSetRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.DeleteConfigSetResponse`
        """
        http_info = self._delete_config_set_http_info(request)
        return self._call_api(**http_info)

    def delete_config_set_invoker(self, request):
        http_info = self._delete_config_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_config_set_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/configsets/{configsetid}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteConfigSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'configsetid' in local_var_params:
            path_params['configsetid'] = local_var_params['configsetid']

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

    def delete_policy_instance(self, request):
        r"""删除指定策略实例

        删除指定策略实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePolicyInstance
        :type request: :class:`huaweicloudsdkucs.v1.DeletePolicyInstanceRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.DeletePolicyInstanceResponse`
        """
        http_info = self._delete_policy_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_policy_instance_invoker(self, request):
        http_info = self._delete_policy_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_policy_instance_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/policyinstances/{policyinstanceid}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePolicyInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policyinstanceid' in local_var_params:
            path_params['policyinstanceid'] = local_var_params['policyinstanceid']

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

    def delete_proxy_united_workload(self, request):
        r"""删除联邦工作负载

        删除联邦工作负载
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteProxyUnitedWorkload
        :type request: :class:`huaweicloudsdkucs.v1.DeleteProxyUnitedWorkloadRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.DeleteProxyUnitedWorkloadResponse`
        """
        http_info = self._delete_proxy_united_workload_http_info(request)
        return self._call_api(**http_info)

    def delete_proxy_united_workload_invoker(self, request):
        http_info = self._delete_proxy_united_workload_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_proxy_united_workload_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/clustergroups/{clustergroupid}/unitedworkload",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteProxyUnitedWorkloadResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clustergroupid' in local_var_params:
            path_params['clustergroupid'] = local_var_params['clustergroupid']

        query_params = []
        if 'kind' in local_var_params:
            query_params.append(('kind', local_var_params['kind']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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

    def delete_repo(self, request):
        r"""删除仓库源

        删除仓库源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRepo
        :type request: :class:`huaweicloudsdkucs.v1.DeleteRepoRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.DeleteRepoResponse`
        """
        http_info = self._delete_repo_http_info(request)
        return self._call_api(**http_info)

    def delete_repo_invoker(self, request):
        http_info = self._delete_repo_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_repo_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/configsets/repos/{repoid}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRepoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repoid' in local_var_params:
            path_params['repoid'] = local_var_params['repoid']

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

    def delete_rule(self, request):
        r"""删除权限策略

        删除权限策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRule
        :type request: :class:`huaweicloudsdkucs.v1.DeleteRuleRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.DeleteRuleResponse`
        """
        http_info = self._delete_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_rule_invoker(self, request):
        http_info = self._delete_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_rule_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/permissions/rules/{ruleid}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ruleid' in local_var_params:
            path_params['ruleid'] = local_var_params['ruleid']

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

    def disable_cluster_group_policy(self, request):
        r"""舰队关闭策略中心

        舰队关闭策略中心
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisableClusterGroupPolicy
        :type request: :class:`huaweicloudsdkucs.v1.DisableClusterGroupPolicyRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.DisableClusterGroupPolicyResponse`
        """
        http_info = self._disable_cluster_group_policy_http_info(request)
        return self._call_api(**http_info)

    def disable_cluster_group_policy_invoker(self, request):
        http_info = self._disable_cluster_group_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disable_cluster_group_policy_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/clustergroups/{clustergroupid}/policy",
            "request_type": request.__class__.__name__,
            "response_type": "DisableClusterGroupPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clustergroupid' in local_var_params:
            path_params['clustergroupid'] = local_var_params['clustergroupid']

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

    def disable_federation(self, request):
        r"""关闭容器集群联邦

        关闭容器舰队联邦
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisableFederation
        :type request: :class:`huaweicloudsdkucs.v1.DisableFederationRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.DisableFederationResponse`
        """
        http_info = self._disable_federation_http_info(request)
        return self._call_api(**http_info)

    def disable_federation_invoker(self, request):
        http_info = self._disable_federation_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disable_federation_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/clustergroups/{clustergroupid}/federations",
            "request_type": request.__class__.__name__,
            "response_type": "DisableFederationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clustergroupid' in local_var_params:
            path_params['clustergroupid'] = local_var_params['clustergroupid']

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

    def download_federation_kubeconfig(self, request):
        r"""下载联邦kubeconfig

        舰队开通联邦并且创建网络连接之后，可以使用此接口下载联邦的kubeconfig
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadFederationKubeconfig
        :type request: :class:`huaweicloudsdkucs.v1.DownloadFederationKubeconfigRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.DownloadFederationKubeconfigResponse`
        """
        http_info = self._download_federation_kubeconfig_http_info(request)
        return self._call_api(**http_info)

    def download_federation_kubeconfig_invoker(self, request):
        http_info = self._download_federation_kubeconfig_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_federation_kubeconfig_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/clustergroups/{clustergroupid}/kubeconfig",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadFederationKubeconfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clustergroupid' in local_var_params:
            path_params['clustergroupid'] = local_var_params['clustergroupid']

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

    def enable_cluster_group_policy(self, request):
        r"""舰队启用策略中心

        舰队启用策略中心
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableClusterGroupPolicy
        :type request: :class:`huaweicloudsdkucs.v1.EnableClusterGroupPolicyRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.EnableClusterGroupPolicyResponse`
        """
        http_info = self._enable_cluster_group_policy_http_info(request)
        return self._call_api(**http_info)

    def enable_cluster_group_policy_invoker(self, request):
        http_info = self._enable_cluster_group_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_cluster_group_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/clustergroups/{clustergroupid}/policy",
            "request_type": request.__class__.__name__,
            "response_type": "EnableClusterGroupPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clustergroupid' in local_var_params:
            path_params['clustergroupid'] = local_var_params['clustergroupid']

        query_params = []
        if 'retry' in local_var_params:
            query_params.append(('retry', local_var_params['retry']))

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

    def enable_federation(self, request):
        r"""启用容器舰队联邦

        启用容器舰队联邦
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableFederation
        :type request: :class:`huaweicloudsdkucs.v1.EnableFederationRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.EnableFederationResponse`
        """
        http_info = self._enable_federation_http_info(request)
        return self._call_api(**http_info)

    def enable_federation_invoker(self, request):
        http_info = self._enable_federation_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_federation_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/clustergroups/{clustergroupid}/federations",
            "request_type": request.__class__.__name__,
            "response_type": "EnableFederationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clustergroupid' in local_var_params:
            path_params['clustergroupid'] = local_var_params['clustergroupid']

        query_params = []
        if 'retryjoinall' in local_var_params:
            query_params.append(('retryjoinall', local_var_params['retryjoinall']))

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

    def join_group(self, request):
        r"""集群加入容器舰队

        集群加入容器舰队
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for JoinGroup
        :type request: :class:`huaweicloudsdkucs.v1.JoinGroupRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.JoinGroupResponse`
        """
        http_info = self._join_group_http_info(request)
        return self._call_api(**http_info)

    def join_group_invoker(self, request):
        http_info = self._join_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _join_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/clusters/{clusterid}/join",
            "request_type": request.__class__.__name__,
            "response_type": "JoinGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clusterid' in local_var_params:
            path_params['clusterid'] = local_var_params['clusterid']

        query_params = []

        header_params = {}

        form_params = {}
        if 'cluster_group_id' in local_var_params:
            form_params['clusterGroupID'] = local_var_params['cluster_group_id']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/x-www-form-urlencoded'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def leave_group(self, request):
        r"""集群移出容器舰队

        集群退出容器舰队
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for LeaveGroup
        :type request: :class:`huaweicloudsdkucs.v1.LeaveGroupRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.LeaveGroupResponse`
        """
        http_info = self._leave_group_http_info(request)
        return self._call_api(**http_info)

    def leave_group_invoker(self, request):
        http_info = self._leave_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _leave_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/clusters/{clusterid}/unjoin",
            "request_type": request.__class__.__name__,
            "response_type": "LeaveGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clusterid' in local_var_params:
            path_params['clusterid'] = local_var_params['clusterid']

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

    def list_addon_instances(self, request):
        r"""获取插件实例列表

        获取插件实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAddonInstances
        :type request: :class:`huaweicloudsdkucs.v1.ListAddonInstancesRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.ListAddonInstancesResponse`
        """
        http_info = self._list_addon_instances_http_info(request)
        return self._call_api(**http_info)

    def list_addon_instances_invoker(self, request):
        http_info = self._list_addon_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_addon_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/addons",
            "request_type": request.__class__.__name__,
            "response_type": "ListAddonInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))
        if 'addon_template_name' in local_var_params:
            query_params.append(('addon_template_name', local_var_params['addon_template_name']))
        if 'is_database_status' in local_var_params:
            query_params.append(('is_database_status', local_var_params['is_database_status']))

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

    def list_addon_templates(self, request):
        r"""获取插件模板列表

        获取插件模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAddonTemplates
        :type request: :class:`huaweicloudsdkucs.v1.ListAddonTemplatesRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.ListAddonTemplatesResponse`
        """
        http_info = self._list_addon_templates_http_info(request)
        return self._call_api(**http_info)

    def list_addon_templates_invoker(self, request):
        http_info = self._list_addon_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_addon_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/addontemplates",
            "request_type": request.__class__.__name__,
            "response_type": "ListAddonTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))
        if 'newest' in local_var_params:
            query_params.append(('newest', local_var_params['newest']))
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))
        if 'addon_template_name' in local_var_params:
            query_params.append(('addon_template_name', local_var_params['addon_template_name']))
        if 'base_update_addon_version' in local_var_params:
            query_params.append(('base_update_addon_version', local_var_params['base_update_addon_version']))

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

    def list_cluster_group(self, request):
        r"""获取容器舰队列表

        获取所有容器舰队信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClusterGroup
        :type request: :class:`huaweicloudsdkucs.v1.ListClusterGroupRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.ListClusterGroupResponse`
        """
        http_info = self._list_cluster_group_http_info(request)
        return self._call_api(**http_info)

    def list_cluster_group_invoker(self, request):
        http_info = self._list_cluster_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_cluster_group_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/clustergroups",
            "request_type": request.__class__.__name__,
            "response_type": "ListClusterGroupResponse"
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
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))

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

    def list_config_sets(self, request):
        r"""获取所有配置集合信息

        获取所有配置集合信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConfigSets
        :type request: :class:`huaweicloudsdkucs.v1.ListConfigSetsRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.ListConfigSetsResponse`
        """
        http_info = self._list_config_sets_http_info(request)
        return self._call_api(**http_info)

    def list_config_sets_invoker(self, request):
        http_info = self._list_config_sets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_config_sets_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/configsets",
            "request_type": request.__class__.__name__,
            "response_type": "ListConfigSetsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'clusterid' in local_var_params:
            query_params.append(('clusterid', local_var_params['clusterid']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))

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

    def list_policy_definitions(self, request):
        r"""获取策略定义列表

        获取策略定义列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPolicyDefinitions
        :type request: :class:`huaweicloudsdkucs.v1.ListPolicyDefinitionsRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.ListPolicyDefinitionsResponse`
        """
        http_info = self._list_policy_definitions_http_info(request)
        return self._call_api(**http_info)

    def list_policy_definitions_invoker(self, request):
        http_info = self._list_policy_definitions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_policy_definitions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/policydefinitions",
            "request_type": request.__class__.__name__,
            "response_type": "ListPolicyDefinitionsResponse"
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

    def list_policy_instances(self, request):
        r"""获取策略实例列表

        获取策略实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPolicyInstances
        :type request: :class:`huaweicloudsdkucs.v1.ListPolicyInstancesRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.ListPolicyInstancesResponse`
        """
        http_info = self._list_policy_instances_http_info(request)
        return self._call_api(**http_info)

    def list_policy_instances_invoker(self, request):
        http_info = self._list_policy_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_policy_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/policyinstances",
            "request_type": request.__class__.__name__,
            "response_type": "ListPolicyInstancesResponse"
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

    def list_policy_jobs(self, request):
        r"""获取策略实例任务列表

        获取策略实例任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPolicyJobs
        :type request: :class:`huaweicloudsdkucs.v1.ListPolicyJobsRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.ListPolicyJobsResponse`
        """
        http_info = self._list_policy_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_policy_jobs_invoker(self, request):
        http_info = self._list_policy_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_policy_jobs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/policy/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListPolicyJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'kind' in local_var_params:
            query_params.append(('kind', local_var_params['kind']))

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

    def list_record_sets(self, request):
        r"""查询域名解析记录集列表

        查询域名解析记录集列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRecordSets
        :type request: :class:`huaweicloudsdkucs.v1.ListRecordSetsRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.ListRecordSetsResponse`
        """
        http_info = self._list_record_sets_http_info(request)
        return self._call_api(**http_info)

    def list_record_sets_invoker(self, request):
        http_info = self._list_record_sets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_record_sets_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/traffic/recordsets",
            "request_type": request.__class__.__name__,
            "response_type": "ListRecordSetsResponse"
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

    def list_repos(self, request):
        r"""获取仓库源列表

        获取仓库源列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRepos
        :type request: :class:`huaweicloudsdkucs.v1.ListReposRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.ListReposResponse`
        """
        http_info = self._list_repos_http_info(request)
        return self._call_api(**http_info)

    def list_repos_invoker(self, request):
        http_info = self._list_repos_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_repos_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/configsets/repos",
            "request_type": request.__class__.__name__,
            "response_type": "ListReposResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'clusterid' in local_var_params:
            query_params.append(('clusterid', local_var_params['clusterid']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))

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

    def list_rule(self, request):
        r"""获取权限策略列表

        获取权限策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRule
        :type request: :class:`huaweicloudsdkucs.v1.ListRuleRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.ListRuleResponse`
        """
        http_info = self._list_rule_http_info(request)
        return self._call_api(**http_info)

    def list_rule_invoker(self, request):
        http_info = self._list_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_rule_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/permissions/rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListRuleResponse"
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
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))

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

    def list_server_configs(self, request):
        r"""查询服务配置信息

        获取各个类型集群的全局配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListServerConfigs
        :type request: :class:`huaweicloudsdkucs.v1.ListServerConfigsRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.ListServerConfigsResponse`
        """
        http_info = self._list_server_configs_http_info(request)
        return self._call_api(**http_info)

    def list_server_configs_invoker(self, request):
        http_info = self._list_server_configs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_server_configs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/serverconfig",
            "request_type": request.__class__.__name__,
            "response_type": "ListServerConfigsResponse"
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

    def register_cluster_group(self, request):
        r"""注册容器舰队

        容器舰队创建API，生成容器舰队时可以选择关联的集群
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RegisterClusterGroup
        :type request: :class:`huaweicloudsdkucs.v1.RegisterClusterGroupRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.RegisterClusterGroupResponse`
        """
        http_info = self._register_cluster_group_http_info(request)
        return self._call_api(**http_info)

    def register_cluster_group_invoker(self, request):
        http_info = self._register_cluster_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _register_cluster_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/clustergroups",
            "request_type": request.__class__.__name__,
            "response_type": "RegisterClusterGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}
        if 'metadata' in local_var_params:
            form_params['metadata'] = local_var_params['metadata']
        if 'spec' in local_var_params:
            form_params['spec'] = local_var_params['spec']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/x-www-form-urlencoded'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_addon_instance(self, request):
        r"""获取插件实例

        获取插件实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAddonInstance
        :type request: :class:`huaweicloudsdkucs.v1.ShowAddonInstanceRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.ShowAddonInstanceResponse`
        """
        http_info = self._show_addon_instance_http_info(request)
        return self._call_api(**http_info)

    def show_addon_instance_invoker(self, request):
        http_info = self._show_addon_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_addon_instance_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/addons/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAddonInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'is_database_status' in local_var_params:
            query_params.append(('is_database_status', local_var_params['is_database_status']))
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))

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

    def show_cluster_group(self, request):
        r"""获取单个容器舰队

        获取单个容器舰队
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowClusterGroup
        :type request: :class:`huaweicloudsdkucs.v1.ShowClusterGroupRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.ShowClusterGroupResponse`
        """
        http_info = self._show_cluster_group_http_info(request)
        return self._call_api(**http_info)

    def show_cluster_group_invoker(self, request):
        http_info = self._show_cluster_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_cluster_group_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/clustergroups/{clustergroupid}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClusterGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clustergroupid' in local_var_params:
            path_params['clustergroupid'] = local_var_params['clustergroupid']

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

    def show_config_set(self, request):
        r"""获取配置集合详细信息

        获取配置集合详细信息，包含仓库源信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowConfigSet
        :type request: :class:`huaweicloudsdkucs.v1.ShowConfigSetRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.ShowConfigSetResponse`
        """
        http_info = self._show_config_set_http_info(request)
        return self._call_api(**http_info)

    def show_config_set_invoker(self, request):
        http_info = self._show_config_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_config_set_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/configsets/{configsetid}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConfigSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'configsetid' in local_var_params:
            path_params['configsetid'] = local_var_params['configsetid']

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

    def show_federation_progress(self, request):
        r"""查询联邦开启进度

        查询联邦开启进度
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFederationProgress
        :type request: :class:`huaweicloudsdkucs.v1.ShowFederationProgressRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.ShowFederationProgressResponse`
        """
        http_info = self._show_federation_progress_http_info(request)
        return self._call_api(**http_info)

    def show_federation_progress_invoker(self, request):
        http_info = self._show_federation_progress_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_federation_progress_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/clustergroups/{clustergroupid}/federations/progress",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFederationProgressResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clustergroupid' in local_var_params:
            path_params['clustergroupid'] = local_var_params['clustergroupid']

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

    def show_gitops_statistics(self, request):
        r"""统计某个用户所有配置集合的运行状态

        统计某个用户所有配置集合的运行状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGitopsStatistics
        :type request: :class:`huaweicloudsdkucs.v1.ShowGitopsStatisticsRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.ShowGitopsStatisticsResponse`
        """
        http_info = self._show_gitops_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_gitops_statistics_invoker(self, request):
        http_info = self._show_gitops_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_gitops_statistics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/configsets/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGitopsStatisticsResponse"
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
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))

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

    def show_policy_definition(self, request):
        r"""获取策略定义

        获取策略定义
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPolicyDefinition
        :type request: :class:`huaweicloudsdkucs.v1.ShowPolicyDefinitionRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.ShowPolicyDefinitionResponse`
        """
        http_info = self._show_policy_definition_http_info(request)
        return self._call_api(**http_info)

    def show_policy_definition_invoker(self, request):
        http_info = self._show_policy_definition_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_policy_definition_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/policydefinitions/{policydefinitionid}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPolicyDefinitionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policydefinitionid' in local_var_params:
            path_params['policydefinitionid'] = local_var_params['policydefinitionid']

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

    def show_policy_instance(self, request):
        r"""获取指定策略实例

        获取指定策略实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPolicyInstance
        :type request: :class:`huaweicloudsdkucs.v1.ShowPolicyInstanceRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.ShowPolicyInstanceResponse`
        """
        http_info = self._show_policy_instance_http_info(request)
        return self._call_api(**http_info)

    def show_policy_instance_invoker(self, request):
        http_info = self._show_policy_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_policy_instance_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/policyinstances/{policyinstanceid}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPolicyInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policyinstanceid' in local_var_params:
            path_params['policyinstanceid'] = local_var_params['policyinstanceid']

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

    def show_policy_job(self, request):
        r"""获取指定策略实例相关任务

        获取指定策略实例相关任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPolicyJob
        :type request: :class:`huaweicloudsdkucs.v1.ShowPolicyJobRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.ShowPolicyJobResponse`
        """
        http_info = self._show_policy_job_http_info(request)
        return self._call_api(**http_info)

    def show_policy_job_invoker(self, request):
        http_info = self._show_policy_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_policy_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/policy/jobs/{jobid}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPolicyJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'jobid' in local_var_params:
            path_params['jobid'] = local_var_params['jobid']

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

    def show_proxy_united_workload(self, request):
        r"""查询联邦工作负载

        查询联邦工作负载
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProxyUnitedWorkload
        :type request: :class:`huaweicloudsdkucs.v1.ShowProxyUnitedWorkloadRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.ShowProxyUnitedWorkloadResponse`
        """
        http_info = self._show_proxy_united_workload_http_info(request)
        return self._call_api(**http_info)

    def show_proxy_united_workload_invoker(self, request):
        http_info = self._show_proxy_united_workload_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_proxy_united_workload_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/clustergroups/{clustergroupid}/unitedworkload",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProxyUnitedWorkloadResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clustergroupid' in local_var_params:
            path_params['clustergroupid'] = local_var_params['clustergroupid']

        query_params = []
        if 'kind' in local_var_params:
            query_params.append(('kind', local_var_params['kind']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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
        r"""获取配额信息

        获取UCS配额信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowQuota
        :type request: :class:`huaweicloudsdkucs.v1.ShowQuotaRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.ShowQuotaResponse`
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
            "resource_path": "/v1/maintenance/quota/{domainid}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowQuotaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domainid' in local_var_params:
            path_params['domainid'] = local_var_params['domainid']

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

    def update_addon_instance(self, request):
        r"""更新插件实例

        更新插件实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAddonInstance
        :type request: :class:`huaweicloudsdkucs.v1.UpdateAddonInstanceRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.UpdateAddonInstanceResponse`
        """
        http_info = self._update_addon_instance_http_info(request)
        return self._call_api(**http_info)

    def update_addon_instance_invoker(self, request):
        http_info = self._update_addon_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_addon_instance_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/addons/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAddonInstanceResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_cluster_group(self, request):
        r"""更新容器舰队描述信息

        更新集群所属的容器舰队description信息；需要用户对相应容器舰队有更新权限
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateClusterGroup
        :type request: :class:`huaweicloudsdkucs.v1.UpdateClusterGroupRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.UpdateClusterGroupResponse`
        """
        http_info = self._update_cluster_group_http_info(request)
        return self._call_api(**http_info)

    def update_cluster_group_invoker(self, request):
        http_info = self._update_cluster_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_cluster_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/clustergroups/{clustergroupid}/description",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateClusterGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clustergroupid' in local_var_params:
            path_params['clustergroupid'] = local_var_params['clustergroupid']

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

    def update_cluster_group_associated_clusters(self, request):
        r"""向容器舰队中添加集群

        向容器舰队中添加集群，同批次可以添加一个或多个集群，该接口无法清空或减少管理的集群。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateClusterGroupAssociatedClusters
        :type request: :class:`huaweicloudsdkucs.v1.UpdateClusterGroupAssociatedClustersRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.UpdateClusterGroupAssociatedClustersResponse`
        """
        http_info = self._update_cluster_group_associated_clusters_http_info(request)
        return self._call_api(**http_info)

    def update_cluster_group_associated_clusters_invoker(self, request):
        http_info = self._update_cluster_group_associated_clusters_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_cluster_group_associated_clusters_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/clustergroups/{clustergroupid}/associatedclusters",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateClusterGroupAssociatedClustersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clustergroupid' in local_var_params:
            path_params['clustergroupid'] = local_var_params['clustergroupid']

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

    def update_cluster_group_associated_rules(self, request):
        r"""更新容器舰队关联权限策略

        更新容器舰队关联权限策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateClusterGroupAssociatedRules
        :type request: :class:`huaweicloudsdkucs.v1.UpdateClusterGroupAssociatedRulesRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.UpdateClusterGroupAssociatedRulesResponse`
        """
        http_info = self._update_cluster_group_associated_rules_http_info(request)
        return self._call_api(**http_info)

    def update_cluster_group_associated_rules_invoker(self, request):
        http_info = self._update_cluster_group_associated_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_cluster_group_associated_rules_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/clustergroups/{clustergroupid}/associatedrules",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateClusterGroupAssociatedRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clustergroupid' in local_var_params:
            path_params['clustergroupid'] = local_var_params['clustergroupid']

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

    def update_cluster_group_associated_zones(self, request):
        r"""更新容器舰队的联邦对应的zone

        更新容器舰队的集群联邦关联的zone
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateClusterGroupAssociatedZones
        :type request: :class:`huaweicloudsdkucs.v1.UpdateClusterGroupAssociatedZonesRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.UpdateClusterGroupAssociatedZonesResponse`
        """
        http_info = self._update_cluster_group_associated_zones_http_info(request)
        return self._call_api(**http_info)

    def update_cluster_group_associated_zones_invoker(self, request):
        http_info = self._update_cluster_group_associated_zones_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_cluster_group_associated_zones_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/clustergroups/{clustergroupid}/associatedzones",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateClusterGroupAssociatedZonesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clustergroupid' in local_var_params:
            path_params['clustergroupid'] = local_var_params['clustergroupid']

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

    def update_config_set(self, request):
        r"""更新配置集合信息

        仅更新配置集合，不更新仓库源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateConfigSet
        :type request: :class:`huaweicloudsdkucs.v1.UpdateConfigSetRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.UpdateConfigSetResponse`
        """
        http_info = self._update_config_set_http_info(request)
        return self._call_api(**http_info)

    def update_config_set_invoker(self, request):
        http_info = self._update_config_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_config_set_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/configsets/{configsetid}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateConfigSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'configsetid' in local_var_params:
            path_params['configsetid'] = local_var_params['configsetid']

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

    def update_policy_defination(self, request):
        r"""更新策略定义

        更新策略定义
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePolicyDefination
        :type request: :class:`huaweicloudsdkucs.v1.UpdatePolicyDefinationRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.UpdatePolicyDefinationResponse`
        """
        http_info = self._update_policy_defination_http_info(request)
        return self._call_api(**http_info)

    def update_policy_defination_invoker(self, request):
        http_info = self._update_policy_defination_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_policy_defination_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/policydefinitions/{policydefinitionid}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePolicyDefinationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policydefinitionid' in local_var_params:
            path_params['policydefinitionid'] = local_var_params['policydefinitionid']

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

    def update_policy_instance(self, request):
        r"""更新指定策略实例

        更新指定策略实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePolicyInstance
        :type request: :class:`huaweicloudsdkucs.v1.UpdatePolicyInstanceRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.UpdatePolicyInstanceResponse`
        """
        http_info = self._update_policy_instance_http_info(request)
        return self._call_api(**http_info)

    def update_policy_instance_invoker(self, request):
        http_info = self._update_policy_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_policy_instance_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/policyinstances/{policyinstanceid}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePolicyInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policyinstanceid' in local_var_params:
            path_params['policyinstanceid'] = local_var_params['policyinstanceid']

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

    def update_proxy_united_workload(self, request):
        r"""更新联邦工作负载

        更新联邦工作负载
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateProxyUnitedWorkload
        :type request: :class:`huaweicloudsdkucs.v1.UpdateProxyUnitedWorkloadRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.UpdateProxyUnitedWorkloadResponse`
        """
        http_info = self._update_proxy_united_workload_http_info(request)
        return self._call_api(**http_info)

    def update_proxy_united_workload_invoker(self, request):
        http_info = self._update_proxy_united_workload_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_proxy_united_workload_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/clustergroups/{clustergroupid}/unitedworkload",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProxyUnitedWorkloadResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clustergroupid' in local_var_params:
            path_params['clustergroupid'] = local_var_params['clustergroupid']

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

    def update_repo(self, request):
        r"""更新仓库源信息

        更新仓库源信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRepo
        :type request: :class:`huaweicloudsdkucs.v1.UpdateRepoRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.UpdateRepoResponse`
        """
        http_info = self._update_repo_http_info(request)
        return self._call_api(**http_info)

    def update_repo_invoker(self, request):
        http_info = self._update_repo_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_repo_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/configsets/repos/{repoid}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRepoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repoid' in local_var_params:
            path_params['repoid'] = local_var_params['repoid']

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

    def update_rule(self, request):
        r"""更新权限策略

        更新权限策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRule
        :type request: :class:`huaweicloudsdkucs.v1.UpdateRuleRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.UpdateRuleResponse`
        """
        http_info = self._update_rule_http_info(request)
        return self._call_api(**http_info)

    def update_rule_invoker(self, request):
        http_info = self._update_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_rule_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/permissions/rules/{ruleid}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ruleid' in local_var_params:
            path_params['ruleid'] = local_var_params['ruleid']

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

    def upgrade_federation(self, request):
        r"""升级容器舰队联邦

        容器舰队联邦版本升级
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpgradeFederation
        :type request: :class:`huaweicloudsdkucs.v1.UpgradeFederationRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.UpgradeFederationResponse`
        """
        http_info = self._upgrade_federation_http_info(request)
        return self._call_api(**http_info)

    def upgrade_federation_invoker(self, request):
        http_info = self._upgrade_federation_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upgrade_federation_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/clustergroups/{clustergroupid}/federations/upgrade",
            "request_type": request.__class__.__name__,
            "response_type": "UpgradeFederationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clustergroupid' in local_var_params:
            path_params['clustergroupid'] = local_var_params['clustergroupid']

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

    def create_cluster_conf(self, request):
        r"""获取集群安装时所需的配置信息

        获取集群安装时所需的配置信息，当前仅本地集群使用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateClusterConf
        :type request: :class:`huaweicloudsdkucs.v1.CreateClusterConfRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.CreateClusterConfResponse`
        """
        http_info = self._create_cluster_conf_http_info(request)
        return self._call_api(**http_info)

    def create_cluster_conf_invoker(self, request):
        http_info = self._create_cluster_conf_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_cluster_conf_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/clusters/{clusterid}/clusterconf",
            "request_type": request.__class__.__name__,
            "response_type": "CreateClusterConfResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clusterid' in local_var_params:
            path_params['clusterid'] = local_var_params['clusterid']

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

    def create_cluster_kubeconfig(self, request):
        r"""获取集群kubeconfig

        获取集群kubeconfig
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateClusterKubeconfig
        :type request: :class:`huaweicloudsdkucs.v1.CreateClusterKubeconfigRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.CreateClusterKubeconfigResponse`
        """
        http_info = self._create_cluster_kubeconfig_http_info(request)
        return self._call_api(**http_info)

    def create_cluster_kubeconfig_invoker(self, request):
        http_info = self._create_cluster_kubeconfig_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_cluster_kubeconfig_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/clusters/{clusterid}/kubeconfig",
            "request_type": request.__class__.__name__,
            "response_type": "CreateClusterKubeconfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clusterid' in local_var_params:
            path_params['clusterid'] = local_var_params['clusterid']

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

    def create_cluster_policy_instance(self, request):
        r"""创建集群策略实例

        创建集群策略实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateClusterPolicyInstance
        :type request: :class:`huaweicloudsdkucs.v1.CreateClusterPolicyInstanceRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.CreateClusterPolicyInstanceResponse`
        """
        http_info = self._create_cluster_policy_instance_http_info(request)
        return self._call_api(**http_info)

    def create_cluster_policy_instance_invoker(self, request):
        http_info = self._create_cluster_policy_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_cluster_policy_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/clusters/{clusterid}/policyinstance",
            "request_type": request.__class__.__name__,
            "response_type": "CreateClusterPolicyInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clusterid' in local_var_params:
            path_params['clusterid'] = local_var_params['clusterid']

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

    def delete_cluster(self, request):
        r"""删除集群

        用于集群解除注册；传入的cluster ID必须符合k8s UUID的格式规则；同时需要用户有对应集群的操作权限，否则会鉴权失败。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCluster
        :type request: :class:`huaweicloudsdkucs.v1.DeleteClusterRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.DeleteClusterResponse`
        """
        http_info = self._delete_cluster_http_info(request)
        return self._call_api(**http_info)

    def delete_cluster_invoker(self, request):
        http_info = self._delete_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_cluster_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/clusters/{clusterid}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clusterid' in local_var_params:
            path_params['clusterid'] = local_var_params['clusterid']

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

    def disable_cluster_policy(self, request):
        r"""集群关闭策略中心

        集群关闭策略中心
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisableClusterPolicy
        :type request: :class:`huaweicloudsdkucs.v1.DisableClusterPolicyRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.DisableClusterPolicyResponse`
        """
        http_info = self._disable_cluster_policy_http_info(request)
        return self._call_api(**http_info)

    def disable_cluster_policy_invoker(self, request):
        http_info = self._disable_cluster_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disable_cluster_policy_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/clusters/{clusterid}/policy",
            "request_type": request.__class__.__name__,
            "response_type": "DisableClusterPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clusterid' in local_var_params:
            path_params['clusterid'] = local_var_params['clusterid']

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

    def disable_git_ops(self, request):
        r"""卸载集群gitops插件

        卸载集群gitops插件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisableGitOps
        :type request: :class:`huaweicloudsdkucs.v1.DisableGitOpsRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.DisableGitOpsResponse`
        """
        http_info = self._disable_git_ops_http_info(request)
        return self._call_api(**http_info)

    def disable_git_ops_invoker(self, request):
        http_info = self._disable_git_ops_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disable_git_ops_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/clusters/{clusterid}/gitops",
            "request_type": request.__class__.__name__,
            "response_type": "DisableGitOpsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clusterid' in local_var_params:
            path_params['clusterid'] = local_var_params['clusterid']

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

    def enable_cluster_policy(self, request):
        r"""集群启用策略中心

        集群启用策略中心
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableClusterPolicy
        :type request: :class:`huaweicloudsdkucs.v1.EnableClusterPolicyRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.EnableClusterPolicyResponse`
        """
        http_info = self._enable_cluster_policy_http_info(request)
        return self._call_api(**http_info)

    def enable_cluster_policy_invoker(self, request):
        http_info = self._enable_cluster_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_cluster_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/clusters/{clusterid}/policy",
            "request_type": request.__class__.__name__,
            "response_type": "EnableClusterPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clusterid' in local_var_params:
            path_params['clusterid'] = local_var_params['clusterid']

        query_params = []
        if 'retry' in local_var_params:
            query_params.append(('retry', local_var_params['retry']))

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

    def enable_git_ops(self, request):
        r"""启用Gitops插件

        启用Gitops插件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableGitOps
        :type request: :class:`huaweicloudsdkucs.v1.EnableGitOpsRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.EnableGitOpsResponse`
        """
        http_info = self._enable_git_ops_http_info(request)
        return self._call_api(**http_info)

    def enable_git_ops_invoker(self, request):
        http_info = self._enable_git_ops_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_git_ops_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/clusters/{clusterid}/gitops",
            "request_type": request.__class__.__name__,
            "response_type": "EnableGitOpsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clusterid' in local_var_params:
            path_params['clusterid'] = local_var_params['clusterid']

        query_params = []
        if 'retry' in local_var_params:
            query_params.append(('retry', local_var_params['retry']))

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

    def list_managed_clusters(self, request):
        r"""获取租户的CCE集群列表

        获取当前租户的CCE集群列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListManagedClusters
        :type request: :class:`huaweicloudsdkucs.v1.ListManagedClustersRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.ListManagedClustersResponse`
        """
        http_info = self._list_managed_clusters_http_info(request)
        return self._call_api(**http_info)

    def list_managed_clusters_invoker(self, request):
        http_info = self._list_managed_clusters_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_managed_clusters_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/managedclusters",
            "request_type": request.__class__.__name__,
            "response_type": "ListManagedClustersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'unimported' in local_var_params:
            query_params.append(('unimported', local_var_params['unimported']))
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

    def list_registered_cluster_versions(self, request):
        r"""查询支持接入UCS的集群版本列表

        查询支持接入UCS的集群版本列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRegisteredClusterVersions
        :type request: :class:`huaweicloudsdkucs.v1.ListRegisteredClusterVersionsRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.ListRegisteredClusterVersionsResponse`
        """
        http_info = self._list_registered_cluster_versions_http_info(request)
        return self._call_api(**http_info)

    def list_registered_cluster_versions_invoker(self, request):
        http_info = self._list_registered_cluster_versions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_registered_cluster_versions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/config/registeredclusterversions",
            "request_type": request.__class__.__name__,
            "response_type": "ListRegisteredClusterVersionsResponse"
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

    def register_cluster(self, request):
        r"""注册集群

        集群注册接口。支持三方集群的注册和CCE导入集群的注册。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RegisterCluster
        :type request: :class:`huaweicloudsdkucs.v1.RegisterClusterRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.RegisterClusterResponse`
        """
        http_info = self._register_cluster_http_info(request)
        return self._call_api(**http_info)

    def register_cluster_invoker(self, request):
        http_info = self._register_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _register_cluster_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/clusters",
            "request_type": request.__class__.__name__,
            "response_type": "RegisterClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}
        if 'kind' in local_var_params:
            form_params['kind'] = local_var_params['kind']
        if 'api_version' in local_var_params:
            form_params['apiVersion'] = local_var_params['api_version']
        if 'metadata' in local_var_params:
            form_params['metadata'] = local_var_params['metadata']
        if 'spec' in local_var_params:
            form_params['spec'] = local_var_params['spec']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/x-www-form-urlencoded'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def retry_cluster_activation(self, request):
        r"""激活集群

        激活集群接口；传入的cluster ID必须符合k8s UUID的格式规则；同时需要用户有对应集群的更新权限，否则会鉴权失败
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RetryClusterActivation
        :type request: :class:`huaweicloudsdkucs.v1.RetryClusterActivationRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.RetryClusterActivationResponse`
        """
        http_info = self._retry_cluster_activation_http_info(request)
        return self._call_api(**http_info)

    def retry_cluster_activation_invoker(self, request):
        http_info = self._retry_cluster_activation_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _retry_cluster_activation_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/clusters/{clusterid}/activation",
            "request_type": request.__class__.__name__,
            "response_type": "RetryClusterActivationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clusterid' in local_var_params:
            path_params['clusterid'] = local_var_params['clusterid']

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

    def show_cluster(self, request):
        r"""获取单个集群

        获取集群信息。传入的cluster ID必须符合k8s UUID的格式规则；同时需要用户有对应集群的获取权限，否则会鉴权失败
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCluster
        :type request: :class:`huaweicloudsdkucs.v1.ShowClusterRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.ShowClusterResponse`
        """
        http_info = self._show_cluster_http_info(request)
        return self._call_api(**http_info)

    def show_cluster_invoker(self, request):
        http_info = self._show_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_cluster_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/clusters/{clusterid}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clusterid' in local_var_params:
            path_params['clusterid'] = local_var_params['clusterid']

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

    def show_cluster_access_info(self, request):
        r"""获取集群接入信息

        该API接口用于获取集群接入信息；传入的cluster ID必须符合k8s UUID的格式规则；同时需要用户有对应集群证书的获取权限，否则会鉴权失败；agent证书只可以下载一次。仅用于获取三方集群的集群接入信息，CCE集群不从该接口获取，如果传入CCE集群ID，返回码为400
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowClusterAccessInfo
        :type request: :class:`huaweicloudsdkucs.v1.ShowClusterAccessInfoRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.ShowClusterAccessInfoResponse`
        """
        http_info = self._show_cluster_access_info_http_info(request)
        return self._call_api(**http_info)

    def show_cluster_access_info_invoker(self, request):
        http_info = self._show_cluster_access_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_cluster_access_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/clusters/{clusterid}/accessinfo",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClusterAccessInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clusterid' in local_var_params:
            path_params['clusterid'] = local_var_params['clusterid']

        query_params = []
        if 'vpcendpoint' in local_var_params:
            query_params.append(('vpcendpoint', local_var_params['vpcendpoint']))
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

    def show_cluster_list(self, request):
        r"""获取集群列表

        获取集群信息列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowClusterList
        :type request: :class:`huaweicloudsdkucs.v1.ShowClusterListRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.ShowClusterListResponse`
        """
        http_info = self._show_cluster_list_http_info(request)
        return self._call_api(**http_info)

    def show_cluster_list_invoker(self, request):
        http_info = self._show_cluster_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_cluster_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/clusters",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClusterListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'enablestatus' in local_var_params:
            query_params.append(('enablestatus', local_var_params['enablestatus']))
        if 'clustergroupid' in local_var_params:
            query_params.append(('clustergroupid', local_var_params['clustergroupid']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'managetype' in local_var_params:
            query_params.append(('managetype', local_var_params['managetype']))
        if 'clusterids' in local_var_params:
            query_params.append(('clusterids', local_var_params['clusterids']))

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

    def show_git_ops_status(self, request):
        r"""获取gitops启用进展

        获取gitops启用进展
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGitOpsStatus
        :type request: :class:`huaweicloudsdkucs.v1.ShowGitOpsStatusRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.ShowGitOpsStatusResponse`
        """
        http_info = self._show_git_ops_status_http_info(request)
        return self._call_api(**http_info)

    def show_git_ops_status_invoker(self, request):
        http_info = self._show_git_ops_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_git_ops_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/clusters/{clusterid}/gitops",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGitOpsStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clusterid' in local_var_params:
            path_params['clusterid'] = local_var_params['clusterid']

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

    def update_cluster(self, request):
        r"""更新集群

        更新集群。当前仅允许更新附着集群和本地集群的国家/城市，允许更新多云集群的工作节点个数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCluster
        :type request: :class:`huaweicloudsdkucs.v1.UpdateClusterRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.UpdateClusterResponse`
        """
        http_info = self._update_cluster_http_info(request)
        return self._call_api(**http_info)

    def update_cluster_invoker(self, request):
        http_info = self._update_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_cluster_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/clusters/{clusterid}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clusterid' in local_var_params:
            path_params['clusterid'] = local_var_params['clusterid']

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

    def update_cluster_rules(self, request):
        r"""集群关联权限策略

        集群关联权限策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateClusterRules
        :type request: :class:`huaweicloudsdkucs.v1.UpdateClusterRulesRequest`
        :rtype: :class:`huaweicloudsdkucs.v1.UpdateClusterRulesResponse`
        """
        http_info = self._update_cluster_rules_http_info(request)
        return self._call_api(**http_info)

    def update_cluster_rules_invoker(self, request):
        http_info = self._update_cluster_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_cluster_rules_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/clusters/{clusterid}/associatedrules",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateClusterRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clusterid' in local_var_params:
            path_params['clusterid'] = local_var_params['clusterid']

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
