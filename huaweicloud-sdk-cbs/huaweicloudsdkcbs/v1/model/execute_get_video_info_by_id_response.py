# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteGetVideoInfoByIdResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'str',
        'update_time': 'str',
        'error_msg': 'str',
        'id': 'str',
        'name': 'str',
        'progress': 'int',
        'status': 'int',
        'subtitle_url': 'str',
        'video_url': 'str',
        'video_shot': 'str',
        'character_config': 'CharacterConfig',
        'compose_actions': 'list[int]',
        'read_config': 'ReadConfigResp',
        'tts_config': 'TtsConfig',
        'video_config': 'VideoConfigResp'
    }

    attribute_map = {
        'create_time': 'create_time',
        'update_time': 'update_time',
        'error_msg': 'error_msg',
        'id': 'id',
        'name': 'name',
        'progress': 'progress',
        'status': 'status',
        'subtitle_url': 'subtitle_url',
        'video_url': 'video_url',
        'video_shot': 'video_shot',
        'character_config': 'character_config',
        'compose_actions': 'compose_actions',
        'read_config': 'read_config',
        'tts_config': 'tts_config',
        'video_config': 'video_config'
    }

    def __init__(self, create_time=None, update_time=None, error_msg=None, id=None, name=None, progress=None, status=None, subtitle_url=None, video_url=None, video_shot=None, character_config=None, compose_actions=None, read_config=None, tts_config=None, video_config=None):
        r"""ExecuteGetVideoInfoByIdResponse

        The model defined in huaweicloud sdk

        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        :param error_msg: 错误信息 如: {\\\&quot;error_code\\\&quot;:\\\&quot;0001\\\&quot;,\\\&quot;error_msg\\\&quot;:\\\&quot;播报内容超过10分钟，请重新调整播报内容。\\\&quot;}
        :type error_msg: str
        :param id: 
        :type id: str
        :param name: 视频名称
        :type name: str
        :param progress: 视频生成进度 0~100
        :type progress: int
        :param status: 0：未初始化 1：生成中 2：生成成功 3：生成失败
        :type status: int
        :param subtitle_url: 字幕地址
        :type subtitle_url: str
        :param video_url: 视频的obs地址，当视频生成成功时返回
        :type video_url: str
        :param video_shot: 视频截图地址，jpg格式 分辨率480 * 270 当status&#x3D;2：生成成功时返回
        :type video_shot: str
        :param character_config: 
        :type character_config: :class:`huaweicloudsdkcbs.v1.CharacterConfig`
        :param compose_actions: 合成动作，如果不为空，则表示可以进行合成操作
        :type compose_actions: list[int]
        :param read_config: 
        :type read_config: :class:`huaweicloudsdkcbs.v1.ReadConfigResp`
        :param tts_config: 
        :type tts_config: :class:`huaweicloudsdkcbs.v1.TtsConfig`
        :param video_config: 
        :type video_config: :class:`huaweicloudsdkcbs.v1.VideoConfigResp`
        """
        
        super(ExecuteGetVideoInfoByIdResponse, self).__init__()

        self._create_time = None
        self._update_time = None
        self._error_msg = None
        self._id = None
        self._name = None
        self._progress = None
        self._status = None
        self._subtitle_url = None
        self._video_url = None
        self._video_shot = None
        self._character_config = None
        self._compose_actions = None
        self._read_config = None
        self._tts_config = None
        self._video_config = None
        self.discriminator = None

        self.create_time = create_time
        self.update_time = update_time
        if error_msg is not None:
            self.error_msg = error_msg
        self.id = id
        self.name = name
        if progress is not None:
            self.progress = progress
        self.status = status
        self.subtitle_url = subtitle_url
        if video_url is not None:
            self.video_url = video_url
        if video_shot is not None:
            self.video_shot = video_shot
        self.character_config = character_config
        if compose_actions is not None:
            self.compose_actions = compose_actions
        self.read_config = read_config
        self.tts_config = tts_config
        self.video_config = video_config

    @property
    def create_time(self):
        r"""Gets the create_time of this ExecuteGetVideoInfoByIdResponse.

        创建时间

        :return: The create_time of this ExecuteGetVideoInfoByIdResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ExecuteGetVideoInfoByIdResponse.

        创建时间

        :param create_time: The create_time of this ExecuteGetVideoInfoByIdResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ExecuteGetVideoInfoByIdResponse.

        更新时间

        :return: The update_time of this ExecuteGetVideoInfoByIdResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ExecuteGetVideoInfoByIdResponse.

        更新时间

        :param update_time: The update_time of this ExecuteGetVideoInfoByIdResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ExecuteGetVideoInfoByIdResponse.

        错误信息 如: {\\\"error_code\\\":\\\"0001\\\",\\\"error_msg\\\":\\\"播报内容超过10分钟，请重新调整播报内容。\\\"}

        :return: The error_msg of this ExecuteGetVideoInfoByIdResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ExecuteGetVideoInfoByIdResponse.

        错误信息 如: {\\\"error_code\\\":\\\"0001\\\",\\\"error_msg\\\":\\\"播报内容超过10分钟，请重新调整播报内容。\\\"}

        :param error_msg: The error_msg of this ExecuteGetVideoInfoByIdResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def id(self):
        r"""Gets the id of this ExecuteGetVideoInfoByIdResponse.

        

        :return: The id of this ExecuteGetVideoInfoByIdResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ExecuteGetVideoInfoByIdResponse.

        

        :param id: The id of this ExecuteGetVideoInfoByIdResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ExecuteGetVideoInfoByIdResponse.

        视频名称

        :return: The name of this ExecuteGetVideoInfoByIdResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ExecuteGetVideoInfoByIdResponse.

        视频名称

        :param name: The name of this ExecuteGetVideoInfoByIdResponse.
        :type name: str
        """
        self._name = name

    @property
    def progress(self):
        r"""Gets the progress of this ExecuteGetVideoInfoByIdResponse.

        视频生成进度 0~100

        :return: The progress of this ExecuteGetVideoInfoByIdResponse.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this ExecuteGetVideoInfoByIdResponse.

        视频生成进度 0~100

        :param progress: The progress of this ExecuteGetVideoInfoByIdResponse.
        :type progress: int
        """
        self._progress = progress

    @property
    def status(self):
        r"""Gets the status of this ExecuteGetVideoInfoByIdResponse.

        0：未初始化 1：生成中 2：生成成功 3：生成失败

        :return: The status of this ExecuteGetVideoInfoByIdResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ExecuteGetVideoInfoByIdResponse.

        0：未初始化 1：生成中 2：生成成功 3：生成失败

        :param status: The status of this ExecuteGetVideoInfoByIdResponse.
        :type status: int
        """
        self._status = status

    @property
    def subtitle_url(self):
        r"""Gets the subtitle_url of this ExecuteGetVideoInfoByIdResponse.

        字幕地址

        :return: The subtitle_url of this ExecuteGetVideoInfoByIdResponse.
        :rtype: str
        """
        return self._subtitle_url

    @subtitle_url.setter
    def subtitle_url(self, subtitle_url):
        r"""Sets the subtitle_url of this ExecuteGetVideoInfoByIdResponse.

        字幕地址

        :param subtitle_url: The subtitle_url of this ExecuteGetVideoInfoByIdResponse.
        :type subtitle_url: str
        """
        self._subtitle_url = subtitle_url

    @property
    def video_url(self):
        r"""Gets the video_url of this ExecuteGetVideoInfoByIdResponse.

        视频的obs地址，当视频生成成功时返回

        :return: The video_url of this ExecuteGetVideoInfoByIdResponse.
        :rtype: str
        """
        return self._video_url

    @video_url.setter
    def video_url(self, video_url):
        r"""Sets the video_url of this ExecuteGetVideoInfoByIdResponse.

        视频的obs地址，当视频生成成功时返回

        :param video_url: The video_url of this ExecuteGetVideoInfoByIdResponse.
        :type video_url: str
        """
        self._video_url = video_url

    @property
    def video_shot(self):
        r"""Gets the video_shot of this ExecuteGetVideoInfoByIdResponse.

        视频截图地址，jpg格式 分辨率480 * 270 当status=2：生成成功时返回

        :return: The video_shot of this ExecuteGetVideoInfoByIdResponse.
        :rtype: str
        """
        return self._video_shot

    @video_shot.setter
    def video_shot(self, video_shot):
        r"""Sets the video_shot of this ExecuteGetVideoInfoByIdResponse.

        视频截图地址，jpg格式 分辨率480 * 270 当status=2：生成成功时返回

        :param video_shot: The video_shot of this ExecuteGetVideoInfoByIdResponse.
        :type video_shot: str
        """
        self._video_shot = video_shot

    @property
    def character_config(self):
        r"""Gets the character_config of this ExecuteGetVideoInfoByIdResponse.

        :return: The character_config of this ExecuteGetVideoInfoByIdResponse.
        :rtype: :class:`huaweicloudsdkcbs.v1.CharacterConfig`
        """
        return self._character_config

    @character_config.setter
    def character_config(self, character_config):
        r"""Sets the character_config of this ExecuteGetVideoInfoByIdResponse.

        :param character_config: The character_config of this ExecuteGetVideoInfoByIdResponse.
        :type character_config: :class:`huaweicloudsdkcbs.v1.CharacterConfig`
        """
        self._character_config = character_config

    @property
    def compose_actions(self):
        r"""Gets the compose_actions of this ExecuteGetVideoInfoByIdResponse.

        合成动作，如果不为空，则表示可以进行合成操作

        :return: The compose_actions of this ExecuteGetVideoInfoByIdResponse.
        :rtype: list[int]
        """
        return self._compose_actions

    @compose_actions.setter
    def compose_actions(self, compose_actions):
        r"""Sets the compose_actions of this ExecuteGetVideoInfoByIdResponse.

        合成动作，如果不为空，则表示可以进行合成操作

        :param compose_actions: The compose_actions of this ExecuteGetVideoInfoByIdResponse.
        :type compose_actions: list[int]
        """
        self._compose_actions = compose_actions

    @property
    def read_config(self):
        r"""Gets the read_config of this ExecuteGetVideoInfoByIdResponse.

        :return: The read_config of this ExecuteGetVideoInfoByIdResponse.
        :rtype: :class:`huaweicloudsdkcbs.v1.ReadConfigResp`
        """
        return self._read_config

    @read_config.setter
    def read_config(self, read_config):
        r"""Sets the read_config of this ExecuteGetVideoInfoByIdResponse.

        :param read_config: The read_config of this ExecuteGetVideoInfoByIdResponse.
        :type read_config: :class:`huaweicloudsdkcbs.v1.ReadConfigResp`
        """
        self._read_config = read_config

    @property
    def tts_config(self):
        r"""Gets the tts_config of this ExecuteGetVideoInfoByIdResponse.

        :return: The tts_config of this ExecuteGetVideoInfoByIdResponse.
        :rtype: :class:`huaweicloudsdkcbs.v1.TtsConfig`
        """
        return self._tts_config

    @tts_config.setter
    def tts_config(self, tts_config):
        r"""Sets the tts_config of this ExecuteGetVideoInfoByIdResponse.

        :param tts_config: The tts_config of this ExecuteGetVideoInfoByIdResponse.
        :type tts_config: :class:`huaweicloudsdkcbs.v1.TtsConfig`
        """
        self._tts_config = tts_config

    @property
    def video_config(self):
        r"""Gets the video_config of this ExecuteGetVideoInfoByIdResponse.

        :return: The video_config of this ExecuteGetVideoInfoByIdResponse.
        :rtype: :class:`huaweicloudsdkcbs.v1.VideoConfigResp`
        """
        return self._video_config

    @video_config.setter
    def video_config(self, video_config):
        r"""Sets the video_config of this ExecuteGetVideoInfoByIdResponse.

        :param video_config: The video_config of this ExecuteGetVideoInfoByIdResponse.
        :type video_config: :class:`huaweicloudsdkcbs.v1.VideoConfigResp`
        """
        self._video_config = video_config

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
        if not isinstance(other, ExecuteGetVideoInfoByIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
