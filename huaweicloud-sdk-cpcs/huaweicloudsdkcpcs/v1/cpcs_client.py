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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcpcs'")


class CpcsClient(Client):
    def __init__(self):
        super(CpcsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcpcs.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CpcsClient":
                raise TypeError("client type error, support client type is CpcsClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def associate_apps(self, request):
        r"""创建密码服务集群与应用绑定关系

        创建密码服务集群与应用绑定关系
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateApps
        :type request: :class:`huaweicloudsdkcpcs.v1.AssociateAppsRequest`
        :rtype: :class:`huaweicloudsdkcpcs.v1.AssociateAppsResponse`
        """
        http_info = self._associate_apps_http_info(request)
        return self._call_api(**http_info)

    def associate_apps_invoker(self, request):
        http_info = self._associate_apps_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _associate_apps_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dew/cpcs/associate-apps",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateAppsResponse"
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

    def authorize_access_keys(self, request):
        r"""密码服务集群授予应用访问密钥的访问权限

        密码服务集群授予应用访问密钥的访问权限
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AuthorizeAccessKeys
        :type request: :class:`huaweicloudsdkcpcs.v1.AuthorizeAccessKeysRequest`
        :rtype: :class:`huaweicloudsdkcpcs.v1.AuthorizeAccessKeysResponse`
        """
        http_info = self._authorize_access_keys_http_info(request)
        return self._call_api(**http_info)

    def authorize_access_keys_invoker(self, request):
        http_info = self._authorize_access_keys_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _authorize_access_keys_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dew/cpcs/cluster/{cluster_id}/authorize-access-keys",
            "request_type": request.__class__.__name__,
            "response_type": "AuthorizeAccessKeysResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def batch_disable_access_keys(self, request):
        r"""停用应用的访问密钥

        停用应用的访问密钥
        &gt; 只有当访问密钥处于“启用”状态时，方可调用此接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDisableAccessKeys
        :type request: :class:`huaweicloudsdkcpcs.v1.BatchDisableAccessKeysRequest`
        :rtype: :class:`huaweicloudsdkcpcs.v1.BatchDisableAccessKeysResponse`
        """
        http_info = self._batch_disable_access_keys_http_info(request)
        return self._call_api(**http_info)

    def batch_disable_access_keys_invoker(self, request):
        http_info = self._batch_disable_access_keys_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_disable_access_keys_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dew/cpcs/apps/{app_id}/access-keys/disable",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDisableAccessKeysResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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

    def batch_enable_access_keys(self, request):
        r"""启用应用的访问密钥

        启用应用的访问密钥
        &gt; 只有当访问密钥处于“停用”状态时，方可调用此接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchEnableAccessKeys
        :type request: :class:`huaweicloudsdkcpcs.v1.BatchEnableAccessKeysRequest`
        :rtype: :class:`huaweicloudsdkcpcs.v1.BatchEnableAccessKeysResponse`
        """
        http_info = self._batch_enable_access_keys_http_info(request)
        return self._call_api(**http_info)

    def batch_enable_access_keys_invoker(self, request):
        http_info = self._batch_enable_access_keys_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_enable_access_keys_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dew/cpcs/apps/{app_id}/access-keys/enable",
            "request_type": request.__class__.__name__,
            "response_type": "BatchEnableAccessKeysResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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

    def cancel_authorize_access_keys(self, request):
        r"""密码服务集群解除对访问密钥的授权

        密码服务集群解除对访问密钥的授权
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelAuthorizeAccessKeys
        :type request: :class:`huaweicloudsdkcpcs.v1.CancelAuthorizeAccessKeysRequest`
        :rtype: :class:`huaweicloudsdkcpcs.v1.CancelAuthorizeAccessKeysResponse`
        """
        http_info = self._cancel_authorize_access_keys_http_info(request)
        return self._call_api(**http_info)

    def cancel_authorize_access_keys_invoker(self, request):
        http_info = self._cancel_authorize_access_keys_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_authorize_access_keys_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dew/cpcs/cluster/{cluster_id}/de-authorize-access-keys",
            "request_type": request.__class__.__name__,
            "response_type": "CancelAuthorizeAccessKeysResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def create_app(self, request):
        r"""创建应用

        创建应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateApp
        :type request: :class:`huaweicloudsdkcpcs.v1.CreateAppRequest`
        :rtype: :class:`huaweicloudsdkcpcs.v1.CreateAppResponse`
        """
        http_info = self._create_app_http_info(request)
        return self._call_api(**http_info)

    def create_app_invoker(self, request):
        http_info = self._create_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_app_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dew/cpcs/apps",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAppResponse"
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

    def create_app_access_key(self, request):
        r"""创建访问密钥

        创建访问密钥
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAppAccessKey
        :type request: :class:`huaweicloudsdkcpcs.v1.CreateAppAccessKeyRequest`
        :rtype: :class:`huaweicloudsdkcpcs.v1.CreateAppAccessKeyResponse`
        """
        http_info = self._create_app_access_key_http_info(request)
        return self._call_api(**http_info)

    def create_app_access_key_invoker(self, request):
        http_info = self._create_app_access_key_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_app_access_key_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dew/cpcs/apps/{app_id}/access-keys",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAppAccessKeyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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

    def create_cluster(self, request):
        r"""创建密码服务集群

        创建密码服务集群
        &gt; 调用接口之后返回订单ID，需要到“待支付订单里面”支付成功之后才能创建密码服务集群。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCluster
        :type request: :class:`huaweicloudsdkcpcs.v1.CreateClusterRequest`
        :rtype: :class:`huaweicloudsdkcpcs.v1.CreateClusterResponse`
        """
        http_info = self._create_cluster_http_info(request)
        return self._call_api(**http_info)

    def create_cluster_invoker(self, request):
        http_info = self._create_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_cluster_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dew/cpcs/cluster",
            "request_type": request.__class__.__name__,
            "response_type": "CreateClusterResponse"
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

    def delete_access_key(self, request):
        r"""删除应用的访问密钥

        删除应用的访问密钥
        &gt; 只有当访问密钥处于“停用”状态时，方可调用此接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAccessKey
        :type request: :class:`huaweicloudsdkcpcs.v1.DeleteAccessKeyRequest`
        :rtype: :class:`huaweicloudsdkcpcs.v1.DeleteAccessKeyResponse`
        """
        http_info = self._delete_access_key_http_info(request)
        return self._call_api(**http_info)

    def delete_access_key_invoker(self, request):
        http_info = self._delete_access_key_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_access_key_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/dew/cpcs/apps/{app_id}/access-keys/{access_key_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAccessKeyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'access_key_id' in local_var_params:
            path_params['access_key_id'] = local_var_params['access_key_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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

    def delete_app(self, request):
        r"""删除应用

        删除应用
        &gt; 只有当应用与任何其它服务没有绑定关系的情况下，方可进行集群删除操作该操作不可恢复，请谨慎执行
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApp
        :type request: :class:`huaweicloudsdkcpcs.v1.DeleteAppRequest`
        :rtype: :class:`huaweicloudsdkcpcs.v1.DeleteAppResponse`
        """
        http_info = self._delete_app_http_info(request)
        return self._call_api(**http_info)

    def delete_app_invoker(self, request):
        http_info = self._delete_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_app_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/dew/cpcs/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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

    def delete_ccsp_cluster(self, request):
        r"""删除密码服务集群

        删除密码服务集群，即释放密码服务集群所有服务实例以及对应的VSM集群实例，并删除集群相关信息
        &gt; 只有当集群与任何应用都没有绑定关系的情况下，且处于“运行中”状态，且退订了集群中所有实例，方可进行集群删除操作，该操作不可恢复，请谨慎执行
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCcspCluster
        :type request: :class:`huaweicloudsdkcpcs.v1.DeleteCcspClusterRequest`
        :rtype: :class:`huaweicloudsdkcpcs.v1.DeleteCcspClusterResponse`
        """
        http_info = self._delete_ccsp_cluster_http_info(request)
        return self._call_api(**http_info)

    def delete_ccsp_cluster_invoker(self, request):
        http_info = self._delete_ccsp_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_ccsp_cluster_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/dew/cpcs/cluster/{cluster_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCcspClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def disable_ccsp_instance(self, request):
        r"""停用密码服务实例的业务功能

        停用密码服务实例的业务功能
        &gt; 只有当密码服务实例处于“启用”状态时，方可调用此接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisableCcspInstance
        :type request: :class:`huaweicloudsdkcpcs.v1.DisableCcspInstanceRequest`
        :rtype: :class:`huaweicloudsdkcpcs.v1.DisableCcspInstanceResponse`
        """
        http_info = self._disable_ccsp_instance_http_info(request)
        return self._call_api(**http_info)

    def disable_ccsp_instance_invoker(self, request):
        http_info = self._disable_ccsp_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disable_ccsp_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dew/cpcs/instances/{instance_id}/disable",
            "request_type": request.__class__.__name__,
            "response_type": "DisableCcspInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def disassociate_apps(self, request):
        r"""解除密码服务集群与应用绑定关系

        解除密码服务集群与应用绑定关系
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisassociateApps
        :type request: :class:`huaweicloudsdkcpcs.v1.DisassociateAppsRequest`
        :rtype: :class:`huaweicloudsdkcpcs.v1.DisassociateAppsResponse`
        """
        http_info = self._disassociate_apps_http_info(request)
        return self._call_api(**http_info)

    def disassociate_apps_invoker(self, request):
        http_info = self._disassociate_apps_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disassociate_apps_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dew/cpcs/disassociate-apps",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateAppsResponse"
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

    def enable_ccsp_instance(self, request):
        r"""启用密码服务实例的业务功能

        启用密码服务实例的业务功能
        &gt; 只有当密码服务实例处于“停用”状态时，方可调用此接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableCcspInstance
        :type request: :class:`huaweicloudsdkcpcs.v1.EnableCcspInstanceRequest`
        :rtype: :class:`huaweicloudsdkcpcs.v1.EnableCcspInstanceResponse`
        """
        http_info = self._enable_ccsp_instance_http_info(request)
        return self._call_api(**http_info)

    def enable_ccsp_instance_invoker(self, request):
        http_info = self._enable_ccsp_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_ccsp_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dew/cpcs/instances/{instance_id}/enable",
            "request_type": request.__class__.__name__,
            "response_type": "EnableCcspInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_ccsp_tenant_images(self, request):
        r"""查询密码服务的镜像

        查询密码服务的镜像
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCcspTenantImages
        :type request: :class:`huaweicloudsdkcpcs.v1.ListCcspTenantImagesRequest`
        :rtype: :class:`huaweicloudsdkcpcs.v1.ListCcspTenantImagesResponse`
        """
        http_info = self._list_ccsp_tenant_images_http_info(request)
        return self._call_api(**http_info)

    def list_ccsp_tenant_images_invoker(self, request):
        http_info = self._list_ccsp_tenant_images_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ccsp_tenant_images_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dew/cpcs/images",
            "request_type": request.__class__.__name__,
            "response_type": "ListCcspTenantImagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'page_num' in local_var_params:
            query_params.append(('page_num', local_var_params['page_num']))
        if 'image_name' in local_var_params:
            query_params.append(('image_name', local_var_params['image_name']))
        if 'service_type' in local_var_params:
            query_params.append(('service_type', local_var_params['service_type']))
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

    def show_access_key(self, request):
        r"""下载访问密钥

        下载访问密钥且只能下载一次。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAccessKey
        :type request: :class:`huaweicloudsdkcpcs.v1.ShowAccessKeyRequest`
        :rtype: :class:`huaweicloudsdkcpcs.v1.ShowAccessKeyResponse`
        """
        http_info = self._show_access_key_http_info(request)
        return self._call_api(**http_info)

    def show_access_key_invoker(self, request):
        http_info = self._show_access_key_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_access_key_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dew/cpcs/apps/{app_id}/access-keys/{access_key_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAccessKeyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'access_key_id' in local_var_params:
            path_params['access_key_id'] = local_var_params['access_key_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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

    def show_app_access_key_list(self, request):
        r"""查询应用的访问密钥列表

        查询应用的访问密钥列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAppAccessKeyList
        :type request: :class:`huaweicloudsdkcpcs.v1.ShowAppAccessKeyListRequest`
        :rtype: :class:`huaweicloudsdkcpcs.v1.ShowAppAccessKeyListResponse`
        """
        http_info = self._show_app_access_key_list_http_info(request)
        return self._call_api(**http_info)

    def show_app_access_key_list_invoker(self, request):
        http_info = self._show_app_access_key_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_app_access_key_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dew/cpcs/apps/{app_id}/access-keys",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppAccessKeyListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'page_num' in local_var_params:
            query_params.append(('page_num', local_var_params['page_num']))
        if 'key_name' in local_var_params:
            query_params.append(('key_name', local_var_params['key_name']))
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

    def show_app_list(self, request):
        r"""查询应用列表

        查询应用列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAppList
        :type request: :class:`huaweicloudsdkcpcs.v1.ShowAppListRequest`
        :rtype: :class:`huaweicloudsdkcpcs.v1.ShowAppListResponse`
        """
        http_info = self._show_app_list_http_info(request)
        return self._call_api(**http_info)

    def show_app_list_invoker(self, request):
        http_info = self._show_app_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_app_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dew/cpcs/apps",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'page_num' in local_var_params:
            query_params.append(('page_num', local_var_params['page_num']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'vpc_name' in local_var_params:
            query_params.append(('vpc_name', local_var_params['vpc_name']))
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

    def show_association_list(self, request):
        r"""查询密码服务集群与应用的绑定关系列表

        查询密码服务集群与应用的绑定关系列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAssociationList
        :type request: :class:`huaweicloudsdkcpcs.v1.ShowAssociationListRequest`
        :rtype: :class:`huaweicloudsdkcpcs.v1.ShowAssociationListResponse`
        """
        http_info = self._show_association_list_http_info(request)
        return self._call_api(**http_info)

    def show_association_list_invoker(self, request):
        http_info = self._show_association_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_association_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dew/cpcs/associations",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAssociationListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'page_num' in local_var_params:
            query_params.append(('page_num', local_var_params['page_num']))
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

    def show_available_az(self, request):
        r"""查询可创建密码服务集群的可用区列表

        查询可创建密码服务集群的可用区列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAvailableAz
        :type request: :class:`huaweicloudsdkcpcs.v1.ShowAvailableAzRequest`
        :rtype: :class:`huaweicloudsdkcpcs.v1.ShowAvailableAzResponse`
        """
        http_info = self._show_available_az_http_info(request)
        return self._call_api(**http_info)

    def show_available_az_invoker(self, request):
        http_info = self._show_available_az_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_available_az_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dew/cpcs/az",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAvailableAzResponse"
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

    def show_ccsp_cluster(self, request):
        r"""查询密码服务集群详情

        查询密码服务集群信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCcspCluster
        :type request: :class:`huaweicloudsdkcpcs.v1.ShowCcspClusterRequest`
        :rtype: :class:`huaweicloudsdkcpcs.v1.ShowCcspClusterResponse`
        """
        http_info = self._show_ccsp_cluster_http_info(request)
        return self._call_api(**http_info)

    def show_ccsp_cluster_invoker(self, request):
        http_info = self._show_ccsp_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_ccsp_cluster_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dew/cpcs/cluster/{cluster_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCcspClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def show_ccsp_cluster_list(self, request):
        r"""查询密码服务集群列表

        查询密码服务集群列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCcspClusterList
        :type request: :class:`huaweicloudsdkcpcs.v1.ShowCcspClusterListRequest`
        :rtype: :class:`huaweicloudsdkcpcs.v1.ShowCcspClusterListResponse`
        """
        http_info = self._show_ccsp_cluster_list_http_info(request)
        return self._call_api(**http_info)

    def show_ccsp_cluster_list_invoker(self, request):
        http_info = self._show_ccsp_cluster_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_ccsp_cluster_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dew/cpcs/cluster",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCcspClusterListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'page_num' in local_var_params:
            query_params.append(('page_num', local_var_params['page_num']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'service_type' in local_var_params:
            query_params.append(('service_type', local_var_params['service_type']))
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

    def show_ccsp_instance_info(self, request):
        r"""查询密码服务实例列表

        查询密码服务实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCcspInstanceInfo
        :type request: :class:`huaweicloudsdkcpcs.v1.ShowCcspInstanceInfoRequest`
        :rtype: :class:`huaweicloudsdkcpcs.v1.ShowCcspInstanceInfoResponse`
        """
        http_info = self._show_ccsp_instance_info_http_info(request)
        return self._call_api(**http_info)

    def show_ccsp_instance_info_invoker(self, request):
        http_info = self._show_ccsp_instance_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_ccsp_instance_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dew/cpcs/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCcspInstanceInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'page_num' in local_var_params:
            query_params.append(('page_num', local_var_params['page_num']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'is_normal' in local_var_params:
            query_params.append(('is_normal', local_var_params['is_normal']))

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

    def show_cluster_access_key_list(self, request):
        r"""查询密码服务集群已授权的访问密钥列表

        查询密码服务集群已授权的访问密钥列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowClusterAccessKeyList
        :type request: :class:`huaweicloudsdkcpcs.v1.ShowClusterAccessKeyListRequest`
        :rtype: :class:`huaweicloudsdkcpcs.v1.ShowClusterAccessKeyListResponse`
        """
        http_info = self._show_cluster_access_key_list_http_info(request)
        return self._call_api(**http_info)

    def show_cluster_access_key_list_invoker(self, request):
        http_info = self._show_cluster_access_key_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_cluster_access_key_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dew/cpcs/cluster/{cluster_id}/access-keys",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClusterAccessKeyListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'page_num' in local_var_params:
            query_params.append(('page_num', local_var_params['page_num']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
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

    def show_cluster_uri(self, request):
        r"""获取密码服务管理界面URL

        获取密码服务管理界面URL
        &gt; URL存在有效期，URL失效后无法跳转管理界面，需要重新获取URL
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowClusterUri
        :type request: :class:`huaweicloudsdkcpcs.v1.ShowClusterUriRequest`
        :rtype: :class:`huaweicloudsdkcpcs.v1.ShowClusterUriResponse`
        """
        http_info = self._show_cluster_uri_http_info(request)
        return self._call_api(**http_info)

    def show_cluster_uri_invoker(self, request):
        http_info = self._show_cluster_uri_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_cluster_uri_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dew/cpcs/cluster/{cluster_id}/uri",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClusterUriResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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

    def show_resource_info(self, request):
        r"""查询租户的资源分布信息

        查询租户的资源分布信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowResourceInfo
        :type request: :class:`huaweicloudsdkcpcs.v1.ShowResourceInfoRequest`
        :rtype: :class:`huaweicloudsdkcpcs.v1.ShowResourceInfoResponse`
        """
        http_info = self._show_resource_info_http_info(request)
        return self._call_api(**http_info)

    def show_resource_info_invoker(self, request):
        http_info = self._show_resource_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_resource_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dew/cpcs/resource-info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourceInfoResponse"
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

    def show_vm_monitor(self, request):
        r"""密码资源指标监控

        获取密码服务实例与虚拟密码机实例的指标（cpu使用率，内存使用率等指标）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVmMonitor
        :type request: :class:`huaweicloudsdkcpcs.v1.ShowVmMonitorRequest`
        :rtype: :class:`huaweicloudsdkcpcs.v1.ShowVmMonitorResponse`
        """
        http_info = self._show_vm_monitor_http_info(request)
        return self._call_api(**http_info)

    def show_vm_monitor_invoker(self, request):
        http_info = self._show_vm_monitor_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_vm_monitor_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dew/cpcs/vm-monitor",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVmMonitorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'metric_name' in local_var_params:
            query_params.append(('metric_name', local_var_params['metric_name']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'vsm_id' in local_var_params:
            query_params.append(('vsm_id', local_var_params['vsm_id']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))
        if 'period' in local_var_params:
            query_params.append(('period', local_var_params['period']))
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))

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
