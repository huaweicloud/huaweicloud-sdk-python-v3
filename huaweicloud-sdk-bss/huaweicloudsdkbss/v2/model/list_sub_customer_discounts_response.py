# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListSubCustomerDiscountsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'sub_customer_discount': 'QuerySubCustomerDiscountV2'
    }

    attribute_map = {
        'sub_customer_discount': 'sub_customer_discount'
    }

    def __init__(self, sub_customer_discount=None):
        """ListSubCustomerDiscountsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._sub_customer_discount = None
        self.discriminator = None

        if sub_customer_discount is not None:
            self.sub_customer_discount = sub_customer_discount

    @property
    def sub_customer_discount(self):
        """Gets the sub_customer_discount of this ListSubCustomerDiscountsResponse.


        :return: The sub_customer_discount of this ListSubCustomerDiscountsResponse.
        :rtype: QuerySubCustomerDiscountV2
        """
        return self._sub_customer_discount

    @sub_customer_discount.setter
    def sub_customer_discount(self, sub_customer_discount):
        """Sets the sub_customer_discount of this ListSubCustomerDiscountsResponse.


        :param sub_customer_discount: The sub_customer_discount of this ListSubCustomerDiscountsResponse.
        :type: QuerySubCustomerDiscountV2
        """
        self._sub_customer_discount = sub_customer_discount

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
        if not isinstance(other, ListSubCustomerDiscountsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
