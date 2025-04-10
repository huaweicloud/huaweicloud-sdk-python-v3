# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnvVariableBase:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'variable_value': 'str'
    }

    attribute_map = {
        'variable_value': 'variable_value'
    }

    def __init__(self, variable_value=None):
        r"""EnvVariableBase

        The model defined in huaweicloud sdk

        :param variable_value: 变量值支持英文字母、数字、英文格式的下划线、中划线，斜线（/）、点、冒号，1 ~ 255个字符。
        :type variable_value: str
        """
        
        

        self._variable_value = None
        self.discriminator = None

        self.variable_value = variable_value

    @property
    def variable_value(self):
        r"""Gets the variable_value of this EnvVariableBase.

        变量值支持英文字母、数字、英文格式的下划线、中划线，斜线（/）、点、冒号，1 ~ 255个字符。

        :return: The variable_value of this EnvVariableBase.
        :rtype: str
        """
        return self._variable_value

    @variable_value.setter
    def variable_value(self, variable_value):
        r"""Sets the variable_value of this EnvVariableBase.

        变量值支持英文字母、数字、英文格式的下划线、中划线，斜线（/）、点、冒号，1 ~ 255个字符。

        :param variable_value: The variable_value of this EnvVariableBase.
        :type variable_value: str
        """
        self._variable_value = variable_value

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
        if not isinstance(other, EnvVariableBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
