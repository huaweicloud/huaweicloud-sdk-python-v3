# coding: utf-8

import pprint
import re

import six





class EffectInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'stop_time': 'str',
        'dx': 'str',
        'dy': 'str',
        'width': 'str',
        'height': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'stop_time': 'stop_time',
        'dx': 'dx',
        'dy': 'dy',
        'width': 'width',
        'height': 'height'
    }

    def __init__(self, start_time=None, stop_time=None, dx=None, dy=None, width=None, height=None):
        """EffectInfo - a model defined in huaweicloud sdk"""
        
        

        self._start_time = None
        self._stop_time = None
        self._dx = None
        self._dy = None
        self._width = None
        self._height = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if stop_time is not None:
            self.stop_time = stop_time
        if dx is not None:
            self.dx = dx
        if dy is not None:
            self.dy = dy
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height

    @property
    def start_time(self):
        """Gets the start_time of this EffectInfo.

        特效处理开始时间点，单位：秒，精确到小数点后4位 

        :return: The start_time of this EffectInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this EffectInfo.

        特效处理开始时间点，单位：秒，精确到小数点后4位 

        :param start_time: The start_time of this EffectInfo.
        :type: str
        """
        self._start_time = start_time

    @property
    def stop_time(self):
        """Gets the stop_time of this EffectInfo.

        特效处理结束时间点，单位：秒，精确到小数点后4位 

        :return: The stop_time of this EffectInfo.
        :rtype: str
        """
        return self._stop_time

    @stop_time.setter
    def stop_time(self, stop_time):
        """Sets the stop_time of this EffectInfo.

        特效处理结束时间点，单位：秒，精确到小数点后4位 

        :param stop_time: The stop_time of this EffectInfo.
        :type: str
        """
        self._stop_time = stop_time

    @property
    def dx(self):
        """Gets the dx of this EffectInfo.

        相对视频源左上角顶点的水平偏移位置坐标。整数型表示像素值，范围[0,4096]，单位px 

        :return: The dx of this EffectInfo.
        :rtype: str
        """
        return self._dx

    @dx.setter
    def dx(self, dx):
        """Sets the dx of this EffectInfo.

        相对视频源左上角顶点的水平偏移位置坐标。整数型表示像素值，范围[0,4096]，单位px 

        :param dx: The dx of this EffectInfo.
        :type: str
        """
        self._dx = dx

    @property
    def dy(self):
        """Gets the dy of this EffectInfo.

        相对视频源左上角顶点的垂直偏移位置坐标。整数型表示像素值，范围[0,4096]，单位px 

        :return: The dy of this EffectInfo.
        :rtype: str
        """
        return self._dy

    @dy.setter
    def dy(self, dy):
        """Sets the dy of this EffectInfo.

        相对视频源左上角顶点的垂直偏移位置坐标。整数型表示像素值，范围[0,4096]，单位px 

        :param dy: The dy of this EffectInfo.
        :type: str
        """
        self._dy = dy

    @property
    def width(self):
        """Gets the width of this EffectInfo.

        特效区域的宽。整数型表示像素值，范围(0,4096]，单位px 

        :return: The width of this EffectInfo.
        :rtype: str
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this EffectInfo.

        特效区域的宽。整数型表示像素值，范围(0,4096]，单位px 

        :param width: The width of this EffectInfo.
        :type: str
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this EffectInfo.

        特效区域的高。整数型表示像素值，范围(0,4096]，单位px 

        :return: The height of this EffectInfo.
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this EffectInfo.

        特效区域的高。整数型表示像素值，范围(0,4096]，单位px 

        :param height: The height of this EffectInfo.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EffectInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
