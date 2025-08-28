# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePluginConfigReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'plugin_provider': 'PluginProviderEnum',
        'api_key': 'str'
    }

    attribute_map = {
        'plugin_provider': 'plugin_provider',
        'api_key': 'api_key'
    }

    def __init__(self, plugin_provider=None, api_key=None):
        r"""CreatePluginConfigReq

        The model defined in huaweicloud sdk

        :param plugin_provider: 
        :type plugin_provider: :class:`huaweicloudsdkmetastudio.v1.PluginProviderEnum`
        :param api_key: 密钥。
        :type api_key: str
        """
        
        

        self._plugin_provider = None
        self._api_key = None
        self.discriminator = None

        self.plugin_provider = plugin_provider
        if api_key is not None:
            self.api_key = api_key

    @property
    def plugin_provider(self):
        r"""Gets the plugin_provider of this CreatePluginConfigReq.

        :return: The plugin_provider of this CreatePluginConfigReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.PluginProviderEnum`
        """
        return self._plugin_provider

    @plugin_provider.setter
    def plugin_provider(self, plugin_provider):
        r"""Sets the plugin_provider of this CreatePluginConfigReq.

        :param plugin_provider: The plugin_provider of this CreatePluginConfigReq.
        :type plugin_provider: :class:`huaweicloudsdkmetastudio.v1.PluginProviderEnum`
        """
        self._plugin_provider = plugin_provider

    @property
    def api_key(self):
        r"""Gets the api_key of this CreatePluginConfigReq.

        密钥。

        :return: The api_key of this CreatePluginConfigReq.
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        r"""Sets the api_key of this CreatePluginConfigReq.

        密钥。

        :param api_key: The api_key of this CreatePluginConfigReq.
        :type api_key: str
        """
        self._api_key = api_key

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
        if not isinstance(other, CreatePluginConfigReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
