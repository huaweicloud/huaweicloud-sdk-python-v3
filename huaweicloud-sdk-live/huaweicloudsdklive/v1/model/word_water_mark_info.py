# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WordWaterMarkInfo:

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
        'font_color': 'str',
        'font_size': 'int',
        'font': 'str',
        'time_zone': 'str',
        'shadow_color': 'str',
        'location': 'WatermarkLocation'
    }

    attribute_map = {
        'format': 'format',
        'font_color': 'font_color',
        'font_size': 'font_size',
        'font': 'font',
        'time_zone': 'time_zone',
        'shadow_color': 'shadow_color',
        'location': 'location'
    }

    def __init__(self, format=None, font_color=None, font_size=None, font=None, time_zone=None, shadow_color=None, location=None):
        r"""WordWaterMarkInfo

        The model defined in huaweicloud sdk

        :param format: 水印文字内容，必填 字幕内容1-64 type为1或2时必填，type为0时非必填
        :type format: str
        :param font_color: 参数校验：首位为#、除#外为6位或8位，每位字符由 0-9、a~f、A~F 组成【务必校验，错误时转码默认白色】
        :type font_color: str
        :param font_size: 字体大小
        :type font_size: int
        :param font: 字体，缺省值 空，可选值：harmonyRegular（鸿蒙）、douyu2.0（斗鱼追光体）
        :type font: str
        :param time_zone: 时区，【取值参考 UTC-1200 至 UTC+1200，前三位UTC，第四位+或-，五六位表示小时，七八位固定00】
        :type time_zone: str
        :param shadow_color: 缺省值 none，参数校验：首位为#、除#外为6位或8位，每位字符由 0-9、a~f、A~F 组成【务必校验，错误时转码默认黑色】
        :type shadow_color: str
        :param location: 
        :type location: :class:`huaweicloudsdklive.v1.WatermarkLocation`
        """
        
        

        self._format = None
        self._font_color = None
        self._font_size = None
        self._font = None
        self._time_zone = None
        self._shadow_color = None
        self._location = None
        self.discriminator = None

        self.format = format
        if font_color is not None:
            self.font_color = font_color
        if font_size is not None:
            self.font_size = font_size
        if font is not None:
            self.font = font
        if time_zone is not None:
            self.time_zone = time_zone
        if shadow_color is not None:
            self.shadow_color = shadow_color
        self.location = location

    @property
    def format(self):
        r"""Gets the format of this WordWaterMarkInfo.

        水印文字内容，必填 字幕内容1-64 type为1或2时必填，type为0时非必填

        :return: The format of this WordWaterMarkInfo.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this WordWaterMarkInfo.

        水印文字内容，必填 字幕内容1-64 type为1或2时必填，type为0时非必填

        :param format: The format of this WordWaterMarkInfo.
        :type format: str
        """
        self._format = format

    @property
    def font_color(self):
        r"""Gets the font_color of this WordWaterMarkInfo.

        参数校验：首位为#、除#外为6位或8位，每位字符由 0-9、a~f、A~F 组成【务必校验，错误时转码默认白色】

        :return: The font_color of this WordWaterMarkInfo.
        :rtype: str
        """
        return self._font_color

    @font_color.setter
    def font_color(self, font_color):
        r"""Sets the font_color of this WordWaterMarkInfo.

        参数校验：首位为#、除#外为6位或8位，每位字符由 0-9、a~f、A~F 组成【务必校验，错误时转码默认白色】

        :param font_color: The font_color of this WordWaterMarkInfo.
        :type font_color: str
        """
        self._font_color = font_color

    @property
    def font_size(self):
        r"""Gets the font_size of this WordWaterMarkInfo.

        字体大小

        :return: The font_size of this WordWaterMarkInfo.
        :rtype: int
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        r"""Sets the font_size of this WordWaterMarkInfo.

        字体大小

        :param font_size: The font_size of this WordWaterMarkInfo.
        :type font_size: int
        """
        self._font_size = font_size

    @property
    def font(self):
        r"""Gets the font of this WordWaterMarkInfo.

        字体，缺省值 空，可选值：harmonyRegular（鸿蒙）、douyu2.0（斗鱼追光体）

        :return: The font of this WordWaterMarkInfo.
        :rtype: str
        """
        return self._font

    @font.setter
    def font(self, font):
        r"""Sets the font of this WordWaterMarkInfo.

        字体，缺省值 空，可选值：harmonyRegular（鸿蒙）、douyu2.0（斗鱼追光体）

        :param font: The font of this WordWaterMarkInfo.
        :type font: str
        """
        self._font = font

    @property
    def time_zone(self):
        r"""Gets the time_zone of this WordWaterMarkInfo.

        时区，【取值参考 UTC-1200 至 UTC+1200，前三位UTC，第四位+或-，五六位表示小时，七八位固定00】

        :return: The time_zone of this WordWaterMarkInfo.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this WordWaterMarkInfo.

        时区，【取值参考 UTC-1200 至 UTC+1200，前三位UTC，第四位+或-，五六位表示小时，七八位固定00】

        :param time_zone: The time_zone of this WordWaterMarkInfo.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def shadow_color(self):
        r"""Gets the shadow_color of this WordWaterMarkInfo.

        缺省值 none，参数校验：首位为#、除#外为6位或8位，每位字符由 0-9、a~f、A~F 组成【务必校验，错误时转码默认黑色】

        :return: The shadow_color of this WordWaterMarkInfo.
        :rtype: str
        """
        return self._shadow_color

    @shadow_color.setter
    def shadow_color(self, shadow_color):
        r"""Sets the shadow_color of this WordWaterMarkInfo.

        缺省值 none，参数校验：首位为#、除#外为6位或8位，每位字符由 0-9、a~f、A~F 组成【务必校验，错误时转码默认黑色】

        :param shadow_color: The shadow_color of this WordWaterMarkInfo.
        :type shadow_color: str
        """
        self._shadow_color = shadow_color

    @property
    def location(self):
        r"""Gets the location of this WordWaterMarkInfo.

        :return: The location of this WordWaterMarkInfo.
        :rtype: :class:`huaweicloudsdklive.v1.WatermarkLocation`
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this WordWaterMarkInfo.

        :param location: The location of this WordWaterMarkInfo.
        :type location: :class:`huaweicloudsdklive.v1.WatermarkLocation`
        """
        self._location = location

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
        if not isinstance(other, WordWaterMarkInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
