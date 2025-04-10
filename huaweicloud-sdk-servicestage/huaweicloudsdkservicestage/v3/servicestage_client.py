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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkservicestage'")


class ServiceStageClient(Client):
    def __init__(self):
        super(ServiceStageClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkservicestage.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "ServiceStageClient":
                raise TypeError("client type error, support client type is ServiceStageClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_application(self, request):
        r"""创建应用

        应用是一个功能相对完备的业务系统，由一个或多个特性相关的组件组成。
        
        此API用来创建应用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateApplication
        :type request: :class:`huaweicloudsdkservicestage.v3.CreateApplicationRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v3.CreateApplicationResponse`
        """
        http_info = self._create_application_http_info(request)
        return self._call_api(**http_info)

    def create_application_invoker(self, request):
        http_info = self._create_application_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_application_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/cas/applications",
            "request_type": request.__class__.__name__,
            "response_type": "CreateApplicationResponse"
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

    def delete_application(self, request):
        r"""根据应用ID删除应用

        此API通过应用ID删除应用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApplication
        :type request: :class:`huaweicloudsdkservicestage.v3.DeleteApplicationRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v3.DeleteApplicationResponse`
        """
        http_info = self._delete_application_http_info(request)
        return self._call_api(**http_info)

    def delete_application_invoker(self, request):
        http_info = self._delete_application_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_application_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/cas/applications/{application_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteApplicationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

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

    def delete_application_configuration(self, request):
        r"""根据应用ID删除应用配置

        此API通过应用ID删除应用配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApplicationConfiguration
        :type request: :class:`huaweicloudsdkservicestage.v3.DeleteApplicationConfigurationRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v3.DeleteApplicationConfigurationResponse`
        """
        http_info = self._delete_application_configuration_http_info(request)
        return self._call_api(**http_info)

    def delete_application_configuration_invoker(self, request):
        http_info = self._delete_application_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_application_configuration_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/cas/applications/{application_id}/configuration",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteApplicationConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []
        if 'environment_id' in local_var_params:
            query_params.append(('environment_id', local_var_params['environment_id']))

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

    def modify_application(self, request):
        r"""根据应用ID修改应用信息

        此API通过应用ID修改应用信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyApplication
        :type request: :class:`huaweicloudsdkservicestage.v3.ModifyApplicationRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v3.ModifyApplicationResponse`
        """
        http_info = self._modify_application_http_info(request)
        return self._call_api(**http_info)

    def modify_application_invoker(self, request):
        http_info = self._modify_application_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_application_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/cas/applications/{application_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyApplicationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

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

    def modify_application_configuration(self, request):
        r"""根据应用ID修改应用配置

        此API通过应用ID修改应用配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyApplicationConfiguration
        :type request: :class:`huaweicloudsdkservicestage.v3.ModifyApplicationConfigurationRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v3.ModifyApplicationConfigurationResponse`
        """
        http_info = self._modify_application_configuration_http_info(request)
        return self._call_api(**http_info)

    def modify_application_configuration_invoker(self, request):
        http_info = self._modify_application_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_application_configuration_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/cas/applications/{application_id}/configuration",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyApplicationConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

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

    def show_application_configuration(self, request):
        r"""根据应用ID获取应用配置

        此API通过应用ID获取应用配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApplicationConfiguration
        :type request: :class:`huaweicloudsdkservicestage.v3.ShowApplicationConfigurationRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v3.ShowApplicationConfigurationResponse`
        """
        http_info = self._show_application_configuration_http_info(request)
        return self._call_api(**http_info)

    def show_application_configuration_invoker(self, request):
        http_info = self._show_application_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_application_configuration_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/cas/applications/{application_id}/configuration",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApplicationConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []
        if 'environment_id' in local_var_params:
            query_params.append(('environment_id', local_var_params['environment_id']))

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

    def show_application_info(self, request):
        r"""根据应用ID获取应用详细信息

        此API通过应用ID获取应用详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApplicationInfo
        :type request: :class:`huaweicloudsdkservicestage.v3.ShowApplicationInfoRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v3.ShowApplicationInfoResponse`
        """
        http_info = self._show_application_info_http_info(request)
        return self._call_api(**http_info)

    def show_application_info_invoker(self, request):
        http_info = self._show_application_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_application_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/cas/applications/{application_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApplicationInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

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

    def show_applications(self, request):
        r"""获取所用应用

        获取所有应用信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApplications
        :type request: :class:`huaweicloudsdkservicestage.v3.ShowApplicationsRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v3.ShowApplicationsResponse`
        """
        http_info = self._show_applications_http_info(request)
        return self._call_api(**http_info)

    def show_applications_invoker(self, request):
        http_info = self._show_applications_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_applications_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/cas/applications",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApplicationsResponse"
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
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))

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

    def create_component(self, request):
        r"""应用中创建组件

        此API用来在应用中创建组件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateComponent
        :type request: :class:`huaweicloudsdkservicestage.v3.CreateComponentRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v3.CreateComponentResponse`
        """
        http_info = self._create_component_http_info(request)
        return self._call_api(**http_info)

    def create_component_invoker(self, request):
        http_info = self._create_component_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_component_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/cas/applications/{application_id}/components",
            "request_type": request.__class__.__name__,
            "response_type": "CreateComponentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

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

    def delete_component(self, request):
        r"""根据组件ID删除组件

        此API通过组件ID删除组件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteComponent
        :type request: :class:`huaweicloudsdkservicestage.v3.DeleteComponentRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v3.DeleteComponentResponse`
        """
        http_info = self._delete_component_http_info(request)
        return self._call_api(**http_info)

    def delete_component_invoker(self, request):
        http_info = self._delete_component_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_component_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/cas/applications/{application_id}/components/{component_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteComponentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']

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

    def modify_component(self, request):
        r"""根据组件ID修改组件信息

        此API通过组件ID修改组件信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyComponent
        :type request: :class:`huaweicloudsdkservicestage.v3.ModifyComponentRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v3.ModifyComponentResponse`
        """
        http_info = self._modify_component_http_info(request)
        return self._call_api(**http_info)

    def modify_component_invoker(self, request):
        http_info = self._modify_component_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_component_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/cas/applications/{application_id}/components/{component_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyComponentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']

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

    def show_component_info(self, request):
        r"""根据组件ID获取组件信息

        通过组件ID获取组件信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowComponentInfo
        :type request: :class:`huaweicloudsdkservicestage.v3.ShowComponentInfoRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v3.ShowComponentInfoResponse`
        """
        http_info = self._show_component_info_http_info(request)
        return self._call_api(**http_info)

    def show_component_info_invoker(self, request):
        http_info = self._show_component_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_component_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/cas/applications/{application_id}/components/{component_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowComponentInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []
        if 'expect_fields' in local_var_params:
            query_params.append(('expect_fields', local_var_params['expect_fields']))

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

    def show_component_records(self, request):
        r"""通过组件ID获取记录

        此API用来通过组件ID获取记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowComponentRecords
        :type request: :class:`huaweicloudsdkservicestage.v3.ShowComponentRecordsRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v3.ShowComponentRecordsResponse`
        """
        http_info = self._show_component_records_http_info(request)
        return self._call_api(**http_info)

    def show_component_records_invoker(self, request):
        http_info = self._show_component_records_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_component_records_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/cas/applications/{application_id}/components/{component_id}/records",
            "request_type": request.__class__.__name__,
            "response_type": "ShowComponentRecordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))

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

    def show_components(self, request):
        r"""获取所有组件

        此API用来获取所有组件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowComponents
        :type request: :class:`huaweicloudsdkservicestage.v3.ShowComponentsRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v3.ShowComponentsResponse`
        """
        http_info = self._show_components_http_info(request)
        return self._call_api(**http_info)

    def show_components_invoker(self, request):
        http_info = self._show_components_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_components_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/cas/components",
            "request_type": request.__class__.__name__,
            "response_type": "ShowComponentsResponse"
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
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'application_name' in local_var_params:
            query_params.append(('application_name', local_var_params['application_name']))
        if 'component_name' in local_var_params:
            query_params.append(('component_name', local_var_params['component_name']))

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

    def show_components_in_application(self, request):
        r"""获取应用所有组件

        通过此API获取应用下所有应用组件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowComponentsInApplication
        :type request: :class:`huaweicloudsdkservicestage.v3.ShowComponentsInApplicationRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v3.ShowComponentsInApplicationResponse`
        """
        http_info = self._show_components_in_application_http_info(request)
        return self._call_api(**http_info)

    def show_components_in_application_invoker(self, request):
        http_info = self._show_components_in_application_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_components_in_application_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/cas/applications/{application_id}/components",
            "request_type": request.__class__.__name__,
            "response_type": "ShowComponentsInApplicationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))

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

    def update_component_action(self, request):
        r"""根据组件ID下发组件任务

        通过组件ID下发组件任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateComponentAction
        :type request: :class:`huaweicloudsdkservicestage.v3.UpdateComponentActionRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v3.UpdateComponentActionResponse`
        """
        http_info = self._update_component_action_http_info(request)
        return self._call_api(**http_info)

    def update_component_action_invoker(self, request):
        http_info = self._update_component_action_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_component_action_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/cas/applications/{application_id}/components/{component_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateComponentActionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']
        if 'component_id' in local_var_params:
            path_params['component_id'] = local_var_params['component_id']

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

    def create_environment(self, request):
        r"""创建环境

        环境是用于应用部署和运行的计算、存储、网络等基础设施的集合。Servicestage把相同VPC下的CCE集群加上多个ELB、RDS、DCS实例组合为一个环境，如：开发环境，测试环境，预生产环境，生产环境。环境内网络互通，可以按环境维度来管理资源、部署服务，减少具体基础设施运维管理的复杂性。
        
        此API用来创建环境。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEnvironment
        :type request: :class:`huaweicloudsdkservicestage.v3.CreateEnvironmentRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v3.CreateEnvironmentResponse`
        """
        http_info = self._create_environment_http_info(request)
        return self._call_api(**http_info)

    def create_environment_invoker(self, request):
        http_info = self._create_environment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_environment_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/cas/environments",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEnvironmentResponse"
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

    def delete_environment(self, request):
        r"""根据环境ID删除环境

        此API通过环境ID删除环境。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEnvironment
        :type request: :class:`huaweicloudsdkservicestage.v3.DeleteEnvironmentRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v3.DeleteEnvironmentResponse`
        """
        http_info = self._delete_environment_http_info(request)
        return self._call_api(**http_info)

    def delete_environment_invoker(self, request):
        http_info = self._delete_environment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_environment_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/cas/environments/{environment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEnvironmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'environment_id' in local_var_params:
            path_params['environment_id'] = local_var_params['environment_id']

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

    def modify_environment(self, request):
        r"""根据环境ID修改环境

        此API通过环境ID修改环境。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyEnvironment
        :type request: :class:`huaweicloudsdkservicestage.v3.ModifyEnvironmentRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v3.ModifyEnvironmentResponse`
        """
        http_info = self._modify_environment_http_info(request)
        return self._call_api(**http_info)

    def modify_environment_invoker(self, request):
        http_info = self._modify_environment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_environment_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/cas/environments/{environment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyEnvironmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'environment_id' in local_var_params:
            path_params['environment_id'] = local_var_params['environment_id']

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

    def modify_resource_in_environment(self, request):
        r"""根据环境ID修改环境资源

        此API用来通过环境ID修改环境资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyResourceInEnvironment
        :type request: :class:`huaweicloudsdkservicestage.v3.ModifyResourceInEnvironmentRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v3.ModifyResourceInEnvironmentResponse`
        """
        http_info = self._modify_resource_in_environment_http_info(request)
        return self._call_api(**http_info)

    def modify_resource_in_environment_invoker(self, request):
        http_info = self._modify_resource_in_environment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_resource_in_environment_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/cas/environments/{environment_id}/resources",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyResourceInEnvironmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'environment_id' in local_var_params:
            path_params['environment_id'] = local_var_params['environment_id']

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

    def show_environment_info(self, request):
        r"""根据环境ID获取环境详细信息

        此API通过环境ID获取环境详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEnvironmentInfo
        :type request: :class:`huaweicloudsdkservicestage.v3.ShowEnvironmentInfoRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v3.ShowEnvironmentInfoResponse`
        """
        http_info = self._show_environment_info_http_info(request)
        return self._call_api(**http_info)

    def show_environment_info_invoker(self, request):
        http_info = self._show_environment_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_environment_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/cas/environments/{environment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEnvironmentInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'environment_id' in local_var_params:
            path_params['environment_id'] = local_var_params['environment_id']

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

    def show_environment_resources(self, request):
        r"""根据环境ID查询环境资源

        此API用来根据环境ID查询环境资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEnvironmentResources
        :type request: :class:`huaweicloudsdkservicestage.v3.ShowEnvironmentResourcesRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v3.ShowEnvironmentResourcesResponse`
        """
        http_info = self._show_environment_resources_http_info(request)
        return self._call_api(**http_info)

    def show_environment_resources_invoker(self, request):
        http_info = self._show_environment_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_environment_resources_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/cas/environments/{environment_id}/resources",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEnvironmentResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'environment_id' in local_var_params:
            path_params['environment_id'] = local_var_params['environment_id']

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

    def show_environments(self, request):
        r"""获取所有环境

        此API用来获取所有已经创建环境。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEnvironments
        :type request: :class:`huaweicloudsdkservicestage.v3.ShowEnvironmentsRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v3.ShowEnvironmentsResponse`
        """
        http_info = self._show_environments_http_info(request)
        return self._call_api(**http_info)

    def show_environments_invoker(self, request):
        http_info = self._show_environments_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_environments_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/cas/environments",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEnvironmentsResponse"
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
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'environment_id' in local_var_params:
            query_params.append(('environment_id', local_var_params['environment_id']))
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

    def show_job_info(self, request):
        r"""get cas job infomation

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJobInfo
        :type request: :class:`huaweicloudsdkservicestage.v3.ShowJobInfoRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v3.ShowJobInfoResponse`
        """
        http_info = self._show_job_info_http_info(request)
        return self._call_api(**http_info)

    def show_job_info_invoker(self, request):
        http_info = self._show_job_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_job_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/cas/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'desc' in local_var_params:
            query_params.append(('desc', local_var_params['desc']))

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

    def show_runtime_stacks(self, request):
        r"""查询运行时栈

        获取运行时信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRuntimeStacks
        :type request: :class:`huaweicloudsdkservicestage.v3.ShowRuntimeStacksRequest`
        :rtype: :class:`huaweicloudsdkservicestage.v3.ShowRuntimeStacksResponse`
        """
        http_info = self._show_runtime_stacks_http_info(request)
        return self._call_api(**http_info)

    def show_runtime_stacks_invoker(self, request):
        http_info = self._show_runtime_stacks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_runtime_stacks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/cas/runtimestacks",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRuntimeStacksResponse"
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
