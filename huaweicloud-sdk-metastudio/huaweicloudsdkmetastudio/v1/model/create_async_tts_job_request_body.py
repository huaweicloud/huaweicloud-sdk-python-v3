# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAsyncTtsJobRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'text': 'str',
        'tts_text': 'str',
        'voice_asset_id': 'str',
        'speed': 'int',
        'pitch': 'int',
        'volume': 'int',
        'audio_format': 'str',
        'need_timestamp': 'bool',
        'silence_flag': 'bool',
        'silence_time_ms': 'int',
        'callback_config': 'TtsCallBackConfig',
        'gen_srt': 'bool',
        'srt_len': 'int',
        'srt_line_limit': 'int',
        'slice_segments': 'bool',
        'channels': 'int',
        'output_external_url': 'str',
        'srt_output_external_url': 'str',
        'action_output_external_url': 'str',
        'is_vocabulary_config_enable': 'bool',
        'is_concurrent_resource': 'bool',
        'priority': 'int'
    }

    attribute_map = {
        'text': 'text',
        'tts_text': 'tts_text',
        'voice_asset_id': 'voice_asset_id',
        'speed': 'speed',
        'pitch': 'pitch',
        'volume': 'volume',
        'audio_format': 'audio_format',
        'need_timestamp': 'need_timestamp',
        'silence_flag': 'silence_flag',
        'silence_time_ms': 'silence_time_ms',
        'callback_config': 'callback_config',
        'gen_srt': 'gen_srt',
        'srt_len': 'srt_len',
        'srt_line_limit': 'srt_line_limit',
        'slice_segments': 'slice_segments',
        'channels': 'channels',
        'output_external_url': 'output_external_url',
        'srt_output_external_url': 'srt_output_external_url',
        'action_output_external_url': 'action_output_external_url',
        'is_vocabulary_config_enable': 'is_vocabulary_config_enable',
        'is_concurrent_resource': 'is_concurrent_resource',
        'priority': 'priority'
    }

    def __init__(self, text=None, tts_text=None, voice_asset_id=None, speed=None, pitch=None, volume=None, audio_format=None, need_timestamp=None, silence_flag=None, silence_time_ms=None, callback_config=None, gen_srt=None, srt_len=None, srt_line_limit=None, slice_segments=None, channels=None, output_external_url=None, srt_output_external_url=None, action_output_external_url=None, is_vocabulary_config_enable=None, is_concurrent_resource=None, priority=None):
        r"""CreateAsyncTtsJobRequestBody

        The model defined in huaweicloud sdk

        :param text: 待合成文本
        :type text: str
        :param tts_text: 发送给tts的待合成文本
        :type tts_text: str
        :param voice_asset_id: 音色ID，获取方式详见[获取音色ID](metastudio_02_0054.xml)。  不同Region的计费标准详见[预置音色计费标准](metastudio_02_0060.xml)。
        :type voice_asset_id: str
        :param speed: 语速。 * 当取值为“100”时，表示一个成年人正常的语速，约为250字/分钟。 * 50表示0.5倍语速，100表示正常语速，200表示2倍语速。
        :type speed: int
        :param pitch: 音高。
        :type pitch: int
        :param volume: 音量。
        :type volume: int
        :param audio_format: 输出音频文件格式。默认WAV。 * WAV：wav格式。 * MP3：mp3格式。
        :type audio_format: str
        :param need_timestamp: 是否需要时间戳。false为不需要，true为需要返回时间戳信息。默认值为false。
        :type need_timestamp: bool
        :param silence_flag: 异常时是否返回静默音频流
        :type silence_flag: bool
        :param silence_time_ms: 异常时返回的静默音频流时长，单位毫秒。
        :type silence_time_ms: int
        :param callback_config: 
        :type callback_config: :class:`huaweicloudsdkmetastudio.v1.TtsCallBackConfig`
        :param gen_srt: 是否开启字幕
        :type gen_srt: bool
        :param srt_len: 字幕最大长度限制
        :type srt_len: int
        :param srt_line_limit: 字幕行数限制，默认为1
        :type srt_line_limit: int
        :param slice_segments: 是否对文本进行分段
        :type slice_segments: bool
        :param channels: 声道。（单声道|双声道） 默认值1，最小值1，最大值2。
        :type channels: int
        :param output_external_url: 音频文件上传的外部URL &gt; * 需要先申请开通白名单， 才允许将音频等文件上传到外部URL。
        :type output_external_url: str
        :param srt_output_external_url: 字幕文件上传的外部URL &gt; * 需要先申请开通白名单， 才允许将字幕等文件上传到外部URL。
        :type srt_output_external_url: str
        :param action_output_external_url: 动作信息文件上传的外部URL &gt; * 需要先申请开通白名单， 才允许将时间戳等文件上传到外部URL。
        :type action_output_external_url: str
        :param is_vocabulary_config_enable: 是否应用当前租户的读法配置
        :type is_vocabulary_config_enable: bool
        :param is_concurrent_resource: 是否使用包周期路数资源进行计费
        :type is_concurrent_resource: bool
        :param priority: 优先级（0-10），0为最高优先级，默认5
        :type priority: int
        """
        
        

        self._text = None
        self._tts_text = None
        self._voice_asset_id = None
        self._speed = None
        self._pitch = None
        self._volume = None
        self._audio_format = None
        self._need_timestamp = None
        self._silence_flag = None
        self._silence_time_ms = None
        self._callback_config = None
        self._gen_srt = None
        self._srt_len = None
        self._srt_line_limit = None
        self._slice_segments = None
        self._channels = None
        self._output_external_url = None
        self._srt_output_external_url = None
        self._action_output_external_url = None
        self._is_vocabulary_config_enable = None
        self._is_concurrent_resource = None
        self._priority = None
        self.discriminator = None

        self.text = text
        if tts_text is not None:
            self.tts_text = tts_text
        self.voice_asset_id = voice_asset_id
        if speed is not None:
            self.speed = speed
        if pitch is not None:
            self.pitch = pitch
        if volume is not None:
            self.volume = volume
        if audio_format is not None:
            self.audio_format = audio_format
        if need_timestamp is not None:
            self.need_timestamp = need_timestamp
        if silence_flag is not None:
            self.silence_flag = silence_flag
        if silence_time_ms is not None:
            self.silence_time_ms = silence_time_ms
        if callback_config is not None:
            self.callback_config = callback_config
        if gen_srt is not None:
            self.gen_srt = gen_srt
        if srt_len is not None:
            self.srt_len = srt_len
        if srt_line_limit is not None:
            self.srt_line_limit = srt_line_limit
        if slice_segments is not None:
            self.slice_segments = slice_segments
        if channels is not None:
            self.channels = channels
        if output_external_url is not None:
            self.output_external_url = output_external_url
        if srt_output_external_url is not None:
            self.srt_output_external_url = srt_output_external_url
        if action_output_external_url is not None:
            self.action_output_external_url = action_output_external_url
        if is_vocabulary_config_enable is not None:
            self.is_vocabulary_config_enable = is_vocabulary_config_enable
        if is_concurrent_resource is not None:
            self.is_concurrent_resource = is_concurrent_resource
        if priority is not None:
            self.priority = priority

    @property
    def text(self):
        r"""Gets the text of this CreateAsyncTtsJobRequestBody.

        待合成文本

        :return: The text of this CreateAsyncTtsJobRequestBody.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        r"""Sets the text of this CreateAsyncTtsJobRequestBody.

        待合成文本

        :param text: The text of this CreateAsyncTtsJobRequestBody.
        :type text: str
        """
        self._text = text

    @property
    def tts_text(self):
        r"""Gets the tts_text of this CreateAsyncTtsJobRequestBody.

        发送给tts的待合成文本

        :return: The tts_text of this CreateAsyncTtsJobRequestBody.
        :rtype: str
        """
        return self._tts_text

    @tts_text.setter
    def tts_text(self, tts_text):
        r"""Sets the tts_text of this CreateAsyncTtsJobRequestBody.

        发送给tts的待合成文本

        :param tts_text: The tts_text of this CreateAsyncTtsJobRequestBody.
        :type tts_text: str
        """
        self._tts_text = tts_text

    @property
    def voice_asset_id(self):
        r"""Gets the voice_asset_id of this CreateAsyncTtsJobRequestBody.

        音色ID，获取方式详见[获取音色ID](metastudio_02_0054.xml)。  不同Region的计费标准详见[预置音色计费标准](metastudio_02_0060.xml)。

        :return: The voice_asset_id of this CreateAsyncTtsJobRequestBody.
        :rtype: str
        """
        return self._voice_asset_id

    @voice_asset_id.setter
    def voice_asset_id(self, voice_asset_id):
        r"""Sets the voice_asset_id of this CreateAsyncTtsJobRequestBody.

        音色ID，获取方式详见[获取音色ID](metastudio_02_0054.xml)。  不同Region的计费标准详见[预置音色计费标准](metastudio_02_0060.xml)。

        :param voice_asset_id: The voice_asset_id of this CreateAsyncTtsJobRequestBody.
        :type voice_asset_id: str
        """
        self._voice_asset_id = voice_asset_id

    @property
    def speed(self):
        r"""Gets the speed of this CreateAsyncTtsJobRequestBody.

        语速。 * 当取值为“100”时，表示一个成年人正常的语速，约为250字/分钟。 * 50表示0.5倍语速，100表示正常语速，200表示2倍语速。

        :return: The speed of this CreateAsyncTtsJobRequestBody.
        :rtype: int
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        r"""Sets the speed of this CreateAsyncTtsJobRequestBody.

        语速。 * 当取值为“100”时，表示一个成年人正常的语速，约为250字/分钟。 * 50表示0.5倍语速，100表示正常语速，200表示2倍语速。

        :param speed: The speed of this CreateAsyncTtsJobRequestBody.
        :type speed: int
        """
        self._speed = speed

    @property
    def pitch(self):
        r"""Gets the pitch of this CreateAsyncTtsJobRequestBody.

        音高。

        :return: The pitch of this CreateAsyncTtsJobRequestBody.
        :rtype: int
        """
        return self._pitch

    @pitch.setter
    def pitch(self, pitch):
        r"""Sets the pitch of this CreateAsyncTtsJobRequestBody.

        音高。

        :param pitch: The pitch of this CreateAsyncTtsJobRequestBody.
        :type pitch: int
        """
        self._pitch = pitch

    @property
    def volume(self):
        r"""Gets the volume of this CreateAsyncTtsJobRequestBody.

        音量。

        :return: The volume of this CreateAsyncTtsJobRequestBody.
        :rtype: int
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        r"""Sets the volume of this CreateAsyncTtsJobRequestBody.

        音量。

        :param volume: The volume of this CreateAsyncTtsJobRequestBody.
        :type volume: int
        """
        self._volume = volume

    @property
    def audio_format(self):
        r"""Gets the audio_format of this CreateAsyncTtsJobRequestBody.

        输出音频文件格式。默认WAV。 * WAV：wav格式。 * MP3：mp3格式。

        :return: The audio_format of this CreateAsyncTtsJobRequestBody.
        :rtype: str
        """
        return self._audio_format

    @audio_format.setter
    def audio_format(self, audio_format):
        r"""Sets the audio_format of this CreateAsyncTtsJobRequestBody.

        输出音频文件格式。默认WAV。 * WAV：wav格式。 * MP3：mp3格式。

        :param audio_format: The audio_format of this CreateAsyncTtsJobRequestBody.
        :type audio_format: str
        """
        self._audio_format = audio_format

    @property
    def need_timestamp(self):
        r"""Gets the need_timestamp of this CreateAsyncTtsJobRequestBody.

        是否需要时间戳。false为不需要，true为需要返回时间戳信息。默认值为false。

        :return: The need_timestamp of this CreateAsyncTtsJobRequestBody.
        :rtype: bool
        """
        return self._need_timestamp

    @need_timestamp.setter
    def need_timestamp(self, need_timestamp):
        r"""Sets the need_timestamp of this CreateAsyncTtsJobRequestBody.

        是否需要时间戳。false为不需要，true为需要返回时间戳信息。默认值为false。

        :param need_timestamp: The need_timestamp of this CreateAsyncTtsJobRequestBody.
        :type need_timestamp: bool
        """
        self._need_timestamp = need_timestamp

    @property
    def silence_flag(self):
        r"""Gets the silence_flag of this CreateAsyncTtsJobRequestBody.

        异常时是否返回静默音频流

        :return: The silence_flag of this CreateAsyncTtsJobRequestBody.
        :rtype: bool
        """
        return self._silence_flag

    @silence_flag.setter
    def silence_flag(self, silence_flag):
        r"""Sets the silence_flag of this CreateAsyncTtsJobRequestBody.

        异常时是否返回静默音频流

        :param silence_flag: The silence_flag of this CreateAsyncTtsJobRequestBody.
        :type silence_flag: bool
        """
        self._silence_flag = silence_flag

    @property
    def silence_time_ms(self):
        r"""Gets the silence_time_ms of this CreateAsyncTtsJobRequestBody.

        异常时返回的静默音频流时长，单位毫秒。

        :return: The silence_time_ms of this CreateAsyncTtsJobRequestBody.
        :rtype: int
        """
        return self._silence_time_ms

    @silence_time_ms.setter
    def silence_time_ms(self, silence_time_ms):
        r"""Sets the silence_time_ms of this CreateAsyncTtsJobRequestBody.

        异常时返回的静默音频流时长，单位毫秒。

        :param silence_time_ms: The silence_time_ms of this CreateAsyncTtsJobRequestBody.
        :type silence_time_ms: int
        """
        self._silence_time_ms = silence_time_ms

    @property
    def callback_config(self):
        r"""Gets the callback_config of this CreateAsyncTtsJobRequestBody.

        :return: The callback_config of this CreateAsyncTtsJobRequestBody.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.TtsCallBackConfig`
        """
        return self._callback_config

    @callback_config.setter
    def callback_config(self, callback_config):
        r"""Sets the callback_config of this CreateAsyncTtsJobRequestBody.

        :param callback_config: The callback_config of this CreateAsyncTtsJobRequestBody.
        :type callback_config: :class:`huaweicloudsdkmetastudio.v1.TtsCallBackConfig`
        """
        self._callback_config = callback_config

    @property
    def gen_srt(self):
        r"""Gets the gen_srt of this CreateAsyncTtsJobRequestBody.

        是否开启字幕

        :return: The gen_srt of this CreateAsyncTtsJobRequestBody.
        :rtype: bool
        """
        return self._gen_srt

    @gen_srt.setter
    def gen_srt(self, gen_srt):
        r"""Sets the gen_srt of this CreateAsyncTtsJobRequestBody.

        是否开启字幕

        :param gen_srt: The gen_srt of this CreateAsyncTtsJobRequestBody.
        :type gen_srt: bool
        """
        self._gen_srt = gen_srt

    @property
    def srt_len(self):
        r"""Gets the srt_len of this CreateAsyncTtsJobRequestBody.

        字幕最大长度限制

        :return: The srt_len of this CreateAsyncTtsJobRequestBody.
        :rtype: int
        """
        return self._srt_len

    @srt_len.setter
    def srt_len(self, srt_len):
        r"""Sets the srt_len of this CreateAsyncTtsJobRequestBody.

        字幕最大长度限制

        :param srt_len: The srt_len of this CreateAsyncTtsJobRequestBody.
        :type srt_len: int
        """
        self._srt_len = srt_len

    @property
    def srt_line_limit(self):
        r"""Gets the srt_line_limit of this CreateAsyncTtsJobRequestBody.

        字幕行数限制，默认为1

        :return: The srt_line_limit of this CreateAsyncTtsJobRequestBody.
        :rtype: int
        """
        return self._srt_line_limit

    @srt_line_limit.setter
    def srt_line_limit(self, srt_line_limit):
        r"""Sets the srt_line_limit of this CreateAsyncTtsJobRequestBody.

        字幕行数限制，默认为1

        :param srt_line_limit: The srt_line_limit of this CreateAsyncTtsJobRequestBody.
        :type srt_line_limit: int
        """
        self._srt_line_limit = srt_line_limit

    @property
    def slice_segments(self):
        r"""Gets the slice_segments of this CreateAsyncTtsJobRequestBody.

        是否对文本进行分段

        :return: The slice_segments of this CreateAsyncTtsJobRequestBody.
        :rtype: bool
        """
        return self._slice_segments

    @slice_segments.setter
    def slice_segments(self, slice_segments):
        r"""Sets the slice_segments of this CreateAsyncTtsJobRequestBody.

        是否对文本进行分段

        :param slice_segments: The slice_segments of this CreateAsyncTtsJobRequestBody.
        :type slice_segments: bool
        """
        self._slice_segments = slice_segments

    @property
    def channels(self):
        r"""Gets the channels of this CreateAsyncTtsJobRequestBody.

        声道。（单声道|双声道） 默认值1，最小值1，最大值2。

        :return: The channels of this CreateAsyncTtsJobRequestBody.
        :rtype: int
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        r"""Sets the channels of this CreateAsyncTtsJobRequestBody.

        声道。（单声道|双声道） 默认值1，最小值1，最大值2。

        :param channels: The channels of this CreateAsyncTtsJobRequestBody.
        :type channels: int
        """
        self._channels = channels

    @property
    def output_external_url(self):
        r"""Gets the output_external_url of this CreateAsyncTtsJobRequestBody.

        音频文件上传的外部URL > * 需要先申请开通白名单， 才允许将音频等文件上传到外部URL。

        :return: The output_external_url of this CreateAsyncTtsJobRequestBody.
        :rtype: str
        """
        return self._output_external_url

    @output_external_url.setter
    def output_external_url(self, output_external_url):
        r"""Sets the output_external_url of this CreateAsyncTtsJobRequestBody.

        音频文件上传的外部URL > * 需要先申请开通白名单， 才允许将音频等文件上传到外部URL。

        :param output_external_url: The output_external_url of this CreateAsyncTtsJobRequestBody.
        :type output_external_url: str
        """
        self._output_external_url = output_external_url

    @property
    def srt_output_external_url(self):
        r"""Gets the srt_output_external_url of this CreateAsyncTtsJobRequestBody.

        字幕文件上传的外部URL > * 需要先申请开通白名单， 才允许将字幕等文件上传到外部URL。

        :return: The srt_output_external_url of this CreateAsyncTtsJobRequestBody.
        :rtype: str
        """
        return self._srt_output_external_url

    @srt_output_external_url.setter
    def srt_output_external_url(self, srt_output_external_url):
        r"""Sets the srt_output_external_url of this CreateAsyncTtsJobRequestBody.

        字幕文件上传的外部URL > * 需要先申请开通白名单， 才允许将字幕等文件上传到外部URL。

        :param srt_output_external_url: The srt_output_external_url of this CreateAsyncTtsJobRequestBody.
        :type srt_output_external_url: str
        """
        self._srt_output_external_url = srt_output_external_url

    @property
    def action_output_external_url(self):
        r"""Gets the action_output_external_url of this CreateAsyncTtsJobRequestBody.

        动作信息文件上传的外部URL > * 需要先申请开通白名单， 才允许将时间戳等文件上传到外部URL。

        :return: The action_output_external_url of this CreateAsyncTtsJobRequestBody.
        :rtype: str
        """
        return self._action_output_external_url

    @action_output_external_url.setter
    def action_output_external_url(self, action_output_external_url):
        r"""Sets the action_output_external_url of this CreateAsyncTtsJobRequestBody.

        动作信息文件上传的外部URL > * 需要先申请开通白名单， 才允许将时间戳等文件上传到外部URL。

        :param action_output_external_url: The action_output_external_url of this CreateAsyncTtsJobRequestBody.
        :type action_output_external_url: str
        """
        self._action_output_external_url = action_output_external_url

    @property
    def is_vocabulary_config_enable(self):
        r"""Gets the is_vocabulary_config_enable of this CreateAsyncTtsJobRequestBody.

        是否应用当前租户的读法配置

        :return: The is_vocabulary_config_enable of this CreateAsyncTtsJobRequestBody.
        :rtype: bool
        """
        return self._is_vocabulary_config_enable

    @is_vocabulary_config_enable.setter
    def is_vocabulary_config_enable(self, is_vocabulary_config_enable):
        r"""Sets the is_vocabulary_config_enable of this CreateAsyncTtsJobRequestBody.

        是否应用当前租户的读法配置

        :param is_vocabulary_config_enable: The is_vocabulary_config_enable of this CreateAsyncTtsJobRequestBody.
        :type is_vocabulary_config_enable: bool
        """
        self._is_vocabulary_config_enable = is_vocabulary_config_enable

    @property
    def is_concurrent_resource(self):
        r"""Gets the is_concurrent_resource of this CreateAsyncTtsJobRequestBody.

        是否使用包周期路数资源进行计费

        :return: The is_concurrent_resource of this CreateAsyncTtsJobRequestBody.
        :rtype: bool
        """
        return self._is_concurrent_resource

    @is_concurrent_resource.setter
    def is_concurrent_resource(self, is_concurrent_resource):
        r"""Sets the is_concurrent_resource of this CreateAsyncTtsJobRequestBody.

        是否使用包周期路数资源进行计费

        :param is_concurrent_resource: The is_concurrent_resource of this CreateAsyncTtsJobRequestBody.
        :type is_concurrent_resource: bool
        """
        self._is_concurrent_resource = is_concurrent_resource

    @property
    def priority(self):
        r"""Gets the priority of this CreateAsyncTtsJobRequestBody.

        优先级（0-10），0为最高优先级，默认5

        :return: The priority of this CreateAsyncTtsJobRequestBody.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this CreateAsyncTtsJobRequestBody.

        优先级（0-10），0为最高优先级，默认5

        :param priority: The priority of this CreateAsyncTtsJobRequestBody.
        :type priority: int
        """
        self._priority = priority

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
        if not isinstance(other, CreateAsyncTtsJobRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
