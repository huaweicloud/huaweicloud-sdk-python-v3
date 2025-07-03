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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkmeeting'")


class MeetingClient(Client):
    def __init__(self):
        super(MeetingClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkmeeting.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "MeetingCredentials")
        else:
            if clazz.__name__ != "MeetingClient":
                raise TypeError("client type error, support client type is MeetingClient")
            client_builder = ClientBuilder(clazz, "MeetingCredentials")

        

        return client_builder

    def add_app_id(self, request):
        r"""添加企业应用

        企业默认管理员添加应用，添加应用后，记录返回信息，后续可通过[[执行App ID鉴权](https://support.huaweicloud.com/api-meeting/meeting_21_0311.html)](tag:hws) [[执行App ID鉴权](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0311.html)](tag:hk)获取accessToken
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddAppId
        :type request: :class:`huaweicloudsdkmeeting.v1.AddAppIdRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.AddAppIdResponse`
        """
        http_info = self._add_app_id_http_info(request)
        return self._call_api(**http_info)

    def add_app_id_invoker(self, request):
        http_info = self._add_app_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_app_id_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/usg/acs/corp/app",
            "request_type": request.__class__.__name__,
            "response_type": "AddAppIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def add_corp(self, request):
        r"""SP管理员创建企业

        创建企业，默认管理员及分配资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddCorp
        :type request: :class:`huaweicloudsdkmeeting.v1.AddCorpRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.AddCorpResponse`
        """
        http_info = self._add_corp_http_info(request)
        return self._call_api(**http_info)

    def add_corp_invoker(self, request):
        http_info = self._add_corp_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_corp_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/dcs/sp/corp",
            "request_type": request.__class__.__name__,
            "response_type": "AddCorpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def add_corp_admin(self, request):
        r"""添加企业管理员

        企业默认管理员添加企业普通管理员。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddCorpAdmin
        :type request: :class:`huaweicloudsdkmeeting.v1.AddCorpAdminRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.AddCorpAdminResponse`
        """
        http_info = self._add_corp_admin_http_info(request)
        return self._call_api(**http_info)

    def add_corp_admin_invoker(self, request):
        http_info = self._add_corp_admin_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_corp_admin_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/dcs/corp/admin",
            "request_type": request.__class__.__name__,
            "response_type": "AddCorpAdminResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_type' in local_var_params:
            query_params.append(('accountType', local_var_params['account_type']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def add_department(self, request):
        r"""添加部门

        企业管理员通过该接口添加部门，最多支持10级部门，每级子部门最多支持100个，默认企业最大部门数量为10000个。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddDepartment
        :type request: :class:`huaweicloudsdkmeeting.v1.AddDepartmentRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.AddDepartmentResponse`
        """
        http_info = self._add_department_http_info(request)
        return self._call_api(**http_info)

    def add_department_invoker(self, request):
        http_info = self._add_department_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_department_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/dcs/corp/dept",
            "request_type": request.__class__.__name__,
            "response_type": "AddDepartmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def add_device(self, request):
        r"""增加终端

        企业管理员通过该接口添加专业会议终端。专业会议终端包括DP300/HUAWEI Bar系列/HUAWEI Board/TE系列。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddDevice
        :type request: :class:`huaweicloudsdkmeeting.v1.AddDeviceRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.AddDeviceResponse`
        """
        http_info = self._add_device_http_info(request)
        return self._call_api(**http_info)

    def add_device_invoker(self, request):
        http_info = self._add_device_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_device_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/dcs/corp/device",
            "request_type": request.__class__.__name__,
            "response_type": "AddDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def add_material(self, request):
        r"""新增信息窗素材

        新增信息窗素材（上传素材文件）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddMaterial
        :type request: :class:`huaweicloudsdkmeeting.v1.AddMaterialRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.AddMaterialResponse`
        """
        http_info = self._add_material_http_info(request)
        return self._call_api(**http_info)

    def add_material_invoker(self, request):
        http_info = self._add_material_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_material_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/sss/materials",
            "request_type": request.__class__.__name__,
            "response_type": "AddMaterialResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def add_program(self, request):
        r"""新增信息窗节目

        新增信息窗节目。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddProgram
        :type request: :class:`huaweicloudsdkmeeting.v1.AddProgramRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.AddProgramResponse`
        """
        http_info = self._add_program_http_info(request)
        return self._call_api(**http_info)

    def add_program_invoker(self, request):
        http_info = self._add_program_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_program_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/sss/programs",
            "request_type": request.__class__.__name__,
            "response_type": "AddProgramResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def add_publication(self, request):
        r"""新增信息窗发布

        新增信息窗发布。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddPublication
        :type request: :class:`huaweicloudsdkmeeting.v1.AddPublicationRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.AddPublicationResponse`
        """
        http_info = self._add_publication_http_info(request)
        return self._call_api(**http_info)

    def add_publication_invoker(self, request):
        http_info = self._add_publication_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_publication_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/sss/publications",
            "request_type": request.__class__.__name__,
            "response_type": "AddPublicationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def add_resource(self, request):
        r"""SP管理员分配企业资源

        企业新增资源发放。该接口同时支持修改，带resourceId后会判断该资源是否存在，存在即修改（支持修改的参数见修改接口），否则按新增处理。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddResource
        :type request: :class:`huaweicloudsdkmeeting.v1.AddResourceRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.AddResourceResponse`
        """
        http_info = self._add_resource_http_info(request)
        return self._call_api(**http_info)

    def add_resource_invoker(self, request):
        http_info = self._add_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_resource_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/dcs/sp/corp/{corp_id}/resource",
            "request_type": request.__class__.__name__,
            "response_type": "AddResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'corp_id' in local_var_params:
            path_params['corp_id'] = local_var_params['corp_id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def add_to_personal_space(self, request):
        r"""保存会议纪要到个人云空间

        用户使用手机扫码后,手机端请求服务端将当前会议纪要文件保存到个人云空间。二维码内容 ：cloudlink://cloudlink.huawei.com/h5page?action&#x3D;SAVE_MEETING_FILE&amp;key1&#x3D;value1&amp;key2&#x3D;value2 。key/value的个数可能变化，终端解析后，在发起后续请求时，将所有key/value存为map，作为入参即可。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddToPersonalSpace
        :type request: :class:`huaweicloudsdkmeeting.v1.AddToPersonalSpaceRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.AddToPersonalSpaceResponse`
        """
        http_info = self._add_to_personal_space_http_info(request)
        return self._call_api(**http_info)

    def add_to_personal_space_invoker(self, request):
        http_info = self._add_to_personal_space_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_to_personal_space_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/sss/meeting-files/save-to-personal-space",
            "request_type": request.__class__.__name__,
            "response_type": "AddToPersonalSpaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def add_user(self, request):
        r"""添加用户

        企业管理员通过该接口添加企业用户。
        &gt; 默认添加用户后，用户第一次登录华为云会议App或者Portal时需要修改密码。若需关闭第一次登录修改密码，请联系华为销售人员，并提供华为云会议企业ID。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddUser
        :type request: :class:`huaweicloudsdkmeeting.v1.AddUserRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.AddUserResponse`
        """
        http_info = self._add_user_http_info(request)
        return self._call_api(**http_info)

    def add_user_invoker(self, request):
        http_info = self._add_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_user_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/dcs/corp/member",
            "request_type": request.__class__.__name__,
            "response_type": "AddUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def allow_audience_join(self, request):
        r"""主持人允许观众入会

        主持人通过接口控制是否允许观众入会。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AllowAudienceJoin
        :type request: :class:`huaweicloudsdkmeeting.v1.AllowAudienceJoinRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.AllowAudienceJoinResponse`
        """
        http_info = self._allow_audience_join_http_info(request)
        return self._call_api(**http_info)

    def allow_audience_join_invoker(self, request):
        http_info = self._allow_audience_join_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _allow_audience_join_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/allowAudience",
            "request_type": request.__class__.__name__,
            "response_type": "AllowAudienceJoinResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def allow_client_record(self, request):
        r"""允许客户端录制

        该接口用于设置允许/禁止与会者客户端本地录制（非云端录制）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AllowClientRecord
        :type request: :class:`huaweicloudsdkmeeting.v1.AllowClientRecordRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.AllowClientRecordResponse`
        """
        http_info = self._allow_client_record_http_info(request)
        return self._call_api(**http_info)

    def allow_client_record_invoker(self, request):
        http_info = self._allow_client_record_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _allow_client_record_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/allowClientRecord",
            "request_type": request.__class__.__name__,
            "response_type": "AllowClientRecordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'participant_id' in local_var_params:
            query_params.append(('participantID', local_var_params['participant_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def allow_guest_unmute(self, request):
        r"""与会者自己解除静音

        该接口用于设置与会者是否可以自己解除静音。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AllowGuestUnmute
        :type request: :class:`huaweicloudsdkmeeting.v1.AllowGuestUnmuteRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.AllowGuestUnmuteResponse`
        """
        http_info = self._allow_guest_unmute_http_info(request)
        return self._call_api(**http_info)

    def allow_guest_unmute_invoker(self, request):
        http_info = self._allow_guest_unmute_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _allow_guest_unmute_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/mute/guestUnMute",
            "request_type": request.__class__.__name__,
            "response_type": "AllowGuestUnmuteResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def allow_waiting_participant(self, request):
        r"""准入等候者

        该接口用于允许等候室中的成员进入会议。可以允许全部成员进入会议，或者允许指定成员进入会议。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AllowWaitingParticipant
        :type request: :class:`huaweicloudsdkmeeting.v1.AllowWaitingParticipantRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.AllowWaitingParticipantResponse`
        """
        http_info = self._allow_waiting_participant_http_info(request)
        return self._call_api(**http_info)

    def allow_waiting_participant_invoker(self, request):
        http_info = self._allow_waiting_participant_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _allow_waiting_participant_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/allowWaitingParticipant",
            "request_type": request.__class__.__name__,
            "response_type": "AllowWaitingParticipantResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def associate_vmr(self, request):
        r"""分配云会议室

        企业管理员通过该接口将云会议室分配给用户、专业会议终端（TE10、TE20、HUAWEI Board、HUAWEI Bar 500及HUAWEI Box系列）、智慧屏TV、电子白板（SmartRooms）、IdeaHub。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateVmr
        :type request: :class:`huaweicloudsdkmeeting.v1.AssociateVmrRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.AssociateVmrResponse`
        """
        http_info = self._associate_vmr_http_info(request)
        return self._call_api(**http_info)

    def associate_vmr_invoker(self, request):
        http_info = self._associate_vmr_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _associate_vmr_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/dcs/corp/vmr/assign-to-member/{account}",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateVmrResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'account' in local_var_params:
            path_params['account'] = local_var_params['account']

        query_params = []
        if 'account_type' in local_var_params:
            query_params.append(('accountType', local_var_params['account_type']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def batch_delete_corp_admins(self, request):
        r"""批量删除企业管理员

        通过该接口批量删除企业管理员。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteCorpAdmins
        :type request: :class:`huaweicloudsdkmeeting.v1.BatchDeleteCorpAdminsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.BatchDeleteCorpAdminsResponse`
        """
        http_info = self._batch_delete_corp_admins_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_corp_admins_invoker(self, request):
        http_info = self._batch_delete_corp_admins_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_corp_admins_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/dcs/corp/admin/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteCorpAdminsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_type' in local_var_params:
            query_params.append(('accountType', local_var_params['account_type']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def batch_delete_devices(self, request):
        r"""批量删除终端

        企业管理员通过该接口批量删除专业会议终端，返回删除失败的列表。
        &gt; 如果需要删除Ideahub、SmartRooms、智慧屏TV请使用[[批量删除用户](https://support.huaweicloud.com/api-meeting/meeting_21_0070.html)](tag:hws)[[批量删除用户](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0070.html)](tag:hk)接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteDevices
        :type request: :class:`huaweicloudsdkmeeting.v1.BatchDeleteDevicesRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.BatchDeleteDevicesResponse`
        """
        http_info = self._batch_delete_devices_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_devices_invoker(self, request):
        http_info = self._batch_delete_devices_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_devices_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/dcs/corp/device/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteDevicesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def batch_delete_materials(self, request):
        r"""删除信息窗素材

        删除信息窗素材。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteMaterials
        :type request: :class:`huaweicloudsdkmeeting.v1.BatchDeleteMaterialsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.BatchDeleteMaterialsResponse`
        """
        http_info = self._batch_delete_materials_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_materials_invoker(self, request):
        http_info = self._batch_delete_materials_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_materials_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/sss/materials/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteMaterialsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def batch_delete_programs(self, request):
        r"""删除信息窗节目

        删除信息窗节目。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeletePrograms
        :type request: :class:`huaweicloudsdkmeeting.v1.BatchDeleteProgramsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.BatchDeleteProgramsResponse`
        """
        http_info = self._batch_delete_programs_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_programs_invoker(self, request):
        http_info = self._batch_delete_programs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_programs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/sss/programs/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteProgramsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def batch_delete_publications(self, request):
        r"""删除信息窗发布

        删除信息窗发布。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeletePublications
        :type request: :class:`huaweicloudsdkmeeting.v1.BatchDeletePublicationsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.BatchDeletePublicationsResponse`
        """
        http_info = self._batch_delete_publications_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_publications_invoker(self, request):
        http_info = self._batch_delete_publications_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_publications_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/sss/publications/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeletePublicationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def batch_delete_users(self, request):
        r"""批量删除用户

        企业管理员通过该接口批量删除企业用户。删除多个用户时，全部删除成功或者全部删除失败。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteUsers
        :type request: :class:`huaweicloudsdkmeeting.v1.BatchDeleteUsersRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.BatchDeleteUsersResponse`
        """
        http_info = self._batch_delete_users_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_users_invoker(self, request):
        http_info = self._batch_delete_users_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_users_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/dcs/corp/member/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteUsersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_type' in local_var_params:
            query_params.append(('accountType', local_var_params['account_type']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def batch_hand(self, request):
        r"""批量举手

        该接口用于批量设置来宾的举手/放下举手状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchHand
        :type request: :class:`huaweicloudsdkmeeting.v1.BatchHandRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.BatchHandResponse`
        """
        http_info = self._batch_hand_http_info(request)
        return self._call_api(**http_info)

    def batch_hand_invoker(self, request):
        http_info = self._batch_hand_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_hand_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/participants/batch/hands",
            "request_type": request.__class__.__name__,
            "response_type": "BatchHandResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def batch_move_to_waiting_room(self, request):
        r"""批量移入等候室

        主持人通过该接口批量移动用户到等候室。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchMoveToWaitingRoom
        :type request: :class:`huaweicloudsdkmeeting.v1.BatchMoveToWaitingRoomRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.BatchMoveToWaitingRoomResponse`
        """
        http_info = self._batch_move_to_waiting_room_http_info(request)
        return self._call_api(**http_info)

    def batch_move_to_waiting_room_invoker(self, request):
        http_info = self._batch_move_to_waiting_room_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_move_to_waiting_room_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/batchMoveToWaitingRoom",
            "request_type": request.__class__.__name__,
            "response_type": "BatchMoveToWaitingRoomResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def batch_search_app_id(self, request):
        r"""分页查询企业应用

        企业默认管理员分页查询企业应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchSearchAppId
        :type request: :class:`huaweicloudsdkmeeting.v1.BatchSearchAppIdRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.BatchSearchAppIdResponse`
        """
        http_info = self._batch_search_app_id_http_info(request)
        return self._call_api(**http_info)

    def batch_search_app_id_invoker(self, request):
        http_info = self._batch_search_app_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_search_app_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/usg/acs/corp/apps",
            "request_type": request.__class__.__name__,
            "response_type": "BatchSearchAppIdResponse"
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
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def batch_show_user_details(self, request):
        r"""批量查询用户详情

        批量查询用户详情，支持指定第三方账号查询详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchShowUserDetails
        :type request: :class:`huaweicloudsdkmeeting.v1.BatchShowUserDetailsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.BatchShowUserDetailsResponse`
        """
        http_info = self._batch_show_user_details_http_info(request)
        return self._call_api(**http_info)

    def batch_show_user_details_invoker(self, request):
        http_info = self._batch_show_user_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_show_user_details_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/abs/users/list",
            "request_type": request.__class__.__name__,
            "response_type": "BatchShowUserDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id_type' in local_var_params:
            query_params.append(('idType', local_var_params['id_type']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def batch_update_devices_status(self, request):
        r"""批量修改终端状态

        企业管理员通过该接口批量修改专业会议终端状态。当硬终端资源到期后，若企业内对应资源的硬终端超过数量后会被系统随机自动停用，此时可通过该接口修改专业会议终端的状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateDevicesStatus
        :type request: :class:`huaweicloudsdkmeeting.v1.BatchUpdateDevicesStatusRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.BatchUpdateDevicesStatusResponse`
        """
        http_info = self._batch_update_devices_status_http_info(request)
        return self._call_api(**http_info)

    def batch_update_devices_status_invoker(self, request):
        http_info = self._batch_update_devices_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_update_devices_status_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/usg/dcs/corp/device/status/{value}",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateDevicesStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'value' in local_var_params:
            path_params['value'] = local_var_params['value']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def batch_update_user_status(self, request):
        r"""批量修改用户状态

        企业管理员通过该接口批量修改用户状态，当用户帐号数资源或者电子白板（SmartRooms）资源到期后，若企业内对应资源的用户帐号超过数量后会被系统随机自动停用，此时可通过该接口修改用户的状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateUserStatus
        :type request: :class:`huaweicloudsdkmeeting.v1.BatchUpdateUserStatusRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.BatchUpdateUserStatusResponse`
        """
        http_info = self._batch_update_user_status_http_info(request)
        return self._call_api(**http_info)

    def batch_update_user_status_invoker(self, request):
        http_info = self._batch_update_user_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_update_user_status_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/usg/dcs/corp/member/status/{value}",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateUserStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'value' in local_var_params:
            path_params['value'] = local_var_params['value']

        query_params = []
        if 'account_type' in local_var_params:
            query_params.append(('accountType', local_var_params['account_type']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def broadcast_participant(self, request):
        r"""广播会场

        该接口用于广播指定的与会者。同一时间，只允许一个与会者被广播。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BroadcastParticipant
        :type request: :class:`huaweicloudsdkmeeting.v1.BroadcastParticipantRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.BroadcastParticipantResponse`
        """
        http_info = self._broadcast_participant_http_info(request)
        return self._call_api(**http_info)

    def broadcast_participant_invoker(self, request):
        http_info = self._broadcast_participant_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _broadcast_participant_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/participants/broadcast",
            "request_type": request.__class__.__name__,
            "response_type": "BroadcastParticipantResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'participant_id' in local_var_params:
            query_params.append(('participantID', local_var_params['participant_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def cancel_broadcast(self, request):
        r"""取消广播

        该接口用于取消广播，包括：取消广播多画面，取消广播会场，取消点名会场。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelBroadcast
        :type request: :class:`huaweicloudsdkmeeting.v1.CancelBroadcastRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CancelBroadcastResponse`
        """
        http_info = self._cancel_broadcast_http_info(request)
        return self._call_api(**http_info)

    def cancel_broadcast_invoker(self, request):
        http_info = self._cancel_broadcast_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_broadcast_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/cancelBroadcast",
            "request_type": request.__class__.__name__,
            "response_type": "CancelBroadcastResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def cancel_meeting(self, request):
        r"""取消预约会议

        该接口用于取消预约的会议。企业管理员可以取消本企业下用户创建的会议，普通用户只能取消自己创建的会议。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.CancelMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CancelMeetingResponse`
        """
        http_info = self._cancel_meeting_http_info(request)
        return self._call_api(**http_info)

    def cancel_meeting_invoker(self, request):
        http_info = self._cancel_meeting_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_meeting_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/mmc/management/conferences",
            "request_type": request.__class__.__name__,
            "response_type": "CancelMeetingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

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

    def cancel_recurring_meeting(self, request):
        r"""取消周期性会议

        该接口用于取消周期性会议。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelRecurringMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.CancelRecurringMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CancelRecurringMeetingResponse`
        """
        http_info = self._cancel_recurring_meeting_http_info(request)
        return self._call_api(**http_info)

    def cancel_recurring_meeting_invoker(self, request):
        http_info = self._cancel_recurring_meeting_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_recurring_meeting_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/mmc/management/cycleconferences",
            "request_type": request.__class__.__name__,
            "response_type": "CancelRecurringMeetingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

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

    def cancel_recurring_sub_meeting(self, request):
        r"""取消周期性会议的子会议

        该接口用于取消周期性会议的子会议。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelRecurringSubMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.CancelRecurringSubMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CancelRecurringSubMeetingResponse`
        """
        http_info = self._cancel_recurring_sub_meeting_http_info(request)
        return self._call_api(**http_info)

    def cancel_recurring_sub_meeting_invoker(self, request):
        http_info = self._cancel_recurring_sub_meeting_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_recurring_sub_meeting_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/mmc/management/conferences/cyclesubconf",
            "request_type": request.__class__.__name__,
            "response_type": "CancelRecurringSubMeetingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

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

    def check_call_number_in_conf(self, request):
        r"""根据号码，查询是否在会议中

        通过该接口查询号码，是否在会议中
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckCallNumberInConf
        :type request: :class:`huaweicloudsdkmeeting.v1.CheckCallNumberInConfRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CheckCallNumberInConfResponse`
        """
        http_info = self._check_call_number_in_conf_http_info(request)
        return self._call_api(**http_info)

    def check_call_number_in_conf_invoker(self, request):
        http_info = self._check_call_number_in_conf_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_call_number_in_conf_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/mms/ncms/conferences/online/check-callnumber-in-conf",
            "request_type": request.__class__.__name__,
            "response_type": "CheckCallNumberInConfResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'call_number' in local_var_params:
            query_params.append(('call_number', local_var_params['call_number']))

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

    def check_slide_verify_code(self, request):
        r"""校验滑块验证码

        该接口提供校验滑块验证码。服务器收到请求，返回校验结果。用户在前台界面通过滑块操作匹配图形，使得抠图和原图吻合。然后服务器进行校验滑块验证码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckSlideVerifyCode
        :type request: :class:`huaweicloudsdkmeeting.v1.CheckSlideVerifyCodeRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CheckSlideVerifyCodeResponse`
        """
        http_info = self._check_slide_verify_code_http_info(request)
        return self._call_api(**http_info)

    def check_slide_verify_code_invoker(self, request):
        http_info = self._check_slide_verify_code_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_slide_verify_code_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/usg/acs/auth/slideverifycode/check",
            "request_type": request.__class__.__name__,
            "response_type": "CheckSlideVerifyCodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def check_token(self, request):
        r"""校验Token

        该接口提供校验token合法性功能。服务器收到请求后，验证token合法性并返回结果。如果参数needGenNewToken为true时，生成新的token并返回。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckToken
        :type request: :class:`huaweicloudsdkmeeting.v1.CheckTokenRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CheckTokenResponse`
        """
        http_info = self._check_token_http_info(request)
        return self._call_api(**http_info)

    def check_token_invoker(self, request):
        http_info = self._check_token_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_token_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/acs/token/validate",
            "request_type": request.__class__.__name__,
            "response_type": "CheckTokenResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def check_veri_code_for_update_user_info(self, request):
        r"""校验手机和邮箱对应的验证码

        企业用户通过该接口校验手机和邮箱对应的验证码，一分钟内记录尝试次数不得超过5次。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckVeriCodeForUpdateUserInfo
        :type request: :class:`huaweicloudsdkmeeting.v1.CheckVeriCodeForUpdateUserInfoRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CheckVeriCodeForUpdateUserInfoResponse`
        """
        http_info = self._check_veri_code_for_update_user_info_http_info(request)
        return self._call_api(**http_info)

    def check_veri_code_for_update_user_info_invoker(self, request):
        http_info = self._check_veri_code_for_update_user_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_veri_code_for_update_user_info_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/dcs/member/verification-code/verify",
            "request_type": request.__class__.__name__,
            "response_type": "CheckVeriCodeForUpdateUserInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def check_verify_code(self, request):
        r"""校验验证码

        该接口提供校验验证码，服务器收到请求，返回结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckVerifyCode
        :type request: :class:`huaweicloudsdkmeeting.v1.CheckVerifyCodeRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CheckVerifyCodeResponse`
        """
        http_info = self._check_verify_code_http_info(request)
        return self._call_api(**http_info)

    def check_verify_code_invoker(self, request):
        http_info = self._check_verify_code_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_verify_code_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/usg/acs/verifycode/check",
            "request_type": request.__class__.__name__,
            "response_type": "CheckVerifyCodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def create_anonymous_auth_random(self, request):
        r"""匿名用户会议鉴权

        该接口用于匿名用户入会鉴权。请求根据会议ID和密码鉴权，返回鉴权随机数（可以根据该随机数获取匿名用户信息、会议信息等）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAnonymousAuthRandom
        :type request: :class:`huaweicloudsdkmeeting.v1.CreateAnonymousAuthRandomRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CreateAnonymousAuthRandomResponse`
        """
        http_info = self._create_anonymous_auth_random_http_info(request)
        return self._call_api(**http_info)

    def create_anonymous_auth_random_invoker(self, request):
        http_info = self._create_anonymous_auth_random_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_anonymous_auth_random_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/mmc/management/conferences/anonymous/auth",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAnonymousAuthRandomResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_password' in local_var_params:
            header_params['X-Password'] = local_var_params['x_password']

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

    def create_auth_random(self, request):
        r"""获取会议鉴权随机数

        根据会议ID + 密码鉴权返回鉴权随机数，如果是小程序调用时，需要企业支持小程序功能
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAuthRandom
        :type request: :class:`huaweicloudsdkmeeting.v1.CreateAuthRandomRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CreateAuthRandomResponse`
        """
        http_info = self._create_auth_random_http_info(request)
        return self._call_api(**http_info)

    def create_auth_random_invoker(self, request):
        http_info = self._create_auth_random_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_auth_random_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/mms/ncms/conferences/auth/random",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAuthRandomResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conf_id' in local_var_params:
            query_params.append(('conf_id', local_var_params['conf_id']))
        if 'guest_waiting' in local_var_params:
            query_params.append(('guest_waiting', local_var_params['guest_waiting']))

        header_params = {}
        if 'x_password' in local_var_params:
            header_params['X-Password'] = local_var_params['x_password']

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

    def create_conf_token(self, request):
        r"""获取会控Token

        该接口用于获取正在召开会议的会控Token（未开始的会议调用该接口返回失败）。Token有效期是半个小时。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateConfToken
        :type request: :class:`huaweicloudsdkmeeting.v1.CreateConfTokenRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CreateConfTokenResponse`
        """
        http_info = self._create_conf_token_http_info(request)
        return self._call_api(**http_info)

    def create_conf_token_invoker(self, request):
        http_info = self._create_conf_token_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_conf_token_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/mmc/control/conferences/token",
            "request_type": request.__class__.__name__,
            "response_type": "CreateConfTokenResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']
        if 'x_password' in local_var_params:
            header_params['X-Password'] = local_var_params['x_password']
        if 'x_login_type' in local_var_params:
            header_params['X-Login-Type'] = local_var_params['x_login_type']
        if 'x_nonce' in local_var_params:
            header_params['X-Nonce'] = local_var_params['x_nonce']

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

    def create_meeting(self, request):
        r"""创建会议

        该接口用于创建立即会议和预约会议。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.CreateMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CreateMeetingResponse`
        """
        http_info = self._create_meeting_http_info(request)
        return self._call_api(**http_info)

    def create_meeting_invoker(self, request):
        http_info = self._create_meeting_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_meeting_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/mmc/management/conferences",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMeetingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

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

    def create_portal_ref_nonce(self, request):
        r"""获取页面免登陆跳转的nonce信息

        通过Access Token生成页面免登陆跳转到华为云会议的Portal的nonce信息。获取到nonce信息后，通过链接https://meeting.huaweicloud.com/?lang&#x3D;zh-CN&amp;nonce&#x3D;xxxxxxxxxxxxx#/login进行免登陆跳转。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePortalRefNonce
        :type request: :class:`huaweicloudsdkmeeting.v1.CreatePortalRefNonceRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CreatePortalRefNonceResponse`
        """
        http_info = self._create_portal_ref_nonce_http_info(request)
        return self._call_api(**http_info)

    def create_portal_ref_nonce_invoker(self, request):
        http_info = self._create_portal_ref_nonce_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_portal_ref_nonce_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/acs/auth/portal-ref-nonce",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePortalRefNonceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def create_recurring_meeting(self, request):
        r"""创建周期性会议

        该接口用于预约周期性会议。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRecurringMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.CreateRecurringMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CreateRecurringMeetingResponse`
        """
        http_info = self._create_recurring_meeting_http_info(request)
        return self._call_api(**http_info)

    def create_recurring_meeting_invoker(self, request):
        http_info = self._create_recurring_meeting_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_recurring_meeting_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/mmc/management/cycleconferences",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRecurringMeetingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

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

    def create_vision_active_code(self, request):
        r"""企业管理员生成激活码

        企业管理员生成智慧屏、电子白板（SmartRooms）、Ideahub的激活码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateVisionActiveCode
        :type request: :class:`huaweicloudsdkmeeting.v1.CreateVisionActiveCodeRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CreateVisionActiveCodeResponse`
        """
        http_info = self._create_vision_active_code_http_info(request)
        return self._call_api(**http_info)

    def create_vision_active_code_invoker(self, request):
        http_info = self._create_vision_active_code_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_vision_active_code_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/dcs/corp/vision/activecode",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVisionActiveCodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def create_web_socket_token(self, request):
        r"""获取websocket建链Token

        该接口用于获取会控WebSocket建链的临时Token。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateWebSocketToken
        :type request: :class:`huaweicloudsdkmeeting.v1.CreateWebSocketTokenRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CreateWebSocketTokenResponse`
        """
        http_info = self._create_web_socket_token_http_info(request)
        return self._call_api(**http_info)

    def create_web_socket_token_invoker(self, request):
        http_info = self._create_web_socket_token_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_web_socket_token_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/mmc/control/conferences/wsToken",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWebSocketTokenResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def create_webinar(self, request):
        r"""预约网络研讨会

        该接口用于创建网络研讨会。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateWebinar
        :type request: :class:`huaweicloudsdkmeeting.v1.CreateWebinarRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.CreateWebinarResponse`
        """
        http_info = self._create_webinar_http_info(request)
        return self._call_api(**http_info)

    def create_webinar_invoker(self, request):
        http_info = self._create_webinar_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_webinar_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/wss/webinar/open/conferences",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWebinarResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def delete_app_id(self, request):
        r"""删除企业应用

        企业管理员删除企业应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAppId
        :type request: :class:`huaweicloudsdkmeeting.v1.DeleteAppIdRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.DeleteAppIdResponse`
        """
        http_info = self._delete_app_id_http_info(request)
        return self._call_api(**http_info)

    def delete_app_id_invoker(self, request):
        http_info = self._delete_app_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_app_id_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/usg/acs/corp/app/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAppIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def delete_attendees(self, request):
        r"""删除与会者

        该接口用于删除与会者。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAttendees
        :type request: :class:`huaweicloudsdkmeeting.v1.DeleteAttendeesRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.DeleteAttendeesResponse`
        """
        http_info = self._delete_attendees_http_info(request)
        return self._call_api(**http_info)

    def delete_attendees_invoker(self, request):
        http_info = self._delete_attendees_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_attendees_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/mmc/control/conferences/attendees/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAttendeesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def delete_corp(self, request):
        r"""SP管理员删除企业

        删除企业。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCorp
        :type request: :class:`huaweicloudsdkmeeting.v1.DeleteCorpRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.DeleteCorpResponse`
        """
        http_info = self._delete_corp_http_info(request)
        return self._call_api(**http_info)

    def delete_corp_invoker(self, request):
        http_info = self._delete_corp_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_corp_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/usg/dcs/sp/corp/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCorpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def delete_corp_vmr(self, request):
        r"""删除云会议室

        企业管理员通过该接口删除企业的云会议室。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCorpVmr
        :type request: :class:`huaweicloudsdkmeeting.v1.DeleteCorpVmrRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.DeleteCorpVmrResponse`
        """
        http_info = self._delete_corp_vmr_http_info(request)
        return self._call_api(**http_info)

    def delete_corp_vmr_invoker(self, request):
        http_info = self._delete_corp_vmr_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_corp_vmr_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/dcs/corp/vmr/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCorpVmrResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def delete_department(self, request):
        r"""删除部门

        企业管理员通过该接口删除部门。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDepartment
        :type request: :class:`huaweicloudsdkmeeting.v1.DeleteDepartmentRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.DeleteDepartmentResponse`
        """
        http_info = self._delete_department_http_info(request)
        return self._call_api(**http_info)

    def delete_department_invoker(self, request):
        http_info = self._delete_department_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_department_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/usg/dcs/corp/dept/{dept_code}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDepartmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dept_code' in local_var_params:
            path_params['dept_code'] = local_var_params['dept_code']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def delete_layout(self, request):
        r"""删除多画面布局

        该接口用于删除当前会议已保存的多画面布局。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteLayout
        :type request: :class:`huaweicloudsdkmeeting.v1.DeleteLayoutRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.DeleteLayoutResponse`
        """
        http_info = self._delete_layout_http_info(request)
        return self._call_api(**http_info)

    def delete_layout_invoker(self, request):
        http_info = self._delete_layout_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_layout_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/mmc/control/conferences/layOut",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLayoutResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'uu_id' in local_var_params:
            query_params.append(('uuID', local_var_params['uu_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def delete_recordings(self, request):
        r"""批量删除录制

        该接口用于批量删除会议的录制。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRecordings
        :type request: :class:`huaweicloudsdkmeeting.v1.DeleteRecordingsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.DeleteRecordingsResponse`
        """
        http_info = self._delete_recordings_http_info(request)
        return self._call_api(**http_info)

    def delete_recordings_invoker(self, request):
        http_info = self._delete_recordings_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_recordings_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/mmc/management/record/files",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRecordingsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conf_uui_ds' in local_var_params:
            query_params.append(('confUUIDs', local_var_params['conf_uui_ds']))
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

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

    def delete_resource(self, request):
        r"""SP管理员根据删除企业资源

        企业删除资源项，删除资源项后，企业资源总数会自动减少。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteResource
        :type request: :class:`huaweicloudsdkmeeting.v1.DeleteResourceRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.DeleteResourceResponse`
        """
        http_info = self._delete_resource_http_info(request)
        return self._call_api(**http_info)

    def delete_resource_invoker(self, request):
        http_info = self._delete_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_resource_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/dcs/sp/corp/{corp_id}/resource/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'corp_id' in local_var_params:
            path_params['corp_id'] = local_var_params['corp_id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def delete_token(self, request):
        r"""注销登录

        该接口提供注销功能。服务器收到请求后，删除该Token。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteToken
        :type request: :class:`huaweicloudsdkmeeting.v1.DeleteTokenRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.DeleteTokenResponse`
        """
        http_info = self._delete_token_http_info(request)
        return self._call_api(**http_info)

    def delete_token_invoker(self, request):
        http_info = self._delete_token_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_token_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/usg/acs/token",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTokenResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def delete_vision_active_code(self, request):
        r"""企业管理员删除激活码

        企业管理员批量删除激活码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteVisionActiveCode
        :type request: :class:`huaweicloudsdkmeeting.v1.DeleteVisionActiveCodeRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.DeleteVisionActiveCodeResponse`
        """
        http_info = self._delete_vision_active_code_http_info(request)
        return self._call_api(**http_info)

    def delete_vision_active_code_invoker(self, request):
        http_info = self._delete_vision_active_code_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_vision_active_code_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/usg/dcs/corp/vision/activecode",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVisionActiveCodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def delete_web_hook_config(self, request):
        r"""删除事件推送

        该接口用于管理员删除已配置的事件推送设置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteWebHookConfig
        :type request: :class:`huaweicloudsdkmeeting.v1.DeleteWebHookConfigRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.DeleteWebHookConfigResponse`
        """
        http_info = self._delete_web_hook_config_http_info(request)
        return self._call_api(**http_info)

    def delete_web_hook_config_invoker(self, request):
        http_info = self._delete_web_hook_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_web_hook_config_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/mmc/management/webhook/link-config",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteWebHookConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

    def delete_webinar(self, request):
        r"""取消网络研讨会

        该接口用于取消已预约的网络研讨会。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteWebinar
        :type request: :class:`huaweicloudsdkmeeting.v1.DeleteWebinarRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.DeleteWebinarResponse`
        """
        http_info = self._delete_webinar_http_info(request)
        return self._call_api(**http_info)

    def delete_webinar_invoker(self, request):
        http_info = self._delete_webinar_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_webinar_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/wss/webinar/open/conferences/{conference_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteWebinarResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'conference_id' in local_var_params:
            path_params['conference_id'] = local_var_params['conference_id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def disassociate_vmr(self, request):
        r"""回收云会议室

        企业管理员通过该接口回收云会议室。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisassociateVmr
        :type request: :class:`huaweicloudsdkmeeting.v1.DisassociateVmrRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.DisassociateVmrResponse`
        """
        http_info = self._disassociate_vmr_http_info(request)
        return self._call_api(**http_info)

    def disassociate_vmr_invoker(self, request):
        http_info = self._disassociate_vmr_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disassociate_vmr_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/dcs/corp/vmr/recycle-from-member/{account}",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateVmrResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'account' in local_var_params:
            path_params['account'] = local_var_params['account']

        query_params = []
        if 'account_type' in local_var_params:
            query_params.append(('accountType', local_var_params['account_type']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def hand(self, request):
        r"""举手

        该接口用于设置指定与会者的举手/放下举手状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for Hand
        :type request: :class:`huaweicloudsdkmeeting.v1.HandRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.HandResponse`
        """
        http_info = self._hand_http_info(request)
        return self._call_api(**http_info)

    def hand_invoker(self, request):
        http_info = self._hand_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _hand_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/participants/hands",
            "request_type": request.__class__.__name__,
            "response_type": "HandResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'participant_id' in local_var_params:
            query_params.append(('participantID', local_var_params['participant_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def hang_up(self, request):
        r"""挂断与会者

        该接口用于挂断正在通话中的与会者。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for HangUp
        :type request: :class:`huaweicloudsdkmeeting.v1.HangUpRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.HangUpResponse`
        """
        http_info = self._hang_up_http_info(request)
        return self._call_api(**http_info)

    def hang_up_invoker(self, request):
        http_info = self._hang_up_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _hang_up_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/mmc/control/conferences/participants/delete",
            "request_type": request.__class__.__name__,
            "response_type": "HangUpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def invite_operate_video(self, request):
        r"""主持人邀请与会者开启/关闭摄像头

        该接口用于邀请指定与会者开启、关闭摄像头。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for InviteOperateVideo
        :type request: :class:`huaweicloudsdkmeeting.v1.InviteOperateVideoRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.InviteOperateVideoResponse`
        """
        http_info = self._invite_operate_video_http_info(request)
        return self._call_api(**http_info)

    def invite_operate_video_invoker(self, request):
        http_info = self._invite_operate_video_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _invite_operate_video_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/participants/video",
            "request_type": request.__class__.__name__,
            "response_type": "InviteOperateVideoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'participant_id' in local_var_params:
            query_params.append(('participantID', local_var_params['participant_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def invite_participant(self, request):
        r"""邀请与会者

        该接口用于邀请与会者加入会议。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for InviteParticipant
        :type request: :class:`huaweicloudsdkmeeting.v1.InviteParticipantRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.InviteParticipantResponse`
        """
        http_info = self._invite_participant_http_info(request)
        return self._call_api(**http_info)

    def invite_participant_invoker(self, request):
        http_info = self._invite_participant_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _invite_participant_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/mmc/control/conferences/participants",
            "request_type": request.__class__.__name__,
            "response_type": "InviteParticipantResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def invite_share(self, request):
        r"""邀请共享

        该接口用于邀请/取消邀请指定与会人共享桌面。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for InviteShare
        :type request: :class:`huaweicloudsdkmeeting.v1.InviteShareRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.InviteShareResponse`
        """
        http_info = self._invite_share_http_info(request)
        return self._call_api(**http_info)

    def invite_share_invoker(self, request):
        http_info = self._invite_share_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _invite_share_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/participants/share/invite",
            "request_type": request.__class__.__name__,
            "response_type": "InviteShareResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'participant_id' in local_var_params:
            query_params.append(('participantID', local_var_params['participant_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def invite_user(self, request):
        r"""邀请用户

        通过手机号码或者邮箱地址邀请用户加入企业。
        * 若被邀请用户在华为云会议系统中不存在，则：
          - 华为云会议免费版和华为云会议标准版发送短信/邮件邀请用户完成注册后加入企业。用户注册成功后，加入该企业。
          - 华为云会议旗舰版在企业内直接添加该用户。用户会收到华为云会议的初始密码，用户第一次以手机号或者邮箱登录时，需要修改密码。
        * 若被邀请用户在华为云会议系统中存在，则该用户会收到短信或者邮件确认。确认完成后改用户加入企业内。该用户的密码保持原来的密码不变。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for InviteUser
        :type request: :class:`huaweicloudsdkmeeting.v1.InviteUserRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.InviteUserResponse`
        """
        http_info = self._invite_user_http_info(request)
        return self._call_api(**http_info)

    def invite_user_invoker(self, request):
        http_info = self._invite_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _invite_user_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/dcs/corp/member/add",
            "request_type": request.__class__.__name__,
            "response_type": "InviteUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def invite_with_pwd(self, request):
        r"""通过会议ID和密码邀请与会者

        该接口用于通过会议ID和密码邀请与会者。一般用于App已知会议ID和来宾密码，通过扫码等方式获取其他终端的SIP号码后，使用该接口将其他终端邀请加入会议中。
        &gt; 需要管理员在企业的“会议设置”&gt;“来宾扫码邀请任意硬终端入会”设置成打开，才允许通过来宾密码邀请其他终端入会。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for InviteWithPwd
        :type request: :class:`huaweicloudsdkmeeting.v1.InviteWithPwdRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.InviteWithPwdResponse`
        """
        http_info = self._invite_with_pwd_http_info(request)
        return self._call_api(**http_info)

    def invite_with_pwd_invoker(self, request):
        http_info = self._invite_with_pwd_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _invite_with_pwd_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/mmc/control/conferences/inviteWithPwd",
            "request_type": request.__class__.__name__,
            "response_type": "InviteWithPwdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

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

    def list_history_webinars(self, request):
        r"""查询历史召开的网络研讨会列表

        该接口用于查询历史网络研讨会。管理员可查询企业内历史网络研讨会，非管理员可查询个人历史网络研讨会。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHistoryWebinars
        :type request: :class:`huaweicloudsdkmeeting.v1.ListHistoryWebinarsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ListHistoryWebinarsResponse`
        """
        http_info = self._list_history_webinars_http_info(request)
        return self._call_api(**http_info)

    def list_history_webinars_invoker(self, request):
        http_info = self._list_history_webinars_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_history_webinars_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/wss/webinar/open/conferences/history",
            "request_type": request.__class__.__name__,
            "response_type": "ListHistoryWebinarsResponse"
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
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'sort_type' in local_var_params:
            query_params.append(('sortType', local_var_params['sort_type']))
        if 'start_time' in local_var_params:
            query_params.append(('startTime', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('endTime', local_var_params['end_time']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def list_network_quality(self, request):
        r"""查询会场网络质量

        查询会场网络质量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNetworkQuality
        :type request: :class:`huaweicloudsdkmeeting.v1.ListNetworkQualityRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ListNetworkQualityResponse`
        """
        http_info = self._list_network_quality_http_info(request)
        return self._call_api(**http_info)

    def list_network_quality_invoker(self, request):
        http_info = self._list_network_quality_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_network_quality_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/mmc/cqs/media/qos",
            "request_type": request.__class__.__name__,
            "response_type": "ListNetworkQualityResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conferenceid' in local_var_params:
            query_params.append(('conferenceid', local_var_params['conferenceid']))
        if 'appid' in local_var_params:
            query_params.append(('appid', local_var_params['appid']))
        if 'confuuid' in local_var_params:
            query_params.append(('confuuid', local_var_params['confuuid']))

        header_params = {}
        if 'conf_token' in local_var_params:
            header_params['confToken'] = local_var_params['conf_token']

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

    def list_ongoing_webinars(self, request):
        r"""查询正在召开的网络研讨会列表

        该接口用于查询正在召开的网络研讨会。管理员可查询企业内正在召开网络研讨会，非管理员可查询自己预订的正在召开的网络研讨会。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOngoingWebinars
        :type request: :class:`huaweicloudsdkmeeting.v1.ListOngoingWebinarsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ListOngoingWebinarsResponse`
        """
        http_info = self._list_ongoing_webinars_http_info(request)
        return self._call_api(**http_info)

    def list_ongoing_webinars_invoker(self, request):
        http_info = self._list_ongoing_webinars_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ongoing_webinars_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/wss/webinar/open/conferences/ongoing",
            "request_type": request.__class__.__name__,
            "response_type": "ListOngoingWebinarsResponse"
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
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'sort_type' in local_var_params:
            query_params.append(('sortType', local_var_params['sort_type']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def list_online_conf_attendee(self, request):
        r"""查询指定会议的在线与会者信息

        该接口用于查询指定会议的在线与会者信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOnlineConfAttendee
        :type request: :class:`huaweicloudsdkmeeting.v1.ListOnlineConfAttendeeRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ListOnlineConfAttendeeResponse`
        """
        http_info = self._list_online_conf_attendee_http_info(request)
        return self._call_api(**http_info)

    def list_online_conf_attendee_invoker(self, request):
        http_info = self._list_online_conf_attendee_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_online_conf_attendee_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/mmc/management/conferences/online/conf-attendee",
            "request_type": request.__class__.__name__,
            "response_type": "ListOnlineConfAttendeeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conf_id' in local_var_params:
            query_params.append(('conf_id', local_var_params['conf_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('search_key', local_var_params['search_key']))

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

    def list_up_coming_webinars(self, request):
        r"""查询即将召开的网络研讨会列表

        该接口用于查询即将召开的网络研讨会。管理员可查询企业内即将召开网络研讨会，非管理员可查询自己预订的即将召开的网络研讨会。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUpComingWebinars
        :type request: :class:`huaweicloudsdkmeeting.v1.ListUpComingWebinarsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ListUpComingWebinarsResponse`
        """
        http_info = self._list_up_coming_webinars_http_info(request)
        return self._call_api(**http_info)

    def list_up_coming_webinars_invoker(self, request):
        http_info = self._list_up_coming_webinars_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_up_coming_webinars_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/wss/webinar/open/conferences/upcoming",
            "request_type": request.__class__.__name__,
            "response_type": "ListUpComingWebinarsResponse"
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
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'sort_type' in local_var_params:
            query_params.append(('sortType', local_var_params['sort_type']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def live(self, request):
        r"""启停会议直播

        该接口用于启动或停止会议直播。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for Live
        :type request: :class:`huaweicloudsdkmeeting.v1.LiveRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.LiveResponse`
        """
        http_info = self._live_http_info(request)
        return self._call_api(**http_info)

    def live_invoker(self, request):
        http_info = self._live_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _live_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/live",
            "request_type": request.__class__.__name__,
            "response_type": "LiveResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def lock_meeting(self, request):
        r"""锁定会议

        该接口用于锁定或解锁会议。锁定会议后，不允许新的来宾主动加入会议。会议锁定后使用主持人密码/主持人链接加入会议或者主持人邀请来宾不受影响。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for LockMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.LockMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.LockMeetingResponse`
        """
        http_info = self._lock_meeting_http_info(request)
        return self._call_api(**http_info)

    def lock_meeting_invoker(self, request):
        http_info = self._lock_meeting_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _lock_meeting_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/lock",
            "request_type": request.__class__.__name__,
            "response_type": "LockMeetingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def lock_view(self, request):
        r"""锁定会场视频源

        该接口用于锁定或者解锁某在线会场的视频源。只适用于专业会议终端（如TE系列等）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for LockView
        :type request: :class:`huaweicloudsdkmeeting.v1.LockViewRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.LockViewResponse`
        """
        http_info = self._lock_view_http_info(request)
        return self._call_api(**http_info)

    def lock_view_invoker(self, request):
        http_info = self._lock_view_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _lock_view_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/lockView",
            "request_type": request.__class__.__name__,
            "response_type": "LockViewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'participant_id' in local_var_params:
            query_params.append(('participantID', local_var_params['participant_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def move_to_waiting_room(self, request):
        r"""移入等候室

        该接口用于将会中的指定与会者移入到等候室。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for MoveToWaitingRoom
        :type request: :class:`huaweicloudsdkmeeting.v1.MoveToWaitingRoomRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.MoveToWaitingRoomResponse`
        """
        http_info = self._move_to_waiting_room_http_info(request)
        return self._call_api(**http_info)

    def move_to_waiting_room_invoker(self, request):
        http_info = self._move_to_waiting_room_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _move_to_waiting_room_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/moveToWaitingRoom",
            "request_type": request.__class__.__name__,
            "response_type": "MoveToWaitingRoomResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def mute_meeting(self, request):
        r"""全场静音

        该接口用于设置整个会议所有与会者（主持人除外）的静音/取消静音状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for MuteMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.MuteMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.MuteMeetingResponse`
        """
        http_info = self._mute_meeting_http_info(request)
        return self._call_api(**http_info)

    def mute_meeting_invoker(self, request):
        http_info = self._mute_meeting_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _mute_meeting_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/mute",
            "request_type": request.__class__.__name__,
            "response_type": "MuteMeetingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def mute_participant(self, request):
        r"""静音与会者

        该接口用于设置指定与会者静音/取消静音状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for MuteParticipant
        :type request: :class:`huaweicloudsdkmeeting.v1.MuteParticipantRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.MuteParticipantResponse`
        """
        http_info = self._mute_participant_http_info(request)
        return self._call_api(**http_info)

    def mute_participant_invoker(self, request):
        http_info = self._mute_participant_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _mute_participant_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/participants/mute",
            "request_type": request.__class__.__name__,
            "response_type": "MuteParticipantResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'participant_id' in local_var_params:
            query_params.append(('participantID', local_var_params['participant_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def pause_conference(self, request):
        r"""主持人暂停/取消暂停会议

        主持人通过接口控制暂停/取消暂停。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PauseConference
        :type request: :class:`huaweicloudsdkmeeting.v1.PauseConferenceRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.PauseConferenceResponse`
        """
        http_info = self._pause_conference_http_info(request)
        return self._call_api(**http_info)

    def pause_conference_invoker(self, request):
        http_info = self._pause_conference_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _pause_conference_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/pause",
            "request_type": request.__class__.__name__,
            "response_type": "PauseConferenceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def prolong_meeting(self, request):
        r"""延长会议

        该接口用于延长会议时间。默认会议自动延长。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ProlongMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.ProlongMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ProlongMeetingResponse`
        """
        http_info = self._prolong_meeting_http_info(request)
        return self._call_api(**http_info)

    def prolong_meeting_invoker(self, request):
        http_info = self._prolong_meeting_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _prolong_meeting_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/duration",
            "request_type": request.__class__.__name__,
            "response_type": "ProlongMeetingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def record(self, request):
        r"""启停会议录制

        该接口用于启动或停止会议云录制。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for Record
        :type request: :class:`huaweicloudsdkmeeting.v1.RecordRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.RecordResponse`
        """
        http_info = self._record_http_info(request)
        return self._call_api(**http_info)

    def record_invoker(self, request):
        http_info = self._record_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _record_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/record",
            "request_type": request.__class__.__name__,
            "response_type": "RecordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def rename_participant(self, request):
        r"""重命名与会者

        重命名某个与会者。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RenameParticipant
        :type request: :class:`huaweicloudsdkmeeting.v1.RenameParticipantRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.RenameParticipantResponse`
        """
        http_info = self._rename_participant_http_info(request)
        return self._call_api(**http_info)

    def rename_participant_invoker(self, request):
        http_info = self._rename_participant_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _rename_participant_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/participants/name",
            "request_type": request.__class__.__name__,
            "response_type": "RenameParticipantResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def reset_activecode(self, request):
        r"""企业管理员通过sn重置激活码

        当硬终端激活码失效时，企业管理员可以通过该接口重置激活码，使用重新获取的激活码激活终端，每24小时可重新激活5次。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetActivecode
        :type request: :class:`huaweicloudsdkmeeting.v1.ResetActivecodeRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ResetActivecodeResponse`
        """
        http_info = self._reset_activecode_http_info(request)
        return self._call_api(**http_info)

    def reset_activecode_invoker(self, request):
        http_info = self._reset_activecode_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_activecode_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/dcs/corp/device/{sn}/activecode",
            "request_type": request.__class__.__name__,
            "response_type": "ResetActivecodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sn' in local_var_params:
            path_params['sn'] = local_var_params['sn']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def reset_app_key(self, request):
        r"""重置企业应用appkey

        企业默认管理员重置企业应用appkey
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetAppKey
        :type request: :class:`huaweicloudsdkmeeting.v1.ResetAppKeyRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ResetAppKeyResponse`
        """
        http_info = self._reset_app_key_http_info(request)
        return self._call_api(**http_info)

    def reset_app_key_invoker(self, request):
        http_info = self._reset_app_key_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_app_key_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/usg/acs/corp/app/{app_id}/reset",
            "request_type": request.__class__.__name__,
            "response_type": "ResetAppKeyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def reset_pwd(self, request):
        r"""用户重置密码

        该接口提供给用户重置密码功能，服务器收到请求，重新设置用户密码并返回结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetPwd
        :type request: :class:`huaweicloudsdkmeeting.v1.ResetPwdRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ResetPwdResponse`
        """
        http_info = self._reset_pwd_http_info(request)
        return self._call_api(**http_info)

    def reset_pwd_invoker(self, request):
        http_info = self._reset_pwd_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_pwd_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/usg/acs/password/reset",
            "request_type": request.__class__.__name__,
            "response_type": "ResetPwdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def reset_pwd_by_admin(self, request):
        r"""企业管理员重置企业成员密码

        企业管理员通过该接口提供企业管理员重置企业成员密码的功能。当服务器收到重置密码的请求时，发送新的密码到企业成员的邮箱或者短信，并返回结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetPwdByAdmin
        :type request: :class:`huaweicloudsdkmeeting.v1.ResetPwdByAdminRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ResetPwdByAdminResponse`
        """
        http_info = self._reset_pwd_by_admin_http_info(request)
        return self._call_api(**http_info)

    def reset_pwd_by_admin_invoker(self, request):
        http_info = self._reset_pwd_by_admin_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_pwd_by_admin_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/usg/acs/password/admin/reset",
            "request_type": request.__class__.__name__,
            "response_type": "ResetPwdByAdminResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def reset_vision_active_code(self, request):
        r"""企业管理员重置帐号的激活码

        企业管理员重置帐号的激活码，重置后，原设备直接解绑，必须重新激活使用,若手机邮箱不填，则不会发送新的激活码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetVisionActiveCode
        :type request: :class:`huaweicloudsdkmeeting.v1.ResetVisionActiveCodeRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ResetVisionActiveCodeResponse`
        """
        http_info = self._reset_vision_active_code_http_info(request)
        return self._call_api(**http_info)

    def reset_vision_active_code_invoker(self, request):
        http_info = self._reset_vision_active_code_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_vision_active_code_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/usg/dcs/corp/vision/activecode/{account}/reset",
            "request_type": request.__class__.__name__,
            "response_type": "ResetVisionActiveCodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'account' in local_var_params:
            path_params['account'] = local_var_params['account']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def resume_simultaneous_interpretation(self, request):
        r"""开启/关闭同声传译

        该接口用于会议主席可以通过该接口开启/关闭同声传译。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResumeSimultaneousInterpretation
        :type request: :class:`huaweicloudsdkmeeting.v1.ResumeSimultaneousInterpretationRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ResumeSimultaneousInterpretationResponse`
        """
        http_info = self._resume_simultaneous_interpretation_http_info(request)
        return self._call_api(**http_info)

    def resume_simultaneous_interpretation_invoker(self, request):
        http_info = self._resume_simultaneous_interpretation_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _resume_simultaneous_interpretation_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/simultaneousInterpretation",
            "request_type": request.__class__.__name__,
            "response_type": "ResumeSimultaneousInterpretationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def rollcall_participant(self, request):
        r"""点名会场

        该接口用于点名指定与会者。点名会场的效果是除了主持人外，点名与会者为非静音状态，未点名的与会者统一为静音状态。同一时间，只允许一个与会者被点名。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RollcallParticipant
        :type request: :class:`huaweicloudsdkmeeting.v1.RollcallParticipantRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.RollcallParticipantResponse`
        """
        http_info = self._rollcall_participant_http_info(request)
        return self._call_api(**http_info)

    def rollcall_participant_invoker(self, request):
        http_info = self._rollcall_participant_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _rollcall_participant_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/participants/rollCall",
            "request_type": request.__class__.__name__,
            "response_type": "RollcallParticipantResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'participant_id' in local_var_params:
            query_params.append(('participantID', local_var_params['participant_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def save_layout(self, request):
        r"""保存多画面布局

        该接口用于保存多画面布局。保存的多画面布局，只能在当前会议使用，会议结束后，保存的多画面布局就会释放。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SaveLayout
        :type request: :class:`huaweicloudsdkmeeting.v1.SaveLayoutRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SaveLayoutResponse`
        """
        http_info = self._save_layout_http_info(request)
        return self._call_api(**http_info)

    def save_layout_invoker(self, request):
        http_info = self._save_layout_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _save_layout_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/layOut",
            "request_type": request.__class__.__name__,
            "response_type": "SaveLayoutResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def search_attendance_records_of_his_meeting(self, request):
        r"""查询历史会议的与会者记录

        该接口用于查询指定历史会议的与会者记录。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchAttendanceRecordsOfHisMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchAttendanceRecordsOfHisMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchAttendanceRecordsOfHisMeetingResponse`
        """
        http_info = self._search_attendance_records_of_his_meeting_http_info(request)
        return self._call_api(**http_info)

    def search_attendance_records_of_his_meeting_invoker(self, request):
        http_info = self._search_attendance_records_of_his_meeting_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_attendance_records_of_his_meeting_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/mmc/management/conferences/history/confAttendeeRecord",
            "request_type": request.__class__.__name__,
            "response_type": "SearchAttendanceRecordsOfHisMeetingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conf_uuid' in local_var_params:
            query_params.append(('confUUID', local_var_params['conf_uuid']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def search_corp(self, request):
        r"""SP管理员分页搜索企业

        SP管理员分页搜索企业。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchCorp
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchCorpRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchCorpResponse`
        """
        http_info = self._search_corp_http_info(request)
        return self._call_api(**http_info)

    def search_corp_invoker(self, request):
        http_info = self._search_corp_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_corp_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/dcs/sp/corp",
            "request_type": request.__class__.__name__,
            "response_type": "SearchCorpResponse"
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
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def search_corp_admins(self, request):
        r"""分页查询企业管理员

        通过该接口分页查询企业管理员。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchCorpAdmins
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchCorpAdminsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchCorpAdminsResponse`
        """
        http_info = self._search_corp_admins_http_info(request)
        return self._call_api(**http_info)

    def search_corp_admins_invoker(self, request):
        http_info = self._search_corp_admins_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_corp_admins_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/dcs/corp/admin",
            "request_type": request.__class__.__name__,
            "response_type": "SearchCorpAdminsResponse"
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
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def search_corp_dir(self, request):
        r"""查询企业通讯录

        企业用户（含管理员）通过该接口查询该企业的通讯录。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchCorpDir
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchCorpDirRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchCorpDirResponse`
        """
        http_info = self._search_corp_dir_http_info(request)
        return self._call_api(**http_info)

    def search_corp_dir_invoker(self, request):
        http_info = self._search_corp_dir_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_corp_dir_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/abs/users",
            "request_type": request.__class__.__name__,
            "response_type": "SearchCorpDirResponse"
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
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'dept_code' in local_var_params:
            query_params.append(('deptCode', local_var_params['dept_code']))
        if 'query_sub_dept' in local_var_params:
            query_params.append(('querySubDept', local_var_params['query_sub_dept']))
        if 'search_scope' in local_var_params:
            query_params.append(('searchScope', local_var_params['search_scope']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def search_corp_external_dir(self, request):
        r"""查询企业外部联系人

        企业用户（含管理员）通过该接口查询该企业的外部联系人或者个人外部联系人。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchCorpExternalDir
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchCorpExternalDirRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchCorpExternalDirResponse`
        """
        http_info = self._search_corp_external_dir_http_info(request)
        return self._call_api(**http_info)

    def search_corp_external_dir_invoker(self, request):
        http_info = self._search_corp_external_dir_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_corp_external_dir_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/abs/external-contacts",
            "request_type": request.__class__.__name__,
            "response_type": "SearchCorpExternalDirResponse"
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
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'search_scope' in local_var_params:
            query_params.append(('searchScope', local_var_params['search_scope']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def search_corp_resources(self, request):
        r"""企业管理员分页查询企业资源订单列表

        企业管理员根据条件查询企业资源订单列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchCorpResources
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchCorpResourcesRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchCorpResourcesResponse`
        """
        http_info = self._search_corp_resources_http_info(request)
        return self._call_api(**http_info)

    def search_corp_resources_invoker(self, request):
        http_info = self._search_corp_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_corp_resources_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/dcs/corp/resource-list",
            "request_type": request.__class__.__name__,
            "response_type": "SearchCorpResourcesResponse"
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
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'start_expire_date' in local_var_params:
            query_params.append(('startExpireDate', local_var_params['start_expire_date']))
        if 'end_expire_date' in local_var_params:
            query_params.append(('endExpireDate', local_var_params['end_expire_date']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'vmr_mode' in local_var_params:
            query_params.append(('vmrMode', local_var_params['vmr_mode']))
        if 'type_id' in local_var_params:
            query_params.append(('typeId', local_var_params['type_id']))
        if 'order_id' in local_var_params:
            query_params.append(('orderId', local_var_params['order_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def search_corp_vmr(self, request):
        r"""企业管理员分页查询企业云会议室

        企业管理员通过该接口分页查询企业的云会议室。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchCorpVmr
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchCorpVmrRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchCorpVmrResponse`
        """
        http_info = self._search_corp_vmr_http_info(request)
        return self._call_api(**http_info)

    def search_corp_vmr_invoker(self, request):
        http_info = self._search_corp_vmr_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_corp_vmr_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/dcs/corp/vmr",
            "request_type": request.__class__.__name__,
            "response_type": "SearchCorpVmrResponse"
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
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'vmr_mode' in local_var_params:
            query_params.append(('vmrMode', local_var_params['vmr_mode']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def search_ctl_records_of_his_meeting(self, request):
        r"""查询历史会议的会控记录

        该接口用于查询指定历史会议的会控记录。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchCtlRecordsOfHisMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchCtlRecordsOfHisMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchCtlRecordsOfHisMeetingResponse`
        """
        http_info = self._search_ctl_records_of_his_meeting_http_info(request)
        return self._call_api(**http_info)

    def search_ctl_records_of_his_meeting_invoker(self, request):
        http_info = self._search_ctl_records_of_his_meeting_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_ctl_records_of_his_meeting_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/mmc/management/conferences/history/confCtlRecord",
            "request_type": request.__class__.__name__,
            "response_type": "SearchCtlRecordsOfHisMeetingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conf_uuid' in local_var_params:
            query_params.append(('confUUID', local_var_params['conf_uuid']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def search_department_by_name(self, request):
        r"""按名称查询所有的部门

        企业管理员通过该接口按名称查询所有的部门。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchDepartmentByName
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchDepartmentByNameRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchDepartmentByNameResponse`
        """
        http_info = self._search_department_by_name_http_info(request)
        return self._call_api(**http_info)

    def search_department_by_name_invoker(self, request):
        http_info = self._search_department_by_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_department_by_name_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/dcs/member/dept",
            "request_type": request.__class__.__name__,
            "response_type": "SearchDepartmentByNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'dept_name' in local_var_params:
            query_params.append(('deptName', local_var_params['dept_name']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def search_devices(self, request):
        r"""分页查询终端

        企业管理员通过该接口分页查询专业会议终端信息。
        &gt; 如果需要查询Ideahub、SmartRooms、智慧屏TV请使用[[分页查询用户](https://support.huaweicloud.com/api-meeting/meeting_21_0071.html)](tag:hws)[[分页查询用户](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0071.html)](tag:hk)接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchDevices
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchDevicesRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchDevicesResponse`
        """
        http_info = self._search_devices_http_info(request)
        return self._call_api(**http_info)

    def search_devices_invoker(self, request):
        http_info = self._search_devices_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_devices_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/dcs/corp/device",
            "request_type": request.__class__.__name__,
            "response_type": "SearchDevicesResponse"
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
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'model' in local_var_params:
            query_params.append(('model', local_var_params['model']))
        if 'dept_code' in local_var_params:
            query_params.append(('deptCode', local_var_params['dept_code']))
        if 'enable_sub_dept' in local_var_params:
            query_params.append(('enableSubDept', local_var_params['enable_sub_dept']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def search_his_meetings(self, request):
        r"""查询历史会议列表

        该接口用于查询已经结束的会议。管理员可以查询本企业内所有的历史会议，普通用户仅能查询自己创建或者被邀请的历史会议。不带查询参数时，默认查询权限范围内的历史会议。
        &gt; * 普通用户如果只是通过会议ID或者会议链接接入会议，不是预定者会前邀请或者会中主持人邀请的，则历史会议中无法查到
        &gt; * 如果同一个会议召开并结束多次，则会产生多条历史会议（会议ID相同，会议UUID不同）
        &gt; * 历史会议记录默认保留6个月，最长保留12个月。保留时间管理员可在“会议设置”的“历史会议留存时间”中修改
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchHisMeetings
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchHisMeetingsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchHisMeetingsResponse`
        """
        http_info = self._search_his_meetings_http_info(request)
        return self._call_api(**http_info)

    def search_his_meetings_invoker(self, request):
        http_info = self._search_his_meetings_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_his_meetings_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/mmc/management/conferences/history",
            "request_type": request.__class__.__name__,
            "response_type": "SearchHisMeetingsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'query_all' in local_var_params:
            query_params.append(('queryAll', local_var_params['query_all']))
        if 'start_date' in local_var_params:
            query_params.append(('startDate', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('endDate', local_var_params['end_date']))
        if 'sort_type' in local_var_params:
            query_params.append(('sortType', local_var_params['sort_type']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

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

    def search_materials(self, request):
        r"""分页查询信息窗素材

        分页查询信息窗素材。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchMaterials
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchMaterialsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchMaterialsResponse`
        """
        http_info = self._search_materials_http_info(request)
        return self._call_api(**http_info)

    def search_materials_invoker(self, request):
        http_info = self._search_materials_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_materials_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/sss/materials",
            "request_type": request.__class__.__name__,
            "response_type": "SearchMaterialsResponse"
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
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def search_meeting_file_list(self, request):
        r"""查询会议纪要列表

        用户查询自己的会议纪要列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchMeetingFileList
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchMeetingFileListRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchMeetingFileListResponse`
        """
        http_info = self._search_meeting_file_list_http_info(request)
        return self._call_api(**http_info)

    def search_meeting_file_list_invoker(self, request):
        http_info = self._search_meeting_file_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_meeting_file_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/sss/meeting-files",
            "request_type": request.__class__.__name__,
            "response_type": "SearchMeetingFileListResponse"
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
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def search_meetings(self, request):
        r"""查询会议列表

        该接口用于查询尚未结束的会议。
        * 管理员可以查询管理权限域内所有的会议，普通用户仅能查询自己创建或者需要参加的会议。不带查询参数时，默认查询权限范围内正在召开或还未召开的会议。
        * 只能查询尚未结束的会议（既正在召开的会议和已预约还未召开的会议）。如果需要查询历史会议列表，请参考[[查询历史会议列表](https://support.huaweicloud.com/api-meeting/meeting_21_0051.html)](tag:hws)[[查询历史会议列表](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0051.html)](tag:hk)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchMeetings
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchMeetingsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchMeetingsResponse`
        """
        http_info = self._search_meetings_http_info(request)
        return self._call_api(**http_info)

    def search_meetings_invoker(self, request):
        http_info = self._search_meetings_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_meetings_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/mmc/management/conferences",
            "request_type": request.__class__.__name__,
            "response_type": "SearchMeetingsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'query_all' in local_var_params:
            query_params.append(('queryAll', local_var_params['query_all']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'query_conf_mode' in local_var_params:
            query_params.append(('queryConfMode', local_var_params['query_conf_mode']))
        if 'sort_type' in local_var_params:
            query_params.append(('sortType', local_var_params['sort_type']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

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

    def search_member_vmr(self, request):
        r"""普通用户分页查询云会议室及个人会议ID

        企业用户通过该接口查询个人已分配的云会议室及个人会议ID。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchMemberVmr
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchMemberVmrRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchMemberVmrResponse`
        """
        http_info = self._search_member_vmr_http_info(request)
        return self._call_api(**http_info)

    def search_member_vmr_invoker(self, request):
        http_info = self._search_member_vmr_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_member_vmr_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/dcs/member/vmr",
            "request_type": request.__class__.__name__,
            "response_type": "SearchMemberVmrResponse"
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
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'special_vmr' in local_var_params:
            query_params.append(('specialVmr', local_var_params['special_vmr']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def search_online_meetings(self, request):
        r"""查询在线会议列表

        该接口用于查询正在召开的会议列表。管理员可以查询本企业内所有在线会议，普通用户仅能查询当前自己帐号创建或者需要参加的在线会议。不带查询参数时，默认查询权限范围内的在线会议，按开始时间升序排列。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchOnlineMeetings
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchOnlineMeetingsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchOnlineMeetingsResponse`
        """
        http_info = self._search_online_meetings_http_info(request)
        return self._call_api(**http_info)

    def search_online_meetings_invoker(self, request):
        http_info = self._search_online_meetings_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_online_meetings_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/mmc/management/conferences/online",
            "request_type": request.__class__.__name__,
            "response_type": "SearchOnlineMeetingsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'query_all' in local_var_params:
            query_params.append(('queryAll', local_var_params['query_all']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

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

    def search_programs(self, request):
        r"""查询信息窗节目

        获取信息窗节目。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchPrograms
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchProgramsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchProgramsResponse`
        """
        http_info = self._search_programs_http_info(request)
        return self._call_api(**http_info)

    def search_programs_invoker(self, request):
        http_info = self._search_programs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_programs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/sss/programs",
            "request_type": request.__class__.__name__,
            "response_type": "SearchProgramsResponse"
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
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def search_publications(self, request):
        r"""查询信息窗发布

        获取信息窗发布。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchPublications
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchPublicationsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchPublicationsResponse`
        """
        http_info = self._search_publications_http_info(request)
        return self._call_api(**http_info)

    def search_publications_invoker(self, request):
        http_info = self._search_publications_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_publications_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/sss/publications",
            "request_type": request.__class__.__name__,
            "response_type": "SearchPublicationsResponse"
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
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def search_recordings(self, request):
        r"""查询录制列表

        该接口用于查询会议录制列表。管理员可以查询本企业内所有的录制，普通用户仅能查询自己创建的会议的录制。不带查询参数时，默认查询权限范围内的录制。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchRecordings
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchRecordingsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchRecordingsResponse`
        """
        http_info = self._search_recordings_http_info(request)
        return self._call_api(**http_info)

    def search_recordings_invoker(self, request):
        http_info = self._search_recordings_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_recordings_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/mmc/management/record/files",
            "request_type": request.__class__.__name__,
            "response_type": "SearchRecordingsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'query_all' in local_var_params:
            query_params.append(('queryAll', local_var_params['query_all']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'start_date' in local_var_params:
            query_params.append(('startDate', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('endDate', local_var_params['end_date']))
        if 'sort_type' in local_var_params:
            query_params.append(('sortType', local_var_params['sort_type']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

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

    def search_resource(self, request):
        r"""SP管理员根据分页查询企业资源

        SP根据条件查询企业的资源项。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchResource
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchResourceRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchResourceResponse`
        """
        http_info = self._search_resource_http_info(request)
        return self._call_api(**http_info)

    def search_resource_invoker(self, request):
        http_info = self._search_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_resource_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/dcs/sp/corp/{corp_id}/resource",
            "request_type": request.__class__.__name__,
            "response_type": "SearchResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'corp_id' in local_var_params:
            path_params['corp_id'] = local_var_params['corp_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'start_expire_date' in local_var_params:
            query_params.append(('startExpireDate', local_var_params['start_expire_date']))
        if 'end_expire_date' in local_var_params:
            query_params.append(('endExpireDate', local_var_params['end_expire_date']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'type_id' in local_var_params:
            query_params.append(('typeId', local_var_params['type_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def search_resource_op_record(self, request):
        r"""SP管理员分页查询企业资源操作记录

        SP根据根据条件查询企业的资源操作记录，支持根据resourceId模糊搜索。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchResourceOpRecord
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchResourceOpRecordRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchResourceOpRecordResponse`
        """
        http_info = self._search_resource_op_record_http_info(request)
        return self._call_api(**http_info)

    def search_resource_op_record_invoker(self, request):
        http_info = self._search_resource_op_record_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_resource_op_record_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/dcs/sp/corp/{corp_id}/resource-record",
            "request_type": request.__class__.__name__,
            "response_type": "SearchResourceOpRecordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'corp_id' in local_var_params:
            path_params['corp_id'] = local_var_params['corp_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'start_expire_date' in local_var_params:
            query_params.append(('startExpireDate', local_var_params['start_expire_date']))
        if 'end_expire_date' in local_var_params:
            query_params.append(('endExpireDate', local_var_params['end_expire_date']))
        if 'start_operate_date' in local_var_params:
            query_params.append(('startOperateDate', local_var_params['start_operate_date']))
        if 'end_operate_date' in local_var_params:
            query_params.append(('endOperateDate', local_var_params['end_operate_date']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'type_id' in local_var_params:
            query_params.append(('typeId', local_var_params['type_id']))
        if 'operate_type' in local_var_params:
            query_params.append(('operateType', local_var_params['operate_type']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def search_users(self, request):
        r"""分页查询用户

        企业管理员通过该接口分页查询企业用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchUsers
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchUsersRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchUsersResponse`
        """
        http_info = self._search_users_http_info(request)
        return self._call_api(**http_info)

    def search_users_invoker(self, request):
        http_info = self._search_users_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_users_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/dcs/corp/member",
            "request_type": request.__class__.__name__,
            "response_type": "SearchUsersResponse"
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
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'sort_field' in local_var_params:
            query_params.append(('sortField', local_var_params['sort_field']))
        if 'is_asc' in local_var_params:
            query_params.append(('isAsc', local_var_params['is_asc']))
        if 'dept_code' in local_var_params:
            query_params.append(('deptCode', local_var_params['dept_code']))
        if 'enable_sub_dept' in local_var_params:
            query_params.append(('enableSubDept', local_var_params['enable_sub_dept']))
        if 'admin_type' in local_var_params:
            query_params.append(('adminType', local_var_params['admin_type']))
        if 'enable_room' in local_var_params:
            query_params.append(('enableRoom', local_var_params['enable_room']))
        if 'user_type' in local_var_params:
            query_params.append(('userType', local_var_params['user_type']))
            collection_formats['userType'] = 'csv'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'contains_un_active' in local_var_params:
            query_params.append(('containsUnActive', local_var_params['contains_un_active']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def search_vision_active_code(self, request):
        r"""企业管理员分页查询激活码

        企业管理员分页查询激活码，支持激活码、终端名称模糊查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchVisionActiveCode
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchVisionActiveCodeRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchVisionActiveCodeResponse`
        """
        http_info = self._search_vision_active_code_http_info(request)
        return self._call_api(**http_info)

    def search_vision_active_code_invoker(self, request):
        http_info = self._search_vision_active_code_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_vision_active_code_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/dcs/corp/vision/activecode",
            "request_type": request.__class__.__name__,
            "response_type": "SearchVisionActiveCodeResponse"
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
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'dev_type' in local_var_params:
            query_params.append(('devType', local_var_params['dev_type']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def send_slide_verify_code(self, request):
        r"""发送滑块验证码

        该接口提供发送滑块验证码。服务器收到请求，返回抠图以及抠图后的原图等结果。需要在前台界面显示出抠图以及抠图后的原图，用户通过滑块操作来匹配图形。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SendSlideVerifyCode
        :type request: :class:`huaweicloudsdkmeeting.v1.SendSlideVerifyCodeRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SendSlideVerifyCodeResponse`
        """
        http_info = self._send_slide_verify_code_http_info(request)
        return self._call_api(**http_info)

    def send_slide_verify_code_invoker(self, request):
        http_info = self._send_slide_verify_code_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _send_slide_verify_code_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/acs/auth/slideverifycode/send",
            "request_type": request.__class__.__name__,
            "response_type": "SendSlideVerifyCodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def send_veri_code_for_change_pwd(self, request):
        r"""发送验证码

        该接口提供发送验证码，服务器收到请求，发送验证码到邮箱或者短信并返回结果。用户在前台界面通过滑块验证后，再进行发送验证码操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SendVeriCodeForChangePwd
        :type request: :class:`huaweicloudsdkmeeting.v1.SendVeriCodeForChangePwdRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SendVeriCodeForChangePwdResponse`
        """
        http_info = self._send_veri_code_for_change_pwd_http_info(request)
        return self._call_api(**http_info)

    def send_veri_code_for_change_pwd_invoker(self, request):
        http_info = self._send_veri_code_for_change_pwd_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _send_veri_code_for_change_pwd_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/acs/verifycode/send",
            "request_type": request.__class__.__name__,
            "response_type": "SendVeriCodeForChangePwdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def send_veri_code_for_update_user_info(self, request):
        r"""获取验证码

        修改用户手机或邮箱时，需要获取验证码。企业用户通过该接口获取验证码，系统会向用户的手机或邮箱发送，验证码1分钟内有效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SendVeriCodeForUpdateUserInfo
        :type request: :class:`huaweicloudsdkmeeting.v1.SendVeriCodeForUpdateUserInfoRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SendVeriCodeForUpdateUserInfoResponse`
        """
        http_info = self._send_veri_code_for_update_user_info_http_info(request)
        return self._call_api(**http_info)

    def send_veri_code_for_update_user_info_invoker(self, request):
        http_info = self._send_veri_code_for_update_user_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _send_veri_code_for_update_user_info_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/dcs/member/verification-code",
            "request_type": request.__class__.__name__,
            "response_type": "SendVeriCodeForUpdateUserInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def set_attendee_lan_channel(self, request):
        r"""设置普通与会人的语言频道

        主持人通过该接口设置某些普通与会者(包括主持人)加入哪个语言频道。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetAttendeeLanChannel
        :type request: :class:`huaweicloudsdkmeeting.v1.SetAttendeeLanChannelRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetAttendeeLanChannelResponse`
        """
        http_info = self._set_attendee_lan_channel_http_info(request)
        return self._call_api(**http_info)

    def set_attendee_lan_channel_invoker(self, request):
        http_info = self._set_attendee_lan_channel_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_attendee_lan_channel_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/setAttendeeLanChannel",
            "request_type": request.__class__.__name__,
            "response_type": "SetAttendeeLanChannelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def set_cohost(self, request):
        r"""申请联席主持人

        该接口用于设置联席主持人或释放联席主持人。只能将来宾设置为联席主持人。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetCohost
        :type request: :class:`huaweicloudsdkmeeting.v1.SetCohostRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetCohostResponse`
        """
        http_info = self._set_cohost_http_info(request)
        return self._call_api(**http_info)

    def set_cohost_invoker(self, request):
        http_info = self._set_cohost_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_cohost_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/participants/cohost",
            "request_type": request.__class__.__name__,
            "response_type": "SetCohostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'participant_id' in local_var_params:
            query_params.append(('participantID', local_var_params['participant_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def set_custom_multi_picture(self, request):
        r"""设置自定义多画面

        该接口用于设置会中多画面。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetCustomMultiPicture
        :type request: :class:`huaweicloudsdkmeeting.v1.SetCustomMultiPictureRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetCustomMultiPictureResponse`
        """
        http_info = self._set_custom_multi_picture_http_info(request)
        return self._call_api(**http_info)

    def set_custom_multi_picture_invoker(self, request):
        http_info = self._set_custom_multi_picture_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_custom_multi_picture_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/display/customMultiPicture",
            "request_type": request.__class__.__name__,
            "response_type": "SetCustomMultiPictureResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def set_host_view(self, request):
        r"""主持人选看

        该接口用于主持人轮询、主持人选看多画面、主持人选看会场操作。只适用于专业会议终端（如TE系列等）为主持人的场景。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetHostView
        :type request: :class:`huaweicloudsdkmeeting.v1.SetHostViewRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetHostViewResponse`
        """
        http_info = self._set_host_view_http_info(request)
        return self._call_api(**http_info)

    def set_host_view_invoker(self, request):
        http_info = self._set_host_view_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_host_view_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/chairView",
            "request_type": request.__class__.__name__,
            "response_type": "SetHostViewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def set_interpreter_group(self, request):
        r"""设置传译组

        主持人通过该接口设置传译组，每个传译组支持两种语言，传译组内支持多个传译员。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetInterpreterGroup
        :type request: :class:`huaweicloudsdkmeeting.v1.SetInterpreterGroupRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetInterpreterGroupResponse`
        """
        http_info = self._set_interpreter_group_http_info(request)
        return self._call_api(**http_info)

    def set_interpreter_group_invoker(self, request):
        http_info = self._set_interpreter_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_interpreter_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/interpreterGroup",
            "request_type": request.__class__.__name__,
            "response_type": "SetInterpreterGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def set_mmr_live(self, request):
        r"""启动/停止Mmr会议直播

        使用场景：会议主持人可以通过该接口启动/停止Mmr会议直播 功能描述：提供启动/停止会议Mmr直播的能力
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetMmrLive
        :type request: :class:`huaweicloudsdkmeeting.v1.SetMmrLiveRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetMmrLiveResponse`
        """
        http_info = self._set_mmr_live_http_info(request)
        return self._call_api(**http_info)

    def set_mmr_live_invoker(self, request):
        http_info = self._set_mmr_live_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_mmr_live_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/mmrLive",
            "request_type": request.__class__.__name__,
            "response_type": "SetMmrLiveResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def set_mmr_record(self, request):
        r"""启动/暂停/停止mmr会议录制

        使用场景：管理员或UC账号主席可以通过该接口启动/停止mmr会议录制 功能描述：提供启动/暂停/停止MMR会议录制的能力
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetMmrRecord
        :type request: :class:`huaweicloudsdkmeeting.v1.SetMmrRecordRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetMmrRecordResponse`
        """
        http_info = self._set_mmr_record_http_info(request)
        return self._call_api(**http_info)

    def set_mmr_record_invoker(self, request):
        http_info = self._set_mmr_record_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_mmr_record_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/mmrRecord",
            "request_type": request.__class__.__name__,
            "response_type": "SetMmrRecordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def set_multi_picture(self, request):
        r"""设置多画面

        设置会议多画面。该接口废弃不用，请使用“[[设置自定义多画面](https://support.huaweicloud.com/api-meeting/meeting_21_0418.html)](tag:hws)[[设置自定义多画面](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0418.html)](tag:hk)”接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetMultiPicture
        :type request: :class:`huaweicloudsdkmeeting.v1.SetMultiPictureRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetMultiPictureResponse`
        """
        http_info = self._set_multi_picture_http_info(request)
        return self._call_api(**http_info)

    def set_multi_picture_invoker(self, request):
        http_info = self._set_multi_picture_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_multi_picture_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/display/multiPicture",
            "request_type": request.__class__.__name__,
            "response_type": "SetMultiPictureResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def set_participant_view(self, request):
        r"""会场选看

        该接口用于专业会议终端（如TE系列等）选看其他与会者。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetParticipantView
        :type request: :class:`huaweicloudsdkmeeting.v1.SetParticipantViewRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetParticipantViewResponse`
        """
        http_info = self._set_participant_view_http_info(request)
        return self._call_api(**http_info)

    def set_participant_view_invoker(self, request):
        http_info = self._set_participant_view_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_participant_view_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/partView",
            "request_type": request.__class__.__name__,
            "response_type": "SetParticipantViewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'participant_id' in local_var_params:
            query_params.append(('participantID', local_var_params['participant_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def set_profile_image(self, request):
        r"""用户设置头像

        用户设置头像
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetProfileImage
        :type request: :class:`huaweicloudsdkmeeting.v1.SetProfileImageRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetProfileImageResponse`
        """
        http_info = self._set_profile_image_http_info(request)
        return self._call_api(**http_info)

    def set_profile_image_invoker(self, request):
        http_info = self._set_profile_image_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_profile_image_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/abs/profile-images",
            "request_type": request.__class__.__name__,
            "response_type": "SetProfileImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def set_role(self, request):
        r"""申请主持人

        该接口用于设置主持人或释放主持人。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetRole
        :type request: :class:`huaweicloudsdkmeeting.v1.SetRoleRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetRoleResponse`
        """
        http_info = self._set_role_http_info(request)
        return self._call_api(**http_info)

    def set_role_invoker(self, request):
        http_info = self._set_role_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_role_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/participants/role",
            "request_type": request.__class__.__name__,
            "response_type": "SetRoleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'participant_id' in local_var_params:
            query_params.append(('participantID', local_var_params['participant_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def set_sso_config(self, request):
        r"""设置SSO登录配置

        该接口用于设置SSO登录的鉴权配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetSsoConfig
        :type request: :class:`huaweicloudsdkmeeting.v1.SetSsoConfigRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetSsoConfigResponse`
        """
        http_info = self._set_sso_config_http_info(request)
        return self._call_api(**http_info)

    def set_sso_config_invoker(self, request):
        http_info = self._set_sso_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_sso_config_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/acs/authorizeconfig",
            "request_type": request.__class__.__name__,
            "response_type": "SetSsoConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def set_user_profile_image(self, request):
        r"""企业管理员设置企业成员头像

        为企业内的用户设置头像（只允许管理员调用）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetUserProfileImage
        :type request: :class:`huaweicloudsdkmeeting.v1.SetUserProfileImageRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetUserProfileImageResponse`
        """
        http_info = self._set_user_profile_image_http_info(request)
        return self._call_api(**http_info)

    def set_user_profile_image_invoker(self, request):
        http_info = self._set_user_profile_image_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_user_profile_image_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/abs/profile-images/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "SetUserProfileImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def set_web_hook_config(self, request):
        r"""设置事件推送

        该接口用于管理员设置企业级会议事件订阅配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetWebHookConfig
        :type request: :class:`huaweicloudsdkmeeting.v1.SetWebHookConfigRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetWebHookConfigResponse`
        """
        http_info = self._set_web_hook_config_http_info(request)
        return self._call_api(**http_info)

    def set_web_hook_config_invoker(self, request):
        http_info = self._set_web_hook_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_web_hook_config_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/mmc/management/webhook/link-config",
            "request_type": request.__class__.__name__,
            "response_type": "SetWebHookConfigResponse"
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

    def show_conf_org(self, request):
        r"""SP管理员查询会议归属企业

        SP管理员根据会议ID查询该会议归属的企业ID。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowConfOrg
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowConfOrgRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowConfOrgResponse`
        """
        http_info = self._show_conf_org_http_info(request)
        return self._call_api(**http_info)

    def show_conf_org_invoker(self, request):
        http_info = self._show_conf_org_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_conf_org_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/mmc/management/conferences/confOrg",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConfOrgResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

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

    def show_corp(self, request):
        r"""SP管理员查询企业

        获取企业。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCorp
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowCorpRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowCorpResponse`
        """
        http_info = self._show_corp_http_info(request)
        return self._call_api(**http_info)

    def show_corp_invoker(self, request):
        http_info = self._show_corp_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_corp_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/dcs/sp/corp/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCorpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def show_corp_admin(self, request):
        r"""查询企业管理员

        通过该接口查询企业管理员。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCorpAdmin
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowCorpAdminRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowCorpAdminResponse`
        """
        http_info = self._show_corp_admin_http_info(request)
        return self._call_api(**http_info)

    def show_corp_admin_invoker(self, request):
        http_info = self._show_corp_admin_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_corp_admin_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/dcs/corp/admin/{account}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCorpAdminResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'account' in local_var_params:
            path_params['account'] = local_var_params['account']

        query_params = []
        if 'account_type' in local_var_params:
            query_params.append(('accountType', local_var_params['account_type']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def show_corp_basic_info(self, request):
        r"""企业管理员查询企业注册信息

        企业管理员通过该接口查询企业注册信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCorpBasicInfo
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowCorpBasicInfoRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowCorpBasicInfoResponse`
        """
        http_info = self._show_corp_basic_info_http_info(request)
        return self._call_api(**http_info)

    def show_corp_basic_info_invoker(self, request):
        http_info = self._show_corp_basic_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_corp_basic_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/dcs/corp",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCorpBasicInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def show_corp_resource(self, request):
        r"""企业管理员查询企业内资源及业务权限

        企业管理员通过该接口查询企业内资源及业务权限，包括查询已使用的资源情况。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCorpResource
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowCorpResourceRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowCorpResourceResponse`
        """
        http_info = self._show_corp_resource_http_info(request)
        return self._call_api(**http_info)

    def show_corp_resource_invoker(self, request):
        http_info = self._show_corp_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_corp_resource_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/dcs/corp/resource",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCorpResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def show_department(self, request):
        r"""通过部门编码查询部门信息

        通过部门编码查询部门信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDepartment
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowDepartmentRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowDepartmentResponse`
        """
        http_info = self._show_department_http_info(request)
        return self._call_api(**http_info)

    def show_department_invoker(self, request):
        http_info = self._show_department_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_department_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/abs/departments/{dept_code}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDepartmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dept_code' in local_var_params:
            path_params['dept_code'] = local_var_params['dept_code']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def show_dept_and_child_dept(self, request):
        r"""查询部门及其一级子部门列表

        企业管理员通过该接口查询部门及其一级子部门列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeptAndChildDept
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowDeptAndChildDeptRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowDeptAndChildDeptResponse`
        """
        http_info = self._show_dept_and_child_dept_http_info(request)
        return self._call_api(**http_info)

    def show_dept_and_child_dept_invoker(self, request):
        http_info = self._show_dept_and_child_dept_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_dept_and_child_dept_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/dcs/member/dept/{dept_code}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeptAndChildDeptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dept_code' in local_var_params:
            path_params['dept_code'] = local_var_params['dept_code']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def show_device_detail(self, request):
        r"""查询终端详情

        企业管理员通过该接口查询专业会议终端详情。
        &gt; 如果需要查询Ideahub、SmartRooms、智慧屏TV详情请使用[[查询用户详情](https://support.huaweicloud.com/api-meeting/meeting_21_0069.html)](tag:hws)[[查询用户详情](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0069.html)](tag:hk)接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeviceDetail
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowDeviceDetailRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowDeviceDetailResponse`
        """
        http_info = self._show_device_detail_http_info(request)
        return self._call_api(**http_info)

    def show_device_detail_invoker(self, request):
        http_info = self._show_device_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_device_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/dcs/corp/device/{sn}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeviceDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sn' in local_var_params:
            path_params['sn'] = local_var_params['sn']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def show_device_status(self, request):
        r"""查询设备状态

        调用本接口可以查询硬终端的状态。
        硬终端与发起查询请求的帐号需在同一企业下，否则会鉴权失败。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeviceStatus
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowDeviceStatusRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowDeviceStatusResponse`
        """
        http_info = self._show_device_status_http_info(request)
        return self._call_api(**http_info)

    def show_device_status_invoker(self, request):
        http_info = self._show_device_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_device_status_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/acs/ap/userstatus",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeviceStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def show_device_types(self, request):
        r"""获取所有终端类型

        企业管理员通过该接口获取所有的专业会议终端类型。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeviceTypes
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowDeviceTypesRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowDeviceTypesResponse`
        """
        http_info = self._show_device_types_http_info(request)
        return self._call_api(**http_info)

    def show_device_types_invoker(self, request):
        http_info = self._show_device_types_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_device_types_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/dcs/termdevtype",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeviceTypesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def show_his_meeting_detail(self, request):
        r"""查询历史会议详情

        该接口用户查询指定历史会议的详情。管理员可以查询本企业内所有的历史会议详情，普通用户仅能查询自己创建或者被邀请的历史会议详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowHisMeetingDetail
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowHisMeetingDetailRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowHisMeetingDetailResponse`
        """
        http_info = self._show_his_meeting_detail_http_info(request)
        return self._call_api(**http_info)

    def show_his_meeting_detail_invoker(self, request):
        http_info = self._show_his_meeting_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_his_meeting_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/mmc/management/conferences/history/confDetail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHisMeetingDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conf_uuid' in local_var_params:
            query_params.append(('confUUID', local_var_params['conf_uuid']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))

        header_params = {}
        if 'x_type' in local_var_params:
            header_params['X-Type'] = local_var_params['x_type']
        if 'x_query_type' in local_var_params:
            header_params['X-Query-Type'] = local_var_params['x_query_type']
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

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

    def show_layout(self, request):
        r"""查询多画面布局

        该接口用于查询当前会议已保存的多画面布局。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLayout
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowLayoutRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowLayoutResponse`
        """
        http_info = self._show_layout_http_info(request)
        return self._call_api(**http_info)

    def show_layout_invoker(self, request):
        http_info = self._show_layout_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_layout_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/mmc/control/conferences/layOut",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLayoutResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def show_meeting_detail(self, request):
        r"""查询会议详情

        查询偏移量
        * 管理员可以查询管理权限域内所有会议的详情，普通用户仅能查询自己创建或者需要参加的会议详情。
        * 只能查询尚未结束的会议（既正在召开的会议和已预约还未召开的会议）。如果需要查询历史会议列详情，请参考[[查询历史会议详情](https://support.huaweicloud.com/api-meeting/meeting_21_0052.html)](tag:hws)[[查询历史会议详情](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0052.html)](tag:hk)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMeetingDetail
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowMeetingDetailRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowMeetingDetailResponse`
        """
        http_info = self._show_meeting_detail_http_info(request)
        return self._call_api(**http_info)

    def show_meeting_detail_invoker(self, request):
        http_info = self._show_meeting_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_meeting_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/mmc/management/conferences/confDetail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMeetingDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))

        header_params = {}
        if 'x_type' in local_var_params:
            header_params['X-Type'] = local_var_params['x_type']
        if 'x_query_type' in local_var_params:
            header_params['X-Query-Type'] = local_var_params['x_query_type']
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

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

    def show_meeting_file(self, request):
        r"""查询会议纪要详情

        用户查询单个会议纪要详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMeetingFile
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowMeetingFileRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowMeetingFileResponse`
        """
        http_info = self._show_meeting_file_http_info(request)
        return self._call_api(**http_info)

    def show_meeting_file_invoker(self, request):
        http_info = self._show_meeting_file_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_meeting_file_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/sss/meeting-files/{file_code}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMeetingFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'file_code' in local_var_params:
            path_params['file_code'] = local_var_params['file_code']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def show_meeting_file_list(self, request):
        r"""打开会议纪要文件列表

        用户使用手机扫码后，手机端请求服务端,让服务端通知指定IdeaHub打开指定用户的会议纪要文件列表。二维码内容 ：cloudlink://cloudlink.huawei.com/h5page?action&#x3D;OPEN_MEETING_FILE_LIST&amp;key1&#x3D;value1&amp;key2&#x3D;value2 。key/value的个数可能变化，终端解析后，在发起后续请求时，将所有key/value存为map，作为入参即可。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMeetingFileList
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowMeetingFileListRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowMeetingFileListResponse`
        """
        http_info = self._show_meeting_file_list_http_info(request)
        return self._call_api(**http_info)

    def show_meeting_file_list_invoker(self, request):
        http_info = self._show_meeting_file_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_meeting_file_list_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/usg/sss/meeting-files/open-meeting-file-list",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMeetingFileListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def show_mgmt_site_status(self, request):
        r"""查询会管状态

        终端通过会控查询会管状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMgmtSiteStatus
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowMgmtSiteStatusRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowMgmtSiteStatusResponse`
        """
        http_info = self._show_mgmt_site_status_http_info(request)
        return self._call_api(**http_info)

    def show_mgmt_site_status_invoker(self, request):
        http_info = self._show_mgmt_site_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_mgmt_site_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/mmc/control/confmaintain/queryMgmtSiteStatus",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMgmtSiteStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_schema_type' in local_var_params:
            header_params['X-Schema-Type'] = local_var_params['x_schema_type']

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

    def show_my_info(self, request):
        r"""用户查询自己的信息

        企业用户通过该接口查询自己的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMyInfo
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowMyInfoRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowMyInfoResponse`
        """
        http_info = self._show_my_info_http_info(request)
        return self._call_api(**http_info)

    def show_my_info_invoker(self, request):
        http_info = self._show_my_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_my_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/dcs/member",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMyInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def show_online_meeting_detail(self, request):
        r"""查询在线会议详情

        该接口用于查询正在召开的会议详情。管理员可以查询本企业内所有的在线会议详情，普通用户仅能查询自己帐号创建或者需要参加的在线会议详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOnlineMeetingDetail
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowOnlineMeetingDetailRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowOnlineMeetingDetailResponse`
        """
        http_info = self._show_online_meeting_detail_http_info(request)
        return self._call_api(**http_info)

    def show_online_meeting_detail_invoker(self, request):
        http_info = self._show_online_meeting_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_online_meeting_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/mmc/management/conferences/online/confDetail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOnlineMeetingDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))

        header_params = {}
        if 'x_type' in local_var_params:
            header_params['X-Type'] = local_var_params['x_type']
        if 'x_query_type' in local_var_params:
            header_params['X-Query-Type'] = local_var_params['x_query_type']
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

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

    def show_org_res(self, request):
        r"""企业管理员查询企业资源使用信息

        企业管理员查询所属企业的资源使用信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOrgRes
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowOrgResRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowOrgResResponse`
        """
        http_info = self._show_org_res_http_info(request)
        return self._call_api(**http_info)

    def show_org_res_invoker(self, request):
        http_info = self._show_org_res_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_org_res_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/mmc/management/orgRes",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOrgResResponse"
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

    def show_program(self, request):
        r"""根据ID查询节目详情

        根据ID获取节目详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProgram
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowProgramRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowProgramResponse`
        """
        http_info = self._show_program_http_info(request)
        return self._call_api(**http_info)

    def show_program_invoker(self, request):
        http_info = self._show_program_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_program_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/sss/programs/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProgramResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def show_publication(self, request):
        r"""根据ID查询信息窗发布详情

        根据ID获取发布详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPublication
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowPublicationRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowPublicationResponse`
        """
        http_info = self._show_publication_http_info(request)
        return self._call_api(**http_info)

    def show_publication_invoker(self, request):
        http_info = self._show_publication_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_publication_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/sss/publications/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPublicationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def show_real_time_info_of_meeting(self, request):
        r"""查询会议实时信息

        该接口用于查询正在召开的会议实时信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRealTimeInfoOfMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowRealTimeInfoOfMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowRealTimeInfoOfMeetingResponse`
        """
        http_info = self._show_real_time_info_of_meeting_http_info(request)
        return self._call_api(**http_info)

    def show_real_time_info_of_meeting_invoker(self, request):
        http_info = self._show_real_time_info_of_meeting_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_real_time_info_of_meeting_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/mmc/control/conferences/realTimeInfo",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRealTimeInfoOfMeetingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def show_record_info(self, request):
        r"""查询单会议录制文件信息

        查询单会议录制文件信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRecordInfo
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowRecordInfoRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowRecordInfoResponse`
        """
        http_info = self._show_record_info_http_info(request)
        return self._call_api(**http_info)

    def show_record_info_invoker(self, request):
        http_info = self._show_record_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_record_info_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/mmc/rlm/record/info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRecordInfoResponse"
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

    def show_recording_detail(self, request):
        r"""查询录制详情

        改接口用于查询某个会议录制的详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRecordingDetail
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowRecordingDetailRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowRecordingDetailResponse`
        """
        http_info = self._show_recording_detail_http_info(request)
        return self._call_api(**http_info)

    def show_recording_detail_invoker(self, request):
        http_info = self._show_recording_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_recording_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/mmc/management/conferences/record/files",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRecordingDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conf_uuid' in local_var_params:
            query_params.append(('confUUID', local_var_params['conf_uuid']))
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

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

    def show_recording_file_download_urls(self, request):
        r"""查询录制文件下载链接

        该接口用户查询指定会议录制文件下载链接。
        &gt; * 仅企业管理员权限的帐号才能查询录制文件的下载链接
        &gt; * 这个接口需要在华为云会议后台开通白名单后才能调用。请联系华为销售人员，并提供华为云会议企业ID
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRecordingFileDownloadUrls
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowRecordingFileDownloadUrlsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowRecordingFileDownloadUrlsResponse`
        """
        http_info = self._show_recording_file_download_urls_http_info(request)
        return self._call_api(**http_info)

    def show_recording_file_download_urls_invoker(self, request):
        http_info = self._show_recording_file_download_urls_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_recording_file_download_urls_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/mmc/management/record/downloadurls",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRecordingFileDownloadUrlsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conf_uuid' in local_var_params:
            query_params.append(('confUUID', local_var_params['conf_uuid']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

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

    def show_region_info_of_meeting(self, request):
        r"""查询会议所在区域信息

        该接口用于查询会议所在区域的IP和域名。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRegionInfoOfMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowRegionInfoOfMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowRegionInfoOfMeetingResponse`
        """
        http_info = self._show_region_info_of_meeting_http_info(request)
        return self._call_api(**http_info)

    def show_region_info_of_meeting_invoker(self, request):
        http_info = self._show_region_info_of_meeting_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_region_info_of_meeting_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/mmc/management/conferences/region/info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRegionInfoOfMeetingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

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

    def show_room_setting(self, request):
        r"""查询网络研讨会高级设置

        该接口用于查询指定网络研讨会的高级设置。管理员可查询企业内的网络研讨会高级设置，非管理员只可查询自己预定的网络研讨会的高级设置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRoomSetting
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowRoomSettingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowRoomSettingResponse`
        """
        http_info = self._show_room_setting_http_info(request)
        return self._call_api(**http_info)

    def show_room_setting_invoker(self, request):
        http_info = self._show_room_setting_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_room_setting_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/wss/webinar/open/room-setting/{conference_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRoomSettingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'conference_id' in local_var_params:
            path_params['conference_id'] = local_var_params['conference_id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def show_sp_res(self, request):
        r"""SP管理员查询SP下资源使用信息

        SP管理员查询所属SP的共享资源使用信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSpRes
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowSpResRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowSpResResponse`
        """
        http_info = self._show_sp_res_http_info(request)
        return self._call_api(**http_info)

    def show_sp_res_invoker(self, request):
        http_info = self._show_sp_res_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sp_res_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/mmc/management/spRes",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSpResResponse"
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

    def show_sp_resource(self, request):
        r"""SP管理员查询资源信息

        SP管理员查询SP的所有资源，包括已使用的资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSpResource
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowSpResourceRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowSpResourceResponse`
        """
        http_info = self._show_sp_resource_http_info(request)
        return self._call_api(**http_info)

    def show_sp_resource_invoker(self, request):
        http_info = self._show_sp_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sp_resource_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/dcs/sp/resource",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSpResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query_group' in local_var_params:
            query_params.append(('queryGroup', local_var_params['query_group']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def show_sso_config(self, request):
        r"""查询SSO登录配置

        该接口用于查询SSO登录的鉴权配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSsoConfig
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowSsoConfigRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowSsoConfigResponse`
        """
        http_info = self._show_sso_config_http_info(request)
        return self._call_api(**http_info)

    def show_sso_config_invoker(self, request):
        http_info = self._show_sso_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sso_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/acs/authorizeconfig",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSsoConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def show_user_detail(self, request):
        r"""查询用户详情

        企业管理员通过该接口查询企业用户详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUserDetail
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowUserDetailRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowUserDetailResponse`
        """
        http_info = self._show_user_detail_http_info(request)
        return self._call_api(**http_info)

    def show_user_detail_invoker(self, request):
        http_info = self._show_user_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_user_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/usg/dcs/corp/member/{account}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUserDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'account' in local_var_params:
            path_params['account'] = local_var_params['account']

        query_params = []
        if 'account_type' in local_var_params:
            query_params.append(('accountType', local_var_params['account_type']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def show_web_hook_config(self, request):
        r"""查询事件推送

        该接口用于管理员查询企业事件订阅配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowWebHookConfig
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowWebHookConfigRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowWebHookConfigResponse`
        """
        http_info = self._show_web_hook_config_http_info(request)
        return self._call_api(**http_info)

    def show_web_hook_config_invoker(self, request):
        http_info = self._show_web_hook_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_web_hook_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/mmc/management/webhook/link-config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWebHookConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'corp_id' in local_var_params:
            query_params.append(('corpId', local_var_params['corp_id']))
        if 'sp_id' in local_var_params:
            query_params.append(('spId', local_var_params['sp_id']))

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

    def show_webinar(self, request):
        r"""查询网络研讨会详情

        该接口用于查询指定网络研讨会的详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowWebinar
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowWebinarRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowWebinarResponse`
        """
        http_info = self._show_webinar_http_info(request)
        return self._call_api(**http_info)

    def show_webinar_invoker(self, request):
        http_info = self._show_webinar_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_webinar_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/wss/webinar/open/conferences/{conference_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWebinarResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'conference_id' in local_var_params:
            path_params['conference_id'] = local_var_params['conference_id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def start_meeting(self, request):
        r"""激活会议

        该接口用于通过会议ID和会议密码激活会议。所有的会控接口都需要在会议激活后才能调用，可以通过该接口先激活会议。
        &gt; 来宾密码是否可以激活会议取决于会议创建时是否设置了“是否允许来宾启动会议”（allowGuestStartConf&#x3D;true）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.StartMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.StartMeetingResponse`
        """
        http_info = self._start_meeting_http_info(request)
        return self._call_api(**http_info)

    def start_meeting_invoker(self, request):
        http_info = self._start_meeting_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_meeting_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/mmc/management/conferences/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartMeetingResponse"
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

    def stop_meeting(self, request):
        r"""结束会议

        该接口用于结束正在召开的会议。
        &gt; * 如果管理员在企业的会议设置中关闭“结束会议保留预约记录”开关，会议结束后会议列表中将删除该会议，与会者不能再次加入该会议。否则会议预约时间到之前，与会者可以再次加入该会议
        &gt; * “结束会议保留预约记录”默认是开的
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.StopMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.StopMeetingResponse`
        """
        http_info = self._stop_meeting_http_info(request)
        return self._call_api(**http_info)

    def stop_meeting_invoker(self, request):
        http_info = self._stop_meeting_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_meeting_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopMeetingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def switch_mode(self, request):
        r"""切换视频显示策略

        该接口用于切换会中视频画面显示策略，包括广播多画面，广播单画面，声控多画面。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchMode
        :type request: :class:`huaweicloudsdkmeeting.v1.SwitchModeRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SwitchModeResponse`
        """
        http_info = self._switch_mode_http_info(request)
        return self._call_api(**http_info)

    def switch_mode_invoker(self, request):
        http_info = self._switch_mode_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_mode_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/display/mode",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchModeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def update_app_id(self, request):
        r"""修改企业应用

        企业默认管理员修改企业应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAppId
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateAppIdRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateAppIdResponse`
        """
        http_info = self._update_app_id_http_info(request)
        return self._call_api(**http_info)

    def update_app_id_invoker(self, request):
        http_info = self._update_app_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_app_id_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/usg/acs/corp/app/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAppIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_contact(self, request):
        r"""修改手机或邮箱

        企业用户通过该接口修改手机或邮箱，需要先获取验证码，验证多次失败会禁止修改。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateContact
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateContactRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateContactResponse`
        """
        http_info = self._update_contact_http_info(request)
        return self._call_api(**http_info)

    def update_contact_invoker(self, request):
        http_info = self._update_contact_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_contact_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/usg/dcs/member/contact",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateContactResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def update_corp(self, request):
        r"""SP管理员修改企业

        修改企业，若任一参数为null或者不携带则不修改。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCorp
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateCorpRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateCorpResponse`
        """
        http_info = self._update_corp_http_info(request)
        return self._call_api(**http_info)

    def update_corp_invoker(self, request):
        http_info = self._update_corp_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_corp_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/usg/dcs/sp/corp/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCorpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def update_corp_basic_info(self, request):
        r"""企业管理员修改企业注册信息

        企业管理员通过该接口修改企业注册信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCorpBasicInfo
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateCorpBasicInfoRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateCorpBasicInfoResponse`
        """
        http_info = self._update_corp_basic_info_http_info(request)
        return self._call_api(**http_info)

    def update_corp_basic_info_invoker(self, request):
        http_info = self._update_corp_basic_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_corp_basic_info_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/usg/dcs/corp",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCorpBasicInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def update_department(self, request):
        r"""修改部门

        企业管理员通过该接口修改部门。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDepartment
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateDepartmentRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateDepartmentResponse`
        """
        http_info = self._update_department_http_info(request)
        return self._call_api(**http_info)

    def update_department_invoker(self, request):
        http_info = self._update_department_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_department_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/usg/dcs/corp/dept/{dept_code}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDepartmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dept_code' in local_var_params:
            path_params['dept_code'] = local_var_params['dept_code']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def update_device(self, request):
        r"""修改终端

        企业管理员通过该接口修改专业会议终端。
        &gt; 如果需要修改Ideahub、SmartRooms、智慧屏TV请使用[[修改用户](https://support.huaweicloud.com/api-meeting/meeting_21_0068.html)](tag:hws)[[修改用户](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0068.html)](tag:hk)接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDevice
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateDeviceRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateDeviceResponse`
        """
        http_info = self._update_device_http_info(request)
        return self._call_api(**http_info)

    def update_device_invoker(self, request):
        http_info = self._update_device_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_device_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/usg/dcs/corp/device/{sn}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sn' in local_var_params:
            path_params['sn'] = local_var_params['sn']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def update_material(self, request):
        r"""更新信息窗素材

        更新信息窗素材。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateMaterial
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateMaterialRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateMaterialResponse`
        """
        http_info = self._update_material_http_info(request)
        return self._call_api(**http_info)

    def update_material_invoker(self, request):
        http_info = self._update_material_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_material_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/usg/sss/materials/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMaterialResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def update_meeting(self, request):
        r"""编辑预约会议

        该接口用于修改已预约的会议。会议开始后，不能被修改。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateMeetingResponse`
        """
        http_info = self._update_meeting_http_info(request)
        return self._call_api(**http_info)

    def update_meeting_invoker(self, request):
        http_info = self._update_meeting_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_meeting_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/management/conferences",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMeetingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

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

    def update_member_vmr(self, request):
        r"""修改用会议室及个人会议ID信息

        企业用户登录后可以修改分配给用户的云会议室及个人会议ID。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateMemberVmr
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateMemberVmrRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateMemberVmrResponse`
        """
        http_info = self._update_member_vmr_http_info(request)
        return self._call_api(**http_info)

    def update_member_vmr_invoker(self, request):
        http_info = self._update_member_vmr_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_member_vmr_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/usg/dcs/member/vmr/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMemberVmrResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def update_my_info(self, request):
        r"""用户修改自己的信息

        企业用户通过该接口修改自己的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateMyInfo
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateMyInfoRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateMyInfoResponse`
        """
        http_info = self._update_my_info_http_info(request)
        return self._call_api(**http_info)

    def update_my_info_invoker(self, request):
        http_info = self._update_my_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_my_info_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/usg/dcs/member",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMyInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def update_program(self, request):
        r"""更新信息窗节目

        更新信息窗节目。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateProgram
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateProgramRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateProgramResponse`
        """
        http_info = self._update_program_http_info(request)
        return self._call_api(**http_info)

    def update_program_invoker(self, request):
        http_info = self._update_program_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_program_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/usg/sss/programs/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProgramResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def update_publication(self, request):
        r"""修改信息窗发布

        修改信息窗发布。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePublication
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdatePublicationRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdatePublicationResponse`
        """
        http_info = self._update_publication_http_info(request)
        return self._call_api(**http_info)

    def update_publication_invoker(self, request):
        http_info = self._update_publication_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_publication_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/usg/sss/publications/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePublicationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def update_pwd(self, request):
        r"""修改密码

        企业成员通过该接口提供用户修改密码功能，服务器收到请求，修改用户密码并返回结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePwd
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdatePwdRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdatePwdResponse`
        """
        http_info = self._update_pwd_http_info(request)
        return self._call_api(**http_info)

    def update_pwd_invoker(self, request):
        http_info = self._update_pwd_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_pwd_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/usg/acs/password",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePwdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def update_recurring_meeting(self, request):
        r"""编辑周期性会议

        该接口用于修改已预约的周期性会议。会议开始后，不能被修改。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRecurringMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateRecurringMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateRecurringMeetingResponse`
        """
        http_info = self._update_recurring_meeting_http_info(request)
        return self._call_api(**http_info)

    def update_recurring_meeting_invoker(self, request):
        http_info = self._update_recurring_meeting_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_recurring_meeting_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/management/cycleconferences",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRecurringMeetingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

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

    def update_recurring_sub_meeting(self, request):
        r"""编辑周期性会议的子会议

        该接口用于修改已预约的周期性会议的子会议。会议开始后，不能被修改。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRecurringSubMeeting
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateRecurringSubMeetingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateRecurringSubMeetingResponse`
        """
        http_info = self._update_recurring_sub_meeting_http_info(request)
        return self._call_api(**http_info)

    def update_recurring_sub_meeting_invoker(self, request):
        http_info = self._update_recurring_sub_meeting_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_recurring_sub_meeting_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/management/conferences/cyclesubconf",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRecurringSubMeetingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_uuid' in local_var_params:
            query_params.append(('userUUID', local_var_params['user_uuid']))
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_authorization_type' in local_var_params:
            header_params['X-Authorization-Type'] = local_var_params['x_authorization_type']
        if 'x_site_id' in local_var_params:
            header_params['X-Site-Id'] = local_var_params['x_site_id']

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

    def update_resource(self, request):
        r"""SP管理员根据修改企业资源

        企业修改资源的过期时间、停用状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateResource
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateResourceRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateResourceResponse`
        """
        http_info = self._update_resource_http_info(request)
        return self._call_api(**http_info)

    def update_resource_invoker(self, request):
        http_info = self._update_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_resource_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/usg/dcs/sp/corp/{corp_id}/resource",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'corp_id' in local_var_params:
            path_params['corp_id'] = local_var_params['corp_id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def update_room_setting(self, request):
        r"""修改网络研讨会高级设置

        该接口用于设置指定网络研讨会的高级设置。管理员可设置企业内的网络研讨会高级设置，非管理员只可设置自己预定的网络研讨会的高级设置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRoomSetting
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateRoomSettingRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateRoomSettingResponse`
        """
        http_info = self._update_room_setting_http_info(request)
        return self._call_api(**http_info)

    def update_room_setting_invoker(self, request):
        http_info = self._update_room_setting_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_room_setting_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/wss/webinar/open/room-setting/{conference_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRoomSettingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'conference_id' in local_var_params:
            path_params['conference_id'] = local_var_params['conference_id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def update_started_conf_config(self, request):
        r"""会中修改配置

        该接口用于修改会议配置，包括会议共享是否锁定，允许呼入范围。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateStartedConfConfig
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateStartedConfConfigRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateStartedConfConfigResponse`
        """
        http_info = self._update_started_conf_config_http_info(request)
        return self._call_api(**http_info)

    def update_started_conf_config_invoker(self, request):
        http_info = self._update_started_conf_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_started_conf_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/control/conferences/updateStartedConfConfig",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateStartedConfConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conference_id' in local_var_params:
            query_params.append(('conferenceID', local_var_params['conference_id']))

        header_params = {}
        if 'x_conference_authorization' in local_var_params:
            header_params['X-Conference-Authorization'] = local_var_params['x_conference_authorization']

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

    def update_token(self, request):
        r"""刷新Token

        该接口提供刷新Token功能，根据传入的Token，刷新Token失效时间并返回结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateToken
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateTokenRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateTokenResponse`
        """
        http_info = self._update_token_http_info(request)
        return self._call_api(**http_info)

    def update_token_invoker(self, request):
        http_info = self._update_token_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_token_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/usg/acs/token",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTokenResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-ID'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def update_user(self, request):
        r"""修改用户

        企业管理员通过该接口修改企业用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateUser
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateUserRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateUserResponse`
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
            "resource_path": "/v1/usg/dcs/corp/member/{account}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'account' in local_var_params:
            path_params['account'] = local_var_params['account']

        query_params = []
        if 'account_type' in local_var_params:
            query_params.append(('accountType', local_var_params['account_type']))

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def update_web_hook_config_status(self, request):
        r"""开启事件推送

        该接口用于管理员变更订阅配置使用状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateWebHookConfigStatus
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateWebHookConfigStatusRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateWebHookConfigStatusResponse`
        """
        http_info = self._update_web_hook_config_status_http_info(request)
        return self._call_api(**http_info)

    def update_web_hook_config_status_invoker(self, request):
        http_info = self._update_web_hook_config_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_web_hook_config_status_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mmc/management/webhook/change-status",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateWebHookConfigStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
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

    def update_webinar(self, request):
        r"""编辑网络研讨会

        该接口用于修改已创建的网络研讨会。网络研讨会开始后不能修改。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateWebinar
        :type request: :class:`huaweicloudsdkmeeting.v1.UpdateWebinarRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UpdateWebinarResponse`
        """
        http_info = self._update_webinar_http_info(request)
        return self._call_api(**http_info)

    def update_webinar_invoker(self, request):
        http_info = self._update_webinar_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_webinar_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/wss/webinar/open/conferences",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateWebinarResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

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

    def upload_file(self, request):
        r"""上传图片

        该接口用户上传网络研讨会高级设置用的图片。图片可用于网络研讨会的封面和Logo。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadFile
        :type request: :class:`huaweicloudsdkmeeting.v1.UploadFileRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.UploadFileResponse`
        """
        http_info = self._upload_file_http_info(request)
        return self._call_api(**http_info)

    def upload_file_invoker(self, request):
        http_info = self._upload_file_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upload_file_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/wss/webinar/open/res/file",
            "request_type": request.__class__.__name__,
            "response_type": "UploadFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def search_qos_history_meetings(self, request):
        r"""查询QoS历史会议列表

        该接口用于查询企业内历史会议的QoS告警。仅旗舰版企业/标准版企业的企业管理员有权限查询。可以查询最近3个月内的数据。
        &gt; 仪表盘的QoS统计功能需要申请才能开通。请联系华为销售人员，并提供华为云会议企业ID。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchQosHistoryMeetings
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchQosHistoryMeetingsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchQosHistoryMeetingsResponse`
        """
        http_info = self._search_qos_history_meetings_http_info(request)
        return self._call_api(**http_info)

    def search_qos_history_meetings_invoker(self, request):
        http_info = self._search_qos_history_meetings_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_qos_history_meetings_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/metrics/conferences/history",
            "request_type": request.__class__.__name__,
            "response_type": "SearchQosHistoryMeetingsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_date' in local_var_params:
            query_params.append(('startDate', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('endDate', local_var_params['end_date']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))

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

    def search_qos_online_meetings(self, request):
        r"""查询QoS在线会议列表

        该接口用于查询企业内正在召开会议的QoS告警。仅旗舰版企业/标准版企业的企业管理员有权限查询。
        &gt; 仪表盘的QoS统计功能需要申请才能开通。请联系华为销售人员，并提供华为云会议企业ID。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchQosOnlineMeetings
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchQosOnlineMeetingsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchQosOnlineMeetingsResponse`
        """
        http_info = self._search_qos_online_meetings_http_info(request)
        return self._call_api(**http_info)

    def search_qos_online_meetings_invoker(self, request):
        http_info = self._search_qos_online_meetings_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_qos_online_meetings_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/metrics/conferences/online",
            "request_type": request.__class__.__name__,
            "response_type": "SearchQosOnlineMeetingsResponse"
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
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))

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

    def search_qos_participant_detail(self, request):
        r"""查询与会者的QoS数据

        该接口用于查询企业内在线会议或历史会议的与会者QoS数据。仅旗舰版企业/标准版企业的企业管理员有权限查询。
        &gt; 仪表盘的QoS统计功能需要申请才能开通。请联系华为销售人员，并提供华为云会议企业ID。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchQosParticipantDetail
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchQosParticipantDetailRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchQosParticipantDetailResponse`
        """
        http_info = self._search_qos_participant_detail_http_info(request)
        return self._call_api(**http_info)

    def search_qos_participant_detail_invoker(self, request):
        http_info = self._search_qos_participant_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_qos_participant_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/metrics/conference/participant/qos",
            "request_type": request.__class__.__name__,
            "response_type": "SearchQosParticipantDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conf_uuid' in local_var_params:
            query_params.append(('confUUID', local_var_params['conf_uuid']))
        if 'conf_type' in local_var_params:
            query_params.append(('confType', local_var_params['conf_type']))
        if 'participant_id' in local_var_params:
            query_params.append(('participantID', local_var_params['participant_id']))
        if 'qos_type' in local_var_params:
            query_params.append(('qosType', local_var_params['qos_type']))

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

    def search_qos_participants(self, request):
        r"""查询QoS会议与会者列表

        该接口用于查询企业内在线会议或历史会议的与会者QoS告警。仅旗舰版企业/标准版企业的企业管理员有权限查询。
        &gt; 仪表盘的QoS统计功能需要申请才能开通。请联系华为销售人员，并提供华为云会议企业ID。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchQosParticipants
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchQosParticipantsRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchQosParticipantsResponse`
        """
        http_info = self._search_qos_participants_http_info(request)
        return self._call_api(**http_info)

    def search_qos_participants_invoker(self, request):
        http_info = self._search_qos_participants_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_qos_participants_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/metrics/conference/participants",
            "request_type": request.__class__.__name__,
            "response_type": "SearchQosParticipantsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'conf_uuid' in local_var_params:
            query_params.append(('confUUID', local_var_params['conf_uuid']))
        if 'conf_type' in local_var_params:
            query_params.append(('confType', local_var_params['conf_type']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search_key' in local_var_params:
            query_params.append(('searchKey', local_var_params['search_key']))

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

    def set_qos_threshold(self, request):
        r"""设置QoS告警阈值

        该接口用于设置QoS告警阈值。仅旗舰版企业/标准版企业的企业管理员有权限设置。
        &gt; 仪表盘的QoS统计功能需要申请才能开通。请联系华为销售人员，并提供华为云会议企业ID。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetQosThreshold
        :type request: :class:`huaweicloudsdkmeeting.v1.SetQosThresholdRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetQosThresholdResponse`
        """
        http_info = self._set_qos_threshold_http_info(request)
        return self._call_api(**http_info)

    def set_qos_threshold_invoker(self, request):
        http_info = self._set_qos_threshold_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_qos_threshold_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/metrics/conference/threshold",
            "request_type": request.__class__.__name__,
            "response_type": "SetQosThresholdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'threshold_type' in local_var_params:
            query_params.append(('thresholdType', local_var_params['threshold_type']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=utf-8'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_qos_threshold(self, request):
        r"""查询QoS告警阈值

        该接口用于查询QoS告警阈值。仅旗舰版企业/标准版企业的企业管理员有权限查询。
        &gt; 该接口用于查询QoS告警阈值。仅旗舰版企业/标准版企业的企业管理员有权限查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowQosThreshold
        :type request: :class:`huaweicloudsdkmeeting.v1.ShowQosThresholdRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowQosThresholdResponse`
        """
        http_info = self._show_qos_threshold_http_info(request)
        return self._call_api(**http_info)

    def show_qos_threshold_invoker(self, request):
        http_info = self._show_qos_threshold_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_qos_threshold_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/metrics/conference/threshold",
            "request_type": request.__class__.__name__,
            "response_type": "ShowQosThresholdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'threshold_type' in local_var_params:
            query_params.append(('thresholdType', local_var_params['threshold_type']))

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

    def search_statistic_conference_info(self, request):
        r"""查询企业级会议总体统计数据

        该接口用于查询企业内：
        * 单日内按小时统计的会议数据。
        * 指定日期范围内按日/按月统计的会议数据。
        &gt; 仅旗舰版企业/标准版企业的企业管理员有权限查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchStatisticConferenceInfo
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchStatisticConferenceInfoRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchStatisticConferenceInfoResponse`
        """
        http_info = self._search_statistic_conference_info_http_info(request)
        return self._call_api(**http_info)

    def search_statistic_conference_info_invoker(self, request):
        http_info = self._search_statistic_conference_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_statistic_conference_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/metrics/dashboard/statistic/conference/info",
            "request_type": request.__class__.__name__,
            "response_type": "SearchStatisticConferenceInfoResponse"
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
        if 'time_unit' in local_var_params:
            query_params.append(('timeUnit', local_var_params['time_unit']))
        if 'start_time' in local_var_params:
            query_params.append(('startTime', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('endTime', local_var_params['end_time']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))

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

    def search_statistic_conference_participant(self, request):
        r"""查询企业级会议与会统计数据

        该接口用于查询企业内与会者数据统计：
        * 查询与会用户统计数据，按日/按月统计。
        * 查询与会硬件终端统计数据，按日/按月统计。
        * 查询与会设备统计数据，按日/按月统计。
        &gt; 仅旗舰版企业/标准版企业的企业管理员有权限查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchStatisticConferenceParticipant
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchStatisticConferenceParticipantRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchStatisticConferenceParticipantResponse`
        """
        http_info = self._search_statistic_conference_participant_http_info(request)
        return self._call_api(**http_info)

    def search_statistic_conference_participant_invoker(self, request):
        http_info = self._search_statistic_conference_participant_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_statistic_conference_participant_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/metrics/dashboard/statistic/conference/participant",
            "request_type": request.__class__.__name__,
            "response_type": "SearchStatisticConferenceParticipantResponse"
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
        if 'time_unit' in local_var_params:
            query_params.append(('timeUnit', local_var_params['time_unit']))
        if 'start_time' in local_var_params:
            query_params.append(('startTime', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('endTime', local_var_params['end_time']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))

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

    def search_statistic_resource_info(self, request):
        r"""查询企业级会议已购资源使用统计数据

        该接口用于查询企业内已购资源使用状况数据统计：
        * 查询已购资源使用状况，按日/按月统计。
        &gt; 仅旗舰版企业/标准版企业的企业管理员有权限查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchStatisticResourceInfo
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchStatisticResourceInfoRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchStatisticResourceInfoResponse`
        """
        http_info = self._search_statistic_resource_info_http_info(request)
        return self._call_api(**http_info)

    def search_statistic_resource_info_invoker(self, request):
        http_info = self._search_statistic_resource_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_statistic_resource_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/metrics/dashboard/statistic/resource/info",
            "request_type": request.__class__.__name__,
            "response_type": "SearchStatisticResourceInfoResponse"
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
        if 'time_unit' in local_var_params:
            query_params.append(('timeUnit', local_var_params['time_unit']))
        if 'start_time' in local_var_params:
            query_params.append(('startTime', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('endTime', local_var_params['end_time']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))

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

    def search_statistic_user_info(self, request):
        r"""查询企业级会议的用户统计数据

        该接口用于查询企业内用户数据统计：
        * 查询会议用户登录数据，按日/按月统计。
        * 查询会议用户激活数据，按日/按月统计。
        * 查询会议用户登录设备数据，按日/按月统计。
        &gt; 仅旗舰版企业/标准版企业的企业管理员有权限查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchStatisticUserInfo
        :type request: :class:`huaweicloudsdkmeeting.v1.SearchStatisticUserInfoRequest`
        :rtype: :class:`huaweicloudsdkmeeting.v1.SearchStatisticUserInfoResponse`
        """
        http_info = self._search_statistic_user_info_http_info(request)
        return self._call_api(**http_info)

    def search_statistic_user_info_invoker(self, request):
        http_info = self._search_statistic_user_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_statistic_user_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/metrics/dashboard/statistic/user/info",
            "request_type": request.__class__.__name__,
            "response_type": "SearchStatisticUserInfoResponse"
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
        if 'time_unit' in local_var_params:
            query_params.append(('timeUnit', local_var_params['time_unit']))
        if 'start_time' in local_var_params:
            query_params.append(('startTime', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('endTime', local_var_params['end_time']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))

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
