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
        'values': 'str',
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'values': 'values',
        'type': 'type'
    }

    def __init__(self, name=None, values=None, type=None):
        """Input - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._values = None
        self._type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if values is not None:
            self.values = values
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
        :type: str
        """
        self._name = name

    @property
    def values(self):
        """Gets the values of this Input.

        参数值

        :return: The values of this Input.
        :rtype: str
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this Input.

        参数值

        :param values: The values of this Input.
        :type: str
        """
        self._values = values

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
        :type: str
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
