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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkidmeclassicapi'")


class IDMEClassicAPIClient(Client):
    def __init__(self):
        super().__init__()
        self.model_package = importlib.import_module("huaweicloudsdkidmeclassicapi.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "IDMEClassicAPIClient":
                raise TypeError("client type error, support client type is IDMEClassicAPIClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_tag(self, request):
        r"""绑定标签

        本接口用于为指定数据模型的数据实例绑定预定义的标签。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态创建并发布一个具有“标签管理”功能的数据模型。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        3. 已在应用运行态的“基础数据管理 &gt; 标签”中创建目标标签。具体操作请参见[标签](https://support.huaweicloud.com/usermanual-idme/idme_clientog_0096.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddTag
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.AddTagRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.AddTagResponse`
        """
        http_info = self._add_tag_http_info(request)
        return self._call_api(**http_info)

    def add_tag_invoker(self, request):
        http_info = self._add_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_tag_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/addTag",
            "request_type": request.__class__.__name__,
            "response_type": "AddTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def add_to_category(self, request):
        r"""添加数据分类

        本接口用于将数据实例添加到指定分类。当需要对零部件、设备、物料等数据实例进行归类管理（如按功能模块、产品线、工艺类型等维度分类）时，可调用本接口建立实例与分类的关联关系。
        - 当实例不存在时，系统将抛出异常。
        - 当实例与指定分类已存在关联关系时，系统将不重复添加，返回值为0。
        - 当实例与指定分类首次建立关联时，返回值为1。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddToCategory
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.AddToCategoryRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.AddToCategoryResponse`
        """
        http_info = self._add_to_category_http_info(request)
        return self._call_api(**http_info)

    def add_to_category_invoker(self, request):
        http_info = self._add_to_category_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_to_category_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/addToCategory",
            "request_type": request.__class__.__name__,
            "response_type": "AddToCategoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def batch_add_child_node(self, request):
        r"""批量添加实例的子节点

        本接口用于批量为指定数据实例添加子节点，建立父子层级关联关系。当BOM（物料清单）需要新增子装配节点、组织架构需要新增下属团队或产品分类需要新增下级类目时，可调用本接口批量完成节点挂载。
        - 调用本接口时，需在parentId中指定父节点实例ID，在childList中传入待添加为子节点的实例ID列表。
        - 添加操作执行后，子节点将发生以下变更：
          - 父节点（parentNode）字段被设置为指定的父节点。
          - 根节点（rootNode）字段被设置为父节点所在树的根节点。
        - 全路径（fullPath）和原始全路径（rawFullPath）字段被更新为包含父节点路径的完整路径。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchAddChildNode
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchAddChildNodeRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchAddChildNodeResponse`
        """
        http_info = self._batch_add_child_node_http_info(request)
        return self._call_api(**http_info)

    def batch_add_child_node_invoker(self, request):
        http_info = self._batch_add_child_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_add_child_node_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchAddChildNode",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAddChildNodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def batch_checkin(self, request):
        r"""批量检入M-V模型数据实例

        本接口用于根据主对象ID批量检入M-V模型数据实例。已检入的数据实例会生成一个新的迭代版本，并将数据存储至系统中。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCheckin
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchCheckinRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchCheckinResponse`
        """
        http_info = self._batch_checkin_http_info(request)
        return self._call_api(**http_info)

    def batch_checkin_invoker(self, request):
        http_info = self._batch_checkin_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_checkin_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchCheckin",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCheckinResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def batch_checkout(self, request):
        r"""批量检出M-V模型数据实例

        本接口用于根据主对象ID（masterId）列表，对指定的多个Master-Branch-Version（M-V）模型实例批量执行检出（Check-out）操作。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCheckout
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchCheckoutRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchCheckoutResponse`
        """
        http_info = self._batch_checkout_http_info(request)
        return self._call_api(**http_info)

    def batch_checkout_invoker(self, request):
        http_info = self._batch_checkout_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_checkout_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchCheckout",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCheckoutResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def batch_checkout_and_update(self, request):
        r"""批量检出并更新M-V模型

        本接口用于根据主对象ID（masterId）列表，对指定的多个Master-Branch-Version（M-V）模型实例批量执行检出（Check-out）并同步更新（Update）的原子操作。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCheckoutAndUpdate
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchCheckoutAndUpdateRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchCheckoutAndUpdateResponse`
        """
        http_info = self._batch_checkout_and_update_http_info(request)
        return self._call_api(**http_info)

    def batch_checkout_and_update_invoker(self, request):
        http_info = self._batch_checkout_and_update_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_checkout_and_update_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchCheckoutAndUpdate",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCheckoutAndUpdateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def batch_checkout_undo(self, request):
        r"""批量撤销检出M-V模型数据实例

        本接口用于批量撤销指定M-V模型实例的检出，将实例数据批量还原至检出前的内容。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCheckoutUndo
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchCheckoutUndoRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchCheckoutUndoResponse`
        """
        http_info = self._batch_checkout_undo_http_info(request)
        return self._call_api(**http_info)

    def batch_checkout_undo_invoker(self, request):
        http_info = self._batch_checkout_undo_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_checkout_undo_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchUndoCheckout",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCheckoutUndoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def batch_checkout_undo_by_admin(self, request):
        r"""管理员批量撤销检出M-V模型数据实例

        本接口用于管理员批量撤销Master-Branch-Version（M-V）模型实例的检出状态，将实例数据批量还原至检出前的最后检入版本内容。适用于数据治理中大规模清理长期锁定实例、批量处理离职员工未检入数据、系统维护前统一释放编辑锁等管理场景。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCheckoutUndoByAdmin
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchCheckoutUndoByAdminRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchCheckoutUndoByAdminResponse`
        """
        http_info = self._batch_checkout_undo_by_admin_http_info(request)
        return self._call_api(**http_info)

    def batch_checkout_undo_by_admin_invoker(self, request):
        http_info = self._batch_checkout_undo_by_admin_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_checkout_undo_by_admin_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchUndoCheckoutByAdmin",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCheckoutUndoByAdminResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def batch_create_share_docs(self, request):
        r"""批量创建分享结构化文档

        本接口用于批量创建结构化文档的分享记录，实现文档的跨用户或跨团队协作共享。当需要将产品设计说明书、工艺卡片、BOM清单等结构化文档共享给团队成员、上下游合作伙伴或全体用户时，可调用本接口一次性完成批量分享配置。
        - 调用本接口时，需在params数组中传入多个分享记录，每个元素对应一条文档分享配置。
        - 分享时可指定被分享用户的权限级别：
          - 当auth_type为read时，被分享用户仅可查看文档内容。
          - 当auth_type为write时，被分享用户可查看和编辑文档内容。
        - 当shared_user_id和shared_user_name均设置为all时，表示将文档分享给所有用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateShareDocs
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchCreateShareDocsRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchCreateShareDocsResponse`
        """
        http_info = self._batch_create_share_docs_http_info(request)
        return self._call_api(**http_info)

    def batch_create_share_docs_invoker(self, request):
        http_info = self._batch_create_share_docs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_share_docs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/structured-doc/share-doc/batch",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateShareDocsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def batch_create_using_post(self, request):
        r"""批量创建实例

        本接口用于在指定的数据模型（数据实体或关系实体）下，批量创建多个数据实例。调用成功后，将返回所有成功创建的实例信息列表。
        在调用本接口前，请确保目标数据模型已满足实例化条件：
        1. 已在应用设计态完成数据模型（数据实体或关系实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchCreateUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchCreateUsingPostResponse`
        """
        http_info = self._batch_create_using_post_http_info(request)
        return self._call_api(**http_info)

    def batch_create_using_post_invoker(self, request):
        http_info = self._batch_create_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchCreate",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def batch_create_view(self, request):
        r"""批量创建多维视图

        本接口用于批量为指定的一个或多个M-V模型数据实例创建新的多维视图。多维视图允许用户从不同的预设维度（如设计视图、工艺视图、采购视图等）来观察和管理同一个数据对象。在同一个数据实例下，视图的标识（item）必须是唯一的。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态创建并发布一个具有“多维视图&amp;多维分支”功能的数据模型。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateView
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchCreateViewRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchCreateViewResponse`
        """
        http_info = self._batch_create_view_http_info(request)
        return self._call_api(**http_info)

    def batch_create_view_invoker(self, request):
        http_info = self._batch_create_view_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_view_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchCreateView",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateViewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def batch_delete_branch(self, request):
        r"""批量删除最新大版本下的所有小版本

        本接口用于根据主对象ID（masterIds）列表，批量删除指定M-V模型实例中最新分支（Branch）下的所有迭代版本（Iteration）。
        此操作为物理删除，执行后数据将无法恢复，请谨慎使用。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteBranch
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchDeleteBranchRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchDeleteBranchResponse`
        """
        http_info = self._batch_delete_branch_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_branch_invoker(self, request):
        http_info = self._batch_delete_branch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_branch_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchDeleteBranch",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteBranchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def batch_delete_latest_version(self, request):
        r"""批量删除版本对象下最新分支的最新版本实例数据

        本接口用于根据多个主对象（Master）ID，批量永久删除指定M-V模型实体下最新分支的最新版本数据实例。此操作为物理删除，执行后数据将无法恢复，请谨慎使用。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteLatestVersion
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchDeleteLatestVersionRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchDeleteLatestVersionResponse`
        """
        http_info = self._batch_delete_latest_version_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_latest_version_invoker(self, request):
        http_info = self._batch_delete_latest_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_latest_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batch-delete-latest-version",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteLatestVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def batch_delete_logical_branch(self, request):
        r"""批量软删除最新大版本下的所有小版本

        本接口用于根据主对象ID（masterIds）列表，批量软删除指定M-V模型实例中最新分支（Branch）下的所有迭代版本（Iteration）。
        软删除操作并非物理删除，而是将目标分支下的所有版本实例标记为已删除状态（rdmDeleteFlag置为1），并将数据转存至XDM应用的XDMLogicDeleteData内置模型中，以便在需要时进行数据恢复或归档查询。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteLogicalBranch
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchDeleteLogicalBranchRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchDeleteLogicalBranchResponse`
        """
        http_info = self._batch_delete_logical_branch_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_logical_branch_invoker(self, request):
        http_info = self._batch_delete_logical_branch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_logical_branch_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchLogicalDeleteBranch",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteLogicalBranchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def batch_delete_logical_latest_version(self, request):
        r"""批量软删除版本对象下最新分支的最新版本实例数据

        本接口用于根据主对象ID（masterIds）列表，批量软删除指定M-V模型实体下最新分支的最新版本数据实例。
        软删除操作并非物理删除，而是将目标实例标记为已删除状态（rdmDeleteFlag置为1），并将数据转存至XDM应用的XDMLogicDeleteData内置模型中，以便在需要时进行数据恢复或归档查询。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteLogicalLatestVersion
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchDeleteLogicalLatestVersionRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchDeleteLogicalLatestVersionResponse`
        """
        http_info = self._batch_delete_logical_latest_version_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_logical_latest_version_invoker(self, request):
        http_info = self._batch_delete_logical_latest_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_logical_latest_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batch-logical-delete-latest-version",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteLogicalLatestVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def batch_delete_logical_using_post(self, request):
        r"""批量软删除实例

        本接口用于根据数据实例的唯一编码（id）列表，批量对指定数据模型下的多个数据实例执行软删除（逻辑删除）操作。
        软删除操作不会从数据库中物理移除数据，而是将所有实例标记为已删除状态，并转存至XDM应用的XDMLogicDeleteData内置模型中。如需彻底删除数据，请使用[批量删除实例 - BatchDeleteUsingPost](BatchDeleteUsingPost.xml)接口。
        在调用本接口前，请确保目标数据模型已满足实例化条件：
        1. 已在应用设计态完成数据模型（数据实体或关系实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteLogicalUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchDeleteLogicalUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchDeleteLogicalUsingPostResponse`
        """
        http_info = self._batch_delete_logical_using_post_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_logical_using_post_invoker(self, request):
        http_info = self._batch_delete_logical_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_logical_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchLogicalDelete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteLogicalUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def batch_delete_share_docs(self, request):
        r"""批量删除结构化文档分享权限

        本接口用于批量删除结构化文档的分享权限记录，撤销已共享文档的访问权限。当项目结束、人员岗位变动或文档权限需要回收时，可调用本接口一次性撤销多个用户的文档分享权限。
        - 调用本接口时，需在ids中传入待删除的分享权限记录ID列表，系统将对列表中的分享记录执行批量删除。
        - 分享权限删除后，被分享用户将无法再通过原分享渠道访问该文档。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteShareDocs
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchDeleteShareDocsRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchDeleteShareDocsResponse`
        """
        http_info = self._batch_delete_share_docs_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_share_docs_invoker(self, request):
        http_info = self._batch_delete_share_docs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_share_docs_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/structured-doc/share-doc/batch",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteShareDocsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def batch_delete_structured_document(self, request):
        r"""批量删除结构化文档

        本接口用于批量删除指定数据模型下的结构化文档。当产品下线、项目归档或文档批量清理时，可调用本接口一次性删除多个结构化文档，提升数据管理效率。
        - 调用本接口时，需在ids中传入待删除文档的ID列表，系统将对列表中的文档执行批量删除操作。
        - 当is_check设置为true时，系统将在删除前检查当前用户是否具备文档删除权限，无权限的文档将被跳过删除。
        - 当is_check设置为false时，系统将直接执行删除，不做权限检查。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteStructuredDocument
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchDeleteStructuredDocumentRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchDeleteStructuredDocumentResponse`
        """
        http_info = self._batch_delete_structured_document_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_structured_document_invoker(self, request):
        http_info = self._batch_delete_structured_document_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_structured_document_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/structured-doc/documents/batch",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteStructuredDocumentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def batch_delete_using_post(self, request):
        r"""批量删除实例

        本接口用于根据数据实例的唯一编码（id）列表，批量删除指定数据模型中的多个数据实例。
        删除操作不可逆，实例删除后将无法恢复。请在调用前务必确认目标实例ID列表，谨慎操作。
        在调用本接口前，请确保目标数据模型已满足实例化条件：
        1. 已在应用设计态完成数据模型（数据实体或关系实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchDeleteUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchDeleteUsingPostResponse`
        """
        http_info = self._batch_delete_using_post_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_using_post_invoker(self, request):
        http_info = self._batch_delete_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchDelete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def batch_execute_revise(self, request):
        r"""批量修订M-V模型数据实例

        本接口用于批量修订一个或多个指定的M-V模型数据实例。修订操作会基于当前实例创建一个新的修订版本，并自动将新实例的version字段更新为下一个修订版本号（例如从A升级到B）。修订后的新实例默认处于“已检入”状态。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchExecuteRevise
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchExecuteReviseRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchExecuteReviseResponse`
        """
        http_info = self._batch_execute_revise_http_info(request)
        return self._call_api(**http_info)

    def batch_execute_revise_invoker(self, request):
        http_info = self._batch_execute_revise_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_execute_revise_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchRevise",
            "request_type": request.__class__.__name__,
            "response_type": "BatchExecuteReviseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def batch_remove_child_node(self, request):
        r"""批量移除实例的子节点

        本接口用于批量移除指定数据实例的子节点，解除父子节点间的层级关联关系。当BOM（物料清单）结构发生变更需要拆解某个装配节点、组织架构调整需要撤销某个部门的下属团队归属，或产品分类体系重组需要移除下级类目时，可调用本接口批量解除子节点关联。
        - 调用本接口时，需在parentId中指定父节点实例ID，在childList中传入待移除的子节点实例ID列表。
        - 移除操作执行后，被移除的子节点将发生以下变更：
          - 父节点（parent）字段被置为空。
          - 根节点（root）字段被置为空。
        - 当父节点的所有子节点均被移除后，该父节点将被置为叶子节点（即不再拥有子节点）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchRemoveChildNode
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchRemoveChildNodeRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchRemoveChildNodeResponse`
        """
        http_info = self._batch_remove_child_node_http_info(request)
        return self._call_api(**http_info)

    def batch_remove_child_node_invoker(self, request):
        http_info = self._batch_remove_child_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_remove_child_node_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchRemoveChildNode",
            "request_type": request.__class__.__name__,
            "response_type": "BatchRemoveChildNodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def batch_show_get_using_post(self, request):
        r"""批量查询实例

        本接口用于根据数据实例的系统唯一标识（id）列表，批量查询指定数据模型下多个实例的完整详细信息。
        在调用本接口前，请确保目标数据模型已满足实例化条件：
        1. 已在应用设计态完成数据模型（数据实体或关系实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchShowGetUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchShowGetUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchShowGetUsingPostResponse`
        """
        http_info = self._batch_show_get_using_post_http_info(request)
        return self._call_api(**http_info)

    def batch_show_get_using_post_invoker(self, request):
        http_info = self._batch_show_get_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_show_get_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchGet",
            "request_type": request.__class__.__name__,
            "response_type": "BatchShowGetUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def batch_update_and_checkin(self, request):
        r"""批量更新并检入M-V模型数据实例

        本接口用于批量更新一个或多个指定的M-V模型数据实例，并在更新成功后自动执行检入（Check-in）操作，将实例从“检出”状态切换为“已检入”状态。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateAndCheckin
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchUpdateAndCheckinRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchUpdateAndCheckinResponse`
        """
        http_info = self._batch_update_and_checkin_http_info(request)
        return self._call_api(**http_info)

    def batch_update_and_checkin_invoker(self, request):
        http_info = self._batch_update_and_checkin_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_update_and_checkin_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchUpdateAndCheckin",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateAndCheckinResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def batch_update_and_revise(self, request):
        r"""批量修订并更新M-V模型数据实例

        根据主对象ID批量修订并更新M-V模型数据实例，即修订后实例的“version.修订版本”更新为新的修订版本，并同时更新该实例的信息。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateAndRevise
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchUpdateAndReviseRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchUpdateAndReviseResponse`
        """
        http_info = self._batch_update_and_revise_http_info(request)
        return self._call_api(**http_info)

    def batch_update_and_revise_invoker(self, request):
        http_info = self._batch_update_and_revise_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_update_and_revise_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchReviseAndUpdate",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateAndReviseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def batch_update_by_admin(self, request):
        r"""管理员批量更新M-V模型数据实例

        本接口用于管理员批量强制更新Master-Branch-Version（M-V）模型数据实例，适用于数据治理中的大规模紧急数据修正、批量版本回滚、全量属性修正等管理场景。对于批量中的每个实例，若其唯一编码不存在，则该实例不做任何更新操作，不影响其他实例的正常更新。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateByAdmin
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchUpdateByAdminRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchUpdateByAdminResponse`
        """
        http_info = self._batch_update_by_admin_http_info(request)
        return self._call_api(**http_info)

    def batch_update_by_admin_invoker(self, request):
        http_info = self._batch_update_by_admin_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_update_by_admin_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchUpdateByAdmin",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateByAdminResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def batch_update_document(self, request):
        r"""批量更新结构化文档

        本接口用于批量更新结构化文档的属性信息。
        - 调用本接口时，需在params数组中传入多个文档的更新信息，每个元素对应一个待更新的文档。
        - 每个文档更新项中，id为必填参数，用于唯一标识目标文档；其余字段为可选，仅更新传入的字段。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateDocument
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchUpdateDocumentRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchUpdateDocumentResponse`
        """
        http_info = self._batch_update_document_http_info(request)
        return self._call_api(**http_info)

    def batch_update_document_invoker(self, request):
        http_info = self._batch_update_document_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_update_document_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/structured-doc/documents/batch/update",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateDocumentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def batch_update_using_post(self, request):
        r"""批量更新实例

        本接口用于批量更新指定数据模型中的多个实例数据。如果请求列表中某个实例的唯一编码（id）在系统中不存在，系统将跳过该实例，不执行任何更新操作，且不会因此导致整个批量请求失败。
        在调用本接口前，请确保目标数据模型已满足实例化条件：
        1. 已在应用设计态完成数据模型（数据实体或关系实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchUpdateUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchUpdateUsingPostResponse`
        """
        http_info = self._batch_update_using_post_http_info(request)
        return self._call_api(**http_info)

    def batch_update_using_post_invoker(self, request):
        http_info = self._batch_update_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_update_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchUpdate",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def batch_update_version(self, request):
        r"""批量升级M-V模型实例的版本号

        本接口用于根据数据实例的唯一标识（id），批量更新/升级指定Master-Branch-Version（M-V）模型实例的版本号信息（包括修订版本version和迭代版本iteration）。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateVersion
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.BatchUpdateVersionRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.BatchUpdateVersionResponse`
        """
        http_info = self._batch_update_version_http_info(request)
        return self._call_api(**http_info)

    def batch_update_version_invoker(self, request):
        http_info = self._batch_update_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_update_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchUpdateVersion",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def checkin(self, request):
        r"""检入M-V模型数据实例

        根据主对象ID检入M-V模型数据实例。已检入的数据实例会生成一个新的迭代版本，并将数据存储至系统中。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for Checkin
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.CheckinRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.CheckinResponse`
        """
        http_info = self._checkin_http_info(request)
        return self._call_api(**http_info)

    def checkin_invoker(self, request):
        http_info = self._checkin_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _checkin_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/checkin",
            "request_type": request.__class__.__name__,
            "response_type": "CheckinResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def checkout(self, request):
        r"""检出M-V模型数据实例

        本接口用于根据主对象ID（masterId），对指定的M-V模型数据实例执行检出（Check-out）操作。
        调用本接口后，系统会基于原实例（已检入版本）完全复制生成一个新的数据实例（工作副本），将其状态修改为“工作中”，并对该主对象加锁，阻止其他用户再次检出，直到当前用户执行“检入”或“撤销检出”。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for Checkout
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.CheckoutRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.CheckoutResponse`
        """
        http_info = self._checkout_http_info(request)
        return self._call_api(**http_info)

    def checkout_invoker(self, request):
        http_info = self._checkout_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _checkout_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/checkout",
            "request_type": request.__class__.__name__,
            "response_type": "CheckoutResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def checkout_and_update(self, request):
        r"""检出并更新M-V模型

        本接口用于根据主对象ID（masterId），对指定的Master-Branch-Version（M-V）模型实例执行检出（Check-out）并同步更新（Update）的原子操作。
        本接口将“检出”与“更新”合并为一次网络请求，系统在生成新工作副本并加锁的同时，直接将请求中指定的属性值应用到该工作副本上。这大幅减少了网络交互次数，避免了“先检出空副本，再发请求更新”带来的数据不一致风险与性能开销。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckoutAndUpdate
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.CheckoutAndUpdateRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.CheckoutAndUpdateResponse`
        """
        http_info = self._checkout_and_update_http_info(request)
        return self._call_api(**http_info)

    def checkout_and_update_invoker(self, request):
        http_info = self._checkout_and_update_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _checkout_and_update_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/checkoutAndUpdate",
            "request_type": request.__class__.__name__,
            "response_type": "CheckoutAndUpdateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def checkout_undo(self, request):
        r"""撤销检出M-V模型数据实例

        本接口用于撤销指定M-V模型实例的检出状态。
        执行撤销检出后，系统会彻底丢弃当前工作副本中的所有未提交修改，将实例数据还原至最近一次检入（Check-in）的历史版本状态，并释放该对象的并发锁，以便自己或他人重新检出。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckoutUndo
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.CheckoutUndoRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.CheckoutUndoResponse`
        """
        http_info = self._checkout_undo_http_info(request)
        return self._call_api(**http_info)

    def checkout_undo_invoker(self, request):
        http_info = self._checkout_undo_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _checkout_undo_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/undoCheckout",
            "request_type": request.__class__.__name__,
            "response_type": "CheckoutUndoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def checkout_undo_by_admin(self, request):
        r"""管理员撤销检出M-V模型数据实例

        本接口用于管理员强制撤销Master-Branch-Version（M-V）模型实例的检出状态，将实例数据还原至检出前的最后检入版本内容。适用于数据治理中因用户离职、会话超时、误操作等导致的实例长期锁定场景。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckoutUndoByAdmin
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.CheckoutUndoByAdminRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.CheckoutUndoByAdminResponse`
        """
        http_info = self._checkout_undo_by_admin_http_info(request)
        return self._call_api(**http_info)

    def checkout_undo_by_admin_invoker(self, request):
        http_info = self._checkout_undo_by_admin_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _checkout_undo_by_admin_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/undoCheckoutByAdmin",
            "request_type": request.__class__.__name__,
            "response_type": "CheckoutUndoByAdminResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def collect_history_data(self, request):
        r"""根据时间范围获取模型的历史记录数

        本接口用于根据指定的时间范围，获取数据模型的历史操作统计记录数，包括创建实例、更新实例、删除实例及软删除实例的数量。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态创建并发布一个具有“系统版本”功能的数据模型。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CollectHistoryData
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.CollectHistoryDataRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.CollectHistoryDataResponse`
        """
        http_info = self._collect_history_data_http_info(request)
        return self._call_api(**http_info)

    def collect_history_data_invoker(self, request):
        http_info = self._collect_history_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _collect_history_data_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/statisticsHistoryData",
            "request_type": request.__class__.__name__,
            "response_type": "CollectHistoryDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def compare_business_version(self, request):
        r"""对比M-V模型实例

        本接口用于根据主对象ID（id），获取指定Master-Branch-Version（M-V）模型下两个不同版本实例的完整数据快照，以便进行属性与关系的差异对比。
        **建议：**
        本接口为基础对比功能。为获得更优的对比体验和更细粒度的控制（如仅对比属性或仅对比关系），推荐使用数据建模引擎（xDM Foundation，简称xDM-F）新增的差异对比接口，即instance-attrs-comparison（属性对比）和instance-relation-comparison（关系对比）接口。更多内容可在应用运行态的“数据服务管理 &gt; 全量数据服务 &gt; 系统管理API &gt; 属性对比API”中查看。
        
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CompareBusinessVersion
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.CompareBusinessVersionRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.CompareBusinessVersionResponse`
        """
        http_info = self._compare_business_version_http_info(request)
        return self._call_api(**http_info)

    def compare_business_version_invoker(self, request):
        http_info = self._compare_business_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _compare_business_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/compareBusinessVersion",
            "request_type": request.__class__.__name__,
            "response_type": "CompareBusinessVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def compare_version(self, request):
        r"""数据实例指定版本对比

        本接口用于对比指定数据实例两个版本之间的属性差异和关系差异，返回基础版本对象及差异对比结果。
        建议使用数据建模引擎（xDM Foundation，简称xDM-F）新增的差异对比功能，即使用instance-attrs-comparison（属性对比）和instance-relation-comparison（关系对比）接口。更多内容可在应用运行态的“数据服务管理 &gt; 全量数据服务 &gt; 系统管理API &gt; 属性对比API”中查看。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态创建并发布一个具有“系统版本”功能的数据模型。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CompareVersion
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.CompareVersionRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.CompareVersionResponse`
        """
        http_info = self._compare_version_http_info(request)
        return self._call_api(**http_info)

    def compare_version_invoker(self, request):
        http_info = self._compare_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _compare_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/compareVersion",
            "request_type": request.__class__.__name__,
            "response_type": "CompareVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def count_using_post(self, request):
        r"""统计指定数据模型的实例总数

        本接口用于根据指定的查询条件，统计指定数据模型中满足条件的实例总数。
        在调用本接口前，请确保目标数据模型已满足实例化条件：
        1. 已在应用设计态完成数据模型（数据实体或关系实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.CountUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.CountUsingPostResponse`
        """
        http_info = self._count_using_post_http_info(request)
        return self._call_api(**http_info)

    def count_using_post_invoker(self, request):
        http_info = self._count_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _count_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/count",
            "request_type": request.__class__.__name__,
            "response_type": "CountUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def create_document(self, request):
        r"""创建结构化文档

        本接口用于在指定数据模型下创建结构化文档。结构化文档是工业数据管理中用于承载设计说明书、工艺卡片、BOM清单等工业文档的载体，支持目录（directory）、Page文档（pageDocument）、Board文档（boardDocument）、Mind文档（mindDocument）、Draw文档（drawDocument）等多种文档类型。
        - 创建结构化文档时，需指定文档标题和文档类型。
        - 如需将文档关联到具体的数据模型实例，可通过instance_id参数指定实例ID。
        - 如需将文档挂载到指定目录下，可通过parent_document_id参数指定父文档ID。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDocument
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.CreateDocumentRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.CreateDocumentResponse`
        """
        http_info = self._create_document_http_info(request)
        return self._call_api(**http_info)

    def create_document_invoker(self, request):
        http_info = self._create_document_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_document_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/structured-doc/documents",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDocumentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def create_multi_view(self, request):
        r"""创建M-V模型视图数据实例

        本接口用于勾选了“多维视图&amp;多维分支”的MV模型创建数据实例。创建实例时给视图属性赋不同视图属性表示实例所属的视图。视图属性为NULL表示的是默认视图，若创建、更新、修订等MV模型特有接口不指定视图参数则表示操作的视图属性为NULL的视图。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateMultiView
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.CreateMultiViewRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.CreateMultiViewResponse`
        """
        http_info = self._create_multi_view_http_info(request)
        return self._call_api(**http_info)

    def create_multi_view_invoker(self, request):
        http_info = self._create_multi_view_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_multi_view_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{mvModelName}/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMultiViewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'mv_model_name' in local_var_params:
            path_params['mvModelName'] = local_var_params['mv_model_name']
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']

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

    def create_using_post(self, request):
        r"""创建实例

        本接口用于在指定的数据模型（数据实体或关系实体）下创建数据实例。调用成功后，将返回新创建实例的详细信息。
        在调用本接口前，请确保目标数据模型已满足实例化条件：
        1. 已在应用设计态完成数据模型（数据实体或关系实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.CreateUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.CreateUsingPostResponse`
        """
        http_info = self._create_using_post_http_info(request)
        return self._call_api(**http_info)

    def create_using_post_invoker(self, request):
        http_info = self._create_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def create_view(self, request):
        r"""创建多维视图

        本接口用于为指定的M-V模型数据实例创建一个新的多维视图。多维视图允许用户从不同的预设维度（如设计视图、工艺视图、采购视图等）来观察和管理同一个数据对象，每个视图下的属性或关系可以独立配置和演进。在同一个数据实例下，视图的标识（item）必须是唯一的。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态创建并发布一个具有“多维视图&amp;多维分支”功能的数据模型。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateView
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.CreateViewRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.CreateViewResponse`
        """
        http_info = self._create_view_http_info(request)
        return self._call_api(**http_info)

    def create_view_invoker(self, request):
        http_info = self._create_view_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_view_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/createView",
            "request_type": request.__class__.__name__,
            "response_type": "CreateViewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def delete_branch(self, request):
        r"""删除最新大版本下的所有小版本

        本接口用于根据主对象ID（masterId）和修订版本号（version），删除指定M-V模型实例中最新分支（Branch）下的所有迭代版本（Iteration）。
        其中：
        - 分支（Branch）：对应M-V模型中的大版本（如版本A、版本B），代表一次完整的修订基线。
        - 迭代（Iteration）：对应分支内的小版本（如A.1、A.2），代表同一修订基线下的多次迭代更新。
        - 本接口将级联删除指定分支下的所有迭代版本，包括该分支的最终版本及其历史迭代记录。
        
        此操作为物理删除，执行后数据将无法恢复，请谨慎使用。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBranch
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteBranchRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteBranchResponse`
        """
        http_info = self._delete_branch_http_info(request)
        return self._call_api(**http_info)

    def delete_branch_invoker(self, request):
        http_info = self._delete_branch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_branch_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/deleteBranch",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBranchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def delete_by_condition_multi_view(self, request):
        r"""条件删除M-V模型数据实例

        根据用户指定条件删除MV模型数据实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteByConditionMultiView
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteByConditionMultiViewRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteByConditionMultiViewResponse`
        """
        http_info = self._delete_by_condition_multi_view_http_info(request)
        return self._call_api(**http_info)

    def delete_by_condition_multi_view_invoker(self, request):
        http_info = self._delete_by_condition_multi_view_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_by_condition_multi_view_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{mvModelName}/deleteByCondition",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteByConditionMultiViewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'mv_model_name' in local_var_params:
            path_params['mvModelName'] = local_var_params['mv_model_name']
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']

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

    def delete_by_condition_using_post(self, request):
        r"""根据指定条件删除实例

        本接口用于根据指定的过滤条件，批量删除指定数据模型下满足条件的所有数据实例。
        删除操作不可逆，实例删除后将无法恢复。请在调用前务必先使用[分页查询实例 - ShowFindUsingPost](ShowFindUsingPost.xml)接口验证条件表达式的准确性。
        在调用本接口前，请确保目标数据模型已满足实例化条件：
        1. 已在应用设计态完成数据模型（数据实体或关系实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteByConditionUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteByConditionUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteByConditionUsingPostResponse`
        """
        http_info = self._delete_by_condition_using_post_http_info(request)
        return self._call_api(**http_info)

    def delete_by_condition_using_post_invoker(self, request):
        http_info = self._delete_by_condition_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_by_condition_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/deleteByCondition",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteByConditionUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def delete_latest_version(self, request):
        r"""删除版本对象下最新分支的最新版本实例数据

        本接口用于根据主对象ID（masterId），精准删除指定Master-Branch-Version（M-V）模型在特定分支下的最新（末端）版本实例。
        此操作为物理删除，执行后数据将无法恢复，请谨慎使用。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteLatestVersion
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteLatestVersionRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteLatestVersionResponse`
        """
        http_info = self._delete_latest_version_http_info(request)
        return self._call_api(**http_info)

    def delete_latest_version_invoker(self, request):
        http_info = self._delete_latest_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_latest_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/deleteLatestVersion",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLatestVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def delete_logical_branch(self, request):
        r"""软删除M-V模型实例下最新分支的所有小版本数据

        本接口用于根据主对象ID（masterId）和修订版本号（version），软删除指定M-V模型实例中最新分支（Branch）下的所有迭代版本（Iteration）。
        软删除操作并非物理删除，而是将目标分支下的所有版本实例标记为已删除状态（rdmDeleteFlag置为1），并将数据转存至XDM应用的XDMLogicDeleteData内置模型中，以便在需要时进行数据恢复或归档查询。
        
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteLogicalBranch
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteLogicalBranchRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteLogicalBranchResponse`
        """
        http_info = self._delete_logical_branch_http_info(request)
        return self._call_api(**http_info)

    def delete_logical_branch_invoker(self, request):
        http_info = self._delete_logical_branch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_logical_branch_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/logicalDeleteBranch",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLogicalBranchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def delete_logical_latest_version(self, request):
        r"""软删除版本对象下最新分支的最新版本实例数据

        本接口用于根据主对象ID，软删除指定M-V模型实体下最新分支的最新版本数据实例。
        软删除操作并非从数据库中物理移除数据，而是将目标实例标记为已删除状态（rdmDeleteFlag置为1），并将该实例的数据转存至XDM应用的XDMLogicDeleteData内置模型中，以便在需要时进行数据恢复或归档查询。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteLogicalLatestVersion
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteLogicalLatestVersionRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteLogicalLatestVersionResponse`
        """
        http_info = self._delete_logical_latest_version_http_info(request)
        return self._call_api(**http_info)

    def delete_logical_latest_version_invoker(self, request):
        http_info = self._delete_logical_latest_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_logical_latest_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/logicalDeleteLatestVersion",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLogicalLatestVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def delete_multi_view(self, request):
        r"""删除M-V模型指定视图版本

        本接口用于勾选了“多维视图&amp;多维分支”的MV模型删除指定的数据实例。若模型配置视图属性，且调用createView接口创建了多维视图。需要在接口参数中给视图属性指定要删除的视图。若入参中书体属性为null，会删除视图属性为null的视图。本接口为同步接口，调用完成后立即返回结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteMultiView
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteMultiViewRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteMultiViewResponse`
        """
        http_info = self._delete_multi_view_http_info(request)
        return self._call_api(**http_info)

    def delete_multi_view_invoker(self, request):
        http_info = self._delete_multi_view_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_multi_view_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{mvModelName}/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMultiViewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'mv_model_name' in local_var_params:
            path_params['mvModelName'] = local_var_params['mv_model_name']
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']

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

    def delete_target(self, request):
        r"""通过目标模型删除关系实体的数据实例

        本接口用于通过目标模型删除关系实体的数据实例，即解除源模型实例与目标模型实例之间的关联关系。
        - 调用本接口时，需在sourceId中指定源模型实例ID，在targetType中指定目标模型的英文名称，系统将删除该源实例与指定目标模型之间的所有关联关系实例。
        - 当latestOnly设置为true时，仅删除源实例关联的最新版本目标模型实例的关系（仅对M-V模型实体生效）。
        - 当latestOnly设置为false时，删除源实例关联的所有版本目标模型实例的关系。
        - 本接口仅执行关系表的DELETE操作，目标端实体的业务数据不受任何影响。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTarget
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteTargetRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteTargetResponse`
        """
        http_info = self._delete_target_http_info(request)
        return self._call_api(**http_info)

    def delete_target_invoker(self, request):
        http_info = self._delete_target_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_target_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/deleteTarget",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTargetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def delete_using_post(self, request):
        r"""删除实例

        本接口用于根据数据实例的唯一编码（id），删除指定数据模型中的一个数据实例。
        删除操作不可逆，实例删除后将无法恢复。请在调用前务必确认目标实例，谨慎操作。
        在调用本接口前，请确保目标数据模型已满足实例化条件：
        1. 已在应用设计态完成数据模型（数据实体或关系实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.DeleteUsingPostResponse`
        """
        http_info = self._delete_using_post_http_info(request)
        return self._call_api(**http_info)

    def delete_using_post_invoker(self, request):
        http_info = self._delete_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def disable_data_instance(self, request):
        r"""失效模型数据实例

        本接口用于批量将指定数据模型的数据实例标记为失效状态，并同步返回实际失效成功的实例数量。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisableDataInstance
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.DisableDataInstanceRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.DisableDataInstanceResponse`
        """
        http_info = self._disable_data_instance_http_info(request)
        return self._call_api(**http_info)

    def disable_data_instance_invoker(self, request):
        http_info = self._disable_data_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disable_data_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/disable",
            "request_type": request.__class__.__name__,
            "response_type": "DisableDataInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def enable_data_instance(self, request):
        r"""生效模型数据实例

        本接口用于批量将指定数据模型中处于失效状态的数据实例重新标记为生效状态，并同步返回实际生效成功的实例数量。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableDataInstance
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.EnableDataInstanceRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.EnableDataInstanceResponse`
        """
        http_info = self._enable_data_instance_http_info(request)
        return self._call_api(**http_info)

    def enable_data_instance_invoker(self, request):
        http_info = self._enable_data_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_data_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/enable",
            "request_type": request.__class__.__name__,
            "response_type": "EnableDataInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def execute_revise(self, request):
        r"""修订M-V模型数据实例

        本接口用于对指定的Master-Branch-Version（M-V）模型实例执行修订（Revise）操作。
        调用本接口后，系统会基于指定的主对象（Master）及其当前最新修订版本，复制并生成一个新的修订版本实例。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteRevise
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ExecuteReviseRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ExecuteReviseResponse`
        """
        http_info = self._execute_revise_http_info(request)
        return self._call_api(**http_info)

    def execute_revise_invoker(self, request):
        http_info = self._execute_revise_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_revise_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/revise",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteReviseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def generate_business_code(self, request):
        r"""生成新模型业务编码

        本接口用于根据指定数据模型在应用设计态预配置的“业务编码生成器”规则，自动生成符合企业命名规范的业务流水码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GenerateBusinessCode
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.GenerateBusinessCodeRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.GenerateBusinessCodeResponse`
        """
        http_info = self._generate_business_code_http_info(request)
        return self._call_api(**http_info)

    def generate_business_code_invoker(self, request):
        http_info = self._generate_business_code_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _generate_business_code_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/generateBusinessCode",
            "request_type": request.__class__.__name__,
            "response_type": "GenerateBusinessCodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def list_all_versions(self, request):
        r"""获取指定M-V模型实例的版本列表

        本接口用于根据主对象ID（masterId），分页获取指定Master-Branch-Version（M-V）模型实例的所有版本信息（包含对应版本下的属性信息）。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAllVersions
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ListAllVersionsRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ListAllVersionsResponse`
        """
        http_info = self._list_all_versions_http_info(request)
        return self._call_api(**http_info)

    def list_all_versions_invoker(self, request):
        http_info = self._list_all_versions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_all_versions_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/getAllVersions/{pageSizePath}/{curPagePath}",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllVersionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'page_size_path' in local_var_params:
            path_params['pageSizePath'] = local_var_params['page_size_path']
        if 'cur_page_path' in local_var_params:
            path_params['curPagePath'] = local_var_params['cur_page_path']
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

        query_params = []
        if 'cur_page' in local_var_params:
            query_params.append(('curPage', local_var_params['cur_page']))
        if 'end_index' in local_var_params:
            query_params.append(('endIndex', local_var_params['end_index']))
        if 'max_page_size' in local_var_params:
            query_params.append(('maxPageSize', local_var_params['max_page_size']))
        if 'page_size' in local_var_params:
            query_params.append(('pageSize', local_var_params['page_size']))
        if 'start_index' in local_var_params:
            query_params.append(('startIndex', local_var_params['start_index']))
        if 'total_pages' in local_var_params:
            query_params.append(('totalPages', local_var_params['total_pages']))
        if 'total_rows' in local_var_params:
            query_params.append(('totalRows', local_var_params['total_rows']))

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

    def list_batch_query_related_objects(self, request):
        r"""批量查询关系实体关联模型的信息

        本接口用于批量查询指定关系实体所关联的源模型或目标模型的所有实例信息，返回结果包含实例的具体属性。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBatchQueryRelatedObjects
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ListBatchQueryRelatedObjectsRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ListBatchQueryRelatedObjectsResponse`
        """
        http_info = self._list_batch_query_related_objects_http_info(request)
        return self._call_api(**http_info)

    def list_batch_query_related_objects_invoker(self, request):
        http_info = self._list_batch_query_related_objects_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_batch_query_related_objects_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/batchQueryRelatedObjects/{pageSizePath}/{curPagePath}",
            "request_type": request.__class__.__name__,
            "response_type": "ListBatchQueryRelatedObjectsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'page_size_path' in local_var_params:
            path_params['pageSizePath'] = local_var_params['page_size_path']
        if 'cur_page_path' in local_var_params:
            path_params['curPagePath'] = local_var_params['cur_page_path']
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

        query_params = []
        if 'cur_page' in local_var_params:
            query_params.append(('curPage', local_var_params['cur_page']))
        if 'end_index' in local_var_params:
            query_params.append(('endIndex', local_var_params['end_index']))
        if 'max_page_size' in local_var_params:
            query_params.append(('maxPageSize', local_var_params['max_page_size']))
        if 'page_size' in local_var_params:
            query_params.append(('pageSize', local_var_params['page_size']))
        if 'start_index' in local_var_params:
            query_params.append(('startIndex', local_var_params['start_index']))
        if 'total_pages' in local_var_params:
            query_params.append(('totalPages', local_var_params['total_pages']))
        if 'total_rows' in local_var_params:
            query_params.append(('totalRows', local_var_params['total_rows']))

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

    def list_get_all_parent_list(self, request):
        r"""获取所有父节点

        本接口用于获取指定数据实例的所有父节点列表，同时返回各父节点的列表属性。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGetAllParentList
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ListGetAllParentListRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ListGetAllParentListResponse`
        """
        http_info = self._list_get_all_parent_list_http_info(request)
        return self._call_api(**http_info)

    def list_get_all_parent_list_invoker(self, request):
        http_info = self._list_get_all_parent_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_get_all_parent_list_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/getAllParentList",
            "request_type": request.__class__.__name__,
            "response_type": "ListGetAllParentListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def list_get_child_list(self, request):
        r"""获取子节点

        本接口用于分页获取指定数据实例的直接子节点列表，同时返回各子节点的列表属性。当需要展开BOM（物料清单）的某个装配节点查看下级零部件、浏览组织架构中某个部门的下属团队或查看产品分类的下一级类目时，可调用本接口获取直接子节点信息。
        调用本接口时，需在parentId中传入目标数据实例的ID，系统将返回该实例的直接子节点（仅返回一层，不向下递归）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGetChildList
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ListGetChildListRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ListGetChildListResponse`
        """
        http_info = self._list_get_child_list_http_info(request)
        return self._call_api(**http_info)

    def list_get_child_list_invoker(self, request):
        http_info = self._list_get_child_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_get_child_list_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/getChildList/{pageSizePath}/{curPagePath}",
            "request_type": request.__class__.__name__,
            "response_type": "ListGetChildListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']
        if 'page_size_path' in local_var_params:
            path_params['pageSizePath'] = local_var_params['page_size_path']
        if 'cur_page_path' in local_var_params:
            path_params['curPagePath'] = local_var_params['cur_page_path']

        query_params = []
        if 'cur_page' in local_var_params:
            query_params.append(('curPage', local_var_params['cur_page']))
        if 'end_index' in local_var_params:
            query_params.append(('endIndex', local_var_params['end_index']))
        if 'max_page_size' in local_var_params:
            query_params.append(('maxPageSize', local_var_params['max_page_size']))
        if 'page_size' in local_var_params:
            query_params.append(('pageSize', local_var_params['page_size']))
        if 'start_index' in local_var_params:
            query_params.append(('startIndex', local_var_params['start_index']))
        if 'total_pages' in local_var_params:
            query_params.append(('totalPages', local_var_params['total_pages']))
        if 'total_rows' in local_var_params:
            query_params.append(('totalRows', local_var_params['total_rows']))

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

    def list_history_data(self, request):
        r"""分页查询模型历史版本信息

        本接口用于分页查询指定数据实例的历史版本信息。系统以数据实例的最后修改时间作为查询条件，根据您指定的时间范围返回该实例的历史版本变更记录。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态创建并发布一个具有“系统版本”功能的数据模型。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHistoryData
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ListHistoryDataRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ListHistoryDataResponse`
        """
        http_info = self._list_history_data_http_info(request)
        return self._call_api(**http_info)

    def list_history_data_invoker(self, request):
        http_info = self._list_history_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_history_data_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/queryHistoryData/{pageSizePath}/{curPagePath}",
            "request_type": request.__class__.__name__,
            "response_type": "ListHistoryDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'page_size_path' in local_var_params:
            path_params['pageSizePath'] = local_var_params['page_size_path']
        if 'cur_page_path' in local_var_params:
            path_params['curPagePath'] = local_var_params['cur_page_path']
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

        query_params = []
        if 'cur_page' in local_var_params:
            query_params.append(('curPage', local_var_params['cur_page']))
        if 'end_index' in local_var_params:
            query_params.append(('endIndex', local_var_params['end_index']))
        if 'max_page_size' in local_var_params:
            query_params.append(('maxPageSize', local_var_params['max_page_size']))
        if 'page_size' in local_var_params:
            query_params.append(('pageSize', local_var_params['page_size']))
        if 'start_index' in local_var_params:
            query_params.append(('startIndex', local_var_params['start_index']))
        if 'total_pages' in local_var_params:
            query_params.append(('totalPages', local_var_params['total_pages']))
        if 'total_rows' in local_var_params:
            query_params.append(('totalRows', local_var_params['total_rows']))

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

    def list_query_documents(self, request):
        r"""查询结构化文档

        本接口用于查询指定数据模型下的结构化文档列表。
        - 当请求中传入instance_id时，返回与该实例关联的结构化文档列表。
        - 当请求中传入type时，返回指定类型的结构化文档列表。
        - 当请求中同时传入instance_id和type时，返回同时满足两个条件的结构化文档列表。
        - 当请求中不传入任何筛选条件时，返回该数据模型下所有的结构化文档列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQueryDocuments
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ListQueryDocumentsRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ListQueryDocumentsResponse`
        """
        http_info = self._list_query_documents_http_info(request)
        return self._call_api(**http_info)

    def list_query_documents_invoker(self, request):
        http_info = self._list_query_documents_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_query_documents_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/structured-doc/documents/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListQueryDocumentsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def list_query_related_objects(self, request):
        r"""查询关系实体关联模型的信息

        本接口用于分页查询指定关系实体所关联的源模型或目标模型的所有实例信息，返回结果包含关联实例的具体属性。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQueryRelatedObjects
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ListQueryRelatedObjectsRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ListQueryRelatedObjectsResponse`
        """
        http_info = self._list_query_related_objects_http_info(request)
        return self._call_api(**http_info)

    def list_query_related_objects_invoker(self, request):
        http_info = self._list_query_related_objects_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_query_related_objects_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/queryRelatedObjects/{pageSizePath}/{curPagePath}",
            "request_type": request.__class__.__name__,
            "response_type": "ListQueryRelatedObjectsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'page_size_path' in local_var_params:
            path_params['pageSizePath'] = local_var_params['page_size_path']
        if 'cur_page_path' in local_var_params:
            path_params['curPagePath'] = local_var_params['cur_page_path']
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

        query_params = []
        if 'cur_page' in local_var_params:
            query_params.append(('curPage', local_var_params['cur_page']))
        if 'end_index' in local_var_params:
            query_params.append(('endIndex', local_var_params['end_index']))
        if 'max_page_size' in local_var_params:
            query_params.append(('maxPageSize', local_var_params['max_page_size']))
        if 'page_size' in local_var_params:
            query_params.append(('pageSize', local_var_params['page_size']))
        if 'start_index' in local_var_params:
            query_params.append(('startIndex', local_var_params['start_index']))
        if 'total_pages' in local_var_params:
            query_params.append(('totalPages', local_var_params['total_pages']))
        if 'total_rows' in local_var_params:
            query_params.append(('totalRows', local_var_params['total_rows']))

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

    def list_query_relationship(self, request):
        r"""查询关系实体的数据实例

        本接口用于分页查询关系实体的数据实例。通过指定数据实例ID及对应的关系角色（源/目标），或数据模型的英文名称及对应的关系角色（源类型/目标类型），返回匹配的关系实体数据实例信息。
        如果对应的关系实体存在“参考对象”类型属性，且参考的数据模型为抽象模型，返回信息仅返回对应模型的英文名称和ID。如果参考的数据模型为实体模型，返回空。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQueryRelationship
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ListQueryRelationshipRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ListQueryRelationshipResponse`
        """
        http_info = self._list_query_relationship_http_info(request)
        return self._call_api(**http_info)

    def list_query_relationship_invoker(self, request):
        http_info = self._list_query_relationship_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_query_relationship_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/queryRelationship/{pageSizePath}/{curPagePath}",
            "request_type": request.__class__.__name__,
            "response_type": "ListQueryRelationshipResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']
        if 'page_size_path' in local_var_params:
            path_params['pageSizePath'] = local_var_params['page_size_path']
        if 'cur_page_path' in local_var_params:
            path_params['curPagePath'] = local_var_params['cur_page_path']

        query_params = []
        if 'cur_page' in local_var_params:
            query_params.append(('curPage', local_var_params['cur_page']))
        if 'end_index' in local_var_params:
            query_params.append(('endIndex', local_var_params['end_index']))
        if 'max_page_size' in local_var_params:
            query_params.append(('maxPageSize', local_var_params['max_page_size']))
        if 'page_size' in local_var_params:
            query_params.append(('pageSize', local_var_params['page_size']))
        if 'start_index' in local_var_params:
            query_params.append(('startIndex', local_var_params['start_index']))
        if 'total_pages' in local_var_params:
            query_params.append(('totalPages', local_var_params['total_pages']))
        if 'total_rows' in local_var_params:
            query_params.append(('totalRows', local_var_params['total_rows']))

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

    def list_query_share_docs(self, request):
        r"""查询结构化文档分享授权列表

        本接口用于查询指定结构化文档的分享授权列表，获取该文档的所有分享记录信息。当需要审计文档的共享范围、回收过期权限或排查文档访问异常时，可调用本接口获取完整的分享授权信息。
        - 调用本接口时，需在params中传入目标结构化文档的ID。
        - 返回结果中包含该文档的所有分享记录，每条记录包含被分享用户、分享用户、权限类型等详细信息。
        - 返回结果中的id字段为分享权限记录的唯一标识，可用于[批量删除结构化文档分享权限 - BatchDeleteShareDocs](BatchDeleteShareDocs.xml)接口删除指定分享权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQueryShareDocs
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ListQueryShareDocsRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ListQueryShareDocsResponse`
        """
        http_info = self._list_query_share_docs_http_info(request)
        return self._call_api(**http_info)

    def list_query_share_docs_invoker(self, request):
        http_info = self._list_query_share_docs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_query_share_docs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/structured-doc/share-doc",
            "request_type": request.__class__.__name__,
            "response_type": "ListQueryShareDocsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def list_query_target(self, request):
        r"""通过源模型实例ID查询关联的目标模型实例

        本接口用于通过源模型的数据实例ID，分页查询并返回与该实例关联的目标模型数据实例信息。返回的实例信息包含目标模板的“列表属性”（即模型中标记为列表展示的属性）。
        如果目标模型存在“参考对象”类型的属性，且参考的数据模型为抽象模型，返回信息仅返回对应模型的英文名称和ID。如果参考的数据模型为实体模型，返回空。
        如果目标对象是M-V模型，可通过设置latestOnly&#x3D;true仅返回源实例关联的最新版本目标对象；默认返回所有版本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQueryTarget
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ListQueryTargetRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ListQueryTargetResponse`
        """
        http_info = self._list_query_target_http_info(request)
        return self._call_api(**http_info)

    def list_query_target_invoker(self, request):
        http_info = self._list_query_target_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_query_target_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/queryTarget/{pageSizePath}/{curPagePath}",
            "request_type": request.__class__.__name__,
            "response_type": "ListQueryTargetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'page_size_path' in local_var_params:
            path_params['pageSizePath'] = local_var_params['page_size_path']
        if 'cur_page_path' in local_var_params:
            path_params['curPagePath'] = local_var_params['cur_page_path']
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

        query_params = []
        if 'cur_page' in local_var_params:
            query_params.append(('curPage', local_var_params['cur_page']))
        if 'end_index' in local_var_params:
            query_params.append(('endIndex', local_var_params['end_index']))
        if 'max_page_size' in local_var_params:
            query_params.append(('maxPageSize', local_var_params['max_page_size']))
        if 'page_size' in local_var_params:
            query_params.append(('pageSize', local_var_params['page_size']))
        if 'start_index' in local_var_params:
            query_params.append(('startIndex', local_var_params['start_index']))
        if 'total_pages' in local_var_params:
            query_params.append(('totalPages', local_var_params['total_pages']))
        if 'total_rows' in local_var_params:
            query_params.append(('totalRows', local_var_params['total_rows']))

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

    def list_query_using_post(self, request):
        r"""根据“列表属性”为“是”的属性查询实例

        当数据模型中存在“列表属性”为“是”的属性时，可通过此接口查询数据模型中的实例数据，且支持分页。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 目标数据模型在应用设计态中，必须至少存在一个“列表属性”为“是”的属性。
        2. 已在应用设计态完成数据模型的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        3. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQueryUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ListQueryUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ListQueryUsingPostResponse`
        """
        http_info = self._list_query_using_post_http_info(request)
        return self._call_api(**http_info)

    def list_query_using_post_invoker(self, request):
        http_info = self._list_query_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_query_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/query/{pageSizePath}/{curPagePath}",
            "request_type": request.__class__.__name__,
            "response_type": "ListQueryUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'page_size_path' in local_var_params:
            path_params['pageSizePath'] = local_var_params['page_size_path']
        if 'cur_page_path' in local_var_params:
            path_params['curPagePath'] = local_var_params['cur_page_path']
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

        query_params = []
        if 'cur_page' in local_var_params:
            query_params.append(('curPage', local_var_params['cur_page']))
        if 'end_index' in local_var_params:
            query_params.append(('endIndex', local_var_params['end_index']))
        if 'max_page_size' in local_var_params:
            query_params.append(('maxPageSize', local_var_params['max_page_size']))
        if 'page_size' in local_var_params:
            query_params.append(('pageSize', local_var_params['page_size']))
        if 'start_index' in local_var_params:
            query_params.append(('startIndex', local_var_params['start_index']))
        if 'total_pages' in local_var_params:
            query_params.append(('totalPages', local_var_params['total_pages']))
        if 'total_rows' in local_var_params:
            query_params.append(('totalRows', local_var_params['total_rows']))

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

    def list_select_using_post(self, request):
        r"""查询实例的指定属性

        本接口用于根据查询条件，按需返回数据模型实例的指定属性信息。
        在调用本接口前，请确保目标数据模型已满足实例化条件：
        1. 已在应用设计态完成数据模型（数据实体或关系实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSelectUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ListSelectUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ListSelectUsingPostResponse`
        """
        http_info = self._list_select_using_post_http_info(request)
        return self._call_api(**http_info)

    def list_select_using_post_invoker(self, request):
        http_info = self._list_select_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_select_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/select/{pageSizePath}/{curPagePath}",
            "request_type": request.__class__.__name__,
            "response_type": "ListSelectUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'page_size_path' in local_var_params:
            path_params['pageSizePath'] = local_var_params['page_size_path']
        if 'cur_page_path' in local_var_params:
            path_params['curPagePath'] = local_var_params['cur_page_path']
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

        query_params = []
        if 'cur_page' in local_var_params:
            query_params.append(('curPage', local_var_params['cur_page']))
        if 'end_index' in local_var_params:
            query_params.append(('endIndex', local_var_params['end_index']))
        if 'max_page_size' in local_var_params:
            query_params.append(('maxPageSize', local_var_params['max_page_size']))
        if 'page_size' in local_var_params:
            query_params.append(('pageSize', local_var_params['page_size']))
        if 'start_index' in local_var_params:
            query_params.append(('startIndex', local_var_params['start_index']))
        if 'total_pages' in local_var_params:
            query_params.append(('totalPages', local_var_params['total_pages']))
        if 'total_rows' in local_var_params:
            query_params.append(('totalRows', local_var_params['total_rows']))

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

    def list_using_post(self, request):
        r"""查询实例的基础属性

        本接口用于根据查询条件，分页检索数据模型实例的基础属性与系统级元数据信息。
        在调用本接口前，请确保目标数据模型已满足实例化条件：
        1. 已在应用设计态完成数据模型（数据实体或关系实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ListUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ListUsingPostResponse`
        """
        http_info = self._list_using_post_http_info(request)
        return self._call_api(**http_info)

    def list_using_post_invoker(self, request):
        http_info = self._list_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/list/{pageSizePath}/{curPagePath}",
            "request_type": request.__class__.__name__,
            "response_type": "ListUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'page_size_path' in local_var_params:
            path_params['pageSizePath'] = local_var_params['page_size_path']
        if 'cur_page_path' in local_var_params:
            path_params['curPagePath'] = local_var_params['cur_page_path']
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

        query_params = []
        if 'cur_page' in local_var_params:
            query_params.append(('curPage', local_var_params['cur_page']))
        if 'end_index' in local_var_params:
            query_params.append(('endIndex', local_var_params['end_index']))
        if 'max_page_size' in local_var_params:
            query_params.append(('maxPageSize', local_var_params['max_page_size']))
        if 'page_size' in local_var_params:
            query_params.append(('pageSize', local_var_params['page_size']))
        if 'start_index' in local_var_params:
            query_params.append(('startIndex', local_var_params['start_index']))
        if 'total_pages' in local_var_params:
            query_params.append(('totalPages', local_var_params['total_pages']))
        if 'total_rows' in local_var_params:
            query_params.append(('totalRows', local_var_params['total_rows']))

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

    def refresh(self, request):
        r"""刷新树形节点

        本接口用于刷新指定数据实例对应的节点全路径。在调用本接口前请确保数据模型具有“树形结构”功能。
        调用本接口时，如果未指定数据实例或指定的数据实例为父节点，则刷新整棵树的所有节点全路径。
        本接口为异步接口，调用后立即返回结果，但实际上整棵树的结构还在刷新中，需适时等待后（刷新时间视该树的大小而定）再查看该树的具体数据是否已刷新。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for Refresh
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.RefreshRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.RefreshResponse`
        """
        http_info = self._refresh_http_info(request)
        return self._call_api(**http_info)

    def refresh_invoker(self, request):
        http_info = self._refresh_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _refresh_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/refresh",
            "request_type": request.__class__.__name__,
            "response_type": "RefreshResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def remove_from_category(self, request):
        r"""移除数据分类

        本接口用于数据实例从指定分类中移除。当零部件变更产品线、设备调整工艺归属或物料重新归类时，可调用本接口解除实例与分类的关联关系。
        - 当实例不存在时，系统将抛出异常。
        - 当实例与指定分类不存在关联关系时，返回值为0。
        - 当实例与指定分类存在关联关系时，返回值为成功移除的关联数据分类个数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RemoveFromCategory
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.RemoveFromCategoryRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.RemoveFromCategoryResponse`
        """
        http_info = self._remove_from_category_http_info(request)
        return self._call_api(**http_info)

    def remove_from_category_invoker(self, request):
        http_info = self._remove_from_category_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _remove_from_category_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/removeFromCategory",
            "request_type": request.__class__.__name__,
            "response_type": "RemoveFromCategoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def remove_tag(self, request):
        r"""解绑标签

        本接口用于为指定数据模型的数据实例解绑标签，移除实例与标签之间的关联关系。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态创建并发布一个具有“标签管理”功能的数据模型。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RemoveTag
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.RemoveTagRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.RemoveTagResponse`
        """
        http_info = self._remove_tag_http_info(request)
        return self._call_api(**http_info)

    def remove_tag_invoker(self, request):
        http_info = self._remove_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _remove_tag_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/removeTag",
            "request_type": request.__class__.__name__,
            "response_type": "RemoveTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def save_all_using_post(self, request):
        r"""根据唯一键为“是”的属性更新实例数据

        本接口用于根据数据模型中“唯一键”为“是”的属性（业务唯一键），对数据实例执行全量保存或更新操作。
        更新（Update）：若系统中已存在匹配该唯一键的实例，则更新其所有字段。
        创建（Insert）：若系统中不存在匹配该唯一键的实例，则自动创建一条新实例。
        在调用本接口前，请确保目标数据模型已满足实例化条件：
        1. 已在应用设计态完成数据模型（数据实体或关系实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SaveAllUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.SaveAllUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.SaveAllUsingPostResponse`
        """
        http_info = self._save_all_using_post_http_info(request)
        return self._call_api(**http_info)

    def save_all_using_post_invoker(self, request):
        http_info = self._save_all_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _save_all_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/saveAll",
            "request_type": request.__class__.__name__,
            "response_type": "SaveAllUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def save_as_using_post(self, request):
        r"""另存实例数据

        本接口用于对指定数据模型的数据实例执行另存为（SaveAs）操作。系统将以指定的源实例为模板，克隆其数据并生成一条全新的实例记录。
        在另存过程中，用户可以灵活控制新实例的属性值：
        - 未作特殊指定的属性，将完全保持与源实例一致。
        - 可通过entityToSave为指定属性赋予新的值。
        - 可通过needSetNullAttrs将指定属性强制清空（置为Null）。
        另存操作不会修改或覆盖源实例，而是生成一个具有全新系统主键（id）的新实例。此功能常用于工业场景中的“图纸/模型版本迭代”、“BOM复制建版”或“基于历史数据快速创建新对象”等业务。
        
        在调用本接口前，请确保目标数据模型已满足实例化条件：
        1. 已在应用设计态完成数据模型（数据实体或关系实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SaveAsUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.SaveAsUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.SaveAsUsingPostResponse`
        """
        http_info = self._save_as_using_post_http_info(request)
        return self._call_api(**http_info)

    def save_as_using_post_invoker(self, request):
        http_info = self._save_as_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _save_as_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/saveAs",
            "request_type": request.__class__.__name__,
            "response_type": "SaveAsUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def save_using_post(self, request):
        r"""根据唯一键为“是”的属性更新实例的指定字段

        本接口用于根据数据模型中“唯一键”为“是”的属性（业务唯一键），对数据实例执行指定字段的保存或更新操作。
          - 更新（Update）：若系统中已存在匹配该唯一键的实例，则仅更新请求体中传入的指定字段。
          - 创建（Insert）：若系统中不存在匹配该唯一键的实例，则自动创建一条新实例。
        
        在调用本接口前，请确保目标数据模型已满足实例化条件：
        1. 已在应用设计态完成数据模型（数据实体或关系实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SaveUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.SaveUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.SaveUsingPostResponse`
        """
        http_info = self._save_using_post_http_info(request)
        return self._call_api(**http_info)

    def save_using_post_invoker(self, request):
        http_info = self._save_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _save_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/save",
            "request_type": request.__class__.__name__,
            "response_type": "SaveUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_find_using_post(self, request):
        r"""分页查询实例

        本接口用于分页查询指定数据模型中的数据实例列表。
        在调用本接口前，请确保目标数据模型已满足实例化条件：
        1. 已在应用设计态完成数据模型（数据实体或关系实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFindUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowFindUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowFindUsingPostResponse`
        """
        http_info = self._show_find_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_find_using_post_invoker(self, request):
        http_info = self._show_find_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_find_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/find/{pageSizePath}/{curPagePath}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFindUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'page_size_path' in local_var_params:
            path_params['pageSizePath'] = local_var_params['page_size_path']
        if 'cur_page_path' in local_var_params:
            path_params['curPagePath'] = local_var_params['cur_page_path']
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

        query_params = []
        if 'cur_page' in local_var_params:
            query_params.append(('curPage', local_var_params['cur_page']))
        if 'end_index' in local_var_params:
            query_params.append(('endIndex', local_var_params['end_index']))
        if 'max_page_size' in local_var_params:
            query_params.append(('maxPageSize', local_var_params['max_page_size']))
        if 'page_size' in local_var_params:
            query_params.append(('pageSize', local_var_params['page_size']))
        if 'start_index' in local_var_params:
            query_params.append(('startIndex', local_var_params['start_index']))
        if 'total_pages' in local_var_params:
            query_params.append(('totalPages', local_var_params['total_pages']))
        if 'total_rows' in local_var_params:
            query_params.append(('totalRows', local_var_params['total_rows']))

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

    def show_get_by_unique_key(self, request):
        r"""根据唯一键为“是”的基本属性查询实例

        当数据模型中存在“唯一键”为“是”的基本属性时，可根据该属性查询实例数据。
        在调用本接口前，请确保目标数据模型已满足实例化条件：
        1. 已在应用设计态完成数据模型（数据实体或关系实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGetByUniqueKey
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowGetByUniqueKeyRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowGetByUniqueKeyResponse`
        """
        http_info = self._show_get_by_unique_key_http_info(request)
        return self._call_api(**http_info)

    def show_get_by_unique_key_invoker(self, request):
        http_info = self._show_get_by_unique_key_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_get_by_unique_key_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/{getUniqueFieldMethod}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGetByUniqueKeyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']
        if 'get_unique_field_method' in local_var_params:
            path_params['getUniqueFieldMethod'] = local_var_params['get_unique_field_method']

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

    def show_get_parent(self, request):
        r"""获取父节点

        本接口用于获取指定数据实例的直接父节点，同时返回父节点的列表属性。当需要查询BOM（物料清单）中某个零部件的直接上级装配节点、查看组织架构中某个部门的直接汇报部门或获取产品分类的直接上级类目时，可调用本接口获取直接父节点信息。
        - 调用本接口时，需在childId中传入目标数据实例的ID，系统将返回该实例的直接父节点（仅返回一层，不向上递归）。
        - 返回结果中包含父节点的完整属性信息，包括创建者、创建时间、租户信息等列表属性。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGetParent
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowGetParentRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowGetParentResponse`
        """
        http_info = self._show_get_parent_http_info(request)
        return self._call_api(**http_info)

    def show_get_parent_invoker(self, request):
        http_info = self._show_get_parent_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_get_parent_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/getParent",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGetParentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_get_root(self, request):
        r"""获取根节点

        本接口用于获取指定数据实例所在树形结构的根节点信息。当需要追溯BOM（物料清单）的顶层装配节点、查找组织架构的顶层部门或定位产品分类的顶级类目时，可调用本接口获取目标节点的根节点。
        调用本接口时，需在id中传入目标数据实例的ID，系统将沿树形结构向上遍历，返回该实例所在树的根节点。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGetRoot
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowGetRootRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowGetRootResponse`
        """
        http_info = self._show_get_root_http_info(request)
        return self._call_api(**http_info)

    def show_get_root_invoker(self, request):
        http_info = self._show_get_root_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_get_root_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/getRoot",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGetRootResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_get_tokens(self, request):
        r"""获取Token信息

        本接口用于通过文档ID和认证类型获取结构化文档的访问Token。获取Token后，可在Token有效期内对指定结构化文档进行只读或读写操作。
        - 当认证类型为read时，获取的Token仅支持对文档进行查看操作。
        - 当认证类型为write时，获取的Token支持对文档进行编辑、保存等操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGetTokens
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowGetTokensRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowGetTokensResponse`
        """
        http_info = self._show_get_tokens_http_info(request)
        return self._call_api(**http_info)

    def show_get_tokens_invoker(self, request):
        http_info = self._show_get_tokens_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_get_tokens_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/structured-doc/tokens",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGetTokensResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_get_using_post(self, request):
        r"""查询实例详情

        本接口用于根据数据实例的唯一编码（id），查询指定数据模型下单个数据实例的完整详细信息。
        在调用本接口前，请确保目标数据模型已满足实例化条件：
        1. 已在应用设计态完成数据模型（数据实体或关系实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGetUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowGetUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowGetUsingPostResponse`
        """
        http_info = self._show_get_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_get_using_post_invoker(self, request):
        http_info = self._show_get_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_get_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/get",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGetUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_logical_delete_by_condition_using_post(self, request):
        r"""根据指定条件软删除实例

        本接口用于根据指定的过滤条件，批量对指定数据模型下满足条件的所有数据实例执行软删除（逻辑删除）操作。
        通过此接口进行删除操作时，系统会将当前删除的实例转存至XDM应用的XDMLogicDeleteData内置模型中。
        在调用本接口前，请确保目标数据模型已满足实例化条件：
        1. 已在应用设计态完成数据模型（数据实体或关系实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLogicalDeleteByConditionUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowLogicalDeleteByConditionUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowLogicalDeleteByConditionUsingPostResponse`
        """
        http_info = self._show_logical_delete_by_condition_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_logical_delete_by_condition_using_post_invoker(self, request):
        http_info = self._show_logical_delete_by_condition_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_logical_delete_by_condition_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/logicalDeleteByCondition",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLogicalDeleteByConditionUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_logical_delete_using_post(self, request):
        r"""软删除实例

        本接口用于根据数据实例的唯一编码（id），对指定数据模型下的单个数据实例执行软删除（逻辑删除）操作。
        软删除操作不会从数据库中物理移除数据，而是将实例标记为已删除状态，并转存至XDM应用的XDMLogicDeleteData内置模型中。如需彻底删除数据，请使用[删除实例 - DeleteUsingPost](DeleteUsingPost.xml)接口。
        在调用本接口前，请确保目标数据模型已满足实例化条件：
        1. 已在应用设计态完成数据模型（数据实体或关系实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLogicalDeleteUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowLogicalDeleteUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowLogicalDeleteUsingPostResponse`
        """
        http_info = self._show_logical_delete_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_logical_delete_using_post_invoker(self, request):
        http_info = self._show_logical_delete_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_logical_delete_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/logicalDelete",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLogicalDeleteUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_statics_page(self, request):
        r"""分页查询数据实例的统计信息

        本接口用于根据指定的聚合函数与分组条件，对指定数据模型的实例数据进行统计计算，并支持对分组后的统计结果进行分页返回。
        在调用本接口前，请确保目标数据模型已满足实例化条件：
        1. 已在应用设计态完成数据模型（数据实体或关系实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowStaticsPage
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowStaticsPageRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowStaticsPageResponse`
        """
        http_info = self._show_statics_page_http_info(request)
        return self._call_api(**http_info)

    def show_statics_page_invoker(self, request):
        http_info = self._show_statics_page_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_statics_page_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/staticsPage/{pageSizePath}/{curPagePath}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowStaticsPageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'page_size_path' in local_var_params:
            path_params['pageSizePath'] = local_var_params['page_size_path']
        if 'cur_page_path' in local_var_params:
            path_params['curPagePath'] = local_var_params['cur_page_path']

        query_params = []
        if 'cur_page' in local_var_params:
            query_params.append(('curPage', local_var_params['cur_page']))
        if 'end_index' in local_var_params:
            query_params.append(('endIndex', local_var_params['end_index']))
        if 'max_page_size' in local_var_params:
            query_params.append(('maxPageSize', local_var_params['max_page_size']))
        if 'page_size' in local_var_params:
            query_params.append(('pageSize', local_var_params['page_size']))
        if 'start_index' in local_var_params:
            query_params.append(('startIndex', local_var_params['start_index']))
        if 'total_pages' in local_var_params:
            query_params.append(('totalPages', local_var_params['total_pages']))
        if 'total_rows' in local_var_params:
            query_params.append(('totalRows', local_var_params['total_rows']))

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

    def show_statics_using_post(self, request):
        r"""查询指定数据模型的实例统计信息

        本接口用于根据指定的聚合函数与分组条件，对指定数据模型的实例数据进行统计计算（如计数、求平均值、求最大/最小值等）。
        在调用本接口前，请确保目标数据模型已满足实例化条件：
        1. 已在应用设计态完成数据模型（数据实体或关系实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowStaticsUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowStaticsUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowStaticsUsingPostResponse`
        """
        http_info = self._show_statics_using_post_http_info(request)
        return self._call_api(**http_info)

    def show_statics_using_post_invoker(self, request):
        http_info = self._show_statics_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_statics_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/statics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowStaticsUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_tag(self, request):
        r"""查询指定数据实例的标签详情

        本接口用于查询指定模型的数据实例已绑定的所有标签详情，返回标签的完整定义信息及所属标签组信息。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态创建并发布一个具有“标签管理”功能的数据模型。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTag
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowTagRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowTagResponse`
        """
        http_info = self._show_tag_http_info(request)
        return self._call_api(**http_info)

    def show_tag_invoker(self, request):
        http_info = self._show_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_tag_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/queryTag",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def show_version_by_master(self, request):
        r"""获取指定版本的M-V模型实例数据

        本接口用于根据主对象ID、迭代版本和版本号，查询M-V模型实例的详细版本信息。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVersionByMaster
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.ShowVersionByMasterRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ShowVersionByMasterResponse`
        """
        http_info = self._show_version_by_master_http_info(request)
        return self._call_api(**http_info)

    def show_version_by_master_invoker(self, request):
        http_info = self._show_version_by_master_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_version_by_master_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/getVersionByMaster",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVersionByMasterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def switch_lifecycle_template(self, request):
        r"""切换生命周期模板

        本接口用于为指定模型的数据实例切换绑定的生命周期模板，并同时指定实例在新模板中的生命周期状态。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态创建并发布一个具有“生命周期管理”功能的数据模型。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        3. 已在运行态创建目标生命周期模板，且模板中包含目标生命周期状态。具体操作请参见[生命周期管理](https://support.huaweicloud.com/usermanual-idme/idme_clientog_0068.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchLifecycleTemplate
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.SwitchLifecycleTemplateRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.SwitchLifecycleTemplateResponse`
        """
        http_info = self._switch_lifecycle_template_http_info(request)
        return self._call_api(**http_info)

    def switch_lifecycle_template_invoker(self, request):
        http_info = self._switch_lifecycle_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_lifecycle_template_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/switchLifecycleTemplate",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchLifecycleTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def update_and_checkin(self, request):
        r"""更新并检入M-V模型数据实例

        本接口用于更新指定M-V模型实例的数据，并同步完成检入操作，即一步完成“修改-提交”流程。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAndCheckin
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.UpdateAndCheckinRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.UpdateAndCheckinResponse`
        """
        http_info = self._update_and_checkin_http_info(request)
        return self._call_api(**http_info)

    def update_and_checkin_invoker(self, request):
        http_info = self._update_and_checkin_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_and_checkin_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/updateAndCheckin",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAndCheckinResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def update_and_revise(self, request):
        r"""修订并更新M-V模型数据实例

        本用于修订一个指定的M-V模型数据实例，并在修订生成新版本的同时，更新该新实例的业务数据。
        修订操作会将version字段升级为新的修订版本号（例如从A升级到B），随后将data参数中指定的属性值应用到新版本实例上。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAndRevise
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.UpdateAndReviseRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.UpdateAndReviseResponse`
        """
        http_info = self._update_and_revise_http_info(request)
        return self._call_api(**http_info)

    def update_and_revise_invoker(self, request):
        http_info = self._update_and_revise_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_and_revise_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/reviseAndUpdate",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAndReviseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def update_by_admin(self, request):
        r"""管理员更新M-V模型数据实例

        本接口用于管理员强制更新Master-Branch-Version（M-V）模型数据实例，适用于数据治理中的紧急数据修正、版本回滚、批量属性修正等管理场景。当实例的唯一编码不存在时，系统将不做任何更新操作。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态完成M-V模型实体（即“父模型”为“VersionObject”的数据实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateByAdmin
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.UpdateByAdminRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.UpdateByAdminResponse`
        """
        http_info = self._update_by_admin_http_info(request)
        return self._call_api(**http_info)

    def update_by_admin_invoker(self, request):
        http_info = self._update_by_admin_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_by_admin_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/updateByAdmin",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateByAdminResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def update_by_condition_using_post(self, request):
        r"""根据指定条件更新实例

        本接口用于根据指定的过滤条件，批量更新指定数据模型下满足条件的所有数据实例。
        在调用本接口前，请确保目标数据模型已满足实例化条件：
        1. 已在应用设计态完成数据模型（数据实体或关系实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateByConditionUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.UpdateByConditionUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.UpdateByConditionUsingPostResponse`
        """
        http_info = self._update_by_condition_using_post_http_info(request)
        return self._call_api(**http_info)

    def update_by_condition_using_post_invoker(self, request):
        http_info = self._update_by_condition_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_by_condition_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/updateByCondition",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateByConditionUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def update_document(self, request):
        r"""更新文档标题

        本接口用于更新结构化文档的标题信息。当文档标题需要随产品版本迭代、工艺变更或项目阶段调整时，可调用本接口修改文档标题。
        调用本接口时，需通过document_id或instance_id指定目标文档。
        若同时传入document_id和instance_id，优先以document_id定位目标文档。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDocument
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.UpdateDocumentRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.UpdateDocumentResponse`
        """
        http_info = self._update_document_http_info(request)
        return self._call_api(**http_info)

    def update_document_invoker(self, request):
        http_info = self._update_document_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_document_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/structured-doc/documents",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDocumentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def update_state(self, request):
        r"""设置生命周期的状态

        本接口用于修改或切换数据实例所绑定的生命周期状态，支持单个或批量实例的状态更新。
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态创建并发布一个具有“生命周期管理”功能的数据模型。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        3. 已在运行态创建并发布目标生命周期模板，且模板中包含目标生命周期状态。具体操作请参见[生命周期管理](https://support.huaweicloud.com/usermanual-idme/idme_clientog_0068.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateState
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.UpdateStateRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.UpdateStateResponse`
        """
        http_info = self._update_state_http_info(request)
        return self._call_api(**http_info)

    def update_state_invoker(self, request):
        http_info = self._update_state_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_state_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/updateState",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateStateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def update_using_post(self, request):
        r"""更新实例

        本接口用于更新指定数据模型中的一个实例数据。如果请求中指定的实例唯一编码（id）不存在，接口将不会执行任何更新操作，也不会返回错误。
        在调用本接口前，请确保目标数据模型已满足实例化条件：
        1. 已在应用设计态完成数据模型（数据实体或关系实体）的创建与发布。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateUsingPost
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.UpdateUsingPostRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.UpdateUsingPostResponse`
        """
        http_info = self._update_using_post_http_info(request)
        return self._call_api(**http_info)

    def update_using_post_invoker(self, request):
        http_info = self._update_using_post_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_using_post_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/update",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateUsingPostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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

    def update_view(self, request):
        r"""更新M-V模型数据实例的多维视图属性

        本接口用于更新指定M-V模型实例的多维视图属性。
        在多维视图管理中，一个零部件（Part）可能衍生出“研发”、“工艺”、“采购”等多个视图。随着业务流转或数据纠错的需求，可能需要对已存在的视图实例进行属性调整：
        - 变更视图标识（视角切换）：当视图绑定的分类标识（item，如MultiViewItem对象）分配错误或业务标准变更时，可通过此接口将其重新绑定到正确的视图标识上。
        - 视图属性脱敏/置空：在切换视角或修正数据时，通过needSetNull参数强制清空某些不再适用于当前视角的敏感或冗余属性。
        
        在调用本接口前，请确保目标数据模型满足以下条件：
        1. 已在应用设计态创建并发布一个具有“多维视图&amp;多维分支”功能的数据模型。具体操作请参见[创建数据实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0007.html)、[创建关系实体](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0022.html)和[应用发布](https://support.huaweicloud.com/usermanual-idme/idme_usermanual_0085.html)。
        2. 已将对应应用成功部署至运行态。具体操作请参见[部署应用](https://support.huaweicloud.com/consog-idme/idme_consog_0022.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateView
        :type request: :class:`huaweicloudsdkidmeclassicapi.v1.UpdateViewRequest`
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.UpdateViewResponse`
        """
        http_info = self._update_view_http_info(request)
        return self._call_api(**http_info)

    def update_view_invoker(self, request):
        http_info = self._update_view_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_view_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/rdm_{identifier}_app/publicservices/api/{modelName}/updateView",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateViewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identifier' in local_var_params:
            path_params['identifier'] = local_var_params['identifier']
        if 'model_name' in local_var_params:
            path_params['modelName'] = local_var_params['model_name']

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
