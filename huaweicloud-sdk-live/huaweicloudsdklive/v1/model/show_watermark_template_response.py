# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWatermarkTemplateResponse(SdkResponse):

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
        'type': 'int',
        'description': 'str',
        'picture_url': 'str',
        'width': 'float',
        'height': 'float',
        'location': 'WatermarkLocation',
        'text': 'WordWaterMarkInfo',
        'scene': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'picture_url': 'picture_url',
        'width': 'width',
        'height': 'height',
        'location': 'location',
        'text': 'text',
        'scene': 'scene',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, name=None, type=None, description=None, picture_url=None, width=None, height=None, location=None, text=None, scene=None, x_request_id=None):
        r"""ShowWatermarkTemplateResponse

        The model defined in huaweicloud sdk

        :param name: 水印模板名称
        :type name: str
        :param type: 水印类型，0图片，1文字,2图文共存
        :type type: int
        :param description: 模板注释
        :type description: str
        :param picture_url: 图片下载路径 校验规则：图片URL长度大于0，最大长度2048，能够正常按URL格式解析，必须是 http 或 https 协议。（OTT 场景限制只支持https） 图片格式: .png/.jpg/.PNG/.JPG结尾
        :type picture_url: str
        :param width: 1）整数型代表水印图片宽的像素值，范围0或[8，4096]，单位px。 2）小数型代表相对输出视频分辨率宽的比率，范围[0,1) 建议宽高只设置一项，另外一项会自适应缩放，避免变形。宽高全部设置为0表示水印图片原始宽高 百分比限制最多保留小数点后4位，width和height 只支持同时为像素或是百分比，不支持一个像素，一个百分比
        :type width: float
        :param height: 水印图片高，值有两种形式： 1）整数型代表水印图片高的像素值，范围0或[8，4096]，单位px。 2）小数型代表相对输出视频分辨率高的比率，范围[0，1) 建议宽高只设置一项，另外一项会自适应缩放，避免变形。宽高全部设置为0表示水印图片原始宽高 百分比限制最多保留小数点后4位，width和height 只支持同时为像素或是百分比，不支持一个像素，一个百分比
        :type height: float
        :param location: 
        :type location: :class:`huaweicloudsdklive.v1.WatermarkLocation`
        :param text: 
        :type text: :class:`huaweicloudsdklive.v1.WordWaterMarkInfo`
        :param scene: 业务属性，cloud_live：云直播，默认值；media_live：媒体直播，不支持修改
        :type scene: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._name = None
        self._type = None
        self._description = None
        self._picture_url = None
        self._width = None
        self._height = None
        self._location = None
        self._text = None
        self._scene = None
        self._x_request_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if picture_url is not None:
            self.picture_url = picture_url
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if location is not None:
            self.location = location
        if text is not None:
            self.text = text
        if scene is not None:
            self.scene = scene
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def name(self):
        r"""Gets the name of this ShowWatermarkTemplateResponse.

        水印模板名称

        :return: The name of this ShowWatermarkTemplateResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowWatermarkTemplateResponse.

        水印模板名称

        :param name: The name of this ShowWatermarkTemplateResponse.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this ShowWatermarkTemplateResponse.

        水印类型，0图片，1文字,2图文共存

        :return: The type of this ShowWatermarkTemplateResponse.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowWatermarkTemplateResponse.

        水印类型，0图片，1文字,2图文共存

        :param type: The type of this ShowWatermarkTemplateResponse.
        :type type: int
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this ShowWatermarkTemplateResponse.

        模板注释

        :return: The description of this ShowWatermarkTemplateResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowWatermarkTemplateResponse.

        模板注释

        :param description: The description of this ShowWatermarkTemplateResponse.
        :type description: str
        """
        self._description = description

    @property
    def picture_url(self):
        r"""Gets the picture_url of this ShowWatermarkTemplateResponse.

        图片下载路径 校验规则：图片URL长度大于0，最大长度2048，能够正常按URL格式解析，必须是 http 或 https 协议。（OTT 场景限制只支持https） 图片格式: .png/.jpg/.PNG/.JPG结尾

        :return: The picture_url of this ShowWatermarkTemplateResponse.
        :rtype: str
        """
        return self._picture_url

    @picture_url.setter
    def picture_url(self, picture_url):
        r"""Sets the picture_url of this ShowWatermarkTemplateResponse.

        图片下载路径 校验规则：图片URL长度大于0，最大长度2048，能够正常按URL格式解析，必须是 http 或 https 协议。（OTT 场景限制只支持https） 图片格式: .png/.jpg/.PNG/.JPG结尾

        :param picture_url: The picture_url of this ShowWatermarkTemplateResponse.
        :type picture_url: str
        """
        self._picture_url = picture_url

    @property
    def width(self):
        r"""Gets the width of this ShowWatermarkTemplateResponse.

        1）整数型代表水印图片宽的像素值，范围0或[8，4096]，单位px。 2）小数型代表相对输出视频分辨率宽的比率，范围[0,1) 建议宽高只设置一项，另外一项会自适应缩放，避免变形。宽高全部设置为0表示水印图片原始宽高 百分比限制最多保留小数点后4位，width和height 只支持同时为像素或是百分比，不支持一个像素，一个百分比

        :return: The width of this ShowWatermarkTemplateResponse.
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        r"""Sets the width of this ShowWatermarkTemplateResponse.

        1）整数型代表水印图片宽的像素值，范围0或[8，4096]，单位px。 2）小数型代表相对输出视频分辨率宽的比率，范围[0,1) 建议宽高只设置一项，另外一项会自适应缩放，避免变形。宽高全部设置为0表示水印图片原始宽高 百分比限制最多保留小数点后4位，width和height 只支持同时为像素或是百分比，不支持一个像素，一个百分比

        :param width: The width of this ShowWatermarkTemplateResponse.
        :type width: float
        """
        self._width = width

    @property
    def height(self):
        r"""Gets the height of this ShowWatermarkTemplateResponse.

        水印图片高，值有两种形式： 1）整数型代表水印图片高的像素值，范围0或[8，4096]，单位px。 2）小数型代表相对输出视频分辨率高的比率，范围[0，1) 建议宽高只设置一项，另外一项会自适应缩放，避免变形。宽高全部设置为0表示水印图片原始宽高 百分比限制最多保留小数点后4位，width和height 只支持同时为像素或是百分比，不支持一个像素，一个百分比

        :return: The height of this ShowWatermarkTemplateResponse.
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        r"""Sets the height of this ShowWatermarkTemplateResponse.

        水印图片高，值有两种形式： 1）整数型代表水印图片高的像素值，范围0或[8，4096]，单位px。 2）小数型代表相对输出视频分辨率高的比率，范围[0，1) 建议宽高只设置一项，另外一项会自适应缩放，避免变形。宽高全部设置为0表示水印图片原始宽高 百分比限制最多保留小数点后4位，width和height 只支持同时为像素或是百分比，不支持一个像素，一个百分比

        :param height: The height of this ShowWatermarkTemplateResponse.
        :type height: float
        """
        self._height = height

    @property
    def location(self):
        r"""Gets the location of this ShowWatermarkTemplateResponse.

        :return: The location of this ShowWatermarkTemplateResponse.
        :rtype: :class:`huaweicloudsdklive.v1.WatermarkLocation`
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this ShowWatermarkTemplateResponse.

        :param location: The location of this ShowWatermarkTemplateResponse.
        :type location: :class:`huaweicloudsdklive.v1.WatermarkLocation`
        """
        self._location = location

    @property
    def text(self):
        r"""Gets the text of this ShowWatermarkTemplateResponse.

        :return: The text of this ShowWatermarkTemplateResponse.
        :rtype: :class:`huaweicloudsdklive.v1.WordWaterMarkInfo`
        """
        return self._text

    @text.setter
    def text(self, text):
        r"""Sets the text of this ShowWatermarkTemplateResponse.

        :param text: The text of this ShowWatermarkTemplateResponse.
        :type text: :class:`huaweicloudsdklive.v1.WordWaterMarkInfo`
        """
        self._text = text

    @property
    def scene(self):
        r"""Gets the scene of this ShowWatermarkTemplateResponse.

        业务属性，cloud_live：云直播，默认值；media_live：媒体直播，不支持修改

        :return: The scene of this ShowWatermarkTemplateResponse.
        :rtype: str
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        r"""Sets the scene of this ShowWatermarkTemplateResponse.

        业务属性，cloud_live：云直播，默认值；media_live：媒体直播，不支持修改

        :param scene: The scene of this ShowWatermarkTemplateResponse.
        :type scene: str
        """
        self._scene = scene

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowWatermarkTemplateResponse.

        :return: The x_request_id of this ShowWatermarkTemplateResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowWatermarkTemplateResponse.

        :param x_request_id: The x_request_id of this ShowWatermarkTemplateResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ShowWatermarkTemplateResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowWatermarkTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
