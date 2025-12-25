# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RolePluginConfigInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'plugin_type': 'str',
        'plugin_source': 'str',
        'plugin_config_id': 'str'
    }

    attribute_map = {
        'plugin_type': 'plugin_type',
        'plugin_source': 'plugin_source',
        'plugin_config_id': 'plugin_config_id'
    }

    def __init__(self, plugin_type=None, plugin_source=None, plugin_config_id=None):
        r"""RolePluginConfigInfo

        The model defined in huaweicloud sdk

        :param plugin_type: 插件类型 * WEATHER_QUERY：天气查询 * WEB_SEARCH：网络搜索
        :type plugin_type: str
        :param plugin_source: 使用的插件来源 * PLUGIN_CONFIG：插件配置 * DEFAULT：默认
        :type plugin_source: str
        :param plugin_config_id: 插件配置ID。
        :type plugin_config_id: str
        """
        
        

        self._plugin_type = None
        self._plugin_source = None
        self._plugin_config_id = None
        self.discriminator = None

        self.plugin_type = plugin_type
        self.plugin_source = plugin_source
        if plugin_config_id is not None:
            self.plugin_config_id = plugin_config_id

    @property
    def plugin_type(self):
        r"""Gets the plugin_type of this RolePluginConfigInfo.

        插件类型 * WEATHER_QUERY：天气查询 * WEB_SEARCH：网络搜索

        :return: The plugin_type of this RolePluginConfigInfo.
        :rtype: str
        """
        return self._plugin_type

    @plugin_type.setter
    def plugin_type(self, plugin_type):
        r"""Sets the plugin_type of this RolePluginConfigInfo.

        插件类型 * WEATHER_QUERY：天气查询 * WEB_SEARCH：网络搜索

        :param plugin_type: The plugin_type of this RolePluginConfigInfo.
        :type plugin_type: str
        """
        self._plugin_type = plugin_type

    @property
    def plugin_source(self):
        r"""Gets the plugin_source of this RolePluginConfigInfo.

        使用的插件来源 * PLUGIN_CONFIG：插件配置 * DEFAULT：默认

        :return: The plugin_source of this RolePluginConfigInfo.
        :rtype: str
        """
        return self._plugin_source

    @plugin_source.setter
    def plugin_source(self, plugin_source):
        r"""Sets the plugin_source of this RolePluginConfigInfo.

        使用的插件来源 * PLUGIN_CONFIG：插件配置 * DEFAULT：默认

        :param plugin_source: The plugin_source of this RolePluginConfigInfo.
        :type plugin_source: str
        """
        self._plugin_source = plugin_source

    @property
    def plugin_config_id(self):
        r"""Gets the plugin_config_id of this RolePluginConfigInfo.

        插件配置ID。

        :return: The plugin_config_id of this RolePluginConfigInfo.
        :rtype: str
        """
        return self._plugin_config_id

    @plugin_config_id.setter
    def plugin_config_id(self, plugin_config_id):
        r"""Sets the plugin_config_id of this RolePluginConfigInfo.

        插件配置ID。

        :param plugin_config_id: The plugin_config_id of this RolePluginConfigInfo.
        :type plugin_config_id: str
        """
        self._plugin_config_id = plugin_config_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RolePluginConfigInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
