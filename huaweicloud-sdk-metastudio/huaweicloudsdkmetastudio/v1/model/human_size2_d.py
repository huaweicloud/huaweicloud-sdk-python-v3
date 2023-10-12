# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HumanSize2D:

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
        """HumanSize2D

        The model defined in huaweicloud sdk

        :param width: 分身数字人宽度像素值。 &gt; 横屏（16:9）背景图片像素为1920x1080；竖屏（9:16）背景图片像素为1080x1920。
        :type width: int
        :param height: 分身数字人高度像素值。 &gt; 横屏（16:9）背景图片像素为1920x1080；竖屏（9:16）背景图片像素为1080x1920。
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
        """Gets the width of this HumanSize2D.

        分身数字人宽度像素值。 > 横屏（16:9）背景图片像素为1920x1080；竖屏（9:16）背景图片像素为1080x1920。

        :return: The width of this HumanSize2D.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this HumanSize2D.

        分身数字人宽度像素值。 > 横屏（16:9）背景图片像素为1920x1080；竖屏（9:16）背景图片像素为1080x1920。

        :param width: The width of this HumanSize2D.
        :type width: int
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this HumanSize2D.

        分身数字人高度像素值。 > 横屏（16:9）背景图片像素为1920x1080；竖屏（9:16）背景图片像素为1080x1920。

        :return: The height of this HumanSize2D.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this HumanSize2D.

        分身数字人高度像素值。 > 横屏（16:9）背景图片像素为1920x1080；竖屏（9:16）背景图片像素为1080x1920。

        :param height: The height of this HumanSize2D.
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
        if not isinstance(other, HumanSize2D):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
