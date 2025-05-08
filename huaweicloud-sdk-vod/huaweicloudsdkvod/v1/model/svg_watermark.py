# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SVGWatermark:

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
        'random_time_min': 'float',
        'random_time_max': 'float',
        'width': 'str',
        'height': 'str'
    }

    attribute_map = {
        'dx': 'dx',
        'dy': 'dy',
        'referpos': 'referpos',
        'timeline_start': 'timeline_start',
        'timeline_duration': 'timeline_duration',
        'random_time_min': 'random_time_min',
        'random_time_max': 'random_time_max',
        'width': 'width',
        'height': 'height'
    }

    def __init__(self, dx=None, dy=None, referpos=None, timeline_start=None, timeline_duration=None, random_time_min=None, random_time_max=None, width=None, height=None):
        r"""SVGWatermark

        The model defined in huaweicloud sdk

        :param dx: 水印图片起点相对输出视频顶点的水平偏移量。 设置方法有如下两种： 整数型：表示图片起点水平偏移视频顶点的像素值，单位px。取值范围：[0，4096] 小数型：表示图片起点相对于视频分辨率宽的水平偏移比率。取值范围：(0，1)，支持4位小数，如0.9999，超出部分系统自动丢弃。 
        :type dx: str
        :param dy: 水印图片起点相对输出视频顶点的垂直偏移量。 设置方法有如下两种： 整数型：表示图片起点水平偏移视频顶点的像素值，单位px。取值范围：[0，4096] 小数型：表示图片起点相对于视频分辨率宽的水平偏移比率。取值范围：(0，1)，支持4位小数，如0.9999，超出部分系统自动丢弃。 
        :type dy: str
        :param referpos: 水印的位置。 取值如下： TopRight：右上角。 TopLeft：左上角。 BottomRight：右下角。 BottomLeft：左下角。 ClockWise：顺时针 AntiClockWise：逆时针 Random：随机跳转 
        :type referpos: str
        :param timeline_start: 水印开始时间，与“timeline_duration”配合使用。 
        :type timeline_start: str
        :param timeline_duration: 水印持续时间，与“timeline_start”配合使用。 取值范围：[数字，ToEND]。“ToEND”表示持续到视频结束。 默认值：ToEND。 
        :type timeline_duration: str
        :param random_time_min: 随机时间最小值，单位：秒 
        :type random_time_min: float
        :param random_time_max: 随机时间最大值，单位：秒 
        :type random_time_max: float
        :param width: 水印图片宽，值有两种形式： 整数型代水印图片宽的像素值，范围[8，4096]，单位px。 小数型代表相对输出视频分辨率宽的比率，范围(0,1)，支持4位小数，如0.9999，超出部分系统自动丢弃。 
        :type width: str
        :param height: 水印图片高，值有两种形式： 整数型代表水印图片高的像素值，范围[8，4096]，单位px。 小数型代表相对输出视频分辨率高的比率，范围(0，1)，支持4位小数，如0.9999，超出部分系统自动丢弃。 
        :type height: str
        """
        
        

        self._dx = None
        self._dy = None
        self._referpos = None
        self._timeline_start = None
        self._timeline_duration = None
        self._random_time_min = None
        self._random_time_max = None
        self._width = None
        self._height = None
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
        if random_time_min is not None:
            self.random_time_min = random_time_min
        if random_time_max is not None:
            self.random_time_max = random_time_max
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height

    @property
    def dx(self):
        r"""Gets the dx of this SVGWatermark.

        水印图片起点相对输出视频顶点的水平偏移量。 设置方法有如下两种： 整数型：表示图片起点水平偏移视频顶点的像素值，单位px。取值范围：[0，4096] 小数型：表示图片起点相对于视频分辨率宽的水平偏移比率。取值范围：(0，1)，支持4位小数，如0.9999，超出部分系统自动丢弃。 

        :return: The dx of this SVGWatermark.
        :rtype: str
        """
        return self._dx

    @dx.setter
    def dx(self, dx):
        r"""Sets the dx of this SVGWatermark.

        水印图片起点相对输出视频顶点的水平偏移量。 设置方法有如下两种： 整数型：表示图片起点水平偏移视频顶点的像素值，单位px。取值范围：[0，4096] 小数型：表示图片起点相对于视频分辨率宽的水平偏移比率。取值范围：(0，1)，支持4位小数，如0.9999，超出部分系统自动丢弃。 

        :param dx: The dx of this SVGWatermark.
        :type dx: str
        """
        self._dx = dx

    @property
    def dy(self):
        r"""Gets the dy of this SVGWatermark.

        水印图片起点相对输出视频顶点的垂直偏移量。 设置方法有如下两种： 整数型：表示图片起点水平偏移视频顶点的像素值，单位px。取值范围：[0，4096] 小数型：表示图片起点相对于视频分辨率宽的水平偏移比率。取值范围：(0，1)，支持4位小数，如0.9999，超出部分系统自动丢弃。 

        :return: The dy of this SVGWatermark.
        :rtype: str
        """
        return self._dy

    @dy.setter
    def dy(self, dy):
        r"""Sets the dy of this SVGWatermark.

        水印图片起点相对输出视频顶点的垂直偏移量。 设置方法有如下两种： 整数型：表示图片起点水平偏移视频顶点的像素值，单位px。取值范围：[0，4096] 小数型：表示图片起点相对于视频分辨率宽的水平偏移比率。取值范围：(0，1)，支持4位小数，如0.9999，超出部分系统自动丢弃。 

        :param dy: The dy of this SVGWatermark.
        :type dy: str
        """
        self._dy = dy

    @property
    def referpos(self):
        r"""Gets the referpos of this SVGWatermark.

        水印的位置。 取值如下： TopRight：右上角。 TopLeft：左上角。 BottomRight：右下角。 BottomLeft：左下角。 ClockWise：顺时针 AntiClockWise：逆时针 Random：随机跳转 

        :return: The referpos of this SVGWatermark.
        :rtype: str
        """
        return self._referpos

    @referpos.setter
    def referpos(self, referpos):
        r"""Sets the referpos of this SVGWatermark.

        水印的位置。 取值如下： TopRight：右上角。 TopLeft：左上角。 BottomRight：右下角。 BottomLeft：左下角。 ClockWise：顺时针 AntiClockWise：逆时针 Random：随机跳转 

        :param referpos: The referpos of this SVGWatermark.
        :type referpos: str
        """
        self._referpos = referpos

    @property
    def timeline_start(self):
        r"""Gets the timeline_start of this SVGWatermark.

        水印开始时间，与“timeline_duration”配合使用。 

        :return: The timeline_start of this SVGWatermark.
        :rtype: str
        """
        return self._timeline_start

    @timeline_start.setter
    def timeline_start(self, timeline_start):
        r"""Sets the timeline_start of this SVGWatermark.

        水印开始时间，与“timeline_duration”配合使用。 

        :param timeline_start: The timeline_start of this SVGWatermark.
        :type timeline_start: str
        """
        self._timeline_start = timeline_start

    @property
    def timeline_duration(self):
        r"""Gets the timeline_duration of this SVGWatermark.

        水印持续时间，与“timeline_start”配合使用。 取值范围：[数字，ToEND]。“ToEND”表示持续到视频结束。 默认值：ToEND。 

        :return: The timeline_duration of this SVGWatermark.
        :rtype: str
        """
        return self._timeline_duration

    @timeline_duration.setter
    def timeline_duration(self, timeline_duration):
        r"""Sets the timeline_duration of this SVGWatermark.

        水印持续时间，与“timeline_start”配合使用。 取值范围：[数字，ToEND]。“ToEND”表示持续到视频结束。 默认值：ToEND。 

        :param timeline_duration: The timeline_duration of this SVGWatermark.
        :type timeline_duration: str
        """
        self._timeline_duration = timeline_duration

    @property
    def random_time_min(self):
        r"""Gets the random_time_min of this SVGWatermark.

        随机时间最小值，单位：秒 

        :return: The random_time_min of this SVGWatermark.
        :rtype: float
        """
        return self._random_time_min

    @random_time_min.setter
    def random_time_min(self, random_time_min):
        r"""Sets the random_time_min of this SVGWatermark.

        随机时间最小值，单位：秒 

        :param random_time_min: The random_time_min of this SVGWatermark.
        :type random_time_min: float
        """
        self._random_time_min = random_time_min

    @property
    def random_time_max(self):
        r"""Gets the random_time_max of this SVGWatermark.

        随机时间最大值，单位：秒 

        :return: The random_time_max of this SVGWatermark.
        :rtype: float
        """
        return self._random_time_max

    @random_time_max.setter
    def random_time_max(self, random_time_max):
        r"""Sets the random_time_max of this SVGWatermark.

        随机时间最大值，单位：秒 

        :param random_time_max: The random_time_max of this SVGWatermark.
        :type random_time_max: float
        """
        self._random_time_max = random_time_max

    @property
    def width(self):
        r"""Gets the width of this SVGWatermark.

        水印图片宽，值有两种形式： 整数型代水印图片宽的像素值，范围[8，4096]，单位px。 小数型代表相对输出视频分辨率宽的比率，范围(0,1)，支持4位小数，如0.9999，超出部分系统自动丢弃。 

        :return: The width of this SVGWatermark.
        :rtype: str
        """
        return self._width

    @width.setter
    def width(self, width):
        r"""Sets the width of this SVGWatermark.

        水印图片宽，值有两种形式： 整数型代水印图片宽的像素值，范围[8，4096]，单位px。 小数型代表相对输出视频分辨率宽的比率，范围(0,1)，支持4位小数，如0.9999，超出部分系统自动丢弃。 

        :param width: The width of this SVGWatermark.
        :type width: str
        """
        self._width = width

    @property
    def height(self):
        r"""Gets the height of this SVGWatermark.

        水印图片高，值有两种形式： 整数型代表水印图片高的像素值，范围[8，4096]，单位px。 小数型代表相对输出视频分辨率高的比率，范围(0，1)，支持4位小数，如0.9999，超出部分系统自动丢弃。 

        :return: The height of this SVGWatermark.
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        r"""Sets the height of this SVGWatermark.

        水印图片高，值有两种形式： 整数型代表水印图片高的像素值，范围[8，4096]，单位px。 小数型代表相对输出视频分辨率高的比率，范围(0，1)，支持4位小数，如0.9999，超出部分系统自动丢弃。 

        :param height: The height of this SVGWatermark.
        :type height: str
        """
        self._height = height

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
        if not isinstance(other, SVGWatermark):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
