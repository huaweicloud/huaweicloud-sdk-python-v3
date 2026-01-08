# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageSpriteInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'row_count': 'int',
        'column_count': 'int',
        'total_count': 'int',
        'width': 'int',
        'height': 'int',
        'output_image_name': 'list[str]',
        'output_webvtt_name': 'str',
        'output': 'ObsObjInfo'
    }

    attribute_map = {
        'row_count': 'row_count',
        'column_count': 'column_count',
        'total_count': 'total_count',
        'width': 'width',
        'height': 'height',
        'output_image_name': 'output_image_name',
        'output_webvtt_name': 'output_webvtt_name',
        'output': 'output'
    }

    def __init__(self, row_count=None, column_count=None, total_count=None, width=None, height=None, output_image_name=None, output_webvtt_name=None, output=None):
        r"""ImageSpriteInfo

        The model defined in huaweicloud sdk

        :param row_count: 雪碧图中小图的行数。
        :type row_count: int
        :param column_count: 雪碧图中小图的列数。
        :type column_count: int
        :param total_count: 雪碧图中小图数量。
        :type total_count: int
        :param width: 雪碧图小图宽度 
        :type width: int
        :param height: 雪碧图小图高度 
        :type height: int
        :param output_image_name: 每一张雪碧图大图的路径。 
        :type output_image_name: list[str]
        :param output_webvtt_name: 雪碧图子图位置与时间关系的 WebVtt 文件路径。WebVtt 文件表明了各个雪碧图小图对应的时间点，以及在雪碧大图里的坐标位置，一般被播放器用于实现预览。 
        :type output_webvtt_name: str
        :param output: 
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        
        

        self._row_count = None
        self._column_count = None
        self._total_count = None
        self._width = None
        self._height = None
        self._output_image_name = None
        self._output_webvtt_name = None
        self._output = None
        self.discriminator = None

        if row_count is not None:
            self.row_count = row_count
        if column_count is not None:
            self.column_count = column_count
        if total_count is not None:
            self.total_count = total_count
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if output_image_name is not None:
            self.output_image_name = output_image_name
        if output_webvtt_name is not None:
            self.output_webvtt_name = output_webvtt_name
        if output is not None:
            self.output = output

    @property
    def row_count(self):
        r"""Gets the row_count of this ImageSpriteInfo.

        雪碧图中小图的行数。

        :return: The row_count of this ImageSpriteInfo.
        :rtype: int
        """
        return self._row_count

    @row_count.setter
    def row_count(self, row_count):
        r"""Sets the row_count of this ImageSpriteInfo.

        雪碧图中小图的行数。

        :param row_count: The row_count of this ImageSpriteInfo.
        :type row_count: int
        """
        self._row_count = row_count

    @property
    def column_count(self):
        r"""Gets the column_count of this ImageSpriteInfo.

        雪碧图中小图的列数。

        :return: The column_count of this ImageSpriteInfo.
        :rtype: int
        """
        return self._column_count

    @column_count.setter
    def column_count(self, column_count):
        r"""Sets the column_count of this ImageSpriteInfo.

        雪碧图中小图的列数。

        :param column_count: The column_count of this ImageSpriteInfo.
        :type column_count: int
        """
        self._column_count = column_count

    @property
    def total_count(self):
        r"""Gets the total_count of this ImageSpriteInfo.

        雪碧图中小图数量。

        :return: The total_count of this ImageSpriteInfo.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ImageSpriteInfo.

        雪碧图中小图数量。

        :param total_count: The total_count of this ImageSpriteInfo.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def width(self):
        r"""Gets the width of this ImageSpriteInfo.

        雪碧图小图宽度 

        :return: The width of this ImageSpriteInfo.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        r"""Sets the width of this ImageSpriteInfo.

        雪碧图小图宽度 

        :param width: The width of this ImageSpriteInfo.
        :type width: int
        """
        self._width = width

    @property
    def height(self):
        r"""Gets the height of this ImageSpriteInfo.

        雪碧图小图高度 

        :return: The height of this ImageSpriteInfo.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        r"""Sets the height of this ImageSpriteInfo.

        雪碧图小图高度 

        :param height: The height of this ImageSpriteInfo.
        :type height: int
        """
        self._height = height

    @property
    def output_image_name(self):
        r"""Gets the output_image_name of this ImageSpriteInfo.

        每一张雪碧图大图的路径。 

        :return: The output_image_name of this ImageSpriteInfo.
        :rtype: list[str]
        """
        return self._output_image_name

    @output_image_name.setter
    def output_image_name(self, output_image_name):
        r"""Sets the output_image_name of this ImageSpriteInfo.

        每一张雪碧图大图的路径。 

        :param output_image_name: The output_image_name of this ImageSpriteInfo.
        :type output_image_name: list[str]
        """
        self._output_image_name = output_image_name

    @property
    def output_webvtt_name(self):
        r"""Gets the output_webvtt_name of this ImageSpriteInfo.

        雪碧图子图位置与时间关系的 WebVtt 文件路径。WebVtt 文件表明了各个雪碧图小图对应的时间点，以及在雪碧大图里的坐标位置，一般被播放器用于实现预览。 

        :return: The output_webvtt_name of this ImageSpriteInfo.
        :rtype: str
        """
        return self._output_webvtt_name

    @output_webvtt_name.setter
    def output_webvtt_name(self, output_webvtt_name):
        r"""Sets the output_webvtt_name of this ImageSpriteInfo.

        雪碧图子图位置与时间关系的 WebVtt 文件路径。WebVtt 文件表明了各个雪碧图小图对应的时间点，以及在雪碧大图里的坐标位置，一般被播放器用于实现预览。 

        :param output_webvtt_name: The output_webvtt_name of this ImageSpriteInfo.
        :type output_webvtt_name: str
        """
        self._output_webvtt_name = output_webvtt_name

    @property
    def output(self):
        r"""Gets the output of this ImageSpriteInfo.

        :return: The output of this ImageSpriteInfo.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this ImageSpriteInfo.

        :param output: The output of this ImageSpriteInfo.
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._output = output

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImageSpriteInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
