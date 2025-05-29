# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Constraints:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'errormsg': 'str',
        'type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'errormsg': 'errormsg',
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, errormsg=None, type=None, value=None):
        r"""Constraints

        The model defined in huaweicloud sdk

        :param errormsg: 错误信息
        :type errormsg: str
        :param type: 类型
        :type type: str
        :param value: 参考值
        :type value: str
        """
        
        

        self._errormsg = None
        self._type = None
        self._value = None
        self.discriminator = None

        if errormsg is not None:
            self.errormsg = errormsg
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value

    @property
    def errormsg(self):
        r"""Gets the errormsg of this Constraints.

        错误信息

        :return: The errormsg of this Constraints.
        :rtype: str
        """
        return self._errormsg

    @errormsg.setter
    def errormsg(self, errormsg):
        r"""Sets the errormsg of this Constraints.

        错误信息

        :param errormsg: The errormsg of this Constraints.
        :type errormsg: str
        """
        self._errormsg = errormsg

    @property
    def type(self):
        r"""Gets the type of this Constraints.

        类型

        :return: The type of this Constraints.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Constraints.

        类型

        :param type: The type of this Constraints.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        r"""Gets the value of this Constraints.

        参考值

        :return: The value of this Constraints.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this Constraints.

        参考值

        :param value: The value of this Constraints.
        :type value: str
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
        if not isinstance(other, Constraints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
