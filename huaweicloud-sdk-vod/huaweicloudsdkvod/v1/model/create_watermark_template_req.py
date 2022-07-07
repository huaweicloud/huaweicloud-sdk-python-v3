# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateWatermarkTemplateReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'watermark_type': 'str',
        'image_process': 'str',
        'dx': 'str',
        'dy': 'str',
        'position': 'str',
        'width': 'str',
        'height': 'str',
        'timeline_start': 'str',
        'timeline_duration': 'str',
        'type': 'str',
        'md5': 'str'
    }

    attribute_map = {
        'name': 'name',
        'watermark_type': 'watermark_type',
        'image_process': 'image_process',
        'dx': 'dx',
        'dy': 'dy',
        'position': 'position',
        'width': 'width',
        'height': 'height',
        'timeline_start': 'timeline_start',
        'timeline_duration': 'timeline_duration',
        'type': 'type',
        'md5': 'md5'
    }

    def __init__(self, name=None, watermark_type=None, image_process=None, dx=None, dy=None, position=None, width=None, height=None, timeline_start=None, timeline_duration=None, type=None, md5=None):
        """CreateWatermarkTemplateReq

        The model defined in huaweicloud sdk

        :param name: 水印模板名称。
        :type name: str
        :param watermark_type: 水印类型，当前只支持Image（图片水印）。
        :type watermark_type: str
        :param image_process: type设置为Image时有效。  目前包括： - Original：只做简单缩放，不做其他处理 - Transparent：图片底色透明 - Grayed：彩色图片变灰
        :type image_process: str
        :param dx: 水印图片相对输出视频的水平偏移量，默认值是0。
        :type dx: str
        :param dy: 水印图片相对输出视频的垂直偏移量，默认值是0。
        :type dy: str
        :param position: 水印的位置。
        :type position: str
        :param width: 水印图片宽。
        :type width: str
        :param height: 水印图片高。
        :type height: str
        :param timeline_start: 水印开始时间，与\&quot;timeline_duration\&quot;配合使用。 取值范围:[0, END)。\&quot;END\&quot;表示视频结束时间。 单位:秒。 
        :type timeline_start: str
        :param timeline_duration: 水印持续时间，与\&quot;timeline_start\&quot;配合使用。 取值范围:(0,END-开始时间]。\&quot;END\&quot;表示视频结束时间。 单位:秒。 默认:END。 
        :type timeline_duration: str
        :param type: 水印图片格式类型。
        :type type: str
        :param md5: 水印图片MD5值。
        :type md5: str
        """
        
        

        self._name = None
        self._watermark_type = None
        self._image_process = None
        self._dx = None
        self._dy = None
        self._position = None
        self._width = None
        self._height = None
        self._timeline_start = None
        self._timeline_duration = None
        self._type = None
        self._md5 = None
        self.discriminator = None

        self.name = name
        if watermark_type is not None:
            self.watermark_type = watermark_type
        if image_process is not None:
            self.image_process = image_process
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
        if timeline_start is not None:
            self.timeline_start = timeline_start
        if timeline_duration is not None:
            self.timeline_duration = timeline_duration
        self.type = type
        if md5 is not None:
            self.md5 = md5

    @property
    def name(self):
        """Gets the name of this CreateWatermarkTemplateReq.

        水印模板名称。

        :return: The name of this CreateWatermarkTemplateReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateWatermarkTemplateReq.

        水印模板名称。

        :param name: The name of this CreateWatermarkTemplateReq.
        :type name: str
        """
        self._name = name

    @property
    def watermark_type(self):
        """Gets the watermark_type of this CreateWatermarkTemplateReq.

        水印类型，当前只支持Image（图片水印）。

        :return: The watermark_type of this CreateWatermarkTemplateReq.
        :rtype: str
        """
        return self._watermark_type

    @watermark_type.setter
    def watermark_type(self, watermark_type):
        """Sets the watermark_type of this CreateWatermarkTemplateReq.

        水印类型，当前只支持Image（图片水印）。

        :param watermark_type: The watermark_type of this CreateWatermarkTemplateReq.
        :type watermark_type: str
        """
        self._watermark_type = watermark_type

    @property
    def image_process(self):
        """Gets the image_process of this CreateWatermarkTemplateReq.

        type设置为Image时有效。  目前包括： - Original：只做简单缩放，不做其他处理 - Transparent：图片底色透明 - Grayed：彩色图片变灰

        :return: The image_process of this CreateWatermarkTemplateReq.
        :rtype: str
        """
        return self._image_process

    @image_process.setter
    def image_process(self, image_process):
        """Sets the image_process of this CreateWatermarkTemplateReq.

        type设置为Image时有效。  目前包括： - Original：只做简单缩放，不做其他处理 - Transparent：图片底色透明 - Grayed：彩色图片变灰

        :param image_process: The image_process of this CreateWatermarkTemplateReq.
        :type image_process: str
        """
        self._image_process = image_process

    @property
    def dx(self):
        """Gets the dx of this CreateWatermarkTemplateReq.

        水印图片相对输出视频的水平偏移量，默认值是0。

        :return: The dx of this CreateWatermarkTemplateReq.
        :rtype: str
        """
        return self._dx

    @dx.setter
    def dx(self, dx):
        """Sets the dx of this CreateWatermarkTemplateReq.

        水印图片相对输出视频的水平偏移量，默认值是0。

        :param dx: The dx of this CreateWatermarkTemplateReq.
        :type dx: str
        """
        self._dx = dx

    @property
    def dy(self):
        """Gets the dy of this CreateWatermarkTemplateReq.

        水印图片相对输出视频的垂直偏移量，默认值是0。

        :return: The dy of this CreateWatermarkTemplateReq.
        :rtype: str
        """
        return self._dy

    @dy.setter
    def dy(self, dy):
        """Sets the dy of this CreateWatermarkTemplateReq.

        水印图片相对输出视频的垂直偏移量，默认值是0。

        :param dy: The dy of this CreateWatermarkTemplateReq.
        :type dy: str
        """
        self._dy = dy

    @property
    def position(self):
        """Gets the position of this CreateWatermarkTemplateReq.

        水印的位置。

        :return: The position of this CreateWatermarkTemplateReq.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this CreateWatermarkTemplateReq.

        水印的位置。

        :param position: The position of this CreateWatermarkTemplateReq.
        :type position: str
        """
        self._position = position

    @property
    def width(self):
        """Gets the width of this CreateWatermarkTemplateReq.

        水印图片宽。

        :return: The width of this CreateWatermarkTemplateReq.
        :rtype: str
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this CreateWatermarkTemplateReq.

        水印图片宽。

        :param width: The width of this CreateWatermarkTemplateReq.
        :type width: str
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this CreateWatermarkTemplateReq.

        水印图片高。

        :return: The height of this CreateWatermarkTemplateReq.
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this CreateWatermarkTemplateReq.

        水印图片高。

        :param height: The height of this CreateWatermarkTemplateReq.
        :type height: str
        """
        self._height = height

    @property
    def timeline_start(self):
        """Gets the timeline_start of this CreateWatermarkTemplateReq.

        水印开始时间，与\"timeline_duration\"配合使用。 取值范围:[0, END)。\"END\"表示视频结束时间。 单位:秒。 

        :return: The timeline_start of this CreateWatermarkTemplateReq.
        :rtype: str
        """
        return self._timeline_start

    @timeline_start.setter
    def timeline_start(self, timeline_start):
        """Sets the timeline_start of this CreateWatermarkTemplateReq.

        水印开始时间，与\"timeline_duration\"配合使用。 取值范围:[0, END)。\"END\"表示视频结束时间。 单位:秒。 

        :param timeline_start: The timeline_start of this CreateWatermarkTemplateReq.
        :type timeline_start: str
        """
        self._timeline_start = timeline_start

    @property
    def timeline_duration(self):
        """Gets the timeline_duration of this CreateWatermarkTemplateReq.

        水印持续时间，与\"timeline_start\"配合使用。 取值范围:(0,END-开始时间]。\"END\"表示视频结束时间。 单位:秒。 默认:END。 

        :return: The timeline_duration of this CreateWatermarkTemplateReq.
        :rtype: str
        """
        return self._timeline_duration

    @timeline_duration.setter
    def timeline_duration(self, timeline_duration):
        """Sets the timeline_duration of this CreateWatermarkTemplateReq.

        水印持续时间，与\"timeline_start\"配合使用。 取值范围:(0,END-开始时间]。\"END\"表示视频结束时间。 单位:秒。 默认:END。 

        :param timeline_duration: The timeline_duration of this CreateWatermarkTemplateReq.
        :type timeline_duration: str
        """
        self._timeline_duration = timeline_duration

    @property
    def type(self):
        """Gets the type of this CreateWatermarkTemplateReq.

        水印图片格式类型。

        :return: The type of this CreateWatermarkTemplateReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateWatermarkTemplateReq.

        水印图片格式类型。

        :param type: The type of this CreateWatermarkTemplateReq.
        :type type: str
        """
        self._type = type

    @property
    def md5(self):
        """Gets the md5 of this CreateWatermarkTemplateReq.

        水印图片MD5值。

        :return: The md5 of this CreateWatermarkTemplateReq.
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this CreateWatermarkTemplateReq.

        水印图片MD5值。

        :param md5: The md5 of this CreateWatermarkTemplateReq.
        :type md5: str
        """
        self._md5 = md5

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
        if not isinstance(other, CreateWatermarkTemplateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
