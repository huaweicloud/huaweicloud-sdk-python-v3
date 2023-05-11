# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'sample_rate': 'str',
        'bitrate': 'int',
        'channels': 'str'
    }

    attribute_map = {
        'sample_rate': 'sample_rate',
        'bitrate': 'bitrate',
        'channels': 'channels'
    }

    def __init__(self, sample_rate=None, bitrate=None, channels=None):
        """AudioInfo

        The model defined in huaweicloud sdk

        :param sample_rate: 音频采样率(有效值范围)&lt;br/&gt; AUDIO_SAMPLE_AUTO (default), AUDIO_SAMPLE_22050：22050Hz&lt;br/&gt; AUDIO_SAMPLE_32000：32000Hz&lt;br/&gt; AUDIO_SAMPLE_44100：44100Hz&lt;br/&gt; AUDIO_SAMPLE_48000：48000Hz&lt;br/&gt; AUDIO_SAMPLE_96000：96000Hz&lt;br/&gt; 
        :type sample_rate: str
        :param bitrate: 音频码率（单位：Kbps）&lt;br/&gt; 
        :type bitrate: int
        :param channels: 声道数(有效值范围)&lt;br/&gt; AUDIO_CHANNELS_1:单声道&lt;br/&gt; AUDIO_CHANNELS_2：双声道&lt;br/&gt; AUDIO_CHANNELS_5_1：5.1声道&lt;br/&gt; 
        :type channels: str
        """
        
        

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
        """Gets the sample_rate of this AudioInfo.

        音频采样率(有效值范围)<br/> AUDIO_SAMPLE_AUTO (default), AUDIO_SAMPLE_22050：22050Hz<br/> AUDIO_SAMPLE_32000：32000Hz<br/> AUDIO_SAMPLE_44100：44100Hz<br/> AUDIO_SAMPLE_48000：48000Hz<br/> AUDIO_SAMPLE_96000：96000Hz<br/> 

        :return: The sample_rate of this AudioInfo.
        :rtype: str
        """
        return self._sample_rate

    @sample_rate.setter
    def sample_rate(self, sample_rate):
        """Sets the sample_rate of this AudioInfo.

        音频采样率(有效值范围)<br/> AUDIO_SAMPLE_AUTO (default), AUDIO_SAMPLE_22050：22050Hz<br/> AUDIO_SAMPLE_32000：32000Hz<br/> AUDIO_SAMPLE_44100：44100Hz<br/> AUDIO_SAMPLE_48000：48000Hz<br/> AUDIO_SAMPLE_96000：96000Hz<br/> 

        :param sample_rate: The sample_rate of this AudioInfo.
        :type sample_rate: str
        """
        self._sample_rate = sample_rate

    @property
    def bitrate(self):
        """Gets the bitrate of this AudioInfo.

        音频码率（单位：Kbps）<br/> 

        :return: The bitrate of this AudioInfo.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this AudioInfo.

        音频码率（单位：Kbps）<br/> 

        :param bitrate: The bitrate of this AudioInfo.
        :type bitrate: int
        """
        self._bitrate = bitrate

    @property
    def channels(self):
        """Gets the channels of this AudioInfo.

        声道数(有效值范围)<br/> AUDIO_CHANNELS_1:单声道<br/> AUDIO_CHANNELS_2：双声道<br/> AUDIO_CHANNELS_5_1：5.1声道<br/> 

        :return: The channels of this AudioInfo.
        :rtype: str
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this AudioInfo.

        声道数(有效值范围)<br/> AUDIO_CHANNELS_1:单声道<br/> AUDIO_CHANNELS_2：双声道<br/> AUDIO_CHANNELS_5_1：5.1声道<br/> 

        :param channels: The channels of this AudioInfo.
        :type channels: str
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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AudioInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
