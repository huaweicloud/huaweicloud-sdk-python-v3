# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListOrderDiscountsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'discounts': 'list[DiscountInfoV3]'
    }

    attribute_map = {
        'discounts': 'discounts'
    }

    def __init__(self, discounts=None):
        """ListOrderDiscountsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._discounts = None
        self.discriminator = None

        if discounts is not None:
            self.discounts = discounts

    @property
    def discounts(self):
        """Gets the discounts of this ListOrderDiscountsResponse.

        |参数名称：可用的优惠券列表。具体请参见表1-30。| |参数约束以及描述：可用的优惠券列表。具体请参见表1-30。|

        :return: The discounts of this ListOrderDiscountsResponse.
        :rtype: list[DiscountInfoV3]
        """
        return self._discounts

    @discounts.setter
    def discounts(self, discounts):
        """Sets the discounts of this ListOrderDiscountsResponse.

        |参数名称：可用的优惠券列表。具体请参见表1-30。| |参数约束以及描述：可用的优惠券列表。具体请参见表1-30。|

        :param discounts: The discounts of this ListOrderDiscountsResponse.
        :type: list[DiscountInfoV3]
        """
        self._discounts = discounts

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
        if not isinstance(other, ListOrderDiscountsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
