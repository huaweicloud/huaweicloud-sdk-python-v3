# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListEventsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'events': 'list[EventInfo]',
        'meta_data': 'TotalMetaData'
    }

    attribute_map = {
        'events': 'events',
        'meta_data': 'meta_data'
    }

    def __init__(self, events=None, meta_data=None):
        """ListEventsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._events = None
        self._meta_data = None
        self.discriminator = None

        if events is not None:
            self.events = events
        if meta_data is not None:
            self.meta_data = meta_data

    @property
    def events(self):
        """Gets the events of this ListEventsResponse.

        一条或者多条事件数据。

        :return: The events of this ListEventsResponse.
        :rtype: list[EventInfo]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this ListEventsResponse.

        一条或者多条事件数据。

        :param events: The events of this ListEventsResponse.
        :type: list[EventInfo]
        """
        self._events = events

    @property
    def meta_data(self):
        """Gets the meta_data of this ListEventsResponse.


        :return: The meta_data of this ListEventsResponse.
        :rtype: TotalMetaData
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this ListEventsResponse.


        :param meta_data: The meta_data of this ListEventsResponse.
        :type: TotalMetaData
        """
        self._meta_data = meta_data

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
        if not isinstance(other, ListEventsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
