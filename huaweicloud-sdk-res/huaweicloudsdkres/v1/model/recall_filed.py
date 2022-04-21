# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecallFiled:

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
        'value': 'int'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, name=None, value=None):
        """RecallFiled

        The model defined in huaweicloud sdk

        :param name: 字段名称。
        :type name: str
        :param value: 使用字段值的个数。
        :type value: int
        """
        
        

        self._name = None
        self._value = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if value is not None:
            self.value = value

    @property
    def name(self):
        """Gets the name of this RecallFiled.

        字段名称。

        :return: The name of this RecallFiled.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RecallFiled.

        字段名称。

        :param name: The name of this RecallFiled.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        """Gets the value of this RecallFiled.

        使用字段值的个数。

        :return: The value of this RecallFiled.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this RecallFiled.

        使用字段值的个数。

        :param value: The value of this RecallFiled.
        :type value: int
        """
        self._value = value

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
        if not isinstance(other, RecallFiled):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
