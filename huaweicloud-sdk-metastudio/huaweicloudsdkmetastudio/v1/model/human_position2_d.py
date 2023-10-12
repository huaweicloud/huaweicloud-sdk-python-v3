# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HumanPosition2D:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'position': 'str',
        'position_x': 'int',
        'position_y': 'int'
    }

    attribute_map = {
        'position': 'position',
        'position_x': 'position_x',
        'position_y': 'position_y'
    }

    def __init__(self, position=None, position_x=None, position_y=None):
        """HumanPosition2D

        The model defined in huaweicloud sdk

        :param position: 分身数字人在背景图片中的位置。 * LEFT： 左 * MIDDLE： 中 * RIGHT： 右 &gt; 当position_x和position_y参数值存在时，position不生效
        :type position: str
        :param position_x: 分身数字人X轴位置，即分身数字图片底边中心点像素的X轴的像素值。 &gt; 横屏（16:9）背景图片像素为1920x1080；竖屏（9:16）背景图片像素为1080x1920。
        :type position_x: int
        :param position_y: 分身数字Y轴位置，即分身数字图片底边中心点像素的Y轴的像素值。 &gt; 横屏（16:9）背景图片像素为1920x1080；竖屏（9:16）背景图片像素为1080x1920。
        :type position_y: int
        """
        
        

        self._position = None
        self._position_x = None
        self._position_y = None
        self.discriminator = None

        if position is not None:
            self.position = position
        if position_x is not None:
            self.position_x = position_x
        if position_y is not None:
            self.position_y = position_y

    @property
    def position(self):
        """Gets the position of this HumanPosition2D.

        分身数字人在背景图片中的位置。 * LEFT： 左 * MIDDLE： 中 * RIGHT： 右 > 当position_x和position_y参数值存在时，position不生效

        :return: The position of this HumanPosition2D.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this HumanPosition2D.

        分身数字人在背景图片中的位置。 * LEFT： 左 * MIDDLE： 中 * RIGHT： 右 > 当position_x和position_y参数值存在时，position不生效

        :param position: The position of this HumanPosition2D.
        :type position: str
        """
        self._position = position

    @property
    def position_x(self):
        """Gets the position_x of this HumanPosition2D.

        分身数字人X轴位置，即分身数字图片底边中心点像素的X轴的像素值。 > 横屏（16:9）背景图片像素为1920x1080；竖屏（9:16）背景图片像素为1080x1920。

        :return: The position_x of this HumanPosition2D.
        :rtype: int
        """
        return self._position_x

    @position_x.setter
    def position_x(self, position_x):
        """Sets the position_x of this HumanPosition2D.

        分身数字人X轴位置，即分身数字图片底边中心点像素的X轴的像素值。 > 横屏（16:9）背景图片像素为1920x1080；竖屏（9:16）背景图片像素为1080x1920。

        :param position_x: The position_x of this HumanPosition2D.
        :type position_x: int
        """
        self._position_x = position_x

    @property
    def position_y(self):
        """Gets the position_y of this HumanPosition2D.

        分身数字Y轴位置，即分身数字图片底边中心点像素的Y轴的像素值。 > 横屏（16:9）背景图片像素为1920x1080；竖屏（9:16）背景图片像素为1080x1920。

        :return: The position_y of this HumanPosition2D.
        :rtype: int
        """
        return self._position_y

    @position_y.setter
    def position_y(self, position_y):
        """Sets the position_y of this HumanPosition2D.

        分身数字Y轴位置，即分身数字图片底边中心点像素的Y轴的像素值。 > 横屏（16:9）背景图片像素为1920x1080；竖屏（9:16）背景图片像素为1080x1920。

        :param position_y: The position_y of this HumanPosition2D.
        :type position_y: int
        """
        self._position_y = position_y

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
        if not isinstance(other, HumanPosition2D):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
