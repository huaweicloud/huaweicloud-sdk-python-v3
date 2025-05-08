# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObjectThumbnailTask:

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
        'dots': 'list[int]',
        'output_filename': 'str',
        'format': 'str',
        'fill_type': 'str',
        'width': 'int',
        'height': 'int',
        'output': 'ObsInfo'
    }

    attribute_map = {
        'type': 'type',
        'percent': 'percent',
        'dots': 'dots',
        'output_filename': 'output_filename',
        'format': 'format',
        'fill_type': 'fill_type',
        'width': 'width',
        'height': 'height',
        'output': 'output'
    }

    def __init__(self, type=None, percent=None, dots=None, output_filename=None, format=None, fill_type=None, width=None, height=None, output=None):
        r"""ObjectThumbnailTask

        The model defined in huaweicloud sdk

        :param type: 采样类型。 取值如下： PERCENT：根据视频时长百分比间隔采样时的百分比值。 DOTS：指定时间点截图。选择同步截图时，需指定此类型。 
        :type type: str
        :param percent: 根据视频时长百分比间隔采样时的百分比值。 
        :type percent: int
        :param dots: 指定时间截图的时间点数组 例如输入[1,3,5]，分别截取视频第1秒、第3秒、第5秒位置的图像帧 最多支持10个时间点 
        :type dots: list[int]
        :param output_filename: 截图输出文件名。 - 如果只抽一张图（即：按DOTS方式，指定1个时间点）则按该指定文件名输出图片。 - 如果抽多张图（即：按DOTS方式指定多个时间点或按TIME间隔截图）则输出图片名在该指定文件名基础上在增加时间点（示例：output_filename_10.jpg）。 - 如果按照PERCENT截图则按照output_filename_0.jpg,output_filename_1.jpg顺序命名 
        :type output_filename: str
        :param format: 截图文件格式 取值如下：jpg、png 
        :type format: str
        :param fill_type: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式： - stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“； - black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。 - white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。 
        :type fill_type: str
        :param width: 图片宽度 取值范围： - [96,3840] - 0：自适应，保持原有宽高 单位：px 
        :type width: int
        :param height: 图片高度 取值范围： - [96,2160] - 0：自适应，保持原有宽高 单位：px 
        :type height: int
        :param output: 
        :type output: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        
        

        self._type = None
        self._percent = None
        self._dots = None
        self._output_filename = None
        self._format = None
        self._fill_type = None
        self._width = None
        self._height = None
        self._output = None
        self.discriminator = None

        self.type = type
        if percent is not None:
            self.percent = percent
        if dots is not None:
            self.dots = dots
        if output_filename is not None:
            self.output_filename = output_filename
        if format is not None:
            self.format = format
        if fill_type is not None:
            self.fill_type = fill_type
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if output is not None:
            self.output = output

    @property
    def type(self):
        r"""Gets the type of this ObjectThumbnailTask.

        采样类型。 取值如下： PERCENT：根据视频时长百分比间隔采样时的百分比值。 DOTS：指定时间点截图。选择同步截图时，需指定此类型。 

        :return: The type of this ObjectThumbnailTask.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ObjectThumbnailTask.

        采样类型。 取值如下： PERCENT：根据视频时长百分比间隔采样时的百分比值。 DOTS：指定时间点截图。选择同步截图时，需指定此类型。 

        :param type: The type of this ObjectThumbnailTask.
        :type type: str
        """
        self._type = type

    @property
    def percent(self):
        r"""Gets the percent of this ObjectThumbnailTask.

        根据视频时长百分比间隔采样时的百分比值。 

        :return: The percent of this ObjectThumbnailTask.
        :rtype: int
        """
        return self._percent

    @percent.setter
    def percent(self, percent):
        r"""Sets the percent of this ObjectThumbnailTask.

        根据视频时长百分比间隔采样时的百分比值。 

        :param percent: The percent of this ObjectThumbnailTask.
        :type percent: int
        """
        self._percent = percent

    @property
    def dots(self):
        r"""Gets the dots of this ObjectThumbnailTask.

        指定时间截图的时间点数组 例如输入[1,3,5]，分别截取视频第1秒、第3秒、第5秒位置的图像帧 最多支持10个时间点 

        :return: The dots of this ObjectThumbnailTask.
        :rtype: list[int]
        """
        return self._dots

    @dots.setter
    def dots(self, dots):
        r"""Sets the dots of this ObjectThumbnailTask.

        指定时间截图的时间点数组 例如输入[1,3,5]，分别截取视频第1秒、第3秒、第5秒位置的图像帧 最多支持10个时间点 

        :param dots: The dots of this ObjectThumbnailTask.
        :type dots: list[int]
        """
        self._dots = dots

    @property
    def output_filename(self):
        r"""Gets the output_filename of this ObjectThumbnailTask.

        截图输出文件名。 - 如果只抽一张图（即：按DOTS方式，指定1个时间点）则按该指定文件名输出图片。 - 如果抽多张图（即：按DOTS方式指定多个时间点或按TIME间隔截图）则输出图片名在该指定文件名基础上在增加时间点（示例：output_filename_10.jpg）。 - 如果按照PERCENT截图则按照output_filename_0.jpg,output_filename_1.jpg顺序命名 

        :return: The output_filename of this ObjectThumbnailTask.
        :rtype: str
        """
        return self._output_filename

    @output_filename.setter
    def output_filename(self, output_filename):
        r"""Sets the output_filename of this ObjectThumbnailTask.

        截图输出文件名。 - 如果只抽一张图（即：按DOTS方式，指定1个时间点）则按该指定文件名输出图片。 - 如果抽多张图（即：按DOTS方式指定多个时间点或按TIME间隔截图）则输出图片名在该指定文件名基础上在增加时间点（示例：output_filename_10.jpg）。 - 如果按照PERCENT截图则按照output_filename_0.jpg,output_filename_1.jpg顺序命名 

        :param output_filename: The output_filename of this ObjectThumbnailTask.
        :type output_filename: str
        """
        self._output_filename = output_filename

    @property
    def format(self):
        r"""Gets the format of this ObjectThumbnailTask.

        截图文件格式 取值如下：jpg、png 

        :return: The format of this ObjectThumbnailTask.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this ObjectThumbnailTask.

        截图文件格式 取值如下：jpg、png 

        :param format: The format of this ObjectThumbnailTask.
        :type format: str
        """
        self._format = format

    @property
    def fill_type(self):
        r"""Gets the fill_type of this ObjectThumbnailTask.

        填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式： - stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“； - black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。 - white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。 

        :return: The fill_type of this ObjectThumbnailTask.
        :rtype: str
        """
        return self._fill_type

    @fill_type.setter
    def fill_type(self, fill_type):
        r"""Sets the fill_type of this ObjectThumbnailTask.

        填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式： - stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“； - black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。 - white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。 

        :param fill_type: The fill_type of this ObjectThumbnailTask.
        :type fill_type: str
        """
        self._fill_type = fill_type

    @property
    def width(self):
        r"""Gets the width of this ObjectThumbnailTask.

        图片宽度 取值范围： - [96,3840] - 0：自适应，保持原有宽高 单位：px 

        :return: The width of this ObjectThumbnailTask.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        r"""Sets the width of this ObjectThumbnailTask.

        图片宽度 取值范围： - [96,3840] - 0：自适应，保持原有宽高 单位：px 

        :param width: The width of this ObjectThumbnailTask.
        :type width: int
        """
        self._width = width

    @property
    def height(self):
        r"""Gets the height of this ObjectThumbnailTask.

        图片高度 取值范围： - [96,2160] - 0：自适应，保持原有宽高 单位：px 

        :return: The height of this ObjectThumbnailTask.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        r"""Sets the height of this ObjectThumbnailTask.

        图片高度 取值范围： - [96,2160] - 0：自适应，保持原有宽高 单位：px 

        :param height: The height of this ObjectThumbnailTask.
        :type height: int
        """
        self._height = height

    @property
    def output(self):
        r"""Gets the output of this ObjectThumbnailTask.

        :return: The output of this ObjectThumbnailTask.
        :rtype: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this ObjectThumbnailTask.

        :param output: The output of this ObjectThumbnailTask.
        :type output: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        self._output = output

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
        if not isinstance(other, ObjectThumbnailTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
