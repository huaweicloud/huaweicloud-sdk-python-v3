# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AwParamBasicValue:

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
        'value_range': 'str'
    }

    attribute_map = {
        'value': 'value',
        'value_range': 'value_range'
    }

    def __init__(self, value=None, value_range=None):
        r"""AwParamBasicValue

        The model defined in huaweicloud sdk

        :param value: 参数默认值，用例有效
        :type value: str
        :param value_range: 参数值范围，逻辑用例有效
        :type value_range: str
        """
        
        

        self._value = None
        self._value_range = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if value_range is not None:
            self.value_range = value_range

    @property
    def value(self):
        r"""Gets the value of this AwParamBasicValue.

        参数默认值，用例有效

        :return: The value of this AwParamBasicValue.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this AwParamBasicValue.

        参数默认值，用例有效

        :param value: The value of this AwParamBasicValue.
        :type value: str
        """
        self._value = value

    @property
    def value_range(self):
        r"""Gets the value_range of this AwParamBasicValue.

        参数值范围，逻辑用例有效

        :return: The value_range of this AwParamBasicValue.
        :rtype: str
        """
        return self._value_range

    @value_range.setter
    def value_range(self, value_range):
        r"""Sets the value_range of this AwParamBasicValue.

        参数值范围，逻辑用例有效

        :param value_range: The value_range of this AwParamBasicValue.
        :type value_range: str
        """
        self._value_range = value_range

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
        if not isinstance(other, AwParamBasicValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
