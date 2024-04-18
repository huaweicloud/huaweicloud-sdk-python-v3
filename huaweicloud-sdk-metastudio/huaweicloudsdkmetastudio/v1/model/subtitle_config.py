# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubtitleConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dx': 'int',
        'dy': 'int',
        'font_name': 'str',
        'font_size': 'int',
        'h': 'int',
        'w': 'int'
    }

    attribute_map = {
        'dx': 'dx',
        'dy': 'dy',
        'font_name': 'font_name',
        'font_size': 'font_size',
        'h': 'h',
        'w': 'w'
    }

    def __init__(self, dx=None, dy=None, font_name=None, font_size=None, h=None, w=None):
        """SubtitleConfig

        The model defined in huaweicloud sdk

        :param dx: 字幕框左下角像素点坐标。  &gt; *横屏（16:9）视频像素为1920x1080；竖屏（9:16）视频像素为1080x1920。
        :type dx: int
        :param dy: 字幕框左下角像素点坐标。  &gt; *横屏（16:9）视频像素为1920x1080；竖屏（9:16）视频像素为1080x1920。
        :type dy: int
        :param font_name: 字体。当前支持的字体： * HarmonyOS_Sans_SC_Black：鸿蒙粗体 * HarmonyOS_Sans_SC_Regular：鸿蒙常规 * HarmonyOS_Sans_SC_Thin：鸿蒙细体
        :type font_name: str
        :param font_size: 字体大小。  取值范围：[4, 120]
        :type font_size: int
        :param h: 字幕框高度 &gt; * 参数h用于方便前端计算字幕框左上角坐标，后台不使用该参数
        :type h: int
        :param w: 字幕框宽度 &gt; * 字幕框宽度固定为屏幕宽度的80% &gt; * 参数w用于方便前端计算字幕框左上角坐标，后台不使用该参数
        :type w: int
        """
        
        

        self._dx = None
        self._dy = None
        self._font_name = None
        self._font_size = None
        self._h = None
        self._w = None
        self.discriminator = None

        if dx is not None:
            self.dx = dx
        if dy is not None:
            self.dy = dy
        if font_name is not None:
            self.font_name = font_name
        if font_size is not None:
            self.font_size = font_size
        if h is not None:
            self.h = h
        if w is not None:
            self.w = w

    @property
    def dx(self):
        """Gets the dx of this SubtitleConfig.

        字幕框左下角像素点坐标。  > *横屏（16:9）视频像素为1920x1080；竖屏（9:16）视频像素为1080x1920。

        :return: The dx of this SubtitleConfig.
        :rtype: int
        """
        return self._dx

    @dx.setter
    def dx(self, dx):
        """Sets the dx of this SubtitleConfig.

        字幕框左下角像素点坐标。  > *横屏（16:9）视频像素为1920x1080；竖屏（9:16）视频像素为1080x1920。

        :param dx: The dx of this SubtitleConfig.
        :type dx: int
        """
        self._dx = dx

    @property
    def dy(self):
        """Gets the dy of this SubtitleConfig.

        字幕框左下角像素点坐标。  > *横屏（16:9）视频像素为1920x1080；竖屏（9:16）视频像素为1080x1920。

        :return: The dy of this SubtitleConfig.
        :rtype: int
        """
        return self._dy

    @dy.setter
    def dy(self, dy):
        """Sets the dy of this SubtitleConfig.

        字幕框左下角像素点坐标。  > *横屏（16:9）视频像素为1920x1080；竖屏（9:16）视频像素为1080x1920。

        :param dy: The dy of this SubtitleConfig.
        :type dy: int
        """
        self._dy = dy

    @property
    def font_name(self):
        """Gets the font_name of this SubtitleConfig.

        字体。当前支持的字体： * HarmonyOS_Sans_SC_Black：鸿蒙粗体 * HarmonyOS_Sans_SC_Regular：鸿蒙常规 * HarmonyOS_Sans_SC_Thin：鸿蒙细体

        :return: The font_name of this SubtitleConfig.
        :rtype: str
        """
        return self._font_name

    @font_name.setter
    def font_name(self, font_name):
        """Sets the font_name of this SubtitleConfig.

        字体。当前支持的字体： * HarmonyOS_Sans_SC_Black：鸿蒙粗体 * HarmonyOS_Sans_SC_Regular：鸿蒙常规 * HarmonyOS_Sans_SC_Thin：鸿蒙细体

        :param font_name: The font_name of this SubtitleConfig.
        :type font_name: str
        """
        self._font_name = font_name

    @property
    def font_size(self):
        """Gets the font_size of this SubtitleConfig.

        字体大小。  取值范围：[4, 120]

        :return: The font_size of this SubtitleConfig.
        :rtype: int
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        """Sets the font_size of this SubtitleConfig.

        字体大小。  取值范围：[4, 120]

        :param font_size: The font_size of this SubtitleConfig.
        :type font_size: int
        """
        self._font_size = font_size

    @property
    def h(self):
        """Gets the h of this SubtitleConfig.

        字幕框高度 > * 参数h用于方便前端计算字幕框左上角坐标，后台不使用该参数

        :return: The h of this SubtitleConfig.
        :rtype: int
        """
        return self._h

    @h.setter
    def h(self, h):
        """Sets the h of this SubtitleConfig.

        字幕框高度 > * 参数h用于方便前端计算字幕框左上角坐标，后台不使用该参数

        :param h: The h of this SubtitleConfig.
        :type h: int
        """
        self._h = h

    @property
    def w(self):
        """Gets the w of this SubtitleConfig.

        字幕框宽度 > * 字幕框宽度固定为屏幕宽度的80% > * 参数w用于方便前端计算字幕框左上角坐标，后台不使用该参数

        :return: The w of this SubtitleConfig.
        :rtype: int
        """
        return self._w

    @w.setter
    def w(self, w):
        """Sets the w of this SubtitleConfig.

        字幕框宽度 > * 字幕框宽度固定为屏幕宽度的80% > * 参数w用于方便前端计算字幕框左上角坐标，后台不使用该参数

        :param w: The w of this SubtitleConfig.
        :type w: int
        """
        self._w = w

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
        if not isinstance(other, SubtitleConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
