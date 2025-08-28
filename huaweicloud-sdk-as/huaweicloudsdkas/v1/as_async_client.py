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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkas'")


class AsAsyncClient(Client):
    def __init__(self):
        super(AsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkas.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "AsAsyncClient":
                raise TypeError("client type error, support client type is AsAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def attach_callback_instance_life_cycle_hook_async(self, request):
        r"""伸缩实例生命周期回调

        通过生命周期操作令牌或者通过实例ID和生命周期挂钩名称对伸缩实例指定的挂钩进行回调操作。如果在超时时间结束前已完成自定义操作，选择终止或继续完成生命周期操作。如果需要更多时间完成自定义操作，选择延长超时时间，实例保持等待状态的时间将增加1小时。只有实例的生命周期挂钩状态为 HANGING 时才可以进行回调操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AttachCallbackInstanceLifeCycleHook
        :type request: :class:`huaweicloudsdkas.v1.AttachCallbackInstanceLifeCycleHookRequest`
        :rtype: :class:`huaweicloudsdkas.v1.AttachCallbackInstanceLifeCycleHookResponse`
        """
        http_info = self._attach_callback_instance_life_cycle_hook_http_info(request)
        return self._call_api(**http_info)

    def attach_callback_instance_life_cycle_hook_async_invoker(self, request):
        http_info = self._attach_callback_instance_life_cycle_hook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _attach_callback_instance_life_cycle_hook_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_instance_hook/{scaling_group_id}/callback",
            "request_type": request.__class__.__name__,
            "response_type": "AttachCallbackInstanceLifeCycleHookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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

    def batch_add_scaling_instances_async(self, request):
        r"""批量添加实例

        批量移出伸缩组中的实例或批量添加伸缩组外的实例。批量对伸缩组中的实例设置或取消其实例保护属性。批量将伸缩组中的实例转入或移出备用状态。说明：- 单次最多批量操作实例个数为10。批量添加后实例数不能大于伸缩组的最大实例数，批量移出后实例数不能小于伸缩组的最小实例数。- 当伸缩组处于INSERVICE状态且没有伸缩活动时，才能添加实例。- 当伸缩组没有伸缩活动时，才能移出实例。- 向伸缩组中添加实例时，必须保证实例所在的可用区包含于伸缩组的可用区内。- 实例处于INSERVICE状态时才可以进行移出、设置或取消实例保护属性等操作。- 当伸缩组发生自动缩容活动时，设置了实例保护的实例不会被移出伸缩组。- 批量移出弹性伸缩组中的实例时，若该实例加入伸缩组时绑定的监听器和伸缩组本身的监听器相同，会解绑定实例和监听器。若该实例加入伸缩组时绑定的监听器和伸缩组本身的监听器不同，会保留实例和监听器的绑定关系。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAddScalingInstances
        :type request: :class:`huaweicloudsdkas.v1.BatchAddScalingInstancesRequest`
        :rtype: :class:`huaweicloudsdkas.v1.BatchAddScalingInstancesResponse`
        """
        http_info = self._batch_add_scaling_instances_http_info(request)
        return self._call_api(**http_info)

    def batch_add_scaling_instances_async_invoker(self, request):
        http_info = self._batch_add_scaling_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_add_scaling_instances_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_group_instance/{scaling_group_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAddScalingInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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

    def batch_delete_scaling_configs_async(self, request):
        r"""批量删除弹性伸缩配置

        批量删除指定弹性伸缩配置。被伸缩组使用的伸缩配置不能被删除。单次最多删除伸缩配置个数为50。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteScalingConfigs
        :type request: :class:`huaweicloudsdkas.v1.BatchDeleteScalingConfigsRequest`
        :rtype: :class:`huaweicloudsdkas.v1.BatchDeleteScalingConfigsResponse`
        """
        http_info = self._batch_delete_scaling_configs_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_scaling_configs_async_invoker(self, request):
        http_info = self._batch_delete_scaling_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_scaling_configs_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_configurations",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteScalingConfigsResponse"
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

    def batch_delete_scaling_policies_async(self, request):
        r"""批量删除弹性伸缩策略。

        批量启用、停用或者删除弹性伸缩策略。单次最多批量操作伸缩策略个数为20。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteScalingPolicies
        :type request: :class:`huaweicloudsdkas.v1.BatchDeleteScalingPoliciesRequest`
        :rtype: :class:`huaweicloudsdkas.v1.BatchDeleteScalingPoliciesResponse`
        """
        http_info = self._batch_delete_scaling_policies_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_scaling_policies_async_invoker(self, request):
        http_info = self._batch_delete_scaling_policies_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_scaling_policies_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_policies/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteScalingPoliciesResponse"
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

    def batch_pause_scaling_policies_async(self, request):
        r"""批量停用弹性伸缩策略。

        批量启用、停用或者删除弹性伸缩策略。单次最多批量操作伸缩策略个数为20。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchPauseScalingPolicies
        :type request: :class:`huaweicloudsdkas.v1.BatchPauseScalingPoliciesRequest`
        :rtype: :class:`huaweicloudsdkas.v1.BatchPauseScalingPoliciesResponse`
        """
        http_info = self._batch_pause_scaling_policies_http_info(request)
        return self._call_api(**http_info)

    def batch_pause_scaling_policies_async_invoker(self, request):
        http_info = self._batch_pause_scaling_policies_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_pause_scaling_policies_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_policies/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchPauseScalingPoliciesResponse"
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

    def batch_protect_scaling_instances_async(self, request):
        r"""批量设置实例保护

        批量移出伸缩组中的实例或批量添加伸缩组外的实例。批量对伸缩组中的实例设置或取消其实例保护属性。批量将伸缩组中的实例转入或移出备用状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchProtectScalingInstances
        :type request: :class:`huaweicloudsdkas.v1.BatchProtectScalingInstancesRequest`
        :rtype: :class:`huaweicloudsdkas.v1.BatchProtectScalingInstancesResponse`
        """
        http_info = self._batch_protect_scaling_instances_http_info(request)
        return self._call_api(**http_info)

    def batch_protect_scaling_instances_async_invoker(self, request):
        http_info = self._batch_protect_scaling_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_protect_scaling_instances_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_group_instance/{scaling_group_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchProtectScalingInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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

    def batch_remove_scaling_instances_async(self, request):
        r"""批量移除实例

        批量移出伸缩组中的实例或批量添加伸缩组外的实例。批量对伸缩组中的实例设置或取消其实例保护属性。批量将伸缩组中的实例转入或移出备用状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchRemoveScalingInstances
        :type request: :class:`huaweicloudsdkas.v1.BatchRemoveScalingInstancesRequest`
        :rtype: :class:`huaweicloudsdkas.v1.BatchRemoveScalingInstancesResponse`
        """
        http_info = self._batch_remove_scaling_instances_http_info(request)
        return self._call_api(**http_info)

    def batch_remove_scaling_instances_async_invoker(self, request):
        http_info = self._batch_remove_scaling_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_remove_scaling_instances_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_group_instance/{scaling_group_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchRemoveScalingInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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

    def batch_resume_scaling_policies_async(self, request):
        r"""批量启用弹性伸缩策略。

        批量启用、停用或者删除弹性伸缩策略。单次最多批量操作伸缩策略个数为20。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchResumeScalingPolicies
        :type request: :class:`huaweicloudsdkas.v1.BatchResumeScalingPoliciesRequest`
        :rtype: :class:`huaweicloudsdkas.v1.BatchResumeScalingPoliciesResponse`
        """
        http_info = self._batch_resume_scaling_policies_http_info(request)
        return self._call_api(**http_info)

    def batch_resume_scaling_policies_async_invoker(self, request):
        http_info = self._batch_resume_scaling_policies_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_resume_scaling_policies_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_policies/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchResumeScalingPoliciesResponse"
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

    def batch_set_scaling_instances_standby_async(self, request):
        r"""批量将实例转为备用状态

        批量移出伸缩组中的实例或批量添加伸缩组外的实例。批量对伸缩组中的实例设置或取消其实例保护属性。批量将伸缩组中的实例转入或移出备用状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchSetScalingInstancesStandby
        :type request: :class:`huaweicloudsdkas.v1.BatchSetScalingInstancesStandbyRequest`
        :rtype: :class:`huaweicloudsdkas.v1.BatchSetScalingInstancesStandbyResponse`
        """
        http_info = self._batch_set_scaling_instances_standby_http_info(request)
        return self._call_api(**http_info)

    def batch_set_scaling_instances_standby_async_invoker(self, request):
        http_info = self._batch_set_scaling_instances_standby_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_set_scaling_instances_standby_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_group_instance/{scaling_group_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchSetScalingInstancesStandbyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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

    def batch_unprotect_scaling_instances_async(self, request):
        r"""批量取消实例保护

        批量移出伸缩组中的实例或批量添加伸缩组外的实例。批量对伸缩组中的实例设置或取消其实例保护属性。批量将伸缩组中的实例转入或移出备用状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchUnprotectScalingInstances
        :type request: :class:`huaweicloudsdkas.v1.BatchUnprotectScalingInstancesRequest`
        :rtype: :class:`huaweicloudsdkas.v1.BatchUnprotectScalingInstancesResponse`
        """
        http_info = self._batch_unprotect_scaling_instances_http_info(request)
        return self._call_api(**http_info)

    def batch_unprotect_scaling_instances_async_invoker(self, request):
        http_info = self._batch_unprotect_scaling_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_unprotect_scaling_instances_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_group_instance/{scaling_group_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUnprotectScalingInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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

    def batch_unset_scaling_instances_stantby_async(self, request):
        r"""批量将实例移出备用状态

        批量移出伸缩组中的实例或批量添加伸缩组外的实例。批量对伸缩组中的实例设置或取消其实例保护属性。批量将伸缩组中的实例转入或移出备用状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchUnsetScalingInstancesStantby
        :type request: :class:`huaweicloudsdkas.v1.BatchUnsetScalingInstancesStantbyRequest`
        :rtype: :class:`huaweicloudsdkas.v1.BatchUnsetScalingInstancesStantbyResponse`
        """
        http_info = self._batch_unset_scaling_instances_stantby_http_info(request)
        return self._call_api(**http_info)

    def batch_unset_scaling_instances_stantby_async_invoker(self, request):
        http_info = self._batch_unset_scaling_instances_stantby_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_unset_scaling_instances_stantby_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_group_instance/{scaling_group_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUnsetScalingInstancesStantbyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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

    def close_warm_pool_async(self, request):
        r"""关闭暖池

        关闭伸缩组的暖池
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CloseWarmPool
        :type request: :class:`huaweicloudsdkas.v1.CloseWarmPoolRequest`
        :rtype: :class:`huaweicloudsdkas.v1.CloseWarmPoolResponse`
        """
        http_info = self._close_warm_pool_http_info(request)
        return self._call_api(**http_info)

    def close_warm_pool_async_invoker(self, request):
        http_info = self._close_warm_pool_http_info(request)
        return AsyncInvoker(self, http_info)

    def _close_warm_pool_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/autoscaling-api/{project_id}/scaling-groups/{scaling_group_id}/warm-pool",
            "request_type": request.__class__.__name__,
            "response_type": "CloseWarmPoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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

    def create_group_scheduled_task_async(self, request):
        r"""创建计划任务

        创建计划任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateGroupScheduledTask
        :type request: :class:`huaweicloudsdkas.v1.CreateGroupScheduledTaskRequest`
        :rtype: :class:`huaweicloudsdkas.v1.CreateGroupScheduledTaskResponse`
        """
        http_info = self._create_group_scheduled_task_http_info(request)
        return self._call_api(**http_info)

    def create_group_scheduled_task_async_invoker(self, request):
        http_info = self._create_group_scheduled_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_group_scheduled_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling-groups/{scaling_group_id}/scheduled-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGroupScheduledTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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

    def create_lify_cycle_hook_async(self, request):
        r"""创建生命周期挂钩

        创建生命周期挂钩，可为伸缩组添加一个或多个生命周期挂钩，最多添加5个。添加生命周期挂钩后，当伸缩组进行伸缩活动时，实例将被生命周期挂钩挂起并置于等待状态（正在加入伸缩组或正在移出伸缩组），实例将保持此状态直至超时时间结束或者用户手动回调。用户能够在实例保持等待状态的时间段内执行自定义操作，例如，用户可以在新启动的实例上安装或配置软件，也可以在实例终止前从实例中下载日志文件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateLifyCycleHook
        :type request: :class:`huaweicloudsdkas.v1.CreateLifyCycleHookRequest`
        :rtype: :class:`huaweicloudsdkas.v1.CreateLifyCycleHookResponse`
        """
        http_info = self._create_lify_cycle_hook_http_info(request)
        return self._call_api(**http_info)

    def create_lify_cycle_hook_async_invoker(self, request):
        http_info = self._create_lify_cycle_hook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_lify_cycle_hook_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_lifecycle_hook/{scaling_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLifyCycleHookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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

    def create_scaling_config_async(self, request):
        r"""创建弹性伸缩配置

        创建弹性伸缩配置。伸缩配置是伸缩组内实例（弹性云服务器云主机）的模板，定义了伸缩组内待添加的实例的规格数据。伸缩配置与伸缩组是解耦的，同一伸缩配置可以被多个伸缩组使用。默认最多可以创建100个伸缩配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateScalingConfig
        :type request: :class:`huaweicloudsdkas.v1.CreateScalingConfigRequest`
        :rtype: :class:`huaweicloudsdkas.v1.CreateScalingConfigResponse`
        """
        http_info = self._create_scaling_config_http_info(request)
        return self._call_api(**http_info)

    def create_scaling_config_async_invoker(self, request):
        http_info = self._create_scaling_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_scaling_config_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_configuration",
            "request_type": request.__class__.__name__,
            "response_type": "CreateScalingConfigResponse"
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

    def create_scaling_group_async(self, request):
        r"""创建弹性伸缩组

        伸缩组是具有相同应用场景的实例的集合，是启停伸缩策略和进行伸缩活动的基本单位。伸缩组内定义了最大实例数、期望实例数、最小实例数、虚拟私有云、子网、负载均衡等信息。默认最多可以创建10个伸缩组。如果伸缩组配置了负载均衡，在添加或移除实例时，会自动为实例绑定或解绑负载均衡监听器。如果伸缩组使用负载均衡健康检查方式，伸缩组中的实例需要启用负载均衡器的监听端口才能通过健康检查。端口启用可在安全组中进行配置，可参考添加安全组规则进行操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateScalingGroup
        :type request: :class:`huaweicloudsdkas.v1.CreateScalingGroupRequest`
        :rtype: :class:`huaweicloudsdkas.v1.CreateScalingGroupResponse`
        """
        http_info = self._create_scaling_group_http_info(request)
        return self._call_api(**http_info)

    def create_scaling_group_async_invoker(self, request):
        http_info = self._create_scaling_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_scaling_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_group",
            "request_type": request.__class__.__name__,
            "response_type": "CreateScalingGroupResponse"
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

    def create_scaling_notification_async(self, request):
        r"""配置伸缩组通知

        给弹性伸缩组配置通知功能。每调用一次该接口，伸缩组即配置一个通知主题及其通知场景，每个伸缩组最多可以增加5个主题。通知主题由用户事先在SMN创建并进行订阅，当通知主题对应的通知场景出现时，伸缩组会向用户的订阅终端发送通知。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateScalingNotification
        :type request: :class:`huaweicloudsdkas.v1.CreateScalingNotificationRequest`
        :rtype: :class:`huaweicloudsdkas.v1.CreateScalingNotificationResponse`
        """
        http_info = self._create_scaling_notification_http_info(request)
        return self._call_api(**http_info)

    def create_scaling_notification_async_invoker(self, request):
        http_info = self._create_scaling_notification_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_scaling_notification_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_notification/{scaling_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CreateScalingNotificationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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

    def create_scaling_policy_async(self, request):
        r"""创建弹性伸缩策略

        创建弹性伸缩策略。伸缩策略定义了伸缩组内实例的扩张和收缩操作。如果执行伸缩策略造成伸缩组期望实例数与伸缩组内实例数不符，弹性伸缩会自动调整实例资源，以匹配期望实例数。当前伸缩策略支持告警触发策略，周期触发策略，定时触发策略。在策略执行具体动作中，可设置实例变化的个数，或根据当前实例的百分比数进行伸缩。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateScalingPolicy
        :type request: :class:`huaweicloudsdkas.v1.CreateScalingPolicyRequest`
        :rtype: :class:`huaweicloudsdkas.v1.CreateScalingPolicyResponse`
        """
        http_info = self._create_scaling_policy_http_info(request)
        return self._call_api(**http_info)

    def create_scaling_policy_async_invoker(self, request):
        http_info = self._create_scaling_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_scaling_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_policy",
            "request_type": request.__class__.__name__,
            "response_type": "CreateScalingPolicyResponse"
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

    def create_scaling_tag_info_async(self, request):
        r"""创建标签

        创建或删除指定资源的标签。每个伸缩组最多添加10个标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateScalingTagInfo
        :type request: :class:`huaweicloudsdkas.v1.CreateScalingTagInfoRequest`
        :rtype: :class:`huaweicloudsdkas.v1.CreateScalingTagInfoResponse`
        """
        http_info = self._create_scaling_tag_info_http_info(request)
        return self._call_api(**http_info)

    def create_scaling_tag_info_async_invoker(self, request):
        http_info = self._create_scaling_tag_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_scaling_tag_info_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autoscaling-api/v1/{project_id}/{resource_type}/{resource_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "CreateScalingTagInfoResponse"
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

    def delete_group_scheduled_task_async(self, request):
        r"""删除计划任务

        删除计划任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteGroupScheduledTask
        :type request: :class:`huaweicloudsdkas.v1.DeleteGroupScheduledTaskRequest`
        :rtype: :class:`huaweicloudsdkas.v1.DeleteGroupScheduledTaskResponse`
        """
        http_info = self._delete_group_scheduled_task_http_info(request)
        return self._call_api(**http_info)

    def delete_group_scheduled_task_async_invoker(self, request):
        http_info = self._delete_group_scheduled_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_group_scheduled_task_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling-groups/{scaling_group_id}/scheduled-tasks/{scheduled_task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGroupScheduledTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']
        if 'scheduled_task_id' in local_var_params:
            path_params['scheduled_task_id'] = local_var_params['scheduled_task_id']

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

    def delete_lifecycle_hook_async(self, request):
        r"""删除生命周期挂钩

        删除一个指定生命周期挂钩。伸缩组进行伸缩活动时，不允许删除该伸缩组内的生命周期挂钩。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteLifecycleHook
        :type request: :class:`huaweicloudsdkas.v1.DeleteLifecycleHookRequest`
        :rtype: :class:`huaweicloudsdkas.v1.DeleteLifecycleHookResponse`
        """
        http_info = self._delete_lifecycle_hook_http_info(request)
        return self._call_api(**http_info)

    def delete_lifecycle_hook_async_invoker(self, request):
        http_info = self._delete_lifecycle_hook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_lifecycle_hook_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_lifecycle_hook/{scaling_group_id}/{lifecycle_hook_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLifecycleHookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']
        if 'lifecycle_hook_name' in local_var_params:
            path_params['lifecycle_hook_name'] = local_var_params['lifecycle_hook_name']

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

    def delete_scaling_config_async(self, request):
        r"""删除弹性伸缩配置

        删除一个指定弹性伸缩配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteScalingConfig
        :type request: :class:`huaweicloudsdkas.v1.DeleteScalingConfigRequest`
        :rtype: :class:`huaweicloudsdkas.v1.DeleteScalingConfigResponse`
        """
        http_info = self._delete_scaling_config_http_info(request)
        return self._call_api(**http_info)

    def delete_scaling_config_async_invoker(self, request):
        http_info = self._delete_scaling_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_scaling_config_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_configuration/{scaling_configuration_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteScalingConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_configuration_id' in local_var_params:
            path_params['scaling_configuration_id'] = local_var_params['scaling_configuration_id']

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

    def delete_scaling_group_async(self, request):
        r"""删除弹性伸缩组

        删除一个指定弹性伸缩组。force_delete属性表示如果伸缩组存在ECS实例或正在进行伸缩活动，是否强制删除伸缩组并移出和释放ECS实例。默认值为no，表示不强制删除伸缩组。如果force_delete的值为no，必须满足以下两个条件，才能删除伸缩组：条件一：伸缩组没有正在进行的伸缩活动。条件二：伸缩组当前的ECS实例数量（current_instance_number）为0。如果force_delete的值为yes，伸缩组会被置于DELETING状态，拒绝接收新的伸缩活动请求，然后等待已有的伸缩活动完成，最后将伸缩组内所有ECS实例移出伸缩组（用户手动添加的ECS实例会被移出伸缩组，弹性伸缩自动创建的ECS实例会被自动删除）并删除伸缩组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteScalingGroup
        :type request: :class:`huaweicloudsdkas.v1.DeleteScalingGroupRequest`
        :rtype: :class:`huaweicloudsdkas.v1.DeleteScalingGroupResponse`
        """
        http_info = self._delete_scaling_group_http_info(request)
        return self._call_api(**http_info)

    def delete_scaling_group_async_invoker(self, request):
        http_info = self._delete_scaling_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_scaling_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_group/{scaling_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteScalingGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

        query_params = []
        if 'force_delete' in local_var_params:
            query_params.append(('force_delete', local_var_params['force_delete']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_scaling_instance_async(self, request):
        r"""移出弹性伸缩组实例

        从弹性伸缩组中移出一个指定实例。实例处于INSERVICE且移出后实例数不能小于伸缩组的最小实例数时才可以移出。当伸缩组没有伸缩活动时，才能移出实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteScalingInstance
        :type request: :class:`huaweicloudsdkas.v1.DeleteScalingInstanceRequest`
        :rtype: :class:`huaweicloudsdkas.v1.DeleteScalingInstanceResponse`
        """
        http_info = self._delete_scaling_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_scaling_instance_async_invoker(self, request):
        http_info = self._delete_scaling_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_scaling_instance_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_group_instance/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteScalingInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'instance_delete' in local_var_params:
            query_params.append(('instance_delete', local_var_params['instance_delete']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_scaling_notification_async(self, request):
        r"""删除伸缩组通知

        删除指定的弹性伸缩组中指定的通知。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteScalingNotification
        :type request: :class:`huaweicloudsdkas.v1.DeleteScalingNotificationRequest`
        :rtype: :class:`huaweicloudsdkas.v1.DeleteScalingNotificationResponse`
        """
        http_info = self._delete_scaling_notification_http_info(request)
        return self._call_api(**http_info)

    def delete_scaling_notification_async_invoker(self, request):
        http_info = self._delete_scaling_notification_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_scaling_notification_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_notification/{scaling_group_id}/{topic_urn}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteScalingNotificationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']
        if 'topic_urn' in local_var_params:
            path_params['topic_urn'] = local_var_params['topic_urn']

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

    def delete_scaling_policy_async(self, request):
        r"""删除弹性伸缩策略

        删除一个指定弹性伸缩策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteScalingPolicy
        :type request: :class:`huaweicloudsdkas.v1.DeleteScalingPolicyRequest`
        :rtype: :class:`huaweicloudsdkas.v1.DeleteScalingPolicyResponse`
        """
        http_info = self._delete_scaling_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_scaling_policy_async_invoker(self, request):
        http_info = self._delete_scaling_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_scaling_policy_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_policy/{scaling_policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteScalingPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_policy_id' in local_var_params:
            path_params['scaling_policy_id'] = local_var_params['scaling_policy_id']

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

    def delete_scaling_tag_info_async(self, request):
        r"""删除标签

        创建或删除指定资源的标签。每个伸缩组最多添加10个标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteScalingTagInfo
        :type request: :class:`huaweicloudsdkas.v1.DeleteScalingTagInfoRequest`
        :rtype: :class:`huaweicloudsdkas.v1.DeleteScalingTagInfoResponse`
        """
        http_info = self._delete_scaling_tag_info_http_info(request)
        return self._call_api(**http_info)

    def delete_scaling_tag_info_async_invoker(self, request):
        http_info = self._delete_scaling_tag_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_scaling_tag_info_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autoscaling-api/v1/{project_id}/{resource_type}/{resource_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteScalingTagInfoResponse"
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

    def execute_scaling_policy_async(self, request):
        r"""执行弹性伸缩策略。

        立即执行或启用或停止一个指定弹性伸缩策略。当伸缩组、伸缩策略状态处于INSERVICE时，伸缩策略才能被正确执行，否则会执行失败。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteScalingPolicy
        :type request: :class:`huaweicloudsdkas.v1.ExecuteScalingPolicyRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ExecuteScalingPolicyResponse`
        """
        http_info = self._execute_scaling_policy_http_info(request)
        return self._call_api(**http_info)

    def execute_scaling_policy_async_invoker(self, request):
        http_info = self._execute_scaling_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _execute_scaling_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_policy/{scaling_policy_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteScalingPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_policy_id' in local_var_params:
            path_params['scaling_policy_id'] = local_var_params['scaling_policy_id']

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

    def list_group_scheduled_tasks_async(self, request):
        r"""查询计划任务列表

        查询计划任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGroupScheduledTasks
        :type request: :class:`huaweicloudsdkas.v1.ListGroupScheduledTasksRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ListGroupScheduledTasksResponse`
        """
        http_info = self._list_group_scheduled_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_group_scheduled_tasks_async_invoker(self, request):
        http_info = self._list_group_scheduled_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_group_scheduled_tasks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling-groups/{scaling_group_id}/scheduled-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListGroupScheduledTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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

    def list_hook_instances_async(self, request):
        r"""查询伸缩实例挂起信息

        添加生命周期挂钩后，当伸缩组进行伸缩活动时，实例将被挂钩挂起并置于等待状态，根据输入条件过滤查询弹性伸缩组中伸缩实例的挂起信息。可根据实例ID进行条件过滤查询。若不加过滤条件默认查询指定伸缩组内所有实例挂起信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHookInstances
        :type request: :class:`huaweicloudsdkas.v1.ListHookInstancesRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ListHookInstancesResponse`
        """
        http_info = self._list_hook_instances_http_info(request)
        return self._call_api(**http_info)

    def list_hook_instances_async_invoker(self, request):
        http_info = self._list_hook_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_hook_instances_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_instance_hook/{scaling_group_id}/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListHookInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_life_cycle_hooks_async(self, request):
        r"""查询生命周期挂钩列表

        根据伸缩组ID查询生命周期挂钩列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLifeCycleHooks
        :type request: :class:`huaweicloudsdkas.v1.ListLifeCycleHooksRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ListLifeCycleHooksResponse`
        """
        http_info = self._list_life_cycle_hooks_http_info(request)
        return self._call_api(**http_info)

    def list_life_cycle_hooks_async_invoker(self, request):
        http_info = self._list_life_cycle_hooks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_life_cycle_hooks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_lifecycle_hook/{scaling_group_id}/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListLifeCycleHooksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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

    def list_resource_instances_async(self, request):
        r"""查询资源实例

        根据项目ID查询指定资源类型的资源实例。资源、资源tag默认按照创建时间倒序。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResourceInstances
        :type request: :class:`huaweicloudsdkas.v1.ListResourceInstancesRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ListResourceInstancesResponse`
        """
        http_info = self._list_resource_instances_http_info(request)
        return self._call_api(**http_info)

    def list_resource_instances_async_invoker(self, request):
        http_info = self._list_resource_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_resource_instances_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autoscaling-api/v1/{project_id}/{resource_type}/resource_instances/action",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceInstancesResponse"
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

    def list_scaling_activity_logs_async(self, request):
        r"""查询伸缩活动日志

        根据输入条件过滤查询伸缩活动日志。查询结果分页显示。可根据起始时间，截止时间，起始行号，记录数进行条件过滤查询。若不加过滤条件默认查询最多20条伸缩活动日志信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListScalingActivityLogs
        :type request: :class:`huaweicloudsdkas.v1.ListScalingActivityLogsRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ListScalingActivityLogsResponse`
        """
        http_info = self._list_scaling_activity_logs_http_info(request)
        return self._call_api(**http_info)

    def list_scaling_activity_logs_async_invoker(self, request):
        http_info = self._list_scaling_activity_logs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_scaling_activity_logs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_activity_log/{scaling_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListScalingActivityLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'start_number' in local_var_params:
            query_params.append(('start_number', local_var_params['start_number']))
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

    def list_scaling_activity_v2_logs_async(self, request):
        r"""查询伸缩活动日志v2版本

        根据输入条件过滤查询伸缩活动日志，支持查询实例伸缩、ELB迁移、实例备用等类型活动。查询结果分页显示。查询伸缩活动日志V2版本与V1版本区别在于，V2版本展示了更详细的实例伸缩日志，如ELB迁移日志，实例备用日志信息。可根据起始时间，截止时间，起始行号，记录数，伸缩活动类型等作为条件过滤查询。若不加过滤条件默认查询最多20条伸缩活动日志信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListScalingActivityV2Logs
        :type request: :class:`huaweicloudsdkas.v1.ListScalingActivityV2LogsRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ListScalingActivityV2LogsResponse`
        """
        http_info = self._list_scaling_activity_v2_logs_http_info(request)
        return self._call_api(**http_info)

    def list_scaling_activity_v2_logs_async_invoker(self, request):
        http_info = self._list_scaling_activity_v2_logs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_scaling_activity_v2_logs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autoscaling-api/v2/{project_id}/scaling_activity_log/{scaling_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListScalingActivityV2LogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

        query_params = []
        if 'log_id' in local_var_params:
            query_params.append(('log_id', local_var_params['log_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'start_number' in local_var_params:
            query_params.append(('start_number', local_var_params['start_number']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
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

    def list_scaling_configs_async(self, request):
        r"""查询弹性伸缩配置列表

        根据输入条件过滤查询弹性伸缩配置。查询结果分页显示。可以根据伸缩配置名称，镜像ID，起始行号，记录条数进行条件过滤查询。若不加过滤条件默认最多查询租户下20条伸缩配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListScalingConfigs
        :type request: :class:`huaweicloudsdkas.v1.ListScalingConfigsRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ListScalingConfigsResponse`
        """
        http_info = self._list_scaling_configs_http_info(request)
        return self._call_api(**http_info)

    def list_scaling_configs_async_invoker(self, request):
        http_info = self._list_scaling_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_scaling_configs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_configuration",
            "request_type": request.__class__.__name__,
            "response_type": "ListScalingConfigsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'scaling_configuration_name' in local_var_params:
            query_params.append(('scaling_configuration_name', local_var_params['scaling_configuration_name']))
        if 'image_id' in local_var_params:
            query_params.append(('image_id', local_var_params['image_id']))
        if 'start_number' in local_var_params:
            query_params.append(('start_number', local_var_params['start_number']))
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

    def list_scaling_groups_async(self, request):
        r"""查询弹性伸缩组列表

        根据输入条件过滤查询弹性伸缩组列表。查询结果分页显示。可根据伸缩组名称，伸缩配置ID，伸缩组状态，企业项目ID，起始行号，记录条数进行条件过滤查询。若不加过滤条件默认最多查询租户下20条伸缩组信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListScalingGroups
        :type request: :class:`huaweicloudsdkas.v1.ListScalingGroupsRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ListScalingGroupsResponse`
        """
        http_info = self._list_scaling_groups_http_info(request)
        return self._call_api(**http_info)

    def list_scaling_groups_async_invoker(self, request):
        http_info = self._list_scaling_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_scaling_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_group",
            "request_type": request.__class__.__name__,
            "response_type": "ListScalingGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'scaling_group_name' in local_var_params:
            query_params.append(('scaling_group_name', local_var_params['scaling_group_name']))
        if 'scaling_configuration_id' in local_var_params:
            query_params.append(('scaling_configuration_id', local_var_params['scaling_configuration_id']))
        if 'scaling_group_status' in local_var_params:
            query_params.append(('scaling_group_status', local_var_params['scaling_group_status']))
        if 'start_number' in local_var_params:
            query_params.append(('start_number', local_var_params['start_number']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
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

    def list_scaling_instances_async(self, request):
        r"""查询弹性伸缩组中的实例列表

        根据输入条件过滤查询弹性伸缩组中实例信息。查询结果分页显示。可根据实例在伸缩组中的生命周期状态，实例健康状态，实例保护状态，起始行号，记录条数进行条件过滤查询。若不加过滤条件默认查询组内最多20条实例信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListScalingInstances
        :type request: :class:`huaweicloudsdkas.v1.ListScalingInstancesRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ListScalingInstancesResponse`
        """
        http_info = self._list_scaling_instances_http_info(request)
        return self._call_api(**http_info)

    def list_scaling_instances_async_invoker(self, request):
        http_info = self._list_scaling_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_scaling_instances_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_group_instance/{scaling_group_id}/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListScalingInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

        query_params = []
        if 'life_cycle_state' in local_var_params:
            query_params.append(('life_cycle_state', local_var_params['life_cycle_state']))
        if 'health_status' in local_var_params:
            query_params.append(('health_status', local_var_params['health_status']))
        if 'protect_from_scaling_down' in local_var_params:
            query_params.append(('protect_from_scaling_down', local_var_params['protect_from_scaling_down']))
        if 'start_number' in local_var_params:
            query_params.append(('start_number', local_var_params['start_number']))
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

    def list_scaling_notifications_async(self, request):
        r"""查询伸缩组通知列表

        根据伸缩组ID查询指定弹性伸缩组的通知列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListScalingNotifications
        :type request: :class:`huaweicloudsdkas.v1.ListScalingNotificationsRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ListScalingNotificationsResponse`
        """
        http_info = self._list_scaling_notifications_http_info(request)
        return self._call_api(**http_info)

    def list_scaling_notifications_async_invoker(self, request):
        http_info = self._list_scaling_notifications_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_scaling_notifications_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_notification/{scaling_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListScalingNotificationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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

    def list_scaling_policies_async(self, request):
        r"""查询弹性伸缩策略列表

        根据输入条件过滤查询弹性伸缩策略。查询结果分页显示。可根据伸缩策略名称，策略类型，伸缩策略ID，起始行号，记录数进行条件过滤查询。若不加过滤条件默认查询租户下指定伸缩组内最多20条伸缩策略信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListScalingPolicies
        :type request: :class:`huaweicloudsdkas.v1.ListScalingPoliciesRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ListScalingPoliciesResponse`
        """
        http_info = self._list_scaling_policies_http_info(request)
        return self._call_api(**http_info)

    def list_scaling_policies_async_invoker(self, request):
        http_info = self._list_scaling_policies_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_scaling_policies_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_policy/{scaling_group_id}/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListScalingPoliciesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

        query_params = []
        if 'scaling_policy_name' in local_var_params:
            query_params.append(('scaling_policy_name', local_var_params['scaling_policy_name']))
        if 'scaling_policy_type' in local_var_params:
            query_params.append(('scaling_policy_type', local_var_params['scaling_policy_type']))
        if 'scaling_policy_id' in local_var_params:
            query_params.append(('scaling_policy_id', local_var_params['scaling_policy_id']))
        if 'start_number' in local_var_params:
            query_params.append(('start_number', local_var_params['start_number']))
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

    def list_scaling_policy_execute_logs_async(self, request):
        r"""查询策略执行日志

        根据输入条件过滤查询策略执行的历史记录。查询结果分页显示。可根据日志ID，伸缩资源类型，伸缩资源ID，策略执行类型，查询额起始，查询截止时间，查询起始行号，查询记录数进行条件过滤查询。若不加过滤条件默认查询最多20条策略执行日志信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListScalingPolicyExecuteLogs
        :type request: :class:`huaweicloudsdkas.v1.ListScalingPolicyExecuteLogsRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ListScalingPolicyExecuteLogsResponse`
        """
        http_info = self._list_scaling_policy_execute_logs_http_info(request)
        return self._call_api(**http_info)

    def list_scaling_policy_execute_logs_async_invoker(self, request):
        http_info = self._list_scaling_policy_execute_logs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_scaling_policy_execute_logs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_policy_execute_log/{scaling_policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListScalingPolicyExecuteLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_policy_id' in local_var_params:
            path_params['scaling_policy_id'] = local_var_params['scaling_policy_id']

        query_params = []
        if 'log_id' in local_var_params:
            query_params.append(('log_id', local_var_params['log_id']))
        if 'scaling_resource_type' in local_var_params:
            query_params.append(('scaling_resource_type', local_var_params['scaling_resource_type']))
        if 'scaling_resource_id' in local_var_params:
            query_params.append(('scaling_resource_id', local_var_params['scaling_resource_id']))
        if 'execute_type' in local_var_params:
            query_params.append(('execute_type', local_var_params['execute_type']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'start_number' in local_var_params:
            query_params.append(('start_number', local_var_params['start_number']))
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

    def list_scaling_tag_infos_by_resource_id_async(self, request):
        r"""查询资源标签

        根据项目ID和资源ID查询指定资源类型的资源标签列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListScalingTagInfosByResourceId
        :type request: :class:`huaweicloudsdkas.v1.ListScalingTagInfosByResourceIdRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ListScalingTagInfosByResourceIdResponse`
        """
        http_info = self._list_scaling_tag_infos_by_resource_id_http_info(request)
        return self._call_api(**http_info)

    def list_scaling_tag_infos_by_resource_id_async_invoker(self, request):
        http_info = self._list_scaling_tag_infos_by_resource_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_scaling_tag_infos_by_resource_id_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autoscaling-api/v1/{project_id}/{resource_type}/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListScalingTagInfosByResourceIdResponse"
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

    def list_scaling_tag_infos_by_tenant_id_async(self, request):
        r"""查询标签

        根据项目ID查询指定资源类型的标签列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListScalingTagInfosByTenantId
        :type request: :class:`huaweicloudsdkas.v1.ListScalingTagInfosByTenantIdRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ListScalingTagInfosByTenantIdResponse`
        """
        http_info = self._list_scaling_tag_infos_by_tenant_id_http_info(request)
        return self._call_api(**http_info)

    def list_scaling_tag_infos_by_tenant_id_async_invoker(self, request):
        http_info = self._list_scaling_tag_infos_by_tenant_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_scaling_tag_infos_by_tenant_id_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autoscaling-api/v1/{project_id}/{resource_type}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListScalingTagInfosByTenantIdResponse"
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

    def list_warm_pool_instances_async(self, request):
        r"""查询暖池内实例信息

        查询暖池内实例信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWarmPoolInstances
        :type request: :class:`huaweicloudsdkas.v1.ListWarmPoolInstancesRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ListWarmPoolInstancesResponse`
        """
        http_info = self._list_warm_pool_instances_http_info(request)
        return self._call_api(**http_info)

    def list_warm_pool_instances_async_invoker(self, request):
        http_info = self._list_warm_pool_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_warm_pool_instances_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autoscaling-api/{project_id}/scaling-groups/{scaling_group_id}/warm-pool-instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListWarmPoolInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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

    def pause_scaling_group_async(self, request):
        r"""停止弹性伸缩组

        启用或停止一个指定弹性伸缩组。已停用状态的伸缩组，不会自动触发任何伸缩活动。当伸缩组正在进行伸缩活动，即使停用，正在进行的伸缩活动也不会立即停止。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PauseScalingGroup
        :type request: :class:`huaweicloudsdkas.v1.PauseScalingGroupRequest`
        :rtype: :class:`huaweicloudsdkas.v1.PauseScalingGroupResponse`
        """
        http_info = self._pause_scaling_group_http_info(request)
        return self._call_api(**http_info)

    def pause_scaling_group_async_invoker(self, request):
        http_info = self._pause_scaling_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _pause_scaling_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_group/{scaling_group_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "PauseScalingGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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

    def pause_scaling_policy_async(self, request):
        r"""停止弹性伸缩策略。

        立即执行或启用或停止一个指定弹性伸缩策略。当伸缩组、伸缩策略状态处于INSERVICE时，伸缩策略才能被正确执行，否则会执行失败。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PauseScalingPolicy
        :type request: :class:`huaweicloudsdkas.v1.PauseScalingPolicyRequest`
        :rtype: :class:`huaweicloudsdkas.v1.PauseScalingPolicyResponse`
        """
        http_info = self._pause_scaling_policy_http_info(request)
        return self._call_api(**http_info)

    def pause_scaling_policy_async_invoker(self, request):
        http_info = self._pause_scaling_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _pause_scaling_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_policy/{scaling_policy_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "PauseScalingPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_policy_id' in local_var_params:
            path_params['scaling_policy_id'] = local_var_params['scaling_policy_id']

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

    def put_warm_pool_async(self, request):
        r"""开启暖池

        开启并修改暖池参数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PutWarmPool
        :type request: :class:`huaweicloudsdkas.v1.PutWarmPoolRequest`
        :rtype: :class:`huaweicloudsdkas.v1.PutWarmPoolResponse`
        """
        http_info = self._put_warm_pool_http_info(request)
        return self._call_api(**http_info)

    def put_warm_pool_async_invoker(self, request):
        http_info = self._put_warm_pool_http_info(request)
        return AsyncInvoker(self, http_info)

    def _put_warm_pool_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/autoscaling-api/{project_id}/scaling-groups/{scaling_group_id}/warm-pool",
            "request_type": request.__class__.__name__,
            "response_type": "PutWarmPoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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

    def resume_scaling_group_async(self, request):
        r"""启用弹性伸缩组

        启用或停止一个指定弹性伸缩组。已停用状态的伸缩组，不会自动触发任何伸缩活动。当伸缩组正在进行伸缩活动，即使停用，正在进行的伸缩活动也不会立即停止。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResumeScalingGroup
        :type request: :class:`huaweicloudsdkas.v1.ResumeScalingGroupRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ResumeScalingGroupResponse`
        """
        http_info = self._resume_scaling_group_http_info(request)
        return self._call_api(**http_info)

    def resume_scaling_group_async_invoker(self, request):
        http_info = self._resume_scaling_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _resume_scaling_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_group/{scaling_group_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "ResumeScalingGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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

    def resume_scaling_policy_async(self, request):
        r"""启用弹性伸缩策略。

        立即执行或启用或停止一个指定弹性伸缩策略。当伸缩组、伸缩策略状态处于INSERVICE时，伸缩策略才能被正确执行，否则会执行失败。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResumeScalingPolicy
        :type request: :class:`huaweicloudsdkas.v1.ResumeScalingPolicyRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ResumeScalingPolicyResponse`
        """
        http_info = self._resume_scaling_policy_http_info(request)
        return self._call_api(**http_info)

    def resume_scaling_policy_async_invoker(self, request):
        http_info = self._resume_scaling_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _resume_scaling_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_policy/{scaling_policy_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "ResumeScalingPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_policy_id' in local_var_params:
            path_params['scaling_policy_id'] = local_var_params['scaling_policy_id']

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

    def show_life_cycle_hook_async(self, request):
        r"""查询生命周期挂钩详情

        根据伸缩组ID及生命周期挂钩名称查询指定的生命周期挂钩详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowLifeCycleHook
        :type request: :class:`huaweicloudsdkas.v1.ShowLifeCycleHookRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ShowLifeCycleHookResponse`
        """
        http_info = self._show_life_cycle_hook_http_info(request)
        return self._call_api(**http_info)

    def show_life_cycle_hook_async_invoker(self, request):
        http_info = self._show_life_cycle_hook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_life_cycle_hook_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_lifecycle_hook/{scaling_group_id}/{lifecycle_hook_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLifeCycleHookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']
        if 'lifecycle_hook_name' in local_var_params:
            path_params['lifecycle_hook_name'] = local_var_params['lifecycle_hook_name']

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

    def show_policy_and_instance_quota_async(self, request):
        r"""查询弹性伸缩策略和伸缩实例配额

        根据伸缩组ID查询指定弹性伸缩组下的伸缩策略和伸缩实例的配额总数及已使用配额数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPolicyAndInstanceQuota
        :type request: :class:`huaweicloudsdkas.v1.ShowPolicyAndInstanceQuotaRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ShowPolicyAndInstanceQuotaResponse`
        """
        http_info = self._show_policy_and_instance_quota_http_info(request)
        return self._call_api(**http_info)

    def show_policy_and_instance_quota_async_invoker(self, request):
        http_info = self._show_policy_and_instance_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_policy_and_instance_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autoscaling-api/v1/{project_id}/quotas/{scaling_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPolicyAndInstanceQuotaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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

    def show_resource_quota_async(self, request):
        r"""查询配额

        查询指定租户下的弹性伸缩组、伸缩配置、伸缩带宽策略、伸缩策略和伸缩实例的配额总数及已使用配额数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourceQuota
        :type request: :class:`huaweicloudsdkas.v1.ShowResourceQuotaRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ShowResourceQuotaResponse`
        """
        http_info = self._show_resource_quota_http_info(request)
        return self._call_api(**http_info)

    def show_resource_quota_async_invoker(self, request):
        http_info = self._show_resource_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_resource_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autoscaling-api/v1/{project_id}/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourceQuotaResponse"
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

    def show_scaling_config_async(self, request):
        r"""查询弹性伸缩配置详情

        根据伸缩配置ID查询一个弹性伸缩配置的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowScalingConfig
        :type request: :class:`huaweicloudsdkas.v1.ShowScalingConfigRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ShowScalingConfigResponse`
        """
        http_info = self._show_scaling_config_http_info(request)
        return self._call_api(**http_info)

    def show_scaling_config_async_invoker(self, request):
        http_info = self._show_scaling_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_scaling_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_configuration/{scaling_configuration_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowScalingConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_configuration_id' in local_var_params:
            path_params['scaling_configuration_id'] = local_var_params['scaling_configuration_id']

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

    def show_scaling_group_async(self, request):
        r"""查询弹性伸缩组详情

        查询一个指定弹性伸缩组详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowScalingGroup
        :type request: :class:`huaweicloudsdkas.v1.ShowScalingGroupRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ShowScalingGroupResponse`
        """
        http_info = self._show_scaling_group_http_info(request)
        return self._call_api(**http_info)

    def show_scaling_group_async_invoker(self, request):
        http_info = self._show_scaling_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_scaling_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_group/{scaling_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowScalingGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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

    def show_scaling_policy_async(self, request):
        r"""查询弹性伸缩策略详情

        查询指定弹性伸缩策略信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowScalingPolicy
        :type request: :class:`huaweicloudsdkas.v1.ShowScalingPolicyRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ShowScalingPolicyResponse`
        """
        http_info = self._show_scaling_policy_http_info(request)
        return self._call_api(**http_info)

    def show_scaling_policy_async_invoker(self, request):
        http_info = self._show_scaling_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_scaling_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_policy/{scaling_policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowScalingPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_policy_id' in local_var_params:
            path_params['scaling_policy_id'] = local_var_params['scaling_policy_id']

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

    def show_warm_pool_async(self, request):
        r"""查询暖池信息

        查询暖池信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWarmPool
        :type request: :class:`huaweicloudsdkas.v1.ShowWarmPoolRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ShowWarmPoolResponse`
        """
        http_info = self._show_warm_pool_http_info(request)
        return self._call_api(**http_info)

    def show_warm_pool_async_invoker(self, request):
        http_info = self._show_warm_pool_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_warm_pool_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autoscaling-api/{project_id}/scaling-groups/{scaling_group_id}/warm-pool",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWarmPoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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

    def update_group_scheduled_task_async(self, request):
        r"""更新计划任务

        更新计划任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateGroupScheduledTask
        :type request: :class:`huaweicloudsdkas.v1.UpdateGroupScheduledTaskRequest`
        :rtype: :class:`huaweicloudsdkas.v1.UpdateGroupScheduledTaskResponse`
        """
        http_info = self._update_group_scheduled_task_http_info(request)
        return self._call_api(**http_info)

    def update_group_scheduled_task_async_invoker(self, request):
        http_info = self._update_group_scheduled_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_group_scheduled_task_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling-groups/{scaling_group_id}/scheduled-tasks/{scheduled_task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGroupScheduledTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']
        if 'scheduled_task_id' in local_var_params:
            path_params['scheduled_task_id'] = local_var_params['scheduled_task_id']

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

    def update_life_cycle_hook_async(self, request):
        r"""修改生命周期挂钩

        修改一个指定生命周期挂钩中的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateLifeCycleHook
        :type request: :class:`huaweicloudsdkas.v1.UpdateLifeCycleHookRequest`
        :rtype: :class:`huaweicloudsdkas.v1.UpdateLifeCycleHookResponse`
        """
        http_info = self._update_life_cycle_hook_http_info(request)
        return self._call_api(**http_info)

    def update_life_cycle_hook_async_invoker(self, request):
        http_info = self._update_life_cycle_hook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_life_cycle_hook_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_lifecycle_hook/{scaling_group_id}/{lifecycle_hook_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLifeCycleHookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']
        if 'lifecycle_hook_name' in local_var_params:
            path_params['lifecycle_hook_name'] = local_var_params['lifecycle_hook_name']

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

    def update_scaling_group_async(self, request):
        r"""修改弹性伸缩组

        修改一个指定弹性伸缩组中的信息。更换伸缩组的伸缩配置，伸缩组中已经存在的使用之前伸缩配置创建的云服务器云主机不受影响。伸缩组为没有正在进行的伸缩活动时，可以修改伸缩组的子网、可用区和负载均衡配置。当伸缩组的期望实例数改变时，会触发伸缩活动加入或移出实例。期望实例数必须大于或等于最小实例数，必须小于或等于最大实例数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateScalingGroup
        :type request: :class:`huaweicloudsdkas.v1.UpdateScalingGroupRequest`
        :rtype: :class:`huaweicloudsdkas.v1.UpdateScalingGroupResponse`
        """
        http_info = self._update_scaling_group_http_info(request)
        return self._call_api(**http_info)

    def update_scaling_group_async_invoker(self, request):
        http_info = self._update_scaling_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_scaling_group_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_group/{scaling_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateScalingGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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

    def update_scaling_policy_async(self, request):
        r"""修改弹性伸缩策略

        修改指定弹性伸缩策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateScalingPolicy
        :type request: :class:`huaweicloudsdkas.v1.UpdateScalingPolicyRequest`
        :rtype: :class:`huaweicloudsdkas.v1.UpdateScalingPolicyResponse`
        """
        http_info = self._update_scaling_policy_http_info(request)
        return self._call_api(**http_info)

    def update_scaling_policy_async_invoker(self, request):
        http_info = self._update_scaling_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_scaling_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/autoscaling-api/v1/{project_id}/scaling_policy/{scaling_policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateScalingPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_policy_id' in local_var_params:
            path_params['scaling_policy_id'] = local_var_params['scaling_policy_id']

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

    def list_api_versions_async(self, request):
        r"""查询弹性伸缩API所有版本信息

        查询弹性伸缩API所有版本信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApiVersions
        :type request: :class:`huaweicloudsdkas.v1.ListApiVersionsRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ListApiVersionsResponse`
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

    def show_api_version_async(self, request):
        r"""查询弹性伸缩API指定版本信息

        根据租户id和资源id查询指定资源类型的标签列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowApiVersion
        :type request: :class:`huaweicloudsdkas.v1.ShowApiVersionRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ShowApiVersionResponse`
        """
        http_info = self._show_api_version_http_info(request)
        return self._call_api(**http_info)

    def show_api_version_async_invoker(self, request):
        http_info = self._show_api_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_api_version_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/{api_version}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApiVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'api_version' in local_var_params:
            path_params['api_version'] = local_var_params['api_version']

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

    def create_scaling_v2_policy_async(self, request):
        r"""创建弹性伸缩策略（V2版本）

        可针对不同类型资源如伸缩组或带宽，创建弹性伸缩策略。创建弹性伸缩策略V2版本与V1版本的区别在于，V2版本支持创建对带宽资源进行调整的策略，通过伸缩资源类型区分伸缩资源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateScalingV2Policy
        :type request: :class:`huaweicloudsdkas.v1.CreateScalingV2PolicyRequest`
        :rtype: :class:`huaweicloudsdkas.v1.CreateScalingV2PolicyResponse`
        """
        http_info = self._create_scaling_v2_policy_http_info(request)
        return self._call_api(**http_info)

    def create_scaling_v2_policy_async_invoker(self, request):
        http_info = self._create_scaling_v2_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_scaling_v2_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/autoscaling-api/v2/{project_id}/scaling_policy",
            "request_type": request.__class__.__name__,
            "response_type": "CreateScalingV2PolicyResponse"
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

    def list_all_scaling_v2_policies_async(self, request):
        r"""查询弹性伸缩策略全量列表（V2版本）

        根据输入条件过滤查询弹性伸缩策略，支持查询当前租户下全量伸缩策略。查询结果分页显示。可根据伸缩资源ID，伸缩资源类型，伸缩策略名称，伸缩策略ID，告警ID，企业项目ID，起始行号，记录数，排序方式等条件进行过滤查询。若不加过滤添加默认查询该租户下最多20条伸缩策略信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAllScalingV2Policies
        :type request: :class:`huaweicloudsdkas.v1.ListAllScalingV2PoliciesRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ListAllScalingV2PoliciesResponse`
        """
        http_info = self._list_all_scaling_v2_policies_http_info(request)
        return self._call_api(**http_info)

    def list_all_scaling_v2_policies_async_invoker(self, request):
        http_info = self._list_all_scaling_v2_policies_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_all_scaling_v2_policies_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autoscaling-api/v2/{project_id}/scaling_policy",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllScalingV2PoliciesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'scaling_resource_id' in local_var_params:
            query_params.append(('scaling_resource_id', local_var_params['scaling_resource_id']))
        if 'scaling_resource_type' in local_var_params:
            query_params.append(('scaling_resource_type', local_var_params['scaling_resource_type']))
        if 'scaling_policy_name' in local_var_params:
            query_params.append(('scaling_policy_name', local_var_params['scaling_policy_name']))
        if 'scaling_policy_type' in local_var_params:
            query_params.append(('scaling_policy_type', local_var_params['scaling_policy_type']))
        if 'scaling_policy_id' in local_var_params:
            query_params.append(('scaling_policy_id', local_var_params['scaling_policy_id']))
        if 'start_number' in local_var_params:
            query_params.append(('start_number', local_var_params['start_number']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_by' in local_var_params:
            query_params.append(('sort_by', local_var_params['sort_by']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'alarm_id' in local_var_params:
            query_params.append(('alarm_id', local_var_params['alarm_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_scaling_v2_policies_async(self, request):
        r"""查询弹性伸缩策略列表（V2版本）

        根据输入条件过滤查询弹性伸缩策略。查询结果分页显示。查询弹性伸缩策略V2版本与V1版本的区别在于，V2版本响应含伸缩资源类型。可根据伸缩策略名称，策略类型，伸缩策略ID，起始行号，记录数进行条件过滤查询。若不加过滤条件默认查询该租户下指定资源下最多20条伸缩策略信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListScalingV2Policies
        :type request: :class:`huaweicloudsdkas.v1.ListScalingV2PoliciesRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ListScalingV2PoliciesResponse`
        """
        http_info = self._list_scaling_v2_policies_http_info(request)
        return self._call_api(**http_info)

    def list_scaling_v2_policies_async_invoker(self, request):
        http_info = self._list_scaling_v2_policies_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_scaling_v2_policies_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autoscaling-api/v2/{project_id}/scaling_policy/{scaling_resource_id}/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListScalingV2PoliciesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_resource_id' in local_var_params:
            path_params['scaling_resource_id'] = local_var_params['scaling_resource_id']

        query_params = []
        if 'scaling_policy_name' in local_var_params:
            query_params.append(('scaling_policy_name', local_var_params['scaling_policy_name']))
        if 'scaling_policy_type' in local_var_params:
            query_params.append(('scaling_policy_type', local_var_params['scaling_policy_type']))
        if 'scaling_policy_id' in local_var_params:
            query_params.append(('scaling_policy_id', local_var_params['scaling_policy_id']))
        if 'start_number' in local_var_params:
            query_params.append(('start_number', local_var_params['start_number']))
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

    def show_scaling_v2_policy_async(self, request):
        r"""查询指定弹性伸缩策略详情（V2版本）

        查询指定弹性伸缩策略信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowScalingV2Policy
        :type request: :class:`huaweicloudsdkas.v1.ShowScalingV2PolicyRequest`
        :rtype: :class:`huaweicloudsdkas.v1.ShowScalingV2PolicyResponse`
        """
        http_info = self._show_scaling_v2_policy_http_info(request)
        return self._call_api(**http_info)

    def show_scaling_v2_policy_async_invoker(self, request):
        http_info = self._show_scaling_v2_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_scaling_v2_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/autoscaling-api/v2/{project_id}/scaling_policy/{scaling_policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowScalingV2PolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_policy_id' in local_var_params:
            path_params['scaling_policy_id'] = local_var_params['scaling_policy_id']

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

    def update_scaling_v2_policy_async(self, request):
        r"""修改弹性伸缩策略（V2版本）

        修改指定弹性伸缩策略。修改弹性伸缩策略V2版本与V1版本的区别在于，V2版本支持修改伸缩资源类型。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateScalingV2Policy
        :type request: :class:`huaweicloudsdkas.v1.UpdateScalingV2PolicyRequest`
        :rtype: :class:`huaweicloudsdkas.v1.UpdateScalingV2PolicyResponse`
        """
        http_info = self._update_scaling_v2_policy_http_info(request)
        return self._call_api(**http_info)

    def update_scaling_v2_policy_async_invoker(self, request):
        http_info = self._update_scaling_v2_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_scaling_v2_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/autoscaling-api/v2/{project_id}/scaling_policy/{scaling_policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateScalingV2PolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'scaling_policy_id' in local_var_params:
            path_params['scaling_policy_id'] = local_var_params['scaling_policy_id']

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
