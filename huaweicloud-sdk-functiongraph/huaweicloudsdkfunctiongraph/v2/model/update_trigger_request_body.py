# coding: utf-8

import pprint
import re

import six





class UpdateTriggerRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'trigger_status': 'str'
    }

    attribute_map = {
        'trigger_status': 'trigger_status'
    }

    def __init__(self, trigger_status=None):
        """UpdateTriggerRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._trigger_status = None
        self.discriminator = None

        if trigger_status is not None:
            self.trigger_status = trigger_status

    @property
    def trigger_status(self):
        """Gets the trigger_status of this UpdateTriggerRequestBody.

        触发器状态

        :return: The trigger_status of this UpdateTriggerRequestBody.
        :rtype: str
        """
        return self._trigger_status

    @trigger_status.setter
    def trigger_status(self, trigger_status):
        """Sets the trigger_status of this UpdateTriggerRequestBody.

        触发器状态

        :param trigger_status: The trigger_status of this UpdateTriggerRequestBody.
        :type: str
        """
        self._trigger_status = trigger_status

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
        if not isinstance(other, UpdateTriggerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
