# coding: utf-8

import pprint
import re

import six





class ChangingTheDelayThresholdRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'delay_threshold_in_kilobytes': 'int'
    }

    attribute_map = {
        'delay_threshold_in_kilobytes': 'delay_threshold_in_kilobytes'
    }

    def __init__(self, delay_threshold_in_kilobytes=None):
        """ChangingTheDelayThresholdRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._delay_threshold_in_kilobytes = None
        self.discriminator = None

        self.delay_threshold_in_kilobytes = delay_threshold_in_kilobytes

    @property
    def delay_threshold_in_kilobytes(self):
        """Gets the delay_threshold_in_kilobytes of this ChangingTheDelayThresholdRequestBody.

        延时阈值，单位是KB。

        :return: The delay_threshold_in_kilobytes of this ChangingTheDelayThresholdRequestBody.
        :rtype: int
        """
        return self._delay_threshold_in_kilobytes

    @delay_threshold_in_kilobytes.setter
    def delay_threshold_in_kilobytes(self, delay_threshold_in_kilobytes):
        """Sets the delay_threshold_in_kilobytes of this ChangingTheDelayThresholdRequestBody.

        延时阈值，单位是KB。

        :param delay_threshold_in_kilobytes: The delay_threshold_in_kilobytes of this ChangingTheDelayThresholdRequestBody.
        :type: int
        """
        self._delay_threshold_in_kilobytes = delay_threshold_in_kilobytes

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
        if not isinstance(other, ChangingTheDelayThresholdRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
