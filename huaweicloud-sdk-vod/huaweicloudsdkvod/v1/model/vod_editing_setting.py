# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VodEditingSetting:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resolution_adaptation': 'bool',
        'resolution_upsample': 'bool',
        'format': 'str',
        'width': 'int',
        'height': 'int',
        'reference': 'str',
        'video_codec': 'int'
    }

    attribute_map = {
        'resolution_adaptation': 'resolution_adaptation',
        'resolution_upsample': 'resolution_upsample',
        'format': 'format',
        'width': 'width',
        'height': 'height',
        'reference': 'reference',
        'video_codec': 'video_codec'
    }

    def __init__(self, resolution_adaptation=None, resolution_upsample=None, format=None, width=None, height=None, reference=None, video_codec=None):
        r"""VodEditingSetting

        The model defined in huaweicloud sdk

        :param resolution_adaptation: 分辨率自适应策略, 选值：true, false（默认true） 输入为true时，width表示长边，height表示短边 输入为false时，width表示宽度，height表示长度 
        :type resolution_adaptation: bool
        :param resolution_upsample: 分辨率上采样开关, 选值：true, false（默认false），若为false则按照原片源输出，分辨率不会上浮。 
        :type resolution_upsample: bool
        :param format: 输出封装格式，HLS、MP4（默认MP4）、MP3、MOV、FLV、AVI。 不支持将视频文件输出成音频封装格式。 
        :type format: str
        :param width: 输出宽或长边，整型，输入小数向下取整，默认0，按源  - 当width、height均为0，则分辨率取片源分辨率； - 当width为0，height非0，则width按片源分辨率比例缩放； - 当width非0，height为0，则height按片源分辨率比例缩放； - 当width、height均非0，则分辨率按用户指定。 - 当视频编码为H.264时，则width最小值为32，最大值为4096。 - 当视频编码为H.265，则width最小值为160，最大值为4096。 
        :type width: int
        :param height: 输出高或短边，整型，输入小数向下取整，默认0，按源  - 当Width、Height均为0，则分辨率取片源分辨率； - 当Width为0，Height非0，则Width按片源分辨率比例缩放； - 当Width非0，Height为0，则Height按片源分辨率比例缩放； - 当Width、Height 均非0，则分辨率按用户指定。 - 当视频编码为H.264时，则height最小值为32，最大值为2880。 - 当视频编码为H.265，则height最小值为160，最大值为2880。 
        :type height: int
        :param reference: 输出参考基准，可选，默认为NONE  - NONE 输出分辨率按输入的第一个片源为主，码率按输出分辨率自适应 - MAX_BITRATE 按码率最大的输入片源参数为基准 - MAX_RESOLUTION 按分辨率最大的输入片源参数为基准 
        :type reference: str
        :param video_codec: 视频编码格式。 取值如下： - 1：VIDEO_CODEC_H264 - 2：VIDEO_CODEC_H265 
        :type video_codec: int
        """
        
        

        self._resolution_adaptation = None
        self._resolution_upsample = None
        self._format = None
        self._width = None
        self._height = None
        self._reference = None
        self._video_codec = None
        self.discriminator = None

        if resolution_adaptation is not None:
            self.resolution_adaptation = resolution_adaptation
        if resolution_upsample is not None:
            self.resolution_upsample = resolution_upsample
        if format is not None:
            self.format = format
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if reference is not None:
            self.reference = reference
        if video_codec is not None:
            self.video_codec = video_codec

    @property
    def resolution_adaptation(self):
        r"""Gets the resolution_adaptation of this VodEditingSetting.

        分辨率自适应策略, 选值：true, false（默认true） 输入为true时，width表示长边，height表示短边 输入为false时，width表示宽度，height表示长度 

        :return: The resolution_adaptation of this VodEditingSetting.
        :rtype: bool
        """
        return self._resolution_adaptation

    @resolution_adaptation.setter
    def resolution_adaptation(self, resolution_adaptation):
        r"""Sets the resolution_adaptation of this VodEditingSetting.

        分辨率自适应策略, 选值：true, false（默认true） 输入为true时，width表示长边，height表示短边 输入为false时，width表示宽度，height表示长度 

        :param resolution_adaptation: The resolution_adaptation of this VodEditingSetting.
        :type resolution_adaptation: bool
        """
        self._resolution_adaptation = resolution_adaptation

    @property
    def resolution_upsample(self):
        r"""Gets the resolution_upsample of this VodEditingSetting.

        分辨率上采样开关, 选值：true, false（默认false），若为false则按照原片源输出，分辨率不会上浮。 

        :return: The resolution_upsample of this VodEditingSetting.
        :rtype: bool
        """
        return self._resolution_upsample

    @resolution_upsample.setter
    def resolution_upsample(self, resolution_upsample):
        r"""Sets the resolution_upsample of this VodEditingSetting.

        分辨率上采样开关, 选值：true, false（默认false），若为false则按照原片源输出，分辨率不会上浮。 

        :param resolution_upsample: The resolution_upsample of this VodEditingSetting.
        :type resolution_upsample: bool
        """
        self._resolution_upsample = resolution_upsample

    @property
    def format(self):
        r"""Gets the format of this VodEditingSetting.

        输出封装格式，HLS、MP4（默认MP4）、MP3、MOV、FLV、AVI。 不支持将视频文件输出成音频封装格式。 

        :return: The format of this VodEditingSetting.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this VodEditingSetting.

        输出封装格式，HLS、MP4（默认MP4）、MP3、MOV、FLV、AVI。 不支持将视频文件输出成音频封装格式。 

        :param format: The format of this VodEditingSetting.
        :type format: str
        """
        self._format = format

    @property
    def width(self):
        r"""Gets the width of this VodEditingSetting.

        输出宽或长边，整型，输入小数向下取整，默认0，按源  - 当width、height均为0，则分辨率取片源分辨率； - 当width为0，height非0，则width按片源分辨率比例缩放； - 当width非0，height为0，则height按片源分辨率比例缩放； - 当width、height均非0，则分辨率按用户指定。 - 当视频编码为H.264时，则width最小值为32，最大值为4096。 - 当视频编码为H.265，则width最小值为160，最大值为4096。 

        :return: The width of this VodEditingSetting.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        r"""Sets the width of this VodEditingSetting.

        输出宽或长边，整型，输入小数向下取整，默认0，按源  - 当width、height均为0，则分辨率取片源分辨率； - 当width为0，height非0，则width按片源分辨率比例缩放； - 当width非0，height为0，则height按片源分辨率比例缩放； - 当width、height均非0，则分辨率按用户指定。 - 当视频编码为H.264时，则width最小值为32，最大值为4096。 - 当视频编码为H.265，则width最小值为160，最大值为4096。 

        :param width: The width of this VodEditingSetting.
        :type width: int
        """
        self._width = width

    @property
    def height(self):
        r"""Gets the height of this VodEditingSetting.

        输出高或短边，整型，输入小数向下取整，默认0，按源  - 当Width、Height均为0，则分辨率取片源分辨率； - 当Width为0，Height非0，则Width按片源分辨率比例缩放； - 当Width非0，Height为0，则Height按片源分辨率比例缩放； - 当Width、Height 均非0，则分辨率按用户指定。 - 当视频编码为H.264时，则height最小值为32，最大值为2880。 - 当视频编码为H.265，则height最小值为160，最大值为2880。 

        :return: The height of this VodEditingSetting.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        r"""Sets the height of this VodEditingSetting.

        输出高或短边，整型，输入小数向下取整，默认0，按源  - 当Width、Height均为0，则分辨率取片源分辨率； - 当Width为0，Height非0，则Width按片源分辨率比例缩放； - 当Width非0，Height为0，则Height按片源分辨率比例缩放； - 当Width、Height 均非0，则分辨率按用户指定。 - 当视频编码为H.264时，则height最小值为32，最大值为2880。 - 当视频编码为H.265，则height最小值为160，最大值为2880。 

        :param height: The height of this VodEditingSetting.
        :type height: int
        """
        self._height = height

    @property
    def reference(self):
        r"""Gets the reference of this VodEditingSetting.

        输出参考基准，可选，默认为NONE  - NONE 输出分辨率按输入的第一个片源为主，码率按输出分辨率自适应 - MAX_BITRATE 按码率最大的输入片源参数为基准 - MAX_RESOLUTION 按分辨率最大的输入片源参数为基准 

        :return: The reference of this VodEditingSetting.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        r"""Sets the reference of this VodEditingSetting.

        输出参考基准，可选，默认为NONE  - NONE 输出分辨率按输入的第一个片源为主，码率按输出分辨率自适应 - MAX_BITRATE 按码率最大的输入片源参数为基准 - MAX_RESOLUTION 按分辨率最大的输入片源参数为基准 

        :param reference: The reference of this VodEditingSetting.
        :type reference: str
        """
        self._reference = reference

    @property
    def video_codec(self):
        r"""Gets the video_codec of this VodEditingSetting.

        视频编码格式。 取值如下： - 1：VIDEO_CODEC_H264 - 2：VIDEO_CODEC_H265 

        :return: The video_codec of this VodEditingSetting.
        :rtype: int
        """
        return self._video_codec

    @video_codec.setter
    def video_codec(self, video_codec):
        r"""Sets the video_codec of this VodEditingSetting.

        视频编码格式。 取值如下： - 1：VIDEO_CODEC_H264 - 2：VIDEO_CODEC_H265 

        :param video_codec: The video_codec of this VodEditingSetting.
        :type video_codec: int
        """
        self._video_codec = video_codec

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
        if not isinstance(other, VodEditingSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
