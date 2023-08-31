# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BaseWidgetInfoLocation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'top': 'int',
        'left': 'int',
        'width': 'int',
        'height': 'int'
    }

    attribute_map = {
        'top': 'top',
        'left': 'left',
        'width': 'width',
        'height': 'height'
    }

    def __init__(self, top=None, left=None, width=None, height=None):
        """BaseWidgetInfoLocation

        The model defined in huaweicloud sdk

        :param top: 监控视图的上坐标
        :type top: int
        :param left: 监控视图的左坐标
        :type left: int
        :param width: 监控视图图表宽度
        :type width: int
        :param height: 监控视图图表高度
        :type height: int
        """
        
        

        self._top = None
        self._left = None
        self._width = None
        self._height = None
        self.discriminator = None

        if top is not None:
            self.top = top
        if left is not None:
            self.left = left
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height

    @property
    def top(self):
        """Gets the top of this BaseWidgetInfoLocation.

        监控视图的上坐标

        :return: The top of this BaseWidgetInfoLocation.
        :rtype: int
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this BaseWidgetInfoLocation.

        监控视图的上坐标

        :param top: The top of this BaseWidgetInfoLocation.
        :type top: int
        """
        self._top = top

    @property
    def left(self):
        """Gets the left of this BaseWidgetInfoLocation.

        监控视图的左坐标

        :return: The left of this BaseWidgetInfoLocation.
        :rtype: int
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this BaseWidgetInfoLocation.

        监控视图的左坐标

        :param left: The left of this BaseWidgetInfoLocation.
        :type left: int
        """
        self._left = left

    @property
    def width(self):
        """Gets the width of this BaseWidgetInfoLocation.

        监控视图图表宽度

        :return: The width of this BaseWidgetInfoLocation.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this BaseWidgetInfoLocation.

        监控视图图表宽度

        :param width: The width of this BaseWidgetInfoLocation.
        :type width: int
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this BaseWidgetInfoLocation.

        监控视图图表高度

        :return: The height of this BaseWidgetInfoLocation.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this BaseWidgetInfoLocation.

        监控视图图表高度

        :param height: The height of this BaseWidgetInfoLocation.
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
        if not isinstance(other, BaseWidgetInfoLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
