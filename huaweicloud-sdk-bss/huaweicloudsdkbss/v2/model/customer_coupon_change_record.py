# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomerCouponChangeRecord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'coupon_id': 'str',
        'trade_detail_type': 'str',
        'trade_time': 'str',
        'trade_id': 'str',
        'change_amount': 'str',
        'balance_after_change': 'str',
        'revenue_expense_type': 'str',
        'bill_cycle': 'str',
        'account_name': 'str',
        'cloud_service_type_name': 'str',
        'resource_type_name': 'str'
    }

    attribute_map = {
        'coupon_id': 'coupon_id',
        'trade_detail_type': 'trade_detail_type',
        'trade_time': 'trade_time',
        'trade_id': 'trade_id',
        'change_amount': 'change_amount',
        'balance_after_change': 'balance_after_change',
        'revenue_expense_type': 'revenue_expense_type',
        'bill_cycle': 'bill_cycle',
        'account_name': 'account_name',
        'cloud_service_type_name': 'cloud_service_type_name',
        'resource_type_name': 'resource_type_name'
    }

    def __init__(self, coupon_id=None, trade_detail_type=None, trade_time=None, trade_id=None, change_amount=None, balance_after_change=None, revenue_expense_type=None, bill_cycle=None, account_name=None, cloud_service_type_name=None, resource_type_name=None):
        r"""CustomerCouponChangeRecord

        The model defined in huaweicloud sdk

        :param coupon_id: |参数名称：优惠券ID| |参数约束及描述：优惠券ID，范围限制:0-64|
        :type coupon_id: str
        :param trade_detail_type: |参数名称：交易详细类型| |参数约束及描述：交易详细类型，范围限制:0-128， SOURCE_OPERAIION_DEDEUCT：消费(包年/包月) SOURCE_OPERAIION_USAGE：消费(按需) SOURCE_OPERAIION_SAVINGS_PLANS：消费(节省计划) SOURCE_OPERAIION_WRITEOFF：消费(欠费还款) SOURCE_OPERAIION_EXPIRECLEAR：过期清零 SOURCE_OPERAIION_UNSUBSCRIBE：退券(退订) SOURCE_OPERAIION_UNFROZEN：退券(流程中) SOURCE_OPERAIION_RFROZEN：退券(流程中) SOURCE_OPERAIION_PRIZE：激活 SOURCE_OPERAIION_BILLREFUND：调账(华为核销) SOURCE_OPERATION_COUPONCANCEL：优惠券回收 SOURCE_OPERATION_DEPOSIT_FROZEN：保证金冻结 SOURCE_OPERATION_DEPOSIT_UNFROZEN：保证金解冻 SOURCE_OPERATION_RETRIEVE：回收(企业回收) SOURCE_OPERATION_TRANSFER：划拨(企业划拨)|
        :type trade_detail_type: str
        :param trade_time: |参数名称：交易时间| |参数约束及描述：交易时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|
        :type trade_time: str
        :param trade_id: |参数名称：交易ID/订单ID| |参数约束及描述：交易ID/订单ID，范围限制：0-128|
        :type trade_id: str
        :param change_amount: |参数名称：变更金额| |参数约束及描述：变更金额|
        :type change_amount: str
        :param balance_after_change: |参数名称：变更后余额| |参数约束及描述：变更后余额|
        :type balance_after_change: str
        :param revenue_expense_type: |参数名称：收支类型| |参数约束及描述：收支类型。REVENUE：收入 EXPENSE：支出|
        :type revenue_expense_type: str
        :param bill_cycle: |参数名称：账期| |参数约束及描述：账期|
        :type bill_cycle: str
        :param account_name: |参数名称：账号名称| |参数约束及描述：账号名称，范围限制：0-128|
        :type account_name: str
        :param cloud_service_type_name: |参数名称：云服务类型名称| |参数约束及描述：产品的云服务名称，范围限制：0-200|
        :type cloud_service_type_name: str
        :param resource_type_name: |参数名称：资源类型名称| |参数约束及描述：产品的资源类型名称，范围限制：0-200|
        :type resource_type_name: str
        """
        
        

        self._coupon_id = None
        self._trade_detail_type = None
        self._trade_time = None
        self._trade_id = None
        self._change_amount = None
        self._balance_after_change = None
        self._revenue_expense_type = None
        self._bill_cycle = None
        self._account_name = None
        self._cloud_service_type_name = None
        self._resource_type_name = None
        self.discriminator = None

        if coupon_id is not None:
            self.coupon_id = coupon_id
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
        if account_name is not None:
            self.account_name = account_name
        if cloud_service_type_name is not None:
            self.cloud_service_type_name = cloud_service_type_name
        if resource_type_name is not None:
            self.resource_type_name = resource_type_name

    @property
    def coupon_id(self):
        r"""Gets the coupon_id of this CustomerCouponChangeRecord.

        |参数名称：优惠券ID| |参数约束及描述：优惠券ID，范围限制:0-64|

        :return: The coupon_id of this CustomerCouponChangeRecord.
        :rtype: str
        """
        return self._coupon_id

    @coupon_id.setter
    def coupon_id(self, coupon_id):
        r"""Sets the coupon_id of this CustomerCouponChangeRecord.

        |参数名称：优惠券ID| |参数约束及描述：优惠券ID，范围限制:0-64|

        :param coupon_id: The coupon_id of this CustomerCouponChangeRecord.
        :type coupon_id: str
        """
        self._coupon_id = coupon_id

    @property
    def trade_detail_type(self):
        r"""Gets the trade_detail_type of this CustomerCouponChangeRecord.

        |参数名称：交易详细类型| |参数约束及描述：交易详细类型，范围限制:0-128， SOURCE_OPERAIION_DEDEUCT：消费(包年/包月) SOURCE_OPERAIION_USAGE：消费(按需) SOURCE_OPERAIION_SAVINGS_PLANS：消费(节省计划) SOURCE_OPERAIION_WRITEOFF：消费(欠费还款) SOURCE_OPERAIION_EXPIRECLEAR：过期清零 SOURCE_OPERAIION_UNSUBSCRIBE：退券(退订) SOURCE_OPERAIION_UNFROZEN：退券(流程中) SOURCE_OPERAIION_RFROZEN：退券(流程中) SOURCE_OPERAIION_PRIZE：激活 SOURCE_OPERAIION_BILLREFUND：调账(华为核销) SOURCE_OPERATION_COUPONCANCEL：优惠券回收 SOURCE_OPERATION_DEPOSIT_FROZEN：保证金冻结 SOURCE_OPERATION_DEPOSIT_UNFROZEN：保证金解冻 SOURCE_OPERATION_RETRIEVE：回收(企业回收) SOURCE_OPERATION_TRANSFER：划拨(企业划拨)|

        :return: The trade_detail_type of this CustomerCouponChangeRecord.
        :rtype: str
        """
        return self._trade_detail_type

    @trade_detail_type.setter
    def trade_detail_type(self, trade_detail_type):
        r"""Sets the trade_detail_type of this CustomerCouponChangeRecord.

        |参数名称：交易详细类型| |参数约束及描述：交易详细类型，范围限制:0-128， SOURCE_OPERAIION_DEDEUCT：消费(包年/包月) SOURCE_OPERAIION_USAGE：消费(按需) SOURCE_OPERAIION_SAVINGS_PLANS：消费(节省计划) SOURCE_OPERAIION_WRITEOFF：消费(欠费还款) SOURCE_OPERAIION_EXPIRECLEAR：过期清零 SOURCE_OPERAIION_UNSUBSCRIBE：退券(退订) SOURCE_OPERAIION_UNFROZEN：退券(流程中) SOURCE_OPERAIION_RFROZEN：退券(流程中) SOURCE_OPERAIION_PRIZE：激活 SOURCE_OPERAIION_BILLREFUND：调账(华为核销) SOURCE_OPERATION_COUPONCANCEL：优惠券回收 SOURCE_OPERATION_DEPOSIT_FROZEN：保证金冻结 SOURCE_OPERATION_DEPOSIT_UNFROZEN：保证金解冻 SOURCE_OPERATION_RETRIEVE：回收(企业回收) SOURCE_OPERATION_TRANSFER：划拨(企业划拨)|

        :param trade_detail_type: The trade_detail_type of this CustomerCouponChangeRecord.
        :type trade_detail_type: str
        """
        self._trade_detail_type = trade_detail_type

    @property
    def trade_time(self):
        r"""Gets the trade_time of this CustomerCouponChangeRecord.

        |参数名称：交易时间| |参数约束及描述：交易时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :return: The trade_time of this CustomerCouponChangeRecord.
        :rtype: str
        """
        return self._trade_time

    @trade_time.setter
    def trade_time(self, trade_time):
        r"""Sets the trade_time of this CustomerCouponChangeRecord.

        |参数名称：交易时间| |参数约束及描述：交易时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :param trade_time: The trade_time of this CustomerCouponChangeRecord.
        :type trade_time: str
        """
        self._trade_time = trade_time

    @property
    def trade_id(self):
        r"""Gets the trade_id of this CustomerCouponChangeRecord.

        |参数名称：交易ID/订单ID| |参数约束及描述：交易ID/订单ID，范围限制：0-128|

        :return: The trade_id of this CustomerCouponChangeRecord.
        :rtype: str
        """
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        r"""Sets the trade_id of this CustomerCouponChangeRecord.

        |参数名称：交易ID/订单ID| |参数约束及描述：交易ID/订单ID，范围限制：0-128|

        :param trade_id: The trade_id of this CustomerCouponChangeRecord.
        :type trade_id: str
        """
        self._trade_id = trade_id

    @property
    def change_amount(self):
        r"""Gets the change_amount of this CustomerCouponChangeRecord.

        |参数名称：变更金额| |参数约束及描述：变更金额|

        :return: The change_amount of this CustomerCouponChangeRecord.
        :rtype: str
        """
        return self._change_amount

    @change_amount.setter
    def change_amount(self, change_amount):
        r"""Sets the change_amount of this CustomerCouponChangeRecord.

        |参数名称：变更金额| |参数约束及描述：变更金额|

        :param change_amount: The change_amount of this CustomerCouponChangeRecord.
        :type change_amount: str
        """
        self._change_amount = change_amount

    @property
    def balance_after_change(self):
        r"""Gets the balance_after_change of this CustomerCouponChangeRecord.

        |参数名称：变更后余额| |参数约束及描述：变更后余额|

        :return: The balance_after_change of this CustomerCouponChangeRecord.
        :rtype: str
        """
        return self._balance_after_change

    @balance_after_change.setter
    def balance_after_change(self, balance_after_change):
        r"""Sets the balance_after_change of this CustomerCouponChangeRecord.

        |参数名称：变更后余额| |参数约束及描述：变更后余额|

        :param balance_after_change: The balance_after_change of this CustomerCouponChangeRecord.
        :type balance_after_change: str
        """
        self._balance_after_change = balance_after_change

    @property
    def revenue_expense_type(self):
        r"""Gets the revenue_expense_type of this CustomerCouponChangeRecord.

        |参数名称：收支类型| |参数约束及描述：收支类型。REVENUE：收入 EXPENSE：支出|

        :return: The revenue_expense_type of this CustomerCouponChangeRecord.
        :rtype: str
        """
        return self._revenue_expense_type

    @revenue_expense_type.setter
    def revenue_expense_type(self, revenue_expense_type):
        r"""Sets the revenue_expense_type of this CustomerCouponChangeRecord.

        |参数名称：收支类型| |参数约束及描述：收支类型。REVENUE：收入 EXPENSE：支出|

        :param revenue_expense_type: The revenue_expense_type of this CustomerCouponChangeRecord.
        :type revenue_expense_type: str
        """
        self._revenue_expense_type = revenue_expense_type

    @property
    def bill_cycle(self):
        r"""Gets the bill_cycle of this CustomerCouponChangeRecord.

        |参数名称：账期| |参数约束及描述：账期|

        :return: The bill_cycle of this CustomerCouponChangeRecord.
        :rtype: str
        """
        return self._bill_cycle

    @bill_cycle.setter
    def bill_cycle(self, bill_cycle):
        r"""Sets the bill_cycle of this CustomerCouponChangeRecord.

        |参数名称：账期| |参数约束及描述：账期|

        :param bill_cycle: The bill_cycle of this CustomerCouponChangeRecord.
        :type bill_cycle: str
        """
        self._bill_cycle = bill_cycle

    @property
    def account_name(self):
        r"""Gets the account_name of this CustomerCouponChangeRecord.

        |参数名称：账号名称| |参数约束及描述：账号名称，范围限制：0-128|

        :return: The account_name of this CustomerCouponChangeRecord.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        r"""Sets the account_name of this CustomerCouponChangeRecord.

        |参数名称：账号名称| |参数约束及描述：账号名称，范围限制：0-128|

        :param account_name: The account_name of this CustomerCouponChangeRecord.
        :type account_name: str
        """
        self._account_name = account_name

    @property
    def cloud_service_type_name(self):
        r"""Gets the cloud_service_type_name of this CustomerCouponChangeRecord.

        |参数名称：云服务类型名称| |参数约束及描述：产品的云服务名称，范围限制：0-200|

        :return: The cloud_service_type_name of this CustomerCouponChangeRecord.
        :rtype: str
        """
        return self._cloud_service_type_name

    @cloud_service_type_name.setter
    def cloud_service_type_name(self, cloud_service_type_name):
        r"""Sets the cloud_service_type_name of this CustomerCouponChangeRecord.

        |参数名称：云服务类型名称| |参数约束及描述：产品的云服务名称，范围限制：0-200|

        :param cloud_service_type_name: The cloud_service_type_name of this CustomerCouponChangeRecord.
        :type cloud_service_type_name: str
        """
        self._cloud_service_type_name = cloud_service_type_name

    @property
    def resource_type_name(self):
        r"""Gets the resource_type_name of this CustomerCouponChangeRecord.

        |参数名称：资源类型名称| |参数约束及描述：产品的资源类型名称，范围限制：0-200|

        :return: The resource_type_name of this CustomerCouponChangeRecord.
        :rtype: str
        """
        return self._resource_type_name

    @resource_type_name.setter
    def resource_type_name(self, resource_type_name):
        r"""Sets the resource_type_name of this CustomerCouponChangeRecord.

        |参数名称：资源类型名称| |参数约束及描述：产品的资源类型名称，范围限制：0-200|

        :param resource_type_name: The resource_type_name of this CustomerCouponChangeRecord.
        :type resource_type_name: str
        """
        self._resource_type_name = resource_type_name

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CustomerCouponChangeRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
