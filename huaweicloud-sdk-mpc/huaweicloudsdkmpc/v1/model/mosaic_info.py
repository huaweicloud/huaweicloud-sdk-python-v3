# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MosaicInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'timeline_start': 'str',
        'timeline_duration': 'str',
        'dx': 'str',
        'dy': 'str',
        'width': 'str',
        'height': 'str'
    }

    attribute_map = {
        'timeline_start': 'timeline_start',
        'timeline_duration': 'timeline_duration',
        'dx': 'dx',
        'dy': 'dy',
        'width': 'width',
        'height': 'height'
    }

    def __init__(self, timeline_start=None, timeline_duration=None, dx=None, dy=None, width=None, height=None):
        """MosaicInfo

        The model defined in huaweicloud sdk

        :param timeline_start: 马赛克开始时间，与“timeline_duration”配合使用。  取值范围：数字。  单位：秒。 
        :type timeline_start: str
        :param timeline_duration: 马赛克持续时间，与“timeline_start”配合使用。  取值范围：[数字，ToEND]。“ToEND”表示持续到视频结束。  默认值：ToEND。 
        :type timeline_duration: str
        :param dx: 马赛克起点相对输出视频顶点的水平偏移量。  设置方法有如下两种：  - 整数型：表示马赛克起点水平偏移视频顶点的像素值，单位px。取值范围：[0，4096] - 小数型：表示马赛克起点相对于视频分辨率宽的水平偏移比率。取值范围：(0，1)，支持4位小数，如0.9999。  示例：输出视频分辨率宽1920，设置“dx”为“0.1”，“referpos”为“TopRight”（右上角），则马赛克右上角到视频右顶点在水平方向上偏移距离为192。 
        :type dx: str
        :param dy: 马赛克起点相对输出视频顶点的垂直偏移量。  - 设置方法有如下两种：整数型：表示马赛克起点垂直偏移视频顶点的像素值，单位px。取值范围：[0，4096] - 小数型：表示马赛克起点相对于视频分辨率高的垂直偏移比率。取值范围：(0，1)，支持4位小数，如0.9999。  示例：输出视频分辨率高1080，设置“dy”为“0.1”，“referpos”为“TopRight”（右上角），则马赛克右上角到视频右顶点在垂直方向上的偏移距离为108。 
        :type dy: str
        :param width: 马赛克宽，值有两种形式： - 整数型代马赛克宽的像素值，范围[8，4096]，单位px。 - 小数型代表相对输出视频分辨率宽的比率，范围(0,1)，支持4位小数，如0.9999。 
        :type width: str
        :param height: 马赛克高，值有两种形式： - 整数型代表马赛克的像素值，范围[8，4096]，单位px。 - 小数型代表相对输出视频分辨率高的比率，范围(0，1)，支持4位小数，如0.9999。 
        :type height: str
        """
        
        

        self._timeline_start = None
        self._timeline_duration = None
        self._dx = None
        self._dy = None
        self._width = None
        self._height = None
        self.discriminator = None

        if timeline_start is not None:
            self.timeline_start = timeline_start
        if timeline_duration is not None:
            self.timeline_duration = timeline_duration
        if dx is not None:
            self.dx = dx
        if dy is not None:
            self.dy = dy
        self.width = width
        self.height = height

    @property
    def timeline_start(self):
        """Gets the timeline_start of this MosaicInfo.

        马赛克开始时间，与“timeline_duration”配合使用。  取值范围：数字。  单位：秒。 

        :return: The timeline_start of this MosaicInfo.
        :rtype: str
        """
        return self._timeline_start

    @timeline_start.setter
    def timeline_start(self, timeline_start):
        """Sets the timeline_start of this MosaicInfo.

        马赛克开始时间，与“timeline_duration”配合使用。  取值范围：数字。  单位：秒。 

        :param timeline_start: The timeline_start of this MosaicInfo.
        :type timeline_start: str
        """
        self._timeline_start = timeline_start

    @property
    def timeline_duration(self):
        """Gets the timeline_duration of this MosaicInfo.

        马赛克持续时间，与“timeline_start”配合使用。  取值范围：[数字，ToEND]。“ToEND”表示持续到视频结束。  默认值：ToEND。 

        :return: The timeline_duration of this MosaicInfo.
        :rtype: str
        """
        return self._timeline_duration

    @timeline_duration.setter
    def timeline_duration(self, timeline_duration):
        """Sets the timeline_duration of this MosaicInfo.

        马赛克持续时间，与“timeline_start”配合使用。  取值范围：[数字，ToEND]。“ToEND”表示持续到视频结束。  默认值：ToEND。 

        :param timeline_duration: The timeline_duration of this MosaicInfo.
        :type timeline_duration: str
        """
        self._timeline_duration = timeline_duration

    @property
    def dx(self):
        """Gets the dx of this MosaicInfo.

        马赛克起点相对输出视频顶点的水平偏移量。  设置方法有如下两种：  - 整数型：表示马赛克起点水平偏移视频顶点的像素值，单位px。取值范围：[0，4096] - 小数型：表示马赛克起点相对于视频分辨率宽的水平偏移比率。取值范围：(0，1)，支持4位小数，如0.9999。  示例：输出视频分辨率宽1920，设置“dx”为“0.1”，“referpos”为“TopRight”（右上角），则马赛克右上角到视频右顶点在水平方向上偏移距离为192。 

        :return: The dx of this MosaicInfo.
        :rtype: str
        """
        return self._dx

    @dx.setter
    def dx(self, dx):
        """Sets the dx of this MosaicInfo.

        马赛克起点相对输出视频顶点的水平偏移量。  设置方法有如下两种：  - 整数型：表示马赛克起点水平偏移视频顶点的像素值，单位px。取值范围：[0，4096] - 小数型：表示马赛克起点相对于视频分辨率宽的水平偏移比率。取值范围：(0，1)，支持4位小数，如0.9999。  示例：输出视频分辨率宽1920，设置“dx”为“0.1”，“referpos”为“TopRight”（右上角），则马赛克右上角到视频右顶点在水平方向上偏移距离为192。 

        :param dx: The dx of this MosaicInfo.
        :type dx: str
        """
        self._dx = dx

    @property
    def dy(self):
        """Gets the dy of this MosaicInfo.

        马赛克起点相对输出视频顶点的垂直偏移量。  - 设置方法有如下两种：整数型：表示马赛克起点垂直偏移视频顶点的像素值，单位px。取值范围：[0，4096] - 小数型：表示马赛克起点相对于视频分辨率高的垂直偏移比率。取值范围：(0，1)，支持4位小数，如0.9999。  示例：输出视频分辨率高1080，设置“dy”为“0.1”，“referpos”为“TopRight”（右上角），则马赛克右上角到视频右顶点在垂直方向上的偏移距离为108。 

        :return: The dy of this MosaicInfo.
        :rtype: str
        """
        return self._dy

    @dy.setter
    def dy(self, dy):
        """Sets the dy of this MosaicInfo.

        马赛克起点相对输出视频顶点的垂直偏移量。  - 设置方法有如下两种：整数型：表示马赛克起点垂直偏移视频顶点的像素值，单位px。取值范围：[0，4096] - 小数型：表示马赛克起点相对于视频分辨率高的垂直偏移比率。取值范围：(0，1)，支持4位小数，如0.9999。  示例：输出视频分辨率高1080，设置“dy”为“0.1”，“referpos”为“TopRight”（右上角），则马赛克右上角到视频右顶点在垂直方向上的偏移距离为108。 

        :param dy: The dy of this MosaicInfo.
        :type dy: str
        """
        self._dy = dy

    @property
    def width(self):
        """Gets the width of this MosaicInfo.

        马赛克宽，值有两种形式： - 整数型代马赛克宽的像素值，范围[8，4096]，单位px。 - 小数型代表相对输出视频分辨率宽的比率，范围(0,1)，支持4位小数，如0.9999。 

        :return: The width of this MosaicInfo.
        :rtype: str
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this MosaicInfo.

        马赛克宽，值有两种形式： - 整数型代马赛克宽的像素值，范围[8，4096]，单位px。 - 小数型代表相对输出视频分辨率宽的比率，范围(0,1)，支持4位小数，如0.9999。 

        :param width: The width of this MosaicInfo.
        :type width: str
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this MosaicInfo.

        马赛克高，值有两种形式： - 整数型代表马赛克的像素值，范围[8，4096]，单位px。 - 小数型代表相对输出视频分辨率高的比率，范围(0，1)，支持4位小数，如0.9999。 

        :return: The height of this MosaicInfo.
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this MosaicInfo.

        马赛克高，值有两种形式： - 整数型代表马赛克的像素值，范围[8，4096]，单位px。 - 小数型代表相对输出视频分辨率高的比率，范围(0，1)，支持4位小数，如0.9999。 

        :param height: The height of this MosaicInfo.
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
        if not isinstance(other, MosaicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
