# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListPostpaidBillSumResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bill_cycle': 'str',
        'initial_amount_due': 'float',
        'consume_amount': 'float',
        'refunds': 'float',
        'adjustments': 'float',
        'tax_amount': 'float',
        'currency': 'str'
    }

    attribute_map = {
        'bill_cycle': 'bill_cycle',
        'initial_amount_due': 'initial_amount_due',
        'consume_amount': 'consume_amount',
        'refunds': 'refunds',
        'adjustments': 'adjustments',
        'tax_amount': 'tax_amount',
        'currency': 'currency'
    }

    def __init__(self, bill_cycle=None, initial_amount_due=None, consume_amount=None, refunds=None, adjustments=None, tax_amount=None, currency=None):
        """ListPostpaidBillSumResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._bill_cycle = None
        self._initial_amount_due = None
        self._consume_amount = None
        self._refunds = None
        self._adjustments = None
        self._tax_amount = None
        self._currency = None
        self.discriminator = None

        if bill_cycle is not None:
            self.bill_cycle = bill_cycle
        if initial_amount_due is not None:
            self.initial_amount_due = initial_amount_due
        if consume_amount is not None:
            self.consume_amount = consume_amount
        if refunds is not None:
            self.refunds = refunds
        if adjustments is not None:
            self.adjustments = adjustments
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if currency is not None:
            self.currency = currency

    @property
    def bill_cycle(self):
        """Gets the bill_cycle of this ListPostpaidBillSumResponse.

        |参数名称：结算周期，只有成功才返回这个参数。表示某年某月的账单汇总。格式：YYYY-MM| |参数约束及描述：结算周期，只有成功才返回这个参数。表示某年某月的账单汇总。格式：YYYY-MM|

        :return: The bill_cycle of this ListPostpaidBillSumResponse.
        :rtype: str
        """
        return self._bill_cycle

    @bill_cycle.setter
    def bill_cycle(self, bill_cycle):
        """Sets the bill_cycle of this ListPostpaidBillSumResponse.

        |参数名称：结算周期，只有成功才返回这个参数。表示某年某月的账单汇总。格式：YYYY-MM| |参数约束及描述：结算周期，只有成功才返回这个参数。表示某年某月的账单汇总。格式：YYYY-MM|

        :param bill_cycle: The bill_cycle of this ListPostpaidBillSumResponse.
        :type: str
        """
        self._bill_cycle = bill_cycle

    @property
    def initial_amount_due(self):
        """Gets the initial_amount_due of this ListPostpaidBillSumResponse.

        |参数名称：初始应还金额（含税）| |参数的约束及描述：初始应还金额（含税）|

        :return: The initial_amount_due of this ListPostpaidBillSumResponse.
        :rtype: float
        """
        return self._initial_amount_due

    @initial_amount_due.setter
    def initial_amount_due(self, initial_amount_due):
        """Sets the initial_amount_due of this ListPostpaidBillSumResponse.

        |参数名称：初始应还金额（含税）| |参数的约束及描述：初始应还金额（含税）|

        :param initial_amount_due: The initial_amount_due of this ListPostpaidBillSumResponse.
        :type: float
        """
        self._initial_amount_due = initial_amount_due

    @property
    def consume_amount(self):
        """Gets the consume_amount of this ListPostpaidBillSumResponse.

        |参数名称：消费金额| |参数的约束及描述：消费金额|

        :return: The consume_amount of this ListPostpaidBillSumResponse.
        :rtype: float
        """
        return self._consume_amount

    @consume_amount.setter
    def consume_amount(self, consume_amount):
        """Sets the consume_amount of this ListPostpaidBillSumResponse.

        |参数名称：消费金额| |参数的约束及描述：消费金额|

        :param consume_amount: The consume_amount of this ListPostpaidBillSumResponse.
        :type: float
        """
        self._consume_amount = consume_amount

    @property
    def refunds(self):
        """Gets the refunds of this ListPostpaidBillSumResponse.

        |参数名称：退款| |参数的约束及描述：退款|

        :return: The refunds of this ListPostpaidBillSumResponse.
        :rtype: float
        """
        return self._refunds

    @refunds.setter
    def refunds(self, refunds):
        """Sets the refunds of this ListPostpaidBillSumResponse.

        |参数名称：退款| |参数的约束及描述：退款|

        :param refunds: The refunds of this ListPostpaidBillSumResponse.
        :type: float
        """
        self._refunds = refunds

    @property
    def adjustments(self):
        """Gets the adjustments of this ListPostpaidBillSumResponse.

        |参数名称：调账| |参数的约束及描述：调账|

        :return: The adjustments of this ListPostpaidBillSumResponse.
        :rtype: float
        """
        return self._adjustments

    @adjustments.setter
    def adjustments(self, adjustments):
        """Sets the adjustments of this ListPostpaidBillSumResponse.

        |参数名称：调账| |参数的约束及描述：调账|

        :param adjustments: The adjustments of this ListPostpaidBillSumResponse.
        :type: float
        """
        self._adjustments = adjustments

    @property
    def tax_amount(self):
        """Gets the tax_amount of this ListPostpaidBillSumResponse.

        |参数名称：销项税金额| |参数的约束及描述：销项税金额|

        :return: The tax_amount of this ListPostpaidBillSumResponse.
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this ListPostpaidBillSumResponse.

        |参数名称：销项税金额| |参数的约束及描述：销项税金额|

        :param tax_amount: The tax_amount of this ListPostpaidBillSumResponse.
        :type: float
        """
        self._tax_amount = tax_amount

    @property
    def currency(self):
        """Gets the currency of this ListPostpaidBillSumResponse.

        |参数名称：只有成功才返回这个参数。人民币：CNY美金：USD| |参数约束及描述：只有成功才返回这个参数。人民币：CNY美金：USD|

        :return: The currency of this ListPostpaidBillSumResponse.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ListPostpaidBillSumResponse.

        |参数名称：只有成功才返回这个参数。人民币：CNY美金：USD| |参数约束及描述：只有成功才返回这个参数。人民币：CNY美金：USD|

        :param currency: The currency of this ListPostpaidBillSumResponse.
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
        if not isinstance(other, ListPostpaidBillSumResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
