# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiBaseInfo:

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
        'content_type': 'str'
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
        'content_type': 'content_type'
    }

    def __init__(self, name=None, type=None, version=None, req_protocol=None, req_method=None, req_uri=None, auth_type=None, auth_opt=None, cors=None, match_mode=None, backend_type=None, remark=None, group_id=None, body_remark=None, result_normal_sample=None, result_failure_sample=None, authorizer_id=None, tags=None, response_id=None, roma_app_id=None, domain_name=None, tag=None, content_type=None):
        """ApiBaseInfo

        The model defined in huaweicloud sdk

        :param name: API名称。  支持汉字、英文、数字、中划线、下划线、点、斜杠、中英文格式下的小括号和冒号、中文格式下的顿号，且只能以英文、汉字和数字开头。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type name: str
        :param type: API类型[，该参数暂未使用](tag:hcs;fcs;) - 1：公有API - 2：私有API
        :type type: int
        :param version: API的版本
        :type version: str
        :param req_protocol: API的请求协议 - HTTP - HTTPS - BOTH：同时支持HTTP和HTTPS
        :type req_protocol: str
        :param req_method: API的请求方式
        :type req_method: str
        :param req_uri: 请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ . 等特殊字符，总长度不超过512，且满足URI规范。 &gt; 需要服从URI规范。
        :type req_uri: str
        :param auth_type: API的认证方式[，site暂不支持IAM认证。](tag:Site) - NONE：无认证 - APP：APP认证 - IAM：IAM认证 - AUTHORIZER：自定义认证
        :type auth_type: str
        :param auth_opt: 
        :type auth_opt: :class:`huaweicloudsdkroma.v2.AuthOpt`
        :param cors: 是否支持跨域 - TRUE：支持 - FALSE：不支持
        :type cors: bool
        :param match_mode: API的匹配方式 - SWA：前缀匹配 - NORMAL：正常匹配（绝对匹配） 默认：NORMAL
        :type match_mode: str
        :param backend_type: 后端类型[，site暂不支持函数工作流。](tag:Site) - HTTP：web后端 - FUNCTION：函数工作流 - MOCK：模拟的后端
        :type backend_type: str
        :param remark: API描述。  不允许带有&lt;、&gt;字符 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type remark: str
        :param group_id: API所属的分组编号
        :type group_id: str
        :param body_remark: API请求体描述，可以是请求体示例、媒体类型、参数等信息。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type body_remark: str
        :param result_normal_sample: 正常响应示例，描述API的正常返回信息。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type result_normal_sample: str
        :param result_failure_sample: 失败返回示例，描述API的异常返回信息。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type result_failure_sample: str
        :param authorizer_id: 前端自定义认证对象的ID
        :type authorizer_id: str
        :param tags: 标签。  支持英文，数字，中文，特殊符号（-*#%.:_），且只能以中文或英文开头。支持输入多个标签，不同标签以英文逗号分割。  默认支持10个标签，如需扩大配额请联系技术工程师修改API_TAG_NUM_LIMIT配置。 
        :type tags: list[str]
        :param response_id: 分组自定义响应ID  暂不支持
        :type response_id: str
        :param roma_app_id: API归属的集成应用编号  API分组为全局分组时或API绑定自定义域名时必填。
        :type roma_app_id: str
        :param domain_name: API绑定的自定义域名，使用自定义域名时roma_app_id字段必填。
        :type domain_name: str
        :param tag: 标签  待废弃，优先使用tags字段
        :type tag: str
        :param content_type: 请求内容格式类型：  application/json application/xml multipart/form-date text/plain
        :type content_type: str
        """
        
        

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

    @property
    def name(self):
        """Gets the name of this ApiBaseInfo.

        API名称。  支持汉字、英文、数字、中划线、下划线、点、斜杠、中英文格式下的小括号和冒号、中文格式下的顿号，且只能以英文、汉字和数字开头。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The name of this ApiBaseInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiBaseInfo.

        API名称。  支持汉字、英文、数字、中划线、下划线、点、斜杠、中英文格式下的小括号和冒号、中文格式下的顿号，且只能以英文、汉字和数字开头。 > 中文字符必须为UTF-8或者unicode编码。

        :param name: The name of this ApiBaseInfo.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this ApiBaseInfo.

        API类型[，该参数暂未使用](tag:hcs;fcs;) - 1：公有API - 2：私有API

        :return: The type of this ApiBaseInfo.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ApiBaseInfo.

        API类型[，该参数暂未使用](tag:hcs;fcs;) - 1：公有API - 2：私有API

        :param type: The type of this ApiBaseInfo.
        :type type: int
        """
        self._type = type

    @property
    def version(self):
        """Gets the version of this ApiBaseInfo.

        API的版本

        :return: The version of this ApiBaseInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ApiBaseInfo.

        API的版本

        :param version: The version of this ApiBaseInfo.
        :type version: str
        """
        self._version = version

    @property
    def req_protocol(self):
        """Gets the req_protocol of this ApiBaseInfo.

        API的请求协议 - HTTP - HTTPS - BOTH：同时支持HTTP和HTTPS

        :return: The req_protocol of this ApiBaseInfo.
        :rtype: str
        """
        return self._req_protocol

    @req_protocol.setter
    def req_protocol(self, req_protocol):
        """Sets the req_protocol of this ApiBaseInfo.

        API的请求协议 - HTTP - HTTPS - BOTH：同时支持HTTP和HTTPS

        :param req_protocol: The req_protocol of this ApiBaseInfo.
        :type req_protocol: str
        """
        self._req_protocol = req_protocol

    @property
    def req_method(self):
        """Gets the req_method of this ApiBaseInfo.

        API的请求方式

        :return: The req_method of this ApiBaseInfo.
        :rtype: str
        """
        return self._req_method

    @req_method.setter
    def req_method(self, req_method):
        """Sets the req_method of this ApiBaseInfo.

        API的请求方式

        :param req_method: The req_method of this ApiBaseInfo.
        :type req_method: str
        """
        self._req_method = req_method

    @property
    def req_uri(self):
        """Gets the req_uri of this ApiBaseInfo.

        请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ . 等特殊字符，总长度不超过512，且满足URI规范。 > 需要服从URI规范。

        :return: The req_uri of this ApiBaseInfo.
        :rtype: str
        """
        return self._req_uri

    @req_uri.setter
    def req_uri(self, req_uri):
        """Sets the req_uri of this ApiBaseInfo.

        请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ . 等特殊字符，总长度不超过512，且满足URI规范。 > 需要服从URI规范。

        :param req_uri: The req_uri of this ApiBaseInfo.
        :type req_uri: str
        """
        self._req_uri = req_uri

    @property
    def auth_type(self):
        """Gets the auth_type of this ApiBaseInfo.

        API的认证方式[，site暂不支持IAM认证。](tag:Site) - NONE：无认证 - APP：APP认证 - IAM：IAM认证 - AUTHORIZER：自定义认证

        :return: The auth_type of this ApiBaseInfo.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this ApiBaseInfo.

        API的认证方式[，site暂不支持IAM认证。](tag:Site) - NONE：无认证 - APP：APP认证 - IAM：IAM认证 - AUTHORIZER：自定义认证

        :param auth_type: The auth_type of this ApiBaseInfo.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def auth_opt(self):
        """Gets the auth_opt of this ApiBaseInfo.


        :return: The auth_opt of this ApiBaseInfo.
        :rtype: :class:`huaweicloudsdkroma.v2.AuthOpt`
        """
        return self._auth_opt

    @auth_opt.setter
    def auth_opt(self, auth_opt):
        """Sets the auth_opt of this ApiBaseInfo.


        :param auth_opt: The auth_opt of this ApiBaseInfo.
        :type auth_opt: :class:`huaweicloudsdkroma.v2.AuthOpt`
        """
        self._auth_opt = auth_opt

    @property
    def cors(self):
        """Gets the cors of this ApiBaseInfo.

        是否支持跨域 - TRUE：支持 - FALSE：不支持

        :return: The cors of this ApiBaseInfo.
        :rtype: bool
        """
        return self._cors

    @cors.setter
    def cors(self, cors):
        """Sets the cors of this ApiBaseInfo.

        是否支持跨域 - TRUE：支持 - FALSE：不支持

        :param cors: The cors of this ApiBaseInfo.
        :type cors: bool
        """
        self._cors = cors

    @property
    def match_mode(self):
        """Gets the match_mode of this ApiBaseInfo.

        API的匹配方式 - SWA：前缀匹配 - NORMAL：正常匹配（绝对匹配） 默认：NORMAL

        :return: The match_mode of this ApiBaseInfo.
        :rtype: str
        """
        return self._match_mode

    @match_mode.setter
    def match_mode(self, match_mode):
        """Sets the match_mode of this ApiBaseInfo.

        API的匹配方式 - SWA：前缀匹配 - NORMAL：正常匹配（绝对匹配） 默认：NORMAL

        :param match_mode: The match_mode of this ApiBaseInfo.
        :type match_mode: str
        """
        self._match_mode = match_mode

    @property
    def backend_type(self):
        """Gets the backend_type of this ApiBaseInfo.

        后端类型[，site暂不支持函数工作流。](tag:Site) - HTTP：web后端 - FUNCTION：函数工作流 - MOCK：模拟的后端

        :return: The backend_type of this ApiBaseInfo.
        :rtype: str
        """
        return self._backend_type

    @backend_type.setter
    def backend_type(self, backend_type):
        """Sets the backend_type of this ApiBaseInfo.

        后端类型[，site暂不支持函数工作流。](tag:Site) - HTTP：web后端 - FUNCTION：函数工作流 - MOCK：模拟的后端

        :param backend_type: The backend_type of this ApiBaseInfo.
        :type backend_type: str
        """
        self._backend_type = backend_type

    @property
    def remark(self):
        """Gets the remark of this ApiBaseInfo.

        API描述。  不允许带有<、>字符 > 中文字符必须为UTF-8或者unicode编码。

        :return: The remark of this ApiBaseInfo.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this ApiBaseInfo.

        API描述。  不允许带有<、>字符 > 中文字符必须为UTF-8或者unicode编码。

        :param remark: The remark of this ApiBaseInfo.
        :type remark: str
        """
        self._remark = remark

    @property
    def group_id(self):
        """Gets the group_id of this ApiBaseInfo.

        API所属的分组编号

        :return: The group_id of this ApiBaseInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ApiBaseInfo.

        API所属的分组编号

        :param group_id: The group_id of this ApiBaseInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def body_remark(self):
        """Gets the body_remark of this ApiBaseInfo.

        API请求体描述，可以是请求体示例、媒体类型、参数等信息。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The body_remark of this ApiBaseInfo.
        :rtype: str
        """
        return self._body_remark

    @body_remark.setter
    def body_remark(self, body_remark):
        """Sets the body_remark of this ApiBaseInfo.

        API请求体描述，可以是请求体示例、媒体类型、参数等信息。 > 中文字符必须为UTF-8或者unicode编码。

        :param body_remark: The body_remark of this ApiBaseInfo.
        :type body_remark: str
        """
        self._body_remark = body_remark

    @property
    def result_normal_sample(self):
        """Gets the result_normal_sample of this ApiBaseInfo.

        正常响应示例，描述API的正常返回信息。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The result_normal_sample of this ApiBaseInfo.
        :rtype: str
        """
        return self._result_normal_sample

    @result_normal_sample.setter
    def result_normal_sample(self, result_normal_sample):
        """Sets the result_normal_sample of this ApiBaseInfo.

        正常响应示例，描述API的正常返回信息。 > 中文字符必须为UTF-8或者unicode编码。

        :param result_normal_sample: The result_normal_sample of this ApiBaseInfo.
        :type result_normal_sample: str
        """
        self._result_normal_sample = result_normal_sample

    @property
    def result_failure_sample(self):
        """Gets the result_failure_sample of this ApiBaseInfo.

        失败返回示例，描述API的异常返回信息。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The result_failure_sample of this ApiBaseInfo.
        :rtype: str
        """
        return self._result_failure_sample

    @result_failure_sample.setter
    def result_failure_sample(self, result_failure_sample):
        """Sets the result_failure_sample of this ApiBaseInfo.

        失败返回示例，描述API的异常返回信息。 > 中文字符必须为UTF-8或者unicode编码。

        :param result_failure_sample: The result_failure_sample of this ApiBaseInfo.
        :type result_failure_sample: str
        """
        self._result_failure_sample = result_failure_sample

    @property
    def authorizer_id(self):
        """Gets the authorizer_id of this ApiBaseInfo.

        前端自定义认证对象的ID

        :return: The authorizer_id of this ApiBaseInfo.
        :rtype: str
        """
        return self._authorizer_id

    @authorizer_id.setter
    def authorizer_id(self, authorizer_id):
        """Sets the authorizer_id of this ApiBaseInfo.

        前端自定义认证对象的ID

        :param authorizer_id: The authorizer_id of this ApiBaseInfo.
        :type authorizer_id: str
        """
        self._authorizer_id = authorizer_id

    @property
    def tags(self):
        """Gets the tags of this ApiBaseInfo.

        标签。  支持英文，数字，中文，特殊符号（-*#%.:_），且只能以中文或英文开头。支持输入多个标签，不同标签以英文逗号分割。  默认支持10个标签，如需扩大配额请联系技术工程师修改API_TAG_NUM_LIMIT配置。 

        :return: The tags of this ApiBaseInfo.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ApiBaseInfo.

        标签。  支持英文，数字，中文，特殊符号（-*#%.:_），且只能以中文或英文开头。支持输入多个标签，不同标签以英文逗号分割。  默认支持10个标签，如需扩大配额请联系技术工程师修改API_TAG_NUM_LIMIT配置。 

        :param tags: The tags of this ApiBaseInfo.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def response_id(self):
        """Gets the response_id of this ApiBaseInfo.

        分组自定义响应ID  暂不支持

        :return: The response_id of this ApiBaseInfo.
        :rtype: str
        """
        return self._response_id

    @response_id.setter
    def response_id(self, response_id):
        """Sets the response_id of this ApiBaseInfo.

        分组自定义响应ID  暂不支持

        :param response_id: The response_id of this ApiBaseInfo.
        :type response_id: str
        """
        self._response_id = response_id

    @property
    def roma_app_id(self):
        """Gets the roma_app_id of this ApiBaseInfo.

        API归属的集成应用编号  API分组为全局分组时或API绑定自定义域名时必填。

        :return: The roma_app_id of this ApiBaseInfo.
        :rtype: str
        """
        return self._roma_app_id

    @roma_app_id.setter
    def roma_app_id(self, roma_app_id):
        """Sets the roma_app_id of this ApiBaseInfo.

        API归属的集成应用编号  API分组为全局分组时或API绑定自定义域名时必填。

        :param roma_app_id: The roma_app_id of this ApiBaseInfo.
        :type roma_app_id: str
        """
        self._roma_app_id = roma_app_id

    @property
    def domain_name(self):
        """Gets the domain_name of this ApiBaseInfo.

        API绑定的自定义域名，使用自定义域名时roma_app_id字段必填。

        :return: The domain_name of this ApiBaseInfo.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ApiBaseInfo.

        API绑定的自定义域名，使用自定义域名时roma_app_id字段必填。

        :param domain_name: The domain_name of this ApiBaseInfo.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def tag(self):
        """Gets the tag of this ApiBaseInfo.

        标签  待废弃，优先使用tags字段

        :return: The tag of this ApiBaseInfo.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ApiBaseInfo.

        标签  待废弃，优先使用tags字段

        :param tag: The tag of this ApiBaseInfo.
        :type tag: str
        """
        self._tag = tag

    @property
    def content_type(self):
        """Gets the content_type of this ApiBaseInfo.

        请求内容格式类型：  application/json application/xml multipart/form-date text/plain

        :return: The content_type of this ApiBaseInfo.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this ApiBaseInfo.

        请求内容格式类型：  application/json application/xml multipart/form-date text/plain

        :param content_type: The content_type of this ApiBaseInfo.
        :type content_type: str
        """
        self._content_type = content_type

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
        if not isinstance(other, ApiBaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
