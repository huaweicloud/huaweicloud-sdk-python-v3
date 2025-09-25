# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Dictionary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'value': 'str',
        'values': 'list[str]'
    }

    attribute_map = {
        'code': 'code',
        'value': 'value',
        'values': 'values'
    }

    def __init__(self, code=None, value=None, values=None):
        r"""Dictionary

        The model defined in huaweicloud sdk

        :param code: **参数解释**： 字典编码 **取值范围**： 字符长度1-256位 
        :type code: str
        :param value: **参数解释**： 字典值（单个值） **取值范围**： 字符长度1-65535位 
        :type value: str
        :param values: **参数解释**： 字典值（多个值） **取值范围**： 
        :type values: list[str]
        """
        
        

        self._code = None
        self._value = None
        self._values = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if value is not None:
            self.value = value
        if values is not None:
            self.values = values

    @property
    def code(self):
        r"""Gets the code of this Dictionary.

        **参数解释**： 字典编码 **取值范围**： 字符长度1-256位 

        :return: The code of this Dictionary.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this Dictionary.

        **参数解释**： 字典编码 **取值范围**： 字符长度1-256位 

        :param code: The code of this Dictionary.
        :type code: str
        """
        self._code = code

    @property
    def value(self):
        r"""Gets the value of this Dictionary.

        **参数解释**： 字典值（单个值） **取值范围**： 字符长度1-65535位 

        :return: The value of this Dictionary.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this Dictionary.

        **参数解释**： 字典值（单个值） **取值范围**： 字符长度1-65535位 

        :param value: The value of this Dictionary.
        :type value: str
        """
        self._value = value

    @property
    def values(self):
        r"""Gets the values of this Dictionary.

        **参数解释**： 字典值（多个值） **取值范围**： 

        :return: The values of this Dictionary.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this Dictionary.

        **参数解释**： 字典值（多个值） **取值范围**： 

        :param values: The values of this Dictionary.
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
        if not isinstance(other, Dictionary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
