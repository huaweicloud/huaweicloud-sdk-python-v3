# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageWatermarkSetting:

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
        'overlay_input': 'str',
        'input': 'ObsObjInfo',
        'base': 'str'
    }

    attribute_map = {
        'dx': 'dx',
        'dy': 'dy',
        'referpos': 'referpos',
        'timeline_start': 'timeline_start',
        'timeline_duration': 'timeline_duration',
        'overlay_input': 'overlay_input',
        'input': 'input',
        'base': 'base'
    }

    def __init__(self, dx=None, dy=None, referpos=None, timeline_start=None, timeline_duration=None, overlay_input=None, input=None, base=None):
        """ImageWatermarkSetting

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
        :param overlay_input: 对应拼接列表中第几个片段打水印，从0开始，\&quot;0表示第1个，“1”表示第二个，不带或填\&quot;ALL\&quot;表示所有拼接片源打水印。 
        :type overlay_input: str
        :param input: 
        :type input: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        :param base: 水印叠加母体  取值如下： - input ：水印叠加在输入片源上，转码输出后实际大小按图像等比例缩放 - output ：水印叠加在转码输出文件上。 
        :type base: str
        """
        
        

        self._dx = None
        self._dy = None
        self._referpos = None
        self._timeline_start = None
        self._timeline_duration = None
        self._overlay_input = None
        self._input = None
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
        if overlay_input is not None:
            self.overlay_input = overlay_input
        if input is not None:
            self.input = input
        if base is not None:
            self.base = base

    @property
    def dx(self):
        """Gets the dx of this ImageWatermarkSetting.

        水印图片起点相对输出视频顶点的水平偏移量。  设置方法有如下两种：  - 整数型：表示图片起点水平偏移视频顶点的像素值，单位px。取值范围：[0，4096] - 小数型：表示图片起点相对于视频分辨率宽的水平偏移比率。取值范围：(0，1)，支持4位小数，如0.9999，超出部分系统自动丢弃。  示例：输出视频分辨率宽1920，设置“dx”为“0.1”，“referpos”为“TopRight”（右上角），则水印图片右上角到视频右顶点在水平方向上偏移距离为192。 

        :return: The dx of this ImageWatermarkSetting.
        :rtype: str
        """
        return self._dx

    @dx.setter
    def dx(self, dx):
        """Sets the dx of this ImageWatermarkSetting.

        水印图片起点相对输出视频顶点的水平偏移量。  设置方法有如下两种：  - 整数型：表示图片起点水平偏移视频顶点的像素值，单位px。取值范围：[0，4096] - 小数型：表示图片起点相对于视频分辨率宽的水平偏移比率。取值范围：(0，1)，支持4位小数，如0.9999，超出部分系统自动丢弃。  示例：输出视频分辨率宽1920，设置“dx”为“0.1”，“referpos”为“TopRight”（右上角），则水印图片右上角到视频右顶点在水平方向上偏移距离为192。 

        :param dx: The dx of this ImageWatermarkSetting.
        :type dx: str
        """
        self._dx = dx

    @property
    def dy(self):
        """Gets the dy of this ImageWatermarkSetting.

        水印图片起点相对输出视频顶点的垂直偏移量。  - 设置方法有如下两种：整数型：表示图片起点垂直偏移视频顶点的像素值，单位px。取值范围：[0，4096] - 小数型：表示图片起点相对于视频分辨率高的垂直偏移比率。取值范围：(0，1)，支持4位小数，如0.9999，超出部分系统自动丢弃。  示例：输出视频分辨率高1080，设置“dy”为“0.1”，“referpos”为“TopRight”（右上角），则水印图片右上角到视频右顶点在垂直方向上的偏移距离为108。 

        :return: The dy of this ImageWatermarkSetting.
        :rtype: str
        """
        return self._dy

    @dy.setter
    def dy(self, dy):
        """Sets the dy of this ImageWatermarkSetting.

        水印图片起点相对输出视频顶点的垂直偏移量。  - 设置方法有如下两种：整数型：表示图片起点垂直偏移视频顶点的像素值，单位px。取值范围：[0，4096] - 小数型：表示图片起点相对于视频分辨率高的垂直偏移比率。取值范围：(0，1)，支持4位小数，如0.9999，超出部分系统自动丢弃。  示例：输出视频分辨率高1080，设置“dy”为“0.1”，“referpos”为“TopRight”（右上角），则水印图片右上角到视频右顶点在垂直方向上的偏移距离为108。 

        :param dy: The dy of this ImageWatermarkSetting.
        :type dy: str
        """
        self._dy = dy

    @property
    def referpos(self):
        """Gets the referpos of this ImageWatermarkSetting.

        水印的位置。  取值如下： - TopRight：右上角。 - TopLeft：左上角。 - BottomRight：右下角。 - BottomLeft：左下角。 

        :return: The referpos of this ImageWatermarkSetting.
        :rtype: str
        """
        return self._referpos

    @referpos.setter
    def referpos(self, referpos):
        """Sets the referpos of this ImageWatermarkSetting.

        水印的位置。  取值如下： - TopRight：右上角。 - TopLeft：左上角。 - BottomRight：右下角。 - BottomLeft：左下角。 

        :param referpos: The referpos of this ImageWatermarkSetting.
        :type referpos: str
        """
        self._referpos = referpos

    @property
    def timeline_start(self):
        """Gets the timeline_start of this ImageWatermarkSetting.

        水印开始时间，与“timeline_duration”配合使用。  取值范围：数字。  单位：秒。 

        :return: The timeline_start of this ImageWatermarkSetting.
        :rtype: str
        """
        return self._timeline_start

    @timeline_start.setter
    def timeline_start(self, timeline_start):
        """Sets the timeline_start of this ImageWatermarkSetting.

        水印开始时间，与“timeline_duration”配合使用。  取值范围：数字。  单位：秒。 

        :param timeline_start: The timeline_start of this ImageWatermarkSetting.
        :type timeline_start: str
        """
        self._timeline_start = timeline_start

    @property
    def timeline_duration(self):
        """Gets the timeline_duration of this ImageWatermarkSetting.

        水印持续时间，与“timeline_start”配合使用。  取值范围：[数字，ToEND]。“ToEND”表示持续到视频结束。  默认值：ToEND。 

        :return: The timeline_duration of this ImageWatermarkSetting.
        :rtype: str
        """
        return self._timeline_duration

    @timeline_duration.setter
    def timeline_duration(self, timeline_duration):
        """Sets the timeline_duration of this ImageWatermarkSetting.

        水印持续时间，与“timeline_start”配合使用。  取值范围：[数字，ToEND]。“ToEND”表示持续到视频结束。  默认值：ToEND。 

        :param timeline_duration: The timeline_duration of this ImageWatermarkSetting.
        :type timeline_duration: str
        """
        self._timeline_duration = timeline_duration

    @property
    def overlay_input(self):
        """Gets the overlay_input of this ImageWatermarkSetting.

        对应拼接列表中第几个片段打水印，从0开始，\"0表示第1个，“1”表示第二个，不带或填\"ALL\"表示所有拼接片源打水印。 

        :return: The overlay_input of this ImageWatermarkSetting.
        :rtype: str
        """
        return self._overlay_input

    @overlay_input.setter
    def overlay_input(self, overlay_input):
        """Sets the overlay_input of this ImageWatermarkSetting.

        对应拼接列表中第几个片段打水印，从0开始，\"0表示第1个，“1”表示第二个，不带或填\"ALL\"表示所有拼接片源打水印。 

        :param overlay_input: The overlay_input of this ImageWatermarkSetting.
        :type overlay_input: str
        """
        self._overlay_input = overlay_input

    @property
    def input(self):
        """Gets the input of this ImageWatermarkSetting.

        :return: The input of this ImageWatermarkSetting.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this ImageWatermarkSetting.

        :param input: The input of this ImageWatermarkSetting.
        :type input: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._input = input

    @property
    def base(self):
        """Gets the base of this ImageWatermarkSetting.

        水印叠加母体  取值如下： - input ：水印叠加在输入片源上，转码输出后实际大小按图像等比例缩放 - output ：水印叠加在转码输出文件上。 

        :return: The base of this ImageWatermarkSetting.
        :rtype: str
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this ImageWatermarkSetting.

        水印叠加母体  取值如下： - input ：水印叠加在输入片源上，转码输出后实际大小按图像等比例缩放 - output ：水印叠加在转码输出文件上。 

        :param base: The base of this ImageWatermarkSetting.
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
        if not isinstance(other, ImageWatermarkSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
