# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'plugin_id': 'str',
        'config': 'dict(str, object)'
    }

    attribute_map = {
        'plugin_id': 'plugin_id',
        'config': 'config'
    }

    def __init__(self, plugin_id=None, config=None):
        r"""PluginConfig

        The model defined in huaweicloud sdk

        :param plugin_id: 插件id
        :type plugin_id: str
        :param config: 单个插件参数
        :type config: dict(str, object)
        """
        
        

        self._plugin_id = None
        self._config = None
        self.discriminator = None

        if plugin_id is not None:
            self.plugin_id = plugin_id
        if config is not None:
            self.config = config

    @property
    def plugin_id(self):
        r"""Gets the plugin_id of this PluginConfig.

        插件id

        :return: The plugin_id of this PluginConfig.
        :rtype: str
        """
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, plugin_id):
        r"""Sets the plugin_id of this PluginConfig.

        插件id

        :param plugin_id: The plugin_id of this PluginConfig.
        :type plugin_id: str
        """
        self._plugin_id = plugin_id

    @property
    def config(self):
        r"""Gets the config of this PluginConfig.

        单个插件参数

        :return: The config of this PluginConfig.
        :rtype: dict(str, object)
        """
        return self._config

    @config.setter
    def config(self, config):
        r"""Sets the config of this PluginConfig.

        单个插件参数

        :param config: The config of this PluginConfig.
        :type config: dict(str, object)
        """
        self._config = config

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
        if not isinstance(other, PluginConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
