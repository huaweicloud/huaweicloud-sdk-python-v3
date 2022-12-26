# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Audio:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'output_policy': 'str',
        'codec': 'int',
        'sample_rate': 'int',
        'bitrate': 'int',
        'channels': 'int'
    }

    attribute_map = {
        'output_policy': 'output_policy',
        'codec': 'codec',
        'sample_rate': 'sample_rate',
        'bitrate': 'bitrate',
        'channels': 'channels'
    }

    def __init__(self, output_policy=None, codec=None, sample_rate=None, bitrate=None, channels=None):
        """Audio

        The model defined in huaweicloud sdk

        :param output_policy: 输出策略。  取值如下： - discard - transcode  &gt;- 当视频参数中的“output_policy”为\&quot;discard\&quot;，且音频参数中的“output_policy”为“transcode”时，表示只输出音频。 &gt;- 当视频参数中的“output_policy”为\&quot;transcode\&quot;，且音频参数中的“output_policy”为“discard”时，表示只输出视频。 &gt;- 同时为\&quot;discard\&quot;时不合法。 &gt;- 同时为“transcode”时，表示输出音视频。 
        :type output_policy: str
        :param codec: 音频编码格式。  取值如下：  - 1：AAC格式。 - 2：HEAAC1格式 。 - 3：HEAAC2格式。 - 4：MP3格式 。 
        :type codec: int
        :param sample_rate: 音频采样率。  取值如下：  - 1：AUDIO_SAMPLE_AUTO - 2：AUDIO_SAMPLE_22050（22050Hz） - 3：AUDIO_SAMPLE_32000（32000Hz） - 4：AUDIO_SAMPLE_44100（44100Hz） - 5：AUDIO_SAMPLE_48000（48000Hz） - 6：AUDIO_SAMPLE_96000（96000Hz） 
        :type sample_rate: int
        :param bitrate: 音频码率。  取值范围：0或[8,1000]。  单位：kbit/s。 
        :type bitrate: int
        :param channels: 声道数。  取值如下： - 1：AUDIO_CHANNELS_1 - 2：AUDIO_CHANNELS_2 - 6：AUDIO_CHANNELS_5_1 
        :type channels: int
        """
        
        

        self._output_policy = None
        self._codec = None
        self._sample_rate = None
        self._bitrate = None
        self._channels = None
        self.discriminator = None

        if output_policy is not None:
            self.output_policy = output_policy
        if codec is not None:
            self.codec = codec
        if sample_rate is not None:
            self.sample_rate = sample_rate
        if bitrate is not None:
            self.bitrate = bitrate
        self.channels = channels

    @property
    def output_policy(self):
        """Gets the output_policy of this Audio.

        输出策略。  取值如下： - discard - transcode  >- 当视频参数中的“output_policy”为\"discard\"，且音频参数中的“output_policy”为“transcode”时，表示只输出音频。 >- 当视频参数中的“output_policy”为\"transcode\"，且音频参数中的“output_policy”为“discard”时，表示只输出视频。 >- 同时为\"discard\"时不合法。 >- 同时为“transcode”时，表示输出音视频。 

        :return: The output_policy of this Audio.
        :rtype: str
        """
        return self._output_policy

    @output_policy.setter
    def output_policy(self, output_policy):
        """Sets the output_policy of this Audio.

        输出策略。  取值如下： - discard - transcode  >- 当视频参数中的“output_policy”为\"discard\"，且音频参数中的“output_policy”为“transcode”时，表示只输出音频。 >- 当视频参数中的“output_policy”为\"transcode\"，且音频参数中的“output_policy”为“discard”时，表示只输出视频。 >- 同时为\"discard\"时不合法。 >- 同时为“transcode”时，表示输出音视频。 

        :param output_policy: The output_policy of this Audio.
        :type output_policy: str
        """
        self._output_policy = output_policy

    @property
    def codec(self):
        """Gets the codec of this Audio.

        音频编码格式。  取值如下：  - 1：AAC格式。 - 2：HEAAC1格式 。 - 3：HEAAC2格式。 - 4：MP3格式 。 

        :return: The codec of this Audio.
        :rtype: int
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        """Sets the codec of this Audio.

        音频编码格式。  取值如下：  - 1：AAC格式。 - 2：HEAAC1格式 。 - 3：HEAAC2格式。 - 4：MP3格式 。 

        :param codec: The codec of this Audio.
        :type codec: int
        """
        self._codec = codec

    @property
    def sample_rate(self):
        """Gets the sample_rate of this Audio.

        音频采样率。  取值如下：  - 1：AUDIO_SAMPLE_AUTO - 2：AUDIO_SAMPLE_22050（22050Hz） - 3：AUDIO_SAMPLE_32000（32000Hz） - 4：AUDIO_SAMPLE_44100（44100Hz） - 5：AUDIO_SAMPLE_48000（48000Hz） - 6：AUDIO_SAMPLE_96000（96000Hz） 

        :return: The sample_rate of this Audio.
        :rtype: int
        """
        return self._sample_rate

    @sample_rate.setter
    def sample_rate(self, sample_rate):
        """Sets the sample_rate of this Audio.

        音频采样率。  取值如下：  - 1：AUDIO_SAMPLE_AUTO - 2：AUDIO_SAMPLE_22050（22050Hz） - 3：AUDIO_SAMPLE_32000（32000Hz） - 4：AUDIO_SAMPLE_44100（44100Hz） - 5：AUDIO_SAMPLE_48000（48000Hz） - 6：AUDIO_SAMPLE_96000（96000Hz） 

        :param sample_rate: The sample_rate of this Audio.
        :type sample_rate: int
        """
        self._sample_rate = sample_rate

    @property
    def bitrate(self):
        """Gets the bitrate of this Audio.

        音频码率。  取值范围：0或[8,1000]。  单位：kbit/s。 

        :return: The bitrate of this Audio.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this Audio.

        音频码率。  取值范围：0或[8,1000]。  单位：kbit/s。 

        :param bitrate: The bitrate of this Audio.
        :type bitrate: int
        """
        self._bitrate = bitrate

    @property
    def channels(self):
        """Gets the channels of this Audio.

        声道数。  取值如下： - 1：AUDIO_CHANNELS_1 - 2：AUDIO_CHANNELS_2 - 6：AUDIO_CHANNELS_5_1 

        :return: The channels of this Audio.
        :rtype: int
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this Audio.

        声道数。  取值如下： - 1：AUDIO_CHANNELS_1 - 2：AUDIO_CHANNELS_2 - 6：AUDIO_CHANNELS_5_1 

        :param channels: The channels of this Audio.
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
        if not isinstance(other, Audio):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
