# coding: utf-8

import pprint
import re

import six





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
        'face_value': 'float',
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
        'balance': 'float',
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
        """IQueryUserPartnerCouponsResultV2 - a model defined in huaweicloud sdk"""
        
        

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

        |参数名称：优惠券实例ID。| |参数约束及描述：优惠券实例ID。|

        :return: The coupon_id of this IQueryUserPartnerCouponsResultV2.
        :rtype: str
        """
        return self._coupon_id

    @coupon_id.setter
    def coupon_id(self, coupon_id):
        """Sets the coupon_id of this IQueryUserPartnerCouponsResultV2.

        |参数名称：优惠券实例ID。| |参数约束及描述：优惠券实例ID。|

        :param coupon_id: The coupon_id of this IQueryUserPartnerCouponsResultV2.
        :type: str
        """
        self._coupon_id = coupon_id

    @property
    def status(self):
        """Gets the status of this IQueryUserPartnerCouponsResultV2.

        |参数名称：优惠券状态：1：未激活；2：待使用；3：已使用；4：已过期。| |参数的约束及描述：优惠券状态：1：未激活；2：待使用；3：已使用；4：已过期。|

        :return: The status of this IQueryUserPartnerCouponsResultV2.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IQueryUserPartnerCouponsResultV2.

        |参数名称：优惠券状态：1：未激活；2：待使用；3：已使用；4：已过期。| |参数的约束及描述：优惠券状态：1：未激活；2：待使用；3：已使用；4：已过期。|

        :param status: The status of this IQueryUserPartnerCouponsResultV2.
        :type: int
        """
        self._status = status

    @property
    def customer_id(self):
        """Gets the customer_id of this IQueryUserPartnerCouponsResultV2.

        |参数名称：客户ID| |参数约束及描述：客户ID|

        :return: The customer_id of this IQueryUserPartnerCouponsResultV2.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this IQueryUserPartnerCouponsResultV2.

        |参数名称：客户ID| |参数约束及描述：客户ID|

        :param customer_id: The customer_id of this IQueryUserPartnerCouponsResultV2.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def coupon_type(self):
        """Gets the coupon_type of this IQueryUserPartnerCouponsResultV2.

        |参数名称：优惠券类型：1：代金券；4：现金券。| |参数的约束及描述：优惠券类型：1：代金券；4：现金券。|

        :return: The coupon_type of this IQueryUserPartnerCouponsResultV2.
        :rtype: int
        """
        return self._coupon_type

    @coupon_type.setter
    def coupon_type(self, coupon_type):
        """Sets the coupon_type of this IQueryUserPartnerCouponsResultV2.

        |参数名称：优惠券类型：1：代金券；4：现金券。| |参数的约束及描述：优惠券类型：1：代金券；4：现金券。|

        :param coupon_type: The coupon_type of this IQueryUserPartnerCouponsResultV2.
        :type: int
        """
        self._coupon_type = coupon_type

    @property
    def measure_id(self):
        """Gets the measure_id of this IQueryUserPartnerCouponsResultV2.

        |参数名称：度量单位。1：元| |参数的约束及描述：度量单位。1：元|

        :return: The measure_id of this IQueryUserPartnerCouponsResultV2.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this IQueryUserPartnerCouponsResultV2.

        |参数名称：度量单位。1：元| |参数的约束及描述：度量单位。1：元|

        :param measure_id: The measure_id of this IQueryUserPartnerCouponsResultV2.
        :type: int
        """
        self._measure_id = measure_id

    @property
    def face_value(self):
        """Gets the face_value of this IQueryUserPartnerCouponsResultV2.

        |参数名称：优惠券金额。| |参数的约束及描述：优惠券金额。|

        :return: The face_value of this IQueryUserPartnerCouponsResultV2.
        :rtype: float
        """
        return self._face_value

    @face_value.setter
    def face_value(self, face_value):
        """Sets the face_value of this IQueryUserPartnerCouponsResultV2.

        |参数名称：优惠券金额。| |参数的约束及描述：优惠券金额。|

        :param face_value: The face_value of this IQueryUserPartnerCouponsResultV2.
        :type: float
        """
        self._face_value = face_value

    @property
    def effective_time(self):
        """Gets the effective_time of this IQueryUserPartnerCouponsResultV2.

        |参数名称：生效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ| |参数约束及描述：生效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :return: The effective_time of this IQueryUserPartnerCouponsResultV2.
        :rtype: str
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        """Sets the effective_time of this IQueryUserPartnerCouponsResultV2.

        |参数名称：生效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ| |参数约束及描述：生效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :param effective_time: The effective_time of this IQueryUserPartnerCouponsResultV2.
        :type: str
        """
        self._effective_time = effective_time

    @property
    def expire_time(self):
        """Gets the expire_time of this IQueryUserPartnerCouponsResultV2.

        |参数名称：失效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ| |参数约束及描述：失效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :return: The expire_time of this IQueryUserPartnerCouponsResultV2.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this IQueryUserPartnerCouponsResultV2.

        |参数名称：失效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ| |参数约束及描述：失效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :param expire_time: The expire_time of this IQueryUserPartnerCouponsResultV2.
        :type: str
        """
        self._expire_time = expire_time

    @property
    def order_id(self):
        """Gets the order_id of this IQueryUserPartnerCouponsResultV2.

        |参数名称：订单ID。| |参数约束及描述：订单ID。|

        :return: The order_id of this IQueryUserPartnerCouponsResultV2.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this IQueryUserPartnerCouponsResultV2.

        |参数名称：订单ID。| |参数约束及描述：订单ID。|

        :param order_id: The order_id of this IQueryUserPartnerCouponsResultV2.
        :type: str
        """
        self._order_id = order_id

    @property
    def promotion_plan_id(self):
        """Gets the promotion_plan_id of this IQueryUserPartnerCouponsResultV2.

        |参数名称：促销计划ID。| |参数约束及描述：促销计划ID。|

        :return: The promotion_plan_id of this IQueryUserPartnerCouponsResultV2.
        :rtype: str
        """
        return self._promotion_plan_id

    @promotion_plan_id.setter
    def promotion_plan_id(self, promotion_plan_id):
        """Sets the promotion_plan_id of this IQueryUserPartnerCouponsResultV2.

        |参数名称：促销计划ID。| |参数约束及描述：促销计划ID。|

        :param promotion_plan_id: The promotion_plan_id of this IQueryUserPartnerCouponsResultV2.
        :type: str
        """
        self._promotion_plan_id = promotion_plan_id

    @property
    def promotion_plan_name(self):
        """Gets the promotion_plan_name of this IQueryUserPartnerCouponsResultV2.

        |参数名称：促销计划名称。| |参数约束及描述：促销计划名称。|

        :return: The promotion_plan_name of this IQueryUserPartnerCouponsResultV2.
        :rtype: str
        """
        return self._promotion_plan_name

    @promotion_plan_name.setter
    def promotion_plan_name(self, promotion_plan_name):
        """Sets the promotion_plan_name of this IQueryUserPartnerCouponsResultV2.

        |参数名称：促销计划名称。| |参数约束及描述：促销计划名称。|

        :param promotion_plan_name: The promotion_plan_name of this IQueryUserPartnerCouponsResultV2.
        :type: str
        """
        self._promotion_plan_name = promotion_plan_name

    @property
    def promotion_plan_desc(self):
        """Gets the promotion_plan_desc of this IQueryUserPartnerCouponsResultV2.

        |参数名称：促销计划描述。| |参数约束及描述：促销计划描述。|

        :return: The promotion_plan_desc of this IQueryUserPartnerCouponsResultV2.
        :rtype: str
        """
        return self._promotion_plan_desc

    @promotion_plan_desc.setter
    def promotion_plan_desc(self, promotion_plan_desc):
        """Sets the promotion_plan_desc of this IQueryUserPartnerCouponsResultV2.

        |参数名称：促销计划描述。| |参数约束及描述：促销计划描述。|

        :param promotion_plan_desc: The promotion_plan_desc of this IQueryUserPartnerCouponsResultV2.
        :type: str
        """
        self._promotion_plan_desc = promotion_plan_desc

    @property
    def media_type(self):
        """Gets the media_type of this IQueryUserPartnerCouponsResultV2.

        |参数名称：介质类型。| |参数的约束及描述：介质类型。|

        :return: The media_type of this IQueryUserPartnerCouponsResultV2.
        :rtype: int
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this IQueryUserPartnerCouponsResultV2.

        |参数名称：介质类型。| |参数的约束及描述：介质类型。|

        :param media_type: The media_type of this IQueryUserPartnerCouponsResultV2.
        :type: int
        """
        self._media_type = media_type

    @property
    def fetch_method(self):
        """Gets the fetch_method of this IQueryUserPartnerCouponsResultV2.

        |参数名称：获取方式：1：线上领取；2：线上兑换；3：线上发放；4：线下获取；5：事件赠送。| |参数的约束及描述：获取方式：1：线上领取；2：线上兑换；3：线上发放；4：线下获取；5：事件赠送。|

        :return: The fetch_method of this IQueryUserPartnerCouponsResultV2.
        :rtype: int
        """
        return self._fetch_method

    @fetch_method.setter
    def fetch_method(self, fetch_method):
        """Sets the fetch_method of this IQueryUserPartnerCouponsResultV2.

        |参数名称：获取方式：1：线上领取；2：线上兑换；3：线上发放；4：线下获取；5：事件赠送。| |参数的约束及描述：获取方式：1：线上领取；2：线上兑换；3：线上发放；4：线下获取；5：事件赠送。|

        :param fetch_method: The fetch_method of this IQueryUserPartnerCouponsResultV2.
        :type: int
        """
        self._fetch_method = fetch_method

    @property
    def use_limits(self):
        """Gets the use_limits of this IQueryUserPartnerCouponsResultV2.

        |参数名称：优惠券使用限制。具体请参见表 ICouponUseLimitInfo。| |参数约束以及描述：优惠券使用限制。具体请参见表 ICouponUseLimitInfo。|

        :return: The use_limits of this IQueryUserPartnerCouponsResultV2.
        :rtype: list[ICouponUseLimitInfoV2]
        """
        return self._use_limits

    @use_limits.setter
    def use_limits(self, use_limits):
        """Sets the use_limits of this IQueryUserPartnerCouponsResultV2.

        |参数名称：优惠券使用限制。具体请参见表 ICouponUseLimitInfo。| |参数约束以及描述：优惠券使用限制。具体请参见表 ICouponUseLimitInfo。|

        :param use_limits: The use_limits of this IQueryUserPartnerCouponsResultV2.
        :type: list[ICouponUseLimitInfoV2]
        """
        self._use_limits = use_limits

    @property
    def active_time(self):
        """Gets the active_time of this IQueryUserPartnerCouponsResultV2.

        |参数名称：激活时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ| |参数约束及描述：激活时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :return: The active_time of this IQueryUserPartnerCouponsResultV2.
        :rtype: str
        """
        return self._active_time

    @active_time.setter
    def active_time(self, active_time):
        """Sets the active_time of this IQueryUserPartnerCouponsResultV2.

        |参数名称：激活时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ| |参数约束及描述：激活时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :param active_time: The active_time of this IQueryUserPartnerCouponsResultV2.
        :type: str
        """
        self._active_time = active_time

    @property
    def last_used_time(self):
        """Gets the last_used_time of this IQueryUserPartnerCouponsResultV2.

        |参数名称：使用时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ| |参数约束及描述：使用时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :return: The last_used_time of this IQueryUserPartnerCouponsResultV2.
        :rtype: str
        """
        return self._last_used_time

    @last_used_time.setter
    def last_used_time(self, last_used_time):
        """Sets the last_used_time of this IQueryUserPartnerCouponsResultV2.

        |参数名称：使用时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ| |参数约束及描述：使用时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :param last_used_time: The last_used_time of this IQueryUserPartnerCouponsResultV2.
        :type: str
        """
        self._last_used_time = last_used_time

    @property
    def promotion_id(self):
        """Gets the promotion_id of this IQueryUserPartnerCouponsResultV2.

        |参数名称：促销ID。| |参数约束及描述：促销ID。|

        :return: The promotion_id of this IQueryUserPartnerCouponsResultV2.
        :rtype: str
        """
        return self._promotion_id

    @promotion_id.setter
    def promotion_id(self, promotion_id):
        """Sets the promotion_id of this IQueryUserPartnerCouponsResultV2.

        |参数名称：促销ID。| |参数约束及描述：促销ID。|

        :param promotion_id: The promotion_id of this IQueryUserPartnerCouponsResultV2.
        :type: str
        """
        self._promotion_id = promotion_id

    @property
    def create_time(self):
        """Gets the create_time of this IQueryUserPartnerCouponsResultV2.

        |参数名称：创建时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ| |参数约束及描述：创建时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :return: The create_time of this IQueryUserPartnerCouponsResultV2.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this IQueryUserPartnerCouponsResultV2.

        |参数名称：创建时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ| |参数约束及描述：创建时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :param create_time: The create_time of this IQueryUserPartnerCouponsResultV2.
        :type: str
        """
        self._create_time = create_time

    @property
    def balance(self):
        """Gets the balance of this IQueryUserPartnerCouponsResultV2.

        |参数名称：余额。如果为老版本优惠券，该值为空| |参数的约束及描述：余额。如果为老版本优惠券，该值为空|

        :return: The balance of this IQueryUserPartnerCouponsResultV2.
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this IQueryUserPartnerCouponsResultV2.

        |参数名称：余额。如果为老版本优惠券，该值为空| |参数的约束及描述：余额。如果为老版本优惠券，该值为空|

        :param balance: The balance of this IQueryUserPartnerCouponsResultV2.
        :type: float
        """
        self._balance = balance

    @property
    def lock_order_id(self):
        """Gets the lock_order_id of this IQueryUserPartnerCouponsResultV2.

        |参数名称：锁定优惠券的订单ID。如果为老版本优惠券，该值为空。| |参数约束及描述：锁定优惠券的订单ID。如果为老版本优惠券，该值为空。|

        :return: The lock_order_id of this IQueryUserPartnerCouponsResultV2.
        :rtype: str
        """
        return self._lock_order_id

    @lock_order_id.setter
    def lock_order_id(self, lock_order_id):
        """Sets the lock_order_id of this IQueryUserPartnerCouponsResultV2.

        |参数名称：锁定优惠券的订单ID。如果为老版本优惠券，该值为空。| |参数约束及描述：锁定优惠券的订单ID。如果为老版本优惠券，该值为空。|

        :param lock_order_id: The lock_order_id of this IQueryUserPartnerCouponsResultV2.
        :type: str
        """
        self._lock_order_id = lock_order_id

    @property
    def is_frozen(self):
        """Gets the is_frozen of this IQueryUserPartnerCouponsResultV2.

        |参数名称：优惠券是否冻结：0：否1：是可用优惠券接口返回时不包括冻结状态的优惠券。| |参数约束及描述：优惠券是否冻结：0：否1：是可用优惠券接口返回时不包括冻结状态的优惠券。|

        :return: The is_frozen of this IQueryUserPartnerCouponsResultV2.
        :rtype: str
        """
        return self._is_frozen

    @is_frozen.setter
    def is_frozen(self, is_frozen):
        """Sets the is_frozen of this IQueryUserPartnerCouponsResultV2.

        |参数名称：优惠券是否冻结：0：否1：是可用优惠券接口返回时不包括冻结状态的优惠券。| |参数约束及描述：优惠券是否冻结：0：否1：是可用优惠券接口返回时不包括冻结状态的优惠券。|

        :param is_frozen: The is_frozen of this IQueryUserPartnerCouponsResultV2.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IQueryUserPartnerCouponsResultV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
