# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SkuInfo:

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
        'period': 'str',
        'queries_limit': 'int',
        'price': 'float'
    }

    attribute_map = {
        'code': 'code',
        'period': 'period',
        'queries_limit': 'queries_limit',
        'price': 'price'
    }

    def __init__(self, code=None, period=None, queries_limit=None, price=None):
        r"""SkuInfo

        The model defined in huaweicloud sdk

        :param code: 计费码。
        :type code: str
        :param period: 计费时期。
        :type period: str
        :param queries_limit: 查询次数。
        :type queries_limit: int
        :param price: 价格。
        :type price: float
        """
        
        

        self._code = None
        self._period = None
        self._queries_limit = None
        self._price = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if period is not None:
            self.period = period
        if queries_limit is not None:
            self.queries_limit = queries_limit
        if price is not None:
            self.price = price

    @property
    def code(self):
        r"""Gets the code of this SkuInfo.

        计费码。

        :return: The code of this SkuInfo.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this SkuInfo.

        计费码。

        :param code: The code of this SkuInfo.
        :type code: str
        """
        self._code = code

    @property
    def period(self):
        r"""Gets the period of this SkuInfo.

        计费时期。

        :return: The period of this SkuInfo.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this SkuInfo.

        计费时期。

        :param period: The period of this SkuInfo.
        :type period: str
        """
        self._period = period

    @property
    def queries_limit(self):
        r"""Gets the queries_limit of this SkuInfo.

        查询次数。

        :return: The queries_limit of this SkuInfo.
        :rtype: int
        """
        return self._queries_limit

    @queries_limit.setter
    def queries_limit(self, queries_limit):
        r"""Sets the queries_limit of this SkuInfo.

        查询次数。

        :param queries_limit: The queries_limit of this SkuInfo.
        :type queries_limit: int
        """
        self._queries_limit = queries_limit

    @property
    def price(self):
        r"""Gets the price of this SkuInfo.

        价格。

        :return: The price of this SkuInfo.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        r"""Sets the price of this SkuInfo.

        价格。

        :param price: The price of this SkuInfo.
        :type price: float
        """
        self._price = price

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
        if not isinstance(other, SkuInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
