# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccountBalanceV3:

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
        'measure_id': 'int'
    }

    attribute_map = {
        'account_id': 'account_id',
        'account_type': 'account_type',
        'amount': 'amount',
        'currency': 'currency',
        'designated_amount': 'designated_amount',
        'credit_amount': 'credit_amount',
        'measure_id': 'measure_id'
    }

    def __init__(self, account_id=None, account_type=None, amount=None, currency=None, designated_amount=None, credit_amount=None, measure_id=None):
        """AccountBalanceV3

        The model defined in huaweicloud sdk

        :param account_id: 账户标识。
        :type account_id: str
        :param account_type: 账户类型。 1：余额2：信用5：奖励金7：保证金
        :type account_type: int
        :param amount: 账户余额。
        :type amount: float
        :param currency: 币种。 USD：美元。
        :type currency: str
        :param designated_amount: 专款专用余额。
        :type designated_amount: float
        :param credit_amount: 总信用额度，仅信用账户存在该字段。
        :type credit_amount: float
        :param measure_id: 度量单位。 1：元
        :type measure_id: int
        """
        
        

        self._account_id = None
        self._account_type = None
        self._amount = None
        self._currency = None
        self._designated_amount = None
        self._credit_amount = None
        self._measure_id = None
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

    @property
    def account_id(self):
        """Gets the account_id of this AccountBalanceV3.

        账户标识。

        :return: The account_id of this AccountBalanceV3.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AccountBalanceV3.

        账户标识。

        :param account_id: The account_id of this AccountBalanceV3.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def account_type(self):
        """Gets the account_type of this AccountBalanceV3.

        账户类型。 1：余额2：信用5：奖励金7：保证金

        :return: The account_type of this AccountBalanceV3.
        :rtype: int
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this AccountBalanceV3.

        账户类型。 1：余额2：信用5：奖励金7：保证金

        :param account_type: The account_type of this AccountBalanceV3.
        :type account_type: int
        """
        self._account_type = account_type

    @property
    def amount(self):
        """Gets the amount of this AccountBalanceV3.

        账户余额。

        :return: The amount of this AccountBalanceV3.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this AccountBalanceV3.

        账户余额。

        :param amount: The amount of this AccountBalanceV3.
        :type amount: float
        """
        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this AccountBalanceV3.

        币种。 USD：美元。

        :return: The currency of this AccountBalanceV3.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this AccountBalanceV3.

        币种。 USD：美元。

        :param currency: The currency of this AccountBalanceV3.
        :type currency: str
        """
        self._currency = currency

    @property
    def designated_amount(self):
        """Gets the designated_amount of this AccountBalanceV3.

        专款专用余额。

        :return: The designated_amount of this AccountBalanceV3.
        :rtype: float
        """
        return self._designated_amount

    @designated_amount.setter
    def designated_amount(self, designated_amount):
        """Sets the designated_amount of this AccountBalanceV3.

        专款专用余额。

        :param designated_amount: The designated_amount of this AccountBalanceV3.
        :type designated_amount: float
        """
        self._designated_amount = designated_amount

    @property
    def credit_amount(self):
        """Gets the credit_amount of this AccountBalanceV3.

        总信用额度，仅信用账户存在该字段。

        :return: The credit_amount of this AccountBalanceV3.
        :rtype: float
        """
        return self._credit_amount

    @credit_amount.setter
    def credit_amount(self, credit_amount):
        """Sets the credit_amount of this AccountBalanceV3.

        总信用额度，仅信用账户存在该字段。

        :param credit_amount: The credit_amount of this AccountBalanceV3.
        :type credit_amount: float
        """
        self._credit_amount = credit_amount

    @property
    def measure_id(self):
        """Gets the measure_id of this AccountBalanceV3.

        度量单位。 1：元

        :return: The measure_id of this AccountBalanceV3.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this AccountBalanceV3.

        度量单位。 1：元

        :param measure_id: The measure_id of this AccountBalanceV3.
        :type measure_id: int
        """
        self._measure_id = measure_id

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
        if not isinstance(other, AccountBalanceV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
