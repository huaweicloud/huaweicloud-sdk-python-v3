# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BoundingBox:

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
        'top_left_y': 'int',
        'top_left_x': 'int',
        'height': 'int'
    }

    attribute_map = {
        'width': 'width',
        'top_left_y': 'top_left_y',
        'top_left_x': 'top_left_x',
        'height': 'height'
    }

    def __init__(self, width=None, top_left_y=None, top_left_x=None, height=None):
        r"""BoundingBox

        The model defined in huaweicloud sdk

        :param width: 矩形框宽度。
        :type width: int
        :param top_left_y: 矩形框左上角纵坐标。
        :type top_left_y: int
        :param top_left_x: 矩形框左上角横坐标。
        :type top_left_x: int
        :param height: 矩形框高度。
        :type height: int
        """
        
        

        self._width = None
        self._top_left_y = None
        self._top_left_x = None
        self._height = None
        self.discriminator = None

        self.width = width
        self.top_left_y = top_left_y
        self.top_left_x = top_left_x
        self.height = height

    @property
    def width(self):
        r"""Gets the width of this BoundingBox.

        矩形框宽度。

        :return: The width of this BoundingBox.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        r"""Sets the width of this BoundingBox.

        矩形框宽度。

        :param width: The width of this BoundingBox.
        :type width: int
        """
        self._width = width

    @property
    def top_left_y(self):
        r"""Gets the top_left_y of this BoundingBox.

        矩形框左上角纵坐标。

        :return: The top_left_y of this BoundingBox.
        :rtype: int
        """
        return self._top_left_y

    @top_left_y.setter
    def top_left_y(self, top_left_y):
        r"""Sets the top_left_y of this BoundingBox.

        矩形框左上角纵坐标。

        :param top_left_y: The top_left_y of this BoundingBox.
        :type top_left_y: int
        """
        self._top_left_y = top_left_y

    @property
    def top_left_x(self):
        r"""Gets the top_left_x of this BoundingBox.

        矩形框左上角横坐标。

        :return: The top_left_x of this BoundingBox.
        :rtype: int
        """
        return self._top_left_x

    @top_left_x.setter
    def top_left_x(self, top_left_x):
        r"""Sets the top_left_x of this BoundingBox.

        矩形框左上角横坐标。

        :param top_left_x: The top_left_x of this BoundingBox.
        :type top_left_x: int
        """
        self._top_left_x = top_left_x

    @property
    def height(self):
        r"""Gets the height of this BoundingBox.

        矩形框高度。

        :return: The height of this BoundingBox.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        r"""Sets the height of this BoundingBox.

        矩形框高度。

        :param height: The height of this BoundingBox.
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
        if not isinstance(other, BoundingBox):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
