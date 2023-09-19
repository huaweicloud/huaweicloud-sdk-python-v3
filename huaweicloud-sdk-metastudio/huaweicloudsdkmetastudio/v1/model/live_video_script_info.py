# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LiveVideoScriptInfo:

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
        'dh_id': 'str',
        'model_asset_id': 'str',
        'voice_config': 'VoiceConfig',
        'background_config': 'list[BackgroundConfigInfo]',
        'layer_config': 'list[LayerConfig]',
        'shoot_scripts': 'list[LiveShootScriptItem]'
    }

    attribute_map = {
        'script_name': 'script_name',
        'script_description': 'script_description',
        'dh_id': 'dh_id',
        'model_asset_id': 'model_asset_id',
        'voice_config': 'voice_config',
        'background_config': 'background_config',
        'layer_config': 'layer_config',
        'shoot_scripts': 'shoot_scripts'
    }

    def __init__(self, script_name=None, script_description=None, dh_id=None, model_asset_id=None, voice_config=None, background_config=None, layer_config=None, shoot_scripts=None):
        """LiveVideoScriptInfo

        The model defined in huaweicloud sdk

        :param script_name: 剧本名称
        :type script_name: str
        :param script_description: 剧本描述。
        :type script_description: str
        :param dh_id: 数字人ID。对应形象和音色组合。
        :type dh_id: str
        :param model_asset_id: 数字人模型资产ID。
        :type model_asset_id: str
        :param voice_config: 
        :type voice_config: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        :param background_config: 背景配置。
        :type background_config: list[:class:`huaweicloudsdkmetastudio.v1.BackgroundConfigInfo`]
        :param layer_config: 图层配置。
        :type layer_config: list[:class:`huaweicloudsdkmetastudio.v1.LayerConfig`]
        :param shoot_scripts: 拍摄脚本列表。
        :type shoot_scripts: list[:class:`huaweicloudsdkmetastudio.v1.LiveShootScriptItem`]
        """
        
        

        self._script_name = None
        self._script_description = None
        self._dh_id = None
        self._model_asset_id = None
        self._voice_config = None
        self._background_config = None
        self._layer_config = None
        self._shoot_scripts = None
        self.discriminator = None

        self.script_name = script_name
        if script_description is not None:
            self.script_description = script_description
        if dh_id is not None:
            self.dh_id = dh_id
        if model_asset_id is not None:
            self.model_asset_id = model_asset_id
        if voice_config is not None:
            self.voice_config = voice_config
        if background_config is not None:
            self.background_config = background_config
        if layer_config is not None:
            self.layer_config = layer_config
        if shoot_scripts is not None:
            self.shoot_scripts = shoot_scripts

    @property
    def script_name(self):
        """Gets the script_name of this LiveVideoScriptInfo.

        剧本名称

        :return: The script_name of this LiveVideoScriptInfo.
        :rtype: str
        """
        return self._script_name

    @script_name.setter
    def script_name(self, script_name):
        """Sets the script_name of this LiveVideoScriptInfo.

        剧本名称

        :param script_name: The script_name of this LiveVideoScriptInfo.
        :type script_name: str
        """
        self._script_name = script_name

    @property
    def script_description(self):
        """Gets the script_description of this LiveVideoScriptInfo.

        剧本描述。

        :return: The script_description of this LiveVideoScriptInfo.
        :rtype: str
        """
        return self._script_description

    @script_description.setter
    def script_description(self, script_description):
        """Sets the script_description of this LiveVideoScriptInfo.

        剧本描述。

        :param script_description: The script_description of this LiveVideoScriptInfo.
        :type script_description: str
        """
        self._script_description = script_description

    @property
    def dh_id(self):
        """Gets the dh_id of this LiveVideoScriptInfo.

        数字人ID。对应形象和音色组合。

        :return: The dh_id of this LiveVideoScriptInfo.
        :rtype: str
        """
        return self._dh_id

    @dh_id.setter
    def dh_id(self, dh_id):
        """Sets the dh_id of this LiveVideoScriptInfo.

        数字人ID。对应形象和音色组合。

        :param dh_id: The dh_id of this LiveVideoScriptInfo.
        :type dh_id: str
        """
        self._dh_id = dh_id

    @property
    def model_asset_id(self):
        """Gets the model_asset_id of this LiveVideoScriptInfo.

        数字人模型资产ID。

        :return: The model_asset_id of this LiveVideoScriptInfo.
        :rtype: str
        """
        return self._model_asset_id

    @model_asset_id.setter
    def model_asset_id(self, model_asset_id):
        """Sets the model_asset_id of this LiveVideoScriptInfo.

        数字人模型资产ID。

        :param model_asset_id: The model_asset_id of this LiveVideoScriptInfo.
        :type model_asset_id: str
        """
        self._model_asset_id = model_asset_id

    @property
    def voice_config(self):
        """Gets the voice_config of this LiveVideoScriptInfo.

        :return: The voice_config of this LiveVideoScriptInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        """
        return self._voice_config

    @voice_config.setter
    def voice_config(self, voice_config):
        """Sets the voice_config of this LiveVideoScriptInfo.

        :param voice_config: The voice_config of this LiveVideoScriptInfo.
        :type voice_config: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        """
        self._voice_config = voice_config

    @property
    def background_config(self):
        """Gets the background_config of this LiveVideoScriptInfo.

        背景配置。

        :return: The background_config of this LiveVideoScriptInfo.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.BackgroundConfigInfo`]
        """
        return self._background_config

    @background_config.setter
    def background_config(self, background_config):
        """Sets the background_config of this LiveVideoScriptInfo.

        背景配置。

        :param background_config: The background_config of this LiveVideoScriptInfo.
        :type background_config: list[:class:`huaweicloudsdkmetastudio.v1.BackgroundConfigInfo`]
        """
        self._background_config = background_config

    @property
    def layer_config(self):
        """Gets the layer_config of this LiveVideoScriptInfo.

        图层配置。

        :return: The layer_config of this LiveVideoScriptInfo.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.LayerConfig`]
        """
        return self._layer_config

    @layer_config.setter
    def layer_config(self, layer_config):
        """Sets the layer_config of this LiveVideoScriptInfo.

        图层配置。

        :param layer_config: The layer_config of this LiveVideoScriptInfo.
        :type layer_config: list[:class:`huaweicloudsdkmetastudio.v1.LayerConfig`]
        """
        self._layer_config = layer_config

    @property
    def shoot_scripts(self):
        """Gets the shoot_scripts of this LiveVideoScriptInfo.

        拍摄脚本列表。

        :return: The shoot_scripts of this LiveVideoScriptInfo.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.LiveShootScriptItem`]
        """
        return self._shoot_scripts

    @shoot_scripts.setter
    def shoot_scripts(self, shoot_scripts):
        """Sets the shoot_scripts of this LiveVideoScriptInfo.

        拍摄脚本列表。

        :param shoot_scripts: The shoot_scripts of this LiveVideoScriptInfo.
        :type shoot_scripts: list[:class:`huaweicloudsdkmetastudio.v1.LiveShootScriptItem`]
        """
        self._shoot_scripts = shoot_scripts

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
        if not isinstance(other, LiveVideoScriptInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
