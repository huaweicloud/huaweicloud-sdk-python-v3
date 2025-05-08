# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetaAudioInfo:

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
        'sampling_rate': 'int',
        'bitrate': 'int'
    }

    attribute_map = {
        'codec': 'codec',
        'sampling_rate': 'sampling_rate',
        'bitrate': 'bitrate'
    }

    def __init__(self, codec=None, sampling_rate=None, bitrate=None):
        r"""MetaAudioInfo

        The model defined in huaweicloud sdk

        :param codec: 音频编码格式 
        :type codec: str
        :param sampling_rate: 音频采样率 
        :type sampling_rate: int
        :param bitrate: 音频码率，单位：bit/s 
        :type bitrate: int
        """
        
        

        self._codec = None
        self._sampling_rate = None
        self._bitrate = None
        self.discriminator = None

        if codec is not None:
            self.codec = codec
        if sampling_rate is not None:
            self.sampling_rate = sampling_rate
        if bitrate is not None:
            self.bitrate = bitrate

    @property
    def codec(self):
        r"""Gets the codec of this MetaAudioInfo.

        音频编码格式 

        :return: The codec of this MetaAudioInfo.
        :rtype: str
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        r"""Sets the codec of this MetaAudioInfo.

        音频编码格式 

        :param codec: The codec of this MetaAudioInfo.
        :type codec: str
        """
        self._codec = codec

    @property
    def sampling_rate(self):
        r"""Gets the sampling_rate of this MetaAudioInfo.

        音频采样率 

        :return: The sampling_rate of this MetaAudioInfo.
        :rtype: int
        """
        return self._sampling_rate

    @sampling_rate.setter
    def sampling_rate(self, sampling_rate):
        r"""Sets the sampling_rate of this MetaAudioInfo.

        音频采样率 

        :param sampling_rate: The sampling_rate of this MetaAudioInfo.
        :type sampling_rate: int
        """
        self._sampling_rate = sampling_rate

    @property
    def bitrate(self):
        r"""Gets the bitrate of this MetaAudioInfo.

        音频码率，单位：bit/s 

        :return: The bitrate of this MetaAudioInfo.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        r"""Sets the bitrate of this MetaAudioInfo.

        音频码率，单位：bit/s 

        :param bitrate: The bitrate of this MetaAudioInfo.
        :type bitrate: int
        """
        self._bitrate = bitrate

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
        if not isinstance(other, MetaAudioInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
