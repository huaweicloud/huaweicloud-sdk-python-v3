# coding: utf-8

import pprint
import re

import six





class CouponSimpleInfoOrderPay:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'type': 'int'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type'
    }

    def __init__(self, id=None, type=None):
        """CouponSimpleInfoOrderPay - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._type = None
        self.discriminator = None

        self.id = id
        self.type = type

    @property
    def id(self):
        """Gets the id of this CouponSimpleInfoOrderPay.

        |参数名称：优惠券ID，同种类型的优惠券，列表前面会优先使用| |参数约束及描述：优惠券ID，同种类型的优惠券，列表前面会优先使用|

        :return: The id of this CouponSimpleInfoOrderPay.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CouponSimpleInfoOrderPay.

        |参数名称：优惠券ID，同种类型的优惠券，列表前面会优先使用| |参数约束及描述：优惠券ID，同种类型的优惠券，列表前面会优先使用|

        :param id: The id of this CouponSimpleInfoOrderPay.
        :type: str
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this CouponSimpleInfoOrderPay.

        |参数名称：折扣类型：取值为300-折扣卷 301-促销代金券302-促销现金券303-促销储值卡| |参数的约束及描述：折扣类型：取值为300-折扣卷 301-促销代金券302-促销现金券303-促销储值卡|

        :return: The type of this CouponSimpleInfoOrderPay.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CouponSimpleInfoOrderPay.

        |参数名称：折扣类型：取值为300-折扣卷 301-促销代金券302-促销现金券303-促销储值卡| |参数的约束及描述：折扣类型：取值为300-折扣卷 301-促销代金券302-促销现金券303-促销储值卡|

        :param type: The type of this CouponSimpleInfoOrderPay.
        :type: int
        """
        self._type = type

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
        if not isinstance(other, CouponSimpleInfoOrderPay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
