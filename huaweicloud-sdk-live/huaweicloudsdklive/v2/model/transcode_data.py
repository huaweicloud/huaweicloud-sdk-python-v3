# coding: utf-8

import pprint
import re

import six





class TranscodeData:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'spec_list': 'list[TranscodeSpec]',
        'time': 'str'
    }

    attribute_map = {
        'spec_list': 'spec_list',
        'time': 'time'
    }

    def __init__(self, spec_list=None, time=None):
        """TranscodeData - a model defined in huaweicloud sdk"""
        
        

        self._spec_list = None
        self._time = None
        self.discriminator = None

        if spec_list is not None:
            self.spec_list = spec_list
        if time is not None:
            self.time = time

    @property
    def spec_list(self):
        """Gets the spec_list of this TranscodeData.

        每个采样时间中的转码时长信息。

        :return: The spec_list of this TranscodeData.
        :rtype: list[TranscodeSpec]
        """
        return self._spec_list

    @spec_list.setter
    def spec_list(self, spec_list):
        """Sets the spec_list of this TranscodeData.

        每个采样时间中的转码时长信息。

        :param spec_list: The spec_list of this TranscodeData.
        :type: list[TranscodeSpec]
        """
        self._spec_list = spec_list

    @property
    def time(self):
        """Gets the time of this TranscodeData.

        采样时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ 。

        :return: The time of this TranscodeData.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this TranscodeData.

        采样时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ 。

        :param time: The time of this TranscodeData.
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
        if not isinstance(other, TranscodeData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
