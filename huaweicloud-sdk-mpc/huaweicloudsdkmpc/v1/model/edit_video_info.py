# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EditVideoInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reference': 'str',
        'width': 'int',
        'height': 'int',
        'codec': 'str',
        'bitrate': 'int',
        'frame_rate': 'int'
    }

    attribute_map = {
        'reference': 'reference',
        'width': 'width',
        'height': 'height',
        'codec': 'codec',
        'bitrate': 'bitrate',
        'frame_rate': 'frame_rate'
    }

    def __init__(self, reference=None, width=None, height=None, codec=None, bitrate=None, frame_rate=None):
        r"""EditVideoInfo

        The model defined in huaweicloud sdk

        :param reference: 剪辑输出视频参数的参照物。取值如下： - MAX，以输入片源中最大分辨率的视频参数作为输出参照。 - MIN，以输入片源中最小分辨率的视频参数作为输出参照。 - CUSTOM，自定义视频输出参数，使用该参数时，所有视频参数必填。- SHORT_HEIGHT_SHORT_WIDTH，当edit_type为MIX时，只能使用该值。
        :type reference: str
        :param width: 视频宽度。
        :type width: int
        :param height: 视频高度。
        :type height: int
        :param codec: 视频频编码格式。
        :type codec: str
        :param bitrate: 视频码率，单位: bit/s 
        :type bitrate: int
        :param frame_rate: 帧率。 
        :type frame_rate: int
        """
        
        

        self._reference = None
        self._width = None
        self._height = None
        self._codec = None
        self._bitrate = None
        self._frame_rate = None
        self.discriminator = None

        if reference is not None:
            self.reference = reference
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if codec is not None:
            self.codec = codec
        if bitrate is not None:
            self.bitrate = bitrate
        if frame_rate is not None:
            self.frame_rate = frame_rate

    @property
    def reference(self):
        r"""Gets the reference of this EditVideoInfo.

        剪辑输出视频参数的参照物。取值如下： - MAX，以输入片源中最大分辨率的视频参数作为输出参照。 - MIN，以输入片源中最小分辨率的视频参数作为输出参照。 - CUSTOM，自定义视频输出参数，使用该参数时，所有视频参数必填。- SHORT_HEIGHT_SHORT_WIDTH，当edit_type为MIX时，只能使用该值。

        :return: The reference of this EditVideoInfo.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        r"""Sets the reference of this EditVideoInfo.

        剪辑输出视频参数的参照物。取值如下： - MAX，以输入片源中最大分辨率的视频参数作为输出参照。 - MIN，以输入片源中最小分辨率的视频参数作为输出参照。 - CUSTOM，自定义视频输出参数，使用该参数时，所有视频参数必填。- SHORT_HEIGHT_SHORT_WIDTH，当edit_type为MIX时，只能使用该值。

        :param reference: The reference of this EditVideoInfo.
        :type reference: str
        """
        self._reference = reference

    @property
    def width(self):
        r"""Gets the width of this EditVideoInfo.

        视频宽度。

        :return: The width of this EditVideoInfo.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        r"""Sets the width of this EditVideoInfo.

        视频宽度。

        :param width: The width of this EditVideoInfo.
        :type width: int
        """
        self._width = width

    @property
    def height(self):
        r"""Gets the height of this EditVideoInfo.

        视频高度。

        :return: The height of this EditVideoInfo.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        r"""Sets the height of this EditVideoInfo.

        视频高度。

        :param height: The height of this EditVideoInfo.
        :type height: int
        """
        self._height = height

    @property
    def codec(self):
        r"""Gets the codec of this EditVideoInfo.

        视频频编码格式。

        :return: The codec of this EditVideoInfo.
        :rtype: str
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        r"""Sets the codec of this EditVideoInfo.

        视频频编码格式。

        :param codec: The codec of this EditVideoInfo.
        :type codec: str
        """
        self._codec = codec

    @property
    def bitrate(self):
        r"""Gets the bitrate of this EditVideoInfo.

        视频码率，单位: bit/s 

        :return: The bitrate of this EditVideoInfo.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        r"""Sets the bitrate of this EditVideoInfo.

        视频码率，单位: bit/s 

        :param bitrate: The bitrate of this EditVideoInfo.
        :type bitrate: int
        """
        self._bitrate = bitrate

    @property
    def frame_rate(self):
        r"""Gets the frame_rate of this EditVideoInfo.

        帧率。 

        :return: The frame_rate of this EditVideoInfo.
        :rtype: int
        """
        return self._frame_rate

    @frame_rate.setter
    def frame_rate(self, frame_rate):
        r"""Sets the frame_rate of this EditVideoInfo.

        帧率。 

        :param frame_rate: The frame_rate of this EditVideoInfo.
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
        if not isinstance(other, EditVideoInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
