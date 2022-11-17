# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WatermarkTemplate:

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
        'image_process': 'str',
        'width': 'str',
        'height': 'str',
        'base': 'str',
        'template_id': 'int',
        'template_name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'dx': 'dx',
        'dy': 'dy',
        'referpos': 'referpos',
        'timeline_start': 'timeline_start',
        'timeline_duration': 'timeline_duration',
        'image_process': 'image_process',
        'width': 'width',
        'height': 'height',
        'base': 'base',
        'template_id': 'template_id',
        'template_name': 'template_name',
        'type': 'type'
    }

    def __init__(self, dx=None, dy=None, referpos=None, timeline_start=None, timeline_duration=None, image_process=None, width=None, height=None, base=None, template_id=None, template_name=None, type=None):
        """WatermarkTemplate

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
        :param image_process: 图片水印处理方式，type设置为Image时有效。  取值如下：  - Original：只做简单缩放，不做其他处理。 - Grayed：彩色图片变灰。 - Transparent：透明化。 
        :type image_process: str
        :param width: 水印图片宽，值有两种形式： - 整数型代水印图片宽的像素值，范围[8，4096]，单位px。 - 小数型代表相对输出视频分辨率宽的比率，范围(0,1)，支持4位小数，如0.9999，超出部分系统自动丢弃。 
        :type width: str
        :param height: 水印图片高，值有两种形式： - 整数型代表水印图片高的像素值，范围[8，4096]，单位px。 - 小数型代表相对输出视频分辨率高的比率，范围(0，1)，支持4位小数，如0.9999，超出部分系统自动丢弃。 
        :type height: str
        :param base: 水印叠加母体  取值如下： - input ：水印叠加在输入片源上，转码输出后实际大小按图像等比例缩放 - output ：水印叠加在转码输出文件上。 
        :type base: str
        :param template_id: 水印模板ID
        :type template_id: int
        :param template_name: 水印模板名称。
        :type template_name: str
        :param type: 水印类型，当前只支持Image（图片水印）。后续根据需求再支持Text（文字水印）。 
        :type type: str
        """
        
        

        self._dx = None
        self._dy = None
        self._referpos = None
        self._timeline_start = None
        self._timeline_duration = None
        self._image_process = None
        self._width = None
        self._height = None
        self._base = None
        self._template_id = None
        self._template_name = None
        self._type = None
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
        if image_process is not None:
            self.image_process = image_process
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if base is not None:
            self.base = base
        if template_id is not None:
            self.template_id = template_id
        if template_name is not None:
            self.template_name = template_name
        if type is not None:
            self.type = type

    @property
    def dx(self):
        """Gets the dx of this WatermarkTemplate.

        水印图片起点相对输出视频顶点的水平偏移量。  设置方法有如下两种：  - 整数型：表示图片起点水平偏移视频顶点的像素值，单位px。取值范围：[0，4096] - 小数型：表示图片起点相对于视频分辨率宽的水平偏移比率。取值范围：(0，1)，支持4位小数，如0.9999，超出部分系统自动丢弃。  示例：输出视频分辨率宽1920，设置“dx”为“0.1”，“referpos”为“TopRight”（右上角），则水印图片右上角到视频右顶点在水平方向上偏移距离为192。 

        :return: The dx of this WatermarkTemplate.
        :rtype: str
        """
        return self._dx

    @dx.setter
    def dx(self, dx):
        """Sets the dx of this WatermarkTemplate.

        水印图片起点相对输出视频顶点的水平偏移量。  设置方法有如下两种：  - 整数型：表示图片起点水平偏移视频顶点的像素值，单位px。取值范围：[0，4096] - 小数型：表示图片起点相对于视频分辨率宽的水平偏移比率。取值范围：(0，1)，支持4位小数，如0.9999，超出部分系统自动丢弃。  示例：输出视频分辨率宽1920，设置“dx”为“0.1”，“referpos”为“TopRight”（右上角），则水印图片右上角到视频右顶点在水平方向上偏移距离为192。 

        :param dx: The dx of this WatermarkTemplate.
        :type dx: str
        """
        self._dx = dx

    @property
    def dy(self):
        """Gets the dy of this WatermarkTemplate.

        水印图片起点相对输出视频顶点的垂直偏移量。  - 设置方法有如下两种：整数型：表示图片起点垂直偏移视频顶点的像素值，单位px。取值范围：[0，4096] - 小数型：表示图片起点相对于视频分辨率高的垂直偏移比率。取值范围：(0，1)，支持4位小数，如0.9999，超出部分系统自动丢弃。  示例：输出视频分辨率高1080，设置“dy”为“0.1”，“referpos”为“TopRight”（右上角），则水印图片右上角到视频右顶点在垂直方向上的偏移距离为108。 

        :return: The dy of this WatermarkTemplate.
        :rtype: str
        """
        return self._dy

    @dy.setter
    def dy(self, dy):
        """Sets the dy of this WatermarkTemplate.

        水印图片起点相对输出视频顶点的垂直偏移量。  - 设置方法有如下两种：整数型：表示图片起点垂直偏移视频顶点的像素值，单位px。取值范围：[0，4096] - 小数型：表示图片起点相对于视频分辨率高的垂直偏移比率。取值范围：(0，1)，支持4位小数，如0.9999，超出部分系统自动丢弃。  示例：输出视频分辨率高1080，设置“dy”为“0.1”，“referpos”为“TopRight”（右上角），则水印图片右上角到视频右顶点在垂直方向上的偏移距离为108。 

        :param dy: The dy of this WatermarkTemplate.
        :type dy: str
        """
        self._dy = dy

    @property
    def referpos(self):
        """Gets the referpos of this WatermarkTemplate.

        水印的位置。  取值如下： - TopRight：右上角。 - TopLeft：左上角。 - BottomRight：右下角。 - BottomLeft：左下角。 

        :return: The referpos of this WatermarkTemplate.
        :rtype: str
        """
        return self._referpos

    @referpos.setter
    def referpos(self, referpos):
        """Sets the referpos of this WatermarkTemplate.

        水印的位置。  取值如下： - TopRight：右上角。 - TopLeft：左上角。 - BottomRight：右下角。 - BottomLeft：左下角。 

        :param referpos: The referpos of this WatermarkTemplate.
        :type referpos: str
        """
        self._referpos = referpos

    @property
    def timeline_start(self):
        """Gets the timeline_start of this WatermarkTemplate.

        水印开始时间，与“timeline_duration”配合使用。  取值范围：数字。  单位：秒。 

        :return: The timeline_start of this WatermarkTemplate.
        :rtype: str
        """
        return self._timeline_start

    @timeline_start.setter
    def timeline_start(self, timeline_start):
        """Sets the timeline_start of this WatermarkTemplate.

        水印开始时间，与“timeline_duration”配合使用。  取值范围：数字。  单位：秒。 

        :param timeline_start: The timeline_start of this WatermarkTemplate.
        :type timeline_start: str
        """
        self._timeline_start = timeline_start

    @property
    def timeline_duration(self):
        """Gets the timeline_duration of this WatermarkTemplate.

        水印持续时间，与“timeline_start”配合使用。  取值范围：[数字，ToEND]。“ToEND”表示持续到视频结束。  默认值：ToEND。 

        :return: The timeline_duration of this WatermarkTemplate.
        :rtype: str
        """
        return self._timeline_duration

    @timeline_duration.setter
    def timeline_duration(self, timeline_duration):
        """Sets the timeline_duration of this WatermarkTemplate.

        水印持续时间，与“timeline_start”配合使用。  取值范围：[数字，ToEND]。“ToEND”表示持续到视频结束。  默认值：ToEND。 

        :param timeline_duration: The timeline_duration of this WatermarkTemplate.
        :type timeline_duration: str
        """
        self._timeline_duration = timeline_duration

    @property
    def image_process(self):
        """Gets the image_process of this WatermarkTemplate.

        图片水印处理方式，type设置为Image时有效。  取值如下：  - Original：只做简单缩放，不做其他处理。 - Grayed：彩色图片变灰。 - Transparent：透明化。 

        :return: The image_process of this WatermarkTemplate.
        :rtype: str
        """
        return self._image_process

    @image_process.setter
    def image_process(self, image_process):
        """Sets the image_process of this WatermarkTemplate.

        图片水印处理方式，type设置为Image时有效。  取值如下：  - Original：只做简单缩放，不做其他处理。 - Grayed：彩色图片变灰。 - Transparent：透明化。 

        :param image_process: The image_process of this WatermarkTemplate.
        :type image_process: str
        """
        self._image_process = image_process

    @property
    def width(self):
        """Gets the width of this WatermarkTemplate.

        水印图片宽，值有两种形式： - 整数型代水印图片宽的像素值，范围[8，4096]，单位px。 - 小数型代表相对输出视频分辨率宽的比率，范围(0,1)，支持4位小数，如0.9999，超出部分系统自动丢弃。 

        :return: The width of this WatermarkTemplate.
        :rtype: str
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this WatermarkTemplate.

        水印图片宽，值有两种形式： - 整数型代水印图片宽的像素值，范围[8，4096]，单位px。 - 小数型代表相对输出视频分辨率宽的比率，范围(0,1)，支持4位小数，如0.9999，超出部分系统自动丢弃。 

        :param width: The width of this WatermarkTemplate.
        :type width: str
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this WatermarkTemplate.

        水印图片高，值有两种形式： - 整数型代表水印图片高的像素值，范围[8，4096]，单位px。 - 小数型代表相对输出视频分辨率高的比率，范围(0，1)，支持4位小数，如0.9999，超出部分系统自动丢弃。 

        :return: The height of this WatermarkTemplate.
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this WatermarkTemplate.

        水印图片高，值有两种形式： - 整数型代表水印图片高的像素值，范围[8，4096]，单位px。 - 小数型代表相对输出视频分辨率高的比率，范围(0，1)，支持4位小数，如0.9999，超出部分系统自动丢弃。 

        :param height: The height of this WatermarkTemplate.
        :type height: str
        """
        self._height = height

    @property
    def base(self):
        """Gets the base of this WatermarkTemplate.

        水印叠加母体  取值如下： - input ：水印叠加在输入片源上，转码输出后实际大小按图像等比例缩放 - output ：水印叠加在转码输出文件上。 

        :return: The base of this WatermarkTemplate.
        :rtype: str
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this WatermarkTemplate.

        水印叠加母体  取值如下： - input ：水印叠加在输入片源上，转码输出后实际大小按图像等比例缩放 - output ：水印叠加在转码输出文件上。 

        :param base: The base of this WatermarkTemplate.
        :type base: str
        """
        self._base = base

    @property
    def template_id(self):
        """Gets the template_id of this WatermarkTemplate.

        水印模板ID

        :return: The template_id of this WatermarkTemplate.
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this WatermarkTemplate.

        水印模板ID

        :param template_id: The template_id of this WatermarkTemplate.
        :type template_id: int
        """
        self._template_id = template_id

    @property
    def template_name(self):
        """Gets the template_name of this WatermarkTemplate.

        水印模板名称。

        :return: The template_name of this WatermarkTemplate.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this WatermarkTemplate.

        水印模板名称。

        :param template_name: The template_name of this WatermarkTemplate.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def type(self):
        """Gets the type of this WatermarkTemplate.

        水印类型，当前只支持Image（图片水印）。后续根据需求再支持Text（文字水印）。 

        :return: The type of this WatermarkTemplate.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WatermarkTemplate.

        水印类型，当前只支持Image（图片水印）。后续根据需求再支持Text（文字水印）。 

        :param type: The type of this WatermarkTemplate.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, WatermarkTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
