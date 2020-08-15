# coding: utf-8

import pprint
import re

import six





class ListStatSummaryRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'end_time': 'str',
        'stat_type': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'stat_type': 'stat_type'
    }

    def __init__(self, start_time=None, end_time=None, stat_type=None):
        """ListStatSummaryRequest - a model defined in huaweicloud sdk"""
        
        

        self._start_time = None
        self._end_time = None
        self._stat_type = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        self.stat_type = stat_type

    @property
    def start_time(self):
        """Gets the start_time of this ListStatSummaryRequest.


        :return: The start_time of this ListStatSummaryRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListStatSummaryRequest.


        :param start_time: The start_time of this ListStatSummaryRequest.
        :type: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListStatSummaryRequest.


        :return: The end_time of this ListStatSummaryRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListStatSummaryRequest.


        :param end_time: The end_time of this ListStatSummaryRequest.
        :type: str
        """
        self._end_time = end_time

    @property
    def stat_type(self):
        """Gets the stat_type of this ListStatSummaryRequest.


        :return: The stat_type of this ListStatSummaryRequest.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        """Sets the stat_type of this ListStatSummaryRequest.


        :param stat_type: The stat_type of this ListStatSummaryRequest.
        :type: str
        """
        self._stat_type = stat_type

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
        if not isinstance(other, ListStatSummaryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
