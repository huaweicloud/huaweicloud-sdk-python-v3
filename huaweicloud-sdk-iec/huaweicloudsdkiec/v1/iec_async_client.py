# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class IecAsyncClient(Client):
    def __init__(self):
        super(IecAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkiec.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials")
        else:
            if clazz.__name__ != "IecAsyncClient":
                raise TypeError("client type error, support client type is IecAsyncClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials")

        

        return client_builder

    def add_nics_async(self, request):
        """添加网卡

        添加网卡。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddNics
        :type request: :class:`huaweicloudsdkiec.v1.AddNicsRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.AddNicsResponse`
        """
        return self._add_nics_with_http_info(request)

    def _add_nics_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v1/cloudservers/{instance_id}/nics',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddNicsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_subnet_async(self, request):
        """路由表关联子网

        路由表关联子网
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateSubnet
        :type request: :class:`huaweicloudsdkiec.v1.AssociateSubnetRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.AssociateSubnetResponse`
        """
        return self._associate_subnet_with_http_info(request)

    def _associate_subnet_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

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
            resource_path='/v1/routetables/{routetable_id}/associate-subnets',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociateSubnetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_reboot_instance_async(self, request):
        """批量重启边缘实例

        批量重启边缘实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchRebootInstance
        :type request: :class:`huaweicloudsdkiec.v1.BatchRebootInstanceRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.BatchRebootInstanceResponse`
        """
        return self._batch_reboot_instance_with_http_info(request)

    def _batch_reboot_instance_with_http_info(self, request):
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
            resource_path='/v1/cloudservers/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchRebootInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_start_instance_async(self, request):
        """批量启动边缘实例

        批量操作启动边缘实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchStartInstance
        :type request: :class:`huaweicloudsdkiec.v1.BatchStartInstanceRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.BatchStartInstanceResponse`
        """
        return self._batch_start_instance_with_http_info(request)

    def _batch_start_instance_with_http_info(self, request):
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
            resource_path='/v1/cloudservers/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchStartInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_stop_instance_async(self, request):
        """批量关机边缘实例

        批量关闭边缘实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchStopInstance
        :type request: :class:`huaweicloudsdkiec.v1.BatchStopInstanceRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.BatchStopInstanceResponse`
        """
        return self._batch_stop_instance_with_http_info(request)

    def _batch_stop_instance_with_http_info(self, request):
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
            resource_path='/v1/cloudservers/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchStopInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_os_async(self, request):
        """切换操作系统

        切换边缘实例操作系统，支持边缘实例创建成功后，保持ip、数据盘不变的情况下重装操作系统。
        
        调用该接口后，系统将卸载系统盘，然后使用新镜像重新创建系统盘，并挂载至实例，实现切换操作系统功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeOs
        :type request: :class:`huaweicloudsdkiec.v1.ChangeOsRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ChangeOsResponse`
        """
        return self._change_os_with_http_info(request)

    def _change_os_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v1/cloudservers/{instance_id}/change-os',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeOsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_deployment_async(self, request):
        """创建部署计划

        为方便您的统一管理，以及跨边缘站点管理资源，IEC基于业务场景角度，定义了边缘业务。
        边缘业务即为逻辑层面的一套资源管理集合。这里的资源主要是指计算实例，包含实例规格、镜像、硬盘、网络等方面。通过指定计算实例的数量、调度策略以及区域分布等形成一套管理集合。[了解更多](https://support.huaweicloud.com/usermanual-iec/iec_02_0301.html)
        
        创建一个部署计划并执行，即可创建一个边缘业务。
        
        - 边缘业务下实例分布取决于部署计划的实例分布与调度策略。
        - 边缘业务下实例名称、规格、镜像等参数取决于部署计划配置计算实例字段。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDeployment
        :type request: :class:`huaweicloudsdkiec.v1.CreateDeploymentRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.CreateDeploymentResponse`
        """
        return self._create_deployment_with_http_info(request)

    def _create_deployment_with_http_info(self, request):
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
            resource_path='/v1/deployments',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDeploymentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_image_async(self, request):
        """从边缘实例创建边缘私有镜像

        使用指定边缘实例的系统盘创建边缘私有镜像。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateImage
        :type request: :class:`huaweicloudsdkiec.v1.CreateImageRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.CreateImageResponse`
        """
        return self._create_image_with_http_info(request)

    def _create_image_with_http_info(self, request):
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
            resource_path='/v1/images/create',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_keypair_async(self, request):
        """创建和导入密钥

        创建SSH密钥，或把公钥导入系统，生成密钥对。
        
        创建SSH密钥成功后，请把响应数据中的私钥内容保存到本地文件，用户使用该私钥登录边缘实例。为保证边缘实例安全，私钥数据只能读取一次，请妥善保管。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateKeypair
        :type request: :class:`huaweicloudsdkiec.v1.CreateKeypairRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.CreateKeypairResponse`
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/os-keypairs',
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

    def create_port_async(self, request):
        """创建端口

        创建端口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePort
        :type request: :class:`huaweicloudsdkiec.v1.CreatePortRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.CreatePortResponse`
        """
        return self._create_port_with_http_info(request)

    def _create_port_with_http_info(self, request):
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
            resource_path='/v1/ports',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePortResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_routes_async(self, request):
        """创建路由

        创建路由
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRoutes
        :type request: :class:`huaweicloudsdkiec.v1.CreateRoutesRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.CreateRoutesResponse`
        """
        return self._create_routes_with_http_info(request)

    def _create_routes_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

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
            resource_path='/v1/routetables/{routetable_id}/add-routes',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateRoutesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_routetable_async(self, request):
        """创建路由表

        创建路由表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRoutetable
        :type request: :class:`huaweicloudsdkiec.v1.CreateRoutetableRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.CreateRoutetableResponse`
        """
        return self._create_routetable_with_http_info(request)

    def _create_routetable_with_http_info(self, request):
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
            resource_path='/v1/routetables',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateRoutetableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_security_group_async(self, request):
        """创建边缘安全组

        根据用户的请求内容，创建对应的安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSecurityGroup
        :type request: :class:`huaweicloudsdkiec.v1.CreateSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.CreateSecurityGroupResponse`
        """
        return self._create_security_group_with_http_info(request)

    def _create_security_group_with_http_info(self, request):
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
            resource_path='/v1/security-groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSecurityGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_security_group_rule_async(self, request):
        """创建安全组规则

        根据用户的请求内容，创建安全组规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSecurityGroupRule
        :type request: :class:`huaweicloudsdkiec.v1.CreateSecurityGroupRuleRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.CreateSecurityGroupRuleResponse`
        """
        return self._create_security_group_rule_with_http_info(request)

    def _create_security_group_rule_with_http_info(self, request):
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
            resource_path='/v1/security-group-rules',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSecurityGroupRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_vpc_async(self, request):
        """创建虚拟私有云

        根据用户的请求内容，创建虚拟私有云。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVpc
        :type request: :class:`huaweicloudsdkiec.v1.CreateVpcRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.CreateVpcResponse`
        """
        return self._create_vpc_with_http_info(request)

    def _create_vpc_with_http_info(self, request):
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
            resource_path='/v1/vpcs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateVpcResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_bandwidth_async(self, request):
        """删除带宽

        删除带宽。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBandwidth
        :type request: :class:`huaweicloudsdkiec.v1.DeleteBandwidthRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeleteBandwidthResponse`
        """
        return self._delete_bandwidth_with_http_info(request)

    def _delete_bandwidth_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'bandwidth_id' in local_var_params:
            path_params['bandwidth_id'] = local_var_params['bandwidth_id']

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
            resource_path='/v1/bandwidths/{bandwidth_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteBandwidthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_deployment_async(self, request):
        """删除部署计划

        删除部署计划。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDeployment
        :type request: :class:`huaweicloudsdkiec.v1.DeleteDeploymentRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeleteDeploymentResponse`
        """
        return self._delete_deployment_with_http_info(request)

    def _delete_deployment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

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
            resource_path='/v1/deployments/{deployment_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDeploymentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_edge_cloud_async(self, request):
        """删除边缘业务

        删除边缘业务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEdgeCloud
        :type request: :class:`huaweicloudsdkiec.v1.DeleteEdgeCloudRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeleteEdgeCloudResponse`
        """
        return self._delete_edge_cloud_with_http_info(request)

    def _delete_edge_cloud_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edgecloud_id' in local_var_params:
            path_params['edgecloud_id'] = local_var_params['edgecloud_id']

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
            resource_path='/v1/edgeclouds/{edgecloud_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEdgeCloudResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_image_async(self, request):
        """删除边缘私有镜像

        将指定ID的边缘私有镜像删除
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteImage
        :type request: :class:`huaweicloudsdkiec.v1.DeleteImageRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeleteImageResponse`
        """
        return self._delete_image_with_http_info(request)

    def _delete_image_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v1/images/{image_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_instances_async(self, request):
        """批量删除边缘实例

        批量删除边缘实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteInstances
        :type request: :class:`huaweicloudsdkiec.v1.DeleteInstancesRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeleteInstancesResponse`
        """
        return self._delete_instances_with_http_info(request)

    def _delete_instances_with_http_info(self, request):
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
            resource_path='/v1/cloudservers/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_keypair_async(self, request):
        """删除密钥

        删除密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteKeypair
        :type request: :class:`huaweicloudsdkiec.v1.DeleteKeypairRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeleteKeypairResponse`
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
            resource_path='/v1/os-keypairs/{keypair_name}',
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

    def delete_nics_async(self, request):
        """删除网卡

        删除网卡。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteNics
        :type request: :class:`huaweicloudsdkiec.v1.DeleteNicsRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeleteNicsResponse`
        """
        return self._delete_nics_with_http_info(request)

    def _delete_nics_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v1/cloudservers/{instance_id}/nics/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteNicsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_port_async(self, request):
        """删除端口

        删除端口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePort
        :type request: :class:`huaweicloudsdkiec.v1.DeletePortRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeletePortResponse`
        """
        return self._delete_port_with_http_info(request)

    def _delete_port_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

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
            resource_path='/v1/ports/{port_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePortResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_routes_async(self, request):
        """删除路由

        删除路由
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRoutes
        :type request: :class:`huaweicloudsdkiec.v1.DeleteRoutesRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeleteRoutesResponse`
        """
        return self._delete_routes_with_http_info(request)

    def _delete_routes_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

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
            resource_path='/v1/routetables/{routetable_id}/delete-routes',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteRoutesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_routetable_async(self, request):
        """删除路由表

        删除路由表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRoutetable
        :type request: :class:`huaweicloudsdkiec.v1.DeleteRoutetableRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeleteRoutetableResponse`
        """
        return self._delete_routetable_with_http_info(request)

    def _delete_routetable_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

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
            resource_path='/v1/routetables/{routetable_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteRoutetableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_security_group_async(self, request):
        """删除安全组

        根据安全组的ID，删除对应的安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSecurityGroup
        :type request: :class:`huaweicloudsdkiec.v1.DeleteSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeleteSecurityGroupResponse`
        """
        return self._delete_security_group_with_http_info(request)

    def _delete_security_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_group_id' in local_var_params:
            path_params['security_group_id'] = local_var_params['security_group_id']

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
            resource_path='/v1/security-groups/{security_group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSecurityGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_security_group_rule_async(self, request):
        """删除安全组规则

        根据安全组的ID，删除对应的安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSecurityGroupRule
        :type request: :class:`huaweicloudsdkiec.v1.DeleteSecurityGroupRuleRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeleteSecurityGroupRuleResponse`
        """
        return self._delete_security_group_rule_with_http_info(request)

    def _delete_security_group_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_group_rule_id' in local_var_params:
            path_params['security_group_rule_id'] = local_var_params['security_group_rule_id']

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
            resource_path='/v1/security-group-rules/{security_group_rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSecurityGroupRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_subnet_async(self, request):
        """删除子网

        根据子网的ID，删除子网。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSubnet
        :type request: :class:`huaweicloudsdkiec.v1.DeleteSubnetRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeleteSubnetResponse`
        """
        return self._delete_subnet_with_http_info(request)

    def _delete_subnet_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

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
            resource_path='/v1/subnets/{subnet_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSubnetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_vpc_async(self, request):
        """删除虚拟私有云

        根据虚拟机私有云的ID，删除对应的虚拟私有云。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteVpc
        :type request: :class:`huaweicloudsdkiec.v1.DeleteVpcRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeleteVpcResponse`
        """
        return self._delete_vpc_with_http_info(request)

    def _delete_vpc_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']

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
            resource_path='/v1/vpcs/{vpc_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteVpcResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disassociate_subnet_async(self, request):
        """路由表解关联子网

        路由表解关联子网
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateSubnet
        :type request: :class:`huaweicloudsdkiec.v1.DisassociateSubnetRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DisassociateSubnetResponse`
        """
        return self._disassociate_subnet_with_http_info(request)

    def _disassociate_subnet_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

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
            resource_path='/v1/routetables/{routetable_id}/disassociate-subnets',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisassociateSubnetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_deployment_async(self, request):
        """执行部署计划

        执行部署计划，创建一个边缘业务。单租户默认可创建10个边缘业务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteDeployment
        :type request: :class:`huaweicloudsdkiec.v1.ExecuteDeploymentRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ExecuteDeploymentResponse`
        """
        return self._execute_deployment_with_http_info(request)

    def _execute_deployment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

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
            resource_path='/v1/deployments/{deployment_id}/deploy',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteDeploymentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def expand_edgecloud_async(self, request):
        """扩容边缘业务

        执行部署计划，对边缘业务进行扩容操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExpandEdgecloud
        :type request: :class:`huaweicloudsdkiec.v1.ExpandEdgecloudRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ExpandEdgecloudResponse`
        """
        return self._expand_edgecloud_with_http_info(request)

    def _expand_edgecloud_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

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
            resource_path='/v1/deployments/{deployment_id}/expand',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExpandEdgecloudResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_bandwidths_async(self, request):
        """查询带宽列表

        查询带宽列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBandwidths
        :type request: :class:`huaweicloudsdkiec.v1.ListBandwidthsRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListBandwidthsResponse`
        """
        return self._list_bandwidths_with_http_info(request)

    def _list_bandwidths_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'site_id' in local_var_params:
            query_params.append(('site_id', local_var_params['site_id']))

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
            resource_path='/v1/bandwidths',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBandwidthsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_cloud_images_async(self, request):
        """查询中心镜像列表

        查询租户在某个云Region的可见镜像列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCloudImages
        :type request: :class:`huaweicloudsdkiec.v1.ListCloudImagesRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListCloudImagesResponse`
        """
        return self._list_cloud_images_with_http_info(request)

    def _list_cloud_images_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'region_id' in local_var_params:
            path_params['region_id'] = local_var_params['region_id']

        query_params = []
        if 'imagetype' in local_var_params:
            query_params.append(('__imagetype', local_var_params['imagetype']))
        if 'isregistered' in local_var_params:
            query_params.append(('__isregistered', local_var_params['isregistered']))
        if 'os_type' in local_var_params:
            query_params.append(('__os_type', local_var_params['os_type']))
        if 'support_diskintensive' in local_var_params:
            query_params.append(('__support_diskintensive', local_var_params['support_diskintensive']))
        if 'support_highperformance' in local_var_params:
            query_params.append(('__support_highperformance', local_var_params['support_highperformance']))
        if 'support_kvm' in local_var_params:
            query_params.append(('__support_kvm', local_var_params['support_kvm']))
        if 'support_kvm_gpu_type' in local_var_params:
            query_params.append(('__support_kvm_gpu_type', local_var_params['support_kvm_gpu_type']))
        if 'support_kvm_infiniband' in local_var_params:
            query_params.append(('__support_kvm_infiniband', local_var_params['support_kvm_infiniband']))
        if 'support_largememory' in local_var_params:
            query_params.append(('__support_largememory', local_var_params['support_largememory']))
        if 'support_xen' in local_var_params:
            query_params.append(('__support_xen', local_var_params['support_xen']))
        if 'support_xen_gpu_type' in local_var_params:
            query_params.append(('__support_xen_gpu_type', local_var_params['support_xen_gpu_type']))
        if 'support_xen_hana' in local_var_params:
            query_params.append(('__support_xen_hana', local_var_params['support_xen_hana']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'owner' in local_var_params:
            query_params.append(('owner', local_var_params['owner']))
        if 'protected' in local_var_params:
            query_params.append(('protected', local_var_params['protected']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'virtual_env_type' in local_var_params:
            query_params.append(('virtual_env_type', local_var_params['virtual_env_type']))
        if 'visibility' in local_var_params:
            query_params.append(('visibility', local_var_params['visibility']))

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
            resource_path='/v1/cloudimages/{region_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCloudImagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_deployments_async(self, request):
        """查询部署计划列表

        查询部署计划列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDeployments
        :type request: :class:`huaweicloudsdkiec.v1.ListDeploymentsRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListDeploymentsResponse`
        """
        return self._list_deployments_with_http_info(request)

    def _list_deployments_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'edgecloud_id' in local_var_params:
            query_params.append(('edgecloud_id', local_var_params['edgecloud_id']))

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
            resource_path='/v1/deployments',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDeploymentsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_edge_cloud_async(self, request):
        """查询边缘业务列表

        查询边缘业务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEdgeCloud
        :type request: :class:`huaweicloudsdkiec.v1.ListEdgeCloudRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListEdgeCloudResponse`
        """
        return self._list_edge_cloud_with_http_info(request)

    def _list_edge_cloud_with_http_info(self, request):
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
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))

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
            resource_path='/v1/edgeclouds',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEdgeCloudResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_flavors_async(self, request):
        """查询边缘规格列表

        查询边缘规格列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFlavors
        :type request: :class:`huaweicloudsdkiec.v1.ListFlavorsRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListFlavorsResponse`
        """
        return self._list_flavors_with_http_info(request)

    def _list_flavors_with_http_info(self, request):
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
        if 'area' in local_var_params:
            query_params.append(('area', local_var_params['area']))
        if 'province' in local_var_params:
            query_params.append(('province', local_var_params['province']))
        if 'city' in local_var_params:
            query_params.append(('city', local_var_params['city']))
        if 'operator' in local_var_params:
            query_params.append(('operator', local_var_params['operator']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'site_ids' in local_var_params:
            query_params.append(('site_ids', local_var_params['site_ids']))

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
            resource_path='/v1/cloudservers/flavors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFlavorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_images_async(self, request):
        """查询镜像列表

        根据不同条件查询镜像列表，例:
        
        -  查询已注册的私有镜像列表: visibility&#x3D;private
        - 公共镜像: visibility&#x3D;public
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListImages
        :type request: :class:`huaweicloudsdkiec.v1.ListImagesRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListImagesResponse`
        """
        return self._list_images_with_http_info(request)

    def _list_images_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'imagetype' in local_var_params:
            query_params.append(('__imagetype', local_var_params['imagetype']))
        if 'protected' in local_var_params:
            query_params.append(('protected', local_var_params['protected']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'visibility' in local_var_params:
            query_params.append(('visibility', local_var_params['visibility']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'os_type' in local_var_params:
            query_params.append(('__os_type', local_var_params['os_type']))
        if 'virtual_env_type' in local_var_params:
            query_params.append(('virtual_env_type', local_var_params['virtual_env_type']))
        if 'isregistered' in local_var_params:
            query_params.append(('__isregistered', local_var_params['isregistered']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'support_kvm' in local_var_params:
            query_params.append(('__support_kvm', local_var_params['support_kvm']))
        if 'support_kvm_gpu_type' in local_var_params:
            query_params.append(('__support_kvm_gpu_type', local_var_params['support_kvm_gpu_type']))
        if 'support_kvm_ascend_310' in local_var_params:
            query_params.append(('__support_kvm_ascend_310', local_var_params['support_kvm_ascend_310']))
        if 'support_kvm_hi1822_hiovs' in local_var_params:
            query_params.append(('__support_kvm_hi1822_hiovs', local_var_params['support_kvm_hi1822_hiovs']))
        if 'support_arm' in local_var_params:
            query_params.append(('__support_arm', local_var_params['support_arm']))
        if 'support_gpu_t4' in local_var_params:
            query_params.append(('__support_gpu_t4', local_var_params['support_gpu_t4']))

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
            resource_path='/v1/images',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListImagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instances_async(self, request):
        """查询边缘实例列表

        查询边缘实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstances
        :type request: :class:`huaweicloudsdkiec.v1.ListInstancesRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListInstancesResponse`
        """
        return self._list_instances_with_http_info(request)

    def _list_instances_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'area' in local_var_params:
            query_params.append(('area', local_var_params['area']))
        if 'province' in local_var_params:
            query_params.append(('province', local_var_params['province']))
        if 'city' in local_var_params:
            query_params.append(('city', local_var_params['city']))
        if 'edgecloud_id' in local_var_params:
            query_params.append(('edgecloud_id', local_var_params['edgecloud_id']))
        if 'site_id' in local_var_params:
            query_params.append(('site_id', local_var_params['site_id']))

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
            resource_path='/v1/cloudservers',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_keypairs_async(self, request):
        """查询密钥列表

        查询密钥信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKeypairs
        :type request: :class:`huaweicloudsdkiec.v1.ListKeypairsRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListKeypairsResponse`
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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
            resource_path='/v1/os-keypairs',
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

    def list_ports_async(self, request):
        """查询端口列表

        查询端口的列表信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPorts
        :type request: :class:`huaweicloudsdkiec.v1.ListPortsRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListPortsResponse`
        """
        return self._list_ports_with_http_info(request)

    def _list_ports_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'network_id' in local_var_params:
            query_params.append(('network_id', local_var_params['network_id']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'fixed_ips' in local_var_params:
            query_params.append(('fixed_ips', local_var_params['fixed_ips']))
            collection_formats['fixed_ips'] = 'multi'
        if 'mac_address' in local_var_params:
            query_params.append(('mac_address', local_var_params['mac_address']))
        if 'device_id' in local_var_params:
            query_params.append(('device_id', local_var_params['device_id']))
        if 'device_owner' in local_var_params:
            query_params.append(('device_owner', local_var_params['device_owner']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'security_groups' in local_var_params:
            query_params.append(('security_groups', local_var_params['security_groups']))

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
            resource_path='/v1/ports',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPortsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_quota_async(self, request):
        """查询配额

        查询租户资源配额。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListQuota
        :type request: :class:`huaweicloudsdkiec.v1.ListQuotaRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListQuotaResponse`
        """
        return self._list_quota_with_http_info(request)

    def _list_quota_with_http_info(self, request):
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
            resource_path='/v1/edgeclouds/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_related_routetables_async(self, request):
        """查询子网关联的路由表

        查询子网关联的路由表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRelatedRoutetables
        :type request: :class:`huaweicloudsdkiec.v1.ListRelatedRoutetablesRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListRelatedRoutetablesResponse`
        """
        return self._list_related_routetables_with_http_info(request)

    def _list_related_routetables_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

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
            resource_path='/v1/subnets/{subnet_id}/routetables',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRelatedRoutetablesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_routes_async(self, request):
        """查询路由列表

        查询路由列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRoutes
        :type request: :class:`huaweicloudsdkiec.v1.ListRoutesRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListRoutesResponse`
        """
        return self._list_routes_with_http_info(request)

    def _list_routes_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

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
            resource_path='/v1/routetables/{routetable_id}/routes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRoutesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_routetables_async(self, request):
        """查询路由表列表

        查询路由列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRoutetables
        :type request: :class:`huaweicloudsdkiec.v1.ListRoutetablesRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListRoutetablesResponse`
        """
        return self._list_routetables_with_http_info(request)

    def _list_routetables_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))

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
            resource_path='/v1/routetables',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRoutetablesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_security_group_rules_async(self, request):
        """查询安全组规则列表

        根据用户的查询条件，获取安全组规则的列表信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSecurityGroupRules
        :type request: :class:`huaweicloudsdkiec.v1.ListSecurityGroupRulesRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListSecurityGroupRulesResponse`
        """
        return self._list_security_group_rules_with_http_info(request)

    def _list_security_group_rules_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'security_group_id' in local_var_params:
            query_params.append(('security_group_id', local_var_params['security_group_id']))

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
            resource_path='/v1/security-group-rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSecurityGroupRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_security_groups_async(self, request):
        """查询安全组列表

        根据特定查询条件，获取安全组的列表信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSecurityGroups
        :type request: :class:`huaweicloudsdkiec.v1.ListSecurityGroupsRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListSecurityGroupsResponse`
        """
        return self._list_security_groups_with_http_info(request)

    def _list_security_groups_with_http_info(self, request):
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
            resource_path='/v1/security-groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSecurityGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_sites_async(self, request):
        """查询边缘站点列表

        查询边缘站点列表。
        
        - 边缘站点：靠近终端应用的位置，基于一个或多个运营商建立的一个城市级站点。边缘站点提供物理隔离的资源池，提供多元算力、存储和网络的能力。用户可以将业务灵活就近部署在边缘站点上，以降低网络时延和成本。
        - 边缘区域：为依据边缘站点的物理位置划分的区域，一个边缘区域包含多个相靠近的边缘站点的集合。IEC当前提供城市级、省级和大区级三个分布层级的边缘区域。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSites
        :type request: :class:`huaweicloudsdkiec.v1.ListSitesRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListSitesResponse`
        """
        return self._list_sites_with_http_info(request)

    def _list_sites_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'area' in local_var_params:
            query_params.append(('area', local_var_params['area']))
        if 'province' in local_var_params:
            query_params.append(('province', local_var_params['province']))
        if 'city' in local_var_params:
            query_params.append(('city', local_var_params['city']))
        if 'flavor' in local_var_params:
            query_params.append(('flavor', local_var_params['flavor']))
        if 'volume_type' in local_var_params:
            query_params.append(('volume_type', local_var_params['volume_type']))

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
            resource_path='/v1/sites',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSitesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_subnets_async(self, request):
        """查询子网列表

        根据查询条件获取子网的列表信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSubnets
        :type request: :class:`huaweicloudsdkiec.v1.ListSubnetsRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListSubnetsResponse`
        """
        return self._list_subnets_with_http_info(request)

    def _list_subnets_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'site_id' in local_var_params:
            query_params.append(('site_id', local_var_params['site_id']))

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
            resource_path='/v1/subnets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSubnetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_vpcs_async(self, request):
        """查询虚拟私有云列表

        获取虚拟私有云的列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVpcs
        :type request: :class:`huaweicloudsdkiec.v1.ListVpcsRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListVpcsResponse`
        """
        return self._list_vpcs_with_http_info(request)

    def _list_vpcs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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
            resource_path='/v1/vpcs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListVpcsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def rebuild_image_async(self, request):
        """重试边缘镜像任务

        重试边缘镜像任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RebuildImage
        :type request: :class:`huaweicloudsdkiec.v1.RebuildImageRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.RebuildImageResponse`
        """
        return self._rebuild_image_with_http_info(request)

    def _rebuild_image_with_http_info(self, request):
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{domain_id}/jobs/{job_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RebuildImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def register_image_async(self, request):
        """注册边缘私有镜像

        将指定Region和ID的IMS镜像注册到边缘IEC-IMS; 
        注意指定的Region必须在当前IEC-IMS支持的Region列表中。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RegisterImage
        :type request: :class:`huaweicloudsdkiec.v1.RegisterImageRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.RegisterImageResponse`
        """
        return self._register_image_with_http_info(request)

    def _register_image_with_http_info(self, request):
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
            resource_path='/v1/images/register',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RegisterImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_bandwidth_async(self, request):
        """查询带宽详情

        查询带宽详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBandwidth
        :type request: :class:`huaweicloudsdkiec.v1.ShowBandwidthRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowBandwidthResponse`
        """
        return self._show_bandwidth_with_http_info(request)

    def _show_bandwidth_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'bandwidth_id' in local_var_params:
            path_params['bandwidth_id'] = local_var_params['bandwidth_id']

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
            resource_path='/v1/bandwidths/{bandwidth_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowBandwidthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_edge_cloud_async(self, request):
        """查询边缘业务详情

        查询边缘业务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEdgeCloud
        :type request: :class:`huaweicloudsdkiec.v1.ShowEdgeCloudRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowEdgeCloudResponse`
        """
        return self._show_edge_cloud_with_http_info(request)

    def _show_edge_cloud_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edgecloud_id' in local_var_params:
            path_params['edgecloud_id'] = local_var_params['edgecloud_id']

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
            resource_path='/v1/edgeclouds/{edgecloud_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEdgeCloudResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_image_async(self, request):
        """查询镜像详情

        查询镜像详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowImage
        :type request: :class:`huaweicloudsdkiec.v1.ShowImageRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowImageResponse`
        """
        return self._show_image_with_http_info(request)

    def _show_image_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v1/images/{image_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_instance_async(self, request):
        """查询边缘实例详情

        查询边缘实例详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstance
        :type request: :class:`huaweicloudsdkiec.v1.ShowInstanceRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowInstanceResponse`
        """
        return self._show_instance_with_http_info(request)

    def _show_instance_with_http_info(self, request):
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
            resource_path='/v1/cloudservers/{server_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_keypair_async(self, request):
        """查询密钥详情

        查询密钥信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowKeypair
        :type request: :class:`huaweicloudsdkiec.v1.ShowKeypairRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowKeypairResponse`
        """
        return self._show_keypair_with_http_info(request)

    def _show_keypair_with_http_info(self, request):
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
            resource_path='/v1/os-keypairs/{keypair_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowKeypairResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_port_async(self, request):
        """查询端口详情

        根据端口的ID，获取端口的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPort
        :type request: :class:`huaweicloudsdkiec.v1.ShowPortRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowPortResponse`
        """
        return self._show_port_with_http_info(request)

    def _show_port_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

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
            resource_path='/v1/ports/{port_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPortResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_routetable_async(self, request):
        """查询路由表详情

        查询路由表详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRoutetable
        :type request: :class:`huaweicloudsdkiec.v1.ShowRoutetableRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowRoutetableResponse`
        """
        return self._show_routetable_with_http_info(request)

    def _show_routetable_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

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
            resource_path='/v1/routetables/{routetable_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowRoutetableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_security_group_async(self, request):
        """查询安全组详情

        根据安全组的ID，获取特定安全组的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSecurityGroup
        :type request: :class:`huaweicloudsdkiec.v1.ShowSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowSecurityGroupResponse`
        """
        return self._show_security_group_with_http_info(request)

    def _show_security_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_group_id' in local_var_params:
            path_params['security_group_id'] = local_var_params['security_group_id']

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
            resource_path='/v1/security-groups/{security_group_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSecurityGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_security_group_rule_async(self, request):
        """查询安全组规则详情

        根据安全组规则的ID，获取安全组规则的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSecurityGroupRule
        :type request: :class:`huaweicloudsdkiec.v1.ShowSecurityGroupRuleRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowSecurityGroupRuleResponse`
        """
        return self._show_security_group_rule_with_http_info(request)

    def _show_security_group_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_group_rule_id' in local_var_params:
            path_params['security_group_rule_id'] = local_var_params['security_group_rule_id']

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
            resource_path='/v1/security-group-rules/{security_group_rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSecurityGroupRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_subnet_async(self, request):
        """查询子网详情

        根据子网的ID，获取子网的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSubnet
        :type request: :class:`huaweicloudsdkiec.v1.ShowSubnetRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowSubnetResponse`
        """
        return self._show_subnet_with_http_info(request)

    def _show_subnet_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

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
            resource_path='/v1/subnets/{subnet_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSubnetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_volume_async(self, request):
        """查询硬盘详情

        查询硬盘详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVolume
        :type request: :class:`huaweicloudsdkiec.v1.ShowVolumeRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowVolumeResponse`
        """
        return self._show_volume_with_http_info(request)

    def _show_volume_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

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
            resource_path='/v1/cloudvolumes/{volume_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowVolumeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_volume_types_async(self, request):
        """查询硬盘类型列表

        查询硬盘类型列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVolumeTypes
        :type request: :class:`huaweicloudsdkiec.v1.ShowVolumeTypesRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowVolumeTypesResponse`
        """
        return self._show_volume_types_with_http_info(request)

    def _show_volume_types_with_http_info(self, request):
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
            resource_path='/v1/cloudvolumes/volume-types',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowVolumeTypesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_vpc_async(self, request):
        """查询虚拟私有云详情

        根据虚拟私有云ID，获取虚拟私有云的详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVpc
        :type request: :class:`huaweicloudsdkiec.v1.ShowVpcRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowVpcResponse`
        """
        return self._show_vpc_with_http_info(request)

    def _show_vpc_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']

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
            resource_path='/v1/vpcs/{vpc_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowVpcResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_bandwidth_async(self, request):
        """更新带宽

        更新带宽。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateBandwidth
        :type request: :class:`huaweicloudsdkiec.v1.UpdateBandwidthRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.UpdateBandwidthResponse`
        """
        return self._update_bandwidth_with_http_info(request)

    def _update_bandwidth_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'bandwidth_id' in local_var_params:
            path_params['bandwidth_id'] = local_var_params['bandwidth_id']

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
            resource_path='/v1/bandwidths/{bandwidth_id}',
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

    def update_instance_async(self, request):
        """修改边缘实例

        修改边缘实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstance
        :type request: :class:`huaweicloudsdkiec.v1.UpdateInstanceRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.UpdateInstanceResponse`
        """
        return self._update_instance_with_http_info(request)

    def _update_instance_with_http_info(self, request):
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
            resource_path='/v1/cloudservers/{server_id}',
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

    def update_port_async(self, request):
        """更新端口

        更新端口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePort
        :type request: :class:`huaweicloudsdkiec.v1.UpdatePortRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.UpdatePortResponse`
        """
        return self._update_port_with_http_info(request)

    def _update_port_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

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
            resource_path='/v1/ports/{port_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePortResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_routes_async(self, request):
        """更新路由

        更新路由信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRoutes
        :type request: :class:`huaweicloudsdkiec.v1.UpdateRoutesRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.UpdateRoutesResponse`
        """
        return self._update_routes_with_http_info(request)

    def _update_routes_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

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
            resource_path='/v1/routetables/{routetable_id}/update-routes',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateRoutesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_routetable_async(self, request):
        """更新路由表

        更新路由表基本信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRoutetable
        :type request: :class:`huaweicloudsdkiec.v1.UpdateRoutetableRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.UpdateRoutetableResponse`
        """
        return self._update_routetable_with_http_info(request)

    def _update_routetable_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

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
            resource_path='/v1/routetables/{routetable_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateRoutetableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_subnet_async(self, request):
        """更新子网

        更新子网的基本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSubnet
        :type request: :class:`huaweicloudsdkiec.v1.UpdateSubnetRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.UpdateSubnetResponse`
        """
        return self._update_subnet_with_http_info(request)

    def _update_subnet_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

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
            resource_path='/v1/subnets/{subnet_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateSubnetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_vpc_async(self, request):
        """更新虚拟私有云

        更新虚拟私有云的信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateVpc
        :type request: :class:`huaweicloudsdkiec.v1.UpdateVpcRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.UpdateVpcResponse`
        """
        return self._update_vpc_with_http_info(request)

    def _update_vpc_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']

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
            resource_path='/v1/vpcs/{vpc_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateVpcResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_firewall_async(self, request):
        """创建网络ACL

        创建网络ACL。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateFirewall
        :type request: :class:`huaweicloudsdkiec.v1.CreateFirewallRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.CreateFirewallResponse`
        """
        return self._create_firewall_with_http_info(request)

    def _create_firewall_with_http_info(self, request):
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
            resource_path='/v1/firewalls',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateFirewallResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_firewall_async(self, request):
        """删除网络ACL

        删除网络ACL。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteFirewall
        :type request: :class:`huaweicloudsdkiec.v1.DeleteFirewallRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeleteFirewallResponse`
        """
        return self._delete_firewall_with_http_info(request)

    def _delete_firewall_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_id' in local_var_params:
            path_params['firewall_id'] = local_var_params['firewall_id']

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
            resource_path='/v1/firewalls/{firewall_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteFirewallResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_firewalls_async(self, request):
        """查询网络ACL列表

        查询网络ACL列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFirewalls
        :type request: :class:`huaweicloudsdkiec.v1.ListFirewallsRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListFirewallsResponse`
        """
        return self._list_firewalls_with_http_info(request)

    def _list_firewalls_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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
            resource_path='/v1/firewalls',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFirewallsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_firewall_async(self, request):
        """查询网络ACL详情

        查询网络ACL详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowFirewall
        :type request: :class:`huaweicloudsdkiec.v1.ShowFirewallRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowFirewallResponse`
        """
        return self._show_firewall_with_http_info(request)

    def _show_firewall_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_id' in local_var_params:
            path_params['firewall_id'] = local_var_params['firewall_id']

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
            resource_path='/v1/firewalls/{firewall_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowFirewallResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_firewall_async(self, request):
        """更新网络ACL

        更新网络ACL。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateFirewall
        :type request: :class:`huaweicloudsdkiec.v1.UpdateFirewallRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.UpdateFirewallResponse`
        """
        return self._update_firewall_with_http_info(request)

    def _update_firewall_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_id' in local_var_params:
            path_params['firewall_id'] = local_var_params['firewall_id']

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
            resource_path='/v1/firewalls/{firewall_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateFirewallResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_firewall_rule_async(self, request):
        """更新网络ACL规则

        更新网络ACL规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateFirewallRule
        :type request: :class:`huaweicloudsdkiec.v1.UpdateFirewallRuleRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.UpdateFirewallRuleResponse`
        """
        return self._update_firewall_rule_with_http_info(request)

    def _update_firewall_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_id' in local_var_params:
            path_params['firewall_id'] = local_var_params['firewall_id']

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
            resource_path='/v1/firewalls/{firewall_id}/firewall-rules',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateFirewallRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_public_ip_async(self, request):
        """创建弹性公网IP

        根据用户的请求内容，创建弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePublicIp
        :type request: :class:`huaweicloudsdkiec.v1.CreatePublicIpRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.CreatePublicIpResponse`
        """
        return self._create_public_ip_with_http_info(request)

    def _create_public_ip_with_http_info(self, request):
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
            resource_path='/v1/publicips',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePublicIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_public_ip_async(self, request):
        """删除弹性公网IP

        根据弹性公网IP的ID，删除对应的弹性公网IP。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePublicIp
        :type request: :class:`huaweicloudsdkiec.v1.DeletePublicIpRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeletePublicIpResponse`
        """
        return self._delete_public_ip_with_http_info(request)

    def _delete_public_ip_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']

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
            resource_path='/v1/publicips/{publicip_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePublicIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_public_ips_async(self, request):
        """查询弹性公网IP列表

        获取弹性公网IP列表信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPublicIps
        :type request: :class:`huaweicloudsdkiec.v1.ListPublicIpsRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListPublicIpsResponse`
        """
        return self._list_public_ips_with_http_info(request)

    def _list_public_ips_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'site_id' in local_var_params:
            query_params.append(('site_id', local_var_params['site_id']))
        if 'port_id' in local_var_params:
            query_params.append(('port_id', local_var_params['port_id']))

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
            resource_path='/v1/publicips',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPublicIpsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_public_ip_async(self, request):
        """查询弹性公网IP

        获取弹性公网IP的详情信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPublicIp
        :type request: :class:`huaweicloudsdkiec.v1.ShowPublicIpRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowPublicIpResponse`
        """
        return self._show_public_ip_with_http_info(request)

    def _show_public_ip_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']

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
            resource_path='/v1/publicips/{publicip_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPublicIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_public_ip_async(self, request):
        """更新弹性公网IP

        更新弹性公网IP的信息，主要用于解绑和绑定EIP和VIP之间的关系。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePublicIp
        :type request: :class:`huaweicloudsdkiec.v1.UpdatePublicIpRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.UpdatePublicIpResponse`
        """
        return self._update_public_ip_with_http_info(request)

    def _update_public_ip_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']

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
            resource_path='/v1/publicips/{publicip_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePublicIpResponse',
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
