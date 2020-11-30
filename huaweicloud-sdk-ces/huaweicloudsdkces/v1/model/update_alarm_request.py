# coding: utf-8

import pprint
import re

import six





class UpdateAlarmRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'alarm_id': 'str',
        'body': 'UpdateAlarmRequestBody'
    }

    attribute_map = {
        'alarm_id': 'alarm_id',
        'body': 'body'
    }

    def __init__(self, alarm_id='al15454523384878yogJg6ao', body=None):
        """UpdateAlarmRequest - a model defined in huaweicloud sdk"""
        
        

        self._alarm_id = None
        self._body = None
        self.discriminator = None

        self.alarm_id = alarm_id
        if body is not None:
            self.body = body

    @property
    def alarm_id(self):
        """Gets the alarm_id of this UpdateAlarmRequest.


        :return: The alarm_id of this UpdateAlarmRequest.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        """Sets the alarm_id of this UpdateAlarmRequest.


        :param alarm_id: The alarm_id of this UpdateAlarmRequest.
        :type: str
        """
        self._alarm_id = alarm_id

    @property
    def body(self):
        """Gets the body of this UpdateAlarmRequest.


        :return: The body of this UpdateAlarmRequest.
        :rtype: UpdateAlarmRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateAlarmRequest.


        :param body: The body of this UpdateAlarmRequest.
        :type: UpdateAlarmRequestBody
        """
        self._body = body

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
        if not isinstance(other, UpdateAlarmRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
