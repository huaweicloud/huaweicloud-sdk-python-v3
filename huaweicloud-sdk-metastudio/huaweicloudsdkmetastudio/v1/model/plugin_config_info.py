# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginConfigInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'plugin_config_id': 'str',
        'plugin_provider': 'PluginProviderEnum',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'plugin_config_id': 'plugin_config_id',
        'plugin_provider': 'plugin_provider',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, plugin_config_id=None, plugin_provider=None, create_time=None, update_time=None):
        r"""PluginConfigInfo

        The model defined in huaweicloud sdk

        :param plugin_config_id: 插件配置ID。
        :type plugin_config_id: str
        :param plugin_provider: 
        :type plugin_provider: :class:`huaweicloudsdkmetastudio.v1.PluginProviderEnum`
        :param create_time: 创建时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param update_time: 更新时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type update_time: str
        """
        
        

        self._plugin_config_id = None
        self._plugin_provider = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if plugin_config_id is not None:
            self.plugin_config_id = plugin_config_id
        if plugin_provider is not None:
            self.plugin_provider = plugin_provider
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def plugin_config_id(self):
        r"""Gets the plugin_config_id of this PluginConfigInfo.

        插件配置ID。

        :return: The plugin_config_id of this PluginConfigInfo.
        :rtype: str
        """
        return self._plugin_config_id

    @plugin_config_id.setter
    def plugin_config_id(self, plugin_config_id):
        r"""Sets the plugin_config_id of this PluginConfigInfo.

        插件配置ID。

        :param plugin_config_id: The plugin_config_id of this PluginConfigInfo.
        :type plugin_config_id: str
        """
        self._plugin_config_id = plugin_config_id

    @property
    def plugin_provider(self):
        r"""Gets the plugin_provider of this PluginConfigInfo.

        :return: The plugin_provider of this PluginConfigInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.PluginProviderEnum`
        """
        return self._plugin_provider

    @plugin_provider.setter
    def plugin_provider(self, plugin_provider):
        r"""Sets the plugin_provider of this PluginConfigInfo.

        :param plugin_provider: The plugin_provider of this PluginConfigInfo.
        :type plugin_provider: :class:`huaweicloudsdkmetastudio.v1.PluginProviderEnum`
        """
        self._plugin_provider = plugin_provider

    @property
    def create_time(self):
        r"""Gets the create_time of this PluginConfigInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this PluginConfigInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this PluginConfigInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this PluginConfigInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this PluginConfigInfo.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this PluginConfigInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this PluginConfigInfo.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param update_time: The update_time of this PluginConfigInfo.
        :type update_time: str
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
        if not isinstance(other, PluginConfigInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
