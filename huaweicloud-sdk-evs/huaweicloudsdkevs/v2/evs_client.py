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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkevs'")


class EvsClient(Client):
    def __init__(self):
        super(EvsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkevs.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "EvsClient":
                raise TypeError("client type error, support client type is EvsClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_create_volume_tags(self, request):
        r"""为指定云硬盘批量添加标签

        为指定云硬盘批量添加标签。
        
        添加标签时，如果云硬盘的标签已存在相同key，则会覆盖已有标签。
        单个云硬盘最多支持创建10个标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateVolumeTags
        :type request: :class:`huaweicloudsdkevs.v2.BatchCreateVolumeTagsRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.BatchCreateVolumeTagsResponse`
        """
        http_info = self._batch_create_volume_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_volume_tags_invoker(self, request):
        http_info = self._batch_create_volume_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_volume_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cloudvolumes/{volume_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateVolumeTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

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

    def batch_delete_volume_tags(self, request):
        r"""为指定云硬盘批量删除标签

        为指定云硬盘批量删除标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteVolumeTags
        :type request: :class:`huaweicloudsdkevs.v2.BatchDeleteVolumeTagsRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.BatchDeleteVolumeTagsResponse`
        """
        http_info = self._batch_delete_volume_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_volume_tags_invoker(self, request):
        http_info = self._batch_delete_volume_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_volume_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cloudvolumes/{volume_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteVolumeTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

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

    def batch_resize_volumes(self, request):
        r"""批量扩容云硬盘

        对按需或者包周期云硬盘进行批量扩容。
        [在批量扩容存在包周期云硬盘的场景下：](tag:hws)
        - [如果您需要查看订单可用的优惠券，请参考\&quot;[查询订单可用优惠券](https://support.huaweicloud.com/api-oce/zh-cn_topic_0092953630.html)\&quot;。](tag:hws)
        - [如果您需要支付订单，请参考\&quot;[支付包周期产品订单](https://support.huaweicloud.com/api-oce/api_order_00030.html)\&quot;。](tag:hws)
        - [如果您需要退订该包周期资源，请参考“[退订包周期资源](https://support.huaweicloud.com/api-oce/zh-cn_topic_0082522030.html)”。](tag:hws)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchResizeVolumes
        :type request: :class:`huaweicloudsdkevs.v2.BatchResizeVolumesRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.BatchResizeVolumesResponse`
        """
        http_info = self._batch_resize_volumes_http_info(request)
        return self._call_api(**http_info)

    def batch_resize_volumes_invoker(self, request):
        http_info = self._batch_resize_volumes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_resize_volumes_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/volumes/batch-extend",
            "request_type": request.__class__.__name__,
            "response_type": "BatchResizeVolumesResponse"
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

    def cinder_accept_volume_transfer(self, request):
        r"""接受云硬盘过户

        通过云硬盘过户记录ID以及身份认证密钥来接受云硬盘过户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CinderAcceptVolumeTransfer
        :type request: :class:`huaweicloudsdkevs.v2.CinderAcceptVolumeTransferRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.CinderAcceptVolumeTransferResponse`
        """
        http_info = self._cinder_accept_volume_transfer_http_info(request)
        return self._call_api(**http_info)

    def cinder_accept_volume_transfer_invoker(self, request):
        http_info = self._cinder_accept_volume_transfer_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cinder_accept_volume_transfer_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/os-volume-transfer/{transfer_id}/accept",
            "request_type": request.__class__.__name__,
            "response_type": "CinderAcceptVolumeTransferResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'transfer_id' in local_var_params:
            path_params['transfer_id'] = local_var_params['transfer_id']

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

    def cinder_create_volume_transfer(self, request):
        r"""创建云硬盘过户

        指定云硬盘来创建云硬盘过户记录，创建成功后，会返回过户记录ID以及身份认证密钥。
        云硬盘在过户过程中的状态变化如下：创建云硬盘过户后，云硬盘状态由“available”变为“awaiting-transfer”。当云硬盘过户被接收后，云硬盘状态变为“available”。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CinderCreateVolumeTransfer
        :type request: :class:`huaweicloudsdkevs.v2.CinderCreateVolumeTransferRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.CinderCreateVolumeTransferResponse`
        """
        http_info = self._cinder_create_volume_transfer_http_info(request)
        return self._call_api(**http_info)

    def cinder_create_volume_transfer_invoker(self, request):
        http_info = self._cinder_create_volume_transfer_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cinder_create_volume_transfer_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/os-volume-transfer",
            "request_type": request.__class__.__name__,
            "response_type": "CinderCreateVolumeTransferResponse"
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

    def cinder_delete_volume_transfer(self, request):
        r"""删除云硬盘过户

        当云硬盘过户未被接受时，您可以删除云硬盘过户记录，接受后则无法执行删除操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CinderDeleteVolumeTransfer
        :type request: :class:`huaweicloudsdkevs.v2.CinderDeleteVolumeTransferRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.CinderDeleteVolumeTransferResponse`
        """
        http_info = self._cinder_delete_volume_transfer_http_info(request)
        return self._call_api(**http_info)

    def cinder_delete_volume_transfer_invoker(self, request):
        http_info = self._cinder_delete_volume_transfer_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cinder_delete_volume_transfer_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/os-volume-transfer/{transfer_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CinderDeleteVolumeTransferResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'transfer_id' in local_var_params:
            path_params['transfer_id'] = local_var_params['transfer_id']

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

    def cinder_list_availability_zones(self, request):
        r"""查询所有的可用分区信息

        查询所有的可用分区信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CinderListAvailabilityZones
        :type request: :class:`huaweicloudsdkevs.v2.CinderListAvailabilityZonesRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.CinderListAvailabilityZonesResponse`
        """
        http_info = self._cinder_list_availability_zones_http_info(request)
        return self._call_api(**http_info)

    def cinder_list_availability_zones_invoker(self, request):
        http_info = self._cinder_list_availability_zones_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cinder_list_availability_zones_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/os-availability-zone",
            "request_type": request.__class__.__name__,
            "response_type": "CinderListAvailabilityZonesResponse"
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

    def cinder_list_quotas(self, request):
        r"""查询租户的详细配额

        查询租户的详细配额。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CinderListQuotas
        :type request: :class:`huaweicloudsdkevs.v2.CinderListQuotasRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.CinderListQuotasResponse`
        """
        http_info = self._cinder_list_quotas_http_info(request)
        return self._call_api(**http_info)

    def cinder_list_quotas_invoker(self, request):
        http_info = self._cinder_list_quotas_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cinder_list_quotas_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/os-quota-sets/{target_project_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CinderListQuotasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'target_project_id' in local_var_params:
            path_params['target_project_id'] = local_var_params['target_project_id']

        query_params = []
        if 'usage' in local_var_params:
            query_params.append(('usage', local_var_params['usage']))

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

    def cinder_list_volume_transfers(self, request):
        r"""查询云硬盘过户记录列表概要

        查询当前租户下所有云硬盘的过户记录列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CinderListVolumeTransfers
        :type request: :class:`huaweicloudsdkevs.v2.CinderListVolumeTransfersRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.CinderListVolumeTransfersResponse`
        """
        http_info = self._cinder_list_volume_transfers_http_info(request)
        return self._call_api(**http_info)

    def cinder_list_volume_transfers_invoker(self, request):
        http_info = self._cinder_list_volume_transfers_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cinder_list_volume_transfers_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/os-volume-transfer",
            "request_type": request.__class__.__name__,
            "response_type": "CinderListVolumeTransfersResponse"
            }

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

    def cinder_list_volume_types(self, request):
        r"""查询云硬盘类型列表

        查询云硬盘类型列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CinderListVolumeTypes
        :type request: :class:`huaweicloudsdkevs.v2.CinderListVolumeTypesRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.CinderListVolumeTypesResponse`
        """
        http_info = self._cinder_list_volume_types_http_info(request)
        return self._call_api(**http_info)

    def cinder_list_volume_types_invoker(self, request):
        http_info = self._cinder_list_volume_types_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cinder_list_volume_types_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/types",
            "request_type": request.__class__.__name__,
            "response_type": "CinderListVolumeTypesResponse"
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

    def cinder_show_volume_transfer(self, request):
        r"""查询单个云硬盘过户记录详情

        查询单个云硬盘的过户记录详情，比如过户记录创建时间、ID以及名称等信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CinderShowVolumeTransfer
        :type request: :class:`huaweicloudsdkevs.v2.CinderShowVolumeTransferRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.CinderShowVolumeTransferResponse`
        """
        http_info = self._cinder_show_volume_transfer_http_info(request)
        return self._call_api(**http_info)

    def cinder_show_volume_transfer_invoker(self, request):
        http_info = self._cinder_show_volume_transfer_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cinder_show_volume_transfer_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/os-volume-transfer/{transfer_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CinderShowVolumeTransferResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'transfer_id' in local_var_params:
            path_params['transfer_id'] = local_var_params['transfer_id']

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

    def create_snapshot(self, request):
        r"""创建云硬盘快照

        创建云硬盘快照。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSnapshot
        :type request: :class:`huaweicloudsdkevs.v2.CreateSnapshotRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.CreateSnapshotResponse`
        """
        http_info = self._create_snapshot_http_info(request)
        return self._call_api(**http_info)

    def create_snapshot_invoker(self, request):
        http_info = self._create_snapshot_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_snapshot_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cloudsnapshots",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSnapshotResponse"
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

    def create_volume(self, request):
        r"""创建云硬盘

        创建按需或包周期云硬盘。
        在创建包周期云硬盘的场景下：
        - 如果您需要查看订单可用的优惠券，请参考\&quot;[查询订单可用优惠券](https://support.huaweicloud.com/api-oce/zh-cn_topic_0092953630.html)\&quot;。
        - 如果您需要支付订单，请参考\&quot;[支付包周期产品订单](https://support.huaweicloud.com/api-oce/zh-cn_topic_0075746561.html)\&quot;。
        - 如果您需要查询订单的资源开通详情，请参考\&quot;[查询订单的资源开通详情](https://support.huaweicloud.com/api-oce/api_order_00001.html)\&quot;。
        - 如果您需要退订该包周期资源，请参考“[退订包周期资源](https://support.huaweicloud.com/api-oce/zh-cn_topic_0082522030.html)”。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateVolume
        :type request: :class:`huaweicloudsdkevs.v2.CreateVolumeRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.CreateVolumeResponse`
        """
        http_info = self._create_volume_http_info(request)
        return self._call_api(**http_info)

    def create_volume_invoker(self, request):
        http_info = self._create_volume_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_volume_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.1/{project_id}/cloudvolumes",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVolumeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_client_token' in local_var_params:
            header_params['X-Client-Token'] = local_var_params['x_client_token']

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

    def delete_snapshot(self, request):
        r"""删除云硬盘快照

        删除云硬盘快照。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSnapshot
        :type request: :class:`huaweicloudsdkevs.v2.DeleteSnapshotRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.DeleteSnapshotResponse`
        """
        http_info = self._delete_snapshot_http_info(request)
        return self._call_api(**http_info)

    def delete_snapshot_invoker(self, request):
        http_info = self._delete_snapshot_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_snapshot_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/cloudsnapshots/{snapshot_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSnapshotResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'snapshot_id' in local_var_params:
            path_params['snapshot_id'] = local_var_params['snapshot_id']

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

    def delete_volume(self, request):
        r"""删除云硬盘

        删除一个云硬盘。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteVolume
        :type request: :class:`huaweicloudsdkevs.v2.DeleteVolumeRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.DeleteVolumeResponse`
        """
        http_info = self._delete_volume_http_info(request)
        return self._call_api(**http_info)

    def delete_volume_invoker(self, request):
        http_info = self._delete_volume_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_volume_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/cloudvolumes/{volume_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVolumeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

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

    def list_snapshots(self, request):
        r"""查询云硬盘快照详情列表

        查询云硬盘快照详细列表信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSnapshots
        :type request: :class:`huaweicloudsdkevs.v2.ListSnapshotsRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.ListSnapshotsResponse`
        """
        http_info = self._list_snapshots_http_info(request)
        return self._call_api(**http_info)

    def list_snapshots_invoker(self, request):
        http_info = self._list_snapshots_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_snapshots_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cloudsnapshots/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ListSnapshotsResponse"
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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'volume_id' in local_var_params:
            query_params.append(('volume_id', local_var_params['volume_id']))
        if 'availability_zone' in local_var_params:
            query_params.append(('availability_zone', local_var_params['availability_zone']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'dedicated_storage_name' in local_var_params:
            query_params.append(('dedicated_storage_name', local_var_params['dedicated_storage_name']))
        if 'dedicated_storage_id' in local_var_params:
            query_params.append(('dedicated_storage_id', local_var_params['dedicated_storage_id']))
        if 'service_type' in local_var_params:
            query_params.append(('service_type', local_var_params['service_type']))
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

    def list_volume_tags(self, request):
        r"""获取云硬盘资源的所有标签

        获取某个租户的所有云硬盘资源的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVolumeTags
        :type request: :class:`huaweicloudsdkevs.v2.ListVolumeTagsRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.ListVolumeTagsResponse`
        """
        http_info = self._list_volume_tags_http_info(request)
        return self._call_api(**http_info)

    def list_volume_tags_invoker(self, request):
        http_info = self._list_volume_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_volume_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cloudvolumes/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListVolumeTagsResponse"
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

    def list_volumes(self, request):
        r"""查询所有云硬盘详情

        查询所有云硬盘的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVolumes
        :type request: :class:`huaweicloudsdkevs.v2.ListVolumesRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.ListVolumesResponse`
        """
        http_info = self._list_volumes_http_info(request)
        return self._call_api(**http_info)

    def list_volumes_invoker(self, request):
        http_info = self._list_volumes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_volumes_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cloudvolumes/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ListVolumesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'metadata' in local_var_params:
            query_params.append(('metadata', local_var_params['metadata']))
        if 'availability_zone' in local_var_params:
            query_params.append(('availability_zone', local_var_params['availability_zone']))
        if 'multiattach' in local_var_params:
            query_params.append(('multiattach', local_var_params['multiattach']))
        if 'service_type' in local_var_params:
            query_params.append(('service_type', local_var_params['service_type']))
        if 'dedicated_storage_id' in local_var_params:
            query_params.append(('dedicated_storage_id', local_var_params['dedicated_storage_id']))
        if 'dedicated_storage_name' in local_var_params:
            query_params.append(('dedicated_storage_name', local_var_params['dedicated_storage_name']))
        if 'volume_type_id' in local_var_params:
            query_params.append(('volume_type_id', local_var_params['volume_type_id']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'ids' in local_var_params:
            query_params.append(('ids', local_var_params['ids']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'server_id' in local_var_params:
            query_params.append(('server_id', local_var_params['server_id']))
        if 'not_metadata' in local_var_params:
            query_params.append(('not_metadata', local_var_params['not_metadata']))

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

    def list_volumes_by_tags(self, request):
        r"""通过标签查询云硬盘资源实例详情

        通过标签查询云硬盘资源实例详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVolumesByTags
        :type request: :class:`huaweicloudsdkevs.v2.ListVolumesByTagsRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.ListVolumesByTagsResponse`
        """
        http_info = self._list_volumes_by_tags_http_info(request)
        return self._call_api(**http_info)

    def list_volumes_by_tags_invoker(self, request):
        http_info = self._list_volumes_by_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_volumes_by_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cloudvolumes/resource_instances/action",
            "request_type": request.__class__.__name__,
            "response_type": "ListVolumesByTagsResponse"
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

    def modify_volume_qo_s(self, request):
        r"""修改云硬盘QoS

        调整云硬盘的iops或者吞吐量。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyVolumeQoS
        :type request: :class:`huaweicloudsdkevs.v2.ModifyVolumeQoSRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.ModifyVolumeQoSResponse`
        """
        http_info = self._modify_volume_qo_s_http_info(request)
        return self._call_api(**http_info)

    def modify_volume_qo_s_invoker(self, request):
        http_info = self._modify_volume_qo_s_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_volume_qo_s_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/cloudvolumes/{volume_id}/qos",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyVolumeQoSResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

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

    def resize_volume(self, request):
        r"""扩容云硬盘

        对按需或者包周期云硬盘进行扩容。
        在扩容包周期云硬盘的场景下：
        - 如果您需要查看订单可用的优惠券，请参考\&quot;[查询订单可用优惠券](https://support.huaweicloud.com/api-oce/zh-cn_topic_0092953630.html)\&quot;。
        - 如果您需要支付订单，请参考\&quot;[支付包周期产品订单](https://support.huaweicloud.com/api-oce/zh-cn_topic_0075746561.html)\&quot;。
        - 如果您需要查询订单的资源开通详情，请参考\&quot;[查询订单的资源开通详情](https://support.huaweicloud.com/api-oce/api_order_00001.html)\&quot;。
        - 如果您需要退订该包周期资源，请参考“[退订包周期资源](https://support.huaweicloud.com/api-oce/zh-cn_topic_0082522030.html)”。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResizeVolume
        :type request: :class:`huaweicloudsdkevs.v2.ResizeVolumeRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.ResizeVolumeResponse`
        """
        http_info = self._resize_volume_http_info(request)
        return self._call_api(**http_info)

    def resize_volume_invoker(self, request):
        http_info = self._resize_volume_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _resize_volume_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.1/{project_id}/cloudvolumes/{volume_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "ResizeVolumeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

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

    def retype_volume(self, request):
        r"""磁盘类型变更

        对按需或者包周期云硬盘进行磁盘类型变更。
        [在磁盘类型变更包周期云硬盘的场景下：](tag:hws)
        - [如果您需要查看订单可用的优惠券，请参考\&quot;[查询订单可用优惠券](https://support.huaweicloud.com/api-oce/zh-cn_topic_0092953630.html)\&quot;。](tag:hws)
        - [如果您需要支付订单，请参考\&quot;[支付包周期产品订单](https://support.huaweicloud.com/api-oce/api_order_00030.html)\&quot;。](tag:hws)
        - [如果您需要查询订单的资源开通详情，请参考\&quot;[查询订单的资源开通详情](https://support.huaweicloud.com/api-oce/api_order_00001.html)\&quot;。](tag:hws)
        - [如果您需要退订该包周期资源，请参考“[退订包周期资源](https://support.huaweicloud.com/api-oce/zh-cn_topic_0082522030.html)”。](tag:hws)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RetypeVolume
        :type request: :class:`huaweicloudsdkevs.v2.RetypeVolumeRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.RetypeVolumeResponse`
        """
        http_info = self._retype_volume_http_info(request)
        return self._call_api(**http_info)

    def retype_volume_invoker(self, request):
        http_info = self._retype_volume_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _retype_volume_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/volumes/{volume_id}/retype",
            "request_type": request.__class__.__name__,
            "response_type": "RetypeVolumeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

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

    def rollback_snapshot(self, request):
        r"""回滚快照到云硬盘

        将快照数据回滚到云硬盘。支持企业项目授权功能。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RollbackSnapshot
        :type request: :class:`huaweicloudsdkevs.v2.RollbackSnapshotRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.RollbackSnapshotResponse`
        """
        http_info = self._rollback_snapshot_http_info(request)
        return self._call_api(**http_info)

    def rollback_snapshot_invoker(self, request):
        http_info = self._rollback_snapshot_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _rollback_snapshot_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cloudsnapshots/{snapshot_id}/rollback",
            "request_type": request.__class__.__name__,
            "response_type": "RollbackSnapshotResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'snapshot_id' in local_var_params:
            path_params['snapshot_id'] = local_var_params['snapshot_id']

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

    def show_job(self, request):
        r"""查询job的状态

        查询Job的执行状态。
        可用于查询创建云硬盘，扩容云硬盘，删除云硬盘等API的执行状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJob
        :type request: :class:`huaweicloudsdkevs.v2.ShowJobRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.ShowJobResponse`
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
            "resource_path": "/v1/{project_id}/jobs/{job_id}",
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

    def show_snapshot(self, request):
        r"""查询单个云硬盘快照详情

        查询单个云硬盘快照信息。支持企业项目授权功能。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSnapshot
        :type request: :class:`huaweicloudsdkevs.v2.ShowSnapshotRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.ShowSnapshotResponse`
        """
        http_info = self._show_snapshot_http_info(request)
        return self._call_api(**http_info)

    def show_snapshot_invoker(self, request):
        http_info = self._show_snapshot_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_snapshot_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cloudsnapshots/{snapshot_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSnapshotResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'snapshot_id' in local_var_params:
            path_params['snapshot_id'] = local_var_params['snapshot_id']

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

    def show_volume(self, request):
        r"""查询单个云硬盘详情

        查询单个云硬盘的详细信息。支持企业项目授权功能。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVolume
        :type request: :class:`huaweicloudsdkevs.v2.ShowVolumeRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.ShowVolumeResponse`
        """
        http_info = self._show_volume_http_info(request)
        return self._call_api(**http_info)

    def show_volume_invoker(self, request):
        http_info = self._show_volume_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_volume_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cloudvolumes/{volume_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVolumeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

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

    def show_volume_tags(self, request):
        r"""查询云硬盘标签

        查询指定云硬盘的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVolumeTags
        :type request: :class:`huaweicloudsdkevs.v2.ShowVolumeTagsRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.ShowVolumeTagsResponse`
        """
        http_info = self._show_volume_tags_http_info(request)
        return self._call_api(**http_info)

    def show_volume_tags_invoker(self, request):
        http_info = self._show_volume_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_volume_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cloudvolumes/{volume_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVolumeTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

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

    def unsubscribe_postpaid_volume(self, request):
        r"""退订包周期计费模式的云硬盘

        退订包周期计费模式的云硬盘，有如下约束：
        -  系统盘、启动盘不可使用当前接口退订，必须和弹性云服务器一起退订
        -  接口的请求body体最多可以传60个云硬盘id
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UnsubscribePostpaidVolume
        :type request: :class:`huaweicloudsdkevs.v2.UnsubscribePostpaidVolumeRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.UnsubscribePostpaidVolumeResponse`
        """
        http_info = self._unsubscribe_postpaid_volume_http_info(request)
        return self._call_api(**http_info)

    def unsubscribe_postpaid_volume_invoker(self, request):
        http_info = self._unsubscribe_postpaid_volume_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _unsubscribe_postpaid_volume_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cloudvolumes/unsubscribe",
            "request_type": request.__class__.__name__,
            "response_type": "UnsubscribePostpaidVolumeResponse"
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

    def update_snapshot(self, request):
        r"""更新云硬盘快照

        更新云硬盘快照。支持企业项目授权功能。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSnapshot
        :type request: :class:`huaweicloudsdkevs.v2.UpdateSnapshotRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.UpdateSnapshotResponse`
        """
        http_info = self._update_snapshot_http_info(request)
        return self._call_api(**http_info)

    def update_snapshot_invoker(self, request):
        http_info = self._update_snapshot_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_snapshot_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/cloudsnapshots/{snapshot_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSnapshotResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'snapshot_id' in local_var_params:
            path_params['snapshot_id'] = local_var_params['snapshot_id']

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

    def update_volume(self, request):
        r"""更新云硬盘

        更新一个云硬盘的名称和描述。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateVolume
        :type request: :class:`huaweicloudsdkevs.v2.UpdateVolumeRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.UpdateVolumeResponse`
        """
        http_info = self._update_volume_http_info(request)
        return self._call_api(**http_info)

    def update_volume_invoker(self, request):
        http_info = self._update_volume_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_volume_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/cloudvolumes/{volume_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateVolumeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

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

    def list_versions(self, request):
        r"""查询接口版本信息列表

        查询接口版本信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVersions
        :type request: :class:`huaweicloudsdkevs.v2.ListVersionsRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.ListVersionsResponse`
        """
        http_info = self._list_versions_http_info(request)
        return self._call_api(**http_info)

    def list_versions_invoker(self, request):
        http_info = self._list_versions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_versions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/",
            "request_type": request.__class__.__name__,
            "response_type": "ListVersionsResponse"
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

    def show_version(self, request):
        r"""查询API接口的版本信息

        查询接口的指定版本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVersion
        :type request: :class:`huaweicloudsdkevs.v2.ShowVersionRequest`
        :rtype: :class:`huaweicloudsdkevs.v2.ShowVersionResponse`
        """
        http_info = self._show_version_http_info(request)
        return self._call_api(**http_info)

    def show_version_invoker(self, request):
        http_info = self._show_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_version_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/{version}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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
