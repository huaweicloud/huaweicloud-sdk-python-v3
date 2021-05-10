# coding: utf-8

import pprint
import re

import six





class DemandResp:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'demand_count': 'int'
    }

    attribute_map = {
        'demand_count': 'demand_count'
    }

    def __init__(self, demand_count=None):
        """DemandResp - a model defined in huaweicloud sdk"""
        
        

        self._demand_count = None
        self.discriminator = None

        self.demand_count = demand_count

    @property
    def demand_count(self):
        """Gets the demand_count of this DemandResp.

        站点需要发放的资源(组)总数。  > 实际发放实例数量为count*demand_count。

        :return: The demand_count of this DemandResp.
        :rtype: int
        """
        return self._demand_count

    @demand_count.setter
    def demand_count(self, demand_count):
        """Sets the demand_count of this DemandResp.

        站点需要发放的资源(组)总数。  > 实际发放实例数量为count*demand_count。

        :param demand_count: The demand_count of this DemandResp.
        :type: int
        """
        self._demand_count = demand_count

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
        if not isinstance(other, DemandResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
