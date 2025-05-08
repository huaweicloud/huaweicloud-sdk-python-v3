# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetaVideoInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bitrate': 'int',
        'codec': 'str',
        'fps': 'int',
        'height': 'int',
        'width': 'int'
    }

    attribute_map = {
        'bitrate': 'bitrate',
        'codec': 'codec',
        'fps': 'fps',
        'height': 'height',
        'width': 'width'
    }

    def __init__(self, bitrate=None, codec=None, fps=None, height=None, width=None):
        r"""MetaVideoInfo

        The model defined in huaweicloud sdk

        :param bitrate: 视频码率，单位：bit/s 
        :type bitrate: int
        :param codec: 视频编码格式 
        :type codec: str
        :param fps: 帧率 
        :type fps: int
        :param height: 视频高度 
        :type height: int
        :param width: 视频宽度 
        :type width: int
        """
        
        

        self._bitrate = None
        self._codec = None
        self._fps = None
        self._height = None
        self._width = None
        self.discriminator = None

        if bitrate is not None:
            self.bitrate = bitrate
        if codec is not None:
            self.codec = codec
        if fps is not None:
            self.fps = fps
        if height is not None:
            self.height = height
        if width is not None:
            self.width = width

    @property
    def bitrate(self):
        r"""Gets the bitrate of this MetaVideoInfo.

        视频码率，单位：bit/s 

        :return: The bitrate of this MetaVideoInfo.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        r"""Sets the bitrate of this MetaVideoInfo.

        视频码率，单位：bit/s 

        :param bitrate: The bitrate of this MetaVideoInfo.
        :type bitrate: int
        """
        self._bitrate = bitrate

    @property
    def codec(self):
        r"""Gets the codec of this MetaVideoInfo.

        视频编码格式 

        :return: The codec of this MetaVideoInfo.
        :rtype: str
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        r"""Sets the codec of this MetaVideoInfo.

        视频编码格式 

        :param codec: The codec of this MetaVideoInfo.
        :type codec: str
        """
        self._codec = codec

    @property
    def fps(self):
        r"""Gets the fps of this MetaVideoInfo.

        帧率 

        :return: The fps of this MetaVideoInfo.
        :rtype: int
        """
        return self._fps

    @fps.setter
    def fps(self, fps):
        r"""Sets the fps of this MetaVideoInfo.

        帧率 

        :param fps: The fps of this MetaVideoInfo.
        :type fps: int
        """
        self._fps = fps

    @property
    def height(self):
        r"""Gets the height of this MetaVideoInfo.

        视频高度 

        :return: The height of this MetaVideoInfo.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        r"""Sets the height of this MetaVideoInfo.

        视频高度 

        :param height: The height of this MetaVideoInfo.
        :type height: int
        """
        self._height = height

    @property
    def width(self):
        r"""Gets the width of this MetaVideoInfo.

        视频宽度 

        :return: The width of this MetaVideoInfo.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        r"""Sets the width of this MetaVideoInfo.

        视频宽度 

        :param width: The width of this MetaVideoInfo.
        :type width: int
        """
        self._width = width

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
        if not isinstance(other, MetaVideoInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
