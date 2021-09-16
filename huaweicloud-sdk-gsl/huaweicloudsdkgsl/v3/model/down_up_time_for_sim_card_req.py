# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownUpTimeForSimCardReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'price_plan_list': 'list[SimPricePlanInfoVO]',
        'down_up_switch': 'int'
    }

    attribute_map = {
        'price_plan_list': 'price_plan_list',
        'down_up_switch': 'down_up_switch'
    }

    def __init__(self, price_plan_list=None, down_up_switch=None):
        """DownUpTimeForSimCardReq - a model defined in huaweicloud sdk"""
        
        

        self._price_plan_list = None
        self._down_up_switch = None
        self.discriminator = None

        if price_plan_list is not None:
            self.price_plan_list = price_plan_list
        if down_up_switch is not None:
            self.down_up_switch = down_up_switch

    @property
    def price_plan_list(self):
        """Gets the price_plan_list of this DownUpTimeForSimCardReq.

        套餐列表

        :return: The price_plan_list of this DownUpTimeForSimCardReq.
        :rtype: list[SimPricePlanInfoVO]
        """
        return self._price_plan_list

    @price_plan_list.setter
    def price_plan_list(self, price_plan_list):
        """Sets the price_plan_list of this DownUpTimeForSimCardReq.

        套餐列表

        :param price_plan_list: The price_plan_list of this DownUpTimeForSimCardReq.
        :type: list[SimPricePlanInfoVO]
        """
        self._price_plan_list = price_plan_list

    @property
    def down_up_switch(self):
        """Gets the down_up_switch of this DownUpTimeForSimCardReq.

        启用停用开关

        :return: The down_up_switch of this DownUpTimeForSimCardReq.
        :rtype: int
        """
        return self._down_up_switch

    @down_up_switch.setter
    def down_up_switch(self, down_up_switch):
        """Sets the down_up_switch of this DownUpTimeForSimCardReq.

        启用停用开关

        :param down_up_switch: The down_up_switch of this DownUpTimeForSimCardReq.
        :type: int
        """
        self._down_up_switch = down_up_switch

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
        if not isinstance(other, DownUpTimeForSimCardReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
