# coding: utf-8

import pprint
import re

import six





class DiscountInfoV3:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'discount_id': 'str',
        'discount_value': 'str',
        'discount_type': 'int',
        'orders': 'list[OrderV3]'
    }

    attribute_map = {
        'discount_id': 'discount_id',
        'discount_value': 'discount_value',
        'discount_type': 'discount_type',
        'orders': 'orders'
    }

    def __init__(self, discount_id=None, discount_value=None, discount_type=None, orders=None):
        """DiscountInfoV3 - a model defined in huaweicloud sdk"""
        
        

        self._discount_id = None
        self._discount_value = None
        self._discount_type = None
        self._orders = None
        self.discriminator = None

        self.discount_id = discount_id
        self.discount_value = discount_value
        self.discount_type = discount_type
        self.orders = orders

    @property
    def discount_id(self):
        """Gets the discount_id of this DiscountInfoV3.

        |参数名称：折扣ID，支付的时候，如果要使用折扣，需要将这个值填入| |参数约束及描述：折扣ID，支付的时候，如果要使用折扣，需要将这个值填入|

        :return: The discount_id of this DiscountInfoV3.
        :rtype: str
        """
        return self._discount_id

    @discount_id.setter
    def discount_id(self, discount_id):
        """Sets the discount_id of this DiscountInfoV3.

        |参数名称：折扣ID，支付的时候，如果要使用折扣，需要将这个值填入| |参数约束及描述：折扣ID，支付的时候，如果要使用折扣，需要将这个值填入|

        :param discount_id: The discount_id of this DiscountInfoV3.
        :type: str
        """
        self._discount_id = discount_id

    @property
    def discount_value(self):
        """Gets the discount_value of this DiscountInfoV3.

        |参数名称：discountType为促销折扣或合作伙伴授予折扣时，为折扣率| |参数约束及描述：discountType为促销折扣或合作伙伴授予折扣时，为折扣率|

        :return: The discount_value of this DiscountInfoV3.
        :rtype: str
        """
        return self._discount_value

    @discount_value.setter
    def discount_value(self, discount_value):
        """Sets the discount_value of this DiscountInfoV3.

        |参数名称：discountType为促销折扣或合作伙伴授予折扣时，为折扣率| |参数约束及描述：discountType为促销折扣或合作伙伴授予折扣时，为折扣率|

        :param discount_value: The discount_value of this DiscountInfoV3.
        :type: str
        """
        self._discount_value = discount_value

    @property
    def discount_type(self):
        """Gets the discount_type of this DiscountInfoV3.

        |参数名称：折扣类型，取值为1：合同折扣（可以有多组）2：商务优惠（仅有一组）3：合作伙伴授予折扣（仅有一组）609：订单调价折扣| |参数的约束及描述：折扣类型，取值为1：合同折扣（可以有多组）2：商务优惠（仅有一组）3：合作伙伴授予折扣（仅有一组）609：订单调价折扣|

        :return: The discount_type of this DiscountInfoV3.
        :rtype: int
        """
        return self._discount_type

    @discount_type.setter
    def discount_type(self, discount_type):
        """Sets the discount_type of this DiscountInfoV3.

        |参数名称：折扣类型，取值为1：合同折扣（可以有多组）2：商务优惠（仅有一组）3：合作伙伴授予折扣（仅有一组）609：订单调价折扣| |参数的约束及描述：折扣类型，取值为1：合同折扣（可以有多组）2：商务优惠（仅有一组）3：合作伙伴授予折扣（仅有一组）609：订单调价折扣|

        :param discount_type: The discount_type of this DiscountInfoV3.
        :type: int
        """
        self._discount_type = discount_type

    @property
    def orders(self):
        """Gets the orders of this DiscountInfoV3.

        |参数名称：订单列表| |参数约束以及描述：订单列表|

        :return: The orders of this DiscountInfoV3.
        :rtype: list[OrderV3]
        """
        return self._orders

    @orders.setter
    def orders(self, orders):
        """Sets the orders of this DiscountInfoV3.

        |参数名称：订单列表| |参数约束以及描述：订单列表|

        :param orders: The orders of this DiscountInfoV3.
        :type: list[OrderV3]
        """
        self._orders = orders

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
        if not isinstance(other, DiscountInfoV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
