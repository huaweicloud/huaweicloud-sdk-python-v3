# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        """AudioTemplateInfo

        The model defined in huaweicloud sdk

        :param sample_rate: 音频采样率(有效值范围) - 1：AUDIO_SAMPLE_AUTO - 2：AUDIO_SAMPLE_22050 - 3：AUDIO_SAMPLE_32000 - 4：AUDIO_SAMPLE_44100 - 5：AUDIO_SAMPLE_48000 - 6：AUDIO_SAMPLE_96000  默认值为1。
        :type sample_rate: int
        :param bitrate: 音频码率（单位：Kbps）。
        :type bitrate: int
        :param channels: 声道数(有效值范围) - 1：AUDIO_CHANNELS_1 - 2：AUDIO_CHANNELS_2
        :type channels: int
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
        """Gets the sample_rate of this AudioTemplateInfo.

        音频采样率(有效值范围) - 1：AUDIO_SAMPLE_AUTO - 2：AUDIO_SAMPLE_22050 - 3：AUDIO_SAMPLE_32000 - 4：AUDIO_SAMPLE_44100 - 5：AUDIO_SAMPLE_48000 - 6：AUDIO_SAMPLE_96000  默认值为1。

        :return: The sample_rate of this AudioTemplateInfo.
        :rtype: int
        """
        return self._sample_rate

    @sample_rate.setter
    def sample_rate(self, sample_rate):
        """Sets the sample_rate of this AudioTemplateInfo.

        音频采样率(有效值范围) - 1：AUDIO_SAMPLE_AUTO - 2：AUDIO_SAMPLE_22050 - 3：AUDIO_SAMPLE_32000 - 4：AUDIO_SAMPLE_44100 - 5：AUDIO_SAMPLE_48000 - 6：AUDIO_SAMPLE_96000  默认值为1。

        :param sample_rate: The sample_rate of this AudioTemplateInfo.
        :type sample_rate: int
        """
        self._sample_rate = sample_rate

    @property
    def bitrate(self):
        """Gets the bitrate of this AudioTemplateInfo.

        音频码率（单位：Kbps）。

        :return: The bitrate of this AudioTemplateInfo.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this AudioTemplateInfo.

        音频码率（单位：Kbps）。

        :param bitrate: The bitrate of this AudioTemplateInfo.
        :type bitrate: int
        """
        self._bitrate = bitrate

    @property
    def channels(self):
        """Gets the channels of this AudioTemplateInfo.

        声道数(有效值范围) - 1：AUDIO_CHANNELS_1 - 2：AUDIO_CHANNELS_2

        :return: The channels of this AudioTemplateInfo.
        :rtype: int
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this AudioTemplateInfo.

        声道数(有效值范围) - 1：AUDIO_CHANNELS_1 - 2：AUDIO_CHANNELS_2

        :param channels: The channels of this AudioTemplateInfo.
        :type channels: int
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
        if not isinstance(other, AudioTemplateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
