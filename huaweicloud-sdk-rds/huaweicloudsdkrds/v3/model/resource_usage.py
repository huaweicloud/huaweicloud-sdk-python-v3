# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceUsage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'value': 'float',
        'total': 'float',
        'contrast': 'float',
        'unit': 'str'
    }

    attribute_map = {
        'value': 'value',
        'total': 'total',
        'contrast': 'contrast',
        'unit': 'unit'
    }

    def __init__(self, value=None, total=None, contrast=None, unit=None):
        r"""ResourceUsage

        The model defined in huaweicloud sdk

        :param value: 当前使用量。
        :type value: float
        :param total: 总量。
        :type total: float
        :param contrast: 对比值。
        :type contrast: float
        :param unit: 单位。
        :type unit: str
        """
        
        

        self._value = None
        self._total = None
        self._contrast = None
        self._unit = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if total is not None:
            self.total = total
        if contrast is not None:
            self.contrast = contrast
        if unit is not None:
            self.unit = unit

    @property
    def value(self):
        r"""Gets the value of this ResourceUsage.

        当前使用量。

        :return: The value of this ResourceUsage.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ResourceUsage.

        当前使用量。

        :param value: The value of this ResourceUsage.
        :type value: float
        """
        self._value = value

    @property
    def total(self):
        r"""Gets the total of this ResourceUsage.

        总量。

        :return: The total of this ResourceUsage.
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ResourceUsage.

        总量。

        :param total: The total of this ResourceUsage.
        :type total: float
        """
        self._total = total

    @property
    def contrast(self):
        r"""Gets the contrast of this ResourceUsage.

        对比值。

        :return: The contrast of this ResourceUsage.
        :rtype: float
        """
        return self._contrast

    @contrast.setter
    def contrast(self, contrast):
        r"""Sets the contrast of this ResourceUsage.

        对比值。

        :param contrast: The contrast of this ResourceUsage.
        :type contrast: float
        """
        self._contrast = contrast

    @property
    def unit(self):
        r"""Gets the unit of this ResourceUsage.

        单位。

        :return: The unit of this ResourceUsage.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this ResourceUsage.

        单位。

        :param unit: The unit of this ResourceUsage.
        :type unit: str
        """
        self._unit = unit

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
        if not isinstance(other, ResourceUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
