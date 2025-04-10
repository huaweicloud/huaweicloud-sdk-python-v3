# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LayerSizeConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'width': 'int',
        'height': 'int'
    }

    attribute_map = {
        'width': 'width',
        'height': 'height'
    }

    def __init__(self, width=None, height=None):
        r"""LayerSizeConfig

        The model defined in huaweicloud sdk

        :param width: **参数解释**： 图层图片左上角像素点的Y轴位置值图层图片宽度像素值（相对画布大小）。 横屏（16:9）画布像素为1920x1080；竖屏（9:16）画布像素为1080x1920。  **约束限制**： 该值为相对于画布的像素值，仅表示布局位置关系，与输出画面分辨率无关。
        :type width: int
        :param height: **参数解释**： 图层图片高度像素值（相对画布大小）。 横屏（16:9）画布像素为1920x1080；竖屏（9:16）画布像素为1080x1920。  **约束限制**： 该值为相对于画布的像素值，仅表示布局位置关系，与输出画面分辨率无关。|
        :type height: int
        """
        
        

        self._width = None
        self._height = None
        self.discriminator = None

        if width is not None:
            self.width = width
        if height is not None:
            self.height = height

    @property
    def width(self):
        r"""Gets the width of this LayerSizeConfig.

        **参数解释**： 图层图片左上角像素点的Y轴位置值图层图片宽度像素值（相对画布大小）。 横屏（16:9）画布像素为1920x1080；竖屏（9:16）画布像素为1080x1920。  **约束限制**： 该值为相对于画布的像素值，仅表示布局位置关系，与输出画面分辨率无关。

        :return: The width of this LayerSizeConfig.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        r"""Sets the width of this LayerSizeConfig.

        **参数解释**： 图层图片左上角像素点的Y轴位置值图层图片宽度像素值（相对画布大小）。 横屏（16:9）画布像素为1920x1080；竖屏（9:16）画布像素为1080x1920。  **约束限制**： 该值为相对于画布的像素值，仅表示布局位置关系，与输出画面分辨率无关。

        :param width: The width of this LayerSizeConfig.
        :type width: int
        """
        self._width = width

    @property
    def height(self):
        r"""Gets the height of this LayerSizeConfig.

        **参数解释**： 图层图片高度像素值（相对画布大小）。 横屏（16:9）画布像素为1920x1080；竖屏（9:16）画布像素为1080x1920。  **约束限制**： 该值为相对于画布的像素值，仅表示布局位置关系，与输出画面分辨率无关。|

        :return: The height of this LayerSizeConfig.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        r"""Sets the height of this LayerSizeConfig.

        **参数解释**： 图层图片高度像素值（相对画布大小）。 横屏（16:9）画布像素为1920x1080；竖屏（9:16）画布像素为1080x1920。  **约束限制**： 该值为相对于画布的像素值，仅表示布局位置关系，与输出画面分辨率无关。|

        :param height: The height of this LayerSizeConfig.
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
        if not isinstance(other, LayerSizeConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
