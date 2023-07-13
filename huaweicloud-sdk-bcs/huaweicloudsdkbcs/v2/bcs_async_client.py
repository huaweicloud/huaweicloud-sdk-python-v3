# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class BcsAsyncClient(Client):
    def __init__(self):
        super(BcsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkbcs.v2.model")

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
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAddPeersToChannel
        :type request: :class:`huaweicloudsdkbcs.v2.BatchAddPeersToChannelRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.BatchAddPeersToChannelResponse`
        """
        return self._batch_add_peers_to_channel_with_http_info(request)

    def _batch_add_peers_to_channel_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='BatchAddPeersToChannelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_create_channels_async(self, request):
        """创建通道

        创建通道
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateChannels
        :type request: :class:`huaweicloudsdkbcs.v2.BatchCreateChannelsRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.BatchCreateChannelsResponse`
        """
        return self._batch_create_channels_with_http_info(request)

    def _batch_create_channels_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='BatchCreateChannelsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_invite_members_to_channel_async(self, request):
        """邀请联盟成员

        批量邀请联盟成员加入通道，此操作会向被邀请方发出邀请通知
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchInviteMembersToChannel
        :type request: :class:`huaweicloudsdkbcs.v2.BatchInviteMembersToChannelRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.BatchInviteMembersToChannelResponse`
        """
        return self._batch_invite_members_to_channel_with_http_info(request)

    def _batch_invite_members_to_channel_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/members/invitations',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchInviteMembersToChannelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_remove_orgs_from_channel_async(self, request):
        """BCS组织退出某通道

        该接口用于BCS组织退出某通道。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchRemoveOrgsFromChannel
        :type request: :class:`huaweicloudsdkbcs.v2.BatchRemoveOrgsFromChannelRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.BatchRemoveOrgsFromChannelResponse`
        """
        return self._batch_remove_orgs_from_channel_with_http_info(request)

    def _batch_remove_orgs_from_channel_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'blockchain_id' in local_var_params:
            path_params['blockchain_id'] = local_var_params['blockchain_id']
        if 'channel_id' in local_var_params:
            path_params['channel_id'] = local_var_params['channel_id']

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
            resource_path='/v2/{project_id}/blockchains/{blockchain_id}/{channel_id}/orgs/quit',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchRemoveOrgsFromChannelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_remove_peers_from_channel_async(self, request):
        """BCS某个组织中的节点退出某通道

        该接口用于BCS某个组织中的节点退出某通道。当节点为通道中最后一个节点时，需要使用组织退通道的接口来将通道中的最后一个节点退出。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchRemovePeersFromChannel
        :type request: :class:`huaweicloudsdkbcs.v2.BatchRemovePeersFromChannelRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.BatchRemovePeersFromChannelResponse`
        """
        return self._batch_remove_peers_from_channel_with_http_info(request)

    def _batch_remove_peers_from_channel_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'blockchain_id' in local_var_params:
            path_params['blockchain_id'] = local_var_params['blockchain_id']
        if 'channel_id' in local_var_params:
            path_params['channel_id'] = local_var_params['channel_id']

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
            resource_path='/v2/{project_id}/blockchains/{blockchain_id}/{channel_id}/peers/quit',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchRemovePeersFromChannelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_blockchain_cert_by_user_name_async(self, request):
        """生成用户证书

        通过用户名生成指定服务实例组织用户证书
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateBlockchainCertByUserName
        :type request: :class:`huaweicloudsdkbcs.v2.CreateBlockchainCertByUserNameRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.CreateBlockchainCertByUserNameResponse`
        """
        return self._create_blockchain_cert_by_user_name_with_http_info(request)

    def _create_blockchain_cert_by_user_name_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'blockchain_id' in local_var_params:
            path_params['blockchain_id'] = local_var_params['blockchain_id']
        if 'org_name' in local_var_params:
            path_params['org_name'] = local_var_params['org_name']
        if 'user_name' in local_var_params:
            path_params['user_name'] = local_var_params['user_name']

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
            resource_path='/v2/{project_id}/blockchains/{blockchain_id}/orgs/{org_name}/usercert/{user_name}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateBlockchainCertByUserNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_new_blockchain_async(self, request):
        """创建服务实例

        创建BCS服务实例,只支持按需创建
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateNewBlockchain
        :type request: :class:`huaweicloudsdkbcs.v2.CreateNewBlockchainRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.CreateNewBlockchainResponse`
        """
        return self._create_new_blockchain_with_http_info(request)

    def _create_new_blockchain_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/blockchains',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateNewBlockchainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_blockchain_async(self, request):
        """删除服务实例

        删除bcs实例。包周期实例不支持
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBlockchain
        :type request: :class:`huaweicloudsdkbcs.v2.DeleteBlockchainRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.DeleteBlockchainResponse`
        """
        return self._delete_blockchain_with_http_info(request)

    def _delete_blockchain_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
        if 'is_delete_ief' in local_var_params:
            query_params.append(('is_delete_ief', local_var_params['is_delete_ief']))
        if 'is_delete_lightpeer' in local_var_params:
            query_params.append(('is_delete_lightpeer', local_var_params['is_delete_lightpeer']))
        if 'ief_nodes_id' in local_var_params:
            query_params.append(('ief_nodes_id', local_var_params['ief_nodes_id']))

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
            cname=cname,
            response_type='DeleteBlockchainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_channel_async(self, request):
        """BCS删除某个通道

        该接口用于BCS删除某个通道。仅支持删除空通道
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteChannel
        :type request: :class:`huaweicloudsdkbcs.v2.DeleteChannelRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.DeleteChannelResponse`
        """
        return self._delete_channel_with_http_info(request)

    def _delete_channel_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'blockchain_id' in local_var_params:
            path_params['blockchain_id'] = local_var_params['blockchain_id']
        if 'channel_id' in local_var_params:
            path_params['channel_id'] = local_var_params['channel_id']

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
            resource_path='/v2/{project_id}/blockchains/{blockchain_id}/channel/{channel_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteChannelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_member_invite_async(self, request):
        """删除邀请成员信息

        可通过此接口批量取消邀请或删除对已退出或拒绝加入或解散的成员邀请信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteMemberInvite
        :type request: :class:`huaweicloudsdkbcs.v2.DeleteMemberInviteRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.DeleteMemberInviteResponse`
        """
        return self._delete_member_invite_with_http_info(request)

    def _delete_member_invite_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/members/invitations',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteMemberInviteResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def download_blockchain_cert_async(self, request):
        """下载证书

        下载指定服务实例相关证书
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadBlockchainCert
        :type request: :class:`huaweicloudsdkbcs.v2.DownloadBlockchainCertRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.DownloadBlockchainCertResponse`
        """
        return self._download_blockchain_cert_with_http_info(request)

    def _download_blockchain_cert_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='DownloadBlockchainCertResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def download_blockchain_sdk_config_async(self, request):
        """下载SDK配置

        下载指定服务实例SDK配置文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadBlockchainSdkConfig
        :type request: :class:`huaweicloudsdkbcs.v2.DownloadBlockchainSdkConfigRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.DownloadBlockchainSdkConfigResponse`
        """
        return self._download_blockchain_sdk_config_with_http_info(request)

    def _download_blockchain_sdk_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='DownloadBlockchainSdkConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def freeze_cert_async(self, request):
        """冻结用户证书

        冻结指定服务实例组织用户证书，冻结后需等待半分钟到一分钟左右生效
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for FreezeCert
        :type request: :class:`huaweicloudsdkbcs.v2.FreezeCertRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.FreezeCertResponse`
        """
        return self._freeze_cert_with_http_info(request)

    def _freeze_cert_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_name' in local_var_params:
            path_params['user_name'] = local_var_params['user_name']
        if 'blockchain_id' in local_var_params:
            path_params['blockchain_id'] = local_var_params['blockchain_id']
        if 'org_name' in local_var_params:
            path_params['org_name'] = local_var_params['org_name']

        query_params = []

        header_params = {}

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/blockchains/{blockchain_id}/orgs/{org_name}/usercert/{user_name}/freeze',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='FreezeCertResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def handle_notification_async(self, request):
        """处理联盟邀请

        处理联盟邀请
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for HandleNotification
        :type request: :class:`huaweicloudsdkbcs.v2.HandleNotificationRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.HandleNotificationResponse`
        """
        return self._handle_notification_with_http_info(request)

    def _handle_notification_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/notification/handle',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='HandleNotificationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def handle_union_member_quit_list_async(self, request):
        """被邀请方退出指定联盟

        被邀请方退出联盟
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for HandleUnionMemberQuitList
        :type request: :class:`huaweicloudsdkbcs.v2.HandleUnionMemberQuitListRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.HandleUnionMemberQuitListResponse`
        """
        return self._handle_union_member_quit_list_with_http_info(request)

    def _handle_union_member_quit_list_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/members/quit',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='HandleUnionMemberQuitListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_bcs_events_async(self, request):
        """查询服务实例告警信息

        该接口用于查询BCS服务的事件、告警数据，可以指定查询时的过滤条件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBcsEvents
        :type request: :class:`huaweicloudsdkbcs.v2.ListBcsEventsRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.ListBcsEventsResponse`
        """
        return self._list_bcs_events_with_http_info(request)

    def _list_bcs_events_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'blockchain_id' in local_var_params:
            path_params['blockchain_id'] = local_var_params['blockchain_id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

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
            resource_path='/v2/{project_id}/blockchains/{blockchain_id}/events',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBcsEventsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_bcs_events_statistic_async(self, request):
        """查询服务实例告警统计接口

        该接口用于查询BCS服务的分段事件、告警统计数据，可以指定查询时的过滤条件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBcsEventsStatistic
        :type request: :class:`huaweicloudsdkbcs.v2.ListBcsEventsStatisticRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.ListBcsEventsStatisticResponse`
        """
        return self._list_bcs_events_statistic_with_http_info(request)

    def _list_bcs_events_statistic_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'blockchain_id' in local_var_params:
            path_params['blockchain_id'] = local_var_params['blockchain_id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

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
            resource_path='/v2/{project_id}/blockchains/{blockchain_id}/events/statistic',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBcsEventsStatisticResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_bcs_metric_async(self, request):
        """查询服务实例监控数据

        该接口用于查询BCS服务的监控数据，可以指定相应的指标名称。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBcsMetric
        :type request: :class:`huaweicloudsdkbcs.v2.ListBcsMetricRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.ListBcsMetricResponse`
        """
        return self._list_bcs_metric_with_http_info(request)

    def _list_bcs_metric_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ListBcsMetricResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_blockchain_channels_async(self, request):
        """查询通道信息

        查询指定服务实例通道信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBlockchainChannels
        :type request: :class:`huaweicloudsdkbcs.v2.ListBlockchainChannelsRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.ListBlockchainChannelsResponse`
        """
        return self._list_blockchain_channels_with_http_info(request)

    def _list_blockchain_channels_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ListBlockchainChannelsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_blockchains_async(self, request):
        """查询服务实例列表

        查询当前项目下所有服务实例的简要信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBlockchains
        :type request: :class:`huaweicloudsdkbcs.v2.ListBlockchainsRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.ListBlockchainsResponse`
        """
        return self._list_blockchains_with_http_info(request)

    def _list_blockchains_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/blockchains',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBlockchainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_entity_metric_async(self, request):
        """查询BCS组织监控数据列表

        该接口用于查询BCS组织的监控数据列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEntityMetric
        :type request: :class:`huaweicloudsdkbcs.v2.ListEntityMetricRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.ListEntityMetricResponse`
        """
        return self._list_entity_metric_with_http_info(request)

    def _list_entity_metric_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ListEntityMetricResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instance_metric_async(self, request):
        """查询BCS组织实例监控数据详情

        该接口用于BCS组织实例监控数据详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstanceMetric
        :type request: :class:`huaweicloudsdkbcs.v2.ListInstanceMetricRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.ListInstanceMetricResponse`
        """
        return self._list_instance_metric_with_http_info(request)

    def _list_instance_metric_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ListInstanceMetricResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_members_async(self, request):
        """获取联盟成员列表

        获取联盟成员列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMembers
        :type request: :class:`huaweicloudsdkbcs.v2.ListMembersRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.ListMembersResponse`
        """
        return self._list_members_with_http_info(request)

    def _list_members_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/members',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListMembersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_notifications_async(self, request):
        """获取全部通知

        获取全部通知
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNotifications
        :type request: :class:`huaweicloudsdkbcs.v2.ListNotificationsRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.ListNotificationsResponse`
        """
        return self._list_notifications_with_http_info(request)

    def _list_notifications_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/notifications',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListNotificationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_op_record_async(self, request):
        """查询异步操作结果

        查询异步操作结果
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOpRecord
        :type request: :class:`huaweicloudsdkbcs.v2.ListOpRecordRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.ListOpRecordResponse`
        """
        return self._list_op_record_with_http_info(request)

    def _list_op_record_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'blockchain_id' in local_var_params:
            query_params.append(('blockchain_id', local_var_params['blockchain_id']))
        if 'operation_status' in local_var_params:
            query_params.append(('operation_status', local_var_params['operation_status']))
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))
        if 'operation_type' in local_var_params:
            query_params.append(('operation_type', local_var_params['operation_type']))
        if 'operation_id' in local_var_params:
            query_params.append(('operation_id', local_var_params['operation_id']))

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
            resource_path='/v2/{project_id}/operation/record',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListOpRecordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_quotas_async(self, request):
        """查询配额

        查询当前项目下BCS服务所有资源的配额信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListQuotas
        :type request: :class:`huaweicloudsdkbcs.v2.ListQuotasRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.ListQuotasResponse`
        """
        return self._list_quotas_with_http_info(request)

    def _list_quotas_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_blockchain_detail_async(self, request):
        """查询实例信息

        查询指定服务实例详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBlockchainDetail
        :type request: :class:`huaweicloudsdkbcs.v2.ShowBlockchainDetailRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.ShowBlockchainDetailResponse`
        """
        return self._show_blockchain_detail_with_http_info(request)

    def _show_blockchain_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ShowBlockchainDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_blockchain_flavors_async(self, request):
        """查询规格

        查询服务联盟链规格信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBlockchainFlavors
        :type request: :class:`huaweicloudsdkbcs.v2.ShowBlockchainFlavorsRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.ShowBlockchainFlavorsResponse`
        """
        return self._show_blockchain_flavors_with_http_info(request)

    def _show_blockchain_flavors_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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
            resource_path='/v2/{project_id}/blockchains/flavors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowBlockchainFlavorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_blockchain_nodes_async(self, request):
        """查询节点信息

        查询指定服务实例节点信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBlockchainNodes
        :type request: :class:`huaweicloudsdkbcs.v2.ShowBlockchainNodesRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.ShowBlockchainNodesResponse`
        """
        return self._show_blockchain_nodes_with_http_info(request)

    def _show_blockchain_nodes_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ShowBlockchainNodesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_blockchain_status_async(self, request):
        """查询创建状态

        查询指定服务实例创建状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBlockchainStatus
        :type request: :class:`huaweicloudsdkbcs.v2.ShowBlockchainStatusRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.ShowBlockchainStatusResponse`
        """
        return self._show_blockchain_status_with_http_info(request)

    def _show_blockchain_status_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ShowBlockchainStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def unfreeze_cert_async(self, request):
        """解冻用户证书

        解冻指定服务实例组织用户证书，解冻后需等待半分钟到一分钟左右生效
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UnfreezeCert
        :type request: :class:`huaweicloudsdkbcs.v2.UnfreezeCertRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.UnfreezeCertResponse`
        """
        return self._unfreeze_cert_with_http_info(request)

    def _unfreeze_cert_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_name' in local_var_params:
            path_params['user_name'] = local_var_params['user_name']
        if 'blockchain_id' in local_var_params:
            path_params['blockchain_id'] = local_var_params['blockchain_id']
        if 'org_name' in local_var_params:
            path_params['org_name'] = local_var_params['org_name']

        query_params = []

        header_params = {}

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/blockchains/{blockchain_id}/orgs/{org_name}/usercert/{user_name}/unfreeze',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UnfreezeCertResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_instance_async(self, request):
        """修改服务实例

        修改实例的节点、组织，目前仅支持添加、删除节点（IEF模式不支持添加、删除节点），添加、删除组织，共4种类型，每次操作只可以操作一种类型。此接口不支持包周期模式; 注意注册IEF节点时，IEF节点名称长度应该为4-24位的字符
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstance
        :type request: :class:`huaweicloudsdkbcs.v2.UpdateInstanceRequest`
        :rtype: :class:`huaweicloudsdkbcs.v2.UpdateInstanceResponse`
        """
        return self._update_instance_with_http_info(request)

    def _update_instance_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='UpdateInstanceResponse',
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
