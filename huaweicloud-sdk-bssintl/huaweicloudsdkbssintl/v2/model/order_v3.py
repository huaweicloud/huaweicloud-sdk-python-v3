# coding: utf-8

import pprint
import re

import six





class OrderV3:


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
        'order_line_items': 'list[OrderLineItemV3]'
    }

    attribute_map = {
        'order_id': 'order_id',
        'order_line_items': 'order_line_items'
    }

    def __init__(self, order_id=None, order_line_items=None):
        """OrderV3 - a model defined in huaweicloud sdk"""
        
        

        self._order_id = None
        self._order_line_items = None
        self.discriminator = None

        self.order_id = order_id
        self.order_line_items = order_line_items

    @property
    def order_id(self):
        """Gets the order_id of this OrderV3.

        |参数名称：订单标识| |参数约束及描述：订单标识|

        :return: The order_id of this OrderV3.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this OrderV3.

        |参数名称：订单标识| |参数约束及描述：订单标识|

        :param order_id: The order_id of this OrderV3.
        :type: str
        """
        self._order_id = order_id

    @property
    def order_line_items(self):
        """Gets the order_line_items of this OrderV3.

        |参数名称：订单行列表| |参数约束以及描述：订单行列表|

        :return: The order_line_items of this OrderV3.
        :rtype: list[OrderLineItemV3]
        """
        return self._order_line_items

    @order_line_items.setter
    def order_line_items(self, order_line_items):
        """Sets the order_line_items of this OrderV3.

        |参数名称：订单行列表| |参数约束以及描述：订单行列表|

        :param order_line_items: The order_line_items of this OrderV3.
        :type: list[OrderLineItemV3]
        """
        self._order_line_items = order_line_items

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
        if not isinstance(other, OrderV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
