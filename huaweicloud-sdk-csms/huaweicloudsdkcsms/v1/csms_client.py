# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class CsmsClient(Client):
    def __init__(self):
        super(CsmsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcsms.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CsmsClient":
                raise TypeError("client type error, support client type is CsmsClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_create_or_delete_tags(self, request):
        """批量添加或删除凭据标签

        - 功能介绍：批量添加或删除凭据标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateOrDeleteTags
        :type request: :class:`huaweicloudsdkcsms.v1.BatchCreateOrDeleteTagsRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.BatchCreateOrDeleteTagsResponse`
        """
        return self._batch_create_or_delete_tags_with_http_info(request)

    def _batch_create_or_delete_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_id' in local_var_params:
            path_params['secret_id'] = local_var_params['secret_id']

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
            resource_path='/v1/{project_id}/csms/{secret_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreateOrDeleteTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_secret(self, request):
        """创建凭据

        创建新的凭据，并将凭据值存入凭据的初始版本。
        
        凭据管理服务将凭据值加密后，存储在凭据对象下的版本中。每个版本可与多个凭据版本状态相关联，凭据版本状态用于标识凭据版本处于的阶段，没有版本状态标记的版本视为已弃用，可用凭据管理服务自动删除。
        
        初始版本的状态被标记为SYSCURRENT。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSecret
        :type request: :class:`huaweicloudsdkcsms.v1.CreateSecretRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.CreateSecretResponse`
        """
        return self._create_secret_with_http_info(request)

    def _create_secret_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v1/{project_id}/secrets',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSecretResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_secret_event(self, request):
        """创建事件

        创建事件，事件可配置在一个或多个凭据对象上。当事件为启用状态且包含的基础事件类型在凭据对象上触发时，云服务会将对应的事件通知发送至事件指定的通知主题上。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSecretEvent
        :type request: :class:`huaweicloudsdkcsms.v1.CreateSecretEventRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.CreateSecretEventResponse`
        """
        return self._create_secret_event_with_http_info(request)

    def _create_secret_event_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v1/{project_id}/csms/events',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSecretEventResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_secret_tag(self, request):
        """添加凭据标签

        添加凭据标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSecretTag
        :type request: :class:`huaweicloudsdkcsms.v1.CreateSecretTagRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.CreateSecretTagResponse`
        """
        return self._create_secret_tag_with_http_info(request)

    def _create_secret_tag_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_id' in local_var_params:
            path_params['secret_id'] = local_var_params['secret_id']

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
            resource_path='/v1/{project_id}/csms/{secret_id}/tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSecretTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_secret_version(self, request):
        """创建凭据版本

        在指定的凭据中，创建一个新的凭据版本，用于加密保管新的凭据值。默认情况下，新创建的凭据版本被标记为SYSCURRENT状态，而SYSCURRENT标记的前一个凭据版本被标记为SYSPREVIOUS状态。您可以通过指定VersionStage参数来覆盖默认行为。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSecretVersion
        :type request: :class:`huaweicloudsdkcsms.v1.CreateSecretVersionRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.CreateSecretVersionResponse`
        """
        return self._create_secret_version_with_http_info(request)

    def _create_secret_version_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_name' in local_var_params:
            path_params['secret_name'] = local_var_params['secret_name']

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
            resource_path='/v1/{project_id}/secrets/{secret_name}/versions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSecretVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_secret(self, request):
        """立即删除凭据

        立即删除指定的凭据，且无法恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSecret
        :type request: :class:`huaweicloudsdkcsms.v1.DeleteSecretRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.DeleteSecretResponse`
        """
        return self._delete_secret_with_http_info(request)

    def _delete_secret_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_name' in local_var_params:
            path_params['secret_name'] = local_var_params['secret_name']

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
            resource_path='/v1/{project_id}/secrets/{secret_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSecretResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_secret_event(self, request):
        """立即删除事件

        立即删除指定的事件，且无法恢复。如事件存在凭据引用，则无法删除，请先解除关联。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSecretEvent
        :type request: :class:`huaweicloudsdkcsms.v1.DeleteSecretEventRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.DeleteSecretEventResponse`
        """
        return self._delete_secret_event_with_http_info(request)

    def _delete_secret_event_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'event_name' in local_var_params:
            path_params['event_name'] = local_var_params['event_name']

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
            resource_path='/v1/{project_id}/csms/events/{event_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSecretEventResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_secret_for_schedule(self, request):
        """创建凭据的定时删除任务

        指定延迟删除时间，创建删除凭据的定时任务，可设置7~30天的的延迟删除时间。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSecretForSchedule
        :type request: :class:`huaweicloudsdkcsms.v1.DeleteSecretForScheduleRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.DeleteSecretForScheduleResponse`
        """
        return self._delete_secret_for_schedule_with_http_info(request)

    def _delete_secret_for_schedule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_name' in local_var_params:
            path_params['secret_name'] = local_var_params['secret_name']

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
            resource_path='/v1/{project_id}/secrets/{secret_name}/scheduled-deleted-tasks/create',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSecretForScheduleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_secret_stage(self, request):
        """删除凭据的版本状态

        删除指定的凭据版本状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSecretStage
        :type request: :class:`huaweicloudsdkcsms.v1.DeleteSecretStageRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.DeleteSecretStageResponse`
        """
        return self._delete_secret_stage_with_http_info(request)

    def _delete_secret_stage_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_name' in local_var_params:
            path_params['secret_name'] = local_var_params['secret_name']
        if 'stage_name' in local_var_params:
            path_params['stage_name'] = local_var_params['stage_name']

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
            resource_path='/v1/{project_id}/secrets/{secret_name}/stages/{stage_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSecretStageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_secret_tag(self, request):
        """删除凭据标签

        删除凭据标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSecretTag
        :type request: :class:`huaweicloudsdkcsms.v1.DeleteSecretTagRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.DeleteSecretTagResponse`
        """
        return self._delete_secret_tag_with_http_info(request)

    def _delete_secret_tag_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_id' in local_var_params:
            path_params['secret_id'] = local_var_params['secret_id']
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
            resource_path='/v1/{project_id}/csms/{secret_id}/tags/{key}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSecretTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def download_secret_blob(self, request):
        """下载凭据备份

        下载指定凭据的备份文件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadSecretBlob
        :type request: :class:`huaweicloudsdkcsms.v1.DownloadSecretBlobRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.DownloadSecretBlobResponse`
        """
        return self._download_secret_blob_with_http_info(request)

    def _download_secret_blob_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_name' in local_var_params:
            path_params['secret_name'] = local_var_params['secret_name']

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
            resource_path='/v1/{project_id}/secrets/{secret_name}/backup',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DownloadSecretBlobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_notification_records(self, request):
        """查询已触发的事件通知记录

        查询三个月内所有已触发的事件通知记录。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNotificationRecords
        :type request: :class:`huaweicloudsdkcsms.v1.ListNotificationRecordsRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.ListNotificationRecordsResponse`
        """
        return self._list_notification_records_with_http_info(request)

    def _list_notification_records_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v1/{project_id}/csms/notification-records',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListNotificationRecordsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_project_secrets_tags(self, request):
        """查询项目标签

        查询用户在指定项目下的所有凭据标签集合。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectSecretsTags
        :type request: :class:`huaweicloudsdkcsms.v1.ListProjectSecretsTagsRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.ListProjectSecretsTagsResponse`
        """
        return self._list_project_secrets_tags_with_http_info(request)

    def _list_project_secrets_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v1/{project_id}/csms/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProjectSecretsTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_resource_instances(self, request):
        """查询凭据实例

        查询凭据实例。通过标签过滤，筛选用户凭据，返回凭据列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceInstances
        :type request: :class:`huaweicloudsdkcsms.v1.ListResourceInstancesRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.ListResourceInstancesResponse`
        """
        return self._list_resource_instances_with_http_info(request)

    def _list_resource_instances_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_instances' in local_var_params:
            path_params['resource_instances'] = local_var_params['resource_instances']

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
            resource_path='/v1/{project_id}/csms/{resource_instances}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListResourceInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_secret_events(self, request):
        """查询事件列表

        查询当前用户在本项目下创建的所有事件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSecretEvents
        :type request: :class:`huaweicloudsdkcsms.v1.ListSecretEventsRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.ListSecretEventsResponse`
        """
        return self._list_secret_events_with_http_info(request)

    def _list_secret_events_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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
            resource_path='/v1/{project_id}/csms/events',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSecretEventsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_secret_tags(self, request):
        """查询凭据标签

        查询凭据标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSecretTags
        :type request: :class:`huaweicloudsdkcsms.v1.ListSecretTagsRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.ListSecretTagsResponse`
        """
        return self._list_secret_tags_with_http_info(request)

    def _list_secret_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_id' in local_var_params:
            path_params['secret_id'] = local_var_params['secret_id']

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
            resource_path='/v1/{project_id}/csms/{secret_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSecretTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_secret_versions(self, request):
        """查询凭据的版本列表

        查询指定凭据下的版本列表信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSecretVersions
        :type request: :class:`huaweicloudsdkcsms.v1.ListSecretVersionsRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.ListSecretVersionsResponse`
        """
        return self._list_secret_versions_with_http_info(request)

    def _list_secret_versions_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_name' in local_var_params:
            path_params['secret_name'] = local_var_params['secret_name']

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
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
            resource_path='/v1/{project_id}/secrets/{secret_name}/versions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSecretVersionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_secrets(self, request):
        """查询凭据列表

        查询当前用户在本项目下创建的所有凭据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSecrets
        :type request: :class:`huaweicloudsdkcsms.v1.ListSecretsRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.ListSecretsResponse`
        """
        return self._list_secrets_with_http_info(request)

    def _list_secrets_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'event_name' in local_var_params:
            query_params.append(('event_name', local_var_params['event_name']))

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
            resource_path='/v1/{project_id}/secrets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSecretsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restore_secret(self, request):
        """取消凭据的定时删除任务

        取消凭据的定时删除任务，凭据对象恢复可使用状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestoreSecret
        :type request: :class:`huaweicloudsdkcsms.v1.RestoreSecretRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.RestoreSecretResponse`
        """
        return self._restore_secret_with_http_info(request)

    def _restore_secret_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_name' in local_var_params:
            path_params['secret_name'] = local_var_params['secret_name']

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
            resource_path='/v1/{project_id}/secrets/{secret_name}/scheduled-deleted-tasks/cancel',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RestoreSecretResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def rotate_secret(self, request):
        """轮转凭据

        立即执行轮转凭据。在指定的凭据中，创建一个新的凭据版本，用于加密存储后台随机产生的凭据值。同时将新创建的凭据版本标记为SYSCURRENT状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RotateSecret
        :type request: :class:`huaweicloudsdkcsms.v1.RotateSecretRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.RotateSecretResponse`
        """
        return self._rotate_secret_with_http_info(request)

    def _rotate_secret_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_name' in local_var_params:
            path_params['secret_name'] = local_var_params['secret_name']

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
            resource_path='/v1/{project_id}/secrets/{secret_name}/rotate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RotateSecretResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_secret(self, request):
        """查询凭据

        查询指定凭据的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSecret
        :type request: :class:`huaweicloudsdkcsms.v1.ShowSecretRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.ShowSecretResponse`
        """
        return self._show_secret_with_http_info(request)

    def _show_secret_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_name' in local_var_params:
            path_params['secret_name'] = local_var_params['secret_name']

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
            resource_path='/v1/{project_id}/secrets/{secret_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSecretResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_secret_event(self, request):
        """查询事件

        查询指定事件的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSecretEvent
        :type request: :class:`huaweicloudsdkcsms.v1.ShowSecretEventRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.ShowSecretEventResponse`
        """
        return self._show_secret_event_with_http_info(request)

    def _show_secret_event_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'event_name' in local_var_params:
            path_params['event_name'] = local_var_params['event_name']

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
            resource_path='/v1/{project_id}/csms/events/{event_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSecretEventResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_secret_stage(self, request):
        """查询凭据的版本状态

        查询指定凭据版本状态标记的版本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSecretStage
        :type request: :class:`huaweicloudsdkcsms.v1.ShowSecretStageRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.ShowSecretStageResponse`
        """
        return self._show_secret_stage_with_http_info(request)

    def _show_secret_stage_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_name' in local_var_params:
            path_params['secret_name'] = local_var_params['secret_name']
        if 'stage_name' in local_var_params:
            path_params['stage_name'] = local_var_params['stage_name']

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
            resource_path='/v1/{project_id}/secrets/{secret_name}/stages/{stage_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSecretStageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_secret_version(self, request):
        """查询凭据的版本与凭据值

        查询指定凭据版本的信息和版本中的明文凭据值，只能查询ENABLED状态的凭据。
        通过/v1/{project_id}/secrets/{secret_name}/versions/latest （即将当前接口URL中的{version_id}赋值为latest）可访问凭据最新版本的凭据值。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSecretVersion
        :type request: :class:`huaweicloudsdkcsms.v1.ShowSecretVersionRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.ShowSecretVersionResponse`
        """
        return self._show_secret_version_with_http_info(request)

    def _show_secret_version_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_name' in local_var_params:
            path_params['secret_name'] = local_var_params['secret_name']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/v1/{project_id}/secrets/{secret_name}/versions/{version_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSecretVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_secret(self, request):
        """更新凭据

        更新指定凭据的元数据信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSecret
        :type request: :class:`huaweicloudsdkcsms.v1.UpdateSecretRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.UpdateSecretResponse`
        """
        return self._update_secret_with_http_info(request)

    def _update_secret_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_name' in local_var_params:
            path_params['secret_name'] = local_var_params['secret_name']

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
            resource_path='/v1/{project_id}/secrets/{secret_name}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateSecretResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_secret_event(self, request):
        """更新事件

        更新指定事件的元数据信息。支持更新的元数据包含事件启用状态、基础类型列表、通知主题。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSecretEvent
        :type request: :class:`huaweicloudsdkcsms.v1.UpdateSecretEventRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.UpdateSecretEventResponse`
        """
        return self._update_secret_event_with_http_info(request)

    def _update_secret_event_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'event_name' in local_var_params:
            path_params['event_name'] = local_var_params['event_name']

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
            resource_path='/v1/{project_id}/csms/events/{event_name}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateSecretEventResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_secret_stage(self, request):
        """更新凭据的版本状态

        更新凭据的版本状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSecretStage
        :type request: :class:`huaweicloudsdkcsms.v1.UpdateSecretStageRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.UpdateSecretStageResponse`
        """
        return self._update_secret_stage_with_http_info(request)

    def _update_secret_stage_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_name' in local_var_params:
            path_params['secret_name'] = local_var_params['secret_name']
        if 'stage_name' in local_var_params:
            path_params['stage_name'] = local_var_params['stage_name']

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
            resource_path='/v1/{project_id}/secrets/{secret_name}/stages/{stage_name}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateSecretStageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_version(self, request):
        """更新凭据版本

        当前支持更新指定凭据版本的有效期，只能更新ENABLED状态的凭据。在关联订阅的事件包含“版本过期”基础事件类型时，每次更新版本有效期后仅会触发一次事件通知。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateVersion
        :type request: :class:`huaweicloudsdkcsms.v1.UpdateVersionRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.UpdateVersionResponse`
        """
        return self._update_version_with_http_info(request)

    def _update_version_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_name' in local_var_params:
            path_params['secret_name'] = local_var_params['secret_name']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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
            resource_path='/v1/{project_id}/secrets/{secret_name}/versions/{version_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def upload_secret_blob(self, request):
        """恢复凭据对象

        通过上传凭据备份文件，恢复凭据对象
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadSecretBlob
        :type request: :class:`huaweicloudsdkcsms.v1.UploadSecretBlobRequest`
        :rtype: :class:`huaweicloudsdkcsms.v1.UploadSecretBlobResponse`
        """
        return self._upload_secret_blob_with_http_info(request)

    def _upload_secret_blob_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v1/{project_id}/secrets/restore',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UploadSecretBlobResponse',
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
