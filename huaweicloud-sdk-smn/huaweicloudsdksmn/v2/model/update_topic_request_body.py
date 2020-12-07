# coding: utf-8

import pprint
import re

import six





class UpdateTopicRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'display_name': 'str'
    }

    attribute_map = {
        'display_name': 'display_name'
    }

    def __init__(self, display_name=None):
        """UpdateTopicRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._display_name = None
        self.discriminator = None

        self.display_name = display_name

    @property
    def display_name(self):
        """Gets the display_name of this UpdateTopicRequestBody.

        Topic的显示名，推送邮件消息时，作为邮件发件人显示。显示名的长度为192byte或64个中文。

        :return: The display_name of this UpdateTopicRequestBody.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this UpdateTopicRequestBody.

        Topic的显示名，推送邮件消息时，作为邮件发件人显示。显示名的长度为192byte或64个中文。

        :param display_name: The display_name of this UpdateTopicRequestBody.
        :type: str
        """
        self._display_name = display_name

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
        if not isinstance(other, UpdateTopicRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
