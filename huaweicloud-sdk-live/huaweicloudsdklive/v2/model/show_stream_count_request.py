# coding: utf-8

import pprint
import re

import six





class ShowStreamCountRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'publish_domains': 'list[str]',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'publish_domains': 'publish_domains',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, publish_domains=None, start_time=None, end_time=None):
        """ShowStreamCountRequest - a model defined in huaweicloud sdk"""
        
        

        self._publish_domains = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.publish_domains = publish_domains
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def publish_domains(self):
        """Gets the publish_domains of this ShowStreamCountRequest.


        :return: The publish_domains of this ShowStreamCountRequest.
        :rtype: list[str]
        """
        return self._publish_domains

    @publish_domains.setter
    def publish_domains(self, publish_domains):
        """Sets the publish_domains of this ShowStreamCountRequest.


        :param publish_domains: The publish_domains of this ShowStreamCountRequest.
        :type: list[str]
        """
        self._publish_domains = publish_domains

    @property
    def start_time(self):
        """Gets the start_time of this ShowStreamCountRequest.


        :return: The start_time of this ShowStreamCountRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowStreamCountRequest.


        :param start_time: The start_time of this ShowStreamCountRequest.
        :type: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowStreamCountRequest.


        :return: The end_time of this ShowStreamCountRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowStreamCountRequest.


        :param end_time: The end_time of this ShowStreamCountRequest.
        :type: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ShowStreamCountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
