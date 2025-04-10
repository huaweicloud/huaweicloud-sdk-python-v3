# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCustomerAccountChangeRecordsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'balance_type': 'str',
        'revenue_expense_type': 'str',
        'trade_type': 'str',
        'trade_time_begin': 'str',
        'trade_time_end': 'str',
        'trade_id': 'str',
        'payment_channel_id': 'str',
        'payment_channel_no': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'balance_type': 'balance_type',
        'revenue_expense_type': 'revenue_expense_type',
        'trade_type': 'trade_type',
        'trade_time_begin': 'trade_time_begin',
        'trade_time_end': 'trade_time_end',
        'trade_id': 'trade_id',
        'payment_channel_id': 'payment_channel_id',
        'payment_channel_no': 'payment_channel_no',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, balance_type=None, revenue_expense_type=None, trade_type=None, trade_time_begin=None, trade_time_end=None, trade_id=None, payment_channel_id=None, payment_channel_no=None, offset=None, limit=None):
        r"""ListCustomerAccountChangeRecordsRequest

        The model defined in huaweicloud sdk

        :param balance_type: |参数名称：账户类型。BALANCE_TYPE_DEBIT：现金账户BALANCE_TYPE_CREDIT：信用账户| |参数的约束及描述：必填|
        :type balance_type: str
        :param revenue_expense_type: |参数名称：收支类型。REVENUE：收入EXPENSE：支出| |参数的约束及描述：非必填|
        :type revenue_expense_type: str
        :param trade_type: |参数名称：交易类型。RECHARGE：充值DEDEUCT：消费REFUND：退款RFROZEN：冻结TRANS：转账，余额和保证金互换（老商务模式，当前已无保证金账户）ADJUST：调账（华为核销等）BEADJUST：经销商拨款BERETRIEVE：经销商回收BEUNBIND：解绑/关联模式切换导致的回收EXPIRED：过期清零BONUSCONVERT：奖励金转换（老商务模式，当前已无奖励金账户）TRADE_MODE_TRANSFER：交易模式变更DEPOSIT：保证金| |参数的约束及描述：非必填|
        :type trade_type: str
        :param trade_time_begin: |参数名称：查询收支明细的开始日期| |参数的约束及描述：非必填|
        :type trade_time_begin: str
        :param trade_time_end: |参数名称：查询收支明细的结束日期| |参数的约束及描述：非必填|
        :type trade_time_end: str
        :param trade_id: |参数名称：交易ID/订单ID| |参数的约束及描述：非必填|
        :type trade_id: str
        :param payment_channel_id: |参数名称：交易渠道。可以一次查询多个，用逗号分隔。1：支付宝2：银行转账4：支付宝/网银5：微信支付6：提现7：激励返点10：交易模式变更11：调账317：银联（统一支付平台）319：Huawei Pay320：华为支付| |参数的约束及描述：非必填|
        :type payment_channel_id: str
        :param payment_channel_no: |参数名称：交易渠道流水号| |参数的约束及描述：非必填|
        :type payment_channel_no: str
        :param offset: |参数名称：偏移量| |参数的约束及描述：非必填|
        :type offset: int
        :param limit: |参数名称：每页的显示条数| |参数的约束及描述：非必填|
        :type limit: int
        """
        
        

        self._balance_type = None
        self._revenue_expense_type = None
        self._trade_type = None
        self._trade_time_begin = None
        self._trade_time_end = None
        self._trade_id = None
        self._payment_channel_id = None
        self._payment_channel_no = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.balance_type = balance_type
        if revenue_expense_type is not None:
            self.revenue_expense_type = revenue_expense_type
        if trade_type is not None:
            self.trade_type = trade_type
        if trade_time_begin is not None:
            self.trade_time_begin = trade_time_begin
        if trade_time_end is not None:
            self.trade_time_end = trade_time_end
        if trade_id is not None:
            self.trade_id = trade_id
        if payment_channel_id is not None:
            self.payment_channel_id = payment_channel_id
        if payment_channel_no is not None:
            self.payment_channel_no = payment_channel_no
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def balance_type(self):
        r"""Gets the balance_type of this ListCustomerAccountChangeRecordsRequest.

        |参数名称：账户类型。BALANCE_TYPE_DEBIT：现金账户BALANCE_TYPE_CREDIT：信用账户| |参数的约束及描述：必填|

        :return: The balance_type of this ListCustomerAccountChangeRecordsRequest.
        :rtype: str
        """
        return self._balance_type

    @balance_type.setter
    def balance_type(self, balance_type):
        r"""Sets the balance_type of this ListCustomerAccountChangeRecordsRequest.

        |参数名称：账户类型。BALANCE_TYPE_DEBIT：现金账户BALANCE_TYPE_CREDIT：信用账户| |参数的约束及描述：必填|

        :param balance_type: The balance_type of this ListCustomerAccountChangeRecordsRequest.
        :type balance_type: str
        """
        self._balance_type = balance_type

    @property
    def revenue_expense_type(self):
        r"""Gets the revenue_expense_type of this ListCustomerAccountChangeRecordsRequest.

        |参数名称：收支类型。REVENUE：收入EXPENSE：支出| |参数的约束及描述：非必填|

        :return: The revenue_expense_type of this ListCustomerAccountChangeRecordsRequest.
        :rtype: str
        """
        return self._revenue_expense_type

    @revenue_expense_type.setter
    def revenue_expense_type(self, revenue_expense_type):
        r"""Sets the revenue_expense_type of this ListCustomerAccountChangeRecordsRequest.

        |参数名称：收支类型。REVENUE：收入EXPENSE：支出| |参数的约束及描述：非必填|

        :param revenue_expense_type: The revenue_expense_type of this ListCustomerAccountChangeRecordsRequest.
        :type revenue_expense_type: str
        """
        self._revenue_expense_type = revenue_expense_type

    @property
    def trade_type(self):
        r"""Gets the trade_type of this ListCustomerAccountChangeRecordsRequest.

        |参数名称：交易类型。RECHARGE：充值DEDEUCT：消费REFUND：退款RFROZEN：冻结TRANS：转账，余额和保证金互换（老商务模式，当前已无保证金账户）ADJUST：调账（华为核销等）BEADJUST：经销商拨款BERETRIEVE：经销商回收BEUNBIND：解绑/关联模式切换导致的回收EXPIRED：过期清零BONUSCONVERT：奖励金转换（老商务模式，当前已无奖励金账户）TRADE_MODE_TRANSFER：交易模式变更DEPOSIT：保证金| |参数的约束及描述：非必填|

        :return: The trade_type of this ListCustomerAccountChangeRecordsRequest.
        :rtype: str
        """
        return self._trade_type

    @trade_type.setter
    def trade_type(self, trade_type):
        r"""Sets the trade_type of this ListCustomerAccountChangeRecordsRequest.

        |参数名称：交易类型。RECHARGE：充值DEDEUCT：消费REFUND：退款RFROZEN：冻结TRANS：转账，余额和保证金互换（老商务模式，当前已无保证金账户）ADJUST：调账（华为核销等）BEADJUST：经销商拨款BERETRIEVE：经销商回收BEUNBIND：解绑/关联模式切换导致的回收EXPIRED：过期清零BONUSCONVERT：奖励金转换（老商务模式，当前已无奖励金账户）TRADE_MODE_TRANSFER：交易模式变更DEPOSIT：保证金| |参数的约束及描述：非必填|

        :param trade_type: The trade_type of this ListCustomerAccountChangeRecordsRequest.
        :type trade_type: str
        """
        self._trade_type = trade_type

    @property
    def trade_time_begin(self):
        r"""Gets the trade_time_begin of this ListCustomerAccountChangeRecordsRequest.

        |参数名称：查询收支明细的开始日期| |参数的约束及描述：非必填|

        :return: The trade_time_begin of this ListCustomerAccountChangeRecordsRequest.
        :rtype: str
        """
        return self._trade_time_begin

    @trade_time_begin.setter
    def trade_time_begin(self, trade_time_begin):
        r"""Sets the trade_time_begin of this ListCustomerAccountChangeRecordsRequest.

        |参数名称：查询收支明细的开始日期| |参数的约束及描述：非必填|

        :param trade_time_begin: The trade_time_begin of this ListCustomerAccountChangeRecordsRequest.
        :type trade_time_begin: str
        """
        self._trade_time_begin = trade_time_begin

    @property
    def trade_time_end(self):
        r"""Gets the trade_time_end of this ListCustomerAccountChangeRecordsRequest.

        |参数名称：查询收支明细的结束日期| |参数的约束及描述：非必填|

        :return: The trade_time_end of this ListCustomerAccountChangeRecordsRequest.
        :rtype: str
        """
        return self._trade_time_end

    @trade_time_end.setter
    def trade_time_end(self, trade_time_end):
        r"""Sets the trade_time_end of this ListCustomerAccountChangeRecordsRequest.

        |参数名称：查询收支明细的结束日期| |参数的约束及描述：非必填|

        :param trade_time_end: The trade_time_end of this ListCustomerAccountChangeRecordsRequest.
        :type trade_time_end: str
        """
        self._trade_time_end = trade_time_end

    @property
    def trade_id(self):
        r"""Gets the trade_id of this ListCustomerAccountChangeRecordsRequest.

        |参数名称：交易ID/订单ID| |参数的约束及描述：非必填|

        :return: The trade_id of this ListCustomerAccountChangeRecordsRequest.
        :rtype: str
        """
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        r"""Sets the trade_id of this ListCustomerAccountChangeRecordsRequest.

        |参数名称：交易ID/订单ID| |参数的约束及描述：非必填|

        :param trade_id: The trade_id of this ListCustomerAccountChangeRecordsRequest.
        :type trade_id: str
        """
        self._trade_id = trade_id

    @property
    def payment_channel_id(self):
        r"""Gets the payment_channel_id of this ListCustomerAccountChangeRecordsRequest.

        |参数名称：交易渠道。可以一次查询多个，用逗号分隔。1：支付宝2：银行转账4：支付宝/网银5：微信支付6：提现7：激励返点10：交易模式变更11：调账317：银联（统一支付平台）319：Huawei Pay320：华为支付| |参数的约束及描述：非必填|

        :return: The payment_channel_id of this ListCustomerAccountChangeRecordsRequest.
        :rtype: str
        """
        return self._payment_channel_id

    @payment_channel_id.setter
    def payment_channel_id(self, payment_channel_id):
        r"""Sets the payment_channel_id of this ListCustomerAccountChangeRecordsRequest.

        |参数名称：交易渠道。可以一次查询多个，用逗号分隔。1：支付宝2：银行转账4：支付宝/网银5：微信支付6：提现7：激励返点10：交易模式变更11：调账317：银联（统一支付平台）319：Huawei Pay320：华为支付| |参数的约束及描述：非必填|

        :param payment_channel_id: The payment_channel_id of this ListCustomerAccountChangeRecordsRequest.
        :type payment_channel_id: str
        """
        self._payment_channel_id = payment_channel_id

    @property
    def payment_channel_no(self):
        r"""Gets the payment_channel_no of this ListCustomerAccountChangeRecordsRequest.

        |参数名称：交易渠道流水号| |参数的约束及描述：非必填|

        :return: The payment_channel_no of this ListCustomerAccountChangeRecordsRequest.
        :rtype: str
        """
        return self._payment_channel_no

    @payment_channel_no.setter
    def payment_channel_no(self, payment_channel_no):
        r"""Sets the payment_channel_no of this ListCustomerAccountChangeRecordsRequest.

        |参数名称：交易渠道流水号| |参数的约束及描述：非必填|

        :param payment_channel_no: The payment_channel_no of this ListCustomerAccountChangeRecordsRequest.
        :type payment_channel_no: str
        """
        self._payment_channel_no = payment_channel_no

    @property
    def offset(self):
        r"""Gets the offset of this ListCustomerAccountChangeRecordsRequest.

        |参数名称：偏移量| |参数的约束及描述：非必填|

        :return: The offset of this ListCustomerAccountChangeRecordsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCustomerAccountChangeRecordsRequest.

        |参数名称：偏移量| |参数的约束及描述：非必填|

        :param offset: The offset of this ListCustomerAccountChangeRecordsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListCustomerAccountChangeRecordsRequest.

        |参数名称：每页的显示条数| |参数的约束及描述：非必填|

        :return: The limit of this ListCustomerAccountChangeRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCustomerAccountChangeRecordsRequest.

        |参数名称：每页的显示条数| |参数的约束及描述：非必填|

        :param limit: The limit of this ListCustomerAccountChangeRecordsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListCustomerAccountChangeRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
