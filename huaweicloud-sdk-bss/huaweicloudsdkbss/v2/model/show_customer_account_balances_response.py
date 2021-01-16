# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowCustomerAccountBalancesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'account_balances': 'list[AccountBalanceV3]',
        'debt_amount': 'float',
        'measure_id': 'int',
        'currency': 'str'
    }

    attribute_map = {
        'account_balances': 'account_balances',
        'debt_amount': 'debt_amount',
        'measure_id': 'measure_id',
        'currency': 'currency'
    }

    def __init__(self, account_balances=None, debt_amount=None, measure_id=None, currency=None):
        """ShowCustomerAccountBalancesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._account_balances = None
        self._debt_amount = None
        self._measure_id = None
        self._currency = None
        self.discriminator = None

        if account_balances is not None:
            self.account_balances = account_balances
        if debt_amount is not None:
            self.debt_amount = debt_amount
        if measure_id is not None:
            self.measure_id = measure_id
        if currency is not None:
            self.currency = currency

    @property
    def account_balances(self):
        """Gets the account_balances of this ShowCustomerAccountBalancesResponse.

        |参数名称：账户余额列表。具体请参见表 AccountBalanceV3| |参数约束以及描述：账户余额列表。具体请参见表 AccountBalanceV3|

        :return: The account_balances of this ShowCustomerAccountBalancesResponse.
        :rtype: list[AccountBalanceV3]
        """
        return self._account_balances

    @account_balances.setter
    def account_balances(self, account_balances):
        """Sets the account_balances of this ShowCustomerAccountBalancesResponse.

        |参数名称：账户余额列表。具体请参见表 AccountBalanceV3| |参数约束以及描述：账户余额列表。具体请参见表 AccountBalanceV3|

        :param account_balances: The account_balances of this ShowCustomerAccountBalancesResponse.
        :type: list[AccountBalanceV3]
        """
        self._account_balances = account_balances

    @property
    def debt_amount(self):
        """Gets the debt_amount of this ShowCustomerAccountBalancesResponse.

        |参数名称：欠款总金额。| |参数的约束及描述：欠款总金额。|

        :return: The debt_amount of this ShowCustomerAccountBalancesResponse.
        :rtype: float
        """
        return self._debt_amount

    @debt_amount.setter
    def debt_amount(self, debt_amount):
        """Sets the debt_amount of this ShowCustomerAccountBalancesResponse.

        |参数名称：欠款总金额。| |参数的约束及描述：欠款总金额。|

        :param debt_amount: The debt_amount of this ShowCustomerAccountBalancesResponse.
        :type: float
        """
        self._debt_amount = debt_amount

    @property
    def measure_id(self):
        """Gets the measure_id of this ShowCustomerAccountBalancesResponse.

        |参数名称：度量单位：1：元2：角3：分| |参数的约束及描述：度量单位：1：元2：角3：分|

        :return: The measure_id of this ShowCustomerAccountBalancesResponse.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this ShowCustomerAccountBalancesResponse.

        |参数名称：度量单位：1：元2：角3：分| |参数的约束及描述：度量单位：1：元2：角3：分|

        :param measure_id: The measure_id of this ShowCustomerAccountBalancesResponse.
        :type: int
        """
        self._measure_id = measure_id

    @property
    def currency(self):
        """Gets the currency of this ShowCustomerAccountBalancesResponse.

        |参数名称：币种。CNY：人民币。USD：美元。| |参数约束及描述：币种。CNY：人民币。USD：美元。|

        :return: The currency of this ShowCustomerAccountBalancesResponse.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ShowCustomerAccountBalancesResponse.

        |参数名称：币种。CNY：人民币。USD：美元。| |参数约束及描述：币种。CNY：人民币。USD：美元。|

        :param currency: The currency of this ShowCustomerAccountBalancesResponse.
        :type: str
        """
        self._currency = currency

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
        if not isinstance(other, ShowCustomerAccountBalancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
