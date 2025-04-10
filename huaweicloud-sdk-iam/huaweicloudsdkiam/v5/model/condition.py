# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Condition:

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
        'value_type': 'str',
        'multi_valued': 'bool',
        'description': 'Description'
    }

    attribute_map = {
        'key': 'key',
        'value_type': 'value_type',
        'multi_valued': 'multi_valued',
        'description': 'description'
    }

    def __init__(self, key=None, value_type=None, multi_valued=None, description=None):
        r"""Condition

        The model defined in huaweicloud sdk

        :param key: 条件键的名称。
        :type key: str
        :param value_type: 条件值的数据类型。
        :type value_type: str
        :param multi_valued: 条件值是否为多值。
        :type multi_valued: bool
        :param description: 
        :type description: :class:`huaweicloudsdkiam.v5.Description`
        """
        
        

        self._key = None
        self._value_type = None
        self._multi_valued = None
        self._description = None
        self.discriminator = None

        self.key = key
        self.value_type = value_type
        self.multi_valued = multi_valued
        self.description = description

    @property
    def key(self):
        r"""Gets the key of this Condition.

        条件键的名称。

        :return: The key of this Condition.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this Condition.

        条件键的名称。

        :param key: The key of this Condition.
        :type key: str
        """
        self._key = key

    @property
    def value_type(self):
        r"""Gets the value_type of this Condition.

        条件值的数据类型。

        :return: The value_type of this Condition.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        r"""Sets the value_type of this Condition.

        条件值的数据类型。

        :param value_type: The value_type of this Condition.
        :type value_type: str
        """
        self._value_type = value_type

    @property
    def multi_valued(self):
        r"""Gets the multi_valued of this Condition.

        条件值是否为多值。

        :return: The multi_valued of this Condition.
        :rtype: bool
        """
        return self._multi_valued

    @multi_valued.setter
    def multi_valued(self, multi_valued):
        r"""Sets the multi_valued of this Condition.

        条件值是否为多值。

        :param multi_valued: The multi_valued of this Condition.
        :type multi_valued: bool
        """
        self._multi_valued = multi_valued

    @property
    def description(self):
        r"""Gets the description of this Condition.

        :return: The description of this Condition.
        :rtype: :class:`huaweicloudsdkiam.v5.Description`
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Condition.

        :param description: The description of this Condition.
        :type description: :class:`huaweicloudsdkiam.v5.Description`
        """
        self._description = description

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
        if not isinstance(other, Condition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
