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
        'h': 'int',
        'w': 'int',
        'font_name': 'str',
        'font_size': 'int',
        'font_color': 'str',
        'stroke_color': 'str',
        'stroke_thickness': 'float',
        'opacity': 'float'
    }

    attribute_map = {
        'dx': 'dx',
        'dy': 'dy',
        'h': 'h',
        'w': 'w',
        'font_name': 'font_name',
        'font_size': 'font_size',
        'font_color': 'font_color',
        'stroke_color': 'stroke_color',
        'stroke_thickness': 'stroke_thickness',
        'opacity': 'opacity'
    }

    def __init__(self, dx=None, dy=None, h=None, w=None, font_name=None, font_size=None, font_color=None, stroke_color=None, stroke_thickness=None, opacity=None):
        r"""SubtitleConfig

        The model defined in huaweicloud sdk

        :param dx: **参数解释**： 字幕框左下角像素点坐标。 **约束限制**： 不涉及。 **默认取值**： 不涉及。
        :type dx: int
        :param dy: **参数解释**： 字幕框左下角像素点坐标。 **约束限制**： 不涉及。 **默认取值**： 不涉及。
        :type dy: int
        :param h: **参数解释**： 字幕框高度。 **约束限制**： 参数h用于方便前端计算字幕框左上角坐标，后台不使用该参数。
        :type h: int
        :param w: **参数解释**： 字幕框宽度。 **约束限制**： * 字幕框宽度固定为屏幕宽度的80% * 参数w用于方便前端计算字幕框左上角坐标，后台不使用该参数
        :type w: int
        :param font_name: **参数解释**： 字体。当前支持的字体请参考[服务支持的字体](metastudio_02_0041.xml) **约束限制**： 不涉及。 **取值范围**： 字符长度0-64位
        :type font_name: str
        :param font_size: **参数解释**： 字体大小。接口的取值范围为0-120，实际业务使用的取值范围要求为24-120，请以业务实际使用要求为准。 **约束限制**： 不涉及。
        :type font_size: int
        :param font_color: **参数解释**： 字幕字体颜色的RGB颜色值。 **约束限制**： 无 **取值范围**： 字符长度0-7位，固定长度
        :type font_color: str
        :param stroke_color: **参数解释**： 字幕字体描边颜色的RGB颜色值。 **约束限制**： 无 **取值范围**： 字符长度0-7位，固定长度
        :type stroke_color: str
        :param stroke_thickness: **参数解释**： 字幕字体描边粗细像素值。 **约束限制**： 无 **取值范围**： 0-50
        :type stroke_thickness: float
        :param opacity: **参数解释**： 字幕字体不透明度，0表示完全透明，1表示完全不透明。默认1。 **约束限制**： 无 **取值范围**： 0-1
        :type opacity: float
        """
        
        

        self._dx = None
        self._dy = None
        self._h = None
        self._w = None
        self._font_name = None
        self._font_size = None
        self._font_color = None
        self._stroke_color = None
        self._stroke_thickness = None
        self._opacity = None
        self.discriminator = None

        if dx is not None:
            self.dx = dx
        if dy is not None:
            self.dy = dy
        if h is not None:
            self.h = h
        if w is not None:
            self.w = w
        if font_name is not None:
            self.font_name = font_name
        if font_size is not None:
            self.font_size = font_size
        if font_color is not None:
            self.font_color = font_color
        if stroke_color is not None:
            self.stroke_color = stroke_color
        if stroke_thickness is not None:
            self.stroke_thickness = stroke_thickness
        if opacity is not None:
            self.opacity = opacity

    @property
    def dx(self):
        r"""Gets the dx of this SubtitleConfig.

        **参数解释**： 字幕框左下角像素点坐标。 **约束限制**： 不涉及。 **默认取值**： 不涉及。

        :return: The dx of this SubtitleConfig.
        :rtype: int
        """
        return self._dx

    @dx.setter
    def dx(self, dx):
        r"""Sets the dx of this SubtitleConfig.

        **参数解释**： 字幕框左下角像素点坐标。 **约束限制**： 不涉及。 **默认取值**： 不涉及。

        :param dx: The dx of this SubtitleConfig.
        :type dx: int
        """
        self._dx = dx

    @property
    def dy(self):
        r"""Gets the dy of this SubtitleConfig.

        **参数解释**： 字幕框左下角像素点坐标。 **约束限制**： 不涉及。 **默认取值**： 不涉及。

        :return: The dy of this SubtitleConfig.
        :rtype: int
        """
        return self._dy

    @dy.setter
    def dy(self, dy):
        r"""Sets the dy of this SubtitleConfig.

        **参数解释**： 字幕框左下角像素点坐标。 **约束限制**： 不涉及。 **默认取值**： 不涉及。

        :param dy: The dy of this SubtitleConfig.
        :type dy: int
        """
        self._dy = dy

    @property
    def h(self):
        r"""Gets the h of this SubtitleConfig.

        **参数解释**： 字幕框高度。 **约束限制**： 参数h用于方便前端计算字幕框左上角坐标，后台不使用该参数。

        :return: The h of this SubtitleConfig.
        :rtype: int
        """
        return self._h

    @h.setter
    def h(self, h):
        r"""Sets the h of this SubtitleConfig.

        **参数解释**： 字幕框高度。 **约束限制**： 参数h用于方便前端计算字幕框左上角坐标，后台不使用该参数。

        :param h: The h of this SubtitleConfig.
        :type h: int
        """
        self._h = h

    @property
    def w(self):
        r"""Gets the w of this SubtitleConfig.

        **参数解释**： 字幕框宽度。 **约束限制**： * 字幕框宽度固定为屏幕宽度的80% * 参数w用于方便前端计算字幕框左上角坐标，后台不使用该参数

        :return: The w of this SubtitleConfig.
        :rtype: int
        """
        return self._w

    @w.setter
    def w(self, w):
        r"""Sets the w of this SubtitleConfig.

        **参数解释**： 字幕框宽度。 **约束限制**： * 字幕框宽度固定为屏幕宽度的80% * 参数w用于方便前端计算字幕框左上角坐标，后台不使用该参数

        :param w: The w of this SubtitleConfig.
        :type w: int
        """
        self._w = w

    @property
    def font_name(self):
        r"""Gets the font_name of this SubtitleConfig.

        **参数解释**： 字体。当前支持的字体请参考[服务支持的字体](metastudio_02_0041.xml) **约束限制**： 不涉及。 **取值范围**： 字符长度0-64位

        :return: The font_name of this SubtitleConfig.
        :rtype: str
        """
        return self._font_name

    @font_name.setter
    def font_name(self, font_name):
        r"""Sets the font_name of this SubtitleConfig.

        **参数解释**： 字体。当前支持的字体请参考[服务支持的字体](metastudio_02_0041.xml) **约束限制**： 不涉及。 **取值范围**： 字符长度0-64位

        :param font_name: The font_name of this SubtitleConfig.
        :type font_name: str
        """
        self._font_name = font_name

    @property
    def font_size(self):
        r"""Gets the font_size of this SubtitleConfig.

        **参数解释**： 字体大小。接口的取值范围为0-120，实际业务使用的取值范围要求为24-120，请以业务实际使用要求为准。 **约束限制**： 不涉及。

        :return: The font_size of this SubtitleConfig.
        :rtype: int
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        r"""Sets the font_size of this SubtitleConfig.

        **参数解释**： 字体大小。接口的取值范围为0-120，实际业务使用的取值范围要求为24-120，请以业务实际使用要求为准。 **约束限制**： 不涉及。

        :param font_size: The font_size of this SubtitleConfig.
        :type font_size: int
        """
        self._font_size = font_size

    @property
    def font_color(self):
        r"""Gets the font_color of this SubtitleConfig.

        **参数解释**： 字幕字体颜色的RGB颜色值。 **约束限制**： 无 **取值范围**： 字符长度0-7位，固定长度

        :return: The font_color of this SubtitleConfig.
        :rtype: str
        """
        return self._font_color

    @font_color.setter
    def font_color(self, font_color):
        r"""Sets the font_color of this SubtitleConfig.

        **参数解释**： 字幕字体颜色的RGB颜色值。 **约束限制**： 无 **取值范围**： 字符长度0-7位，固定长度

        :param font_color: The font_color of this SubtitleConfig.
        :type font_color: str
        """
        self._font_color = font_color

    @property
    def stroke_color(self):
        r"""Gets the stroke_color of this SubtitleConfig.

        **参数解释**： 字幕字体描边颜色的RGB颜色值。 **约束限制**： 无 **取值范围**： 字符长度0-7位，固定长度

        :return: The stroke_color of this SubtitleConfig.
        :rtype: str
        """
        return self._stroke_color

    @stroke_color.setter
    def stroke_color(self, stroke_color):
        r"""Sets the stroke_color of this SubtitleConfig.

        **参数解释**： 字幕字体描边颜色的RGB颜色值。 **约束限制**： 无 **取值范围**： 字符长度0-7位，固定长度

        :param stroke_color: The stroke_color of this SubtitleConfig.
        :type stroke_color: str
        """
        self._stroke_color = stroke_color

    @property
    def stroke_thickness(self):
        r"""Gets the stroke_thickness of this SubtitleConfig.

        **参数解释**： 字幕字体描边粗细像素值。 **约束限制**： 无 **取值范围**： 0-50

        :return: The stroke_thickness of this SubtitleConfig.
        :rtype: float
        """
        return self._stroke_thickness

    @stroke_thickness.setter
    def stroke_thickness(self, stroke_thickness):
        r"""Sets the stroke_thickness of this SubtitleConfig.

        **参数解释**： 字幕字体描边粗细像素值。 **约束限制**： 无 **取值范围**： 0-50

        :param stroke_thickness: The stroke_thickness of this SubtitleConfig.
        :type stroke_thickness: float
        """
        self._stroke_thickness = stroke_thickness

    @property
    def opacity(self):
        r"""Gets the opacity of this SubtitleConfig.

        **参数解释**： 字幕字体不透明度，0表示完全透明，1表示完全不透明。默认1。 **约束限制**： 无 **取值范围**： 0-1

        :return: The opacity of this SubtitleConfig.
        :rtype: float
        """
        return self._opacity

    @opacity.setter
    def opacity(self, opacity):
        r"""Sets the opacity of this SubtitleConfig.

        **参数解释**： 字幕字体不透明度，0表示完全透明，1表示完全不透明。默认1。 **约束限制**： 无 **取值范围**： 0-1

        :param opacity: The opacity of this SubtitleConfig.
        :type opacity: float
        """
        self._opacity = opacity

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
