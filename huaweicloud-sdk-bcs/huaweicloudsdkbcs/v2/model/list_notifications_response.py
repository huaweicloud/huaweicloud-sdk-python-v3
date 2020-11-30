# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListNotificationsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'notifications': 'list[NotificationList]'
    }

    attribute_map = {
        'notifications': 'notifications'
    }

    def __init__(self, notifications=None):
        """ListNotificationsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._notifications = None
        self.discriminator = None

        if notifications is not None:
            self.notifications = notifications

    @property
    def notifications(self):
        """Gets the notifications of this ListNotificationsResponse.

        通知列表

        :return: The notifications of this ListNotificationsResponse.
        :rtype: list[NotificationList]
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """Sets the notifications of this ListNotificationsResponse.

        通知列表

        :param notifications: The notifications of this ListNotificationsResponse.
        :type: list[NotificationList]
        """
        self._notifications = notifications

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
        if not isinstance(other, ListNotificationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
