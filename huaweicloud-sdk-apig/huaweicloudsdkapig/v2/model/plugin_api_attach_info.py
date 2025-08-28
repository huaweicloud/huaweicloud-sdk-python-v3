# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginApiAttachInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'plugin_attach_id': 'str',
        'plugin_id': 'str',
        'plugin_name': 'str',
        'plugin_type': 'str',
        'plugin_scope': 'str',
        'env_id': 'str',
        'env_name': 'str',
        'api_id': 'str',
        'api_name': 'str',
        'attached_time': 'datetime'
    }

    attribute_map = {
        'plugin_attach_id': 'plugin_attach_id',
        'plugin_id': 'plugin_id',
        'plugin_name': 'plugin_name',
        'plugin_type': 'plugin_type',
        'plugin_scope': 'plugin_scope',
        'env_id': 'env_id',
        'env_name': 'env_name',
        'api_id': 'api_id',
        'api_name': 'api_name',
        'attached_time': 'attached_time'
    }

    def __init__(self, plugin_attach_id=None, plugin_id=None, plugin_name=None, plugin_type=None, plugin_scope=None, env_id=None, env_name=None, api_id=None, api_name=None, attached_time=None):
        r"""PluginApiAttachInfo

        The model defined in huaweicloud sdk

        :param plugin_attach_id: 插件绑定编码。
        :type plugin_attach_id: str
        :param plugin_id: 插件编码。
        :type plugin_id: str
        :param plugin_name: 插件名称。支持汉字，英文，数字，中划线，下划线，且只能以英文和汉字开头，3-255字符 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type plugin_name: str
        :param plugin_type: 插件类型。 - cors：跨域资源共享 - set_resp_headers：HTTP响应头管理 - kafka_log：Kafka日志推送 - breaker：断路器 - rate_limit: 流量控制 - third_auth: 第三方认证 - proxy_cache: 响应缓存 - proxy_mirror: 请求镜像 - oidc_auth: OIDC认证 - jwt_auth: JWT认证
        :type plugin_type: str
        :param plugin_scope: 插件可见范围。global：全局可见。
        :type plugin_scope: str
        :param env_id: 绑定API的环境编码。
        :type env_id: str
        :param env_name: api授权绑定的环境名称
        :type env_name: str
        :param api_id: 绑定的API编码。
        :type api_id: str
        :param api_name: API的名称
        :type api_name: str
        :param attached_time: 绑定时间。
        :type attached_time: datetime
        """
        
        

        self._plugin_attach_id = None
        self._plugin_id = None
        self._plugin_name = None
        self._plugin_type = None
        self._plugin_scope = None
        self._env_id = None
        self._env_name = None
        self._api_id = None
        self._api_name = None
        self._attached_time = None
        self.discriminator = None

        if plugin_attach_id is not None:
            self.plugin_attach_id = plugin_attach_id
        if plugin_id is not None:
            self.plugin_id = plugin_id
        if plugin_name is not None:
            self.plugin_name = plugin_name
        if plugin_type is not None:
            self.plugin_type = plugin_type
        if plugin_scope is not None:
            self.plugin_scope = plugin_scope
        if env_id is not None:
            self.env_id = env_id
        if env_name is not None:
            self.env_name = env_name
        if api_id is not None:
            self.api_id = api_id
        if api_name is not None:
            self.api_name = api_name
        if attached_time is not None:
            self.attached_time = attached_time

    @property
    def plugin_attach_id(self):
        r"""Gets the plugin_attach_id of this PluginApiAttachInfo.

        插件绑定编码。

        :return: The plugin_attach_id of this PluginApiAttachInfo.
        :rtype: str
        """
        return self._plugin_attach_id

    @plugin_attach_id.setter
    def plugin_attach_id(self, plugin_attach_id):
        r"""Sets the plugin_attach_id of this PluginApiAttachInfo.

        插件绑定编码。

        :param plugin_attach_id: The plugin_attach_id of this PluginApiAttachInfo.
        :type plugin_attach_id: str
        """
        self._plugin_attach_id = plugin_attach_id

    @property
    def plugin_id(self):
        r"""Gets the plugin_id of this PluginApiAttachInfo.

        插件编码。

        :return: The plugin_id of this PluginApiAttachInfo.
        :rtype: str
        """
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, plugin_id):
        r"""Sets the plugin_id of this PluginApiAttachInfo.

        插件编码。

        :param plugin_id: The plugin_id of this PluginApiAttachInfo.
        :type plugin_id: str
        """
        self._plugin_id = plugin_id

    @property
    def plugin_name(self):
        r"""Gets the plugin_name of this PluginApiAttachInfo.

        插件名称。支持汉字，英文，数字，中划线，下划线，且只能以英文和汉字开头，3-255字符 > 中文字符必须为UTF-8或者unicode编码。

        :return: The plugin_name of this PluginApiAttachInfo.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        r"""Sets the plugin_name of this PluginApiAttachInfo.

        插件名称。支持汉字，英文，数字，中划线，下划线，且只能以英文和汉字开头，3-255字符 > 中文字符必须为UTF-8或者unicode编码。

        :param plugin_name: The plugin_name of this PluginApiAttachInfo.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def plugin_type(self):
        r"""Gets the plugin_type of this PluginApiAttachInfo.

        插件类型。 - cors：跨域资源共享 - set_resp_headers：HTTP响应头管理 - kafka_log：Kafka日志推送 - breaker：断路器 - rate_limit: 流量控制 - third_auth: 第三方认证 - proxy_cache: 响应缓存 - proxy_mirror: 请求镜像 - oidc_auth: OIDC认证 - jwt_auth: JWT认证

        :return: The plugin_type of this PluginApiAttachInfo.
        :rtype: str
        """
        return self._plugin_type

    @plugin_type.setter
    def plugin_type(self, plugin_type):
        r"""Sets the plugin_type of this PluginApiAttachInfo.

        插件类型。 - cors：跨域资源共享 - set_resp_headers：HTTP响应头管理 - kafka_log：Kafka日志推送 - breaker：断路器 - rate_limit: 流量控制 - third_auth: 第三方认证 - proxy_cache: 响应缓存 - proxy_mirror: 请求镜像 - oidc_auth: OIDC认证 - jwt_auth: JWT认证

        :param plugin_type: The plugin_type of this PluginApiAttachInfo.
        :type plugin_type: str
        """
        self._plugin_type = plugin_type

    @property
    def plugin_scope(self):
        r"""Gets the plugin_scope of this PluginApiAttachInfo.

        插件可见范围。global：全局可见。

        :return: The plugin_scope of this PluginApiAttachInfo.
        :rtype: str
        """
        return self._plugin_scope

    @plugin_scope.setter
    def plugin_scope(self, plugin_scope):
        r"""Sets the plugin_scope of this PluginApiAttachInfo.

        插件可见范围。global：全局可见。

        :param plugin_scope: The plugin_scope of this PluginApiAttachInfo.
        :type plugin_scope: str
        """
        self._plugin_scope = plugin_scope

    @property
    def env_id(self):
        r"""Gets the env_id of this PluginApiAttachInfo.

        绑定API的环境编码。

        :return: The env_id of this PluginApiAttachInfo.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        r"""Sets the env_id of this PluginApiAttachInfo.

        绑定API的环境编码。

        :param env_id: The env_id of this PluginApiAttachInfo.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def env_name(self):
        r"""Gets the env_name of this PluginApiAttachInfo.

        api授权绑定的环境名称

        :return: The env_name of this PluginApiAttachInfo.
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        r"""Sets the env_name of this PluginApiAttachInfo.

        api授权绑定的环境名称

        :param env_name: The env_name of this PluginApiAttachInfo.
        :type env_name: str
        """
        self._env_name = env_name

    @property
    def api_id(self):
        r"""Gets the api_id of this PluginApiAttachInfo.

        绑定的API编码。

        :return: The api_id of this PluginApiAttachInfo.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        r"""Sets the api_id of this PluginApiAttachInfo.

        绑定的API编码。

        :param api_id: The api_id of this PluginApiAttachInfo.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def api_name(self):
        r"""Gets the api_name of this PluginApiAttachInfo.

        API的名称

        :return: The api_name of this PluginApiAttachInfo.
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        r"""Sets the api_name of this PluginApiAttachInfo.

        API的名称

        :param api_name: The api_name of this PluginApiAttachInfo.
        :type api_name: str
        """
        self._api_name = api_name

    @property
    def attached_time(self):
        r"""Gets the attached_time of this PluginApiAttachInfo.

        绑定时间。

        :return: The attached_time of this PluginApiAttachInfo.
        :rtype: datetime
        """
        return self._attached_time

    @attached_time.setter
    def attached_time(self, attached_time):
        r"""Sets the attached_time of this PluginApiAttachInfo.

        绑定时间。

        :param attached_time: The attached_time of this PluginApiAttachInfo.
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
        if not isinstance(other, PluginApiAttachInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
