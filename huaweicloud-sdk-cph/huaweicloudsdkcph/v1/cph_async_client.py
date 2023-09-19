# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class CphAsyncClient(Client):
    def __init__(self):
        super(CphAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcph.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "CphClient":
            raise TypeError("client type error, support client type is CphClient")

        return ClientBuilder(clazz)

    def batch_create_tags_async(self, request):
        """批量添加标签

        批量添加标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateTags
        :type request: :class:`huaweicloudsdkcph.v1.BatchCreateTagsRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.BatchCreateTagsResponse`
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
            resource_path='/v1/{project_id}/{resource_type}/{resource_id}/tags/action',
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

    def batch_delete_tags_async(self, request):
        """批量删除标签

        批量删除标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteTags
        :type request: :class:`huaweicloudsdkcph.v1.BatchDeleteTagsRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.BatchDeleteTagsResponse`
        """
        return self._batch_delete_tags_with_http_info(request)

    def _batch_delete_tags_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/{resource_type}/{resource_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_export_cloud_phone_data_async(self, request):
        """导出云手机数据

        批量导出云手机中的数据。该接口为异步接口。[接口调用前请先确保已完成CPH服务操作OBS桶的委托授权。委托CPH操作OBS桶请参见[委托CPH操作OBS桶](https://support.huaweicloud.com/bestpractice-cph/cph_bp_0050.html)。](tag:hws)[接口调用前请先确保已完成CPH服务操作OBS桶的委托授权。委托CPH操作OBS桶请参见[委托CPH操作OBS桶](https://support.huaweicloud.com/intl/zh-cn/bestpractice-cph/cph_bp_0050.html)。](tag:hws_hk)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchExportCloudPhoneData
        :type request: :class:`huaweicloudsdkcph.v1.BatchExportCloudPhoneDataRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.BatchExportCloudPhoneDataResponse`
        """
        return self._batch_export_cloud_phone_data_with_http_info(request)

    def _batch_export_cloud_phone_data_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cloud-phone/phones/batch-storage',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchExportCloudPhoneDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_import_cloud_phone_data_async(self, request):
        """恢复云手机数据

        批量恢复数据到云手机中。该接口为异步接口。[接口调用前请先确保已完成CPH服务操作OBS桶的委托授权。委托CPH操作OBS桶请参见[委托CPH操作OBS桶](https://support.huaweicloud.com/bestpractice-cph/cph_bp_0050.html)。](tag:hws)[接口调用前请先确保已完成CPH服务操作OBS桶的委托授权。委托CPH操作OBS桶请参见[委托CPH操作OBS桶](https://support.huaweicloud.com/intl/zh-cn/bestpractice-cph/cph_bp_0050.html)。](tag:hws_hk)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchImportCloudPhoneData
        :type request: :class:`huaweicloudsdkcph.v1.BatchImportCloudPhoneDataRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.BatchImportCloudPhoneDataResponse`
        """
        return self._batch_import_cloud_phone_data_with_http_info(request)

    def _batch_import_cloud_phone_data_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cloud-phone/phones/batch-restore',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchImportCloudPhoneDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_cloud_phone_server_model_async(self, request):
        """变更云手机服务器规格

        变更云手机服务器规格。变更的目标规格也必须为特殊的规格才可变更。接口调用成功后，大约2分钟左右规格会变更结束，在订单中心可以查看到变更的订单状态为成功，且查询服务器的详细信息，可以查看到服务器规格名称已经变成新的规格名称。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeCloudPhoneServerModel
        :type request: :class:`huaweicloudsdkcph.v1.ChangeCloudPhoneServerModelRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ChangeCloudPhoneServerModelResponse`
        """
        return self._change_cloud_phone_server_model_with_http_info(request)

    def _change_cloud_phone_server_model_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cloud-phone/servers/change-server-model',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeCloudPhoneServerModelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_net2_cloud_phone_server_async(self, request):
        """购买自定义网络云手机服务器

        购买自定义网络的云手机服务器。自定义网络是云手机全新一代网络配置管理模式，支持您复用已有的VPC网络管理云手机服务器，支持云手机服务器复用您已购买的共享带宽等资源。
        - 请确保您已具有虚拟私有云资源，创建服务器需要指定一个已有的虚拟私有云，否则无法创建服务器。
        - 请确保已正确创建委托（委托名称cph_admin_trust，委托服务CPH），委托未被删除， 确保委托包含VPC FullAccess权限，委托及权限校验失败将导致云服务器创建失败。创建委托时委托类型选择“云服务”，云服务选择“CPH”，即允许CPH调用云服务。
        - 请确保您使用的账号具有Security Administrator权限或者具备创建委托的细粒度权限iam:agencies:createAgency。
        - 请确保您有足够的服务器及网络配额，配额校验不通过将导致创建失败。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateNet2CloudPhoneServer
        :type request: :class:`huaweicloudsdkcph.v1.CreateNet2CloudPhoneServerRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.CreateNet2CloudPhoneServerResponse`
        """
        return self._create_net2_cloud_phone_server_with_http_info(request)

    def _create_net2_cloud_phone_server_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cloud-phone/servers',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateNet2CloudPhoneServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_share_apps_async(self, request):
        """删除共享应用

        在共享应用存储目录中删除共享应用，该功能仅在支持共享应用的云手机规格上可实现。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteShareApps
        :type request: :class:`huaweicloudsdkcph.v1.DeleteShareAppsRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.DeleteShareAppsResponse`
        """
        return self._delete_share_apps_with_http_info(request)

    def _delete_share_apps_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cloud-phone/phones/share-apps',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteShareAppsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_share_files_async(self, request):
        """删除共享存储文件

        删除共享存储目录中文件，该功能仅在支持共享存储的云手机规格上可实现。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteShareFiles
        :type request: :class:`huaweicloudsdkcph.v1.DeleteShareFilesRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.DeleteShareFilesResponse`
        """
        return self._delete_share_files_with_http_info(request)

    def _delete_share_files_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cloud-phone/phones/share-files',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteShareFilesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def import_traffic_async(self, request):
        """云手机流量导流

        手机流量路由修改。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportTraffic
        :type request: :class:`huaweicloudsdkcph.v1.ImportTrafficRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ImportTrafficResponse`
        """
        return self._import_traffic_with_http_info(request)

    def _import_traffic_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cloud-phone/phones-traffic',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ImportTrafficResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_cloud_phone_images_async(self, request):
        """查询手机镜像

        根据项目ID查询可用的手机镜像。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCloudPhoneImages
        :type request: :class:`huaweicloudsdkcph.v1.ListCloudPhoneImagesRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListCloudPhoneImagesResponse`
        """
        return self._list_cloud_phone_images_with_http_info(request)

    def _list_cloud_phone_images_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/cloud-phone/phone-images',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCloudPhoneImagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_cloud_phone_models_async(self, request):
        """查询云手机规格列表

        查询或统计云手机的规格列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCloudPhoneModels
        :type request: :class:`huaweicloudsdkcph.v1.ListCloudPhoneModelsRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListCloudPhoneModelsResponse`
        """
        return self._list_cloud_phone_models_with_http_info(request)

    def _list_cloud_phone_models_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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
            resource_path='/v1/{project_id}/cloud-phone/phone-models',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCloudPhoneModelsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_cloud_phone_server_models_async(self, request):
        """查询云手机服务器规格列表

        查询云手机服务器的规格列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCloudPhoneServerModels
        :type request: :class:`huaweicloudsdkcph.v1.ListCloudPhoneServerModelsRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListCloudPhoneServerModelsResponse`
        """
        return self._list_cloud_phone_server_models_with_http_info(request)

    def _list_cloud_phone_server_models_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_type' in local_var_params:
            query_params.append(('product_type', local_var_params['product_type']))

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
            resource_path='/v1/{project_id}/cloud-phone/server-models',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCloudPhoneServerModelsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_cloud_phone_servers_async(self, request):
        """查询云手机服务器列表

        分页查询云手机服务器，云手机服务器列表按照创建时间进行降序排列。分页查询可以指定offset以及limit。如果不存在云手机服务器，则返回空列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCloudPhoneServers
        :type request: :class:`huaweicloudsdkcph.v1.ListCloudPhoneServersRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListCloudPhoneServersResponse`
        """
        return self._list_cloud_phone_servers_with_http_info(request)

    def _list_cloud_phone_servers_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'server_name' in local_var_params:
            query_params.append(('server_name', local_var_params['server_name']))
        if 'server_id' in local_var_params:
            query_params.append(('server_id', local_var_params['server_id']))
        if 'network_version' in local_var_params:
            query_params.append(('network_version', local_var_params['network_version']))

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
            resource_path='/v1/{project_id}/cloud-phone/servers',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCloudPhoneServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_cloud_phones_async(self, request):
        """查询云手机列表

        分页查询云手机，云手机列表按照创建时间进行降序排列。分页查询可以指定offset以及limit。如果不存在云手机，则返回空列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCloudPhones
        :type request: :class:`huaweicloudsdkcph.v1.ListCloudPhonesRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListCloudPhonesResponse`
        """
        return self._list_cloud_phones_with_http_info(request)

    def _list_cloud_phones_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'phone_name' in local_var_params:
            query_params.append(('phone_name', local_var_params['phone_name']))
        if 'server_id' in local_var_params:
            query_params.append(('server_id', local_var_params['server_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

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
            resource_path='/v1/{project_id}/cloud-phone/phones',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCloudPhonesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_encode_servers_async(self, request):
        """查询编码服务

        查询编码服务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEncodeServers
        :type request: :class:`huaweicloudsdkcph.v1.ListEncodeServersRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListEncodeServersResponse`
        """
        return self._list_encode_servers_with_http_info(request)

    def _list_encode_servers_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'server_id' in local_var_params:
            query_params.append(('server_id', local_var_params['server_id']))

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
            resource_path='/v1/{project_id}/cloud-phone/encode-servers',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEncodeServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_jobs_async(self, request):
        """查询任务执行状态列表

        查询同一个request id下的任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListJobs
        :type request: :class:`huaweicloudsdkcph.v1.ListJobsRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListJobsResponse`
        """
        return self._list_jobs_with_http_info(request)

    def _list_jobs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'request_id' in local_var_params:
            query_params.append(('request_id', local_var_params['request_id']))
        if 'request_ids' in local_var_params:
            query_params.append(('request_ids', local_var_params['request_ids']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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
            resource_path='/v1/{project_id}/cloud-phone/jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_project_tags_async(self, request):
        """查询项目标签

        查询租户在指定区域和资源类型的所有标签集合。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectTags
        :type request: :class:`huaweicloudsdkcph.v1.ListProjectTagsRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListProjectTagsResponse`
        """
        return self._list_project_tags_with_http_info(request)

    def _list_project_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v1/{project_id}/{resource_type}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProjectTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_resource_instances_async(self, request):
        """查询资源实例

        查询资源实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResourceInstances
        :type request: :class:`huaweicloudsdkcph.v1.ListResourceInstancesRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListResourceInstancesResponse`
        """
        return self._list_resource_instances_with_http_info(request)

    def _list_resource_instances_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/{resource_type}/resource_instances/action',
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

    def list_resource_tags_async(self, request):
        """查询资源标签

        查询资源标签列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResourceTags
        :type request: :class:`huaweicloudsdkcph.v1.ListResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListResourceTagsResponse`
        """
        return self._list_resource_tags_with_http_info(request)

    def _list_resource_tags_with_http_info(self, request):
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
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/{resource_type}/{resource_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListResourceTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_share_files_async(self, request):
        """查询共享存储文件

        查询共享存储指定路径下的文件列表，该功能仅在支持共享存储的云手机规格上可实现。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListShareFiles
        :type request: :class:`huaweicloudsdkcph.v1.ListShareFilesRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListShareFilesResponse`
        """
        return self._list_share_files_with_http_info(request)

    def _list_share_files_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'server_ids' in local_var_params:
            query_params.append(('server_ids', local_var_params['server_ids']))
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))

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
            resource_path='/v1/{project_id}/cloud-phone/servers/share-files',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListShareFilesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def push_share_apps_async(self, request):
        """推送共享应用

        推送应用tar文件至共享应用存储目录中，该功能仅在支持共享应用的云手机规格上可实现。[接口调用前请先确保已完成CPH服务操作OBS桶的委托授权。委托CPH操作OBS桶请参见[委托CPH操作OBS桶](https://support.huaweicloud.com/bestpractice-cph/cph_bp_0050.html)。](tag:hws)[接口调用前请先确保已完成CPH服务操作OBS桶的委托授权。委托CPH操作OBS桶请参见[委托CPH操作OBS桶](https://support.huaweicloud.com/intl/zh-cn/bestpractice-cph/cph_bp_0050.html)。](tag:hws_hk)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PushShareApps
        :type request: :class:`huaweicloudsdkcph.v1.PushShareAppsRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.PushShareAppsResponse`
        """
        return self._push_share_apps_with_http_info(request)

    def _push_share_apps_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cloud-phone/phones/share-apps',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='PushShareAppsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def push_share_files_async(self, request):
        """推送共享存储文件

        推送文件至共享存储目录中，该功能仅在支持共享存储的云手机规格上可实现。[接口调用前请先确保已完成CPH服务操作OBS桶的委托授权。委托CPH操作OBS桶请参见[委托CPH操作OBS桶](https://support.huaweicloud.com/bestpractice-cph/cph_bp_0050.html)。](tag:hws)[接口调用前请先确保已完成CPH服务操作OBS桶的委托授权。委托CPH操作OBS桶请参见[委托CPH操作OBS桶](https://support.huaweicloud.com/intl/zh-cn/bestpractice-cph/cph_bp_0050.html)。](tag:hws_hk)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PushShareFiles
        :type request: :class:`huaweicloudsdkcph.v1.PushShareFilesRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.PushShareFilesResponse`
        """
        return self._push_share_files_with_http_info(request)

    def _push_share_files_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cloud-phone/phones/share-files',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='PushShareFilesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reset_cloud_phone_async(self, request):
        """重置云手机

        批量重置云手机，将云手机恢复出厂设置。该接口为异步接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetCloudPhone
        :type request: :class:`huaweicloudsdkcph.v1.ResetCloudPhoneRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ResetCloudPhoneResponse`
        """
        return self._reset_cloud_phone_with_http_info(request)

    def _reset_cloud_phone_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cloud-phone/phones/batch-reset',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResetCloudPhoneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restart_cloud_phone_async(self, request):
        """重启云手机

        批量重启云手机，也可用于开启云手机。该接口为异步接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestartCloudPhone
        :type request: :class:`huaweicloudsdkcph.v1.RestartCloudPhoneRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.RestartCloudPhoneResponse`
        """
        return self._restart_cloud_phone_with_http_info(request)

    def _restart_cloud_phone_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cloud-phone/phones/batch-restart',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RestartCloudPhoneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restart_cloud_phone_server_async(self, request):
        """重启云手机服务器

        批量重启云手机服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestartCloudPhoneServer
        :type request: :class:`huaweicloudsdkcph.v1.RestartCloudPhoneServerRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.RestartCloudPhoneServerResponse`
        """
        return self._restart_cloud_phone_server_with_http_info(request)

    def _restart_cloud_phone_server_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cloud-phone/servers/batch-restart',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RestartCloudPhoneServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restart_encode_server_async(self, request):
        """重启编码服务

        批量重启编码服务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestartEncodeServer
        :type request: :class:`huaweicloudsdkcph.v1.RestartEncodeServerRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.RestartEncodeServerResponse`
        """
        return self._restart_encode_server_with_http_info(request)

    def _restart_encode_server_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cloud-phone/encode-servers/batch-restart',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RestartEncodeServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_bandwidth_detail_async(self, request):
        """查询带宽信息

        查询云手机使用的带宽信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBandwidthDetail
        :type request: :class:`huaweicloudsdkcph.v1.ShowBandwidthDetailRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ShowBandwidthDetailResponse`
        """
        return self._show_bandwidth_detail_with_http_info(request)

    def _show_bandwidth_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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
            resource_path='/v1/{project_id}/cloud-phone/bandwidths',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowBandwidthDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_cloud_phone_detail_async(self, request):
        """查询云手机详情

        查询云手机的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCloudPhoneDetail
        :type request: :class:`huaweicloudsdkcph.v1.ShowCloudPhoneDetailRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ShowCloudPhoneDetailResponse`
        """
        return self._show_cloud_phone_detail_with_http_info(request)

    def _show_cloud_phone_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'phone_id' in local_var_params:
            path_params['phone_id'] = local_var_params['phone_id']

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
            resource_path='/v1/{project_id}/cloud-phone/phones/{phone_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCloudPhoneDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_cloud_phone_server_detail_async(self, request):
        """查询云手机服务器详情

        根据server_id查询云手机服务器的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCloudPhoneServerDetail
        :type request: :class:`huaweicloudsdkcph.v1.ShowCloudPhoneServerDetailRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ShowCloudPhoneServerDetailResponse`
        """
        return self._show_cloud_phone_server_detail_with_http_info(request)

    def _show_cloud_phone_server_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloud-phone/servers/{server_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCloudPhoneServerDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job_async(self, request):
        """查询任务执行状态

        查询任务的执行状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJob
        :type request: :class:`huaweicloudsdkcph.v1.ShowJobRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ShowJobResponse`
        """
        return self._show_job_with_http_info(request)

    def _show_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1/{project_id}/cloud-phone/jobs/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_cloud_phone_async(self, request):
        """关闭云手机

        批量关闭云手机。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopCloudPhone
        :type request: :class:`huaweicloudsdkcph.v1.StopCloudPhoneRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.StopCloudPhoneResponse`
        """
        return self._stop_cloud_phone_with_http_info(request)

    def _stop_cloud_phone_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cloud-phone/phones/batch-stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopCloudPhoneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_bandwidth_async(self, request):
        """修改共享带宽

        修改云手机使用的共享带宽大小。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateBandwidth
        :type request: :class:`huaweicloudsdkcph.v1.UpdateBandwidthRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.UpdateBandwidthResponse`
        """
        return self._update_bandwidth_with_http_info(request)

    def _update_bandwidth_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'band_width_id' in local_var_params:
            path_params['band_width_id'] = local_var_params['band_width_id']

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
            resource_path='/v1/{project_id}/cloud-phone/bandwidths/{band_width_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateBandwidthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_cloud_phone_property_async(self, request):
        """更新云手机属性

        部分云手机属性开放更新能力，部分属性无法更新，部分属性需要重启手机生效，属性约束请云手机属性列表。如果手机处于异常状态，属性更新后需恢复手机状态为运行中才可生效。该接口为异步接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCloudPhoneProperty
        :type request: :class:`huaweicloudsdkcph.v1.UpdateCloudPhonePropertyRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.UpdateCloudPhonePropertyResponse`
        """
        return self._update_cloud_phone_property_with_http_info(request)

    def _update_cloud_phone_property_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cloud-phone/phones/batch-update-property',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateCloudPhonePropertyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_keypair_async(self, request):
        """更改密钥对

        修改连接云手机的密钥对。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateKeypair
        :type request: :class:`huaweicloudsdkcph.v1.UpdateKeypairRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.UpdateKeypairResponse`
        """
        return self._update_keypair_with_http_info(request)

    def _update_keypair_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cloud-phone/servers/open-access',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateKeypairResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_phone_name_async(self, request):
        """修改云手机名称

        根据phoneId修改phoneName。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePhoneName
        :type request: :class:`huaweicloudsdkcph.v1.UpdatePhoneNameRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.UpdatePhoneNameResponse`
        """
        return self._update_phone_name_with_http_info(request)

    def _update_phone_name_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'phone_id' in local_var_params:
            path_params['phone_id'] = local_var_params['phone_id']

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
            resource_path='/v1/{project_id}/cloud-phone/phones/{phone_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePhoneNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_server_name_async(self, request):
        """修改云手机服务器名称

        根据serverId修改serverName。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateServerName
        :type request: :class:`huaweicloudsdkcph.v1.UpdateServerNameRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.UpdateServerNameResponse`
        """
        return self._update_server_name_with_http_info(request)

    def _update_server_name_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloud-phone/servers/{server_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateServerNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def install_apk_async(self, request):
        """安装apk

        在云手机中安装apk。系统会将指定的apk文件下载后直接安装到云手机中。
        支持安装单apk应用和多apk应用。可使用install命令安装单apk应用，一次只支持安装一个apk；可使用install-multiple命令安装多apk应用（多apk应用为单个应用拆分成多个apk），一次只支持同一个应用的多个apk。该接口为异步接口。[接口调用前请先确保已完成CPH服务操作OBS桶的委托授权。委托CPH操作OBS桶请参见[委托CPH操作OBS桶](https://support.huaweicloud.com/bestpractice-cph/cph_bp_0050.html)。](tag:hws)[接口调用前请先确保已完成CPH服务操作OBS桶的委托授权。委托CPH操作OBS桶请参见[委托CPH操作OBS桶](https://support.huaweicloud.com/intl/zh-cn/bestpractice-cph/cph_bp_0050.html)。](tag:hws_hk)
        - 管理面性能有限，对相同服务器批量执行的ADB命令，将会阻塞云手机其他任务执行。
        - 建议通过开发应用市场的方式安装apk。允许安装的apk大小限制为2G（即不可将obs桶内大于2G的apk安装到手机中），超过限制将返回错误。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for InstallApk
        :type request: :class:`huaweicloudsdkcph.v1.InstallApkRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.InstallApkResponse`
        """
        return self._install_apk_with_http_info(request)

    def _install_apk_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cloud-phone/phones/commands',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='InstallApkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def push_file_async(self, request):
        """推送文件

        推送文件到云手机文件系统中。系统会将所指定的文件下载解压后，将解压后的内容全部推送到云手机的根目录下。只支持指定tar格式的文件进行推送，您需要将tar文件提前上传至您的OBS桶中。该接口为异步接口。[接口调用前请先确保已完成CPH服务操作OBS桶的委托授权。委托CPH操作OBS桶请参见[委托CPH操作OBS桶](https://support.huaweicloud.com/bestpractice-cph/cph_bp_0050.html)。](tag:hws)[接口调用前请先确保已完成CPH服务操作OBS桶的委托授权。委托CPH操作OBS桶请参见[委托CPH操作OBS桶](https://support.huaweicloud.com/intl/zh-cn/bestpractice-cph/cph_bp_0050.html)。](tag:hws_hk)
        - 管理面性能有限，对相同服务器批量执行的ADB命令，将会阻塞云手机其他任务执行。
        - 允许推送的文件大小限制为6G（即不可将obs桶内大于6G的文件推送到手机中），超过限制将返回错误。
        - 手机的系统有限制，推送到系统盘不保证推送成功，推荐把文件推送到手机的数据盘。所以在构建\&quot;tar\&quot;文件时，应将待推送的文件放到本地创建的data目录后将其打包（如tar -cvf data.tar data ），以确保把文件推送到手机的数据盘下。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PushFile
        :type request: :class:`huaweicloudsdkcph.v1.PushFileRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.PushFileResponse`
        """
        return self._push_file_with_http_info(request)

    def _push_file_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cloud-phone/phones/commands',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='PushFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_shell_command_async(self, request):
        """执行异步adb命令

        在云手机中执行shell命令。该接口为异步接口。
        - 管理面性能有限，对相同服务器批量执行的ADB命令，将会阻塞云手机其他任务执行。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunShellCommand
        :type request: :class:`huaweicloudsdkcph.v1.RunShellCommandRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.RunShellCommandResponse`
        """
        return self._run_shell_command_with_http_info(request)

    def _run_shell_command_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cloud-phone/phones/commands',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunShellCommandResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_sync_command_async(self, request):
        """执行同步adb命令

        在云手机中同步执行命令并返回命令执行的输出信息，该接口仅支持adb shell命令的执行。1分钟内每个用户调用接口次数上限为6次，每个云手机允许执行命令超时时间为2秒，接口时间不超过30秒，执行云手机数越多，接口耗时相应越长。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunSyncCommand
        :type request: :class:`huaweicloudsdkcph.v1.RunSyncCommandRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.RunSyncCommandResponse`
        """
        return self._run_sync_command_with_http_info(request)

    def _run_sync_command_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cloud-phone/phones/sync-commands',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunSyncCommandResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def uninstall_apk_async(self, request):
        """卸载apk

        在云手机中卸载apk。该接口为异步接口。
        - 管理面性能有限，对相同服务器批量执行的ADB命令，将会阻塞云手机其他任务执行。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UninstallApk
        :type request: :class:`huaweicloudsdkcph.v1.UninstallApkRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.UninstallApkResponse`
        """
        return self._uninstall_apk_with_http_info(request)

    def _uninstall_apk_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cloud-phone/phones/commands',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UninstallApkResponse',
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
