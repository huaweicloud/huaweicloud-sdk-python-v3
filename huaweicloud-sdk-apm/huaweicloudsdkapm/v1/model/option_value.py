# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OptionValue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'value': 'str',
        'hint': 'str'
    }

    attribute_map = {
        'value': 'value',
        'hint': 'hint'
    }

    def __init__(self, value=None, hint=None):
        r"""OptionValue

        The model defined in huaweicloud sdk

        :param value: 可选值
        :type value: str
        :param hint: 提示信息
        :type hint: str
        """
        
        

        self._value = None
        self._hint = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if hint is not None:
            self.hint = hint

    @property
    def value(self):
        r"""Gets the value of this OptionValue.

        可选值

        :return: The value of this OptionValue.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this OptionValue.

        可选值

        :param value: The value of this OptionValue.
        :type value: str
        """
        self._value = value

    @property
    def hint(self):
        r"""Gets the hint of this OptionValue.

        提示信息

        :return: The hint of this OptionValue.
        :rtype: str
        """
        return self._hint

    @hint.setter
    def hint(self, hint):
        r"""Sets the hint of this OptionValue.

        提示信息

        :param hint: The hint of this OptionValue.
        :type hint: str
        """
        self._hint = hint

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
        if not isinstance(other, OptionValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
