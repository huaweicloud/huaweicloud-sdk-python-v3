# coding: utf-8

import pprint
import re

import six





class DeviceStatusCondition:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'status_list': 'list[str]'
    }

    attribute_map = {
        'status_list': 'status_list'
    }

    def __init__(self, status_list=None):
        """DeviceStatusCondition - a model defined in huaweicloud sdk"""
        
        

        self._status_list = None
        self.discriminator = None

        if status_list is not None:
            self.status_list = status_list

    @property
    def status_list(self):
        """Gets the status_list of this DeviceStatusCondition.

        状态列表，设备状态条件携带该参数。

        :return: The status_list of this DeviceStatusCondition.
        :rtype: list[str]
        """
        return self._status_list

    @status_list.setter
    def status_list(self, status_list):
        """Sets the status_list of this DeviceStatusCondition.

        状态列表，设备状态条件携带该参数。

        :param status_list: The status_list of this DeviceStatusCondition.
        :type: list[str]
        """
        self._status_list = status_list

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
        if not isinstance(other, DeviceStatusCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
