# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WatermarkLocation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'location': 'str',
        'x_offset': 'float',
        'y_offset': 'float'
    }

    attribute_map = {
        'location': 'location',
        'x_offset': 'x_offset',
        'y_offset': 'y_offset'
    }

    def __init__(self, location=None, x_offset=None, y_offset=None):
        r"""WatermarkLocation

        The model defined in huaweicloud sdk

        :param location: 水印位置。  包含如下选项： - TOPLEFT：左上 - TOPRIGHT：右上 - BOTTOMLEFT：左下 - BOTTOMRIGHT：右下 - RANDOM：随机模式，图片水印将随机在视频流的左上、右上、左下、右下四个位置展示。
        :type location: str
        :param x_offset: 水印相对输出视频的水平偏移量。 说明：值有两种形式： 1）整数型代表偏移像素，范围[1，4096]，单位px。 2）小数型代表水平偏移量与输出分辨率宽的比率，范围[0，1) 百分比限制最多保留小数点后4位
        :type x_offset: float
        :param y_offset: 水印相对输出视频的垂直偏移量 说明: 值有两种形式： 1）整数型代表偏移像素，范围[1，4096]，单位px。 2）小数型代表垂直偏移量与输出分辨率高的比率，范围[0，1) 百分比限制最多保留小数点后4位
        :type y_offset: float
        """
        
        

        self._location = None
        self._x_offset = None
        self._y_offset = None
        self.discriminator = None

        if location is not None:
            self.location = location
        if x_offset is not None:
            self.x_offset = x_offset
        if y_offset is not None:
            self.y_offset = y_offset

    @property
    def location(self):
        r"""Gets the location of this WatermarkLocation.

        水印位置。  包含如下选项： - TOPLEFT：左上 - TOPRIGHT：右上 - BOTTOMLEFT：左下 - BOTTOMRIGHT：右下 - RANDOM：随机模式，图片水印将随机在视频流的左上、右上、左下、右下四个位置展示。

        :return: The location of this WatermarkLocation.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this WatermarkLocation.

        水印位置。  包含如下选项： - TOPLEFT：左上 - TOPRIGHT：右上 - BOTTOMLEFT：左下 - BOTTOMRIGHT：右下 - RANDOM：随机模式，图片水印将随机在视频流的左上、右上、左下、右下四个位置展示。

        :param location: The location of this WatermarkLocation.
        :type location: str
        """
        self._location = location

    @property
    def x_offset(self):
        r"""Gets the x_offset of this WatermarkLocation.

        水印相对输出视频的水平偏移量。 说明：值有两种形式： 1）整数型代表偏移像素，范围[1，4096]，单位px。 2）小数型代表水平偏移量与输出分辨率宽的比率，范围[0，1) 百分比限制最多保留小数点后4位

        :return: The x_offset of this WatermarkLocation.
        :rtype: float
        """
        return self._x_offset

    @x_offset.setter
    def x_offset(self, x_offset):
        r"""Sets the x_offset of this WatermarkLocation.

        水印相对输出视频的水平偏移量。 说明：值有两种形式： 1）整数型代表偏移像素，范围[1，4096]，单位px。 2）小数型代表水平偏移量与输出分辨率宽的比率，范围[0，1) 百分比限制最多保留小数点后4位

        :param x_offset: The x_offset of this WatermarkLocation.
        :type x_offset: float
        """
        self._x_offset = x_offset

    @property
    def y_offset(self):
        r"""Gets the y_offset of this WatermarkLocation.

        水印相对输出视频的垂直偏移量 说明: 值有两种形式： 1）整数型代表偏移像素，范围[1，4096]，单位px。 2）小数型代表垂直偏移量与输出分辨率高的比率，范围[0，1) 百分比限制最多保留小数点后4位

        :return: The y_offset of this WatermarkLocation.
        :rtype: float
        """
        return self._y_offset

    @y_offset.setter
    def y_offset(self, y_offset):
        r"""Sets the y_offset of this WatermarkLocation.

        水印相对输出视频的垂直偏移量 说明: 值有两种形式： 1）整数型代表偏移像素，范围[1，4096]，单位px。 2）小数型代表垂直偏移量与输出分辨率高的比率，范围[0，1) 百分比限制最多保留小数点后4位

        :param y_offset: The y_offset of this WatermarkLocation.
        :type y_offset: float
        """
        self._y_offset = y_offset

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
        if not isinstance(other, WatermarkLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
