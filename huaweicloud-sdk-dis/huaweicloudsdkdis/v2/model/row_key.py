# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RowKey:

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
        'type': 'str'
    }

    attribute_map = {
        'value': 'value',
        'type': 'type'
    }

    def __init__(self, value=None, type=None):
        r"""RowKey

        The model defined in huaweicloud sdk

        :param value: 通道内JSON数据的JSON属性名，用于生成HBase数据的rowkey。
        :type value: str
        :param type: 通道内JSON数据的JSON属性的类型名称。
        :type type: str
        """
        
        

        self._value = None
        self._type = None
        self.discriminator = None

        self.value = value
        self.type = type

    @property
    def value(self):
        r"""Gets the value of this RowKey.

        通道内JSON数据的JSON属性名，用于生成HBase数据的rowkey。

        :return: The value of this RowKey.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this RowKey.

        通道内JSON数据的JSON属性名，用于生成HBase数据的rowkey。

        :param value: The value of this RowKey.
        :type value: str
        """
        self._value = value

    @property
    def type(self):
        r"""Gets the type of this RowKey.

        通道内JSON数据的JSON属性的类型名称。

        :return: The type of this RowKey.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RowKey.

        通道内JSON数据的JSON属性的类型名称。

        :param type: The type of this RowKey.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, RowKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
