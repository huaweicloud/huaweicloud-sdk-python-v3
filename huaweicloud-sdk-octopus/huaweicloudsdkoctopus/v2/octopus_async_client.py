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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkoctopus'")


class OctopusAsyncClient(Client):
    def __init__(self):
        super(OctopusAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkoctopus.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "OctopusAsyncClient":
                raise TypeError("client type error, support client type is OctopusAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_sim_algorithm_images_async(self, request):
        r"""创建算法镜像

        A DRF ViewSet for algorithm image.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSimAlgorithmImages
        :type request: :class:`huaweicloudsdkoctopus.v2.CreateSimAlgorithmImagesRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.CreateSimAlgorithmImagesResponse`
        """
        http_info = self._create_sim_algorithm_images_http_info(request)
        return self._call_api(**http_info)

    def create_sim_algorithm_images_async_invoker(self, request):
        http_info = self._create_sim_algorithm_images_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_sim_algorithm_images_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/sim/pm/algorithm-images",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSimAlgorithmImagesResponse"
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

    def create_sim_algorithms_async(self, request):
        r"""创建算法

        A DRF ViewSet for algorithm.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSimAlgorithms
        :type request: :class:`huaweicloudsdkoctopus.v2.CreateSimAlgorithmsRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.CreateSimAlgorithmsResponse`
        """
        http_info = self._create_sim_algorithms_http_info(request)
        return self._call_api(**http_info)

    def create_sim_algorithms_async_invoker(self, request):
        http_info = self._create_sim_algorithms_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_sim_algorithms_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/sim/pm/algorithms",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSimAlgorithmsResponse"
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

    def create_sim_batch_configs_async(self, request):
        r"""创建仿真任务配置

        A DRF ViewSet for BatchConfig.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSimBatchConfigs
        :type request: :class:`huaweicloudsdkoctopus.v2.CreateSimBatchConfigsRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.CreateSimBatchConfigsResponse`
        """
        http_info = self._create_sim_batch_configs_http_info(request)
        return self._call_api(**http_info)

    def create_sim_batch_configs_async_invoker(self, request):
        http_info = self._create_sim_batch_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_sim_batch_configs_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/sim/pm/batch-configs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSimBatchConfigsResponse"
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

    def create_sim_batches_async(self, request):
        r"""创建仿真任务

        A DRF ViewSet for Batch.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSimBatches
        :type request: :class:`huaweicloudsdkoctopus.v2.CreateSimBatchesRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.CreateSimBatchesResponse`
        """
        http_info = self._create_sim_batches_http_info(request)
        return self._call_api(**http_info)

    def create_sim_batches_async_invoker(self, request):
        http_info = self._create_sim_batches_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_sim_batches_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/sim/pm/batches",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSimBatchesResponse"
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

    def create_sim_extensions_async(self, request):
        r"""创建扩展文件

        此接口用于创建扩展文件。接口基于地图文件的sha256判断扩展文件是否已存在，如果扩展文件不存在，响应中提供预签链接用于上传文件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSimExtensions
        :type request: :class:`huaweicloudsdkoctopus.v2.CreateSimExtensionsRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.CreateSimExtensionsResponse`
        """
        http_info = self._create_sim_extensions_http_info(request)
        return self._call_api(**http_info)

    def create_sim_extensions_async_invoker(self, request):
        http_info = self._create_sim_extensions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_sim_extensions_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/sim/pm/extensions",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSimExtensionsResponse"
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

    def create_sim_sm_maps_async(self, request):
        r"""创建场景地图

        创建场景地图.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSimSmMaps
        :type request: :class:`huaweicloudsdkoctopus.v2.CreateSimSmMapsRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.CreateSimSmMapsResponse`
        """
        http_info = self._create_sim_sm_maps_http_info(request)
        return self._call_api(**http_info)

    def create_sim_sm_maps_async_invoker(self, request):
        http_info = self._create_sim_sm_maps_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_sim_sm_maps_http_info(self, request):
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

    def create_sim_sm_scenarios_async(self, request):
        r"""创建仿真场景

        创建仿真场景.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSimSmScenarios
        :type request: :class:`huaweicloudsdkoctopus.v2.CreateSimSmScenariosRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.CreateSimSmScenariosResponse`
        """
        http_info = self._create_sim_sm_scenarios_http_info(request)
        return self._call_api(**http_info)

    def create_sim_sm_scenarios_async_invoker(self, request):
        http_info = self._create_sim_sm_scenarios_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_sim_sm_scenarios_http_info(self, request):
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

    def create_sim_sm_scenarios_files_async(self, request):
        r"""创建场景文件

        创建场景文件.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSimSmScenariosFiles
        :type request: :class:`huaweicloudsdkoctopus.v2.CreateSimSmScenariosFilesRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.CreateSimSmScenariosFilesResponse`
        """
        http_info = self._create_sim_sm_scenarios_files_http_info(request)
        return self._call_api(**http_info)

    def create_sim_sm_scenarios_files_async_invoker(self, request):
        http_info = self._create_sim_sm_scenarios_files_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_sim_sm_scenarios_files_http_info(self, request):
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

    def delete_sim_algorithm_images_async(self, request):
        r"""删除算法镜像

        A DRF ViewSet for algorithm image.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSimAlgorithmImages
        :type request: :class:`huaweicloudsdkoctopus.v2.DeleteSimAlgorithmImagesRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.DeleteSimAlgorithmImagesResponse`
        """
        http_info = self._delete_sim_algorithm_images_http_info(request)
        return self._call_api(**http_info)

    def delete_sim_algorithm_images_async_invoker(self, request):
        http_info = self._delete_sim_algorithm_images_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_sim_algorithm_images_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/sim/pm/algorithm-images/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSimAlgorithmImagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def delete_sim_algorithms_async(self, request):
        r"""删除算法

        A DRF ViewSet for algorithm.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSimAlgorithms
        :type request: :class:`huaweicloudsdkoctopus.v2.DeleteSimAlgorithmsRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.DeleteSimAlgorithmsResponse`
        """
        http_info = self._delete_sim_algorithms_http_info(request)
        return self._call_api(**http_info)

    def delete_sim_algorithms_async_invoker(self, request):
        http_info = self._delete_sim_algorithms_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_sim_algorithms_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/sim/pm/algorithms/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSimAlgorithmsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def delete_sim_batch_configs_async(self, request):
        r"""删除仿真任务配置

        A DRF ViewSet for BatchConfig.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSimBatchConfigs
        :type request: :class:`huaweicloudsdkoctopus.v2.DeleteSimBatchConfigsRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.DeleteSimBatchConfigsResponse`
        """
        http_info = self._delete_sim_batch_configs_http_info(request)
        return self._call_api(**http_info)

    def delete_sim_batch_configs_async_invoker(self, request):
        http_info = self._delete_sim_batch_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_sim_batch_configs_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/sim/pm/batch-configs/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSimBatchConfigsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def delete_sim_batches_async(self, request):
        r"""删除仿真任务

        A DRF ViewSet for Batch.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSimBatches
        :type request: :class:`huaweicloudsdkoctopus.v2.DeleteSimBatchesRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.DeleteSimBatchesResponse`
        """
        http_info = self._delete_sim_batches_http_info(request)
        return self._call_api(**http_info)

    def delete_sim_batches_async_invoker(self, request):
        http_info = self._delete_sim_batches_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_sim_batches_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/sim/pm/batches/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSimBatchesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def delete_sim_extensions_async(self, request):
        r"""删除扩展文件

        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSimExtensions
        :type request: :class:`huaweicloudsdkoctopus.v2.DeleteSimExtensionsRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.DeleteSimExtensionsResponse`
        """
        http_info = self._delete_sim_extensions_http_info(request)
        return self._call_api(**http_info)

    def delete_sim_extensions_async_invoker(self, request):
        http_info = self._delete_sim_extensions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_sim_extensions_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/sim/pm/extensions/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSimExtensionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def list_sim_algorithm_images_async(self, request):
        r"""获取算法镜像列表

        A DRF ViewSet for algorithm image.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSimAlgorithmImages
        :type request: :class:`huaweicloudsdkoctopus.v2.ListSimAlgorithmImagesRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.ListSimAlgorithmImagesResponse`
        """
        http_info = self._list_sim_algorithm_images_http_info(request)
        return self._call_api(**http_info)

    def list_sim_algorithm_images_async_invoker(self, request):
        http_info = self._list_sim_algorithm_images_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_sim_algorithm_images_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/sim/pm/algorithm-images",
            "request_type": request.__class__.__name__,
            "response_type": "ListSimAlgorithmImagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'algorithm' in local_var_params:
            query_params.append(('algorithm', local_var_params['algorithm']))
        if 'algorithm_id' in local_var_params:
            query_params.append(('algorithm_id', local_var_params['algorithm_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'ordering' in local_var_params:
            query_params.append(('ordering', local_var_params['ordering']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
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

    def list_sim_algorithms_async(self, request):
        r"""获取算法列表

        A DRF ViewSet for algorithm.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSimAlgorithms
        :type request: :class:`huaweicloudsdkoctopus.v2.ListSimAlgorithmsRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.ListSimAlgorithmsResponse`
        """
        http_info = self._list_sim_algorithms_http_info(request)
        return self._call_api(**http_info)

    def list_sim_algorithms_async_invoker(self, request):
        http_info = self._list_sim_algorithms_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_sim_algorithms_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/sim/pm/algorithms",
            "request_type": request.__class__.__name__,
            "response_type": "ListSimAlgorithmsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'ordering' in local_var_params:
            query_params.append(('ordering', local_var_params['ordering']))
        if 'image_repo_id' in local_var_params:
            query_params.append(('image_repo_id', local_var_params['image_repo_id']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))

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

    def list_sim_batch_configs_async(self, request):
        r"""获取仿真任务配置列表

        A DRF ViewSet for BatchConfig.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSimBatchConfigs
        :type request: :class:`huaweicloudsdkoctopus.v2.ListSimBatchConfigsRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.ListSimBatchConfigsResponse`
        """
        http_info = self._list_sim_batch_configs_http_info(request)
        return self._call_api(**http_info)

    def list_sim_batch_configs_async_invoker(self, request):
        http_info = self._list_sim_batch_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_sim_batch_configs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/sim/pm/batch-configs",
            "request_type": request.__class__.__name__,
            "response_type": "ListSimBatchConfigsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'algorithm_id' in local_var_params:
            query_params.append(('algorithm_id', local_var_params['algorithm_id']))
        if 'algorithm_name' in local_var_params:
            query_params.append(('algorithm_name', local_var_params['algorithm_name']))
        if 'builtins_algorithm' in local_var_params:
            query_params.append(('builtins_algorithm', local_var_params['builtins_algorithm']))
        if 'custom_evaluation_image_id' in local_var_params:
            query_params.append(('custom_evaluation_image_id', local_var_params['custom_evaluation_image_id']))
        if 'custom_simulator_image_id' in local_var_params:
            query_params.append(('custom_simulator_image_id', local_var_params['custom_simulator_image_id']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'evaluation_id' in local_var_params:
            query_params.append(('evaluation_id', local_var_params['evaluation_id']))
        if 'evaluation_name' in local_var_params:
            query_params.append(('evaluation_name', local_var_params['evaluation_name']))
        if 'evaluations' in local_var_params:
            query_params.append(('evaluations', local_var_params['evaluations']))
            collection_formats['evaluations'] = 'multi'
        if 'generalization_id' in local_var_params:
            query_params.append(('generalization_id', local_var_params['generalization_id']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'ordering' in local_var_params:
            query_params.append(('ordering', local_var_params['ordering']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))
        if 'suit_id' in local_var_params:
            query_params.append(('suit_id', local_var_params['suit_id']))
        if 'triggerable' in local_var_params:
            query_params.append(('triggerable', local_var_params['triggerable']))

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

    def list_sim_batches_async(self, request):
        r"""获取仿真任务列表

        A DRF ViewSet for Batch.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSimBatches
        :type request: :class:`huaweicloudsdkoctopus.v2.ListSimBatchesRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.ListSimBatchesResponse`
        """
        http_info = self._list_sim_batches_http_info(request)
        return self._call_api(**http_info)

    def list_sim_batches_async_invoker(self, request):
        http_info = self._list_sim_batches_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_sim_batches_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/sim/pm/batches",
            "request_type": request.__class__.__name__,
            "response_type": "ListSimBatchesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'algorithm_image_version' in local_var_params:
            query_params.append(('algorithm_image_version', local_var_params['algorithm_image_version']))
        if 'algorithm_name' in local_var_params:
            query_params.append(('algorithm_name', local_var_params['algorithm_name']))
        if 'batch_config_id' in local_var_params:
            query_params.append(('batch_config_id', local_var_params['batch_config_id']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'generalization_id' in local_var_params:
            query_params.append(('generalization_id', local_var_params['generalization_id']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'ordering' in local_var_params:
            query_params.append(('ordering', local_var_params['ordering']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))
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

    def list_sim_extensions_async(self, request):
        r"""获取扩展文件列表

        A DRF ViewSet for Extensions.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSimExtensions
        :type request: :class:`huaweicloudsdkoctopus.v2.ListSimExtensionsRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.ListSimExtensionsResponse`
        """
        http_info = self._list_sim_extensions_http_info(request)
        return self._call_api(**http_info)

    def list_sim_extensions_async_invoker(self, request):
        http_info = self._list_sim_extensions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_sim_extensions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/sim/pm/extensions",
            "request_type": request.__class__.__name__,
            "response_type": "ListSimExtensionsResponse"
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
        if 'ordering' in local_var_params:
            query_params.append(('ordering', local_var_params['ordering']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))

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

    def list_sim_simulations_async(self, request):
        r"""获取仿真子任务列表

        List simulations data.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSimSimulations
        :type request: :class:`huaweicloudsdkoctopus.v2.ListSimSimulationsRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.ListSimSimulationsResponse`
        """
        http_info = self._list_sim_simulations_http_info(request)
        return self._call_api(**http_info)

    def list_sim_simulations_async_invoker(self, request):
        http_info = self._list_sim_simulations_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_sim_simulations_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/sim/pm/simulations",
            "request_type": request.__class__.__name__,
            "response_type": "ListSimSimulationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'algorithm_name' in local_var_params:
            query_params.append(('algorithm_name', local_var_params['algorithm_name']))
        if 'batch_id' in local_var_params:
            query_params.append(('batch_id', local_var_params['batch_id']))
        if 'batch_name' in local_var_params:
            query_params.append(('batch_name', local_var_params['batch_name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'label' in local_var_params:
            query_params.append(('label', local_var_params['label']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'ordering' in local_var_params:
            query_params.append(('ordering', local_var_params['ordering']))
        if 'scenario_resource_id' in local_var_params:
            query_params.append(('scenario_resource_id', local_var_params['scenario_resource_id']))
        if 'scenario_resource_type' in local_var_params:
            query_params.append(('scenario_resource_type', local_var_params['scenario_resource_type']))
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

    def list_sim_sm_scenarios_async(self, request):
        r"""场景列表

        A DRF ViewSet for Scenario.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSimSmScenarios
        :type request: :class:`huaweicloudsdkoctopus.v2.ListSimSmScenariosRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.ListSimSmScenariosResponse`
        """
        http_info = self._list_sim_sm_scenarios_http_info(request)
        return self._call_api(**http_info)

    def list_sim_sm_scenarios_async_invoker(self, request):
        http_info = self._list_sim_sm_scenarios_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_sim_sm_scenarios_http_info(self, request):
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

    def show_sim_algorithm_async(self, request):
        r"""获取算法详情

        A DRF ViewSet for algorithm.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSimAlgorithm
        :type request: :class:`huaweicloudsdkoctopus.v2.ShowSimAlgorithmRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.ShowSimAlgorithmResponse`
        """
        http_info = self._show_sim_algorithm_http_info(request)
        return self._call_api(**http_info)

    def show_sim_algorithm_async_invoker(self, request):
        http_info = self._show_sim_algorithm_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_sim_algorithm_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/sim/pm/algorithms/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSimAlgorithmResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def show_sim_algorithm_image_async(self, request):
        r"""获取算法镜像详情

        A DRF ViewSet for algorithm image.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSimAlgorithmImage
        :type request: :class:`huaweicloudsdkoctopus.v2.ShowSimAlgorithmImageRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.ShowSimAlgorithmImageResponse`
        """
        http_info = self._show_sim_algorithm_image_http_info(request)
        return self._call_api(**http_info)

    def show_sim_algorithm_image_async_invoker(self, request):
        http_info = self._show_sim_algorithm_image_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_sim_algorithm_image_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/sim/pm/algorithm-images/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSimAlgorithmImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def show_sim_batch_config_async(self, request):
        r"""获取仿真任务配置详情

        A DRF ViewSet for BatchConfig.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSimBatchConfig
        :type request: :class:`huaweicloudsdkoctopus.v2.ShowSimBatchConfigRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.ShowSimBatchConfigResponse`
        """
        http_info = self._show_sim_batch_config_http_info(request)
        return self._call_api(**http_info)

    def show_sim_batch_config_async_invoker(self, request):
        http_info = self._show_sim_batch_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_sim_batch_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/sim/pm/batch-configs/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSimBatchConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def show_sim_extension_async(self, request):
        r"""获取扩展文件详情

        A DRF ViewSet for Extensions.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSimExtension
        :type request: :class:`huaweicloudsdkoctopus.v2.ShowSimExtensionRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.ShowSimExtensionResponse`
        """
        http_info = self._show_sim_extension_http_info(request)
        return self._call_api(**http_info)

    def show_sim_extension_async_invoker(self, request):
        http_info = self._show_sim_extension_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_sim_extension_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/sim/pm/extensions/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSimExtensionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def show_sim_simulations_files_async(self, request):
        r"""获取指定的仿真任务下的pb、日志、回放文件

        Get obs file pre-signed url in simulation.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSimSimulationsFiles
        :type request: :class:`huaweicloudsdkoctopus.v2.ShowSimSimulationsFilesRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.ShowSimSimulationsFilesResponse`
        """
        http_info = self._show_sim_simulations_files_http_info(request)
        return self._call_api(**http_info)

    def show_sim_simulations_files_async_invoker(self, request):
        http_info = self._show_sim_simulations_files_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_sim_simulations_files_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/sim/pm/simulations/{id}/files",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSimSimulationsFilesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

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

    def update_sim_algorithm_images_async(self, request):
        r"""更新算法镜像

        A DRF ViewSet for algorithm image.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSimAlgorithmImages
        :type request: :class:`huaweicloudsdkoctopus.v2.UpdateSimAlgorithmImagesRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.UpdateSimAlgorithmImagesResponse`
        """
        http_info = self._update_sim_algorithm_images_http_info(request)
        return self._call_api(**http_info)

    def update_sim_algorithm_images_async_invoker(self, request):
        http_info = self._update_sim_algorithm_images_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_sim_algorithm_images_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v2/{project_id}/sim/pm/algorithm-images/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSimAlgorithmImagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def update_sim_algorithms_async(self, request):
        r"""更新算法

        A DRF ViewSet for algorithm.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSimAlgorithms
        :type request: :class:`huaweicloudsdkoctopus.v2.UpdateSimAlgorithmsRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.UpdateSimAlgorithmsResponse`
        """
        http_info = self._update_sim_algorithms_http_info(request)
        return self._call_api(**http_info)

    def update_sim_algorithms_async_invoker(self, request):
        http_info = self._update_sim_algorithms_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_sim_algorithms_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v2/{project_id}/sim/pm/algorithms/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSimAlgorithmsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def update_sim_batch_configs_extensions_async(self, request):
        r"""配置任务关联扩展文件

        A DRF ViewSet for &#x60;/batch-configs/x/extensions/&#x60;.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSimBatchConfigsExtensions
        :type request: :class:`huaweicloudsdkoctopus.v2.UpdateSimBatchConfigsExtensionsRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.UpdateSimBatchConfigsExtensionsResponse`
        """
        http_info = self._update_sim_batch_configs_extensions_http_info(request)
        return self._call_api(**http_info)

    def update_sim_batch_configs_extensions_async_invoker(self, request):
        http_info = self._update_sim_batch_configs_extensions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_sim_batch_configs_extensions_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/sim/pm/batch-configs/{batch_config_id}/extensions/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSimBatchConfigsExtensionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']
        if 'batch_config_id' in local_var_params:
            path_params['batch_config_id'] = local_var_params['batch_config_id']

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

    def update_sim_extensions_async(self, request):
        r"""修改扩展文件

        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSimExtensions
        :type request: :class:`huaweicloudsdkoctopus.v2.UpdateSimExtensionsRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.UpdateSimExtensionsResponse`
        """
        http_info = self._update_sim_extensions_http_info(request)
        return self._call_api(**http_info)

    def update_sim_extensions_async_invoker(self, request):
        http_info = self._update_sim_extensions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_sim_extensions_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v2/{project_id}/sim/pm/extensions/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSimExtensionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def update_sim_sm_maps_files_async(self, request):
        r"""修改场景地图文件

        修改场景地图文件.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSimSmMapsFiles
        :type request: :class:`huaweicloudsdkoctopus.v2.UpdateSimSmMapsFilesRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.UpdateSimSmMapsFilesResponse`
        """
        http_info = self._update_sim_sm_maps_files_http_info(request)
        return self._call_api(**http_info)

    def update_sim_sm_maps_files_async_invoker(self, request):
        http_info = self._update_sim_sm_maps_files_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_sim_sm_maps_files_http_info(self, request):
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

    def update_sim_sm_scenarios_files_async(self, request):
        r"""修改场景文件

        修改场景文件.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSimSmScenariosFiles
        :type request: :class:`huaweicloudsdkoctopus.v2.UpdateSimSmScenariosFilesRequest`
        :rtype: :class:`huaweicloudsdkoctopus.v2.UpdateSimSmScenariosFilesResponse`
        """
        http_info = self._update_sim_sm_scenarios_files_http_info(request)
        return self._call_api(**http_info)

    def update_sim_sm_scenarios_files_async_invoker(self, request):
        http_info = self._update_sim_sm_scenarios_files_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_sim_sm_scenarios_files_http_info(self, request):
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
