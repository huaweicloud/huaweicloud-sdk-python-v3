# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BalanceTypePay:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'balance_type_id': 'str',
        'deduct_amount': 'float'
    }

    attribute_map = {
        'balance_type_id': 'balance_type_id',
        'deduct_amount': 'deduct_amount'
    }

    def __init__(self, balance_type_id=None, deduct_amount=None):
        """BalanceTypePay

        The model defined in huaweicloud sdk

        :param balance_type_id: 账户类型。 BALANCE_TYPE_DEBIT：现金账户BALANCE_TYPE_CREDIT：信用账户BALANCE_TYPE_BONUS：奖励账户（该账户已下线）BALANCE_TYPE_COUPON：代金券账户BALANCE_TYPE_DEBIT_RATE：折扣账户
        :type balance_type_id: str
        :param deduct_amount: 支出金额。 单位：分
        :type deduct_amount: float
        """
        
        

        self._balance_type_id = None
        self._deduct_amount = None
        self.discriminator = None

        if balance_type_id is not None:
            self.balance_type_id = balance_type_id
        if deduct_amount is not None:
            self.deduct_amount = deduct_amount

    @property
    def balance_type_id(self):
        """Gets the balance_type_id of this BalanceTypePay.

        账户类型。 BALANCE_TYPE_DEBIT：现金账户BALANCE_TYPE_CREDIT：信用账户BALANCE_TYPE_BONUS：奖励账户（该账户已下线）BALANCE_TYPE_COUPON：代金券账户BALANCE_TYPE_DEBIT_RATE：折扣账户

        :return: The balance_type_id of this BalanceTypePay.
        :rtype: str
        """
        return self._balance_type_id

    @balance_type_id.setter
    def balance_type_id(self, balance_type_id):
        """Sets the balance_type_id of this BalanceTypePay.

        账户类型。 BALANCE_TYPE_DEBIT：现金账户BALANCE_TYPE_CREDIT：信用账户BALANCE_TYPE_BONUS：奖励账户（该账户已下线）BALANCE_TYPE_COUPON：代金券账户BALANCE_TYPE_DEBIT_RATE：折扣账户

        :param balance_type_id: The balance_type_id of this BalanceTypePay.
        :type balance_type_id: str
        """
        self._balance_type_id = balance_type_id

    @property
    def deduct_amount(self):
        """Gets the deduct_amount of this BalanceTypePay.

        支出金额。 单位：分

        :return: The deduct_amount of this BalanceTypePay.
        :rtype: float
        """
        return self._deduct_amount

    @deduct_amount.setter
    def deduct_amount(self, deduct_amount):
        """Sets the deduct_amount of this BalanceTypePay.

        支出金额。 单位：分

        :param deduct_amount: The deduct_amount of this BalanceTypePay.
        :type deduct_amount: float
        """
        self._deduct_amount = deduct_amount

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
        if not isinstance(other, BalanceTypePay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
