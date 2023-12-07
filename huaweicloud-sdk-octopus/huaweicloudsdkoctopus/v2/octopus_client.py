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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkoctopus'")


class OctopusClient(Client):
    def __init__(self):
        super(OctopusClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkoctopus.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "OctopusClient":
                raise TypeError("client type error, support client type is OctopusClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_sim_sm_maps(self, request):
        """创建场景地图

        创建场景地图.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSimSmMaps
        :type request: :class:`huaweicloudsdkoctopus.v2.CreateSimSmMapsRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.CreateSimSmMapsResponse`
        """
        http_info = self._create_sim_sm_maps_http_info(request)
        return self._call_api(**http_info)

    def create_sim_sm_maps_invoker(self, request):
        http_info = self._create_sim_sm_maps_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_sim_sm_maps_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/sim/sm/maps",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSimSmMapsResponse"
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

    def create_sim_sm_scenarios(self, request):
        """创建仿真场景

        创建仿真场景.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSimSmScenarios
        :type request: :class:`huaweicloudsdkoctopus.v2.CreateSimSmScenariosRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.CreateSimSmScenariosResponse`
        """
        http_info = self._create_sim_sm_scenarios_http_info(request)
        return self._call_api(**http_info)

    def create_sim_sm_scenarios_invoker(self, request):
        http_info = self._create_sim_sm_scenarios_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_sim_sm_scenarios_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/sim/sm/scenarios",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSimSmScenariosResponse"
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

    def create_sim_sm_scenarios_files(self, request):
        """创建场景文件

        创建场景文件.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSimSmScenariosFiles
        :type request: :class:`huaweicloudsdkoctopus.v2.CreateSimSmScenariosFilesRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.CreateSimSmScenariosFilesResponse`
        """
        http_info = self._create_sim_sm_scenarios_files_http_info(request)
        return self._call_api(**http_info)

    def create_sim_sm_scenarios_files_invoker(self, request):
        http_info = self._create_sim_sm_scenarios_files_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_sim_sm_scenarios_files_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/sim/sm/scenarios/{parent_lookup_id}/files",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSimSmScenariosFilesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'parent_lookup_id' in local_var_params:
            path_params['parent_lookup_id'] = local_var_params['parent_lookup_id']

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

    def list_sim_sm_scenarios(self, request):
        """场景列表

        A DRF ViewSet for Scenario.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSimSmScenarios
        :type request: :class:`huaweicloudsdkoctopus.v2.ListSimSmScenariosRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.ListSimSmScenariosResponse`
        """
        http_info = self._list_sim_sm_scenarios_http_info(request)
        return self._call_api(**http_info)

    def list_sim_sm_scenarios_invoker(self, request):
        http_info = self._list_sim_sm_scenarios_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sim_sm_scenarios_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/sim/sm/scenarios",
            "request_type": request.__class__.__name__,
            "response_type": "ListSimSmScenariosResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'exclude_group' in local_var_params:
            query_params.append(('exclude_group', local_var_params['exclude_group']))
        if 'file' in local_var_params:
            query_params.append(('file', local_var_params['file']))
        if 'gen_scenario' in local_var_params:
            query_params.append(('gen_scenario', local_var_params['gen_scenario']))
        if 'group' in local_var_params:
            query_params.append(('group', local_var_params['group']))
            collection_formats['group'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'label' in local_var_params:
            query_params.append(('label', local_var_params['label']))
        if 'map' in local_var_params:
            query_params.append(('map', local_var_params['map']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'ordering' in local_var_params:
            query_params.append(('ordering', local_var_params['ordering']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))
        if 'simulator' in local_var_params:
            query_params.append(('simulator', local_var_params['simulator']))
        if 'source' in local_var_params:
            query_params.append(('source', local_var_params['source']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))

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

    def update_sim_sm_maps_files(self, request):
        """修改场景地图文件

        修改场景地图文件.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSimSmMapsFiles
        :type request: :class:`huaweicloudsdkoctopus.v2.UpdateSimSmMapsFilesRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.UpdateSimSmMapsFilesResponse`
        """
        http_info = self._update_sim_sm_maps_files_http_info(request)
        return self._call_api(**http_info)

    def update_sim_sm_maps_files_invoker(self, request):
        http_info = self._update_sim_sm_maps_files_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_sim_sm_maps_files_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v2/{project_id}/sim/sm/maps/{parent_lookup_id}/files/{sha256}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSimSmMapsFilesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'parent_lookup_id' in local_var_params:
            path_params['parent_lookup_id'] = local_var_params['parent_lookup_id']
        if 'sha256' in local_var_params:
            path_params['sha256'] = local_var_params['sha256']

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

    def update_sim_sm_scenarios_files(self, request):
        """修改场景文件

        修改场景文件.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSimSmScenariosFiles
        :type request: :class:`huaweicloudsdkoctopus.v2.UpdateSimSmScenariosFilesRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.UpdateSimSmScenariosFilesResponse`
        """
        http_info = self._update_sim_sm_scenarios_files_http_info(request)
        return self._call_api(**http_info)

    def update_sim_sm_scenarios_files_invoker(self, request):
        http_info = self._update_sim_sm_scenarios_files_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_sim_sm_scenarios_files_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v2/{project_id}/sim/sm/scenarios/{parent_lookup_id}/files/{sha256}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSimSmScenariosFilesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'parent_lookup_id' in local_var_params:
            path_params['parent_lookup_id'] = local_var_params['parent_lookup_id']
        if 'sha256' in local_var_params:
            path_params['sha256'] = local_var_params['sha256']

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
