# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoAssetMeta:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'video_codec': 'str',
        'width': 'int',
        'height': 'int',
        'frame_rate': 'str',
        'video_bit_rate': 'int',
        'duration': 'int',
        'audio_codec': 'str',
        'audio_bit_rate': 'int',
        'audio_channels': 'int',
        'sample': 'int',
        'mode': 'str',
        'video_transcoding_status': 'str',
        'error_info': 'ErrorResponse'
    }

    attribute_map = {
        'video_codec': 'video_codec',
        'width': 'width',
        'height': 'height',
        'frame_rate': 'frame_rate',
        'video_bit_rate': 'video_bit_rate',
        'duration': 'duration',
        'audio_codec': 'audio_codec',
        'audio_bit_rate': 'audio_bit_rate',
        'audio_channels': 'audio_channels',
        'sample': 'sample',
        'mode': 'mode',
        'video_transcoding_status': 'video_transcoding_status',
        'error_info': 'error_info'
    }

    def __init__(self, video_codec=None, width=None, height=None, frame_rate=None, video_bit_rate=None, duration=None, audio_codec=None, audio_bit_rate=None, audio_channels=None, sample=None, mode=None, video_transcoding_status=None, error_info=None):
        r"""VideoAssetMeta

        The model defined in huaweicloud sdk

        :param video_codec: **参数解释**： 视频编码格式。 **约束限制**： 用户无需填写，系统自行提取。 **取值范围**： 字符长度0-32位。 **默认取值**： 不涉及
        :type video_codec: str
        :param width: **参数解释**： 视频画面宽度。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及
        :type width: int
        :param height: **参数解释**： 视频画面高度。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及
        :type height: int
        :param frame_rate: **参数解释**： 视频帧率。 **约束限制**： 用户无需填写，系统自行提取。 **取值范围**： 字符长度0-32位。 **默认取值**： 不涉及
        :type frame_rate: str
        :param video_bit_rate: **参数解释**： 视频平均码率,单位kbps。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及
        :type video_bit_rate: int
        :param duration: **参数解释**： 时长,单位秒。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及
        :type duration: int
        :param audio_codec: **参数解释**： 音频编码格式。 **约束限制**： 用户无需填写，系统自行提取。 **取值范围**： 字符长度0-32位。 **默认取值**： 不涉及
        :type audio_codec: str
        :param audio_bit_rate: **参数解释**： 音频平均码率,单位kbps。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及
        :type audio_bit_rate: int
        :param audio_channels: **参数解释**： 音频声道数。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及
        :type audio_channels: int
        :param sample: **参数解释**： 采样率,HZ。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及
        :type sample: int
        :param mode: **参数解释**： 横向画面或纵向画面。 **约束限制**： 用户无需填写，系统自行提取。 **取值范围**： * Horizontal：横向 * Vertical：纵向  **默认取值**： 不涉及
        :type mode: str
        :param video_transcoding_status: **参数解释**： 视频转码状态。 **约束限制**： 用户无需填写，系统自行填写。 **取值范围**： * WAITING：等待 * TRANSCODING：转码中 * FAILED：失败 * SUCCEEDED：成功  **默认取值**： 不涉及
        :type video_transcoding_status: str
        :param error_info: 
        :type error_info: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        
        

        self._video_codec = None
        self._width = None
        self._height = None
        self._frame_rate = None
        self._video_bit_rate = None
        self._duration = None
        self._audio_codec = None
        self._audio_bit_rate = None
        self._audio_channels = None
        self._sample = None
        self._mode = None
        self._video_transcoding_status = None
        self._error_info = None
        self.discriminator = None

        if video_codec is not None:
            self.video_codec = video_codec
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if frame_rate is not None:
            self.frame_rate = frame_rate
        if video_bit_rate is not None:
            self.video_bit_rate = video_bit_rate
        if duration is not None:
            self.duration = duration
        if audio_codec is not None:
            self.audio_codec = audio_codec
        if audio_bit_rate is not None:
            self.audio_bit_rate = audio_bit_rate
        if audio_channels is not None:
            self.audio_channels = audio_channels
        if sample is not None:
            self.sample = sample
        if mode is not None:
            self.mode = mode
        if video_transcoding_status is not None:
            self.video_transcoding_status = video_transcoding_status
        if error_info is not None:
            self.error_info = error_info

    @property
    def video_codec(self):
        r"""Gets the video_codec of this VideoAssetMeta.

        **参数解释**： 视频编码格式。 **约束限制**： 用户无需填写，系统自行提取。 **取值范围**： 字符长度0-32位。 **默认取值**： 不涉及

        :return: The video_codec of this VideoAssetMeta.
        :rtype: str
        """
        return self._video_codec

    @video_codec.setter
    def video_codec(self, video_codec):
        r"""Sets the video_codec of this VideoAssetMeta.

        **参数解释**： 视频编码格式。 **约束限制**： 用户无需填写，系统自行提取。 **取值范围**： 字符长度0-32位。 **默认取值**： 不涉及

        :param video_codec: The video_codec of this VideoAssetMeta.
        :type video_codec: str
        """
        self._video_codec = video_codec

    @property
    def width(self):
        r"""Gets the width of this VideoAssetMeta.

        **参数解释**： 视频画面宽度。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及

        :return: The width of this VideoAssetMeta.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        r"""Sets the width of this VideoAssetMeta.

        **参数解释**： 视频画面宽度。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及

        :param width: The width of this VideoAssetMeta.
        :type width: int
        """
        self._width = width

    @property
    def height(self):
        r"""Gets the height of this VideoAssetMeta.

        **参数解释**： 视频画面高度。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及

        :return: The height of this VideoAssetMeta.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        r"""Sets the height of this VideoAssetMeta.

        **参数解释**： 视频画面高度。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及

        :param height: The height of this VideoAssetMeta.
        :type height: int
        """
        self._height = height

    @property
    def frame_rate(self):
        r"""Gets the frame_rate of this VideoAssetMeta.

        **参数解释**： 视频帧率。 **约束限制**： 用户无需填写，系统自行提取。 **取值范围**： 字符长度0-32位。 **默认取值**： 不涉及

        :return: The frame_rate of this VideoAssetMeta.
        :rtype: str
        """
        return self._frame_rate

    @frame_rate.setter
    def frame_rate(self, frame_rate):
        r"""Sets the frame_rate of this VideoAssetMeta.

        **参数解释**： 视频帧率。 **约束限制**： 用户无需填写，系统自行提取。 **取值范围**： 字符长度0-32位。 **默认取值**： 不涉及

        :param frame_rate: The frame_rate of this VideoAssetMeta.
        :type frame_rate: str
        """
        self._frame_rate = frame_rate

    @property
    def video_bit_rate(self):
        r"""Gets the video_bit_rate of this VideoAssetMeta.

        **参数解释**： 视频平均码率,单位kbps。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及

        :return: The video_bit_rate of this VideoAssetMeta.
        :rtype: int
        """
        return self._video_bit_rate

    @video_bit_rate.setter
    def video_bit_rate(self, video_bit_rate):
        r"""Sets the video_bit_rate of this VideoAssetMeta.

        **参数解释**： 视频平均码率,单位kbps。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及

        :param video_bit_rate: The video_bit_rate of this VideoAssetMeta.
        :type video_bit_rate: int
        """
        self._video_bit_rate = video_bit_rate

    @property
    def duration(self):
        r"""Gets the duration of this VideoAssetMeta.

        **参数解释**： 时长,单位秒。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及

        :return: The duration of this VideoAssetMeta.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this VideoAssetMeta.

        **参数解释**： 时长,单位秒。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及

        :param duration: The duration of this VideoAssetMeta.
        :type duration: int
        """
        self._duration = duration

    @property
    def audio_codec(self):
        r"""Gets the audio_codec of this VideoAssetMeta.

        **参数解释**： 音频编码格式。 **约束限制**： 用户无需填写，系统自行提取。 **取值范围**： 字符长度0-32位。 **默认取值**： 不涉及

        :return: The audio_codec of this VideoAssetMeta.
        :rtype: str
        """
        return self._audio_codec

    @audio_codec.setter
    def audio_codec(self, audio_codec):
        r"""Sets the audio_codec of this VideoAssetMeta.

        **参数解释**： 音频编码格式。 **约束限制**： 用户无需填写，系统自行提取。 **取值范围**： 字符长度0-32位。 **默认取值**： 不涉及

        :param audio_codec: The audio_codec of this VideoAssetMeta.
        :type audio_codec: str
        """
        self._audio_codec = audio_codec

    @property
    def audio_bit_rate(self):
        r"""Gets the audio_bit_rate of this VideoAssetMeta.

        **参数解释**： 音频平均码率,单位kbps。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及

        :return: The audio_bit_rate of this VideoAssetMeta.
        :rtype: int
        """
        return self._audio_bit_rate

    @audio_bit_rate.setter
    def audio_bit_rate(self, audio_bit_rate):
        r"""Sets the audio_bit_rate of this VideoAssetMeta.

        **参数解释**： 音频平均码率,单位kbps。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及

        :param audio_bit_rate: The audio_bit_rate of this VideoAssetMeta.
        :type audio_bit_rate: int
        """
        self._audio_bit_rate = audio_bit_rate

    @property
    def audio_channels(self):
        r"""Gets the audio_channels of this VideoAssetMeta.

        **参数解释**： 音频声道数。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及

        :return: The audio_channels of this VideoAssetMeta.
        :rtype: int
        """
        return self._audio_channels

    @audio_channels.setter
    def audio_channels(self, audio_channels):
        r"""Sets the audio_channels of this VideoAssetMeta.

        **参数解释**： 音频声道数。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及

        :param audio_channels: The audio_channels of this VideoAssetMeta.
        :type audio_channels: int
        """
        self._audio_channels = audio_channels

    @property
    def sample(self):
        r"""Gets the sample of this VideoAssetMeta.

        **参数解释**： 采样率,HZ。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及

        :return: The sample of this VideoAssetMeta.
        :rtype: int
        """
        return self._sample

    @sample.setter
    def sample(self, sample):
        r"""Sets the sample of this VideoAssetMeta.

        **参数解释**： 采样率,HZ。 **约束限制**： 用户无需填写，系统自行提取。 **默认取值**： 不涉及

        :param sample: The sample of this VideoAssetMeta.
        :type sample: int
        """
        self._sample = sample

    @property
    def mode(self):
        r"""Gets the mode of this VideoAssetMeta.

        **参数解释**： 横向画面或纵向画面。 **约束限制**： 用户无需填写，系统自行提取。 **取值范围**： * Horizontal：横向 * Vertical：纵向  **默认取值**： 不涉及

        :return: The mode of this VideoAssetMeta.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this VideoAssetMeta.

        **参数解释**： 横向画面或纵向画面。 **约束限制**： 用户无需填写，系统自行提取。 **取值范围**： * Horizontal：横向 * Vertical：纵向  **默认取值**： 不涉及

        :param mode: The mode of this VideoAssetMeta.
        :type mode: str
        """
        self._mode = mode

    @property
    def video_transcoding_status(self):
        r"""Gets the video_transcoding_status of this VideoAssetMeta.

        **参数解释**： 视频转码状态。 **约束限制**： 用户无需填写，系统自行填写。 **取值范围**： * WAITING：等待 * TRANSCODING：转码中 * FAILED：失败 * SUCCEEDED：成功  **默认取值**： 不涉及

        :return: The video_transcoding_status of this VideoAssetMeta.
        :rtype: str
        """
        return self._video_transcoding_status

    @video_transcoding_status.setter
    def video_transcoding_status(self, video_transcoding_status):
        r"""Sets the video_transcoding_status of this VideoAssetMeta.

        **参数解释**： 视频转码状态。 **约束限制**： 用户无需填写，系统自行填写。 **取值范围**： * WAITING：等待 * TRANSCODING：转码中 * FAILED：失败 * SUCCEEDED：成功  **默认取值**： 不涉及

        :param video_transcoding_status: The video_transcoding_status of this VideoAssetMeta.
        :type video_transcoding_status: str
        """
        self._video_transcoding_status = video_transcoding_status

    @property
    def error_info(self):
        r"""Gets the error_info of this VideoAssetMeta.

        :return: The error_info of this VideoAssetMeta.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        r"""Sets the error_info of this VideoAssetMeta.

        :param error_info: The error_info of this VideoAssetMeta.
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
        if not isinstance(other, VideoAssetMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
