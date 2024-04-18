# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AudioAssetMeta:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'duration': 'int',
        'audio_codec': 'str',
        'audio_bit_rate': 'int',
        'audio_channels': 'int',
        'sample': 'int',
        'error_info': 'ErrorResponse'
    }

    attribute_map = {
        'duration': 'duration',
        'audio_codec': 'audio_codec',
        'audio_bit_rate': 'audio_bit_rate',
        'audio_channels': 'audio_channels',
        'sample': 'sample',
        'error_info': 'error_info'
    }

    def __init__(self, duration=None, audio_codec=None, audio_bit_rate=None, audio_channels=None, sample=None, error_info=None):
        """AudioAssetMeta

        The model defined in huaweicloud sdk

        :param duration: 时长,单位秒
        :type duration: int
        :param audio_codec: 音频编码格式
        :type audio_codec: str
        :param audio_bit_rate: 音频平均码率,单位kbps
        :type audio_bit_rate: int
        :param audio_channels: 音频声道数
        :type audio_channels: int
        :param sample: 采样率,HZ
        :type sample: int
        :param error_info: 
        :type error_info: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        
        

        self._duration = None
        self._audio_codec = None
        self._audio_bit_rate = None
        self._audio_channels = None
        self._sample = None
        self._error_info = None
        self.discriminator = None

        if duration is not None:
            self.duration = duration
        if audio_codec is not None:
            self.audio_codec = audio_codec
        if audio_bit_rate is not None:
            self.audio_bit_rate = audio_bit_rate
        if audio_channels is not None:
            self.audio_channels = audio_channels
        if sample is not None:
            self.sample = sample
        if error_info is not None:
            self.error_info = error_info

    @property
    def duration(self):
        """Gets the duration of this AudioAssetMeta.

        时长,单位秒

        :return: The duration of this AudioAssetMeta.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this AudioAssetMeta.

        时长,单位秒

        :param duration: The duration of this AudioAssetMeta.
        :type duration: int
        """
        self._duration = duration

    @property
    def audio_codec(self):
        """Gets the audio_codec of this AudioAssetMeta.

        音频编码格式

        :return: The audio_codec of this AudioAssetMeta.
        :rtype: str
        """
        return self._audio_codec

    @audio_codec.setter
    def audio_codec(self, audio_codec):
        """Sets the audio_codec of this AudioAssetMeta.

        音频编码格式

        :param audio_codec: The audio_codec of this AudioAssetMeta.
        :type audio_codec: str
        """
        self._audio_codec = audio_codec

    @property
    def audio_bit_rate(self):
        """Gets the audio_bit_rate of this AudioAssetMeta.

        音频平均码率,单位kbps

        :return: The audio_bit_rate of this AudioAssetMeta.
        :rtype: int
        """
        return self._audio_bit_rate

    @audio_bit_rate.setter
    def audio_bit_rate(self, audio_bit_rate):
        """Sets the audio_bit_rate of this AudioAssetMeta.

        音频平均码率,单位kbps

        :param audio_bit_rate: The audio_bit_rate of this AudioAssetMeta.
        :type audio_bit_rate: int
        """
        self._audio_bit_rate = audio_bit_rate

    @property
    def audio_channels(self):
        """Gets the audio_channels of this AudioAssetMeta.

        音频声道数

        :return: The audio_channels of this AudioAssetMeta.
        :rtype: int
        """
        return self._audio_channels

    @audio_channels.setter
    def audio_channels(self, audio_channels):
        """Sets the audio_channels of this AudioAssetMeta.

        音频声道数

        :param audio_channels: The audio_channels of this AudioAssetMeta.
        :type audio_channels: int
        """
        self._audio_channels = audio_channels

    @property
    def sample(self):
        """Gets the sample of this AudioAssetMeta.

        采样率,HZ

        :return: The sample of this AudioAssetMeta.
        :rtype: int
        """
        return self._sample

    @sample.setter
    def sample(self, sample):
        """Sets the sample of this AudioAssetMeta.

        采样率,HZ

        :param sample: The sample of this AudioAssetMeta.
        :type sample: int
        """
        self._sample = sample

    @property
    def error_info(self):
        """Gets the error_info of this AudioAssetMeta.

        :return: The error_info of this AudioAssetMeta.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        """Sets the error_info of this AudioAssetMeta.

        :param error_info: The error_info of this AudioAssetMeta.
        :type error_info: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        self._error_info = error_info

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
        if not isinstance(other, AudioAssetMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
