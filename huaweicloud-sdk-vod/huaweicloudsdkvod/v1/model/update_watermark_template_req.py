# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateWatermarkTemplateReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'dx': 'str',
        'dy': 'str',
        'position': 'str',
        'width': 'str',
        'height': 'str',
        'watermark_type': 'str',
        'image_process': 'str',
        'timeline_start': 'str',
        'timeline_duration': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'dx': 'dx',
        'dy': 'dy',
        'position': 'position',
        'width': 'width',
        'height': 'height',
        'watermark_type': 'watermark_type',
        'image_process': 'image_process',
        'timeline_start': 'timeline_start',
        'timeline_duration': 'timeline_duration'
    }

    def __init__(self, id=None, name=None, dx=None, dy=None, position=None, width=None, height=None, watermark_type=None, image_process=None, timeline_start=None, timeline_duration=None):
        """UpdateWatermarkTemplateReq

        The model defined in huaweicloud sdk

        :param id: 水印模板配置id&lt;br/&gt;
        :type id: str
        :param name: 水印模板名称&lt;br/&gt;
        :type name: str
        :param dx: 水印图片相对输出视频的水平偏移量，默认值是0&lt;br/&gt;
        :type dx: str
        :param dy: 水印图片相对输出视频的垂直偏移量，默认值是0&lt;br/&gt;
        :type dy: str
        :param position: 水印的位置&lt;br/&gt;
        :type position: str
        :param width: 水印图片宽&lt;br/&gt;
        :type width: str
        :param height: 水印图片高&lt;br/&gt;
        :type height: str
        :param watermark_type: 水印类型，当前只支持Image（图片水印）&lt;br/&gt;
        :type watermark_type: str
        :param image_process: type设置为Image时有效。  目前包括： - Original：只做简单缩放，不做其他处理 - Transparent：图片底色透明 - Grayed：彩色图片变灰
        :type image_process: str
        :param timeline_start: 水印开始时间，与\&quot;timeline_duration\&quot;配合使用。 取值范围:[0, END)。\&quot;END\&quot;表示视频结束时间。 单位:秒。 
        :type timeline_start: str
        :param timeline_duration: 水印持续时间，与\&quot;timeline_start\&quot;配合使用。 取值范围:(0,END-开始时间]。\&quot;END\&quot;表示视频结束时间。 单位:秒。 默认:END。 
        :type timeline_duration: str
        """
        
        

        self._id = None
        self._name = None
        self._dx = None
        self._dy = None
        self._position = None
        self._width = None
        self._height = None
        self._watermark_type = None
        self._image_process = None
        self._timeline_start = None
        self._timeline_duration = None
        self.discriminator = None

        self.id = id
        if name is not None:
            self.name = name
        if dx is not None:
            self.dx = dx
        if dy is not None:
            self.dy = dy
        if position is not None:
            self.position = position
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if watermark_type is not None:
            self.watermark_type = watermark_type
        if image_process is not None:
            self.image_process = image_process
        if timeline_start is not None:
            self.timeline_start = timeline_start
        if timeline_duration is not None:
            self.timeline_duration = timeline_duration

    @property
    def id(self):
        """Gets the id of this UpdateWatermarkTemplateReq.

        水印模板配置id<br/>

        :return: The id of this UpdateWatermarkTemplateReq.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateWatermarkTemplateReq.

        水印模板配置id<br/>

        :param id: The id of this UpdateWatermarkTemplateReq.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this UpdateWatermarkTemplateReq.

        水印模板名称<br/>

        :return: The name of this UpdateWatermarkTemplateReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateWatermarkTemplateReq.

        水印模板名称<br/>

        :param name: The name of this UpdateWatermarkTemplateReq.
        :type name: str
        """
        self._name = name

    @property
    def dx(self):
        """Gets the dx of this UpdateWatermarkTemplateReq.

        水印图片相对输出视频的水平偏移量，默认值是0<br/>

        :return: The dx of this UpdateWatermarkTemplateReq.
        :rtype: str
        """
        return self._dx

    @dx.setter
    def dx(self, dx):
        """Sets the dx of this UpdateWatermarkTemplateReq.

        水印图片相对输出视频的水平偏移量，默认值是0<br/>

        :param dx: The dx of this UpdateWatermarkTemplateReq.
        :type dx: str
        """
        self._dx = dx

    @property
    def dy(self):
        """Gets the dy of this UpdateWatermarkTemplateReq.

        水印图片相对输出视频的垂直偏移量，默认值是0<br/>

        :return: The dy of this UpdateWatermarkTemplateReq.
        :rtype: str
        """
        return self._dy

    @dy.setter
    def dy(self, dy):
        """Sets the dy of this UpdateWatermarkTemplateReq.

        水印图片相对输出视频的垂直偏移量，默认值是0<br/>

        :param dy: The dy of this UpdateWatermarkTemplateReq.
        :type dy: str
        """
        self._dy = dy

    @property
    def position(self):
        """Gets the position of this UpdateWatermarkTemplateReq.

        水印的位置<br/>

        :return: The position of this UpdateWatermarkTemplateReq.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this UpdateWatermarkTemplateReq.

        水印的位置<br/>

        :param position: The position of this UpdateWatermarkTemplateReq.
        :type position: str
        """
        self._position = position

    @property
    def width(self):
        """Gets the width of this UpdateWatermarkTemplateReq.

        水印图片宽<br/>

        :return: The width of this UpdateWatermarkTemplateReq.
        :rtype: str
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this UpdateWatermarkTemplateReq.

        水印图片宽<br/>

        :param width: The width of this UpdateWatermarkTemplateReq.
        :type width: str
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this UpdateWatermarkTemplateReq.

        水印图片高<br/>

        :return: The height of this UpdateWatermarkTemplateReq.
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this UpdateWatermarkTemplateReq.

        水印图片高<br/>

        :param height: The height of this UpdateWatermarkTemplateReq.
        :type height: str
        """
        self._height = height

    @property
    def watermark_type(self):
        """Gets the watermark_type of this UpdateWatermarkTemplateReq.

        水印类型，当前只支持Image（图片水印）<br/>

        :return: The watermark_type of this UpdateWatermarkTemplateReq.
        :rtype: str
        """
        return self._watermark_type

    @watermark_type.setter
    def watermark_type(self, watermark_type):
        """Sets the watermark_type of this UpdateWatermarkTemplateReq.

        水印类型，当前只支持Image（图片水印）<br/>

        :param watermark_type: The watermark_type of this UpdateWatermarkTemplateReq.
        :type watermark_type: str
        """
        self._watermark_type = watermark_type

    @property
    def image_process(self):
        """Gets the image_process of this UpdateWatermarkTemplateReq.

        type设置为Image时有效。  目前包括： - Original：只做简单缩放，不做其他处理 - Transparent：图片底色透明 - Grayed：彩色图片变灰

        :return: The image_process of this UpdateWatermarkTemplateReq.
        :rtype: str
        """
        return self._image_process

    @image_process.setter
    def image_process(self, image_process):
        """Sets the image_process of this UpdateWatermarkTemplateReq.

        type设置为Image时有效。  目前包括： - Original：只做简单缩放，不做其他处理 - Transparent：图片底色透明 - Grayed：彩色图片变灰

        :param image_process: The image_process of this UpdateWatermarkTemplateReq.
        :type image_process: str
        """
        self._image_process = image_process

    @property
    def timeline_start(self):
        """Gets the timeline_start of this UpdateWatermarkTemplateReq.

        水印开始时间，与\"timeline_duration\"配合使用。 取值范围:[0, END)。\"END\"表示视频结束时间。 单位:秒。 

        :return: The timeline_start of this UpdateWatermarkTemplateReq.
        :rtype: str
        """
        return self._timeline_start

    @timeline_start.setter
    def timeline_start(self, timeline_start):
        """Sets the timeline_start of this UpdateWatermarkTemplateReq.

        水印开始时间，与\"timeline_duration\"配合使用。 取值范围:[0, END)。\"END\"表示视频结束时间。 单位:秒。 

        :param timeline_start: The timeline_start of this UpdateWatermarkTemplateReq.
        :type timeline_start: str
        """
        self._timeline_start = timeline_start

    @property
    def timeline_duration(self):
        """Gets the timeline_duration of this UpdateWatermarkTemplateReq.

        水印持续时间，与\"timeline_start\"配合使用。 取值范围:(0,END-开始时间]。\"END\"表示视频结束时间。 单位:秒。 默认:END。 

        :return: The timeline_duration of this UpdateWatermarkTemplateReq.
        :rtype: str
        """
        return self._timeline_duration

    @timeline_duration.setter
    def timeline_duration(self, timeline_duration):
        """Sets the timeline_duration of this UpdateWatermarkTemplateReq.

        水印持续时间，与\"timeline_start\"配合使用。 取值范围:(0,END-开始时间]。\"END\"表示视频结束时间。 单位:秒。 默认:END。 

        :param timeline_duration: The timeline_duration of this UpdateWatermarkTemplateReq.
        :type timeline_duration: str
        """
        self._timeline_duration = timeline_duration

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
        if not isinstance(other, UpdateWatermarkTemplateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
