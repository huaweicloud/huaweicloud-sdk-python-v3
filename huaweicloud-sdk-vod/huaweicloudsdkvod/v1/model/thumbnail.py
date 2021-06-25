# coding: utf-8

import pprint
import re

import six





class Thumbnail:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'percent': 'int',
        'time': 'int',
        'dots': 'list[int]',
        'cover_position': 'int',
        'format': 'int',
        'aspect_ratio': 'int',
        'max_length': 'int'
    }

    attribute_map = {
        'type': 'type',
        'percent': 'percent',
        'time': 'time',
        'dots': 'dots',
        'cover_position': 'cover_position',
        'format': 'format',
        'aspect_ratio': 'aspect_ratio',
        'max_length': 'max_length'
    }

    def __init__(self, type=None, percent=None, time=None, dots=None, cover_position=None, format=None, aspect_ratio=None, max_length=None):
        """Thumbnail - a model defined in huaweicloud sdk"""
        
        

        self._type = None
        self._percent = None
        self._time = None
        self._dots = None
        self._cover_position = None
        self._format = None
        self._aspect_ratio = None
        self._max_length = None
        self.discriminator = None

        self.type = type
        if percent is not None:
            self.percent = percent
        if time is not None:
            self.time = time
        if dots is not None:
            self.dots = dots
        if cover_position is not None:
            self.cover_position = cover_position
        if format is not None:
            self.format = format
        if aspect_ratio is not None:
            self.aspect_ratio = aspect_ratio
        if max_length is not None:
            self.max_length = max_length

    @property
    def type(self):
        """Gets the type of this Thumbnail.

        采样类型。支持三种采样方式（当前只支持“time”）： “percent”：根据视频时长的百分比间隔采样 “time”：根据时间间隔采样 “dots” : 指定时间点截图 

        :return: The type of this Thumbnail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Thumbnail.

        采样类型。支持三种采样方式（当前只支持“time”）： “percent”：根据视频时长的百分比间隔采样 “time”：根据时间间隔采样 “dots” : 指定时间点截图 

        :param type: The type of this Thumbnail.
        :type: str
        """
        self._type = type

    @property
    def percent(self):
        """Gets the percent of this Thumbnail.

        根据视频时长百分比间隔采样时的百分比值

        :return: The percent of this Thumbnail.
        :rtype: int
        """
        return self._percent

    @percent.setter
    def percent(self, percent):
        """Sets the percent of this Thumbnail.

        根据视频时长百分比间隔采样时的百分比值

        :param percent: The percent of this Thumbnail.
        :type: int
        """
        self._percent = percent

    @property
    def time(self):
        """Gets the time of this Thumbnail.

        根据时间间隔采样时的时间间隔值

        :return: The time of this Thumbnail.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this Thumbnail.

        根据时间间隔采样时的时间间隔值

        :param time: The time of this Thumbnail.
        :type: int
        """
        self._time = time

    @property
    def dots(self):
        """Gets the dots of this Thumbnail.

        指定时间截图时的时间点数组

        :return: The dots of this Thumbnail.
        :rtype: list[int]
        """
        return self._dots

    @dots.setter
    def dots(self, dots):
        """Sets the dots of this Thumbnail.

        指定时间截图时的时间点数组

        :param dots: The dots of this Thumbnail.
        :type: list[int]
        """
        self._dots = dots

    @property
    def cover_position(self):
        """Gets the cover_position of this Thumbnail.

        该值表示指定第几张截图作为封面(从1开始)

        :return: The cover_position of this Thumbnail.
        :rtype: int
        """
        return self._cover_position

    @cover_position.setter
    def cover_position(self, cover_position):
        """Sets the cover_position of this Thumbnail.

        该值表示指定第几张截图作为封面(从1开始)

        :param cover_position: The cover_position of this Thumbnail.
        :type: int
        """
        self._cover_position = cover_position

    @property
    def format(self):
        """Gets the format of this Thumbnail.

        截图文件格式，枚举值（jpg，png，webP）。当前只支持jpg。1 : jpg。

        :return: The format of this Thumbnail.
        :rtype: int
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this Thumbnail.

        截图文件格式，枚举值（jpg，png，webP）。当前只支持jpg。1 : jpg。

        :param format: The format of this Thumbnail.
        :type: int
        """
        self._format = format

    @property
    def aspect_ratio(self):
        """Gets the aspect_ratio of this Thumbnail.

        纵横比（保留,图像缩放方式）。0：自适应（保持原有宽高比）。1：16:9

        :return: The aspect_ratio of this Thumbnail.
        :rtype: int
        """
        return self._aspect_ratio

    @aspect_ratio.setter
    def aspect_ratio(self, aspect_ratio):
        """Sets the aspect_ratio of this Thumbnail.

        纵横比（保留,图像缩放方式）。0：自适应（保持原有宽高比）。1：16:9

        :param aspect_ratio: The aspect_ratio of this Thumbnail.
        :type: int
        """
        self._aspect_ratio = aspect_ratio

    @property
    def max_length(self):
        """Gets the max_length of this Thumbnail.

        截图最长边的尺寸（单位：像素）（宽边尺寸按照该尺寸与原始视频像素等比缩放计算） 

        :return: The max_length of this Thumbnail.
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this Thumbnail.

        截图最长边的尺寸（单位：像素）（宽边尺寸按照该尺寸与原始视频像素等比缩放计算） 

        :param max_length: The max_length of this Thumbnail.
        :type: int
        """
        self._max_length = max_length

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
        if not isinstance(other, Thumbnail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other