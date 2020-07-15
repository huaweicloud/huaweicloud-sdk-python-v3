# coding: utf-8

import pprint
import re

import six





class ModifyAlarmActionReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'alarm_enabled': 'bool'
    }

    attribute_map = {
        'alarm_enabled': 'alarm_enabled'
    }

    def __init__(self, alarm_enabled=False):
        """ModifyAlarmActionReq - a model defined in huaweicloud sdk"""
        
        

        self._alarm_enabled = None
        self.discriminator = None

        self.alarm_enabled = alarm_enabled

    @property
    def alarm_enabled(self):
        """Gets the alarm_enabled of this ModifyAlarmActionReq.

        告警是否启用。true：启动。false：停止

        :return: The alarm_enabled of this ModifyAlarmActionReq.
        :rtype: bool
        """
        return self._alarm_enabled

    @alarm_enabled.setter
    def alarm_enabled(self, alarm_enabled):
        """Sets the alarm_enabled of this ModifyAlarmActionReq.

        告警是否启用。true：启动。false：停止

        :param alarm_enabled: The alarm_enabled of this ModifyAlarmActionReq.
        :type: bool
        """
        self._alarm_enabled = alarm_enabled

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
        if not isinstance(other, ModifyAlarmActionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
