# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsChartsTagValueCount:

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
        'count': 'int'
    }

    attribute_map = {
        'value': 'value',
        'count': 'count'
    }

    def __init__(self, value=None, count=None):
        r"""OpsChartsTagValueCount

        The model defined in huaweicloud sdk

        :param value: 标签值。
        :type value: str
        :param count: 出现次数。
        :type count: int
        """
        
        

        self._value = None
        self._count = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if count is not None:
            self.count = count

    @property
    def value(self):
        r"""Gets the value of this OpsChartsTagValueCount.

        标签值。

        :return: The value of this OpsChartsTagValueCount.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this OpsChartsTagValueCount.

        标签值。

        :param value: The value of this OpsChartsTagValueCount.
        :type value: str
        """
        self._value = value

    @property
    def count(self):
        r"""Gets the count of this OpsChartsTagValueCount.

        出现次数。

        :return: The count of this OpsChartsTagValueCount.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this OpsChartsTagValueCount.

        出现次数。

        :param count: The count of this OpsChartsTagValueCount.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, OpsChartsTagValueCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
