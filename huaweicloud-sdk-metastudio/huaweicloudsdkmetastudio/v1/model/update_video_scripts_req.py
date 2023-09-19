# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVideoScriptsReq:

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
        'video_making_type': 'str',
        'human_image': 'str',
        'model_asset_id': 'str',
        'model_asset_type': 'str',
        'scene_asset_id': 'str',
        'voice_config': 'VoiceConfig',
        'video_config': 'VideoConfig',
        'shoot_scripts': 'list[ShootScriptItem]',
        'priv_data': 'str',
        'background_music_config': 'BackgroundMusicConfig'
    }

    attribute_map = {
        'script_name': 'script_name',
        'script_description': 'script_description',
        'video_making_type': 'video_making_type',
        'human_image': 'human_image',
        'model_asset_id': 'model_asset_id',
        'model_asset_type': 'model_asset_type',
        'scene_asset_id': 'scene_asset_id',
        'voice_config': 'voice_config',
        'video_config': 'video_config',
        'shoot_scripts': 'shoot_scripts',
        'priv_data': 'priv_data',
        'background_music_config': 'background_music_config'
    }

    def __init__(self, script_name=None, script_description=None, video_making_type=None, human_image=None, model_asset_id=None, model_asset_type=None, scene_asset_id=None, voice_config=None, video_config=None, shoot_scripts=None, priv_data=None, background_music_config=None):
        """UpdateVideoScriptsReq

        The model defined in huaweicloud sdk

        :param script_name: 剧本名称。
        :type script_name: str
        :param script_description: 剧本描述。
        :type script_description: str
        :param video_making_type: 视频生成类型。该参数取值是MODEL时，model_asset_id必填；取值是PICTURE时，human_image必填。 * MODEL：通过分数数字人模型生成视频 * PICTURE： 通过单张照片生成视频
        :type video_making_type: str
        :param human_image: 人物照片，需要Base64编码。
        :type human_image: str
        :param model_asset_id: 数字人资产ID。
        :type model_asset_id: str
        :param model_asset_type: 数字人模型类型。  * HUMAN_MODEL_2D：分身数字人 * HUMAN_MODEL_3D：3D数字人
        :type model_asset_type: str
        :param scene_asset_id: 场景资产ID。
        :type scene_asset_id: str
        :param voice_config: 
        :type voice_config: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        :param video_config: 
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        :param shoot_scripts: 剧本参数。
        :type shoot_scripts: list[:class:`huaweicloudsdkmetastudio.v1.ShootScriptItem`]
        :param priv_data: 私有数据，用户填写，原样带回。
        :type priv_data: str
        :param background_music_config: 
        :type background_music_config: :class:`huaweicloudsdkmetastudio.v1.BackgroundMusicConfig`
        """
        
        

        self._script_name = None
        self._script_description = None
        self._video_making_type = None
        self._human_image = None
        self._model_asset_id = None
        self._model_asset_type = None
        self._scene_asset_id = None
        self._voice_config = None
        self._video_config = None
        self._shoot_scripts = None
        self._priv_data = None
        self._background_music_config = None
        self.discriminator = None

        if script_name is not None:
            self.script_name = script_name
        if script_description is not None:
            self.script_description = script_description
        if video_making_type is not None:
            self.video_making_type = video_making_type
        if human_image is not None:
            self.human_image = human_image
        if model_asset_id is not None:
            self.model_asset_id = model_asset_id
        if model_asset_type is not None:
            self.model_asset_type = model_asset_type
        if scene_asset_id is not None:
            self.scene_asset_id = scene_asset_id
        if voice_config is not None:
            self.voice_config = voice_config
        if video_config is not None:
            self.video_config = video_config
        if shoot_scripts is not None:
            self.shoot_scripts = shoot_scripts
        if priv_data is not None:
            self.priv_data = priv_data
        if background_music_config is not None:
            self.background_music_config = background_music_config

    @property
    def script_name(self):
        """Gets the script_name of this UpdateVideoScriptsReq.

        剧本名称。

        :return: The script_name of this UpdateVideoScriptsReq.
        :rtype: str
        """
        return self._script_name

    @script_name.setter
    def script_name(self, script_name):
        """Sets the script_name of this UpdateVideoScriptsReq.

        剧本名称。

        :param script_name: The script_name of this UpdateVideoScriptsReq.
        :type script_name: str
        """
        self._script_name = script_name

    @property
    def script_description(self):
        """Gets the script_description of this UpdateVideoScriptsReq.

        剧本描述。

        :return: The script_description of this UpdateVideoScriptsReq.
        :rtype: str
        """
        return self._script_description

    @script_description.setter
    def script_description(self, script_description):
        """Sets the script_description of this UpdateVideoScriptsReq.

        剧本描述。

        :param script_description: The script_description of this UpdateVideoScriptsReq.
        :type script_description: str
        """
        self._script_description = script_description

    @property
    def video_making_type(self):
        """Gets the video_making_type of this UpdateVideoScriptsReq.

        视频生成类型。该参数取值是MODEL时，model_asset_id必填；取值是PICTURE时，human_image必填。 * MODEL：通过分数数字人模型生成视频 * PICTURE： 通过单张照片生成视频

        :return: The video_making_type of this UpdateVideoScriptsReq.
        :rtype: str
        """
        return self._video_making_type

    @video_making_type.setter
    def video_making_type(self, video_making_type):
        """Sets the video_making_type of this UpdateVideoScriptsReq.

        视频生成类型。该参数取值是MODEL时，model_asset_id必填；取值是PICTURE时，human_image必填。 * MODEL：通过分数数字人模型生成视频 * PICTURE： 通过单张照片生成视频

        :param video_making_type: The video_making_type of this UpdateVideoScriptsReq.
        :type video_making_type: str
        """
        self._video_making_type = video_making_type

    @property
    def human_image(self):
        """Gets the human_image of this UpdateVideoScriptsReq.

        人物照片，需要Base64编码。

        :return: The human_image of this UpdateVideoScriptsReq.
        :rtype: str
        """
        return self._human_image

    @human_image.setter
    def human_image(self, human_image):
        """Sets the human_image of this UpdateVideoScriptsReq.

        人物照片，需要Base64编码。

        :param human_image: The human_image of this UpdateVideoScriptsReq.
        :type human_image: str
        """
        self._human_image = human_image

    @property
    def model_asset_id(self):
        """Gets the model_asset_id of this UpdateVideoScriptsReq.

        数字人资产ID。

        :return: The model_asset_id of this UpdateVideoScriptsReq.
        :rtype: str
        """
        return self._model_asset_id

    @model_asset_id.setter
    def model_asset_id(self, model_asset_id):
        """Sets the model_asset_id of this UpdateVideoScriptsReq.

        数字人资产ID。

        :param model_asset_id: The model_asset_id of this UpdateVideoScriptsReq.
        :type model_asset_id: str
        """
        self._model_asset_id = model_asset_id

    @property
    def model_asset_type(self):
        """Gets the model_asset_type of this UpdateVideoScriptsReq.

        数字人模型类型。  * HUMAN_MODEL_2D：分身数字人 * HUMAN_MODEL_3D：3D数字人

        :return: The model_asset_type of this UpdateVideoScriptsReq.
        :rtype: str
        """
        return self._model_asset_type

    @model_asset_type.setter
    def model_asset_type(self, model_asset_type):
        """Sets the model_asset_type of this UpdateVideoScriptsReq.

        数字人模型类型。  * HUMAN_MODEL_2D：分身数字人 * HUMAN_MODEL_3D：3D数字人

        :param model_asset_type: The model_asset_type of this UpdateVideoScriptsReq.
        :type model_asset_type: str
        """
        self._model_asset_type = model_asset_type

    @property
    def scene_asset_id(self):
        """Gets the scene_asset_id of this UpdateVideoScriptsReq.

        场景资产ID。

        :return: The scene_asset_id of this UpdateVideoScriptsReq.
        :rtype: str
        """
        return self._scene_asset_id

    @scene_asset_id.setter
    def scene_asset_id(self, scene_asset_id):
        """Sets the scene_asset_id of this UpdateVideoScriptsReq.

        场景资产ID。

        :param scene_asset_id: The scene_asset_id of this UpdateVideoScriptsReq.
        :type scene_asset_id: str
        """
        self._scene_asset_id = scene_asset_id

    @property
    def voice_config(self):
        """Gets the voice_config of this UpdateVideoScriptsReq.

        :return: The voice_config of this UpdateVideoScriptsReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        """
        return self._voice_config

    @voice_config.setter
    def voice_config(self, voice_config):
        """Sets the voice_config of this UpdateVideoScriptsReq.

        :param voice_config: The voice_config of this UpdateVideoScriptsReq.
        :type voice_config: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        """
        self._voice_config = voice_config

    @property
    def video_config(self):
        """Gets the video_config of this UpdateVideoScriptsReq.

        :return: The video_config of this UpdateVideoScriptsReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        """
        return self._video_config

    @video_config.setter
    def video_config(self, video_config):
        """Sets the video_config of this UpdateVideoScriptsReq.

        :param video_config: The video_config of this UpdateVideoScriptsReq.
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        """
        self._video_config = video_config

    @property
    def shoot_scripts(self):
        """Gets the shoot_scripts of this UpdateVideoScriptsReq.

        剧本参数。

        :return: The shoot_scripts of this UpdateVideoScriptsReq.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.ShootScriptItem`]
        """
        return self._shoot_scripts

    @shoot_scripts.setter
    def shoot_scripts(self, shoot_scripts):
        """Sets the shoot_scripts of this UpdateVideoScriptsReq.

        剧本参数。

        :param shoot_scripts: The shoot_scripts of this UpdateVideoScriptsReq.
        :type shoot_scripts: list[:class:`huaweicloudsdkmetastudio.v1.ShootScriptItem`]
        """
        self._shoot_scripts = shoot_scripts

    @property
    def priv_data(self):
        """Gets the priv_data of this UpdateVideoScriptsReq.

        私有数据，用户填写，原样带回。

        :return: The priv_data of this UpdateVideoScriptsReq.
        :rtype: str
        """
        return self._priv_data

    @priv_data.setter
    def priv_data(self, priv_data):
        """Sets the priv_data of this UpdateVideoScriptsReq.

        私有数据，用户填写，原样带回。

        :param priv_data: The priv_data of this UpdateVideoScriptsReq.
        :type priv_data: str
        """
        self._priv_data = priv_data

    @property
    def background_music_config(self):
        """Gets the background_music_config of this UpdateVideoScriptsReq.

        :return: The background_music_config of this UpdateVideoScriptsReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.BackgroundMusicConfig`
        """
        return self._background_music_config

    @background_music_config.setter
    def background_music_config(self, background_music_config):
        """Sets the background_music_config of this UpdateVideoScriptsReq.

        :param background_music_config: The background_music_config of this UpdateVideoScriptsReq.
        :type background_music_config: :class:`huaweicloudsdkmetastudio.v1.BackgroundMusicConfig`
        """
        self._background_music_config = background_music_config

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
        if not isinstance(other, UpdateVideoScriptsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
