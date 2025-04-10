# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePhotoDigitalHumanVideoReq:

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
        'human_image': 'str',
        'voice_config': 'VoiceConfig',
        'video_config': 'PhotoVideoConfig',
        'shoot_scripts': 'list[ShootScriptItem]',
        'output_asset_config': 'OutputAssetConfig',
        'background_music_config': 'BackgroundMusicConfig',
        'review_config': 'ReviewConfig',
        'callback_config': 'CallBackConfig'
    }

    attribute_map = {
        'script_id': 'script_id',
        'human_image': 'human_image',
        'voice_config': 'voice_config',
        'video_config': 'video_config',
        'shoot_scripts': 'shoot_scripts',
        'output_asset_config': 'output_asset_config',
        'background_music_config': 'background_music_config',
        'review_config': 'review_config',
        'callback_config': 'callback_config'
    }

    def __init__(self, script_id=None, human_image=None, voice_config=None, video_config=None, shoot_scripts=None, output_asset_config=None, background_music_config=None, review_config=None, callback_config=None):
        r"""CreatePhotoDigitalHumanVideoReq

        The model defined in huaweicloud sdk

        :param script_id: 剧本ID。 &gt; * 如果shoot_scripts中shoot_script.script_type为\&quot;TEXT\&quot;，则台词以shoot_scripts中的文本为准； &gt; * 如果shoot_scripts中shoot_script.script_type为\&quot;AUDIO\&quot;，则台词以script_id对应剧本中的音频为准。
        :type script_id: str
        :param human_image: 人物照片，需要Base64编码。照片分辨率不超过1080P。
        :type human_image: str
        :param voice_config: 
        :type voice_config: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        :param video_config: 
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.PhotoVideoConfig`
        :param shoot_scripts: 剧本列表。照片数字人仅支持传入一个剧本shoot_script，剧本参数仅支持shoot_script.script_type、shoot_script.text_config；
        :type shoot_scripts: list[:class:`huaweicloudsdkmetastudio.v1.ShootScriptItem`]
        :param output_asset_config: 
        :type output_asset_config: :class:`huaweicloudsdkmetastudio.v1.OutputAssetConfig`
        :param background_music_config: 
        :type background_music_config: :class:`huaweicloudsdkmetastudio.v1.BackgroundMusicConfig`
        :param review_config: 
        :type review_config: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        :param callback_config: 
        :type callback_config: :class:`huaweicloudsdkmetastudio.v1.CallBackConfig`
        """
        
        

        self._script_id = None
        self._human_image = None
        self._voice_config = None
        self._video_config = None
        self._shoot_scripts = None
        self._output_asset_config = None
        self._background_music_config = None
        self._review_config = None
        self._callback_config = None
        self.discriminator = None

        if script_id is not None:
            self.script_id = script_id
        self.human_image = human_image
        if voice_config is not None:
            self.voice_config = voice_config
        if video_config is not None:
            self.video_config = video_config
        self.shoot_scripts = shoot_scripts
        self.output_asset_config = output_asset_config
        if background_music_config is not None:
            self.background_music_config = background_music_config
        if review_config is not None:
            self.review_config = review_config
        if callback_config is not None:
            self.callback_config = callback_config

    @property
    def script_id(self):
        r"""Gets the script_id of this CreatePhotoDigitalHumanVideoReq.

        剧本ID。 > * 如果shoot_scripts中shoot_script.script_type为\"TEXT\"，则台词以shoot_scripts中的文本为准； > * 如果shoot_scripts中shoot_script.script_type为\"AUDIO\"，则台词以script_id对应剧本中的音频为准。

        :return: The script_id of this CreatePhotoDigitalHumanVideoReq.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        r"""Sets the script_id of this CreatePhotoDigitalHumanVideoReq.

        剧本ID。 > * 如果shoot_scripts中shoot_script.script_type为\"TEXT\"，则台词以shoot_scripts中的文本为准； > * 如果shoot_scripts中shoot_script.script_type为\"AUDIO\"，则台词以script_id对应剧本中的音频为准。

        :param script_id: The script_id of this CreatePhotoDigitalHumanVideoReq.
        :type script_id: str
        """
        self._script_id = script_id

    @property
    def human_image(self):
        r"""Gets the human_image of this CreatePhotoDigitalHumanVideoReq.

        人物照片，需要Base64编码。照片分辨率不超过1080P。

        :return: The human_image of this CreatePhotoDigitalHumanVideoReq.
        :rtype: str
        """
        return self._human_image

    @human_image.setter
    def human_image(self, human_image):
        r"""Sets the human_image of this CreatePhotoDigitalHumanVideoReq.

        人物照片，需要Base64编码。照片分辨率不超过1080P。

        :param human_image: The human_image of this CreatePhotoDigitalHumanVideoReq.
        :type human_image: str
        """
        self._human_image = human_image

    @property
    def voice_config(self):
        r"""Gets the voice_config of this CreatePhotoDigitalHumanVideoReq.

        :return: The voice_config of this CreatePhotoDigitalHumanVideoReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        """
        return self._voice_config

    @voice_config.setter
    def voice_config(self, voice_config):
        r"""Sets the voice_config of this CreatePhotoDigitalHumanVideoReq.

        :param voice_config: The voice_config of this CreatePhotoDigitalHumanVideoReq.
        :type voice_config: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        """
        self._voice_config = voice_config

    @property
    def video_config(self):
        r"""Gets the video_config of this CreatePhotoDigitalHumanVideoReq.

        :return: The video_config of this CreatePhotoDigitalHumanVideoReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.PhotoVideoConfig`
        """
        return self._video_config

    @video_config.setter
    def video_config(self, video_config):
        r"""Sets the video_config of this CreatePhotoDigitalHumanVideoReq.

        :param video_config: The video_config of this CreatePhotoDigitalHumanVideoReq.
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.PhotoVideoConfig`
        """
        self._video_config = video_config

    @property
    def shoot_scripts(self):
        r"""Gets the shoot_scripts of this CreatePhotoDigitalHumanVideoReq.

        剧本列表。照片数字人仅支持传入一个剧本shoot_script，剧本参数仅支持shoot_script.script_type、shoot_script.text_config；

        :return: The shoot_scripts of this CreatePhotoDigitalHumanVideoReq.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.ShootScriptItem`]
        """
        return self._shoot_scripts

    @shoot_scripts.setter
    def shoot_scripts(self, shoot_scripts):
        r"""Sets the shoot_scripts of this CreatePhotoDigitalHumanVideoReq.

        剧本列表。照片数字人仅支持传入一个剧本shoot_script，剧本参数仅支持shoot_script.script_type、shoot_script.text_config；

        :param shoot_scripts: The shoot_scripts of this CreatePhotoDigitalHumanVideoReq.
        :type shoot_scripts: list[:class:`huaweicloudsdkmetastudio.v1.ShootScriptItem`]
        """
        self._shoot_scripts = shoot_scripts

    @property
    def output_asset_config(self):
        r"""Gets the output_asset_config of this CreatePhotoDigitalHumanVideoReq.

        :return: The output_asset_config of this CreatePhotoDigitalHumanVideoReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.OutputAssetConfig`
        """
        return self._output_asset_config

    @output_asset_config.setter
    def output_asset_config(self, output_asset_config):
        r"""Sets the output_asset_config of this CreatePhotoDigitalHumanVideoReq.

        :param output_asset_config: The output_asset_config of this CreatePhotoDigitalHumanVideoReq.
        :type output_asset_config: :class:`huaweicloudsdkmetastudio.v1.OutputAssetConfig`
        """
        self._output_asset_config = output_asset_config

    @property
    def background_music_config(self):
        r"""Gets the background_music_config of this CreatePhotoDigitalHumanVideoReq.

        :return: The background_music_config of this CreatePhotoDigitalHumanVideoReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.BackgroundMusicConfig`
        """
        return self._background_music_config

    @background_music_config.setter
    def background_music_config(self, background_music_config):
        r"""Sets the background_music_config of this CreatePhotoDigitalHumanVideoReq.

        :param background_music_config: The background_music_config of this CreatePhotoDigitalHumanVideoReq.
        :type background_music_config: :class:`huaweicloudsdkmetastudio.v1.BackgroundMusicConfig`
        """
        self._background_music_config = background_music_config

    @property
    def review_config(self):
        r"""Gets the review_config of this CreatePhotoDigitalHumanVideoReq.

        :return: The review_config of this CreatePhotoDigitalHumanVideoReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        return self._review_config

    @review_config.setter
    def review_config(self, review_config):
        r"""Sets the review_config of this CreatePhotoDigitalHumanVideoReq.

        :param review_config: The review_config of this CreatePhotoDigitalHumanVideoReq.
        :type review_config: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        self._review_config = review_config

    @property
    def callback_config(self):
        r"""Gets the callback_config of this CreatePhotoDigitalHumanVideoReq.

        :return: The callback_config of this CreatePhotoDigitalHumanVideoReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CallBackConfig`
        """
        return self._callback_config

    @callback_config.setter
    def callback_config(self, callback_config):
        r"""Sets the callback_config of this CreatePhotoDigitalHumanVideoReq.

        :param callback_config: The callback_config of this CreatePhotoDigitalHumanVideoReq.
        :type callback_config: :class:`huaweicloudsdkmetastudio.v1.CallBackConfig`
        """
        self._callback_config = callback_config

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
        if not isinstance(other, CreatePhotoDigitalHumanVideoReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
