# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'width': 'int',
        'height': 'int',
        'bitrate': 'int',
        'bitrate_bps': 'int',
        'frame_rate': 'int',
        'codec': 'str'
    }

    attribute_map = {
        'width': 'width',
        'height': 'height',
        'bitrate': 'bitrate',
        'bitrate_bps': 'bitrate_bps',
        'frame_rate': 'frame_rate',
        'codec': 'codec'
    }

    def __init__(self, width=None, height=None, bitrate=None, bitrate_bps=None, frame_rate=None, codec=None):
        """VideoInfo

        The model defined in huaweicloud sdk

        :param width: 视频宽度
        :type width: int
        :param height: 视频高度
        :type height: int
        :param bitrate: 视频码率，单位: kbit/s 
        :type bitrate: int
        :param bitrate_bps: 视频码率，单位: bit/s 
        :type bitrate_bps: int
        :param frame_rate: 帧率。    取值范围：0或[5,60]，0表示自适应。    单位：帧每秒。    &gt; 若设置的帧率不在取值范围内，则自动调整为0，若设置的帧率高于片源帧率，则自动调整为片源帧率。 
        :type frame_rate: int
        :param codec: 视频编码格式
        :type codec: str
        """
        
        

        self._width = None
        self._height = None
        self._bitrate = None
        self._bitrate_bps = None
        self._frame_rate = None
        self._codec = None
        self.discriminator = None

        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if bitrate is not None:
            self.bitrate = bitrate
        if bitrate_bps is not None:
            self.bitrate_bps = bitrate_bps
        if frame_rate is not None:
            self.frame_rate = frame_rate
        if codec is not None:
            self.codec = codec

    @property
    def width(self):
        """Gets the width of this VideoInfo.

        视频宽度

        :return: The width of this VideoInfo.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this VideoInfo.

        视频宽度

        :param width: The width of this VideoInfo.
        :type width: int
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this VideoInfo.

        视频高度

        :return: The height of this VideoInfo.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this VideoInfo.

        视频高度

        :param height: The height of this VideoInfo.
        :type height: int
        """
        self._height = height

    @property
    def bitrate(self):
        """Gets the bitrate of this VideoInfo.

        视频码率，单位: kbit/s 

        :return: The bitrate of this VideoInfo.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this VideoInfo.

        视频码率，单位: kbit/s 

        :param bitrate: The bitrate of this VideoInfo.
        :type bitrate: int
        """
        self._bitrate = bitrate

    @property
    def bitrate_bps(self):
        """Gets the bitrate_bps of this VideoInfo.

        视频码率，单位: bit/s 

        :return: The bitrate_bps of this VideoInfo.
        :rtype: int
        """
        return self._bitrate_bps

    @bitrate_bps.setter
    def bitrate_bps(self, bitrate_bps):
        """Sets the bitrate_bps of this VideoInfo.

        视频码率，单位: bit/s 

        :param bitrate_bps: The bitrate_bps of this VideoInfo.
        :type bitrate_bps: int
        """
        self._bitrate_bps = bitrate_bps

    @property
    def frame_rate(self):
        """Gets the frame_rate of this VideoInfo.

        帧率。    取值范围：0或[5,60]，0表示自适应。    单位：帧每秒。    > 若设置的帧率不在取值范围内，则自动调整为0，若设置的帧率高于片源帧率，则自动调整为片源帧率。 

        :return: The frame_rate of this VideoInfo.
        :rtype: int
        """
        return self._frame_rate

    @frame_rate.setter
    def frame_rate(self, frame_rate):
        """Sets the frame_rate of this VideoInfo.

        帧率。    取值范围：0或[5,60]，0表示自适应。    单位：帧每秒。    > 若设置的帧率不在取值范围内，则自动调整为0，若设置的帧率高于片源帧率，则自动调整为片源帧率。 

        :param frame_rate: The frame_rate of this VideoInfo.
        :type frame_rate: int
        """
        self._frame_rate = frame_rate

    @property
    def codec(self):
        """Gets the codec of this VideoInfo.

        视频编码格式

        :return: The codec of this VideoInfo.
        :rtype: str
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        """Sets the codec of this VideoInfo.

        视频编码格式

        :param codec: The codec of this VideoInfo.
        :type codec: str
        """
        self._codec = codec

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
        if not isinstance(other, VideoInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
