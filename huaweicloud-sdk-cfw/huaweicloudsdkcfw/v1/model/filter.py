# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Filter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'field': 'str',
        'values': 'list[str]',
        'operator': 'str'
    }

    attribute_map = {
        'field': 'field',
        'values': 'values',
        'operator': 'operator'
    }

    def __init__(self, field=None, values=None, operator=None):
        r"""Filter

        The model defined in huaweicloud sdk

        :param field: **参数解释**： 日志字段，如src_ip **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type field: str
        :param values: **参数解释**： 值 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type values: list[str]
        :param operator: **参数解释**： 操作符 **约束限制**： 不涉及 **取值范围**： equal 等于 not_equal 不等于 contain 包含 starts_with 以开始 **默认取值**： 不涉及
        :type operator: str
        """
        
        

        self._field = None
        self._values = None
        self._operator = None
        self.discriminator = None

        self.field = field
        if values is not None:
            self.values = values
        self.operator = operator

    @property
    def field(self):
        r"""Gets the field of this Filter.

        **参数解释**： 日志字段，如src_ip **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The field of this Filter.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        r"""Sets the field of this Filter.

        **参数解释**： 日志字段，如src_ip **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param field: The field of this Filter.
        :type field: str
        """
        self._field = field

    @property
    def values(self):
        r"""Gets the values of this Filter.

        **参数解释**： 值 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The values of this Filter.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this Filter.

        **参数解释**： 值 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param values: The values of this Filter.
        :type values: list[str]
        """
        self._values = values

    @property
    def operator(self):
        r"""Gets the operator of this Filter.

        **参数解释**： 操作符 **约束限制**： 不涉及 **取值范围**： equal 等于 not_equal 不等于 contain 包含 starts_with 以开始 **默认取值**： 不涉及

        :return: The operator of this Filter.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this Filter.

        **参数解释**： 操作符 **约束限制**： 不涉及 **取值范围**： equal 等于 not_equal 不等于 contain 包含 starts_with 以开始 **默认取值**： 不涉及

        :param operator: The operator of this Filter.
        :type operator: str
        """
        self._operator = operator

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
        if not isinstance(other, Filter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
