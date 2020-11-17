# coding: utf-8

import pprint
import re

import six





class ShowResourceHistoryRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'marker': 'str',
        'limit': 'int',
        'earlier_time': 'int',
        'later_time': 'int',
        'chronological_order': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'marker': 'marker',
        'limit': 'limit',
        'earlier_time': 'earlier_time',
        'later_time': 'later_time',
        'chronological_order': 'chronological_order'
    }

    def __init__(self, resource_id=None, marker=None, limit=None, earlier_time=None, later_time=None, chronological_order=None):
        """ShowResourceHistoryRequest - a model defined in huaweicloud sdk"""
        
        

        self._resource_id = None
        self._marker = None
        self._limit = None
        self._earlier_time = None
        self._later_time = None
        self._chronological_order = None
        self.discriminator = None

        self.resource_id = resource_id
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if earlier_time is not None:
            self.earlier_time = earlier_time
        if later_time is not None:
            self.later_time = later_time
        if chronological_order is not None:
            self.chronological_order = chronological_order

    @property
    def resource_id(self):
        """Gets the resource_id of this ShowResourceHistoryRequest.


        :return: The resource_id of this ShowResourceHistoryRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ShowResourceHistoryRequest.


        :param resource_id: The resource_id of this ShowResourceHistoryRequest.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def marker(self):
        """Gets the marker of this ShowResourceHistoryRequest.


        :return: The marker of this ShowResourceHistoryRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ShowResourceHistoryRequest.


        :param marker: The marker of this ShowResourceHistoryRequest.
        :type: str
        """
        self._marker = marker

    @property
    def limit(self):
        """Gets the limit of this ShowResourceHistoryRequest.


        :return: The limit of this ShowResourceHistoryRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowResourceHistoryRequest.


        :param limit: The limit of this ShowResourceHistoryRequest.
        :type: int
        """
        self._limit = limit

    @property
    def earlier_time(self):
        """Gets the earlier_time of this ShowResourceHistoryRequest.


        :return: The earlier_time of this ShowResourceHistoryRequest.
        :rtype: int
        """
        return self._earlier_time

    @earlier_time.setter
    def earlier_time(self, earlier_time):
        """Sets the earlier_time of this ShowResourceHistoryRequest.


        :param earlier_time: The earlier_time of this ShowResourceHistoryRequest.
        :type: int
        """
        self._earlier_time = earlier_time

    @property
    def later_time(self):
        """Gets the later_time of this ShowResourceHistoryRequest.


        :return: The later_time of this ShowResourceHistoryRequest.
        :rtype: int
        """
        return self._later_time

    @later_time.setter
    def later_time(self, later_time):
        """Sets the later_time of this ShowResourceHistoryRequest.


        :param later_time: The later_time of this ShowResourceHistoryRequest.
        :type: int
        """
        self._later_time = later_time

    @property
    def chronological_order(self):
        """Gets the chronological_order of this ShowResourceHistoryRequest.


        :return: The chronological_order of this ShowResourceHistoryRequest.
        :rtype: str
        """
        return self._chronological_order

    @chronological_order.setter
    def chronological_order(self, chronological_order):
        """Sets the chronological_order of this ShowResourceHistoryRequest.


        :param chronological_order: The chronological_order of this ShowResourceHistoryRequest.
        :type: str
        """
        self._chronological_order = chronological_order

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
        if not isinstance(other, ShowResourceHistoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
