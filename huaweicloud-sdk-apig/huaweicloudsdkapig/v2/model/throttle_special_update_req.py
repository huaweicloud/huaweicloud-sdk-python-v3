# coding: utf-8

import pprint
import re

import six





class ThrottleSpecialUpdateReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'call_limits': 'int'
    }

    attribute_map = {
        'call_limits': 'call_limits'
    }

    def __init__(self, call_limits=None):
        """ThrottleSpecialUpdateReq - a model defined in huaweicloud sdk"""
        
        

        self._call_limits = None
        self.discriminator = None

        self.call_limits = call_limits

    @property
    def call_limits(self):
        """Gets the call_limits of this ThrottleSpecialUpdateReq.

        流控时间内特殊对象能够访问API的最大次数限制

        :return: The call_limits of this ThrottleSpecialUpdateReq.
        :rtype: int
        """
        return self._call_limits

    @call_limits.setter
    def call_limits(self, call_limits):
        """Sets the call_limits of this ThrottleSpecialUpdateReq.

        流控时间内特殊对象能够访问API的最大次数限制

        :param call_limits: The call_limits of this ThrottleSpecialUpdateReq.
        :type: int
        """
        self._call_limits = call_limits

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
        if not isinstance(other, ThrottleSpecialUpdateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
