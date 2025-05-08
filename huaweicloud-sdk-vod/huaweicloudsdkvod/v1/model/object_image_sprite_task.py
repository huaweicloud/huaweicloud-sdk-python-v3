# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObjectImageSpriteTask:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sample_type': 'str',
        'sample_interval': 'int',
        'row_count': 'int',
        'column_count': 'int',
        'width': 'int',
        'height': 'int',
        'resolution_adaptive': 'str',
        'fill_type': 'str',
        'format': 'str',
        'output_object_name': 'str',
        'webvtt_object_name': 'str',
        'output': 'ObsInfo'
    }

    attribute_map = {
        'sample_type': 'sample_type',
        'sample_interval': 'sample_interval',
        'row_count': 'row_count',
        'column_count': 'column_count',
        'width': 'width',
        'height': 'height',
        'resolution_adaptive': 'resolution_adaptive',
        'fill_type': 'fill_type',
        'format': 'format',
        'output_object_name': 'output_object_name',
        'webvtt_object_name': 'webvtt_object_name',
        'output': 'output'
    }

    def __init__(self, sample_type=None, sample_interval=None, row_count=None, column_count=None, width=None, height=None, resolution_adaptive=None, fill_type=None, format=None, output_object_name=None, webvtt_object_name=None, output=None):
        r"""ObjectImageSpriteTask

        The model defined in huaweicloud sdk

        :param sample_type: 采样类型，取值： - PERCENT：按百分比 - TIME：按时间间隔 
        :type sample_type: str
        :param sample_interval: 采样间隔。 -当 sample_type 为 PERCENT 时，指定采样间隔的百分比，(0&lt;sample_interval&lt;&#x3D;100)。 -当 sample_type 为 TIME 时，指定采样间隔的时间，单位为秒(&gt;0)。 
        :type sample_interval: int
        :param row_count: 雪碧图中小图的行数，行数*列数不得超过 100。
        :type row_count: int
        :param column_count: 雪碧图中小图的列数，行数*列数不得超过 100。
        :type column_count: int
        :param width: 雪碧图中小图的宽度（或长边）的最大值，取值范围：0 和 [96, 4096]，单位：px。 - 当 width、height 均为 0，则分辨率同源； - 当 width 为 0，Height 非 0，则 Width 按比例缩放； - 当 width 非 0，Height 为 0，则 Height 按比例缩放； - 当 width、Height 均非 0，则分辨率按用户指定 
        :type width: int
        :param height: 雪碧图中小图的高度（或短边）的最大值，取值范围：0 和 [96, 4096]，单位：px。 - 当 width、height 均为 0，则分辨率同源； - 当 width 为 0，height 非 0，则 width 按比例缩放； - 当 width 非 0，height 为 0，则 height 按比例缩放； - 当 width、height 均非 0，则分辨率按用户指定。 
        :type height: int
        :param resolution_adaptive: 分辨率自适应，可选值： - open：开启，此时，Width 代表视频的长边，Height 表示视频的短边； - close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。 
        :type resolution_adaptive: str
        :param fill_type: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式： - stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“； - black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。 - white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。 
        :type fill_type: str
        :param format: 图片格式，取值为 jpg、png。默认为 jpg。
        :type format: str
        :param output_object_name: 截取雪碧图后，雪碧图图片文件的输出文件名，如果不填，则默认为：{inputName}_imageSprite_{雪碧图id}_{number}.{format}.{雪碧图id}和{number}从0开始递增 
        :type output_object_name: str
        :param webvtt_object_name: 截取雪碧图后，Web VTT 文件的输出路径，只能为相对路径。如果不填，则默认为相对路径：{inputName}_imageSprite_{雪碧图_id}.vtt 
        :type webvtt_object_name: str
        :param output: 
        :type output: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        
        

        self._sample_type = None
        self._sample_interval = None
        self._row_count = None
        self._column_count = None
        self._width = None
        self._height = None
        self._resolution_adaptive = None
        self._fill_type = None
        self._format = None
        self._output_object_name = None
        self._webvtt_object_name = None
        self._output = None
        self.discriminator = None

        self.sample_type = sample_type
        self.sample_interval = sample_interval
        self.row_count = row_count
        self.column_count = column_count
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if resolution_adaptive is not None:
            self.resolution_adaptive = resolution_adaptive
        if fill_type is not None:
            self.fill_type = fill_type
        if format is not None:
            self.format = format
        if output_object_name is not None:
            self.output_object_name = output_object_name
        if webvtt_object_name is not None:
            self.webvtt_object_name = webvtt_object_name
        if output is not None:
            self.output = output

    @property
    def sample_type(self):
        r"""Gets the sample_type of this ObjectImageSpriteTask.

        采样类型，取值： - PERCENT：按百分比 - TIME：按时间间隔 

        :return: The sample_type of this ObjectImageSpriteTask.
        :rtype: str
        """
        return self._sample_type

    @sample_type.setter
    def sample_type(self, sample_type):
        r"""Sets the sample_type of this ObjectImageSpriteTask.

        采样类型，取值： - PERCENT：按百分比 - TIME：按时间间隔 

        :param sample_type: The sample_type of this ObjectImageSpriteTask.
        :type sample_type: str
        """
        self._sample_type = sample_type

    @property
    def sample_interval(self):
        r"""Gets the sample_interval of this ObjectImageSpriteTask.

        采样间隔。 -当 sample_type 为 PERCENT 时，指定采样间隔的百分比，(0<sample_interval<=100)。 -当 sample_type 为 TIME 时，指定采样间隔的时间，单位为秒(>0)。 

        :return: The sample_interval of this ObjectImageSpriteTask.
        :rtype: int
        """
        return self._sample_interval

    @sample_interval.setter
    def sample_interval(self, sample_interval):
        r"""Sets the sample_interval of this ObjectImageSpriteTask.

        采样间隔。 -当 sample_type 为 PERCENT 时，指定采样间隔的百分比，(0<sample_interval<=100)。 -当 sample_type 为 TIME 时，指定采样间隔的时间，单位为秒(>0)。 

        :param sample_interval: The sample_interval of this ObjectImageSpriteTask.
        :type sample_interval: int
        """
        self._sample_interval = sample_interval

    @property
    def row_count(self):
        r"""Gets the row_count of this ObjectImageSpriteTask.

        雪碧图中小图的行数，行数*列数不得超过 100。

        :return: The row_count of this ObjectImageSpriteTask.
        :rtype: int
        """
        return self._row_count

    @row_count.setter
    def row_count(self, row_count):
        r"""Sets the row_count of this ObjectImageSpriteTask.

        雪碧图中小图的行数，行数*列数不得超过 100。

        :param row_count: The row_count of this ObjectImageSpriteTask.
        :type row_count: int
        """
        self._row_count = row_count

    @property
    def column_count(self):
        r"""Gets the column_count of this ObjectImageSpriteTask.

        雪碧图中小图的列数，行数*列数不得超过 100。

        :return: The column_count of this ObjectImageSpriteTask.
        :rtype: int
        """
        return self._column_count

    @column_count.setter
    def column_count(self, column_count):
        r"""Sets the column_count of this ObjectImageSpriteTask.

        雪碧图中小图的列数，行数*列数不得超过 100。

        :param column_count: The column_count of this ObjectImageSpriteTask.
        :type column_count: int
        """
        self._column_count = column_count

    @property
    def width(self):
        r"""Gets the width of this ObjectImageSpriteTask.

        雪碧图中小图的宽度（或长边）的最大值，取值范围：0 和 [96, 4096]，单位：px。 - 当 width、height 均为 0，则分辨率同源； - 当 width 为 0，Height 非 0，则 Width 按比例缩放； - 当 width 非 0，Height 为 0，则 Height 按比例缩放； - 当 width、Height 均非 0，则分辨率按用户指定 

        :return: The width of this ObjectImageSpriteTask.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        r"""Sets the width of this ObjectImageSpriteTask.

        雪碧图中小图的宽度（或长边）的最大值，取值范围：0 和 [96, 4096]，单位：px。 - 当 width、height 均为 0，则分辨率同源； - 当 width 为 0，Height 非 0，则 Width 按比例缩放； - 当 width 非 0，Height 为 0，则 Height 按比例缩放； - 当 width、Height 均非 0，则分辨率按用户指定 

        :param width: The width of this ObjectImageSpriteTask.
        :type width: int
        """
        self._width = width

    @property
    def height(self):
        r"""Gets the height of this ObjectImageSpriteTask.

        雪碧图中小图的高度（或短边）的最大值，取值范围：0 和 [96, 4096]，单位：px。 - 当 width、height 均为 0，则分辨率同源； - 当 width 为 0，height 非 0，则 width 按比例缩放； - 当 width 非 0，height 为 0，则 height 按比例缩放； - 当 width、height 均非 0，则分辨率按用户指定。 

        :return: The height of this ObjectImageSpriteTask.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        r"""Sets the height of this ObjectImageSpriteTask.

        雪碧图中小图的高度（或短边）的最大值，取值范围：0 和 [96, 4096]，单位：px。 - 当 width、height 均为 0，则分辨率同源； - 当 width 为 0，height 非 0，则 width 按比例缩放； - 当 width 非 0，height 为 0，则 height 按比例缩放； - 当 width、height 均非 0，则分辨率按用户指定。 

        :param height: The height of this ObjectImageSpriteTask.
        :type height: int
        """
        self._height = height

    @property
    def resolution_adaptive(self):
        r"""Gets the resolution_adaptive of this ObjectImageSpriteTask.

        分辨率自适应，可选值： - open：开启，此时，Width 代表视频的长边，Height 表示视频的短边； - close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。 

        :return: The resolution_adaptive of this ObjectImageSpriteTask.
        :rtype: str
        """
        return self._resolution_adaptive

    @resolution_adaptive.setter
    def resolution_adaptive(self, resolution_adaptive):
        r"""Sets the resolution_adaptive of this ObjectImageSpriteTask.

        分辨率自适应，可选值： - open：开启，此时，Width 代表视频的长边，Height 表示视频的短边； - close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。 

        :param resolution_adaptive: The resolution_adaptive of this ObjectImageSpriteTask.
        :type resolution_adaptive: str
        """
        self._resolution_adaptive = resolution_adaptive

    @property
    def fill_type(self):
        r"""Gets the fill_type of this ObjectImageSpriteTask.

        填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式： - stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“； - black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。 - white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。 

        :return: The fill_type of this ObjectImageSpriteTask.
        :rtype: str
        """
        return self._fill_type

    @fill_type.setter
    def fill_type(self, fill_type):
        r"""Sets the fill_type of this ObjectImageSpriteTask.

        填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式： - stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“； - black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。 - white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。 

        :param fill_type: The fill_type of this ObjectImageSpriteTask.
        :type fill_type: str
        """
        self._fill_type = fill_type

    @property
    def format(self):
        r"""Gets the format of this ObjectImageSpriteTask.

        图片格式，取值为 jpg、png。默认为 jpg。

        :return: The format of this ObjectImageSpriteTask.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this ObjectImageSpriteTask.

        图片格式，取值为 jpg、png。默认为 jpg。

        :param format: The format of this ObjectImageSpriteTask.
        :type format: str
        """
        self._format = format

    @property
    def output_object_name(self):
        r"""Gets the output_object_name of this ObjectImageSpriteTask.

        截取雪碧图后，雪碧图图片文件的输出文件名，如果不填，则默认为：{inputName}_imageSprite_{雪碧图id}_{number}.{format}.{雪碧图id}和{number}从0开始递增 

        :return: The output_object_name of this ObjectImageSpriteTask.
        :rtype: str
        """
        return self._output_object_name

    @output_object_name.setter
    def output_object_name(self, output_object_name):
        r"""Sets the output_object_name of this ObjectImageSpriteTask.

        截取雪碧图后，雪碧图图片文件的输出文件名，如果不填，则默认为：{inputName}_imageSprite_{雪碧图id}_{number}.{format}.{雪碧图id}和{number}从0开始递增 

        :param output_object_name: The output_object_name of this ObjectImageSpriteTask.
        :type output_object_name: str
        """
        self._output_object_name = output_object_name

    @property
    def webvtt_object_name(self):
        r"""Gets the webvtt_object_name of this ObjectImageSpriteTask.

        截取雪碧图后，Web VTT 文件的输出路径，只能为相对路径。如果不填，则默认为相对路径：{inputName}_imageSprite_{雪碧图_id}.vtt 

        :return: The webvtt_object_name of this ObjectImageSpriteTask.
        :rtype: str
        """
        return self._webvtt_object_name

    @webvtt_object_name.setter
    def webvtt_object_name(self, webvtt_object_name):
        r"""Sets the webvtt_object_name of this ObjectImageSpriteTask.

        截取雪碧图后，Web VTT 文件的输出路径，只能为相对路径。如果不填，则默认为相对路径：{inputName}_imageSprite_{雪碧图_id}.vtt 

        :param webvtt_object_name: The webvtt_object_name of this ObjectImageSpriteTask.
        :type webvtt_object_name: str
        """
        self._webvtt_object_name = webvtt_object_name

    @property
    def output(self):
        r"""Gets the output of this ObjectImageSpriteTask.

        :return: The output of this ObjectImageSpriteTask.
        :rtype: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this ObjectImageSpriteTask.

        :param output: The output of this ObjectImageSpriteTask.
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
        if not isinstance(other, ObjectImageSpriteTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
