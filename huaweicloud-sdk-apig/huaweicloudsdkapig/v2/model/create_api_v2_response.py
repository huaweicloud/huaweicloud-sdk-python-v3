# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreateApiV2Response(SdkResponse):


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
        'func_info': 'ApiFunc',
        'mock_info': 'ApiMock',
        'req_params': 'list[ReqParam]',
        'backend_params': 'list[BackendParam]',
        'policy_functions': 'list[ApiPolicyFunctionResp]',
        'policy_mocks': 'list[ApiPolicyMockResp]',
        'backend_api': 'BackendApi',
        'policy_https': 'list[ApiPolicyHttpResp]'
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
        'func_info': 'func_info',
        'mock_info': 'mock_info',
        'req_params': 'req_params',
        'backend_params': 'backend_params',
        'policy_functions': 'policy_functions',
        'policy_mocks': 'policy_mocks',
        'backend_api': 'backend_api',
        'policy_https': 'policy_https'
    }

    def __init__(self, name=None, type=None, version=None, req_protocol='HTTPS', req_method=None, req_uri=None, auth_type=None, auth_opt=None, cors=False, match_mode=None, backend_type=None, remark=None, group_id=None, body_remark=None, result_normal_sample=None, result_failure_sample=None, authorizer_id=None, tags=None, response_id=None, roma_app_id=None, domain_name=None, tag=None, id=None, status=None, arrange_necessary=None, register_time=None, update_time=None, group_name=None, group_version='V1', run_env_id=None, run_env_name=None, publish_id=None, func_info=None, mock_info=None, req_params=None, backend_params=None, policy_functions=None, policy_mocks=None, backend_api=None, policy_https=None):
        """CreateApiV2Response - a model defined in huaweicloud sdk"""
        
        super().__init__()

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
        self._func_info = None
        self._mock_info = None
        self._req_params = None
        self._backend_params = None
        self._policy_functions = None
        self._policy_mocks = None
        self._backend_api = None
        self._policy_https = None
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
        if backend_api is not None:
            self.backend_api = backend_api
        if policy_https is not None:
            self.policy_https = policy_https

    @property
    def name(self):
        """Gets the name of this CreateApiV2Response.

        API名称长度。  为3 ~ 64位的字符串，字符串由中文、英文字母、数字、下划线组成，且只能以英文或中文开头。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The name of this CreateApiV2Response.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateApiV2Response.

        API名称长度。  为3 ~ 64位的字符串，字符串由中文、英文字母、数字、下划线组成，且只能以英文或中文开头。 > 中文字符必须为UTF-8或者unicode编码。

        :param name: The name of this CreateApiV2Response.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this CreateApiV2Response.

        API类型 - 1：公有API - 2：私有API

        :return: The type of this CreateApiV2Response.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateApiV2Response.

        API类型 - 1：公有API - 2：私有API

        :param type: The type of this CreateApiV2Response.
        :type: int
        """
        self._type = type

    @property
    def version(self):
        """Gets the version of this CreateApiV2Response.

        API的版本

        :return: The version of this CreateApiV2Response.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CreateApiV2Response.

        API的版本

        :param version: The version of this CreateApiV2Response.
        :type: str
        """
        self._version = version

    @property
    def req_protocol(self):
        """Gets the req_protocol of this CreateApiV2Response.

        API的请求协议 - HTTP - HTTPS - BOTH：同时支持HTTP和HTTPS

        :return: The req_protocol of this CreateApiV2Response.
        :rtype: str
        """
        return self._req_protocol

    @req_protocol.setter
    def req_protocol(self, req_protocol):
        """Sets the req_protocol of this CreateApiV2Response.

        API的请求协议 - HTTP - HTTPS - BOTH：同时支持HTTP和HTTPS

        :param req_protocol: The req_protocol of this CreateApiV2Response.
        :type: str
        """
        self._req_protocol = req_protocol

    @property
    def req_method(self):
        """Gets the req_method of this CreateApiV2Response.

        API的请求方式

        :return: The req_method of this CreateApiV2Response.
        :rtype: str
        """
        return self._req_method

    @req_method.setter
    def req_method(self, req_method):
        """Sets the req_method of this CreateApiV2Response.

        API的请求方式

        :param req_method: The req_method of this CreateApiV2Response.
        :type: str
        """
        self._req_method = req_method

    @property
    def req_uri(self):
        """Gets the req_uri of this CreateApiV2Response.

        请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ . 等特殊字符，总长度不超过512，且满足URI规范。  支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、中划线、下划线组成，且只能以英文开头。 > 需要服从URI规范。

        :return: The req_uri of this CreateApiV2Response.
        :rtype: str
        """
        return self._req_uri

    @req_uri.setter
    def req_uri(self, req_uri):
        """Sets the req_uri of this CreateApiV2Response.

        请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ . 等特殊字符，总长度不超过512，且满足URI规范。  支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、中划线、下划线组成，且只能以英文开头。 > 需要服从URI规范。

        :param req_uri: The req_uri of this CreateApiV2Response.
        :type: str
        """
        self._req_uri = req_uri

    @property
    def auth_type(self):
        """Gets the auth_type of this CreateApiV2Response.

        API的认证方式 - NONE：无认证 - APP：APP认证 - IAM：IAM认证 - AUTHORIZER：自定义认证

        :return: The auth_type of this CreateApiV2Response.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this CreateApiV2Response.

        API的认证方式 - NONE：无认证 - APP：APP认证 - IAM：IAM认证 - AUTHORIZER：自定义认证

        :param auth_type: The auth_type of this CreateApiV2Response.
        :type: str
        """
        self._auth_type = auth_type

    @property
    def auth_opt(self):
        """Gets the auth_opt of this CreateApiV2Response.


        :return: The auth_opt of this CreateApiV2Response.
        :rtype: AuthOpt
        """
        return self._auth_opt

    @auth_opt.setter
    def auth_opt(self, auth_opt):
        """Sets the auth_opt of this CreateApiV2Response.


        :param auth_opt: The auth_opt of this CreateApiV2Response.
        :type: AuthOpt
        """
        self._auth_opt = auth_opt

    @property
    def cors(self):
        """Gets the cors of this CreateApiV2Response.

        是否支持跨域 - TRUE：支持 - FALSE：不支持

        :return: The cors of this CreateApiV2Response.
        :rtype: bool
        """
        return self._cors

    @cors.setter
    def cors(self, cors):
        """Sets the cors of this CreateApiV2Response.

        是否支持跨域 - TRUE：支持 - FALSE：不支持

        :param cors: The cors of this CreateApiV2Response.
        :type: bool
        """
        self._cors = cors

    @property
    def match_mode(self):
        """Gets the match_mode of this CreateApiV2Response.

        API的匹配方式 - SWA：前缀匹配 - NORMAL：正常匹配（绝对匹配） 默认：NORMAL

        :return: The match_mode of this CreateApiV2Response.
        :rtype: str
        """
        return self._match_mode

    @match_mode.setter
    def match_mode(self, match_mode):
        """Sets the match_mode of this CreateApiV2Response.

        API的匹配方式 - SWA：前缀匹配 - NORMAL：正常匹配（绝对匹配） 默认：NORMAL

        :param match_mode: The match_mode of this CreateApiV2Response.
        :type: str
        """
        self._match_mode = match_mode

    @property
    def backend_type(self):
        """Gets the backend_type of this CreateApiV2Response.

        后端类型 - HTTP：web后端 - FUNCTION：函数工作流 - MOCK：模拟的后端

        :return: The backend_type of this CreateApiV2Response.
        :rtype: str
        """
        return self._backend_type

    @backend_type.setter
    def backend_type(self, backend_type):
        """Sets the backend_type of this CreateApiV2Response.

        后端类型 - HTTP：web后端 - FUNCTION：函数工作流 - MOCK：模拟的后端

        :param backend_type: The backend_type of this CreateApiV2Response.
        :type: str
        """
        self._backend_type = backend_type

    @property
    def remark(self):
        """Gets the remark of this CreateApiV2Response.

        API描述。字符长度不超过255 > 中文字符必须为UTF-8或者unicode编码。

        :return: The remark of this CreateApiV2Response.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this CreateApiV2Response.

        API描述。字符长度不超过255 > 中文字符必须为UTF-8或者unicode编码。

        :param remark: The remark of this CreateApiV2Response.
        :type: str
        """
        self._remark = remark

    @property
    def group_id(self):
        """Gets the group_id of this CreateApiV2Response.

        API所属的分组编号

        :return: The group_id of this CreateApiV2Response.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this CreateApiV2Response.

        API所属的分组编号

        :param group_id: The group_id of this CreateApiV2Response.
        :type: str
        """
        self._group_id = group_id

    @property
    def body_remark(self):
        """Gets the body_remark of this CreateApiV2Response.

        API请求体描述，可以是请求体示例、媒体类型、参数等信息。字符长度不超过20480 > 中文字符必须为UTF-8或者unicode编码。

        :return: The body_remark of this CreateApiV2Response.
        :rtype: str
        """
        return self._body_remark

    @body_remark.setter
    def body_remark(self, body_remark):
        """Sets the body_remark of this CreateApiV2Response.

        API请求体描述，可以是请求体示例、媒体类型、参数等信息。字符长度不超过20480 > 中文字符必须为UTF-8或者unicode编码。

        :param body_remark: The body_remark of this CreateApiV2Response.
        :type: str
        """
        self._body_remark = body_remark

    @property
    def result_normal_sample(self):
        """Gets the result_normal_sample of this CreateApiV2Response.

        正常响应示例，描述API的正常返回信息。字符长度不超过20480 > 中文字符必须为UTF-8或者unicode编码。

        :return: The result_normal_sample of this CreateApiV2Response.
        :rtype: str
        """
        return self._result_normal_sample

    @result_normal_sample.setter
    def result_normal_sample(self, result_normal_sample):
        """Sets the result_normal_sample of this CreateApiV2Response.

        正常响应示例，描述API的正常返回信息。字符长度不超过20480 > 中文字符必须为UTF-8或者unicode编码。

        :param result_normal_sample: The result_normal_sample of this CreateApiV2Response.
        :type: str
        """
        self._result_normal_sample = result_normal_sample

    @property
    def result_failure_sample(self):
        """Gets the result_failure_sample of this CreateApiV2Response.

        失败返回示例，描述API的异常返回信息。字符长度不超过20480 > 中文字符必须为UTF-8或者unicode编码。

        :return: The result_failure_sample of this CreateApiV2Response.
        :rtype: str
        """
        return self._result_failure_sample

    @result_failure_sample.setter
    def result_failure_sample(self, result_failure_sample):
        """Sets the result_failure_sample of this CreateApiV2Response.

        失败返回示例，描述API的异常返回信息。字符长度不超过20480 > 中文字符必须为UTF-8或者unicode编码。

        :param result_failure_sample: The result_failure_sample of this CreateApiV2Response.
        :type: str
        """
        self._result_failure_sample = result_failure_sample

    @property
    def authorizer_id(self):
        """Gets the authorizer_id of this CreateApiV2Response.

        前端自定义认证对象的ID

        :return: The authorizer_id of this CreateApiV2Response.
        :rtype: str
        """
        return self._authorizer_id

    @authorizer_id.setter
    def authorizer_id(self, authorizer_id):
        """Sets the authorizer_id of this CreateApiV2Response.

        前端自定义认证对象的ID

        :param authorizer_id: The authorizer_id of this CreateApiV2Response.
        :type: str
        """
        self._authorizer_id = authorizer_id

    @property
    def tags(self):
        """Gets the tags of this CreateApiV2Response.

        标签。  支持英文，数字，下划线，且只能以英文开头。支持输入多个标签，不同标签以英文逗号分割。 

        :return: The tags of this CreateApiV2Response.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateApiV2Response.

        标签。  支持英文，数字，下划线，且只能以英文开头。支持输入多个标签，不同标签以英文逗号分割。 

        :param tags: The tags of this CreateApiV2Response.
        :type: list[str]
        """
        self._tags = tags

    @property
    def response_id(self):
        """Gets the response_id of this CreateApiV2Response.

        分组自定义响应ID

        :return: The response_id of this CreateApiV2Response.
        :rtype: str
        """
        return self._response_id

    @response_id.setter
    def response_id(self, response_id):
        """Sets the response_id of this CreateApiV2Response.

        分组自定义响应ID

        :param response_id: The response_id of this CreateApiV2Response.
        :type: str
        """
        self._response_id = response_id

    @property
    def roma_app_id(self):
        """Gets the roma_app_id of this CreateApiV2Response.

        集成应用ID  暂不支持

        :return: The roma_app_id of this CreateApiV2Response.
        :rtype: str
        """
        return self._roma_app_id

    @roma_app_id.setter
    def roma_app_id(self, roma_app_id):
        """Sets the roma_app_id of this CreateApiV2Response.

        集成应用ID  暂不支持

        :param roma_app_id: The roma_app_id of this CreateApiV2Response.
        :type: str
        """
        self._roma_app_id = roma_app_id

    @property
    def domain_name(self):
        """Gets the domain_name of this CreateApiV2Response.

        API绑定的自定义域名  暂不支持

        :return: The domain_name of this CreateApiV2Response.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this CreateApiV2Response.

        API绑定的自定义域名  暂不支持

        :param domain_name: The domain_name of this CreateApiV2Response.
        :type: str
        """
        self._domain_name = domain_name

    @property
    def tag(self):
        """Gets the tag of this CreateApiV2Response.

        标签  待废弃，优先使用tags字段

        :return: The tag of this CreateApiV2Response.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this CreateApiV2Response.

        标签  待废弃，优先使用tags字段

        :param tag: The tag of this CreateApiV2Response.
        :type: str
        """
        self._tag = tag

    @property
    def id(self):
        """Gets the id of this CreateApiV2Response.

        API编号

        :return: The id of this CreateApiV2Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateApiV2Response.

        API编号

        :param id: The id of this CreateApiV2Response.
        :type: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this CreateApiV2Response.

        API的状态

        :return: The status of this CreateApiV2Response.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateApiV2Response.

        API的状态

        :param status: The status of this CreateApiV2Response.
        :type: int
        """
        self._status = status

    @property
    def arrange_necessary(self):
        """Gets the arrange_necessary of this CreateApiV2Response.

        是否需要编排

        :return: The arrange_necessary of this CreateApiV2Response.
        :rtype: int
        """
        return self._arrange_necessary

    @arrange_necessary.setter
    def arrange_necessary(self, arrange_necessary):
        """Sets the arrange_necessary of this CreateApiV2Response.

        是否需要编排

        :param arrange_necessary: The arrange_necessary of this CreateApiV2Response.
        :type: int
        """
        self._arrange_necessary = arrange_necessary

    @property
    def register_time(self):
        """Gets the register_time of this CreateApiV2Response.

        API注册时间

        :return: The register_time of this CreateApiV2Response.
        :rtype: datetime
        """
        return self._register_time

    @register_time.setter
    def register_time(self, register_time):
        """Sets the register_time of this CreateApiV2Response.

        API注册时间

        :param register_time: The register_time of this CreateApiV2Response.
        :type: datetime
        """
        self._register_time = register_time

    @property
    def update_time(self):
        """Gets the update_time of this CreateApiV2Response.

        API修改时间

        :return: The update_time of this CreateApiV2Response.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this CreateApiV2Response.

        API修改时间

        :param update_time: The update_time of this CreateApiV2Response.
        :type: datetime
        """
        self._update_time = update_time

    @property
    def group_name(self):
        """Gets the group_name of this CreateApiV2Response.

        API所属分组的名称

        :return: The group_name of this CreateApiV2Response.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this CreateApiV2Response.

        API所属分组的名称

        :param group_name: The group_name of this CreateApiV2Response.
        :type: str
        """
        self._group_name = group_name

    @property
    def group_version(self):
        """Gets the group_version of this CreateApiV2Response.

        API所属分组的版本  默认V1，其他版本暂不支持

        :return: The group_version of this CreateApiV2Response.
        :rtype: str
        """
        return self._group_version

    @group_version.setter
    def group_version(self, group_version):
        """Sets the group_version of this CreateApiV2Response.

        API所属分组的版本  默认V1，其他版本暂不支持

        :param group_version: The group_version of this CreateApiV2Response.
        :type: str
        """
        self._group_version = group_version

    @property
    def run_env_id(self):
        """Gets the run_env_id of this CreateApiV2Response.

        发布的环境id

        :return: The run_env_id of this CreateApiV2Response.
        :rtype: str
        """
        return self._run_env_id

    @run_env_id.setter
    def run_env_id(self, run_env_id):
        """Sets the run_env_id of this CreateApiV2Response.

        发布的环境id

        :param run_env_id: The run_env_id of this CreateApiV2Response.
        :type: str
        """
        self._run_env_id = run_env_id

    @property
    def run_env_name(self):
        """Gets the run_env_name of this CreateApiV2Response.

        发布的环境名称

        :return: The run_env_name of this CreateApiV2Response.
        :rtype: str
        """
        return self._run_env_name

    @run_env_name.setter
    def run_env_name(self, run_env_name):
        """Sets the run_env_name of this CreateApiV2Response.

        发布的环境名称

        :param run_env_name: The run_env_name of this CreateApiV2Response.
        :type: str
        """
        self._run_env_name = run_env_name

    @property
    def publish_id(self):
        """Gets the publish_id of this CreateApiV2Response.

        发布记录编号  存在多个发布记录时，编号之间用|隔开

        :return: The publish_id of this CreateApiV2Response.
        :rtype: str
        """
        return self._publish_id

    @publish_id.setter
    def publish_id(self, publish_id):
        """Sets the publish_id of this CreateApiV2Response.

        发布记录编号  存在多个发布记录时，编号之间用|隔开

        :param publish_id: The publish_id of this CreateApiV2Response.
        :type: str
        """
        self._publish_id = publish_id

    @property
    def func_info(self):
        """Gets the func_info of this CreateApiV2Response.


        :return: The func_info of this CreateApiV2Response.
        :rtype: ApiFunc
        """
        return self._func_info

    @func_info.setter
    def func_info(self, func_info):
        """Sets the func_info of this CreateApiV2Response.


        :param func_info: The func_info of this CreateApiV2Response.
        :type: ApiFunc
        """
        self._func_info = func_info

    @property
    def mock_info(self):
        """Gets the mock_info of this CreateApiV2Response.


        :return: The mock_info of this CreateApiV2Response.
        :rtype: ApiMock
        """
        return self._mock_info

    @mock_info.setter
    def mock_info(self, mock_info):
        """Sets the mock_info of this CreateApiV2Response.


        :param mock_info: The mock_info of this CreateApiV2Response.
        :type: ApiMock
        """
        self._mock_info = mock_info

    @property
    def req_params(self):
        """Gets the req_params of this CreateApiV2Response.

        API的请求参数列表

        :return: The req_params of this CreateApiV2Response.
        :rtype: list[ReqParam]
        """
        return self._req_params

    @req_params.setter
    def req_params(self, req_params):
        """Sets the req_params of this CreateApiV2Response.

        API的请求参数列表

        :param req_params: The req_params of this CreateApiV2Response.
        :type: list[ReqParam]
        """
        self._req_params = req_params

    @property
    def backend_params(self):
        """Gets the backend_params of this CreateApiV2Response.

        API的后端参数列表

        :return: The backend_params of this CreateApiV2Response.
        :rtype: list[BackendParam]
        """
        return self._backend_params

    @backend_params.setter
    def backend_params(self, backend_params):
        """Sets the backend_params of this CreateApiV2Response.

        API的后端参数列表

        :param backend_params: The backend_params of this CreateApiV2Response.
        :type: list[BackendParam]
        """
        self._backend_params = backend_params

    @property
    def policy_functions(self):
        """Gets the policy_functions of this CreateApiV2Response.

        函数工作流策略后端列表

        :return: The policy_functions of this CreateApiV2Response.
        :rtype: list[ApiPolicyFunctionResp]
        """
        return self._policy_functions

    @policy_functions.setter
    def policy_functions(self, policy_functions):
        """Sets the policy_functions of this CreateApiV2Response.

        函数工作流策略后端列表

        :param policy_functions: The policy_functions of this CreateApiV2Response.
        :type: list[ApiPolicyFunctionResp]
        """
        self._policy_functions = policy_functions

    @property
    def policy_mocks(self):
        """Gets the policy_mocks of this CreateApiV2Response.

        mock策略后端列表

        :return: The policy_mocks of this CreateApiV2Response.
        :rtype: list[ApiPolicyMockResp]
        """
        return self._policy_mocks

    @policy_mocks.setter
    def policy_mocks(self, policy_mocks):
        """Sets the policy_mocks of this CreateApiV2Response.

        mock策略后端列表

        :param policy_mocks: The policy_mocks of this CreateApiV2Response.
        :type: list[ApiPolicyMockResp]
        """
        self._policy_mocks = policy_mocks

    @property
    def backend_api(self):
        """Gets the backend_api of this CreateApiV2Response.


        :return: The backend_api of this CreateApiV2Response.
        :rtype: BackendApi
        """
        return self._backend_api

    @backend_api.setter
    def backend_api(self, backend_api):
        """Sets the backend_api of this CreateApiV2Response.


        :param backend_api: The backend_api of this CreateApiV2Response.
        :type: BackendApi
        """
        self._backend_api = backend_api

    @property
    def policy_https(self):
        """Gets the policy_https of this CreateApiV2Response.

        web策略后端列表

        :return: The policy_https of this CreateApiV2Response.
        :rtype: list[ApiPolicyHttpResp]
        """
        return self._policy_https

    @policy_https.setter
    def policy_https(self, policy_https):
        """Sets the policy_https of this CreateApiV2Response.

        web策略后端列表

        :param policy_https: The policy_https of this CreateApiV2Response.
        :type: list[ApiPolicyHttpResp]
        """
        self._policy_https = policy_https

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateApiV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
