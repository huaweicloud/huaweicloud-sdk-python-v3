# coding: utf-8

import pprint
import re

import six





class ThumbnailPara:


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
        'start_time': 'int',
        'duration': 'int',
        'dots': 'list[int]',
        'output_filename': 'str',
        'format': 'int',
        'aspect_ratio': 'int',
        'width': 'int',
        'height': 'int',
        'max_length': 'int'
    }

    attribute_map = {
        'type': 'type',
        'percent': 'percent',
        'time': 'time',
        'start_time': 'start_time',
        'duration': 'duration',
        'dots': 'dots',
        'output_filename': 'output_filename',
        'format': 'format',
        'aspect_ratio': 'aspect_ratio',
        'width': 'width',
        'height': 'height',
        'max_length': 'max_length'
    }

    def __init__(self, type='TIME', percent=None, time=12, start_time=0, duration=None, dots=None, output_filename=None, format=1, aspect_ratio=0, width=None, height=None, max_length=480):
        """ThumbnailPara - a model defined in huaweicloud sdk"""
        
        

        self._type = None
        self._percent = None
        self._time = None
        self._start_time = None
        self._duration = None
        self._dots = None
        self._output_filename = None
        self._format = None
        self._aspect_ratio = None
        self._width = None
        self._height = None
        self._max_length = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if percent is not None:
            self.percent = percent
        if time is not None:
            self.time = time
        if start_time is not None:
            self.start_time = start_time
        if duration is not None:
            self.duration = duration
        if dots is not None:
            self.dots = dots
        if output_filename is not None:
            self.output_filename = output_filename
        if format is not None:
            self.format = format
        if aspect_ratio is not None:
            self.aspect_ratio = aspect_ratio
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if max_length is not None:
            self.max_length = max_length

    @property
    def type(self):
        """Gets the type of this ThumbnailPara.

        采样类型。  取值如下： - \"PERCENT\"：根据视频时长的百分比间隔采样。 - \"TIME\"：根据时间间隔采样截图。 - \"DOTS\"：指定时间点截图。 默认值：\"TIME\" 

        :return: The type of this ThumbnailPara.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ThumbnailPara.

        采样类型。  取值如下： - \"PERCENT\"：根据视频时长的百分比间隔采样。 - \"TIME\"：根据时间间隔采样截图。 - \"DOTS\"：指定时间点截图。 默认值：\"TIME\" 

        :param type: The type of this ThumbnailPara.
        :type: str
        """
        self._type = type

    @property
    def percent(self):
        """Gets the percent of this ThumbnailPara.

        根据视频时长百分比间隔采样时的百分比值。 

        :return: The percent of this ThumbnailPara.
        :rtype: int
        """
        return self._percent

    @percent.setter
    def percent(self, percent):
        """Sets the percent of this ThumbnailPara.

        根据视频时长百分比间隔采样时的百分比值。 

        :param percent: The percent of this ThumbnailPara.
        :type: int
        """
        self._percent = percent

    @property
    def time(self):
        """Gets the time of this ThumbnailPara.

        采样截图的时间间隔值。  默认值：12。  单位：秒 

        :return: The time of this ThumbnailPara.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ThumbnailPara.

        采样截图的时间间隔值。  默认值：12。  单位：秒 

        :param time: The time of this ThumbnailPara.
        :type: int
        """
        self._time = time

    @property
    def start_time(self):
        """Gets the start_time of this ThumbnailPara.

        采样类型为“TIME”模式的开始时间，和“time”配合使用。  默认值：0。  单位：秒。 

        :return: The start_time of this ThumbnailPara.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ThumbnailPara.

        采样类型为“TIME”模式的开始时间，和“time”配合使用。  默认值：0。  单位：秒。 

        :param start_time: The start_time of this ThumbnailPara.
        :type: int
        """
        self._start_time = start_time

    @property
    def duration(self):
        """Gets the duration of this ThumbnailPara.

        采样类型为“TIME”模式的持续时间，和“time”、“start_time”配合使用，表示从视频文件的第“start_time”开始，持续时间为“duration”，每间隔“time”生成一张截图。 取值范围：[数字，ToEND]。“ToEND”表示持续到视频结束。  默认值： ToEND。  单位：秒。 > “duration”必须大于等0，若设置为0，则截图持续时间从“start_time”到视频结束。 

        :return: The duration of this ThumbnailPara.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ThumbnailPara.

        采样类型为“TIME”模式的持续时间，和“time”、“start_time”配合使用，表示从视频文件的第“start_time”开始，持续时间为“duration”，每间隔“time”生成一张截图。 取值范围：[数字，ToEND]。“ToEND”表示持续到视频结束。  默认值： ToEND。  单位：秒。 > “duration”必须大于等0，若设置为0，则截图持续时间从“start_time”到视频结束。 

        :param duration: The duration of this ThumbnailPara.
        :type: int
        """
        self._duration = duration

    @property
    def dots(self):
        """Gets the dots of this ThumbnailPara.

        指定时间截图时的时间点数组，最多支持10个。 

        :return: The dots of this ThumbnailPara.
        :rtype: list[int]
        """
        return self._dots

    @dots.setter
    def dots(self, dots):
        """Sets the dots of this ThumbnailPara.

        指定时间截图时的时间点数组，最多支持10个。 

        :param dots: The dots of this ThumbnailPara.
        :type: list[int]
        """
        self._dots = dots

    @property
    def output_filename(self):
        """Gets the output_filename of this ThumbnailPara.

        截图输出文件名。  - 如果只抽一张图（即：按DOTS方式，指定1个时间点）则按该指定文件名输出图片。  - 如果抽多张图（即：按DOTS方式指定多个时间点或按TIME间隔截图）则输出图片名在该指定文件名基础上在增加时间点（示例：output_filename_10.jpg）。  - 如果指定了压缩抽帧图片生成tar包，则tar包按该指定文件名输出。 

        :return: The output_filename of this ThumbnailPara.
        :rtype: str
        """
        return self._output_filename

    @output_filename.setter
    def output_filename(self, output_filename):
        """Sets the output_filename of this ThumbnailPara.

        截图输出文件名。  - 如果只抽一张图（即：按DOTS方式，指定1个时间点）则按该指定文件名输出图片。  - 如果抽多张图（即：按DOTS方式指定多个时间点或按TIME间隔截图）则输出图片名在该指定文件名基础上在增加时间点（示例：output_filename_10.jpg）。  - 如果指定了压缩抽帧图片生成tar包，则tar包按该指定文件名输出。 

        :param output_filename: The output_filename of this ThumbnailPara.
        :type: str
        """
        self._output_filename = output_filename

    @property
    def format(self):
        """Gets the format of this ThumbnailPara.

        截图文件格式。  取值如下：  1：表示jpg格式 

        :return: The format of this ThumbnailPara.
        :rtype: int
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this ThumbnailPara.

        截图文件格式。  取值如下：  1：表示jpg格式 

        :param format: The format of this ThumbnailPara.
        :type: int
        """
        self._format = format

    @property
    def aspect_ratio(self):
        """Gets the aspect_ratio of this ThumbnailPara.

        纵横比。 

        :return: The aspect_ratio of this ThumbnailPara.
        :rtype: int
        """
        return self._aspect_ratio

    @aspect_ratio.setter
    def aspect_ratio(self, aspect_ratio):
        """Sets the aspect_ratio of this ThumbnailPara.

        纵横比。 

        :param aspect_ratio: The aspect_ratio of this ThumbnailPara.
        :type: int
        """
        self._aspect_ratio = aspect_ratio

    @property
    def width(self):
        """Gets the width of this ThumbnailPara.

        图片宽度  取值范围：(96,3840]  单位：px 

        :return: The width of this ThumbnailPara.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this ThumbnailPara.

        图片宽度  取值范围：(96,3840]  单位：px 

        :param width: The width of this ThumbnailPara.
        :type: int
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this ThumbnailPara.

        图片高度  取值范围：(96,2160]  单位：px 

        :return: The height of this ThumbnailPara.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this ThumbnailPara.

        图片高度  取值范围：(96,2160]  单位：px 

        :param height: The height of this ThumbnailPara.
        :type: int
        """
        self._height = height

    @property
    def max_length(self):
        """Gets the max_length of this ThumbnailPara.

        截图最长边的尺寸。宽边尺寸按照该尺寸与原始视频像素等比缩放计算。  取值范围：[240,3840]  默认值：480  单位：像素 > 该参数和width/height选择使用，以width/height优先，若width/height都不等于0，则图片尺寸按width/height得出；反之，则图片尺寸按 max_length 得出。 > 若该参数和width/height都未选择，则取max_length默认为480 

        :return: The max_length of this ThumbnailPara.
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this ThumbnailPara.

        截图最长边的尺寸。宽边尺寸按照该尺寸与原始视频像素等比缩放计算。  取值范围：[240,3840]  默认值：480  单位：像素 > 该参数和width/height选择使用，以width/height优先，若width/height都不等于0，则图片尺寸按width/height得出；反之，则图片尺寸按 max_length 得出。 > 若该参数和width/height都未选择，则取max_length默认为480 

        :param max_length: The max_length of this ThumbnailPara.
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
        if not isinstance(other, ThumbnailPara):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
