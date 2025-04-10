# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCustomerMonthlySumResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'bill_sums': 'list[BillSumRecordInfoV2]',
        'consume_amount': 'decimal.Decimal',
        'debt_amount': 'decimal.Decimal',
        'coupon_amount': 'decimal.Decimal',
        'flexipurchase_coupon_amount': 'decimal.Decimal',
        'stored_value_card_amount': 'decimal.Decimal',
        'cash_amount': 'decimal.Decimal',
        'credit_amount': 'decimal.Decimal',
        'writeoff_amount': 'decimal.Decimal',
        'measure_id': 'int',
        'currency': 'str'
    }

    attribute_map = {
        'total_count': 'total_count',
        'bill_sums': 'bill_sums',
        'consume_amount': 'consume_amount',
        'debt_amount': 'debt_amount',
        'coupon_amount': 'coupon_amount',
        'flexipurchase_coupon_amount': 'flexipurchase_coupon_amount',
        'stored_value_card_amount': 'stored_value_card_amount',
        'cash_amount': 'cash_amount',
        'credit_amount': 'credit_amount',
        'writeoff_amount': 'writeoff_amount',
        'measure_id': 'measure_id',
        'currency': 'currency'
    }

    def __init__(self, total_count=None, bill_sums=None, consume_amount=None, debt_amount=None, coupon_amount=None, flexipurchase_coupon_amount=None, stored_value_card_amount=None, cash_amount=None, credit_amount=None, writeoff_amount=None, measure_id=None, currency=None):
        r"""ShowCustomerMonthlySumResponse

        The model defined in huaweicloud sdk

        :param total_count: 总条数，必须大于等于0。
        :type total_count: int
        :param bill_sums: 账单记录，具体参考表2。
        :type bill_sums: list[:class:`huaweicloudsdkbss.v2.BillSumRecordInfoV2`]
        :param consume_amount: 总金额（包含退订）。
        :type consume_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param debt_amount: 总欠费金额。
        :type debt_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param coupon_amount: 代金券金额。
        :type coupon_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param flexipurchase_coupon_amount: 现金券金额，预留。
        :type flexipurchase_coupon_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param stored_value_card_amount: 储值卡金额，预留。
        :type stored_value_card_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param cash_amount: 现金账户金额。
        :type cash_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param credit_amount: 信用账户金额。
        :type credit_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param writeoff_amount: 欠费核销金额。
        :type writeoff_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param measure_id: 金额单位。 1：元
        :type measure_id: int
        :param currency: 币种。 CNY：人民币。
        :type currency: str
        """
        
        super(ShowCustomerMonthlySumResponse, self).__init__()

        self._total_count = None
        self._bill_sums = None
        self._consume_amount = None
        self._debt_amount = None
        self._coupon_amount = None
        self._flexipurchase_coupon_amount = None
        self._stored_value_card_amount = None
        self._cash_amount = None
        self._credit_amount = None
        self._writeoff_amount = None
        self._measure_id = None
        self._currency = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if bill_sums is not None:
            self.bill_sums = bill_sums
        if consume_amount is not None:
            self.consume_amount = consume_amount
        if debt_amount is not None:
            self.debt_amount = debt_amount
        if coupon_amount is not None:
            self.coupon_amount = coupon_amount
        if flexipurchase_coupon_amount is not None:
            self.flexipurchase_coupon_amount = flexipurchase_coupon_amount
        if stored_value_card_amount is not None:
            self.stored_value_card_amount = stored_value_card_amount
        if cash_amount is not None:
            self.cash_amount = cash_amount
        if credit_amount is not None:
            self.credit_amount = credit_amount
        if writeoff_amount is not None:
            self.writeoff_amount = writeoff_amount
        if measure_id is not None:
            self.measure_id = measure_id
        if currency is not None:
            self.currency = currency

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowCustomerMonthlySumResponse.

        总条数，必须大于等于0。

        :return: The total_count of this ShowCustomerMonthlySumResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowCustomerMonthlySumResponse.

        总条数，必须大于等于0。

        :param total_count: The total_count of this ShowCustomerMonthlySumResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def bill_sums(self):
        r"""Gets the bill_sums of this ShowCustomerMonthlySumResponse.

        账单记录，具体参考表2。

        :return: The bill_sums of this ShowCustomerMonthlySumResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.BillSumRecordInfoV2`]
        """
        return self._bill_sums

    @bill_sums.setter
    def bill_sums(self, bill_sums):
        r"""Sets the bill_sums of this ShowCustomerMonthlySumResponse.

        账单记录，具体参考表2。

        :param bill_sums: The bill_sums of this ShowCustomerMonthlySumResponse.
        :type bill_sums: list[:class:`huaweicloudsdkbss.v2.BillSumRecordInfoV2`]
        """
        self._bill_sums = bill_sums

    @property
    def consume_amount(self):
        r"""Gets the consume_amount of this ShowCustomerMonthlySumResponse.

        总金额（包含退订）。

        :return: The consume_amount of this ShowCustomerMonthlySumResponse.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._consume_amount

    @consume_amount.setter
    def consume_amount(self, consume_amount):
        r"""Sets the consume_amount of this ShowCustomerMonthlySumResponse.

        总金额（包含退订）。

        :param consume_amount: The consume_amount of this ShowCustomerMonthlySumResponse.
        :type consume_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._consume_amount = consume_amount

    @property
    def debt_amount(self):
        r"""Gets the debt_amount of this ShowCustomerMonthlySumResponse.

        总欠费金额。

        :return: The debt_amount of this ShowCustomerMonthlySumResponse.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._debt_amount

    @debt_amount.setter
    def debt_amount(self, debt_amount):
        r"""Sets the debt_amount of this ShowCustomerMonthlySumResponse.

        总欠费金额。

        :param debt_amount: The debt_amount of this ShowCustomerMonthlySumResponse.
        :type debt_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._debt_amount = debt_amount

    @property
    def coupon_amount(self):
        r"""Gets the coupon_amount of this ShowCustomerMonthlySumResponse.

        代金券金额。

        :return: The coupon_amount of this ShowCustomerMonthlySumResponse.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._coupon_amount

    @coupon_amount.setter
    def coupon_amount(self, coupon_amount):
        r"""Sets the coupon_amount of this ShowCustomerMonthlySumResponse.

        代金券金额。

        :param coupon_amount: The coupon_amount of this ShowCustomerMonthlySumResponse.
        :type coupon_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._coupon_amount = coupon_amount

    @property
    def flexipurchase_coupon_amount(self):
        r"""Gets the flexipurchase_coupon_amount of this ShowCustomerMonthlySumResponse.

        现金券金额，预留。

        :return: The flexipurchase_coupon_amount of this ShowCustomerMonthlySumResponse.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._flexipurchase_coupon_amount

    @flexipurchase_coupon_amount.setter
    def flexipurchase_coupon_amount(self, flexipurchase_coupon_amount):
        r"""Sets the flexipurchase_coupon_amount of this ShowCustomerMonthlySumResponse.

        现金券金额，预留。

        :param flexipurchase_coupon_amount: The flexipurchase_coupon_amount of this ShowCustomerMonthlySumResponse.
        :type flexipurchase_coupon_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._flexipurchase_coupon_amount = flexipurchase_coupon_amount

    @property
    def stored_value_card_amount(self):
        r"""Gets the stored_value_card_amount of this ShowCustomerMonthlySumResponse.

        储值卡金额，预留。

        :return: The stored_value_card_amount of this ShowCustomerMonthlySumResponse.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._stored_value_card_amount

    @stored_value_card_amount.setter
    def stored_value_card_amount(self, stored_value_card_amount):
        r"""Sets the stored_value_card_amount of this ShowCustomerMonthlySumResponse.

        储值卡金额，预留。

        :param stored_value_card_amount: The stored_value_card_amount of this ShowCustomerMonthlySumResponse.
        :type stored_value_card_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._stored_value_card_amount = stored_value_card_amount

    @property
    def cash_amount(self):
        r"""Gets the cash_amount of this ShowCustomerMonthlySumResponse.

        现金账户金额。

        :return: The cash_amount of this ShowCustomerMonthlySumResponse.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._cash_amount

    @cash_amount.setter
    def cash_amount(self, cash_amount):
        r"""Sets the cash_amount of this ShowCustomerMonthlySumResponse.

        现金账户金额。

        :param cash_amount: The cash_amount of this ShowCustomerMonthlySumResponse.
        :type cash_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._cash_amount = cash_amount

    @property
    def credit_amount(self):
        r"""Gets the credit_amount of this ShowCustomerMonthlySumResponse.

        信用账户金额。

        :return: The credit_amount of this ShowCustomerMonthlySumResponse.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._credit_amount

    @credit_amount.setter
    def credit_amount(self, credit_amount):
        r"""Sets the credit_amount of this ShowCustomerMonthlySumResponse.

        信用账户金额。

        :param credit_amount: The credit_amount of this ShowCustomerMonthlySumResponse.
        :type credit_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._credit_amount = credit_amount

    @property
    def writeoff_amount(self):
        r"""Gets the writeoff_amount of this ShowCustomerMonthlySumResponse.

        欠费核销金额。

        :return: The writeoff_amount of this ShowCustomerMonthlySumResponse.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._writeoff_amount

    @writeoff_amount.setter
    def writeoff_amount(self, writeoff_amount):
        r"""Sets the writeoff_amount of this ShowCustomerMonthlySumResponse.

        欠费核销金额。

        :param writeoff_amount: The writeoff_amount of this ShowCustomerMonthlySumResponse.
        :type writeoff_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._writeoff_amount = writeoff_amount

    @property
    def measure_id(self):
        r"""Gets the measure_id of this ShowCustomerMonthlySumResponse.

        金额单位。 1：元

        :return: The measure_id of this ShowCustomerMonthlySumResponse.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        r"""Sets the measure_id of this ShowCustomerMonthlySumResponse.

        金额单位。 1：元

        :param measure_id: The measure_id of this ShowCustomerMonthlySumResponse.
        :type measure_id: int
        """
        self._measure_id = measure_id

    @property
    def currency(self):
        r"""Gets the currency of this ShowCustomerMonthlySumResponse.

        币种。 CNY：人民币。

        :return: The currency of this ShowCustomerMonthlySumResponse.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        r"""Sets the currency of this ShowCustomerMonthlySumResponse.

        币种。 CNY：人民币。

        :param currency: The currency of this ShowCustomerMonthlySumResponse.
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
        if not isinstance(other, ShowCustomerMonthlySumResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
