# coding: utf-8

import pprint
import re

import six





class ListQueuesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'include_deadletter': 'bool'
    }

    attribute_map = {
        'include_deadletter': 'include_deadletter'
    }

    def __init__(self, include_deadletter=None):
        """ListQueuesRequest - a model defined in huaweicloud sdk"""
        
        

        self._include_deadletter = None
        self.discriminator = None

        if include_deadletter is not None:
            self.include_deadletter = include_deadletter

    @property
    def include_deadletter(self):
        """Gets the include_deadletter of this ListQueuesRequest.


        :return: The include_deadletter of this ListQueuesRequest.
        :rtype: bool
        """
        return self._include_deadletter

    @include_deadletter.setter
    def include_deadletter(self, include_deadletter):
        """Sets the include_deadletter of this ListQueuesRequest.


        :param include_deadletter: The include_deadletter of this ListQueuesRequest.
        :type: bool
        """
        self._include_deadletter = include_deadletter

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
        if not isinstance(other, ListQueuesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
