# coding: utf-8

import pprint
import re

import six





class ListEventsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'event_type': 'str',
        'event_name': 'str',
        '_from': 'int',
        'to': 'int',
        'start': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'event_type': 'event_type',
        'event_name': 'event_name',
        '_from': 'from',
        'to': 'to',
        'start': 'start',
        'limit': 'limit'
    }

    def __init__(self, event_type=None, event_name=None, _from=None, to=None, start=None, limit=None):
        """ListEventsRequest - a model defined in huaweicloud sdk"""
        
        

        self._event_type = None
        self._event_name = None
        self.__from = None
        self._to = None
        self._start = None
        self._limit = None
        self.discriminator = None

        if event_type is not None:
            self.event_type = event_type
        if event_name is not None:
            self.event_name = event_name
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if start is not None:
            self.start = start
        if limit is not None:
            self.limit = limit

    @property
    def event_type(self):
        """Gets the event_type of this ListEventsRequest.


        :return: The event_type of this ListEventsRequest.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this ListEventsRequest.


        :param event_type: The event_type of this ListEventsRequest.
        :type: str
        """
        self._event_type = event_type

    @property
    def event_name(self):
        """Gets the event_name of this ListEventsRequest.


        :return: The event_name of this ListEventsRequest.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this ListEventsRequest.


        :param event_name: The event_name of this ListEventsRequest.
        :type: str
        """
        self._event_name = event_name

    @property
    def _from(self):
        """Gets the _from of this ListEventsRequest.


        :return: The _from of this ListEventsRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this ListEventsRequest.


        :param _from: The _from of this ListEventsRequest.
        :type: int
        """
        self.__from = _from

    @property
    def to(self):
        """Gets the to of this ListEventsRequest.


        :return: The to of this ListEventsRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this ListEventsRequest.


        :param to: The to of this ListEventsRequest.
        :type: int
        """
        self._to = to

    @property
    def start(self):
        """Gets the start of this ListEventsRequest.


        :return: The start of this ListEventsRequest.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ListEventsRequest.


        :param start: The start of this ListEventsRequest.
        :type: int
        """
        self._start = start

    @property
    def limit(self):
        """Gets the limit of this ListEventsRequest.


        :return: The limit of this ListEventsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEventsRequest.


        :param limit: The limit of this ListEventsRequest.
        :type: int
        """
        self._limit = limit

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
        if not isinstance(other, ListEventsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
