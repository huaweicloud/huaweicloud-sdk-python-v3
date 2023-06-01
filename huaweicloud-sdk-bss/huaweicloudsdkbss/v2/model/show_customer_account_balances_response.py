# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'debt_amount': 'decimal.Decimal',
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
        """ShowCustomerAccountBalancesResponse

        The model defined in huaweicloud sdk

        :param account_balances: 账户余额列表。 具体请参见表1。
        :type account_balances: list[:class:`huaweicloudsdkbss.v2.AccountBalanceV3`]
        :param debt_amount: 欠款总金额。
        :type debt_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param measure_id: 度量单位。 1：元
        :type measure_id: int
        :param currency: 币种。 CNY：人民币。
        :type currency: str
        """
        
        super(ShowCustomerAccountBalancesResponse, self).__init__()

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

        账户余额列表。 具体请参见表1。

        :return: The account_balances of this ShowCustomerAccountBalancesResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.AccountBalanceV3`]
        """
        return self._account_balances

    @account_balances.setter
    def account_balances(self, account_balances):
        """Sets the account_balances of this ShowCustomerAccountBalancesResponse.

        账户余额列表。 具体请参见表1。

        :param account_balances: The account_balances of this ShowCustomerAccountBalancesResponse.
        :type account_balances: list[:class:`huaweicloudsdkbss.v2.AccountBalanceV3`]
        """
        self._account_balances = account_balances

    @property
    def debt_amount(self):
        """Gets the debt_amount of this ShowCustomerAccountBalancesResponse.

        欠款总金额。

        :return: The debt_amount of this ShowCustomerAccountBalancesResponse.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._debt_amount

    @debt_amount.setter
    def debt_amount(self, debt_amount):
        """Sets the debt_amount of this ShowCustomerAccountBalancesResponse.

        欠款总金额。

        :param debt_amount: The debt_amount of this ShowCustomerAccountBalancesResponse.
        :type debt_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._debt_amount = debt_amount

    @property
    def measure_id(self):
        """Gets the measure_id of this ShowCustomerAccountBalancesResponse.

        度量单位。 1：元

        :return: The measure_id of this ShowCustomerAccountBalancesResponse.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this ShowCustomerAccountBalancesResponse.

        度量单位。 1：元

        :param measure_id: The measure_id of this ShowCustomerAccountBalancesResponse.
        :type measure_id: int
        """
        self._measure_id = measure_id

    @property
    def currency(self):
        """Gets the currency of this ShowCustomerAccountBalancesResponse.

        币种。 CNY：人民币。

        :return: The currency of this ShowCustomerAccountBalancesResponse.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ShowCustomerAccountBalancesResponse.

        币种。 CNY：人民币。

        :param currency: The currency of this ShowCustomerAccountBalancesResponse.
        :type currency: str
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
        if not isinstance(other, ShowCustomerAccountBalancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
