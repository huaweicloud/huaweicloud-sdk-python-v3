# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TtsJobDetail:

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
        'websocket_job_id': 'str',
        'asset_id': 'str',
        'tts_service_enum': 'str',
        'text_length': 'int',
        'create_time': 'str',
        'audio_format': 'str',
        'need_timestamp': 'bool',
        'gen_srt': 'bool',
        'job_type': 'str',
        'job_state': 'str',
        'fail_msg': 'str',
        'files': 'list[TtsJobFile]'
    }

    attribute_map = {
        'job_id': 'job_id',
        'websocket_job_id': 'websocket_job_id',
        'asset_id': 'asset_id',
        'tts_service_enum': 'tts_service_enum',
        'text_length': 'text_length',
        'create_time': 'create_time',
        'audio_format': 'audio_format',
        'need_timestamp': 'need_timestamp',
        'gen_srt': 'gen_srt',
        'job_type': 'job_type',
        'job_state': 'job_state',
        'fail_msg': 'fail_msg',
        'files': 'files'
    }

    def __init__(self, job_id=None, websocket_job_id=None, asset_id=None, tts_service_enum=None, text_length=None, create_time=None, audio_format=None, need_timestamp=None, gen_srt=None, job_type=None, job_state=None, fail_msg=None, files=None):
        r"""TtsJobDetail

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param websocket_job_id: websocket任务ID。
        :type websocket_job_id: str
        :param asset_id: 音色ID
        :type asset_id: str
        :param tts_service_enum: 声音版本
        :type tts_service_enum: str
        :param text_length: 文本长度
        :type text_length: int
        :param create_time: 任务创建时间。
        :type create_time: str
        :param audio_format: 输出音频文件格式。默认WAV。 * WAV：wav格式。 * MP3：mp3格式。 * PCM：pcm格式。
        :type audio_format: str
        :param need_timestamp: 是否需要时间戳。false为不需要，true为需要返回时间戳信息。默认值为false。
        :type need_timestamp: bool
        :param gen_srt: 是否开启字幕
        :type gen_srt: bool
        :param job_type: 任务类型。 * PRELOAD：预加载任务 * WEBSOCKET：websocket接口任务 * ASYNC_JOB：异步任务 * AUDITION：试听任务
        :type job_type: str
        :param job_state: 任务状态。 * WAITING：等待中 * PROCESSING：合成中 * FAILED：合成失败 * SUCCEED：合成成功
        :type job_state: str
        :param fail_msg: 任务合成错误信息
        :type fail_msg: str
        :param files: 任务合成文件列表。
        :type files: list[:class:`huaweicloudsdkmetastudio.v1.TtsJobFile`]
        """
        
        

        self._job_id = None
        self._websocket_job_id = None
        self._asset_id = None
        self._tts_service_enum = None
        self._text_length = None
        self._create_time = None
        self._audio_format = None
        self._need_timestamp = None
        self._gen_srt = None
        self._job_type = None
        self._job_state = None
        self._fail_msg = None
        self._files = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if websocket_job_id is not None:
            self.websocket_job_id = websocket_job_id
        if asset_id is not None:
            self.asset_id = asset_id
        if tts_service_enum is not None:
            self.tts_service_enum = tts_service_enum
        if text_length is not None:
            self.text_length = text_length
        if create_time is not None:
            self.create_time = create_time
        if audio_format is not None:
            self.audio_format = audio_format
        if need_timestamp is not None:
            self.need_timestamp = need_timestamp
        if gen_srt is not None:
            self.gen_srt = gen_srt
        if job_type is not None:
            self.job_type = job_type
        if job_state is not None:
            self.job_state = job_state
        if fail_msg is not None:
            self.fail_msg = fail_msg
        if files is not None:
            self.files = files

    @property
    def job_id(self):
        r"""Gets the job_id of this TtsJobDetail.

        任务ID。

        :return: The job_id of this TtsJobDetail.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this TtsJobDetail.

        任务ID。

        :param job_id: The job_id of this TtsJobDetail.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def websocket_job_id(self):
        r"""Gets the websocket_job_id of this TtsJobDetail.

        websocket任务ID。

        :return: The websocket_job_id of this TtsJobDetail.
        :rtype: str
        """
        return self._websocket_job_id

    @websocket_job_id.setter
    def websocket_job_id(self, websocket_job_id):
        r"""Sets the websocket_job_id of this TtsJobDetail.

        websocket任务ID。

        :param websocket_job_id: The websocket_job_id of this TtsJobDetail.
        :type websocket_job_id: str
        """
        self._websocket_job_id = websocket_job_id

    @property
    def asset_id(self):
        r"""Gets the asset_id of this TtsJobDetail.

        音色ID

        :return: The asset_id of this TtsJobDetail.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this TtsJobDetail.

        音色ID

        :param asset_id: The asset_id of this TtsJobDetail.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def tts_service_enum(self):
        r"""Gets the tts_service_enum of this TtsJobDetail.

        声音版本

        :return: The tts_service_enum of this TtsJobDetail.
        :rtype: str
        """
        return self._tts_service_enum

    @tts_service_enum.setter
    def tts_service_enum(self, tts_service_enum):
        r"""Sets the tts_service_enum of this TtsJobDetail.

        声音版本

        :param tts_service_enum: The tts_service_enum of this TtsJobDetail.
        :type tts_service_enum: str
        """
        self._tts_service_enum = tts_service_enum

    @property
    def text_length(self):
        r"""Gets the text_length of this TtsJobDetail.

        文本长度

        :return: The text_length of this TtsJobDetail.
        :rtype: int
        """
        return self._text_length

    @text_length.setter
    def text_length(self, text_length):
        r"""Sets the text_length of this TtsJobDetail.

        文本长度

        :param text_length: The text_length of this TtsJobDetail.
        :type text_length: int
        """
        self._text_length = text_length

    @property
    def create_time(self):
        r"""Gets the create_time of this TtsJobDetail.

        任务创建时间。

        :return: The create_time of this TtsJobDetail.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TtsJobDetail.

        任务创建时间。

        :param create_time: The create_time of this TtsJobDetail.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def audio_format(self):
        r"""Gets the audio_format of this TtsJobDetail.

        输出音频文件格式。默认WAV。 * WAV：wav格式。 * MP3：mp3格式。 * PCM：pcm格式。

        :return: The audio_format of this TtsJobDetail.
        :rtype: str
        """
        return self._audio_format

    @audio_format.setter
    def audio_format(self, audio_format):
        r"""Sets the audio_format of this TtsJobDetail.

        输出音频文件格式。默认WAV。 * WAV：wav格式。 * MP3：mp3格式。 * PCM：pcm格式。

        :param audio_format: The audio_format of this TtsJobDetail.
        :type audio_format: str
        """
        self._audio_format = audio_format

    @property
    def need_timestamp(self):
        r"""Gets the need_timestamp of this TtsJobDetail.

        是否需要时间戳。false为不需要，true为需要返回时间戳信息。默认值为false。

        :return: The need_timestamp of this TtsJobDetail.
        :rtype: bool
        """
        return self._need_timestamp

    @need_timestamp.setter
    def need_timestamp(self, need_timestamp):
        r"""Sets the need_timestamp of this TtsJobDetail.

        是否需要时间戳。false为不需要，true为需要返回时间戳信息。默认值为false。

        :param need_timestamp: The need_timestamp of this TtsJobDetail.
        :type need_timestamp: bool
        """
        self._need_timestamp = need_timestamp

    @property
    def gen_srt(self):
        r"""Gets the gen_srt of this TtsJobDetail.

        是否开启字幕

        :return: The gen_srt of this TtsJobDetail.
        :rtype: bool
        """
        return self._gen_srt

    @gen_srt.setter
    def gen_srt(self, gen_srt):
        r"""Sets the gen_srt of this TtsJobDetail.

        是否开启字幕

        :param gen_srt: The gen_srt of this TtsJobDetail.
        :type gen_srt: bool
        """
        self._gen_srt = gen_srt

    @property
    def job_type(self):
        r"""Gets the job_type of this TtsJobDetail.

        任务类型。 * PRELOAD：预加载任务 * WEBSOCKET：websocket接口任务 * ASYNC_JOB：异步任务 * AUDITION：试听任务

        :return: The job_type of this TtsJobDetail.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this TtsJobDetail.

        任务类型。 * PRELOAD：预加载任务 * WEBSOCKET：websocket接口任务 * ASYNC_JOB：异步任务 * AUDITION：试听任务

        :param job_type: The job_type of this TtsJobDetail.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def job_state(self):
        r"""Gets the job_state of this TtsJobDetail.

        任务状态。 * WAITING：等待中 * PROCESSING：合成中 * FAILED：合成失败 * SUCCEED：合成成功

        :return: The job_state of this TtsJobDetail.
        :rtype: str
        """
        return self._job_state

    @job_state.setter
    def job_state(self, job_state):
        r"""Sets the job_state of this TtsJobDetail.

        任务状态。 * WAITING：等待中 * PROCESSING：合成中 * FAILED：合成失败 * SUCCEED：合成成功

        :param job_state: The job_state of this TtsJobDetail.
        :type job_state: str
        """
        self._job_state = job_state

    @property
    def fail_msg(self):
        r"""Gets the fail_msg of this TtsJobDetail.

        任务合成错误信息

        :return: The fail_msg of this TtsJobDetail.
        :rtype: str
        """
        return self._fail_msg

    @fail_msg.setter
    def fail_msg(self, fail_msg):
        r"""Sets the fail_msg of this TtsJobDetail.

        任务合成错误信息

        :param fail_msg: The fail_msg of this TtsJobDetail.
        :type fail_msg: str
        """
        self._fail_msg = fail_msg

    @property
    def files(self):
        r"""Gets the files of this TtsJobDetail.

        任务合成文件列表。

        :return: The files of this TtsJobDetail.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.TtsJobFile`]
        """
        return self._files

    @files.setter
    def files(self, files):
        r"""Sets the files of this TtsJobDetail.

        任务合成文件列表。

        :param files: The files of this TtsJobDetail.
        :type files: list[:class:`huaweicloudsdkmetastudio.v1.TtsJobFile`]
        """
        self._files = files

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
        if not isinstance(other, TtsJobDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
