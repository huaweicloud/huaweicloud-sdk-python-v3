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


class BcsAsyncClient(Client):
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
        super(BcsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkbcs.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "BcsClient":
            raise TypeError("client type error, support client type is BcsClient")

        return ClientBuilder(clazz)

    def batch_add_peers_to_channel_async(self, request):
        """peer节点加入通道

        peer节点加入通道,目前仅支持往一个通道中加入peer

        :param BatchAddPeersToChannelRequest request
        :return: BatchAddPeersToChannelResponse
        """
        return self.batch_add_peers_to_channel_with_http_info(request)

    def batch_add_peers_to_channel_with_http_info(self, request):
        """peer节点加入通道

        peer节点加入通道,目前仅支持往一个通道中加入peer

        :param BatchAddPeersToChannelRequest request
        :return: BatchAddPeersToChannelResponse
        """

        all_params = ['blockchain_id', 'batch_add_peers_to_channel_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'blockchain_id' in local_var_params:
            path_params['blockchain_id'] = local_var_params['blockchain_id']

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
            resource_path='/v2/{project_id}/blockchains/{blockchain_id}/channels/peers',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchAddPeersToChannelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_create_channels_async(self, request):
        """创建通道

        创建通道

        :param BatchCreateChannelsRequest request
        :return: BatchCreateChannelsResponse
        """
        return self.batch_create_channels_with_http_info(request)

    def batch_create_channels_with_http_info(self, request):
        """创建通道

        创建通道

        :param BatchCreateChannelsRequest request
        :return: BatchCreateChannelsResponse
        """

        all_params = ['blockchain_id', 'batch_create_channels_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'blockchain_id' in local_var_params:
            path_params['blockchain_id'] = local_var_params['blockchain_id']

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
            resource_path='/v2/{project_id}/blockchains/{blockchain_id}/channels',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchCreateChannelsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_invite_members_to_channel_async(self, request):
        """邀请联盟成员

        批量邀请联盟成员加入通道，此操作会向被邀请方发出邀请通知

        :param BatchInviteMembersToChannelRequest request
        :return: BatchInviteMembersToChannelResponse
        """
        return self.batch_invite_members_to_channel_with_http_info(request)

    def batch_invite_members_to_channel_with_http_info(self, request):
        """邀请联盟成员

        批量邀请联盟成员加入通道，此操作会向被邀请方发出邀请通知

        :param BatchInviteMembersToChannelRequest request
        :return: BatchInviteMembersToChannelResponse
        """

        all_params = ['batch_invite_members_to_channel_request_body']
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
            resource_path='/v2/{project_id}/members/invitations',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchInviteMembersToChannelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_new_blockchain_async(self, request):
        """创建服务实例

        创建BCS服务实例

        :param CreateNewBlockchainRequest request
        :return: CreateNewBlockchainResponse
        """
        return self.create_new_blockchain_with_http_info(request)

    def create_new_blockchain_with_http_info(self, request):
        """创建服务实例

        创建BCS服务实例

        :param CreateNewBlockchainRequest request
        :return: CreateNewBlockchainResponse
        """

        all_params = ['create_new_blockchain_request_body']
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
            resource_path='/v2/{project_id}/blockchains',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateNewBlockchainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_blockchain_async(self, request):
        """删除bcs实例

        删除bcs实例

        :param DeleteBlockchainRequest request
        :return: DeleteBlockchainResponse
        """
        return self.delete_blockchain_with_http_info(request)

    def delete_blockchain_with_http_info(self, request):
        """删除bcs实例

        删除bcs实例

        :param DeleteBlockchainRequest request
        :return: DeleteBlockchainResponse
        """

        all_params = ['blockchain_id', 'is_delete_storage', 'is_delete_obs', 'is_delete_resource']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'blockchain_id' in local_var_params:
            path_params['blockchain_id'] = local_var_params['blockchain_id']

        query_params = []
        if 'is_delete_storage' in local_var_params:
            query_params.append(('is_delete_storage', local_var_params['is_delete_storage']))
        if 'is_delete_obs' in local_var_params:
            query_params.append(('is_delete_obs', local_var_params['is_delete_obs']))
        if 'is_delete_resource' in local_var_params:
            query_params.append(('is_delete_resource', local_var_params['is_delete_resource']))

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
            resource_path='/v2/{project_id}/blockchains/{blockchain_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteBlockchainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def download_blockchain_cert_async(self, request):
        """下载证书

        下载指定服务实例相关证书

        :param DownloadBlockchainCertRequest request
        :return: DownloadBlockchainCertResponse
        """
        return self.download_blockchain_cert_with_http_info(request)

    def download_blockchain_cert_with_http_info(self, request):
        """下载证书

        下载指定服务实例相关证书

        :param DownloadBlockchainCertRequest request
        :return: DownloadBlockchainCertResponse
        """

        all_params = ['blockchain_id', 'org_name', 'cert_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'blockchain_id' in local_var_params:
            path_params['blockchain_id'] = local_var_params['blockchain_id']

        query_params = []
        if 'org_name' in local_var_params:
            query_params.append(('org_name', local_var_params['org_name']))
        if 'cert_type' in local_var_params:
            query_params.append(('cert_type', local_var_params['cert_type']))

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
            resource_path='/v2/{project_id}/blockchains/{blockchain_id}/cert',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DownloadBlockchainCertResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def download_blockchain_sdk_config_async(self, request):
        """下载SDK配置

        下载指定服务实例SDK配置文件

        :param DownloadBlockchainSdkConfigRequest request
        :return: DownloadBlockchainSdkConfigResponse
        """
        return self.download_blockchain_sdk_config_with_http_info(request)

    def download_blockchain_sdk_config_with_http_info(self, request):
        """下载SDK配置

        下载指定服务实例SDK配置文件

        :param DownloadBlockchainSdkConfigRequest request
        :return: DownloadBlockchainSdkConfigResponse
        """

        all_params = ['blockchain_id', 'download_blockchain_sdk_config_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'blockchain_id' in local_var_params:
            path_params['blockchain_id'] = local_var_params['blockchain_id']

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
            resource_path='/v2/{project_id}/blockchains/{blockchain_id}/sdk-cfg',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DownloadBlockchainSdkConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def handle_notification_async(self, request):
        """处理联盟邀请

        处理联盟邀请

        :param HandleNotificationRequest request
        :return: HandleNotificationResponse
        """
        return self.handle_notification_with_http_info(request)

    def handle_notification_with_http_info(self, request):
        """处理联盟邀请

        处理联盟邀请

        :param HandleNotificationRequest request
        :return: HandleNotificationResponse
        """

        all_params = ['handle_notification_request_body']
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
            resource_path='/v2/{project_id}/notification/handle',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='HandleNotificationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_bcs_metric_async(self, request):
        """查询BCS服务实例监控数据

        [该接口用于查询BCS服务的监控数据，可以指定相应的指标名称,目前不支持IEF节点](tag:online)[该接口用于查询BCS服务的监控数据，可以指定相应的指标名称](tag:hcs)

        :param ListBcsMetricRequest request
        :return: ListBcsMetricResponse
        """
        return self.list_bcs_metric_with_http_info(request)

    def list_bcs_metric_with_http_info(self, request):
        """查询BCS服务实例监控数据

        [该接口用于查询BCS服务的监控数据，可以指定相应的指标名称,目前不支持IEF节点](tag:online)[该接口用于查询BCS服务的监控数据，可以指定相应的指标名称](tag:hcs)

        :param ListBcsMetricRequest request
        :return: ListBcsMetricResponse
        """

        all_params = ['blockchain_id', 'list_bcs_metric_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'blockchain_id' in local_var_params:
            path_params['blockchain_id'] = local_var_params['blockchain_id']

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
            resource_path='/v2/{project_id}/blockchains/{blockchain_id}/metric/list',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListBcsMetricResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_blockchain_channels_async(self, request):
        """查询通道信息

        查询指定服务实例通道信息

        :param ListBlockchainChannelsRequest request
        :return: ListBlockchainChannelsResponse
        """
        return self.list_blockchain_channels_with_http_info(request)

    def list_blockchain_channels_with_http_info(self, request):
        """查询通道信息

        查询指定服务实例通道信息

        :param ListBlockchainChannelsRequest request
        :return: ListBlockchainChannelsResponse
        """

        all_params = ['blockchain_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'blockchain_id' in local_var_params:
            path_params['blockchain_id'] = local_var_params['blockchain_id']

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
            resource_path='/v2/{project_id}/blockchains/{blockchain_id}/channels',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListBlockchainChannelsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_blockchains_async(self, request):
        """查询服务实例简要信息

        查询当前项目下所有服务实例的简要信息

        :param ListBlockchainsRequest request
        :return: ListBlockchainsResponse
        """
        return self.list_blockchains_with_http_info(request)

    def list_blockchains_with_http_info(self, request):
        """查询服务实例简要信息

        查询当前项目下所有服务实例的简要信息

        :param ListBlockchainsRequest request
        :return: ListBlockchainsResponse
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
            resource_path='/v2/{project_id}/blockchains',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListBlockchainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_entity_metric_async(self, request):
        """查询BCS组织监控数据列表

        该接口用于查询BCS组织的监控数据列表。

        :param ListEntityMetricRequest request
        :return: ListEntityMetricResponse
        """
        return self.list_entity_metric_with_http_info(request)

    def list_entity_metric_with_http_info(self, request):
        """查询BCS组织监控数据列表

        该接口用于查询BCS组织的监控数据列表。

        :param ListEntityMetricRequest request
        :return: ListEntityMetricResponse
        """

        all_params = ['blockchain_id', 'list_entity_metric_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'blockchain_id' in local_var_params:
            path_params['blockchain_id'] = local_var_params['blockchain_id']

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
            resource_path='/v2/{project_id}/blockchains/{blockchain_id}/entity/metric/list',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListEntityMetricResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_instance_metric_async(self, request):
        """查询BCS组织实例监控数据详情

        该接口用于BCS组织实例监控数据详情。

        :param ListInstanceMetricRequest request
        :return: ListInstanceMetricResponse
        """
        return self.list_instance_metric_with_http_info(request)

    def list_instance_metric_with_http_info(self, request):
        """查询BCS组织实例监控数据详情

        该接口用于BCS组织实例监控数据详情。

        :param ListInstanceMetricRequest request
        :return: ListInstanceMetricResponse
        """

        all_params = ['blockchain_id', 'list_instance_metric_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'blockchain_id' in local_var_params:
            path_params['blockchain_id'] = local_var_params['blockchain_id']

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
            resource_path='/v2/{project_id}/blockchains/{blockchain_id}/entity/instance/metric/list',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListInstanceMetricResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_members_async(self, request):
        """获取联盟成员列表

        获取联盟成员列表

        :param ListMembersRequest request
        :return: ListMembersResponse
        """
        return self.list_members_with_http_info(request)

    def list_members_with_http_info(self, request):
        """获取联盟成员列表

        获取联盟成员列表

        :param ListMembersRequest request
        :return: ListMembersResponse
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
            resource_path='/v2/{project_id}/members',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListMembersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_notifications_async(self, request):
        """获取全部通知

        获取全部通知

        :param ListNotificationsRequest request
        :return: ListNotificationsResponse
        """
        return self.list_notifications_with_http_info(request)

    def list_notifications_with_http_info(self, request):
        """获取全部通知

        获取全部通知

        :param ListNotificationsRequest request
        :return: ListNotificationsResponse
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
            resource_path='/v2/{project_id}/notifications',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListNotificationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_quotas_async(self, request):
        """查询配额

        查询当前项目下BCS服务所有资源的配额信息

        :param ListQuotasRequest request
        :return: ListQuotasResponse
        """
        return self.list_quotas_with_http_info(request)

    def list_quotas_with_http_info(self, request):
        """查询配额

        查询当前项目下BCS服务所有资源的配额信息

        :param ListQuotasRequest request
        :return: ListQuotasResponse
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
            resource_path='/v2/{project_id}/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_blockchain_detail_async(self, request):
        """查询详细信息

        查询指定服务实例详细信息

        :param ShowBlockchainDetailRequest request
        :return: ShowBlockchainDetailResponse
        """
        return self.show_blockchain_detail_with_http_info(request)

    def show_blockchain_detail_with_http_info(self, request):
        """查询详细信息

        查询指定服务实例详细信息

        :param ShowBlockchainDetailRequest request
        :return: ShowBlockchainDetailResponse
        """

        all_params = ['blockchain_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'blockchain_id' in local_var_params:
            path_params['blockchain_id'] = local_var_params['blockchain_id']

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
            resource_path='/v2/{project_id}/blockchains/{blockchain_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowBlockchainDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_blockchain_nodes_async(self, request):
        """查询节点信息

        查询指定服务实例节点信息

        :param ShowBlockchainNodesRequest request
        :return: ShowBlockchainNodesResponse
        """
        return self.show_blockchain_nodes_with_http_info(request)

    def show_blockchain_nodes_with_http_info(self, request):
        """查询节点信息

        查询指定服务实例节点信息

        :param ShowBlockchainNodesRequest request
        :return: ShowBlockchainNodesResponse
        """

        all_params = ['blockchain_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'blockchain_id' in local_var_params:
            path_params['blockchain_id'] = local_var_params['blockchain_id']

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
            resource_path='/v2/{project_id}/blockchains/{blockchain_id}/nodes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowBlockchainNodesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_blockchain_status_async(self, request):
        """查询创建状态

        查询指定服务实例创建状态

        :param ShowBlockchainStatusRequest request
        :return: ShowBlockchainStatusResponse
        """
        return self.show_blockchain_status_with_http_info(request)

    def show_blockchain_status_with_http_info(self, request):
        """查询创建状态

        查询指定服务实例创建状态

        :param ShowBlockchainStatusRequest request
        :return: ShowBlockchainStatusResponse
        """

        all_params = ['blockchain_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'blockchain_id' in local_var_params:
            path_params['blockchain_id'] = local_var_params['blockchain_id']

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
            resource_path='/v2/{project_id}/blockchains/{blockchain_id}/status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowBlockchainStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_instance_async(self, request):
        """修改实例

        修改实例的节点、组织，目前仅支持添加节点，添加组织

        :param UpdateInstanceRequest request
        :return: UpdateInstanceResponse
        """
        return self.update_instance_with_http_info(request)

    def update_instance_with_http_info(self, request):
        """修改实例

        修改实例的节点、组织，目前仅支持添加节点，添加组织

        :param UpdateInstanceRequest request
        :return: UpdateInstanceResponse
        """

        all_params = ['blockchain_id', 'update_instance_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'blockchain_id' in local_var_params:
            path_params['blockchain_id'] = local_var_params['blockchain_id']

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
            resource_path='/v2/{project_id}/blockchains/{blockchain_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateInstanceResponse',
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
        :param header_params: Header parameters to be
            placed in the request header.
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
            request_type=request_type,
	    async_request=True)
