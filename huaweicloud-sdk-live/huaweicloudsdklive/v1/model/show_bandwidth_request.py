# coding: utf-8

import pprint
import re

import six





class ShowBandwidthRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'step': 'int'
    }

    attribute_map = {
        'domain': 'domain',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'step': 'step'
    }

    def __init__(self, domain=None, start_time=None, end_time=None, step=None):
        """ShowBandwidthRequest - a model defined in huaweicloud sdk"""
        
        

        self._domain = None
        self._start_time = None
        self._end_time = None
        self._step = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if step is not None:
            self.step = step

    @property
    def domain(self):
        """Gets the domain of this ShowBandwidthRequest.


        :return: The domain of this ShowBandwidthRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ShowBandwidthRequest.


        :param domain: The domain of this ShowBandwidthRequest.
        :type: str
        """
        self._domain = domain

    @property
    def start_time(self):
        """Gets the start_time of this ShowBandwidthRequest.


        :return: The start_time of this ShowBandwidthRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowBandwidthRequest.


        :param start_time: The start_time of this ShowBandwidthRequest.
        :type: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowBandwidthRequest.


        :return: The end_time of this ShowBandwidthRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowBandwidthRequest.


        :param end_time: The end_time of this ShowBandwidthRequest.
        :type: str
        """
        self._end_time = end_time

    @property
    def step(self):
        """Gets the step of this ShowBandwidthRequest.


        :return: The step of this ShowBandwidthRequest.
        :rtype: int
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this ShowBandwidthRequest.


        :param step: The step of this ShowBandwidthRequest.
        :type: int
        """
        self._step = step

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
        if not isinstance(other, ShowBandwidthRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
