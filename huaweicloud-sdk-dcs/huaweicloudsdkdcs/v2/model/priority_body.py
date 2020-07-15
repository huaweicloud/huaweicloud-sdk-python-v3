# coding: utf-8

import pprint
import re

import six





class PriorityBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'slave_priority_weight': 'int'
    }

    attribute_map = {
        'slave_priority_weight': 'slave_priority_weight'
    }

    def __init__(self, slave_priority_weight=None):
        """PriorityBody - a model defined in huaweicloud sdk"""
        
        

        self._slave_priority_weight = None
        self.discriminator = None

        self.slave_priority_weight = slave_priority_weight

    @property
    def slave_priority_weight(self):
        """Gets the slave_priority_weight of this PriorityBody.

        副本优先级，取值范围是0到100，0为默认禁止倒换。

        :return: The slave_priority_weight of this PriorityBody.
        :rtype: int
        """
        return self._slave_priority_weight

    @slave_priority_weight.setter
    def slave_priority_weight(self, slave_priority_weight):
        """Sets the slave_priority_weight of this PriorityBody.

        副本优先级，取值范围是0到100，0为默认禁止倒换。

        :param slave_priority_weight: The slave_priority_weight of this PriorityBody.
        :type: int
        """
        self._slave_priority_weight = slave_priority_weight

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
        if not isinstance(other, PriorityBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
