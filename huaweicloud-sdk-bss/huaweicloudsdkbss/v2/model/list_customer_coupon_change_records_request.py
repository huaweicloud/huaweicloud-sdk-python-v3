# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCustomerCouponChangeRecordsRequest:

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
        'trade_id': 'str',
        'trade_time_begin': 'str',
        'trade_time_end': 'str',
        'coupon_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'balance_type': 'balance_type',
        'revenue_expense_type': 'revenue_expense_type',
        'trade_type': 'trade_type',
        'trade_id': 'trade_id',
        'trade_time_begin': 'trade_time_begin',
        'trade_time_end': 'trade_time_end',
        'coupon_id': 'coupon_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, balance_type=None, revenue_expense_type=None, trade_type=None, trade_id=None, trade_time_begin=None, trade_time_end=None, coupon_id=None, offset=None, limit=None):
        r"""ListCustomerCouponChangeRecordsRequest

        The model defined in huaweicloud sdk

        :param balance_type: |参数名称：账户类型| |参数的约束及描述：该参数必填，BALANCE_TYPE_COUPON：代金券账户|
        :type balance_type: str
        :param revenue_expense_type: |参数名称：收支类型| |参数的约束及描述：该参数非必填，REVENUE：收入 EXPENSE：支出。此参数不携带时，不作为筛选条件；此参数携带值不允许为空、空串，有枚举值校验。|
        :type revenue_expense_type: str
        :param trade_type: |参数名称：交易类型| |参数的约束及描述：该参数非必填，ADJUST：激活 DEDEUCT：消费 REFUND：退券 RFROZEN：冻结 EXPIRED：过期清零 COUPONADJUST：划拨 COUPONCANCEL：回收。此参数不携带时，不作为筛选条件；此参数携带值不允许为空、空串，有枚举值校验。|
        :type trade_type: str
        :param trade_id: |参数名称：交易ID/订单ID| |参数的约束及描述：该参数非必填，范围限制：0-128。此参数不携带或携带值为空时，不作为筛选条件。|
        :type trade_id: str
        :param trade_time_begin: |参数名称：查询收支明细的开始日期| |参数的约束及描述：该参数非必填，东八区时间，格式为YYYY-MM-DD，此参数不携带、携带值为空时，默认值为一年前的当天日期；此参数不允许携带值为空串，有参数校验。|
        :type trade_time_begin: str
        :param trade_time_end: |参数名称：查询收支明细的结束日期| |参数的约束及描述：该参数非必填，东八区时间，格式为YYYY-MM-DD，此参数不携带、携带值为空时，默认值为当前日期；此参数不允许携带值为空串，有参数校验。|
        :type trade_time_end: str
        :param coupon_id: |参数名称：优惠券ID。| |参数的约束及描述：该参数非必填，范围限制：0-64。此参数不携带或携带值为空时，不作为筛选条件。|
        :type coupon_id: str
        :param offset: |参数名称：偏移量| |参数的约束及描述：该参数非必填，范围限制：0-2147483647，默认值为0。此参数不携带或携带值为空时，默认传参为0。|
        :type offset: int
        :param limit: |参数名称：每次查询的数量| |参数的约束及描述：该参数非必填，范围限制：1-100，默认值为10。此参数不携带或携带值为空时，默认传参为10。|
        :type limit: int
        """
        
        

        self._balance_type = None
        self._revenue_expense_type = None
        self._trade_type = None
        self._trade_id = None
        self._trade_time_begin = None
        self._trade_time_end = None
        self._coupon_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.balance_type = balance_type
        if revenue_expense_type is not None:
            self.revenue_expense_type = revenue_expense_type
        if trade_type is not None:
            self.trade_type = trade_type
        if trade_id is not None:
            self.trade_id = trade_id
        if trade_time_begin is not None:
            self.trade_time_begin = trade_time_begin
        if trade_time_end is not None:
            self.trade_time_end = trade_time_end
        if coupon_id is not None:
            self.coupon_id = coupon_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def balance_type(self):
        r"""Gets the balance_type of this ListCustomerCouponChangeRecordsRequest.

        |参数名称：账户类型| |参数的约束及描述：该参数必填，BALANCE_TYPE_COUPON：代金券账户|

        :return: The balance_type of this ListCustomerCouponChangeRecordsRequest.
        :rtype: str
        """
        return self._balance_type

    @balance_type.setter
    def balance_type(self, balance_type):
        r"""Sets the balance_type of this ListCustomerCouponChangeRecordsRequest.

        |参数名称：账户类型| |参数的约束及描述：该参数必填，BALANCE_TYPE_COUPON：代金券账户|

        :param balance_type: The balance_type of this ListCustomerCouponChangeRecordsRequest.
        :type balance_type: str
        """
        self._balance_type = balance_type

    @property
    def revenue_expense_type(self):
        r"""Gets the revenue_expense_type of this ListCustomerCouponChangeRecordsRequest.

        |参数名称：收支类型| |参数的约束及描述：该参数非必填，REVENUE：收入 EXPENSE：支出。此参数不携带时，不作为筛选条件；此参数携带值不允许为空、空串，有枚举值校验。|

        :return: The revenue_expense_type of this ListCustomerCouponChangeRecordsRequest.
        :rtype: str
        """
        return self._revenue_expense_type

    @revenue_expense_type.setter
    def revenue_expense_type(self, revenue_expense_type):
        r"""Sets the revenue_expense_type of this ListCustomerCouponChangeRecordsRequest.

        |参数名称：收支类型| |参数的约束及描述：该参数非必填，REVENUE：收入 EXPENSE：支出。此参数不携带时，不作为筛选条件；此参数携带值不允许为空、空串，有枚举值校验。|

        :param revenue_expense_type: The revenue_expense_type of this ListCustomerCouponChangeRecordsRequest.
        :type revenue_expense_type: str
        """
        self._revenue_expense_type = revenue_expense_type

    @property
    def trade_type(self):
        r"""Gets the trade_type of this ListCustomerCouponChangeRecordsRequest.

        |参数名称：交易类型| |参数的约束及描述：该参数非必填，ADJUST：激活 DEDEUCT：消费 REFUND：退券 RFROZEN：冻结 EXPIRED：过期清零 COUPONADJUST：划拨 COUPONCANCEL：回收。此参数不携带时，不作为筛选条件；此参数携带值不允许为空、空串，有枚举值校验。|

        :return: The trade_type of this ListCustomerCouponChangeRecordsRequest.
        :rtype: str
        """
        return self._trade_type

    @trade_type.setter
    def trade_type(self, trade_type):
        r"""Sets the trade_type of this ListCustomerCouponChangeRecordsRequest.

        |参数名称：交易类型| |参数的约束及描述：该参数非必填，ADJUST：激活 DEDEUCT：消费 REFUND：退券 RFROZEN：冻结 EXPIRED：过期清零 COUPONADJUST：划拨 COUPONCANCEL：回收。此参数不携带时，不作为筛选条件；此参数携带值不允许为空、空串，有枚举值校验。|

        :param trade_type: The trade_type of this ListCustomerCouponChangeRecordsRequest.
        :type trade_type: str
        """
        self._trade_type = trade_type

    @property
    def trade_id(self):
        r"""Gets the trade_id of this ListCustomerCouponChangeRecordsRequest.

        |参数名称：交易ID/订单ID| |参数的约束及描述：该参数非必填，范围限制：0-128。此参数不携带或携带值为空时，不作为筛选条件。|

        :return: The trade_id of this ListCustomerCouponChangeRecordsRequest.
        :rtype: str
        """
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        r"""Sets the trade_id of this ListCustomerCouponChangeRecordsRequest.

        |参数名称：交易ID/订单ID| |参数的约束及描述：该参数非必填，范围限制：0-128。此参数不携带或携带值为空时，不作为筛选条件。|

        :param trade_id: The trade_id of this ListCustomerCouponChangeRecordsRequest.
        :type trade_id: str
        """
        self._trade_id = trade_id

    @property
    def trade_time_begin(self):
        r"""Gets the trade_time_begin of this ListCustomerCouponChangeRecordsRequest.

        |参数名称：查询收支明细的开始日期| |参数的约束及描述：该参数非必填，东八区时间，格式为YYYY-MM-DD，此参数不携带、携带值为空时，默认值为一年前的当天日期；此参数不允许携带值为空串，有参数校验。|

        :return: The trade_time_begin of this ListCustomerCouponChangeRecordsRequest.
        :rtype: str
        """
        return self._trade_time_begin

    @trade_time_begin.setter
    def trade_time_begin(self, trade_time_begin):
        r"""Sets the trade_time_begin of this ListCustomerCouponChangeRecordsRequest.

        |参数名称：查询收支明细的开始日期| |参数的约束及描述：该参数非必填，东八区时间，格式为YYYY-MM-DD，此参数不携带、携带值为空时，默认值为一年前的当天日期；此参数不允许携带值为空串，有参数校验。|

        :param trade_time_begin: The trade_time_begin of this ListCustomerCouponChangeRecordsRequest.
        :type trade_time_begin: str
        """
        self._trade_time_begin = trade_time_begin

    @property
    def trade_time_end(self):
        r"""Gets the trade_time_end of this ListCustomerCouponChangeRecordsRequest.

        |参数名称：查询收支明细的结束日期| |参数的约束及描述：该参数非必填，东八区时间，格式为YYYY-MM-DD，此参数不携带、携带值为空时，默认值为当前日期；此参数不允许携带值为空串，有参数校验。|

        :return: The trade_time_end of this ListCustomerCouponChangeRecordsRequest.
        :rtype: str
        """
        return self._trade_time_end

    @trade_time_end.setter
    def trade_time_end(self, trade_time_end):
        r"""Sets the trade_time_end of this ListCustomerCouponChangeRecordsRequest.

        |参数名称：查询收支明细的结束日期| |参数的约束及描述：该参数非必填，东八区时间，格式为YYYY-MM-DD，此参数不携带、携带值为空时，默认值为当前日期；此参数不允许携带值为空串，有参数校验。|

        :param trade_time_end: The trade_time_end of this ListCustomerCouponChangeRecordsRequest.
        :type trade_time_end: str
        """
        self._trade_time_end = trade_time_end

    @property
    def coupon_id(self):
        r"""Gets the coupon_id of this ListCustomerCouponChangeRecordsRequest.

        |参数名称：优惠券ID。| |参数的约束及描述：该参数非必填，范围限制：0-64。此参数不携带或携带值为空时，不作为筛选条件。|

        :return: The coupon_id of this ListCustomerCouponChangeRecordsRequest.
        :rtype: str
        """
        return self._coupon_id

    @coupon_id.setter
    def coupon_id(self, coupon_id):
        r"""Sets the coupon_id of this ListCustomerCouponChangeRecordsRequest.

        |参数名称：优惠券ID。| |参数的约束及描述：该参数非必填，范围限制：0-64。此参数不携带或携带值为空时，不作为筛选条件。|

        :param coupon_id: The coupon_id of this ListCustomerCouponChangeRecordsRequest.
        :type coupon_id: str
        """
        self._coupon_id = coupon_id

    @property
    def offset(self):
        r"""Gets the offset of this ListCustomerCouponChangeRecordsRequest.

        |参数名称：偏移量| |参数的约束及描述：该参数非必填，范围限制：0-2147483647，默认值为0。此参数不携带或携带值为空时，默认传参为0。|

        :return: The offset of this ListCustomerCouponChangeRecordsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCustomerCouponChangeRecordsRequest.

        |参数名称：偏移量| |参数的约束及描述：该参数非必填，范围限制：0-2147483647，默认值为0。此参数不携带或携带值为空时，默认传参为0。|

        :param offset: The offset of this ListCustomerCouponChangeRecordsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListCustomerCouponChangeRecordsRequest.

        |参数名称：每次查询的数量| |参数的约束及描述：该参数非必填，范围限制：1-100，默认值为10。此参数不携带或携带值为空时，默认传参为10。|

        :return: The limit of this ListCustomerCouponChangeRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCustomerCouponChangeRecordsRequest.

        |参数名称：每次查询的数量| |参数的约束及描述：该参数非必填，范围限制：1-100，默认值为10。此参数不携带或携带值为空时，默认传参为10。|

        :param limit: The limit of this ListCustomerCouponChangeRecordsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListCustomerCouponChangeRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
