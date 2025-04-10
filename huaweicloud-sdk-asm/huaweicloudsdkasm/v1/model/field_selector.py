# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FieldSelector:

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
        'values': 'list[str]'
    }

    attribute_map = {
        'key': 'key',
        'operator': 'operator',
        'values': 'values'
    }

    def __init__(self, key=None, operator=None, values=None):
        r"""FieldSelector

        The model defined in huaweicloud sdk

        :param key: Key值
        :type key: str
        :param operator: 操作符，仅支持取值\&quot;In\&quot;
        :type operator: str
        :param values: Value值
        :type values: list[str]
        """
        
        

        self._key = None
        self._operator = None
        self._values = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if operator is not None:
            self.operator = operator
        if values is not None:
            self.values = values

    @property
    def key(self):
        r"""Gets the key of this FieldSelector.

        Key值

        :return: The key of this FieldSelector.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this FieldSelector.

        Key值

        :param key: The key of this FieldSelector.
        :type key: str
        """
        self._key = key

    @property
    def operator(self):
        r"""Gets the operator of this FieldSelector.

        操作符，仅支持取值\"In\"

        :return: The operator of this FieldSelector.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this FieldSelector.

        操作符，仅支持取值\"In\"

        :param operator: The operator of this FieldSelector.
        :type operator: str
        """
        self._operator = operator

    @property
    def values(self):
        r"""Gets the values of this FieldSelector.

        Value值

        :return: The values of this FieldSelector.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this FieldSelector.

        Value值

        :param values: The values of this FieldSelector.
        :type values: list[str]
        """
        self._values = values

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
        if not isinstance(other, FieldSelector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
