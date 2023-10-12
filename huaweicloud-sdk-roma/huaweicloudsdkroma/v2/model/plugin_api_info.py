# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginApiInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_id': 'str',
        'api_name': 'str',
        'type': 'int',
        'req_protocol': 'str',
        'req_method': 'str',
        'req_uri': 'str',
        'auth_type': 'str',
        'match_mode': 'str',
        'remark': 'str',
        'group_id': 'str',
        'group_name': 'str',
        'roma_app_id': 'str',
        'env_id': 'str',
        'env_name': 'str',
        'publish_id': 'str',
        'plugin_attach_id': 'str',
        'attached_time': 'datetime'
    }

    attribute_map = {
        'api_id': 'api_id',
        'api_name': 'api_name',
        'type': 'type',
        'req_protocol': 'req_protocol',
        'req_method': 'req_method',
        'req_uri': 'req_uri',
        'auth_type': 'auth_type',
        'match_mode': 'match_mode',
        'remark': 'remark',
        'group_id': 'group_id',
        'group_name': 'group_name',
        'roma_app_id': 'roma_app_id',
        'env_id': 'env_id',
        'env_name': 'env_name',
        'publish_id': 'publish_id',
        'plugin_attach_id': 'plugin_attach_id',
        'attached_time': 'attached_time'
    }

    def __init__(self, api_id=None, api_name=None, type=None, req_protocol=None, req_method=None, req_uri=None, auth_type=None, match_mode=None, remark=None, group_id=None, group_name=None, roma_app_id=None, env_id=None, env_name=None, publish_id=None, plugin_attach_id=None, attached_time=None):
        """PluginApiInfo

        The model defined in huaweicloud sdk

        :param api_id: API编号
        :type api_id: str
        :param api_name: API名称。 支持汉字、英文、数字、中划线、下划线、点、斜杠、中英文格式下的小括号和冒号、中文格式下的顿号，且只能以英文、汉字和数字开头，3-255个字符。  &gt; 中文字符必须为UTF-8或者unicode编码。
        :type api_name: str
        :param type: API类型 - 1：公有API - 2：私有API
        :type type: int
        :param req_protocol: API的请求协议 - HTTP - HTTPS - BOTH：同时支持HTTP和HTTPS
        :type req_protocol: str
        :param req_method: API的请求方式
        :type req_method: str
        :param req_uri: 请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ .等特殊字符，总长度不超过512，且满足URI规范。 支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、中划线、下划线组成，且只能以英文开头。  &gt; 需要服从URI规范。
        :type req_uri: str
        :param auth_type: API的认证方式 - NONE：无认证 - APP：APP认证 - IAM：IAM认证 - AUTHORIZER：自定义认证
        :type auth_type: str
        :param match_mode: API的匹配方式 - SWA：前缀匹配 - NORMAL：正常匹配（绝对匹配） 默认：NORMAL
        :type match_mode: str
        :param remark: API描述。
        :type remark: str
        :param group_id: API所属的分组编号
        :type group_id: str
        :param group_name: API所属分组的名称
        :type group_name: str
        :param roma_app_id: 归属集成应用编码
        :type roma_app_id: str
        :param env_id: 绑定API的环境编码。
        :type env_id: str
        :param env_name: 绑定API的环境名称
        :type env_name: str
        :param publish_id: 发布编码。
        :type publish_id: str
        :param plugin_attach_id: 插件绑定编码。
        :type plugin_attach_id: str
        :param attached_time: 绑定时间。
        :type attached_time: datetime
        """
        
        

        self._api_id = None
        self._api_name = None
        self._type = None
        self._req_protocol = None
        self._req_method = None
        self._req_uri = None
        self._auth_type = None
        self._match_mode = None
        self._remark = None
        self._group_id = None
        self._group_name = None
        self._roma_app_id = None
        self._env_id = None
        self._env_name = None
        self._publish_id = None
        self._plugin_attach_id = None
        self._attached_time = None
        self.discriminator = None

        if api_id is not None:
            self.api_id = api_id
        if api_name is not None:
            self.api_name = api_name
        if type is not None:
            self.type = type
        if req_protocol is not None:
            self.req_protocol = req_protocol
        if req_method is not None:
            self.req_method = req_method
        if req_uri is not None:
            self.req_uri = req_uri
        if auth_type is not None:
            self.auth_type = auth_type
        if match_mode is not None:
            self.match_mode = match_mode
        if remark is not None:
            self.remark = remark
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if roma_app_id is not None:
            self.roma_app_id = roma_app_id
        if env_id is not None:
            self.env_id = env_id
        if env_name is not None:
            self.env_name = env_name
        if publish_id is not None:
            self.publish_id = publish_id
        if plugin_attach_id is not None:
            self.plugin_attach_id = plugin_attach_id
        if attached_time is not None:
            self.attached_time = attached_time

    @property
    def api_id(self):
        """Gets the api_id of this PluginApiInfo.

        API编号

        :return: The api_id of this PluginApiInfo.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this PluginApiInfo.

        API编号

        :param api_id: The api_id of this PluginApiInfo.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def api_name(self):
        """Gets the api_name of this PluginApiInfo.

        API名称。 支持汉字、英文、数字、中划线、下划线、点、斜杠、中英文格式下的小括号和冒号、中文格式下的顿号，且只能以英文、汉字和数字开头，3-255个字符。  > 中文字符必须为UTF-8或者unicode编码。

        :return: The api_name of this PluginApiInfo.
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        """Sets the api_name of this PluginApiInfo.

        API名称。 支持汉字、英文、数字、中划线、下划线、点、斜杠、中英文格式下的小括号和冒号、中文格式下的顿号，且只能以英文、汉字和数字开头，3-255个字符。  > 中文字符必须为UTF-8或者unicode编码。

        :param api_name: The api_name of this PluginApiInfo.
        :type api_name: str
        """
        self._api_name = api_name

    @property
    def type(self):
        """Gets the type of this PluginApiInfo.

        API类型 - 1：公有API - 2：私有API

        :return: The type of this PluginApiInfo.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PluginApiInfo.

        API类型 - 1：公有API - 2：私有API

        :param type: The type of this PluginApiInfo.
        :type type: int
        """
        self._type = type

    @property
    def req_protocol(self):
        """Gets the req_protocol of this PluginApiInfo.

        API的请求协议 - HTTP - HTTPS - BOTH：同时支持HTTP和HTTPS

        :return: The req_protocol of this PluginApiInfo.
        :rtype: str
        """
        return self._req_protocol

    @req_protocol.setter
    def req_protocol(self, req_protocol):
        """Sets the req_protocol of this PluginApiInfo.

        API的请求协议 - HTTP - HTTPS - BOTH：同时支持HTTP和HTTPS

        :param req_protocol: The req_protocol of this PluginApiInfo.
        :type req_protocol: str
        """
        self._req_protocol = req_protocol

    @property
    def req_method(self):
        """Gets the req_method of this PluginApiInfo.

        API的请求方式

        :return: The req_method of this PluginApiInfo.
        :rtype: str
        """
        return self._req_method

    @req_method.setter
    def req_method(self, req_method):
        """Sets the req_method of this PluginApiInfo.

        API的请求方式

        :param req_method: The req_method of this PluginApiInfo.
        :type req_method: str
        """
        self._req_method = req_method

    @property
    def req_uri(self):
        """Gets the req_uri of this PluginApiInfo.

        请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ .等特殊字符，总长度不超过512，且满足URI规范。 支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、中划线、下划线组成，且只能以英文开头。  > 需要服从URI规范。

        :return: The req_uri of this PluginApiInfo.
        :rtype: str
        """
        return self._req_uri

    @req_uri.setter
    def req_uri(self, req_uri):
        """Sets the req_uri of this PluginApiInfo.

        请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ .等特殊字符，总长度不超过512，且满足URI规范。 支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、中划线、下划线组成，且只能以英文开头。  > 需要服从URI规范。

        :param req_uri: The req_uri of this PluginApiInfo.
        :type req_uri: str
        """
        self._req_uri = req_uri

    @property
    def auth_type(self):
        """Gets the auth_type of this PluginApiInfo.

        API的认证方式 - NONE：无认证 - APP：APP认证 - IAM：IAM认证 - AUTHORIZER：自定义认证

        :return: The auth_type of this PluginApiInfo.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this PluginApiInfo.

        API的认证方式 - NONE：无认证 - APP：APP认证 - IAM：IAM认证 - AUTHORIZER：自定义认证

        :param auth_type: The auth_type of this PluginApiInfo.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def match_mode(self):
        """Gets the match_mode of this PluginApiInfo.

        API的匹配方式 - SWA：前缀匹配 - NORMAL：正常匹配（绝对匹配） 默认：NORMAL

        :return: The match_mode of this PluginApiInfo.
        :rtype: str
        """
        return self._match_mode

    @match_mode.setter
    def match_mode(self, match_mode):
        """Sets the match_mode of this PluginApiInfo.

        API的匹配方式 - SWA：前缀匹配 - NORMAL：正常匹配（绝对匹配） 默认：NORMAL

        :param match_mode: The match_mode of this PluginApiInfo.
        :type match_mode: str
        """
        self._match_mode = match_mode

    @property
    def remark(self):
        """Gets the remark of this PluginApiInfo.

        API描述。

        :return: The remark of this PluginApiInfo.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this PluginApiInfo.

        API描述。

        :param remark: The remark of this PluginApiInfo.
        :type remark: str
        """
        self._remark = remark

    @property
    def group_id(self):
        """Gets the group_id of this PluginApiInfo.

        API所属的分组编号

        :return: The group_id of this PluginApiInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this PluginApiInfo.

        API所属的分组编号

        :param group_id: The group_id of this PluginApiInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        """Gets the group_name of this PluginApiInfo.

        API所属分组的名称

        :return: The group_name of this PluginApiInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this PluginApiInfo.

        API所属分组的名称

        :param group_name: The group_name of this PluginApiInfo.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def roma_app_id(self):
        """Gets the roma_app_id of this PluginApiInfo.

        归属集成应用编码

        :return: The roma_app_id of this PluginApiInfo.
        :rtype: str
        """
        return self._roma_app_id

    @roma_app_id.setter
    def roma_app_id(self, roma_app_id):
        """Sets the roma_app_id of this PluginApiInfo.

        归属集成应用编码

        :param roma_app_id: The roma_app_id of this PluginApiInfo.
        :type roma_app_id: str
        """
        self._roma_app_id = roma_app_id

    @property
    def env_id(self):
        """Gets the env_id of this PluginApiInfo.

        绑定API的环境编码。

        :return: The env_id of this PluginApiInfo.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this PluginApiInfo.

        绑定API的环境编码。

        :param env_id: The env_id of this PluginApiInfo.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def env_name(self):
        """Gets the env_name of this PluginApiInfo.

        绑定API的环境名称

        :return: The env_name of this PluginApiInfo.
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        """Sets the env_name of this PluginApiInfo.

        绑定API的环境名称

        :param env_name: The env_name of this PluginApiInfo.
        :type env_name: str
        """
        self._env_name = env_name

    @property
    def publish_id(self):
        """Gets the publish_id of this PluginApiInfo.

        发布编码。

        :return: The publish_id of this PluginApiInfo.
        :rtype: str
        """
        return self._publish_id

    @publish_id.setter
    def publish_id(self, publish_id):
        """Sets the publish_id of this PluginApiInfo.

        发布编码。

        :param publish_id: The publish_id of this PluginApiInfo.
        :type publish_id: str
        """
        self._publish_id = publish_id

    @property
    def plugin_attach_id(self):
        """Gets the plugin_attach_id of this PluginApiInfo.

        插件绑定编码。

        :return: The plugin_attach_id of this PluginApiInfo.
        :rtype: str
        """
        return self._plugin_attach_id

    @plugin_attach_id.setter
    def plugin_attach_id(self, plugin_attach_id):
        """Sets the plugin_attach_id of this PluginApiInfo.

        插件绑定编码。

        :param plugin_attach_id: The plugin_attach_id of this PluginApiInfo.
        :type plugin_attach_id: str
        """
        self._plugin_attach_id = plugin_attach_id

    @property
    def attached_time(self):
        """Gets the attached_time of this PluginApiInfo.

        绑定时间。

        :return: The attached_time of this PluginApiInfo.
        :rtype: datetime
        """
        return self._attached_time

    @attached_time.setter
    def attached_time(self, attached_time):
        """Sets the attached_time of this PluginApiInfo.

        绑定时间。

        :param attached_time: The attached_time of this PluginApiInfo.
        :type attached_time: datetime
        """
        self._attached_time = attached_time

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
        if not isinstance(other, PluginApiInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
