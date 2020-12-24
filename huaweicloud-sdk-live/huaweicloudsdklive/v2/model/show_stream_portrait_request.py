# coding: utf-8

import pprint
import re

import six





class ShowStreamPortraitRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'play_domain': 'str',
        'stream': 'str',
        'time': 'str'
    }

    attribute_map = {
        'play_domain': 'play_domain',
        'stream': 'stream',
        'time': 'time'
    }

    def __init__(self, play_domain=None, stream=None, time=None):
        """ShowStreamPortraitRequest - a model defined in huaweicloud sdk"""
        
        

        self._play_domain = None
        self._stream = None
        self._time = None
        self.discriminator = None

        self.play_domain = play_domain
        if stream is not None:
            self.stream = stream
        self.time = time

    @property
    def play_domain(self):
        """Gets the play_domain of this ShowStreamPortraitRequest.


        :return: The play_domain of this ShowStreamPortraitRequest.
        :rtype: str
        """
        return self._play_domain

    @play_domain.setter
    def play_domain(self, play_domain):
        """Sets the play_domain of this ShowStreamPortraitRequest.


        :param play_domain: The play_domain of this ShowStreamPortraitRequest.
        :type: str
        """
        self._play_domain = play_domain

    @property
    def stream(self):
        """Gets the stream of this ShowStreamPortraitRequest.


        :return: The stream of this ShowStreamPortraitRequest.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this ShowStreamPortraitRequest.


        :param stream: The stream of this ShowStreamPortraitRequest.
        :type: str
        """
        self._stream = stream

    @property
    def time(self):
        """Gets the time of this ShowStreamPortraitRequest.


        :return: The time of this ShowStreamPortraitRequest.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ShowStreamPortraitRequest.


        :param time: The time of this ShowStreamPortraitRequest.
        :type: str
        """
        self._time = time

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
        if not isinstance(other, ShowStreamPortraitRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
