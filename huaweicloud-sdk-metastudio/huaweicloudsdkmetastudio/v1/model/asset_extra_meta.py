# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssetExtraMeta:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'voice_model_meta': 'VoiceModelAssetMeta',
        'ppt_meta': 'PPTAssetMeta',
        'material_meta': 'MaterialAssetMeta',
        'human_model_2d_meta': 'HumanModel2DAssetMeta',
        'image_meta': 'ImageAssetMeta',
        'video_meta': 'VideoAssetMeta',
        'audio_meta': 'AudioAssetMeta'
    }

    attribute_map = {
        'voice_model_meta': 'voice_model_meta',
        'ppt_meta': 'ppt_meta',
        'material_meta': 'material_meta',
        'human_model_2d_meta': 'human_model_2d_meta',
        'image_meta': 'image_meta',
        'video_meta': 'video_meta',
        'audio_meta': 'audio_meta'
    }

    def __init__(self, voice_model_meta=None, ppt_meta=None, material_meta=None, human_model_2d_meta=None, image_meta=None, video_meta=None, audio_meta=None):
        r"""AssetExtraMeta

        The model defined in huaweicloud sdk

        :param voice_model_meta: 
        :type voice_model_meta: :class:`huaweicloudsdkmetastudio.v1.VoiceModelAssetMeta`
        :param ppt_meta: 
        :type ppt_meta: :class:`huaweicloudsdkmetastudio.v1.PPTAssetMeta`
        :param material_meta: 
        :type material_meta: :class:`huaweicloudsdkmetastudio.v1.MaterialAssetMeta`
        :param human_model_2d_meta: 
        :type human_model_2d_meta: :class:`huaweicloudsdkmetastudio.v1.HumanModel2DAssetMeta`
        :param image_meta: 
        :type image_meta: :class:`huaweicloudsdkmetastudio.v1.ImageAssetMeta`
        :param video_meta: 
        :type video_meta: :class:`huaweicloudsdkmetastudio.v1.VideoAssetMeta`
        :param audio_meta: 
        :type audio_meta: :class:`huaweicloudsdkmetastudio.v1.AudioAssetMeta`
        """
        
        

        self._voice_model_meta = None
        self._ppt_meta = None
        self._material_meta = None
        self._human_model_2d_meta = None
        self._image_meta = None
        self._video_meta = None
        self._audio_meta = None
        self.discriminator = None

        if voice_model_meta is not None:
            self.voice_model_meta = voice_model_meta
        if ppt_meta is not None:
            self.ppt_meta = ppt_meta
        if material_meta is not None:
            self.material_meta = material_meta
        if human_model_2d_meta is not None:
            self.human_model_2d_meta = human_model_2d_meta
        if image_meta is not None:
            self.image_meta = image_meta
        if video_meta is not None:
            self.video_meta = video_meta
        if audio_meta is not None:
            self.audio_meta = audio_meta

    @property
    def voice_model_meta(self):
        r"""Gets the voice_model_meta of this AssetExtraMeta.

        :return: The voice_model_meta of this AssetExtraMeta.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VoiceModelAssetMeta`
        """
        return self._voice_model_meta

    @voice_model_meta.setter
    def voice_model_meta(self, voice_model_meta):
        r"""Sets the voice_model_meta of this AssetExtraMeta.

        :param voice_model_meta: The voice_model_meta of this AssetExtraMeta.
        :type voice_model_meta: :class:`huaweicloudsdkmetastudio.v1.VoiceModelAssetMeta`
        """
        self._voice_model_meta = voice_model_meta

    @property
    def ppt_meta(self):
        r"""Gets the ppt_meta of this AssetExtraMeta.

        :return: The ppt_meta of this AssetExtraMeta.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.PPTAssetMeta`
        """
        return self._ppt_meta

    @ppt_meta.setter
    def ppt_meta(self, ppt_meta):
        r"""Sets the ppt_meta of this AssetExtraMeta.

        :param ppt_meta: The ppt_meta of this AssetExtraMeta.
        :type ppt_meta: :class:`huaweicloudsdkmetastudio.v1.PPTAssetMeta`
        """
        self._ppt_meta = ppt_meta

    @property
    def material_meta(self):
        r"""Gets the material_meta of this AssetExtraMeta.

        :return: The material_meta of this AssetExtraMeta.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.MaterialAssetMeta`
        """
        return self._material_meta

    @material_meta.setter
    def material_meta(self, material_meta):
        r"""Sets the material_meta of this AssetExtraMeta.

        :param material_meta: The material_meta of this AssetExtraMeta.
        :type material_meta: :class:`huaweicloudsdkmetastudio.v1.MaterialAssetMeta`
        """
        self._material_meta = material_meta

    @property
    def human_model_2d_meta(self):
        r"""Gets the human_model_2d_meta of this AssetExtraMeta.

        :return: The human_model_2d_meta of this AssetExtraMeta.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.HumanModel2DAssetMeta`
        """
        return self._human_model_2d_meta

    @human_model_2d_meta.setter
    def human_model_2d_meta(self, human_model_2d_meta):
        r"""Sets the human_model_2d_meta of this AssetExtraMeta.

        :param human_model_2d_meta: The human_model_2d_meta of this AssetExtraMeta.
        :type human_model_2d_meta: :class:`huaweicloudsdkmetastudio.v1.HumanModel2DAssetMeta`
        """
        self._human_model_2d_meta = human_model_2d_meta

    @property
    def image_meta(self):
        r"""Gets the image_meta of this AssetExtraMeta.

        :return: The image_meta of this AssetExtraMeta.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ImageAssetMeta`
        """
        return self._image_meta

    @image_meta.setter
    def image_meta(self, image_meta):
        r"""Sets the image_meta of this AssetExtraMeta.

        :param image_meta: The image_meta of this AssetExtraMeta.
        :type image_meta: :class:`huaweicloudsdkmetastudio.v1.ImageAssetMeta`
        """
        self._image_meta = image_meta

    @property
    def video_meta(self):
        r"""Gets the video_meta of this AssetExtraMeta.

        :return: The video_meta of this AssetExtraMeta.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VideoAssetMeta`
        """
        return self._video_meta

    @video_meta.setter
    def video_meta(self, video_meta):
        r"""Sets the video_meta of this AssetExtraMeta.

        :param video_meta: The video_meta of this AssetExtraMeta.
        :type video_meta: :class:`huaweicloudsdkmetastudio.v1.VideoAssetMeta`
        """
        self._video_meta = video_meta

    @property
    def audio_meta(self):
        r"""Gets the audio_meta of this AssetExtraMeta.

        :return: The audio_meta of this AssetExtraMeta.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.AudioAssetMeta`
        """
        return self._audio_meta

    @audio_meta.setter
    def audio_meta(self, audio_meta):
        r"""Sets the audio_meta of this AssetExtraMeta.

        :param audio_meta: The audio_meta of this AssetExtraMeta.
        :type audio_meta: :class:`huaweicloudsdkmetastudio.v1.AudioAssetMeta`
        """
        self._audio_meta = audio_meta

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
        if not isinstance(other, AssetExtraMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
