# coding: utf-8

import pprint
import re

import six





class ListTracesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'trace_type': 'str',
        'limit': 'int',
        '_from': 'int',
        'next': 'str',
        'to': 'int',
        'tracker_name': 'str',
        'service_type': 'str',
        'user': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'resource_type': 'str',
        'trace_id': 'str',
        'trace_name': 'str',
        'trace_rating': 'str'
    }

    attribute_map = {
        'trace_type': 'trace_type',
        'limit': 'limit',
        '_from': 'from',
        'next': 'next',
        'to': 'to',
        'tracker_name': 'tracker_name',
        'service_type': 'service_type',
        'user': 'user',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_type': 'resource_type',
        'trace_id': 'trace_id',
        'trace_name': 'trace_name',
        'trace_rating': 'trace_rating'
    }

    def __init__(self, trace_type=None, limit=None, _from=None, next=None, to=None, tracker_name=None, service_type=None, user=None, resource_id=None, resource_name=None, resource_type=None, trace_id=None, trace_name=None, trace_rating=None):
        """ListTracesRequest - a model defined in huaweicloud sdk"""
        
        

        self._trace_type = None
        self._limit = None
        self.__from = None
        self._next = None
        self._to = None
        self._tracker_name = None
        self._service_type = None
        self._user = None
        self._resource_id = None
        self._resource_name = None
        self._resource_type = None
        self._trace_id = None
        self._trace_name = None
        self._trace_rating = None
        self.discriminator = None

        self.trace_type = trace_type
        if limit is not None:
            self.limit = limit
        if _from is not None:
            self._from = _from
        if next is not None:
            self.next = next
        if to is not None:
            self.to = to
        if tracker_name is not None:
            self.tracker_name = tracker_name
        if service_type is not None:
            self.service_type = service_type
        if user is not None:
            self.user = user
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_type is not None:
            self.resource_type = resource_type
        if trace_id is not None:
            self.trace_id = trace_id
        if trace_name is not None:
            self.trace_name = trace_name
        if trace_rating is not None:
            self.trace_rating = trace_rating

    @property
    def trace_type(self):
        """Gets the trace_type of this ListTracesRequest.


        :return: The trace_type of this ListTracesRequest.
        :rtype: str
        """
        return self._trace_type

    @trace_type.setter
    def trace_type(self, trace_type):
        """Sets the trace_type of this ListTracesRequest.


        :param trace_type: The trace_type of this ListTracesRequest.
        :type: str
        """
        self._trace_type = trace_type

    @property
    def limit(self):
        """Gets the limit of this ListTracesRequest.


        :return: The limit of this ListTracesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTracesRequest.


        :param limit: The limit of this ListTracesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def _from(self):
        """Gets the _from of this ListTracesRequest.


        :return: The _from of this ListTracesRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this ListTracesRequest.


        :param _from: The _from of this ListTracesRequest.
        :type: int
        """
        self.__from = _from

    @property
    def next(self):
        """Gets the next of this ListTracesRequest.


        :return: The next of this ListTracesRequest.
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this ListTracesRequest.


        :param next: The next of this ListTracesRequest.
        :type: str
        """
        self._next = next

    @property
    def to(self):
        """Gets the to of this ListTracesRequest.


        :return: The to of this ListTracesRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this ListTracesRequest.


        :param to: The to of this ListTracesRequest.
        :type: int
        """
        self._to = to

    @property
    def tracker_name(self):
        """Gets the tracker_name of this ListTracesRequest.


        :return: The tracker_name of this ListTracesRequest.
        :rtype: str
        """
        return self._tracker_name

    @tracker_name.setter
    def tracker_name(self, tracker_name):
        """Sets the tracker_name of this ListTracesRequest.


        :param tracker_name: The tracker_name of this ListTracesRequest.
        :type: str
        """
        self._tracker_name = tracker_name

    @property
    def service_type(self):
        """Gets the service_type of this ListTracesRequest.


        :return: The service_type of this ListTracesRequest.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this ListTracesRequest.


        :param service_type: The service_type of this ListTracesRequest.
        :type: str
        """
        self._service_type = service_type

    @property
    def user(self):
        """Gets the user of this ListTracesRequest.


        :return: The user of this ListTracesRequest.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ListTracesRequest.


        :param user: The user of this ListTracesRequest.
        :type: str
        """
        self._user = user

    @property
    def resource_id(self):
        """Gets the resource_id of this ListTracesRequest.


        :return: The resource_id of this ListTracesRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ListTracesRequest.


        :param resource_id: The resource_id of this ListTracesRequest.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this ListTracesRequest.


        :return: The resource_name of this ListTracesRequest.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ListTracesRequest.


        :param resource_name: The resource_name of this ListTracesRequest.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        """Gets the resource_type of this ListTracesRequest.


        :return: The resource_type of this ListTracesRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ListTracesRequest.


        :param resource_type: The resource_type of this ListTracesRequest.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def trace_id(self):
        """Gets the trace_id of this ListTracesRequest.


        :return: The trace_id of this ListTracesRequest.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        """Sets the trace_id of this ListTracesRequest.


        :param trace_id: The trace_id of this ListTracesRequest.
        :type: str
        """
        self._trace_id = trace_id

    @property
    def trace_name(self):
        """Gets the trace_name of this ListTracesRequest.


        :return: The trace_name of this ListTracesRequest.
        :rtype: str
        """
        return self._trace_name

    @trace_name.setter
    def trace_name(self, trace_name):
        """Sets the trace_name of this ListTracesRequest.


        :param trace_name: The trace_name of this ListTracesRequest.
        :type: str
        """
        self._trace_name = trace_name

    @property
    def trace_rating(self):
        """Gets the trace_rating of this ListTracesRequest.


        :return: The trace_rating of this ListTracesRequest.
        :rtype: str
        """
        return self._trace_rating

    @trace_rating.setter
    def trace_rating(self, trace_rating):
        """Sets the trace_rating of this ListTracesRequest.


        :param trace_rating: The trace_rating of this ListTracesRequest.
        :type: str
        """
        self._trace_rating = trace_rating

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
        if not isinstance(other, ListTracesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
