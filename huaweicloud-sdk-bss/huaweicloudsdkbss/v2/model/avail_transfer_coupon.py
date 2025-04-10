# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AvailTransferCoupon:

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
        'plan_name': 'str',
        'balance': 'str',
        'effective_time': 'str',
        'expire_time': 'str',
        'use_limits': 'list[ICouponUseLimitInfoV2]'
    }

    attribute_map = {
        'coupon_id': 'coupon_id',
        'plan_name': 'plan_name',
        'balance': 'balance',
        'effective_time': 'effective_time',
        'expire_time': 'expire_time',
        'use_limits': 'use_limits'
    }

    def __init__(self, coupon_id=None, plan_name=None, balance=None, effective_time=None, expire_time=None, use_limits=None):
        r"""AvailTransferCoupon

        The model defined in huaweicloud sdk

        :param coupon_id: 优惠券ID。
        :type coupon_id: str
        :param plan_name: 促销计划名称。
        :type plan_name: str
        :param balance: 优惠券余额。单位为元
        :type balance: str
        :param effective_time: 生效时间。 UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”。
        :type effective_time: str
        :param expire_time: 失效时间。 UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”。
        :type expire_time: str
        :param use_limits: 优惠券限制。 具体请参见表3。
        :type use_limits: list[:class:`huaweicloudsdkbss.v2.ICouponUseLimitInfoV2`]
        """
        
        

        self._coupon_id = None
        self._plan_name = None
        self._balance = None
        self._effective_time = None
        self._expire_time = None
        self._use_limits = None
        self.discriminator = None

        if coupon_id is not None:
            self.coupon_id = coupon_id
        if plan_name is not None:
            self.plan_name = plan_name
        if balance is not None:
            self.balance = balance
        if effective_time is not None:
            self.effective_time = effective_time
        if expire_time is not None:
            self.expire_time = expire_time
        if use_limits is not None:
            self.use_limits = use_limits

    @property
    def coupon_id(self):
        r"""Gets the coupon_id of this AvailTransferCoupon.

        优惠券ID。

        :return: The coupon_id of this AvailTransferCoupon.
        :rtype: str
        """
        return self._coupon_id

    @coupon_id.setter
    def coupon_id(self, coupon_id):
        r"""Sets the coupon_id of this AvailTransferCoupon.

        优惠券ID。

        :param coupon_id: The coupon_id of this AvailTransferCoupon.
        :type coupon_id: str
        """
        self._coupon_id = coupon_id

    @property
    def plan_name(self):
        r"""Gets the plan_name of this AvailTransferCoupon.

        促销计划名称。

        :return: The plan_name of this AvailTransferCoupon.
        :rtype: str
        """
        return self._plan_name

    @plan_name.setter
    def plan_name(self, plan_name):
        r"""Sets the plan_name of this AvailTransferCoupon.

        促销计划名称。

        :param plan_name: The plan_name of this AvailTransferCoupon.
        :type plan_name: str
        """
        self._plan_name = plan_name

    @property
    def balance(self):
        r"""Gets the balance of this AvailTransferCoupon.

        优惠券余额。单位为元

        :return: The balance of this AvailTransferCoupon.
        :rtype: str
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        r"""Sets the balance of this AvailTransferCoupon.

        优惠券余额。单位为元

        :param balance: The balance of this AvailTransferCoupon.
        :type balance: str
        """
        self._balance = balance

    @property
    def effective_time(self):
        r"""Gets the effective_time of this AvailTransferCoupon.

        生效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :return: The effective_time of this AvailTransferCoupon.
        :rtype: str
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        r"""Sets the effective_time of this AvailTransferCoupon.

        生效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :param effective_time: The effective_time of this AvailTransferCoupon.
        :type effective_time: str
        """
        self._effective_time = effective_time

    @property
    def expire_time(self):
        r"""Gets the expire_time of this AvailTransferCoupon.

        失效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :return: The expire_time of this AvailTransferCoupon.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this AvailTransferCoupon.

        失效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :param expire_time: The expire_time of this AvailTransferCoupon.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def use_limits(self):
        r"""Gets the use_limits of this AvailTransferCoupon.

        优惠券限制。 具体请参见表3。

        :return: The use_limits of this AvailTransferCoupon.
        :rtype: list[:class:`huaweicloudsdkbss.v2.ICouponUseLimitInfoV2`]
        """
        return self._use_limits

    @use_limits.setter
    def use_limits(self, use_limits):
        r"""Sets the use_limits of this AvailTransferCoupon.

        优惠券限制。 具体请参见表3。

        :param use_limits: The use_limits of this AvailTransferCoupon.
        :type use_limits: list[:class:`huaweicloudsdkbss.v2.ICouponUseLimitInfoV2`]
        """
        self._use_limits = use_limits

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
        if not isinstance(other, AvailTransferCoupon):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
