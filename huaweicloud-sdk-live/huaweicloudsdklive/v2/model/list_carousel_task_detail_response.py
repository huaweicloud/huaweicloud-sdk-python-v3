# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCarouselTaskDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'end_time': 'str',
        'video_framerate_list': 'list[int]',
        'video_bitrate_list': 'list[int]',
        'audio_framerate_list': 'list[int]',
        'audio_bitrate_list': 'list[int]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'video_framerate_list': 'video_framerate_list',
        'video_bitrate_list': 'video_bitrate_list',
        'audio_framerate_list': 'audio_framerate_list',
        'audio_bitrate_list': 'audio_bitrate_list',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, start_time=None, end_time=None, video_framerate_list=None, video_bitrate_list=None, audio_framerate_list=None, audio_bitrate_list=None, x_request_id=None):
        r"""ListCarouselTaskDetailResponse

        The model defined in huaweicloud sdk

        :param start_time: 采样开始时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。
        :type start_time: str
        :param end_time: 采样结束时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。
        :type end_time: str
        :param video_framerate_list: 视频帧率信息列表，单位为fps。
        :type video_framerate_list: list[int]
        :param video_bitrate_list: 视频码率信息列表，单位为kbps。
        :type video_bitrate_list: list[int]
        :param audio_framerate_list: 音频帧率信息列表，单位为fps。
        :type audio_framerate_list: list[int]
        :param audio_bitrate_list: 音频码率信息列表，单位为kbps。
        :type audio_bitrate_list: list[int]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._start_time = None
        self._end_time = None
        self._video_framerate_list = None
        self._video_bitrate_list = None
        self._audio_framerate_list = None
        self._audio_bitrate_list = None
        self._x_request_id = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if video_framerate_list is not None:
            self.video_framerate_list = video_framerate_list
        if video_bitrate_list is not None:
            self.video_bitrate_list = video_bitrate_list
        if audio_framerate_list is not None:
            self.audio_framerate_list = audio_framerate_list
        if audio_bitrate_list is not None:
            self.audio_bitrate_list = audio_bitrate_list
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ListCarouselTaskDetailResponse.

        采样开始时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。

        :return: The start_time of this ListCarouselTaskDetailResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListCarouselTaskDetailResponse.

        采样开始时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。

        :param start_time: The start_time of this ListCarouselTaskDetailResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListCarouselTaskDetailResponse.

        采样结束时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。

        :return: The end_time of this ListCarouselTaskDetailResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListCarouselTaskDetailResponse.

        采样结束时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。

        :param end_time: The end_time of this ListCarouselTaskDetailResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def video_framerate_list(self):
        r"""Gets the video_framerate_list of this ListCarouselTaskDetailResponse.

        视频帧率信息列表，单位为fps。

        :return: The video_framerate_list of this ListCarouselTaskDetailResponse.
        :rtype: list[int]
        """
        return self._video_framerate_list

    @video_framerate_list.setter
    def video_framerate_list(self, video_framerate_list):
        r"""Sets the video_framerate_list of this ListCarouselTaskDetailResponse.

        视频帧率信息列表，单位为fps。

        :param video_framerate_list: The video_framerate_list of this ListCarouselTaskDetailResponse.
        :type video_framerate_list: list[int]
        """
        self._video_framerate_list = video_framerate_list

    @property
    def video_bitrate_list(self):
        r"""Gets the video_bitrate_list of this ListCarouselTaskDetailResponse.

        视频码率信息列表，单位为kbps。

        :return: The video_bitrate_list of this ListCarouselTaskDetailResponse.
        :rtype: list[int]
        """
        return self._video_bitrate_list

    @video_bitrate_list.setter
    def video_bitrate_list(self, video_bitrate_list):
        r"""Sets the video_bitrate_list of this ListCarouselTaskDetailResponse.

        视频码率信息列表，单位为kbps。

        :param video_bitrate_list: The video_bitrate_list of this ListCarouselTaskDetailResponse.
        :type video_bitrate_list: list[int]
        """
        self._video_bitrate_list = video_bitrate_list

    @property
    def audio_framerate_list(self):
        r"""Gets the audio_framerate_list of this ListCarouselTaskDetailResponse.

        音频帧率信息列表，单位为fps。

        :return: The audio_framerate_list of this ListCarouselTaskDetailResponse.
        :rtype: list[int]
        """
        return self._audio_framerate_list

    @audio_framerate_list.setter
    def audio_framerate_list(self, audio_framerate_list):
        r"""Sets the audio_framerate_list of this ListCarouselTaskDetailResponse.

        音频帧率信息列表，单位为fps。

        :param audio_framerate_list: The audio_framerate_list of this ListCarouselTaskDetailResponse.
        :type audio_framerate_list: list[int]
        """
        self._audio_framerate_list = audio_framerate_list

    @property
    def audio_bitrate_list(self):
        r"""Gets the audio_bitrate_list of this ListCarouselTaskDetailResponse.

        音频码率信息列表，单位为kbps。

        :return: The audio_bitrate_list of this ListCarouselTaskDetailResponse.
        :rtype: list[int]
        """
        return self._audio_bitrate_list

    @audio_bitrate_list.setter
    def audio_bitrate_list(self, audio_bitrate_list):
        r"""Sets the audio_bitrate_list of this ListCarouselTaskDetailResponse.

        音频码率信息列表，单位为kbps。

        :param audio_bitrate_list: The audio_bitrate_list of this ListCarouselTaskDetailResponse.
        :type audio_bitrate_list: list[int]
        """
        self._audio_bitrate_list = audio_bitrate_list

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListCarouselTaskDetailResponse.

        :return: The x_request_id of this ListCarouselTaskDetailResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListCarouselTaskDetailResponse.

        :param x_request_id: The x_request_id of this ListCarouselTaskDetailResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ListCarouselTaskDetailResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListCarouselTaskDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
