# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourcePriceResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'charge_mode': 'str',
        'sale_price': 'object',
        'discount': 'object',
        'original_price': 'object',
        'period_type': 'str',
        'period_count': 'int'
    }

    attribute_map = {
        'charge_mode': 'charge_mode',
        'sale_price': 'sale_price',
        'discount': 'discount',
        'original_price': 'original_price',
        'period_type': 'period_type',
        'period_count': 'period_count'
    }

    def __init__(self, charge_mode=None, sale_price=None, discount=None, original_price=None, period_type=None, period_count=None):
        """ResourcePriceResponse

        The model defined in huaweicloud sdk

        :param charge_mode: 计费模式，包周期计费、按需计费、免费的返回，不支持的资源不返回 PRE_PAID 包周期计费 POST_PAID 按需计费 FREE 免费
        :type charge_mode: str
        :param sale_price: 执行计划中的每个资源部署后最终优惠后的金额（只考虑商务折扣以及伙伴折扣，不包含促销折扣及优惠券），保留小数点后2位，向上取整，默认单位是元
        :type sale_price: object
        :param discount: 执行计划中的每个资源部署后的优惠额，保留小数点后2位，向上取整，默认单位是元
        :type discount: object
        :param original_price: 执行计划中的每个资源部署后的原价，保留小数点后2位，向上取整，默认单位是元
        :type original_price: object
        :param period_type: 包周期和按需的计费单位，包周期计费和按需计费返回，免费不会返回 HOUR：小时，包周期计费和按需计费返回，免费不会返回 DAY：天，包周期计费返回，按需计费和免费不会返回 WEEK：周，包周期计费返回，按需计费和免费不会返回 MONTH：月，包周期计费返回，按需计费和免费不会返回 YEAR：年，包周期计费返回，按需计费和免费不会返回 BYTE：字节，按需计费返回，包周期计费和免费不会返回 MB：百万字节，按需计费返回，包周期计费和免费不会返回 GB：千兆字节，按需计费返回，包周期计费和免费不会返回
        :type period_type: str
        :param period_count: 订购数量。包周期计费和按需计费返回，免费不会返回。
        :type period_count: int
        """
        
        

        self._charge_mode = None
        self._sale_price = None
        self._discount = None
        self._original_price = None
        self._period_type = None
        self._period_count = None
        self.discriminator = None

        if charge_mode is not None:
            self.charge_mode = charge_mode
        if sale_price is not None:
            self.sale_price = sale_price
        if discount is not None:
            self.discount = discount
        if original_price is not None:
            self.original_price = original_price
        if period_type is not None:
            self.period_type = period_type
        if period_count is not None:
            self.period_count = period_count

    @property
    def charge_mode(self):
        """Gets the charge_mode of this ResourcePriceResponse.

        计费模式，包周期计费、按需计费、免费的返回，不支持的资源不返回 PRE_PAID 包周期计费 POST_PAID 按需计费 FREE 免费

        :return: The charge_mode of this ResourcePriceResponse.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this ResourcePriceResponse.

        计费模式，包周期计费、按需计费、免费的返回，不支持的资源不返回 PRE_PAID 包周期计费 POST_PAID 按需计费 FREE 免费

        :param charge_mode: The charge_mode of this ResourcePriceResponse.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def sale_price(self):
        """Gets the sale_price of this ResourcePriceResponse.

        执行计划中的每个资源部署后最终优惠后的金额（只考虑商务折扣以及伙伴折扣，不包含促销折扣及优惠券），保留小数点后2位，向上取整，默认单位是元

        :return: The sale_price of this ResourcePriceResponse.
        :rtype: object
        """
        return self._sale_price

    @sale_price.setter
    def sale_price(self, sale_price):
        """Sets the sale_price of this ResourcePriceResponse.

        执行计划中的每个资源部署后最终优惠后的金额（只考虑商务折扣以及伙伴折扣，不包含促销折扣及优惠券），保留小数点后2位，向上取整，默认单位是元

        :param sale_price: The sale_price of this ResourcePriceResponse.
        :type sale_price: object
        """
        self._sale_price = sale_price

    @property
    def discount(self):
        """Gets the discount of this ResourcePriceResponse.

        执行计划中的每个资源部署后的优惠额，保留小数点后2位，向上取整，默认单位是元

        :return: The discount of this ResourcePriceResponse.
        :rtype: object
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this ResourcePriceResponse.

        执行计划中的每个资源部署后的优惠额，保留小数点后2位，向上取整，默认单位是元

        :param discount: The discount of this ResourcePriceResponse.
        :type discount: object
        """
        self._discount = discount

    @property
    def original_price(self):
        """Gets the original_price of this ResourcePriceResponse.

        执行计划中的每个资源部署后的原价，保留小数点后2位，向上取整，默认单位是元

        :return: The original_price of this ResourcePriceResponse.
        :rtype: object
        """
        return self._original_price

    @original_price.setter
    def original_price(self, original_price):
        """Sets the original_price of this ResourcePriceResponse.

        执行计划中的每个资源部署后的原价，保留小数点后2位，向上取整，默认单位是元

        :param original_price: The original_price of this ResourcePriceResponse.
        :type original_price: object
        """
        self._original_price = original_price

    @property
    def period_type(self):
        """Gets the period_type of this ResourcePriceResponse.

        包周期和按需的计费单位，包周期计费和按需计费返回，免费不会返回 HOUR：小时，包周期计费和按需计费返回，免费不会返回 DAY：天，包周期计费返回，按需计费和免费不会返回 WEEK：周，包周期计费返回，按需计费和免费不会返回 MONTH：月，包周期计费返回，按需计费和免费不会返回 YEAR：年，包周期计费返回，按需计费和免费不会返回 BYTE：字节，按需计费返回，包周期计费和免费不会返回 MB：百万字节，按需计费返回，包周期计费和免费不会返回 GB：千兆字节，按需计费返回，包周期计费和免费不会返回

        :return: The period_type of this ResourcePriceResponse.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this ResourcePriceResponse.

        包周期和按需的计费单位，包周期计费和按需计费返回，免费不会返回 HOUR：小时，包周期计费和按需计费返回，免费不会返回 DAY：天，包周期计费返回，按需计费和免费不会返回 WEEK：周，包周期计费返回，按需计费和免费不会返回 MONTH：月，包周期计费返回，按需计费和免费不会返回 YEAR：年，包周期计费返回，按需计费和免费不会返回 BYTE：字节，按需计费返回，包周期计费和免费不会返回 MB：百万字节，按需计费返回，包周期计费和免费不会返回 GB：千兆字节，按需计费返回，包周期计费和免费不会返回

        :param period_type: The period_type of this ResourcePriceResponse.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_count(self):
        """Gets the period_count of this ResourcePriceResponse.

        订购数量。包周期计费和按需计费返回，免费不会返回。

        :return: The period_count of this ResourcePriceResponse.
        :rtype: int
        """
        return self._period_count

    @period_count.setter
    def period_count(self, period_count):
        """Sets the period_count of this ResourcePriceResponse.

        订购数量。包周期计费和按需计费返回，免费不会返回。

        :param period_count: The period_count of this ResourcePriceResponse.
        :type period_count: int
        """
        self._period_count = period_count

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
        if not isinstance(other, ResourcePriceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
