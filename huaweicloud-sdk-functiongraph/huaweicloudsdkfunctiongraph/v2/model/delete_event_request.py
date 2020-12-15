# coding: utf-8

import pprint
import re

import six





class DeleteEventRequest:


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
        'function_urn': 'str'
    }

    attribute_map = {
        'event_id': 'event_id',
        'function_urn': 'function_urn'
    }

    def __init__(self, event_id=None, function_urn=None):
        """DeleteEventRequest - a model defined in huaweicloud sdk"""
        
        

        self._event_id = None
        self._function_urn = None
        self.discriminator = None

        self.event_id = event_id
        self.function_urn = function_urn

    @property
    def event_id(self):
        """Gets the event_id of this DeleteEventRequest.


        :return: The event_id of this DeleteEventRequest.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this DeleteEventRequest.


        :param event_id: The event_id of this DeleteEventRequest.
        :type: str
        """
        self._event_id = event_id

    @property
    def function_urn(self):
        """Gets the function_urn of this DeleteEventRequest.


        :return: The function_urn of this DeleteEventRequest.
        :rtype: str
        """
        return self._function_urn

    @function_urn.setter
    def function_urn(self, function_urn):
        """Sets the function_urn of this DeleteEventRequest.


        :param function_urn: The function_urn of this DeleteEventRequest.
        :type: str
        """
        self._function_urn = function_urn

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
        if not isinstance(other, DeleteEventRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
