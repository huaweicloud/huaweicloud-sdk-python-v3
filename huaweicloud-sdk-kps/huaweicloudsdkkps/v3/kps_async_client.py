# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class KpsAsyncClient(Client):
    def __init__(self):
        super(KpsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkkps.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "KpsClient":
            raise TypeError("client type error, support client type is KpsClient")

        return ClientBuilder(clazz)

    def associate_keypair_async(self, request):
        """绑定SSH密钥对

        给指定的虚拟机绑定（替换或重置，替换需提供虚拟机已配置的SSH密钥对私钥；重置不需要提供虚拟机的SSH密钥对私钥）新的SSH密钥对。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateKeypair
        :type request: :class:`huaweicloudsdkkps.v3.AssociateKeypairRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.AssociateKeypairResponse`
        """
        return self._associate_keypair_with_http_info(request)

    def _associate_keypair_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/keypairs/associate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociateKeypairResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_associate_keypair_async(self, request):
        """批量绑定SSH密钥对

        给指定的虚拟机批量绑定新的SSH密钥对。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAssociateKeypair
        :type request: :class:`huaweicloudsdkkps.v3.BatchAssociateKeypairRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.BatchAssociateKeypairResponse`
        """
        return self._batch_associate_keypair_with_http_info(request)

    def _batch_associate_keypair_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/keypairs/batch-associate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchAssociateKeypairResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def clear_private_key_async(self, request):
        """清除私钥

        清除SSH密钥对私钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ClearPrivateKey
        :type request: :class:`huaweicloudsdkkps.v3.ClearPrivateKeyRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.ClearPrivateKeyResponse`
        """
        return self._clear_private_key_with_http_info(request)

    def _clear_private_key_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'keypair_name' in local_var_params:
            path_params['keypair_name'] = local_var_params['keypair_name']

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
            resource_path='/v3/{project_id}/keypairs/{keypair_name}/private-key',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ClearPrivateKeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_keypair_async(self, request):
        """创建和导入SSH密钥对

        创建和导入SSH密钥对
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateKeypair
        :type request: :class:`huaweicloudsdkkps.v3.CreateKeypairRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.CreateKeypairResponse`
        """
        return self._create_keypair_with_http_info(request)

    def _create_keypair_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/keypairs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateKeypairResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_all_failed_task_async(self, request):
        """删除所有失败的任务

        删除操作失败的任务信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAllFailedTask
        :type request: :class:`huaweicloudsdkkps.v3.DeleteAllFailedTaskRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.DeleteAllFailedTaskResponse`
        """
        return self._delete_all_failed_task_with_http_info(request)

    def _delete_all_failed_task_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/failed-tasks',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAllFailedTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_failed_task_async(self, request):
        """删除失败的任务

        删除失败的任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteFailedTask
        :type request: :class:`huaweicloudsdkkps.v3.DeleteFailedTaskRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.DeleteFailedTaskResponse`
        """
        return self._delete_failed_task_with_http_info(request)

    def _delete_failed_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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
            resource_path='/v3/{project_id}/failed-tasks/{task_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteFailedTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_keypair_async(self, request):
        """删除SSH密钥对

        删除SSH密钥对。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteKeypair
        :type request: :class:`huaweicloudsdkkps.v3.DeleteKeypairRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.DeleteKeypairResponse`
        """
        return self._delete_keypair_with_http_info(request)

    def _delete_keypair_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'keypair_name' in local_var_params:
            path_params['keypair_name'] = local_var_params['keypair_name']

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
            resource_path='/v3/{project_id}/keypairs/{keypair_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteKeypairResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disassociate_keypair_async(self, request):
        """解绑SSH密钥对

        给指定的虚拟机解除绑定SSH密钥对并恢复SSH密码登录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateKeypair
        :type request: :class:`huaweicloudsdkkps.v3.DisassociateKeypairRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.DisassociateKeypairResponse`
        """
        return self._disassociate_keypair_with_http_info(request)

    def _disassociate_keypair_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/keypairs/disassociate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisassociateKeypairResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def export_private_key_async(self, request):
        """导出私钥

        导出指定密钥对的私钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportPrivateKey
        :type request: :class:`huaweicloudsdkkps.v3.ExportPrivateKeyRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.ExportPrivateKeyResponse`
        """
        return self._export_private_key_with_http_info(request)

    def _export_private_key_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/keypairs/private-key/export',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExportPrivateKeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def import_private_key_async(self, request):
        """导入私钥

        导入私钥到指定密钥对。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportPrivateKey
        :type request: :class:`huaweicloudsdkkps.v3.ImportPrivateKeyRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.ImportPrivateKeyResponse`
        """
        return self._import_private_key_with_http_info(request)

    def _import_private_key_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/keypairs/private-key/import',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ImportPrivateKeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_failed_task_async(self, request):
        """查询失败的任务信息

        查询绑定、解绑等操作失败的任务信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFailedTask
        :type request: :class:`huaweicloudsdkkps.v3.ListFailedTaskRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.ListFailedTaskResponse`
        """
        return self._list_failed_task_with_http_info(request)

    def _list_failed_task_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/failed-tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFailedTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_keypair_detail_async(self, request):
        """查询SSH密钥对详细信息

        查询SSH密钥对详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKeypairDetail
        :type request: :class:`huaweicloudsdkkps.v3.ListKeypairDetailRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.ListKeypairDetailResponse`
        """
        return self._list_keypair_detail_with_http_info(request)

    def _list_keypair_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'keypair_name' in local_var_params:
            path_params['keypair_name'] = local_var_params['keypair_name']

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
            resource_path='/v3/{project_id}/keypairs/{keypair_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListKeypairDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_keypair_task_async(self, request):
        """查询任务信息

        根据SSH密钥对接口返回的task_id，查询SSH密钥对当前任务的执行状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKeypairTask
        :type request: :class:`huaweicloudsdkkps.v3.ListKeypairTaskRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.ListKeypairTaskResponse`
        """
        return self._list_keypair_task_with_http_info(request)

    def _list_keypair_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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
            resource_path='/v3/{project_id}/tasks/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListKeypairTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_keypairs_async(self, request):
        """查询SSH密钥对列表

        查询SSH密钥对列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKeypairs
        :type request: :class:`huaweicloudsdkkps.v3.ListKeypairsRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.ListKeypairsResponse`
        """
        return self._list_keypairs_with_http_info(request)

    def _list_keypairs_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/keypairs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListKeypairsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_running_task_async(self, request):
        """查询正在处理的任务信息

        查询正在处理的任务信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRunningTask
        :type request: :class:`huaweicloudsdkkps.v3.ListRunningTaskRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.ListRunningTaskResponse`
        """
        return self._list_running_task_with_http_info(request)

    def _list_running_task_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/running-tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRunningTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_keypair_description_async(self, request):
        """更新SSH密钥对描述

        更新SSH密钥对描述。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateKeypairDescription
        :type request: :class:`huaweicloudsdkkps.v3.UpdateKeypairDescriptionRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.UpdateKeypairDescriptionResponse`
        """
        return self._update_keypair_description_with_http_info(request)

    def _update_keypair_description_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'keypair_name' in local_var_params:
            path_params['keypair_name'] = local_var_params['keypair_name']

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
            resource_path='/v3/{project_id}/keypairs/{keypair_name}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateKeypairDescriptionResponse',
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
