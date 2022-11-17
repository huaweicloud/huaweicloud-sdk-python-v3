# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCustomerOrderDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'order_info': 'CustomerOrderV3',
        'order_line_items': 'list[OrderLineItemEntityV2]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'order_info': 'order_info',
        'order_line_items': 'order_line_items'
    }

    def __init__(self, total_count=None, order_info=None, order_line_items=None):
        """ShowCustomerOrderDetailsResponse

        The model defined in huaweicloud sdk

        :param total_count: 订单项个数。
        :type total_count: int
        :param order_info: 
        :type order_info: :class:`huaweicloudsdkbss.v2.CustomerOrderV3`
        :param order_line_items: 订单对应的订单项。 具体请参见表5。
        :type order_line_items: list[:class:`huaweicloudsdkbss.v2.OrderLineItemEntityV2`]
        """
        
        super(ShowCustomerOrderDetailsResponse, self).__init__()

        self._total_count = None
        self._order_info = None
        self._order_line_items = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if order_info is not None:
            self.order_info = order_info
        if order_line_items is not None:
            self.order_line_items = order_line_items

    @property
    def total_count(self):
        """Gets the total_count of this ShowCustomerOrderDetailsResponse.

        订单项个数。

        :return: The total_count of this ShowCustomerOrderDetailsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ShowCustomerOrderDetailsResponse.

        订单项个数。

        :param total_count: The total_count of this ShowCustomerOrderDetailsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def order_info(self):
        """Gets the order_info of this ShowCustomerOrderDetailsResponse.

        :return: The order_info of this ShowCustomerOrderDetailsResponse.
        :rtype: :class:`huaweicloudsdkbss.v2.CustomerOrderV3`
        """
        return self._order_info

    @order_info.setter
    def order_info(self, order_info):
        """Sets the order_info of this ShowCustomerOrderDetailsResponse.

        :param order_info: The order_info of this ShowCustomerOrderDetailsResponse.
        :type order_info: :class:`huaweicloudsdkbss.v2.CustomerOrderV3`
        """
        self._order_info = order_info

    @property
    def order_line_items(self):
        """Gets the order_line_items of this ShowCustomerOrderDetailsResponse.

        订单对应的订单项。 具体请参见表5。

        :return: The order_line_items of this ShowCustomerOrderDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.OrderLineItemEntityV2`]
        """
        return self._order_line_items

    @order_line_items.setter
    def order_line_items(self, order_line_items):
        """Sets the order_line_items of this ShowCustomerOrderDetailsResponse.

        订单对应的订单项。 具体请参见表5。

        :param order_line_items: The order_line_items of this ShowCustomerOrderDetailsResponse.
        :type order_line_items: list[:class:`huaweicloudsdkbss.v2.OrderLineItemEntityV2`]
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
        if not isinstance(other, ShowCustomerOrderDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
