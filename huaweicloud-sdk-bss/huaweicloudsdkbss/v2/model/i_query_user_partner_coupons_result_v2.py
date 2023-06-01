# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IQueryUserPartnerCouponsResultV2:

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
        'status': 'int',
        'customer_id': 'str',
        'coupon_type': 'int',
        'measure_id': 'int',
        'face_value': 'decimal.Decimal',
        'effective_time': 'str',
        'expire_time': 'str',
        'order_id': 'str',
        'promotion_plan_id': 'str',
        'promotion_plan_name': 'str',
        'promotion_plan_desc': 'str',
        'media_type': 'int',
        'fetch_method': 'int',
        'use_limits': 'list[ICouponUseLimitInfoV2]',
        'active_time': 'str',
        'last_used_time': 'str',
        'promotion_id': 'str',
        'create_time': 'str',
        'balance': 'decimal.Decimal',
        'lock_order_id': 'str',
        'is_frozen': 'str'
    }

    attribute_map = {
        'coupon_id': 'coupon_id',
        'status': 'status',
        'customer_id': 'customer_id',
        'coupon_type': 'coupon_type',
        'measure_id': 'measure_id',
        'face_value': 'face_value',
        'effective_time': 'effective_time',
        'expire_time': 'expire_time',
        'order_id': 'order_id',
        'promotion_plan_id': 'promotion_plan_id',
        'promotion_plan_name': 'promotion_plan_name',
        'promotion_plan_desc': 'promotion_plan_desc',
        'media_type': 'media_type',
        'fetch_method': 'fetch_method',
        'use_limits': 'use_limits',
        'active_time': 'active_time',
        'last_used_time': 'last_used_time',
        'promotion_id': 'promotion_id',
        'create_time': 'create_time',
        'balance': 'balance',
        'lock_order_id': 'lock_order_id',
        'is_frozen': 'is_frozen'
    }

    def __init__(self, coupon_id=None, status=None, customer_id=None, coupon_type=None, measure_id=None, face_value=None, effective_time=None, expire_time=None, order_id=None, promotion_plan_id=None, promotion_plan_name=None, promotion_plan_desc=None, media_type=None, fetch_method=None, use_limits=None, active_time=None, last_used_time=None, promotion_id=None, create_time=None, balance=None, lock_order_id=None, is_frozen=None):
        """IQueryUserPartnerCouponsResultV2

        The model defined in huaweicloud sdk

        :param coupon_id: 优惠券ID。
        :type coupon_id: str
        :param status: 优惠券状态： 1：未激活2：可使用3：已使用4：已过期5：已回收
        :type status: int
        :param customer_id: 客户账号ID。
        :type customer_id: str
        :param coupon_type: 优惠券类别： 1：代金券4：现金券
        :type coupon_type: int
        :param measure_id: 优惠券面额单位。 1：元。
        :type measure_id: int
        :param face_value: 优惠券面值。
        :type face_value: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param effective_time: 生效时间。 UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”。
        :type effective_time: str
        :param expire_time: 失效时间。 UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”。
        :type expire_time: str
        :param order_id: 订单ID。
        :type order_id: str
        :param promotion_plan_id: 促销计划ID。
        :type promotion_plan_id: str
        :param promotion_plan_name: 促销计划名称。
        :type promotion_plan_name: str
        :param promotion_plan_desc: 促销计划描述。
        :type promotion_plan_desc: str
        :param media_type: 介质类型。 1：电子券2：纸质券
        :type media_type: int
        :param fetch_method: 获取方式。 1：线上领取2：线上兑换3：线上发放4：线下获取5：事件赠送
        :type fetch_method: int
        :param use_limits: 优惠券限制。 具体请参见表3。
        :type use_limits: list[:class:`huaweicloudsdkbss.v2.ICouponUseLimitInfoV2`]
        :param active_time: 优惠券的激活时间。
        :type active_time: str
        :param last_used_time: 优惠券的使用时间。
        :type last_used_time: str
        :param promotion_id: 促销活动ID。
        :type promotion_id: str
        :param create_time: 优惠券的创建时间。
        :type create_time: str
        :param balance: 优惠券余额。
        :type balance: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param lock_order_id: 锁定优惠券的订单ID。 如果为老版本优惠券，该值为空。
        :type lock_order_id: str
        :param is_frozen: 优惠券是否冻结。 0：否1：是 可用优惠券接口返回时不包括冻结状态的优惠券。
        :type is_frozen: str
        """
        
        

        self._coupon_id = None
        self._status = None
        self._customer_id = None
        self._coupon_type = None
        self._measure_id = None
        self._face_value = None
        self._effective_time = None
        self._expire_time = None
        self._order_id = None
        self._promotion_plan_id = None
        self._promotion_plan_name = None
        self._promotion_plan_desc = None
        self._media_type = None
        self._fetch_method = None
        self._use_limits = None
        self._active_time = None
        self._last_used_time = None
        self._promotion_id = None
        self._create_time = None
        self._balance = None
        self._lock_order_id = None
        self._is_frozen = None
        self.discriminator = None

        if coupon_id is not None:
            self.coupon_id = coupon_id
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
        if effective_time is not None:
            self.effective_time = effective_time
        if expire_time is not None:
            self.expire_time = expire_time
        if order_id is not None:
            self.order_id = order_id
        if promotion_plan_id is not None:
            self.promotion_plan_id = promotion_plan_id
        if promotion_plan_name is not None:
            self.promotion_plan_name = promotion_plan_name
        if promotion_plan_desc is not None:
            self.promotion_plan_desc = promotion_plan_desc
        if media_type is not None:
            self.media_type = media_type
        if fetch_method is not None:
            self.fetch_method = fetch_method
        if use_limits is not None:
            self.use_limits = use_limits
        if active_time is not None:
            self.active_time = active_time
        if last_used_time is not None:
            self.last_used_time = last_used_time
        if promotion_id is not None:
            self.promotion_id = promotion_id
        if create_time is not None:
            self.create_time = create_time
        if balance is not None:
            self.balance = balance
        if lock_order_id is not None:
            self.lock_order_id = lock_order_id
        if is_frozen is not None:
            self.is_frozen = is_frozen

    @property
    def coupon_id(self):
        """Gets the coupon_id of this IQueryUserPartnerCouponsResultV2.

        优惠券ID。

        :return: The coupon_id of this IQueryUserPartnerCouponsResultV2.
        :rtype: str
        """
        return self._coupon_id

    @coupon_id.setter
    def coupon_id(self, coupon_id):
        """Sets the coupon_id of this IQueryUserPartnerCouponsResultV2.

        优惠券ID。

        :param coupon_id: The coupon_id of this IQueryUserPartnerCouponsResultV2.
        :type coupon_id: str
        """
        self._coupon_id = coupon_id

    @property
    def status(self):
        """Gets the status of this IQueryUserPartnerCouponsResultV2.

        优惠券状态： 1：未激活2：可使用3：已使用4：已过期5：已回收

        :return: The status of this IQueryUserPartnerCouponsResultV2.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IQueryUserPartnerCouponsResultV2.

        优惠券状态： 1：未激活2：可使用3：已使用4：已过期5：已回收

        :param status: The status of this IQueryUserPartnerCouponsResultV2.
        :type status: int
        """
        self._status = status

    @property
    def customer_id(self):
        """Gets the customer_id of this IQueryUserPartnerCouponsResultV2.

        客户账号ID。

        :return: The customer_id of this IQueryUserPartnerCouponsResultV2.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this IQueryUserPartnerCouponsResultV2.

        客户账号ID。

        :param customer_id: The customer_id of this IQueryUserPartnerCouponsResultV2.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def coupon_type(self):
        """Gets the coupon_type of this IQueryUserPartnerCouponsResultV2.

        优惠券类别： 1：代金券4：现金券

        :return: The coupon_type of this IQueryUserPartnerCouponsResultV2.
        :rtype: int
        """
        return self._coupon_type

    @coupon_type.setter
    def coupon_type(self, coupon_type):
        """Sets the coupon_type of this IQueryUserPartnerCouponsResultV2.

        优惠券类别： 1：代金券4：现金券

        :param coupon_type: The coupon_type of this IQueryUserPartnerCouponsResultV2.
        :type coupon_type: int
        """
        self._coupon_type = coupon_type

    @property
    def measure_id(self):
        """Gets the measure_id of this IQueryUserPartnerCouponsResultV2.

        优惠券面额单位。 1：元。

        :return: The measure_id of this IQueryUserPartnerCouponsResultV2.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this IQueryUserPartnerCouponsResultV2.

        优惠券面额单位。 1：元。

        :param measure_id: The measure_id of this IQueryUserPartnerCouponsResultV2.
        :type measure_id: int
        """
        self._measure_id = measure_id

    @property
    def face_value(self):
        """Gets the face_value of this IQueryUserPartnerCouponsResultV2.

        优惠券面值。

        :return: The face_value of this IQueryUserPartnerCouponsResultV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._face_value

    @face_value.setter
    def face_value(self, face_value):
        """Sets the face_value of this IQueryUserPartnerCouponsResultV2.

        优惠券面值。

        :param face_value: The face_value of this IQueryUserPartnerCouponsResultV2.
        :type face_value: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._face_value = face_value

    @property
    def effective_time(self):
        """Gets the effective_time of this IQueryUserPartnerCouponsResultV2.

        生效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :return: The effective_time of this IQueryUserPartnerCouponsResultV2.
        :rtype: str
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        """Sets the effective_time of this IQueryUserPartnerCouponsResultV2.

        生效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :param effective_time: The effective_time of this IQueryUserPartnerCouponsResultV2.
        :type effective_time: str
        """
        self._effective_time = effective_time

    @property
    def expire_time(self):
        """Gets the expire_time of this IQueryUserPartnerCouponsResultV2.

        失效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :return: The expire_time of this IQueryUserPartnerCouponsResultV2.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this IQueryUserPartnerCouponsResultV2.

        失效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :param expire_time: The expire_time of this IQueryUserPartnerCouponsResultV2.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def order_id(self):
        """Gets the order_id of this IQueryUserPartnerCouponsResultV2.

        订单ID。

        :return: The order_id of this IQueryUserPartnerCouponsResultV2.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this IQueryUserPartnerCouponsResultV2.

        订单ID。

        :param order_id: The order_id of this IQueryUserPartnerCouponsResultV2.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def promotion_plan_id(self):
        """Gets the promotion_plan_id of this IQueryUserPartnerCouponsResultV2.

        促销计划ID。

        :return: The promotion_plan_id of this IQueryUserPartnerCouponsResultV2.
        :rtype: str
        """
        return self._promotion_plan_id

    @promotion_plan_id.setter
    def promotion_plan_id(self, promotion_plan_id):
        """Sets the promotion_plan_id of this IQueryUserPartnerCouponsResultV2.

        促销计划ID。

        :param promotion_plan_id: The promotion_plan_id of this IQueryUserPartnerCouponsResultV2.
        :type promotion_plan_id: str
        """
        self._promotion_plan_id = promotion_plan_id

    @property
    def promotion_plan_name(self):
        """Gets the promotion_plan_name of this IQueryUserPartnerCouponsResultV2.

        促销计划名称。

        :return: The promotion_plan_name of this IQueryUserPartnerCouponsResultV2.
        :rtype: str
        """
        return self._promotion_plan_name

    @promotion_plan_name.setter
    def promotion_plan_name(self, promotion_plan_name):
        """Sets the promotion_plan_name of this IQueryUserPartnerCouponsResultV2.

        促销计划名称。

        :param promotion_plan_name: The promotion_plan_name of this IQueryUserPartnerCouponsResultV2.
        :type promotion_plan_name: str
        """
        self._promotion_plan_name = promotion_plan_name

    @property
    def promotion_plan_desc(self):
        """Gets the promotion_plan_desc of this IQueryUserPartnerCouponsResultV2.

        促销计划描述。

        :return: The promotion_plan_desc of this IQueryUserPartnerCouponsResultV2.
        :rtype: str
        """
        return self._promotion_plan_desc

    @promotion_plan_desc.setter
    def promotion_plan_desc(self, promotion_plan_desc):
        """Sets the promotion_plan_desc of this IQueryUserPartnerCouponsResultV2.

        促销计划描述。

        :param promotion_plan_desc: The promotion_plan_desc of this IQueryUserPartnerCouponsResultV2.
        :type promotion_plan_desc: str
        """
        self._promotion_plan_desc = promotion_plan_desc

    @property
    def media_type(self):
        """Gets the media_type of this IQueryUserPartnerCouponsResultV2.

        介质类型。 1：电子券2：纸质券

        :return: The media_type of this IQueryUserPartnerCouponsResultV2.
        :rtype: int
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this IQueryUserPartnerCouponsResultV2.

        介质类型。 1：电子券2：纸质券

        :param media_type: The media_type of this IQueryUserPartnerCouponsResultV2.
        :type media_type: int
        """
        self._media_type = media_type

    @property
    def fetch_method(self):
        """Gets the fetch_method of this IQueryUserPartnerCouponsResultV2.

        获取方式。 1：线上领取2：线上兑换3：线上发放4：线下获取5：事件赠送

        :return: The fetch_method of this IQueryUserPartnerCouponsResultV2.
        :rtype: int
        """
        return self._fetch_method

    @fetch_method.setter
    def fetch_method(self, fetch_method):
        """Sets the fetch_method of this IQueryUserPartnerCouponsResultV2.

        获取方式。 1：线上领取2：线上兑换3：线上发放4：线下获取5：事件赠送

        :param fetch_method: The fetch_method of this IQueryUserPartnerCouponsResultV2.
        :type fetch_method: int
        """
        self._fetch_method = fetch_method

    @property
    def use_limits(self):
        """Gets the use_limits of this IQueryUserPartnerCouponsResultV2.

        优惠券限制。 具体请参见表3。

        :return: The use_limits of this IQueryUserPartnerCouponsResultV2.
        :rtype: list[:class:`huaweicloudsdkbss.v2.ICouponUseLimitInfoV2`]
        """
        return self._use_limits

    @use_limits.setter
    def use_limits(self, use_limits):
        """Sets the use_limits of this IQueryUserPartnerCouponsResultV2.

        优惠券限制。 具体请参见表3。

        :param use_limits: The use_limits of this IQueryUserPartnerCouponsResultV2.
        :type use_limits: list[:class:`huaweicloudsdkbss.v2.ICouponUseLimitInfoV2`]
        """
        self._use_limits = use_limits

    @property
    def active_time(self):
        """Gets the active_time of this IQueryUserPartnerCouponsResultV2.

        优惠券的激活时间。

        :return: The active_time of this IQueryUserPartnerCouponsResultV2.
        :rtype: str
        """
        return self._active_time

    @active_time.setter
    def active_time(self, active_time):
        """Sets the active_time of this IQueryUserPartnerCouponsResultV2.

        优惠券的激活时间。

        :param active_time: The active_time of this IQueryUserPartnerCouponsResultV2.
        :type active_time: str
        """
        self._active_time = active_time

    @property
    def last_used_time(self):
        """Gets the last_used_time of this IQueryUserPartnerCouponsResultV2.

        优惠券的使用时间。

        :return: The last_used_time of this IQueryUserPartnerCouponsResultV2.
        :rtype: str
        """
        return self._last_used_time

    @last_used_time.setter
    def last_used_time(self, last_used_time):
        """Sets the last_used_time of this IQueryUserPartnerCouponsResultV2.

        优惠券的使用时间。

        :param last_used_time: The last_used_time of this IQueryUserPartnerCouponsResultV2.
        :type last_used_time: str
        """
        self._last_used_time = last_used_time

    @property
    def promotion_id(self):
        """Gets the promotion_id of this IQueryUserPartnerCouponsResultV2.

        促销活动ID。

        :return: The promotion_id of this IQueryUserPartnerCouponsResultV2.
        :rtype: str
        """
        return self._promotion_id

    @promotion_id.setter
    def promotion_id(self, promotion_id):
        """Sets the promotion_id of this IQueryUserPartnerCouponsResultV2.

        促销活动ID。

        :param promotion_id: The promotion_id of this IQueryUserPartnerCouponsResultV2.
        :type promotion_id: str
        """
        self._promotion_id = promotion_id

    @property
    def create_time(self):
        """Gets the create_time of this IQueryUserPartnerCouponsResultV2.

        优惠券的创建时间。

        :return: The create_time of this IQueryUserPartnerCouponsResultV2.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this IQueryUserPartnerCouponsResultV2.

        优惠券的创建时间。

        :param create_time: The create_time of this IQueryUserPartnerCouponsResultV2.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def balance(self):
        """Gets the balance of this IQueryUserPartnerCouponsResultV2.

        优惠券余额。

        :return: The balance of this IQueryUserPartnerCouponsResultV2.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this IQueryUserPartnerCouponsResultV2.

        优惠券余额。

        :param balance: The balance of this IQueryUserPartnerCouponsResultV2.
        :type balance: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._balance = balance

    @property
    def lock_order_id(self):
        """Gets the lock_order_id of this IQueryUserPartnerCouponsResultV2.

        锁定优惠券的订单ID。 如果为老版本优惠券，该值为空。

        :return: The lock_order_id of this IQueryUserPartnerCouponsResultV2.
        :rtype: str
        """
        return self._lock_order_id

    @lock_order_id.setter
    def lock_order_id(self, lock_order_id):
        """Sets the lock_order_id of this IQueryUserPartnerCouponsResultV2.

        锁定优惠券的订单ID。 如果为老版本优惠券，该值为空。

        :param lock_order_id: The lock_order_id of this IQueryUserPartnerCouponsResultV2.
        :type lock_order_id: str
        """
        self._lock_order_id = lock_order_id

    @property
    def is_frozen(self):
        """Gets the is_frozen of this IQueryUserPartnerCouponsResultV2.

        优惠券是否冻结。 0：否1：是 可用优惠券接口返回时不包括冻结状态的优惠券。

        :return: The is_frozen of this IQueryUserPartnerCouponsResultV2.
        :rtype: str
        """
        return self._is_frozen

    @is_frozen.setter
    def is_frozen(self, is_frozen):
        """Sets the is_frozen of this IQueryUserPartnerCouponsResultV2.

        优惠券是否冻结。 0：否1：是 可用优惠券接口返回时不包括冻结状态的优惠券。

        :param is_frozen: The is_frozen of this IQueryUserPartnerCouponsResultV2.
        :type is_frozen: str
        """
        self._is_frozen = is_frozen

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
        if not isinstance(other, IQueryUserPartnerCouponsResultV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
