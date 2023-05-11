# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TextWatermark:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dx': 'str',
        'dy': 'str',
        'referpos': 'str',
        'timeline_start': 'str',
        'timeline_duration': 'str',
        'font_name': 'str',
        'font_size': 'int',
        'font_color': 'str',
        'base': 'str'
    }

    attribute_map = {
        'dx': 'dx',
        'dy': 'dy',
        'referpos': 'referpos',
        'timeline_start': 'timeline_start',
        'timeline_duration': 'timeline_duration',
        'font_name': 'font_name',
        'font_size': 'font_size',
        'font_color': 'font_color',
        'base': 'base'
    }

    def __init__(self, dx=None, dy=None, referpos=None, timeline_start=None, timeline_duration=None, font_name=None, font_size=None, font_color=None, base=None):
        """TextWatermark

        The model defined in huaweicloud sdk

        :param dx: 水印图片起点相对输出视频顶点的水平偏移量。  设置方法有如下两种：  - 整数型：表示图片起点水平偏移视频顶点的像素值，单位px。取值范围：[0，4096] - 小数型：表示图片起点相对于视频分辨率宽的水平偏移比率。取值范围：(0，1)，支持4位小数，如0.9999，超出部分系统自动丢弃。  示例：输出视频分辨率宽1920，设置“dx”为“0.1”，“referpos”为“TopRight”（右上角），则水印图片右上角到视频右顶点在水平方向上偏移距离为192。 
        :type dx: str
        :param dy: 水印图片起点相对输出视频顶点的垂直偏移量。  - 设置方法有如下两种：整数型：表示图片起点垂直偏移视频顶点的像素值，单位px。取值范围：[0，4096] - 小数型：表示图片起点相对于视频分辨率高的垂直偏移比率。取值范围：(0，1)，支持4位小数，如0.9999，超出部分系统自动丢弃。  示例：输出视频分辨率高1080，设置“dy”为“0.1”，“referpos”为“TopRight”（右上角），则水印图片右上角到视频右顶点在垂直方向上的偏移距离为108。 
        :type dy: str
        :param referpos: 水印的位置。  取值如下： - TopRight：右上角。 - TopLeft：左上角。 - BottomRight：右下角。 - BottomLeft：左下角。 
        :type referpos: str
        :param timeline_start: 水印开始时间，与“timeline_duration”配合使用。  取值范围：数字。  单位：秒。 
        :type timeline_start: str
        :param timeline_duration: 水印持续时间，与“timeline_start”配合使用。  取值范围：[数字，ToEND]。“ToEND”表示持续到视频结束。  默认值：ToEND。 
        :type timeline_duration: str
        :param font_name: 字体，当前支持fzyouh 
        :type font_name: str
        :param font_size: 字体大小。  取值范围：[4, 120] 
        :type font_size: int
        :param font_color: 字体颜色。 目前颜色支持 black，blue，white，green，red，yellow，brown，gold，pink，orange，purple。 
        :type font_color: str
        :param base: 水印叠加母体 取值如下： - input：水印叠加在输入片源上，转码输出后实际大小按图像等比例缩放 - output：水印叠加在转码输出文件上。 默认值：input 
        :type base: str
        """
        
        

        self._dx = None
        self._dy = None
        self._referpos = None
        self._timeline_start = None
        self._timeline_duration = None
        self._font_name = None
        self._font_size = None
        self._font_color = None
        self._base = None
        self.discriminator = None

        if dx is not None:
            self.dx = dx
        if dy is not None:
            self.dy = dy
        if referpos is not None:
            self.referpos = referpos
        if timeline_start is not None:
            self.timeline_start = timeline_start
        if timeline_duration is not None:
            self.timeline_duration = timeline_duration
        if font_name is not None:
            self.font_name = font_name
        if font_size is not None:
            self.font_size = font_size
        if font_color is not None:
            self.font_color = font_color
        if base is not None:
            self.base = base

    @property
    def dx(self):
        """Gets the dx of this TextWatermark.

        水印图片起点相对输出视频顶点的水平偏移量。  设置方法有如下两种：  - 整数型：表示图片起点水平偏移视频顶点的像素值，单位px。取值范围：[0，4096] - 小数型：表示图片起点相对于视频分辨率宽的水平偏移比率。取值范围：(0，1)，支持4位小数，如0.9999，超出部分系统自动丢弃。  示例：输出视频分辨率宽1920，设置“dx”为“0.1”，“referpos”为“TopRight”（右上角），则水印图片右上角到视频右顶点在水平方向上偏移距离为192。 

        :return: The dx of this TextWatermark.
        :rtype: str
        """
        return self._dx

    @dx.setter
    def dx(self, dx):
        """Sets the dx of this TextWatermark.

        水印图片起点相对输出视频顶点的水平偏移量。  设置方法有如下两种：  - 整数型：表示图片起点水平偏移视频顶点的像素值，单位px。取值范围：[0，4096] - 小数型：表示图片起点相对于视频分辨率宽的水平偏移比率。取值范围：(0，1)，支持4位小数，如0.9999，超出部分系统自动丢弃。  示例：输出视频分辨率宽1920，设置“dx”为“0.1”，“referpos”为“TopRight”（右上角），则水印图片右上角到视频右顶点在水平方向上偏移距离为192。 

        :param dx: The dx of this TextWatermark.
        :type dx: str
        """
        self._dx = dx

    @property
    def dy(self):
        """Gets the dy of this TextWatermark.

        水印图片起点相对输出视频顶点的垂直偏移量。  - 设置方法有如下两种：整数型：表示图片起点垂直偏移视频顶点的像素值，单位px。取值范围：[0，4096] - 小数型：表示图片起点相对于视频分辨率高的垂直偏移比率。取值范围：(0，1)，支持4位小数，如0.9999，超出部分系统自动丢弃。  示例：输出视频分辨率高1080，设置“dy”为“0.1”，“referpos”为“TopRight”（右上角），则水印图片右上角到视频右顶点在垂直方向上的偏移距离为108。 

        :return: The dy of this TextWatermark.
        :rtype: str
        """
        return self._dy

    @dy.setter
    def dy(self, dy):
        """Sets the dy of this TextWatermark.

        水印图片起点相对输出视频顶点的垂直偏移量。  - 设置方法有如下两种：整数型：表示图片起点垂直偏移视频顶点的像素值，单位px。取值范围：[0，4096] - 小数型：表示图片起点相对于视频分辨率高的垂直偏移比率。取值范围：(0，1)，支持4位小数，如0.9999，超出部分系统自动丢弃。  示例：输出视频分辨率高1080，设置“dy”为“0.1”，“referpos”为“TopRight”（右上角），则水印图片右上角到视频右顶点在垂直方向上的偏移距离为108。 

        :param dy: The dy of this TextWatermark.
        :type dy: str
        """
        self._dy = dy

    @property
    def referpos(self):
        """Gets the referpos of this TextWatermark.

        水印的位置。  取值如下： - TopRight：右上角。 - TopLeft：左上角。 - BottomRight：右下角。 - BottomLeft：左下角。 

        :return: The referpos of this TextWatermark.
        :rtype: str
        """
        return self._referpos

    @referpos.setter
    def referpos(self, referpos):
        """Sets the referpos of this TextWatermark.

        水印的位置。  取值如下： - TopRight：右上角。 - TopLeft：左上角。 - BottomRight：右下角。 - BottomLeft：左下角。 

        :param referpos: The referpos of this TextWatermark.
        :type referpos: str
        """
        self._referpos = referpos

    @property
    def timeline_start(self):
        """Gets the timeline_start of this TextWatermark.

        水印开始时间，与“timeline_duration”配合使用。  取值范围：数字。  单位：秒。 

        :return: The timeline_start of this TextWatermark.
        :rtype: str
        """
        return self._timeline_start

    @timeline_start.setter
    def timeline_start(self, timeline_start):
        """Sets the timeline_start of this TextWatermark.

        水印开始时间，与“timeline_duration”配合使用。  取值范围：数字。  单位：秒。 

        :param timeline_start: The timeline_start of this TextWatermark.
        :type timeline_start: str
        """
        self._timeline_start = timeline_start

    @property
    def timeline_duration(self):
        """Gets the timeline_duration of this TextWatermark.

        水印持续时间，与“timeline_start”配合使用。  取值范围：[数字，ToEND]。“ToEND”表示持续到视频结束。  默认值：ToEND。 

        :return: The timeline_duration of this TextWatermark.
        :rtype: str
        """
        return self._timeline_duration

    @timeline_duration.setter
    def timeline_duration(self, timeline_duration):
        """Sets the timeline_duration of this TextWatermark.

        水印持续时间，与“timeline_start”配合使用。  取值范围：[数字，ToEND]。“ToEND”表示持续到视频结束。  默认值：ToEND。 

        :param timeline_duration: The timeline_duration of this TextWatermark.
        :type timeline_duration: str
        """
        self._timeline_duration = timeline_duration

    @property
    def font_name(self):
        """Gets the font_name of this TextWatermark.

        字体，当前支持fzyouh 

        :return: The font_name of this TextWatermark.
        :rtype: str
        """
        return self._font_name

    @font_name.setter
    def font_name(self, font_name):
        """Sets the font_name of this TextWatermark.

        字体，当前支持fzyouh 

        :param font_name: The font_name of this TextWatermark.
        :type font_name: str
        """
        self._font_name = font_name

    @property
    def font_size(self):
        """Gets the font_size of this TextWatermark.

        字体大小。  取值范围：[4, 120] 

        :return: The font_size of this TextWatermark.
        :rtype: int
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        """Sets the font_size of this TextWatermark.

        字体大小。  取值范围：[4, 120] 

        :param font_size: The font_size of this TextWatermark.
        :type font_size: int
        """
        self._font_size = font_size

    @property
    def font_color(self):
        """Gets the font_color of this TextWatermark.

        字体颜色。 目前颜色支持 black，blue，white，green，red，yellow，brown，gold，pink，orange，purple。 

        :return: The font_color of this TextWatermark.
        :rtype: str
        """
        return self._font_color

    @font_color.setter
    def font_color(self, font_color):
        """Sets the font_color of this TextWatermark.

        字体颜色。 目前颜色支持 black，blue，white，green，red，yellow，brown，gold，pink，orange，purple。 

        :param font_color: The font_color of this TextWatermark.
        :type font_color: str
        """
        self._font_color = font_color

    @property
    def base(self):
        """Gets the base of this TextWatermark.

        水印叠加母体 取值如下： - input：水印叠加在输入片源上，转码输出后实际大小按图像等比例缩放 - output：水印叠加在转码输出文件上。 默认值：input 

        :return: The base of this TextWatermark.
        :rtype: str
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this TextWatermark.

        水印叠加母体 取值如下： - input：水印叠加在输入片源上，转码输出后实际大小按图像等比例缩放 - output：水印叠加在转码输出文件上。 默认值：input 

        :param base: The base of this TextWatermark.
        :type base: str
        """
        self._base = base

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
        if not isinstance(other, TextWatermark):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
