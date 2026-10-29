# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Division:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'begin_value': 'decimal.Decimal',
        'end_value': 'decimal.Decimal',
        'begin_unit': 'int',
        'end_unit': 'int',
        'official_price': 'str'
    }

    attribute_map = {
        'begin_value': 'begin_value',
        'end_value': 'end_value',
        'begin_unit': 'begin_unit',
        'end_unit': 'end_unit',
        'official_price': 'official_price'
    }

    def __init__(self, begin_value=None, end_value=None, begin_unit=None, end_unit=None, official_price=None):
        r"""Division

        The model defined in huaweicloud sdk

        :param begin_value: 阶梯起始值
        :type begin_value: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        :param end_value: 阶梯结束值
        :type end_value: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        :param begin_unit: 阶梯起始单位
        :type begin_unit: int
        :param end_unit: 阶梯结束单位
        :type end_unit: int
        :param official_price: 阶梯官网价
        :type official_price: str
        """
        
        

        self._begin_value = None
        self._end_value = None
        self._begin_unit = None
        self._end_unit = None
        self._official_price = None
        self.discriminator = None

        if begin_value is not None:
            self.begin_value = begin_value
        if end_value is not None:
            self.end_value = end_value
        if begin_unit is not None:
            self.begin_unit = begin_unit
        if end_unit is not None:
            self.end_unit = end_unit
        if official_price is not None:
            self.official_price = official_price

    @property
    def begin_value(self):
        r"""Gets the begin_value of this Division.

        阶梯起始值

        :return: The begin_value of this Division.
        :rtype: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        """
        return self._begin_value

    @begin_value.setter
    def begin_value(self, begin_value):
        r"""Sets the begin_value of this Division.

        阶梯起始值

        :param begin_value: The begin_value of this Division.
        :type begin_value: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        """
        self._begin_value = begin_value

    @property
    def end_value(self):
        r"""Gets the end_value of this Division.

        阶梯结束值

        :return: The end_value of this Division.
        :rtype: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        """
        return self._end_value

    @end_value.setter
    def end_value(self, end_value):
        r"""Sets the end_value of this Division.

        阶梯结束值

        :param end_value: The end_value of this Division.
        :type end_value: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        """
        self._end_value = end_value

    @property
    def begin_unit(self):
        r"""Gets the begin_unit of this Division.

        阶梯起始单位

        :return: The begin_unit of this Division.
        :rtype: int
        """
        return self._begin_unit

    @begin_unit.setter
    def begin_unit(self, begin_unit):
        r"""Sets the begin_unit of this Division.

        阶梯起始单位

        :param begin_unit: The begin_unit of this Division.
        :type begin_unit: int
        """
        self._begin_unit = begin_unit

    @property
    def end_unit(self):
        r"""Gets the end_unit of this Division.

        阶梯结束单位

        :return: The end_unit of this Division.
        :rtype: int
        """
        return self._end_unit

    @end_unit.setter
    def end_unit(self, end_unit):
        r"""Sets the end_unit of this Division.

        阶梯结束单位

        :param end_unit: The end_unit of this Division.
        :type end_unit: int
        """
        self._end_unit = end_unit

    @property
    def official_price(self):
        r"""Gets the official_price of this Division.

        阶梯官网价

        :return: The official_price of this Division.
        :rtype: str
        """
        return self._official_price

    @official_price.setter
    def official_price(self, official_price):
        r"""Sets the official_price of this Division.

        阶梯官网价

        :param official_price: The official_price of this Division.
        :type official_price: str
        """
        self._official_price = official_price

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
        if not isinstance(other, Division):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
