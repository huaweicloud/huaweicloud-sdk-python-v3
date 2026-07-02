# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPluginsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'plugins_modifying': 'bool',
        'plugins': 'list[PluginEntity]'
    }

    attribute_map = {
        'plugins_modifying': 'plugins_modifying',
        'plugins': 'plugins'
    }

    def __init__(self, plugins_modifying=None, plugins=None):
        r"""ListPluginsResponse

        The model defined in huaweicloud sdk

        :param plugins_modifying: 插件是否在变更中。
        :type plugins_modifying: bool
        :param plugins: 插件信息列表。
        :type plugins: list[:class:`huaweicloudsdkrabbitmq.v2.PluginEntity`]
        """
        
        super().__init__()

        self._plugins_modifying = None
        self._plugins = None
        self.discriminator = None

        if plugins_modifying is not None:
            self.plugins_modifying = plugins_modifying
        if plugins is not None:
            self.plugins = plugins

    @property
    def plugins_modifying(self):
        r"""Gets the plugins_modifying of this ListPluginsResponse.

        插件是否在变更中。

        :return: The plugins_modifying of this ListPluginsResponse.
        :rtype: bool
        """
        return self._plugins_modifying

    @plugins_modifying.setter
    def plugins_modifying(self, plugins_modifying):
        r"""Sets the plugins_modifying of this ListPluginsResponse.

        插件是否在变更中。

        :param plugins_modifying: The plugins_modifying of this ListPluginsResponse.
        :type plugins_modifying: bool
        """
        self._plugins_modifying = plugins_modifying

    @property
    def plugins(self):
        r"""Gets the plugins of this ListPluginsResponse.

        插件信息列表。

        :return: The plugins of this ListPluginsResponse.
        :rtype: list[:class:`huaweicloudsdkrabbitmq.v2.PluginEntity`]
        """
        return self._plugins

    @plugins.setter
    def plugins(self, plugins):
        r"""Sets the plugins of this ListPluginsResponse.

        插件信息列表。

        :param plugins: The plugins of this ListPluginsResponse.
        :type plugins: list[:class:`huaweicloudsdkrabbitmq.v2.PluginEntity`]
        """
        self._plugins = plugins

    def to_dict(self):
        import warnings
        warnings.warn("ListPluginsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListPluginsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
