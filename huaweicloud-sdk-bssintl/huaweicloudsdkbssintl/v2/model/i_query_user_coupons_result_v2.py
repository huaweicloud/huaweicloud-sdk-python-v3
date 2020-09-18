# coding: utf-8

import pprint
import re

import six





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
        """IQueryUserCouponsResultV2 - a model defined in huaweicloud sdk"""
        
        

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

        |参数名称：优惠券实例ID。| |参数约束及描述：优惠券实例ID。|

        :return: The coupon_id of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._coupon_id

    @coupon_id.setter
    def coupon_id(self, coupon_id):
        """Sets the coupon_id of this IQueryUserCouponsResultV2.

        |参数名称：优惠券实例ID。| |参数约束及描述：优惠券实例ID。|

        :param coupon_id: The coupon_id of this IQueryUserCouponsResultV2.
        :type: str
        """
        self._coupon_id = coupon_id

    @property
    def coupon_code(self):
        """Gets the coupon_code of this IQueryUserCouponsResultV2.

        |参数名称：优惠券编码。| |参数约束及描述：优惠券编码。|

        :return: The coupon_code of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._coupon_code

    @coupon_code.setter
    def coupon_code(self, coupon_code):
        """Sets the coupon_code of this IQueryUserCouponsResultV2.

        |参数名称：优惠券编码。| |参数约束及描述：优惠券编码。|

        :param coupon_code: The coupon_code of this IQueryUserCouponsResultV2.
        :type: str
        """
        self._coupon_code = coupon_code

    @property
    def status(self):
        """Gets the status of this IQueryUserCouponsResultV2.

        |参数名称：优惠券状态：1：未激活；2：待使用；3：已使用；4：已过期。| |参数的约束及描述：优惠券状态：1：未激活；2：待使用；3：已使用；4：已过期。|

        :return: The status of this IQueryUserCouponsResultV2.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IQueryUserCouponsResultV2.

        |参数名称：优惠券状态：1：未激活；2：待使用；3：已使用；4：已过期。| |参数的约束及描述：优惠券状态：1：未激活；2：待使用；3：已使用；4：已过期。|

        :param status: The status of this IQueryUserCouponsResultV2.
        :type: int
        """
        self._status = status

    @property
    def customer_id(self):
        """Gets the customer_id of this IQueryUserCouponsResultV2.

        |参数名称：客户ID| |参数约束及描述：客户ID|

        :return: The customer_id of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this IQueryUserCouponsResultV2.

        |参数名称：客户ID| |参数约束及描述：客户ID|

        :param customer_id: The customer_id of this IQueryUserCouponsResultV2.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def coupon_type(self):
        """Gets the coupon_type of this IQueryUserCouponsResultV2.

        |参数名称：优惠券类型：1：代金券；2：折扣券；3：产品券；4：现金券。| |参数的约束及描述：优惠券类型：1：代金券；2：折扣券；3：产品券；4：现金券。|

        :return: The coupon_type of this IQueryUserCouponsResultV2.
        :rtype: int
        """
        return self._coupon_type

    @coupon_type.setter
    def coupon_type(self, coupon_type):
        """Sets the coupon_type of this IQueryUserCouponsResultV2.

        |参数名称：优惠券类型：1：代金券；2：折扣券；3：产品券；4：现金券。| |参数的约束及描述：优惠券类型：1：代金券；2：折扣券；3：产品券；4：现金券。|

        :param coupon_type: The coupon_type of this IQueryUserCouponsResultV2.
        :type: int
        """
        self._coupon_type = coupon_type

    @property
    def measure_id(self):
        """Gets the measure_id of this IQueryUserCouponsResultV2.

        |参数名称：度量单位。1：元| |参数的约束及描述：度量单位。1：元|

        :return: The measure_id of this IQueryUserCouponsResultV2.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this IQueryUserCouponsResultV2.

        |参数名称：度量单位。1：元| |参数的约束及描述：度量单位。1：元|

        :param measure_id: The measure_id of this IQueryUserCouponsResultV2.
        :type: int
        """
        self._measure_id = measure_id

    @property
    def face_value(self):
        """Gets the face_value of this IQueryUserCouponsResultV2.

        |参数名称：优惠券金额。| |参数的约束及描述：优惠券金额。|

        :return: The face_value of this IQueryUserCouponsResultV2.
        :rtype: float
        """
        return self._face_value

    @face_value.setter
    def face_value(self, face_value):
        """Sets the face_value of this IQueryUserCouponsResultV2.

        |参数名称：优惠券金额。| |参数的约束及描述：优惠券金额。|

        :param face_value: The face_value of this IQueryUserCouponsResultV2.
        :type: float
        """
        self._face_value = face_value

    @property
    def valid_time(self):
        """Gets the valid_time of this IQueryUserCouponsResultV2.

        |参数名称：生效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ| |参数约束及描述：生效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :return: The valid_time of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._valid_time

    @valid_time.setter
    def valid_time(self, valid_time):
        """Sets the valid_time of this IQueryUserCouponsResultV2.

        |参数名称：生效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ| |参数约束及描述：生效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :param valid_time: The valid_time of this IQueryUserCouponsResultV2.
        :type: str
        """
        self._valid_time = valid_time

    @property
    def expire_time(self):
        """Gets the expire_time of this IQueryUserCouponsResultV2.

        |参数名称：失效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ| |参数约束及描述：失效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :return: The expire_time of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this IQueryUserCouponsResultV2.

        |参数名称：失效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ| |参数约束及描述：失效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :param expire_time: The expire_time of this IQueryUserCouponsResultV2.
        :type: str
        """
        self._expire_time = expire_time

    @property
    def order_id(self):
        """Gets the order_id of this IQueryUserCouponsResultV2.

        |参数名称：订单ID。| |参数约束及描述：订单ID。|

        :return: The order_id of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this IQueryUserCouponsResultV2.

        |参数名称：订单ID。| |参数约束及描述：订单ID。|

        :param order_id: The order_id of this IQueryUserCouponsResultV2.
        :type: str
        """
        self._order_id = order_id

    @property
    def promotion_plan_id(self):
        """Gets the promotion_plan_id of this IQueryUserCouponsResultV2.

        |参数名称：促销计划ID。| |参数约束及描述：促销计划ID。|

        :return: The promotion_plan_id of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._promotion_plan_id

    @promotion_plan_id.setter
    def promotion_plan_id(self, promotion_plan_id):
        """Sets the promotion_plan_id of this IQueryUserCouponsResultV2.

        |参数名称：促销计划ID。| |参数约束及描述：促销计划ID。|

        :param promotion_plan_id: The promotion_plan_id of this IQueryUserCouponsResultV2.
        :type: str
        """
        self._promotion_plan_id = promotion_plan_id

    @property
    def plan_name(self):
        """Gets the plan_name of this IQueryUserCouponsResultV2.

        |参数名称：促销计划名称。| |参数约束及描述：促销计划名称。|

        :return: The plan_name of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._plan_name

    @plan_name.setter
    def plan_name(self, plan_name):
        """Sets the plan_name of this IQueryUserCouponsResultV2.

        |参数名称：促销计划名称。| |参数约束及描述：促销计划名称。|

        :param plan_name: The plan_name of this IQueryUserCouponsResultV2.
        :type: str
        """
        self._plan_name = plan_name

    @property
    def plan_desc(self):
        """Gets the plan_desc of this IQueryUserCouponsResultV2.

        |参数名称：促销计划描述。| |参数约束及描述：促销计划描述。|

        :return: The plan_desc of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._plan_desc

    @plan_desc.setter
    def plan_desc(self, plan_desc):
        """Sets the plan_desc of this IQueryUserCouponsResultV2.

        |参数名称：促销计划描述。| |参数约束及描述：促销计划描述。|

        :param plan_desc: The plan_desc of this IQueryUserCouponsResultV2.
        :type: str
        """
        self._plan_desc = plan_desc

    @property
    def media_type(self):
        """Gets the media_type of this IQueryUserCouponsResultV2.

        |参数名称：介质类型。| |参数的约束及描述：介质类型。|

        :return: The media_type of this IQueryUserCouponsResultV2.
        :rtype: int
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this IQueryUserCouponsResultV2.

        |参数名称：介质类型。| |参数的约束及描述：介质类型。|

        :param media_type: The media_type of this IQueryUserCouponsResultV2.
        :type: int
        """
        self._media_type = media_type

    @property
    def fetch_method(self):
        """Gets the fetch_method of this IQueryUserCouponsResultV2.

        |参数名称：获取方式：1：线上领取；2：线上兑换；3：线上发放；4：线下获取；5：事件赠送。| |参数的约束及描述：获取方式：1：线上领取；2：线上兑换；3：线上发放；4：线下获取；5：事件赠送。|

        :return: The fetch_method of this IQueryUserCouponsResultV2.
        :rtype: int
        """
        return self._fetch_method

    @fetch_method.setter
    def fetch_method(self, fetch_method):
        """Sets the fetch_method of this IQueryUserCouponsResultV2.

        |参数名称：获取方式：1：线上领取；2：线上兑换；3：线上发放；4：线下获取；5：事件赠送。| |参数的约束及描述：获取方式：1：线上领取；2：线上兑换；3：线上发放；4：线下获取；5：事件赠送。|

        :param fetch_method: The fetch_method of this IQueryUserCouponsResultV2.
        :type: int
        """
        self._fetch_method = fetch_method

    @property
    def use_limits(self):
        """Gets the use_limits of this IQueryUserCouponsResultV2.

        |参数名称：优惠券使用限制。具体请参见表 ICouponUseLimitInfo。| |参数约束以及描述：优惠券使用限制。具体请参见表 ICouponUseLimitInfo。|

        :return: The use_limits of this IQueryUserCouponsResultV2.
        :rtype: list[ICouponUseLimitInfoV2]
        """
        return self._use_limits

    @use_limits.setter
    def use_limits(self, use_limits):
        """Sets the use_limits of this IQueryUserCouponsResultV2.

        |参数名称：优惠券使用限制。具体请参见表 ICouponUseLimitInfo。| |参数约束以及描述：优惠券使用限制。具体请参见表 ICouponUseLimitInfo。|

        :param use_limits: The use_limits of this IQueryUserCouponsResultV2.
        :type: list[ICouponUseLimitInfoV2]
        """
        self._use_limits = use_limits

    @property
    def active_time(self):
        """Gets the active_time of this IQueryUserCouponsResultV2.

        |参数名称：激活时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ| |参数约束及描述：激活时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :return: The active_time of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._active_time

    @active_time.setter
    def active_time(self, active_time):
        """Sets the active_time of this IQueryUserCouponsResultV2.

        |参数名称：激活时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ| |参数约束及描述：激活时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :param active_time: The active_time of this IQueryUserCouponsResultV2.
        :type: str
        """
        self._active_time = active_time

    @property
    def reserve_time(self):
        """Gets the reserve_time of this IQueryUserCouponsResultV2.

        |参数名称：使用时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ| |参数约束及描述：使用时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :return: The reserve_time of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._reserve_time

    @reserve_time.setter
    def reserve_time(self, reserve_time):
        """Sets the reserve_time of this IQueryUserCouponsResultV2.

        |参数名称：使用时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ| |参数约束及描述：使用时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :param reserve_time: The reserve_time of this IQueryUserCouponsResultV2.
        :type: str
        """
        self._reserve_time = reserve_time

    @property
    def promotion_id(self):
        """Gets the promotion_id of this IQueryUserCouponsResultV2.

        |参数名称：促销ID。| |参数约束及描述：促销ID。|

        :return: The promotion_id of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._promotion_id

    @promotion_id.setter
    def promotion_id(self, promotion_id):
        """Sets the promotion_id of this IQueryUserCouponsResultV2.

        |参数名称：促销ID。| |参数约束及描述：促销ID。|

        :param promotion_id: The promotion_id of this IQueryUserCouponsResultV2.
        :type: str
        """
        self._promotion_id = promotion_id

    @property
    def create_time(self):
        """Gets the create_time of this IQueryUserCouponsResultV2.

        |参数名称：创建时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ| |参数约束及描述：创建时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :return: The create_time of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this IQueryUserCouponsResultV2.

        |参数名称：创建时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ| |参数约束及描述：创建时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :param create_time: The create_time of this IQueryUserCouponsResultV2.
        :type: str
        """
        self._create_time = create_time

    @property
    def coupon_version(self):
        """Gets the coupon_version of this IQueryUserCouponsResultV2.

        |参数名称：优惠券版本：1：老版本，老版本优惠券只能使用一次；2：新版本，新版本优惠券可以反复使用。| |参数的约束及描述：优惠券版本：1：老版本，老版本优惠券只能使用一次；2：新版本，新版本优惠券可以反复使用。|

        :return: The coupon_version of this IQueryUserCouponsResultV2.
        :rtype: int
        """
        return self._coupon_version

    @coupon_version.setter
    def coupon_version(self, coupon_version):
        """Sets the coupon_version of this IQueryUserCouponsResultV2.

        |参数名称：优惠券版本：1：老版本，老版本优惠券只能使用一次；2：新版本，新版本优惠券可以反复使用。| |参数的约束及描述：优惠券版本：1：老版本，老版本优惠券只能使用一次；2：新版本，新版本优惠券可以反复使用。|

        :param coupon_version: The coupon_version of this IQueryUserCouponsResultV2.
        :type: int
        """
        self._coupon_version = coupon_version

    @property
    def balance(self):
        """Gets the balance of this IQueryUserCouponsResultV2.

        |参数名称：余额。如果为老版本优惠券，该值为空| |参数的约束及描述：余额。如果为老版本优惠券，该值为空|

        :return: The balance of this IQueryUserCouponsResultV2.
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this IQueryUserCouponsResultV2.

        |参数名称：余额。如果为老版本优惠券，该值为空| |参数的约束及描述：余额。如果为老版本优惠券，该值为空|

        :param balance: The balance of this IQueryUserCouponsResultV2.
        :type: float
        """
        self._balance = balance

    @property
    def lock_order_id(self):
        """Gets the lock_order_id of this IQueryUserCouponsResultV2.

        |参数名称：锁定优惠券的订单ID。如果为老版本优惠券，该值为空。| |参数约束及描述：锁定优惠券的订单ID。如果为老版本优惠券，该值为空。|

        :return: The lock_order_id of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._lock_order_id

    @lock_order_id.setter
    def lock_order_id(self, lock_order_id):
        """Sets the lock_order_id of this IQueryUserCouponsResultV2.

        |参数名称：锁定优惠券的订单ID。如果为老版本优惠券，该值为空。| |参数约束及描述：锁定优惠券的订单ID。如果为老版本优惠券，该值为空。|

        :param lock_order_id: The lock_order_id of this IQueryUserCouponsResultV2.
        :type: str
        """
        self._lock_order_id = lock_order_id

    @property
    def coupon_usage(self):
        """Gets the coupon_usage of this IQueryUserCouponsResultV2.

        |参数名称：优惠券用途。| |参数约束及描述：优惠券用途。|

        :return: The coupon_usage of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._coupon_usage

    @coupon_usage.setter
    def coupon_usage(self, coupon_usage):
        """Sets the coupon_usage of this IQueryUserCouponsResultV2.

        |参数名称：优惠券用途。| |参数约束及描述：优惠券用途。|

        :param coupon_usage: The coupon_usage of this IQueryUserCouponsResultV2.
        :type: str
        """
        self._coupon_usage = coupon_usage

    @property
    def is_frozen(self):
        """Gets the is_frozen of this IQueryUserCouponsResultV2.

        |参数名称：优惠券是否冻结：0：否1：是可用优惠券接口返回时不包括冻结状态的优惠券。| |参数约束及描述：优惠券是否冻结：0：否1：是可用优惠券接口返回时不包括冻结状态的优惠券。|

        :return: The is_frozen of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._is_frozen

    @is_frozen.setter
    def is_frozen(self, is_frozen):
        """Sets the is_frozen of this IQueryUserCouponsResultV2.

        |参数名称：优惠券是否冻结：0：否1：是可用优惠券接口返回时不包括冻结状态的优惠券。| |参数约束及描述：优惠券是否冻结：0：否1：是可用优惠券接口返回时不包括冻结状态的优惠券。|

        :param is_frozen: The is_frozen of this IQueryUserCouponsResultV2.
        :type: str
        """
        self._is_frozen = is_frozen

    @property
    def currency(self):
        """Gets the currency of this IQueryUserCouponsResultV2.

        |参数名称：币种。| |参数约束及描述：币种。|

        :return: The currency of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this IQueryUserCouponsResultV2.

        |参数名称：币种。| |参数约束及描述：币种。|

        :param currency: The currency of this IQueryUserCouponsResultV2.
        :type: str
        """
        self._currency = currency

    @property
    def extend_param1(self):
        """Gets the extend_param1 of this IQueryUserCouponsResultV2.

        |参数名称：扩展字段。| |参数约束及描述：扩展字段。|

        :return: The extend_param1 of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._extend_param1

    @extend_param1.setter
    def extend_param1(self, extend_param1):
        """Sets the extend_param1 of this IQueryUserCouponsResultV2.

        |参数名称：扩展字段。| |参数约束及描述：扩展字段。|

        :param extend_param1: The extend_param1 of this IQueryUserCouponsResultV2.
        :type: str
        """
        self._extend_param1 = extend_param1

    @property
    def source_id(self):
        """Gets the source_id of this IQueryUserCouponsResultV2.

        |参数名称：发放人标识| |参数约束及描述：用于标识优惠券唯一的发放人； 云豆兑换优惠券时sourceId填写云豆计划Id； 累计送优惠券时sourceId填写累计送计划Id； 抽奖送优惠券时sourceId填写抽奖计划Id； 事件送优惠券时sourceId填写事件计划Id； 定制优惠券时sourceId填写创建人Id；|

        :return: The source_id of this IQueryUserCouponsResultV2.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this IQueryUserCouponsResultV2.

        |参数名称：发放人标识| |参数约束及描述：用于标识优惠券唯一的发放人； 云豆兑换优惠券时sourceId填写云豆计划Id； 累计送优惠券时sourceId填写累计送计划Id； 抽奖送优惠券时sourceId填写抽奖计划Id； 事件送优惠券时sourceId填写事件计划Id； 定制优惠券时sourceId填写创建人Id；|

        :param source_id: The source_id of this IQueryUserCouponsResultV2.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IQueryUserCouponsResultV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
