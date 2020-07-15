# coding: utf-8

import pprint
import re

import six





class ListScalingActivityLogsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'scaling_group_id': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'start_number': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'scaling_group_id': 'scaling_group_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'start_number': 'start_number',
        'limit': 'limit'
    }

    def __init__(self, scaling_group_id=None, start_time=None, end_time=None, start_number=None, limit=None):
        """ListScalingActivityLogsRequest - a model defined in huaweicloud sdk"""
        
        

        self._scaling_group_id = None
        self._start_time = None
        self._end_time = None
        self._start_number = None
        self._limit = None
        self.discriminator = None

        self.scaling_group_id = scaling_group_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if start_number is not None:
            self.start_number = start_number
        if limit is not None:
            self.limit = limit

    @property
    def scaling_group_id(self):
        """Gets the scaling_group_id of this ListScalingActivityLogsRequest.


        :return: The scaling_group_id of this ListScalingActivityLogsRequest.
        :rtype: str
        """
        return self._scaling_group_id

    @scaling_group_id.setter
    def scaling_group_id(self, scaling_group_id):
        """Sets the scaling_group_id of this ListScalingActivityLogsRequest.


        :param scaling_group_id: The scaling_group_id of this ListScalingActivityLogsRequest.
        :type: str
        """
        self._scaling_group_id = scaling_group_id

    @property
    def start_time(self):
        """Gets the start_time of this ListScalingActivityLogsRequest.


        :return: The start_time of this ListScalingActivityLogsRequest.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListScalingActivityLogsRequest.


        :param start_time: The start_time of this ListScalingActivityLogsRequest.
        :type: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListScalingActivityLogsRequest.


        :return: The end_time of this ListScalingActivityLogsRequest.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListScalingActivityLogsRequest.


        :param end_time: The end_time of this ListScalingActivityLogsRequest.
        :type: datetime
        """
        self._end_time = end_time

    @property
    def start_number(self):
        """Gets the start_number of this ListScalingActivityLogsRequest.


        :return: The start_number of this ListScalingActivityLogsRequest.
        :rtype: int
        """
        return self._start_number

    @start_number.setter
    def start_number(self, start_number):
        """Sets the start_number of this ListScalingActivityLogsRequest.


        :param start_number: The start_number of this ListScalingActivityLogsRequest.
        :type: int
        """
        self._start_number = start_number

    @property
    def limit(self):
        """Gets the limit of this ListScalingActivityLogsRequest.


        :return: The limit of this ListScalingActivityLogsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListScalingActivityLogsRequest.


        :param limit: The limit of this ListScalingActivityLogsRequest.
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
        if not isinstance(other, ListScalingActivityLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
