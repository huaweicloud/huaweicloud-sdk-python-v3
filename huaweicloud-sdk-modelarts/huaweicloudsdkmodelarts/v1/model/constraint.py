# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Constraint:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attribute': 'str',
        'operator': 'str',
        'value': 'object'
    }

    attribute_map = {
        'attribute': 'attribute',
        'operator': 'operator',
        'value': 'value'
    }

    def __init__(self, attribute=None, operator=None, value=None):
        r"""Constraint

        The model defined in huaweicloud sdk

        :param attribute: 条件属性，参数的某个字段值。
        :type attribute: str
        :param operator: 操作，当前只支持equal操作。
        :type operator: str
        :param value: 取值。
        :type value: object
        """
        
        

        self._attribute = None
        self._operator = None
        self._value = None
        self.discriminator = None

        if attribute is not None:
            self.attribute = attribute
        if operator is not None:
            self.operator = operator
        if value is not None:
            self.value = value

    @property
    def attribute(self):
        r"""Gets the attribute of this Constraint.

        条件属性，参数的某个字段值。

        :return: The attribute of this Constraint.
        :rtype: str
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        r"""Sets the attribute of this Constraint.

        条件属性，参数的某个字段值。

        :param attribute: The attribute of this Constraint.
        :type attribute: str
        """
        self._attribute = attribute

    @property
    def operator(self):
        r"""Gets the operator of this Constraint.

        操作，当前只支持equal操作。

        :return: The operator of this Constraint.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this Constraint.

        操作，当前只支持equal操作。

        :param operator: The operator of this Constraint.
        :type operator: str
        """
        self._operator = operator

    @property
    def value(self):
        r"""Gets the value of this Constraint.

        取值。

        :return: The value of this Constraint.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this Constraint.

        取值。

        :param value: The value of this Constraint.
        :type value: object
        """
        self._value = value

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Constraint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
