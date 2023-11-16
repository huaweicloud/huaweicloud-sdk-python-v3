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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkddm'")


class DdmClient(Client):
    def __init__(self):
        super(DdmClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkddm.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "DdmClient":
                raise TypeError("client type error, support client type is DdmClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_database(self, request):
        """创建DDM逻辑库

        创建DDM逻辑库。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDatabase
        :type request: :class:`huaweicloudsdkddm.v1.CreateDatabaseRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.CreateDatabaseResponse`
        """
        http_info = self._create_database_http_info(request)
        return self._call_api(**http_info)

    def create_database_invoker(self, request):
        http_info = self._create_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_database_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/databases",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDatabaseResponse"
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
            ['application/json;charset=UTF-8'])

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

    def create_instance(self, request):
        """购买DDM实例

        创建一个DDM实例。
        
        DDM运行于虚拟私有云。申请DDM实例前，需保证有可用的虚拟私有云，并且已配置好子网与安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstance
        :type request: :class:`huaweicloudsdkddm.v1.CreateInstanceRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.CreateInstanceResponse`
        """
        http_info = self._create_instance_http_info(request)
        return self._call_api(**http_info)

    def create_instance_invoker(self, request):
        http_info = self._create_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances",
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
            ['application/json;charset=UTF-8'])

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

    def create_users(self, request):
        """创建DDM帐号

        DDM帐号用于连接和管理逻辑库。一个DDM实例最多能创建100个DDM帐号，一个DDM帐号可以关联多个逻辑库。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateUsers
        :type request: :class:`huaweicloudsdkddm.v1.CreateUsersRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.CreateUsersResponse`
        """
        http_info = self._create_users_http_info(request)
        return self._call_api(**http_info)

    def create_users_invoker(self, request):
        http_info = self._create_users_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_users_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "CreateUsersResponse"
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
            ['application/json;charset=UTF-8'])

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

    def delete_database(self, request):
        """删除DDM逻辑库

        删除指定的逻辑库，释放该逻辑库的所有资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDatabase
        :type request: :class:`huaweicloudsdkddm.v1.DeleteDatabaseRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.DeleteDatabaseResponse`
        """
        http_info = self._delete_database_http_info(request)
        return self._call_api(**http_info)

    def delete_database_invoker(self, request):
        http_info = self._delete_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_database_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/databases/{ddm_dbname}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDatabaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'ddm_dbname' in local_var_params:
            path_params['ddm_dbname'] = local_var_params['ddm_dbname']

        query_params = []
        if 'delete_rds_data' in local_var_params:
            query_params.append(('delete_rds_data', local_var_params['delete_rds_data']))

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

    def delete_instance(self, request):
        """删除DDM实例

        删除指定的DDM实例，释放该实例的所有资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstance
        :type request: :class:`huaweicloudsdkddm.v1.DeleteInstanceRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.DeleteInstanceResponse`
        """
        http_info = self._delete_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_invoker(self, request):
        http_info = self._delete_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_instance_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'delete_rds_data' in local_var_params:
            query_params.append(('delete_rds_data', local_var_params['delete_rds_data']))

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

    def delete_user(self, request):
        """删除DDM帐号

        删除指定的DDM实例帐号，如果帐号关联了逻辑库，则对应的关联关系也会删除。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteUser
        :type request: :class:`huaweicloudsdkddm.v1.DeleteUserRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.DeleteUserResponse`
        """
        http_info = self._delete_user_http_info(request)
        return self._call_api(**http_info)

    def delete_user_invoker(self, request):
        http_info = self._delete_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_user_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/users/{username}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'username' in local_var_params:
            path_params['username'] = local_var_params['username']

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

    def expand_instance_nodes(self, request):
        """DDM实例节点扩容

        对指定的DDM实例的节点个数进行扩容，支持按需实例与包周期实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExpandInstanceNodes
        :type request: :class:`huaweicloudsdkddm.v1.ExpandInstanceNodesRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ExpandInstanceNodesResponse`
        """
        http_info = self._expand_instance_nodes_http_info(request)
        return self._call_api(**http_info)

    def expand_instance_nodes_invoker(self, request):
        http_info = self._expand_instance_nodes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _expand_instance_nodes_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/action/enlarge",
            "request_type": request.__class__.__name__,
            "response_type": "ExpandInstanceNodesResponse"
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
            ['application/json;charset=UTF-8'])

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

    def list_available_rds_list(self, request):
        """查询创建逻辑库可选取的数据库实例列表

        查询创建逻辑库可选取的数据库实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAvailableRdsList
        :type request: :class:`huaweicloudsdkddm.v1.ListAvailableRdsListRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ListAvailableRdsListResponse`
        """
        http_info = self._list_available_rds_list_http_info(request)
        return self._call_api(**http_info)

    def list_available_rds_list_invoker(self, request):
        http_info = self._list_available_rds_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_available_rds_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/rds",
            "request_type": request.__class__.__name__,
            "response_type": "ListAvailableRdsListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_databases(self, request):
        """查询DDM逻辑库列表

        查询DDM逻辑库列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDatabases
        :type request: :class:`huaweicloudsdkddm.v1.ListDatabasesRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ListDatabasesResponse`
        """
        http_info = self._list_databases_http_info(request)
        return self._call_api(**http_info)

    def list_databases_invoker(self, request):
        http_info = self._list_databases_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_databases_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/databases",
            "request_type": request.__class__.__name__,
            "response_type": "ListDatabasesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_engines(self, request):
        """查询DDM引擎信息

        查询DDM引擎信息详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEngines
        :type request: :class:`huaweicloudsdkddm.v1.ListEnginesRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ListEnginesResponse`
        """
        http_info = self._list_engines_http_info(request)
        return self._call_api(**http_info)

    def list_engines_invoker(self, request):
        http_info = self._list_engines_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_engines_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/engines",
            "request_type": request.__class__.__name__,
            "response_type": "ListEnginesResponse"
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

    def list_flavors(self, request):
        """查询DDM可用区规格信息

        查询DDM可用区规格信息详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFlavors
        :type request: :class:`huaweicloudsdkddm.v1.ListFlavorsRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ListFlavorsResponse`
        """
        http_info = self._list_flavors_http_info(request)
        return self._call_api(**http_info)

    def list_flavors_invoker(self, request):
        http_info = self._list_flavors_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_flavors_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/flavors",
            "request_type": request.__class__.__name__,
            "response_type": "ListFlavorsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'engine_id' in local_var_params:
            query_params.append(('engine_id', local_var_params['engine_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_instances(self, request):
        """查询DDM实例列表

        查询DDM实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstances
        :type request: :class:`huaweicloudsdkddm.v1.ListInstancesRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ListInstancesResponse`
        """
        http_info = self._list_instances_http_info(request)
        return self._call_api(**http_info)

    def list_instances_invoker(self, request):
        http_info = self._list_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances",
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

    def list_nodes(self, request):
        """查询DDM实例节点列表

        查询DDM实例节点列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNodes
        :type request: :class:`huaweicloudsdkddm.v1.ListNodesRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ListNodesResponse`
        """
        http_info = self._list_nodes_http_info(request)
        return self._call_api(**http_info)

    def list_nodes_invoker(self, request):
        http_info = self._list_nodes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_nodes_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/nodes",
            "request_type": request.__class__.__name__,
            "response_type": "ListNodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_read_write_ratio(self, request):
        """读写比例监控

        查询指定时间段内在DDM实例的读写次数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListReadWriteRatio
        :type request: :class:`huaweicloudsdkddm.v1.ListReadWriteRatioRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ListReadWriteRatioResponse`
        """
        http_info = self._list_read_write_ratio_http_info(request)
        return self._call_api(**http_info)

    def list_read_write_ratio_invoker(self, request):
        http_info = self._list_read_write_ratio_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_read_write_ratio_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/read-write-ratio",
            "request_type": request.__class__.__name__,
            "response_type": "ListReadWriteRatioResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'cur_page' in local_var_params:
            query_params.append(('curPage', local_var_params['cur_page']))
        if 'per_page' in local_var_params:
            query_params.append(('perPage', local_var_params['per_page']))
        if 'start_date' in local_var_params:
            query_params.append(('startDate', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('endDate', local_var_params['end_date']))

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

    def list_slow_log(self, request):
        """慢日志监控

        查询指定时间段内在DDM实例上执行过的慢sql相关信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSlowLog
        :type request: :class:`huaweicloudsdkddm.v1.ListSlowLogRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ListSlowLogResponse`
        """
        http_info = self._list_slow_log_http_info(request)
        return self._call_api(**http_info)

    def list_slow_log_invoker(self, request):
        http_info = self._list_slow_log_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_slow_log_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/slowlog",
            "request_type": request.__class__.__name__,
            "response_type": "ListSlowLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'cur_page' in local_var_params:
            query_params.append(('curPage', local_var_params['cur_page']))
        if 'per_page' in local_var_params:
            query_params.append(('perPage', local_var_params['per_page']))
        if 'start_date' in local_var_params:
            query_params.append(('startDate', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('endDate', local_var_params['end_date']))

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

    def list_users(self, request):
        """查询DDM帐号列表

        查询DDM帐号列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUsers
        :type request: :class:`huaweicloudsdkddm.v1.ListUsersRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ListUsersResponse`
        """
        http_info = self._list_users_http_info(request)
        return self._call_api(**http_info)

    def list_users_invoker(self, request):
        http_info = self._list_users_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_users_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "ListUsersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def rebuild_config(self, request):
        """DDM表数据重载

        DDM实例跨region容灾场景下，针对目标DDM实例实现表数据reload，使数据同步。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RebuildConfig
        :type request: :class:`huaweicloudsdkddm.v1.RebuildConfigRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.RebuildConfigResponse`
        """
        http_info = self._rebuild_config_http_info(request)
        return self._call_api(**http_info)

    def rebuild_config_invoker(self, request):
        http_info = self._rebuild_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _rebuild_config_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/reload-config",
            "request_type": request.__class__.__name__,
            "response_type": "RebuildConfigResponse"
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

    def reset_administrator(self, request):
        """DDM管理员账号密码管理

        首次调用时新建DDM管理员帐号并设置密码。后续调用时仅更新管理员密码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetAdministrator
        :type request: :class:`huaweicloudsdkddm.v1.ResetAdministratorRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ResetAdministratorResponse`
        """
        http_info = self._reset_administrator_http_info(request)
        return self._call_api(**http_info)

    def reset_administrator_invoker(self, request):
        http_info = self._reset_administrator_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_administrator_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/admin-user",
            "request_type": request.__class__.__name__,
            "response_type": "ResetAdministratorResponse"
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
            ['application/json;charset=UTF-8'])

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

    def reset_user_password(self, request):
        """重置DDM账号密码

        重置现有DDM帐号的密码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetUserPassword
        :type request: :class:`huaweicloudsdkddm.v1.ResetUserPasswordRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ResetUserPasswordResponse`
        """
        http_info = self._reset_user_password_http_info(request)
        return self._call_api(**http_info)

    def reset_user_password_invoker(self, request):
        http_info = self._reset_user_password_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_user_password_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/users/{username}/password",
            "request_type": request.__class__.__name__,
            "response_type": "ResetUserPasswordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'username' in local_var_params:
            path_params['username'] = local_var_params['username']

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
            ['application/json;charset=UTF-8'])

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

    def resize_flavor(self, request):
        """变更DDM实例规格

        变更DDM实例规格。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResizeFlavor
        :type request: :class:`huaweicloudsdkddm.v1.ResizeFlavorRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ResizeFlavorResponse`
        """
        http_info = self._resize_flavor_http_info(request)
        return self._call_api(**http_info)

    def resize_flavor_invoker(self, request):
        http_info = self._resize_flavor_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _resize_flavor_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/flavor",
            "request_type": request.__class__.__name__,
            "response_type": "ResizeFlavorResponse"
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
            ['application/json;charset=UTF-8'])

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

    def restart_instance(self, request):
        """重启DDM实例

        重启指定的DDM实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestartInstance
        :type request: :class:`huaweicloudsdkddm.v1.RestartInstanceRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.RestartInstanceResponse`
        """
        http_info = self._restart_instance_http_info(request)
        return self._call_api(**http_info)

    def restart_instance_invoker(self, request):
        http_info = self._restart_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restart_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "RestartInstanceResponse"
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
            ['application/json;charset=UTF-8'])

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

    def show_database(self, request):
        """查询DDM逻辑库详细信息

        查询指定逻辑库的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDatabase
        :type request: :class:`huaweicloudsdkddm.v1.ShowDatabaseRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ShowDatabaseResponse`
        """
        http_info = self._show_database_http_info(request)
        return self._call_api(**http_info)

    def show_database_invoker(self, request):
        http_info = self._show_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_database_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/databases/{ddm_dbname}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDatabaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'ddm_dbname' in local_var_params:
            path_params['ddm_dbname'] = local_var_params['ddm_dbname']

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

    def show_instance(self, request):
        """查询DDM实例详情

        查询指定DDM实例的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstance
        :type request: :class:`huaweicloudsdkddm.v1.ShowInstanceRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ShowInstanceResponse`
        """
        http_info = self._show_instance_http_info(request)
        return self._call_api(**http_info)

    def show_instance_invoker(self, request):
        http_info = self._show_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceResponse"
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

    def show_instance_param(self, request):
        """查询DDM指定实例的参数详情

        查询DDM指定实例的参数详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceParam
        :type request: :class:`huaweicloudsdkddm.v1.ShowInstanceParamRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ShowInstanceParamResponse`
        """
        http_info = self._show_instance_param_http_info(request)
        return self._call_api(**http_info)

    def show_instance_param_invoker(self, request):
        http_info = self._show_instance_param_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_param_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceParamResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def show_node(self, request):
        """查询DDM实例节点详情

        查询DDM实例节点详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNode
        :type request: :class:`huaweicloudsdkddm.v1.ShowNodeRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ShowNodeResponse`
        """
        http_info = self._show_node_http_info(request)
        return self._call_api(**http_info)

    def show_node_invoker(self, request):
        http_info = self._show_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_node_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/nodes/{node_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

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

    def shrink_instance_nodes(self, request):
        """DDM实例节点缩容

        对指定的DDM实例的节点个数进行缩容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShrinkInstanceNodes
        :type request: :class:`huaweicloudsdkddm.v1.ShrinkInstanceNodesRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ShrinkInstanceNodesResponse`
        """
        http_info = self._shrink_instance_nodes_http_info(request)
        return self._call_api(**http_info)

    def shrink_instance_nodes_invoker(self, request):
        http_info = self._shrink_instance_nodes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _shrink_instance_nodes_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/action/reduce",
            "request_type": request.__class__.__name__,
            "response_type": "ShrinkInstanceNodesResponse"
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
            ['application/json;charset=UTF-8'])

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

    def update_database_info(self, request):
        """同步DN信息

        同步当前DDM实例已关联的所有DN实例配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDatabaseInfo
        :type request: :class:`huaweicloudsdkddm.v1.UpdateDatabaseInfoRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.UpdateDatabaseInfoResponse`
        """
        http_info = self._update_database_info_http_info(request)
        return self._call_api(**http_info)

    def update_database_info_invoker(self, request):
        http_info = self._update_database_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_database_info_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/rds/sync",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDatabaseInfoResponse"
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

    def update_instance_name(self, request):
        """修改DDM实例名称

        修改DDM实例名称。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceName
        :type request: :class:`huaweicloudsdkddm.v1.UpdateInstanceNameRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.UpdateInstanceNameResponse`
        """
        http_info = self._update_instance_name_http_info(request)
        return self._call_api(**http_info)

    def update_instance_name_invoker(self, request):
        http_info = self._update_instance_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_name_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/modify-name",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceNameResponse"
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
            ['application/json;charset=UTF-8'])

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

    def update_instance_param(self, request):
        """修改DDM实例参数

        修改DDM实例参数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceParam
        :type request: :class:`huaweicloudsdkddm.v1.UpdateInstanceParamRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.UpdateInstanceParamResponse`
        """
        http_info = self._update_instance_param_http_info(request)
        return self._call_api(**http_info)

    def update_instance_param_invoker(self, request):
        http_info = self._update_instance_param_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_param_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceParamResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def update_instance_security_group(self, request):
        """修改DDM实例安全组

        修改DDM实例安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceSecurityGroup
        :type request: :class:`huaweicloudsdkddm.v1.UpdateInstanceSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.UpdateInstanceSecurityGroupResponse`
        """
        http_info = self._update_instance_security_group_http_info(request)
        return self._call_api(**http_info)

    def update_instance_security_group_invoker(self, request):
        http_info = self._update_instance_security_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_security_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/modify-security-group",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceSecurityGroupResponse"
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
            ['application/json;charset=UTF-8'])

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

    def update_read_and_write_strategy(self, request):
        """修改DDM已关联的数据库实例的读策略

        修改DDM已关联的数据库实例的读策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateReadAndWriteStrategy
        :type request: :class:`huaweicloudsdkddm.v1.UpdateReadAndWriteStrategyRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.UpdateReadAndWriteStrategyResponse`
        """
        http_info = self._update_read_and_write_strategy_http_info(request)
        return self._call_api(**http_info)

    def update_read_and_write_strategy_invoker(self, request):
        http_info = self._update_read_and_write_strategy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_read_and_write_strategy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/action/read-write-strategy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateReadAndWriteStrategyResponse"
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
            ['application/json;charset=UTF-8'])

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

    def update_user(self, request):
        """修改DDM帐号

        修改现有DDM帐号的权限或者与逻辑库的管理关系。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateUser
        :type request: :class:`huaweicloudsdkddm.v1.UpdateUserRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.UpdateUserResponse`
        """
        http_info = self._update_user_http_info(request)
        return self._call_api(**http_info)

    def update_user_invoker(self, request):
        http_info = self._update_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_user_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/users/{username}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'username' in local_var_params:
            path_params['username'] = local_var_params['username']

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
            ['application/json;charset=UTF-8'])

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

    def validate_weak_password(self, request):
        """弱密码校验

        弱密码校验
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ValidateWeakPassword
        :type request: :class:`huaweicloudsdkddm.v1.ValidateWeakPasswordRequest`
        :rtype: :class:`huaweicloudsdkddm.v1.ValidateWeakPasswordResponse`
        """
        http_info = self._validate_weak_password_http_info(request)
        return self._call_api(**http_info)

    def validate_weak_password_invoker(self, request):
        http_info = self._validate_weak_password_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _validate_weak_password_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/weak-password-verification",
            "request_type": request.__class__.__name__,
            "response_type": "ValidateWeakPasswordResponse"
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
            ['application/json;charset=UTF-8'])

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
