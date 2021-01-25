# coding: utf-8

import pprint
import re

import six





class OrderLineItemV3:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'order_line_item_ids': 'list[str]',
        'discount_mode': 'int',
        'discount_amount': 'float',
        'discount_ratio': 'float'
    }

    attribute_map = {
        'order_line_item_ids': 'order_line_item_ids',
        'discount_mode': 'discount_mode',
        'discount_amount': 'discount_amount',
        'discount_ratio': 'discount_ratio'
    }

    def __init__(self, order_line_item_ids=None, discount_mode=None, discount_amount=None, discount_ratio=None):
        """OrderLineItemV3 - a model defined in huaweicloud sdk"""
        
        

        self._order_line_item_ids = None
        self._discount_mode = None
        self._discount_amount = None
        self._discount_ratio = None
        self.discriminator = None

        self.order_line_item_ids = order_line_item_ids
        self.discount_mode = discount_mode
        self.discount_amount = discount_amount
        self.discount_ratio = discount_ratio

    @property
    def order_line_item_ids(self):
        """Gets the order_line_item_ids of this OrderLineItemV3.

        |参数名称：用于合并的订单项列表，会将相同产品、相同规格（对于线性产品）、相同最终价格（例如，严选产品改价）的进行合并| |参数约束以及描述：用于合并的订单项列表，会将相同产品、相同规格（对于线性产品）、相同最终价格（例如，严选产品改价）的进行合并|

        :return: The order_line_item_ids of this OrderLineItemV3.
        :rtype: list[str]
        """
        return self._order_line_item_ids

    @order_line_item_ids.setter
    def order_line_item_ids(self, order_line_item_ids):
        """Sets the order_line_item_ids of this OrderLineItemV3.

        |参数名称：用于合并的订单项列表，会将相同产品、相同规格（对于线性产品）、相同最终价格（例如，严选产品改价）的进行合并| |参数约束以及描述：用于合并的订单项列表，会将相同产品、相同规格（对于线性产品）、相同最终价格（例如，严选产品改价）的进行合并|

        :param order_line_item_ids: The order_line_item_ids of this OrderLineItemV3.
        :type: list[str]
        """
        self._order_line_item_ids = order_line_item_ids

    @property
    def discount_mode(self):
        """Gets the discount_mode of this OrderLineItemV3.

        |参数名称：折扣模式 0：折扣 1：一口价 2：满减| |参数的约束及描述：折扣模式 0：折扣 1：一口价 2：满减|

        :return: The discount_mode of this OrderLineItemV3.
        :rtype: int
        """
        return self._discount_mode

    @discount_mode.setter
    def discount_mode(self, discount_mode):
        """Sets the discount_mode of this OrderLineItemV3.

        |参数名称：折扣模式 0：折扣 1：一口价 2：满减| |参数的约束及描述：折扣模式 0：折扣 1：一口价 2：满减|

        :param discount_mode: The discount_mode of this OrderLineItemV3.
        :type: int
        """
        self._discount_mode = discount_mode

    @property
    def discount_amount(self):
        """Gets the discount_amount of this OrderLineItemV3.

        |参数名称：折扣额（减免金额）| |参数的约束及描述：折扣额（减免金额）|

        :return: The discount_amount of this OrderLineItemV3.
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this OrderLineItemV3.

        |参数名称：折扣额（减免金额）| |参数的约束及描述：折扣额（减免金额）|

        :param discount_amount: The discount_amount of this OrderLineItemV3.
        :type: float
        """
        self._discount_amount = discount_amount

    @property
    def discount_ratio(self):
        """Gets the discount_ratio of this OrderLineItemV3.

        |参数名称：折扣比例，折扣为| |参数的约束及描述：折扣比例，折扣为|

        :return: The discount_ratio of this OrderLineItemV3.
        :rtype: float
        """
        return self._discount_ratio

    @discount_ratio.setter
    def discount_ratio(self, discount_ratio):
        """Sets the discount_ratio of this OrderLineItemV3.

        |参数名称：折扣比例，折扣为| |参数的约束及描述：折扣比例，折扣为|

        :param discount_ratio: The discount_ratio of this OrderLineItemV3.
        :type: float
        """
        self._discount_ratio = discount_ratio

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
        if not isinstance(other, OrderLineItemV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
