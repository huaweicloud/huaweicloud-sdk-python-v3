# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UninstallPluginRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'plugin_name': 'str'
    }

    attribute_map = {
        'plugin_name': 'plugin_name'
    }

    def __init__(self, plugin_name=None):
        r"""UninstallPluginRequestBody

        The model defined in huaweicloud sdk

        :param plugin_name: **参数解释**: 插件名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type plugin_name: str
        """
        
        

        self._plugin_name = None
        self.discriminator = None

        self.plugin_name = plugin_name

    @property
    def plugin_name(self):
        r"""Gets the plugin_name of this UninstallPluginRequestBody.

        **参数解释**: 插件名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The plugin_name of this UninstallPluginRequestBody.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        r"""Sets the plugin_name of this UninstallPluginRequestBody.

        **参数解释**: 插件名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param plugin_name: The plugin_name of this UninstallPluginRequestBody.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

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
        if not isinstance(other, UninstallPluginRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
