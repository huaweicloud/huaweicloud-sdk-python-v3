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


class CphClient(Client):
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
        super(CphClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcph.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "CphClient":
            raise TypeError("client type error, support client type is CphClient")

        return ClientBuilder(clazz)

    def batch_export_cloud_phone_data(self, request):
        """导出云手机数据

        批量导出云手机中的数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchExportCloudPhoneData
        :type request: :class:`huaweicloudsdkcph.v1.BatchExportCloudPhoneDataRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.BatchExportCloudPhoneDataResponse`
        """
        return self.batch_export_cloud_phone_data_with_http_info(request)

    def batch_export_cloud_phone_data_with_http_info(self, request):
        all_params = ['batch_export_cloud_phone_data_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def batch_import_cloud_phone_data(self, request):
        """恢复云手机数据

        导入数据到手机中。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchImportCloudPhoneData
        :type request: :class:`huaweicloudsdkcph.v1.BatchImportCloudPhoneDataRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.BatchImportCloudPhoneDataResponse`
        """
        return self.batch_import_cloud_phone_data_with_http_info(request)

    def batch_import_cloud_phone_data_with_http_info(self, request):
        all_params = ['batch_import_cloud_phone_data_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def batch_migrate_cloud_phone(self, request):
        """迁移云手机

        批量迁移整台云手机，包括云手机的系统盘数据和数据盘数据。该接口为异步接口，迁移完成的时间和手机的数据量有一定关系，整机数据大小为11G时，迁移时间大约为3-5分钟。迁移前请关闭云手机。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchMigrateCloudPhone
        :type request: :class:`huaweicloudsdkcph.v1.BatchMigrateCloudPhoneRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.BatchMigrateCloudPhoneResponse`
        """
        return self.batch_migrate_cloud_phone_with_http_info(request)

    def batch_migrate_cloud_phone_with_http_info(self, request):
        all_params = ['batch_migrate_cloud_phone_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1/{project_id}/cloud-phone/phones/batch-migrate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchMigrateCloudPhoneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_cloud_phone_server_model(self, request):
        """变更云手机服务器规格

        变更云手机服务器规格。只有能使用physical.rx1.xlarge.special私有规格的租户才可使用本接口。变更的目标规格也必须为特殊的规格才可变更。接口调用成功后，大约2分钟左右规格会变更结束，在订单中心可以查看到变更的订单状态为成功，且查询服务器的详细信息，可以查看到服务器规格名称已经变成新的规格名称。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeCloudPhoneServerModel
        :type request: :class:`huaweicloudsdkcph.v1.ChangeCloudPhoneServerModelRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ChangeCloudPhoneServerModelResponse`
        """
        return self.change_cloud_phone_server_model_with_http_info(request)

    def change_cloud_phone_server_model_with_http_info(self, request):
        all_params = ['change_cloud_phone_server_model_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def create_cloud_phone_server(self, request):
        """购买系统定义网络云手机服务器

        购买系统定义网络云手机服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCloudPhoneServer
        :type request: :class:`huaweicloudsdkcph.v1.CreateCloudPhoneServerRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.CreateCloudPhoneServerResponse`
        """
        return self.create_cloud_phone_server_with_http_info(request)

    def create_cloud_phone_server_with_http_info(self, request):
        all_params = ['create_cloud_phone_server_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1/{project_id}/cloud-phone/phones',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCloudPhoneServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_net2_cloud_phone_server(self, request):
        """购买自定义网络云手机服务器

        购买自定义网络的云手机服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateNet2CloudPhoneServer
        :type request: :class:`huaweicloudsdkcph.v1.CreateNet2CloudPhoneServerRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.CreateNet2CloudPhoneServerResponse`
        """
        return self.create_net2_cloud_phone_server_with_http_info(request)

    def create_net2_cloud_phone_server_with_http_info(self, request):
        all_params = ['create_net2_cloud_phone_server_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def delete_share_apps(self, request):
        """删除共享应用

        在共享应用存储目录中删除共享应用，该功能仅在支持共享应用的云手机规格上可实现。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteShareApps
        :type request: :class:`huaweicloudsdkcph.v1.DeleteShareAppsRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.DeleteShareAppsResponse`
        """
        return self.delete_share_apps_with_http_info(request)

    def delete_share_apps_with_http_info(self, request):
        all_params = ['delete_share_apps_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def delete_share_files(self, request):
        """删除共享存储文件

        删除共享存储目录中文件，该功能仅在支持共享存储的云手机规格上可实现。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteShareFiles
        :type request: :class:`huaweicloudsdkcph.v1.DeleteShareFilesRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.DeleteShareFilesResponse`
        """
        return self.delete_share_files_with_http_info(request)

    def delete_share_files_with_http_info(self, request):
        all_params = ['delete_share_files_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def import_traffic(self, request):
        """云手机流量导流

        手机流量路由修改。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportTraffic
        :type request: :class:`huaweicloudsdkcph.v1.ImportTrafficRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ImportTrafficResponse`
        """
        return self.import_traffic_with_http_info(request)

    def import_traffic_with_http_info(self, request):
        all_params = ['import_traffic_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def list_cloud_phone_images(self, request):
        """查询手机镜像

        根据项目ID查询可用的手机镜像。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCloudPhoneImages
        :type request: :class:`huaweicloudsdkcph.v1.ListCloudPhoneImagesRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListCloudPhoneImagesResponse`
        """
        return self.list_cloud_phone_images_with_http_info(request)

    def list_cloud_phone_images_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def list_cloud_phone_models(self, request):
        """查询云手机规格列表

        查询或统计云手机的规格列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCloudPhoneModels
        :type request: :class:`huaweicloudsdkcph.v1.ListCloudPhoneModelsRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListCloudPhoneModelsResponse`
        """
        return self.list_cloud_phone_models_with_http_info(request)

    def list_cloud_phone_models_with_http_info(self, request):
        all_params = ['status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

    def list_cloud_phone_server_models(self, request):
        """查询云手机服务器规格列表

        查询云手机服务器的规格列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCloudPhoneServerModels
        :type request: :class:`huaweicloudsdkcph.v1.ListCloudPhoneServerModelsRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListCloudPhoneServerModelsResponse`
        """
        return self.list_cloud_phone_server_models_with_http_info(request)

    def list_cloud_phone_server_models_with_http_info(self, request):
        all_params = ['product_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def list_cloud_phone_servers(self, request):
        """查询云手机服务器列表

        分页查询云手机服务器，云手机服务器列表按照创建时间进行降序排列。分页查询可以指定offset以及limit。如果不存在云手机服务器，则返回空列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCloudPhoneServers
        :type request: :class:`huaweicloudsdkcph.v1.ListCloudPhoneServersRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListCloudPhoneServersResponse`
        """
        return self.list_cloud_phone_servers_with_http_info(request)

    def list_cloud_phone_servers_with_http_info(self, request):
        all_params = ['offset', 'limit', 'server_name', 'server_id', 'network_version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def list_cloud_phones(self, request):
        """查询云手机列表

        分页查询云手机，云手机列表按照创建时间进行降序排列。分页查询可以指定offset以及limit。如果不存在云手机，则返回空列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCloudPhones
        :type request: :class:`huaweicloudsdkcph.v1.ListCloudPhonesRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListCloudPhonesResponse`
        """
        return self.list_cloud_phones_with_http_info(request)

    def list_cloud_phones_with_http_info(self, request):
        all_params = ['offset', 'limit', 'phone_name', 'server_id', 'status', 'type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def list_encode_servers(self, request):
        """查询编码服务

        查询编码服务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEncodeServers
        :type request: :class:`huaweicloudsdkcph.v1.ListEncodeServersRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListEncodeServersResponse`
        """
        return self.list_encode_servers_with_http_info(request)

    def list_encode_servers_with_http_info(self, request):
        all_params = ['offset', 'limit', 'type', 'status', 'server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def list_jobs(self, request):
        """查询任务执行状态列表

        查询同一个request id下的任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListJobs
        :type request: :class:`huaweicloudsdkcph.v1.ListJobsRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListJobsResponse`
        """
        return self.list_jobs_with_http_info(request)

    def list_jobs_with_http_info(self, request):
        all_params = ['request_id', 'request_ids']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'request_id' in local_var_params:
            query_params.append(('request_id', local_var_params['request_id']))
        if 'request_ids' in local_var_params:
            query_params.append(('request_ids', local_var_params['request_ids']))

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

    def list_share_files(self, request):
        """查询共享存储文件

        查询共享存储指定路径下的文件列表，该功能仅在支持共享存储的云手机规格上可实现。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListShareFiles
        :type request: :class:`huaweicloudsdkcph.v1.ListShareFilesRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ListShareFilesResponse`
        """
        return self.list_share_files_with_http_info(request)

    def list_share_files_with_http_info(self, request):
        all_params = ['server_ids', 'path', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def push_share_apps(self, request):
        """推送共享应用

        推送应用tar文件至共享应用存储目录中，该功能仅在支持共享应用的云手机规格上可实现。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PushShareApps
        :type request: :class:`huaweicloudsdkcph.v1.PushShareAppsRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.PushShareAppsResponse`
        """
        return self.push_share_apps_with_http_info(request)

    def push_share_apps_with_http_info(self, request):
        all_params = ['push_share_apps_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def push_share_files(self, request):
        """推送共享存储文件

        推送文件至共享存储目录中，该功能仅在支持共享存储的云手机规格上可实现。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PushShareFiles
        :type request: :class:`huaweicloudsdkcph.v1.PushShareFilesRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.PushShareFilesResponse`
        """
        return self.push_share_files_with_http_info(request)

    def push_share_files_with_http_info(self, request):
        all_params = ['push_share_files_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def reset_cloud_phone(self, request):
        """重置云手机

        批量重置云手机，将云手机恢复出厂设置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetCloudPhone
        :type request: :class:`huaweicloudsdkcph.v1.ResetCloudPhoneRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ResetCloudPhoneResponse`
        """
        return self.reset_cloud_phone_with_http_info(request)

    def reset_cloud_phone_with_http_info(self, request):
        all_params = ['reset_cloud_phone_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def restart_cloud_phone(self, request):
        """重启云手机

        批量重启云手机，也可用于开启云手机。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestartCloudPhone
        :type request: :class:`huaweicloudsdkcph.v1.RestartCloudPhoneRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.RestartCloudPhoneResponse`
        """
        return self.restart_cloud_phone_with_http_info(request)

    def restart_cloud_phone_with_http_info(self, request):
        all_params = ['restart_cloud_phone_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def restart_cloud_phone_server(self, request):
        """重启云手机服务器

        批量重启云手机服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestartCloudPhoneServer
        :type request: :class:`huaweicloudsdkcph.v1.RestartCloudPhoneServerRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.RestartCloudPhoneServerResponse`
        """
        return self.restart_cloud_phone_server_with_http_info(request)

    def restart_cloud_phone_server_with_http_info(self, request):
        all_params = ['restart_cloud_phone_server_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def restart_encode_server(self, request):
        """重启编码服务

        批量重启编码服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestartEncodeServer
        :type request: :class:`huaweicloudsdkcph.v1.RestartEncodeServerRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.RestartEncodeServerResponse`
        """
        return self.restart_encode_server_with_http_info(request)

    def restart_encode_server_with_http_info(self, request):
        all_params = ['restart_encode_server_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def show_bandwidth_detail(self, request):
        """查询带宽信息

        查询云手机使用的带宽信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBandwidthDetail
        :type request: :class:`huaweicloudsdkcph.v1.ShowBandwidthDetailRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ShowBandwidthDetailResponse`
        """
        return self.show_bandwidth_detail_with_http_info(request)

    def show_bandwidth_detail_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def show_cloud_phone_detail(self, request):
        """查询云手机详情

        查询云手机的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCloudPhoneDetail
        :type request: :class:`huaweicloudsdkcph.v1.ShowCloudPhoneDetailRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ShowCloudPhoneDetailResponse`
        """
        return self.show_cloud_phone_detail_with_http_info(request)

    def show_cloud_phone_detail_with_http_info(self, request):
        all_params = ['phone_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def show_cloud_phone_server_detail(self, request):
        """查询云手机服务器详情

        根据server_id查询云手机服务器的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCloudPhoneServerDetail
        :type request: :class:`huaweicloudsdkcph.v1.ShowCloudPhoneServerDetailRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ShowCloudPhoneServerDetailResponse`
        """
        return self.show_cloud_phone_server_detail_with_http_info(request)

    def show_cloud_phone_server_detail_with_http_info(self, request):
        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def show_job(self, request):
        """查询任务执行状态

        查询任务的执行状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJob
        :type request: :class:`huaweicloudsdkcph.v1.ShowJobRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.ShowJobResponse`
        """
        return self.show_job_with_http_info(request)

    def show_job_with_http_info(self, request):
        all_params = ['job_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def stop_cloud_phone(self, request):
        """关闭云手机

        批量关闭云手机。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopCloudPhone
        :type request: :class:`huaweicloudsdkcph.v1.StopCloudPhoneRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.StopCloudPhoneResponse`
        """
        return self.stop_cloud_phone_with_http_info(request)

    def stop_cloud_phone_with_http_info(self, request):
        all_params = ['stop_cloud_phone_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def update_bandwidth(self, request):
        """修改共享带宽

        修改云手机使用的共享带宽大小。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateBandwidth
        :type request: :class:`huaweicloudsdkcph.v1.UpdateBandwidthRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.UpdateBandwidthResponse`
        """
        return self.update_bandwidth_with_http_info(request)

    def update_bandwidth_with_http_info(self, request):
        all_params = ['band_width_id', 'update_bandwidth_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def update_cloud_phone_property(self, request):
        """更新云手机属性

        部分云手机属性开放更新能力，部分属性无法更新，部分属性需要重启手机生效，属性约束请云手机属性列表。如果手机处于异常状态，属性更新后需恢复手机状态为运行中才可生效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCloudPhoneProperty
        :type request: :class:`huaweicloudsdkcph.v1.UpdateCloudPhonePropertyRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.UpdateCloudPhonePropertyResponse`
        """
        return self.update_cloud_phone_property_with_http_info(request)

    def update_cloud_phone_property_with_http_info(self, request):
        all_params = ['update_cloud_phone_property_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def update_keypair(self, request):
        """更改密钥对

        修改连接云手机的密钥对。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateKeypair
        :type request: :class:`huaweicloudsdkcph.v1.UpdateKeypairRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.UpdateKeypairResponse`
        """
        return self.update_keypair_with_http_info(request)

    def update_keypair_with_http_info(self, request):
        all_params = ['update_keypair_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def update_phone_name(self, request):
        """修改云手机名称

        根据phoneId修改phoneName。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePhoneName
        :type request: :class:`huaweicloudsdkcph.v1.UpdatePhoneNameRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.UpdatePhoneNameResponse`
        """
        return self.update_phone_name_with_http_info(request)

    def update_phone_name_with_http_info(self, request):
        all_params = ['phone_id', 'update_phone_name_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def update_server_name(self, request):
        """修改云手机服务器名称

        根据serverId修改serverName。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateServerName
        :type request: :class:`huaweicloudsdkcph.v1.UpdateServerNameRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.UpdateServerNameResponse`
        """
        return self.update_server_name_with_http_info(request)

    def update_server_name_with_http_info(self, request):
        all_params = ['server_id', 'update_server_name_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def install_apk(self, request):
        """安装apk

        在云手机中安装apk。系统会将指定的apk文件下载后直接安装到云手机中。
        支持安装单apk应用和多apk应用。可使用install命令安装单apk应用，一次只支持安装一个apk；可使用install-multiple命令安装多apk应用（多apk应用为单个应用拆分成多个apk），一次只支持同一个应用的多个apk。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for InstallApk
        :type request: :class:`huaweicloudsdkcph.v1.InstallApkRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.InstallApkResponse`
        """
        return self.install_apk_with_http_info(request)

    def install_apk_with_http_info(self, request):
        all_params = ['install_apk_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def push_file(self, request):
        """推送文件

        推送文件到云手机文件系统中。系统会将所指定的文件下载解压后，将解压后的内容全部推送到云手机的根目录下。只支持指定tar格式的文件进行推送，您需要将tar文件提前上传至您的OBS桶中。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PushFile
        :type request: :class:`huaweicloudsdkcph.v1.PushFileRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.PushFileResponse`
        """
        return self.push_file_with_http_info(request)

    def push_file_with_http_info(self, request):
        all_params = ['push_file_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def run_shell_command(self, request):
        """执行异步adb命令

        在云手机中执行shell命令。该接口为异步接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunShellCommand
        :type request: :class:`huaweicloudsdkcph.v1.RunShellCommandRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.RunShellCommandResponse`
        """
        return self.run_shell_command_with_http_info(request)

    def run_shell_command_with_http_info(self, request):
        all_params = ['run_shell_command_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def run_sync_command(self, request):
        """执行同步adb命令

        在云手机中同步执行命令并返回命令执行的输出信息，该接口仅支持adb shell命令的执行。1分钟内每个用户调用接口次数上限为6次，每个云手机允许执行命令超时时间为2秒，接口时间不超过30秒，执行云手机数越多，接口耗时相应越长。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunSyncCommand
        :type request: :class:`huaweicloudsdkcph.v1.RunSyncCommandRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.RunSyncCommandResponse`
        """
        return self.run_sync_command_with_http_info(request)

    def run_sync_command_with_http_info(self, request):
        all_params = ['run_sync_command_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def uninstall_apk(self, request):
        """卸载apk

        在云手机中卸载apk。该接口为异步接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UninstallApk
        :type request: :class:`huaweicloudsdkcph.v1.UninstallApkRequest`
        :rtype: :class:`huaweicloudsdkcph.v1.UninstallApkResponse`
        """
        return self.uninstall_apk_with_http_info(request)

    def uninstall_apk_with_http_info(self, request):
        all_params = ['uninstall_apk_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
