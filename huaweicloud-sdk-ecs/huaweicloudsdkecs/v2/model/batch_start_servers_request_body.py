# coding: utf-8

import pprint
import re

import six





class BatchStartServersRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'os_start': 'BatchStartServersOption'
    }

    attribute_map = {
        'os_start': 'os-start'
    }

    def __init__(self, os_start=None):
        """BatchStartServersRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._os_start = None
        self.discriminator = None

        self.os_start = os_start

    @property
    def os_start(self):
        """Gets the os_start of this BatchStartServersRequestBody.


        :return: The os_start of this BatchStartServersRequestBody.
        :rtype: BatchStartServersOption
        """
        return self._os_start

    @os_start.setter
    def os_start(self, os_start):
        """Sets the os_start of this BatchStartServersRequestBody.


        :param os_start: The os_start of this BatchStartServersRequestBody.
        :type: BatchStartServersOption
        """
        self._os_start = os_start

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
        if not isinstance(other, BatchStartServersRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
