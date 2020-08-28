# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListCustomersBalancesDetailResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'customer_balances': 'list[CustomerBalancesV2]'
    }

    attribute_map = {
        'customer_balances': 'customer_balances'
    }

    def __init__(self, customer_balances=None):
        """ListCustomersBalancesDetailResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._customer_balances = None
        self.discriminator = None

        if customer_balances is not None:
            self.customer_balances = customer_balances

    @property
    def customer_balances(self):
        """Gets the customer_balances of this ListCustomersBalancesDetailResponse.

        |参数名称：总额，即最终优惠后的金额，| |参数约束以及描述：总额，即最终优惠后的金额，|

        :return: The customer_balances of this ListCustomersBalancesDetailResponse.
        :rtype: list[CustomerBalancesV2]
        """
        return self._customer_balances

    @customer_balances.setter
    def customer_balances(self, customer_balances):
        """Sets the customer_balances of this ListCustomersBalancesDetailResponse.

        |参数名称：总额，即最终优惠后的金额，| |参数约束以及描述：总额，即最终优惠后的金额，|

        :param customer_balances: The customer_balances of this ListCustomersBalancesDetailResponse.
        :type: list[CustomerBalancesV2]
        """
        self._customer_balances = customer_balances

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
        if not isinstance(other, ListCustomersBalancesDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
