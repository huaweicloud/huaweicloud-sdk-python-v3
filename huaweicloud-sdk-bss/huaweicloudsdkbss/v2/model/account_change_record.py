# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccountChangeRecord:

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
        'type': 'str'
    }

    attribute_map = {
        'account_change_id': 'account_change_id',
        'trade_detail_type': 'trade_detail_type',
        'trade_time': 'trade_time',
        'trade_id': 'trade_id',
        'change_amount': 'change_amount',
        'balance_after_change': 'balance_after_change',
        'type': 'type'
    }

    def __init__(self, account_change_id=None, trade_detail_type=None, trade_time=None, trade_id=None, change_amount=None, balance_after_change=None, type=None):
        r"""AccountChangeRecord

        The model defined in huaweicloud sdk

        :param account_change_id: 收支明细流水号。
        :type account_change_id: str
        :param trade_detail_type: 交易详细类型。 SOURCE_OPERAIION_ADJUST_CREDIT：调账(信用额度调整)SOURCE_OPERAIION_RECHARGE：充值SOURCE_OPERAIION_DEDEUCT：消费(包年/包月)SOURCE_OPERAIION_MANUALFROZE：冻结(人工冻结)SOURCE_OPERAIION_MANUALUNFROZE：冻结(人工解冻)SOURCE_OPERAIION_MANUALCLEARFROZEN：冻结(人工清零)SOURCE_OPERAIION_TRANS_TO_BALANCE：转账(保证金转余额)SOURCE_OPERATION_BEADJUST：伙伴拨款SOURCE_OPERATION_BEUNBIND：交易模式变更(切换/解除关联回收)SOURCE_OPERAIION_EXPIRECLEAR：过期清零SOURCE_OPERAIION_ONETIME：消费(一次性扣费)SOURCE_OPERAIION_REFUND：退款SOURCE_OPERAIION_UNFROZEN：退款(退款解冻)SOURCE_OPERAIION_CLEARFROZEN：退款(退款清零)SOURCE_OPERAIION_ADJUST：调账(余额调整)SOURCE_OPERAIION_USAGE：消费(按需)SOURCE_OPERAIION_WRITEOFF：消费(欠费还款)SOURCE_OPERAIION_UNSUBSCRIBE：退款SOURCE_OPERAIION_RFROZEN：退款(退款冻结)SOURCE_OPERAIION_TRANS_TO_FOREGIFT：转账(余额转保证金)SOURCE_OPERAIION_PRIZE：调账(赠送)SOURCE_OPERATION_BERETRIEVE：伙伴回收SOURCE_OPERAIION_PRECISIONCOMP：消费(精度补扣)SOURCE_OPERAIION_FREERESDEDUCT：消费(免费资源扣减)SOURCE_OPERAIION_MERGE：奖励金转换(合并)SOURCE_OPERAIION_CONVERT_BONUS：奖励金转换SOURCE_OPERAIION_RECHARGE_REBATE：充值(激励返点)SOURCE_OPERATION_COUPONCANCEL：优惠券回收SOURCE_OPERAIION_BILLREFUND：调账(华为核销)SOURCE_OPERATION_TRADEMODE_TRANSFER：交易模式变更(和伙伴关联)SOURCE_OPERATION_SYSTEM_FROZEN：系统冻结（购买标销合同的伙伴涉及该模式）SOURCE_OPERATION_SYSTEM_UNFROZEN：系统解冻（购买标销合同的伙伴涉及该模式）SOURCE_OPERATION_COUPON_QUOTA_TRANSFER：调账(兑换现金券额度)SOURCE_OPERATIION_RIDEDUCT：消费(预留实例)SOURCE_OPERATION_COUPON_QUOTA_RECLAIM：代金券回收
        :type trade_detail_type: str
        :param trade_time: 交易时间。 UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2016-03-28T14:45:38Z”。
        :type trade_time: str
        :param trade_id: 交易ID/订单ID。
        :type trade_id: str
        :param change_amount: 变更金额，单位为元。
        :type change_amount: str
        :param balance_after_change: 变更后余额，单位为元。
        :type balance_after_change: str
        :param type: 收支类型。 1：收入2：支出
        :type type: str
        """
        
        

        self._account_change_id = None
        self._trade_detail_type = None
        self._trade_time = None
        self._trade_id = None
        self._change_amount = None
        self._balance_after_change = None
        self._type = None
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
        if type is not None:
            self.type = type

    @property
    def account_change_id(self):
        r"""Gets the account_change_id of this AccountChangeRecord.

        收支明细流水号。

        :return: The account_change_id of this AccountChangeRecord.
        :rtype: str
        """
        return self._account_change_id

    @account_change_id.setter
    def account_change_id(self, account_change_id):
        r"""Sets the account_change_id of this AccountChangeRecord.

        收支明细流水号。

        :param account_change_id: The account_change_id of this AccountChangeRecord.
        :type account_change_id: str
        """
        self._account_change_id = account_change_id

    @property
    def trade_detail_type(self):
        r"""Gets the trade_detail_type of this AccountChangeRecord.

        交易详细类型。 SOURCE_OPERAIION_ADJUST_CREDIT：调账(信用额度调整)SOURCE_OPERAIION_RECHARGE：充值SOURCE_OPERAIION_DEDEUCT：消费(包年/包月)SOURCE_OPERAIION_MANUALFROZE：冻结(人工冻结)SOURCE_OPERAIION_MANUALUNFROZE：冻结(人工解冻)SOURCE_OPERAIION_MANUALCLEARFROZEN：冻结(人工清零)SOURCE_OPERAIION_TRANS_TO_BALANCE：转账(保证金转余额)SOURCE_OPERATION_BEADJUST：伙伴拨款SOURCE_OPERATION_BEUNBIND：交易模式变更(切换/解除关联回收)SOURCE_OPERAIION_EXPIRECLEAR：过期清零SOURCE_OPERAIION_ONETIME：消费(一次性扣费)SOURCE_OPERAIION_REFUND：退款SOURCE_OPERAIION_UNFROZEN：退款(退款解冻)SOURCE_OPERAIION_CLEARFROZEN：退款(退款清零)SOURCE_OPERAIION_ADJUST：调账(余额调整)SOURCE_OPERAIION_USAGE：消费(按需)SOURCE_OPERAIION_WRITEOFF：消费(欠费还款)SOURCE_OPERAIION_UNSUBSCRIBE：退款SOURCE_OPERAIION_RFROZEN：退款(退款冻结)SOURCE_OPERAIION_TRANS_TO_FOREGIFT：转账(余额转保证金)SOURCE_OPERAIION_PRIZE：调账(赠送)SOURCE_OPERATION_BERETRIEVE：伙伴回收SOURCE_OPERAIION_PRECISIONCOMP：消费(精度补扣)SOURCE_OPERAIION_FREERESDEDUCT：消费(免费资源扣减)SOURCE_OPERAIION_MERGE：奖励金转换(合并)SOURCE_OPERAIION_CONVERT_BONUS：奖励金转换SOURCE_OPERAIION_RECHARGE_REBATE：充值(激励返点)SOURCE_OPERATION_COUPONCANCEL：优惠券回收SOURCE_OPERAIION_BILLREFUND：调账(华为核销)SOURCE_OPERATION_TRADEMODE_TRANSFER：交易模式变更(和伙伴关联)SOURCE_OPERATION_SYSTEM_FROZEN：系统冻结（购买标销合同的伙伴涉及该模式）SOURCE_OPERATION_SYSTEM_UNFROZEN：系统解冻（购买标销合同的伙伴涉及该模式）SOURCE_OPERATION_COUPON_QUOTA_TRANSFER：调账(兑换现金券额度)SOURCE_OPERATIION_RIDEDUCT：消费(预留实例)SOURCE_OPERATION_COUPON_QUOTA_RECLAIM：代金券回收

        :return: The trade_detail_type of this AccountChangeRecord.
        :rtype: str
        """
        return self._trade_detail_type

    @trade_detail_type.setter
    def trade_detail_type(self, trade_detail_type):
        r"""Sets the trade_detail_type of this AccountChangeRecord.

        交易详细类型。 SOURCE_OPERAIION_ADJUST_CREDIT：调账(信用额度调整)SOURCE_OPERAIION_RECHARGE：充值SOURCE_OPERAIION_DEDEUCT：消费(包年/包月)SOURCE_OPERAIION_MANUALFROZE：冻结(人工冻结)SOURCE_OPERAIION_MANUALUNFROZE：冻结(人工解冻)SOURCE_OPERAIION_MANUALCLEARFROZEN：冻结(人工清零)SOURCE_OPERAIION_TRANS_TO_BALANCE：转账(保证金转余额)SOURCE_OPERATION_BEADJUST：伙伴拨款SOURCE_OPERATION_BEUNBIND：交易模式变更(切换/解除关联回收)SOURCE_OPERAIION_EXPIRECLEAR：过期清零SOURCE_OPERAIION_ONETIME：消费(一次性扣费)SOURCE_OPERAIION_REFUND：退款SOURCE_OPERAIION_UNFROZEN：退款(退款解冻)SOURCE_OPERAIION_CLEARFROZEN：退款(退款清零)SOURCE_OPERAIION_ADJUST：调账(余额调整)SOURCE_OPERAIION_USAGE：消费(按需)SOURCE_OPERAIION_WRITEOFF：消费(欠费还款)SOURCE_OPERAIION_UNSUBSCRIBE：退款SOURCE_OPERAIION_RFROZEN：退款(退款冻结)SOURCE_OPERAIION_TRANS_TO_FOREGIFT：转账(余额转保证金)SOURCE_OPERAIION_PRIZE：调账(赠送)SOURCE_OPERATION_BERETRIEVE：伙伴回收SOURCE_OPERAIION_PRECISIONCOMP：消费(精度补扣)SOURCE_OPERAIION_FREERESDEDUCT：消费(免费资源扣减)SOURCE_OPERAIION_MERGE：奖励金转换(合并)SOURCE_OPERAIION_CONVERT_BONUS：奖励金转换SOURCE_OPERAIION_RECHARGE_REBATE：充值(激励返点)SOURCE_OPERATION_COUPONCANCEL：优惠券回收SOURCE_OPERAIION_BILLREFUND：调账(华为核销)SOURCE_OPERATION_TRADEMODE_TRANSFER：交易模式变更(和伙伴关联)SOURCE_OPERATION_SYSTEM_FROZEN：系统冻结（购买标销合同的伙伴涉及该模式）SOURCE_OPERATION_SYSTEM_UNFROZEN：系统解冻（购买标销合同的伙伴涉及该模式）SOURCE_OPERATION_COUPON_QUOTA_TRANSFER：调账(兑换现金券额度)SOURCE_OPERATIION_RIDEDUCT：消费(预留实例)SOURCE_OPERATION_COUPON_QUOTA_RECLAIM：代金券回收

        :param trade_detail_type: The trade_detail_type of this AccountChangeRecord.
        :type trade_detail_type: str
        """
        self._trade_detail_type = trade_detail_type

    @property
    def trade_time(self):
        r"""Gets the trade_time of this AccountChangeRecord.

        交易时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2016-03-28T14:45:38Z”。

        :return: The trade_time of this AccountChangeRecord.
        :rtype: str
        """
        return self._trade_time

    @trade_time.setter
    def trade_time(self, trade_time):
        r"""Sets the trade_time of this AccountChangeRecord.

        交易时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2016-03-28T14:45:38Z”。

        :param trade_time: The trade_time of this AccountChangeRecord.
        :type trade_time: str
        """
        self._trade_time = trade_time

    @property
    def trade_id(self):
        r"""Gets the trade_id of this AccountChangeRecord.

        交易ID/订单ID。

        :return: The trade_id of this AccountChangeRecord.
        :rtype: str
        """
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        r"""Sets the trade_id of this AccountChangeRecord.

        交易ID/订单ID。

        :param trade_id: The trade_id of this AccountChangeRecord.
        :type trade_id: str
        """
        self._trade_id = trade_id

    @property
    def change_amount(self):
        r"""Gets the change_amount of this AccountChangeRecord.

        变更金额，单位为元。

        :return: The change_amount of this AccountChangeRecord.
        :rtype: str
        """
        return self._change_amount

    @change_amount.setter
    def change_amount(self, change_amount):
        r"""Sets the change_amount of this AccountChangeRecord.

        变更金额，单位为元。

        :param change_amount: The change_amount of this AccountChangeRecord.
        :type change_amount: str
        """
        self._change_amount = change_amount

    @property
    def balance_after_change(self):
        r"""Gets the balance_after_change of this AccountChangeRecord.

        变更后余额，单位为元。

        :return: The balance_after_change of this AccountChangeRecord.
        :rtype: str
        """
        return self._balance_after_change

    @balance_after_change.setter
    def balance_after_change(self, balance_after_change):
        r"""Sets the balance_after_change of this AccountChangeRecord.

        变更后余额，单位为元。

        :param balance_after_change: The balance_after_change of this AccountChangeRecord.
        :type balance_after_change: str
        """
        self._balance_after_change = balance_after_change

    @property
    def type(self):
        r"""Gets the type of this AccountChangeRecord.

        收支类型。 1：收入2：支出

        :return: The type of this AccountChangeRecord.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AccountChangeRecord.

        收支类型。 1：收入2：支出

        :param type: The type of this AccountChangeRecord.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, AccountChangeRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
