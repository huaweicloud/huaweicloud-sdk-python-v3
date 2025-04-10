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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkidme'")


class IdmeAsyncClient(Client):
    def __init__(self):
        super(IdmeAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkidme.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "IdmeAsyncClient":
                raise TypeError("client type error, support client type is IdmeAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_xdm_application_async(self, request):
        r"""创建应用

        本接口用于创建工业数字模型驱动引擎（Industrial Digital Model Engine，简称iDME）的应用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateXdmApplication
        :type request: :class:`huaweicloudsdkidme.v1.CreateXdmApplicationRequest`
        :rtype: :class:`huaweicloudsdkidme.v1.CreateXdmApplicationResponse`
        """
        http_info = self._create_xdm_application_http_info(request)
        return self._call_api(**http_info)

    def create_xdm_application_async_invoker(self, request):
        http_info = self._create_xdm_application_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_xdm_application_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/apps",
            "request_type": request.__class__.__name__,
            "response_type": "CreateXdmApplicationResponse"
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

    def delete_cloud_service_async(self, request):
        r"""删除iDME实例

        本接口用于删除工业数字模型驱动引擎（Industrial Digital Model Engine，简称iDME）实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCloudService
        :type request: :class:`huaweicloudsdkidme.v1.DeleteCloudServiceRequest`
        :rtype: :class:`huaweicloudsdkidme.v1.DeleteCloudServiceResponse`
        """
        http_info = self._delete_cloud_service_http_info(request)
        return self._call_api(**http_info)

    def delete_cloud_service_async_invoker(self, request):
        http_info = self._delete_cloud_service_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_cloud_service_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/{service_type}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCloudServiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_type' in local_var_params:
            path_params['service_type'] = local_var_params['service_type']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def delete_xdm_application_async(self, request):
        r"""删除应用

        本接口用于删除工业数字模型驱动引擎（Industrial Digital Model Engine，简称iDME）的应用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteXdmApplication
        :type request: :class:`huaweicloudsdkidme.v1.DeleteXdmApplicationRequest`
        :rtype: :class:`huaweicloudsdkidme.v1.DeleteXdmApplicationResponse`
        """
        http_info = self._delete_xdm_application_http_info(request)
        return self._call_api(**http_info)

    def delete_xdm_application_async_invoker(self, request):
        http_info = self._delete_xdm_application_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_xdm_application_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteXdmApplicationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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

    def deploy_application_async(self, request):
        r"""部署应用

        本接口用于部署工业数字模型驱动引擎（Industrial Digital Model Engine，简称iDME）的应用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeployApplication
        :type request: :class:`huaweicloudsdkidme.v1.DeployApplicationRequest`
        :rtype: :class:`huaweicloudsdkidme.v1.DeployApplicationResponse`
        """
        http_info = self._deploy_application_http_info(request)
        return self._call_api(**http_info)

    def deploy_application_async_invoker(self, request):
        http_info = self._deploy_application_http_info(request)
        return AsyncInvoker(self, http_info)

    def _deploy_application_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/envs/{env_id}/apps/{app_id}/deploy",
            "request_type": request.__class__.__name__,
            "response_type": "DeployApplicationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'env_id' in local_var_params:
            path_params['env_id'] = local_var_params['env_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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

    def list_apps_async(self, request):
        r"""获取租户下的应用清单

        本接口用于获取租户在工业数字模型驱动引擎（Industrial Digital Model Engine，简称iDME）的应用清单。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApps
        :type request: :class:`huaweicloudsdkidme.v1.ListAppsRequest`
        :rtype: :class:`huaweicloudsdkidme.v1.ListAppsResponse`
        """
        http_info = self._list_apps_http_info(request)
        return self._call_api(**http_info)

    def list_apps_async_invoker(self, request):
        http_info = self._list_apps_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_apps_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/apps",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_num' in local_var_params:
            query_params.append(('page_num', local_var_params['page_num']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))

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

    def list_envs_async(self, request):
        r"""获取运行服务清单

        本接口用于获取租户在工业数字模型驱动引擎（Industrial Digital Model Engine，简称iDME）的运行服务清单。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEnvs
        :type request: :class:`huaweicloudsdkidme.v1.ListEnvsRequest`
        :rtype: :class:`huaweicloudsdkidme.v1.ListEnvsResponse`
        """
        http_info = self._list_envs_http_info(request)
        return self._call_api(**http_info)

    def list_envs_async_invoker(self, request):
        http_info = self._list_envs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_envs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/envs",
            "request_type": request.__class__.__name__,
            "response_type": "ListEnvsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_num' in local_var_params:
            query_params.append(('page_num', local_var_params['page_num']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'env_types' in local_var_params:
            query_params.append(('env_types', local_var_params['env_types']))

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

    def modify_application_async(self, request):
        r"""编辑应用

        本接口用于修改工业数字模型驱动引擎（Industrial Digital Model Engine，简称iDME）的应用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ModifyApplication
        :type request: :class:`huaweicloudsdkidme.v1.ModifyApplicationRequest`
        :rtype: :class:`huaweicloudsdkidme.v1.ModifyApplicationResponse`
        """
        http_info = self._modify_application_http_info(request)
        return self._call_api(**http_info)

    def modify_application_async_invoker(self, request):
        http_info = self._modify_application_http_info(request)
        return AsyncInvoker(self, http_info)

    def _modify_application_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyApplicationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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

    def subscribe_cloud_service_async(self, request):
        r"""开通iDME实例

        本接口用于开通工业数字模型驱动引擎（Industrial Digital Model Engine，简称iDME）实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SubscribeCloudService
        :type request: :class:`huaweicloudsdkidme.v1.SubscribeCloudServiceRequest`
        :rtype: :class:`huaweicloudsdkidme.v1.SubscribeCloudServiceResponse`
        """
        http_info = self._subscribe_cloud_service_http_info(request)
        return self._call_api(**http_info)

    def subscribe_cloud_service_async_invoker(self, request):
        http_info = self._subscribe_cloud_service_http_info(request)
        return AsyncInvoker(self, http_info)

    def _subscribe_cloud_service_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{service_type}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "SubscribeCloudServiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_type' in local_var_params:
            path_params['service_type'] = local_var_params['service_type']

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

    def uninstall_async(self, request):
        r"""卸载应用

        本接口用于卸载指定运行服务下的工业数字模型驱动引擎（Industrial Digital Model Engine，简称iDME）应用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for Uninstall
        :type request: :class:`huaweicloudsdkidme.v1.UninstallRequest`
        :rtype: :class:`huaweicloudsdkidme.v1.UninstallResponse`
        """
        http_info = self._uninstall_http_info(request)
        return self._call_api(**http_info)

    def uninstall_async_invoker(self, request):
        http_info = self._uninstall_http_info(request)
        return AsyncInvoker(self, http_info)

    def _uninstall_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/envs/{env_id}/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UninstallResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'env_id' in local_var_params:
            path_params['env_id'] = local_var_params['env_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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
