# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMonthlyExpendituresResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_code': 'str',
        'error_msg': 'str',
        'currency': 'str',
        'total_count': 'int',
        'total_amount': 'float',
        'debt_amount': 'float',
        'coupon_amount': 'float',
        'cashcoupon_amount': 'float',
        'storedcard_amount': 'float',
        'debit_amount': 'float',
        'credit_amount': 'float',
        'measure_id': 'int',
        'bill_sums': 'list[BillSumRecordInfo]'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'currency': 'currency',
        'total_count': 'total_count',
        'total_amount': 'total_amount',
        'debt_amount': 'debt_amount',
        'coupon_amount': 'coupon_amount',
        'cashcoupon_amount': 'cashcoupon_amount',
        'storedcard_amount': 'storedcard_amount',
        'debit_amount': 'debit_amount',
        'credit_amount': 'credit_amount',
        'measure_id': 'measure_id',
        'bill_sums': 'bill_sums'
    }

    def __init__(self, error_code=None, error_msg=None, currency=None, total_count=None, total_amount=None, debt_amount=None, coupon_amount=None, cashcoupon_amount=None, storedcard_amount=None, debit_amount=None, credit_amount=None, measure_id=None, bill_sums=None):
        """ListMonthlyExpendituresResponse

        The model defined in huaweicloud sdk

        :param error_code: 返回码
        :type error_code: str
        :param error_msg: 返回码描述
        :type error_msg: str
        :param currency: 货币单位代码 USD：美元
        :type currency: str
        :param total_count: 总条数
        :type total_count: int
        :param total_amount: 总金额（包含退订）。
        :type total_amount: float
        :param debt_amount: 总欠费金额。
        :type debt_amount: float
        :param coupon_amount: 代金券金额。
        :type coupon_amount: float
        :param cashcoupon_amount: 现金券金额，预留。
        :type cashcoupon_amount: float
        :param storedcard_amount: 储值卡金额，预留。
        :type storedcard_amount: float
        :param debit_amount: 现金账户金额。
        :type debit_amount: float
        :param credit_amount: 信用账户金额。
        :type credit_amount: float
        :param measure_id: 金额单位。 1：元3：分 默认值为3。
        :type measure_id: int
        :param bill_sums: 账单记录，具体参考表3。
        :type bill_sums: list[:class:`huaweicloudsdkbssintl.v2.BillSumRecordInfo`]
        """
        
        super(ListMonthlyExpendituresResponse, self).__init__()

        self._error_code = None
        self._error_msg = None
        self._currency = None
        self._total_count = None
        self._total_amount = None
        self._debt_amount = None
        self._coupon_amount = None
        self._cashcoupon_amount = None
        self._storedcard_amount = None
        self._debit_amount = None
        self._credit_amount = None
        self._measure_id = None
        self._bill_sums = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if currency is not None:
            self.currency = currency
        if total_count is not None:
            self.total_count = total_count
        if total_amount is not None:
            self.total_amount = total_amount
        if debt_amount is not None:
            self.debt_amount = debt_amount
        if coupon_amount is not None:
            self.coupon_amount = coupon_amount
        if cashcoupon_amount is not None:
            self.cashcoupon_amount = cashcoupon_amount
        if storedcard_amount is not None:
            self.storedcard_amount = storedcard_amount
        if debit_amount is not None:
            self.debit_amount = debit_amount
        if credit_amount is not None:
            self.credit_amount = credit_amount
        if measure_id is not None:
            self.measure_id = measure_id
        if bill_sums is not None:
            self.bill_sums = bill_sums

    @property
    def error_code(self):
        """Gets the error_code of this ListMonthlyExpendituresResponse.

        返回码

        :return: The error_code of this ListMonthlyExpendituresResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ListMonthlyExpendituresResponse.

        返回码

        :param error_code: The error_code of this ListMonthlyExpendituresResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this ListMonthlyExpendituresResponse.

        返回码描述

        :return: The error_msg of this ListMonthlyExpendituresResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this ListMonthlyExpendituresResponse.

        返回码描述

        :param error_msg: The error_msg of this ListMonthlyExpendituresResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def currency(self):
        """Gets the currency of this ListMonthlyExpendituresResponse.

        货币单位代码 USD：美元

        :return: The currency of this ListMonthlyExpendituresResponse.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ListMonthlyExpendituresResponse.

        货币单位代码 USD：美元

        :param currency: The currency of this ListMonthlyExpendituresResponse.
        :type currency: str
        """
        self._currency = currency

    @property
    def total_count(self):
        """Gets the total_count of this ListMonthlyExpendituresResponse.

        总条数

        :return: The total_count of this ListMonthlyExpendituresResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListMonthlyExpendituresResponse.

        总条数

        :param total_count: The total_count of this ListMonthlyExpendituresResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def total_amount(self):
        """Gets the total_amount of this ListMonthlyExpendituresResponse.

        总金额（包含退订）。

        :return: The total_amount of this ListMonthlyExpendituresResponse.
        :rtype: float
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this ListMonthlyExpendituresResponse.

        总金额（包含退订）。

        :param total_amount: The total_amount of this ListMonthlyExpendituresResponse.
        :type total_amount: float
        """
        self._total_amount = total_amount

    @property
    def debt_amount(self):
        """Gets the debt_amount of this ListMonthlyExpendituresResponse.

        总欠费金额。

        :return: The debt_amount of this ListMonthlyExpendituresResponse.
        :rtype: float
        """
        return self._debt_amount

    @debt_amount.setter
    def debt_amount(self, debt_amount):
        """Sets the debt_amount of this ListMonthlyExpendituresResponse.

        总欠费金额。

        :param debt_amount: The debt_amount of this ListMonthlyExpendituresResponse.
        :type debt_amount: float
        """
        self._debt_amount = debt_amount

    @property
    def coupon_amount(self):
        """Gets the coupon_amount of this ListMonthlyExpendituresResponse.

        代金券金额。

        :return: The coupon_amount of this ListMonthlyExpendituresResponse.
        :rtype: float
        """
        return self._coupon_amount

    @coupon_amount.setter
    def coupon_amount(self, coupon_amount):
        """Sets the coupon_amount of this ListMonthlyExpendituresResponse.

        代金券金额。

        :param coupon_amount: The coupon_amount of this ListMonthlyExpendituresResponse.
        :type coupon_amount: float
        """
        self._coupon_amount = coupon_amount

    @property
    def cashcoupon_amount(self):
        """Gets the cashcoupon_amount of this ListMonthlyExpendituresResponse.

        现金券金额，预留。

        :return: The cashcoupon_amount of this ListMonthlyExpendituresResponse.
        :rtype: float
        """
        return self._cashcoupon_amount

    @cashcoupon_amount.setter
    def cashcoupon_amount(self, cashcoupon_amount):
        """Sets the cashcoupon_amount of this ListMonthlyExpendituresResponse.

        现金券金额，预留。

        :param cashcoupon_amount: The cashcoupon_amount of this ListMonthlyExpendituresResponse.
        :type cashcoupon_amount: float
        """
        self._cashcoupon_amount = cashcoupon_amount

    @property
    def storedcard_amount(self):
        """Gets the storedcard_amount of this ListMonthlyExpendituresResponse.

        储值卡金额，预留。

        :return: The storedcard_amount of this ListMonthlyExpendituresResponse.
        :rtype: float
        """
        return self._storedcard_amount

    @storedcard_amount.setter
    def storedcard_amount(self, storedcard_amount):
        """Sets the storedcard_amount of this ListMonthlyExpendituresResponse.

        储值卡金额，预留。

        :param storedcard_amount: The storedcard_amount of this ListMonthlyExpendituresResponse.
        :type storedcard_amount: float
        """
        self._storedcard_amount = storedcard_amount

    @property
    def debit_amount(self):
        """Gets the debit_amount of this ListMonthlyExpendituresResponse.

        现金账户金额。

        :return: The debit_amount of this ListMonthlyExpendituresResponse.
        :rtype: float
        """
        return self._debit_amount

    @debit_amount.setter
    def debit_amount(self, debit_amount):
        """Sets the debit_amount of this ListMonthlyExpendituresResponse.

        现金账户金额。

        :param debit_amount: The debit_amount of this ListMonthlyExpendituresResponse.
        :type debit_amount: float
        """
        self._debit_amount = debit_amount

    @property
    def credit_amount(self):
        """Gets the credit_amount of this ListMonthlyExpendituresResponse.

        信用账户金额。

        :return: The credit_amount of this ListMonthlyExpendituresResponse.
        :rtype: float
        """
        return self._credit_amount

    @credit_amount.setter
    def credit_amount(self, credit_amount):
        """Sets the credit_amount of this ListMonthlyExpendituresResponse.

        信用账户金额。

        :param credit_amount: The credit_amount of this ListMonthlyExpendituresResponse.
        :type credit_amount: float
        """
        self._credit_amount = credit_amount

    @property
    def measure_id(self):
        """Gets the measure_id of this ListMonthlyExpendituresResponse.

        金额单位。 1：元3：分 默认值为3。

        :return: The measure_id of this ListMonthlyExpendituresResponse.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this ListMonthlyExpendituresResponse.

        金额单位。 1：元3：分 默认值为3。

        :param measure_id: The measure_id of this ListMonthlyExpendituresResponse.
        :type measure_id: int
        """
        self._measure_id = measure_id

    @property
    def bill_sums(self):
        """Gets the bill_sums of this ListMonthlyExpendituresResponse.

        账单记录，具体参考表3。

        :return: The bill_sums of this ListMonthlyExpendituresResponse.
        :rtype: list[:class:`huaweicloudsdkbssintl.v2.BillSumRecordInfo`]
        """
        return self._bill_sums

    @bill_sums.setter
    def bill_sums(self, bill_sums):
        """Sets the bill_sums of this ListMonthlyExpendituresResponse.

        账单记录，具体参考表3。

        :param bill_sums: The bill_sums of this ListMonthlyExpendituresResponse.
        :type bill_sums: list[:class:`huaweicloudsdkbssintl.v2.BillSumRecordInfo`]
        """
        self._bill_sums = bill_sums

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
        if not isinstance(other, ListMonthlyExpendituresResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
