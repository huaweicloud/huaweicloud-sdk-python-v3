# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApiVersionDetailV2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'int',
        'version': 'str',
        'req_protocol': 'str',
        'req_method': 'str',
        'req_uri': 'str',
        'auth_type': 'str',
        'auth_opt': 'AuthOpt',
        'cors': 'bool',
        'match_mode': 'str',
        'backend_type': 'str',
        'remark': 'str',
        'group_id': 'str',
        'body_remark': 'str',
        'result_normal_sample': 'str',
        'result_failure_sample': 'str',
        'authorizer_id': 'str',
        'tags': 'list[str]',
        'response_id': 'str',
        'roma_app_id': 'str',
        'domain_name': 'str',
        'tag': 'str',
        'content_type': 'str',
        'id': 'str',
        'status': 'int',
        'arrange_necessary': 'int',
        'register_time': 'datetime',
        'update_time': 'datetime',
        'group_name': 'str',
        'group_version': 'str',
        'run_env_id': 'str',
        'run_env_name': 'str',
        'publish_id': 'str',
        'publish_time': 'datetime',
        'roma_app_name': 'str',
        'ld_api_id': 'str',
        'backend_api': 'BackendApi',
        'api_group_info': 'ApiGroupCommonInfo',
        'func_info': 'ApiFunc',
        'mock_info': 'ApiMock',
        'req_params': 'list[ReqParam]',
        'backend_params': 'list[BackendParam]',
        'policy_functions': 'list[ApiPolicyFunctionResp]',
        'policy_mocks': 'list[ApiPolicyMockResp]',
        'policy_https': 'list[ApiPolicyHttpResp]',
        'sl_domain': 'str',
        'sl_domains': 'list[str]',
        'version_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'version': 'version',
        'req_protocol': 'req_protocol',
        'req_method': 'req_method',
        'req_uri': 'req_uri',
        'auth_type': 'auth_type',
        'auth_opt': 'auth_opt',
        'cors': 'cors',
        'match_mode': 'match_mode',
        'backend_type': 'backend_type',
        'remark': 'remark',
        'group_id': 'group_id',
        'body_remark': 'body_remark',
        'result_normal_sample': 'result_normal_sample',
        'result_failure_sample': 'result_failure_sample',
        'authorizer_id': 'authorizer_id',
        'tags': 'tags',
        'response_id': 'response_id',
        'roma_app_id': 'roma_app_id',
        'domain_name': 'domain_name',
        'tag': 'tag',
        'content_type': 'content_type',
        'id': 'id',
        'status': 'status',
        'arrange_necessary': 'arrange_necessary',
        'register_time': 'register_time',
        'update_time': 'update_time',
        'group_name': 'group_name',
        'group_version': 'group_version',
        'run_env_id': 'run_env_id',
        'run_env_name': 'run_env_name',
        'publish_id': 'publish_id',
        'publish_time': 'publish_time',
        'roma_app_name': 'roma_app_name',
        'ld_api_id': 'ld_api_id',
        'backend_api': 'backend_api',
        'api_group_info': 'api_group_info',
        'func_info': 'func_info',
        'mock_info': 'mock_info',
        'req_params': 'req_params',
        'backend_params': 'backend_params',
        'policy_functions': 'policy_functions',
        'policy_mocks': 'policy_mocks',
        'policy_https': 'policy_https',
        'sl_domain': 'sl_domain',
        'sl_domains': 'sl_domains',
        'version_id': 'version_id'
    }

    def __init__(self, name=None, type=None, version=None, req_protocol=None, req_method=None, req_uri=None, auth_type=None, auth_opt=None, cors=None, match_mode=None, backend_type=None, remark=None, group_id=None, body_remark=None, result_normal_sample=None, result_failure_sample=None, authorizer_id=None, tags=None, response_id=None, roma_app_id=None, domain_name=None, tag=None, content_type=None, id=None, status=None, arrange_necessary=None, register_time=None, update_time=None, group_name=None, group_version=None, run_env_id=None, run_env_name=None, publish_id=None, publish_time=None, roma_app_name=None, ld_api_id=None, backend_api=None, api_group_info=None, func_info=None, mock_info=None, req_params=None, backend_params=None, policy_functions=None, policy_mocks=None, policy_https=None, sl_domain=None, sl_domains=None, version_id=None):
        """ListApiVersionDetailV2Response

        The model defined in huaweicloud sdk

        :param name: API名称。  支持汉字、英文、数字、中划线、下划线、点、斜杠、中英文格式下的小括号和冒号、中文格式下的顿号，且只能以英文、汉字和数字开头，3-255个字符。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type name: str
        :param type: API类型 - 1：公有API - 2：私有API
        :type type: int
        :param version: API的版本
        :type version: str
        :param req_protocol: API的请求协议 - HTTP - HTTPS - BOTH：同时支持HTTP和HTTPS - GRPCS
        :type req_protocol: str
        :param req_method: API的请求方式，当API的请求协议为GRPC类型协议时请求方式固定为POST。
        :type req_method: str
        :param req_uri: 请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ . 等特殊字符，总长度不超过512，且满足URI规范。  &gt; 需要服从URI规范。
        :type req_uri: str
        :param auth_type: API的认证方式 - NONE：无认证 - APP：APP认证 - IAM：IAM认证 - AUTHORIZER：自定义认证，当auth_type取值为AUTHORIZER时，authorizer_id字段必须传入  当API的请求协议为GRPC类型时不支持自定义认证。
        :type auth_type: str
        :param auth_opt: 
        :type auth_opt: :class:`huaweicloudsdkapig.v2.AuthOpt`
        :param cors: 是否支持跨域 - TRUE：支持 - FALSE：不支持
        :type cors: bool
        :param match_mode: API的匹配方式 - SWA：前缀匹配 - NORMAL：正常匹配（绝对匹配） 默认：NORMAL
        :type match_mode: str
        :param backend_type: 后端类型 - HTTP：web后端 - FUNCTION：函数工作流，当backend_type取值为FUNCTION时，func_info字段必须传入 - MOCK：模拟的后端，当backend_type取值为MOCK时，mock_info字段必须传入 - GRPC：grpc后端
        :type backend_type: str
        :param remark: API描述。字符长度不超过255 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type remark: str
        :param group_id: API所属的分组编号
        :type group_id: str
        :param body_remark: API请求体描述，可以是请求体示例、媒体类型、参数等信息。字符长度不超过20480 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type body_remark: str
        :param result_normal_sample: 正常响应示例，描述API的正常返回信息。字符长度不超过20480 &gt; 中文字符必须为UTF-8或者unicode编码。  当API的请求协议为GRPC类型时不支持配置。
        :type result_normal_sample: str
        :param result_failure_sample: 失败返回示例，描述API的异常返回信息。字符长度不超过20480 &gt; 中文字符必须为UTF-8或者unicode编码。  当API的请求协议为GRPC类型时不支持配置。
        :type result_failure_sample: str
        :param authorizer_id: 前端自定义认证对象的ID，API请求协议为GRPC类型时不支持前端自定义认证
        :type authorizer_id: str
        :param tags: 标签。  支持英文，数字，中文，特殊符号（-*#%.:_），且只能以中文或英文开头。  默认支持10个标签，如需扩大配额请联系技术工程师修改API_TAG_NUM_LIMIT配置。 
        :type tags: list[str]
        :param response_id: 分组自定义响应ID
        :type response_id: str
        :param roma_app_id: 集成应用ID  暂不支持
        :type roma_app_id: str
        :param domain_name: API绑定的自定义域名  暂不支持
        :type domain_name: str
        :param tag: 标签  待废弃，优先使用tags字段
        :type tag: str
        :param content_type: 请求内容格式类型：  application/json application/xml multipart/form-data text/plain  暂不支持
        :type content_type: str
        :param id: API编号
        :type id: str
        :param status: API状态   - 1： 有效
        :type status: int
        :param arrange_necessary: 是否需要编排
        :type arrange_necessary: int
        :param register_time: API注册时间
        :type register_time: datetime
        :param update_time: API修改时间
        :type update_time: datetime
        :param group_name: API所属分组的名称
        :type group_name: str
        :param group_version: API所属分组的版本  默认V1，其他版本暂不支持
        :type group_version: str
        :param run_env_id: 发布的环境编号  存在多个发布记录时，环境编号之间用|隔开
        :type run_env_id: str
        :param run_env_name: 发布的环境名称  存在多个发布记录时，环境名称之间用|隔开
        :type run_env_name: str
        :param publish_id: 发布记录编号  存在多个发布记录时，发布记录编号之间用|隔开
        :type publish_id: str
        :param publish_time: 版本发布时间
        :type publish_time: datetime
        :param roma_app_name: API归属的集成应用名称  暂不支持
        :type roma_app_name: str
        :param ld_api_id: 当API的后端为自定义后端时，对应的自定义后端API编号  暂不支持
        :type ld_api_id: str
        :param backend_api: 
        :type backend_api: :class:`huaweicloudsdkapig.v2.BackendApi`
        :param api_group_info: 
        :type api_group_info: :class:`huaweicloudsdkapig.v2.ApiGroupCommonInfo`
        :param func_info: 
        :type func_info: :class:`huaweicloudsdkapig.v2.ApiFunc`
        :param mock_info: 
        :type mock_info: :class:`huaweicloudsdkapig.v2.ApiMock`
        :param req_params: API的请求参数列表
        :type req_params: list[:class:`huaweicloudsdkapig.v2.ReqParam`]
        :param backend_params: API的后端参数列表
        :type backend_params: list[:class:`huaweicloudsdkapig.v2.BackendParam`]
        :param policy_functions: 函数工作流策略后端列表
        :type policy_functions: list[:class:`huaweicloudsdkapig.v2.ApiPolicyFunctionResp`]
        :param policy_mocks: mock策略后端列表
        :type policy_mocks: list[:class:`huaweicloudsdkapig.v2.ApiPolicyMockResp`]
        :param policy_https: web策略后端列表
        :type policy_https: list[:class:`huaweicloudsdkapig.v2.ApiPolicyHttpResp`]
        :param sl_domain: 系统默认分配的子域名
        :type sl_domain: str
        :param sl_domains: 系统默认分配的子域名列表
        :type sl_domains: list[str]
        :param version_id: 版本编号
        :type version_id: str
        """
        
        super(ListApiVersionDetailV2Response, self).__init__()

        self._name = None
        self._type = None
        self._version = None
        self._req_protocol = None
        self._req_method = None
        self._req_uri = None
        self._auth_type = None
        self._auth_opt = None
        self._cors = None
        self._match_mode = None
        self._backend_type = None
        self._remark = None
        self._group_id = None
        self._body_remark = None
        self._result_normal_sample = None
        self._result_failure_sample = None
        self._authorizer_id = None
        self._tags = None
        self._response_id = None
        self._roma_app_id = None
        self._domain_name = None
        self._tag = None
        self._content_type = None
        self._id = None
        self._status = None
        self._arrange_necessary = None
        self._register_time = None
        self._update_time = None
        self._group_name = None
        self._group_version = None
        self._run_env_id = None
        self._run_env_name = None
        self._publish_id = None
        self._publish_time = None
        self._roma_app_name = None
        self._ld_api_id = None
        self._backend_api = None
        self._api_group_info = None
        self._func_info = None
        self._mock_info = None
        self._req_params = None
        self._backend_params = None
        self._policy_functions = None
        self._policy_mocks = None
        self._policy_https = None
        self._sl_domain = None
        self._sl_domains = None
        self._version_id = None
        self.discriminator = None

        self.name = name
        self.type = type
        if version is not None:
            self.version = version
        self.req_protocol = req_protocol
        self.req_method = req_method
        self.req_uri = req_uri
        self.auth_type = auth_type
        if auth_opt is not None:
            self.auth_opt = auth_opt
        if cors is not None:
            self.cors = cors
        if match_mode is not None:
            self.match_mode = match_mode
        self.backend_type = backend_type
        if remark is not None:
            self.remark = remark
        self.group_id = group_id
        if body_remark is not None:
            self.body_remark = body_remark
        if result_normal_sample is not None:
            self.result_normal_sample = result_normal_sample
        if result_failure_sample is not None:
            self.result_failure_sample = result_failure_sample
        if authorizer_id is not None:
            self.authorizer_id = authorizer_id
        if tags is not None:
            self.tags = tags
        if response_id is not None:
            self.response_id = response_id
        if roma_app_id is not None:
            self.roma_app_id = roma_app_id
        if domain_name is not None:
            self.domain_name = domain_name
        if tag is not None:
            self.tag = tag
        if content_type is not None:
            self.content_type = content_type
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if arrange_necessary is not None:
            self.arrange_necessary = arrange_necessary
        if register_time is not None:
            self.register_time = register_time
        if update_time is not None:
            self.update_time = update_time
        if group_name is not None:
            self.group_name = group_name
        if group_version is not None:
            self.group_version = group_version
        if run_env_id is not None:
            self.run_env_id = run_env_id
        if run_env_name is not None:
            self.run_env_name = run_env_name
        if publish_id is not None:
            self.publish_id = publish_id
        if publish_time is not None:
            self.publish_time = publish_time
        if roma_app_name is not None:
            self.roma_app_name = roma_app_name
        if ld_api_id is not None:
            self.ld_api_id = ld_api_id
        if backend_api is not None:
            self.backend_api = backend_api
        if api_group_info is not None:
            self.api_group_info = api_group_info
        if func_info is not None:
            self.func_info = func_info
        if mock_info is not None:
            self.mock_info = mock_info
        if req_params is not None:
            self.req_params = req_params
        if backend_params is not None:
            self.backend_params = backend_params
        if policy_functions is not None:
            self.policy_functions = policy_functions
        if policy_mocks is not None:
            self.policy_mocks = policy_mocks
        if policy_https is not None:
            self.policy_https = policy_https
        if sl_domain is not None:
            self.sl_domain = sl_domain
        if sl_domains is not None:
            self.sl_domains = sl_domains
        if version_id is not None:
            self.version_id = version_id

    @property
    def name(self):
        """Gets the name of this ListApiVersionDetailV2Response.

        API名称。  支持汉字、英文、数字、中划线、下划线、点、斜杠、中英文格式下的小括号和冒号、中文格式下的顿号，且只能以英文、汉字和数字开头，3-255个字符。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The name of this ListApiVersionDetailV2Response.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListApiVersionDetailV2Response.

        API名称。  支持汉字、英文、数字、中划线、下划线、点、斜杠、中英文格式下的小括号和冒号、中文格式下的顿号，且只能以英文、汉字和数字开头，3-255个字符。 > 中文字符必须为UTF-8或者unicode编码。

        :param name: The name of this ListApiVersionDetailV2Response.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this ListApiVersionDetailV2Response.

        API类型 - 1：公有API - 2：私有API

        :return: The type of this ListApiVersionDetailV2Response.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListApiVersionDetailV2Response.

        API类型 - 1：公有API - 2：私有API

        :param type: The type of this ListApiVersionDetailV2Response.
        :type type: int
        """
        self._type = type

    @property
    def version(self):
        """Gets the version of this ListApiVersionDetailV2Response.

        API的版本

        :return: The version of this ListApiVersionDetailV2Response.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ListApiVersionDetailV2Response.

        API的版本

        :param version: The version of this ListApiVersionDetailV2Response.
        :type version: str
        """
        self._version = version

    @property
    def req_protocol(self):
        """Gets the req_protocol of this ListApiVersionDetailV2Response.

        API的请求协议 - HTTP - HTTPS - BOTH：同时支持HTTP和HTTPS - GRPCS

        :return: The req_protocol of this ListApiVersionDetailV2Response.
        :rtype: str
        """
        return self._req_protocol

    @req_protocol.setter
    def req_protocol(self, req_protocol):
        """Sets the req_protocol of this ListApiVersionDetailV2Response.

        API的请求协议 - HTTP - HTTPS - BOTH：同时支持HTTP和HTTPS - GRPCS

        :param req_protocol: The req_protocol of this ListApiVersionDetailV2Response.
        :type req_protocol: str
        """
        self._req_protocol = req_protocol

    @property
    def req_method(self):
        """Gets the req_method of this ListApiVersionDetailV2Response.

        API的请求方式，当API的请求协议为GRPC类型协议时请求方式固定为POST。

        :return: The req_method of this ListApiVersionDetailV2Response.
        :rtype: str
        """
        return self._req_method

    @req_method.setter
    def req_method(self, req_method):
        """Sets the req_method of this ListApiVersionDetailV2Response.

        API的请求方式，当API的请求协议为GRPC类型协议时请求方式固定为POST。

        :param req_method: The req_method of this ListApiVersionDetailV2Response.
        :type req_method: str
        """
        self._req_method = req_method

    @property
    def req_uri(self):
        """Gets the req_uri of this ListApiVersionDetailV2Response.

        请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ . 等特殊字符，总长度不超过512，且满足URI规范。  > 需要服从URI规范。

        :return: The req_uri of this ListApiVersionDetailV2Response.
        :rtype: str
        """
        return self._req_uri

    @req_uri.setter
    def req_uri(self, req_uri):
        """Sets the req_uri of this ListApiVersionDetailV2Response.

        请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ . 等特殊字符，总长度不超过512，且满足URI规范。  > 需要服从URI规范。

        :param req_uri: The req_uri of this ListApiVersionDetailV2Response.
        :type req_uri: str
        """
        self._req_uri = req_uri

    @property
    def auth_type(self):
        """Gets the auth_type of this ListApiVersionDetailV2Response.

        API的认证方式 - NONE：无认证 - APP：APP认证 - IAM：IAM认证 - AUTHORIZER：自定义认证，当auth_type取值为AUTHORIZER时，authorizer_id字段必须传入  当API的请求协议为GRPC类型时不支持自定义认证。

        :return: The auth_type of this ListApiVersionDetailV2Response.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this ListApiVersionDetailV2Response.

        API的认证方式 - NONE：无认证 - APP：APP认证 - IAM：IAM认证 - AUTHORIZER：自定义认证，当auth_type取值为AUTHORIZER时，authorizer_id字段必须传入  当API的请求协议为GRPC类型时不支持自定义认证。

        :param auth_type: The auth_type of this ListApiVersionDetailV2Response.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def auth_opt(self):
        """Gets the auth_opt of this ListApiVersionDetailV2Response.

        :return: The auth_opt of this ListApiVersionDetailV2Response.
        :rtype: :class:`huaweicloudsdkapig.v2.AuthOpt`
        """
        return self._auth_opt

    @auth_opt.setter
    def auth_opt(self, auth_opt):
        """Sets the auth_opt of this ListApiVersionDetailV2Response.

        :param auth_opt: The auth_opt of this ListApiVersionDetailV2Response.
        :type auth_opt: :class:`huaweicloudsdkapig.v2.AuthOpt`
        """
        self._auth_opt = auth_opt

    @property
    def cors(self):
        """Gets the cors of this ListApiVersionDetailV2Response.

        是否支持跨域 - TRUE：支持 - FALSE：不支持

        :return: The cors of this ListApiVersionDetailV2Response.
        :rtype: bool
        """
        return self._cors

    @cors.setter
    def cors(self, cors):
        """Sets the cors of this ListApiVersionDetailV2Response.

        是否支持跨域 - TRUE：支持 - FALSE：不支持

        :param cors: The cors of this ListApiVersionDetailV2Response.
        :type cors: bool
        """
        self._cors = cors

    @property
    def match_mode(self):
        """Gets the match_mode of this ListApiVersionDetailV2Response.

        API的匹配方式 - SWA：前缀匹配 - NORMAL：正常匹配（绝对匹配） 默认：NORMAL

        :return: The match_mode of this ListApiVersionDetailV2Response.
        :rtype: str
        """
        return self._match_mode

    @match_mode.setter
    def match_mode(self, match_mode):
        """Sets the match_mode of this ListApiVersionDetailV2Response.

        API的匹配方式 - SWA：前缀匹配 - NORMAL：正常匹配（绝对匹配） 默认：NORMAL

        :param match_mode: The match_mode of this ListApiVersionDetailV2Response.
        :type match_mode: str
        """
        self._match_mode = match_mode

    @property
    def backend_type(self):
        """Gets the backend_type of this ListApiVersionDetailV2Response.

        后端类型 - HTTP：web后端 - FUNCTION：函数工作流，当backend_type取值为FUNCTION时，func_info字段必须传入 - MOCK：模拟的后端，当backend_type取值为MOCK时，mock_info字段必须传入 - GRPC：grpc后端

        :return: The backend_type of this ListApiVersionDetailV2Response.
        :rtype: str
        """
        return self._backend_type

    @backend_type.setter
    def backend_type(self, backend_type):
        """Sets the backend_type of this ListApiVersionDetailV2Response.

        后端类型 - HTTP：web后端 - FUNCTION：函数工作流，当backend_type取值为FUNCTION时，func_info字段必须传入 - MOCK：模拟的后端，当backend_type取值为MOCK时，mock_info字段必须传入 - GRPC：grpc后端

        :param backend_type: The backend_type of this ListApiVersionDetailV2Response.
        :type backend_type: str
        """
        self._backend_type = backend_type

    @property
    def remark(self):
        """Gets the remark of this ListApiVersionDetailV2Response.

        API描述。字符长度不超过255 > 中文字符必须为UTF-8或者unicode编码。

        :return: The remark of this ListApiVersionDetailV2Response.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this ListApiVersionDetailV2Response.

        API描述。字符长度不超过255 > 中文字符必须为UTF-8或者unicode编码。

        :param remark: The remark of this ListApiVersionDetailV2Response.
        :type remark: str
        """
        self._remark = remark

    @property
    def group_id(self):
        """Gets the group_id of this ListApiVersionDetailV2Response.

        API所属的分组编号

        :return: The group_id of this ListApiVersionDetailV2Response.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ListApiVersionDetailV2Response.

        API所属的分组编号

        :param group_id: The group_id of this ListApiVersionDetailV2Response.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def body_remark(self):
        """Gets the body_remark of this ListApiVersionDetailV2Response.

        API请求体描述，可以是请求体示例、媒体类型、参数等信息。字符长度不超过20480 > 中文字符必须为UTF-8或者unicode编码。

        :return: The body_remark of this ListApiVersionDetailV2Response.
        :rtype: str
        """
        return self._body_remark

    @body_remark.setter
    def body_remark(self, body_remark):
        """Sets the body_remark of this ListApiVersionDetailV2Response.

        API请求体描述，可以是请求体示例、媒体类型、参数等信息。字符长度不超过20480 > 中文字符必须为UTF-8或者unicode编码。

        :param body_remark: The body_remark of this ListApiVersionDetailV2Response.
        :type body_remark: str
        """
        self._body_remark = body_remark

    @property
    def result_normal_sample(self):
        """Gets the result_normal_sample of this ListApiVersionDetailV2Response.

        正常响应示例，描述API的正常返回信息。字符长度不超过20480 > 中文字符必须为UTF-8或者unicode编码。  当API的请求协议为GRPC类型时不支持配置。

        :return: The result_normal_sample of this ListApiVersionDetailV2Response.
        :rtype: str
        """
        return self._result_normal_sample

    @result_normal_sample.setter
    def result_normal_sample(self, result_normal_sample):
        """Sets the result_normal_sample of this ListApiVersionDetailV2Response.

        正常响应示例，描述API的正常返回信息。字符长度不超过20480 > 中文字符必须为UTF-8或者unicode编码。  当API的请求协议为GRPC类型时不支持配置。

        :param result_normal_sample: The result_normal_sample of this ListApiVersionDetailV2Response.
        :type result_normal_sample: str
        """
        self._result_normal_sample = result_normal_sample

    @property
    def result_failure_sample(self):
        """Gets the result_failure_sample of this ListApiVersionDetailV2Response.

        失败返回示例，描述API的异常返回信息。字符长度不超过20480 > 中文字符必须为UTF-8或者unicode编码。  当API的请求协议为GRPC类型时不支持配置。

        :return: The result_failure_sample of this ListApiVersionDetailV2Response.
        :rtype: str
        """
        return self._result_failure_sample

    @result_failure_sample.setter
    def result_failure_sample(self, result_failure_sample):
        """Sets the result_failure_sample of this ListApiVersionDetailV2Response.

        失败返回示例，描述API的异常返回信息。字符长度不超过20480 > 中文字符必须为UTF-8或者unicode编码。  当API的请求协议为GRPC类型时不支持配置。

        :param result_failure_sample: The result_failure_sample of this ListApiVersionDetailV2Response.
        :type result_failure_sample: str
        """
        self._result_failure_sample = result_failure_sample

    @property
    def authorizer_id(self):
        """Gets the authorizer_id of this ListApiVersionDetailV2Response.

        前端自定义认证对象的ID，API请求协议为GRPC类型时不支持前端自定义认证

        :return: The authorizer_id of this ListApiVersionDetailV2Response.
        :rtype: str
        """
        return self._authorizer_id

    @authorizer_id.setter
    def authorizer_id(self, authorizer_id):
        """Sets the authorizer_id of this ListApiVersionDetailV2Response.

        前端自定义认证对象的ID，API请求协议为GRPC类型时不支持前端自定义认证

        :param authorizer_id: The authorizer_id of this ListApiVersionDetailV2Response.
        :type authorizer_id: str
        """
        self._authorizer_id = authorizer_id

    @property
    def tags(self):
        """Gets the tags of this ListApiVersionDetailV2Response.

        标签。  支持英文，数字，中文，特殊符号（-*#%.:_），且只能以中文或英文开头。  默认支持10个标签，如需扩大配额请联系技术工程师修改API_TAG_NUM_LIMIT配置。 

        :return: The tags of this ListApiVersionDetailV2Response.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListApiVersionDetailV2Response.

        标签。  支持英文，数字，中文，特殊符号（-*#%.:_），且只能以中文或英文开头。  默认支持10个标签，如需扩大配额请联系技术工程师修改API_TAG_NUM_LIMIT配置。 

        :param tags: The tags of this ListApiVersionDetailV2Response.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def response_id(self):
        """Gets the response_id of this ListApiVersionDetailV2Response.

        分组自定义响应ID

        :return: The response_id of this ListApiVersionDetailV2Response.
        :rtype: str
        """
        return self._response_id

    @response_id.setter
    def response_id(self, response_id):
        """Sets the response_id of this ListApiVersionDetailV2Response.

        分组自定义响应ID

        :param response_id: The response_id of this ListApiVersionDetailV2Response.
        :type response_id: str
        """
        self._response_id = response_id

    @property
    def roma_app_id(self):
        """Gets the roma_app_id of this ListApiVersionDetailV2Response.

        集成应用ID  暂不支持

        :return: The roma_app_id of this ListApiVersionDetailV2Response.
        :rtype: str
        """
        return self._roma_app_id

    @roma_app_id.setter
    def roma_app_id(self, roma_app_id):
        """Sets the roma_app_id of this ListApiVersionDetailV2Response.

        集成应用ID  暂不支持

        :param roma_app_id: The roma_app_id of this ListApiVersionDetailV2Response.
        :type roma_app_id: str
        """
        self._roma_app_id = roma_app_id

    @property
    def domain_name(self):
        """Gets the domain_name of this ListApiVersionDetailV2Response.

        API绑定的自定义域名  暂不支持

        :return: The domain_name of this ListApiVersionDetailV2Response.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ListApiVersionDetailV2Response.

        API绑定的自定义域名  暂不支持

        :param domain_name: The domain_name of this ListApiVersionDetailV2Response.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def tag(self):
        """Gets the tag of this ListApiVersionDetailV2Response.

        标签  待废弃，优先使用tags字段

        :return: The tag of this ListApiVersionDetailV2Response.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ListApiVersionDetailV2Response.

        标签  待废弃，优先使用tags字段

        :param tag: The tag of this ListApiVersionDetailV2Response.
        :type tag: str
        """
        self._tag = tag

    @property
    def content_type(self):
        """Gets the content_type of this ListApiVersionDetailV2Response.

        请求内容格式类型：  application/json application/xml multipart/form-data text/plain  暂不支持

        :return: The content_type of this ListApiVersionDetailV2Response.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this ListApiVersionDetailV2Response.

        请求内容格式类型：  application/json application/xml multipart/form-data text/plain  暂不支持

        :param content_type: The content_type of this ListApiVersionDetailV2Response.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def id(self):
        """Gets the id of this ListApiVersionDetailV2Response.

        API编号

        :return: The id of this ListApiVersionDetailV2Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListApiVersionDetailV2Response.

        API编号

        :param id: The id of this ListApiVersionDetailV2Response.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this ListApiVersionDetailV2Response.

        API状态   - 1： 有效

        :return: The status of this ListApiVersionDetailV2Response.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListApiVersionDetailV2Response.

        API状态   - 1： 有效

        :param status: The status of this ListApiVersionDetailV2Response.
        :type status: int
        """
        self._status = status

    @property
    def arrange_necessary(self):
        """Gets the arrange_necessary of this ListApiVersionDetailV2Response.

        是否需要编排

        :return: The arrange_necessary of this ListApiVersionDetailV2Response.
        :rtype: int
        """
        return self._arrange_necessary

    @arrange_necessary.setter
    def arrange_necessary(self, arrange_necessary):
        """Sets the arrange_necessary of this ListApiVersionDetailV2Response.

        是否需要编排

        :param arrange_necessary: The arrange_necessary of this ListApiVersionDetailV2Response.
        :type arrange_necessary: int
        """
        self._arrange_necessary = arrange_necessary

    @property
    def register_time(self):
        """Gets the register_time of this ListApiVersionDetailV2Response.

        API注册时间

        :return: The register_time of this ListApiVersionDetailV2Response.
        :rtype: datetime
        """
        return self._register_time

    @register_time.setter
    def register_time(self, register_time):
        """Sets the register_time of this ListApiVersionDetailV2Response.

        API注册时间

        :param register_time: The register_time of this ListApiVersionDetailV2Response.
        :type register_time: datetime
        """
        self._register_time = register_time

    @property
    def update_time(self):
        """Gets the update_time of this ListApiVersionDetailV2Response.

        API修改时间

        :return: The update_time of this ListApiVersionDetailV2Response.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ListApiVersionDetailV2Response.

        API修改时间

        :param update_time: The update_time of this ListApiVersionDetailV2Response.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def group_name(self):
        """Gets the group_name of this ListApiVersionDetailV2Response.

        API所属分组的名称

        :return: The group_name of this ListApiVersionDetailV2Response.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this ListApiVersionDetailV2Response.

        API所属分组的名称

        :param group_name: The group_name of this ListApiVersionDetailV2Response.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def group_version(self):
        """Gets the group_version of this ListApiVersionDetailV2Response.

        API所属分组的版本  默认V1，其他版本暂不支持

        :return: The group_version of this ListApiVersionDetailV2Response.
        :rtype: str
        """
        return self._group_version

    @group_version.setter
    def group_version(self, group_version):
        """Sets the group_version of this ListApiVersionDetailV2Response.

        API所属分组的版本  默认V1，其他版本暂不支持

        :param group_version: The group_version of this ListApiVersionDetailV2Response.
        :type group_version: str
        """
        self._group_version = group_version

    @property
    def run_env_id(self):
        """Gets the run_env_id of this ListApiVersionDetailV2Response.

        发布的环境编号  存在多个发布记录时，环境编号之间用|隔开

        :return: The run_env_id of this ListApiVersionDetailV2Response.
        :rtype: str
        """
        return self._run_env_id

    @run_env_id.setter
    def run_env_id(self, run_env_id):
        """Sets the run_env_id of this ListApiVersionDetailV2Response.

        发布的环境编号  存在多个发布记录时，环境编号之间用|隔开

        :param run_env_id: The run_env_id of this ListApiVersionDetailV2Response.
        :type run_env_id: str
        """
        self._run_env_id = run_env_id

    @property
    def run_env_name(self):
        """Gets the run_env_name of this ListApiVersionDetailV2Response.

        发布的环境名称  存在多个发布记录时，环境名称之间用|隔开

        :return: The run_env_name of this ListApiVersionDetailV2Response.
        :rtype: str
        """
        return self._run_env_name

    @run_env_name.setter
    def run_env_name(self, run_env_name):
        """Sets the run_env_name of this ListApiVersionDetailV2Response.

        发布的环境名称  存在多个发布记录时，环境名称之间用|隔开

        :param run_env_name: The run_env_name of this ListApiVersionDetailV2Response.
        :type run_env_name: str
        """
        self._run_env_name = run_env_name

    @property
    def publish_id(self):
        """Gets the publish_id of this ListApiVersionDetailV2Response.

        发布记录编号  存在多个发布记录时，发布记录编号之间用|隔开

        :return: The publish_id of this ListApiVersionDetailV2Response.
        :rtype: str
        """
        return self._publish_id

    @publish_id.setter
    def publish_id(self, publish_id):
        """Sets the publish_id of this ListApiVersionDetailV2Response.

        发布记录编号  存在多个发布记录时，发布记录编号之间用|隔开

        :param publish_id: The publish_id of this ListApiVersionDetailV2Response.
        :type publish_id: str
        """
        self._publish_id = publish_id

    @property
    def publish_time(self):
        """Gets the publish_time of this ListApiVersionDetailV2Response.

        版本发布时间

        :return: The publish_time of this ListApiVersionDetailV2Response.
        :rtype: datetime
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        """Sets the publish_time of this ListApiVersionDetailV2Response.

        版本发布时间

        :param publish_time: The publish_time of this ListApiVersionDetailV2Response.
        :type publish_time: datetime
        """
        self._publish_time = publish_time

    @property
    def roma_app_name(self):
        """Gets the roma_app_name of this ListApiVersionDetailV2Response.

        API归属的集成应用名称  暂不支持

        :return: The roma_app_name of this ListApiVersionDetailV2Response.
        :rtype: str
        """
        return self._roma_app_name

    @roma_app_name.setter
    def roma_app_name(self, roma_app_name):
        """Sets the roma_app_name of this ListApiVersionDetailV2Response.

        API归属的集成应用名称  暂不支持

        :param roma_app_name: The roma_app_name of this ListApiVersionDetailV2Response.
        :type roma_app_name: str
        """
        self._roma_app_name = roma_app_name

    @property
    def ld_api_id(self):
        """Gets the ld_api_id of this ListApiVersionDetailV2Response.

        当API的后端为自定义后端时，对应的自定义后端API编号  暂不支持

        :return: The ld_api_id of this ListApiVersionDetailV2Response.
        :rtype: str
        """
        return self._ld_api_id

    @ld_api_id.setter
    def ld_api_id(self, ld_api_id):
        """Sets the ld_api_id of this ListApiVersionDetailV2Response.

        当API的后端为自定义后端时，对应的自定义后端API编号  暂不支持

        :param ld_api_id: The ld_api_id of this ListApiVersionDetailV2Response.
        :type ld_api_id: str
        """
        self._ld_api_id = ld_api_id

    @property
    def backend_api(self):
        """Gets the backend_api of this ListApiVersionDetailV2Response.

        :return: The backend_api of this ListApiVersionDetailV2Response.
        :rtype: :class:`huaweicloudsdkapig.v2.BackendApi`
        """
        return self._backend_api

    @backend_api.setter
    def backend_api(self, backend_api):
        """Sets the backend_api of this ListApiVersionDetailV2Response.

        :param backend_api: The backend_api of this ListApiVersionDetailV2Response.
        :type backend_api: :class:`huaweicloudsdkapig.v2.BackendApi`
        """
        self._backend_api = backend_api

    @property
    def api_group_info(self):
        """Gets the api_group_info of this ListApiVersionDetailV2Response.

        :return: The api_group_info of this ListApiVersionDetailV2Response.
        :rtype: :class:`huaweicloudsdkapig.v2.ApiGroupCommonInfo`
        """
        return self._api_group_info

    @api_group_info.setter
    def api_group_info(self, api_group_info):
        """Sets the api_group_info of this ListApiVersionDetailV2Response.

        :param api_group_info: The api_group_info of this ListApiVersionDetailV2Response.
        :type api_group_info: :class:`huaweicloudsdkapig.v2.ApiGroupCommonInfo`
        """
        self._api_group_info = api_group_info

    @property
    def func_info(self):
        """Gets the func_info of this ListApiVersionDetailV2Response.

        :return: The func_info of this ListApiVersionDetailV2Response.
        :rtype: :class:`huaweicloudsdkapig.v2.ApiFunc`
        """
        return self._func_info

    @func_info.setter
    def func_info(self, func_info):
        """Sets the func_info of this ListApiVersionDetailV2Response.

        :param func_info: The func_info of this ListApiVersionDetailV2Response.
        :type func_info: :class:`huaweicloudsdkapig.v2.ApiFunc`
        """
        self._func_info = func_info

    @property
    def mock_info(self):
        """Gets the mock_info of this ListApiVersionDetailV2Response.

        :return: The mock_info of this ListApiVersionDetailV2Response.
        :rtype: :class:`huaweicloudsdkapig.v2.ApiMock`
        """
        return self._mock_info

    @mock_info.setter
    def mock_info(self, mock_info):
        """Sets the mock_info of this ListApiVersionDetailV2Response.

        :param mock_info: The mock_info of this ListApiVersionDetailV2Response.
        :type mock_info: :class:`huaweicloudsdkapig.v2.ApiMock`
        """
        self._mock_info = mock_info

    @property
    def req_params(self):
        """Gets the req_params of this ListApiVersionDetailV2Response.

        API的请求参数列表

        :return: The req_params of this ListApiVersionDetailV2Response.
        :rtype: list[:class:`huaweicloudsdkapig.v2.ReqParam`]
        """
        return self._req_params

    @req_params.setter
    def req_params(self, req_params):
        """Sets the req_params of this ListApiVersionDetailV2Response.

        API的请求参数列表

        :param req_params: The req_params of this ListApiVersionDetailV2Response.
        :type req_params: list[:class:`huaweicloudsdkapig.v2.ReqParam`]
        """
        self._req_params = req_params

    @property
    def backend_params(self):
        """Gets the backend_params of this ListApiVersionDetailV2Response.

        API的后端参数列表

        :return: The backend_params of this ListApiVersionDetailV2Response.
        :rtype: list[:class:`huaweicloudsdkapig.v2.BackendParam`]
        """
        return self._backend_params

    @backend_params.setter
    def backend_params(self, backend_params):
        """Sets the backend_params of this ListApiVersionDetailV2Response.

        API的后端参数列表

        :param backend_params: The backend_params of this ListApiVersionDetailV2Response.
        :type backend_params: list[:class:`huaweicloudsdkapig.v2.BackendParam`]
        """
        self._backend_params = backend_params

    @property
    def policy_functions(self):
        """Gets the policy_functions of this ListApiVersionDetailV2Response.

        函数工作流策略后端列表

        :return: The policy_functions of this ListApiVersionDetailV2Response.
        :rtype: list[:class:`huaweicloudsdkapig.v2.ApiPolicyFunctionResp`]
        """
        return self._policy_functions

    @policy_functions.setter
    def policy_functions(self, policy_functions):
        """Sets the policy_functions of this ListApiVersionDetailV2Response.

        函数工作流策略后端列表

        :param policy_functions: The policy_functions of this ListApiVersionDetailV2Response.
        :type policy_functions: list[:class:`huaweicloudsdkapig.v2.ApiPolicyFunctionResp`]
        """
        self._policy_functions = policy_functions

    @property
    def policy_mocks(self):
        """Gets the policy_mocks of this ListApiVersionDetailV2Response.

        mock策略后端列表

        :return: The policy_mocks of this ListApiVersionDetailV2Response.
        :rtype: list[:class:`huaweicloudsdkapig.v2.ApiPolicyMockResp`]
        """
        return self._policy_mocks

    @policy_mocks.setter
    def policy_mocks(self, policy_mocks):
        """Sets the policy_mocks of this ListApiVersionDetailV2Response.

        mock策略后端列表

        :param policy_mocks: The policy_mocks of this ListApiVersionDetailV2Response.
        :type policy_mocks: list[:class:`huaweicloudsdkapig.v2.ApiPolicyMockResp`]
        """
        self._policy_mocks = policy_mocks

    @property
    def policy_https(self):
        """Gets the policy_https of this ListApiVersionDetailV2Response.

        web策略后端列表

        :return: The policy_https of this ListApiVersionDetailV2Response.
        :rtype: list[:class:`huaweicloudsdkapig.v2.ApiPolicyHttpResp`]
        """
        return self._policy_https

    @policy_https.setter
    def policy_https(self, policy_https):
        """Sets the policy_https of this ListApiVersionDetailV2Response.

        web策略后端列表

        :param policy_https: The policy_https of this ListApiVersionDetailV2Response.
        :type policy_https: list[:class:`huaweicloudsdkapig.v2.ApiPolicyHttpResp`]
        """
        self._policy_https = policy_https

    @property
    def sl_domain(self):
        """Gets the sl_domain of this ListApiVersionDetailV2Response.

        系统默认分配的子域名

        :return: The sl_domain of this ListApiVersionDetailV2Response.
        :rtype: str
        """
        return self._sl_domain

    @sl_domain.setter
    def sl_domain(self, sl_domain):
        """Sets the sl_domain of this ListApiVersionDetailV2Response.

        系统默认分配的子域名

        :param sl_domain: The sl_domain of this ListApiVersionDetailV2Response.
        :type sl_domain: str
        """
        self._sl_domain = sl_domain

    @property
    def sl_domains(self):
        """Gets the sl_domains of this ListApiVersionDetailV2Response.

        系统默认分配的子域名列表

        :return: The sl_domains of this ListApiVersionDetailV2Response.
        :rtype: list[str]
        """
        return self._sl_domains

    @sl_domains.setter
    def sl_domains(self, sl_domains):
        """Sets the sl_domains of this ListApiVersionDetailV2Response.

        系统默认分配的子域名列表

        :param sl_domains: The sl_domains of this ListApiVersionDetailV2Response.
        :type sl_domains: list[str]
        """
        self._sl_domains = sl_domains

    @property
    def version_id(self):
        """Gets the version_id of this ListApiVersionDetailV2Response.

        版本编号

        :return: The version_id of this ListApiVersionDetailV2Response.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this ListApiVersionDetailV2Response.

        版本编号

        :param version_id: The version_id of this ListApiVersionDetailV2Response.
        :type version_id: str
        """
        self._version_id = version_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListApiVersionDetailV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
