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
        'coupon_infos': 'list[CouponSimpleInfoOrderPay]',
        'discount_infos': 'list[DiscountSimpleInfo]'
    }

    attribute_map = {
        'order_id': 'order_id',
        'coupon_infos': 'coupon_infos',
        'discount_infos': 'discount_infos'
    }

    def __init__(self, order_id=None, coupon_infos=None, discount_infos=None):
        """PayCustomerOrderReq - a model defined in huaweicloud sdk"""
        
        

        self._order_id = None
        self._coupon_infos = None
        self._discount_infos = None
        self.discriminator = None

        self.order_id = order_id
        if coupon_infos is not None:
            self.coupon_infos = coupon_infos
        if discount_infos is not None:
            self.discount_infos = discount_infos

    @property
    def order_id(self):
        """Gets the order_id of this PayCustomerOrderReq.

        订单编号。 取值为调用“查询订单列表”接口时响应消息中的“order_id”字段的值或调用“续订包年/包月资源”接口时响应消息“order_ids”中的订单ID。

        :return: The order_id of this PayCustomerOrderReq.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this PayCustomerOrderReq.

        订单编号。 取值为调用“查询订单列表”接口时响应消息中的“order_id”字段的值或调用“续订包年/包月资源”接口时响应消息“order_ids”中的订单ID。

        :param order_id: The order_id of this PayCustomerOrderReq.
        :type: str
        """
        self._order_id = order_id

    @property
    def coupon_infos(self):
        """Gets the coupon_infos of this PayCustomerOrderReq.

        优惠券ID列表，目前仅支持传递一个优惠券ID。 请从“查询订单可用优惠券”接口的响应参数中获取。 具体参见表1。

        :return: The coupon_infos of this PayCustomerOrderReq.
        :rtype: list[CouponSimpleInfoOrderPay]
        """
        return self._coupon_infos

    @coupon_infos.setter
    def coupon_infos(self, coupon_infos):
        """Sets the coupon_infos of this PayCustomerOrderReq.

        优惠券ID列表，目前仅支持传递一个优惠券ID。 请从“查询订单可用优惠券”接口的响应参数中获取。 具体参见表1。

        :param coupon_infos: The coupon_infos of this PayCustomerOrderReq.
        :type: list[CouponSimpleInfoOrderPay]
        """
        self._coupon_infos = coupon_infos

    @property
    def discount_infos(self):
        """Gets the discount_infos of this PayCustomerOrderReq.

        折扣ID列表，目前仅支持传递一个折扣ID。 请从“查询订单可用折扣”接口的响应参数中获取。 具体参见表2。

        :return: The discount_infos of this PayCustomerOrderReq.
        :rtype: list[DiscountSimpleInfo]
        """
        return self._discount_infos

    @discount_infos.setter
    def discount_infos(self, discount_infos):
        """Sets the discount_infos of this PayCustomerOrderReq.

        折扣ID列表，目前仅支持传递一个折扣ID。 请从“查询订单可用折扣”接口的响应参数中获取。 具体参见表2。

        :param discount_infos: The discount_infos of this PayCustomerOrderReq.
        :type: list[DiscountSimpleInfo]
        """
        self._discount_infos = discount_infos

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
