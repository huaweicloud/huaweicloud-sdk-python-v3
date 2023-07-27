# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class HssClient(Client):
    def __init__(self):
        super(HssClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkhss.v5.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "HssClient":
            raise TypeError("client type error, support client type is HssClient")

        return ClientBuilder(clazz)

    def add_hosts_group(self, request):
        """创建服务器组

        创建服务器组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddHostsGroup
        :type request: :class:`huaweicloudsdkhss.v5.AddHostsGroupRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.AddHostsGroupResponse`
        """
        return self._add_hosts_group_with_http_info(request)

    def _add_hosts_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/host-management/groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddHostsGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_policy_group(self, request):
        """部署策略

        部署策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociatePolicyGroup
        :type request: :class:`huaweicloudsdkhss.v5.AssociatePolicyGroupRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.AssociatePolicyGroupResponse`
        """
        return self._associate_policy_group_with_http_info(request)

    def _associate_policy_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/policy/deploy',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociatePolicyGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_create_tags(self, request):
        """批量创建标签

        批量创建标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateTags
        :type request: :class:`huaweicloudsdkhss.v5.BatchCreateTagsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.BatchCreateTagsResponse`
        """
        return self._batch_create_tags_with_http_info(request)

    def _batch_create_tags_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/{resource_type}/{resource_id}/tags/create',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreateTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_event(self, request):
        """处理告警事件

        处理告警事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeEvent
        :type request: :class:`huaweicloudsdkhss.v5.ChangeEventRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ChangeEventResponse`
        """
        return self._change_event_with_http_info(request)

    def _change_event_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'container_name' in local_var_params:
            query_params.append(('container_name', local_var_params['container_name']))
        if 'container_id' in local_var_params:
            query_params.append(('container_id', local_var_params['container_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/event/operate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeEventResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_hosts_group(self, request):
        """编辑服务器组

        编辑服务器组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeHostsGroup
        :type request: :class:`huaweicloudsdkhss.v5.ChangeHostsGroupRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ChangeHostsGroupResponse`
        """
        return self._change_hosts_group_with_http_info(request)

    def _change_hosts_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/host-management/groups',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeHostsGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_vul_status(self, request):
        """修改漏洞的状态

        修改漏洞的状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeVulStatus
        :type request: :class:`huaweicloudsdkhss.v5.ChangeVulStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ChangeVulStatusResponse`
        """
        return self._change_vul_status_with_http_info(request)

    def _change_vul_status_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/vulnerability/status',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeVulStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_hosts_group(self, request):
        """删除服务器组

        删除服务器组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteHostsGroup
        :type request: :class:`huaweicloudsdkhss.v5.DeleteHostsGroupRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.DeleteHostsGroupResponse`
        """
        return self._delete_hosts_group_with_http_info(request)

    def _delete_hosts_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/host-management/groups',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteHostsGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_resource_instance_tag(self, request):
        """删除资源标签

        删除单个资源下的标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteResourceInstanceTag
        :type request: :class:`huaweicloudsdkhss.v5.DeleteResourceInstanceTagRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.DeleteResourceInstanceTagResponse`
        """
        return self._delete_resource_instance_tag_with_http_info(request)

    def _delete_resource_instance_tag_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/{resource_type}/{resource_id}/tags/{key}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteResourceInstanceTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_alarm_white_list(self, request):
        """查询告警白名单列表

        查询告警白名单列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarmWhiteList
        :type request: :class:`huaweicloudsdkhss.v5.ListAlarmWhiteListRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAlarmWhiteListResponse`
        """
        return self._list_alarm_white_list_with_http_info(request)

    def _list_alarm_white_list_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'hash' in local_var_params:
            query_params.append(('hash', local_var_params['hash']))
        if 'event_type' in local_var_params:
            query_params.append(('event_type', local_var_params['event_type']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/event/white-list/alarm',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAlarmWhiteListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_app_change_histories(self, request):
        """获取软件信息的历史变动记录

        获取软件信息的历史变动记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAppChangeHistories
        :type request: :class:`huaweicloudsdkhss.v5.ListAppChangeHistoriesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAppChangeHistoriesResponse`
        """
        return self._list_app_change_histories_with_http_info(request)

    def _list_app_change_histories_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'variation_type' in local_var_params:
            query_params.append(('variation_type', local_var_params['variation_type']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

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
            resource_path='/v5/{project_id}/asset/app/change-history',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAppChangeHistoriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_app_statistics(self, request):
        """查询软件列表

        查询软件列表，支持通过软件名称查询对应的服务器数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAppStatistics
        :type request: :class:`huaweicloudsdkhss.v5.ListAppStatisticsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAppStatisticsResponse`
        """
        return self._list_app_statistics_with_http_info(request)

    def _list_app_statistics_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v5/{project_id}/asset/app/statistics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAppStatisticsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apps(self, request):
        """查询软件的服务器列表

        查询软件的服务器列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApps
        :type request: :class:`huaweicloudsdkhss.v5.ListAppsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAppsResponse`
        """
        return self._list_apps_with_http_info(request)

    def _list_apps_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))
        if 'install_dir' in local_var_params:
            query_params.append(('install_dir', local_var_params['install_dir']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v5/{project_id}/asset/apps',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAppsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_auto_launch_change_histories(self, request):
        """获取自启动项的历史变动记录

        获取自启动项的历史变动记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAutoLaunchChangeHistories
        :type request: :class:`huaweicloudsdkhss.v5.ListAutoLaunchChangeHistoriesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAutoLaunchChangeHistoriesResponse`
        """
        return self._list_auto_launch_change_histories_with_http_info(request)

    def _list_auto_launch_change_histories_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'auto_launch_name' in local_var_params:
            query_params.append(('auto_launch_name', local_var_params['auto_launch_name']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'variation_type' in local_var_params:
            query_params.append(('variation_type', local_var_params['variation_type']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

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
            resource_path='/v5/{project_id}/asset/auto-launch/change-history',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAutoLaunchChangeHistoriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_auto_launch_statistics(self, request):
        """查询自启动项信息

        查询自启动信息，支持通过传入自启动名称查询启动类型和服务器数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAutoLaunchStatistics
        :type request: :class:`huaweicloudsdkhss.v5.ListAutoLaunchStatisticsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAutoLaunchStatisticsResponse`
        """
        return self._list_auto_launch_statistics_with_http_info(request)

    def _list_auto_launch_statistics_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v5/{project_id}/asset/auto-launch/statistics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAutoLaunchStatisticsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_auto_launchs(self, request):
        """查询自启动项的服务列表

        查询自启动项的服务列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAutoLaunchs
        :type request: :class:`huaweicloudsdkhss.v5.ListAutoLaunchsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListAutoLaunchsResponse`
        """
        return self._list_auto_launchs_with_http_info(request)

    def _list_auto_launchs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v5/{project_id}/asset/auto-launchs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAutoLaunchsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_host_groups(self, request):
        """查询服务器组列表

        查询服务器组列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHostGroups
        :type request: :class:`huaweicloudsdkhss.v5.ListHostGroupsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListHostGroupsResponse`
        """
        return self._list_host_groups_with_http_info(request)

    def _list_host_groups_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/host-management/groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListHostGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_host_protect_history_info(self, request):
        """查询主机静态网页防篡改防护动态

        查询主机静态网页防篡改防护动态：展示服务器名称、服务器ip、防护策略、检测时间、防护文件、事件描述信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHostProtectHistoryInfo
        :type request: :class:`huaweicloudsdkhss.v5.ListHostProtectHistoryInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListHostProtectHistoryInfoResponse`
        """
        return self._list_host_protect_history_info_with_http_info(request)

    def _list_host_protect_history_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/webtamper/static/protect-history',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListHostProtectHistoryInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_host_rasp_protect_history_info(self, request):
        """查询主机动态网页防篡改防护动态

        查询主机动态网页防篡改防护动态：包含告警级别、服务器ip、服务器名称、威胁类型、告警时间、攻击源ip、攻击源url信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHostRaspProtectHistoryInfo
        :type request: :class:`huaweicloudsdkhss.v5.ListHostRaspProtectHistoryInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListHostRaspProtectHistoryInfoResponse`
        """
        return self._list_host_rasp_protect_history_info_with_http_info(request)

    def _list_host_rasp_protect_history_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'alarm_level' in local_var_params:
            query_params.append(('alarm_level', local_var_params['alarm_level']))
        if 'severity' in local_var_params:
            query_params.append(('severity', local_var_params['severity']))
        if 'protect_status' in local_var_params:
            query_params.append(('protect_status', local_var_params['protect_status']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/webtamper/rasp/protect-history',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListHostRaspProtectHistoryInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_host_status(self, request):
        """查询云服务器列表

        查询云服务器列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHostStatus
        :type request: :class:`huaweicloudsdkhss.v5.ListHostStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListHostStatusResponse`
        """
        return self._list_host_status_with_http_info(request)

    def _list_host_status_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))
        if 'agent_status' in local_var_params:
            query_params.append(('agent_status', local_var_params['agent_status']))
        if 'detect_result' in local_var_params:
            query_params.append(('detect_result', local_var_params['detect_result']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'host_status' in local_var_params:
            query_params.append(('host_status', local_var_params['host_status']))
        if 'os_type' in local_var_params:
            query_params.append(('os_type', local_var_params['os_type']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'public_ip' in local_var_params:
            query_params.append(('public_ip', local_var_params['public_ip']))
        if 'ip_addr' in local_var_params:
            query_params.append(('ip_addr', local_var_params['ip_addr']))
        if 'protect_status' in local_var_params:
            query_params.append(('protect_status', local_var_params['protect_status']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))
        if 'policy_group_id' in local_var_params:
            query_params.append(('policy_group_id', local_var_params['policy_group_id']))
        if 'policy_group_name' in local_var_params:
            query_params.append(('policy_group_name', local_var_params['policy_group_name']))
        if 'charging_mode' in local_var_params:
            query_params.append(('charging_mode', local_var_params['charging_mode']))
        if 'refresh' in local_var_params:
            query_params.append(('refresh', local_var_params['refresh']))
        if 'above_version' in local_var_params:
            query_params.append(('above_version', local_var_params['above_version']))
        if 'outside_host' in local_var_params:
            query_params.append(('outside_host', local_var_params['outside_host']))
        if 'asset_value' in local_var_params:
            query_params.append(('asset_value', local_var_params['asset_value']))
        if 'label' in local_var_params:
            query_params.append(('label', local_var_params['label']))
        if 'server_group' in local_var_params:
            query_params.append(('server_group', local_var_params['server_group']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/host-management/hosts',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListHostStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_host_vuls(self, request):
        """查询单台服务器漏洞信息

        查询单台服务器漏洞信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHostVuls
        :type request: :class:`huaweicloudsdkhss.v5.ListHostVulsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListHostVulsResponse`
        """
        return self._list_host_vuls_with_http_info(request)

    def _list_host_vuls_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'host_id' in local_var_params:
            path_params['host_id'] = local_var_params['host_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'vul_name' in local_var_params:
            query_params.append(('vul_name', local_var_params['vul_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'handle_status' in local_var_params:
            query_params.append(('handle_status', local_var_params['handle_status']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

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
            resource_path='/v5/{project_id}/vulnerability/host/{host_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListHostVulsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_jar_package_host_info(self, request):
        """查询指定中间件的服务器列表

        查询指定中间件的服务器列表，通过传入中间件名称参数，返回对应的中间件服务器列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListJarPackageHostInfo
        :type request: :class:`huaweicloudsdkhss.v5.ListJarPackageHostInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListJarPackageHostInfoResponse`
        """
        return self._list_jar_package_host_info_with_http_info(request)

    def _list_jar_package_host_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'file_name' in local_var_params:
            query_params.append(('file_name', local_var_params['file_name']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v5/{project_id}/asset/midwares/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListJarPackageHostInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_jar_package_statistics(self, request):
        """查询中间件列表

        查询中间件列表，支持通过中间件名称查询对应的服务器树
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListJarPackageStatistics
        :type request: :class:`huaweicloudsdkhss.v5.ListJarPackageStatisticsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListJarPackageStatisticsResponse`
        """
        return self._list_jar_package_statistics_with_http_info(request)

    def _list_jar_package_statistics_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'file_name' in local_var_params:
            query_params.append(('file_name', local_var_params['file_name']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v5/{project_id}/asset/midwares',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListJarPackageStatisticsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_password_complexity(self, request):
        """查询口令复杂度策略检测报告

        查询口令复杂度策略检测报告
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPasswordComplexity
        :type request: :class:`huaweicloudsdkhss.v5.ListPasswordComplexityRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListPasswordComplexityResponse`
        """
        return self._list_password_complexity_with_http_info(request)

    def _list_password_complexity_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v5/{project_id}/baseline/password-complexity',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPasswordComplexityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_policy_group(self, request):
        """查询策略组列表

        查询策略组列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPolicyGroup
        :type request: :class:`huaweicloudsdkhss.v5.ListPolicyGroupRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListPolicyGroupResponse`
        """
        return self._list_policy_group_with_http_info(request)

    def _list_policy_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/policy/groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPolicyGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_port_statistics(self, request):
        """查询开放端口列表

        查询开放端口列表，支持通过传入端口或协议类型查询服务器数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPortStatistics
        :type request: :class:`huaweicloudsdkhss.v5.ListPortStatisticsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListPortStatisticsResponse`
        """
        return self._list_port_statistics_with_http_info(request)

    def _list_port_statistics_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'port' in local_var_params:
            query_params.append(('port', local_var_params['port']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v5/{project_id}/asset/port/statistics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPortStatisticsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_ports(self, request):
        """查询单服务器的开放端口列表

        查询单服务器的开放端口列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPorts
        :type request: :class:`huaweicloudsdkhss.v5.ListPortsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListPortsResponse`
        """
        return self._list_ports_with_http_info(request)

    def _list_ports_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'port' in local_var_params:
            query_params.append(('port', local_var_params['port']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v5/{project_id}/asset/ports',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPortsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_process_statistics(self, request):
        """查询进程列表

        查询进程列表，通过传入进程路径参数查询对应的服务器数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProcessStatistics
        :type request: :class:`huaweicloudsdkhss.v5.ListProcessStatisticsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListProcessStatisticsResponse`
        """
        return self._list_process_statistics_with_http_info(request)

    def _list_process_statistics_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v5/{project_id}/asset/process/statistics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProcessStatisticsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_protection_policy(self, request):
        """查询防护策略列表

        查询防护策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProtectionPolicy
        :type request: :class:`huaweicloudsdkhss.v5.ListProtectionPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListProtectionPolicyResponse`
        """
        return self._list_protection_policy_with_http_info(request)

    def _list_protection_policy_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'policy_name' in local_var_params:
            query_params.append(('policy_name', local_var_params['policy_name']))
        if 'protect_policy_id' in local_var_params:
            query_params.append(('protect_policy_id', local_var_params['protect_policy_id']))
        if 'operating_system' in local_var_params:
            query_params.append(('operating_system', local_var_params['operating_system']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/ransomware/protection/policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProtectionPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_protection_server(self, request):
        """查询勒索防护服务器列表

        查询勒索防护服务器列表，与云备份服务配合使用。因此使用勒索相关接口之前确保该局点有云备份服务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProtectionServer
        :type request: :class:`huaweicloudsdkhss.v5.ListProtectionServerRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListProtectionServerResponse`
        """
        return self._list_protection_server_with_http_info(request)

    def _list_protection_server_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'os_type' in local_var_params:
            query_params.append(('os_type', local_var_params['os_type']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'host_status' in local_var_params:
            query_params.append(('host_status', local_var_params['host_status']))
        if 'last_days' in local_var_params:
            query_params.append(('last_days', local_var_params['last_days']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/ransomware/server',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProtectionServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_quotas_detail(self, request):
        """查询配额详情

        查询配额详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQuotasDetail
        :type request: :class:`huaweicloudsdkhss.v5.ListQuotasDetailRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListQuotasDetailResponse`
        """
        return self._list_quotas_detail_with_http_info(request)

    def _list_quotas_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'quota_status' in local_var_params:
            query_params.append(('quota_status', local_var_params['quota_status']))
        if 'used_status' in local_var_params:
            query_params.append(('used_status', local_var_params['used_status']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'charging_mode' in local_var_params:
            query_params.append(('charging_mode', local_var_params['charging_mode']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/billing/quotas-detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListQuotasDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_risk_config_check_rules(self, request):
        """查询指定安全配置项的检查项列表

        查询指定安全配置项的检查项列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRiskConfigCheckRules
        :type request: :class:`huaweicloudsdkhss.v5.ListRiskConfigCheckRulesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListRiskConfigCheckRulesResponse`
        """
        return self._list_risk_config_check_rules_with_http_info(request)

    def _list_risk_config_check_rules_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'check_name' in local_var_params:
            path_params['check_name'] = local_var_params['check_name']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'standard' in local_var_params:
            query_params.append(('standard', local_var_params['standard']))
        if 'result_type' in local_var_params:
            query_params.append(('result_type', local_var_params['result_type']))
        if 'check_rule_name' in local_var_params:
            query_params.append(('check_rule_name', local_var_params['check_rule_name']))
        if 'severity' in local_var_params:
            query_params.append(('severity', local_var_params['severity']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v5/{project_id}/baseline/risk-config/{check_name}/check-rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRiskConfigCheckRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_risk_config_hosts(self, request):
        """查询指定安全配置项的受影响服务器列表

        查询指定安全配置项的受影响服务器列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRiskConfigHosts
        :type request: :class:`huaweicloudsdkhss.v5.ListRiskConfigHostsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListRiskConfigHostsResponse`
        """
        return self._list_risk_config_hosts_with_http_info(request)

    def _list_risk_config_hosts_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'check_name' in local_var_params:
            path_params['check_name'] = local_var_params['check_name']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'standard' in local_var_params:
            query_params.append(('standard', local_var_params['standard']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v5/{project_id}/baseline/risk-config/{check_name}/hosts',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRiskConfigHostsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_risk_configs(self, request):
        """查询租户的服务器安全配置检测结果列表

        查询租户的服务器安全配置检测结果列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRiskConfigs
        :type request: :class:`huaweicloudsdkhss.v5.ListRiskConfigsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListRiskConfigsResponse`
        """
        return self._list_risk_configs_with_http_info(request)

    def _list_risk_configs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'check_name' in local_var_params:
            query_params.append(('check_name', local_var_params['check_name']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'severity' in local_var_params:
            query_params.append(('severity', local_var_params['severity']))
        if 'standard' in local_var_params:
            query_params.append(('standard', local_var_params['standard']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v5/{project_id}/baseline/risk-configs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRiskConfigsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_security_events(self, request):
        """查入侵事件列表

        查入侵事件列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSecurityEvents
        :type request: :class:`huaweicloudsdkhss.v5.ListSecurityEventsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListSecurityEventsResponse`
        """
        return self._list_security_events_with_http_info(request)

    def _list_security_events_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'last_days' in local_var_params:
            query_params.append(('last_days', local_var_params['last_days']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'container_name' in local_var_params:
            query_params.append(('container_name', local_var_params['container_name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'event_types' in local_var_params:
            query_params.append(('event_types', local_var_params['event_types']))
            collection_formats['event_types'] = 'csv'
        if 'handle_status' in local_var_params:
            query_params.append(('handle_status', local_var_params['handle_status']))
        if 'severity' in local_var_params:
            query_params.append(('severity', local_var_params['severity']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'event_class_ids' in local_var_params:
            query_params.append(('event_class_ids', local_var_params['event_class_ids']))
            collection_formats['event_class_ids'] = 'csv'

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/event/events',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSecurityEventsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_user_change_histories(self, request):
        """获取账户变动历史信息

        获取账户变动历史记录信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUserChangeHistories
        :type request: :class:`huaweicloudsdkhss.v5.ListUserChangeHistoriesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListUserChangeHistoriesResponse`
        """
        return self._list_user_change_histories_with_http_info(request)

    def _list_user_change_histories_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'root_permission' in local_var_params:
            query_params.append(('root_permission', local_var_params['root_permission']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'change_type' in local_var_params:
            query_params.append(('change_type', local_var_params['change_type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

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
            resource_path='/v5/{project_id}/asset/user/change-history',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListUserChangeHistoriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_user_statistics(self, request):
        """查询账号信息列表

        查询账号信息列表，支持通过传入账号名称参数查询对应的服务器数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUserStatistics
        :type request: :class:`huaweicloudsdkhss.v5.ListUserStatisticsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListUserStatisticsResponse`
        """
        return self._list_user_statistics_with_http_info(request)

    def _list_user_statistics_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v5/{project_id}/asset/user/statistics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListUserStatisticsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_users(self, request):
        """查询账号的服务器列表

        查询账号的服务器列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUsers
        :type request: :class:`huaweicloudsdkhss.v5.ListUsersRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListUsersResponse`
        """
        return self._list_users_with_http_info(request)

    def _list_users_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'login_permission' in local_var_params:
            query_params.append(('login_permission', local_var_params['login_permission']))
        if 'root_permission' in local_var_params:
            query_params.append(('root_permission', local_var_params['root_permission']))
        if 'user_group' in local_var_params:
            query_params.append(('user_group', local_var_params['user_group']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v5/{project_id}/asset/users',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_vul_hosts(self, request):
        """查询单个漏洞影响的云服务器信息

        查询单个漏洞影响的云服务器信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVulHosts
        :type request: :class:`huaweicloudsdkhss.v5.ListVulHostsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListVulHostsResponse`
        """
        return self._list_vul_hosts_with_http_info(request)

    def _list_vul_hosts_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'vul_id' in local_var_params:
            query_params.append(('vul_id', local_var_params['vul_id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'asset_value' in local_var_params:
            query_params.append(('asset_value', local_var_params['asset_value']))
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))
        if 'handle_status' in local_var_params:
            query_params.append(('handle_status', local_var_params['handle_status']))
        if 'severity_level' in local_var_params:
            query_params.append(('severity_level', local_var_params['severity_level']))
        if 'is_affect_business' in local_var_params:
            query_params.append(('is_affect_business', local_var_params['is_affect_business']))

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
            resource_path='/v5/{project_id}/vulnerability/hosts',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListVulHostsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_vulnerabilities(self, request):
        """查询漏洞列表

        查询漏洞列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVulnerabilities
        :type request: :class:`huaweicloudsdkhss.v5.ListVulnerabilitiesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListVulnerabilitiesResponse`
        """
        return self._list_vulnerabilities_with_http_info(request)

    def _list_vulnerabilities_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'vul_id' in local_var_params:
            query_params.append(('vul_id', local_var_params['vul_id']))
        if 'vul_name' in local_var_params:
            query_params.append(('vul_name', local_var_params['vul_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'repair_priority' in local_var_params:
            query_params.append(('repair_priority', local_var_params['repair_priority']))
        if 'handle_status' in local_var_params:
            query_params.append(('handle_status', local_var_params['handle_status']))
        if 'cve_id' in local_var_params:
            query_params.append(('cve_id', local_var_params['cve_id']))
        if 'label_list' in local_var_params:
            query_params.append(('label_list', local_var_params['label_list']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'asset_value' in local_var_params:
            query_params.append(('asset_value', local_var_params['asset_value']))
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))

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
            resource_path='/v5/{project_id}/vulnerability/vulnerabilities',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListVulnerabilitiesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_weak_password_users(self, request):
        """查询弱口令检测结果列表

        查询弱口令检测结果列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWeakPasswordUsers
        :type request: :class:`huaweicloudsdkhss.v5.ListWeakPasswordUsersRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListWeakPasswordUsersResponse`
        """
        return self._list_weak_password_users_with_http_info(request)

    def _list_weak_password_users_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v5/{project_id}/baseline/weak-password-users',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListWeakPasswordUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_wtp_protect_host(self, request):
        """查询防护列表

        查询防护列表：查询网页防篡改主机防护状态列表信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWtpProtectHost
        :type request: :class:`huaweicloudsdkhss.v5.ListWtpProtectHostRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListWtpProtectHostResponse`
        """
        return self._list_wtp_protect_host_with_http_info(request)

    def _list_wtp_protect_host_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'public_ip' in local_var_params:
            query_params.append(('public_ip', local_var_params['public_ip']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))
        if 'os_type' in local_var_params:
            query_params.append(('os_type', local_var_params['os_type']))
        if 'protect_status' in local_var_params:
            query_params.append(('protect_status', local_var_params['protect_status']))
        if 'agent_status' in local_var_params:
            query_params.append(('agent_status', local_var_params['agent_status']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/webtamper/hosts',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListWtpProtectHostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_rasp_switch(self, request):
        """开启/关闭动态网页防篡改防护

        开启/关闭动态网页防篡改防护，下发/清空动态网页防篡改策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetRaspSwitch
        :type request: :class:`huaweicloudsdkhss.v5.SetRaspSwitchRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.SetRaspSwitchResponse`
        """
        return self._set_rasp_switch_with_http_info(request)

    def _set_rasp_switch_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/webtamper/rasp/status',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SetRaspSwitchResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_wtp_protection_status_info(self, request):
        """开启关闭网页防篡改防护

        开启/关闭网页防篡改功能防护，下发/清空网页防篡改策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetWtpProtectionStatusInfo
        :type request: :class:`huaweicloudsdkhss.v5.SetWtpProtectionStatusInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.SetWtpProtectionStatusInfoResponse`
        """
        return self._set_wtp_protection_status_info_with_http_info(request)

    def _set_wtp_protection_status_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/webtamper/static/status',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SetWtpProtectionStatusInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_asset_statistic(self, request):
        """统计资产信息，账号、端口、进程等

        资产统计信息，账号、端口、进程等
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAssetStatistic
        :type request: :class:`huaweicloudsdkhss.v5.ShowAssetStatisticRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowAssetStatisticResponse`
        """
        return self._show_asset_statistic_with_http_info(request)

    def _show_asset_statistic_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))

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
            resource_path='/v5/{project_id}/asset/statistics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAssetStatisticResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_backup_policy_info(self, request):
        """查询HSS存储库绑定的备份策略信息

        查询HSS存储库绑定的备份策略信息,确保已经购买了勒索防护存储库，可以从cbr云备份服务进行验证，确保已经存在HSS_projectid命名的存储库已经购买
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBackupPolicyInfo
        :type request: :class:`huaweicloudsdkhss.v5.ShowBackupPolicyInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowBackupPolicyInfoResponse`
        """
        return self._show_backup_policy_info_with_http_info(request)

    def _show_backup_policy_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/backup/policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowBackupPolicyInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_check_rule_detail(self, request):
        """查询配置检查项检测报告

        查询配置检查项检测报告
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCheckRuleDetail
        :type request: :class:`huaweicloudsdkhss.v5.ShowCheckRuleDetailRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowCheckRuleDetailResponse`
        """
        return self._show_check_rule_detail_with_http_info(request)

    def _show_check_rule_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'check_name' in local_var_params:
            query_params.append(('check_name', local_var_params['check_name']))
        if 'check_type' in local_var_params:
            query_params.append(('check_type', local_var_params['check_type']))
        if 'check_rule_id' in local_var_params:
            query_params.append(('check_rule_id', local_var_params['check_rule_id']))
        if 'standard' in local_var_params:
            query_params.append(('standard', local_var_params['standard']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))

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
            resource_path='/v5/{project_id}/baseline/check-rule/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCheckRuleDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_resource_quotas(self, request):
        """查询配额信息

        查询配额信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowResourceQuotas
        :type request: :class:`huaweicloudsdkhss.v5.ShowResourceQuotasRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowResourceQuotasResponse`
        """
        return self._show_resource_quotas_with_http_info(request)

    def _show_resource_quotas_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))
        if 'charging_mode' in local_var_params:
            query_params.append(('charging_mode', local_var_params['charging_mode']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/billing/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowResourceQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_risk_config_detail(self, request):
        """查询指定安全配置项的检查结果

        查询指定安全配置项的检查结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRiskConfigDetail
        :type request: :class:`huaweicloudsdkhss.v5.ShowRiskConfigDetailRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowRiskConfigDetailResponse`
        """
        return self._show_risk_config_detail_with_http_info(request)

    def _show_risk_config_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'check_name' in local_var_params:
            path_params['check_name'] = local_var_params['check_name']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'standard' in local_var_params:
            query_params.append(('standard', local_var_params['standard']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v5/{project_id}/baseline/risk-config/{check_name}/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowRiskConfigDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_protection(self, request):
        """开启勒索病毒防护

        开启勒索病毒防护,请保证该region有cbr云备份服务，勒索服务与云备份服务有关联关系
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartProtection
        :type request: :class:`huaweicloudsdkhss.v5.StartProtectionRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.StartProtectionResponse`
        """
        return self._start_protection_with_http_info(request)

    def _start_protection_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/ransomware/protection/open',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StartProtectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_protection(self, request):
        """关闭勒索病毒防护

        关闭勒索病毒防护
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopProtection
        :type request: :class:`huaweicloudsdkhss.v5.StopProtectionRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.StopProtectionResponse`
        """
        return self._stop_protection_with_http_info(request)

    def _stop_protection_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/ransomware/protection/close',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopProtectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def switch_hosts_protect_status(self, request):
        """切换防护状态

        切换防护状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchHostsProtectStatus
        :type request: :class:`huaweicloudsdkhss.v5.SwitchHostsProtectStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.SwitchHostsProtectStatusResponse`
        """
        return self._switch_hosts_protect_status_with_http_info(request)

    def _switch_hosts_protect_status_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/host-management/protection',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SwitchHostsProtectStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_backup_policy_info(self, request):
        """修改存储库绑定的备份策略

        修改存储库绑定的备份策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateBackupPolicyInfo
        :type request: :class:`huaweicloudsdkhss.v5.UpdateBackupPolicyInfoRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.UpdateBackupPolicyInfoResponse`
        """
        return self._update_backup_policy_info_with_http_info(request)

    def _update_backup_policy_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/backup/policy',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateBackupPolicyInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_protection_policy(self, request):
        """修改防护策略

        修改防护策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateProtectionPolicy
        :type request: :class:`huaweicloudsdkhss.v5.UpdateProtectionPolicyRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.UpdateProtectionPolicyResponse`
        """
        return self._update_protection_policy_with_http_info(request)

    def _update_protection_policy_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/ransomware/protection/policy',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateProtectionPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

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
