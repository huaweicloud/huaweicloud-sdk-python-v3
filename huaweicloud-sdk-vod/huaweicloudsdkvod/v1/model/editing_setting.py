# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EditingSetting:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resolution_adaptation': 'str',
        'resolution_upsample': 'str',
        'format': 'str',
        'width': 'int',
        'height': 'int',
        'reference': 'str',
        'video_codec': 'int'
    }

    attribute_map = {
        'resolution_adaptation': 'resolution_adaptation',
        'resolution_upsample': 'resolution_upsample',
        'format': 'format',
        'width': 'width',
        'height': 'height',
        'reference': 'reference',
        'video_codec': 'video_codec'
    }

    def __init__(self, resolution_adaptation=None, resolution_upsample=None, format=None, width=None, height=None, reference=None, video_codec=None):
        r"""EditingSetting

        The model defined in huaweicloud sdk

        :param resolution_adaptation: 分辨率自适应策略, 选值：OPEN, CLOSE（默认OPEN） 输入为OPEN时，width表示长边，height表示短边 输入为CLOSE时，width表示宽度，height表示长度 
        :type resolution_adaptation: str
        :param resolution_upsample: 分辨率上采样开关, 选值：ON, OFF（默认OFF） 
        :type resolution_upsample: str
        :param format: 输出封装格式，HLS、MP4（默认MP4）、MP3、MOV、FLV、AVI 
        :type format: str
        :param width: 输出宽或长边，整型，输入小数向下取整，默认0，按源  - 当 width、height 均为 0，则分辨率取片源分辨率； - 当 width 为 0，height 非 0，则 width 按片源分辨率比例缩放； - 当 width 非 0，height 为 0，则 height 按片源分辨率比例缩放； - 当 width、height 均非 0，则分辨率按用户指定。 
        :type width: int
        :param height: 输出高或短边，整型，输入小数向下取整，默认0，按源  - 当 Width、Height 均为 0，则分辨率取片源分辨率； - 当 Width 为 0，Height 非 0，则 Width 按片源分辨率比例缩放； - 当 Width 非 0，Height 为 0，则 Height 按片源分辨率比例缩放； - 当 Width、Height 均非 0，则分辨率按用户指定。 
        :type height: int
        :param reference: 输出参考基准，可选，默认为空  - NONE 输出分辨率按输入的第一个片源为主，码率按输出分辨率自适应，帧率固定输出25fps - MAX_BITRATE 按码率最大的输入片源参数为基准 - MAX_RESOLUTION 按分辨率最大的输入片源参数为基准 
        :type reference: str
        :param video_codec: 视频编码格式。 取值如下： - 1：VIDEO_CODEC_H264 - 2：VIDEO_CODEC_H265 
        :type video_codec: int
        """
        
        

        self._resolution_adaptation = None
        self._resolution_upsample = None
        self._format = None
        self._width = None
        self._height = None
        self._reference = None
        self._video_codec = None
        self.discriminator = None

        if resolution_adaptation is not None:
            self.resolution_adaptation = resolution_adaptation
        if resolution_upsample is not None:
            self.resolution_upsample = resolution_upsample
        if format is not None:
            self.format = format
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if reference is not None:
            self.reference = reference
        if video_codec is not None:
            self.video_codec = video_codec

    @property
    def resolution_adaptation(self):
        r"""Gets the resolution_adaptation of this EditingSetting.

        分辨率自适应策略, 选值：OPEN, CLOSE（默认OPEN） 输入为OPEN时，width表示长边，height表示短边 输入为CLOSE时，width表示宽度，height表示长度 

        :return: The resolution_adaptation of this EditingSetting.
        :rtype: str
        """
        return self._resolution_adaptation

    @resolution_adaptation.setter
    def resolution_adaptation(self, resolution_adaptation):
        r"""Sets the resolution_adaptation of this EditingSetting.

        分辨率自适应策略, 选值：OPEN, CLOSE（默认OPEN） 输入为OPEN时，width表示长边，height表示短边 输入为CLOSE时，width表示宽度，height表示长度 

        :param resolution_adaptation: The resolution_adaptation of this EditingSetting.
        :type resolution_adaptation: str
        """
        self._resolution_adaptation = resolution_adaptation

    @property
    def resolution_upsample(self):
        r"""Gets the resolution_upsample of this EditingSetting.

        分辨率上采样开关, 选值：ON, OFF（默认OFF） 

        :return: The resolution_upsample of this EditingSetting.
        :rtype: str
        """
        return self._resolution_upsample

    @resolution_upsample.setter
    def resolution_upsample(self, resolution_upsample):
        r"""Sets the resolution_upsample of this EditingSetting.

        分辨率上采样开关, 选值：ON, OFF（默认OFF） 

        :param resolution_upsample: The resolution_upsample of this EditingSetting.
        :type resolution_upsample: str
        """
        self._resolution_upsample = resolution_upsample

    @property
    def format(self):
        r"""Gets the format of this EditingSetting.

        输出封装格式，HLS、MP4（默认MP4）、MP3、MOV、FLV、AVI 

        :return: The format of this EditingSetting.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this EditingSetting.

        输出封装格式，HLS、MP4（默认MP4）、MP3、MOV、FLV、AVI 

        :param format: The format of this EditingSetting.
        :type format: str
        """
        self._format = format

    @property
    def width(self):
        r"""Gets the width of this EditingSetting.

        输出宽或长边，整型，输入小数向下取整，默认0，按源  - 当 width、height 均为 0，则分辨率取片源分辨率； - 当 width 为 0，height 非 0，则 width 按片源分辨率比例缩放； - 当 width 非 0，height 为 0，则 height 按片源分辨率比例缩放； - 当 width、height 均非 0，则分辨率按用户指定。 

        :return: The width of this EditingSetting.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        r"""Sets the width of this EditingSetting.

        输出宽或长边，整型，输入小数向下取整，默认0，按源  - 当 width、height 均为 0，则分辨率取片源分辨率； - 当 width 为 0，height 非 0，则 width 按片源分辨率比例缩放； - 当 width 非 0，height 为 0，则 height 按片源分辨率比例缩放； - 当 width、height 均非 0，则分辨率按用户指定。 

        :param width: The width of this EditingSetting.
        :type width: int
        """
        self._width = width

    @property
    def height(self):
        r"""Gets the height of this EditingSetting.

        输出高或短边，整型，输入小数向下取整，默认0，按源  - 当 Width、Height 均为 0，则分辨率取片源分辨率； - 当 Width 为 0，Height 非 0，则 Width 按片源分辨率比例缩放； - 当 Width 非 0，Height 为 0，则 Height 按片源分辨率比例缩放； - 当 Width、Height 均非 0，则分辨率按用户指定。 

        :return: The height of this EditingSetting.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        r"""Sets the height of this EditingSetting.

        输出高或短边，整型，输入小数向下取整，默认0，按源  - 当 Width、Height 均为 0，则分辨率取片源分辨率； - 当 Width 为 0，Height 非 0，则 Width 按片源分辨率比例缩放； - 当 Width 非 0，Height 为 0，则 Height 按片源分辨率比例缩放； - 当 Width、Height 均非 0，则分辨率按用户指定。 

        :param height: The height of this EditingSetting.
        :type height: int
        """
        self._height = height

    @property
    def reference(self):
        r"""Gets the reference of this EditingSetting.

        输出参考基准，可选，默认为空  - NONE 输出分辨率按输入的第一个片源为主，码率按输出分辨率自适应，帧率固定输出25fps - MAX_BITRATE 按码率最大的输入片源参数为基准 - MAX_RESOLUTION 按分辨率最大的输入片源参数为基准 

        :return: The reference of this EditingSetting.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        r"""Sets the reference of this EditingSetting.

        输出参考基准，可选，默认为空  - NONE 输出分辨率按输入的第一个片源为主，码率按输出分辨率自适应，帧率固定输出25fps - MAX_BITRATE 按码率最大的输入片源参数为基准 - MAX_RESOLUTION 按分辨率最大的输入片源参数为基准 

        :param reference: The reference of this EditingSetting.
        :type reference: str
        """
        self._reference = reference

    @property
    def video_codec(self):
        r"""Gets the video_codec of this EditingSetting.

        视频编码格式。 取值如下： - 1：VIDEO_CODEC_H264 - 2：VIDEO_CODEC_H265 

        :return: The video_codec of this EditingSetting.
        :rtype: int
        """
        return self._video_codec

    @video_codec.setter
    def video_codec(self, video_codec):
        r"""Sets the video_codec of this EditingSetting.

        视频编码格式。 取值如下： - 1：VIDEO_CODEC_H264 - 2：VIDEO_CODEC_H265 

        :param video_codec: The video_codec of this EditingSetting.
        :type video_codec: int
        """
        self._video_codec = video_codec

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
        if not isinstance(other, EditingSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
