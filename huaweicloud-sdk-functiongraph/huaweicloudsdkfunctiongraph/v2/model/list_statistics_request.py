# coding: utf-8

import pprint
import re

import six





class ListStatisticsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'filter': 'str',
        'period': 'str',
        'month_code': 'str'
    }

    attribute_map = {
        'filter': 'filter',
        'period': 'period',
        'month_code': 'month_code'
    }

    def __init__(self, filter=None, period=None, month_code=None):
        """ListStatisticsRequest - a model defined in huaweicloud sdk"""
        
        

        self._filter = None
        self._period = None
        self._month_code = None
        self.discriminator = None

        self.filter = filter
        if period is not None:
            self.period = period
        self.month_code = month_code

    @property
    def filter(self):
        """Gets the filter of this ListStatisticsRequest.


        :return: The filter of this ListStatisticsRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ListStatisticsRequest.


        :param filter: The filter of this ListStatisticsRequest.
        :type: str
        """
        self._filter = filter

    @property
    def period(self):
        """Gets the period of this ListStatisticsRequest.


        :return: The period of this ListStatisticsRequest.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ListStatisticsRequest.


        :param period: The period of this ListStatisticsRequest.
        :type: str
        """
        self._period = period

    @property
    def month_code(self):
        """Gets the month_code of this ListStatisticsRequest.


        :return: The month_code of this ListStatisticsRequest.
        :rtype: str
        """
        return self._month_code

    @month_code.setter
    def month_code(self, month_code):
        """Sets the month_code of this ListStatisticsRequest.


        :param month_code: The month_code of this ListStatisticsRequest.
        :type: str
        """
        self._month_code = month_code

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
        if not isinstance(other, ListStatisticsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
