# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Show2DDigitalHumanVideoResponse(SdkResponse):

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
        'start_time': 'str',
        'end_time': 'str',
        'duration': 'float',
        'output_asset_config': 'OutputAssetInfo',
        'error_info': 'ErrorResponse',
        'create_time': 'str',
        'lastupdate_time': 'str',
        'script_id': 'str',
        'video_making_type': 'str',
        'human_image': 'str',
        'model_asset_id': 'str',
        'voice_config': 'VoiceConfig',
        'video_config': 'VideoConfig',
        'shoot_scripts': 'list[ShootScriptItem]',
        'background_music_config': 'BackgroundMusicConfig',
        'x_request_id': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'state': 'state',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'duration': 'duration',
        'output_asset_config': 'output_asset_config',
        'error_info': 'error_info',
        'create_time': 'create_time',
        'lastupdate_time': 'lastupdate_time',
        'script_id': 'script_id',
        'video_making_type': 'video_making_type',
        'human_image': 'human_image',
        'model_asset_id': 'model_asset_id',
        'voice_config': 'voice_config',
        'video_config': 'video_config',
        'shoot_scripts': 'shoot_scripts',
        'background_music_config': 'background_music_config',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, job_id=None, state=None, start_time=None, end_time=None, duration=None, output_asset_config=None, error_info=None, create_time=None, lastupdate_time=None, script_id=None, video_making_type=None, human_image=None, model_asset_id=None, voice_config=None, video_config=None, shoot_scripts=None, background_music_config=None, x_request_id=None):
        """Show2DDigitalHumanVideoResponse

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param state: 任务的状态。 * WAITING：等待 * PROCESSING：处理中 * SUCCEED：成功 * FAILED：失败 * CANCELED：取消
        :type state: str
        :param start_time: 数字人视频制作开始时间。
        :type start_time: str
        :param end_time: 数字人视频制作结束时间。
        :type end_time: str
        :param duration: 数字人视频内容时长。
        :type duration: float
        :param output_asset_config: 
        :type output_asset_config: :class:`huaweicloudsdkmetastudio.v1.OutputAssetInfo`
        :param error_info: 
        :type error_info: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        :param create_time: 任务创建时间。
        :type create_time: str
        :param lastupdate_time: 任务更新时间。
        :type lastupdate_time: str
        :param script_id: 剧本ID。
        :type script_id: str
        :param video_making_type: 视频生成类型。该参数取值是MODEL时，model_asset_id必填；取值是PICTURE时，human_image必填。 * MODEL：通过分数数字人模型生成视频 * PICTURE： 通过单张照片生成视频
        :type video_making_type: str
        :param human_image: 人物照片，需要Base64编码。
        :type human_image: str
        :param model_asset_id: 分身数字人模型资产ID。
        :type model_asset_id: str
        :param voice_config: 
        :type voice_config: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        :param video_config: 
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        :param shoot_scripts: 拍摄脚本列表。
        :type shoot_scripts: list[:class:`huaweicloudsdkmetastudio.v1.ShootScriptItem`]
        :param background_music_config: 
        :type background_music_config: :class:`huaweicloudsdkmetastudio.v1.BackgroundMusicConfig`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(Show2DDigitalHumanVideoResponse, self).__init__()

        self._job_id = None
        self._state = None
        self._start_time = None
        self._end_time = None
        self._duration = None
        self._output_asset_config = None
        self._error_info = None
        self._create_time = None
        self._lastupdate_time = None
        self._script_id = None
        self._video_making_type = None
        self._human_image = None
        self._model_asset_id = None
        self._voice_config = None
        self._video_config = None
        self._shoot_scripts = None
        self._background_music_config = None
        self._x_request_id = None
        self.discriminator = None

        self.job_id = job_id
        self.state = state
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if duration is not None:
            self.duration = duration
        if output_asset_config is not None:
            self.output_asset_config = output_asset_config
        if error_info is not None:
            self.error_info = error_info
        if create_time is not None:
            self.create_time = create_time
        if lastupdate_time is not None:
            self.lastupdate_time = lastupdate_time
        if script_id is not None:
            self.script_id = script_id
        if video_making_type is not None:
            self.video_making_type = video_making_type
        if human_image is not None:
            self.human_image = human_image
        if model_asset_id is not None:
            self.model_asset_id = model_asset_id
        if voice_config is not None:
            self.voice_config = voice_config
        if video_config is not None:
            self.video_config = video_config
        if shoot_scripts is not None:
            self.shoot_scripts = shoot_scripts
        if background_music_config is not None:
            self.background_music_config = background_music_config
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def job_id(self):
        """Gets the job_id of this Show2DDigitalHumanVideoResponse.

        任务ID。

        :return: The job_id of this Show2DDigitalHumanVideoResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this Show2DDigitalHumanVideoResponse.

        任务ID。

        :param job_id: The job_id of this Show2DDigitalHumanVideoResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def state(self):
        """Gets the state of this Show2DDigitalHumanVideoResponse.

        任务的状态。 * WAITING：等待 * PROCESSING：处理中 * SUCCEED：成功 * FAILED：失败 * CANCELED：取消

        :return: The state of this Show2DDigitalHumanVideoResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Show2DDigitalHumanVideoResponse.

        任务的状态。 * WAITING：等待 * PROCESSING：处理中 * SUCCEED：成功 * FAILED：失败 * CANCELED：取消

        :param state: The state of this Show2DDigitalHumanVideoResponse.
        :type state: str
        """
        self._state = state

    @property
    def start_time(self):
        """Gets the start_time of this Show2DDigitalHumanVideoResponse.

        数字人视频制作开始时间。

        :return: The start_time of this Show2DDigitalHumanVideoResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Show2DDigitalHumanVideoResponse.

        数字人视频制作开始时间。

        :param start_time: The start_time of this Show2DDigitalHumanVideoResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this Show2DDigitalHumanVideoResponse.

        数字人视频制作结束时间。

        :return: The end_time of this Show2DDigitalHumanVideoResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this Show2DDigitalHumanVideoResponse.

        数字人视频制作结束时间。

        :param end_time: The end_time of this Show2DDigitalHumanVideoResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def duration(self):
        """Gets the duration of this Show2DDigitalHumanVideoResponse.

        数字人视频内容时长。

        :return: The duration of this Show2DDigitalHumanVideoResponse.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Show2DDigitalHumanVideoResponse.

        数字人视频内容时长。

        :param duration: The duration of this Show2DDigitalHumanVideoResponse.
        :type duration: float
        """
        self._duration = duration

    @property
    def output_asset_config(self):
        """Gets the output_asset_config of this Show2DDigitalHumanVideoResponse.

        :return: The output_asset_config of this Show2DDigitalHumanVideoResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.OutputAssetInfo`
        """
        return self._output_asset_config

    @output_asset_config.setter
    def output_asset_config(self, output_asset_config):
        """Sets the output_asset_config of this Show2DDigitalHumanVideoResponse.

        :param output_asset_config: The output_asset_config of this Show2DDigitalHumanVideoResponse.
        :type output_asset_config: :class:`huaweicloudsdkmetastudio.v1.OutputAssetInfo`
        """
        self._output_asset_config = output_asset_config

    @property
    def error_info(self):
        """Gets the error_info of this Show2DDigitalHumanVideoResponse.

        :return: The error_info of this Show2DDigitalHumanVideoResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        """Sets the error_info of this Show2DDigitalHumanVideoResponse.

        :param error_info: The error_info of this Show2DDigitalHumanVideoResponse.
        :type error_info: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        self._error_info = error_info

    @property
    def create_time(self):
        """Gets the create_time of this Show2DDigitalHumanVideoResponse.

        任务创建时间。

        :return: The create_time of this Show2DDigitalHumanVideoResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Show2DDigitalHumanVideoResponse.

        任务创建时间。

        :param create_time: The create_time of this Show2DDigitalHumanVideoResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def lastupdate_time(self):
        """Gets the lastupdate_time of this Show2DDigitalHumanVideoResponse.

        任务更新时间。

        :return: The lastupdate_time of this Show2DDigitalHumanVideoResponse.
        :rtype: str
        """
        return self._lastupdate_time

    @lastupdate_time.setter
    def lastupdate_time(self, lastupdate_time):
        """Sets the lastupdate_time of this Show2DDigitalHumanVideoResponse.

        任务更新时间。

        :param lastupdate_time: The lastupdate_time of this Show2DDigitalHumanVideoResponse.
        :type lastupdate_time: str
        """
        self._lastupdate_time = lastupdate_time

    @property
    def script_id(self):
        """Gets the script_id of this Show2DDigitalHumanVideoResponse.

        剧本ID。

        :return: The script_id of this Show2DDigitalHumanVideoResponse.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        """Sets the script_id of this Show2DDigitalHumanVideoResponse.

        剧本ID。

        :param script_id: The script_id of this Show2DDigitalHumanVideoResponse.
        :type script_id: str
        """
        self._script_id = script_id

    @property
    def video_making_type(self):
        """Gets the video_making_type of this Show2DDigitalHumanVideoResponse.

        视频生成类型。该参数取值是MODEL时，model_asset_id必填；取值是PICTURE时，human_image必填。 * MODEL：通过分数数字人模型生成视频 * PICTURE： 通过单张照片生成视频

        :return: The video_making_type of this Show2DDigitalHumanVideoResponse.
        :rtype: str
        """
        return self._video_making_type

    @video_making_type.setter
    def video_making_type(self, video_making_type):
        """Sets the video_making_type of this Show2DDigitalHumanVideoResponse.

        视频生成类型。该参数取值是MODEL时，model_asset_id必填；取值是PICTURE时，human_image必填。 * MODEL：通过分数数字人模型生成视频 * PICTURE： 通过单张照片生成视频

        :param video_making_type: The video_making_type of this Show2DDigitalHumanVideoResponse.
        :type video_making_type: str
        """
        self._video_making_type = video_making_type

    @property
    def human_image(self):
        """Gets the human_image of this Show2DDigitalHumanVideoResponse.

        人物照片，需要Base64编码。

        :return: The human_image of this Show2DDigitalHumanVideoResponse.
        :rtype: str
        """
        return self._human_image

    @human_image.setter
    def human_image(self, human_image):
        """Sets the human_image of this Show2DDigitalHumanVideoResponse.

        人物照片，需要Base64编码。

        :param human_image: The human_image of this Show2DDigitalHumanVideoResponse.
        :type human_image: str
        """
        self._human_image = human_image

    @property
    def model_asset_id(self):
        """Gets the model_asset_id of this Show2DDigitalHumanVideoResponse.

        分身数字人模型资产ID。

        :return: The model_asset_id of this Show2DDigitalHumanVideoResponse.
        :rtype: str
        """
        return self._model_asset_id

    @model_asset_id.setter
    def model_asset_id(self, model_asset_id):
        """Sets the model_asset_id of this Show2DDigitalHumanVideoResponse.

        分身数字人模型资产ID。

        :param model_asset_id: The model_asset_id of this Show2DDigitalHumanVideoResponse.
        :type model_asset_id: str
        """
        self._model_asset_id = model_asset_id

    @property
    def voice_config(self):
        """Gets the voice_config of this Show2DDigitalHumanVideoResponse.

        :return: The voice_config of this Show2DDigitalHumanVideoResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        """
        return self._voice_config

    @voice_config.setter
    def voice_config(self, voice_config):
        """Sets the voice_config of this Show2DDigitalHumanVideoResponse.

        :param voice_config: The voice_config of this Show2DDigitalHumanVideoResponse.
        :type voice_config: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        """
        self._voice_config = voice_config

    @property
    def video_config(self):
        """Gets the video_config of this Show2DDigitalHumanVideoResponse.

        :return: The video_config of this Show2DDigitalHumanVideoResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        """
        return self._video_config

    @video_config.setter
    def video_config(self, video_config):
        """Sets the video_config of this Show2DDigitalHumanVideoResponse.

        :param video_config: The video_config of this Show2DDigitalHumanVideoResponse.
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        """
        self._video_config = video_config

    @property
    def shoot_scripts(self):
        """Gets the shoot_scripts of this Show2DDigitalHumanVideoResponse.

        拍摄脚本列表。

        :return: The shoot_scripts of this Show2DDigitalHumanVideoResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.ShootScriptItem`]
        """
        return self._shoot_scripts

    @shoot_scripts.setter
    def shoot_scripts(self, shoot_scripts):
        """Sets the shoot_scripts of this Show2DDigitalHumanVideoResponse.

        拍摄脚本列表。

        :param shoot_scripts: The shoot_scripts of this Show2DDigitalHumanVideoResponse.
        :type shoot_scripts: list[:class:`huaweicloudsdkmetastudio.v1.ShootScriptItem`]
        """
        self._shoot_scripts = shoot_scripts

    @property
    def background_music_config(self):
        """Gets the background_music_config of this Show2DDigitalHumanVideoResponse.

        :return: The background_music_config of this Show2DDigitalHumanVideoResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.BackgroundMusicConfig`
        """
        return self._background_music_config

    @background_music_config.setter
    def background_music_config(self, background_music_config):
        """Sets the background_music_config of this Show2DDigitalHumanVideoResponse.

        :param background_music_config: The background_music_config of this Show2DDigitalHumanVideoResponse.
        :type background_music_config: :class:`huaweicloudsdkmetastudio.v1.BackgroundMusicConfig`
        """
        self._background_music_config = background_music_config

    @property
    def x_request_id(self):
        """Gets the x_request_id of this Show2DDigitalHumanVideoResponse.

        :return: The x_request_id of this Show2DDigitalHumanVideoResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this Show2DDigitalHumanVideoResponse.

        :param x_request_id: The x_request_id of this Show2DDigitalHumanVideoResponse.
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
        if not isinstance(other, Show2DDigitalHumanVideoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
