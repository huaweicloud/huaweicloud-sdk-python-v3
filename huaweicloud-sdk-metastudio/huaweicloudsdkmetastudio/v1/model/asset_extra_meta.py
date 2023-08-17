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
        'human_model_meta': 'HumanModelAssetMeta',
        'voice_model_meta': 'VoiceModelAssetMeta',
        'ppt_meta': 'PPTAssetMeta',
        'animation_meta': 'AnimationAssetMeta',
        'scene_meta': 'SceneAssetMeta',
        'material_meta': 'MaterialAssetMeta',
        'human_model_2d_meta': 'HumanModel2DAssetMeta'
    }

    attribute_map = {
        'human_model_meta': 'human_model_meta',
        'voice_model_meta': 'voice_model_meta',
        'ppt_meta': 'ppt_meta',
        'animation_meta': 'animation_meta',
        'scene_meta': 'scene_meta',
        'material_meta': 'material_meta',
        'human_model_2d_meta': 'human_model_2d_meta'
    }

    def __init__(self, human_model_meta=None, voice_model_meta=None, ppt_meta=None, animation_meta=None, scene_meta=None, material_meta=None, human_model_2d_meta=None):
        """AssetExtraMeta

        The model defined in huaweicloud sdk

        :param human_model_meta: 
        :type human_model_meta: :class:`huaweicloudsdkmetastudio.v1.HumanModelAssetMeta`
        :param voice_model_meta: 
        :type voice_model_meta: :class:`huaweicloudsdkmetastudio.v1.VoiceModelAssetMeta`
        :param ppt_meta: 
        :type ppt_meta: :class:`huaweicloudsdkmetastudio.v1.PPTAssetMeta`
        :param animation_meta: 
        :type animation_meta: :class:`huaweicloudsdkmetastudio.v1.AnimationAssetMeta`
        :param scene_meta: 
        :type scene_meta: :class:`huaweicloudsdkmetastudio.v1.SceneAssetMeta`
        :param material_meta: 
        :type material_meta: :class:`huaweicloudsdkmetastudio.v1.MaterialAssetMeta`
        :param human_model_2d_meta: 
        :type human_model_2d_meta: :class:`huaweicloudsdkmetastudio.v1.HumanModel2DAssetMeta`
        """
        
        

        self._human_model_meta = None
        self._voice_model_meta = None
        self._ppt_meta = None
        self._animation_meta = None
        self._scene_meta = None
        self._material_meta = None
        self._human_model_2d_meta = None
        self.discriminator = None

        if human_model_meta is not None:
            self.human_model_meta = human_model_meta
        if voice_model_meta is not None:
            self.voice_model_meta = voice_model_meta
        if ppt_meta is not None:
            self.ppt_meta = ppt_meta
        if animation_meta is not None:
            self.animation_meta = animation_meta
        if scene_meta is not None:
            self.scene_meta = scene_meta
        if material_meta is not None:
            self.material_meta = material_meta
        if human_model_2d_meta is not None:
            self.human_model_2d_meta = human_model_2d_meta

    @property
    def human_model_meta(self):
        """Gets the human_model_meta of this AssetExtraMeta.

        :return: The human_model_meta of this AssetExtraMeta.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.HumanModelAssetMeta`
        """
        return self._human_model_meta

    @human_model_meta.setter
    def human_model_meta(self, human_model_meta):
        """Sets the human_model_meta of this AssetExtraMeta.

        :param human_model_meta: The human_model_meta of this AssetExtraMeta.
        :type human_model_meta: :class:`huaweicloudsdkmetastudio.v1.HumanModelAssetMeta`
        """
        self._human_model_meta = human_model_meta

    @property
    def voice_model_meta(self):
        """Gets the voice_model_meta of this AssetExtraMeta.

        :return: The voice_model_meta of this AssetExtraMeta.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VoiceModelAssetMeta`
        """
        return self._voice_model_meta

    @voice_model_meta.setter
    def voice_model_meta(self, voice_model_meta):
        """Sets the voice_model_meta of this AssetExtraMeta.

        :param voice_model_meta: The voice_model_meta of this AssetExtraMeta.
        :type voice_model_meta: :class:`huaweicloudsdkmetastudio.v1.VoiceModelAssetMeta`
        """
        self._voice_model_meta = voice_model_meta

    @property
    def ppt_meta(self):
        """Gets the ppt_meta of this AssetExtraMeta.

        :return: The ppt_meta of this AssetExtraMeta.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.PPTAssetMeta`
        """
        return self._ppt_meta

    @ppt_meta.setter
    def ppt_meta(self, ppt_meta):
        """Sets the ppt_meta of this AssetExtraMeta.

        :param ppt_meta: The ppt_meta of this AssetExtraMeta.
        :type ppt_meta: :class:`huaweicloudsdkmetastudio.v1.PPTAssetMeta`
        """
        self._ppt_meta = ppt_meta

    @property
    def animation_meta(self):
        """Gets the animation_meta of this AssetExtraMeta.

        :return: The animation_meta of this AssetExtraMeta.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.AnimationAssetMeta`
        """
        return self._animation_meta

    @animation_meta.setter
    def animation_meta(self, animation_meta):
        """Sets the animation_meta of this AssetExtraMeta.

        :param animation_meta: The animation_meta of this AssetExtraMeta.
        :type animation_meta: :class:`huaweicloudsdkmetastudio.v1.AnimationAssetMeta`
        """
        self._animation_meta = animation_meta

    @property
    def scene_meta(self):
        """Gets the scene_meta of this AssetExtraMeta.

        :return: The scene_meta of this AssetExtraMeta.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.SceneAssetMeta`
        """
        return self._scene_meta

    @scene_meta.setter
    def scene_meta(self, scene_meta):
        """Sets the scene_meta of this AssetExtraMeta.

        :param scene_meta: The scene_meta of this AssetExtraMeta.
        :type scene_meta: :class:`huaweicloudsdkmetastudio.v1.SceneAssetMeta`
        """
        self._scene_meta = scene_meta

    @property
    def material_meta(self):
        """Gets the material_meta of this AssetExtraMeta.

        :return: The material_meta of this AssetExtraMeta.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.MaterialAssetMeta`
        """
        return self._material_meta

    @material_meta.setter
    def material_meta(self, material_meta):
        """Sets the material_meta of this AssetExtraMeta.

        :param material_meta: The material_meta of this AssetExtraMeta.
        :type material_meta: :class:`huaweicloudsdkmetastudio.v1.MaterialAssetMeta`
        """
        self._material_meta = material_meta

    @property
    def human_model_2d_meta(self):
        """Gets the human_model_2d_meta of this AssetExtraMeta.

        :return: The human_model_2d_meta of this AssetExtraMeta.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.HumanModel2DAssetMeta`
        """
        return self._human_model_2d_meta

    @human_model_2d_meta.setter
    def human_model_2d_meta(self, human_model_2d_meta):
        """Sets the human_model_2d_meta of this AssetExtraMeta.

        :param human_model_2d_meta: The human_model_2d_meta of this AssetExtraMeta.
        :type human_model_2d_meta: :class:`huaweicloudsdkmetastudio.v1.HumanModel2DAssetMeta`
        """
        self._human_model_2d_meta = human_model_2d_meta

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
