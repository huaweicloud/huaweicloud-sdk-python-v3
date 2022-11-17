# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IQueryUserCouponsResultV2:

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
        'coupon_code': 'str',
        'status': 'int',
        'customer_id': 'str',
        'coupon_type': 'int',
        'measure_id': 'int',
        'face_value': 'float',
        'valid_time': 'str',
        'expire_time': 'str',
        'order_id': 'str',
        'promotion_plan_id': 'str',
        'plan_name': 'str',
        'plan_desc': 'str',
        'media_type': 'int',
        'fetch_method': 'int',
        'use_limits': 'list[ICouponUseLimitInfoV2]',
        'active_time': 'str',
        'reserve_time': 'str',
        'promotion_id': 'str',
        'create_time': 'str',
        'coupon_version': 'int',
        'balance': 'float',
        'lock_order_id': 'str',
        'coupon_usage': 'str',
        'is_frozen': 'str',
        'currency': 'str',
        'extend_param1': 'str',
        'source_id': 'str'
    }

    attribute_map = {
        'coupon_id': 'coupon_id',
        'coupon_code': 'coupon_code',
        'status': 'status',
        'customer_id': 'customer_id',
        'coupon_type': 'coupon_type',
        'measure_id': 'measure_id',
        'face_value': 'face_value',
        'valid_time': 'valid_time',
        'expire_time': 'expire_time',
        'order_id': 'order_id',
        'promotion_plan_id': 'promotion_plan_id',
        'plan_name': 'plan_name',
        'plan_desc': 'plan_desc',
        'media_type': 'media_type',
        'fetch_method': 'fetch_method',
        'use_limits': 'use_limits',
        'active_time': 'active_time',
        'reserve_time': 'reserve_time',
        'promotion_id': 'promotion_id',
        'create_time': 'create_time',
        'coupon_version': 'coupon_version',
        'balance': 'balance',
        'lock_order_id': 'lock_order_id',
        'coupon_usage': 'coupon_usage',
        'is_frozen': 'is_frozen',
        'currency': 'currency',
        'extend_param1': 'extend_param1',
        'source_id': 'source_id'
    }

    def __init__(self, coupon_id=None, coupon_code=None, status=None, customer_id=None, coupon_type=None, measure_id=None, face_value=None, valid_time=None, expire_time=None, order_id=None, promotion_plan_id=None, plan_name=None, plan_desc=None, media_type=None, fetch_method=None, use_limits=None, active_time=None, reserve_time=None, promotion_id=None, create_time=None, coupon_version=None, balance=None, lock_order_id=None, coupon_usage=None, is_frozen=None, currency=None, extend_param1=None, source_id=None):
        """IQueryUserCouponsResultV2

        The model defined in huaweicloud sdk

        :param coupon_id: 优惠券实例ID。
        :type coupon_id: str
        :param coupon_code: 优惠券编码。
        :type coupon_code: str
        :param status: 优惠券状态： 1：未激活2：待使用3：已使用4：已过期5：已回收
        :type status: int
        :param customer_id: 客户账号ID。
        :type customer_id: str
        :param coupon_type: 优惠券类型： 1：代金券2：折扣券（预留）3：产品券（预留）4：现金券（预留）
        :type coupon_type: int
        :param measure_id: 度量单位。 1：元
        :type measure_id: int
        :param face_value: 优惠券金额。
        :type face_value: float
        :param valid_time: 生效时间。 UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”。
        :type valid_time: str
        :param expire_time: 失效时间。 UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”。
        :type expire_time: str
        :param order_id: 订单ID。
        :type order_id: str
        :param promotion_plan_id: 促销计划ID。
        :type promotion_plan_id: str
        :param plan_name: 促销计划名称。
        :type plan_name: str
        :param plan_desc: 促销计划描述。
        :type plan_desc: str
        :param media_type: 介质类型。 1：电子券2：纸质券
        :type media_type: int
        :param fetch_method: 获取方式： 1：线上领取2：线上兑换3：线上发放4：线下获取5：事件赠送
        :type fetch_method: int
        :param use_limits: 优惠券使用限制。 具体请参见表3。
        :type use_limits: list[:class:`huaweicloudsdkbssintl.v2.ICouponUseLimitInfoV2`]
        :param active_time: 激活时间。 UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”。
        :type active_time: str
        :param reserve_time: 使用时间。 UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”。
        :type reserve_time: str
        :param promotion_id: 促销ID。
        :type promotion_id: str
        :param create_time: 创建时间。 UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”。
        :type create_time: str
        :param coupon_version: 优惠券版本： 1：老版本，老版本优惠券只能使用一次2：新版本，新版本优惠券可以反复使用
        :type coupon_version: int
        :param balance: 优惠券余额。单位：元。 如果为老版本优惠券，该值为空。
        :type balance: float
        :param lock_order_id: 锁定优惠券的订单ID。 如果为老版本优惠券，该值为空。
        :type lock_order_id: str
        :param coupon_usage: 优惠券用途。
        :type coupon_usage: str
        :param is_frozen: 优惠券是否冻结： 0：否1：是
        :type is_frozen: str
        :param currency: 币种。 USD：美元
        :type currency: str
        :param extend_param1: 扩展字段。
        :type extend_param1: str
        :param source_id: 发券来源。 如果是合作伙伴发送的券，此处为伙伴ID。如果是活动发券，此处为活动ID：云豆兑换优惠券：云豆计划ID累计送优惠券：累计送计划ID抽奖送优惠券：抽奖计划ID事件送优惠券：事件计划ID定制优惠券：创建人ID
        :type source_id: str
        """
        
        

        self._coupon_id = None
        self._coupon_code = None
        self._status = None
        self._customer_id = None
        self._coupon_type = None
        self._measure_id = None
        self._face_value = None
        self._valid_time = None
        self._expire_time = None
        self._order_id = None
        self._promotion_plan_id = None
        self._plan_name = None
        self._plan_desc = None
        self._media_type = None
        self._fetch_method = None
        self._use_limits = None
        self._active_time = None
        self._reserve_time = None
        self._promotion_id = None
        self._create_time = None
        self._coupon_version = None
        self._balance = None
        self._lock_order_id = None
        self._coupon_usage = None
        self._is_frozen = None
        self._currency = None
        self._extend_param1 = None
        self._source_id = None
        self.discriminator = None

        if coupon_id is not None:
            self.coupon_id = coupon_id
        if coupon_code is not None:
            self.coupon_code = coupon_code
        if status is not None:
            self.status = status
        if customer_id is not None:
            self.customer_id = customer_id
        if coupon_type is not None:
            self.coupon_type = coupon_type
        if measure_id is not None:
            self.measure_id = measure_id
        if face_value is not None:
            self.face_value = face_value
        if valid_time is not None:
            self.valid_time = valid_time
        if expire_time is not None:
            self.expire_time = expire_time
        if order_id is not None:
            self.order_id = order_id
        if promotion_plan_id is not None:
            self.promotion_plan_id = promotion_plan_id
        if plan_name is not None:
            self.plan_name = plan_name
        if plan_desc is not None:
            self.plan_desc = plan_desc
        if media_type is not None:
            self.media_type = media_type
        if fetch_method is not None:
            self.fetch_method = fetch_method
        if use_limits is not None:
            self.use_limits = use_limits
        if active_time is not None:
            self.active_time = active_time
        if reserve_time is not None:
            self.reserve_time = reserve_time
        if promotion_id is not None:
            self.promotion_id = promotion_id
        if create_time is not None:
            self.create_time = create_time
        if coupon_version is not None:
            self.coupon_version = coupon_version
        if balance is not None:
            self.balance = balance
        if lock_order_id is not None:
            self.lock_order_id = lock_order_id
        if coupon_usage is not None:
            self.coupon_usage = coupon_usage
        if is_frozen is not None:
            self.is_frozen = is_frozen
        if currency is not None:
            self.currency = currency
        if extend_param1 is not None:
            self.extend_param1 = extend_param1
        if source_id is not None:
            self.source_id = source_id

    @property
    def coupon_id(self):
        """Gets the coupon_id of this IQueryUserCouponsResultV2.

        优惠券实例ID。

        :return: The coupon_id of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._coupon_id

    @coupon_id.setter
    def coupon_id(self, coupon_id):
        """Sets the coupon_id of this IQueryUserCouponsResultV2.

        优惠券实例ID。

        :param coupon_id: The coupon_id of this IQueryUserCouponsResultV2.
        :type coupon_id: str
        """
        self._coupon_id = coupon_id

    @property
    def coupon_code(self):
        """Gets the coupon_code of this IQueryUserCouponsResultV2.

        优惠券编码。

        :return: The coupon_code of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._coupon_code

    @coupon_code.setter
    def coupon_code(self, coupon_code):
        """Sets the coupon_code of this IQueryUserCouponsResultV2.

        优惠券编码。

        :param coupon_code: The coupon_code of this IQueryUserCouponsResultV2.
        :type coupon_code: str
        """
        self._coupon_code = coupon_code

    @property
    def status(self):
        """Gets the status of this IQueryUserCouponsResultV2.

        优惠券状态： 1：未激活2：待使用3：已使用4：已过期5：已回收

        :return: The status of this IQueryUserCouponsResultV2.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IQueryUserCouponsResultV2.

        优惠券状态： 1：未激活2：待使用3：已使用4：已过期5：已回收

        :param status: The status of this IQueryUserCouponsResultV2.
        :type status: int
        """
        self._status = status

    @property
    def customer_id(self):
        """Gets the customer_id of this IQueryUserCouponsResultV2.

        客户账号ID。

        :return: The customer_id of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this IQueryUserCouponsResultV2.

        客户账号ID。

        :param customer_id: The customer_id of this IQueryUserCouponsResultV2.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def coupon_type(self):
        """Gets the coupon_type of this IQueryUserCouponsResultV2.

        优惠券类型： 1：代金券2：折扣券（预留）3：产品券（预留）4：现金券（预留）

        :return: The coupon_type of this IQueryUserCouponsResultV2.
        :rtype: int
        """
        return self._coupon_type

    @coupon_type.setter
    def coupon_type(self, coupon_type):
        """Sets the coupon_type of this IQueryUserCouponsResultV2.

        优惠券类型： 1：代金券2：折扣券（预留）3：产品券（预留）4：现金券（预留）

        :param coupon_type: The coupon_type of this IQueryUserCouponsResultV2.
        :type coupon_type: int
        """
        self._coupon_type = coupon_type

    @property
    def measure_id(self):
        """Gets the measure_id of this IQueryUserCouponsResultV2.

        度量单位。 1：元

        :return: The measure_id of this IQueryUserCouponsResultV2.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this IQueryUserCouponsResultV2.

        度量单位。 1：元

        :param measure_id: The measure_id of this IQueryUserCouponsResultV2.
        :type measure_id: int
        """
        self._measure_id = measure_id

    @property
    def face_value(self):
        """Gets the face_value of this IQueryUserCouponsResultV2.

        优惠券金额。

        :return: The face_value of this IQueryUserCouponsResultV2.
        :rtype: float
        """
        return self._face_value

    @face_value.setter
    def face_value(self, face_value):
        """Sets the face_value of this IQueryUserCouponsResultV2.

        优惠券金额。

        :param face_value: The face_value of this IQueryUserCouponsResultV2.
        :type face_value: float
        """
        self._face_value = face_value

    @property
    def valid_time(self):
        """Gets the valid_time of this IQueryUserCouponsResultV2.

        生效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :return: The valid_time of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._valid_time

    @valid_time.setter
    def valid_time(self, valid_time):
        """Sets the valid_time of this IQueryUserCouponsResultV2.

        生效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :param valid_time: The valid_time of this IQueryUserCouponsResultV2.
        :type valid_time: str
        """
        self._valid_time = valid_time

    @property
    def expire_time(self):
        """Gets the expire_time of this IQueryUserCouponsResultV2.

        失效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :return: The expire_time of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this IQueryUserCouponsResultV2.

        失效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :param expire_time: The expire_time of this IQueryUserCouponsResultV2.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def order_id(self):
        """Gets the order_id of this IQueryUserCouponsResultV2.

        订单ID。

        :return: The order_id of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this IQueryUserCouponsResultV2.

        订单ID。

        :param order_id: The order_id of this IQueryUserCouponsResultV2.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def promotion_plan_id(self):
        """Gets the promotion_plan_id of this IQueryUserCouponsResultV2.

        促销计划ID。

        :return: The promotion_plan_id of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._promotion_plan_id

    @promotion_plan_id.setter
    def promotion_plan_id(self, promotion_plan_id):
        """Sets the promotion_plan_id of this IQueryUserCouponsResultV2.

        促销计划ID。

        :param promotion_plan_id: The promotion_plan_id of this IQueryUserCouponsResultV2.
        :type promotion_plan_id: str
        """
        self._promotion_plan_id = promotion_plan_id

    @property
    def plan_name(self):
        """Gets the plan_name of this IQueryUserCouponsResultV2.

        促销计划名称。

        :return: The plan_name of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._plan_name

    @plan_name.setter
    def plan_name(self, plan_name):
        """Sets the plan_name of this IQueryUserCouponsResultV2.

        促销计划名称。

        :param plan_name: The plan_name of this IQueryUserCouponsResultV2.
        :type plan_name: str
        """
        self._plan_name = plan_name

    @property
    def plan_desc(self):
        """Gets the plan_desc of this IQueryUserCouponsResultV2.

        促销计划描述。

        :return: The plan_desc of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._plan_desc

    @plan_desc.setter
    def plan_desc(self, plan_desc):
        """Sets the plan_desc of this IQueryUserCouponsResultV2.

        促销计划描述。

        :param plan_desc: The plan_desc of this IQueryUserCouponsResultV2.
        :type plan_desc: str
        """
        self._plan_desc = plan_desc

    @property
    def media_type(self):
        """Gets the media_type of this IQueryUserCouponsResultV2.

        介质类型。 1：电子券2：纸质券

        :return: The media_type of this IQueryUserCouponsResultV2.
        :rtype: int
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this IQueryUserCouponsResultV2.

        介质类型。 1：电子券2：纸质券

        :param media_type: The media_type of this IQueryUserCouponsResultV2.
        :type media_type: int
        """
        self._media_type = media_type

    @property
    def fetch_method(self):
        """Gets the fetch_method of this IQueryUserCouponsResultV2.

        获取方式： 1：线上领取2：线上兑换3：线上发放4：线下获取5：事件赠送

        :return: The fetch_method of this IQueryUserCouponsResultV2.
        :rtype: int
        """
        return self._fetch_method

    @fetch_method.setter
    def fetch_method(self, fetch_method):
        """Sets the fetch_method of this IQueryUserCouponsResultV2.

        获取方式： 1：线上领取2：线上兑换3：线上发放4：线下获取5：事件赠送

        :param fetch_method: The fetch_method of this IQueryUserCouponsResultV2.
        :type fetch_method: int
        """
        self._fetch_method = fetch_method

    @property
    def use_limits(self):
        """Gets the use_limits of this IQueryUserCouponsResultV2.

        优惠券使用限制。 具体请参见表3。

        :return: The use_limits of this IQueryUserCouponsResultV2.
        :rtype: list[:class:`huaweicloudsdkbssintl.v2.ICouponUseLimitInfoV2`]
        """
        return self._use_limits

    @use_limits.setter
    def use_limits(self, use_limits):
        """Sets the use_limits of this IQueryUserCouponsResultV2.

        优惠券使用限制。 具体请参见表3。

        :param use_limits: The use_limits of this IQueryUserCouponsResultV2.
        :type use_limits: list[:class:`huaweicloudsdkbssintl.v2.ICouponUseLimitInfoV2`]
        """
        self._use_limits = use_limits

    @property
    def active_time(self):
        """Gets the active_time of this IQueryUserCouponsResultV2.

        激活时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :return: The active_time of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._active_time

    @active_time.setter
    def active_time(self, active_time):
        """Sets the active_time of this IQueryUserCouponsResultV2.

        激活时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :param active_time: The active_time of this IQueryUserCouponsResultV2.
        :type active_time: str
        """
        self._active_time = active_time

    @property
    def reserve_time(self):
        """Gets the reserve_time of this IQueryUserCouponsResultV2.

        使用时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :return: The reserve_time of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._reserve_time

    @reserve_time.setter
    def reserve_time(self, reserve_time):
        """Sets the reserve_time of this IQueryUserCouponsResultV2.

        使用时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :param reserve_time: The reserve_time of this IQueryUserCouponsResultV2.
        :type reserve_time: str
        """
        self._reserve_time = reserve_time

    @property
    def promotion_id(self):
        """Gets the promotion_id of this IQueryUserCouponsResultV2.

        促销ID。

        :return: The promotion_id of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._promotion_id

    @promotion_id.setter
    def promotion_id(self, promotion_id):
        """Sets the promotion_id of this IQueryUserCouponsResultV2.

        促销ID。

        :param promotion_id: The promotion_id of this IQueryUserCouponsResultV2.
        :type promotion_id: str
        """
        self._promotion_id = promotion_id

    @property
    def create_time(self):
        """Gets the create_time of this IQueryUserCouponsResultV2.

        创建时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :return: The create_time of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this IQueryUserCouponsResultV2.

        创建时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :param create_time: The create_time of this IQueryUserCouponsResultV2.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def coupon_version(self):
        """Gets the coupon_version of this IQueryUserCouponsResultV2.

        优惠券版本： 1：老版本，老版本优惠券只能使用一次2：新版本，新版本优惠券可以反复使用

        :return: The coupon_version of this IQueryUserCouponsResultV2.
        :rtype: int
        """
        return self._coupon_version

    @coupon_version.setter
    def coupon_version(self, coupon_version):
        """Sets the coupon_version of this IQueryUserCouponsResultV2.

        优惠券版本： 1：老版本，老版本优惠券只能使用一次2：新版本，新版本优惠券可以反复使用

        :param coupon_version: The coupon_version of this IQueryUserCouponsResultV2.
        :type coupon_version: int
        """
        self._coupon_version = coupon_version

    @property
    def balance(self):
        """Gets the balance of this IQueryUserCouponsResultV2.

        优惠券余额。单位：元。 如果为老版本优惠券，该值为空。

        :return: The balance of this IQueryUserCouponsResultV2.
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this IQueryUserCouponsResultV2.

        优惠券余额。单位：元。 如果为老版本优惠券，该值为空。

        :param balance: The balance of this IQueryUserCouponsResultV2.
        :type balance: float
        """
        self._balance = balance

    @property
    def lock_order_id(self):
        """Gets the lock_order_id of this IQueryUserCouponsResultV2.

        锁定优惠券的订单ID。 如果为老版本优惠券，该值为空。

        :return: The lock_order_id of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._lock_order_id

    @lock_order_id.setter
    def lock_order_id(self, lock_order_id):
        """Sets the lock_order_id of this IQueryUserCouponsResultV2.

        锁定优惠券的订单ID。 如果为老版本优惠券，该值为空。

        :param lock_order_id: The lock_order_id of this IQueryUserCouponsResultV2.
        :type lock_order_id: str
        """
        self._lock_order_id = lock_order_id

    @property
    def coupon_usage(self):
        """Gets the coupon_usage of this IQueryUserCouponsResultV2.

        优惠券用途。

        :return: The coupon_usage of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._coupon_usage

    @coupon_usage.setter
    def coupon_usage(self, coupon_usage):
        """Sets the coupon_usage of this IQueryUserCouponsResultV2.

        优惠券用途。

        :param coupon_usage: The coupon_usage of this IQueryUserCouponsResultV2.
        :type coupon_usage: str
        """
        self._coupon_usage = coupon_usage

    @property
    def is_frozen(self):
        """Gets the is_frozen of this IQueryUserCouponsResultV2.

        优惠券是否冻结： 0：否1：是

        :return: The is_frozen of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._is_frozen

    @is_frozen.setter
    def is_frozen(self, is_frozen):
        """Sets the is_frozen of this IQueryUserCouponsResultV2.

        优惠券是否冻结： 0：否1：是

        :param is_frozen: The is_frozen of this IQueryUserCouponsResultV2.
        :type is_frozen: str
        """
        self._is_frozen = is_frozen

    @property
    def currency(self):
        """Gets the currency of this IQueryUserCouponsResultV2.

        币种。 USD：美元

        :return: The currency of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this IQueryUserCouponsResultV2.

        币种。 USD：美元

        :param currency: The currency of this IQueryUserCouponsResultV2.
        :type currency: str
        """
        self._currency = currency

    @property
    def extend_param1(self):
        """Gets the extend_param1 of this IQueryUserCouponsResultV2.

        扩展字段。

        :return: The extend_param1 of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._extend_param1

    @extend_param1.setter
    def extend_param1(self, extend_param1):
        """Sets the extend_param1 of this IQueryUserCouponsResultV2.

        扩展字段。

        :param extend_param1: The extend_param1 of this IQueryUserCouponsResultV2.
        :type extend_param1: str
        """
        self._extend_param1 = extend_param1

    @property
    def source_id(self):
        """Gets the source_id of this IQueryUserCouponsResultV2.

        发券来源。 如果是合作伙伴发送的券，此处为伙伴ID。如果是活动发券，此处为活动ID：云豆兑换优惠券：云豆计划ID累计送优惠券：累计送计划ID抽奖送优惠券：抽奖计划ID事件送优惠券：事件计划ID定制优惠券：创建人ID

        :return: The source_id of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this IQueryUserCouponsResultV2.

        发券来源。 如果是合作伙伴发送的券，此处为伙伴ID。如果是活动发券，此处为活动ID：云豆兑换优惠券：云豆计划ID累计送优惠券：累计送计划ID抽奖送优惠券：抽奖计划ID事件送优惠券：事件计划ID定制优惠券：创建人ID

        :param source_id: The source_id of this IQueryUserCouponsResultV2.
        :type source_id: str
        """
        self._source_id = source_id

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
        if not isinstance(other, IQueryUserCouponsResultV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
