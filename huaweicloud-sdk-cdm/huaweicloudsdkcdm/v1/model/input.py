# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Input:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'value': 'str',
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'type': 'type'
    }

    def __init__(self, name=None, value=None, type=None):
        """Input

        The model defined in huaweicloud sdk

        :param name: 参数名
        :type name: str
        :param value: 参数值
        :type value: str
        :param type: 值类型
        :type type: str
        """
        
        

        self._name = None
        self._value = None
        self._type = None
        self.discriminator = None

        self.name = name
        self.value = value
        if type is not None:
            self.type = type

    @property
    def name(self):
        """Gets the name of this Input.

        参数名

        :return: The name of this Input.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Input.

        参数名

        :param name: The name of this Input.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        """Gets the value of this Input.

        参数值

        :return: The value of this Input.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Input.

        参数值

        :param value: The value of this Input.
        :type value: str
        """
        self._value = value

    @property
    def type(self):
        """Gets the type of this Input.

        值类型

        :return: The type of this Input.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Input.

        值类型

        :param type: The type of this Input.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, Input):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
