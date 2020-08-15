# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListNotifyEventResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'event_name': 'list[str]',
        'total': 'int'
    }

    attribute_map = {
        'event_name': 'event_name',
        'total': 'total'
    }

    def __init__(self, event_name=None, total=None):
        """ListNotifyEventResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._event_name = None
        self._total = None
        self.discriminator = None

        if event_name is not None:
            self.event_name = event_name
        if total is not None:
            self.total = total

    @property
    def event_name(self):
        """Gets the event_name of this ListNotifyEventResponse.

        事件名称

        :return: The event_name of this ListNotifyEventResponse.
        :rtype: list[str]
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this ListNotifyEventResponse.

        事件名称

        :param event_name: The event_name of this ListNotifyEventResponse.
        :type: list[str]
        """
        self._event_name = event_name

    @property
    def total(self):
        """Gets the total of this ListNotifyEventResponse.

        点播通知事件总数

        :return: The total of this ListNotifyEventResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListNotifyEventResponse.

        点播通知事件总数

        :param total: The total of this ListNotifyEventResponse.
        :type: int
        """
        self._total = total

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
        if not isinstance(other, ListNotifyEventResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
