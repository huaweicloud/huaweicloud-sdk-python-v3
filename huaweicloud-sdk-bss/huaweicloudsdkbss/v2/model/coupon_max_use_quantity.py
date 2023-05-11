# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CouponMaxUseQuantity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'coupon_type': 'int',
        'coupon_group': 'int',
        'use_quantity_value': 'int'
    }

    attribute_map = {
        'coupon_type': 'coupon_type',
        'coupon_group': 'coupon_group',
        'use_quantity_value': 'use_quantity_value'
    }

    def __init__(self, coupon_type=None, coupon_group=None, use_quantity_value=None):
        """CouponMaxUseQuantity

        The model defined in huaweicloud sdk

        :param coupon_type: 优惠券类型。 1：代金券2：折扣券3：产品券4：现金券
        :type coupon_type: int
        :param coupon_group: 优惠券分组。 1：云商店发放的券2：华为云券-1024-专用代金券3：华为云券-使用限制-抵扣硬件的券0：华为云服务券（排除上述取值之外的券）
        :type coupon_group: int
        :param use_quantity_value: 优惠券使用数量。
        :type use_quantity_value: int
        """
        
        

        self._coupon_type = None
        self._coupon_group = None
        self._use_quantity_value = None
        self.discriminator = None

        if coupon_type is not None:
            self.coupon_type = coupon_type
        if coupon_group is not None:
            self.coupon_group = coupon_group
        if use_quantity_value is not None:
            self.use_quantity_value = use_quantity_value

    @property
    def coupon_type(self):
        """Gets the coupon_type of this CouponMaxUseQuantity.

        优惠券类型。 1：代金券2：折扣券3：产品券4：现金券

        :return: The coupon_type of this CouponMaxUseQuantity.
        :rtype: int
        """
        return self._coupon_type

    @coupon_type.setter
    def coupon_type(self, coupon_type):
        """Sets the coupon_type of this CouponMaxUseQuantity.

        优惠券类型。 1：代金券2：折扣券3：产品券4：现金券

        :param coupon_type: The coupon_type of this CouponMaxUseQuantity.
        :type coupon_type: int
        """
        self._coupon_type = coupon_type

    @property
    def coupon_group(self):
        """Gets the coupon_group of this CouponMaxUseQuantity.

        优惠券分组。 1：云商店发放的券2：华为云券-1024-专用代金券3：华为云券-使用限制-抵扣硬件的券0：华为云服务券（排除上述取值之外的券）

        :return: The coupon_group of this CouponMaxUseQuantity.
        :rtype: int
        """
        return self._coupon_group

    @coupon_group.setter
    def coupon_group(self, coupon_group):
        """Sets the coupon_group of this CouponMaxUseQuantity.

        优惠券分组。 1：云商店发放的券2：华为云券-1024-专用代金券3：华为云券-使用限制-抵扣硬件的券0：华为云服务券（排除上述取值之外的券）

        :param coupon_group: The coupon_group of this CouponMaxUseQuantity.
        :type coupon_group: int
        """
        self._coupon_group = coupon_group

    @property
    def use_quantity_value(self):
        """Gets the use_quantity_value of this CouponMaxUseQuantity.

        优惠券使用数量。

        :return: The use_quantity_value of this CouponMaxUseQuantity.
        :rtype: int
        """
        return self._use_quantity_value

    @use_quantity_value.setter
    def use_quantity_value(self, use_quantity_value):
        """Sets the use_quantity_value of this CouponMaxUseQuantity.

        优惠券使用数量。

        :param use_quantity_value: The use_quantity_value of this CouponMaxUseQuantity.
        :type use_quantity_value: int
        """
        self._use_quantity_value = use_quantity_value

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
        if not isinstance(other, CouponMaxUseQuantity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
