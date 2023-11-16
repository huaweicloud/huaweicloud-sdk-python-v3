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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkelb'")


class ElbAsyncClient(Client):
    def __init__(self):
        super(ElbAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkelb.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "ElbAsyncClient":
                raise TypeError("client type error, support client type is ElbAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_create_listener_tags_async(self, request):
        """批量添加监听器标签

        批量添加监听器标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateListenerTags
        :type request: :class:`huaweicloudsdkelb.v2.BatchCreateListenerTagsRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.BatchCreateListenerTagsResponse`
        """
        http_info = self._batch_create_listener_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_listener_tags_async_invoker(self, request):
        http_info = self._batch_create_listener_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_listener_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/listeners/{listener_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateListenerTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'listener_id' in local_var_params:
            path_params['listener_id'] = local_var_params['listener_id']

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

    def batch_create_loadbalancer_tags_async(self, request):
        """批量添加负载均衡器标签

        批量添加负载均衡器标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateLoadbalancerTags
        :type request: :class:`huaweicloudsdkelb.v2.BatchCreateLoadbalancerTagsRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.BatchCreateLoadbalancerTagsResponse`
        """
        http_info = self._batch_create_loadbalancer_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_loadbalancer_tags_async_invoker(self, request):
        http_info = self._batch_create_loadbalancer_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_loadbalancer_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/loadbalancers/{loadbalancer_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateLoadbalancerTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'loadbalancer_id' in local_var_params:
            path_params['loadbalancer_id'] = local_var_params['loadbalancer_id']

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

    def batch_delete_listener_tags_async(self, request):
        """批量删除监听器标签

        批量删除监听器标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteListenerTags
        :type request: :class:`huaweicloudsdkelb.v2.BatchDeleteListenerTagsRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.BatchDeleteListenerTagsResponse`
        """
        http_info = self._batch_delete_listener_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_listener_tags_async_invoker(self, request):
        http_info = self._batch_delete_listener_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_listener_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/listeners/{listener_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteListenerTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'listener_id' in local_var_params:
            path_params['listener_id'] = local_var_params['listener_id']

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

    def batch_delete_loadbalancer_tags_async(self, request):
        """批量删除负载均衡器标签

        批量删除负载均衡器标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteLoadbalancerTags
        :type request: :class:`huaweicloudsdkelb.v2.BatchDeleteLoadbalancerTagsRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.BatchDeleteLoadbalancerTagsResponse`
        """
        http_info = self._batch_delete_loadbalancer_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_loadbalancer_tags_async_invoker(self, request):
        http_info = self._batch_delete_loadbalancer_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_loadbalancer_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/loadbalancers/{loadbalancer_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteLoadbalancerTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'loadbalancer_id' in local_var_params:
            path_params['loadbalancer_id'] = local_var_params['loadbalancer_id']

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

    def create_healthmonitor_async(self, request):
        """创建健康检查

        给后端云服务器组添加健康检查
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateHealthmonitor
        :type request: :class:`huaweicloudsdkelb.v2.CreateHealthmonitorRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.CreateHealthmonitorResponse`
        """
        http_info = self._create_healthmonitor_http_info(request)
        return self._call_api(**http_info)

    def create_healthmonitor_async_invoker(self, request):
        http_info = self._create_healthmonitor_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_healthmonitor_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/elb/healthmonitors",
            "request_type": request.__class__.__name__,
            "response_type": "CreateHealthmonitorResponse"
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

    def create_l7policy_async(self, request):
        """创建转发策略

        创建listener关联的转发策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateL7policy
        :type request: :class:`huaweicloudsdkelb.v2.CreateL7policyRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.CreateL7policyResponse`
        """
        http_info = self._create_l7policy_http_info(request)
        return self._call_api(**http_info)

    def create_l7policy_async_invoker(self, request):
        http_info = self._create_l7policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_l7policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/elb/l7policies",
            "request_type": request.__class__.__name__,
            "response_type": "CreateL7policyResponse"
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

    def create_l7rule_async(self, request):
        """创建转发规则

        创建转发规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateL7rule
        :type request: :class:`huaweicloudsdkelb.v2.CreateL7ruleRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.CreateL7ruleResponse`
        """
        http_info = self._create_l7rule_http_info(request)
        return self._call_api(**http_info)

    def create_l7rule_async_invoker(self, request):
        http_info = self._create_l7rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_l7rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/elb/l7policies/{l7policy_id}/rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateL7ruleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'l7policy_id' in local_var_params:
            path_params['l7policy_id'] = local_var_params['l7policy_id']

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

    def create_listener_async(self, request):
        """创建监听器

        创建与负载均衡器绑定的监听器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateListener
        :type request: :class:`huaweicloudsdkelb.v2.CreateListenerRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.CreateListenerResponse`
        """
        http_info = self._create_listener_http_info(request)
        return self._call_api(**http_info)

    def create_listener_async_invoker(self, request):
        http_info = self._create_listener_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_listener_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/elb/listeners",
            "request_type": request.__class__.__name__,
            "response_type": "CreateListenerResponse"
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

    def create_listener_tags_async(self, request):
        """添加监听器标签

        给指定监听器添加标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateListenerTags
        :type request: :class:`huaweicloudsdkelb.v2.CreateListenerTagsRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.CreateListenerTagsResponse`
        """
        http_info = self._create_listener_tags_http_info(request)
        return self._call_api(**http_info)

    def create_listener_tags_async_invoker(self, request):
        http_info = self._create_listener_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_listener_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/listeners/{listener_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreateListenerTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'listener_id' in local_var_params:
            path_params['listener_id'] = local_var_params['listener_id']

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

    def create_loadbalancer_async(self, request):
        """创建负载均衡器

        创建私网类型的增强型负载均衡器。创建成功后，该接口会返回创建的增强型负载均衡器的ID、所属子网ID、负载均衡器IP等详细信息。若要创建公网类型的增强型负载均衡器，还需调用创建浮动IP的接口，将浮动IP与私网负载均衡器的vip_port_id绑定。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateLoadbalancer
        :type request: :class:`huaweicloudsdkelb.v2.CreateLoadbalancerRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.CreateLoadbalancerResponse`
        """
        http_info = self._create_loadbalancer_http_info(request)
        return self._call_api(**http_info)

    def create_loadbalancer_async_invoker(self, request):
        http_info = self._create_loadbalancer_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_loadbalancer_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/elb/loadbalancers",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLoadbalancerResponse"
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

    def create_loadbalancer_tags_async(self, request):
        """添加负载均衡器标签

        给指定负载均衡器添加标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateLoadbalancerTags
        :type request: :class:`huaweicloudsdkelb.v2.CreateLoadbalancerTagsRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.CreateLoadbalancerTagsResponse`
        """
        http_info = self._create_loadbalancer_tags_http_info(request)
        return self._call_api(**http_info)

    def create_loadbalancer_tags_async_invoker(self, request):
        http_info = self._create_loadbalancer_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_loadbalancer_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/loadbalancers/{loadbalancer_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLoadbalancerTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'loadbalancer_id' in local_var_params:
            path_params['loadbalancer_id'] = local_var_params['loadbalancer_id']

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

    def create_member_async(self, request):
        """创建后端云服务器

        添加属于某个后端云服务器组的后端云服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMember
        :type request: :class:`huaweicloudsdkelb.v2.CreateMemberRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.CreateMemberResponse`
        """
        http_info = self._create_member_http_info(request)
        return self._call_api(**http_info)

    def create_member_async_invoker(self, request):
        http_info = self._create_member_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_member_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/elb/pools/{pool_id}/members",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMemberResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']

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

    def create_pool_async(self, request):
        """创建后端云服务器组

        创建后端云服务器组。将多个后端云服务器添加到后端云服务器组中后，请求会在后端云服务器间按后端云服务器组的负载均衡算法和后端云服务器的权重来做请求分发。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePool
        :type request: :class:`huaweicloudsdkelb.v2.CreatePoolRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.CreatePoolResponse`
        """
        http_info = self._create_pool_http_info(request)
        return self._call_api(**http_info)

    def create_pool_async_invoker(self, request):
        http_info = self._create_pool_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_pool_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/elb/pools",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePoolResponse"
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

    def create_whitelist_async(self, request):
        """创建白名单

        创建白名单，控制监听器的访问权限。若开启了白名单功能，只有白名单中放通的IP可以访问该监听器的后端服务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWhitelist
        :type request: :class:`huaweicloudsdkelb.v2.CreateWhitelistRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.CreateWhitelistResponse`
        """
        http_info = self._create_whitelist_http_info(request)
        return self._call_api(**http_info)

    def create_whitelist_async_invoker(self, request):
        http_info = self._create_whitelist_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_whitelist_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/elb/whitelists",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWhitelistResponse"
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

    def delete_healthmonitor_async(self, request):
        """删除健康检查

        删除健康检查
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteHealthmonitor
        :type request: :class:`huaweicloudsdkelb.v2.DeleteHealthmonitorRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.DeleteHealthmonitorResponse`
        """
        http_info = self._delete_healthmonitor_http_info(request)
        return self._call_api(**http_info)

    def delete_healthmonitor_async_invoker(self, request):
        http_info = self._delete_healthmonitor_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_healthmonitor_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/elb/healthmonitors/{healthmonitor_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteHealthmonitorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'healthmonitor_id' in local_var_params:
            path_params['healthmonitor_id'] = local_var_params['healthmonitor_id']

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

    def delete_l7policy_async(self, request):
        """删除转发策略

        删除转发策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteL7policy
        :type request: :class:`huaweicloudsdkelb.v2.DeleteL7policyRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.DeleteL7policyResponse`
        """
        http_info = self._delete_l7policy_http_info(request)
        return self._call_api(**http_info)

    def delete_l7policy_async_invoker(self, request):
        http_info = self._delete_l7policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_l7policy_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/elb/l7policies/{l7policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteL7policyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'l7policy_id' in local_var_params:
            path_params['l7policy_id'] = local_var_params['l7policy_id']

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

    def delete_l7rule_async(self, request):
        """删除转发规则

        删除转发规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteL7rule
        :type request: :class:`huaweicloudsdkelb.v2.DeleteL7ruleRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.DeleteL7ruleResponse`
        """
        http_info = self._delete_l7rule_http_info(request)
        return self._call_api(**http_info)

    def delete_l7rule_async_invoker(self, request):
        http_info = self._delete_l7rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_l7rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/elb/l7policies/{l7policy_id}/rules/{l7rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteL7ruleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'l7policy_id' in local_var_params:
            path_params['l7policy_id'] = local_var_params['l7policy_id']
        if 'l7rule_id' in local_var_params:
            path_params['l7rule_id'] = local_var_params['l7rule_id']

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

    def delete_listener_async(self, request):
        """删除监听器

        根据指定ID删除监听器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteListener
        :type request: :class:`huaweicloudsdkelb.v2.DeleteListenerRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.DeleteListenerResponse`
        """
        http_info = self._delete_listener_http_info(request)
        return self._call_api(**http_info)

    def delete_listener_async_invoker(self, request):
        http_info = self._delete_listener_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_listener_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/elb/listeners/{listener_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteListenerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'listener_id' in local_var_params:
            path_params['listener_id'] = local_var_params['listener_id']

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

    def delete_listener_tags_async(self, request):
        """删除监听器标签

        删除监听器的某个key对应的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteListenerTags
        :type request: :class:`huaweicloudsdkelb.v2.DeleteListenerTagsRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.DeleteListenerTagsResponse`
        """
        http_info = self._delete_listener_tags_http_info(request)
        return self._call_api(**http_info)

    def delete_listener_tags_async_invoker(self, request):
        http_info = self._delete_listener_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_listener_tags_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/{project_id}/listeners/{listener_id}/tags/{key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteListenerTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'listener_id' in local_var_params:
            path_params['listener_id'] = local_var_params['listener_id']
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

    def delete_loadbalancer_async(self, request):
        """删除负载均衡

        根据指定ID删除负载均衡器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteLoadbalancer
        :type request: :class:`huaweicloudsdkelb.v2.DeleteLoadbalancerRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.DeleteLoadbalancerResponse`
        """
        http_info = self._delete_loadbalancer_http_info(request)
        return self._call_api(**http_info)

    def delete_loadbalancer_async_invoker(self, request):
        http_info = self._delete_loadbalancer_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_loadbalancer_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/elb/loadbalancers/{loadbalancer_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLoadbalancerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'loadbalancer_id' in local_var_params:
            path_params['loadbalancer_id'] = local_var_params['loadbalancer_id']

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

    def delete_loadbalancer_tags_async(self, request):
        """删除负载均衡标签

        删除负载均衡器的某个key对应的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteLoadbalancerTags
        :type request: :class:`huaweicloudsdkelb.v2.DeleteLoadbalancerTagsRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.DeleteLoadbalancerTagsResponse`
        """
        http_info = self._delete_loadbalancer_tags_http_info(request)
        return self._call_api(**http_info)

    def delete_loadbalancer_tags_async_invoker(self, request):
        http_info = self._delete_loadbalancer_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_loadbalancer_tags_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.0/{project_id}/loadbalancers/{loadbalancer_id}/tags/{key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLoadbalancerTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'loadbalancer_id' in local_var_params:
            path_params['loadbalancer_id'] = local_var_params['loadbalancer_id']
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

    def delete_member_async(self, request):
        """删除后端云服务器

        删除后端云服务器
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteMember
        :type request: :class:`huaweicloudsdkelb.v2.DeleteMemberRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.DeleteMemberResponse`
        """
        http_info = self._delete_member_http_info(request)
        return self._call_api(**http_info)

    def delete_member_async_invoker(self, request):
        http_info = self._delete_member_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_member_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/elb/pools/{pool_id}/members/{member_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMemberResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']
        if 'member_id' in local_var_params:
            path_params['member_id'] = local_var_params['member_id']

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

    def delete_pool_async(self, request):
        """删除后端云服务器组

        删除后端云服务器组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePool
        :type request: :class:`huaweicloudsdkelb.v2.DeletePoolRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.DeletePoolResponse`
        """
        http_info = self._delete_pool_http_info(request)
        return self._call_api(**http_info)

    def delete_pool_async_invoker(self, request):
        http_info = self._delete_pool_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_pool_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/elb/pools/{pool_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']

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

    def delete_whitelist_async(self, request):
        """删除白名单

        删除白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteWhitelist
        :type request: :class:`huaweicloudsdkelb.v2.DeleteWhitelistRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.DeleteWhitelistResponse`
        """
        http_info = self._delete_whitelist_http_info(request)
        return self._call_api(**http_info)

    def delete_whitelist_async_invoker(self, request):
        http_info = self._delete_whitelist_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_whitelist_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/elb/whitelists/{whitelist_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteWhitelistResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'whitelist_id' in local_var_params:
            path_params['whitelist_id'] = local_var_params['whitelist_id']

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

    def list_healthmonitors_async(self, request):
        """查询健康检查列表

        查询健康检查列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHealthmonitors
        :type request: :class:`huaweicloudsdkelb.v2.ListHealthmonitorsRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.ListHealthmonitorsResponse`
        """
        http_info = self._list_healthmonitors_http_info(request)
        return self._call_api(**http_info)

    def list_healthmonitors_async_invoker(self, request):
        http_info = self._list_healthmonitors_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_healthmonitors_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/elb/healthmonitors",
            "request_type": request.__class__.__name__,
            "response_type": "ListHealthmonitorsResponse"
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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'delay' in local_var_params:
            query_params.append(('delay', local_var_params['delay']))
        if 'max_retries' in local_var_params:
            query_params.append(('max_retries', local_var_params['max_retries']))
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'timeout' in local_var_params:
            query_params.append(('timeout', local_var_params['timeout']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'monitor_port' in local_var_params:
            query_params.append(('monitor_port', local_var_params['monitor_port']))
        if 'expected_codes' in local_var_params:
            query_params.append(('expected_codes', local_var_params['expected_codes']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'url_path' in local_var_params:
            query_params.append(('url_path', local_var_params['url_path']))
        if 'http_method' in local_var_params:
            query_params.append(('http_method', local_var_params['http_method']))

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

    def list_l7policies_async(self, request):
        """查询转发策略列表

        查询转发策略。支持过滤查询和分页查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListL7policies
        :type request: :class:`huaweicloudsdkelb.v2.ListL7policiesRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.ListL7policiesResponse`
        """
        http_info = self._list_l7policies_http_info(request)
        return self._call_api(**http_info)

    def list_l7policies_async_invoker(self, request):
        http_info = self._list_l7policies_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_l7policies_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/elb/l7policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListL7policiesResponse"
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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'listener_id' in local_var_params:
            query_params.append(('listener_id', local_var_params['listener_id']))
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))
        if 'redirect_pool_id' in local_var_params:
            query_params.append(('redirect_pool_id', local_var_params['redirect_pool_id']))
        if 'redirect_listener_id' in local_var_params:
            query_params.append(('redirect_listener_id', local_var_params['redirect_listener_id']))
        if 'redirect_url' in local_var_params:
            query_params.append(('redirect_url', local_var_params['redirect_url']))
        if 'position' in local_var_params:
            query_params.append(('position', local_var_params['position']))
        if 'provisioning_status' in local_var_params:
            query_params.append(('provisioning_status', local_var_params['provisioning_status']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'display_all_rules' in local_var_params:
            query_params.append(('display_all_rules', local_var_params['display_all_rules']))

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

    def list_l7rules_async(self, request):
        """查询转发规则列表

        查询指定转发策略下关联的转发规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListL7rules
        :type request: :class:`huaweicloudsdkelb.v2.ListL7rulesRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.ListL7rulesResponse`
        """
        http_info = self._list_l7rules_http_info(request)
        return self._call_api(**http_info)

    def list_l7rules_async_invoker(self, request):
        http_info = self._list_l7rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_l7rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/elb/l7policies/{l7policy_id}/rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListL7rulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'l7policy_id' in local_var_params:
            path_params['l7policy_id'] = local_var_params['l7policy_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'compare_type' in local_var_params:
            query_params.append(('compare_type', local_var_params['compare_type']))
        if 'invert' in local_var_params:
            query_params.append(('invert', local_var_params['invert']))
        if 'key' in local_var_params:
            query_params.append(('key', local_var_params['key']))
        if 'value' in local_var_params:
            query_params.append(('value', local_var_params['value']))
        if 'provisioning_status' in local_var_params:
            query_params.append(('provisioning_status', local_var_params['provisioning_status']))

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

    def list_listener_tags_async(self, request):
        """查询所有监听器的标签列表

        查询指定项目下所有监听器的标签列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListListenerTags
        :type request: :class:`huaweicloudsdkelb.v2.ListListenerTagsRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.ListListenerTagsResponse`
        """
        http_info = self._list_listener_tags_http_info(request)
        return self._call_api(**http_info)

    def list_listener_tags_async_invoker(self, request):
        http_info = self._list_listener_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_listener_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/listeners/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListListenerTagsResponse"
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

    def list_listeners_async(self, request):
        """查询监听器列表

        查询监听器列表。支持过滤查询和分页查询。可以通过监听器ID、协议类型、监听端口号、关联的后端云服务器的IP等查询监听器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListListeners
        :type request: :class:`huaweicloudsdkelb.v2.ListListenersRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.ListListenersResponse`
        """
        http_info = self._list_listeners_http_info(request)
        return self._call_api(**http_info)

    def list_listeners_async_invoker(self, request):
        http_info = self._list_listeners_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_listeners_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/elb/listeners",
            "request_type": request.__class__.__name__,
            "response_type": "ListListenersResponse"
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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'loadbalancer_id' in local_var_params:
            query_params.append(('loadbalancer_id', local_var_params['loadbalancer_id']))
        if 'connection_limit' in local_var_params:
            query_params.append(('connection_limit', local_var_params['connection_limit']))
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'default_pool_id' in local_var_params:
            query_params.append(('default_pool_id', local_var_params['default_pool_id']))
        if 'default_tls_container_ref' in local_var_params:
            query_params.append(('default_tls_container_ref', local_var_params['default_tls_container_ref']))
        if 'client_ca_tls_container_ref' in local_var_params:
            query_params.append(('client_ca_tls_container_ref', local_var_params['client_ca_tls_container_ref']))
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
        if 'protocol_port' in local_var_params:
            query_params.append(('protocol_port', local_var_params['protocol_port']))
        if 'tls_ciphers_policy' in local_var_params:
            query_params.append(('tls_ciphers_policy', local_var_params['tls_ciphers_policy']))
        if 'tls_container_id' in local_var_params:
            query_params.append(('tls_container_id', local_var_params['tls_container_id']))
        if 'http2_enable' in local_var_params:
            query_params.append(('http2_enable', local_var_params['http2_enable']))
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

    def list_listeners_by_tags_async(self, request):
        """根据标签查询监听器

        根据标签过滤查询监听器实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListListenersByTags
        :type request: :class:`huaweicloudsdkelb.v2.ListListenersByTagsRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.ListListenersByTagsResponse`
        """
        http_info = self._list_listeners_by_tags_http_info(request)
        return self._call_api(**http_info)

    def list_listeners_by_tags_async_invoker(self, request):
        http_info = self._list_listeners_by_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_listeners_by_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/listeners/resource_instances/action",
            "request_type": request.__class__.__name__,
            "response_type": "ListListenersByTagsResponse"
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

    def list_loadbalancer_tags_async(self, request):
        """查询所有负载均衡器的标签列表

        查询指定项目下所有负载均衡器的标签列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLoadbalancerTags
        :type request: :class:`huaweicloudsdkelb.v2.ListLoadbalancerTagsRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.ListLoadbalancerTagsResponse`
        """
        http_info = self._list_loadbalancer_tags_http_info(request)
        return self._call_api(**http_info)

    def list_loadbalancer_tags_async_invoker(self, request):
        http_info = self._list_loadbalancer_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_loadbalancer_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/loadbalancers/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListLoadbalancerTagsResponse"
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

    def list_loadbalancers_async(self, request):
        """查询负载均衡列表

        查询负载均衡器列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLoadbalancers
        :type request: :class:`huaweicloudsdkelb.v2.ListLoadbalancersRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.ListLoadbalancersResponse`
        """
        http_info = self._list_loadbalancers_http_info(request)
        return self._call_api(**http_info)

    def list_loadbalancers_async_invoker(self, request):
        http_info = self._list_loadbalancers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_loadbalancers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/elb/loadbalancers",
            "request_type": request.__class__.__name__,
            "response_type": "ListLoadbalancersResponse"
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
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'operating_status' in local_var_params:
            query_params.append(('operating_status', local_var_params['operating_status']))
        if 'provisioning_status' in local_var_params:
            query_params.append(('provisioning_status', local_var_params['provisioning_status']))
        if 'vip_address' in local_var_params:
            query_params.append(('vip_address', local_var_params['vip_address']))
        if 'vip_port_id' in local_var_params:
            query_params.append(('vip_port_id', local_var_params['vip_port_id']))
        if 'vip_subnet_id' in local_var_params:
            query_params.append(('vip_subnet_id', local_var_params['vip_subnet_id']))
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'member_address' in local_var_params:
            query_params.append(('member_address', local_var_params['member_address']))
        if 'member_device_id' in local_var_params:
            query_params.append(('member_device_id', local_var_params['member_device_id']))

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

    def list_loadbalancers_by_tags_async(self, request):
        """根据标签查询负载均衡器

        根据标签过滤查询负载均衡实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLoadbalancersByTags
        :type request: :class:`huaweicloudsdkelb.v2.ListLoadbalancersByTagsRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.ListLoadbalancersByTagsResponse`
        """
        http_info = self._list_loadbalancers_by_tags_http_info(request)
        return self._call_api(**http_info)

    def list_loadbalancers_by_tags_async_invoker(self, request):
        http_info = self._list_loadbalancers_by_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_loadbalancers_by_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.0/{project_id}/loadbalancers/resource_instances/action",
            "request_type": request.__class__.__name__,
            "response_type": "ListLoadbalancersByTagsResponse"
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

    def list_members_async(self, request):
        """查询后端云服务器列表

        查询属于某个后端云服务器组的后端云服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMembers
        :type request: :class:`huaweicloudsdkelb.v2.ListMembersRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.ListMembersResponse`
        """
        http_info = self._list_members_http_info(request)
        return self._call_api(**http_info)

    def list_members_async_invoker(self, request):
        http_info = self._list_members_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_members_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/elb/pools/{pool_id}/members",
            "request_type": request.__class__.__name__,
            "response_type": "ListMembersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'address' in local_var_params:
            query_params.append(('address', local_var_params['address']))
        if 'protocol_port' in local_var_params:
            query_params.append(('protocol_port', local_var_params['protocol_port']))
        if 'subnet_id' in local_var_params:
            query_params.append(('subnet_id', local_var_params['subnet_id']))
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'weight' in local_var_params:
            query_params.append(('weight', local_var_params['weight']))

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

    def list_pools_async(self, request):
        """查询后端云服务器组列表

        查询后端云服务器组列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPools
        :type request: :class:`huaweicloudsdkelb.v2.ListPoolsRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.ListPoolsResponse`
        """
        http_info = self._list_pools_http_info(request)
        return self._call_api(**http_info)

    def list_pools_async_invoker(self, request):
        http_info = self._list_pools_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_pools_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/elb/pools",
            "request_type": request.__class__.__name__,
            "response_type": "ListPoolsResponse"
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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'healthmonitor_id' in local_var_params:
            query_params.append(('healthmonitor_id', local_var_params['healthmonitor_id']))
        if 'loadbalancer_id' in local_var_params:
            query_params.append(('loadbalancer_id', local_var_params['loadbalancer_id']))
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
        if 'lb_algorithm' in local_var_params:
            query_params.append(('lb_algorithm', local_var_params['lb_algorithm']))
        if 'member_address' in local_var_params:
            query_params.append(('member_address', local_var_params['member_address']))
        if 'member_device_id' in local_var_params:
            query_params.append(('member_device_id', local_var_params['member_device_id']))
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

    def list_whitelists_async(self, request):
        """查询白名单列表

        查询白名单，支持过滤查询和分页查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWhitelists
        :type request: :class:`huaweicloudsdkelb.v2.ListWhitelistsRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.ListWhitelistsResponse`
        """
        http_info = self._list_whitelists_http_info(request)
        return self._call_api(**http_info)

    def list_whitelists_async_invoker(self, request):
        http_info = self._list_whitelists_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_whitelists_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/elb/whitelists",
            "request_type": request.__class__.__name__,
            "response_type": "ListWhitelistsResponse"
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
        if 'enable_whitelist' in local_var_params:
            query_params.append(('enable_whitelist', local_var_params['enable_whitelist']))
        if 'listener_id' in local_var_params:
            query_params.append(('listener_id', local_var_params['listener_id']))
        if 'whitelist' in local_var_params:
            query_params.append(('whitelist', local_var_params['whitelist']))

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

    def show_healthmonitors_async(self, request):
        """查询健康检查详情

        根据指定ID查询健康检查详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHealthmonitors
        :type request: :class:`huaweicloudsdkelb.v2.ShowHealthmonitorsRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.ShowHealthmonitorsResponse`
        """
        http_info = self._show_healthmonitors_http_info(request)
        return self._call_api(**http_info)

    def show_healthmonitors_async_invoker(self, request):
        http_info = self._show_healthmonitors_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_healthmonitors_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/elb/healthmonitors/{healthmonitor_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHealthmonitorsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'healthmonitor_id' in local_var_params:
            path_params['healthmonitor_id'] = local_var_params['healthmonitor_id']

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

    def show_l7policy_async(self, request):
        """查询转发策略详情

        根据指定ID查询转发策略详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowL7policy
        :type request: :class:`huaweicloudsdkelb.v2.ShowL7policyRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.ShowL7policyResponse`
        """
        http_info = self._show_l7policy_http_info(request)
        return self._call_api(**http_info)

    def show_l7policy_async_invoker(self, request):
        http_info = self._show_l7policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_l7policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/elb/l7policies/{l7policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowL7policyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'l7policy_id' in local_var_params:
            path_params['l7policy_id'] = local_var_params['l7policy_id']

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

    def show_l7rule_async(self, request):
        """查询转发规则详情

        根据指定ID查询某转发策略下关联的转发规则详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowL7rule
        :type request: :class:`huaweicloudsdkelb.v2.ShowL7ruleRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.ShowL7ruleResponse`
        """
        http_info = self._show_l7rule_http_info(request)
        return self._call_api(**http_info)

    def show_l7rule_async_invoker(self, request):
        http_info = self._show_l7rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_l7rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/elb/l7policies/{l7policy_id}/rules/{l7rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowL7ruleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'l7policy_id' in local_var_params:
            path_params['l7policy_id'] = local_var_params['l7policy_id']
        if 'l7rule_id' in local_var_params:
            path_params['l7rule_id'] = local_var_params['l7rule_id']

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

    def show_listener_async(self, request):
        """查询监听器详情

        根据指定ID查询监听器详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowListener
        :type request: :class:`huaweicloudsdkelb.v2.ShowListenerRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.ShowListenerResponse`
        """
        http_info = self._show_listener_http_info(request)
        return self._call_api(**http_info)

    def show_listener_async_invoker(self, request):
        http_info = self._show_listener_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_listener_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/elb/listeners/{listener_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowListenerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'listener_id' in local_var_params:
            path_params['listener_id'] = local_var_params['listener_id']

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

    def show_listener_tags_async(self, request):
        """查询监听器的标签详情

        查询指定监听器的所有标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowListenerTags
        :type request: :class:`huaweicloudsdkelb.v2.ShowListenerTagsRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.ShowListenerTagsResponse`
        """
        http_info = self._show_listener_tags_http_info(request)
        return self._call_api(**http_info)

    def show_listener_tags_async_invoker(self, request):
        http_info = self._show_listener_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_listener_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/listeners/{listener_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowListenerTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'listener_id' in local_var_params:
            path_params['listener_id'] = local_var_params['listener_id']

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

    def show_loadbalancer_async(self, request):
        """查询负载均衡详情

        根据指定负载均衡器ID查询负载均衡器详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowLoadbalancer
        :type request: :class:`huaweicloudsdkelb.v2.ShowLoadbalancerRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.ShowLoadbalancerResponse`
        """
        http_info = self._show_loadbalancer_http_info(request)
        return self._call_api(**http_info)

    def show_loadbalancer_async_invoker(self, request):
        http_info = self._show_loadbalancer_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_loadbalancer_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/elb/loadbalancers/{loadbalancer_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLoadbalancerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'loadbalancer_id' in local_var_params:
            path_params['loadbalancer_id'] = local_var_params['loadbalancer_id']

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

    def show_loadbalancer_tags_async(self, request):
        """查询负载均衡器的标签详情

        查询指定负载均衡器的所有标签信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowLoadbalancerTags
        :type request: :class:`huaweicloudsdkelb.v2.ShowLoadbalancerTagsRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.ShowLoadbalancerTagsResponse`
        """
        http_info = self._show_loadbalancer_tags_http_info(request)
        return self._call_api(**http_info)

    def show_loadbalancer_tags_async_invoker(self, request):
        http_info = self._show_loadbalancer_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_loadbalancer_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/{project_id}/loadbalancers/{loadbalancer_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLoadbalancerTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'loadbalancer_id' in local_var_params:
            path_params['loadbalancer_id'] = local_var_params['loadbalancer_id']

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

    def show_loadbalancers_status_async(self, request):
        """查询负载均衡状态树

        查询负载均衡器状态树。可通过该接口查询负载均衡器关联的监听器、后端云服务器组、后端云服务器、健康检查、转发策略、转发规则的主要信息，了解负载均衡器下资源的拓扑情况。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowLoadbalancersStatus
        :type request: :class:`huaweicloudsdkelb.v2.ShowLoadbalancersStatusRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.ShowLoadbalancersStatusResponse`
        """
        http_info = self._show_loadbalancers_status_http_info(request)
        return self._call_api(**http_info)

    def show_loadbalancers_status_async_invoker(self, request):
        http_info = self._show_loadbalancers_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_loadbalancers_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/elb/loadbalancers/{loadbalancer_id}/statuses",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLoadbalancersStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'loadbalancer_id' in local_var_params:
            path_params['loadbalancer_id'] = local_var_params['loadbalancer_id']

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

    def show_member_async(self, request):
        """查询后端云服务器详情

        根据指定ID查询后端云服务器详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMember
        :type request: :class:`huaweicloudsdkelb.v2.ShowMemberRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.ShowMemberResponse`
        """
        http_info = self._show_member_http_info(request)
        return self._call_api(**http_info)

    def show_member_async_invoker(self, request):
        http_info = self._show_member_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_member_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/elb/pools/{pool_id}/members/{member_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMemberResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']
        if 'member_id' in local_var_params:
            path_params['member_id'] = local_var_params['member_id']

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

    def show_pool_async(self, request):
        """查询后端云服务器组详情

        根据指定ID查询后端云服务器组详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPool
        :type request: :class:`huaweicloudsdkelb.v2.ShowPoolRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.ShowPoolResponse`
        """
        http_info = self._show_pool_http_info(request)
        return self._call_api(**http_info)

    def show_pool_async_invoker(self, request):
        http_info = self._show_pool_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_pool_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/elb/pools/{pool_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']

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

    def show_whitelist_async(self, request):
        """查询白名单详情

        根据指定ID查询白名单详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWhitelist
        :type request: :class:`huaweicloudsdkelb.v2.ShowWhitelistRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.ShowWhitelistResponse`
        """
        http_info = self._show_whitelist_http_info(request)
        return self._call_api(**http_info)

    def show_whitelist_async_invoker(self, request):
        http_info = self._show_whitelist_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_whitelist_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/elb/whitelists/{whitelist_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWhitelistResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'whitelist_id' in local_var_params:
            path_params['whitelist_id'] = local_var_params['whitelist_id']

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

    def update_healthmonitor_async(self, request):
        """更新健康检查

        更新健康检查
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateHealthmonitor
        :type request: :class:`huaweicloudsdkelb.v2.UpdateHealthmonitorRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.UpdateHealthmonitorResponse`
        """
        http_info = self._update_healthmonitor_http_info(request)
        return self._call_api(**http_info)

    def update_healthmonitor_async_invoker(self, request):
        http_info = self._update_healthmonitor_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_healthmonitor_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/elb/healthmonitors/{healthmonitor_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHealthmonitorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'healthmonitor_id' in local_var_params:
            path_params['healthmonitor_id'] = local_var_params['healthmonitor_id']

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

    def update_l7policies_async(self, request):
        """更新转发策略

        更新转发策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateL7policies
        :type request: :class:`huaweicloudsdkelb.v2.UpdateL7policiesRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.UpdateL7policiesResponse`
        """
        http_info = self._update_l7policies_http_info(request)
        return self._call_api(**http_info)

    def update_l7policies_async_invoker(self, request):
        http_info = self._update_l7policies_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_l7policies_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/elb/l7policies/{l7policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateL7policiesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'l7policy_id' in local_var_params:
            path_params['l7policy_id'] = local_var_params['l7policy_id']

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

    def update_l7rule_async(self, request):
        """更新转发规则

        更新指定的转发规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateL7rule
        :type request: :class:`huaweicloudsdkelb.v2.UpdateL7ruleRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.UpdateL7ruleResponse`
        """
        http_info = self._update_l7rule_http_info(request)
        return self._call_api(**http_info)

    def update_l7rule_async_invoker(self, request):
        http_info = self._update_l7rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_l7rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/elb/l7policies/{l7policy_id}/rules/{l7rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateL7ruleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'l7policy_id' in local_var_params:
            path_params['l7policy_id'] = local_var_params['l7policy_id']
        if 'l7rule_id' in local_var_params:
            path_params['l7rule_id'] = local_var_params['l7rule_id']

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

    def update_listener_async(self, request):
        """更新监听器

        更新监听器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateListener
        :type request: :class:`huaweicloudsdkelb.v2.UpdateListenerRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.UpdateListenerResponse`
        """
        http_info = self._update_listener_http_info(request)
        return self._call_api(**http_info)

    def update_listener_async_invoker(self, request):
        http_info = self._update_listener_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_listener_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/elb/listeners/{listener_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateListenerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'listener_id' in local_var_params:
            path_params['listener_id'] = local_var_params['listener_id']

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

    def update_loadbalancer_async(self, request):
        """更新负载均衡器

        更新负载均衡器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateLoadbalancer
        :type request: :class:`huaweicloudsdkelb.v2.UpdateLoadbalancerRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.UpdateLoadbalancerResponse`
        """
        http_info = self._update_loadbalancer_http_info(request)
        return self._call_api(**http_info)

    def update_loadbalancer_async_invoker(self, request):
        http_info = self._update_loadbalancer_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_loadbalancer_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/elb/loadbalancers/{loadbalancer_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLoadbalancerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'loadbalancer_id' in local_var_params:
            path_params['loadbalancer_id'] = local_var_params['loadbalancer_id']

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

    def update_member_async(self, request):
        """更新后端云服务器

        更新后端云服务器
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMember
        :type request: :class:`huaweicloudsdkelb.v2.UpdateMemberRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.UpdateMemberResponse`
        """
        http_info = self._update_member_http_info(request)
        return self._call_api(**http_info)

    def update_member_async_invoker(self, request):
        http_info = self._update_member_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_member_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/elb/pools/{pool_id}/members/{member_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMemberResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'member_id' in local_var_params:
            path_params['member_id'] = local_var_params['member_id']
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']

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

    def update_pool_async(self, request):
        """更新后端云服务器组

        更新后端云服务器组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePool
        :type request: :class:`huaweicloudsdkelb.v2.UpdatePoolRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.UpdatePoolResponse`
        """
        http_info = self._update_pool_http_info(request)
        return self._call_api(**http_info)

    def update_pool_async_invoker(self, request):
        http_info = self._update_pool_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_pool_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/elb/pools/{pool_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']

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

    def update_whitelist_async(self, request):
        """更新白名单

        更新白名单。可以打开或关闭白名单，或更新访问控制的IP。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateWhitelist
        :type request: :class:`huaweicloudsdkelb.v2.UpdateWhitelistRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.UpdateWhitelistResponse`
        """
        http_info = self._update_whitelist_http_info(request)
        return self._call_api(**http_info)

    def update_whitelist_async_invoker(self, request):
        http_info = self._update_whitelist_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_whitelist_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/elb/whitelists/{whitelist_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateWhitelistResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'whitelist_id' in local_var_params:
            path_params['whitelist_id'] = local_var_params['whitelist_id']

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

    def create_certificate_async(self, request):
        """创建SSL证书

        创建SSL证书。将监听器和SSL证书绑定后，可以通过负载均衡器实现服务端认证，后端服务器只要提供HTTP服务就能实现安全可靠的连接。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCertificate
        :type request: :class:`huaweicloudsdkelb.v2.CreateCertificateRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.CreateCertificateResponse`
        """
        http_info = self._create_certificate_http_info(request)
        return self._call_api(**http_info)

    def create_certificate_async_invoker(self, request):
        http_info = self._create_certificate_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_certificate_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/elb/certificates",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCertificateResponse"
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

    def delete_certificate_async(self, request):
        """删除SSL证书

        删除指定的SSL证书
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCertificate
        :type request: :class:`huaweicloudsdkelb.v2.DeleteCertificateRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.DeleteCertificateResponse`
        """
        http_info = self._delete_certificate_http_info(request)
        return self._call_api(**http_info)

    def delete_certificate_async_invoker(self, request):
        http_info = self._delete_certificate_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_certificate_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/elb/certificates/{certificate_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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

    def list_certificates_async(self, request):
        """查询SSL证书列表

        查询SSL证书。支持过滤查询和分页查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCertificates
        :type request: :class:`huaweicloudsdkelb.v2.ListCertificatesRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.ListCertificatesResponse`
        """
        http_info = self._list_certificates_http_info(request)
        return self._call_api(**http_info)

    def list_certificates_async_invoker(self, request):
        http_info = self._list_certificates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_certificates_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/elb/certificates",
            "request_type": request.__class__.__name__,
            "response_type": "ListCertificatesResponse"
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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'private_key' in local_var_params:
            query_params.append(('private_key', local_var_params['private_key']))
        if 'certificate' in local_var_params:
            query_params.append(('certificate', local_var_params['certificate']))

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

    def show_certificate_async(self, request):
        """查询SSL证书详情

        查询指定SSL证书的详情信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCertificate
        :type request: :class:`huaweicloudsdkelb.v2.ShowCertificateRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.ShowCertificateResponse`
        """
        http_info = self._show_certificate_http_info(request)
        return self._call_api(**http_info)

    def show_certificate_async_invoker(self, request):
        http_info = self._show_certificate_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_certificate_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/elb/certificates/{certificate_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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

    def update_certificate_async(self, request):
        """更新SSL证书

        更新指定的SSL证书
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCertificate
        :type request: :class:`huaweicloudsdkelb.v2.UpdateCertificateRequest`
        :rtype: :class:`huaweicloudsdkelb.v2.UpdateCertificateResponse`
        """
        http_info = self._update_certificate_http_info(request)
        return self._call_api(**http_info)

    def update_certificate_async_invoker(self, request):
        http_info = self._update_certificate_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_certificate_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/elb/certificates/{certificate_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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
