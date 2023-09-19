# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PhotoVideoConfig:

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
        'frame_rate': 'str'
    }

    attribute_map = {
        'codec': 'codec',
        'bitrate': 'bitrate',
        'frame_rate': 'frame_rate'
    }

    def __init__(self, codec=None, bitrate=None, frame_rate=None):
        """PhotoVideoConfig

        The model defined in huaweicloud sdk

        :param codec: 视频编码格式及视频文件格式。 * H264: h264编码，输出mp4文件
        :type codec: str
        :param bitrate: 输出平均码率。  单位：kbps。  最小值40，最大值30000。
        :type bitrate: int
        :param frame_rate: 帧率。  单位：FPS。
        :type frame_rate: str
        """
        
        

        self._codec = None
        self._bitrate = None
        self._frame_rate = None
        self.discriminator = None

        self.codec = codec
        if bitrate is not None:
            self.bitrate = bitrate
        if frame_rate is not None:
            self.frame_rate = frame_rate

    @property
    def codec(self):
        """Gets the codec of this PhotoVideoConfig.

        视频编码格式及视频文件格式。 * H264: h264编码，输出mp4文件

        :return: The codec of this PhotoVideoConfig.
        :rtype: str
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        """Sets the codec of this PhotoVideoConfig.

        视频编码格式及视频文件格式。 * H264: h264编码，输出mp4文件

        :param codec: The codec of this PhotoVideoConfig.
        :type codec: str
        """
        self._codec = codec

    @property
    def bitrate(self):
        """Gets the bitrate of this PhotoVideoConfig.

        输出平均码率。  单位：kbps。  最小值40，最大值30000。

        :return: The bitrate of this PhotoVideoConfig.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this PhotoVideoConfig.

        输出平均码率。  单位：kbps。  最小值40，最大值30000。

        :param bitrate: The bitrate of this PhotoVideoConfig.
        :type bitrate: int
        """
        self._bitrate = bitrate

    @property
    def frame_rate(self):
        """Gets the frame_rate of this PhotoVideoConfig.

        帧率。  单位：FPS。

        :return: The frame_rate of this PhotoVideoConfig.
        :rtype: str
        """
        return self._frame_rate

    @frame_rate.setter
    def frame_rate(self, frame_rate):
        """Sets the frame_rate of this PhotoVideoConfig.

        帧率。  单位：FPS。

        :param frame_rate: The frame_rate of this PhotoVideoConfig.
        :type frame_rate: str
        """
        self._frame_rate = frame_rate

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
        if not isinstance(other, PhotoVideoConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
