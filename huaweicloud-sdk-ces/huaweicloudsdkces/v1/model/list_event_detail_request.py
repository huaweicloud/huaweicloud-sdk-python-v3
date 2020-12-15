# coding: utf-8

import pprint
import re

import six





class ListEventDetailRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'event_name': 'str',
        'event_type': 'str',
        'event_source': 'str',
        'event_level': 'str',
        'event_user': 'str',
        'event_state': 'str',
        '_from': 'int',
        'to': 'int',
        'start': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'event_name': 'event_name',
        'event_type': 'event_type',
        'event_source': 'event_source',
        'event_level': 'event_level',
        'event_user': 'event_user',
        'event_state': 'event_state',
        '_from': 'from',
        'to': 'to',
        'start': 'start',
        'limit': 'limit'
    }

    def __init__(self, event_name=None, event_type=None, event_source=None, event_level=None, event_user=None, event_state=None, _from=None, to=None, start=None, limit=None):
        """ListEventDetailRequest - a model defined in huaweicloud sdk"""
        
        

        self._event_name = None
        self._event_type = None
        self._event_source = None
        self._event_level = None
        self._event_user = None
        self._event_state = None
        self.__from = None
        self._to = None
        self._start = None
        self._limit = None
        self.discriminator = None

        self.event_name = event_name
        self.event_type = event_type
        if event_source is not None:
            self.event_source = event_source
        if event_level is not None:
            self.event_level = event_level
        if event_user is not None:
            self.event_user = event_user
        if event_state is not None:
            self.event_state = event_state
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if start is not None:
            self.start = start
        if limit is not None:
            self.limit = limit

    @property
    def event_name(self):
        """Gets the event_name of this ListEventDetailRequest.


        :return: The event_name of this ListEventDetailRequest.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this ListEventDetailRequest.


        :param event_name: The event_name of this ListEventDetailRequest.
        :type: str
        """
        self._event_name = event_name

    @property
    def event_type(self):
        """Gets the event_type of this ListEventDetailRequest.


        :return: The event_type of this ListEventDetailRequest.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this ListEventDetailRequest.


        :param event_type: The event_type of this ListEventDetailRequest.
        :type: str
        """
        self._event_type = event_type

    @property
    def event_source(self):
        """Gets the event_source of this ListEventDetailRequest.


        :return: The event_source of this ListEventDetailRequest.
        :rtype: str
        """
        return self._event_source

    @event_source.setter
    def event_source(self, event_source):
        """Sets the event_source of this ListEventDetailRequest.


        :param event_source: The event_source of this ListEventDetailRequest.
        :type: str
        """
        self._event_source = event_source

    @property
    def event_level(self):
        """Gets the event_level of this ListEventDetailRequest.


        :return: The event_level of this ListEventDetailRequest.
        :rtype: str
        """
        return self._event_level

    @event_level.setter
    def event_level(self, event_level):
        """Sets the event_level of this ListEventDetailRequest.


        :param event_level: The event_level of this ListEventDetailRequest.
        :type: str
        """
        self._event_level = event_level

    @property
    def event_user(self):
        """Gets the event_user of this ListEventDetailRequest.


        :return: The event_user of this ListEventDetailRequest.
        :rtype: str
        """
        return self._event_user

    @event_user.setter
    def event_user(self, event_user):
        """Sets the event_user of this ListEventDetailRequest.


        :param event_user: The event_user of this ListEventDetailRequest.
        :type: str
        """
        self._event_user = event_user

    @property
    def event_state(self):
        """Gets the event_state of this ListEventDetailRequest.


        :return: The event_state of this ListEventDetailRequest.
        :rtype: str
        """
        return self._event_state

    @event_state.setter
    def event_state(self, event_state):
        """Sets the event_state of this ListEventDetailRequest.


        :param event_state: The event_state of this ListEventDetailRequest.
        :type: str
        """
        self._event_state = event_state

    @property
    def _from(self):
        """Gets the _from of this ListEventDetailRequest.


        :return: The _from of this ListEventDetailRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this ListEventDetailRequest.


        :param _from: The _from of this ListEventDetailRequest.
        :type: int
        """
        self.__from = _from

    @property
    def to(self):
        """Gets the to of this ListEventDetailRequest.


        :return: The to of this ListEventDetailRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this ListEventDetailRequest.


        :param to: The to of this ListEventDetailRequest.
        :type: int
        """
        self._to = to

    @property
    def start(self):
        """Gets the start of this ListEventDetailRequest.


        :return: The start of this ListEventDetailRequest.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ListEventDetailRequest.


        :param start: The start of this ListEventDetailRequest.
        :type: int
        """
        self._start = start

    @property
    def limit(self):
        """Gets the limit of this ListEventDetailRequest.


        :return: The limit of this ListEventDetailRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEventDetailRequest.


        :param limit: The limit of this ListEventDetailRequest.
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
        if not isinstance(other, ListEventDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
