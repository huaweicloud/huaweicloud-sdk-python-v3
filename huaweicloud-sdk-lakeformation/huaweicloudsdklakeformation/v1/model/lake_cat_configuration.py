# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LakeCatConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'value': 'str',
        'description': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value',
        'description': 'description'
    }

    def __init__(self, key=None, value=None, description=None):
        """LakeCatConfiguration

        The model defined in huaweicloud sdk

        :param key: 配置项的key
        :type key: str
        :param value: 配置项的值
        :type value: str
        :param description: 配置项描述
        :type description: str
        """
        
        

        self._key = None
        self._value = None
        self._description = None
        self.discriminator = None

        self.key = key
        self.value = value
        if description is not None:
            self.description = description

    @property
    def key(self):
        """Gets the key of this LakeCatConfiguration.

        配置项的key

        :return: The key of this LakeCatConfiguration.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this LakeCatConfiguration.

        配置项的key

        :param key: The key of this LakeCatConfiguration.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        """Gets the value of this LakeCatConfiguration.

        配置项的值

        :return: The value of this LakeCatConfiguration.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this LakeCatConfiguration.

        配置项的值

        :param value: The value of this LakeCatConfiguration.
        :type value: str
        """
        self._value = value

    @property
    def description(self):
        """Gets the description of this LakeCatConfiguration.

        配置项描述

        :return: The description of this LakeCatConfiguration.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LakeCatConfiguration.

        配置项描述

        :param description: The description of this LakeCatConfiguration.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, LakeCatConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
