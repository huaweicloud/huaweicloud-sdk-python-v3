# coding: utf-8

import pprint
import re

import six





class BalanceTypeDeductSumV2:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'balance_type': 'str',
        'amount': 'float',
        'bill_type': 'str'
    }

    attribute_map = {
        'balance_type': 'balance_type',
        'amount': 'amount',
        'bill_type': 'bill_type'
    }

    def __init__(self, balance_type=None, amount=None, bill_type=None):
        """BalanceTypeDeductSumV2 - a model defined in huaweicloud sdk"""
        
        

        self._balance_type = None
        self._amount = None
        self._bill_type = None
        self.discriminator = None

        if balance_type is not None:
            self.balance_type = balance_type
        if amount is not None:
            self.amount = amount
        if bill_type is not None:
            self.bill_type = bill_type

    @property
    def balance_type(self):
        """Gets the balance_type of this BalanceTypeDeductSumV2.

        |参数名称：账户类型。BALANCE_TYPE_DEBIT：余额BALANCE_TYPE_CREDIT：信用BALANCE_TYPE_BONUS：奖励BALANCE_TYPE_COUPON：代金券BALANCE_TYPE_RCASH_COUPON 现金券。BALANCE_TYPE_STORED_VALUE_CARD：储值卡消费| |参数约束及描述：账户类型。BALANCE_TYPE_DEBIT：余额BALANCE_TYPE_CREDIT：信用BALANCE_TYPE_BONUS：奖励BALANCE_TYPE_COUPON：代金券BALANCE_TYPE_RCASH_COUPON 现金券。BALANCE_TYPE_STORED_VALUE_CARD：储值卡消费|

        :return: The balance_type of this BalanceTypeDeductSumV2.
        :rtype: str
        """
        return self._balance_type

    @balance_type.setter
    def balance_type(self, balance_type):
        """Sets the balance_type of this BalanceTypeDeductSumV2.

        |参数名称：账户类型。BALANCE_TYPE_DEBIT：余额BALANCE_TYPE_CREDIT：信用BALANCE_TYPE_BONUS：奖励BALANCE_TYPE_COUPON：代金券BALANCE_TYPE_RCASH_COUPON 现金券。BALANCE_TYPE_STORED_VALUE_CARD：储值卡消费| |参数约束及描述：账户类型。BALANCE_TYPE_DEBIT：余额BALANCE_TYPE_CREDIT：信用BALANCE_TYPE_BONUS：奖励BALANCE_TYPE_COUPON：代金券BALANCE_TYPE_RCASH_COUPON 现金券。BALANCE_TYPE_STORED_VALUE_CARD：储值卡消费|

        :param balance_type: The balance_type of this BalanceTypeDeductSumV2.
        :type: str
        """
        self._balance_type = balance_type

    @property
    def amount(self):
        """Gets the amount of this BalanceTypeDeductSumV2.

        |参数名称：金额。对于billType=1或者2的账单，该金额为负值。| |参数的约束及描述：金额。对于billType=1或者2的账单，该金额为负值。|

        :return: The amount of this BalanceTypeDeductSumV2.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this BalanceTypeDeductSumV2.

        |参数名称：金额。对于billType=1或者2的账单，该金额为负值。| |参数的约束及描述：金额。对于billType=1或者2的账单，该金额为负值。|

        :param amount: The amount of this BalanceTypeDeductSumV2.
        :type: float
        """
        self._amount = amount

    @property
    def bill_type(self):
        """Gets the bill_type of this BalanceTypeDeductSumV2.

        |参数名称：费用类型。0：正常；1：退订；2：华为核销。| |参数约束及描述：费用类型。0：正常；1：退订；2：华为核销。|

        :return: The bill_type of this BalanceTypeDeductSumV2.
        :rtype: str
        """
        return self._bill_type

    @bill_type.setter
    def bill_type(self, bill_type):
        """Sets the bill_type of this BalanceTypeDeductSumV2.

        |参数名称：费用类型。0：正常；1：退订；2：华为核销。| |参数约束及描述：费用类型。0：正常；1：退订；2：华为核销。|

        :param bill_type: The bill_type of this BalanceTypeDeductSumV2.
        :type: str
        """
        self._bill_type = bill_type

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
        if not isinstance(other, BalanceTypeDeductSumV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
