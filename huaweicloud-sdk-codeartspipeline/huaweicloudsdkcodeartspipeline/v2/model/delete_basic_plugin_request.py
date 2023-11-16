# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteBasicPluginRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'plugin_name': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'plugin_name': 'plugin_name'
    }

    def __init__(self, domain_id=None, plugin_name=None):
        """DeleteBasicPluginRequest

        The model defined in huaweicloud sdk

        :param domain_id: 租户ID
        :type domain_id: str
        :param plugin_name: 是否调用成功
        :type plugin_name: str
        """
        
        

        self._domain_id = None
        self._plugin_name = None
        self.discriminator = None

        self.domain_id = domain_id
        if plugin_name is not None:
            self.plugin_name = plugin_name

    @property
    def domain_id(self):
        """Gets the domain_id of this DeleteBasicPluginRequest.

        租户ID

        :return: The domain_id of this DeleteBasicPluginRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this DeleteBasicPluginRequest.

        租户ID

        :param domain_id: The domain_id of this DeleteBasicPluginRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def plugin_name(self):
        """Gets the plugin_name of this DeleteBasicPluginRequest.

        是否调用成功

        :return: The plugin_name of this DeleteBasicPluginRequest.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """Sets the plugin_name of this DeleteBasicPluginRequest.

        是否调用成功

        :param plugin_name: The plugin_name of this DeleteBasicPluginRequest.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

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
        if not isinstance(other, DeleteBasicPluginRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
