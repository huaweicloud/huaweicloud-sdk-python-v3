# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginOperApiInfo:

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
        'api_ids': 'list[str]'
    }

    attribute_map = {
        'env_id': 'env_id',
        'api_ids': 'api_ids'
    }

    def __init__(self, env_id=None, api_ids=None):
        """PluginOperApiInfo

        The model defined in huaweicloud sdk

        :param env_id: 绑定API的环境编码。
        :type env_id: str
        :param api_ids: 绑定的API编码列表。
        :type api_ids: list[str]
        """
        
        

        self._env_id = None
        self._api_ids = None
        self.discriminator = None

        self.env_id = env_id
        self.api_ids = api_ids

    @property
    def env_id(self):
        """Gets the env_id of this PluginOperApiInfo.

        绑定API的环境编码。

        :return: The env_id of this PluginOperApiInfo.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this PluginOperApiInfo.

        绑定API的环境编码。

        :param env_id: The env_id of this PluginOperApiInfo.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def api_ids(self):
        """Gets the api_ids of this PluginOperApiInfo.

        绑定的API编码列表。

        :return: The api_ids of this PluginOperApiInfo.
        :rtype: list[str]
        """
        return self._api_ids

    @api_ids.setter
    def api_ids(self, api_ids):
        """Sets the api_ids of this PluginOperApiInfo.

        绑定的API编码列表。

        :param api_ids: The api_ids of this PluginOperApiInfo.
        :type api_ids: list[str]
        """
        self._api_ids = api_ids

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
        if not isinstance(other, PluginOperApiInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
