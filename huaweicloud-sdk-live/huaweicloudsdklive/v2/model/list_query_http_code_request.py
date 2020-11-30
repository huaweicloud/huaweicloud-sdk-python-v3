# coding: utf-8

import pprint
import re

import six





class ListQueryHttpCodeRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'play_domains': 'list[str]',
        'code': 'list[str]',
        'region': 'list[str]',
        'isp': 'list[str]',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'play_domains': 'play_domains',
        'code': 'code',
        'region': 'region',
        'isp': 'isp',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, play_domains=None, code=None, region=None, isp=None, start_time=None, end_time=None):
        """ListQueryHttpCodeRequest - a model defined in huaweicloud sdk"""
        
        

        self._play_domains = None
        self._code = None
        self._region = None
        self._isp = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.play_domains = play_domains
        if code is not None:
            self.code = code
        if region is not None:
            self.region = region
        if isp is not None:
            self.isp = isp
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def play_domains(self):
        """Gets the play_domains of this ListQueryHttpCodeRequest.


        :return: The play_domains of this ListQueryHttpCodeRequest.
        :rtype: list[str]
        """
        return self._play_domains

    @play_domains.setter
    def play_domains(self, play_domains):
        """Sets the play_domains of this ListQueryHttpCodeRequest.


        :param play_domains: The play_domains of this ListQueryHttpCodeRequest.
        :type: list[str]
        """
        self._play_domains = play_domains

    @property
    def code(self):
        """Gets the code of this ListQueryHttpCodeRequest.


        :return: The code of this ListQueryHttpCodeRequest.
        :rtype: list[str]
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ListQueryHttpCodeRequest.


        :param code: The code of this ListQueryHttpCodeRequest.
        :type: list[str]
        """
        self._code = code

    @property
    def region(self):
        """Gets the region of this ListQueryHttpCodeRequest.


        :return: The region of this ListQueryHttpCodeRequest.
        :rtype: list[str]
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListQueryHttpCodeRequest.


        :param region: The region of this ListQueryHttpCodeRequest.
        :type: list[str]
        """
        self._region = region

    @property
    def isp(self):
        """Gets the isp of this ListQueryHttpCodeRequest.


        :return: The isp of this ListQueryHttpCodeRequest.
        :rtype: list[str]
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this ListQueryHttpCodeRequest.


        :param isp: The isp of this ListQueryHttpCodeRequest.
        :type: list[str]
        """
        self._isp = isp

    @property
    def start_time(self):
        """Gets the start_time of this ListQueryHttpCodeRequest.


        :return: The start_time of this ListQueryHttpCodeRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListQueryHttpCodeRequest.


        :param start_time: The start_time of this ListQueryHttpCodeRequest.
        :type: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListQueryHttpCodeRequest.


        :return: The end_time of this ListQueryHttpCodeRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListQueryHttpCodeRequest.


        :param end_time: The end_time of this ListQueryHttpCodeRequest.
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
        if not isinstance(other, ListQueryHttpCodeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
