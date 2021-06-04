# coding: utf-8

import pprint
import re

import six





class RangeStatusRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'range_status': 'str'
    }

    attribute_map = {
        'range_status': 'range_status'
    }

    def __init__(self, range_status=None):
        """RangeStatusRequest - a model defined in huaweicloud sdk"""
        
        

        self._range_status = None
        self.discriminator = None

        self.range_status = range_status

    @property
    def range_status(self):
        """Gets the range_status of this RangeStatusRequest.

        range状态（\"off\"/\"on\"）

        :return: The range_status of this RangeStatusRequest.
        :rtype: str
        """
        return self._range_status

    @range_status.setter
    def range_status(self, range_status):
        """Sets the range_status of this RangeStatusRequest.

        range状态（\"off\"/\"on\"）

        :param range_status: The range_status of this RangeStatusRequest.
        :type: str
        """
        self._range_status = range_status

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
        if not isinstance(other, RangeStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
