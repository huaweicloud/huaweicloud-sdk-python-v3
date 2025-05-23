# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSmartChatJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'state': 'str',
        'duration': 'float',
        'start_time': 'str',
        'end_time': 'str',
        'error_info': 'ErrorResponse',
        'create_time': 'str',
        'lastupdate_time': 'str',
        'rtc_room_info': 'RTCRoomInfoList',
        'chat_subtitle_config': 'SmartChatSubtitleConfig',
        'video_config': 'SmartChatVideoConfig',
        'voice_config_list': 'list[SmartChatVoiceConfig]',
        'chat_state': 'int',
        'language': 'LanguageEnum',
        'chat_video_type': 'str',
        'chat_access_address': 'str',
        'chat_access_rest_address': 'str',
        'is_transparent': 'bool',
        'default_language': 'str',
        'client_id': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'state': 'state',
        'duration': 'duration',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'error_info': 'error_info',
        'create_time': 'create_time',
        'lastupdate_time': 'lastupdate_time',
        'rtc_room_info': 'rtc_room_info',
        'chat_subtitle_config': 'chat_subtitle_config',
        'video_config': 'video_config',
        'voice_config_list': 'voice_config_list',
        'chat_state': 'chat_state',
        'language': 'language',
        'chat_video_type': 'chat_video_type',
        'chat_access_address': 'chat_access_address',
        'chat_access_rest_address': 'chat_access_rest_address',
        'is_transparent': 'is_transparent',
        'default_language': 'default_language',
        'client_id': 'client_id',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, job_id=None, state=None, duration=None, start_time=None, end_time=None, error_info=None, create_time=None, lastupdate_time=None, rtc_room_info=None, chat_subtitle_config=None, video_config=None, voice_config_list=None, chat_state=None, language=None, chat_video_type=None, chat_access_address=None, chat_access_rest_address=None, is_transparent=None, default_language=None, client_id=None, x_request_id=None):
        r"""ShowSmartChatJobResponse

        The model defined in huaweicloud sdk

        :param job_id: 数字人智能交互对话任务ID。
        :type job_id: str
        :param state: 数字人智能交互对话任务的状态。 * WAITING: 等待 * PROCESSING: 处理中 * SUCCEED: 成功 * FAILED: 失败 * CANCELED: 取消 * HEARTBEAT: 心跳 * IDLE: 空闲 * DELETING: 删除中
        :type state: str
        :param duration: 数字人智能交互对话时长，单位秒。
        :type duration: float
        :param start_time: 数字人智能交互对话任务开始时间。格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type start_time: str
        :param end_time: 数字人智能交互对话任务结束时间。格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type end_time: str
        :param error_info: 
        :type error_info: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        :param create_time: 数字人智能交互对话任务创建时间。格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param lastupdate_time: 数字人智能交互对话任务最后更新时间。格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type lastupdate_time: str
        :param rtc_room_info: 
        :type rtc_room_info: :class:`huaweicloudsdkmetastudio.v1.RTCRoomInfoList`
        :param chat_subtitle_config: 
        :type chat_subtitle_config: :class:`huaweicloudsdkmetastudio.v1.SmartChatSubtitleConfig`
        :param video_config: 
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.SmartChatVideoConfig`
        :param voice_config_list: 语音配置参数列表。
        :type voice_config_list: list[:class:`huaweicloudsdkmetastudio.v1.SmartChatVoiceConfig`]
        :param chat_state: 数字人智能交互对话的状态。 0: 等待建链 1: 等待关闭链路 2: 建链成功 3: 进入休眠 4: 等待休眠
        :type chat_state: int
        :param language: 
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        :param chat_video_type: 智能交互对话端配置。 * COMPUTER: 电脑端 * MOBILE: 手机端 * HUB: 大屏
        :type chat_video_type: str
        :param chat_access_address: 智能交互接入地址。
        :type chat_access_address: str
        :param chat_access_rest_address: 智能交互Rest接口接入地址。
        :type chat_access_rest_address: str
        :param is_transparent: 是否透明背景
        :type is_transparent: bool
        :param default_language: 默认语言，智能交互接口使用。默认值CN。 * CN：中文。 * EN：英文。 * ESP：西班牙语（仅海外站点支持） * por：葡萄牙语（仅海外站点支持） * Arabic：阿拉伯语（仅海外站点支持） * Thai：泰语（仅海外站点支持）
        :type default_language: str
        :param client_id: clientId
        :type client_id: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowSmartChatJobResponse, self).__init__()

        self._job_id = None
        self._state = None
        self._duration = None
        self._start_time = None
        self._end_time = None
        self._error_info = None
        self._create_time = None
        self._lastupdate_time = None
        self._rtc_room_info = None
        self._chat_subtitle_config = None
        self._video_config = None
        self._voice_config_list = None
        self._chat_state = None
        self._language = None
        self._chat_video_type = None
        self._chat_access_address = None
        self._chat_access_rest_address = None
        self._is_transparent = None
        self._default_language = None
        self._client_id = None
        self._x_request_id = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if state is not None:
            self.state = state
        if duration is not None:
            self.duration = duration
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if error_info is not None:
            self.error_info = error_info
        if create_time is not None:
            self.create_time = create_time
        if lastupdate_time is not None:
            self.lastupdate_time = lastupdate_time
        if rtc_room_info is not None:
            self.rtc_room_info = rtc_room_info
        if chat_subtitle_config is not None:
            self.chat_subtitle_config = chat_subtitle_config
        if video_config is not None:
            self.video_config = video_config
        if voice_config_list is not None:
            self.voice_config_list = voice_config_list
        if chat_state is not None:
            self.chat_state = chat_state
        if language is not None:
            self.language = language
        if chat_video_type is not None:
            self.chat_video_type = chat_video_type
        if chat_access_address is not None:
            self.chat_access_address = chat_access_address
        if chat_access_rest_address is not None:
            self.chat_access_rest_address = chat_access_rest_address
        if is_transparent is not None:
            self.is_transparent = is_transparent
        if default_language is not None:
            self.default_language = default_language
        if client_id is not None:
            self.client_id = client_id
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowSmartChatJobResponse.

        数字人智能交互对话任务ID。

        :return: The job_id of this ShowSmartChatJobResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowSmartChatJobResponse.

        数字人智能交互对话任务ID。

        :param job_id: The job_id of this ShowSmartChatJobResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def state(self):
        r"""Gets the state of this ShowSmartChatJobResponse.

        数字人智能交互对话任务的状态。 * WAITING: 等待 * PROCESSING: 处理中 * SUCCEED: 成功 * FAILED: 失败 * CANCELED: 取消 * HEARTBEAT: 心跳 * IDLE: 空闲 * DELETING: 删除中

        :return: The state of this ShowSmartChatJobResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ShowSmartChatJobResponse.

        数字人智能交互对话任务的状态。 * WAITING: 等待 * PROCESSING: 处理中 * SUCCEED: 成功 * FAILED: 失败 * CANCELED: 取消 * HEARTBEAT: 心跳 * IDLE: 空闲 * DELETING: 删除中

        :param state: The state of this ShowSmartChatJobResponse.
        :type state: str
        """
        self._state = state

    @property
    def duration(self):
        r"""Gets the duration of this ShowSmartChatJobResponse.

        数字人智能交互对话时长，单位秒。

        :return: The duration of this ShowSmartChatJobResponse.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this ShowSmartChatJobResponse.

        数字人智能交互对话时长，单位秒。

        :param duration: The duration of this ShowSmartChatJobResponse.
        :type duration: float
        """
        self._duration = duration

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowSmartChatJobResponse.

        数字人智能交互对话任务开始时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The start_time of this ShowSmartChatJobResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowSmartChatJobResponse.

        数字人智能交互对话任务开始时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param start_time: The start_time of this ShowSmartChatJobResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowSmartChatJobResponse.

        数字人智能交互对话任务结束时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The end_time of this ShowSmartChatJobResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowSmartChatJobResponse.

        数字人智能交互对话任务结束时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param end_time: The end_time of this ShowSmartChatJobResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def error_info(self):
        r"""Gets the error_info of this ShowSmartChatJobResponse.

        :return: The error_info of this ShowSmartChatJobResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        r"""Sets the error_info of this ShowSmartChatJobResponse.

        :param error_info: The error_info of this ShowSmartChatJobResponse.
        :type error_info: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        self._error_info = error_info

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowSmartChatJobResponse.

        数字人智能交互对话任务创建时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this ShowSmartChatJobResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowSmartChatJobResponse.

        数字人智能交互对话任务创建时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this ShowSmartChatJobResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def lastupdate_time(self):
        r"""Gets the lastupdate_time of this ShowSmartChatJobResponse.

        数字人智能交互对话任务最后更新时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The lastupdate_time of this ShowSmartChatJobResponse.
        :rtype: str
        """
        return self._lastupdate_time

    @lastupdate_time.setter
    def lastupdate_time(self, lastupdate_time):
        r"""Sets the lastupdate_time of this ShowSmartChatJobResponse.

        数字人智能交互对话任务最后更新时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param lastupdate_time: The lastupdate_time of this ShowSmartChatJobResponse.
        :type lastupdate_time: str
        """
        self._lastupdate_time = lastupdate_time

    @property
    def rtc_room_info(self):
        r"""Gets the rtc_room_info of this ShowSmartChatJobResponse.

        :return: The rtc_room_info of this ShowSmartChatJobResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.RTCRoomInfoList`
        """
        return self._rtc_room_info

    @rtc_room_info.setter
    def rtc_room_info(self, rtc_room_info):
        r"""Sets the rtc_room_info of this ShowSmartChatJobResponse.

        :param rtc_room_info: The rtc_room_info of this ShowSmartChatJobResponse.
        :type rtc_room_info: :class:`huaweicloudsdkmetastudio.v1.RTCRoomInfoList`
        """
        self._rtc_room_info = rtc_room_info

    @property
    def chat_subtitle_config(self):
        r"""Gets the chat_subtitle_config of this ShowSmartChatJobResponse.

        :return: The chat_subtitle_config of this ShowSmartChatJobResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.SmartChatSubtitleConfig`
        """
        return self._chat_subtitle_config

    @chat_subtitle_config.setter
    def chat_subtitle_config(self, chat_subtitle_config):
        r"""Sets the chat_subtitle_config of this ShowSmartChatJobResponse.

        :param chat_subtitle_config: The chat_subtitle_config of this ShowSmartChatJobResponse.
        :type chat_subtitle_config: :class:`huaweicloudsdkmetastudio.v1.SmartChatSubtitleConfig`
        """
        self._chat_subtitle_config = chat_subtitle_config

    @property
    def video_config(self):
        r"""Gets the video_config of this ShowSmartChatJobResponse.

        :return: The video_config of this ShowSmartChatJobResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.SmartChatVideoConfig`
        """
        return self._video_config

    @video_config.setter
    def video_config(self, video_config):
        r"""Sets the video_config of this ShowSmartChatJobResponse.

        :param video_config: The video_config of this ShowSmartChatJobResponse.
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.SmartChatVideoConfig`
        """
        self._video_config = video_config

    @property
    def voice_config_list(self):
        r"""Gets the voice_config_list of this ShowSmartChatJobResponse.

        语音配置参数列表。

        :return: The voice_config_list of this ShowSmartChatJobResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.SmartChatVoiceConfig`]
        """
        return self._voice_config_list

    @voice_config_list.setter
    def voice_config_list(self, voice_config_list):
        r"""Sets the voice_config_list of this ShowSmartChatJobResponse.

        语音配置参数列表。

        :param voice_config_list: The voice_config_list of this ShowSmartChatJobResponse.
        :type voice_config_list: list[:class:`huaweicloudsdkmetastudio.v1.SmartChatVoiceConfig`]
        """
        self._voice_config_list = voice_config_list

    @property
    def chat_state(self):
        r"""Gets the chat_state of this ShowSmartChatJobResponse.

        数字人智能交互对话的状态。 0: 等待建链 1: 等待关闭链路 2: 建链成功 3: 进入休眠 4: 等待休眠

        :return: The chat_state of this ShowSmartChatJobResponse.
        :rtype: int
        """
        return self._chat_state

    @chat_state.setter
    def chat_state(self, chat_state):
        r"""Sets the chat_state of this ShowSmartChatJobResponse.

        数字人智能交互对话的状态。 0: 等待建链 1: 等待关闭链路 2: 建链成功 3: 进入休眠 4: 等待休眠

        :param chat_state: The chat_state of this ShowSmartChatJobResponse.
        :type chat_state: int
        """
        self._chat_state = chat_state

    @property
    def language(self):
        r"""Gets the language of this ShowSmartChatJobResponse.

        :return: The language of this ShowSmartChatJobResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ShowSmartChatJobResponse.

        :param language: The language of this ShowSmartChatJobResponse.
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        self._language = language

    @property
    def chat_video_type(self):
        r"""Gets the chat_video_type of this ShowSmartChatJobResponse.

        智能交互对话端配置。 * COMPUTER: 电脑端 * MOBILE: 手机端 * HUB: 大屏

        :return: The chat_video_type of this ShowSmartChatJobResponse.
        :rtype: str
        """
        return self._chat_video_type

    @chat_video_type.setter
    def chat_video_type(self, chat_video_type):
        r"""Sets the chat_video_type of this ShowSmartChatJobResponse.

        智能交互对话端配置。 * COMPUTER: 电脑端 * MOBILE: 手机端 * HUB: 大屏

        :param chat_video_type: The chat_video_type of this ShowSmartChatJobResponse.
        :type chat_video_type: str
        """
        self._chat_video_type = chat_video_type

    @property
    def chat_access_address(self):
        r"""Gets the chat_access_address of this ShowSmartChatJobResponse.

        智能交互接入地址。

        :return: The chat_access_address of this ShowSmartChatJobResponse.
        :rtype: str
        """
        return self._chat_access_address

    @chat_access_address.setter
    def chat_access_address(self, chat_access_address):
        r"""Sets the chat_access_address of this ShowSmartChatJobResponse.

        智能交互接入地址。

        :param chat_access_address: The chat_access_address of this ShowSmartChatJobResponse.
        :type chat_access_address: str
        """
        self._chat_access_address = chat_access_address

    @property
    def chat_access_rest_address(self):
        r"""Gets the chat_access_rest_address of this ShowSmartChatJobResponse.

        智能交互Rest接口接入地址。

        :return: The chat_access_rest_address of this ShowSmartChatJobResponse.
        :rtype: str
        """
        return self._chat_access_rest_address

    @chat_access_rest_address.setter
    def chat_access_rest_address(self, chat_access_rest_address):
        r"""Sets the chat_access_rest_address of this ShowSmartChatJobResponse.

        智能交互Rest接口接入地址。

        :param chat_access_rest_address: The chat_access_rest_address of this ShowSmartChatJobResponse.
        :type chat_access_rest_address: str
        """
        self._chat_access_rest_address = chat_access_rest_address

    @property
    def is_transparent(self):
        r"""Gets the is_transparent of this ShowSmartChatJobResponse.

        是否透明背景

        :return: The is_transparent of this ShowSmartChatJobResponse.
        :rtype: bool
        """
        return self._is_transparent

    @is_transparent.setter
    def is_transparent(self, is_transparent):
        r"""Sets the is_transparent of this ShowSmartChatJobResponse.

        是否透明背景

        :param is_transparent: The is_transparent of this ShowSmartChatJobResponse.
        :type is_transparent: bool
        """
        self._is_transparent = is_transparent

    @property
    def default_language(self):
        r"""Gets the default_language of this ShowSmartChatJobResponse.

        默认语言，智能交互接口使用。默认值CN。 * CN：中文。 * EN：英文。 * ESP：西班牙语（仅海外站点支持） * por：葡萄牙语（仅海外站点支持） * Arabic：阿拉伯语（仅海外站点支持） * Thai：泰语（仅海外站点支持）

        :return: The default_language of this ShowSmartChatJobResponse.
        :rtype: str
        """
        return self._default_language

    @default_language.setter
    def default_language(self, default_language):
        r"""Sets the default_language of this ShowSmartChatJobResponse.

        默认语言，智能交互接口使用。默认值CN。 * CN：中文。 * EN：英文。 * ESP：西班牙语（仅海外站点支持） * por：葡萄牙语（仅海外站点支持） * Arabic：阿拉伯语（仅海外站点支持） * Thai：泰语（仅海外站点支持）

        :param default_language: The default_language of this ShowSmartChatJobResponse.
        :type default_language: str
        """
        self._default_language = default_language

    @property
    def client_id(self):
        r"""Gets the client_id of this ShowSmartChatJobResponse.

        clientId

        :return: The client_id of this ShowSmartChatJobResponse.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        r"""Sets the client_id of this ShowSmartChatJobResponse.

        clientId

        :param client_id: The client_id of this ShowSmartChatJobResponse.
        :type client_id: str
        """
        self._client_id = client_id

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowSmartChatJobResponse.

        :return: The x_request_id of this ShowSmartChatJobResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowSmartChatJobResponse.

        :param x_request_id: The x_request_id of this ShowSmartChatJobResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowSmartChatJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
