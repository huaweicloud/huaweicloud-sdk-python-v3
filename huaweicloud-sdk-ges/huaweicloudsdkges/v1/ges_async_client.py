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


class GesAsyncClient(Client):
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
        super(GesAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkges.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "GesClient":
            raise TypeError("client type error, support client type is GesClient")

        return ClientBuilder(clazz)

    def attach_eip_async(self, request):
        """绑定EIP(1.0.6)

        可以通过绑定弹性公网IP（简称EIP）访问GES服务。

        :param AttachEipRequest request
        :return: AttachEipResponse
        """
        return self.attach_eip_with_http_info(request)

    def attach_eip_with_http_info(self, request):
        """绑定EIP(1.0.6)

        可以通过绑定弹性公网IP（简称EIP）访问GES服务。

        :param AttachEipRequest request
        :return: AttachEipResponse
        """

        all_params = ['graph_id', 'action_id', 'bind_eip_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))

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
            resource_path='/v1.0/{project_id}/graphs/{graph_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AttachEipResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def check_metadata_async(self, request):
        """校验元数据文件(1.0.0)

        校验用户选择的数据集和元数据文件。

        :param CheckMetadataRequest request
        :return: CheckMetadataResponse
        """
        return self.check_metadata_with_http_info(request)

    def check_metadata_with_http_info(self, request):
        """校验元数据文件(1.0.0)

        校验用户选择的数据集和元数据文件。

        :param CheckMetadataRequest request
        :return: CheckMetadataResponse
        """

        all_params = ['action_id', 'check_metadata_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))

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
            resource_path='/v1.0/{project_id}/graphs/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CheckMetadataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def clear_graph_async(self, request):
        """清空图(2.1.2)

        清空图中所有数据。

        :param ClearGraphRequest request
        :return: ClearGraphResponse
        """
        return self.clear_graph_with_http_info(request)

    def clear_graph_with_http_info(self, request):
        """清空图(2.1.2)

        清空图中所有数据。

        :param ClearGraphRequest request
        :return: ClearGraphResponse
        """

        all_params = ['graph_id', 'action_id', 'clear_metadata']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))
        if 'clear_metadata' in local_var_params:
            query_params.append(('clear-metadata', local_var_params['clear_metadata']))

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
            resource_path='/v1.0/{project_id}/graphs/{graph_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ClearGraphResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_backup_async(self, request):
        """新增备份(1.0.0)

        新增备份。当前图数据出现错误或故障时，可以启动备份图进行恢复。

        :param CreateBackupRequest request
        :return: CreateBackupResponse
        """
        return self.create_backup_with_http_info(request)

    def create_backup_with_http_info(self, request):
        """新增备份(1.0.0)

        新增备份。当前图数据出现错误或故障时，可以启动备份图进行恢复。

        :param CreateBackupRequest request
        :return: CreateBackupResponse
        """

        all_params = ['graph_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

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
            resource_path='/v1.0/{project_id}/graphs/{graph_id}/backups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateBackupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_graph_async(self, request):
        """创建图(2.2.2)

        创建一个图。

        :param CreateGraphRequest request
        :return: CreateGraphResponse
        """
        return self.create_graph_with_http_info(request)

    def create_graph_with_http_info(self, request):
        """创建图(2.2.2)

        创建一个图。

        :param CreateGraphRequest request
        :return: CreateGraphResponse
        """

        all_params = ['create_graph_req']
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/graphs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateGraphResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_metadata_async(self, request):
        """新增元数据(2.1.18)

        新增元数据。

        :param CreateMetadataRequest request
        :return: CreateMetadataResponse
        """
        return self.create_metadata_with_http_info(request)

    def create_metadata_with_http_info(self, request):
        """新增元数据(2.1.18)

        新增元数据。

        :param CreateMetadataRequest request
        :return: CreateMetadataResponse
        """

        all_params = ['create_metadata_req']
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/graphs/metadatas',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateMetadataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_backup_async(self, request):
        """删除备份(1.0.0)

        删除备份。

        :param DeleteBackupRequest request
        :return: DeleteBackupResponse
        """
        return self.delete_backup_with_http_info(request)

    def delete_backup_with_http_info(self, request):
        """删除备份(1.0.0)

        删除备份。

        :param DeleteBackupRequest request
        :return: DeleteBackupResponse
        """

        all_params = ['backup_id', 'graph_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

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
            resource_path='/v1.0/{project_id}/graphs/{graph_id}/backups/{backup_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteBackupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_graph_async(self, request):
        """删除图(1.0.0)

        删除一个图。

        :param DeleteGraphRequest request
        :return: DeleteGraphResponse
        """
        return self.delete_graph_with_http_info(request)

    def delete_graph_with_http_info(self, request):
        """删除图(1.0.0)

        删除一个图。

        :param DeleteGraphRequest request
        :return: DeleteGraphResponse
        """

        all_params = ['graph_id', 'keep_backup']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

        query_params = []
        if 'keep_backup' in local_var_params:
            query_params.append(('keepBackup', local_var_params['keep_backup']))

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
            resource_path='/v1.0/{project_id}/graphs/{graph_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteGraphResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_metadata_async(self, request):
        """删除元数据(1.0.2)

        删除元数据。

        :param DeleteMetadataRequest request
        :return: DeleteMetadataResponse
        """
        return self.delete_metadata_with_http_info(request)

    def delete_metadata_with_http_info(self, request):
        """删除元数据(1.0.2)

        删除元数据。

        :param DeleteMetadataRequest request
        :return: DeleteMetadataResponse
        """

        all_params = ['metadata_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'metadata_id' in local_var_params:
            path_params['metadata_id'] = local_var_params['metadata_id']

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
            resource_path='/v1.0/{project_id}/graphs/metadatas/{metadata_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteMetadataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def detach_eip_async(self, request):
        """解绑EIP(1.0.6)

        当无需继续使用EIP时，您可通过解绑EIP来释放网络资源。

        :param DetachEipRequest request
        :return: DetachEipResponse
        """
        return self.detach_eip_with_http_info(request)

    def detach_eip_with_http_info(self, request):
        """解绑EIP(1.0.6)

        当无需继续使用EIP时，您可通过解绑EIP来释放网络资源。

        :param DetachEipRequest request
        :return: DetachEipResponse
        """

        all_params = ['graph_id', 'action_id', 'unbind_eip_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))

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
            resource_path='/v1.0/{project_id}/graphs/{graph_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DetachEipResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def export_graph_async(self, request):
        """导出图(1.0.5)

        导出图。

        :param ExportGraphRequest request
        :return: ExportGraphResponse
        """
        return self.export_graph_with_http_info(request)

    def export_graph_with_http_info(self, request):
        """导出图(1.0.5)

        导出图。

        :param ExportGraphRequest request
        :return: ExportGraphResponse
        """

        all_params = ['graph_id', 'action_id', 'export_graph_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))

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
            resource_path='/v1.0/{project_id}/graphs/{graph_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ExportGraphResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def import_graph_async(self, request):
        """增量导入图(2.1.14)

        增量导入图数据。

        :param ImportGraphRequest request
        :return: ImportGraphResponse
        """
        return self.import_graph_with_http_info(request)

    def import_graph_with_http_info(self, request):
        """增量导入图(2.1.14)

        增量导入图数据。

        :param ImportGraphRequest request
        :return: ImportGraphResponse
        """

        all_params = ['graph_id', 'action_id', 'import_graph_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))

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
            resource_path='/v1.0/{project_id}/graphs/{graph_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ImportGraphResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_backups_async(self, request):
        """查看所有备份列表(1.0.0)

        查询备份列表。

        :param ListBackupsRequest request
        :return: ListBackupsResponse
        """
        return self.list_backups_with_http_info(request)

    def list_backups_with_http_info(self, request):
        """查看所有备份列表(1.0.0)

        查询备份列表。

        :param ListBackupsRequest request
        :return: ListBackupsResponse
        """

        all_params = ['limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/graphs/backups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListBackupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_graph_backups_async(self, request):
        """查看某个图的备份列表(1.0.0)

        查询某个图下的备份列表。

        :param ListGraphBackupsRequest request
        :return: ListGraphBackupsResponse
        """
        return self.list_graph_backups_with_http_info(request)

    def list_graph_backups_with_http_info(self, request):
        """查看某个图的备份列表(1.0.0)

        查询某个图下的备份列表。

        :param ListGraphBackupsRequest request
        :return: ListGraphBackupsResponse
        """

        all_params = ['graph_id', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

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
            resource_path='/v1.0/{project_id}/graphs/{graph_id}/backups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListGraphBackupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_graph_metadatas_async(self, request):
        """查询元数据(1.0.2)

        查询某个图下的元数据。

        :param ListGraphMetadatasRequest request
        :return: ListGraphMetadatasResponse
        """
        return self.list_graph_metadatas_with_http_info(request)

    def list_graph_metadatas_with_http_info(self, request):
        """查询元数据(1.0.2)

        查询某个图下的元数据。

        :param ListGraphMetadatasRequest request
        :return: ListGraphMetadatasResponse
        """

        all_params = ['metadata_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'metadata_id' in local_var_params:
            path_params['metadata_id'] = local_var_params['metadata_id']

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
            resource_path='/v1.0/{project_id}/graphs/metadatas/{metadata_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListGraphMetadatasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_graphs_async(self, request):
        """查询图列表(2.1.18)

        查询当前租户所有的图。

        :param ListGraphsRequest request
        :return: ListGraphsResponse
        """
        return self.list_graphs_with_http_info(request)

    def list_graphs_with_http_info(self, request):
        """查询图列表(2.1.18)

        查询当前租户所有的图。

        :param ListGraphsRequest request
        :return: ListGraphsResponse
        """

        all_params = ['offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/graphs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListGraphsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_jobs_async(self, request):
        """查询任务中心(1.1.8)

        查询管理面任务中心。当前创建图、关闭图、启动图、删除图、增加备份、导入图、导出图、升级图等操作为异步任务，该API用于查询这些任务的详情。

        :param ListJobsRequest request
        :return: ListJobsResponse
        """
        return self.list_jobs_with_http_info(request)

    def list_jobs_with_http_info(self, request):
        """查询任务中心(1.1.8)

        查询管理面任务中心。当前创建图、关闭图、启动图、删除图、增加备份、导入图、导出图、升级图等操作为异步任务，该API用于查询这些任务的详情。

        :param ListJobsRequest request
        :return: ListJobsResponse
        """

        all_params = ['end_time', 'graph_name', 'limit', 'offset', 'start_time', 'status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'end_time' in local_var_params:
            query_params.append(('endTime', local_var_params['end_time']))
        if 'graph_name' in local_var_params:
            query_params.append(('graph_name', local_var_params['graph_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'start_time' in local_var_params:
            query_params.append(('startTime', local_var_params['start_time']))
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
            resource_path='/v1.0/{project_id}/graphs/jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_metadatas_async(self, request):
        """查询元数据列表(1.0.2)

        查询元数据列表。

        :param ListMetadatasRequest request
        :return: ListMetadatasResponse
        """
        return self.list_metadatas_with_http_info(request)

    def list_metadatas_with_http_info(self, request):
        """查询元数据列表(1.0.2)

        查询元数据列表。

        :param ListMetadatasRequest request
        :return: ListMetadatasResponse
        """

        all_params = ['limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/{project_id}/graphs/metadatas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListMetadatasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_quotas_async(self, request):
        """查询配额(1.0.0)

        查询租户配额。

        :param ListQuotasRequest request
        :return: ListQuotasResponse
        """
        return self.list_quotas_with_http_info(request)

    def list_quotas_with_http_info(self, request):
        """查询配额(1.0.0)

        查询租户配额。

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
            resource_path='/v1.0/{project_id}/graphs/quotas',
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


    def restart_graph_async(self, request):
        """强制重启图(2.2.21)

        强制启动一个图。针对导入、导出 、运行中 、清空中的图。强制重启图，会将该图执行中的异步任务变为失败，然后停止图、启动图到运行状态。

        :param RestartGraphRequest request
        :return: RestartGraphResponse
        """
        return self.restart_graph_with_http_info(request)

    def restart_graph_with_http_info(self, request):
        """强制重启图(2.2.21)

        强制启动一个图。针对导入、导出 、运行中 、清空中的图。强制重启图，会将该图执行中的异步任务变为失败，然后停止图、启动图到运行状态。

        :param RestartGraphRequest request
        :return: RestartGraphResponse
        """

        all_params = ['graph_id', 'action_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))

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
            resource_path='/v1.0/{project_id}/graphs/{graph_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RestartGraphResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_graph_async(self, request):
        """查询图详情(1.0.0)

        根据图ID查询某个图详情。

        :param ShowGraphRequest request
        :return: ShowGraphResponse
        """
        return self.show_graph_with_http_info(request)

    def show_graph_with_http_info(self, request):
        """查询图详情(1.0.0)

        根据图ID查询某个图详情。

        :param ShowGraphRequest request
        :return: ShowGraphResponse
        """

        all_params = ['graph_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

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
            resource_path='/v1.0/{project_id}/graphs/{graph_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowGraphResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_job_async(self, request):
        """查询Job状态(1.0.0)-管理面

        查询Job的执行状态。对创建图、关闭图、启动图、删除图、导入图等异步API命令下发后，会返回jobId，通过jobId查询任务的执行状态。

        :param ShowJobRequest request
        :return: ShowJobResponse
        """
        return self.show_job_with_http_info(request)

    def show_job_with_http_info(self, request):
        """查询Job状态(1.0.0)-管理面

        查询Job的执行状态。对创建图、关闭图、启动图、删除图、导入图等异步API命令下发后，会返回jobId，通过jobId查询任务的执行状态。

        :param ShowJobRequest request
        :return: ShowJobResponse
        """

        all_params = ['graph_id', 'job_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']
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
            resource_path='/v1.0/{project_id}/graphs/{graph_id}/jobs/{job_id}/status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def start_graph_async(self, request):
        """启动图(1.0.0)

        启动一个图。暂时不用的图可以先关闭，需要使用时再启动。

        :param StartGraphRequest request
        :return: StartGraphResponse
        """
        return self.start_graph_with_http_info(request)

    def start_graph_with_http_info(self, request):
        """启动图(1.0.0)

        启动一个图。暂时不用的图可以先关闭，需要使用时再启动。

        :param StartGraphRequest request
        :return: StartGraphResponse
        """

        all_params = ['graph_id', 'action_id', 'start_graph_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))

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
            resource_path='/v1.0/{project_id}/graphs/{graph_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StartGraphResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def stop_graph_async(self, request):
        """关闭图(1.0.0)

        关闭一个图。如果图创建好了，暂时不用可以先关闭，需要使用时再启用。 >处于关闭状态的图不计算实例费用。

        :param StopGraphRequest request
        :return: StopGraphResponse
        """
        return self.stop_graph_with_http_info(request)

    def stop_graph_with_http_info(self, request):
        """关闭图(1.0.0)

        关闭一个图。如果图创建好了，暂时不用可以先关闭，需要使用时再启用。 >处于关闭状态的图不计算实例费用。

        :param StopGraphRequest request
        :return: StopGraphResponse
        """

        all_params = ['graph_id', 'action_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))

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
            resource_path='/v1.0/{project_id}/graphs/{graph_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StopGraphResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def upgrade_graph_async(self, request):
        """升级图(1.0.5)

        升级图。图引擎服务会定期升级版本，用户可根据需要升级图。

        :param UpgradeGraphRequest request
        :return: UpgradeGraphResponse
        """
        return self.upgrade_graph_with_http_info(request)

    def upgrade_graph_with_http_info(self, request):
        """升级图(1.0.5)

        升级图。图引擎服务会定期升级版本，用户可根据需要升级图。

        :param UpgradeGraphRequest request
        :return: UpgradeGraphResponse
        """

        all_params = ['graph_id', 'action_id', 'upgrade_graph_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))

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
            resource_path='/v1.0/{project_id}/graphs/{graph_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpgradeGraphResponse',
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
