# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IndexUsageCondition:

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
        'min_value': 'float',
        'max_value': 'float'
    }

    attribute_map = {
        'field': 'field',
        'min_value': 'min_value',
        'max_value': 'max_value'
    }

    def __init__(self, field=None, min_value=None, max_value=None):
        r"""IndexUsageCondition

        The model defined in huaweicloud sdk

        :param field: 过滤字段
        :type field: str
        :param min_value: 最小值
        :type min_value: float
        :param max_value: 最大值
        :type max_value: float
        """
        
        

        self._field = None
        self._min_value = None
        self._max_value = None
        self.discriminator = None

        if field is not None:
            self.field = field
        if min_value is not None:
            self.min_value = min_value
        if max_value is not None:
            self.max_value = max_value

    @property
    def field(self):
        r"""Gets the field of this IndexUsageCondition.

        过滤字段

        :return: The field of this IndexUsageCondition.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        r"""Sets the field of this IndexUsageCondition.

        过滤字段

        :param field: The field of this IndexUsageCondition.
        :type field: str
        """
        self._field = field

    @property
    def min_value(self):
        r"""Gets the min_value of this IndexUsageCondition.

        最小值

        :return: The min_value of this IndexUsageCondition.
        :rtype: float
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        r"""Sets the min_value of this IndexUsageCondition.

        最小值

        :param min_value: The min_value of this IndexUsageCondition.
        :type min_value: float
        """
        self._min_value = min_value

    @property
    def max_value(self):
        r"""Gets the max_value of this IndexUsageCondition.

        最大值

        :return: The max_value of this IndexUsageCondition.
        :rtype: float
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        r"""Sets the max_value of this IndexUsageCondition.

        最大值

        :param max_value: The max_value of this IndexUsageCondition.
        :type max_value: float
        """
        self._max_value = max_value

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
        if not isinstance(other, IndexUsageCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
