# coding: utf-8

from __future__ import absolute_import

import importlib
import warnings

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest

try:
    from huaweicloudsdkcore.invoker.invoker import AsyncInvoker
except ImportError as e:
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkiec'")


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
        r"""添加网卡

        添加网卡。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddNics
        :type request: :class:`huaweicloudsdkiec.v1.AddNicsRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.AddNicsResponse`
        """
        http_info = self._add_nics_http_info(request)
        return self._call_api(**http_info)

    def add_nics_async_invoker(self, request):
        http_info = self._add_nics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_nics_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/cloudservers/{instance_id}/nics",
            "request_type": request.__class__.__name__,
            "response_type": "AddNicsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def associate_subnet_async(self, request):
        r"""路由表关联子网

        路由表关联子网
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateSubnet
        :type request: :class:`huaweicloudsdkiec.v1.AssociateSubnetRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.AssociateSubnetResponse`
        """
        http_info = self._associate_subnet_http_info(request)
        return self._call_api(**http_info)

    def associate_subnet_async_invoker(self, request):
        http_info = self._associate_subnet_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_subnet_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/routetables/{routetable_id}/associate-subnets",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateSubnetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

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

    def batch_reboot_instance_async(self, request):
        r"""批量重启边缘实例

        批量重启边缘实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchRebootInstance
        :type request: :class:`huaweicloudsdkiec.v1.BatchRebootInstanceRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.BatchRebootInstanceResponse`
        """
        http_info = self._batch_reboot_instance_http_info(request)
        return self._call_api(**http_info)

    def batch_reboot_instance_async_invoker(self, request):
        http_info = self._batch_reboot_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_reboot_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/cloudservers/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchRebootInstanceResponse"
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

    def batch_start_instance_async(self, request):
        r"""批量启动边缘实例

        批量操作启动边缘实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchStartInstance
        :type request: :class:`huaweicloudsdkiec.v1.BatchStartInstanceRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.BatchStartInstanceResponse`
        """
        http_info = self._batch_start_instance_http_info(request)
        return self._call_api(**http_info)

    def batch_start_instance_async_invoker(self, request):
        http_info = self._batch_start_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_start_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/cloudservers/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchStartInstanceResponse"
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

    def batch_stop_instance_async(self, request):
        r"""批量关机边缘实例

        批量关闭边缘实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchStopInstance
        :type request: :class:`huaweicloudsdkiec.v1.BatchStopInstanceRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.BatchStopInstanceResponse`
        """
        http_info = self._batch_stop_instance_http_info(request)
        return self._call_api(**http_info)

    def batch_stop_instance_async_invoker(self, request):
        http_info = self._batch_stop_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_stop_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/cloudservers/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchStopInstanceResponse"
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

    def change_os_async(self, request):
        r"""切换操作系统

        切换边缘实例操作系统，支持边缘实例创建成功后，保持ip、数据盘不变的情况下重装操作系统。
        
        调用该接口后，系统将卸载系统盘，然后使用新镜像重新创建系统盘，并挂载至实例，实现切换操作系统功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeOs
        :type request: :class:`huaweicloudsdkiec.v1.ChangeOsRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ChangeOsResponse`
        """
        http_info = self._change_os_http_info(request)
        return self._call_api(**http_info)

    def change_os_async_invoker(self, request):
        http_info = self._change_os_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_os_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/cloudservers/{instance_id}/change-os",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeOsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def create_deployment_async(self, request):
        r"""创建部署计划

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
        http_info = self._create_deployment_http_info(request)
        return self._call_api(**http_info)

    def create_deployment_async_invoker(self, request):
        http_info = self._create_deployment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_deployment_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/deployments",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDeploymentResponse"
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

    def create_image_async(self, request):
        r"""从边缘实例创建边缘私有镜像

        使用指定边缘实例的系统盘创建边缘私有镜像。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateImage
        :type request: :class:`huaweicloudsdkiec.v1.CreateImageRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.CreateImageResponse`
        """
        http_info = self._create_image_http_info(request)
        return self._call_api(**http_info)

    def create_image_async_invoker(self, request):
        http_info = self._create_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_image_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/images/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateImageResponse"
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

    def create_instance_async(self, request):
        r"""创建边缘实例

        创建边缘实例。单租户默认可创建50个边缘实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInstance
        :type request: :class:`huaweicloudsdkiec.v1.CreateInstanceRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.CreateInstanceResponse`
        """
        http_info = self._create_instance_http_info(request)
        return self._call_api(**http_info)

    def create_instance_async_invoker(self, request):
        http_info = self._create_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/cloudservers",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceResponse"
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

    def create_keypair_async(self, request):
        r"""创建和导入密钥

        创建SSH密钥，或把公钥导入系统，生成密钥对。
        
        创建SSH密钥成功后，请把响应数据中的私钥内容保存到本地文件，用户使用该私钥登录边缘实例。为保证边缘实例安全，私钥数据只能读取一次，请妥善保管。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateKeypair
        :type request: :class:`huaweicloudsdkiec.v1.CreateKeypairRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.CreateKeypairResponse`
        """
        http_info = self._create_keypair_http_info(request)
        return self._call_api(**http_info)

    def create_keypair_async_invoker(self, request):
        http_info = self._create_keypair_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_keypair_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/os-keypairs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateKeypairResponse"
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

    def create_port_async(self, request):
        r"""创建端口

        创建端口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePort
        :type request: :class:`huaweicloudsdkiec.v1.CreatePortRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.CreatePortResponse`
        """
        http_info = self._create_port_http_info(request)
        return self._call_api(**http_info)

    def create_port_async_invoker(self, request):
        http_info = self._create_port_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_port_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ports",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePortResponse"
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

    def create_routes_async(self, request):
        r"""创建路由

        创建路由
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRoutes
        :type request: :class:`huaweicloudsdkiec.v1.CreateRoutesRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.CreateRoutesResponse`
        """
        http_info = self._create_routes_http_info(request)
        return self._call_api(**http_info)

    def create_routes_async_invoker(self, request):
        http_info = self._create_routes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_routes_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/routetables/{routetable_id}/add-routes",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRoutesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

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

    def create_routetable_async(self, request):
        r"""创建路由表

        创建路由表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRoutetable
        :type request: :class:`huaweicloudsdkiec.v1.CreateRoutetableRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.CreateRoutetableResponse`
        """
        http_info = self._create_routetable_http_info(request)
        return self._call_api(**http_info)

    def create_routetable_async_invoker(self, request):
        http_info = self._create_routetable_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_routetable_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/routetables",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRoutetableResponse"
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

    def create_security_group_async(self, request):
        r"""创建边缘安全组

        根据用户的请求内容，创建对应的安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSecurityGroup
        :type request: :class:`huaweicloudsdkiec.v1.CreateSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.CreateSecurityGroupResponse`
        """
        http_info = self._create_security_group_http_info(request)
        return self._call_api(**http_info)

    def create_security_group_async_invoker(self, request):
        http_info = self._create_security_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_security_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/security-groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSecurityGroupResponse"
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

    def create_security_group_rule_async(self, request):
        r"""创建安全组规则

        根据用户的请求内容，创建安全组规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSecurityGroupRule
        :type request: :class:`huaweicloudsdkiec.v1.CreateSecurityGroupRuleRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.CreateSecurityGroupRuleResponse`
        """
        http_info = self._create_security_group_rule_http_info(request)
        return self._call_api(**http_info)

    def create_security_group_rule_async_invoker(self, request):
        http_info = self._create_security_group_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_security_group_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/security-group-rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSecurityGroupRuleResponse"
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

    def create_vpc_async(self, request):
        r"""创建虚拟私有云

        根据用户的请求内容，创建虚拟私有云。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVpc
        :type request: :class:`huaweicloudsdkiec.v1.CreateVpcRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.CreateVpcResponse`
        """
        http_info = self._create_vpc_http_info(request)
        return self._call_api(**http_info)

    def create_vpc_async_invoker(self, request):
        http_info = self._create_vpc_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_vpc_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/vpcs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVpcResponse"
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

    def delete_bandwidth_async(self, request):
        r"""删除带宽

        删除带宽。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBandwidth
        :type request: :class:`huaweicloudsdkiec.v1.DeleteBandwidthRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeleteBandwidthResponse`
        """
        http_info = self._delete_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def delete_bandwidth_async_invoker(self, request):
        http_info = self._delete_bandwidth_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_bandwidth_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/bandwidths/{bandwidth_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBandwidthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'bandwidth_id' in local_var_params:
            path_params['bandwidth_id'] = local_var_params['bandwidth_id']

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

    def delete_deployment_async(self, request):
        r"""删除部署计划

        删除部署计划。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDeployment
        :type request: :class:`huaweicloudsdkiec.v1.DeleteDeploymentRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeleteDeploymentResponse`
        """
        http_info = self._delete_deployment_http_info(request)
        return self._call_api(**http_info)

    def delete_deployment_async_invoker(self, request):
        http_info = self._delete_deployment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_deployment_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/deployments/{deployment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDeploymentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

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

    def delete_edge_cloud_async(self, request):
        r"""删除边缘业务

        删除边缘业务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEdgeCloud
        :type request: :class:`huaweicloudsdkiec.v1.DeleteEdgeCloudRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeleteEdgeCloudResponse`
        """
        http_info = self._delete_edge_cloud_http_info(request)
        return self._call_api(**http_info)

    def delete_edge_cloud_async_invoker(self, request):
        http_info = self._delete_edge_cloud_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_edge_cloud_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/edgeclouds/{edgecloud_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEdgeCloudResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edgecloud_id' in local_var_params:
            path_params['edgecloud_id'] = local_var_params['edgecloud_id']

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

    def delete_image_async(self, request):
        r"""删除边缘私有镜像

        将指定ID的边缘私有镜像删除
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteImage
        :type request: :class:`huaweicloudsdkiec.v1.DeleteImageRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeleteImageResponse`
        """
        http_info = self._delete_image_http_info(request)
        return self._call_api(**http_info)

    def delete_image_async_invoker(self, request):
        http_info = self._delete_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_image_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/images/{image_id}",
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

    def delete_instances_async(self, request):
        r"""批量删除边缘实例

        批量删除边缘实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteInstances
        :type request: :class:`huaweicloudsdkiec.v1.DeleteInstancesRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeleteInstancesResponse`
        """
        http_info = self._delete_instances_http_info(request)
        return self._call_api(**http_info)

    def delete_instances_async_invoker(self, request):
        http_info = self._delete_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_instances_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/cloudservers/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstancesResponse"
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

    def delete_keypair_async(self, request):
        r"""删除密钥

        删除密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteKeypair
        :type request: :class:`huaweicloudsdkiec.v1.DeleteKeypairRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeleteKeypairResponse`
        """
        http_info = self._delete_keypair_http_info(request)
        return self._call_api(**http_info)

    def delete_keypair_async_invoker(self, request):
        http_info = self._delete_keypair_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_keypair_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/os-keypairs/{keypair_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteKeypairResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'keypair_name' in local_var_params:
            path_params['keypair_name'] = local_var_params['keypair_name']

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

    def delete_nics_async(self, request):
        r"""删除网卡

        删除网卡。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteNics
        :type request: :class:`huaweicloudsdkiec.v1.DeleteNicsRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeleteNicsResponse`
        """
        http_info = self._delete_nics_http_info(request)
        return self._call_api(**http_info)

    def delete_nics_async_invoker(self, request):
        http_info = self._delete_nics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_nics_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/cloudservers/{instance_id}/nics/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNicsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def delete_port_async(self, request):
        r"""删除端口

        删除端口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePort
        :type request: :class:`huaweicloudsdkiec.v1.DeletePortRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeletePortResponse`
        """
        http_info = self._delete_port_http_info(request)
        return self._call_api(**http_info)

    def delete_port_async_invoker(self, request):
        http_info = self._delete_port_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_port_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/ports/{port_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePortResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

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

    def delete_routes_async(self, request):
        r"""删除路由

        删除路由
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRoutes
        :type request: :class:`huaweicloudsdkiec.v1.DeleteRoutesRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeleteRoutesResponse`
        """
        http_info = self._delete_routes_http_info(request)
        return self._call_api(**http_info)

    def delete_routes_async_invoker(self, request):
        http_info = self._delete_routes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_routes_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/routetables/{routetable_id}/delete-routes",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRoutesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

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

    def delete_routetable_async(self, request):
        r"""删除路由表

        删除路由表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRoutetable
        :type request: :class:`huaweicloudsdkiec.v1.DeleteRoutetableRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeleteRoutetableResponse`
        """
        http_info = self._delete_routetable_http_info(request)
        return self._call_api(**http_info)

    def delete_routetable_async_invoker(self, request):
        http_info = self._delete_routetable_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_routetable_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/routetables/{routetable_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRoutetableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

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

    def delete_security_group_async(self, request):
        r"""删除安全组

        根据安全组的ID，删除对应的安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSecurityGroup
        :type request: :class:`huaweicloudsdkiec.v1.DeleteSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeleteSecurityGroupResponse`
        """
        http_info = self._delete_security_group_http_info(request)
        return self._call_api(**http_info)

    def delete_security_group_async_invoker(self, request):
        http_info = self._delete_security_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_security_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/security-groups/{security_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSecurityGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_group_id' in local_var_params:
            path_params['security_group_id'] = local_var_params['security_group_id']

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

    def delete_security_group_rule_async(self, request):
        r"""删除安全组规则

        根据安全组的ID，删除对应的安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSecurityGroupRule
        :type request: :class:`huaweicloudsdkiec.v1.DeleteSecurityGroupRuleRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeleteSecurityGroupRuleResponse`
        """
        http_info = self._delete_security_group_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_security_group_rule_async_invoker(self, request):
        http_info = self._delete_security_group_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_security_group_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/security-group-rules/{security_group_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSecurityGroupRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_group_rule_id' in local_var_params:
            path_params['security_group_rule_id'] = local_var_params['security_group_rule_id']

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

    def delete_subnet_async(self, request):
        r"""删除子网

        根据子网的ID，删除子网。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSubnet
        :type request: :class:`huaweicloudsdkiec.v1.DeleteSubnetRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeleteSubnetResponse`
        """
        http_info = self._delete_subnet_http_info(request)
        return self._call_api(**http_info)

    def delete_subnet_async_invoker(self, request):
        http_info = self._delete_subnet_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_subnet_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/subnets/{subnet_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSubnetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

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

    def delete_vpc_async(self, request):
        r"""删除虚拟私有云

        根据虚拟机私有云的ID，删除对应的虚拟私有云。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteVpc
        :type request: :class:`huaweicloudsdkiec.v1.DeleteVpcRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeleteVpcResponse`
        """
        http_info = self._delete_vpc_http_info(request)
        return self._call_api(**http_info)

    def delete_vpc_async_invoker(self, request):
        http_info = self._delete_vpc_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_vpc_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/vpcs/{vpc_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVpcResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']

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

    def disassociate_subnet_async(self, request):
        r"""路由表解关联子网

        路由表解关联子网
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateSubnet
        :type request: :class:`huaweicloudsdkiec.v1.DisassociateSubnetRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DisassociateSubnetResponse`
        """
        http_info = self._disassociate_subnet_http_info(request)
        return self._call_api(**http_info)

    def disassociate_subnet_async_invoker(self, request):
        http_info = self._disassociate_subnet_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disassociate_subnet_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/routetables/{routetable_id}/disassociate-subnets",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateSubnetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

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

    def execute_deployment_async(self, request):
        r"""执行部署计划

        执行部署计划，创建一个边缘业务。单租户默认可创建10个边缘业务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteDeployment
        :type request: :class:`huaweicloudsdkiec.v1.ExecuteDeploymentRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ExecuteDeploymentResponse`
        """
        http_info = self._execute_deployment_http_info(request)
        return self._call_api(**http_info)

    def execute_deployment_async_invoker(self, request):
        http_info = self._execute_deployment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _execute_deployment_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/deployments/{deployment_id}/deploy",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteDeploymentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

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

    def expand_edgecloud_async(self, request):
        r"""扩容边缘业务

        执行部署计划，对边缘业务进行扩容操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExpandEdgecloud
        :type request: :class:`huaweicloudsdkiec.v1.ExpandEdgecloudRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ExpandEdgecloudResponse`
        """
        http_info = self._expand_edgecloud_http_info(request)
        return self._call_api(**http_info)

    def expand_edgecloud_async_invoker(self, request):
        http_info = self._expand_edgecloud_http_info(request)
        return AsyncInvoker(self, http_info)

    def _expand_edgecloud_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/deployments/{deployment_id}/expand",
            "request_type": request.__class__.__name__,
            "response_type": "ExpandEdgecloudResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

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

    def list_bandwidth_types_async(self, request):
        r"""查询共享带宽类型列表

        查询共享带宽类型列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBandwidthTypes
        :type request: :class:`huaweicloudsdkiec.v1.ListBandwidthTypesRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListBandwidthTypesResponse`
        """
        http_info = self._list_bandwidth_types_http_info(request)
        return self._call_api(**http_info)

    def list_bandwidth_types_async_invoker(self, request):
        http_info = self._list_bandwidth_types_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_bandwidth_types_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/share-bandwidth-types",
            "request_type": request.__class__.__name__,
            "response_type": "ListBandwidthTypesResponse"
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
        if 'site_id' in local_var_params:
            query_params.append(('site_id', local_var_params['site_id']))
        if 'bandwidth_type' in local_var_params:
            query_params.append(('bandwidth_type', local_var_params['bandwidth_type']))

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

    def list_bandwidths_async(self, request):
        r"""查询带宽列表

        查询带宽列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBandwidths
        :type request: :class:`huaweicloudsdkiec.v1.ListBandwidthsRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListBandwidthsResponse`
        """
        http_info = self._list_bandwidths_http_info(request)
        return self._call_api(**http_info)

    def list_bandwidths_async_invoker(self, request):
        http_info = self._list_bandwidths_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_bandwidths_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/bandwidths",
            "request_type": request.__class__.__name__,
            "response_type": "ListBandwidthsResponse"
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
        if 'site_id' in local_var_params:
            query_params.append(('site_id', local_var_params['site_id']))

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

    def list_cloud_images_async(self, request):
        r"""查询中心镜像列表

        查询租户在某个云Region的可见镜像列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCloudImages
        :type request: :class:`huaweicloudsdkiec.v1.ListCloudImagesRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListCloudImagesResponse`
        """
        http_info = self._list_cloud_images_http_info(request)
        return self._call_api(**http_info)

    def list_cloud_images_async_invoker(self, request):
        http_info = self._list_cloud_images_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cloud_images_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/cloudimages/{region_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListCloudImagesResponse"
            }

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

    def list_deployments_async(self, request):
        r"""查询部署计划列表

        查询部署计划列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDeployments
        :type request: :class:`huaweicloudsdkiec.v1.ListDeploymentsRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListDeploymentsResponse`
        """
        http_info = self._list_deployments_http_info(request)
        return self._call_api(**http_info)

    def list_deployments_async_invoker(self, request):
        http_info = self._list_deployments_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_deployments_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/deployments",
            "request_type": request.__class__.__name__,
            "response_type": "ListDeploymentsResponse"
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
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'edgecloud_id' in local_var_params:
            query_params.append(('edgecloud_id', local_var_params['edgecloud_id']))

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

    def list_edge_cloud_async(self, request):
        r"""查询边缘业务列表

        查询边缘业务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEdgeCloud
        :type request: :class:`huaweicloudsdkiec.v1.ListEdgeCloudRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListEdgeCloudResponse`
        """
        http_info = self._list_edge_cloud_http_info(request)
        return self._call_api(**http_info)

    def list_edge_cloud_async_invoker(self, request):
        http_info = self._list_edge_cloud_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_edge_cloud_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgeclouds",
            "request_type": request.__class__.__name__,
            "response_type": "ListEdgeCloudResponse"
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
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))

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

    def list_flavors_async(self, request):
        r"""查询边缘规格列表

        查询边缘规格列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFlavors
        :type request: :class:`huaweicloudsdkiec.v1.ListFlavorsRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListFlavorsResponse`
        """
        http_info = self._list_flavors_http_info(request)
        return self._call_api(**http_info)

    def list_flavors_async_invoker(self, request):
        http_info = self._list_flavors_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_flavors_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/cloudservers/flavors",
            "request_type": request.__class__.__name__,
            "response_type": "ListFlavorsResponse"
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

    def list_images_async(self, request):
        r"""查询镜像列表

        根据不同条件查询镜像列表，例:
        
        -  查询已注册的私有镜像列表: visibility&#x3D;private
        - 公共镜像: visibility&#x3D;public
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListImages
        :type request: :class:`huaweicloudsdkiec.v1.ListImagesRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListImagesResponse`
        """
        http_info = self._list_images_http_info(request)
        return self._call_api(**http_info)

    def list_images_async_invoker(self, request):
        http_info = self._list_images_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_images_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/images",
            "request_type": request.__class__.__name__,
            "response_type": "ListImagesResponse"
            }

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

    def list_instances_async(self, request):
        r"""查询边缘实例列表

        查询边缘实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstances
        :type request: :class:`huaweicloudsdkiec.v1.ListInstancesRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListInstancesResponse`
        """
        http_info = self._list_instances_http_info(request)
        return self._call_api(**http_info)

    def list_instances_async_invoker(self, request):
        http_info = self._list_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instances_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/cloudservers",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstancesResponse"
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

    def list_keypairs_async(self, request):
        r"""查询密钥列表

        查询密钥信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKeypairs
        :type request: :class:`huaweicloudsdkiec.v1.ListKeypairsRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListKeypairsResponse`
        """
        http_info = self._list_keypairs_http_info(request)
        return self._call_api(**http_info)

    def list_keypairs_async_invoker(self, request):
        http_info = self._list_keypairs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_keypairs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/os-keypairs",
            "request_type": request.__class__.__name__,
            "response_type": "ListKeypairsResponse"
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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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

    def list_ports_async(self, request):
        r"""查询端口列表

        查询端口的列表信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPorts
        :type request: :class:`huaweicloudsdkiec.v1.ListPortsRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListPortsResponse`
        """
        http_info = self._list_ports_http_info(request)
        return self._call_api(**http_info)

    def list_ports_async_invoker(self, request):
        http_info = self._list_ports_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ports_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ports",
            "request_type": request.__class__.__name__,
            "response_type": "ListPortsResponse"
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

    def list_quota_async(self, request):
        r"""查询配额

        查询租户资源配额。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListQuota
        :type request: :class:`huaweicloudsdkiec.v1.ListQuotaRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListQuotaResponse`
        """
        http_info = self._list_quota_http_info(request)
        return self._call_api(**http_info)

    def list_quota_async_invoker(self, request):
        http_info = self._list_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgeclouds/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ListQuotaResponse"
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

    def list_related_routetables_async(self, request):
        r"""查询子网关联的路由表

        查询子网关联的路由表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRelatedRoutetables
        :type request: :class:`huaweicloudsdkiec.v1.ListRelatedRoutetablesRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListRelatedRoutetablesResponse`
        """
        http_info = self._list_related_routetables_http_info(request)
        return self._call_api(**http_info)

    def list_related_routetables_async_invoker(self, request):
        http_info = self._list_related_routetables_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_related_routetables_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/subnets/{subnet_id}/routetables",
            "request_type": request.__class__.__name__,
            "response_type": "ListRelatedRoutetablesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

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

    def list_routes_async(self, request):
        r"""查询路由列表

        查询路由列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRoutes
        :type request: :class:`huaweicloudsdkiec.v1.ListRoutesRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListRoutesResponse`
        """
        http_info = self._list_routes_http_info(request)
        return self._call_api(**http_info)

    def list_routes_async_invoker(self, request):
        http_info = self._list_routes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_routes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/routetables/{routetable_id}/routes",
            "request_type": request.__class__.__name__,
            "response_type": "ListRoutesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

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

    def list_routetables_async(self, request):
        r"""查询路由表列表

        查询路由列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRoutetables
        :type request: :class:`huaweicloudsdkiec.v1.ListRoutetablesRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListRoutetablesResponse`
        """
        http_info = self._list_routetables_http_info(request)
        return self._call_api(**http_info)

    def list_routetables_async_invoker(self, request):
        http_info = self._list_routetables_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_routetables_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/routetables",
            "request_type": request.__class__.__name__,
            "response_type": "ListRoutetablesResponse"
            }

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

    def list_security_group_rules_async(self, request):
        r"""查询安全组规则列表

        根据用户的查询条件，获取安全组规则的列表信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSecurityGroupRules
        :type request: :class:`huaweicloudsdkiec.v1.ListSecurityGroupRulesRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListSecurityGroupRulesResponse`
        """
        http_info = self._list_security_group_rules_http_info(request)
        return self._call_api(**http_info)

    def list_security_group_rules_async_invoker(self, request):
        http_info = self._list_security_group_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_security_group_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/security-group-rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListSecurityGroupRulesResponse"
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
        if 'security_group_id' in local_var_params:
            query_params.append(('security_group_id', local_var_params['security_group_id']))

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

    def list_security_groups_async(self, request):
        r"""查询安全组列表

        根据特定查询条件，获取安全组的列表信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSecurityGroups
        :type request: :class:`huaweicloudsdkiec.v1.ListSecurityGroupsRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListSecurityGroupsResponse`
        """
        http_info = self._list_security_groups_http_info(request)
        return self._call_api(**http_info)

    def list_security_groups_async_invoker(self, request):
        http_info = self._list_security_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_security_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/security-groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListSecurityGroupsResponse"
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

    def list_sites_async(self, request):
        r"""查询边缘站点列表

        查询边缘站点列表。
        
        - 边缘站点：靠近终端应用的位置，基于一个或多个运营商建立的一个城市级站点。边缘站点提供物理隔离的资源池，提供多元算力、存储和网络的能力。用户可以将业务灵活就近部署在边缘站点上，以降低网络时延和成本。
        - 边缘区域：为依据边缘站点的物理位置划分的区域，一个边缘区域包含多个相靠近的边缘站点的集合。IEC当前提供城市级、省级和大区级三个分布层级的边缘区域。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSites
        :type request: :class:`huaweicloudsdkiec.v1.ListSitesRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListSitesResponse`
        """
        http_info = self._list_sites_http_info(request)
        return self._call_api(**http_info)

    def list_sites_async_invoker(self, request):
        http_info = self._list_sites_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_sites_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/sites",
            "request_type": request.__class__.__name__,
            "response_type": "ListSitesResponse"
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

    def list_subnets_async(self, request):
        r"""查询子网列表

        根据查询条件获取子网的列表信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSubnets
        :type request: :class:`huaweicloudsdkiec.v1.ListSubnetsRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListSubnetsResponse`
        """
        http_info = self._list_subnets_http_info(request)
        return self._call_api(**http_info)

    def list_subnets_async_invoker(self, request):
        http_info = self._list_subnets_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_subnets_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/subnets",
            "request_type": request.__class__.__name__,
            "response_type": "ListSubnetsResponse"
            }

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

    def list_volume_async(self, request):
        r"""查询硬盘列表

        查询硬盘列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVolume
        :type request: :class:`huaweicloudsdkiec.v1.ListVolumeRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListVolumeResponse`
        """
        http_info = self._list_volume_http_info(request)
        return self._call_api(**http_info)

    def list_volume_async_invoker(self, request):
        http_info = self._list_volume_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_volume_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/cloudvolumes",
            "request_type": request.__class__.__name__,
            "response_type": "ListVolumeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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

    def list_vpcs_async(self, request):
        r"""查询虚拟私有云列表

        获取虚拟私有云的列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVpcs
        :type request: :class:`huaweicloudsdkiec.v1.ListVpcsRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListVpcsResponse`
        """
        http_info = self._list_vpcs_http_info(request)
        return self._call_api(**http_info)

    def list_vpcs_async_invoker(self, request):
        http_info = self._list_vpcs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_vpcs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/vpcs",
            "request_type": request.__class__.__name__,
            "response_type": "ListVpcsResponse"
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
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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

    def rebuild_image_async(self, request):
        r"""重试边缘镜像任务

        重试边缘镜像任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RebuildImage
        :type request: :class:`huaweicloudsdkiec.v1.RebuildImageRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.RebuildImageResponse`
        """
        http_info = self._rebuild_image_http_info(request)
        return self._call_api(**http_info)

    def rebuild_image_async_invoker(self, request):
        http_info = self._rebuild_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _rebuild_image_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/jobs/{job_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "RebuildImageResponse"
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

    def register_image_async(self, request):
        r"""注册边缘私有镜像

        将指定Region和ID的IMS镜像注册到边缘IEC-IMS; 
        注意指定的Region必须在当前IEC-IMS支持的Region列表中。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RegisterImage
        :type request: :class:`huaweicloudsdkiec.v1.RegisterImageRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.RegisterImageResponse`
        """
        http_info = self._register_image_http_info(request)
        return self._call_api(**http_info)

    def register_image_async_invoker(self, request):
        http_info = self._register_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _register_image_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/images/register",
            "request_type": request.__class__.__name__,
            "response_type": "RegisterImageResponse"
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

    def show_bandwidth_async(self, request):
        r"""查询带宽详情

        查询带宽详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBandwidth
        :type request: :class:`huaweicloudsdkiec.v1.ShowBandwidthRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowBandwidthResponse`
        """
        http_info = self._show_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def show_bandwidth_async_invoker(self, request):
        http_info = self._show_bandwidth_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_bandwidth_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/bandwidths/{bandwidth_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBandwidthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'bandwidth_id' in local_var_params:
            path_params['bandwidth_id'] = local_var_params['bandwidth_id']

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

    def show_edge_cloud_async(self, request):
        r"""查询边缘业务详情

        查询边缘业务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEdgeCloud
        :type request: :class:`huaweicloudsdkiec.v1.ShowEdgeCloudRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowEdgeCloudResponse`
        """
        http_info = self._show_edge_cloud_http_info(request)
        return self._call_api(**http_info)

    def show_edge_cloud_async_invoker(self, request):
        http_info = self._show_edge_cloud_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_edge_cloud_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgeclouds/{edgecloud_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEdgeCloudResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edgecloud_id' in local_var_params:
            path_params['edgecloud_id'] = local_var_params['edgecloud_id']

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

    def show_image_async(self, request):
        r"""查询镜像详情

        查询镜像详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowImage
        :type request: :class:`huaweicloudsdkiec.v1.ShowImageRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowImageResponse`
        """
        http_info = self._show_image_http_info(request)
        return self._call_api(**http_info)

    def show_image_async_invoker(self, request):
        http_info = self._show_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_image_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/images/{image_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowImageResponse"
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

    def show_instance_async(self, request):
        r"""查询边缘实例详情

        查询边缘实例详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstance
        :type request: :class:`huaweicloudsdkiec.v1.ShowInstanceRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowInstanceResponse`
        """
        http_info = self._show_instance_http_info(request)
        return self._call_api(**http_info)

    def show_instance_async_invoker(self, request):
        http_info = self._show_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_instance_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/cloudservers/{server_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceResponse"
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

    def show_keypair_async(self, request):
        r"""查询密钥详情

        查询密钥信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowKeypair
        :type request: :class:`huaweicloudsdkiec.v1.ShowKeypairRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowKeypairResponse`
        """
        http_info = self._show_keypair_http_info(request)
        return self._call_api(**http_info)

    def show_keypair_async_invoker(self, request):
        http_info = self._show_keypair_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_keypair_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/os-keypairs/{keypair_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowKeypairResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'keypair_name' in local_var_params:
            path_params['keypair_name'] = local_var_params['keypair_name']

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

    def show_port_async(self, request):
        r"""查询端口详情

        根据端口的ID，获取端口的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPort
        :type request: :class:`huaweicloudsdkiec.v1.ShowPortRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowPortResponse`
        """
        http_info = self._show_port_http_info(request)
        return self._call_api(**http_info)

    def show_port_async_invoker(self, request):
        http_info = self._show_port_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_port_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ports/{port_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPortResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

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

    def show_routetable_async(self, request):
        r"""查询路由表详情

        查询路由表详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRoutetable
        :type request: :class:`huaweicloudsdkiec.v1.ShowRoutetableRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowRoutetableResponse`
        """
        http_info = self._show_routetable_http_info(request)
        return self._call_api(**http_info)

    def show_routetable_async_invoker(self, request):
        http_info = self._show_routetable_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_routetable_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/routetables/{routetable_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRoutetableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

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

    def show_security_group_async(self, request):
        r"""查询安全组详情

        根据安全组的ID，获取特定安全组的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSecurityGroup
        :type request: :class:`huaweicloudsdkiec.v1.ShowSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowSecurityGroupResponse`
        """
        http_info = self._show_security_group_http_info(request)
        return self._call_api(**http_info)

    def show_security_group_async_invoker(self, request):
        http_info = self._show_security_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_security_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/security-groups/{security_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSecurityGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_group_id' in local_var_params:
            path_params['security_group_id'] = local_var_params['security_group_id']

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

    def show_security_group_rule_async(self, request):
        r"""查询安全组规则详情

        根据安全组规则的ID，获取安全组规则的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSecurityGroupRule
        :type request: :class:`huaweicloudsdkiec.v1.ShowSecurityGroupRuleRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowSecurityGroupRuleResponse`
        """
        http_info = self._show_security_group_rule_http_info(request)
        return self._call_api(**http_info)

    def show_security_group_rule_async_invoker(self, request):
        http_info = self._show_security_group_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_security_group_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/security-group-rules/{security_group_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSecurityGroupRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_group_rule_id' in local_var_params:
            path_params['security_group_rule_id'] = local_var_params['security_group_rule_id']

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

    def show_subnet_async(self, request):
        r"""查询子网详情

        根据子网的ID，获取子网的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSubnet
        :type request: :class:`huaweicloudsdkiec.v1.ShowSubnetRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowSubnetResponse`
        """
        http_info = self._show_subnet_http_info(request)
        return self._call_api(**http_info)

    def show_subnet_async_invoker(self, request):
        http_info = self._show_subnet_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_subnet_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/subnets/{subnet_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSubnetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

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

    def show_volume_async(self, request):
        r"""查询硬盘详情

        查询硬盘详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVolume
        :type request: :class:`huaweicloudsdkiec.v1.ShowVolumeRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowVolumeResponse`
        """
        http_info = self._show_volume_http_info(request)
        return self._call_api(**http_info)

    def show_volume_async_invoker(self, request):
        http_info = self._show_volume_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_volume_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/cloudvolumes/{volume_id}",
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

    def show_volume_types_async(self, request):
        r"""查询硬盘类型列表

        查询硬盘类型列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVolumeTypes
        :type request: :class:`huaweicloudsdkiec.v1.ShowVolumeTypesRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowVolumeTypesResponse`
        """
        http_info = self._show_volume_types_http_info(request)
        return self._call_api(**http_info)

    def show_volume_types_async_invoker(self, request):
        http_info = self._show_volume_types_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_volume_types_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/cloudvolumes/volume-types",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVolumeTypesResponse"
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

    def show_vpc_async(self, request):
        r"""查询虚拟私有云详情

        根据虚拟私有云ID，获取虚拟私有云的详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVpc
        :type request: :class:`huaweicloudsdkiec.v1.ShowVpcRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowVpcResponse`
        """
        http_info = self._show_vpc_http_info(request)
        return self._call_api(**http_info)

    def show_vpc_async_invoker(self, request):
        http_info = self._show_vpc_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_vpc_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/vpcs/{vpc_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVpcResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']

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

    def update_bandwidth_async(self, request):
        r"""更新带宽

        更新带宽。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateBandwidth
        :type request: :class:`huaweicloudsdkiec.v1.UpdateBandwidthRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.UpdateBandwidthResponse`
        """
        http_info = self._update_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def update_bandwidth_async_invoker(self, request):
        http_info = self._update_bandwidth_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_bandwidth_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/bandwidths/{bandwidth_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateBandwidthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'bandwidth_id' in local_var_params:
            path_params['bandwidth_id'] = local_var_params['bandwidth_id']

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

    def update_instance_async(self, request):
        r"""修改边缘实例

        修改边缘实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstance
        :type request: :class:`huaweicloudsdkiec.v1.UpdateInstanceRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.UpdateInstanceResponse`
        """
        http_info = self._update_instance_http_info(request)
        return self._call_api(**http_info)

    def update_instance_async_invoker(self, request):
        http_info = self._update_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_instance_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/cloudservers/{server_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceResponse"
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

    def update_port_async(self, request):
        r"""更新端口

        更新端口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePort
        :type request: :class:`huaweicloudsdkiec.v1.UpdatePortRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.UpdatePortResponse`
        """
        http_info = self._update_port_http_info(request)
        return self._call_api(**http_info)

    def update_port_async_invoker(self, request):
        http_info = self._update_port_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_port_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/ports/{port_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePortResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

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

    def update_routes_async(self, request):
        r"""更新路由

        更新路由信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRoutes
        :type request: :class:`huaweicloudsdkiec.v1.UpdateRoutesRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.UpdateRoutesResponse`
        """
        http_info = self._update_routes_http_info(request)
        return self._call_api(**http_info)

    def update_routes_async_invoker(self, request):
        http_info = self._update_routes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_routes_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/routetables/{routetable_id}/update-routes",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRoutesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

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

    def update_routetable_async(self, request):
        r"""更新路由表

        更新路由表基本信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRoutetable
        :type request: :class:`huaweicloudsdkiec.v1.UpdateRoutetableRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.UpdateRoutetableResponse`
        """
        http_info = self._update_routetable_http_info(request)
        return self._call_api(**http_info)

    def update_routetable_async_invoker(self, request):
        http_info = self._update_routetable_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_routetable_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/routetables/{routetable_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRoutetableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

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

    def update_subnet_async(self, request):
        r"""更新子网

        更新子网的基本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSubnet
        :type request: :class:`huaweicloudsdkiec.v1.UpdateSubnetRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.UpdateSubnetResponse`
        """
        http_info = self._update_subnet_http_info(request)
        return self._call_api(**http_info)

    def update_subnet_async_invoker(self, request):
        http_info = self._update_subnet_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_subnet_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/subnets/{subnet_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSubnetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

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

    def update_vpc_async(self, request):
        r"""更新虚拟私有云

        更新虚拟私有云的信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateVpc
        :type request: :class:`huaweicloudsdkiec.v1.UpdateVpcRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.UpdateVpcResponse`
        """
        http_info = self._update_vpc_http_info(request)
        return self._call_api(**http_info)

    def update_vpc_async_invoker(self, request):
        http_info = self._update_vpc_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_vpc_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/vpcs/{vpc_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateVpcResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']

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

    def create_firewall_async(self, request):
        r"""创建网络ACL

        创建网络ACL。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateFirewall
        :type request: :class:`huaweicloudsdkiec.v1.CreateFirewallRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.CreateFirewallResponse`
        """
        http_info = self._create_firewall_http_info(request)
        return self._call_api(**http_info)

    def create_firewall_async_invoker(self, request):
        http_info = self._create_firewall_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_firewall_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/firewalls",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFirewallResponse"
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

    def delete_firewall_async(self, request):
        r"""删除网络ACL

        删除网络ACL。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteFirewall
        :type request: :class:`huaweicloudsdkiec.v1.DeleteFirewallRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeleteFirewallResponse`
        """
        http_info = self._delete_firewall_http_info(request)
        return self._call_api(**http_info)

    def delete_firewall_async_invoker(self, request):
        http_info = self._delete_firewall_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_firewall_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/firewalls/{firewall_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteFirewallResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_id' in local_var_params:
            path_params['firewall_id'] = local_var_params['firewall_id']

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

    def list_firewalls_async(self, request):
        r"""查询网络ACL列表

        查询网络ACL列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFirewalls
        :type request: :class:`huaweicloudsdkiec.v1.ListFirewallsRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListFirewallsResponse`
        """
        http_info = self._list_firewalls_http_info(request)
        return self._call_api(**http_info)

    def list_firewalls_async_invoker(self, request):
        http_info = self._list_firewalls_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_firewalls_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/firewalls",
            "request_type": request.__class__.__name__,
            "response_type": "ListFirewallsResponse"
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
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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

    def show_firewall_async(self, request):
        r"""查询网络ACL详情

        查询网络ACL详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowFirewall
        :type request: :class:`huaweicloudsdkiec.v1.ShowFirewallRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowFirewallResponse`
        """
        http_info = self._show_firewall_http_info(request)
        return self._call_api(**http_info)

    def show_firewall_async_invoker(self, request):
        http_info = self._show_firewall_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_firewall_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/firewalls/{firewall_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFirewallResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_id' in local_var_params:
            path_params['firewall_id'] = local_var_params['firewall_id']

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

    def update_firewall_async(self, request):
        r"""更新网络ACL

        更新网络ACL。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateFirewall
        :type request: :class:`huaweicloudsdkiec.v1.UpdateFirewallRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.UpdateFirewallResponse`
        """
        http_info = self._update_firewall_http_info(request)
        return self._call_api(**http_info)

    def update_firewall_async_invoker(self, request):
        http_info = self._update_firewall_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_firewall_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/firewalls/{firewall_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateFirewallResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_id' in local_var_params:
            path_params['firewall_id'] = local_var_params['firewall_id']

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

    def update_firewall_rule_async(self, request):
        r"""更新网络ACL规则

        更新网络ACL规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateFirewallRule
        :type request: :class:`huaweicloudsdkiec.v1.UpdateFirewallRuleRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.UpdateFirewallRuleResponse`
        """
        http_info = self._update_firewall_rule_http_info(request)
        return self._call_api(**http_info)

    def update_firewall_rule_async_invoker(self, request):
        http_info = self._update_firewall_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_firewall_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/firewalls/{firewall_id}/firewall-rules",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateFirewallRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_id' in local_var_params:
            path_params['firewall_id'] = local_var_params['firewall_id']

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

    def create_public_ip_async(self, request):
        r"""创建弹性公网IP

        根据用户的请求内容，创建弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePublicIp
        :type request: :class:`huaweicloudsdkiec.v1.CreatePublicIpRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.CreatePublicIpResponse`
        """
        http_info = self._create_public_ip_http_info(request)
        return self._call_api(**http_info)

    def create_public_ip_async_invoker(self, request):
        http_info = self._create_public_ip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_public_ip_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/publicips",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePublicIpResponse"
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

    def delete_public_ip_async(self, request):
        r"""删除弹性公网IP

        根据弹性公网IP的ID，删除对应的弹性公网IP。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePublicIp
        :type request: :class:`huaweicloudsdkiec.v1.DeletePublicIpRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DeletePublicIpResponse`
        """
        http_info = self._delete_public_ip_http_info(request)
        return self._call_api(**http_info)

    def delete_public_ip_async_invoker(self, request):
        http_info = self._delete_public_ip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_public_ip_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/publicips/{publicip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePublicIpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']

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

    def list_public_ips_async(self, request):
        r"""查询弹性公网IP列表

        获取弹性公网IP列表信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPublicIps
        :type request: :class:`huaweicloudsdkiec.v1.ListPublicIpsRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ListPublicIpsResponse`
        """
        http_info = self._list_public_ips_http_info(request)
        return self._call_api(**http_info)

    def list_public_ips_async_invoker(self, request):
        http_info = self._list_public_ips_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_public_ips_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/publicips",
            "request_type": request.__class__.__name__,
            "response_type": "ListPublicIpsResponse"
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
        if 'site_id' in local_var_params:
            query_params.append(('site_id', local_var_params['site_id']))
        if 'port_id' in local_var_params:
            query_params.append(('port_id', local_var_params['port_id']))

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

    def show_public_ip_async(self, request):
        r"""查询弹性公网IP

        获取弹性公网IP的详情信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPublicIp
        :type request: :class:`huaweicloudsdkiec.v1.ShowPublicIpRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.ShowPublicIpResponse`
        """
        http_info = self._show_public_ip_http_info(request)
        return self._call_api(**http_info)

    def show_public_ip_async_invoker(self, request):
        http_info = self._show_public_ip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_public_ip_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/publicips/{publicip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPublicIpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']

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

    def update_public_ip_async(self, request):
        r"""更新弹性公网IP

        更新弹性公网IP的信息，主要用于解绑和绑定EIP和VIP之间的关系。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePublicIp
        :type request: :class:`huaweicloudsdkiec.v1.UpdatePublicIpRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.UpdatePublicIpResponse`
        """
        http_info = self._update_public_ip_http_info(request)
        return self._call_api(**http_info)

    def update_public_ip_async_invoker(self, request):
        http_info = self._update_public_ip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_public_ip_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/publicips/{publicip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePublicIpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']

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

    def attach_vip_bandwidth_async(self, request):
        r"""端口绑定带宽

        IPv6虚拟IP或者IPv6私网IP绑定带宽，支持公网访问。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AttachVipBandwidth
        :type request: :class:`huaweicloudsdkiec.v1.AttachVipBandwidthRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.AttachVipBandwidthResponse`
        """
        http_info = self._attach_vip_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def attach_vip_bandwidth_async_invoker(self, request):
        http_info = self._attach_vip_bandwidth_http_info(request)
        return AsyncInvoker(self, http_info)

    def _attach_vip_bandwidth_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/vports/{vport_id}/bandwidth/attach",
            "request_type": request.__class__.__name__,
            "response_type": "AttachVipBandwidthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vport_id' in local_var_params:
            path_params['vport_id'] = local_var_params['vport_id']

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

    def detach_vip_bandwidth_async(self, request):
        r"""端口解绑带宽

        IPv6虚拟IP或者IPv6私网IP解绑带宽。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetachVipBandwidth
        :type request: :class:`huaweicloudsdkiec.v1.DetachVipBandwidthRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.DetachVipBandwidthResponse`
        """
        http_info = self._detach_vip_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def detach_vip_bandwidth_async_invoker(self, request):
        http_info = self._detach_vip_bandwidth_http_info(request)
        return AsyncInvoker(self, http_info)

    def _detach_vip_bandwidth_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/vports/{vport_id}/bandwidth/detach",
            "request_type": request.__class__.__name__,
            "response_type": "DetachVipBandwidthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vport_id' in local_var_params:
            path_params['vport_id'] = local_var_params['vport_id']

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

    def create_subnet_async(self, request):
        r"""创建子网

        根据用户的请求内容，创建子网。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSubnet
        :type request: :class:`huaweicloudsdkiec.v1.CreateSubnetRequest`
        :rtype: :class:`huaweicloudsdkiec.v1.CreateSubnetResponse`
        """
        http_info = self._create_subnet_http_info(request)
        return self._call_api(**http_info)

    def create_subnet_async_invoker(self, request):
        http_info = self._create_subnet_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_subnet_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/subnets",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSubnetResponse"
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
            kwargs["async_request"] = True
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
