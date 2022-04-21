# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        """DiscountInfoV3

        The model defined in huaweicloud sdk

        :param discount_id: 订单的可用折扣ID。 支付订单时，输入该参数的值，即可使用折扣。
        :type discount_id: str
        :param discount_value: 折扣率或者满减值，如果折扣模式是一口价，这个值为空。
        :type discount_value: str
        :param discount_type: 折扣类型，取值为 0：促销折扣1：合同折扣2：商务优惠3：合作伙伴授予折扣609：订单调价折扣
        :type discount_type: int
        :param orders: 可使用折扣的订单列表。 具体请参见表3。
        :type orders: list[:class:`huaweicloudsdkbssintl.v2.OrderV3`]
        """
        
        

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

        订单的可用折扣ID。 支付订单时，输入该参数的值，即可使用折扣。

        :return: The discount_id of this DiscountInfoV3.
        :rtype: str
        """
        return self._discount_id

    @discount_id.setter
    def discount_id(self, discount_id):
        """Sets the discount_id of this DiscountInfoV3.

        订单的可用折扣ID。 支付订单时，输入该参数的值，即可使用折扣。

        :param discount_id: The discount_id of this DiscountInfoV3.
        :type discount_id: str
        """
        self._discount_id = discount_id

    @property
    def discount_value(self):
        """Gets the discount_value of this DiscountInfoV3.

        折扣率或者满减值，如果折扣模式是一口价，这个值为空。

        :return: The discount_value of this DiscountInfoV3.
        :rtype: str
        """
        return self._discount_value

    @discount_value.setter
    def discount_value(self, discount_value):
        """Sets the discount_value of this DiscountInfoV3.

        折扣率或者满减值，如果折扣模式是一口价，这个值为空。

        :param discount_value: The discount_value of this DiscountInfoV3.
        :type discount_value: str
        """
        self._discount_value = discount_value

    @property
    def discount_type(self):
        """Gets the discount_type of this DiscountInfoV3.

        折扣类型，取值为 0：促销折扣1：合同折扣2：商务优惠3：合作伙伴授予折扣609：订单调价折扣

        :return: The discount_type of this DiscountInfoV3.
        :rtype: int
        """
        return self._discount_type

    @discount_type.setter
    def discount_type(self, discount_type):
        """Sets the discount_type of this DiscountInfoV3.

        折扣类型，取值为 0：促销折扣1：合同折扣2：商务优惠3：合作伙伴授予折扣609：订单调价折扣

        :param discount_type: The discount_type of this DiscountInfoV3.
        :type discount_type: int
        """
        self._discount_type = discount_type

    @property
    def orders(self):
        """Gets the orders of this DiscountInfoV3.

        可使用折扣的订单列表。 具体请参见表3。

        :return: The orders of this DiscountInfoV3.
        :rtype: list[:class:`huaweicloudsdkbssintl.v2.OrderV3`]
        """
        return self._orders

    @orders.setter
    def orders(self, orders):
        """Sets the orders of this DiscountInfoV3.

        可使用折扣的订单列表。 具体请参见表3。

        :param orders: The orders of this DiscountInfoV3.
        :type orders: list[:class:`huaweicloudsdkbssintl.v2.OrderV3`]
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
        if not isinstance(other, DiscountInfoV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
