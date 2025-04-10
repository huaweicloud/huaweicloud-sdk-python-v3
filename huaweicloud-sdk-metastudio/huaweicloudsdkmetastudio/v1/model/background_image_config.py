# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackgroundImageConfig:

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
        'width': 'int',
        'height': 'int'
    }

    attribute_map = {
        'dx': 'dx',
        'dy': 'dy',
        'width': 'width',
        'height': 'height'
    }

    def __init__(self, dx=None, dy=None, width=None, height=None):
        r"""BackgroundImageConfig

        The model defined in huaweicloud sdk

        :param dx: **参数解释**： 背景图片左上角像素点的X轴位置值（画布左上角坐标是0x0）。 横屏（16:9）画布像素为1920x1080；竖屏（9:16）画布像素为1080x1920。  **约束限制**： 需要保证背景图片要铺满画布。即dx &lt;&#x3D; 0，并且横屏时dx + width &gt;&#x3D;1920，竖屏时dx + width &gt;&#x3D;1080。
        :type dx: int
        :param dy: **参数解释**： 背景图片左上角像素点的Y轴位置值（画布左上角坐标是0x0）。 横屏（16:9）画布像素为1920x1080；竖屏（9:16）画布像素为1080x1920。  **约束限制**：  需要保证背景图片要铺满画布。即dy &lt;&#x3D; 0，并且横屏时dy + height &gt;&#x3D;1080，竖屏时dy + height &gt;&#x3D;1920。
        :type dy: int
        :param width: **参数解释**： 背景图片宽度像素值（相对画布大小）。 横屏（16:9）画布像素为1920x1080；竖屏（9:16）画布像素为1080x1920。  **约束限制**： 需要保证背景图片要铺满画布。即width &gt; 1080，并且横屏时dx + width &gt;&#x3D;1920，竖屏时dx + width &gt;&#x3D;1080。
        :type width: int
        :param height: **参数解释**： 背景图片高度像素值（相对画布大小）。 横屏（16:9）画布像素为1920x1080；竖屏（9:16）画布像素为1080x1920。  **约束限制**： 需要保证背景图片要铺满画布。height&gt; 1080，并且横屏时dy + height &gt;&#x3D;1080，竖屏时dy + height &gt;&#x3D;1920。
        :type height: int
        """
        
        

        self._dx = None
        self._dy = None
        self._width = None
        self._height = None
        self.discriminator = None

        self.dx = dx
        self.dy = dy
        self.width = width
        self.height = height

    @property
    def dx(self):
        r"""Gets the dx of this BackgroundImageConfig.

        **参数解释**： 背景图片左上角像素点的X轴位置值（画布左上角坐标是0x0）。 横屏（16:9）画布像素为1920x1080；竖屏（9:16）画布像素为1080x1920。  **约束限制**： 需要保证背景图片要铺满画布。即dx <= 0，并且横屏时dx + width >=1920，竖屏时dx + width >=1080。

        :return: The dx of this BackgroundImageConfig.
        :rtype: int
        """
        return self._dx

    @dx.setter
    def dx(self, dx):
        r"""Sets the dx of this BackgroundImageConfig.

        **参数解释**： 背景图片左上角像素点的X轴位置值（画布左上角坐标是0x0）。 横屏（16:9）画布像素为1920x1080；竖屏（9:16）画布像素为1080x1920。  **约束限制**： 需要保证背景图片要铺满画布。即dx <= 0，并且横屏时dx + width >=1920，竖屏时dx + width >=1080。

        :param dx: The dx of this BackgroundImageConfig.
        :type dx: int
        """
        self._dx = dx

    @property
    def dy(self):
        r"""Gets the dy of this BackgroundImageConfig.

        **参数解释**： 背景图片左上角像素点的Y轴位置值（画布左上角坐标是0x0）。 横屏（16:9）画布像素为1920x1080；竖屏（9:16）画布像素为1080x1920。  **约束限制**：  需要保证背景图片要铺满画布。即dy <= 0，并且横屏时dy + height >=1080，竖屏时dy + height >=1920。

        :return: The dy of this BackgroundImageConfig.
        :rtype: int
        """
        return self._dy

    @dy.setter
    def dy(self, dy):
        r"""Sets the dy of this BackgroundImageConfig.

        **参数解释**： 背景图片左上角像素点的Y轴位置值（画布左上角坐标是0x0）。 横屏（16:9）画布像素为1920x1080；竖屏（9:16）画布像素为1080x1920。  **约束限制**：  需要保证背景图片要铺满画布。即dy <= 0，并且横屏时dy + height >=1080，竖屏时dy + height >=1920。

        :param dy: The dy of this BackgroundImageConfig.
        :type dy: int
        """
        self._dy = dy

    @property
    def width(self):
        r"""Gets the width of this BackgroundImageConfig.

        **参数解释**： 背景图片宽度像素值（相对画布大小）。 横屏（16:9）画布像素为1920x1080；竖屏（9:16）画布像素为1080x1920。  **约束限制**： 需要保证背景图片要铺满画布。即width > 1080，并且横屏时dx + width >=1920，竖屏时dx + width >=1080。

        :return: The width of this BackgroundImageConfig.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        r"""Sets the width of this BackgroundImageConfig.

        **参数解释**： 背景图片宽度像素值（相对画布大小）。 横屏（16:9）画布像素为1920x1080；竖屏（9:16）画布像素为1080x1920。  **约束限制**： 需要保证背景图片要铺满画布。即width > 1080，并且横屏时dx + width >=1920，竖屏时dx + width >=1080。

        :param width: The width of this BackgroundImageConfig.
        :type width: int
        """
        self._width = width

    @property
    def height(self):
        r"""Gets the height of this BackgroundImageConfig.

        **参数解释**： 背景图片高度像素值（相对画布大小）。 横屏（16:9）画布像素为1920x1080；竖屏（9:16）画布像素为1080x1920。  **约束限制**： 需要保证背景图片要铺满画布。height> 1080，并且横屏时dy + height >=1080，竖屏时dy + height >=1920。

        :return: The height of this BackgroundImageConfig.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        r"""Sets the height of this BackgroundImageConfig.

        **参数解释**： 背景图片高度像素值（相对画布大小）。 横屏（16:9）画布像素为1920x1080；竖屏（9:16）画布像素为1080x1920。  **约束限制**： 需要保证背景图片要铺满画布。height> 1080，并且横屏时dy + height >=1080，竖屏时dy + height >=1920。

        :param height: The height of this BackgroundImageConfig.
        :type height: int
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
        if not isinstance(other, BackgroundImageConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
