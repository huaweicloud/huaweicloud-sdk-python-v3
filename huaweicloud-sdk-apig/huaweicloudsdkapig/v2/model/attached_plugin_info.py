# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachedPluginInfo:

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
        'attached_time': 'datetime',
        'plugin_content': 'str',
        'remark': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'plugin_attach_id': 'plugin_attach_id',
        'plugin_id': 'plugin_id',
        'plugin_name': 'plugin_name',
        'plugin_type': 'plugin_type',
        'plugin_scope': 'plugin_scope',
        'env_id': 'env_id',
        'env_name': 'env_name',
        'attached_time': 'attached_time',
        'plugin_content': 'plugin_content',
        'remark': 'remark',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, plugin_attach_id=None, plugin_id=None, plugin_name=None, plugin_type=None, plugin_scope=None, env_id=None, env_name=None, attached_time=None, plugin_content=None, remark=None, create_time=None, update_time=None):
        """AttachedPluginInfo

        The model defined in huaweicloud sdk

        :param plugin_attach_id: 插件绑定编码。
        :type plugin_attach_id: str
        :param plugin_id: 插件编码。
        :type plugin_id: str
        :param plugin_name: 插件名称。支持汉字，英文，数字，中划线，下划线，且只能以英文和汉字开头，3-255字符 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type plugin_name: str
        :param plugin_type: 插件类型 - cors：跨域资源共享 - set_resp_headers：HTTP响应头管理 - kafka_log：Kafka日志推送 - breaker：断路器 - rate_limit: 流量控制
        :type plugin_type: str
        :param plugin_scope: 插件可见范围。global：全局可见。
        :type plugin_scope: str
        :param env_id: 绑定API的环境编码。
        :type env_id: str
        :param env_name: api授权绑定的环境名称
        :type env_name: str
        :param attached_time: 绑定时间。
        :type attached_time: datetime
        :param plugin_content: 插件定义内容，支持json。
        :type plugin_content: str
        :param remark: 插件描述，255字符。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type remark: str
        :param create_time: 创建时间。
        :type create_time: datetime
        :param update_time: 更新时间。
        :type update_time: datetime
        """
        
        

        self._plugin_attach_id = None
        self._plugin_id = None
        self._plugin_name = None
        self._plugin_type = None
        self._plugin_scope = None
        self._env_id = None
        self._env_name = None
        self._attached_time = None
        self._plugin_content = None
        self._remark = None
        self._create_time = None
        self._update_time = None
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
        if attached_time is not None:
            self.attached_time = attached_time
        if plugin_content is not None:
            self.plugin_content = plugin_content
        if remark is not None:
            self.remark = remark
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def plugin_attach_id(self):
        """Gets the plugin_attach_id of this AttachedPluginInfo.

        插件绑定编码。

        :return: The plugin_attach_id of this AttachedPluginInfo.
        :rtype: str
        """
        return self._plugin_attach_id

    @plugin_attach_id.setter
    def plugin_attach_id(self, plugin_attach_id):
        """Sets the plugin_attach_id of this AttachedPluginInfo.

        插件绑定编码。

        :param plugin_attach_id: The plugin_attach_id of this AttachedPluginInfo.
        :type plugin_attach_id: str
        """
        self._plugin_attach_id = plugin_attach_id

    @property
    def plugin_id(self):
        """Gets the plugin_id of this AttachedPluginInfo.

        插件编码。

        :return: The plugin_id of this AttachedPluginInfo.
        :rtype: str
        """
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, plugin_id):
        """Sets the plugin_id of this AttachedPluginInfo.

        插件编码。

        :param plugin_id: The plugin_id of this AttachedPluginInfo.
        :type plugin_id: str
        """
        self._plugin_id = plugin_id

    @property
    def plugin_name(self):
        """Gets the plugin_name of this AttachedPluginInfo.

        插件名称。支持汉字，英文，数字，中划线，下划线，且只能以英文和汉字开头，3-255字符 > 中文字符必须为UTF-8或者unicode编码。

        :return: The plugin_name of this AttachedPluginInfo.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """Sets the plugin_name of this AttachedPluginInfo.

        插件名称。支持汉字，英文，数字，中划线，下划线，且只能以英文和汉字开头，3-255字符 > 中文字符必须为UTF-8或者unicode编码。

        :param plugin_name: The plugin_name of this AttachedPluginInfo.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def plugin_type(self):
        """Gets the plugin_type of this AttachedPluginInfo.

        插件类型 - cors：跨域资源共享 - set_resp_headers：HTTP响应头管理 - kafka_log：Kafka日志推送 - breaker：断路器 - rate_limit: 流量控制

        :return: The plugin_type of this AttachedPluginInfo.
        :rtype: str
        """
        return self._plugin_type

    @plugin_type.setter
    def plugin_type(self, plugin_type):
        """Sets the plugin_type of this AttachedPluginInfo.

        插件类型 - cors：跨域资源共享 - set_resp_headers：HTTP响应头管理 - kafka_log：Kafka日志推送 - breaker：断路器 - rate_limit: 流量控制

        :param plugin_type: The plugin_type of this AttachedPluginInfo.
        :type plugin_type: str
        """
        self._plugin_type = plugin_type

    @property
    def plugin_scope(self):
        """Gets the plugin_scope of this AttachedPluginInfo.

        插件可见范围。global：全局可见。

        :return: The plugin_scope of this AttachedPluginInfo.
        :rtype: str
        """
        return self._plugin_scope

    @plugin_scope.setter
    def plugin_scope(self, plugin_scope):
        """Sets the plugin_scope of this AttachedPluginInfo.

        插件可见范围。global：全局可见。

        :param plugin_scope: The plugin_scope of this AttachedPluginInfo.
        :type plugin_scope: str
        """
        self._plugin_scope = plugin_scope

    @property
    def env_id(self):
        """Gets the env_id of this AttachedPluginInfo.

        绑定API的环境编码。

        :return: The env_id of this AttachedPluginInfo.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this AttachedPluginInfo.

        绑定API的环境编码。

        :param env_id: The env_id of this AttachedPluginInfo.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def env_name(self):
        """Gets the env_name of this AttachedPluginInfo.

        api授权绑定的环境名称

        :return: The env_name of this AttachedPluginInfo.
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        """Sets the env_name of this AttachedPluginInfo.

        api授权绑定的环境名称

        :param env_name: The env_name of this AttachedPluginInfo.
        :type env_name: str
        """
        self._env_name = env_name

    @property
    def attached_time(self):
        """Gets the attached_time of this AttachedPluginInfo.

        绑定时间。

        :return: The attached_time of this AttachedPluginInfo.
        :rtype: datetime
        """
        return self._attached_time

    @attached_time.setter
    def attached_time(self, attached_time):
        """Sets the attached_time of this AttachedPluginInfo.

        绑定时间。

        :param attached_time: The attached_time of this AttachedPluginInfo.
        :type attached_time: datetime
        """
        self._attached_time = attached_time

    @property
    def plugin_content(self):
        """Gets the plugin_content of this AttachedPluginInfo.

        插件定义内容，支持json。

        :return: The plugin_content of this AttachedPluginInfo.
        :rtype: str
        """
        return self._plugin_content

    @plugin_content.setter
    def plugin_content(self, plugin_content):
        """Sets the plugin_content of this AttachedPluginInfo.

        插件定义内容，支持json。

        :param plugin_content: The plugin_content of this AttachedPluginInfo.
        :type plugin_content: str
        """
        self._plugin_content = plugin_content

    @property
    def remark(self):
        """Gets the remark of this AttachedPluginInfo.

        插件描述，255字符。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The remark of this AttachedPluginInfo.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this AttachedPluginInfo.

        插件描述，255字符。 > 中文字符必须为UTF-8或者unicode编码。

        :param remark: The remark of this AttachedPluginInfo.
        :type remark: str
        """
        self._remark = remark

    @property
    def create_time(self):
        """Gets the create_time of this AttachedPluginInfo.

        创建时间。

        :return: The create_time of this AttachedPluginInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this AttachedPluginInfo.

        创建时间。

        :param create_time: The create_time of this AttachedPluginInfo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this AttachedPluginInfo.

        更新时间。

        :return: The update_time of this AttachedPluginInfo.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this AttachedPluginInfo.

        更新时间。

        :param update_time: The update_time of this AttachedPluginInfo.
        :type update_time: datetime
        """
        self._update_time = update_time

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
        if not isinstance(other, AttachedPluginInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
