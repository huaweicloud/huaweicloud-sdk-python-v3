# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOrderCouponsByOrderIdResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'user_coupons': 'list[CouponInfoV2]',
        'coupon_max_use_quantity': 'list[CouponMaxUseQuantity]'
    }

    attribute_map = {
        'count': 'count',
        'user_coupons': 'user_coupons',
        'coupon_max_use_quantity': 'coupon_max_use_quantity'
    }

    def __init__(self, count=None, user_coupons=None, coupon_max_use_quantity=None):
        """ListOrderCouponsByOrderIdResponse

        The model defined in huaweicloud sdk

        :param count: 查询总数。
        :type count: int
        :param user_coupons: 可用的优惠券列表。 具体请参见表2。
        :type user_coupons: list[:class:`huaweicloudsdkbss.v2.CouponInfoV2`]
        :param coupon_max_use_quantity: 优惠券使用的最大数量。 具体请参见表4。
        :type coupon_max_use_quantity: list[:class:`huaweicloudsdkbss.v2.CouponMaxUseQuantity`]
        """
        
        super(ListOrderCouponsByOrderIdResponse, self).__init__()

        self._count = None
        self._user_coupons = None
        self._coupon_max_use_quantity = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if user_coupons is not None:
            self.user_coupons = user_coupons
        if coupon_max_use_quantity is not None:
            self.coupon_max_use_quantity = coupon_max_use_quantity

    @property
    def count(self):
        """Gets the count of this ListOrderCouponsByOrderIdResponse.

        查询总数。

        :return: The count of this ListOrderCouponsByOrderIdResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListOrderCouponsByOrderIdResponse.

        查询总数。

        :param count: The count of this ListOrderCouponsByOrderIdResponse.
        :type count: int
        """
        self._count = count

    @property
    def user_coupons(self):
        """Gets the user_coupons of this ListOrderCouponsByOrderIdResponse.

        可用的优惠券列表。 具体请参见表2。

        :return: The user_coupons of this ListOrderCouponsByOrderIdResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.CouponInfoV2`]
        """
        return self._user_coupons

    @user_coupons.setter
    def user_coupons(self, user_coupons):
        """Sets the user_coupons of this ListOrderCouponsByOrderIdResponse.

        可用的优惠券列表。 具体请参见表2。

        :param user_coupons: The user_coupons of this ListOrderCouponsByOrderIdResponse.
        :type user_coupons: list[:class:`huaweicloudsdkbss.v2.CouponInfoV2`]
        """
        self._user_coupons = user_coupons

    @property
    def coupon_max_use_quantity(self):
        """Gets the coupon_max_use_quantity of this ListOrderCouponsByOrderIdResponse.

        优惠券使用的最大数量。 具体请参见表4。

        :return: The coupon_max_use_quantity of this ListOrderCouponsByOrderIdResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.CouponMaxUseQuantity`]
        """
        return self._coupon_max_use_quantity

    @coupon_max_use_quantity.setter
    def coupon_max_use_quantity(self, coupon_max_use_quantity):
        """Sets the coupon_max_use_quantity of this ListOrderCouponsByOrderIdResponse.

        优惠券使用的最大数量。 具体请参见表4。

        :param coupon_max_use_quantity: The coupon_max_use_quantity of this ListOrderCouponsByOrderIdResponse.
        :type coupon_max_use_quantity: list[:class:`huaweicloudsdkbss.v2.CouponMaxUseQuantity`]
        """
        self._coupon_max_use_quantity = coupon_max_use_quantity

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
        if not isinstance(other, ListOrderCouponsByOrderIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
