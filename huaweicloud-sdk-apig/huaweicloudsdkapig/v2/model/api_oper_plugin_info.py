# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiOperPluginInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'env_id': 'str',
        'plugin_ids': 'list[str]'
    }

    attribute_map = {
        'env_id': 'env_id',
        'plugin_ids': 'plugin_ids'
    }

    def __init__(self, env_id=None, plugin_ids=None):
        """ApiOperPluginInfo

        The model defined in huaweicloud sdk

        :param env_id: 绑定API的环境编码。
        :type env_id: str
        :param plugin_ids: 绑定的插件编码列表。
        :type plugin_ids: list[str]
        """
        
        

        self._env_id = None
        self._plugin_ids = None
        self.discriminator = None

        self.env_id = env_id
        self.plugin_ids = plugin_ids

    @property
    def env_id(self):
        """Gets the env_id of this ApiOperPluginInfo.

        绑定API的环境编码。

        :return: The env_id of this ApiOperPluginInfo.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this ApiOperPluginInfo.

        绑定API的环境编码。

        :param env_id: The env_id of this ApiOperPluginInfo.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def plugin_ids(self):
        """Gets the plugin_ids of this ApiOperPluginInfo.

        绑定的插件编码列表。

        :return: The plugin_ids of this ApiOperPluginInfo.
        :rtype: list[str]
        """
        return self._plugin_ids

    @plugin_ids.setter
    def plugin_ids(self, plugin_ids):
        """Sets the plugin_ids of this ApiOperPluginInfo.

        绑定的插件编码列表。

        :param plugin_ids: The plugin_ids of this ApiOperPluginInfo.
        :type plugin_ids: list[str]
        """
        self._plugin_ids = plugin_ids

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
        if not isinstance(other, ApiOperPluginInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
