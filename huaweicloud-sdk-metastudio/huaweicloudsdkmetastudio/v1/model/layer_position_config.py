# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LayerPositionConfig:

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
        'layer_index': 'int'
    }

    attribute_map = {
        'dx': 'dx',
        'dy': 'dy',
        'layer_index': 'layer_index'
    }

    def __init__(self, dx=None, dy=None, layer_index=None):
        """LayerPositionConfig

        The model defined in huaweicloud sdk

        :param dx: 图层图片左上角像素点的X轴位置值（相对背景图片）。 &gt; 横屏（16:9）背景图片像素为1920x1080；竖屏（9:16）背景图片像素为1080x1920。
        :type dx: int
        :param dy: 图层图片左上角像素点的Y轴位置值（相对背景图片）。 &gt; 横屏（16:9）背景图片像素为1920x1080；竖屏（9:16）背景图片像素为1080x1920。
        :type dy: int
        :param layer_index: 图片/视频/人物图的层顺序。 &gt; * 图层顺序从1开始的整数，底层图层顺序是1，往上依次增加。
        :type layer_index: int
        """
        
        

        self._dx = None
        self._dy = None
        self._layer_index = None
        self.discriminator = None

        self.dx = dx
        self.dy = dy
        self.layer_index = layer_index

    @property
    def dx(self):
        """Gets the dx of this LayerPositionConfig.

        图层图片左上角像素点的X轴位置值（相对背景图片）。 > 横屏（16:9）背景图片像素为1920x1080；竖屏（9:16）背景图片像素为1080x1920。

        :return: The dx of this LayerPositionConfig.
        :rtype: int
        """
        return self._dx

    @dx.setter
    def dx(self, dx):
        """Sets the dx of this LayerPositionConfig.

        图层图片左上角像素点的X轴位置值（相对背景图片）。 > 横屏（16:9）背景图片像素为1920x1080；竖屏（9:16）背景图片像素为1080x1920。

        :param dx: The dx of this LayerPositionConfig.
        :type dx: int
        """
        self._dx = dx

    @property
    def dy(self):
        """Gets the dy of this LayerPositionConfig.

        图层图片左上角像素点的Y轴位置值（相对背景图片）。 > 横屏（16:9）背景图片像素为1920x1080；竖屏（9:16）背景图片像素为1080x1920。

        :return: The dy of this LayerPositionConfig.
        :rtype: int
        """
        return self._dy

    @dy.setter
    def dy(self, dy):
        """Sets the dy of this LayerPositionConfig.

        图层图片左上角像素点的Y轴位置值（相对背景图片）。 > 横屏（16:9）背景图片像素为1920x1080；竖屏（9:16）背景图片像素为1080x1920。

        :param dy: The dy of this LayerPositionConfig.
        :type dy: int
        """
        self._dy = dy

    @property
    def layer_index(self):
        """Gets the layer_index of this LayerPositionConfig.

        图片/视频/人物图的层顺序。 > * 图层顺序从1开始的整数，底层图层顺序是1，往上依次增加。

        :return: The layer_index of this LayerPositionConfig.
        :rtype: int
        """
        return self._layer_index

    @layer_index.setter
    def layer_index(self, layer_index):
        """Sets the layer_index of this LayerPositionConfig.

        图片/视频/人物图的层顺序。 > * 图层顺序从1开始的整数，底层图层顺序是1，往上依次增加。

        :param layer_index: The layer_index of this LayerPositionConfig.
        :type layer_index: int
        """
        self._layer_index = layer_index

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
        if not isinstance(other, LayerPositionConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
