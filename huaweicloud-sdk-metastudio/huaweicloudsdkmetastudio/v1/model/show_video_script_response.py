# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVideoScriptResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'script_name': 'str',
        'script_description': 'str',
        'view_mode': 'str',
        'model_asset_id': 'str',
        'model_asset_type': 'str',
        'voice_config': 'VoiceConfig',
        'video_config': 'VideoConfig',
        'priv_data': 'str',
        'background_music_config': 'BackgroundMusicConfig',
        'review_config': 'ReviewConfig',
        'audio_files': 'ShootScriptAudioFiles',
        'action_config': 'ActionConfig',
        'shoot_scripts': 'list[ShootScriptShowItem]',
        'script_id': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'script_cover_url': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'script_name': 'script_name',
        'script_description': 'script_description',
        'view_mode': 'view_mode',
        'model_asset_id': 'model_asset_id',
        'model_asset_type': 'model_asset_type',
        'voice_config': 'voice_config',
        'video_config': 'video_config',
        'priv_data': 'priv_data',
        'background_music_config': 'background_music_config',
        'review_config': 'review_config',
        'audio_files': 'audio_files',
        'action_config': 'action_config',
        'shoot_scripts': 'shoot_scripts',
        'script_id': 'script_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'script_cover_url': 'script_cover_url',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, script_name=None, script_description=None, view_mode=None, model_asset_id=None, model_asset_type=None, voice_config=None, video_config=None, priv_data=None, background_music_config=None, review_config=None, audio_files=None, action_config=None, shoot_scripts=None, script_id=None, create_time=None, update_time=None, script_cover_url=None, x_request_id=None):
        r"""ShowVideoScriptResponse

        The model defined in huaweicloud sdk

        :param script_name: **参数解释**： 剧本名称。 **约束限制**： 不涉及。 **取值范围**： 只能使用中英文字符，字符长度1-256位。 **默认取值**： 不涉及。
        :type script_name: str
        :param script_description: **参数解释**： 剧本描述。 **约束限制**： 不涉及。 **取值范围**： 字符长度0-1024位。 **默认取值**： 不涉及。
        :type script_description: str
        :param view_mode: **参数解释**： 横竖屏类型。 **约束限制**： 不涉及。 **取值范围**： * LANDSCAPE：横屏。 * VERTICAL：竖屏。
        :type view_mode: str
        :param model_asset_id: **参数解释**： 数字人模型资产ID。 **约束限制**： 不涉及 **取值范围**： 字符长度0-64位。 **默认取值**： 不涉及
        :type model_asset_id: str
        :param model_asset_type: **参数解释**： 数字人模型类型。 **约束限制**： 不涉及 **取值范围**： * HUMAN_MODEL_2D：分身数字人  **默认取值**： 不涉及
        :type model_asset_type: str
        :param voice_config: 
        :type voice_config: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        :param video_config: 
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        :param priv_data: **参数解释**： 私有数据，用户填写，原样带回。 **约束限制**： 不涉及 **取值范围**： 字符长度0-8192位 **默认取值**： 不涉及
        :type priv_data: str
        :param background_music_config: 
        :type background_music_config: :class:`huaweicloudsdkmetastudio.v1.BackgroundMusicConfig`
        :param review_config: 
        :type review_config: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        :param audio_files: 
        :type audio_files: :class:`huaweicloudsdkmetastudio.v1.ShootScriptAudioFiles`
        :param action_config: 
        :type action_config: :class:`huaweicloudsdkmetastudio.v1.ActionConfig`
        :param shoot_scripts: 拍摄脚本列表。
        :type shoot_scripts: list[:class:`huaweicloudsdkmetastudio.v1.ShootScriptShowItem`]
        :param script_id: 剧本ID。
        :type script_id: str
        :param create_time: 创建时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param update_time: 更新时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type update_time: str
        :param script_cover_url: 剧本封面下载url。
        :type script_cover_url: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowVideoScriptResponse, self).__init__()

        self._script_name = None
        self._script_description = None
        self._view_mode = None
        self._model_asset_id = None
        self._model_asset_type = None
        self._voice_config = None
        self._video_config = None
        self._priv_data = None
        self._background_music_config = None
        self._review_config = None
        self._audio_files = None
        self._action_config = None
        self._shoot_scripts = None
        self._script_id = None
        self._create_time = None
        self._update_time = None
        self._script_cover_url = None
        self._x_request_id = None
        self.discriminator = None

        if script_name is not None:
            self.script_name = script_name
        if script_description is not None:
            self.script_description = script_description
        if view_mode is not None:
            self.view_mode = view_mode
        if model_asset_id is not None:
            self.model_asset_id = model_asset_id
        if model_asset_type is not None:
            self.model_asset_type = model_asset_type
        if voice_config is not None:
            self.voice_config = voice_config
        if video_config is not None:
            self.video_config = video_config
        if priv_data is not None:
            self.priv_data = priv_data
        if background_music_config is not None:
            self.background_music_config = background_music_config
        if review_config is not None:
            self.review_config = review_config
        if audio_files is not None:
            self.audio_files = audio_files
        if action_config is not None:
            self.action_config = action_config
        if shoot_scripts is not None:
            self.shoot_scripts = shoot_scripts
        if script_id is not None:
            self.script_id = script_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if script_cover_url is not None:
            self.script_cover_url = script_cover_url
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def script_name(self):
        r"""Gets the script_name of this ShowVideoScriptResponse.

        **参数解释**： 剧本名称。 **约束限制**： 不涉及。 **取值范围**： 只能使用中英文字符，字符长度1-256位。 **默认取值**： 不涉及。

        :return: The script_name of this ShowVideoScriptResponse.
        :rtype: str
        """
        return self._script_name

    @script_name.setter
    def script_name(self, script_name):
        r"""Sets the script_name of this ShowVideoScriptResponse.

        **参数解释**： 剧本名称。 **约束限制**： 不涉及。 **取值范围**： 只能使用中英文字符，字符长度1-256位。 **默认取值**： 不涉及。

        :param script_name: The script_name of this ShowVideoScriptResponse.
        :type script_name: str
        """
        self._script_name = script_name

    @property
    def script_description(self):
        r"""Gets the script_description of this ShowVideoScriptResponse.

        **参数解释**： 剧本描述。 **约束限制**： 不涉及。 **取值范围**： 字符长度0-1024位。 **默认取值**： 不涉及。

        :return: The script_description of this ShowVideoScriptResponse.
        :rtype: str
        """
        return self._script_description

    @script_description.setter
    def script_description(self, script_description):
        r"""Sets the script_description of this ShowVideoScriptResponse.

        **参数解释**： 剧本描述。 **约束限制**： 不涉及。 **取值范围**： 字符长度0-1024位。 **默认取值**： 不涉及。

        :param script_description: The script_description of this ShowVideoScriptResponse.
        :type script_description: str
        """
        self._script_description = script_description

    @property
    def view_mode(self):
        r"""Gets the view_mode of this ShowVideoScriptResponse.

        **参数解释**： 横竖屏类型。 **约束限制**： 不涉及。 **取值范围**： * LANDSCAPE：横屏。 * VERTICAL：竖屏。

        :return: The view_mode of this ShowVideoScriptResponse.
        :rtype: str
        """
        return self._view_mode

    @view_mode.setter
    def view_mode(self, view_mode):
        r"""Sets the view_mode of this ShowVideoScriptResponse.

        **参数解释**： 横竖屏类型。 **约束限制**： 不涉及。 **取值范围**： * LANDSCAPE：横屏。 * VERTICAL：竖屏。

        :param view_mode: The view_mode of this ShowVideoScriptResponse.
        :type view_mode: str
        """
        self._view_mode = view_mode

    @property
    def model_asset_id(self):
        r"""Gets the model_asset_id of this ShowVideoScriptResponse.

        **参数解释**： 数字人模型资产ID。 **约束限制**： 不涉及 **取值范围**： 字符长度0-64位。 **默认取值**： 不涉及

        :return: The model_asset_id of this ShowVideoScriptResponse.
        :rtype: str
        """
        return self._model_asset_id

    @model_asset_id.setter
    def model_asset_id(self, model_asset_id):
        r"""Sets the model_asset_id of this ShowVideoScriptResponse.

        **参数解释**： 数字人模型资产ID。 **约束限制**： 不涉及 **取值范围**： 字符长度0-64位。 **默认取值**： 不涉及

        :param model_asset_id: The model_asset_id of this ShowVideoScriptResponse.
        :type model_asset_id: str
        """
        self._model_asset_id = model_asset_id

    @property
    def model_asset_type(self):
        r"""Gets the model_asset_type of this ShowVideoScriptResponse.

        **参数解释**： 数字人模型类型。 **约束限制**： 不涉及 **取值范围**： * HUMAN_MODEL_2D：分身数字人  **默认取值**： 不涉及

        :return: The model_asset_type of this ShowVideoScriptResponse.
        :rtype: str
        """
        return self._model_asset_type

    @model_asset_type.setter
    def model_asset_type(self, model_asset_type):
        r"""Sets the model_asset_type of this ShowVideoScriptResponse.

        **参数解释**： 数字人模型类型。 **约束限制**： 不涉及 **取值范围**： * HUMAN_MODEL_2D：分身数字人  **默认取值**： 不涉及

        :param model_asset_type: The model_asset_type of this ShowVideoScriptResponse.
        :type model_asset_type: str
        """
        self._model_asset_type = model_asset_type

    @property
    def voice_config(self):
        r"""Gets the voice_config of this ShowVideoScriptResponse.

        :return: The voice_config of this ShowVideoScriptResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        """
        return self._voice_config

    @voice_config.setter
    def voice_config(self, voice_config):
        r"""Sets the voice_config of this ShowVideoScriptResponse.

        :param voice_config: The voice_config of this ShowVideoScriptResponse.
        :type voice_config: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        """
        self._voice_config = voice_config

    @property
    def video_config(self):
        r"""Gets the video_config of this ShowVideoScriptResponse.

        :return: The video_config of this ShowVideoScriptResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        """
        return self._video_config

    @video_config.setter
    def video_config(self, video_config):
        r"""Sets the video_config of this ShowVideoScriptResponse.

        :param video_config: The video_config of this ShowVideoScriptResponse.
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        """
        self._video_config = video_config

    @property
    def priv_data(self):
        r"""Gets the priv_data of this ShowVideoScriptResponse.

        **参数解释**： 私有数据，用户填写，原样带回。 **约束限制**： 不涉及 **取值范围**： 字符长度0-8192位 **默认取值**： 不涉及

        :return: The priv_data of this ShowVideoScriptResponse.
        :rtype: str
        """
        return self._priv_data

    @priv_data.setter
    def priv_data(self, priv_data):
        r"""Sets the priv_data of this ShowVideoScriptResponse.

        **参数解释**： 私有数据，用户填写，原样带回。 **约束限制**： 不涉及 **取值范围**： 字符长度0-8192位 **默认取值**： 不涉及

        :param priv_data: The priv_data of this ShowVideoScriptResponse.
        :type priv_data: str
        """
        self._priv_data = priv_data

    @property
    def background_music_config(self):
        r"""Gets the background_music_config of this ShowVideoScriptResponse.

        :return: The background_music_config of this ShowVideoScriptResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.BackgroundMusicConfig`
        """
        return self._background_music_config

    @background_music_config.setter
    def background_music_config(self, background_music_config):
        r"""Sets the background_music_config of this ShowVideoScriptResponse.

        :param background_music_config: The background_music_config of this ShowVideoScriptResponse.
        :type background_music_config: :class:`huaweicloudsdkmetastudio.v1.BackgroundMusicConfig`
        """
        self._background_music_config = background_music_config

    @property
    def review_config(self):
        r"""Gets the review_config of this ShowVideoScriptResponse.

        :return: The review_config of this ShowVideoScriptResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        return self._review_config

    @review_config.setter
    def review_config(self, review_config):
        r"""Sets the review_config of this ShowVideoScriptResponse.

        :param review_config: The review_config of this ShowVideoScriptResponse.
        :type review_config: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        self._review_config = review_config

    @property
    def audio_files(self):
        r"""Gets the audio_files of this ShowVideoScriptResponse.

        :return: The audio_files of this ShowVideoScriptResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShootScriptAudioFiles`
        """
        return self._audio_files

    @audio_files.setter
    def audio_files(self, audio_files):
        r"""Sets the audio_files of this ShowVideoScriptResponse.

        :param audio_files: The audio_files of this ShowVideoScriptResponse.
        :type audio_files: :class:`huaweicloudsdkmetastudio.v1.ShootScriptAudioFiles`
        """
        self._audio_files = audio_files

    @property
    def action_config(self):
        r"""Gets the action_config of this ShowVideoScriptResponse.

        :return: The action_config of this ShowVideoScriptResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ActionConfig`
        """
        return self._action_config

    @action_config.setter
    def action_config(self, action_config):
        r"""Sets the action_config of this ShowVideoScriptResponse.

        :param action_config: The action_config of this ShowVideoScriptResponse.
        :type action_config: :class:`huaweicloudsdkmetastudio.v1.ActionConfig`
        """
        self._action_config = action_config

    @property
    def shoot_scripts(self):
        r"""Gets the shoot_scripts of this ShowVideoScriptResponse.

        拍摄脚本列表。

        :return: The shoot_scripts of this ShowVideoScriptResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.ShootScriptShowItem`]
        """
        return self._shoot_scripts

    @shoot_scripts.setter
    def shoot_scripts(self, shoot_scripts):
        r"""Sets the shoot_scripts of this ShowVideoScriptResponse.

        拍摄脚本列表。

        :param shoot_scripts: The shoot_scripts of this ShowVideoScriptResponse.
        :type shoot_scripts: list[:class:`huaweicloudsdkmetastudio.v1.ShootScriptShowItem`]
        """
        self._shoot_scripts = shoot_scripts

    @property
    def script_id(self):
        r"""Gets the script_id of this ShowVideoScriptResponse.

        剧本ID。

        :return: The script_id of this ShowVideoScriptResponse.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        r"""Sets the script_id of this ShowVideoScriptResponse.

        剧本ID。

        :param script_id: The script_id of this ShowVideoScriptResponse.
        :type script_id: str
        """
        self._script_id = script_id

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowVideoScriptResponse.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this ShowVideoScriptResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowVideoScriptResponse.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this ShowVideoScriptResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowVideoScriptResponse.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this ShowVideoScriptResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowVideoScriptResponse.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param update_time: The update_time of this ShowVideoScriptResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def script_cover_url(self):
        r"""Gets the script_cover_url of this ShowVideoScriptResponse.

        剧本封面下载url。

        :return: The script_cover_url of this ShowVideoScriptResponse.
        :rtype: str
        """
        return self._script_cover_url

    @script_cover_url.setter
    def script_cover_url(self, script_cover_url):
        r"""Sets the script_cover_url of this ShowVideoScriptResponse.

        剧本封面下载url。

        :param script_cover_url: The script_cover_url of this ShowVideoScriptResponse.
        :type script_cover_url: str
        """
        self._script_cover_url = script_cover_url

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowVideoScriptResponse.

        :return: The x_request_id of this ShowVideoScriptResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowVideoScriptResponse.

        :param x_request_id: The x_request_id of this ShowVideoScriptResponse.
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
        if not isinstance(other, ShowVideoScriptResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
