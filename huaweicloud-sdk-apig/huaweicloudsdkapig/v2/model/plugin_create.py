# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'plugin_name': 'str',
        'plugin_type': 'str',
        'plugin_scope': 'str',
        'plugin_content': 'str',
        'remark': 'str'
    }

    attribute_map = {
        'plugin_name': 'plugin_name',
        'plugin_type': 'plugin_type',
        'plugin_scope': 'plugin_scope',
        'plugin_content': 'plugin_content',
        'remark': 'remark'
    }

    def __init__(self, plugin_name=None, plugin_type=None, plugin_scope=None, plugin_content=None, remark=None):
        """PluginCreate

        The model defined in huaweicloud sdk

        :param plugin_name: 插件名称。支持汉字，英文，数字，中划线，下划线，且只能以英文和汉字开头，3-255字符。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type plugin_name: str
        :param plugin_type: 插件类型 - cors：跨域资源共享 - set_resp_headers：HTTP响应头管理 - kafka_log：Kafka日志推送  - breaker：断路器 - rate_limit: 流量控制 - third_auth: 第三方认证
        :type plugin_type: str
        :param plugin_scope: 插件可见范围。global：全局可见；
        :type plugin_scope: str
        :param plugin_content: 插件定义内容，支持json。参考提供的具体模型定义  CorsPluginContent：跨域资源共享 定义内容 SetRespHeadersContent：HTTP响应头管理 定义内容 KafkaLogContent：Kafka日志推送 定义内容 BreakerContent：断路器 定义内容 RateLimitContent 流量控制 定义内容 ThirdAuthContent: 第三方认证 定义内容
        :type plugin_content: str
        :param remark: 插件描述，255字符。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type remark: str
        """
        
        

        self._plugin_name = None
        self._plugin_type = None
        self._plugin_scope = None
        self._plugin_content = None
        self._remark = None
        self.discriminator = None

        self.plugin_name = plugin_name
        self.plugin_type = plugin_type
        self.plugin_scope = plugin_scope
        self.plugin_content = plugin_content
        if remark is not None:
            self.remark = remark

    @property
    def plugin_name(self):
        """Gets the plugin_name of this PluginCreate.

        插件名称。支持汉字，英文，数字，中划线，下划线，且只能以英文和汉字开头，3-255字符。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The plugin_name of this PluginCreate.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """Sets the plugin_name of this PluginCreate.

        插件名称。支持汉字，英文，数字，中划线，下划线，且只能以英文和汉字开头，3-255字符。 > 中文字符必须为UTF-8或者unicode编码。

        :param plugin_name: The plugin_name of this PluginCreate.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def plugin_type(self):
        """Gets the plugin_type of this PluginCreate.

        插件类型 - cors：跨域资源共享 - set_resp_headers：HTTP响应头管理 - kafka_log：Kafka日志推送  - breaker：断路器 - rate_limit: 流量控制 - third_auth: 第三方认证

        :return: The plugin_type of this PluginCreate.
        :rtype: str
        """
        return self._plugin_type

    @plugin_type.setter
    def plugin_type(self, plugin_type):
        """Sets the plugin_type of this PluginCreate.

        插件类型 - cors：跨域资源共享 - set_resp_headers：HTTP响应头管理 - kafka_log：Kafka日志推送  - breaker：断路器 - rate_limit: 流量控制 - third_auth: 第三方认证

        :param plugin_type: The plugin_type of this PluginCreate.
        :type plugin_type: str
        """
        self._plugin_type = plugin_type

    @property
    def plugin_scope(self):
        """Gets the plugin_scope of this PluginCreate.

        插件可见范围。global：全局可见；

        :return: The plugin_scope of this PluginCreate.
        :rtype: str
        """
        return self._plugin_scope

    @plugin_scope.setter
    def plugin_scope(self, plugin_scope):
        """Sets the plugin_scope of this PluginCreate.

        插件可见范围。global：全局可见；

        :param plugin_scope: The plugin_scope of this PluginCreate.
        :type plugin_scope: str
        """
        self._plugin_scope = plugin_scope

    @property
    def plugin_content(self):
        """Gets the plugin_content of this PluginCreate.

        插件定义内容，支持json。参考提供的具体模型定义  CorsPluginContent：跨域资源共享 定义内容 SetRespHeadersContent：HTTP响应头管理 定义内容 KafkaLogContent：Kafka日志推送 定义内容 BreakerContent：断路器 定义内容 RateLimitContent 流量控制 定义内容 ThirdAuthContent: 第三方认证 定义内容

        :return: The plugin_content of this PluginCreate.
        :rtype: str
        """
        return self._plugin_content

    @plugin_content.setter
    def plugin_content(self, plugin_content):
        """Sets the plugin_content of this PluginCreate.

        插件定义内容，支持json。参考提供的具体模型定义  CorsPluginContent：跨域资源共享 定义内容 SetRespHeadersContent：HTTP响应头管理 定义内容 KafkaLogContent：Kafka日志推送 定义内容 BreakerContent：断路器 定义内容 RateLimitContent 流量控制 定义内容 ThirdAuthContent: 第三方认证 定义内容

        :param plugin_content: The plugin_content of this PluginCreate.
        :type plugin_content: str
        """
        self._plugin_content = plugin_content

    @property
    def remark(self):
        """Gets the remark of this PluginCreate.

        插件描述，255字符。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The remark of this PluginCreate.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this PluginCreate.

        插件描述，255字符。 > 中文字符必须为UTF-8或者unicode编码。

        :param remark: The remark of this PluginCreate.
        :type remark: str
        """
        self._remark = remark

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
        if not isinstance(other, PluginCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
