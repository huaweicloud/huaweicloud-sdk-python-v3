# coding: utf-8

import pprint
import re

import six





class CreateEventsResponseBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'event_id': 'str',
        'event_name': 'str'
    }

    attribute_map = {
        'event_id': 'event_id',
        'event_name': 'event_name'
    }

    def __init__(self, event_id=None, event_name=None):
        """CreateEventsResponseBody - a model defined in huaweicloud sdk"""
        
        

        self._event_id = None
        self._event_name = None
        self.discriminator = None

        self.event_id = event_id
        self.event_name = event_name

    @property
    def event_id(self):
        """Gets the event_id of this CreateEventsResponseBody.

        事件ID。

        :return: The event_id of this CreateEventsResponseBody.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this CreateEventsResponseBody.

        事件ID。

        :param event_id: The event_id of this CreateEventsResponseBody.
        :type: str
        """
        self._event_id = event_id

    @property
    def event_name(self):
        """Gets the event_name of this CreateEventsResponseBody.

        事件名称。  必须以字母开头，只能包含0-9/a-z/A-Z/_，长度最短为1，最大为64。

        :return: The event_name of this CreateEventsResponseBody.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this CreateEventsResponseBody.

        事件名称。  必须以字母开头，只能包含0-9/a-z/A-Z/_，长度最短为1，最大为64。

        :param event_name: The event_name of this CreateEventsResponseBody.
        :type: str
        """
        self._event_name = event_name

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
        if not isinstance(other, CreateEventsResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
