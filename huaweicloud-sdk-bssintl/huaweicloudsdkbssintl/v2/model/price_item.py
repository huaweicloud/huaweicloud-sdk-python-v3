# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PriceItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offering_id': 'str',
        'currency': 'str',
        'official_price': 'str',
        'charging_mode': 'str',
        'period_type': 'int',
        'period_nums': 'list[int]',
        'billing_usage_factor': 'str'
    }

    attribute_map = {
        'offering_id': 'offering_id',
        'currency': 'currency',
        'official_price': 'official_price',
        'charging_mode': 'charging_mode',
        'period_type': 'period_type',
        'period_nums': 'period_nums',
        'billing_usage_factor': 'billing_usage_factor'
    }

    def __init__(self, offering_id=None, currency=None, official_price=None, charging_mode=None, period_type=None, period_nums=None, billing_usage_factor=None):
        r"""PriceItem

        The model defined in huaweicloud sdk

        :param offering_id: 商品Id
        :type offering_id: str
        :param currency: 币种，USD
        :type currency: str
        :param official_price: 官网价
        :type official_price: str
        :param charging_mode: 计费模式，PERIOD：包年/包月、ON_DEMAND：按需、ONE_TIME：一次性、ON_DEMAND_PKG：按需套餐包
        :type charging_mode: str
        :param period_type: 销售周期类型，0：天 2：月 3：年 4：小时
        :type period_type: int
        :param period_nums: 销售周期数列表
        :type period_nums: list[int]
        :param billing_usage_factor: 计费因子编码
        :type billing_usage_factor: str
        """
        
        

        self._offering_id = None
        self._currency = None
        self._official_price = None
        self._charging_mode = None
        self._period_type = None
        self._period_nums = None
        self._billing_usage_factor = None
        self.discriminator = None

        if offering_id is not None:
            self.offering_id = offering_id
        if currency is not None:
            self.currency = currency
        if official_price is not None:
            self.official_price = official_price
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if period_type is not None:
            self.period_type = period_type
        if period_nums is not None:
            self.period_nums = period_nums
        if billing_usage_factor is not None:
            self.billing_usage_factor = billing_usage_factor

    @property
    def offering_id(self):
        r"""Gets the offering_id of this PriceItem.

        商品Id

        :return: The offering_id of this PriceItem.
        :rtype: str
        """
        return self._offering_id

    @offering_id.setter
    def offering_id(self, offering_id):
        r"""Sets the offering_id of this PriceItem.

        商品Id

        :param offering_id: The offering_id of this PriceItem.
        :type offering_id: str
        """
        self._offering_id = offering_id

    @property
    def currency(self):
        r"""Gets the currency of this PriceItem.

        币种，USD

        :return: The currency of this PriceItem.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        r"""Sets the currency of this PriceItem.

        币种，USD

        :param currency: The currency of this PriceItem.
        :type currency: str
        """
        self._currency = currency

    @property
    def official_price(self):
        r"""Gets the official_price of this PriceItem.

        官网价

        :return: The official_price of this PriceItem.
        :rtype: str
        """
        return self._official_price

    @official_price.setter
    def official_price(self, official_price):
        r"""Sets the official_price of this PriceItem.

        官网价

        :param official_price: The official_price of this PriceItem.
        :type official_price: str
        """
        self._official_price = official_price

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this PriceItem.

        计费模式，PERIOD：包年/包月、ON_DEMAND：按需、ONE_TIME：一次性、ON_DEMAND_PKG：按需套餐包

        :return: The charging_mode of this PriceItem.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this PriceItem.

        计费模式，PERIOD：包年/包月、ON_DEMAND：按需、ONE_TIME：一次性、ON_DEMAND_PKG：按需套餐包

        :param charging_mode: The charging_mode of this PriceItem.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def period_type(self):
        r"""Gets the period_type of this PriceItem.

        销售周期类型，0：天 2：月 3：年 4：小时

        :return: The period_type of this PriceItem.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this PriceItem.

        销售周期类型，0：天 2：月 3：年 4：小时

        :param period_type: The period_type of this PriceItem.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def period_nums(self):
        r"""Gets the period_nums of this PriceItem.

        销售周期数列表

        :return: The period_nums of this PriceItem.
        :rtype: list[int]
        """
        return self._period_nums

    @period_nums.setter
    def period_nums(self, period_nums):
        r"""Sets the period_nums of this PriceItem.

        销售周期数列表

        :param period_nums: The period_nums of this PriceItem.
        :type period_nums: list[int]
        """
        self._period_nums = period_nums

    @property
    def billing_usage_factor(self):
        r"""Gets the billing_usage_factor of this PriceItem.

        计费因子编码

        :return: The billing_usage_factor of this PriceItem.
        :rtype: str
        """
        return self._billing_usage_factor

    @billing_usage_factor.setter
    def billing_usage_factor(self, billing_usage_factor):
        r"""Sets the billing_usage_factor of this PriceItem.

        计费因子编码

        :param billing_usage_factor: The billing_usage_factor of this PriceItem.
        :type billing_usage_factor: str
        """
        self._billing_usage_factor = billing_usage_factor

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
        if not isinstance(other, PriceItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
