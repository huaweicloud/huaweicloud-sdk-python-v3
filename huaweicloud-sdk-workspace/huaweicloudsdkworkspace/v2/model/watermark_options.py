# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WatermarkOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'show_style': 'str',
        'color': 'str',
        'font_size': 'int',
        'opacity_setting': 'str',
        'content_item_count': 'int',
        'display_format': 'str',
        'lean': 'int',
        'content_customized': 'str',
        'content_color': 'str',
        'watermark_security_access': 'bool',
        'user_extend_info_switch': 'bool',
        'user_extend_info': 'str'
    }

    attribute_map = {
        'show_style': 'show_style',
        'color': 'color',
        'font_size': 'font_size',
        'opacity_setting': 'opacity_setting',
        'content_item_count': 'content_item_count',
        'display_format': 'display_format',
        'lean': 'lean',
        'content_customized': 'content_customized',
        'content_color': 'content_color',
        'watermark_security_access': 'watermark_security_access',
        'user_extend_info_switch': 'user_extend_info_switch',
        'user_extend_info': 'user_extend_info'
    }

    def __init__(self, show_style=None, color=None, font_size=None, opacity_setting=None, content_item_count=None, display_format=None, lean=None, content_customized=None, content_color=None, watermark_security_access=None, user_extend_info_switch=None, user_extend_info=None):
        r"""WatermarkOptions

        The model defined in huaweicloud sdk

        :param show_style: 展示方式。取值为：FIXED：固定位置。RANDOM：随机运动。
        :type show_style: str
        :param color: 颜色。格式：RRGGBB。默认：2a2a2a。
        :type color: str
        :param font_size: 字体大小。取值范围为[1-200]。默认：30。
        :type font_size: int
        :param opacity_setting: 不透明度（%）。取值范围为[0-100]。默认：\&quot;12.5\&quot;。
        :type opacity_setting: str
        :param content_item_count: 条目数量。取值范围为[1-30]。默认：1。
        :type content_item_count: int
        :param display_format: 水印内容显示格式。
        :type display_format: str
        :param lean: 倾斜度。取值范围为[-90-90]。默认：-45。
        :type lean: int
        :param content_customized: 自定义内容。内容不得带有类似&#39;&gt;&#39;的特殊字符。
        :type content_customized: str
        :param content_color: 内容颜色。
        :type content_color: str
        :param watermark_security_access: 安全优先开关。
        :type watermark_security_access: bool
        :param user_extend_info_switch: 用户扩展信息开关。false：表示关闭。true：表示开启。
        :type user_extend_info_switch: bool
        :param user_extend_info: 用户扩展信息。
        :type user_extend_info: str
        """
        
        

        self._show_style = None
        self._color = None
        self._font_size = None
        self._opacity_setting = None
        self._content_item_count = None
        self._display_format = None
        self._lean = None
        self._content_customized = None
        self._content_color = None
        self._watermark_security_access = None
        self._user_extend_info_switch = None
        self._user_extend_info = None
        self.discriminator = None

        if show_style is not None:
            self.show_style = show_style
        if color is not None:
            self.color = color
        if font_size is not None:
            self.font_size = font_size
        if opacity_setting is not None:
            self.opacity_setting = opacity_setting
        if content_item_count is not None:
            self.content_item_count = content_item_count
        if display_format is not None:
            self.display_format = display_format
        if lean is not None:
            self.lean = lean
        if content_customized is not None:
            self.content_customized = content_customized
        if content_color is not None:
            self.content_color = content_color
        if watermark_security_access is not None:
            self.watermark_security_access = watermark_security_access
        if user_extend_info_switch is not None:
            self.user_extend_info_switch = user_extend_info_switch
        if user_extend_info is not None:
            self.user_extend_info = user_extend_info

    @property
    def show_style(self):
        r"""Gets the show_style of this WatermarkOptions.

        展示方式。取值为：FIXED：固定位置。RANDOM：随机运动。

        :return: The show_style of this WatermarkOptions.
        :rtype: str
        """
        return self._show_style

    @show_style.setter
    def show_style(self, show_style):
        r"""Sets the show_style of this WatermarkOptions.

        展示方式。取值为：FIXED：固定位置。RANDOM：随机运动。

        :param show_style: The show_style of this WatermarkOptions.
        :type show_style: str
        """
        self._show_style = show_style

    @property
    def color(self):
        r"""Gets the color of this WatermarkOptions.

        颜色。格式：RRGGBB。默认：2a2a2a。

        :return: The color of this WatermarkOptions.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        r"""Sets the color of this WatermarkOptions.

        颜色。格式：RRGGBB。默认：2a2a2a。

        :param color: The color of this WatermarkOptions.
        :type color: str
        """
        self._color = color

    @property
    def font_size(self):
        r"""Gets the font_size of this WatermarkOptions.

        字体大小。取值范围为[1-200]。默认：30。

        :return: The font_size of this WatermarkOptions.
        :rtype: int
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        r"""Sets the font_size of this WatermarkOptions.

        字体大小。取值范围为[1-200]。默认：30。

        :param font_size: The font_size of this WatermarkOptions.
        :type font_size: int
        """
        self._font_size = font_size

    @property
    def opacity_setting(self):
        r"""Gets the opacity_setting of this WatermarkOptions.

        不透明度（%）。取值范围为[0-100]。默认：\"12.5\"。

        :return: The opacity_setting of this WatermarkOptions.
        :rtype: str
        """
        return self._opacity_setting

    @opacity_setting.setter
    def opacity_setting(self, opacity_setting):
        r"""Sets the opacity_setting of this WatermarkOptions.

        不透明度（%）。取值范围为[0-100]。默认：\"12.5\"。

        :param opacity_setting: The opacity_setting of this WatermarkOptions.
        :type opacity_setting: str
        """
        self._opacity_setting = opacity_setting

    @property
    def content_item_count(self):
        r"""Gets the content_item_count of this WatermarkOptions.

        条目数量。取值范围为[1-30]。默认：1。

        :return: The content_item_count of this WatermarkOptions.
        :rtype: int
        """
        return self._content_item_count

    @content_item_count.setter
    def content_item_count(self, content_item_count):
        r"""Sets the content_item_count of this WatermarkOptions.

        条目数量。取值范围为[1-30]。默认：1。

        :param content_item_count: The content_item_count of this WatermarkOptions.
        :type content_item_count: int
        """
        self._content_item_count = content_item_count

    @property
    def display_format(self):
        r"""Gets the display_format of this WatermarkOptions.

        水印内容显示格式。

        :return: The display_format of this WatermarkOptions.
        :rtype: str
        """
        return self._display_format

    @display_format.setter
    def display_format(self, display_format):
        r"""Sets the display_format of this WatermarkOptions.

        水印内容显示格式。

        :param display_format: The display_format of this WatermarkOptions.
        :type display_format: str
        """
        self._display_format = display_format

    @property
    def lean(self):
        r"""Gets the lean of this WatermarkOptions.

        倾斜度。取值范围为[-90-90]。默认：-45。

        :return: The lean of this WatermarkOptions.
        :rtype: int
        """
        return self._lean

    @lean.setter
    def lean(self, lean):
        r"""Sets the lean of this WatermarkOptions.

        倾斜度。取值范围为[-90-90]。默认：-45。

        :param lean: The lean of this WatermarkOptions.
        :type lean: int
        """
        self._lean = lean

    @property
    def content_customized(self):
        r"""Gets the content_customized of this WatermarkOptions.

        自定义内容。内容不得带有类似'>'的特殊字符。

        :return: The content_customized of this WatermarkOptions.
        :rtype: str
        """
        return self._content_customized

    @content_customized.setter
    def content_customized(self, content_customized):
        r"""Sets the content_customized of this WatermarkOptions.

        自定义内容。内容不得带有类似'>'的特殊字符。

        :param content_customized: The content_customized of this WatermarkOptions.
        :type content_customized: str
        """
        self._content_customized = content_customized

    @property
    def content_color(self):
        r"""Gets the content_color of this WatermarkOptions.

        内容颜色。

        :return: The content_color of this WatermarkOptions.
        :rtype: str
        """
        return self._content_color

    @content_color.setter
    def content_color(self, content_color):
        r"""Sets the content_color of this WatermarkOptions.

        内容颜色。

        :param content_color: The content_color of this WatermarkOptions.
        :type content_color: str
        """
        self._content_color = content_color

    @property
    def watermark_security_access(self):
        r"""Gets the watermark_security_access of this WatermarkOptions.

        安全优先开关。

        :return: The watermark_security_access of this WatermarkOptions.
        :rtype: bool
        """
        return self._watermark_security_access

    @watermark_security_access.setter
    def watermark_security_access(self, watermark_security_access):
        r"""Sets the watermark_security_access of this WatermarkOptions.

        安全优先开关。

        :param watermark_security_access: The watermark_security_access of this WatermarkOptions.
        :type watermark_security_access: bool
        """
        self._watermark_security_access = watermark_security_access

    @property
    def user_extend_info_switch(self):
        r"""Gets the user_extend_info_switch of this WatermarkOptions.

        用户扩展信息开关。false：表示关闭。true：表示开启。

        :return: The user_extend_info_switch of this WatermarkOptions.
        :rtype: bool
        """
        return self._user_extend_info_switch

    @user_extend_info_switch.setter
    def user_extend_info_switch(self, user_extend_info_switch):
        r"""Sets the user_extend_info_switch of this WatermarkOptions.

        用户扩展信息开关。false：表示关闭。true：表示开启。

        :param user_extend_info_switch: The user_extend_info_switch of this WatermarkOptions.
        :type user_extend_info_switch: bool
        """
        self._user_extend_info_switch = user_extend_info_switch

    @property
    def user_extend_info(self):
        r"""Gets the user_extend_info of this WatermarkOptions.

        用户扩展信息。

        :return: The user_extend_info of this WatermarkOptions.
        :rtype: str
        """
        return self._user_extend_info

    @user_extend_info.setter
    def user_extend_info(self, user_extend_info):
        r"""Sets the user_extend_info of this WatermarkOptions.

        用户扩展信息。

        :param user_extend_info: The user_extend_info of this WatermarkOptions.
        :type user_extend_info: str
        """
        self._user_extend_info = user_extend_info

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
        if not isinstance(other, WatermarkOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
