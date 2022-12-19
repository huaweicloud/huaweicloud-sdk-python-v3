# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskAdvancedSettings:

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
        'option_value': 'str',
        'description': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value',
        'option_value': 'option_value',
        'description': 'description'
    }

    def __init__(self, key=None, value=None, option_value=None, description=None):
        """TaskAdvancedSettings

        The model defined in huaweicloud sdk

        :param key: 高级选项对应的名称
        :type key: str
        :param value: 高级选项对应的取值
        :type value: str
        :param option_value: 高级选项对应的可选项
        :type option_value: str
        :param description: 高级选项对应的中文描述
        :type description: str
        """
        
        

        self._key = None
        self._value = None
        self._option_value = None
        self._description = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if option_value is not None:
            self.option_value = option_value
        if description is not None:
            self.description = description

    @property
    def key(self):
        """Gets the key of this TaskAdvancedSettings.

        高级选项对应的名称

        :return: The key of this TaskAdvancedSettings.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this TaskAdvancedSettings.

        高级选项对应的名称

        :param key: The key of this TaskAdvancedSettings.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        """Gets the value of this TaskAdvancedSettings.

        高级选项对应的取值

        :return: The value of this TaskAdvancedSettings.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TaskAdvancedSettings.

        高级选项对应的取值

        :param value: The value of this TaskAdvancedSettings.
        :type value: str
        """
        self._value = value

    @property
    def option_value(self):
        """Gets the option_value of this TaskAdvancedSettings.

        高级选项对应的可选项

        :return: The option_value of this TaskAdvancedSettings.
        :rtype: str
        """
        return self._option_value

    @option_value.setter
    def option_value(self, option_value):
        """Sets the option_value of this TaskAdvancedSettings.

        高级选项对应的可选项

        :param option_value: The option_value of this TaskAdvancedSettings.
        :type option_value: str
        """
        self._option_value = option_value

    @property
    def description(self):
        """Gets the description of this TaskAdvancedSettings.

        高级选项对应的中文描述

        :return: The description of this TaskAdvancedSettings.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaskAdvancedSettings.

        高级选项对应的中文描述

        :param description: The description of this TaskAdvancedSettings.
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
        if not isinstance(other, TaskAdvancedSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
