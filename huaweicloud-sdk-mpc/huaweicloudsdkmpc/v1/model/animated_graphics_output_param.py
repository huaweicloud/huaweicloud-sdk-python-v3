# coding: utf-8

import pprint
import re

import six





class AnimatedGraphicsOutputParam:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'format': 'str',
        'width': 'int',
        'height': 'int',
        'start': 'int',
        'end': 'int',
        'frame_rate': 'int'
    }

    attribute_map = {
        'format': 'format',
        'width': 'width',
        'height': 'height',
        'start': 'start',
        'end': 'end',
        'frame_rate': 'frame_rate'
    }

    def __init__(self, format=None, width=None, height=None, start=None, end=None, frame_rate=15):
        """AnimatedGraphicsOutputParam - a model defined in huaweicloud sdk"""
        
        

        self._format = None
        self._width = None
        self._height = None
        self._start = None
        self._end = None
        self._frame_rate = None
        self.discriminator = None

        if format is not None:
            self.format = format
        self.width = width
        self.height = height
        self.start = start
        self.end = end
        if frame_rate is not None:
            self.frame_rate = frame_rate

    @property
    def format(self):
        """Gets the format of this AnimatedGraphicsOutputParam.

        动图格式，目前仅支持取值 gif 

        :return: The format of this AnimatedGraphicsOutputParam.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this AnimatedGraphicsOutputParam.

        动图格式，目前仅支持取值 gif 

        :param format: The format of this AnimatedGraphicsOutputParam.
        :type: str
        """
        self._format = format

    @property
    def width(self):
        """Gets the width of this AnimatedGraphicsOutputParam.

        输出动图的宽。  取值范围：0，-1或[32,3840]之间2的倍数。  >- 若设置为-1， 则宽根据高来自适应，此时“height”不能取-1或0。 >- 若设置为0，则取原始视频的宽，此时“height”只能取0。 

        :return: The width of this AnimatedGraphicsOutputParam.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this AnimatedGraphicsOutputParam.

        输出动图的宽。  取值范围：0，-1或[32,3840]之间2的倍数。  >- 若设置为-1， 则宽根据高来自适应，此时“height”不能取-1或0。 >- 若设置为0，则取原始视频的宽，此时“height”只能取0。 

        :param width: The width of this AnimatedGraphicsOutputParam.
        :type: int
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this AnimatedGraphicsOutputParam.

        输出动图的高。  取值范围：0，-1或[32,2160]之间2的倍数。  >- 若设置为-1， 则高根据宽来自适应，此时“width”不能取-1或0。 >- 若设置为0，则取原始视频的高，此时“width”只能取0。 

        :return: The height of this AnimatedGraphicsOutputParam.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this AnimatedGraphicsOutputParam.

        输出动图的高。  取值范围：0，-1或[32,2160]之间2的倍数。  >- 若设置为-1， 则高根据宽来自适应，此时“width”不能取-1或0。 >- 若设置为0，则取原始视频的高，此时“width”只能取0。 

        :param height: The height of this AnimatedGraphicsOutputParam.
        :type: int
        """
        self._height = height

    @property
    def start(self):
        """Gets the start of this AnimatedGraphicsOutputParam.

        起始时间，单位：毫秒 

        :return: The start of this AnimatedGraphicsOutputParam.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this AnimatedGraphicsOutputParam.

        起始时间，单位：毫秒 

        :param start: The start of this AnimatedGraphicsOutputParam.
        :type: int
        """
        self._start = start

    @property
    def end(self):
        """Gets the end of this AnimatedGraphicsOutputParam.

        结束时间。  单位：毫秒。  end、start差值最多60秒。 

        :return: The end of this AnimatedGraphicsOutputParam.
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this AnimatedGraphicsOutputParam.

        结束时间。  单位：毫秒。  end、start差值最多60秒。 

        :param end: The end of this AnimatedGraphicsOutputParam.
        :type: int
        """
        self._end = end

    @property
    def frame_rate(self):
        """Gets the frame_rate of this AnimatedGraphicsOutputParam.

        动图帧率。  取值范围：[1,75] 

        :return: The frame_rate of this AnimatedGraphicsOutputParam.
        :rtype: int
        """
        return self._frame_rate

    @frame_rate.setter
    def frame_rate(self, frame_rate):
        """Sets the frame_rate of this AnimatedGraphicsOutputParam.

        动图帧率。  取值范围：[1,75] 

        :param frame_rate: The frame_rate of this AnimatedGraphicsOutputParam.
        :type: int
        """
        self._frame_rate = frame_rate

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
        if not isinstance(other, AnimatedGraphicsOutputParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
