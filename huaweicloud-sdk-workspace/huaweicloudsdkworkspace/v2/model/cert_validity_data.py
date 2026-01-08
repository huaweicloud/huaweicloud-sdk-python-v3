# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CertValidityData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'value': 'int',
        'start_from': 'str'
    }

    attribute_map = {
        'type': 'type',
        'value': 'value',
        'start_from': 'start_from'
    }

    def __init__(self, type=None, value=None, start_from=None):
        r"""CertValidityData

        The model defined in huaweicloud sdk

        :param type: 时间单位, YEAR 年。
        :type type: str
        :param value: 时间数值。
        :type value: int
        :param start_from: 证书过期时间。
        :type start_from: str
        """
        
        

        self._type = None
        self._value = None
        self._start_from = None
        self.discriminator = None

        self.type = type
        self.value = value
        if start_from is not None:
            self.start_from = start_from

    @property
    def type(self):
        r"""Gets the type of this CertValidityData.

        时间单位, YEAR 年。

        :return: The type of this CertValidityData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CertValidityData.

        时间单位, YEAR 年。

        :param type: The type of this CertValidityData.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        r"""Gets the value of this CertValidityData.

        时间数值。

        :return: The value of this CertValidityData.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this CertValidityData.

        时间数值。

        :param value: The value of this CertValidityData.
        :type value: int
        """
        self._value = value

    @property
    def start_from(self):
        r"""Gets the start_from of this CertValidityData.

        证书过期时间。

        :return: The start_from of this CertValidityData.
        :rtype: str
        """
        return self._start_from

    @start_from.setter
    def start_from(self, start_from):
        r"""Sets the start_from of this CertValidityData.

        证书过期时间。

        :param start_from: The start_from of this CertValidityData.
        :type start_from: str
        """
        self._start_from = start_from

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
        if not isinstance(other, CertValidityData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
