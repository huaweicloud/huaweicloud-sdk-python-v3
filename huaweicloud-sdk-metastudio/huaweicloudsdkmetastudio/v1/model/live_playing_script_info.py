# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LivePlayingScriptInfo:

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
        'model_asset_id': 'str',
        'shoot_scripts': 'list[LivePlayingShootScriptItem]'
    }

    attribute_map = {
        'script_name': 'script_name',
        'model_asset_id': 'model_asset_id',
        'shoot_scripts': 'shoot_scripts'
    }

    def __init__(self, script_name=None, model_asset_id=None, shoot_scripts=None):
        r"""LivePlayingScriptInfo

        The model defined in huaweicloud sdk

        :param script_name: 剧本名称
        :type script_name: str
        :param model_asset_id: 数字人模型资产ID，可以从资产库中查询。
        :type model_asset_id: str
        :param shoot_scripts: 拍摄脚本列表。
        :type shoot_scripts: list[:class:`huaweicloudsdkmetastudio.v1.LivePlayingShootScriptItem`]
        """
        
        

        self._script_name = None
        self._model_asset_id = None
        self._shoot_scripts = None
        self.discriminator = None

        if script_name is not None:
            self.script_name = script_name
        if model_asset_id is not None:
            self.model_asset_id = model_asset_id
        if shoot_scripts is not None:
            self.shoot_scripts = shoot_scripts

    @property
    def script_name(self):
        r"""Gets the script_name of this LivePlayingScriptInfo.

        剧本名称

        :return: The script_name of this LivePlayingScriptInfo.
        :rtype: str
        """
        return self._script_name

    @script_name.setter
    def script_name(self, script_name):
        r"""Sets the script_name of this LivePlayingScriptInfo.

        剧本名称

        :param script_name: The script_name of this LivePlayingScriptInfo.
        :type script_name: str
        """
        self._script_name = script_name

    @property
    def model_asset_id(self):
        r"""Gets the model_asset_id of this LivePlayingScriptInfo.

        数字人模型资产ID，可以从资产库中查询。

        :return: The model_asset_id of this LivePlayingScriptInfo.
        :rtype: str
        """
        return self._model_asset_id

    @model_asset_id.setter
    def model_asset_id(self, model_asset_id):
        r"""Sets the model_asset_id of this LivePlayingScriptInfo.

        数字人模型资产ID，可以从资产库中查询。

        :param model_asset_id: The model_asset_id of this LivePlayingScriptInfo.
        :type model_asset_id: str
        """
        self._model_asset_id = model_asset_id

    @property
    def shoot_scripts(self):
        r"""Gets the shoot_scripts of this LivePlayingScriptInfo.

        拍摄脚本列表。

        :return: The shoot_scripts of this LivePlayingScriptInfo.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.LivePlayingShootScriptItem`]
        """
        return self._shoot_scripts

    @shoot_scripts.setter
    def shoot_scripts(self, shoot_scripts):
        r"""Sets the shoot_scripts of this LivePlayingScriptInfo.

        拍摄脚本列表。

        :param shoot_scripts: The shoot_scripts of this LivePlayingScriptInfo.
        :type shoot_scripts: list[:class:`huaweicloudsdkmetastudio.v1.LivePlayingShootScriptItem`]
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
        if not isinstance(other, LivePlayingScriptInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
