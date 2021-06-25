# coding: utf-8

import pprint
import re

import six





class AudioTemplateInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'sample_rate': 'int',
        'bitrate': 'int',
        'channels': 'int'
    }

    attribute_map = {
        'sample_rate': 'sample_rate',
        'bitrate': 'bitrate',
        'channels': 'channels'
    }

    def __init__(self, sample_rate=None, bitrate=None, channels=None):
        """AudioTemplateInfo - a model defined in huaweicloud sdk"""
        
        

        self._sample_rate = None
        self._bitrate = None
        self._channels = None
        self.discriminator = None

        self.sample_rate = sample_rate
        if bitrate is not None:
            self.bitrate = bitrate
        self.channels = channels

    @property
    def sample_rate(self):
        """Gets the sample_rate of this AudioTemplateInfo.

        音频采样率(有效值范围)<br/>  AUDIO_SAMPLE_AUTO=1 (default), AUDIO_SAMPLE_22050=2<br/> AUDIO_SAMPLE_32000=3<br/> AUDIO_SAMPLE_44100=4<br/> AUDIO_SAMPLE_48000=5<br/> AUDIO_SAMPLE_96000=6<br/> 

        :return: The sample_rate of this AudioTemplateInfo.
        :rtype: int
        """
        return self._sample_rate

    @sample_rate.setter
    def sample_rate(self, sample_rate):
        """Sets the sample_rate of this AudioTemplateInfo.

        音频采样率(有效值范围)<br/>  AUDIO_SAMPLE_AUTO=1 (default), AUDIO_SAMPLE_22050=2<br/> AUDIO_SAMPLE_32000=3<br/> AUDIO_SAMPLE_44100=4<br/> AUDIO_SAMPLE_48000=5<br/> AUDIO_SAMPLE_96000=6<br/> 

        :param sample_rate: The sample_rate of this AudioTemplateInfo.
        :type: int
        """
        self._sample_rate = sample_rate

    @property
    def bitrate(self):
        """Gets the bitrate of this AudioTemplateInfo.

        音频码率（单位：Kbps）<br/> 

        :return: The bitrate of this AudioTemplateInfo.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this AudioTemplateInfo.

        音频码率（单位：Kbps）<br/> 

        :param bitrate: The bitrate of this AudioTemplateInfo.
        :type: int
        """
        self._bitrate = bitrate

    @property
    def channels(self):
        """Gets the channels of this AudioTemplateInfo.

        声道数(有效值范围)<br/> AUDIO_CHANNELS_1=1<br/> AUDIO_CHANNELS_2=2<br/> 

        :return: The channels of this AudioTemplateInfo.
        :rtype: int
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this AudioTemplateInfo.

        声道数(有效值范围)<br/> AUDIO_CHANNELS_1=1<br/> AUDIO_CHANNELS_2=2<br/> 

        :param channels: The channels of this AudioTemplateInfo.
        :type: int
        """
        self._channels = channels

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
        if not isinstance(other, AudioTemplateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
