# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EditAudioInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'codec': 'str',
        'bitrate': 'int',
        'sample': 'int',
        'channels': 'str'
    }

    attribute_map = {
        'codec': 'codec',
        'bitrate': 'bitrate',
        'sample': 'sample',
        'channels': 'channels'
    }

    def __init__(self, codec=None, bitrate=None, sample=None, channels=None):
        """EditAudioInfo

        The model defined in huaweicloud sdk

        :param codec: 音频编码格式,取值有：[AAC, HEAAC, MP3]。
        :type codec: str
        :param bitrate: 视频码率，单位: bit/s 
        :type bitrate: int
        :param sample: 采样率, 单位: HZ 
        :type sample: int
        :param channels: 声道数。
        :type channels: str
        """
        
        

        self._codec = None
        self._bitrate = None
        self._sample = None
        self._channels = None
        self.discriminator = None

        if codec is not None:
            self.codec = codec
        if bitrate is not None:
            self.bitrate = bitrate
        if sample is not None:
            self.sample = sample
        if channels is not None:
            self.channels = channels

    @property
    def codec(self):
        """Gets the codec of this EditAudioInfo.

        音频编码格式,取值有：[AAC, HEAAC, MP3]。

        :return: The codec of this EditAudioInfo.
        :rtype: str
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        """Sets the codec of this EditAudioInfo.

        音频编码格式,取值有：[AAC, HEAAC, MP3]。

        :param codec: The codec of this EditAudioInfo.
        :type codec: str
        """
        self._codec = codec

    @property
    def bitrate(self):
        """Gets the bitrate of this EditAudioInfo.

        视频码率，单位: bit/s 

        :return: The bitrate of this EditAudioInfo.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this EditAudioInfo.

        视频码率，单位: bit/s 

        :param bitrate: The bitrate of this EditAudioInfo.
        :type bitrate: int
        """
        self._bitrate = bitrate

    @property
    def sample(self):
        """Gets the sample of this EditAudioInfo.

        采样率, 单位: HZ 

        :return: The sample of this EditAudioInfo.
        :rtype: int
        """
        return self._sample

    @sample.setter
    def sample(self, sample):
        """Sets the sample of this EditAudioInfo.

        采样率, 单位: HZ 

        :param sample: The sample of this EditAudioInfo.
        :type sample: int
        """
        self._sample = sample

    @property
    def channels(self):
        """Gets the channels of this EditAudioInfo.

        声道数。

        :return: The channels of this EditAudioInfo.
        :rtype: str
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this EditAudioInfo.

        声道数。

        :param channels: The channels of this EditAudioInfo.
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
        if not isinstance(other, EditAudioInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
