# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PaneSetting:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pane_id': 'str',
        'x': 'str',
        'y': 'str',
        'width': 'str',
        'height': 'str'
    }

    attribute_map = {
        'pane_id': 'pane_id',
        'x': 'x',
        'y': 'y',
        'width': 'width',
        'height': 'height'
    }

    def __init__(self, pane_id=None, x=None, y=None, width=None, height=None):
        """PaneSetting

        The model defined in huaweicloud sdk

        :param pane_id: 原视频的id。
        :type pane_id: str
        :param x: pane_id标记的原视频起点，在合成视频中相对于左下角的水平偏移量。 目前只支持小数类型，表示相对于输出视频宽的水平偏移比率。取值范围(0,1)。
        :type x: str
        :param y: pane_id标记的原视频，在合成视频中相对于左下角的垂直偏移量。 目前只支持小数型，表示相对于输出视频高的垂直偏移比率。取值范围:(0,1)。
        :type y: str
        :param width: pane_id标记的原视频，在合成视频中占的宽。目前只支持小数型，范围(0,1)，表示占据合成视频宽的比率。 
        :type width: str
        :param height: pane_id标记的原视频，在合成视频中占的高。目前只支持小数型，范围(0,1)，表示占据合成视频高的比率。 
        :type height: str
        """
        
        

        self._pane_id = None
        self._x = None
        self._y = None
        self._width = None
        self._height = None
        self.discriminator = None

        self.pane_id = pane_id
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @property
    def pane_id(self):
        """Gets the pane_id of this PaneSetting.

        原视频的id。

        :return: The pane_id of this PaneSetting.
        :rtype: str
        """
        return self._pane_id

    @pane_id.setter
    def pane_id(self, pane_id):
        """Sets the pane_id of this PaneSetting.

        原视频的id。

        :param pane_id: The pane_id of this PaneSetting.
        :type pane_id: str
        """
        self._pane_id = pane_id

    @property
    def x(self):
        """Gets the x of this PaneSetting.

        pane_id标记的原视频起点，在合成视频中相对于左下角的水平偏移量。 目前只支持小数类型，表示相对于输出视频宽的水平偏移比率。取值范围(0,1)。

        :return: The x of this PaneSetting.
        :rtype: str
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this PaneSetting.

        pane_id标记的原视频起点，在合成视频中相对于左下角的水平偏移量。 目前只支持小数类型，表示相对于输出视频宽的水平偏移比率。取值范围(0,1)。

        :param x: The x of this PaneSetting.
        :type x: str
        """
        self._x = x

    @property
    def y(self):
        """Gets the y of this PaneSetting.

        pane_id标记的原视频，在合成视频中相对于左下角的垂直偏移量。 目前只支持小数型，表示相对于输出视频高的垂直偏移比率。取值范围:(0,1)。

        :return: The y of this PaneSetting.
        :rtype: str
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this PaneSetting.

        pane_id标记的原视频，在合成视频中相对于左下角的垂直偏移量。 目前只支持小数型，表示相对于输出视频高的垂直偏移比率。取值范围:(0,1)。

        :param y: The y of this PaneSetting.
        :type y: str
        """
        self._y = y

    @property
    def width(self):
        """Gets the width of this PaneSetting.

        pane_id标记的原视频，在合成视频中占的宽。目前只支持小数型，范围(0,1)，表示占据合成视频宽的比率。 

        :return: The width of this PaneSetting.
        :rtype: str
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this PaneSetting.

        pane_id标记的原视频，在合成视频中占的宽。目前只支持小数型，范围(0,1)，表示占据合成视频宽的比率。 

        :param width: The width of this PaneSetting.
        :type width: str
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this PaneSetting.

        pane_id标记的原视频，在合成视频中占的高。目前只支持小数型，范围(0,1)，表示占据合成视频高的比率。 

        :return: The height of this PaneSetting.
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this PaneSetting.

        pane_id标记的原视频，在合成视频中占的高。目前只支持小数型，范围(0,1)，表示占据合成视频高的比率。 

        :param height: The height of this PaneSetting.
        :type height: str
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
        if not isinstance(other, PaneSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
