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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcae'")


class CaeAsyncClient(Client):
    def __init__(self):
        super(CaeAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcae.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CaeAsyncClient":
                raise TypeError("client type error, support client type is CaeAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_agency_async(self, request):
        r"""创建委托

        创建委托。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAgency
        :type request: :class:`huaweicloudsdkcae.v1.CreateAgencyRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.CreateAgencyResponse`
        """
        http_info = self._create_agency_http_info(request)
        return self._call_api(**http_info)

    def create_agency_async_invoker(self, request):
        http_info = self._create_agency_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_agency_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cae/agencies",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAgencyResponse"
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

    def list_agencies_async(self, request):
        r"""获取委托列表

        获取委托列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAgencies
        :type request: :class:`huaweicloudsdkcae.v1.ListAgenciesRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ListAgenciesResponse`
        """
        http_info = self._list_agencies_http_info(request)
        return self._call_api(**http_info)

    def list_agencies_async_invoker(self, request):
        http_info = self._list_agencies_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_agencies_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cae/agencies",
            "request_type": request.__class__.__name__,
            "response_type": "ListAgenciesResponse"
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

    def create_application_async(self, request):
        r"""创建应用

        创建应用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateApplication
        :type request: :class:`huaweicloudsdkcae.v1.CreateApplicationRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.CreateApplicationResponse`
        """
        http_info = self._create_application_http_info(request)
        return self._call_api(**http_info)

    def create_application_async_invoker(self, request):
        http_info = self._create_application_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_application_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cae/applications",
            "request_type": request.__class__.__name__,
            "response_type": "CreateApplicationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def delete_application_async(self, request):
        r"""删除应用

        删除应用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteApplication
        :type request: :class:`huaweicloudsdkcae.v1.DeleteApplicationRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.DeleteApplicationResponse`
        """
        http_info = self._delete_application_http_info(request)
        return self._call_api(**http_info)

    def delete_application_async_invoker(self, request):
        http_info = self._delete_application_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_application_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/cae/applications/{application_id}",
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
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def list_applications_async(self, request):
        r"""获取应用列表

        获取应用列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApplications
        :type request: :class:`huaweicloudsdkcae.v1.ListApplicationsRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ListApplicationsResponse`
        """
        http_info = self._list_applications_http_info(request)
        return self._call_api(**http_info)

    def list_applications_async_invoker(self, request):
        http_info = self._list_applications_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_applications_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cae/applications",
            "request_type": request.__class__.__name__,
            "response_type": "ListApplicationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def show_application_async(self, request):
        r"""获取应用详情

        获取应用详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowApplication
        :type request: :class:`huaweicloudsdkcae.v1.ShowApplicationRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ShowApplicationResponse`
        """
        http_info = self._show_application_http_info(request)
        return self._call_api(**http_info)

    def show_application_async_invoker(self, request):
        http_info = self._show_application_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_application_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cae/applications/{application_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApplicationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def create_certificate_async(self, request):
        r"""创建证书

        创建证书。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCertificate
        :type request: :class:`huaweicloudsdkcae.v1.CreateCertificateRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.CreateCertificateResponse`
        """
        http_info = self._create_certificate_http_info(request)
        return self._call_api(**http_info)

    def create_certificate_async_invoker(self, request):
        http_info = self._create_certificate_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_certificate_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cae/certificates",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def delete_certificate_async(self, request):
        r"""删除证书

        删除证书。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCertificate
        :type request: :class:`huaweicloudsdkcae.v1.DeleteCertificateRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.DeleteCertificateResponse`
        """
        http_info = self._delete_certificate_http_info(request)
        return self._call_api(**http_info)

    def delete_certificate_async_invoker(self, request):
        http_info = self._delete_certificate_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_certificate_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/cae/certificates/{certificate_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def list_certificates_async(self, request):
        r"""获取证书列表

        获取证书列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCertificates
        :type request: :class:`huaweicloudsdkcae.v1.ListCertificatesRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ListCertificatesResponse`
        """
        http_info = self._list_certificates_http_info(request)
        return self._call_api(**http_info)

    def list_certificates_async_invoker(self, request):
        http_info = self._list_certificates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_certificates_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cae/certificates",
            "request_type": request.__class__.__name__,
            "response_type": "ListCertificatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def update_certificate_async(self, request):
        r"""修改证书

        修改证书。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCertificate
        :type request: :class:`huaweicloudsdkcae.v1.UpdateCertificateRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.UpdateCertificateResponse`
        """
        http_info = self._update_certificate_http_info(request)
        return self._call_api(**http_info)

    def update_certificate_async_invoker(self, request):
        http_info = self._update_certificate_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_certificate_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/cae/certificates/{certificate_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def create_component_async(self, request):
        r"""创建组件

        创建组件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateComponent
        :type request: :class:`huaweicloudsdkcae.v1.CreateComponentRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.CreateComponentResponse`
        """
        http_info = self._create_component_http_info(request)
        return self._call_api(**http_info)

    def create_component_async_invoker(self, request):
        http_info = self._create_component_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_component_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cae/applications/{application_id}/components",
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
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def create_component_with_configuration_async(self, request):
        r"""创建、生效配置并部署组件

        创建、生效配置并部署组件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateComponentWithConfiguration
        :type request: :class:`huaweicloudsdkcae.v1.CreateComponentWithConfigurationRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.CreateComponentWithConfigurationResponse`
        """
        http_info = self._create_component_with_configuration_http_info(request)
        return self._call_api(**http_info)

    def create_component_with_configuration_async_invoker(self, request):
        http_info = self._create_component_with_configuration_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_component_with_configuration_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cae/applications/{application_id}/component-with-configurations",
            "request_type": request.__class__.__name__,
            "response_type": "CreateComponentWithConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def delete_component_async(self, request):
        r"""删除组件

        删除组件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteComponent
        :type request: :class:`huaweicloudsdkcae.v1.DeleteComponentRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.DeleteComponentResponse`
        """
        http_info = self._delete_component_http_info(request)
        return self._call_api(**http_info)

    def delete_component_async_invoker(self, request):
        http_info = self._delete_component_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_component_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/cae/applications/{application_id}/components/{component_id}",
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
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def execute_action_async(self, request):
        r"""操作组件

        对组件执行指定操作，如部署、升级、重启、停止、启动、伸缩、配置、回滚。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteAction
        :type request: :class:`huaweicloudsdkcae.v1.ExecuteActionRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ExecuteActionResponse`
        """
        http_info = self._execute_action_http_info(request)
        return self._call_api(**http_info)

    def execute_action_async_invoker(self, request):
        http_info = self._execute_action_http_info(request)
        return AsyncInvoker(self, http_info)

    def _execute_action_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cae/applications/{application_id}/components/{component_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteActionResponse"
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
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def list_component_instances_async(self, request):
        r"""获取组件实例列表

        获取组件实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListComponentInstances
        :type request: :class:`huaweicloudsdkcae.v1.ListComponentInstancesRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ListComponentInstancesResponse`
        """
        http_info = self._list_component_instances_http_info(request)
        return self._call_api(**http_info)

    def list_component_instances_async_invoker(self, request):
        http_info = self._list_component_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_component_instances_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cae/applications/{application_id}/components/{component_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListComponentInstancesResponse"
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
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def list_component_snapshots_async(self, request):
        r"""获取组件快照列表

        获取组件快照列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListComponentSnapshots
        :type request: :class:`huaweicloudsdkcae.v1.ListComponentSnapshotsRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ListComponentSnapshotsResponse`
        """
        http_info = self._list_component_snapshots_http_info(request)
        return self._call_api(**http_info)

    def list_component_snapshots_async_invoker(self, request):
        http_info = self._list_component_snapshots_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_component_snapshots_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cae/applications/{application_id}/components/{component_id}/snapshots",
            "request_type": request.__class__.__name__,
            "response_type": "ListComponentSnapshotsResponse"
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
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def list_components_async(self, request):
        r"""获取组件列表

        获取组件列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListComponents
        :type request: :class:`huaweicloudsdkcae.v1.ListComponentsRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ListComponentsResponse`
        """
        http_info = self._list_components_http_info(request)
        return self._call_api(**http_info)

    def list_components_async_invoker(self, request):
        http_info = self._list_components_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_components_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cae/applications/{application_id}/components",
            "request_type": request.__class__.__name__,
            "response_type": "ListComponentsResponse"
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
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def show_component_async(self, request):
        r"""获取组件详情

        获取组件详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowComponent
        :type request: :class:`huaweicloudsdkcae.v1.ShowComponentRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ShowComponentResponse`
        """
        http_info = self._show_component_http_info(request)
        return self._call_api(**http_info)

    def show_component_async_invoker(self, request):
        http_info = self._show_component_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_component_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cae/applications/{application_id}/components/{component_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowComponentResponse"
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
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def update_component_async(self, request):
        r"""更新组件

        更新组件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateComponent
        :type request: :class:`huaweicloudsdkcae.v1.UpdateComponentRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.UpdateComponentResponse`
        """
        http_info = self._update_component_http_info(request)
        return self._call_api(**http_info)

    def update_component_async_invoker(self, request):
        http_info = self._update_component_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_component_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/cae/applications/{application_id}/components/{component_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateComponentResponse"
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
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def create_component_configuration_async(self, request):
        r"""创建组件配置

        创建组件配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateComponentConfiguration
        :type request: :class:`huaweicloudsdkcae.v1.CreateComponentConfigurationRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.CreateComponentConfigurationResponse`
        """
        http_info = self._create_component_configuration_http_info(request)
        return self._call_api(**http_info)

    def create_component_configuration_async_invoker(self, request):
        http_info = self._create_component_configuration_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_component_configuration_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cae/applications/{application_id}/components/{component_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "CreateComponentConfigurationResponse"
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
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def delete_component_configuration_async(self, request):
        r"""删除组件配置

        删除组件配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteComponentConfiguration
        :type request: :class:`huaweicloudsdkcae.v1.DeleteComponentConfigurationRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.DeleteComponentConfigurationResponse`
        """
        http_info = self._delete_component_configuration_http_info(request)
        return self._call_api(**http_info)

    def delete_component_configuration_async_invoker(self, request):
        http_info = self._delete_component_configuration_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_component_configuration_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/cae/applications/{application_id}/components/{component_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteComponentConfigurationResponse"
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
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def list_component_configurations_async(self, request):
        r"""获取组件配置列表

        获取组件配置列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListComponentConfigurations
        :type request: :class:`huaweicloudsdkcae.v1.ListComponentConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ListComponentConfigurationsResponse`
        """
        http_info = self._list_component_configurations_http_info(request)
        return self._call_api(**http_info)

    def list_component_configurations_async_invoker(self, request):
        http_info = self._list_component_configurations_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_component_configurations_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cae/applications/{application_id}/components/{component_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "ListComponentConfigurationsResponse"
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
        if 'display_mode' in local_var_params:
            query_params.append(('displayMode', local_var_params['display_mode']))

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def create_domain_async(self, request):
        r"""创建域名

        创建域名。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDomain
        :type request: :class:`huaweicloudsdkcae.v1.CreateDomainRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.CreateDomainResponse`
        """
        http_info = self._create_domain_http_info(request)
        return self._call_api(**http_info)

    def create_domain_async_invoker(self, request):
        http_info = self._create_domain_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_domain_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cae/domains",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDomainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def delete_domain_async(self, request):
        r"""删除域名

        删除域名。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDomain
        :type request: :class:`huaweicloudsdkcae.v1.DeleteDomainRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.DeleteDomainResponse`
        """
        http_info = self._delete_domain_http_info(request)
        return self._call_api(**http_info)

    def delete_domain_async_invoker(self, request):
        http_info = self._delete_domain_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_domain_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/cae/domains/{domain_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDomainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def list_domains_async(self, request):
        r"""获取域名列表

        获取域名列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDomains
        :type request: :class:`huaweicloudsdkcae.v1.ListDomainsRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ListDomainsResponse`
        """
        http_info = self._list_domains_http_info(request)
        return self._call_api(**http_info)

    def list_domains_async_invoker(self, request):
        http_info = self._list_domains_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_domains_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cae/domains",
            "request_type": request.__class__.__name__,
            "response_type": "ListDomainsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def list_eips_async(self, request):
        r"""获取集群节点弹性公网IP列表

        获取集群节点弹性公网IP列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEips
        :type request: :class:`huaweicloudsdkcae.v1.ListEipsRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ListEipsResponse`
        """
        http_info = self._list_eips_http_info(request)
        return self._call_api(**http_info)

    def list_eips_async_invoker(self, request):
        http_info = self._list_eips_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_eips_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cae/eips",
            "request_type": request.__class__.__name__,
            "response_type": "ListEipsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def update_eip_async(self, request):
        r"""修改出入网带宽以及开闭状态

        修改出入网带宽以及开闭状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEip
        :type request: :class:`huaweicloudsdkcae.v1.UpdateEipRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.UpdateEipResponse`
        """
        http_info = self._update_eip_http_info(request)
        return self._call_api(**http_info)

    def update_eip_async_invoker(self, request):
        http_info = self._update_eip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_eip_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/cae/eips",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEipResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def create_environment_async(self, request):
        r"""创建环境

        创建环境。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEnvironment
        :type request: :class:`huaweicloudsdkcae.v1.CreateEnvironmentRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.CreateEnvironmentResponse`
        """
        http_info = self._create_environment_http_info(request)
        return self._call_api(**http_info)

    def create_environment_async_invoker(self, request):
        http_info = self._create_environment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_environment_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cae/environments",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEnvironmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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

    def delete_environment_async(self, request):
        r"""删除环境

        删除环境。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEnvironment
        :type request: :class:`huaweicloudsdkcae.v1.DeleteEnvironmentRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.DeleteEnvironmentResponse`
        """
        http_info = self._delete_environment_http_info(request)
        return self._call_api(**http_info)

    def delete_environment_async_invoker(self, request):
        http_info = self._delete_environment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_environment_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/cae/environments/{environment_id}",
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
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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

    def list_environments_async(self, request):
        r"""获取环境列表

        获取环境列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEnvironments
        :type request: :class:`huaweicloudsdkcae.v1.ListEnvironmentsRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ListEnvironmentsResponse`
        """
        http_info = self._list_environments_http_info(request)
        return self._call_api(**http_info)

    def list_environments_async_invoker(self, request):
        http_info = self._list_environments_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_environments_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cae/environments",
            "request_type": request.__class__.__name__,
            "response_type": "ListEnvironmentsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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

    def retry_job_async(self, request):
        r"""重试任务

        重试任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RetryJob
        :type request: :class:`huaweicloudsdkcae.v1.RetryJobRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.RetryJobResponse`
        """
        http_info = self._retry_job_http_info(request)
        return self._call_api(**http_info)

    def retry_job_async_invoker(self, request):
        http_info = self._retry_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _retry_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cae/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "RetryJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def show_job_async(self, request):
        r"""获取任务详情

        获取任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJob
        :type request: :class:`huaweicloudsdkcae.v1.ShowJobRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ShowJobResponse`
        """
        http_info = self._show_job_http_info(request)
        return self._call_api(**http_info)

    def show_job_async_invoker(self, request):
        http_info = self._show_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cae/jobs/{job_id}",
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
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def create_monitor_system_async(self, request):
        r"""创建监控系统配置

        创建监控系统配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMonitorSystem
        :type request: :class:`huaweicloudsdkcae.v1.CreateMonitorSystemRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.CreateMonitorSystemResponse`
        """
        http_info = self._create_monitor_system_http_info(request)
        return self._call_api(**http_info)

    def create_monitor_system_async_invoker(self, request):
        http_info = self._create_monitor_system_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_monitor_system_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cae/monitor-system",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMonitorSystemResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def show_monitor_system_async(self, request):
        r"""获取监控系统配置

        获取监控系统配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMonitorSystem
        :type request: :class:`huaweicloudsdkcae.v1.ShowMonitorSystemRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ShowMonitorSystemResponse`
        """
        http_info = self._show_monitor_system_http_info(request)
        return self._call_api(**http_info)

    def show_monitor_system_async_invoker(self, request):
        http_info = self._show_monitor_system_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_monitor_system_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cae/monitor-system",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMonitorSystemResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def update_monitor_system_async(self, request):
        r"""更新监控系统配置

        更新监控系统配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMonitorSystem
        :type request: :class:`huaweicloudsdkcae.v1.UpdateMonitorSystemRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.UpdateMonitorSystemResponse`
        """
        http_info = self._update_monitor_system_http_info(request)
        return self._call_api(**http_info)

    def update_monitor_system_async_invoker(self, request):
        http_info = self._update_monitor_system_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_monitor_system_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/cae/monitor-system/{monitor_system_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMonitorSystemResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'monitor_system_id' in local_var_params:
            path_params['monitor_system_id'] = local_var_params['monitor_system_id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def create_notice_rule_async(self, request):
        r"""创建事件通知规则。

        创建事件通知规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateNoticeRule
        :type request: :class:`huaweicloudsdkcae.v1.CreateNoticeRuleRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.CreateNoticeRuleResponse`
        """
        http_info = self._create_notice_rule_http_info(request)
        return self._call_api(**http_info)

    def create_notice_rule_async_invoker(self, request):
        http_info = self._create_notice_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_notice_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cae/notice-rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateNoticeRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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

    def delete_notice_rule_async(self, request):
        r"""删除事件通知规则。

        删除事件通知规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteNoticeRule
        :type request: :class:`huaweicloudsdkcae.v1.DeleteNoticeRuleRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.DeleteNoticeRuleResponse`
        """
        http_info = self._delete_notice_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_notice_rule_async_invoker(self, request):
        http_info = self._delete_notice_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_notice_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/cae/notice-rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNoticeRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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

    def list_notice_rules_async(self, request):
        r"""查询事件通知规则列表。

        查询事件通知规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNoticeRules
        :type request: :class:`huaweicloudsdkcae.v1.ListNoticeRulesRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ListNoticeRulesResponse`
        """
        http_info = self._list_notice_rules_http_info(request)
        return self._call_api(**http_info)

    def list_notice_rules_async_invoker(self, request):
        http_info = self._list_notice_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_notice_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cae/notice-rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListNoticeRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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

    def show_notice_rule_async(self, request):
        r"""查询事件通知规则。

        查询事件通知规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNoticeRule
        :type request: :class:`huaweicloudsdkcae.v1.ShowNoticeRuleRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ShowNoticeRuleResponse`
        """
        http_info = self._show_notice_rule_http_info(request)
        return self._call_api(**http_info)

    def show_notice_rule_async_invoker(self, request):
        http_info = self._show_notice_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_notice_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cae/notice-rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNoticeRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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

    def update_notice_rule_async(self, request):
        r"""修改事件通知规则。

        修改事件通知规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateNoticeRule
        :type request: :class:`huaweicloudsdkcae.v1.UpdateNoticeRuleRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.UpdateNoticeRuleResponse`
        """
        http_info = self._update_notice_rule_http_info(request)
        return self._call_api(**http_info)

    def update_notice_rule_async_invoker(self, request):
        http_info = self._update_notice_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_notice_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/cae/notice-rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNoticeRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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

    def create_secret_async(self, request):
        r"""关联租户已注册的凭据。

        关联租户已注册的凭据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSecret
        :type request: :class:`huaweicloudsdkcae.v1.CreateSecretRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.CreateSecretResponse`
        """
        http_info = self._create_secret_http_info(request)
        return self._call_api(**http_info)

    def create_secret_async_invoker(self, request):
        http_info = self._create_secret_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_secret_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cae/dew-secrets",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSecretResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def delete_secret_async(self, request):
        r"""删除用户已在DEW服务上注册的凭据。

        删除用户已在DEW服务上注册的凭据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSecret
        :type request: :class:`huaweicloudsdkcae.v1.DeleteSecretRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.DeleteSecretResponse`
        """
        http_info = self._delete_secret_http_info(request)
        return self._call_api(**http_info)

    def delete_secret_async_invoker(self, request):
        http_info = self._delete_secret_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_secret_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/cae/dew-secrets/{secret_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSecretResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_id' in local_var_params:
            path_params['secret_id'] = local_var_params['secret_id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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

    def list_effective_components_async(self, request):
        r"""获取当前正在使用对应凭据组件列表。

        获取当前正在使用的对应凭据组件列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEffectiveComponents
        :type request: :class:`huaweicloudsdkcae.v1.ListEffectiveComponentsRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ListEffectiveComponentsResponse`
        """
        http_info = self._list_effective_components_http_info(request)
        return self._call_api(**http_info)

    def list_effective_components_async_invoker(self, request):
        http_info = self._list_effective_components_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_effective_components_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cae/dew-secrets/{secret_id}/effective-components",
            "request_type": request.__class__.__name__,
            "response_type": "ListEffectiveComponentsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_id' in local_var_params:
            path_params['secret_id'] = local_var_params['secret_id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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

    def list_secrets_async(self, request):
        r"""获取用户现有的凭据。

        获取用户现有的凭据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSecrets
        :type request: :class:`huaweicloudsdkcae.v1.ListSecretsRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ListSecretsResponse`
        """
        http_info = self._list_secrets_http_info(request)
        return self._call_api(**http_info)

    def list_secrets_async_invoker(self, request):
        http_info = self._list_secrets_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_secrets_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cae/dew-secrets",
            "request_type": request.__class__.__name__,
            "response_type": "ListSecretsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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

    def update_secret_async(self, request):
        r"""修改用户已在DEW服务上注册的凭据版本。

        修改用户已在DEW服务上注册的凭据版本。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSecret
        :type request: :class:`huaweicloudsdkcae.v1.UpdateSecretRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.UpdateSecretResponse`
        """
        http_info = self._update_secret_http_info(request)
        return self._call_api(**http_info)

    def update_secret_async_invoker(self, request):
        http_info = self._update_secret_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_secret_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/cae/dew-secrets/{secret_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSecretResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'secret_id' in local_var_params:
            path_params['secret_id'] = local_var_params['secret_id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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

    def create_volume_async(self, request):
        r"""授权云存储

        授权云存储。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVolume
        :type request: :class:`huaweicloudsdkcae.v1.CreateVolumeRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.CreateVolumeResponse`
        """
        http_info = self._create_volume_http_info(request)
        return self._call_api(**http_info)

    def create_volume_async_invoker(self, request):
        http_info = self._create_volume_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_volume_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cae/volumes",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVolumeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def delete_volume_async(self, request):
        r"""解绑云存储

        解绑云存储。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteVolume
        :type request: :class:`huaweicloudsdkcae.v1.DeleteVolumeRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.DeleteVolumeResponse`
        """
        http_info = self._delete_volume_http_info(request)
        return self._call_api(**http_info)

    def delete_volume_async_invoker(self, request):
        http_info = self._delete_volume_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_volume_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/cae/volumes/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVolumeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def list_volumes_async(self, request):
        r"""获取云存储列表

        获取云存储列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVolumes
        :type request: :class:`huaweicloudsdkcae.v1.ListVolumesRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ListVolumesResponse`
        """
        http_info = self._list_volumes_http_info(request)
        return self._call_api(**http_info)

    def list_volumes_async_invoker(self, request):
        http_info = self._list_volumes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_volumes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cae/volumes",
            "request_type": request.__class__.__name__,
            "response_type": "ListVolumesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def create_vpc_egress_async(self, request):
        r"""创建CAE环境访问VPC配置

        创建CAE环境访问VPC配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVpcEgress
        :type request: :class:`huaweicloudsdkcae.v1.CreateVpcEgressRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.CreateVpcEgressResponse`
        """
        http_info = self._create_vpc_egress_http_info(request)
        return self._call_api(**http_info)

    def create_vpc_egress_async_invoker(self, request):
        http_info = self._create_vpc_egress_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_vpc_egress_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cae/vpc-egress",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVpcEgressResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def delete_vpc_egress_async(self, request):
        r"""删除CAE环境访问VPC配置

        删除CAE环境访问VPC配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteVpcEgress
        :type request: :class:`huaweicloudsdkcae.v1.DeleteVpcEgressRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.DeleteVpcEgressResponse`
        """
        http_info = self._delete_vpc_egress_http_info(request)
        return self._call_api(**http_info)

    def delete_vpc_egress_async_invoker(self, request):
        http_info = self._delete_vpc_egress_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_vpc_egress_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/cae/vpc-egress/{vpc_egress_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVpcEgressResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_egress_id' in local_var_params:
            path_params['vpc_egress_id'] = local_var_params['vpc_egress_id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def list_vpc_egress_async(self, request):
        r"""获取CAE环境访问VPC配置

        获取CAE环境访问VPC配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVpcEgress
        :type request: :class:`huaweicloudsdkcae.v1.ListVpcEgressRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ListVpcEgressResponse`
        """
        http_info = self._list_vpc_egress_http_info(request)
        return self._call_api(**http_info)

    def list_vpc_egress_async_invoker(self, request):
        http_info = self._list_vpc_egress_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_vpc_egress_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cae/vpc-egress",
            "request_type": request.__class__.__name__,
            "response_type": "ListVpcEgressResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def create_timer_rule_async(self, request):
        r"""创建定时启停规则

        创建定时启停规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTimerRule
        :type request: :class:`huaweicloudsdkcae.v1.CreateTimerRuleRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.CreateTimerRuleResponse`
        """
        http_info = self._create_timer_rule_http_info(request)
        return self._call_api(**http_info)

    def create_timer_rule_async_invoker(self, request):
        http_info = self._create_timer_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_timer_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cae/timer-rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTimerRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def delete_timer_rule_async(self, request):
        r"""删除定时启停规则

        删除定时启停规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTimerRule
        :type request: :class:`huaweicloudsdkcae.v1.DeleteTimerRuleRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.DeleteTimerRuleResponse`
        """
        http_info = self._delete_timer_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_timer_rule_async_invoker(self, request):
        http_info = self._delete_timer_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_timer_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/cae/timer-rules/{timer_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTimerRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'timer_rule_id' in local_var_params:
            path_params['timer_rule_id'] = local_var_params['timer_rule_id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def list_timer_rules_async(self, request):
        r"""获取定时启停规则列表

        获取定时启停规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTimerRules
        :type request: :class:`huaweicloudsdkcae.v1.ListTimerRulesRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ListTimerRulesResponse`
        """
        http_info = self._list_timer_rules_http_info(request)
        return self._call_api(**http_info)

    def list_timer_rules_async_invoker(self, request):
        http_info = self._list_timer_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_timer_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cae/timer-rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListTimerRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def show_execution_result_async(self, request):
        r"""获取上次定时启停规则的执行情况

        获取上次定时启停规则的执行情况。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowExecutionResult
        :type request: :class:`huaweicloudsdkcae.v1.ShowExecutionResultRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.ShowExecutionResultResponse`
        """
        http_info = self._show_execution_result_http_info(request)
        return self._call_api(**http_info)

    def show_execution_result_async_invoker(self, request):
        http_info = self._show_execution_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_execution_result_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cae/timer-rules/{timer_rule_id}/execution-results",
            "request_type": request.__class__.__name__,
            "response_type": "ShowExecutionResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'timer_rule_id' in local_var_params:
            path_params['timer_rule_id'] = local_var_params['timer_rule_id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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

    def update_timer_rule_async(self, request):
        r"""修改定时启停规则

        修改定时启停规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTimerRule
        :type request: :class:`huaweicloudsdkcae.v1.UpdateTimerRuleRequest`
        :rtype: :class:`huaweicloudsdkcae.v1.UpdateTimerRuleResponse`
        """
        http_info = self._update_timer_rule_http_info(request)
        return self._call_api(**http_info)

    def update_timer_rule_async_invoker(self, request):
        http_info = self._update_timer_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_timer_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/cae/timer-rules/{timer_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTimerRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'timer_rule_id' in local_var_params:
            path_params['timer_rule_id'] = local_var_params['timer_rule_id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment_id' in local_var_params:
            header_params['X-Environment-ID'] = local_var_params['x_environment_id']

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
