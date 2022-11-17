# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CouponInfoV2:

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
        'coupon_type': 'int',
        'measure_id': 'int',
        'face_value': 'float',
        'effective_time': 'str',
        'expire_time': 'str',
        'plan_name': 'str',
        'plan_desc': 'str',
        'use_limits': 'list[LimitInfoV2]',
        'active_time': 'str',
        'last_used_time': 'str',
        'create_time': 'str',
        'coupon_version': 'int',
        'balance': 'float',
        'used_by_order_id': 'str',
        'coupon_usage': 'str',
        'coupon_group': 'int'
    }

    attribute_map = {
        'coupon_id': 'coupon_id',
        'coupon_code': 'coupon_code',
        'status': 'status',
        'coupon_type': 'coupon_type',
        'measure_id': 'measure_id',
        'face_value': 'face_value',
        'effective_time': 'effective_time',
        'expire_time': 'expire_time',
        'plan_name': 'plan_name',
        'plan_desc': 'plan_desc',
        'use_limits': 'use_limits',
        'active_time': 'active_time',
        'last_used_time': 'last_used_time',
        'create_time': 'create_time',
        'coupon_version': 'coupon_version',
        'balance': 'balance',
        'used_by_order_id': 'used_by_order_id',
        'coupon_usage': 'coupon_usage',
        'coupon_group': 'coupon_group'
    }

    def __init__(self, coupon_id=None, coupon_code=None, status=None, coupon_type=None, measure_id=None, face_value=None, effective_time=None, expire_time=None, plan_name=None, plan_desc=None, use_limits=None, active_time=None, last_used_time=None, create_time=None, coupon_version=None, balance=None, used_by_order_id=None, coupon_usage=None, coupon_group=None):
        """CouponInfoV2

        The model defined in huaweicloud sdk

        :param coupon_id: 优惠券实例ID。
        :type coupon_id: str
        :param coupon_code: 优惠券编码。
        :type coupon_code: str
        :param status: 优惠券状态： 1：未激活2：待使用
        :type status: int
        :param coupon_type: 优惠券类型。 1：代金券2：折扣券3：产品券4：现金券
        :type coupon_type: int
        :param measure_id: 面额单位： 1：元。
        :type measure_id: int
        :param face_value: 面值。
        :type face_value: float
        :param effective_time: 生效时间。 UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”。
        :type effective_time: str
        :param expire_time: 失效时间。 UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”。
        :type expire_time: str
        :param plan_name: 促销计划名称。
        :type plan_name: str
        :param plan_desc: 促销计划描述。
        :type plan_desc: str
        :param use_limits: 优惠券限制。 具体请参见表3。
        :type use_limits: list[:class:`huaweicloudsdkbss.v2.LimitInfoV2`]
        :param active_time: 激活时间。 UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”。
        :type active_time: str
        :param last_used_time: 上一次使用时间。 UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”。
        :type last_used_time: str
        :param create_time: 创建时间。 UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”。
        :type create_time: str
        :param coupon_version: 优惠券版本。 1：老版本（包含三种：代金券、折扣券和奖金券）2：新版本（只有代金券）
        :type coupon_version: int
        :param balance: 余额。
        :type balance: float
        :param used_by_order_id: 使用优惠券的订单ID。表示有订单正在使用这个优惠券，优惠券已被锁定，只有锁定优惠券的订单才能使用这个优惠券，其他订单不能使用该优惠券。
        :type used_by_order_id: str
        :param coupon_usage: 优惠券用途。
        :type coupon_usage: str
        :param coupon_group: 优惠券分组。 1：云商店发放的券2：华为云券-1024-专用代金券3：华为云券-使用限制-抵扣硬件的券0：华为云服务券（排除上述取值之外的券）
        :type coupon_group: int
        """
        
        

        self._coupon_id = None
        self._coupon_code = None
        self._status = None
        self._coupon_type = None
        self._measure_id = None
        self._face_value = None
        self._effective_time = None
        self._expire_time = None
        self._plan_name = None
        self._plan_desc = None
        self._use_limits = None
        self._active_time = None
        self._last_used_time = None
        self._create_time = None
        self._coupon_version = None
        self._balance = None
        self._used_by_order_id = None
        self._coupon_usage = None
        self._coupon_group = None
        self.discriminator = None

        if coupon_id is not None:
            self.coupon_id = coupon_id
        if coupon_code is not None:
            self.coupon_code = coupon_code
        if status is not None:
            self.status = status
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
        if plan_name is not None:
            self.plan_name = plan_name
        if plan_desc is not None:
            self.plan_desc = plan_desc
        if use_limits is not None:
            self.use_limits = use_limits
        if active_time is not None:
            self.active_time = active_time
        if last_used_time is not None:
            self.last_used_time = last_used_time
        if create_time is not None:
            self.create_time = create_time
        if coupon_version is not None:
            self.coupon_version = coupon_version
        if balance is not None:
            self.balance = balance
        if used_by_order_id is not None:
            self.used_by_order_id = used_by_order_id
        if coupon_usage is not None:
            self.coupon_usage = coupon_usage
        if coupon_group is not None:
            self.coupon_group = coupon_group

    @property
    def coupon_id(self):
        """Gets the coupon_id of this CouponInfoV2.

        优惠券实例ID。

        :return: The coupon_id of this CouponInfoV2.
        :rtype: str
        """
        return self._coupon_id

    @coupon_id.setter
    def coupon_id(self, coupon_id):
        """Sets the coupon_id of this CouponInfoV2.

        优惠券实例ID。

        :param coupon_id: The coupon_id of this CouponInfoV2.
        :type coupon_id: str
        """
        self._coupon_id = coupon_id

    @property
    def coupon_code(self):
        """Gets the coupon_code of this CouponInfoV2.

        优惠券编码。

        :return: The coupon_code of this CouponInfoV2.
        :rtype: str
        """
        return self._coupon_code

    @coupon_code.setter
    def coupon_code(self, coupon_code):
        """Sets the coupon_code of this CouponInfoV2.

        优惠券编码。

        :param coupon_code: The coupon_code of this CouponInfoV2.
        :type coupon_code: str
        """
        self._coupon_code = coupon_code

    @property
    def status(self):
        """Gets the status of this CouponInfoV2.

        优惠券状态： 1：未激活2：待使用

        :return: The status of this CouponInfoV2.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CouponInfoV2.

        优惠券状态： 1：未激活2：待使用

        :param status: The status of this CouponInfoV2.
        :type status: int
        """
        self._status = status

    @property
    def coupon_type(self):
        """Gets the coupon_type of this CouponInfoV2.

        优惠券类型。 1：代金券2：折扣券3：产品券4：现金券

        :return: The coupon_type of this CouponInfoV2.
        :rtype: int
        """
        return self._coupon_type

    @coupon_type.setter
    def coupon_type(self, coupon_type):
        """Sets the coupon_type of this CouponInfoV2.

        优惠券类型。 1：代金券2：折扣券3：产品券4：现金券

        :param coupon_type: The coupon_type of this CouponInfoV2.
        :type coupon_type: int
        """
        self._coupon_type = coupon_type

    @property
    def measure_id(self):
        """Gets the measure_id of this CouponInfoV2.

        面额单位： 1：元。

        :return: The measure_id of this CouponInfoV2.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this CouponInfoV2.

        面额单位： 1：元。

        :param measure_id: The measure_id of this CouponInfoV2.
        :type measure_id: int
        """
        self._measure_id = measure_id

    @property
    def face_value(self):
        """Gets the face_value of this CouponInfoV2.

        面值。

        :return: The face_value of this CouponInfoV2.
        :rtype: float
        """
        return self._face_value

    @face_value.setter
    def face_value(self, face_value):
        """Sets the face_value of this CouponInfoV2.

        面值。

        :param face_value: The face_value of this CouponInfoV2.
        :type face_value: float
        """
        self._face_value = face_value

    @property
    def effective_time(self):
        """Gets the effective_time of this CouponInfoV2.

        生效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :return: The effective_time of this CouponInfoV2.
        :rtype: str
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        """Sets the effective_time of this CouponInfoV2.

        生效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :param effective_time: The effective_time of this CouponInfoV2.
        :type effective_time: str
        """
        self._effective_time = effective_time

    @property
    def expire_time(self):
        """Gets the expire_time of this CouponInfoV2.

        失效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :return: The expire_time of this CouponInfoV2.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this CouponInfoV2.

        失效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :param expire_time: The expire_time of this CouponInfoV2.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def plan_name(self):
        """Gets the plan_name of this CouponInfoV2.

        促销计划名称。

        :return: The plan_name of this CouponInfoV2.
        :rtype: str
        """
        return self._plan_name

    @plan_name.setter
    def plan_name(self, plan_name):
        """Sets the plan_name of this CouponInfoV2.

        促销计划名称。

        :param plan_name: The plan_name of this CouponInfoV2.
        :type plan_name: str
        """
        self._plan_name = plan_name

    @property
    def plan_desc(self):
        """Gets the plan_desc of this CouponInfoV2.

        促销计划描述。

        :return: The plan_desc of this CouponInfoV2.
        :rtype: str
        """
        return self._plan_desc

    @plan_desc.setter
    def plan_desc(self, plan_desc):
        """Sets the plan_desc of this CouponInfoV2.

        促销计划描述。

        :param plan_desc: The plan_desc of this CouponInfoV2.
        :type plan_desc: str
        """
        self._plan_desc = plan_desc

    @property
    def use_limits(self):
        """Gets the use_limits of this CouponInfoV2.

        优惠券限制。 具体请参见表3。

        :return: The use_limits of this CouponInfoV2.
        :rtype: list[:class:`huaweicloudsdkbss.v2.LimitInfoV2`]
        """
        return self._use_limits

    @use_limits.setter
    def use_limits(self, use_limits):
        """Sets the use_limits of this CouponInfoV2.

        优惠券限制。 具体请参见表3。

        :param use_limits: The use_limits of this CouponInfoV2.
        :type use_limits: list[:class:`huaweicloudsdkbss.v2.LimitInfoV2`]
        """
        self._use_limits = use_limits

    @property
    def active_time(self):
        """Gets the active_time of this CouponInfoV2.

        激活时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :return: The active_time of this CouponInfoV2.
        :rtype: str
        """
        return self._active_time

    @active_time.setter
    def active_time(self, active_time):
        """Sets the active_time of this CouponInfoV2.

        激活时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :param active_time: The active_time of this CouponInfoV2.
        :type active_time: str
        """
        self._active_time = active_time

    @property
    def last_used_time(self):
        """Gets the last_used_time of this CouponInfoV2.

        上一次使用时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :return: The last_used_time of this CouponInfoV2.
        :rtype: str
        """
        return self._last_used_time

    @last_used_time.setter
    def last_used_time(self, last_used_time):
        """Sets the last_used_time of this CouponInfoV2.

        上一次使用时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :param last_used_time: The last_used_time of this CouponInfoV2.
        :type last_used_time: str
        """
        self._last_used_time = last_used_time

    @property
    def create_time(self):
        """Gets the create_time of this CouponInfoV2.

        创建时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :return: The create_time of this CouponInfoV2.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CouponInfoV2.

        创建时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :param create_time: The create_time of this CouponInfoV2.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def coupon_version(self):
        """Gets the coupon_version of this CouponInfoV2.

        优惠券版本。 1：老版本（包含三种：代金券、折扣券和奖金券）2：新版本（只有代金券）

        :return: The coupon_version of this CouponInfoV2.
        :rtype: int
        """
        return self._coupon_version

    @coupon_version.setter
    def coupon_version(self, coupon_version):
        """Sets the coupon_version of this CouponInfoV2.

        优惠券版本。 1：老版本（包含三种：代金券、折扣券和奖金券）2：新版本（只有代金券）

        :param coupon_version: The coupon_version of this CouponInfoV2.
        :type coupon_version: int
        """
        self._coupon_version = coupon_version

    @property
    def balance(self):
        """Gets the balance of this CouponInfoV2.

        余额。

        :return: The balance of this CouponInfoV2.
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this CouponInfoV2.

        余额。

        :param balance: The balance of this CouponInfoV2.
        :type balance: float
        """
        self._balance = balance

    @property
    def used_by_order_id(self):
        """Gets the used_by_order_id of this CouponInfoV2.

        使用优惠券的订单ID。表示有订单正在使用这个优惠券，优惠券已被锁定，只有锁定优惠券的订单才能使用这个优惠券，其他订单不能使用该优惠券。

        :return: The used_by_order_id of this CouponInfoV2.
        :rtype: str
        """
        return self._used_by_order_id

    @used_by_order_id.setter
    def used_by_order_id(self, used_by_order_id):
        """Sets the used_by_order_id of this CouponInfoV2.

        使用优惠券的订单ID。表示有订单正在使用这个优惠券，优惠券已被锁定，只有锁定优惠券的订单才能使用这个优惠券，其他订单不能使用该优惠券。

        :param used_by_order_id: The used_by_order_id of this CouponInfoV2.
        :type used_by_order_id: str
        """
        self._used_by_order_id = used_by_order_id

    @property
    def coupon_usage(self):
        """Gets the coupon_usage of this CouponInfoV2.

        优惠券用途。

        :return: The coupon_usage of this CouponInfoV2.
        :rtype: str
        """
        return self._coupon_usage

    @coupon_usage.setter
    def coupon_usage(self, coupon_usage):
        """Sets the coupon_usage of this CouponInfoV2.

        优惠券用途。

        :param coupon_usage: The coupon_usage of this CouponInfoV2.
        :type coupon_usage: str
        """
        self._coupon_usage = coupon_usage

    @property
    def coupon_group(self):
        """Gets the coupon_group of this CouponInfoV2.

        优惠券分组。 1：云商店发放的券2：华为云券-1024-专用代金券3：华为云券-使用限制-抵扣硬件的券0：华为云服务券（排除上述取值之外的券）

        :return: The coupon_group of this CouponInfoV2.
        :rtype: int
        """
        return self._coupon_group

    @coupon_group.setter
    def coupon_group(self, coupon_group):
        """Sets the coupon_group of this CouponInfoV2.

        优惠券分组。 1：云商店发放的券2：华为云券-1024-专用代金券3：华为云券-使用限制-抵扣硬件的券0：华为云服务券（排除上述取值之外的券）

        :param coupon_group: The coupon_group of this CouponInfoV2.
        :type coupon_group: int
        """
        self._coupon_group = coupon_group

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
        if not isinstance(other, CouponInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
