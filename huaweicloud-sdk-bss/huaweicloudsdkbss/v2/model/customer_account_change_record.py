# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomerAccountChangeRecord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_change_id': 'str',
        'trade_detail_type': 'str',
        'trade_time': 'str',
        'trade_id': 'str',
        'change_amount': 'str',
        'balance_after_change': 'str',
        'revenue_expense_type': 'str',
        'bill_cycle': 'str',
        'payment_channel_id': 'str',
        'payment_channel_no': 'str'
    }

    attribute_map = {
        'account_change_id': 'account_change_id',
        'trade_detail_type': 'trade_detail_type',
        'trade_time': 'trade_time',
        'trade_id': 'trade_id',
        'change_amount': 'change_amount',
        'balance_after_change': 'balance_after_change',
        'revenue_expense_type': 'revenue_expense_type',
        'bill_cycle': 'bill_cycle',
        'payment_channel_id': 'payment_channel_id',
        'payment_channel_no': 'payment_channel_no'
    }

    def __init__(self, account_change_id=None, trade_detail_type=None, trade_time=None, trade_id=None, change_amount=None, balance_after_change=None, revenue_expense_type=None, bill_cycle=None, payment_channel_id=None, payment_channel_no=None):
        """CustomerAccountChangeRecord

        The model defined in huaweicloud sdk

        :param account_change_id: |参数名称：收支明细流水号| |参数约束及描述：收支明细流水号|
        :type account_change_id: str
        :param trade_detail_type: |参数名称：交易详细类型| |参数约束及描述：交易详细类型|
        :type trade_detail_type: str
        :param trade_time: |参数名称：交易时间| |参数约束及描述：交易时间|
        :type trade_time: str
        :param trade_id: |参数名称：交易ID/订单ID| |参数约束及描述：交易ID/订单ID|
        :type trade_id: str
        :param change_amount: |参数名称：变更金额| |参数约束及描述：变更金额|
        :type change_amount: str
        :param balance_after_change: |参数名称：变更后余额| |参数约束及描述：变更后余额|
        :type balance_after_change: str
        :param revenue_expense_type: |参数名称：收支类型| |参数约束及描述：收支类型|
        :type revenue_expense_type: str
        :param bill_cycle: |参数名称：账期| |参数约束及描述：账期|
        :type bill_cycle: str
        :param payment_channel_id: |参数名称：交易渠道| |参数约束及描述：交易渠道|
        :type payment_channel_id: str
        :param payment_channel_no: |参数名称：交易渠道流水号| |参数约束及描述：交易渠道流水号|
        :type payment_channel_no: str
        """
        
        

        self._account_change_id = None
        self._trade_detail_type = None
        self._trade_time = None
        self._trade_id = None
        self._change_amount = None
        self._balance_after_change = None
        self._revenue_expense_type = None
        self._bill_cycle = None
        self._payment_channel_id = None
        self._payment_channel_no = None
        self.discriminator = None

        if account_change_id is not None:
            self.account_change_id = account_change_id
        if trade_detail_type is not None:
            self.trade_detail_type = trade_detail_type
        if trade_time is not None:
            self.trade_time = trade_time
        if trade_id is not None:
            self.trade_id = trade_id
        if change_amount is not None:
            self.change_amount = change_amount
        if balance_after_change is not None:
            self.balance_after_change = balance_after_change
        if revenue_expense_type is not None:
            self.revenue_expense_type = revenue_expense_type
        if bill_cycle is not None:
            self.bill_cycle = bill_cycle
        if payment_channel_id is not None:
            self.payment_channel_id = payment_channel_id
        if payment_channel_no is not None:
            self.payment_channel_no = payment_channel_no

    @property
    def account_change_id(self):
        """Gets the account_change_id of this CustomerAccountChangeRecord.

        |参数名称：收支明细流水号| |参数约束及描述：收支明细流水号|

        :return: The account_change_id of this CustomerAccountChangeRecord.
        :rtype: str
        """
        return self._account_change_id

    @account_change_id.setter
    def account_change_id(self, account_change_id):
        """Sets the account_change_id of this CustomerAccountChangeRecord.

        |参数名称：收支明细流水号| |参数约束及描述：收支明细流水号|

        :param account_change_id: The account_change_id of this CustomerAccountChangeRecord.
        :type account_change_id: str
        """
        self._account_change_id = account_change_id

    @property
    def trade_detail_type(self):
        """Gets the trade_detail_type of this CustomerAccountChangeRecord.

        |参数名称：交易详细类型| |参数约束及描述：交易详细类型|

        :return: The trade_detail_type of this CustomerAccountChangeRecord.
        :rtype: str
        """
        return self._trade_detail_type

    @trade_detail_type.setter
    def trade_detail_type(self, trade_detail_type):
        """Sets the trade_detail_type of this CustomerAccountChangeRecord.

        |参数名称：交易详细类型| |参数约束及描述：交易详细类型|

        :param trade_detail_type: The trade_detail_type of this CustomerAccountChangeRecord.
        :type trade_detail_type: str
        """
        self._trade_detail_type = trade_detail_type

    @property
    def trade_time(self):
        """Gets the trade_time of this CustomerAccountChangeRecord.

        |参数名称：交易时间| |参数约束及描述：交易时间|

        :return: The trade_time of this CustomerAccountChangeRecord.
        :rtype: str
        """
        return self._trade_time

    @trade_time.setter
    def trade_time(self, trade_time):
        """Sets the trade_time of this CustomerAccountChangeRecord.

        |参数名称：交易时间| |参数约束及描述：交易时间|

        :param trade_time: The trade_time of this CustomerAccountChangeRecord.
        :type trade_time: str
        """
        self._trade_time = trade_time

    @property
    def trade_id(self):
        """Gets the trade_id of this CustomerAccountChangeRecord.

        |参数名称：交易ID/订单ID| |参数约束及描述：交易ID/订单ID|

        :return: The trade_id of this CustomerAccountChangeRecord.
        :rtype: str
        """
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        """Sets the trade_id of this CustomerAccountChangeRecord.

        |参数名称：交易ID/订单ID| |参数约束及描述：交易ID/订单ID|

        :param trade_id: The trade_id of this CustomerAccountChangeRecord.
        :type trade_id: str
        """
        self._trade_id = trade_id

    @property
    def change_amount(self):
        """Gets the change_amount of this CustomerAccountChangeRecord.

        |参数名称：变更金额| |参数约束及描述：变更金额|

        :return: The change_amount of this CustomerAccountChangeRecord.
        :rtype: str
        """
        return self._change_amount

    @change_amount.setter
    def change_amount(self, change_amount):
        """Sets the change_amount of this CustomerAccountChangeRecord.

        |参数名称：变更金额| |参数约束及描述：变更金额|

        :param change_amount: The change_amount of this CustomerAccountChangeRecord.
        :type change_amount: str
        """
        self._change_amount = change_amount

    @property
    def balance_after_change(self):
        """Gets the balance_after_change of this CustomerAccountChangeRecord.

        |参数名称：变更后余额| |参数约束及描述：变更后余额|

        :return: The balance_after_change of this CustomerAccountChangeRecord.
        :rtype: str
        """
        return self._balance_after_change

    @balance_after_change.setter
    def balance_after_change(self, balance_after_change):
        """Sets the balance_after_change of this CustomerAccountChangeRecord.

        |参数名称：变更后余额| |参数约束及描述：变更后余额|

        :param balance_after_change: The balance_after_change of this CustomerAccountChangeRecord.
        :type balance_after_change: str
        """
        self._balance_after_change = balance_after_change

    @property
    def revenue_expense_type(self):
        """Gets the revenue_expense_type of this CustomerAccountChangeRecord.

        |参数名称：收支类型| |参数约束及描述：收支类型|

        :return: The revenue_expense_type of this CustomerAccountChangeRecord.
        :rtype: str
        """
        return self._revenue_expense_type

    @revenue_expense_type.setter
    def revenue_expense_type(self, revenue_expense_type):
        """Sets the revenue_expense_type of this CustomerAccountChangeRecord.

        |参数名称：收支类型| |参数约束及描述：收支类型|

        :param revenue_expense_type: The revenue_expense_type of this CustomerAccountChangeRecord.
        :type revenue_expense_type: str
        """
        self._revenue_expense_type = revenue_expense_type

    @property
    def bill_cycle(self):
        """Gets the bill_cycle of this CustomerAccountChangeRecord.

        |参数名称：账期| |参数约束及描述：账期|

        :return: The bill_cycle of this CustomerAccountChangeRecord.
        :rtype: str
        """
        return self._bill_cycle

    @bill_cycle.setter
    def bill_cycle(self, bill_cycle):
        """Sets the bill_cycle of this CustomerAccountChangeRecord.

        |参数名称：账期| |参数约束及描述：账期|

        :param bill_cycle: The bill_cycle of this CustomerAccountChangeRecord.
        :type bill_cycle: str
        """
        self._bill_cycle = bill_cycle

    @property
    def payment_channel_id(self):
        """Gets the payment_channel_id of this CustomerAccountChangeRecord.

        |参数名称：交易渠道| |参数约束及描述：交易渠道|

        :return: The payment_channel_id of this CustomerAccountChangeRecord.
        :rtype: str
        """
        return self._payment_channel_id

    @payment_channel_id.setter
    def payment_channel_id(self, payment_channel_id):
        """Sets the payment_channel_id of this CustomerAccountChangeRecord.

        |参数名称：交易渠道| |参数约束及描述：交易渠道|

        :param payment_channel_id: The payment_channel_id of this CustomerAccountChangeRecord.
        :type payment_channel_id: str
        """
        self._payment_channel_id = payment_channel_id

    @property
    def payment_channel_no(self):
        """Gets the payment_channel_no of this CustomerAccountChangeRecord.

        |参数名称：交易渠道流水号| |参数约束及描述：交易渠道流水号|

        :return: The payment_channel_no of this CustomerAccountChangeRecord.
        :rtype: str
        """
        return self._payment_channel_no

    @payment_channel_no.setter
    def payment_channel_no(self, payment_channel_no):
        """Sets the payment_channel_no of this CustomerAccountChangeRecord.

        |参数名称：交易渠道流水号| |参数约束及描述：交易渠道流水号|

        :param payment_channel_no: The payment_channel_no of this CustomerAccountChangeRecord.
        :type payment_channel_no: str
        """
        self._payment_channel_no = payment_channel_no

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
        if not isinstance(other, CustomerAccountChangeRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
