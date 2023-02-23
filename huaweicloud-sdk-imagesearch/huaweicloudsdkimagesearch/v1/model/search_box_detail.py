# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchBoxDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x': 'int',
        'y': 'int',
        'width': 'int',
        'height': 'int'
    }

    attribute_map = {
        'x': 'x',
        'y': 'y',
        'width': 'width',
        'height': 'height'
    }

    def __init__(self, x=None, y=None, width=None, height=None):
        """SearchBoxDetail

        The model defined in huaweicloud sdk

        :param x: 区域中x坐标的最小值，单位：像素。
        :type x: int
        :param y: 区域中y坐标的最小值，单位：像素。
        :type y: int
        :param width: 区域的宽度，单位：像素。
        :type width: int
        :param height: 区域的高度，单位：像素。
        :type height: int
        """
        
        

        self._x = None
        self._y = None
        self._width = None
        self._height = None
        self.discriminator = None

        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height

    @property
    def x(self):
        """Gets the x of this SearchBoxDetail.

        区域中x坐标的最小值，单位：像素。

        :return: The x of this SearchBoxDetail.
        :rtype: int
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this SearchBoxDetail.

        区域中x坐标的最小值，单位：像素。

        :param x: The x of this SearchBoxDetail.
        :type x: int
        """
        self._x = x

    @property
    def y(self):
        """Gets the y of this SearchBoxDetail.

        区域中y坐标的最小值，单位：像素。

        :return: The y of this SearchBoxDetail.
        :rtype: int
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this SearchBoxDetail.

        区域中y坐标的最小值，单位：像素。

        :param y: The y of this SearchBoxDetail.
        :type y: int
        """
        self._y = y

    @property
    def width(self):
        """Gets the width of this SearchBoxDetail.

        区域的宽度，单位：像素。

        :return: The width of this SearchBoxDetail.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this SearchBoxDetail.

        区域的宽度，单位：像素。

        :param width: The width of this SearchBoxDetail.
        :type width: int
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this SearchBoxDetail.

        区域的高度，单位：像素。

        :return: The height of this SearchBoxDetail.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this SearchBoxDetail.

        区域的高度，单位：像素。

        :param height: The height of this SearchBoxDetail.
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
        if not isinstance(other, SearchBoxDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
