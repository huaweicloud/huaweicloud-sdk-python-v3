# coding: utf-8

import pprint
import re

import six





class AudioInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'language': 'str',
        'codec': 'str',
        'sample': 'int',
        'channels': 'int',
        'sky_switch': 'int',
        'bitrate': 'int',
        'bitrate_bps': 'int'
    }

    attribute_map = {
        'language': 'language',
        'codec': 'codec',
        'sample': 'sample',
        'channels': 'channels',
        'sky_switch': 'sky_switch',
        'bitrate': 'bitrate',
        'bitrate_bps': 'bitrate_bps'
    }

    def __init__(self, language=None, codec=None, sample=None, channels=None, sky_switch=None, bitrate=None, bitrate_bps=None):
        """AudioInfo - a model defined in huaweicloud sdk"""
        
        

        self._language = None
        self._codec = None
        self._sample = None
        self._channels = None
        self._sky_switch = None
        self._bitrate = None
        self._bitrate_bps = None
        self.discriminator = None

        if language is not None:
            self.language = language
        if codec is not None:
            self.codec = codec
        if sample is not None:
            self.sample = sample
        if channels is not None:
            self.channels = channels
        if sky_switch is not None:
            self.sky_switch = sky_switch
        if bitrate is not None:
            self.bitrate = bitrate
        if bitrate_bps is not None:
            self.bitrate_bps = bitrate_bps

    @property
    def language(self):
        """Gets the language of this AudioInfo.

        声轨语言。

        :return: The language of this AudioInfo.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this AudioInfo.

        声轨语言。

        :param language: The language of this AudioInfo.
        :type: str
        """
        self._language = language

    @property
    def codec(self):
        """Gets the codec of this AudioInfo.

        音频编码格式

        :return: The codec of this AudioInfo.
        :rtype: str
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        """Sets the codec of this AudioInfo.

        音频编码格式

        :param codec: The codec of this AudioInfo.
        :type: str
        """
        self._codec = codec

    @property
    def sample(self):
        """Gets the sample of this AudioInfo.

        音频采样率

        :return: The sample of this AudioInfo.
        :rtype: int
        """
        return self._sample

    @sample.setter
    def sample(self, sample):
        """Sets the sample of this AudioInfo.

        音频采样率

        :param sample: The sample of this AudioInfo.
        :type: int
        """
        self._sample = sample

    @property
    def channels(self):
        """Gets the channels of this AudioInfo.

        音频信道

        :return: The channels of this AudioInfo.
        :rtype: int
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this AudioInfo.

        音频信道

        :param channels: The channels of this AudioInfo.
        :type: int
        """
        self._channels = channels

    @property
    def sky_switch(self):
        """Gets the sky_switch of this AudioInfo.

        是否开启了天空音。

        :return: The sky_switch of this AudioInfo.
        :rtype: int
        """
        return self._sky_switch

    @sky_switch.setter
    def sky_switch(self, sky_switch):
        """Sets the sky_switch of this AudioInfo.

        是否开启了天空音。

        :param sky_switch: The sky_switch of this AudioInfo.
        :type: int
        """
        self._sky_switch = sky_switch

    @property
    def bitrate(self):
        """Gets the bitrate of this AudioInfo.

        音频码率，单位: kbit/s 

        :return: The bitrate of this AudioInfo.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this AudioInfo.

        音频码率，单位: kbit/s 

        :param bitrate: The bitrate of this AudioInfo.
        :type: int
        """
        self._bitrate = bitrate

    @property
    def bitrate_bps(self):
        """Gets the bitrate_bps of this AudioInfo.

        音频码率，单位: bit/s 

        :return: The bitrate_bps of this AudioInfo.
        :rtype: int
        """
        return self._bitrate_bps

    @bitrate_bps.setter
    def bitrate_bps(self, bitrate_bps):
        """Sets the bitrate_bps of this AudioInfo.

        音频码率，单位: bit/s 

        :param bitrate_bps: The bitrate_bps of this AudioInfo.
        :type: int
        """
        self._bitrate_bps = bitrate_bps

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
        if not isinstance(other, AudioInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
