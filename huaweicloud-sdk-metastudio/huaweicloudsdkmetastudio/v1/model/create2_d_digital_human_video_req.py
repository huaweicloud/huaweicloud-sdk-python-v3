# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Create2DDigitalHumanVideoReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'script_id': 'str',
        'video_making_type': 'str',
        'model_asset_id': 'str',
        'human_image': 'str',
        'voice_config': 'VoiceConfig',
        'video_config': 'VideoConfig',
        'shoot_scripts': 'list[ShootScriptItem]',
        'output_asset_config': 'OutputAssetConfig',
        'background_music_config': 'BackgroundMusicConfig'
    }

    attribute_map = {
        'script_id': 'script_id',
        'video_making_type': 'video_making_type',
        'model_asset_id': 'model_asset_id',
        'human_image': 'human_image',
        'voice_config': 'voice_config',
        'video_config': 'video_config',
        'shoot_scripts': 'shoot_scripts',
        'output_asset_config': 'output_asset_config',
        'background_music_config': 'background_music_config'
    }

    def __init__(self, script_id=None, video_making_type=None, model_asset_id=None, human_image=None, voice_config=None, video_config=None, shoot_scripts=None, output_asset_config=None, background_music_config=None):
        """Create2DDigitalHumanVideoReq

        The model defined in huaweicloud sdk

        :param script_id: 剧本ID。 &gt; * 如果填写了script_id，model_asset_id、voice_config、scene_asset_id、video_config、shoot_scripts可以不填，以脚本中的配置为准。 &gt; * 如果填写了script_id，并且同时也填写了model_asset_id、voice_config、scene_asset_id、video_config、shoot_scripts则以本接口中的配置为准。
        :type script_id: str
        :param video_making_type: 视频生成类型。该参数取值是MODEL时，model_asset_id必填；取值是PICTURE时，human_image必填。 * MODEL：通过分数数字人模型生成视频 * PICTURE： 通过单张照片生成视频
        :type video_making_type: str
        :param model_asset_id: 分身数字人模型资产ID。
        :type model_asset_id: str
        :param human_image: 人物照片，需要Base64编码。照片分辨率不超过1080P。
        :type human_image: str
        :param voice_config: 
        :type voice_config: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        :param video_config: 
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        :param shoot_scripts: 拍摄脚本列表。
        :type shoot_scripts: list[:class:`huaweicloudsdkmetastudio.v1.ShootScriptItem`]
        :param output_asset_config: 
        :type output_asset_config: :class:`huaweicloudsdkmetastudio.v1.OutputAssetConfig`
        :param background_music_config: 
        :type background_music_config: :class:`huaweicloudsdkmetastudio.v1.BackgroundMusicConfig`
        """
        
        

        self._script_id = None
        self._video_making_type = None
        self._model_asset_id = None
        self._human_image = None
        self._voice_config = None
        self._video_config = None
        self._shoot_scripts = None
        self._output_asset_config = None
        self._background_music_config = None
        self.discriminator = None

        if script_id is not None:
            self.script_id = script_id
        if video_making_type is not None:
            self.video_making_type = video_making_type
        if model_asset_id is not None:
            self.model_asset_id = model_asset_id
        if human_image is not None:
            self.human_image = human_image
        if voice_config is not None:
            self.voice_config = voice_config
        if video_config is not None:
            self.video_config = video_config
        if shoot_scripts is not None:
            self.shoot_scripts = shoot_scripts
        if output_asset_config is not None:
            self.output_asset_config = output_asset_config
        if background_music_config is not None:
            self.background_music_config = background_music_config

    @property
    def script_id(self):
        """Gets the script_id of this Create2DDigitalHumanVideoReq.

        剧本ID。 > * 如果填写了script_id，model_asset_id、voice_config、scene_asset_id、video_config、shoot_scripts可以不填，以脚本中的配置为准。 > * 如果填写了script_id，并且同时也填写了model_asset_id、voice_config、scene_asset_id、video_config、shoot_scripts则以本接口中的配置为准。

        :return: The script_id of this Create2DDigitalHumanVideoReq.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        """Sets the script_id of this Create2DDigitalHumanVideoReq.

        剧本ID。 > * 如果填写了script_id，model_asset_id、voice_config、scene_asset_id、video_config、shoot_scripts可以不填，以脚本中的配置为准。 > * 如果填写了script_id，并且同时也填写了model_asset_id、voice_config、scene_asset_id、video_config、shoot_scripts则以本接口中的配置为准。

        :param script_id: The script_id of this Create2DDigitalHumanVideoReq.
        :type script_id: str
        """
        self._script_id = script_id

    @property
    def video_making_type(self):
        """Gets the video_making_type of this Create2DDigitalHumanVideoReq.

        视频生成类型。该参数取值是MODEL时，model_asset_id必填；取值是PICTURE时，human_image必填。 * MODEL：通过分数数字人模型生成视频 * PICTURE： 通过单张照片生成视频

        :return: The video_making_type of this Create2DDigitalHumanVideoReq.
        :rtype: str
        """
        return self._video_making_type

    @video_making_type.setter
    def video_making_type(self, video_making_type):
        """Sets the video_making_type of this Create2DDigitalHumanVideoReq.

        视频生成类型。该参数取值是MODEL时，model_asset_id必填；取值是PICTURE时，human_image必填。 * MODEL：通过分数数字人模型生成视频 * PICTURE： 通过单张照片生成视频

        :param video_making_type: The video_making_type of this Create2DDigitalHumanVideoReq.
        :type video_making_type: str
        """
        self._video_making_type = video_making_type

    @property
    def model_asset_id(self):
        """Gets the model_asset_id of this Create2DDigitalHumanVideoReq.

        分身数字人模型资产ID。

        :return: The model_asset_id of this Create2DDigitalHumanVideoReq.
        :rtype: str
        """
        return self._model_asset_id

    @model_asset_id.setter
    def model_asset_id(self, model_asset_id):
        """Sets the model_asset_id of this Create2DDigitalHumanVideoReq.

        分身数字人模型资产ID。

        :param model_asset_id: The model_asset_id of this Create2DDigitalHumanVideoReq.
        :type model_asset_id: str
        """
        self._model_asset_id = model_asset_id

    @property
    def human_image(self):
        """Gets the human_image of this Create2DDigitalHumanVideoReq.

        人物照片，需要Base64编码。照片分辨率不超过1080P。

        :return: The human_image of this Create2DDigitalHumanVideoReq.
        :rtype: str
        """
        return self._human_image

    @human_image.setter
    def human_image(self, human_image):
        """Sets the human_image of this Create2DDigitalHumanVideoReq.

        人物照片，需要Base64编码。照片分辨率不超过1080P。

        :param human_image: The human_image of this Create2DDigitalHumanVideoReq.
        :type human_image: str
        """
        self._human_image = human_image

    @property
    def voice_config(self):
        """Gets the voice_config of this Create2DDigitalHumanVideoReq.

        :return: The voice_config of this Create2DDigitalHumanVideoReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        """
        return self._voice_config

    @voice_config.setter
    def voice_config(self, voice_config):
        """Sets the voice_config of this Create2DDigitalHumanVideoReq.

        :param voice_config: The voice_config of this Create2DDigitalHumanVideoReq.
        :type voice_config: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        """
        self._voice_config = voice_config

    @property
    def video_config(self):
        """Gets the video_config of this Create2DDigitalHumanVideoReq.

        :return: The video_config of this Create2DDigitalHumanVideoReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        """
        return self._video_config

    @video_config.setter
    def video_config(self, video_config):
        """Sets the video_config of this Create2DDigitalHumanVideoReq.

        :param video_config: The video_config of this Create2DDigitalHumanVideoReq.
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        """
        self._video_config = video_config

    @property
    def shoot_scripts(self):
        """Gets the shoot_scripts of this Create2DDigitalHumanVideoReq.

        拍摄脚本列表。

        :return: The shoot_scripts of this Create2DDigitalHumanVideoReq.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.ShootScriptItem`]
        """
        return self._shoot_scripts

    @shoot_scripts.setter
    def shoot_scripts(self, shoot_scripts):
        """Sets the shoot_scripts of this Create2DDigitalHumanVideoReq.

        拍摄脚本列表。

        :param shoot_scripts: The shoot_scripts of this Create2DDigitalHumanVideoReq.
        :type shoot_scripts: list[:class:`huaweicloudsdkmetastudio.v1.ShootScriptItem`]
        """
        self._shoot_scripts = shoot_scripts

    @property
    def output_asset_config(self):
        """Gets the output_asset_config of this Create2DDigitalHumanVideoReq.

        :return: The output_asset_config of this Create2DDigitalHumanVideoReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.OutputAssetConfig`
        """
        return self._output_asset_config

    @output_asset_config.setter
    def output_asset_config(self, output_asset_config):
        """Sets the output_asset_config of this Create2DDigitalHumanVideoReq.

        :param output_asset_config: The output_asset_config of this Create2DDigitalHumanVideoReq.
        :type output_asset_config: :class:`huaweicloudsdkmetastudio.v1.OutputAssetConfig`
        """
        self._output_asset_config = output_asset_config

    @property
    def background_music_config(self):
        """Gets the background_music_config of this Create2DDigitalHumanVideoReq.

        :return: The background_music_config of this Create2DDigitalHumanVideoReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.BackgroundMusicConfig`
        """
        return self._background_music_config

    @background_music_config.setter
    def background_music_config(self, background_music_config):
        """Sets the background_music_config of this Create2DDigitalHumanVideoReq.

        :param background_music_config: The background_music_config of this Create2DDigitalHumanVideoReq.
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
        if not isinstance(other, Create2DDigitalHumanVideoReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
