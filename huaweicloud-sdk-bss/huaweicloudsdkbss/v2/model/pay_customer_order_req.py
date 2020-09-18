# coding: utf-8

import pprint
import re

import six





class PayCustomerOrderReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'order_id': 'str',
        'coupon_infos': 'list[CouponSimpleInfoOrderPay]'
    }

    attribute_map = {
        'order_id': 'order_id',
        'coupon_infos': 'coupon_infos'
    }

    def __init__(self, order_id=None, coupon_infos=None):
        """PayCustomerOrderReq - a model defined in huaweicloud sdk"""
        
        

        self._order_id = None
        self._coupon_infos = None
        self.discriminator = None

        self.order_id = order_id
        if coupon_infos is not None:
            self.coupon_infos = coupon_infos

    @property
    def order_id(self):
        """Gets the order_id of this PayCustomerOrderReq.

        |参数名称：订单ID。| |参数约束及描述：订单ID。|

        :return: The order_id of this PayCustomerOrderReq.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this PayCustomerOrderReq.

        |参数名称：订单ID。| |参数约束及描述：订单ID。|

        :param order_id: The order_id of this PayCustomerOrderReq.
        :type: str
        """
        self._order_id = order_id

    @property
    def coupon_infos(self):
        """Gets the coupon_infos of this PayCustomerOrderReq.

        |参数名称：字段预留。优惠券列表，目前仅支持传递一个优惠券ID。请从“1.3-查询订单可用优惠券”接口的响应参数中获取。| |参数约束以及描述：字段预留。优惠券列表，目前仅支持传递一个优惠券ID。请从“1.3-查询订单可用优惠券”接口的响应参数中获取。|

        :return: The coupon_infos of this PayCustomerOrderReq.
        :rtype: list[CouponSimpleInfoOrderPay]
        """
        return self._coupon_infos

    @coupon_infos.setter
    def coupon_infos(self, coupon_infos):
        """Sets the coupon_infos of this PayCustomerOrderReq.

        |参数名称：字段预留。优惠券列表，目前仅支持传递一个优惠券ID。请从“1.3-查询订单可用优惠券”接口的响应参数中获取。| |参数约束以及描述：字段预留。优惠券列表，目前仅支持传递一个优惠券ID。请从“1.3-查询订单可用优惠券”接口的响应参数中获取。|

        :param coupon_infos: The coupon_infos of this PayCustomerOrderReq.
        :type: list[CouponSimpleInfoOrderPay]
        """
        self._coupon_infos = coupon_infos

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
        if not isinstance(other, PayCustomerOrderReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
