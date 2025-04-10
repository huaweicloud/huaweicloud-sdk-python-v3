# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomerBalancesV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'customer_id': 'str',
        'debt_amount': 'decimal.Decimal',
        'amount': 'decimal.Decimal',
        'currency': 'str',
        'measure_id': 'int'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'debt_amount': 'debt_amount',
        'amount': 'amount',
        'currency': 'currency',
        'measure_id': 'measure_id'
    }

    def __init__(self, customer_id=None, debt_amount=None, amount=None, currency=None, measure_id=None):
        r"""CustomerBalancesV2

        The model defined in huaweicloud sdk

        :param customer_id: 客户账号ID。
        :type customer_id: str
        :param debt_amount: 客户欠款总额度。
        :type debt_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param amount: 客户可用总额度。
        :type amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param currency: 币种。 CNY：人民币。
        :type currency: str
        :param measure_id: 度量单位： 1：元
        :type measure_id: int
        """
        
        

        self._customer_id = None
        self._debt_amount = None
        self._amount = None
        self._currency = None
        self._measure_id = None
        self.discriminator = None

        self.customer_id = customer_id
        if debt_amount is not None:
            self.debt_amount = debt_amount
        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        if measure_id is not None:
            self.measure_id = measure_id

    @property
    def customer_id(self):
        r"""Gets the customer_id of this CustomerBalancesV2.

        客户账号ID。

        :return: The customer_id of this CustomerBalancesV2.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        r"""Sets the customer_id of this CustomerBalancesV2.

        客户账号ID。

        :param customer_id: The customer_id of this CustomerBalancesV2.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def debt_amount(self):
        r"""Gets the debt_amount of this CustomerBalancesV2.

        客户欠款总额度。

        :return: The debt_amount of this CustomerBalancesV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._debt_amount

    @debt_amount.setter
    def debt_amount(self, debt_amount):
        r"""Sets the debt_amount of this CustomerBalancesV2.

        客户欠款总额度。

        :param debt_amount: The debt_amount of this CustomerBalancesV2.
        :type debt_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._debt_amount = debt_amount

    @property
    def amount(self):
        r"""Gets the amount of this CustomerBalancesV2.

        客户可用总额度。

        :return: The amount of this CustomerBalancesV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        r"""Sets the amount of this CustomerBalancesV2.

        客户可用总额度。

        :param amount: The amount of this CustomerBalancesV2.
        :type amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._amount = amount

    @property
    def currency(self):
        r"""Gets the currency of this CustomerBalancesV2.

        币种。 CNY：人民币。

        :return: The currency of this CustomerBalancesV2.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        r"""Sets the currency of this CustomerBalancesV2.

        币种。 CNY：人民币。

        :param currency: The currency of this CustomerBalancesV2.
        :type currency: str
        """
        self._currency = currency

    @property
    def measure_id(self):
        r"""Gets the measure_id of this CustomerBalancesV2.

        度量单位： 1：元

        :return: The measure_id of this CustomerBalancesV2.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        r"""Sets the measure_id of this CustomerBalancesV2.

        度量单位： 1：元

        :param measure_id: The measure_id of this CustomerBalancesV2.
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
        if not isinstance(other, CustomerBalancesV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
