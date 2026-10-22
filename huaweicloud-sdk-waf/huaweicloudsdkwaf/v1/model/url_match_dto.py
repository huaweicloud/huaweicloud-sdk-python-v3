# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UrlMatchDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operator': 'str',
        'value': 'str'
    }

    attribute_map = {
        'operator': 'operator',
        'value': 'value'
    }

    def __init__(self, operator=None, value=None):
        r"""UrlMatchDTO

        The model defined in huaweicloud sdk

        :param operator: 匹配算子（EQUAL/CONTAIN）
        :type operator: str
        :param value: 匹配值（URL 或 URL 片段）
        :type value: str
        """
        
        

        self._operator = None
        self._value = None
        self.discriminator = None

        self.operator = operator
        self.value = value

    @property
    def operator(self):
        r"""Gets the operator of this UrlMatchDTO.

        匹配算子（EQUAL/CONTAIN）

        :return: The operator of this UrlMatchDTO.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this UrlMatchDTO.

        匹配算子（EQUAL/CONTAIN）

        :param operator: The operator of this UrlMatchDTO.
        :type operator: str
        """
        self._operator = operator

    @property
    def value(self):
        r"""Gets the value of this UrlMatchDTO.

        匹配值（URL 或 URL 片段）

        :return: The value of this UrlMatchDTO.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this UrlMatchDTO.

        匹配值（URL 或 URL 片段）

        :param value: The value of this UrlMatchDTO.
        :type value: str
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
        if not isinstance(other, UrlMatchDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
