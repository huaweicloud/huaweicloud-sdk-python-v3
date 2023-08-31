# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class EcAsyncClient(Client):
    def __init__(self):
        super(EcAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkec.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls, "GlobalCredentials")

        if clazz.__name__ != "EcClient":
            raise TypeError("client type error, support client type is EcClient")

        return ClientBuilder(clazz, "GlobalCredentials")

    def create_ecn_access_point_async(self, request):
        """添加新的接入点

        添加新的接入点
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEcnAccessPoint
        :type request: :class:`huaweicloudsdkec.v1.CreateEcnAccessPointRequest`
        :rtype: :class:`huaweicloudsdkec.v1.CreateEcnAccessPointResponse`
        """
        return self._create_ecn_access_point_with_http_info(request)

    def _create_ecn_access_point_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ecn_id' in local_var_params:
            path_params['ecn_id'] = local_var_params['ecn_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/enterprise-connect-network/{ecn_id}/access-point',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateEcnAccessPointResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_ecn_access_point_async(self, request):
        """删除接入点

        根据企业连接网络ID，删除接入点
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEcnAccessPoint
        :type request: :class:`huaweicloudsdkec.v1.DeleteEcnAccessPointRequest`
        :rtype: :class:`huaweicloudsdkec.v1.DeleteEcnAccessPointResponse`
        """
        return self._delete_ecn_access_point_with_http_info(request)

    def _delete_ecn_access_point_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ecn_id' in local_var_params:
            path_params['ecn_id'] = local_var_params['ecn_id']
        if 'access_point_id' in local_var_params:
            path_params['access_point_id'] = local_var_params['access_point_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/enterprise-connect-network/{ecn_id}/access-point/{access_point_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEcnAccessPointResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_ecn_access_point_by_ecn_id_async(self, request):
        """查询接入点

        根据企业连接网络ID，查询其下所有接入点
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEcnAccessPointByEcnId
        :type request: :class:`huaweicloudsdkec.v1.ListEcnAccessPointByEcnIdRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ListEcnAccessPointByEcnIdResponse`
        """
        return self._list_ecn_access_point_by_ecn_id_with_http_info(request)

    def _list_ecn_access_point_by_ecn_id_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ecn_id' in local_var_params:
            path_params['ecn_id'] = local_var_params['ecn_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/enterprise-connect-network/{ecn_id}/access-point',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEcnAccessPointByEcnIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_ecn_access_point_async(self, request):
        """更新接入点

        根据企业连接网络ID，更新接入点
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEcnAccessPoint
        :type request: :class:`huaweicloudsdkec.v1.UpdateEcnAccessPointRequest`
        :rtype: :class:`huaweicloudsdkec.v1.UpdateEcnAccessPointResponse`
        """
        return self._update_ecn_access_point_with_http_info(request)

    def _update_ecn_access_point_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ecn_id' in local_var_params:
            path_params['ecn_id'] = local_var_params['ecn_id']
        if 'access_point_id' in local_var_params:
            path_params['access_point_id'] = local_var_params['access_point_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/enterprise-connect-network/{ecn_id}/access-point/{access_point_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEcnAccessPointResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_ecn_with_ieg_async(self, request):
        """绑定智能企业网关到企业连接网络

        绑定智能企业网关到企业连接网络
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddEcnWithIeg
        :type request: :class:`huaweicloudsdkec.v1.AddEcnWithIegRequest`
        :rtype: :class:`huaweicloudsdkec.v1.AddEcnWithIegResponse`
        """
        return self._add_ecn_with_ieg_with_http_info(request)

    def _add_ecn_with_ieg_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ecn_id' in local_var_params:
            path_params['ecn_id'] = local_var_params['ecn_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/enterprise-connect-network/{ecn_id}/relationship/intelligent-enterprise-gateway',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddEcnWithIegResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_ecn_with_ieg_async(self, request):
        """解除智能企业网关和企业连接网络的绑定

        解除智能企业网关和企业连接网络的绑定
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEcnWithIeg
        :type request: :class:`huaweicloudsdkec.v1.DeleteEcnWithIegRequest`
        :rtype: :class:`huaweicloudsdkec.v1.DeleteEcnWithIegResponse`
        """
        return self._delete_ecn_with_ieg_with_http_info(request)

    def _delete_ecn_with_ieg_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ecn_id' in local_var_params:
            path_params['ecn_id'] = local_var_params['ecn_id']
        if 'relation_id' in local_var_params:
            path_params['relation_id'] = local_var_params['relation_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/enterprise-connect-network/{ecn_id}/relationship/intelligent-enterprise-gateway/{relation_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEcnWithIegResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_ecn_async(self, request):
        """查询企业连接网络列表

        查询租户的企业连接网络列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEcn
        :type request: :class:`huaweicloudsdkec.v1.ListEcnRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ListEcnResponse`
        """
        return self._list_ecn_with_http_info(request)

    def _list_ecn_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'

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
            resource_path='/v1/{domain_id}/enterprise-connect/enterprise-connect-network',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEcnResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_ecn_with_ieg_async(self, request):
        """查询企业连接网络与智能企业网关绑定关系

        根据企业连接网络ID，查询企业连接网络与智能企业网关绑定关系
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEcnWithIeg
        :type request: :class:`huaweicloudsdkec.v1.ListEcnWithIegRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ListEcnWithIegResponse`
        """
        return self._list_ecn_with_ieg_with_http_info(request)

    def _list_ecn_with_ieg_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ecn_id' in local_var_params:
            path_params['ecn_id'] = local_var_params['ecn_id']

        query_params = []
        if 'ieg_id' in local_var_params:
            query_params.append(('ieg_id', local_var_params['ieg_id']))

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
            resource_path='/v1/{domain_id}/enterprise-connect/enterprise-connect-network/{ecn_id}/relationship/intelligent-enterprise-gateway',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEcnWithIegResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_ecn_info_async(self, request):
        """查询企业连接网络

        根据企业连接网络ID，查询企业连接网络
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEcnInfo
        :type request: :class:`huaweicloudsdkec.v1.ShowEcnInfoRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ShowEcnInfoResponse`
        """
        return self._show_ecn_info_with_http_info(request)

    def _show_ecn_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ecn_id' in local_var_params:
            path_params['ecn_id'] = local_var_params['ecn_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/enterprise-connect-network/{ecn_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEcnInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_ecn_with_ieg_async(self, request):
        """查询企业连接网络与单个智能企业网关绑定关系

        查询企业连接网络与单个智能企业网关绑定关系
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEcnWithIeg
        :type request: :class:`huaweicloudsdkec.v1.ShowEcnWithIegRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ShowEcnWithIegResponse`
        """
        return self._show_ecn_with_ieg_with_http_info(request)

    def _show_ecn_with_ieg_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ecn_id' in local_var_params:
            path_params['ecn_id'] = local_var_params['ecn_id']
        if 'relation_id' in local_var_params:
            path_params['relation_id'] = local_var_params['relation_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/enterprise-connect-network/{ecn_id}/relationship/intelligent-enterprise-gateway/{relation_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEcnWithIegResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_ecn_async(self, request):
        """更新企业连接网络

        根据企业连接网络ID，更新企业连接网络
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEcn
        :type request: :class:`huaweicloudsdkec.v1.UpdateEcnRequest`
        :rtype: :class:`huaweicloudsdkec.v1.UpdateEcnResponse`
        """
        return self._update_ecn_with_http_info(request)

    def _update_ecn_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ecn_id' in local_var_params:
            path_params['ecn_id'] = local_var_params['ecn_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/enterprise-connect-network/{ecn_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEcnResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_equipment_async(self, request):
        """激活智能企业网关设备

        激活智能企业网关设备
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEquipment
        :type request: :class:`huaweicloudsdkec.v1.CreateEquipmentRequest`
        :rtype: :class:`huaweicloudsdkec.v1.CreateEquipmentResponse`
        """
        return self._create_equipment_with_http_info(request)

    def _create_equipment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateEquipmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_equipment_async(self, request):
        """移除智能企业网关设备

        移除智能企业网关设备
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEquipment
        :type request: :class:`huaweicloudsdkec.v1.DeleteEquipmentRequest`
        :rtype: :class:`huaweicloudsdkec.v1.DeleteEquipmentResponse`
        """
        return self._delete_equipment_with_http_info(request)

    def _delete_equipment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEquipmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def generate_initial_configuration_async(self, request):
        """生成智能企业网关设备初始配置

        生成智能企业网关设备初始配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GenerateInitialConfiguration
        :type request: :class:`huaweicloudsdkec.v1.GenerateInitialConfigurationRequest`
        :rtype: :class:`huaweicloudsdkec.v1.GenerateInitialConfigurationResponse`
        """
        return self._generate_initial_configuration_with_http_info(request)

    def _generate_initial_configuration_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/initial-configuration',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='GenerateInitialConfigurationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_equipments_async(self, request):
        """查询智能企业网关设备列表

        根据智能企业网关ID，查询智能企业网关设备列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEquipments
        :type request: :class:`huaweicloudsdkec.v1.ListEquipmentsRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ListEquipmentsResponse`
        """
        return self._list_equipments_with_http_info(request)

    def _list_equipments_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEquipmentsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reboot_equipment_async(self, request):
        """重启智能企业网关设备

        重启智能企业网关设备
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RebootEquipment
        :type request: :class:`huaweicloudsdkec.v1.RebootEquipmentRequest`
        :rtype: :class:`huaweicloudsdkec.v1.RebootEquipmentResponse`
        """
        return self._reboot_equipment_with_http_info(request)

    def _reboot_equipment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/reboot',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RebootEquipmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_equipment_info_async(self, request):
        """查询智能企业网关设备

        查询智能企业网关设备
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEquipmentInfo
        :type request: :class:`huaweicloudsdkec.v1.ShowEquipmentInfoRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ShowEquipmentInfoResponse`
        """
        return self._show_equipment_info_with_http_info(request)

    def _show_equipment_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEquipmentInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_equipment_specific_config_async(self, request):
        """查询智能企业网关设备基础规格配置

        查询智能企业网关设备基础规格配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEquipmentSpecificConfig
        :type request: :class:`huaweicloudsdkec.v1.ShowEquipmentSpecificConfigRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ShowEquipmentSpecificConfigResponse`
        """
        return self._show_equipment_specific_config_with_http_info(request)

    def _show_equipment_specific_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'equipment_type' in local_var_params:
            path_params['equipment_type'] = local_var_params['equipment_type']

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
            resource_path='/v1/{domain_id}/enterprise-connect/equipment-specification/{equipment_type}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEquipmentSpecificConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_equipment_esn_async(self, request):
        """修改智能企业网关设备ESN

        修改智能企业网关设备ESN
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEquipmentEsn
        :type request: :class:`huaweicloudsdkec.v1.UpdateEquipmentEsnRequest`
        :rtype: :class:`huaweicloudsdkec.v1.UpdateEquipmentEsnResponse`
        """
        return self._update_equipment_esn_with_http_info(request)

    def _update_equipment_esn_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/esn',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEquipmentEsnResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_equipment_info_async(self, request):
        """更新智能企业网关设备

        更新智能企业网关设备
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEquipmentInfo
        :type request: :class:`huaweicloudsdkec.v1.UpdateEquipmentInfoRequest`
        :rtype: :class:`huaweicloudsdkec.v1.UpdateEquipmentInfoResponse`
        """
        return self._update_equipment_info_with_http_info(request)

    def _update_equipment_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEquipmentInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_equipment_lan_config_async(self, request):
        """创建智能企业网关设备LAN口配置

        创建智能企业网关设备LAN口配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEquipmentLanConfig
        :type request: :class:`huaweicloudsdkec.v1.CreateEquipmentLanConfigRequest`
        :rtype: :class:`huaweicloudsdkec.v1.CreateEquipmentLanConfigResponse`
        """
        return self._create_equipment_lan_config_with_http_info(request)

    def _create_equipment_lan_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/lan-interface',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateEquipmentLanConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_equipment_lan_config_async(self, request):
        """删除智能企业网关设备LAN口配置

        删除智能企业网关设备LAN口配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEquipmentLanConfig
        :type request: :class:`huaweicloudsdkec.v1.DeleteEquipmentLanConfigRequest`
        :rtype: :class:`huaweicloudsdkec.v1.DeleteEquipmentLanConfigResponse`
        """
        return self._delete_equipment_lan_config_with_http_info(request)

    def _delete_equipment_lan_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

        query_params = []
        if 'interface_name' in local_var_params:
            query_params.append(('interface_name', local_var_params['interface_name']))
        if 'vlan_id' in local_var_params:
            query_params.append(('vlan_id', local_var_params['vlan_id']))

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/lan-interface',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEquipmentLanConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_equipment_interface_name_async(self, request):
        """查询智能企业网关已配置的接口名字

        查询智能企业网关已配置的接口名字
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEquipmentInterfaceName
        :type request: :class:`huaweicloudsdkec.v1.ListEquipmentInterfaceNameRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ListEquipmentInterfaceNameResponse`
        """
        return self._list_equipment_interface_name_with_http_info(request)

    def _list_equipment_interface_name_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/interface-name',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEquipmentInterfaceNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_equipment_dns_info_async(self, request):
        """查询智能企业网关设备主备DNS配置

        查询智能企业网关设备主备DNS配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEquipmentDnsInfo
        :type request: :class:`huaweicloudsdkec.v1.ShowEquipmentDnsInfoRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ShowEquipmentDnsInfoResponse`
        """
        return self._show_equipment_dns_info_with_http_info(request)

    def _show_equipment_dns_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/lan-interface/dns',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEquipmentDnsInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_equipment_lan_info_async(self, request):
        """查询智能企业网关设备LAN口配置

        查询智能企业网关设备LAN口配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEquipmentLanInfo
        :type request: :class:`huaweicloudsdkec.v1.ShowEquipmentLanInfoRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ShowEquipmentLanInfoResponse`
        """
        return self._show_equipment_lan_info_with_http_info(request)

    def _show_equipment_lan_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/lan-interface',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEquipmentLanInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_equipment_dns_info_async(self, request):
        """更新智能企业网关设备主备DNS配置

        更新智能企业网关设备主备DNS配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEquipmentDnsInfo
        :type request: :class:`huaweicloudsdkec.v1.UpdateEquipmentDnsInfoRequest`
        :rtype: :class:`huaweicloudsdkec.v1.UpdateEquipmentDnsInfoResponse`
        """
        return self._update_equipment_dns_info_with_http_info(request)

    def _update_equipment_dns_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/lan-interface/dns',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEquipmentDnsInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_equipment_lan_config_async(self, request):
        """更新智能企业网关设备LAN口配置

        更新智能企业网关设备LAN口配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEquipmentLanConfig
        :type request: :class:`huaweicloudsdkec.v1.UpdateEquipmentLanConfigRequest`
        :rtype: :class:`huaweicloudsdkec.v1.UpdateEquipmentLanConfigResponse`
        """
        return self._update_equipment_lan_config_with_http_info(request)

    def _update_equipment_lan_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/lan-interface',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEquipmentLanConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_equipment_ospf_async(self, request):
        """查询智能企业网关设备OSPF配置

        查询智能企业网关设备OSPF配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEquipmentOspf
        :type request: :class:`huaweicloudsdkec.v1.ShowEquipmentOspfRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ShowEquipmentOspfResponse`
        """
        return self._show_equipment_ospf_with_http_info(request)

    def _show_equipment_ospf_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/ospf',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEquipmentOspfResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_equipment_ospf_async(self, request):
        """配置智能企业网关设备OSPF协议

        配置智能企业网关设备OSPF协议
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEquipmentOspf
        :type request: :class:`huaweicloudsdkec.v1.UpdateEquipmentOspfRequest`
        :rtype: :class:`huaweicloudsdkec.v1.UpdateEquipmentOspfResponse`
        """
        return self._update_equipment_ospf_with_http_info(request)

    def _update_equipment_ospf_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/ospf',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEquipmentOspfResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_equipment_static_route_config_async(self, request):
        """创建智能企业网关设备静态路由配置

        创建智能企业网关设备静态路由配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEquipmentStaticRouteConfig
        :type request: :class:`huaweicloudsdkec.v1.CreateEquipmentStaticRouteConfigRequest`
        :rtype: :class:`huaweicloudsdkec.v1.CreateEquipmentStaticRouteConfigResponse`
        """
        return self._create_equipment_static_route_config_with_http_info(request)

    def _create_equipment_static_route_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/static-route',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateEquipmentStaticRouteConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_equipment_static_route_config_async(self, request):
        """删除智能企业网关设备静态路由配置

        删除智能企业网关设备静态路由配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEquipmentStaticRouteConfig
        :type request: :class:`huaweicloudsdkec.v1.DeleteEquipmentStaticRouteConfigRequest`
        :rtype: :class:`huaweicloudsdkec.v1.DeleteEquipmentStaticRouteConfigResponse`
        """
        return self._delete_equipment_static_route_config_with_http_info(request)

    def _delete_equipment_static_route_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

        query_params = []
        if 'prefix' in local_var_params:
            query_params.append(('prefix', local_var_params['prefix']))
        if 'next_hop' in local_var_params:
            query_params.append(('next_hop', local_var_params['next_hop']))
        if 'interface_name' in local_var_params:
            query_params.append(('interface_name', local_var_params['interface_name']))

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/static-route',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEquipmentStaticRouteConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_equipment_static_route_info_async(self, request):
        """查询智能企业网关设备静态路由配置

        查询智能企业网关设备静态路由配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEquipmentStaticRouteInfo
        :type request: :class:`huaweicloudsdkec.v1.ShowEquipmentStaticRouteInfoRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ShowEquipmentStaticRouteInfoResponse`
        """
        return self._show_equipment_static_route_info_with_http_info(request)

    def _show_equipment_static_route_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/static-route',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEquipmentStaticRouteInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_equipment_static_route_config_async(self, request):
        """更新智能企业网关设备静态路由配置

        更新智能企业网关设备静态路由配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEquipmentStaticRouteConfig
        :type request: :class:`huaweicloudsdkec.v1.UpdateEquipmentStaticRouteConfigRequest`
        :rtype: :class:`huaweicloudsdkec.v1.UpdateEquipmentStaticRouteConfigResponse`
        """
        return self._update_equipment_static_route_config_with_http_info(request)

    def _update_equipment_static_route_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/static-route',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEquipmentStaticRouteConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_equipment_wan_info_async(self, request):
        """查询智能企业网关设备WAN口配置

        查询智能企业网关设备WAN口配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEquipmentWanInfo
        :type request: :class:`huaweicloudsdkec.v1.ShowEquipmentWanInfoRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ShowEquipmentWanInfoResponse`
        """
        return self._show_equipment_wan_info_with_http_info(request)

    def _show_equipment_wan_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/wan-interface',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEquipmentWanInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_equipment_wan_config_async(self, request):
        """更新智能企业网关设备WAN口配置

        更新智能企业网关设备WAN口配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEquipmentWanConfig
        :type request: :class:`huaweicloudsdkec.v1.UpdateEquipmentWanConfigRequest`
        :rtype: :class:`huaweicloudsdkec.v1.UpdateEquipmentWanConfigResponse`
        """
        return self._update_equipment_wan_config_with_http_info(request)

    def _update_equipment_wan_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'equipment_id' in local_var_params:
            path_params['equipment_id'] = local_var_params['equipment_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/equipment/{equipment_id}/wan-interface',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEquipmentWanConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_ecn_with_er_async(self, request):
        """关联企业路由器到企业连接网络

        关联企业路由器到企业连接网络
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddEcnWithEr
        :type request: :class:`huaweicloudsdkec.v1.AddEcnWithErRequest`
        :rtype: :class:`huaweicloudsdkec.v1.AddEcnWithErResponse`
        """
        return self._add_ecn_with_er_with_http_info(request)

    def _add_ecn_with_er_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ecn_id' in local_var_params:
            path_params['ecn_id'] = local_var_params['ecn_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/enterprise-connect-network/{ecn_id}/relationship/enterprise-router',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddEcnWithErResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_ecn_with_er_async(self, request):
        """解除企业路由器和企业连接网络的关联

        解除企业路由器和企业连接网络的关联
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEcnWithEr
        :type request: :class:`huaweicloudsdkec.v1.DeleteEcnWithErRequest`
        :rtype: :class:`huaweicloudsdkec.v1.DeleteEcnWithErResponse`
        """
        return self._delete_ecn_with_er_with_http_info(request)

    def _delete_ecn_with_er_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ecn_id' in local_var_params:
            path_params['ecn_id'] = local_var_params['ecn_id']
        if 'relation_id' in local_var_params:
            path_params['relation_id'] = local_var_params['relation_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/enterprise-connect-network/{ecn_id}/relationship/enterprise-router/{relation_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEcnWithErResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_ecn_with_er_async(self, request):
        """查询企业连接网络网与企业路由器关联关系

        根据企业连接网络ID，查询企业连接网络网与企业路由器关联关系
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEcnWithEr
        :type request: :class:`huaweicloudsdkec.v1.ListEcnWithErRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ListEcnWithErResponse`
        """
        return self._list_ecn_with_er_with_http_info(request)

    def _list_ecn_with_er_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ecn_id' in local_var_params:
            path_params['ecn_id'] = local_var_params['ecn_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/enterprise-connect-network/{ecn_id}/relationship/enterprise-router',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEcnWithErResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_ieg_password_async(self, request):
        """修改IEG设备admin账户密码

        修改IEG设备admin账户密码
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeIegPassword
        :type request: :class:`huaweicloudsdkec.v1.ChangeIegPasswordRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ChangeIegPasswordResponse`
        """
        return self._change_ieg_password_with_http_info(request)

    def _change_ieg_password_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/password',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeIegPasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_ieg_async(self, request):
        """查询租户智能企业网关列表

        查询租户智能企业网关列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListIeg
        :type request: :class:`huaweicloudsdkec.v1.ListIegRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ListIegResponse`
        """
        return self._list_ieg_with_http_info(request)

    def _list_ieg_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListIegResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_ieg_info_async(self, request):
        """查询租户单个智能企业网关

        根据智能企业网关ID，查询租户智能企业网关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowIegInfo
        :type request: :class:`huaweicloudsdkec.v1.ShowIegInfoRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ShowIegInfoResponse`
        """
        return self._show_ieg_info_with_http_info(request)

    def _show_ieg_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowIegInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def switch_equipment_ha_type_async(self, request):
        """交换双机主备属性

        交换双机主备属性
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SwitchEquipmentHaType
        :type request: :class:`huaweicloudsdkec.v1.SwitchEquipmentHaTypeRequest`
        :rtype: :class:`huaweicloudsdkec.v1.SwitchEquipmentHaTypeResponse`
        """
        return self._switch_equipment_ha_type_with_http_info(request)

    def _switch_equipment_ha_type_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/switch-ha-type',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SwitchEquipmentHaTypeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_ieg_async(self, request):
        """更新智能企业网关

        根据智能企业网关ID，更新智能企业网关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateIeg
        :type request: :class:`huaweicloudsdkec.v1.UpdateIegRequest`
        :rtype: :class:`huaweicloudsdkec.v1.UpdateIegResponse`
        """
        return self._update_ieg_with_http_info(request)

    def _update_ieg_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateIegResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_quotas_info_async(self, request):
        """查询EC相关的指定租户的配额

        查询EC相关的指定租户的配额
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowQuotasInfo
        :type request: :class:`huaweicloudsdkec.v1.ShowQuotasInfoRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ShowQuotasInfoResponse`
        """
        return self._show_quotas_info_with_http_info(request)

    def _show_quotas_info_with_http_info(self, request):
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
            resource_path='/v1/enterprise-connect/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowQuotasInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_vrrp_config_async(self, request):
        """创建vrrp配置

        创建vrrp配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddVrrpConfig
        :type request: :class:`huaweicloudsdkec.v1.AddVrrpConfigRequest`
        :rtype: :class:`huaweicloudsdkec.v1.AddVrrpConfigResponse`
        """
        return self._add_vrrp_config_with_http_info(request)

    def _add_vrrp_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/vrrp-config',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddVrrpConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_vrrp_config_async(self, request):
        """删除vrrp配置

        删除vrrp配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteVrrpConfig
        :type request: :class:`huaweicloudsdkec.v1.DeleteVrrpConfigRequest`
        :rtype: :class:`huaweicloudsdkec.v1.DeleteVrrpConfigResponse`
        """
        return self._delete_vrrp_config_with_http_info(request)

    def _delete_vrrp_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'virtual_router_id' in local_var_params:
            path_params['virtual_router_id'] = local_var_params['virtual_router_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/vrrp-config/{virtual_router_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteVrrpConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_vrrp_config_async(self, request):
        """查询vrrp配置列表

        查询vrrp配置列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVrrpConfig
        :type request: :class:`huaweicloudsdkec.v1.ShowVrrpConfigRequest`
        :rtype: :class:`huaweicloudsdkec.v1.ShowVrrpConfigResponse`
        """
        return self._show_vrrp_config_with_http_info(request)

    def _show_vrrp_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/vrrp-config',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowVrrpConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_vrrp_config_async(self, request):
        """更新vrrp配置

        更新vrrp配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateVrrpConfig
        :type request: :class:`huaweicloudsdkec.v1.UpdateVrrpConfigRequest`
        :rtype: :class:`huaweicloudsdkec.v1.UpdateVrrpConfigResponse`
        """
        return self._update_vrrp_config_with_http_info(request)

    def _update_vrrp_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ieg_id' in local_var_params:
            path_params['ieg_id'] = local_var_params['ieg_id']
        if 'virtual_router_id' in local_var_params:
            path_params['virtual_router_id'] = local_var_params['virtual_router_id']

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
            resource_path='/v1/{domain_id}/enterprise-connect/intelligent-enterprise-gateway/{ieg_id}/vrrp-config/{virtual_router_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateVrrpConfigResponse',
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
