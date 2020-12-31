# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

import six

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class AsClient(Client):
    """
    :param configuration: .Configuration object for this client
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def __init__(self):
        super(AsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkas.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "AsClient":
            raise TypeError("client type error, support client type is AsClient")

        return ClientBuilder(clazz)

    def batch_delete_scaling_configs(self, request):
        """批量删除弹性伸缩配置

        批量删除指定弹性伸缩配置。被伸缩组使用的伸缩配置不能被删除。单次最多删除伸缩配置个数为50。

        :param BatchDeleteScalingConfigsRequest request
        :return: BatchDeleteScalingConfigsResponse
        """
        return self.batch_delete_scaling_configs_with_http_info(request)

    def batch_delete_scaling_configs_with_http_info(self, request):
        """批量删除弹性伸缩配置

        批量删除指定弹性伸缩配置。被伸缩组使用的伸缩配置不能被删除。单次最多删除伸缩配置个数为50。

        :param BatchDeleteScalingConfigsRequest request
        :return: BatchDeleteScalingConfigsResponse
        """

        all_params = ['bodyparam']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/autoscaling-api/v1/{project_id}/scaling_configurations',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteScalingConfigsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def complete_lifecycle_action(self, request):
        """伸缩实例生命周期回调

        通过生命周期操作令牌或者通过实例ID和生命周期挂钩名称对伸缩实例指定的挂钩进行回调操作。如果在超时时间结束前已完成自定义操作，选择终止或继续完成生命周期操作。如果需要更多时间完成自定义操作，选择延长超时时间，实例保持等待状态的时间将增加1小时。只有实例的生命周期挂钩状态为 HANGING 时才可以进行回调操作。

        :param CompleteLifecycleActionRequest request
        :return: CompleteLifecycleActionResponse
        """
        return self.complete_lifecycle_action_with_http_info(request)

    def complete_lifecycle_action_with_http_info(self, request):
        """伸缩实例生命周期回调

        通过生命周期操作令牌或者通过实例ID和生命周期挂钩名称对伸缩实例指定的挂钩进行回调操作。如果在超时时间结束前已完成自定义操作，选择终止或继续完成生命周期操作。如果需要更多时间完成自定义操作，选择延长超时时间，实例保持等待状态的时间将增加1小时。只有实例的生命周期挂钩状态为 HANGING 时才可以进行回调操作。

        :param CompleteLifecycleActionRequest request
        :return: CompleteLifecycleActionResponse
        """

        all_params = ['scaling_group_id', 'bodyparam']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/autoscaling-api/v1/{project_id}/scaling_instance_hook/{scaling_group_id}/callback',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CompleteLifecycleActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_lify_cycle_hook(self, request):
        """创建生命周期挂钩

        创建生命周期挂钩，可为伸缩组添加一个或多个生命周期挂钩，最多添加5个。添加生命周期挂钩后，当伸缩组进行伸缩活动时，实例将被生命周期挂钩挂起并置于等待状态（正在加入伸缩组或正在移出伸缩组），实例将保持此状态直至超时时间结束或者用户手动回调。用户能够在实例保持等待状态的时间段内执行自定义操作，例如，用户可以在新启动的实例上安装或配置软件，也可以在实例终止前从实例中下载日志文件。

        :param CreateLifyCycleHookRequest request
        :return: CreateLifyCycleHookResponse
        """
        return self.create_lify_cycle_hook_with_http_info(request)

    def create_lify_cycle_hook_with_http_info(self, request):
        """创建生命周期挂钩

        创建生命周期挂钩，可为伸缩组添加一个或多个生命周期挂钩，最多添加5个。添加生命周期挂钩后，当伸缩组进行伸缩活动时，实例将被生命周期挂钩挂起并置于等待状态（正在加入伸缩组或正在移出伸缩组），实例将保持此状态直至超时时间结束或者用户手动回调。用户能够在实例保持等待状态的时间段内执行自定义操作，例如，用户可以在新启动的实例上安装或配置软件，也可以在实例终止前从实例中下载日志文件。

        :param CreateLifyCycleHookRequest request
        :return: CreateLifyCycleHookResponse
        """

        all_params = ['scaling_group_id', 'bodyparam']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/autoscaling-api/v1/{project_id}/scaling_lifecycle_hook/{scaling_group_id}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateLifyCycleHookResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_scaling_config(self, request):
        """创建弹性伸缩配置

        创建弹性伸缩配置。伸缩配置是伸缩组内实例（弹性云服务器云主机）的模板，定义了伸缩组内待添加的实例的规格数据。伸缩配置与伸缩组是解耦的，同一伸缩配置可以被多个伸缩组使用。默认最多可以创建100个伸缩配置。

        :param CreateScalingConfigRequest request
        :return: CreateScalingConfigResponse
        """
        return self.create_scaling_config_with_http_info(request)

    def create_scaling_config_with_http_info(self, request):
        """创建弹性伸缩配置

        创建弹性伸缩配置。伸缩配置是伸缩组内实例（弹性云服务器云主机）的模板，定义了伸缩组内待添加的实例的规格数据。伸缩配置与伸缩组是解耦的，同一伸缩配置可以被多个伸缩组使用。默认最多可以创建100个伸缩配置。

        :param CreateScalingConfigRequest request
        :return: CreateScalingConfigResponse
        """

        all_params = ['bodyparam']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/autoscaling-api/v1/{project_id}/scaling_configuration',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateScalingConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_scaling_group(self, request):
        """创建弹性伸缩组

        伸缩组是具有相同应用场景的实例的集合，是启停伸缩策略和进行伸缩活动的基本单位。伸缩组内定义了最大实例数、期望实例数、最小实例数、虚拟私有云、子网、负载均衡等信息。默认最多可以创建10个伸缩组。如果伸缩组配置了负载均衡，在添加或移除实例时，会自动为实例绑定或解绑负载均衡监听器。如果伸缩组使用负载均衡健康检查方式，伸缩组中的实例需要启用负载均衡器的监听端口才能通过健康检查。端口启用可在安全组中进行配置，可参考添加安全组规则进行操作。

        :param CreateScalingGroupRequest request
        :return: CreateScalingGroupResponse
        """
        return self.create_scaling_group_with_http_info(request)

    def create_scaling_group_with_http_info(self, request):
        """创建弹性伸缩组

        伸缩组是具有相同应用场景的实例的集合，是启停伸缩策略和进行伸缩活动的基本单位。伸缩组内定义了最大实例数、期望实例数、最小实例数、虚拟私有云、子网、负载均衡等信息。默认最多可以创建10个伸缩组。如果伸缩组配置了负载均衡，在添加或移除实例时，会自动为实例绑定或解绑负载均衡监听器。如果伸缩组使用负载均衡健康检查方式，伸缩组中的实例需要启用负载均衡器的监听端口才能通过健康检查。端口启用可在安全组中进行配置，可参考添加安全组规则进行操作。

        :param CreateScalingGroupRequest request
        :return: CreateScalingGroupResponse
        """

        all_params = ['bodyparam']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/autoscaling-api/v1/{project_id}/scaling_group',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateScalingGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_scaling_notification(self, request):
        """配置伸缩组通知

        给弹性伸缩组配置通知功能。每调用一次该接口，伸缩组即配置一个通知主题及其通知场景，每个伸缩组最多可以增加5个主题。通知主题由用户事先在SMN创建并进行订阅，当通知主题对应的通知场景出现时，伸缩组会向用户的订阅终端发送通知。

        :param CreateScalingNotificationRequest request
        :return: CreateScalingNotificationResponse
        """
        return self.create_scaling_notification_with_http_info(request)

    def create_scaling_notification_with_http_info(self, request):
        """配置伸缩组通知

        给弹性伸缩组配置通知功能。每调用一次该接口，伸缩组即配置一个通知主题及其通知场景，每个伸缩组最多可以增加5个主题。通知主题由用户事先在SMN创建并进行订阅，当通知主题对应的通知场景出现时，伸缩组会向用户的订阅终端发送通知。

        :param CreateScalingNotificationRequest request
        :return: CreateScalingNotificationResponse
        """

        all_params = ['scaling_group_id', 'bodyparam']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/autoscaling-api/v1/{project_id}/scaling_notification/{scaling_group_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateScalingNotificationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_scaling_policy(self, request):
        """创建弹性伸缩策略

        创建弹性伸缩策略。伸缩策略定义了伸缩组内实例的扩张和收缩操作。如果执行伸缩策略造成伸缩组期望实例数与伸缩组内实例数不符，弹性伸缩会自动调整实例资源，以匹配期望实例数。当前伸缩策略支持告警触发策略，周期触发策略，定时触发策略。在策略执行具体动作中，可设置实例变化的个数，或根据当前实例的百分比数进行伸缩。

        :param CreateScalingPolicyRequest request
        :return: CreateScalingPolicyResponse
        """
        return self.create_scaling_policy_with_http_info(request)

    def create_scaling_policy_with_http_info(self, request):
        """创建弹性伸缩策略

        创建弹性伸缩策略。伸缩策略定义了伸缩组内实例的扩张和收缩操作。如果执行伸缩策略造成伸缩组期望实例数与伸缩组内实例数不符，弹性伸缩会自动调整实例资源，以匹配期望实例数。当前伸缩策略支持告警触发策略，周期触发策略，定时触发策略。在策略执行具体动作中，可设置实例变化的个数，或根据当前实例的百分比数进行伸缩。

        :param CreateScalingPolicyRequest request
        :return: CreateScalingPolicyResponse
        """

        all_params = ['bodyparam']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/autoscaling-api/v1/{project_id}/scaling_policy',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateScalingPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_scaling_tags(self, request):
        """创建标签

        创建或删除指定资源的标签。每个伸缩组最多添加10个标签。

        :param CreateScalingTagsRequest request
        :return: CreateScalingTagsResponse
        """
        return self.create_scaling_tags_with_http_info(request)

    def create_scaling_tags_with_http_info(self, request):
        """创建标签

        创建或删除指定资源的标签。每个伸缩组最多添加10个标签。

        :param CreateScalingTagsRequest request
        :return: CreateScalingTagsResponse
        """

        all_params = ['resource_type', 'resource_id', 'bodyparam']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/autoscaling-api/v1/{project_id}/{resource_type}/{resource_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateScalingTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_lifecycle_hook(self, request):
        """删除生命周期挂钩

        删除一个指定生命周期挂钩。伸缩组进行伸缩活动时，不允许删除该伸缩组内的生命周期挂钩。

        :param DeleteLifecycleHookRequest request
        :return: DeleteLifecycleHookResponse
        """
        return self.delete_lifecycle_hook_with_http_info(request)

    def delete_lifecycle_hook_with_http_info(self, request):
        """删除生命周期挂钩

        删除一个指定生命周期挂钩。伸缩组进行伸缩活动时，不允许删除该伸缩组内的生命周期挂钩。

        :param DeleteLifecycleHookRequest request
        :return: DeleteLifecycleHookResponse
        """

        all_params = ['scaling_group_id', 'lifecycle_hook_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']
        if 'lifecycle_hook_name' in local_var_params:
            path_params['lifecycle_hook_name'] = local_var_params['lifecycle_hook_name']

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
            resource_path='/autoscaling-api/v1/{project_id}/scaling_lifecycle_hook/{scaling_group_id}/{lifecycle_hook_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteLifecycleHookResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_scaling_config(self, request):
        """删除弹性伸缩配置

        删除一个指定弹性伸缩配置。

        :param DeleteScalingConfigRequest request
        :return: DeleteScalingConfigResponse
        """
        return self.delete_scaling_config_with_http_info(request)

    def delete_scaling_config_with_http_info(self, request):
        """删除弹性伸缩配置

        删除一个指定弹性伸缩配置。

        :param DeleteScalingConfigRequest request
        :return: DeleteScalingConfigResponse
        """

        all_params = ['scaling_configuration_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'scaling_configuration_id' in local_var_params:
            path_params['scaling_configuration_id'] = local_var_params['scaling_configuration_id']

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
            resource_path='/autoscaling-api/v1/{project_id}/scaling_configuration/{scaling_configuration_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteScalingConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_scaling_group(self, request):
        """删除弹性伸缩组

        删除一个指定弹性伸缩组。force_delete属性表示如果伸缩组存在ECS实例或正在进行伸缩活动，是否强制删除伸缩组并移出和释放ECS实例。默认值为no，表示不强制删除伸缩组。如果force_delete的值为no，必须满足以下两个条件，才能删除伸缩组：条件一：伸缩组没有正在进行的伸缩活动。条件二：伸缩组当前的ECS实例数量（current_instance_number）为0。如果force_delete的值为yes，伸缩组会被置于DELETING状态，拒绝接收新的伸缩活动请求，然后等待已有的伸缩活动完成，最后将伸缩组内所有ECS实例移出伸缩组（用户手动添加的ECS实例会被移出伸缩组，弹性伸缩自动创建的ECS实例会被自动删除）并删除伸缩组。

        :param DeleteScalingGroupRequest request
        :return: DeleteScalingGroupResponse
        """
        return self.delete_scaling_group_with_http_info(request)

    def delete_scaling_group_with_http_info(self, request):
        """删除弹性伸缩组

        删除一个指定弹性伸缩组。force_delete属性表示如果伸缩组存在ECS实例或正在进行伸缩活动，是否强制删除伸缩组并移出和释放ECS实例。默认值为no，表示不强制删除伸缩组。如果force_delete的值为no，必须满足以下两个条件，才能删除伸缩组：条件一：伸缩组没有正在进行的伸缩活动。条件二：伸缩组当前的ECS实例数量（current_instance_number）为0。如果force_delete的值为yes，伸缩组会被置于DELETING状态，拒绝接收新的伸缩活动请求，然后等待已有的伸缩活动完成，最后将伸缩组内所有ECS实例移出伸缩组（用户手动添加的ECS实例会被移出伸缩组，弹性伸缩自动创建的ECS实例会被自动删除）并删除伸缩组。

        :param DeleteScalingGroupRequest request
        :return: DeleteScalingGroupResponse
        """

        all_params = ['scaling_group_id', 'force_delete']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

        query_params = []
        if 'force_delete' in local_var_params:
            query_params.append(('force_delete', local_var_params['force_delete']))

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
            resource_path='/autoscaling-api/v1/{project_id}/scaling_group/{scaling_group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteScalingGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_scaling_instance(self, request):
        """移出弹性伸缩组实例

        从弹性伸缩组中移出一个指定实例。实例处于INSERVICE且移出后实例数不能小于伸缩组的最小实例数时才可以移出。当伸缩组没有伸缩活动时，才能移出实例。

        :param DeleteScalingInstanceRequest request
        :return: DeleteScalingInstanceResponse
        """
        return self.delete_scaling_instance_with_http_info(request)

    def delete_scaling_instance_with_http_info(self, request):
        """移出弹性伸缩组实例

        从弹性伸缩组中移出一个指定实例。实例处于INSERVICE且移出后实例数不能小于伸缩组的最小实例数时才可以移出。当伸缩组没有伸缩活动时，才能移出实例。

        :param DeleteScalingInstanceRequest request
        :return: DeleteScalingInstanceResponse
        """

        all_params = ['instance_id', 'instance_delete']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'instance_delete' in local_var_params:
            query_params.append(('instance_delete', local_var_params['instance_delete']))

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
            resource_path='/autoscaling-api/v1/{project_id}/scaling_group_instance/{instance_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteScalingInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_scaling_notification(self, request):
        """删除伸缩组通知

        删除指定的弹性伸缩组中指定的通知。

        :param DeleteScalingNotificationRequest request
        :return: DeleteScalingNotificationResponse
        """
        return self.delete_scaling_notification_with_http_info(request)

    def delete_scaling_notification_with_http_info(self, request):
        """删除伸缩组通知

        删除指定的弹性伸缩组中指定的通知。

        :param DeleteScalingNotificationRequest request
        :return: DeleteScalingNotificationResponse
        """

        all_params = ['scaling_group_id', 'topic_urn']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']
        if 'topic_urn' in local_var_params:
            path_params['topic_urn'] = local_var_params['topic_urn']

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
            resource_path='/autoscaling-api/v1/{project_id}/scaling_notification/{scaling_group_id}/{topic_urn}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteScalingNotificationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_scaling_policy(self, request):
        """删除弹性伸缩策略

        删除一个指定弹性伸缩策略。

        :param DeleteScalingPolicyRequest request
        :return: DeleteScalingPolicyResponse
        """
        return self.delete_scaling_policy_with_http_info(request)

    def delete_scaling_policy_with_http_info(self, request):
        """删除弹性伸缩策略

        删除一个指定弹性伸缩策略。

        :param DeleteScalingPolicyRequest request
        :return: DeleteScalingPolicyResponse
        """

        all_params = ['scaling_policy_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'scaling_policy_id' in local_var_params:
            path_params['scaling_policy_id'] = local_var_params['scaling_policy_id']

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
            resource_path='/autoscaling-api/v1/{project_id}/scaling_policy/{scaling_policy_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteScalingPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_scaling_tags(self, request):
        """删除标签

        创建或删除指定资源的标签。每个伸缩组最多添加10个标签。

        :param DeleteScalingTagsRequest request
        :return: DeleteScalingTagsResponse
        """
        return self.delete_scaling_tags_with_http_info(request)

    def delete_scaling_tags_with_http_info(self, request):
        """删除标签

        创建或删除指定资源的标签。每个伸缩组最多添加10个标签。

        :param DeleteScalingTagsRequest request
        :return: DeleteScalingTagsResponse
        """

        all_params = ['resource_type', 'resource_id', 'bodyparam']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/autoscaling-api/v1/{project_id}/{resource_type}/{resource_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteScalingTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def enable_or_disable_scaling_group(self, request):
        """启用或停止弹性伸缩组

        启用或停止一个指定弹性伸缩组。已停用状态的伸缩组，不会自动触发任何伸缩活动。当伸缩组正在进行伸缩活动，即使停用，正在进行的伸缩活动也不会立即停止。

        :param EnableOrDisableScalingGroupRequest request
        :return: EnableOrDisableScalingGroupResponse
        """
        return self.enable_or_disable_scaling_group_with_http_info(request)

    def enable_or_disable_scaling_group_with_http_info(self, request):
        """启用或停止弹性伸缩组

        启用或停止一个指定弹性伸缩组。已停用状态的伸缩组，不会自动触发任何伸缩活动。当伸缩组正在进行伸缩活动，即使停用，正在进行的伸缩活动也不会立即停止。

        :param EnableOrDisableScalingGroupRequest request
        :return: EnableOrDisableScalingGroupResponse
        """

        all_params = ['scaling_group_id', 'body_param']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/autoscaling-api/v1/{project_id}/scaling_group/{scaling_group_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='EnableOrDisableScalingGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def execute_scaling_policy(self, request):
        """执行或启用或停止弹性伸缩策略。

        立即执行或启用或停止一个指定弹性伸缩策略。当伸缩组、伸缩策略状态处于INSERVICE时，伸缩策略才能被正确执行，否则会执行失败。

        :param ExecuteScalingPolicyRequest request
        :return: ExecuteScalingPolicyResponse
        """
        return self.execute_scaling_policy_with_http_info(request)

    def execute_scaling_policy_with_http_info(self, request):
        """执行或启用或停止弹性伸缩策略。

        立即执行或启用或停止一个指定弹性伸缩策略。当伸缩组、伸缩策略状态处于INSERVICE时，伸缩策略才能被正确执行，否则会执行失败。

        :param ExecuteScalingPolicyRequest request
        :return: ExecuteScalingPolicyResponse
        """

        all_params = ['scaling_policy_id', 'bodyparam']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'scaling_policy_id' in local_var_params:
            path_params['scaling_policy_id'] = local_var_params['scaling_policy_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/autoscaling-api/v1/{project_id}/scaling_policy/{scaling_policy_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ExecuteScalingPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_hook_instances(self, request):
        """查询伸缩实例挂起信息

        添加生命周期挂钩后，当伸缩组进行伸缩活动时，实例将被挂钩挂起并置于等待状态，根据输入条件过滤查询弹性伸缩组中伸缩实例的挂起信息。可根据实例ID进行条件过滤查询。若不加过滤条件默认查询指定伸缩组内所有实例挂起信息。

        :param ListHookInstancesRequest request
        :return: ListHookInstancesResponse
        """
        return self.list_hook_instances_with_http_info(request)

    def list_hook_instances_with_http_info(self, request):
        """查询伸缩实例挂起信息

        添加生命周期挂钩后，当伸缩组进行伸缩活动时，实例将被挂钩挂起并置于等待状态，根据输入条件过滤查询弹性伸缩组中伸缩实例的挂起信息。可根据实例ID进行条件过滤查询。若不加过滤条件默认查询指定伸缩组内所有实例挂起信息。

        :param ListHookInstancesRequest request
        :return: ListHookInstancesResponse
        """

        all_params = ['scaling_group_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))

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
            resource_path='/autoscaling-api/v1/{project_id}/scaling_instance_hook/{scaling_group_id}/list',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListHookInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_life_cycle_hooks(self, request):
        """查询生命周期挂钩列表

        根据伸缩组ID查询生命周期挂钩列表。

        :param ListLifeCycleHooksRequest request
        :return: ListLifeCycleHooksResponse
        """
        return self.list_life_cycle_hooks_with_http_info(request)

    def list_life_cycle_hooks_with_http_info(self, request):
        """查询生命周期挂钩列表

        根据伸缩组ID查询生命周期挂钩列表。

        :param ListLifeCycleHooksRequest request
        :return: ListLifeCycleHooksResponse
        """

        all_params = ['scaling_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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
            resource_path='/autoscaling-api/v1/{project_id}/scaling_lifecycle_hook/{scaling_group_id}/list',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListLifeCycleHooksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_resource_instances(self, request):
        """查询资源实例

        根据项目ID查询指定资源类型的资源实例。资源、资源tag默认按照创建时间倒序。

        :param ListResourceInstancesRequest request
        :return: ListResourceInstancesResponse
        """
        return self.list_resource_instances_with_http_info(request)

    def list_resource_instances_with_http_info(self, request):
        """查询资源实例

        根据项目ID查询指定资源类型的资源实例。资源、资源tag默认按照创建时间倒序。

        :param ListResourceInstancesRequest request
        :return: ListResourceInstancesResponse
        """

        all_params = ['resource_type', 'bodyparam']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/autoscaling-api/v1/{project_id}/{resource_type}/resource_instances/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListResourceInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_scaling_activity_logs(self, request):
        """查询伸缩活动日志

        根据输入条件过滤查询伸缩活动日志。查询结果分页显示。可根据起始时间，截止时间，起始行号，记录数进行条件过滤查询。若不加过滤条件默认查询最多20条伸缩活动日志信息。

        :param ListScalingActivityLogsRequest request
        :return: ListScalingActivityLogsResponse
        """
        return self.list_scaling_activity_logs_with_http_info(request)

    def list_scaling_activity_logs_with_http_info(self, request):
        """查询伸缩活动日志

        根据输入条件过滤查询伸缩活动日志。查询结果分页显示。可根据起始时间，截止时间，起始行号，记录数进行条件过滤查询。若不加过滤条件默认查询最多20条伸缩活动日志信息。

        :param ListScalingActivityLogsRequest request
        :return: ListScalingActivityLogsResponse
        """

        all_params = ['scaling_group_id', 'start_time', 'end_time', 'start_number', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/autoscaling-api/v1/{project_id}/scaling_activity_log/{scaling_group_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListScalingActivityLogsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_scaling_configs(self, request):
        """查询弹性伸缩配置列表

        根据输入条件过滤查询弹性伸缩配置。查询结果分页显示。可以根据伸缩配置名称，镜像ID，起始行号，记录条数进行条件过滤查询。若不加过滤条件默认最多查询租户下20条伸缩配置信息。

        :param ListScalingConfigsRequest request
        :return: ListScalingConfigsResponse
        """
        return self.list_scaling_configs_with_http_info(request)

    def list_scaling_configs_with_http_info(self, request):
        """查询弹性伸缩配置列表

        根据输入条件过滤查询弹性伸缩配置。查询结果分页显示。可以根据伸缩配置名称，镜像ID，起始行号，记录条数进行条件过滤查询。若不加过滤条件默认最多查询租户下20条伸缩配置信息。

        :param ListScalingConfigsRequest request
        :return: ListScalingConfigsResponse
        """

        all_params = ['scaling_configuration_name', 'image_id', 'start_number', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/autoscaling-api/v1/{project_id}/scaling_configuration',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListScalingConfigsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_scaling_groups(self, request):
        """查询弹性伸缩组列表

        根据输入条件过滤查询弹性伸缩组列表。查询结果分页显示。可根据伸缩组名称，伸缩配置ID，伸缩组状态，企业项目ID，起始行号，记录条数进行条件过滤查询。若不加过滤条件默认最多查询租户下20条伸缩组信息。

        :param ListScalingGroupsRequest request
        :return: ListScalingGroupsResponse
        """
        return self.list_scaling_groups_with_http_info(request)

    def list_scaling_groups_with_http_info(self, request):
        """查询弹性伸缩组列表

        根据输入条件过滤查询弹性伸缩组列表。查询结果分页显示。可根据伸缩组名称，伸缩配置ID，伸缩组状态，企业项目ID，起始行号，记录条数进行条件过滤查询。若不加过滤条件默认最多查询租户下20条伸缩组信息。

        :param ListScalingGroupsRequest request
        :return: ListScalingGroupsResponse
        """

        all_params = ['scaling_group_name', 'scaling_configuration_id', 'scaling_group_status', 'start_number', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/autoscaling-api/v1/{project_id}/scaling_group',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListScalingGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_scaling_instances(self, request):
        """查询弹性伸缩组中的实例列表

        根据输入条件过滤查询弹性伸缩组中实例信息。查询结果分页显示。可根据实例在伸缩组中的生命周期状态，实例健康状态，实例保护状态，起始行号，记录条数进行条件过滤查询。若不加过滤条件默认查询组内最多20条实例信息

        :param ListScalingInstancesRequest request
        :return: ListScalingInstancesResponse
        """
        return self.list_scaling_instances_with_http_info(request)

    def list_scaling_instances_with_http_info(self, request):
        """查询弹性伸缩组中的实例列表

        根据输入条件过滤查询弹性伸缩组中实例信息。查询结果分页显示。可根据实例在伸缩组中的生命周期状态，实例健康状态，实例保护状态，起始行号，记录条数进行条件过滤查询。若不加过滤条件默认查询组内最多20条实例信息

        :param ListScalingInstancesRequest request
        :return: ListScalingInstancesResponse
        """

        all_params = ['scaling_group_id', 'life_cycle_state', 'health_status', 'protect_from_scaling_down', 'start_number', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/autoscaling-api/v1/{project_id}/scaling_group_instance/{scaling_group_id}/list',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListScalingInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_scaling_notifications(self, request):
        """查询伸缩组通知列表

        根据伸缩组ID查询指定弹性伸缩组的通知列表。

        :param ListScalingNotificationsRequest request
        :return: ListScalingNotificationsResponse
        """
        return self.list_scaling_notifications_with_http_info(request)

    def list_scaling_notifications_with_http_info(self, request):
        """查询伸缩组通知列表

        根据伸缩组ID查询指定弹性伸缩组的通知列表。

        :param ListScalingNotificationsRequest request
        :return: ListScalingNotificationsResponse
        """

        all_params = ['scaling_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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
            resource_path='/autoscaling-api/v1/{project_id}/scaling_notification/{scaling_group_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListScalingNotificationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_scaling_policies(self, request):
        """查询弹性伸缩策略列表

        根据输入条件过滤查询弹性伸缩策略。查询结果分页显示。可根据伸缩策略名称，策略类型，伸缩策略ID，起始行号，记录数进行条件过滤查询。若不加过滤条件默认查询租户下指定伸缩组内最多20条伸缩策略信息。

        :param ListScalingPoliciesRequest request
        :return: ListScalingPoliciesResponse
        """
        return self.list_scaling_policies_with_http_info(request)

    def list_scaling_policies_with_http_info(self, request):
        """查询弹性伸缩策略列表

        根据输入条件过滤查询弹性伸缩策略。查询结果分页显示。可根据伸缩策略名称，策略类型，伸缩策略ID，起始行号，记录数进行条件过滤查询。若不加过滤条件默认查询租户下指定伸缩组内最多20条伸缩策略信息。

        :param ListScalingPoliciesRequest request
        :return: ListScalingPoliciesResponse
        """

        all_params = ['scaling_group_id', 'scaling_policy_name', 'scaling_policy_type', 'scaling_policy_id', 'start_number', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/autoscaling-api/v1/{project_id}/scaling_policy/{scaling_group_id}/list',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListScalingPoliciesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_scaling_policy_execute_logs(self, request):
        """查询策略执行日志

        根据输入条件过滤查询策略执行的历史记录。查询结果分页显示。可根据日志ID，伸缩资源类型，伸缩资源ID，策略执行类型，查询额起始，查询截止时间，查询起始行号，查询记录数进行条件过滤查询。若不加过滤条件默认查询最多20条策略执行日志信息。

        :param ListScalingPolicyExecuteLogsRequest request
        :return: ListScalingPolicyExecuteLogsResponse
        """
        return self.list_scaling_policy_execute_logs_with_http_info(request)

    def list_scaling_policy_execute_logs_with_http_info(self, request):
        """查询策略执行日志

        根据输入条件过滤查询策略执行的历史记录。查询结果分页显示。可根据日志ID，伸缩资源类型，伸缩资源ID，策略执行类型，查询额起始，查询截止时间，查询起始行号，查询记录数进行条件过滤查询。若不加过滤条件默认查询最多20条策略执行日志信息。

        :param ListScalingPolicyExecuteLogsRequest request
        :return: ListScalingPolicyExecuteLogsResponse
        """

        all_params = ['scaling_policy_id', 'log_id', 'scaling_resource_type', 'scaling_resource_id', 'execute_type', 'start_time', 'end_time', 'start_number', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/autoscaling-api/v1/{project_id}/scaling_policy_execute_log/{scaling_policy_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListScalingPolicyExecuteLogsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_scaling_tag_infos_by_resource_id(self, request):
        """查询资源标签

        根据项目ID和资源ID查询指定资源类型的资源标签列表。

        :param ListScalingTagInfosByResourceIdRequest request
        :return: ListScalingTagInfosByResourceIdResponse
        """
        return self.list_scaling_tag_infos_by_resource_id_with_http_info(request)

    def list_scaling_tag_infos_by_resource_id_with_http_info(self, request):
        """查询资源标签

        根据项目ID和资源ID查询指定资源类型的资源标签列表。

        :param ListScalingTagInfosByResourceIdRequest request
        :return: ListScalingTagInfosByResourceIdResponse
        """

        all_params = ['resource_type', 'resource_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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
            resource_path='/autoscaling-api/v1/{project_id}/{resource_type}/{resource_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListScalingTagInfosByResourceIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_scaling_tag_infos_by_tenant_id(self, request):
        """查询标签

        根据项目ID查询指定资源类型的标签列表。

        :param ListScalingTagInfosByTenantIdRequest request
        :return: ListScalingTagInfosByTenantIdResponse
        """
        return self.list_scaling_tag_infos_by_tenant_id_with_http_info(request)

    def list_scaling_tag_infos_by_tenant_id_with_http_info(self, request):
        """查询标签

        根据项目ID查询指定资源类型的标签列表。

        :param ListScalingTagInfosByTenantIdRequest request
        :return: ListScalingTagInfosByTenantIdResponse
        """

        all_params = ['resource_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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
            resource_path='/autoscaling-api/v1/{project_id}/{resource_type}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListScalingTagInfosByTenantIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_life_cycle_hook(self, request):
        """查询生命周期挂钩详情

        根据伸缩组ID及生命周期挂钩名称查询指定的生命周期挂钩详情。

        :param ShowLifeCycleHookRequest request
        :return: ShowLifeCycleHookResponse
        """
        return self.show_life_cycle_hook_with_http_info(request)

    def show_life_cycle_hook_with_http_info(self, request):
        """查询生命周期挂钩详情

        根据伸缩组ID及生命周期挂钩名称查询指定的生命周期挂钩详情。

        :param ShowLifeCycleHookRequest request
        :return: ShowLifeCycleHookResponse
        """

        all_params = ['scaling_group_id', 'lifecycle_hook_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']
        if 'lifecycle_hook_name' in local_var_params:
            path_params['lifecycle_hook_name'] = local_var_params['lifecycle_hook_name']

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
            resource_path='/autoscaling-api/v1/{project_id}/scaling_lifecycle_hook/{scaling_group_id}/{lifecycle_hook_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowLifeCycleHookResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_policy_and_instance_quota(self, request):
        """查询弹性伸缩策略和伸缩实例配额

        根据伸缩组ID查询指定弹性伸缩组下的伸缩策略和伸缩实例的配额总数及已使用配额数。

        :param ShowPolicyAndInstanceQuotaRequest request
        :return: ShowPolicyAndInstanceQuotaResponse
        """
        return self.show_policy_and_instance_quota_with_http_info(request)

    def show_policy_and_instance_quota_with_http_info(self, request):
        """查询弹性伸缩策略和伸缩实例配额

        根据伸缩组ID查询指定弹性伸缩组下的伸缩策略和伸缩实例的配额总数及已使用配额数。

        :param ShowPolicyAndInstanceQuotaRequest request
        :return: ShowPolicyAndInstanceQuotaResponse
        """

        all_params = ['scaling_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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
            resource_path='/autoscaling-api/v1/{project_id}/quotas/{scaling_group_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPolicyAndInstanceQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_resource_quota(self, request):
        """查询配额

        查询指定租户下的弹性伸缩组、伸缩配置、伸缩带宽策略、伸缩策略和伸缩实例的配额总数及已使用配额数。

        :param ShowResourceQuotaRequest request
        :return: ShowResourceQuotaResponse
        """
        return self.show_resource_quota_with_http_info(request)

    def show_resource_quota_with_http_info(self, request):
        """查询配额

        查询指定租户下的弹性伸缩组、伸缩配置、伸缩带宽策略、伸缩策略和伸缩实例的配额总数及已使用配额数。

        :param ShowResourceQuotaRequest request
        :return: ShowResourceQuotaResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

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
            resource_path='/autoscaling-api/v1/{project_id}/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowResourceQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_scaling_config(self, request):
        """查询弹性伸缩配置详情

        根据伸缩配置ID查询一个弹性伸缩配置的详细信息。

        :param ShowScalingConfigRequest request
        :return: ShowScalingConfigResponse
        """
        return self.show_scaling_config_with_http_info(request)

    def show_scaling_config_with_http_info(self, request):
        """查询弹性伸缩配置详情

        根据伸缩配置ID查询一个弹性伸缩配置的详细信息。

        :param ShowScalingConfigRequest request
        :return: ShowScalingConfigResponse
        """

        all_params = ['scaling_configuration_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'scaling_configuration_id' in local_var_params:
            path_params['scaling_configuration_id'] = local_var_params['scaling_configuration_id']

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
            resource_path='/autoscaling-api/v1/{project_id}/scaling_configuration/{scaling_configuration_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowScalingConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_scaling_group(self, request):
        """查询弹性伸缩组详情

        查询一个指定弹性伸缩组详情。

        :param ShowScalingGroupRequest request
        :return: ShowScalingGroupResponse
        """
        return self.show_scaling_group_with_http_info(request)

    def show_scaling_group_with_http_info(self, request):
        """查询弹性伸缩组详情

        查询一个指定弹性伸缩组详情。

        :param ShowScalingGroupRequest request
        :return: ShowScalingGroupResponse
        """

        all_params = ['scaling_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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
            resource_path='/autoscaling-api/v1/{project_id}/scaling_group/{scaling_group_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowScalingGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_scaling_policy(self, request):
        """查询弹性伸缩策略详情

        查询指定弹性伸缩策略信息。

        :param ShowScalingPolicyRequest request
        :return: ShowScalingPolicyResponse
        """
        return self.show_scaling_policy_with_http_info(request)

    def show_scaling_policy_with_http_info(self, request):
        """查询弹性伸缩策略详情

        查询指定弹性伸缩策略信息。

        :param ShowScalingPolicyRequest request
        :return: ShowScalingPolicyResponse
        """

        all_params = ['scaling_policy_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'scaling_policy_id' in local_var_params:
            path_params['scaling_policy_id'] = local_var_params['scaling_policy_id']

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
            resource_path='/autoscaling-api/v1/{project_id}/scaling_policy/{scaling_policy_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowScalingPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_life_cycle_hook(self, request):
        """修改生命周期挂钩

        修改一个指定生命周期挂钩中的信息。

        :param UpdateLifeCycleHookRequest request
        :return: UpdateLifeCycleHookResponse
        """
        return self.update_life_cycle_hook_with_http_info(request)

    def update_life_cycle_hook_with_http_info(self, request):
        """修改生命周期挂钩

        修改一个指定生命周期挂钩中的信息。

        :param UpdateLifeCycleHookRequest request
        :return: UpdateLifeCycleHookResponse
        """

        all_params = ['scaling_group_id', 'lifecycle_hook_name', 'bodyparam']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']
        if 'lifecycle_hook_name' in local_var_params:
            path_params['lifecycle_hook_name'] = local_var_params['lifecycle_hook_name']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/autoscaling-api/v1/{project_id}/scaling_lifecycle_hook/{scaling_group_id}/{lifecycle_hook_name}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateLifeCycleHookResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_scaling_group(self, request):
        """修改弹性伸缩组

        修改一个指定弹性伸缩组中的信息。更换伸缩组的伸缩配置，伸缩组中已经存在的使用之前伸缩配置创建的云服务器云主机不受影响。伸缩组为没有正在进行的伸缩活动时，可以修改伸缩组的子网、可用区和负载均衡配置。当伸缩组的期望实例数改变时，会触发伸缩活动加入或移出实例。期望实例数必须大于或等于最小实例数，必须小于或等于最大实例数。

        :param UpdateScalingGroupRequest request
        :return: UpdateScalingGroupResponse
        """
        return self.update_scaling_group_with_http_info(request)

    def update_scaling_group_with_http_info(self, request):
        """修改弹性伸缩组

        修改一个指定弹性伸缩组中的信息。更换伸缩组的伸缩配置，伸缩组中已经存在的使用之前伸缩配置创建的云服务器云主机不受影响。伸缩组为没有正在进行的伸缩活动时，可以修改伸缩组的子网、可用区和负载均衡配置。当伸缩组的期望实例数改变时，会触发伸缩活动加入或移出实例。期望实例数必须大于或等于最小实例数，必须小于或等于最大实例数。

        :param UpdateScalingGroupRequest request
        :return: UpdateScalingGroupResponse
        """

        all_params = ['scaling_group_id', 'bodyparam']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/autoscaling-api/v1/{project_id}/scaling_group/{scaling_group_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateScalingGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_scaling_group_instance(self, request):
        """批量操作实例

        批量移出伸缩组中的实例或批量添加伸缩组外的实例。批量对伸缩组中的实例设置或取消其实例保护属性。批量将伸缩组中的实例转入或移出备用状态。

        :param UpdateScalingGroupInstanceRequest request
        :return: UpdateScalingGroupInstanceResponse
        """
        return self.update_scaling_group_instance_with_http_info(request)

    def update_scaling_group_instance_with_http_info(self, request):
        """批量操作实例

        批量移出伸缩组中的实例或批量添加伸缩组外的实例。批量对伸缩组中的实例设置或取消其实例保护属性。批量将伸缩组中的实例转入或移出备用状态。

        :param UpdateScalingGroupInstanceRequest request
        :return: UpdateScalingGroupInstanceResponse
        """

        all_params = ['scaling_group_id', 'bodyparam']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'scaling_group_id' in local_var_params:
            path_params['scaling_group_id'] = local_var_params['scaling_group_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/autoscaling-api/v1/{project_id}/scaling_group_instance/{scaling_group_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateScalingGroupInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_scaling_policy(self, request):
        """修改弹性伸缩策略

        修改指定弹性伸缩策略。

        :param UpdateScalingPolicyRequest request
        :return: UpdateScalingPolicyResponse
        """
        return self.update_scaling_policy_with_http_info(request)

    def update_scaling_policy_with_http_info(self, request):
        """修改弹性伸缩策略

        修改指定弹性伸缩策略。

        :param UpdateScalingPolicyRequest request
        :return: UpdateScalingPolicyResponse
        """

        all_params = ['scaling_policy_id', 'bodyparam']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'scaling_policy_id' in local_var_params:
            path_params['scaling_policy_id'] = local_var_params['scaling_policy_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/autoscaling-api/v1/{project_id}/scaling_policy/{scaling_policy_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateScalingPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
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
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type)
