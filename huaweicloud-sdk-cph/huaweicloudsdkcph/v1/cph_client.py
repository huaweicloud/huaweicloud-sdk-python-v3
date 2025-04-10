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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcph'")


class CphClient(Client):
    def __init__(self):
        super(CphClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcph.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CphClient":
                raise TypeError("client type error, support client type is CphClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_image_member(self, request):
        r"""共享镜像给指定账号

        镜像共享,共享镜像给指定账号。
        - 镜像只能共享给同region下的其他华为云账号(project_id)。
        - 同一镜像最多只能共享给10个其他账号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddImageMember
        :type request: :class:`huaweicloudsdkcph.v1.AddImageMemberRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.AddImageMemberResponse`
        """
        http_info = self._add_image_member_http_info(request)
        return self._call_api(**http_info)

    def add_image_member_invoker(self, request):
        http_info = self._add_image_member_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_image_member_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloud-phone/images/{image_id}/members",
            "request_type": request.__class__.__name__,
            "response_type": "AddImageMemberResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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

    def batch_create_tags(self, request):
        r"""批量添加标签

        批量添加标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateTags
        :type request: :class:`huaweicloudsdkcph.v1.BatchCreateTagsRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.BatchCreateTagsResponse`
        """
        http_info = self._batch_create_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_tags_invoker(self, request):
        http_info = self._batch_create_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{resource_type}/{resource_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateTagsResponse"
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

    def batch_delete_tags(self, request):
        r"""批量删除标签

        批量删除标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteTags
        :type request: :class:`huaweicloudsdkcph.v1.BatchDeleteTagsRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.BatchDeleteTagsResponse`
        """
        http_info = self._batch_delete_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_tags_invoker(self, request):
        http_info = self._batch_delete_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{resource_type}/{resource_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteTagsResponse"
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

    def batch_export_cloud_phone_data(self, request):
        r"""导出云手机数据

        批量导出云手机中的数据。该接口为异步接口。[接口调用前请先确保已完成CPH服务操作OBS桶的委托授权。委托CPH操作OBS桶请参见[委托CPH操作OBS桶](https://support.huaweicloud.com/bestpractice-cph/cph_bp_0050.html)。](tag:hws)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchExportCloudPhoneData
        :type request: :class:`huaweicloudsdkcph.v1.BatchExportCloudPhoneDataRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.BatchExportCloudPhoneDataResponse`
        """
        http_info = self._batch_export_cloud_phone_data_http_info(request)
        return self._call_api(**http_info)

    def batch_export_cloud_phone_data_invoker(self, request):
        http_info = self._batch_export_cloud_phone_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_export_cloud_phone_data_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloud-phone/phones/batch-storage",
            "request_type": request.__class__.__name__,
            "response_type": "BatchExportCloudPhoneDataResponse"
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

    def batch_import_cloud_phone_data(self, request):
        r"""恢复云手机数据

        批量恢复数据到云手机中。该接口为异步接口。[接口调用前请先确保已完成CPH服务操作OBS桶的委托授权。委托CPH操作OBS桶请参见[委托CPH操作OBS桶](https://support.huaweicloud.com/bestpractice-cph/cph_bp_0050.html)。](tag:hws)
        
        高版本手机导出的数据无法在低版本手机内恢复。低版本手机导出的数据可以在高版本手机内恢复，但可能会在极少数场景下有不兼容的风险。因此推荐您在同版本手机间进行导出与恢复。
        
        手机在运行状态会有数据缓存，直接运行恢复的文件可能带来访问失败、应用崩溃等现象，建议在还原成功后重启手机，以保证云手机稳定运行。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchImportCloudPhoneData
        :type request: :class:`huaweicloudsdkcph.v1.BatchImportCloudPhoneDataRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.BatchImportCloudPhoneDataResponse`
        """
        http_info = self._batch_import_cloud_phone_data_http_info(request)
        return self._call_api(**http_info)

    def batch_import_cloud_phone_data_invoker(self, request):
        http_info = self._batch_import_cloud_phone_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_import_cloud_phone_data_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloud-phone/phones/batch-restore",
            "request_type": request.__class__.__name__,
            "response_type": "BatchImportCloudPhoneDataResponse"
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

    def batch_show_phone_connect_infos(self, request):
        r"""获取云手机连接信息

        获取云手机连接信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchShowPhoneConnectInfos
        :type request: :class:`huaweicloudsdkcph.v1.BatchShowPhoneConnectInfosRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.BatchShowPhoneConnectInfosResponse`
        """
        http_info = self._batch_show_phone_connect_infos_http_info(request)
        return self._call_api(**http_info)

    def batch_show_phone_connect_infos_invoker(self, request):
        http_info = self._batch_show_phone_connect_infos_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_show_phone_connect_infos_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloud-phone/phones/batch-connection",
            "request_type": request.__class__.__name__,
            "response_type": "BatchShowPhoneConnectInfosResponse"
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

    def change_cloud_phone_server(self, request):
        r"""切换云手机服务器

        切换云手机服务器, 支持您换一台新的云手机服务器。切换后服务器名称、服务器ID和服务器所在AZ与原服务器相同, 服务器计费保持不变。服务器切换的同时服务器上的手机重新创建，不保留用户数据。切换需要额外的资源和资源配额。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeCloudPhoneServer
        :type request: :class:`huaweicloudsdkcph.v1.ChangeCloudPhoneServerRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ChangeCloudPhoneServerResponse`
        """
        http_info = self._change_cloud_phone_server_http_info(request)
        return self._call_api(**http_info)

    def change_cloud_phone_server_invoker(self, request):
        http_info = self._change_cloud_phone_server_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_cloud_phone_server_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cloud-phone/servers/{server_id}/change",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeCloudPhoneServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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

    def change_cloud_phone_server_model(self, request):
        r"""变更云手机服务器规格

        变更云手机服务器规格。接口调用成功后，大约2分钟左右规格会变更结束，在订单中心可以查看到变更的订单状态为成功，且查询服务器的详细信息，可以查看到服务器规格名称已经变成新的规格名称。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeCloudPhoneServerModel
        :type request: :class:`huaweicloudsdkcph.v1.ChangeCloudPhoneServerModelRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ChangeCloudPhoneServerModelResponse`
        """
        http_info = self._change_cloud_phone_server_model_http_info(request)
        return self._call_api(**http_info)

    def change_cloud_phone_server_model_invoker(self, request):
        http_info = self._change_cloud_phone_server_model_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_cloud_phone_server_model_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloud-phone/servers/change-server-model",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeCloudPhoneServerModelResponse"
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

    def create_cloud_phone_single_server(self, request):
        r"""创建云手机裸服务器

        该接口创建的服务器仅包含服务器和服务器的镜像，不包含云手机实例和镜像等内容。若需要创建包含云手机实例的服务器，请使用创建云手机服务器接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCloudPhoneSingleServer
        :type request: :class:`huaweicloudsdkcph.v1.CreateCloudPhoneSingleServerRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.CreateCloudPhoneSingleServerResponse`
        """
        http_info = self._create_cloud_phone_single_server_http_info(request)
        return self._call_api(**http_info)

    def create_cloud_phone_single_server_invoker(self, request):
        http_info = self._create_cloud_phone_single_server_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_cloud_phone_single_server_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.1/{project_id}/cloud-phone/servers",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCloudPhoneSingleServerResponse"
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

    def create_net2_cloud_phone_server(self, request):
        r"""[创建](tag:fcs)[购买](tag:hws,hws_hk,cmcc)云手机服务器

        [创建](tag:fcs)[购买](tag:hws,hws_hk,cmcc)云手机服务器，支持您复用已有的VPC网络管理云手机服务器，支持云手机服务器复用您已[创建](tag:fcs)[购买](tag:hws,hws_hk,cmcc)的共享带宽等资源。
        - 请确保您使用的账号具有CPH AgencyDependencyAccess权限。
        - 请确保您有足够的服务器及网络配额，配额校验不通过将导致创建失败。
        [- 当前只支持按需创建。](tag:fcs)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateNet2CloudPhoneServer
        :type request: :class:`huaweicloudsdkcph.v1.CreateNet2CloudPhoneServerRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.CreateNet2CloudPhoneServerResponse`
        """
        http_info = self._create_net2_cloud_phone_server_http_info(request)
        return self._call_api(**http_info)

    def create_net2_cloud_phone_server_invoker(self, request):
        http_info = self._create_net2_cloud_phone_server_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_net2_cloud_phone_server_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cloud-phone/servers",
            "request_type": request.__class__.__name__,
            "response_type": "CreateNet2CloudPhoneServerResponse"
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

    def delete_cloud_phone_server(self, request):
        r"""删除云手机服务器

        删除云手机服务器，仅可以删除按需购买的云手机服务器，最多删除十台。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCloudPhoneServer
        :type request: :class:`huaweicloudsdkcph.v1.DeleteCloudPhoneServerRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.DeleteCloudPhoneServerResponse`
        """
        http_info = self._delete_cloud_phone_server_http_info(request)
        return self._call_api(**http_info)

    def delete_cloud_phone_server_invoker(self, request):
        http_info = self._delete_cloud_phone_server_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_cloud_phone_server_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/cloud-phone/servers",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCloudPhoneServerResponse"
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

    def delete_image(self, request):
        r"""删除镜像

        删除自定义镜像
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteImage
        :type request: :class:`huaweicloudsdkcph.v1.DeleteImageRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.DeleteImageResponse`
        """
        http_info = self._delete_image_http_info(request)
        return self._call_api(**http_info)

    def delete_image_invoker(self, request):
        http_info = self._delete_image_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_image_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/cloud-phone/images/{image_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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

    def delete_image_member(self, request):
        r"""删除共享镜像

        删除共享镜像
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteImageMember
        :type request: :class:`huaweicloudsdkcph.v1.DeleteImageMemberRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.DeleteImageMemberResponse`
        """
        http_info = self._delete_image_member_http_info(request)
        return self._call_api(**http_info)

    def delete_image_member_invoker(self, request):
        http_info = self._delete_image_member_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_image_member_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/cloud-phone/images/{image_id}/members/{member_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteImageMemberResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']
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

    def delete_share_apps(self, request):
        r"""删除共享应用

        在共享应用存储目录中删除共享应用，该功能仅在支持共享应用的云手机规格上可实现。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteShareApps
        :type request: :class:`huaweicloudsdkcph.v1.DeleteShareAppsRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.DeleteShareAppsResponse`
        """
        http_info = self._delete_share_apps_http_info(request)
        return self._call_api(**http_info)

    def delete_share_apps_invoker(self, request):
        http_info = self._delete_share_apps_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_share_apps_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/cloud-phone/phones/share-apps",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteShareAppsResponse"
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

    def delete_share_files(self, request):
        r"""删除共享存储文件

        删除共享存储目录中文件，该功能仅在支持共享存储的云手机规格上可实现。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteShareFiles
        :type request: :class:`huaweicloudsdkcph.v1.DeleteShareFilesRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.DeleteShareFilesResponse`
        """
        http_info = self._delete_share_files_http_info(request)
        return self._call_api(**http_info)

    def delete_share_files_invoker(self, request):
        http_info = self._delete_share_files_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_share_files_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloud-phone/phones/share-files",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteShareFilesResponse"
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

    def expand_phone_data_volume_size(self, request):
        r"""扩容云手机数据盘大小

        扩容云手机数据盘大小
        - 注意: 本接口会产生扩容新增容量的费用，新增容量不算入服务器免费存储额度内。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExpandPhoneDataVolumeSize
        :type request: :class:`huaweicloudsdkcph.v1.ExpandPhoneDataVolumeSizeRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ExpandPhoneDataVolumeSizeResponse`
        """
        http_info = self._expand_phone_data_volume_size_http_info(request)
        return self._call_api(**http_info)

    def expand_phone_data_volume_size_invoker(self, request):
        http_info = self._expand_phone_data_volume_size_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _expand_phone_data_volume_size_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloud-phone/phones/expand-volume",
            "request_type": request.__class__.__name__,
            "response_type": "ExpandPhoneDataVolumeSizeResponse"
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

    def import_traffic(self, request):
        r"""云手机流量导流

        手机流量路由修改。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportTraffic
        :type request: :class:`huaweicloudsdkcph.v1.ImportTrafficRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ImportTrafficResponse`
        """
        http_info = self._import_traffic_http_info(request)
        return self._call_api(**http_info)

    def import_traffic_invoker(self, request):
        http_info = self._import_traffic_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_traffic_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloud-phone/phones-traffic",
            "request_type": request.__class__.__name__,
            "response_type": "ImportTrafficResponse"
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

    def list_cloud_phone_images(self, request):
        r"""查询手机镜像

        根据项目ID查询可用的手机镜像。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCloudPhoneImages
        :type request: :class:`huaweicloudsdkcph.v1.ListCloudPhoneImagesRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListCloudPhoneImagesResponse`
        """
        http_info = self._list_cloud_phone_images_http_info(request)
        return self._call_api(**http_info)

    def list_cloud_phone_images_invoker(self, request):
        http_info = self._list_cloud_phone_images_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_cloud_phone_images_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloud-phone/phone-images",
            "request_type": request.__class__.__name__,
            "response_type": "ListCloudPhoneImagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'image_type' in local_var_params:
            query_params.append(('image_type', local_var_params['image_type']))

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

    def list_cloud_phone_models(self, request):
        r"""查询云手机规格列表

        查询或统计云手机的规格列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCloudPhoneModels
        :type request: :class:`huaweicloudsdkcph.v1.ListCloudPhoneModelsRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListCloudPhoneModelsResponse`
        """
        http_info = self._list_cloud_phone_models_http_info(request)
        return self._call_api(**http_info)

    def list_cloud_phone_models_invoker(self, request):
        http_info = self._list_cloud_phone_models_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_cloud_phone_models_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloud-phone/phone-models",
            "request_type": request.__class__.__name__,
            "response_type": "ListCloudPhoneModelsResponse"
            }

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

    def list_cloud_phone_server_models(self, request):
        r"""查询云手机服务器规格列表

        查询云手机服务器的规格列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCloudPhoneServerModels
        :type request: :class:`huaweicloudsdkcph.v1.ListCloudPhoneServerModelsRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListCloudPhoneServerModelsResponse`
        """
        http_info = self._list_cloud_phone_server_models_http_info(request)
        return self._call_api(**http_info)

    def list_cloud_phone_server_models_invoker(self, request):
        http_info = self._list_cloud_phone_server_models_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_cloud_phone_server_models_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloud-phone/server-models",
            "request_type": request.__class__.__name__,
            "response_type": "ListCloudPhoneServerModelsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_type' in local_var_params:
            query_params.append(('product_type', local_var_params['product_type']))

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

    def list_cloud_phone_servers(self, request):
        r"""查询云手机服务器列表

        分页查询云手机服务器，云手机服务器列表按照创建时间进行降序排列。分页查询可以指定offset以及limit。如果不存在云手机服务器，则返回空列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCloudPhoneServers
        :type request: :class:`huaweicloudsdkcph.v1.ListCloudPhoneServersRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListCloudPhoneServersResponse`
        """
        http_info = self._list_cloud_phone_servers_http_info(request)
        return self._call_api(**http_info)

    def list_cloud_phone_servers_invoker(self, request):
        http_info = self._list_cloud_phone_servers_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_cloud_phone_servers_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloud-phone/servers",
            "request_type": request.__class__.__name__,
            "response_type": "ListCloudPhoneServersResponse"
            }

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
        if 'phone_model_name' in local_var_params:
            query_params.append(('phone_model_name', local_var_params['phone_model_name']))
        if 'create_since' in local_var_params:
            query_params.append(('create_since', local_var_params['create_since']))
        if 'create_until' in local_var_params:
            query_params.append(('create_until', local_var_params['create_until']))
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

    def list_cloud_phones(self, request):
        r"""查询云手机列表

        分页查询云手机，云手机列表按照创建时间进行降序排列。分页查询可以指定offset以及limit。如果不存在云手机，则返回空列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCloudPhones
        :type request: :class:`huaweicloudsdkcph.v1.ListCloudPhonesRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListCloudPhonesResponse`
        """
        http_info = self._list_cloud_phones_http_info(request)
        return self._call_api(**http_info)

    def list_cloud_phones_invoker(self, request):
        http_info = self._list_cloud_phones_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_cloud_phones_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloud-phone/phones",
            "request_type": request.__class__.__name__,
            "response_type": "ListCloudPhonesResponse"
            }

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

    def list_encode_servers(self, request):
        r"""查询编码服务

        查询编码服务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEncodeServers
        :type request: :class:`huaweicloudsdkcph.v1.ListEncodeServersRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListEncodeServersResponse`
        """
        http_info = self._list_encode_servers_http_info(request)
        return self._call_api(**http_info)

    def list_encode_servers_invoker(self, request):
        http_info = self._list_encode_servers_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_encode_servers_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloud-phone/encode-servers",
            "request_type": request.__class__.__name__,
            "response_type": "ListEncodeServersResponse"
            }

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

    def list_image_members(self, request):
        r"""获取镜像已共享账号列表

        获取镜像已共享账号列表
        - 路径中的project_id为共享账号的租户id
        - 路径中的image_id为共享账号的镜像id
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListImageMembers
        :type request: :class:`huaweicloudsdkcph.v1.ListImageMembersRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListImageMembersResponse`
        """
        http_info = self._list_image_members_http_info(request)
        return self._call_api(**http_info)

    def list_image_members_invoker(self, request):
        http_info = self._list_image_members_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_image_members_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloud-phone/images/{image_id}/members",
            "request_type": request.__class__.__name__,
            "response_type": "ListImageMembersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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

    def list_images(self, request):
        r"""查询自定义镜像列表

        查询自定义镜像列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListImages
        :type request: :class:`huaweicloudsdkcph.v1.ListImagesRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListImagesResponse`
        """
        http_info = self._list_images_http_info(request)
        return self._call_api(**http_info)

    def list_images_invoker(self, request):
        http_info = self._list_images_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_images_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloud-phone/images",
            "request_type": request.__class__.__name__,
            "response_type": "ListImagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'image_type' in local_var_params:
            query_params.append(('image_type', local_var_params['image_type']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'image_id' in local_var_params:
            query_params.append(('image_id', local_var_params['image_id']))
        if 'image_name' in local_var_params:
            query_params.append(('image_name', local_var_params['image_name']))
        if 'create_since' in local_var_params:
            query_params.append(('create_since', local_var_params['create_since']))
        if 'create_until' in local_var_params:
            query_params.append(('create_until', local_var_params['create_until']))
        if 'src_project_id' in local_var_params:
            query_params.append(('src_project_id', local_var_params['src_project_id']))

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

    def list_jobs(self, request):
        r"""查询任务执行状态列表

        查询同一个request id下的任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListJobs
        :type request: :class:`huaweicloudsdkcph.v1.ListJobsRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListJobsResponse`
        """
        http_info = self._list_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_jobs_invoker(self, request):
        http_info = self._list_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_jobs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloud-phone/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListJobsResponse"
            }

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

    def list_project_tags(self, request):
        r"""查询项目标签

        查询租户在指定区域和资源类型的所有标签集合。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectTags
        :type request: :class:`huaweicloudsdkcph.v1.ListProjectTagsRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListProjectTagsResponse`
        """
        http_info = self._list_project_tags_http_info(request)
        return self._call_api(**http_info)

    def list_project_tags_invoker(self, request):
        http_info = self._list_project_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_project_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/{resource_type}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectTagsResponse"
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

    def list_resource_instances(self, request):
        r"""查询资源实例

        查询资源实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceInstances
        :type request: :class:`huaweicloudsdkcph.v1.ListResourceInstancesRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListResourceInstancesResponse`
        """
        http_info = self._list_resource_instances_http_info(request)
        return self._call_api(**http_info)

    def list_resource_instances_invoker(self, request):
        http_info = self._list_resource_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_resource_instances_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{resource_type}/resource_instances/action",
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

    def list_resource_tags(self, request):
        r"""查询资源标签

        查询资源标签列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceTags
        :type request: :class:`huaweicloudsdkcph.v1.ListResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListResourceTagsResponse`
        """
        http_info = self._list_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def list_resource_tags_invoker(self, request):
        http_info = self._list_resource_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_resource_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/{resource_type}/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceTagsResponse"
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

    def list_share_files(self, request):
        r"""查询共享存储文件

        查询共享存储指定路径下的文件列表，该功能仅在支持共享存储的云手机规格上可实现。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListShareFiles
        :type request: :class:`huaweicloudsdkcph.v1.ListShareFilesRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListShareFilesResponse`
        """
        http_info = self._list_share_files_http_info(request)
        return self._call_api(**http_info)

    def list_share_files_invoker(self, request):
        http_info = self._list_share_files_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_share_files_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloud-phone/servers/share-files",
            "request_type": request.__class__.__name__,
            "response_type": "ListShareFilesResponse"
            }

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

    def push_share_apps(self, request):
        r"""推送共享应用

        推送应用tar文件至共享应用存储目录中，该功能仅在支持共享应用的云手机服务器上可实现。[接口调用前请先确保已完成CPH服务操作OBS桶的委托授权。委托CPH操作OBS桶请参见[委托CPH操作OBS桶](https://support.huaweicloud.com/bestpractice-cph/cph_bp_0050.html)。](tag:hws)
        
        注意：不能向存在低安卓版本云手机的服务器推送高安卓版本手机导出的应用包，否则可能会造成手机数据兼容性问题。如果您使用的是physical.kg1.4xlarge.a.cp服务器规格，请确保共享存储的可用空间大于两倍的tar包大小
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PushShareApps
        :type request: :class:`huaweicloudsdkcph.v1.PushShareAppsRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.PushShareAppsResponse`
        """
        http_info = self._push_share_apps_http_info(request)
        return self._call_api(**http_info)

    def push_share_apps_invoker(self, request):
        http_info = self._push_share_apps_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _push_share_apps_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloud-phone/phones/share-apps",
            "request_type": request.__class__.__name__,
            "response_type": "PushShareAppsResponse"
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

    def push_share_files(self, request):
        r"""推送共享存储文件

        推送文件至共享存储目录中，该功能仅在支持共享存储的云手机规格上可实现。[接口调用前请先确保已完成CPH服务操作OBS桶的委托授权。委托CPH操作OBS桶请参见[委托CPH操作OBS桶](https://support.huaweicloud.com/bestpractice-cph/cph_bp_0050.html)。](tag:hws)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PushShareFiles
        :type request: :class:`huaweicloudsdkcph.v1.PushShareFilesRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.PushShareFilesResponse`
        """
        http_info = self._push_share_files_http_info(request)
        return self._call_api(**http_info)

    def push_share_files_invoker(self, request):
        http_info = self._push_share_files_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _push_share_files_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloud-phone/phones/share-files",
            "request_type": request.__class__.__name__,
            "response_type": "PushShareFilesResponse"
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

    def reset_cloud_phone(self, request):
        r"""重置云手机

        批量重置云手机，将云手机恢复出厂设置。该接口为异步接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetCloudPhone
        :type request: :class:`huaweicloudsdkcph.v1.ResetCloudPhoneRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ResetCloudPhoneResponse`
        """
        http_info = self._reset_cloud_phone_http_info(request)
        return self._call_api(**http_info)

    def reset_cloud_phone_invoker(self, request):
        http_info = self._reset_cloud_phone_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_cloud_phone_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloud-phone/phones/batch-reset",
            "request_type": request.__class__.__name__,
            "response_type": "ResetCloudPhoneResponse"
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

    def restart_cloud_phone(self, request):
        r"""重启云手机

        批量重启云手机，也可用于开启云手机。该接口为异步接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestartCloudPhone
        :type request: :class:`huaweicloudsdkcph.v1.RestartCloudPhoneRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.RestartCloudPhoneResponse`
        """
        http_info = self._restart_cloud_phone_http_info(request)
        return self._call_api(**http_info)

    def restart_cloud_phone_invoker(self, request):
        http_info = self._restart_cloud_phone_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restart_cloud_phone_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloud-phone/phones/batch-restart",
            "request_type": request.__class__.__name__,
            "response_type": "RestartCloudPhoneResponse"
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

    def restart_cloud_phone_server(self, request):
        r"""重启云手机服务器

        批量重启云手机服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestartCloudPhoneServer
        :type request: :class:`huaweicloudsdkcph.v1.RestartCloudPhoneServerRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.RestartCloudPhoneServerResponse`
        """
        http_info = self._restart_cloud_phone_server_http_info(request)
        return self._call_api(**http_info)

    def restart_cloud_phone_server_invoker(self, request):
        http_info = self._restart_cloud_phone_server_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restart_cloud_phone_server_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloud-phone/servers/batch-restart",
            "request_type": request.__class__.__name__,
            "response_type": "RestartCloudPhoneServerResponse"
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

    def restart_encode_server(self, request):
        r"""重启编码服务

        批量重启编码服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestartEncodeServer
        :type request: :class:`huaweicloudsdkcph.v1.RestartEncodeServerRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.RestartEncodeServerResponse`
        """
        http_info = self._restart_encode_server_http_info(request)
        return self._call_api(**http_info)

    def restart_encode_server_invoker(self, request):
        http_info = self._restart_encode_server_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restart_encode_server_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloud-phone/encode-servers/batch-restart",
            "request_type": request.__class__.__name__,
            "response_type": "RestartEncodeServerResponse"
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

    def show_bandwidth_detail(self, request):
        r"""查询带宽信息

        查询云手机使用的带宽信息，本接口只适用于使用系统定义网络的服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBandwidthDetail
        :type request: :class:`huaweicloudsdkcph.v1.ShowBandwidthDetailRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ShowBandwidthDetailResponse`
        """
        http_info = self._show_bandwidth_detail_http_info(request)
        return self._call_api(**http_info)

    def show_bandwidth_detail_invoker(self, request):
        http_info = self._show_bandwidth_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_bandwidth_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloud-phone/bandwidths",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBandwidthDetailResponse"
            }

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

    def show_cloud_phone_detail(self, request):
        r"""查询云手机详情

        查询云手机的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCloudPhoneDetail
        :type request: :class:`huaweicloudsdkcph.v1.ShowCloudPhoneDetailRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ShowCloudPhoneDetailResponse`
        """
        http_info = self._show_cloud_phone_detail_http_info(request)
        return self._call_api(**http_info)

    def show_cloud_phone_detail_invoker(self, request):
        http_info = self._show_cloud_phone_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_cloud_phone_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloud-phone/phones/{phone_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCloudPhoneDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'phone_id' in local_var_params:
            path_params['phone_id'] = local_var_params['phone_id']

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

    def show_cloud_phone_server_detail(self, request):
        r"""查询云手机服务器详情

        根据server_id查询云手机服务器的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCloudPhoneServerDetail
        :type request: :class:`huaweicloudsdkcph.v1.ShowCloudPhoneServerDetailRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ShowCloudPhoneServerDetailResponse`
        """
        http_info = self._show_cloud_phone_server_detail_http_info(request)
        return self._call_api(**http_info)

    def show_cloud_phone_server_detail_invoker(self, request):
        http_info = self._show_cloud_phone_server_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_cloud_phone_server_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloud-phone/servers/{server_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCloudPhoneServerDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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

    def show_job(self, request):
        r"""查询任务执行状态

        查询任务的执行状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJob
        :type request: :class:`huaweicloudsdkcph.v1.ShowJobRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ShowJobResponse`
        """
        http_info = self._show_job_http_info(request)
        return self._call_api(**http_info)

    def show_job_invoker(self, request):
        http_info = self._show_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cloud-phone/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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

    def stop_cloud_phone(self, request):
        r"""关闭云手机

        批量关闭云手机。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopCloudPhone
        :type request: :class:`huaweicloudsdkcph.v1.StopCloudPhoneRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.StopCloudPhoneResponse`
        """
        http_info = self._stop_cloud_phone_http_info(request)
        return self._call_api(**http_info)

    def stop_cloud_phone_invoker(self, request):
        http_info = self._stop_cloud_phone_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_cloud_phone_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloud-phone/phones/batch-stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopCloudPhoneResponse"
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

    def update_bandwidth(self, request):
        r"""修改共享带宽

        修改云手机使用的共享带宽大小，本接口只适用于使用系统定义网络的服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateBandwidth
        :type request: :class:`huaweicloudsdkcph.v1.UpdateBandwidthRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.UpdateBandwidthResponse`
        """
        http_info = self._update_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def update_bandwidth_invoker(self, request):
        http_info = self._update_bandwidth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_bandwidth_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/cloud-phone/bandwidths/{band_width_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateBandwidthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'band_width_id' in local_var_params:
            path_params['band_width_id'] = local_var_params['band_width_id']

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

    def update_cloud_phone_property(self, request):
        r"""更新云手机属性

        部分云手机属性开放更新能力，部分属性无法更新，部分属性需要重启手机生效，属性约束请云手机属性列表。如果手机处于异常状态，属性更新后需恢复手机状态为运行中才可生效。该接口为异步接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCloudPhoneProperty
        :type request: :class:`huaweicloudsdkcph.v1.UpdateCloudPhonePropertyRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.UpdateCloudPhonePropertyResponse`
        """
        http_info = self._update_cloud_phone_property_http_info(request)
        return self._call_api(**http_info)

    def update_cloud_phone_property_invoker(self, request):
        http_info = self._update_cloud_phone_property_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_cloud_phone_property_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloud-phone/phones/batch-update-property",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCloudPhonePropertyResponse"
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

    def update_image_member(self, request):
        r"""更新共享镜像接受信息

        用户收到共享镜像后，选择接受或拒绝共享镜像。未接受的共享镜像无法使用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateImageMember
        :type request: :class:`huaweicloudsdkcph.v1.UpdateImageMemberRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.UpdateImageMemberResponse`
        """
        http_info = self._update_image_member_http_info(request)
        return self._call_api(**http_info)

    def update_image_member_invoker(self, request):
        http_info = self._update_image_member_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_image_member_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/cloud-phone/images/{image_id}/members",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateImageMemberResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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

    def update_keypair(self, request):
        r"""更改密钥对

        修改连接云手机的密钥对。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateKeypair
        :type request: :class:`huaweicloudsdkcph.v1.UpdateKeypairRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.UpdateKeypairResponse`
        """
        http_info = self._update_keypair_http_info(request)
        return self._call_api(**http_info)

    def update_keypair_invoker(self, request):
        http_info = self._update_keypair_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_keypair_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/cloud-phone/servers/open-access",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateKeypairResponse"
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

    def update_phone_name(self, request):
        r"""修改云手机名称

        根据phoneId修改phoneName。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePhoneName
        :type request: :class:`huaweicloudsdkcph.v1.UpdatePhoneNameRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.UpdatePhoneNameResponse`
        """
        http_info = self._update_phone_name_http_info(request)
        return self._call_api(**http_info)

    def update_phone_name_invoker(self, request):
        http_info = self._update_phone_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_phone_name_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/cloud-phone/phones/{phone_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePhoneNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'phone_id' in local_var_params:
            path_params['phone_id'] = local_var_params['phone_id']

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

    def update_server_name(self, request):
        r"""修改云手机服务器名称

        根据serverId修改serverName。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateServerName
        :type request: :class:`huaweicloudsdkcph.v1.UpdateServerNameRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.UpdateServerNameResponse`
        """
        http_info = self._update_server_name_http_info(request)
        return self._call_api(**http_info)

    def update_server_name_invoker(self, request):
        http_info = self._update_server_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_server_name_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/cloud-phone/servers/{server_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateServerNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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

    def install_apk(self, request):
        r"""安装apk

        在云手机中安装apk。系统会将指定的apk文件下载后直接安装到云手机中。
        支持安装单apk应用和多apk应用。可使用install命令安装单apk应用，一次只支持安装一个apk，如果一次传多个apk只有第一个安装成功；可使用install-multiple命令安装多apk应用（多apk应用为单个应用拆分成多个apk），一次只支持同一个应用的多个apk。该接口为异步接口。[接口调用前请先确保已完成CPH服务操作OBS桶的委托授权。委托CPH操作OBS桶请参见[委托CPH操作OBS桶](https://support.huaweicloud.com/bestpractice-cph/cph_bp_0050.html)。](tag:hws)
        - 管理面性能有限，对相同服务器批量执行的ADB命令，将会阻塞云手机其他任务执行。
        - 允许安装的apk大小限制为2G（即不可将obs桶内大于2G的apk安装到手机中），超过限制将返回错误。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for InstallApk
        :type request: :class:`huaweicloudsdkcph.v1.InstallApkRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.InstallApkResponse`
        """
        http_info = self._install_apk_http_info(request)
        return self._call_api(**http_info)

    def install_apk_invoker(self, request):
        http_info = self._install_apk_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _install_apk_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloud-phone/phones/commands",
            "request_type": request.__class__.__name__,
            "response_type": "InstallApkResponse"
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

    def push_file(self, request):
        r"""推送文件

        推送文件到云手机文件系统中。系统会将所指定的文件下载解压后，将解压后的内容全部推送到云手机的根目录下。只支持指定tar格式的文件进行推送，您需要将tar文件提前上传至您的OBS桶中。该接口为异步接口。[接口调用前请先确保已完成CPH服务操作OBS桶的委托授权。委托CPH操作OBS桶请参见[委托CPH操作OBS桶](https://support.huaweicloud.com/bestpractice-cph/cph_bp_0050.html)。](tag:hws)
        - 管理面性能有限，对相同服务器批量执行的ADB命令，将会阻塞云手机其他任务执行。
        - 允许推送的文件大小限制为6G（即不可将obs桶内大于6G的文件推送到手机中），超过限制将返回错误。
        - 手机的系统有限制，推送到系统盘不保证推送成功，推荐把文件推送到手机的数据盘。所以在构建\&quot;tar\&quot;文件时，应将待推送的文件放到本地创建的data目录后将其打包（如tar -cvf data.tar data ），以确保把文件推送到手机的数据盘下。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PushFile
        :type request: :class:`huaweicloudsdkcph.v1.PushFileRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.PushFileResponse`
        """
        http_info = self._push_file_http_info(request)
        return self._call_api(**http_info)

    def push_file_invoker(self, request):
        http_info = self._push_file_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _push_file_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloud-phone/phones/commands",
            "request_type": request.__class__.__name__,
            "response_type": "PushFileResponse"
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

    def run_shell_command(self, request):
        r"""异步执行adb命令

        在云手机中执行shell命令。该接口为异步接口。
        - 管理面性能有限，对相同服务器批量执行的ADB命令，将会阻塞云手机其他任务执行。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunShellCommand
        :type request: :class:`huaweicloudsdkcph.v1.RunShellCommandRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.RunShellCommandResponse`
        """
        http_info = self._run_shell_command_http_info(request)
        return self._call_api(**http_info)

    def run_shell_command_invoker(self, request):
        http_info = self._run_shell_command_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_shell_command_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloud-phone/phones/commands",
            "request_type": request.__class__.__name__,
            "response_type": "RunShellCommandResponse"
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

    def run_sync_command(self, request):
        r"""同步执行adb命令

        在云手机中同步执行命令并返回命令执行的输出信息，该接口仅支持adb shell命令的执行。1分钟内每个用户调用接口次数上限为6次，每个云手机允许执行命令超时时间为2秒，接口时间不超过30秒，执行云手机数越多，接口耗时相应越长。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunSyncCommand
        :type request: :class:`huaweicloudsdkcph.v1.RunSyncCommandRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.RunSyncCommandResponse`
        """
        http_info = self._run_sync_command_http_info(request)
        return self._call_api(**http_info)

    def run_sync_command_invoker(self, request):
        http_info = self._run_sync_command_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_sync_command_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloud-phone/phones/sync-commands",
            "request_type": request.__class__.__name__,
            "response_type": "RunSyncCommandResponse"
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

    def uninstall_apk(self, request):
        r"""卸载apk

        在云手机中卸载apk。该接口为异步接口。
        - 管理面性能有限，对相同服务器批量执行的ADB命令，将会阻塞云手机其他任务执行。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UninstallApk
        :type request: :class:`huaweicloudsdkcph.v1.UninstallApkRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.UninstallApkResponse`
        """
        http_info = self._uninstall_apk_http_info(request)
        return self._call_api(**http_info)

    def uninstall_apk_invoker(self, request):
        http_info = self._uninstall_apk_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _uninstall_apk_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cloud-phone/phones/commands",
            "request_type": request.__class__.__name__,
            "response_type": "UninstallApkResponse"
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
