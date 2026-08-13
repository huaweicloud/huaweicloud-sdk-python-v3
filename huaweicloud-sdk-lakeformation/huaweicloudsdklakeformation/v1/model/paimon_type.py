# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PaimonType:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'precision': 'int',
        'scale': 'int',
        'length': 'int'
    }

    attribute_map = {
        'name': 'name',
        'precision': 'precision',
        'scale': 'scale',
        'length': 'length'
    }

    def __init__(self, name=None, precision=None, scale=None, length=None):
        r"""PaimonType

        The model defined in huaweicloud sdk

        :param name: Paimon类型名称
        :type name: str
        :param precision: 精度，适用于 DECIMAL(p,s) 的 p（1-38），以及 TIME(p)/TIMESTAMP(p)/TIMESTAMP_LTZ(p) 的小数秒精度 p（0-9）。
        :type precision: int
        :param scale: 标度，适用于 DECIMAL(p,s) 的 s（0-precision）。
        :type scale: int
        :param length: CHAR(n)、VARCHAR(n)、BINARY(n)、VARBINARY(n)的长度（n）
        :type length: int
        """
        
        

        self._name = None
        self._precision = None
        self._scale = None
        self._length = None
        self.discriminator = None

        self.name = name
        if precision is not None:
            self.precision = precision
        if scale is not None:
            self.scale = scale
        if length is not None:
            self.length = length

    @property
    def name(self):
        r"""Gets the name of this PaimonType.

        Paimon类型名称

        :return: The name of this PaimonType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PaimonType.

        Paimon类型名称

        :param name: The name of this PaimonType.
        :type name: str
        """
        self._name = name

    @property
    def precision(self):
        r"""Gets the precision of this PaimonType.

        精度，适用于 DECIMAL(p,s) 的 p（1-38），以及 TIME(p)/TIMESTAMP(p)/TIMESTAMP_LTZ(p) 的小数秒精度 p（0-9）。

        :return: The precision of this PaimonType.
        :rtype: int
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        r"""Sets the precision of this PaimonType.

        精度，适用于 DECIMAL(p,s) 的 p（1-38），以及 TIME(p)/TIMESTAMP(p)/TIMESTAMP_LTZ(p) 的小数秒精度 p（0-9）。

        :param precision: The precision of this PaimonType.
        :type precision: int
        """
        self._precision = precision

    @property
    def scale(self):
        r"""Gets the scale of this PaimonType.

        标度，适用于 DECIMAL(p,s) 的 s（0-precision）。

        :return: The scale of this PaimonType.
        :rtype: int
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        r"""Sets the scale of this PaimonType.

        标度，适用于 DECIMAL(p,s) 的 s（0-precision）。

        :param scale: The scale of this PaimonType.
        :type scale: int
        """
        self._scale = scale

    @property
    def length(self):
        r"""Gets the length of this PaimonType.

        CHAR(n)、VARCHAR(n)、BINARY(n)、VARBINARY(n)的长度（n）

        :return: The length of this PaimonType.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        r"""Sets the length of this PaimonType.

        CHAR(n)、VARCHAR(n)、BINARY(n)、VARBINARY(n)的长度（n）

        :param length: The length of this PaimonType.
        :type length: int
        """
        self._length = length

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
        if not isinstance(other, PaimonType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
