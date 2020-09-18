# coding: utf-8

import pprint
import re

import six





class TransferAmountInfoV2:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'avail_transfer_amount': 'float',
        'measure_id': 'int',
        'currency': 'str',
        'amount': 'float',
        'credit_amount': 'float',
        'expire_time': 'str'
    }

    attribute_map = {
        'avail_transfer_amount': 'avail_transfer_amount',
        'measure_id': 'measure_id',
        'currency': 'currency',
        'amount': 'amount',
        'credit_amount': 'credit_amount',
        'expire_time': 'expire_time'
    }

    def __init__(self, avail_transfer_amount=None, measure_id=None, currency=None, amount=None, credit_amount=None, expire_time=None):
        """TransferAmountInfoV2 - a model defined in huaweicloud sdk"""
        
        

        self._avail_transfer_amount = None
        self._measure_id = None
        self._currency = None
        self._amount = None
        self._credit_amount = None
        self._expire_time = None
        self.discriminator = None

        if avail_transfer_amount is not None:
            self.avail_transfer_amount = avail_transfer_amount
        if measure_id is not None:
            self.measure_id = measure_id
        if currency is not None:
            self.currency = currency
        if amount is not None:
            self.amount = amount
        if credit_amount is not None:
            self.credit_amount = credit_amount
        if expire_time is not None:
            self.expire_time = expire_time

    @property
    def avail_transfer_amount(self):
        """Gets the avail_transfer_amount of this TransferAmountInfoV2.

        |参数名称：可拨款的金额。| |参数的约束及描述：可拨款的金额。|

        :return: The avail_transfer_amount of this TransferAmountInfoV2.
        :rtype: float
        """
        return self._avail_transfer_amount

    @avail_transfer_amount.setter
    def avail_transfer_amount(self, avail_transfer_amount):
        """Sets the avail_transfer_amount of this TransferAmountInfoV2.

        |参数名称：可拨款的金额。| |参数的约束及描述：可拨款的金额。|

        :param avail_transfer_amount: The avail_transfer_amount of this TransferAmountInfoV2.
        :type: float
        """
        self._avail_transfer_amount = avail_transfer_amount

    @property
    def measure_id(self):
        """Gets the measure_id of this TransferAmountInfoV2.

        |参数名称：金额单位。1：元| |参数的约束及描述：金额单位。1：元|

        :return: The measure_id of this TransferAmountInfoV2.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this TransferAmountInfoV2.

        |参数名称：金额单位。1：元| |参数的约束及描述：金额单位。1：元|

        :param measure_id: The measure_id of this TransferAmountInfoV2.
        :type: int
        """
        self._measure_id = measure_id

    @property
    def currency(self):
        """Gets the currency of this TransferAmountInfoV2.

        |参数名称：币种。CNY：人民币USD：美金| |参数约束及描述：币种。CNY：人民币USD：美金|

        :return: The currency of this TransferAmountInfoV2.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this TransferAmountInfoV2.

        |参数名称：币种。CNY：人民币USD：美金| |参数约束及描述：币种。CNY：人民币USD：美金|

        :param currency: The currency of this TransferAmountInfoV2.
        :type: str
        """
        self._currency = currency

    @property
    def amount(self):
        """Gets the amount of this TransferAmountInfoV2.

        |参数名称：账户余额（仅balance_type=信用账户时才有这个字段）。| |参数的约束及描述：账户余额（仅balance_type=信用账户时才有这个字段）。|

        :return: The amount of this TransferAmountInfoV2.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TransferAmountInfoV2.

        |参数名称：账户余额（仅balance_type=信用账户时才有这个字段）。| |参数的约束及描述：账户余额（仅balance_type=信用账户时才有这个字段）。|

        :param amount: The amount of this TransferAmountInfoV2.
        :type: float
        """
        self._amount = amount

    @property
    def credit_amount(self):
        """Gets the credit_amount of this TransferAmountInfoV2.

        |参数名称：信用额度（仅balance_type=信用账户时才有这个字段）。| |参数的约束及描述：信用额度（仅balance_type=信用账户时才有这个字段）。|

        :return: The credit_amount of this TransferAmountInfoV2.
        :rtype: float
        """
        return self._credit_amount

    @credit_amount.setter
    def credit_amount(self, credit_amount):
        """Sets the credit_amount of this TransferAmountInfoV2.

        |参数名称：信用额度（仅balance_type=信用账户时才有这个字段）。| |参数的约束及描述：信用额度（仅balance_type=信用账户时才有这个字段）。|

        :param credit_amount: The credit_amount of this TransferAmountInfoV2.
        :type: float
        """
        self._credit_amount = credit_amount

    @property
    def expire_time(self):
        """Gets the expire_time of this TransferAmountInfoV2.

        |参数名称：信用额度过期时间。UTC时间，格式为：2016-03-28T14:45:38Z。（仅balance_type=信用账户时才有这个字段）。如果查询信用账户可拨款余额的查询结果没有失效时间，表示永久有效。| |参数约束及描述：信用额度过期时间。UTC时间，格式为：2016-03-28T14:45:38Z。（仅balance_type=信用账户时才有这个字段）。如果查询信用账户可拨款余额的查询结果没有失效时间，表示永久有效。|

        :return: The expire_time of this TransferAmountInfoV2.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this TransferAmountInfoV2.

        |参数名称：信用额度过期时间。UTC时间，格式为：2016-03-28T14:45:38Z。（仅balance_type=信用账户时才有这个字段）。如果查询信用账户可拨款余额的查询结果没有失效时间，表示永久有效。| |参数约束及描述：信用额度过期时间。UTC时间，格式为：2016-03-28T14:45:38Z。（仅balance_type=信用账户时才有这个字段）。如果查询信用账户可拨款余额的查询结果没有失效时间，表示永久有效。|

        :param expire_time: The expire_time of this TransferAmountInfoV2.
        :type: str
        """
        self._expire_time = expire_time

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TransferAmountInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
