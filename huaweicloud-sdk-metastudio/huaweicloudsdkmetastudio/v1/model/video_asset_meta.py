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
        """VideoAssetMeta

        The model defined in huaweicloud sdk

        :param video_codec: 视频编码格式
        :type video_codec: str
        :param width: 视频宽度
        :type width: int
        :param height: 视频高度
        :type height: int
        :param frame_rate: 帧率
        :type frame_rate: str
        :param video_bit_rate: 视频平均码率,单位kbps
        :type video_bit_rate: int
        :param duration: 时长,单位秒
        :type duration: int
        :param audio_codec: 音频编码格式
        :type audio_codec: str
        :param audio_bit_rate: 音频平均码率,单位kbps
        :type audio_bit_rate: int
        :param audio_channels: 音频声道数
        :type audio_channels: int
        :param sample: 采样率,HZ
        :type sample: int
        :param mode: Horizontal&#x3D;横向；Vertical&#x3D;纵向
        :type mode: str
        :param video_transcoding_status: 视频转码状态。 * WAITING：等待 * TRANSCODING：转码中 * FAILED：失败 * SUCCEEDED：成功
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
        """Gets the video_codec of this VideoAssetMeta.

        视频编码格式

        :return: The video_codec of this VideoAssetMeta.
        :rtype: str
        """
        return self._video_codec

    @video_codec.setter
    def video_codec(self, video_codec):
        """Sets the video_codec of this VideoAssetMeta.

        视频编码格式

        :param video_codec: The video_codec of this VideoAssetMeta.
        :type video_codec: str
        """
        self._video_codec = video_codec

    @property
    def width(self):
        """Gets the width of this VideoAssetMeta.

        视频宽度

        :return: The width of this VideoAssetMeta.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this VideoAssetMeta.

        视频宽度

        :param width: The width of this VideoAssetMeta.
        :type width: int
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this VideoAssetMeta.

        视频高度

        :return: The height of this VideoAssetMeta.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this VideoAssetMeta.

        视频高度

        :param height: The height of this VideoAssetMeta.
        :type height: int
        """
        self._height = height

    @property
    def frame_rate(self):
        """Gets the frame_rate of this VideoAssetMeta.

        帧率

        :return: The frame_rate of this VideoAssetMeta.
        :rtype: str
        """
        return self._frame_rate

    @frame_rate.setter
    def frame_rate(self, frame_rate):
        """Sets the frame_rate of this VideoAssetMeta.

        帧率

        :param frame_rate: The frame_rate of this VideoAssetMeta.
        :type frame_rate: str
        """
        self._frame_rate = frame_rate

    @property
    def video_bit_rate(self):
        """Gets the video_bit_rate of this VideoAssetMeta.

        视频平均码率,单位kbps

        :return: The video_bit_rate of this VideoAssetMeta.
        :rtype: int
        """
        return self._video_bit_rate

    @video_bit_rate.setter
    def video_bit_rate(self, video_bit_rate):
        """Sets the video_bit_rate of this VideoAssetMeta.

        视频平均码率,单位kbps

        :param video_bit_rate: The video_bit_rate of this VideoAssetMeta.
        :type video_bit_rate: int
        """
        self._video_bit_rate = video_bit_rate

    @property
    def duration(self):
        """Gets the duration of this VideoAssetMeta.

        时长,单位秒

        :return: The duration of this VideoAssetMeta.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this VideoAssetMeta.

        时长,单位秒

        :param duration: The duration of this VideoAssetMeta.
        :type duration: int
        """
        self._duration = duration

    @property
    def audio_codec(self):
        """Gets the audio_codec of this VideoAssetMeta.

        音频编码格式

        :return: The audio_codec of this VideoAssetMeta.
        :rtype: str
        """
        return self._audio_codec

    @audio_codec.setter
    def audio_codec(self, audio_codec):
        """Sets the audio_codec of this VideoAssetMeta.

        音频编码格式

        :param audio_codec: The audio_codec of this VideoAssetMeta.
        :type audio_codec: str
        """
        self._audio_codec = audio_codec

    @property
    def audio_bit_rate(self):
        """Gets the audio_bit_rate of this VideoAssetMeta.

        音频平均码率,单位kbps

        :return: The audio_bit_rate of this VideoAssetMeta.
        :rtype: int
        """
        return self._audio_bit_rate

    @audio_bit_rate.setter
    def audio_bit_rate(self, audio_bit_rate):
        """Sets the audio_bit_rate of this VideoAssetMeta.

        音频平均码率,单位kbps

        :param audio_bit_rate: The audio_bit_rate of this VideoAssetMeta.
        :type audio_bit_rate: int
        """
        self._audio_bit_rate = audio_bit_rate

    @property
    def audio_channels(self):
        """Gets the audio_channels of this VideoAssetMeta.

        音频声道数

        :return: The audio_channels of this VideoAssetMeta.
        :rtype: int
        """
        return self._audio_channels

    @audio_channels.setter
    def audio_channels(self, audio_channels):
        """Sets the audio_channels of this VideoAssetMeta.

        音频声道数

        :param audio_channels: The audio_channels of this VideoAssetMeta.
        :type audio_channels: int
        """
        self._audio_channels = audio_channels

    @property
    def sample(self):
        """Gets the sample of this VideoAssetMeta.

        采样率,HZ

        :return: The sample of this VideoAssetMeta.
        :rtype: int
        """
        return self._sample

    @sample.setter
    def sample(self, sample):
        """Sets the sample of this VideoAssetMeta.

        采样率,HZ

        :param sample: The sample of this VideoAssetMeta.
        :type sample: int
        """
        self._sample = sample

    @property
    def mode(self):
        """Gets the mode of this VideoAssetMeta.

        Horizontal=横向；Vertical=纵向

        :return: The mode of this VideoAssetMeta.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this VideoAssetMeta.

        Horizontal=横向；Vertical=纵向

        :param mode: The mode of this VideoAssetMeta.
        :type mode: str
        """
        self._mode = mode

    @property
    def video_transcoding_status(self):
        """Gets the video_transcoding_status of this VideoAssetMeta.

        视频转码状态。 * WAITING：等待 * TRANSCODING：转码中 * FAILED：失败 * SUCCEEDED：成功

        :return: The video_transcoding_status of this VideoAssetMeta.
        :rtype: str
        """
        return self._video_transcoding_status

    @video_transcoding_status.setter
    def video_transcoding_status(self, video_transcoding_status):
        """Sets the video_transcoding_status of this VideoAssetMeta.

        视频转码状态。 * WAITING：等待 * TRANSCODING：转码中 * FAILED：失败 * SUCCEEDED：成功

        :param video_transcoding_status: The video_transcoding_status of this VideoAssetMeta.
        :type video_transcoding_status: str
        """
        self._video_transcoding_status = video_transcoding_status

    @property
    def error_info(self):
        """Gets the error_info of this VideoAssetMeta.

        :return: The error_info of this VideoAssetMeta.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        """Sets the error_info of this VideoAssetMeta.

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
