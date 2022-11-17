# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PayCustomerOrderV3Req:

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
        'use_coupon': 'str',
        'use_discount': 'str',
        'coupon_infos': 'list[CouponSimpleInfoOrderPayV3]',
        'discount_infos': 'list[DiscountSimpleInfoV3]'
    }

    attribute_map = {
        'order_id': 'order_id',
        'use_coupon': 'use_coupon',
        'use_discount': 'use_discount',
        'coupon_infos': 'coupon_infos',
        'discount_infos': 'discount_infos'
    }

    def __init__(self, order_id=None, use_coupon=None, use_discount=None, coupon_infos=None, discount_infos=None):
        """PayCustomerOrderV3Req

        The model defined in huaweicloud sdk

        :param order_id: 订单编号。 取值为调用“查询订单列表”接口时响应消息中的“order_id”字段的值或调用“续订包年/包月资源”接口时响应消息“order_ids”中的订单ID。
        :type order_id: str
        :param use_coupon: 本次订单支付是否使用优惠券。传递“YES”时，coupon_infos字段必选，传递“NO”时，会忽略coupon_infos字段的传值。 使用优惠券：YES，不使用优惠券：NO
        :type use_coupon: str
        :param use_discount: 本次订单支付是否使用折扣。传递“YES”时，discount_infos字段必选，传递“NO”时，会忽略discount_infos字段的传值。 使用折扣：YES，不使用折扣：NO
        :type use_discount: str
        :param coupon_infos: 优惠券ID列表，目前支持传递最多三个优惠券ID。 请从“查询订单可用优惠券”接口的响应参数中获取。 具体参见表1。 当use_coupon参数取值为“YES”，本字段必填；当use_coupon参数取值为“NO”，本字段不可填写，否则报参数错误。
        :type coupon_infos: list[:class:`huaweicloudsdkbssintl.v2.CouponSimpleInfoOrderPayV3`]
        :param discount_infos: 折扣ID列表，目前仅支持传递一个折扣ID。 请从“查询订单可用折扣”接口的响应参数中获取。 具体参见表2。 当use_discount参数取值为“YES”，本字段必填；当use_discount参数取值为“NO”，本字段不可填写，否则报参数错误。
        :type discount_infos: list[:class:`huaweicloudsdkbssintl.v2.DiscountSimpleInfoV3`]
        """
        
        

        self._order_id = None
        self._use_coupon = None
        self._use_discount = None
        self._coupon_infos = None
        self._discount_infos = None
        self.discriminator = None

        self.order_id = order_id
        self.use_coupon = use_coupon
        self.use_discount = use_discount
        if coupon_infos is not None:
            self.coupon_infos = coupon_infos
        if discount_infos is not None:
            self.discount_infos = discount_infos

    @property
    def order_id(self):
        """Gets the order_id of this PayCustomerOrderV3Req.

        订单编号。 取值为调用“查询订单列表”接口时响应消息中的“order_id”字段的值或调用“续订包年/包月资源”接口时响应消息“order_ids”中的订单ID。

        :return: The order_id of this PayCustomerOrderV3Req.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this PayCustomerOrderV3Req.

        订单编号。 取值为调用“查询订单列表”接口时响应消息中的“order_id”字段的值或调用“续订包年/包月资源”接口时响应消息“order_ids”中的订单ID。

        :param order_id: The order_id of this PayCustomerOrderV3Req.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def use_coupon(self):
        """Gets the use_coupon of this PayCustomerOrderV3Req.

        本次订单支付是否使用优惠券。传递“YES”时，coupon_infos字段必选，传递“NO”时，会忽略coupon_infos字段的传值。 使用优惠券：YES，不使用优惠券：NO

        :return: The use_coupon of this PayCustomerOrderV3Req.
        :rtype: str
        """
        return self._use_coupon

    @use_coupon.setter
    def use_coupon(self, use_coupon):
        """Sets the use_coupon of this PayCustomerOrderV3Req.

        本次订单支付是否使用优惠券。传递“YES”时，coupon_infos字段必选，传递“NO”时，会忽略coupon_infos字段的传值。 使用优惠券：YES，不使用优惠券：NO

        :param use_coupon: The use_coupon of this PayCustomerOrderV3Req.
        :type use_coupon: str
        """
        self._use_coupon = use_coupon

    @property
    def use_discount(self):
        """Gets the use_discount of this PayCustomerOrderV3Req.

        本次订单支付是否使用折扣。传递“YES”时，discount_infos字段必选，传递“NO”时，会忽略discount_infos字段的传值。 使用折扣：YES，不使用折扣：NO

        :return: The use_discount of this PayCustomerOrderV3Req.
        :rtype: str
        """
        return self._use_discount

    @use_discount.setter
    def use_discount(self, use_discount):
        """Sets the use_discount of this PayCustomerOrderV3Req.

        本次订单支付是否使用折扣。传递“YES”时，discount_infos字段必选，传递“NO”时，会忽略discount_infos字段的传值。 使用折扣：YES，不使用折扣：NO

        :param use_discount: The use_discount of this PayCustomerOrderV3Req.
        :type use_discount: str
        """
        self._use_discount = use_discount

    @property
    def coupon_infos(self):
        """Gets the coupon_infos of this PayCustomerOrderV3Req.

        优惠券ID列表，目前支持传递最多三个优惠券ID。 请从“查询订单可用优惠券”接口的响应参数中获取。 具体参见表1。 当use_coupon参数取值为“YES”，本字段必填；当use_coupon参数取值为“NO”，本字段不可填写，否则报参数错误。

        :return: The coupon_infos of this PayCustomerOrderV3Req.
        :rtype: list[:class:`huaweicloudsdkbssintl.v2.CouponSimpleInfoOrderPayV3`]
        """
        return self._coupon_infos

    @coupon_infos.setter
    def coupon_infos(self, coupon_infos):
        """Sets the coupon_infos of this PayCustomerOrderV3Req.

        优惠券ID列表，目前支持传递最多三个优惠券ID。 请从“查询订单可用优惠券”接口的响应参数中获取。 具体参见表1。 当use_coupon参数取值为“YES”，本字段必填；当use_coupon参数取值为“NO”，本字段不可填写，否则报参数错误。

        :param coupon_infos: The coupon_infos of this PayCustomerOrderV3Req.
        :type coupon_infos: list[:class:`huaweicloudsdkbssintl.v2.CouponSimpleInfoOrderPayV3`]
        """
        self._coupon_infos = coupon_infos

    @property
    def discount_infos(self):
        """Gets the discount_infos of this PayCustomerOrderV3Req.

        折扣ID列表，目前仅支持传递一个折扣ID。 请从“查询订单可用折扣”接口的响应参数中获取。 具体参见表2。 当use_discount参数取值为“YES”，本字段必填；当use_discount参数取值为“NO”，本字段不可填写，否则报参数错误。

        :return: The discount_infos of this PayCustomerOrderV3Req.
        :rtype: list[:class:`huaweicloudsdkbssintl.v2.DiscountSimpleInfoV3`]
        """
        return self._discount_infos

    @discount_infos.setter
    def discount_infos(self, discount_infos):
        """Sets the discount_infos of this PayCustomerOrderV3Req.

        折扣ID列表，目前仅支持传递一个折扣ID。 请从“查询订单可用折扣”接口的响应参数中获取。 具体参见表2。 当use_discount参数取值为“YES”，本字段必填；当use_discount参数取值为“NO”，本字段不可填写，否则报参数错误。

        :param discount_infos: The discount_infos of this PayCustomerOrderV3Req.
        :type discount_infos: list[:class:`huaweicloudsdkbssintl.v2.DiscountSimpleInfoV3`]
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
        if not isinstance(other, PayCustomerOrderV3Req):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
