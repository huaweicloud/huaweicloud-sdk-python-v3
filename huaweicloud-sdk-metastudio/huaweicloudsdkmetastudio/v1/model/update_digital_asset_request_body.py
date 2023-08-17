# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDigitalAssetRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_name': 'str',
        'asset_description': 'str',
        'asset_type': 'str',
        'asset_state': 'str',
        'asset_owner': 'str',
        'tags': 'list[str]',
        'asset_extra_meta': 'AssetExtraMeta',
        'system_properties': 'list[SystemProperty]'
    }

    attribute_map = {
        'asset_name': 'asset_name',
        'asset_description': 'asset_description',
        'asset_type': 'asset_type',
        'asset_state': 'asset_state',
        'asset_owner': 'asset_owner',
        'tags': 'tags',
        'asset_extra_meta': 'asset_extra_meta',
        'system_properties': 'system_properties'
    }

    def __init__(self, asset_name=None, asset_description=None, asset_type=None, asset_state=None, asset_owner=None, tags=None, asset_extra_meta=None, system_properties=None):
        """UpdateDigitalAssetRequestBody

        The model defined in huaweicloud sdk

        :param asset_name: 资产名称。
        :type asset_name: str
        :param asset_description: 资产描述。
        :type asset_description: str
        :param asset_type: 资产类型。 * HUMAN_MODEL：数字人模型 * VOICE_MODEL：音色模型（仅系统管理员可更新） * SCENE：场景模型 * ANIMATION：动作动画 * VIDEO：视频文件 * IMAGE：图片文件 * PPT：幻灯片文件 * MATERIAL：风格化素材 * NORMAL_MODEL: 普通模型 * COMMON_FILE：通用文件 * HUMAN_MODEL_2D:2D数字人网络模型 * BUSINESS_CARD_TEMPLET: 数字人名片模板 * MUSIC: 音乐
        :type asset_type: str
        :param asset_state: 资产状态。 * UNACTIVED：取消激活。未激活的资产不可用于其他业务 * ACTIVED：激活。激活后的资产可用于其他业务
        :type asset_state: str
        :param asset_owner: 项目ID。
        :type asset_owner: str
        :param tags: 标签列表。
        :type tags: list[str]
        :param asset_extra_meta: 
        :type asset_extra_meta: :class:`huaweicloudsdkmetastudio.v1.AssetExtraMeta`
        :param system_properties: 设置系统属性。
        :type system_properties: list[:class:`huaweicloudsdkmetastudio.v1.SystemProperty`]
        """
        
        

        self._asset_name = None
        self._asset_description = None
        self._asset_type = None
        self._asset_state = None
        self._asset_owner = None
        self._tags = None
        self._asset_extra_meta = None
        self._system_properties = None
        self.discriminator = None

        if asset_name is not None:
            self.asset_name = asset_name
        if asset_description is not None:
            self.asset_description = asset_description
        if asset_type is not None:
            self.asset_type = asset_type
        if asset_state is not None:
            self.asset_state = asset_state
        if asset_owner is not None:
            self.asset_owner = asset_owner
        if tags is not None:
            self.tags = tags
        if asset_extra_meta is not None:
            self.asset_extra_meta = asset_extra_meta
        if system_properties is not None:
            self.system_properties = system_properties

    @property
    def asset_name(self):
        """Gets the asset_name of this UpdateDigitalAssetRequestBody.

        资产名称。

        :return: The asset_name of this UpdateDigitalAssetRequestBody.
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        """Sets the asset_name of this UpdateDigitalAssetRequestBody.

        资产名称。

        :param asset_name: The asset_name of this UpdateDigitalAssetRequestBody.
        :type asset_name: str
        """
        self._asset_name = asset_name

    @property
    def asset_description(self):
        """Gets the asset_description of this UpdateDigitalAssetRequestBody.

        资产描述。

        :return: The asset_description of this UpdateDigitalAssetRequestBody.
        :rtype: str
        """
        return self._asset_description

    @asset_description.setter
    def asset_description(self, asset_description):
        """Sets the asset_description of this UpdateDigitalAssetRequestBody.

        资产描述。

        :param asset_description: The asset_description of this UpdateDigitalAssetRequestBody.
        :type asset_description: str
        """
        self._asset_description = asset_description

    @property
    def asset_type(self):
        """Gets the asset_type of this UpdateDigitalAssetRequestBody.

        资产类型。 * HUMAN_MODEL：数字人模型 * VOICE_MODEL：音色模型（仅系统管理员可更新） * SCENE：场景模型 * ANIMATION：动作动画 * VIDEO：视频文件 * IMAGE：图片文件 * PPT：幻灯片文件 * MATERIAL：风格化素材 * NORMAL_MODEL: 普通模型 * COMMON_FILE：通用文件 * HUMAN_MODEL_2D:2D数字人网络模型 * BUSINESS_CARD_TEMPLET: 数字人名片模板 * MUSIC: 音乐

        :return: The asset_type of this UpdateDigitalAssetRequestBody.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        """Sets the asset_type of this UpdateDigitalAssetRequestBody.

        资产类型。 * HUMAN_MODEL：数字人模型 * VOICE_MODEL：音色模型（仅系统管理员可更新） * SCENE：场景模型 * ANIMATION：动作动画 * VIDEO：视频文件 * IMAGE：图片文件 * PPT：幻灯片文件 * MATERIAL：风格化素材 * NORMAL_MODEL: 普通模型 * COMMON_FILE：通用文件 * HUMAN_MODEL_2D:2D数字人网络模型 * BUSINESS_CARD_TEMPLET: 数字人名片模板 * MUSIC: 音乐

        :param asset_type: The asset_type of this UpdateDigitalAssetRequestBody.
        :type asset_type: str
        """
        self._asset_type = asset_type

    @property
    def asset_state(self):
        """Gets the asset_state of this UpdateDigitalAssetRequestBody.

        资产状态。 * UNACTIVED：取消激活。未激活的资产不可用于其他业务 * ACTIVED：激活。激活后的资产可用于其他业务

        :return: The asset_state of this UpdateDigitalAssetRequestBody.
        :rtype: str
        """
        return self._asset_state

    @asset_state.setter
    def asset_state(self, asset_state):
        """Sets the asset_state of this UpdateDigitalAssetRequestBody.

        资产状态。 * UNACTIVED：取消激活。未激活的资产不可用于其他业务 * ACTIVED：激活。激活后的资产可用于其他业务

        :param asset_state: The asset_state of this UpdateDigitalAssetRequestBody.
        :type asset_state: str
        """
        self._asset_state = asset_state

    @property
    def asset_owner(self):
        """Gets the asset_owner of this UpdateDigitalAssetRequestBody.

        项目ID。

        :return: The asset_owner of this UpdateDigitalAssetRequestBody.
        :rtype: str
        """
        return self._asset_owner

    @asset_owner.setter
    def asset_owner(self, asset_owner):
        """Sets the asset_owner of this UpdateDigitalAssetRequestBody.

        项目ID。

        :param asset_owner: The asset_owner of this UpdateDigitalAssetRequestBody.
        :type asset_owner: str
        """
        self._asset_owner = asset_owner

    @property
    def tags(self):
        """Gets the tags of this UpdateDigitalAssetRequestBody.

        标签列表。

        :return: The tags of this UpdateDigitalAssetRequestBody.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UpdateDigitalAssetRequestBody.

        标签列表。

        :param tags: The tags of this UpdateDigitalAssetRequestBody.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def asset_extra_meta(self):
        """Gets the asset_extra_meta of this UpdateDigitalAssetRequestBody.

        :return: The asset_extra_meta of this UpdateDigitalAssetRequestBody.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.AssetExtraMeta`
        """
        return self._asset_extra_meta

    @asset_extra_meta.setter
    def asset_extra_meta(self, asset_extra_meta):
        """Sets the asset_extra_meta of this UpdateDigitalAssetRequestBody.

        :param asset_extra_meta: The asset_extra_meta of this UpdateDigitalAssetRequestBody.
        :type asset_extra_meta: :class:`huaweicloudsdkmetastudio.v1.AssetExtraMeta`
        """
        self._asset_extra_meta = asset_extra_meta

    @property
    def system_properties(self):
        """Gets the system_properties of this UpdateDigitalAssetRequestBody.

        设置系统属性。

        :return: The system_properties of this UpdateDigitalAssetRequestBody.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.SystemProperty`]
        """
        return self._system_properties

    @system_properties.setter
    def system_properties(self, system_properties):
        """Sets the system_properties of this UpdateDigitalAssetRequestBody.

        设置系统属性。

        :param system_properties: The system_properties of this UpdateDigitalAssetRequestBody.
        :type system_properties: list[:class:`huaweicloudsdkmetastudio.v1.SystemProperty`]
        """
        self._system_properties = system_properties

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
        if not isinstance(other, UpdateDigitalAssetRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
