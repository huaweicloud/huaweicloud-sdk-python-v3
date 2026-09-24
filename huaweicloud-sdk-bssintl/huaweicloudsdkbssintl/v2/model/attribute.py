# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Attribute:

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
        'name': 'str',
        'value': 'str',
        'unit': 'str',
        'linear_range': 'LinearRange'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name',
        'value': 'value',
        'unit': 'unit',
        'linear_range': 'linear_range'
    }

    def __init__(self, code=None, name=None, value=None, unit=None, linear_range=None):
        r"""Attribute

        The model defined in huaweicloud sdk

        :param code: 属性编码
        :type code: str
        :param name: 属性名称
        :type name: str
        :param value: 属性取值
        :type value: str
        :param unit: 属性单位
        :type unit: str
        :param linear_range: 
        :type linear_range: :class:`huaweicloudsdkbssintl.v2.LinearRange`
        """
        
        

        self._code = None
        self._name = None
        self._value = None
        self._unit = None
        self._linear_range = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if unit is not None:
            self.unit = unit
        if linear_range is not None:
            self.linear_range = linear_range

    @property
    def code(self):
        r"""Gets the code of this Attribute.

        属性编码

        :return: The code of this Attribute.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this Attribute.

        属性编码

        :param code: The code of this Attribute.
        :type code: str
        """
        self._code = code

    @property
    def name(self):
        r"""Gets the name of this Attribute.

        属性名称

        :return: The name of this Attribute.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Attribute.

        属性名称

        :param name: The name of this Attribute.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        r"""Gets the value of this Attribute.

        属性取值

        :return: The value of this Attribute.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this Attribute.

        属性取值

        :param value: The value of this Attribute.
        :type value: str
        """
        self._value = value

    @property
    def unit(self):
        r"""Gets the unit of this Attribute.

        属性单位

        :return: The unit of this Attribute.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this Attribute.

        属性单位

        :param unit: The unit of this Attribute.
        :type unit: str
        """
        self._unit = unit

    @property
    def linear_range(self):
        r"""Gets the linear_range of this Attribute.

        :return: The linear_range of this Attribute.
        :rtype: :class:`huaweicloudsdkbssintl.v2.LinearRange`
        """
        return self._linear_range

    @linear_range.setter
    def linear_range(self, linear_range):
        r"""Sets the linear_range of this Attribute.

        :param linear_range: The linear_range of this Attribute.
        :type linear_range: :class:`huaweicloudsdkbssintl.v2.LinearRange`
        """
        self._linear_range = linear_range

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
        if not isinstance(other, Attribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
