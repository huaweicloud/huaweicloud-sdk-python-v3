# coding: utf-8

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
        'key': 'str',
        'operator': 'str',
        'value': 'list[str]'
    }

    attribute_map = {
        'key': 'key',
        'operator': 'operator',
        'value': 'value'
    }

    def __init__(self, key=None, operator=None, value=None):
        r"""Filter

        The model defined in huaweicloud sdk

        :param key: 分组条件键值。
        :type key: str
        :param operator: 分组条件键值键关系，支持between（范围）、like（类似）、in（包含）、not（非）。
        :type operator: str
        :param value: 分组条件键对应值。
        :type value: list[str]
        """
        
        

        self._key = None
        self._operator = None
        self._value = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if operator is not None:
            self.operator = operator
        if value is not None:
            self.value = value

    @property
    def key(self):
        r"""Gets the key of this Filter.

        分组条件键值。

        :return: The key of this Filter.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this Filter.

        分组条件键值。

        :param key: The key of this Filter.
        :type key: str
        """
        self._key = key

    @property
    def operator(self):
        r"""Gets the operator of this Filter.

        分组条件键值键关系，支持between（范围）、like（类似）、in（包含）、not（非）。

        :return: The operator of this Filter.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this Filter.

        分组条件键值键关系，支持between（范围）、like（类似）、in（包含）、not（非）。

        :param operator: The operator of this Filter.
        :type operator: str
        """
        self._operator = operator

    @property
    def value(self):
        r"""Gets the value of this Filter.

        分组条件键对应值。

        :return: The value of this Filter.
        :rtype: list[str]
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this Filter.

        分组条件键对应值。

        :param value: The value of this Filter.
        :type value: list[str]
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
        if not isinstance(other, Filter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
