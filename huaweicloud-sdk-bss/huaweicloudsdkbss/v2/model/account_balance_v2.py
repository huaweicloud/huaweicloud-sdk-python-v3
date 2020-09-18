# coding: utf-8

import pprint
import re

import six





class AccountBalanceV2:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'account_id': 'str',
        'account_type': 'int',
        'amount': 'float',
        'currency': 'str',
        'designated_amount': 'float',
        'credit_amount': 'float',
        'measure_id': 'int',
        'memo': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'account_type': 'account_type',
        'amount': 'amount',
        'currency': 'currency',
        'designated_amount': 'designated_amount',
        'credit_amount': 'credit_amount',
        'measure_id': 'measure_id',
        'memo': 'memo'
    }

    def __init__(self, account_id=None, account_type=None, amount=None, currency='CNY', designated_amount=None, credit_amount=None, measure_id=None, memo=None):
        """AccountBalanceV2 - a model defined in huaweicloud sdk"""
        
        

        self._account_id = None
        self._account_type = None
        self._amount = None
        self._currency = None
        self._designated_amount = None
        self._credit_amount = None
        self._measure_id = None
        self._memo = None
        self.discriminator = None

        self.account_id = account_id
        self.account_type = account_type
        self.amount = amount
        self.currency = currency
        if designated_amount is not None:
            self.designated_amount = designated_amount
        if credit_amount is not None:
            self.credit_amount = credit_amount
        self.measure_id = measure_id
        if memo is not None:
            self.memo = memo

    @property
    def account_id(self):
        """Gets the account_id of this AccountBalanceV2.

        |参数名称：账户标识。| |参数约束及描述：账户标识。|

        :return: The account_id of this AccountBalanceV2.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AccountBalanceV2.

        |参数名称：账户标识。| |参数约束及描述：账户标识。|

        :param account_id: The account_id of this AccountBalanceV2.
        :type: str
        """
        self._account_id = account_id

    @property
    def account_type(self):
        """Gets the account_type of this AccountBalanceV2.

        |参数名称：账户类型：1：余额2：信用5：奖励7：保证金8：可拨款| |参数的约束及描述：账户类型：1：余额2：信用5：奖励7：保证金8：可拨款|

        :return: The account_type of this AccountBalanceV2.
        :rtype: int
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this AccountBalanceV2.

        |参数名称：账户类型：1：余额2：信用5：奖励7：保证金8：可拨款| |参数的约束及描述：账户类型：1：余额2：信用5：奖励7：保证金8：可拨款|

        :param account_type: The account_type of this AccountBalanceV2.
        :type: int
        """
        self._account_type = account_type

    @property
    def amount(self):
        """Gets the amount of this AccountBalanceV2.

        |参数名称：余额。| |参数的约束及描述：余额。|

        :return: The amount of this AccountBalanceV2.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this AccountBalanceV2.

        |参数名称：余额。| |参数的约束及描述：余额。|

        :param amount: The amount of this AccountBalanceV2.
        :type: float
        """
        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this AccountBalanceV2.

        |参数名称：币种。当前固定为CNY。| |参数约束及描述：币种。当前固定为CNY。|

        :return: The currency of this AccountBalanceV2.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this AccountBalanceV2.

        |参数名称：币种。当前固定为CNY。| |参数约束及描述：币种。当前固定为CNY。|

        :param currency: The currency of this AccountBalanceV2.
        :type: str
        """
        self._currency = currency

    @property
    def designated_amount(self):
        """Gets the designated_amount of this AccountBalanceV2.

        |参数名称：专款专用余额。| |参数的约束及描述：专款专用余额。|

        :return: The designated_amount of this AccountBalanceV2.
        :rtype: float
        """
        return self._designated_amount

    @designated_amount.setter
    def designated_amount(self, designated_amount):
        """Sets the designated_amount of this AccountBalanceV2.

        |参数名称：专款专用余额。| |参数的约束及描述：专款专用余额。|

        :param designated_amount: The designated_amount of this AccountBalanceV2.
        :type: float
        """
        self._designated_amount = designated_amount

    @property
    def credit_amount(self):
        """Gets the credit_amount of this AccountBalanceV2.

        |参数名称：总信用额度。只有账户类型是2:信用的时候才有该字段| |参数的约束及描述：总信用额度。只有账户类型是2:信用的时候才有该字段|

        :return: The credit_amount of this AccountBalanceV2.
        :rtype: float
        """
        return self._credit_amount

    @credit_amount.setter
    def credit_amount(self, credit_amount):
        """Sets the credit_amount of this AccountBalanceV2.

        |参数名称：总信用额度。只有账户类型是2:信用的时候才有该字段| |参数的约束及描述：总信用额度。只有账户类型是2:信用的时候才有该字段|

        :param credit_amount: The credit_amount of this AccountBalanceV2.
        :type: float
        """
        self._credit_amount = credit_amount

    @property
    def measure_id(self):
        """Gets the measure_id of this AccountBalanceV2.

        |参数名称：度量单位。1：元。| |参数的约束及描述：度量单位。1：元。|

        :return: The measure_id of this AccountBalanceV2.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this AccountBalanceV2.

        |参数名称：度量单位。1：元。| |参数的约束及描述：度量单位。1：元。|

        :param measure_id: The measure_id of this AccountBalanceV2.
        :type: int
        """
        self._measure_id = measure_id

    @property
    def memo(self):
        """Gets the memo of this AccountBalanceV2.

        |参数名称：备注。| |参数约束及描述：备注。|

        :return: The memo of this AccountBalanceV2.
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this AccountBalanceV2.

        |参数名称：备注。| |参数约束及描述：备注。|

        :param memo: The memo of this AccountBalanceV2.
        :type: str
        """
        self._memo = memo

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
        if not isinstance(other, AccountBalanceV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
