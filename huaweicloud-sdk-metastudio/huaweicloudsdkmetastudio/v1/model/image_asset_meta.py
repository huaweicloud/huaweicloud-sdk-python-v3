# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageAssetMeta:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'codec': 'str',
        'width': 'int',
        'height': 'int',
        'size': 'int',
        'mode': 'str',
        'frame_rate': 'str',
        'duration': 'int',
        'error_info': 'ErrorResponse'
    }

    attribute_map = {
        'codec': 'codec',
        'width': 'width',
        'height': 'height',
        'size': 'size',
        'mode': 'mode',
        'frame_rate': 'frame_rate',
        'duration': 'duration',
        'error_info': 'error_info'
    }

    def __init__(self, codec=None, width=None, height=None, size=None, mode=None, frame_rate=None, duration=None, error_info=None):
        r"""ImageAssetMeta

        The model defined in huaweicloud sdk

        :param codec: **参数解释**： 图片编码格式。 **约束限制**： 用户无需填写，系统自行提取。 **取值范围**： 字符长度0-32位。 **默认取值**： 不涉及。
        :type codec: str
        :param width: **参数解释**： 图片宽度。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及。
        :type width: int
        :param height: **参数解释**： 图片高度。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及。
        :type height: int
        :param size: **参数解释**： 图片大小。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及。
        :type size: int
        :param mode: **参数解释**： 图片形态。 **约束限制**： 用户无需填写，系统自行提取。 **取值范围**： * Horizontal：横向 * Vertical：纵向  **默认取值**： 不涉及。
        :type mode: str
        :param frame_rate: **参数解释**： 视频帧率。 **约束限制**： 用户无需填写，系统自行提取。 **取值范围**： 字符长度0-32位。 **默认取值**： 不涉及
        :type frame_rate: str
        :param duration: **参数解释**： 时长,单位秒。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及
        :type duration: int
        :param error_info: 
        :type error_info: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        
        

        self._codec = None
        self._width = None
        self._height = None
        self._size = None
        self._mode = None
        self._frame_rate = None
        self._duration = None
        self._error_info = None
        self.discriminator = None

        if codec is not None:
            self.codec = codec
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if size is not None:
            self.size = size
        if mode is not None:
            self.mode = mode
        if frame_rate is not None:
            self.frame_rate = frame_rate
        if duration is not None:
            self.duration = duration
        if error_info is not None:
            self.error_info = error_info

    @property
    def codec(self):
        r"""Gets the codec of this ImageAssetMeta.

        **参数解释**： 图片编码格式。 **约束限制**： 用户无需填写，系统自行提取。 **取值范围**： 字符长度0-32位。 **默认取值**： 不涉及。

        :return: The codec of this ImageAssetMeta.
        :rtype: str
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        r"""Sets the codec of this ImageAssetMeta.

        **参数解释**： 图片编码格式。 **约束限制**： 用户无需填写，系统自行提取。 **取值范围**： 字符长度0-32位。 **默认取值**： 不涉及。

        :param codec: The codec of this ImageAssetMeta.
        :type codec: str
        """
        self._codec = codec

    @property
    def width(self):
        r"""Gets the width of this ImageAssetMeta.

        **参数解释**： 图片宽度。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及。

        :return: The width of this ImageAssetMeta.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        r"""Sets the width of this ImageAssetMeta.

        **参数解释**： 图片宽度。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及。

        :param width: The width of this ImageAssetMeta.
        :type width: int
        """
        self._width = width

    @property
    def height(self):
        r"""Gets the height of this ImageAssetMeta.

        **参数解释**： 图片高度。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及。

        :return: The height of this ImageAssetMeta.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        r"""Sets the height of this ImageAssetMeta.

        **参数解释**： 图片高度。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及。

        :param height: The height of this ImageAssetMeta.
        :type height: int
        """
        self._height = height

    @property
    def size(self):
        r"""Gets the size of this ImageAssetMeta.

        **参数解释**： 图片大小。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及。

        :return: The size of this ImageAssetMeta.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ImageAssetMeta.

        **参数解释**： 图片大小。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及。

        :param size: The size of this ImageAssetMeta.
        :type size: int
        """
        self._size = size

    @property
    def mode(self):
        r"""Gets the mode of this ImageAssetMeta.

        **参数解释**： 图片形态。 **约束限制**： 用户无需填写，系统自行提取。 **取值范围**： * Horizontal：横向 * Vertical：纵向  **默认取值**： 不涉及。

        :return: The mode of this ImageAssetMeta.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this ImageAssetMeta.

        **参数解释**： 图片形态。 **约束限制**： 用户无需填写，系统自行提取。 **取值范围**： * Horizontal：横向 * Vertical：纵向  **默认取值**： 不涉及。

        :param mode: The mode of this ImageAssetMeta.
        :type mode: str
        """
        self._mode = mode

    @property
    def frame_rate(self):
        r"""Gets the frame_rate of this ImageAssetMeta.

        **参数解释**： 视频帧率。 **约束限制**： 用户无需填写，系统自行提取。 **取值范围**： 字符长度0-32位。 **默认取值**： 不涉及

        :return: The frame_rate of this ImageAssetMeta.
        :rtype: str
        """
        return self._frame_rate

    @frame_rate.setter
    def frame_rate(self, frame_rate):
        r"""Sets the frame_rate of this ImageAssetMeta.

        **参数解释**： 视频帧率。 **约束限制**： 用户无需填写，系统自行提取。 **取值范围**： 字符长度0-32位。 **默认取值**： 不涉及

        :param frame_rate: The frame_rate of this ImageAssetMeta.
        :type frame_rate: str
        """
        self._frame_rate = frame_rate

    @property
    def duration(self):
        r"""Gets the duration of this ImageAssetMeta.

        **参数解释**： 时长,单位秒。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及

        :return: The duration of this ImageAssetMeta.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this ImageAssetMeta.

        **参数解释**： 时长,单位秒。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及

        :param duration: The duration of this ImageAssetMeta.
        :type duration: int
        """
        self._duration = duration

    @property
    def error_info(self):
        r"""Gets the error_info of this ImageAssetMeta.

        :return: The error_info of this ImageAssetMeta.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        r"""Sets the error_info of this ImageAssetMeta.

        :param error_info: The error_info of this ImageAssetMeta.
        :type error_info: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        self._error_info = error_info

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
        if not isinstance(other, ImageAssetMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
