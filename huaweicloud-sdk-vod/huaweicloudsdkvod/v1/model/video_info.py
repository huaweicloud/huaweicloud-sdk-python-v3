# coding: utf-8

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
        'stream_name': 'str',
        'quality': 'str',
        'width': 'int',
        'height': 'int',
        'bitrate': 'int',
        'frame_rate': 'int'
    }

    attribute_map = {
        'stream_name': 'stream_name',
        'quality': 'quality',
        'width': 'width',
        'height': 'height',
        'bitrate': 'bitrate',
        'frame_rate': 'frame_rate'
    }

    def __init__(self, stream_name=None, quality=None, width=None, height=None, bitrate=None, frame_rate=None):
        r"""VideoInfo

        The model defined in huaweicloud sdk

        :param stream_name: 流名，流名仅支持数字、字母、下划线、中划线。 如果流名不填，则点播会按照video_stream_l{index}形式，生成一个流名。 
        :type stream_name: str
        :param quality: 画质&lt;br/&gt; 4K默认分辨率3840*2160，码率8000kbit/s&lt;br/&gt; 2K默认分辨率2560*1440，码率7000kbit/s&lt;br/&gt; FULL_HD默认分辨率1920*1080，码率3000kbit/s&lt;br/&gt; HD默认分辨率1280*720，码率1000kbit/s&lt;br/&gt; SD默认分辨率854*480，码率600kbit/s&lt;br/&gt; FLUENT默认分辨率480*270，码率300kbit/s&lt;br/&gt; 
        :type quality: str
        :param width: 视频宽度&lt;br/&gt; 
        :type width: int
        :param height: 视频高度&lt;br/&gt; 
        :type height: int
        :param bitrate: 码率,单位：kbit/s&lt;br/&gt; 
        :type bitrate: int
        :param frame_rate: 帧率（默认为0，0代表自适应，单位是帧每秒）&lt;br/&gt; 
        :type frame_rate: int
        """
        
        

        self._stream_name = None
        self._quality = None
        self._width = None
        self._height = None
        self._bitrate = None
        self._frame_rate = None
        self.discriminator = None

        if stream_name is not None:
            self.stream_name = stream_name
        self.quality = quality
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        self.bitrate = bitrate
        self.frame_rate = frame_rate

    @property
    def stream_name(self):
        r"""Gets the stream_name of this VideoInfo.

        流名，流名仅支持数字、字母、下划线、中划线。 如果流名不填，则点播会按照video_stream_l{index}形式，生成一个流名。 

        :return: The stream_name of this VideoInfo.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        r"""Sets the stream_name of this VideoInfo.

        流名，流名仅支持数字、字母、下划线、中划线。 如果流名不填，则点播会按照video_stream_l{index}形式，生成一个流名。 

        :param stream_name: The stream_name of this VideoInfo.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def quality(self):
        r"""Gets the quality of this VideoInfo.

        画质<br/> 4K默认分辨率3840*2160，码率8000kbit/s<br/> 2K默认分辨率2560*1440，码率7000kbit/s<br/> FULL_HD默认分辨率1920*1080，码率3000kbit/s<br/> HD默认分辨率1280*720，码率1000kbit/s<br/> SD默认分辨率854*480，码率600kbit/s<br/> FLUENT默认分辨率480*270，码率300kbit/s<br/> 

        :return: The quality of this VideoInfo.
        :rtype: str
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        r"""Sets the quality of this VideoInfo.

        画质<br/> 4K默认分辨率3840*2160，码率8000kbit/s<br/> 2K默认分辨率2560*1440，码率7000kbit/s<br/> FULL_HD默认分辨率1920*1080，码率3000kbit/s<br/> HD默认分辨率1280*720，码率1000kbit/s<br/> SD默认分辨率854*480，码率600kbit/s<br/> FLUENT默认分辨率480*270，码率300kbit/s<br/> 

        :param quality: The quality of this VideoInfo.
        :type quality: str
        """
        self._quality = quality

    @property
    def width(self):
        r"""Gets the width of this VideoInfo.

        视频宽度<br/> 

        :return: The width of this VideoInfo.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        r"""Sets the width of this VideoInfo.

        视频宽度<br/> 

        :param width: The width of this VideoInfo.
        :type width: int
        """
        self._width = width

    @property
    def height(self):
        r"""Gets the height of this VideoInfo.

        视频高度<br/> 

        :return: The height of this VideoInfo.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        r"""Sets the height of this VideoInfo.

        视频高度<br/> 

        :param height: The height of this VideoInfo.
        :type height: int
        """
        self._height = height

    @property
    def bitrate(self):
        r"""Gets the bitrate of this VideoInfo.

        码率,单位：kbit/s<br/> 

        :return: The bitrate of this VideoInfo.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        r"""Sets the bitrate of this VideoInfo.

        码率,单位：kbit/s<br/> 

        :param bitrate: The bitrate of this VideoInfo.
        :type bitrate: int
        """
        self._bitrate = bitrate

    @property
    def frame_rate(self):
        r"""Gets the frame_rate of this VideoInfo.

        帧率（默认为0，0代表自适应，单位是帧每秒）<br/> 

        :return: The frame_rate of this VideoInfo.
        :rtype: int
        """
        return self._frame_rate

    @frame_rate.setter
    def frame_rate(self, frame_rate):
        r"""Sets the frame_rate of this VideoInfo.

        帧率（默认为0，0代表自适应，单位是帧每秒）<br/> 

        :param frame_rate: The frame_rate of this VideoInfo.
        :type frame_rate: int
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
        if not isinstance(other, VideoInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
