# coding: utf-8

import pprint
import re

import six





class UpdateAutoTerminateTimeServerRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'auto_terminate_time': 'str'
    }

    attribute_map = {
        'auto_terminate_time': 'auto_terminate_time'
    }

    def __init__(self, auto_terminate_time=None):
        """UpdateAutoTerminateTimeServerRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._auto_terminate_time = None
        self.discriminator = None

        self.auto_terminate_time = auto_terminate_time

    @property
    def auto_terminate_time(self):
        """Gets the auto_terminate_time of this UpdateAutoTerminateTimeServerRequestBody.

        销毁时间

        :return: The auto_terminate_time of this UpdateAutoTerminateTimeServerRequestBody.
        :rtype: str
        """
        return self._auto_terminate_time

    @auto_terminate_time.setter
    def auto_terminate_time(self, auto_terminate_time):
        """Sets the auto_terminate_time of this UpdateAutoTerminateTimeServerRequestBody.

        销毁时间

        :param auto_terminate_time: The auto_terminate_time of this UpdateAutoTerminateTimeServerRequestBody.
        :type: str
        """
        self._auto_terminate_time = auto_terminate_time

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
        if not isinstance(other, UpdateAutoTerminateTimeServerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
