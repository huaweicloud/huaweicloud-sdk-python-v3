# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DefaultPluginInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'plugin_type': 'PluginTypeEnum',
        'support_default': 'bool'
    }

    attribute_map = {
        'plugin_type': 'plugin_type',
        'support_default': 'support_default'
    }

    def __init__(self, plugin_type=None, support_default=None):
        r"""DefaultPluginInfo

        The model defined in huaweicloud sdk

        :param plugin_type: 
        :type plugin_type: :class:`huaweicloudsdkmetastudio.v1.PluginTypeEnum`
        :param support_default: 支持默认插件。
        :type support_default: bool
        """
        
        

        self._plugin_type = None
        self._support_default = None
        self.discriminator = None

        if plugin_type is not None:
            self.plugin_type = plugin_type
        if support_default is not None:
            self.support_default = support_default

    @property
    def plugin_type(self):
        r"""Gets the plugin_type of this DefaultPluginInfo.

        :return: The plugin_type of this DefaultPluginInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.PluginTypeEnum`
        """
        return self._plugin_type

    @plugin_type.setter
    def plugin_type(self, plugin_type):
        r"""Sets the plugin_type of this DefaultPluginInfo.

        :param plugin_type: The plugin_type of this DefaultPluginInfo.
        :type plugin_type: :class:`huaweicloudsdkmetastudio.v1.PluginTypeEnum`
        """
        self._plugin_type = plugin_type

    @property
    def support_default(self):
        r"""Gets the support_default of this DefaultPluginInfo.

        支持默认插件。

        :return: The support_default of this DefaultPluginInfo.
        :rtype: bool
        """
        return self._support_default

    @support_default.setter
    def support_default(self, support_default):
        r"""Sets the support_default of this DefaultPluginInfo.

        支持默认插件。

        :param support_default: The support_default of this DefaultPluginInfo.
        :type support_default: bool
        """
        self._support_default = support_default

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
        if not isinstance(other, DefaultPluginInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
