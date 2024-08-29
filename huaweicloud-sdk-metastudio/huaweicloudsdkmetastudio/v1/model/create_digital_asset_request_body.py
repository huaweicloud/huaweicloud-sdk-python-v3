# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDigitalAssetRequestBody:

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
        'asset_owner': 'str',
        'review_config': 'ReviewConfig',
        'tags': 'list[str]',
        'asset_extra_meta': 'AssetExtraMeta',
        'system_properties': 'list[SystemProperty]',
        'shared_config': 'AssetSharedConfig',
        'is_need_generate_cover': 'bool',
        'asset_order': 'int',
        'supported_service': 'list[SupportedServiceEnum]'
    }

    attribute_map = {
        'asset_name': 'asset_name',
        'asset_description': 'asset_description',
        'asset_type': 'asset_type',
        'asset_owner': 'asset_owner',
        'review_config': 'review_config',
        'tags': 'tags',
        'asset_extra_meta': 'asset_extra_meta',
        'system_properties': 'system_properties',
        'shared_config': 'shared_config',
        'is_need_generate_cover': 'is_need_generate_cover',
        'asset_order': 'asset_order',
        'supported_service': 'supported_service'
    }

    def __init__(self, asset_name=None, asset_description=None, asset_type=None, asset_owner=None, review_config=None, tags=None, asset_extra_meta=None, system_properties=None, shared_config=None, is_need_generate_cover=None, asset_order=None, supported_service=None):
        """CreateDigitalAssetRequestBody

        The model defined in huaweicloud sdk

        :param asset_name: 资产名称。
        :type asset_name: str
        :param asset_description: 资产描述。
        :type asset_description: str
        :param asset_type: 资产类型。  公共资产类型： * VOICE_MODEL：音色模型（仅系统管理员可上传，普通租户仅可查询） * VIDEO：视频文件 * IMAGE：图片文件 * PPT：幻灯片文件 * MUSIC: 音乐 * AUDIO: 音频 * COMMON_FILE：通用文件  分身数字人资产： * HUMAN_MODEL_2D: 分身数字人模型 * BUSINESS_CARD_TEMPLET: 数字人名片模板  3D数字人资产： * HUMAN_MODEL：3D数字人模型 * SCENE：场景模型 * ANIMATION：动作动画 * MATERIAL：风格化素材 * NORMAL_MODEL: 普通模型
        :type asset_type: str
        :param asset_owner: 项目ID。 &gt; * 仅管理员账号可设置此参数。
        :type asset_owner: str
        :param review_config: 
        :type review_config: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        :param tags: 标签列表。 &gt; 分身形象系统资产的tag定义如下： &gt; - 行业：NEWS,BUSINESS,E-COMMERCE,MARKETING,KNOWLEDGE,EDUCATION,SPORTS &gt; - 性别：MALE,FEMALE &gt; - 姿势：FULL-BODY,HALF-BODY,STANDING,SITTING,WALKING &gt; - 区域：ASIAN,WESTERN,MIDDLE-EASTERNER,AFRICAN,LATINO
        :type tags: list[str]
        :param asset_extra_meta: 
        :type asset_extra_meta: :class:`huaweicloudsdkmetastudio.v1.AssetExtraMeta`
        :param system_properties: 设置系统属性。
        :type system_properties: list[:class:`huaweicloudsdkmetastudio.v1.SystemProperty`]
        :param shared_config: 
        :type shared_config: :class:`huaweicloudsdkmetastudio.v1.AssetSharedConfig`
        :param is_need_generate_cover: 是否需要生成封面。
        :type is_need_generate_cover: bool
        :param asset_order: 展示顺序
        :type asset_order: int
        :param supported_service: 支持的业务类型。： * VIDEO_2D：分身数字人视频制作 * LIVE_2D：分身数字人直播 * CHAT_2D：分身数字人智能交互
        :type supported_service: list[:class:`huaweicloudsdkmetastudio.v1.SupportedServiceEnum`]
        """
        
        

        self._asset_name = None
        self._asset_description = None
        self._asset_type = None
        self._asset_owner = None
        self._review_config = None
        self._tags = None
        self._asset_extra_meta = None
        self._system_properties = None
        self._shared_config = None
        self._is_need_generate_cover = None
        self._asset_order = None
        self._supported_service = None
        self.discriminator = None

        self.asset_name = asset_name
        if asset_description is not None:
            self.asset_description = asset_description
        self.asset_type = asset_type
        if asset_owner is not None:
            self.asset_owner = asset_owner
        if review_config is not None:
            self.review_config = review_config
        if tags is not None:
            self.tags = tags
        if asset_extra_meta is not None:
            self.asset_extra_meta = asset_extra_meta
        if system_properties is not None:
            self.system_properties = system_properties
        if shared_config is not None:
            self.shared_config = shared_config
        if is_need_generate_cover is not None:
            self.is_need_generate_cover = is_need_generate_cover
        if asset_order is not None:
            self.asset_order = asset_order
        if supported_service is not None:
            self.supported_service = supported_service

    @property
    def asset_name(self):
        """Gets the asset_name of this CreateDigitalAssetRequestBody.

        资产名称。

        :return: The asset_name of this CreateDigitalAssetRequestBody.
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        """Sets the asset_name of this CreateDigitalAssetRequestBody.

        资产名称。

        :param asset_name: The asset_name of this CreateDigitalAssetRequestBody.
        :type asset_name: str
        """
        self._asset_name = asset_name

    @property
    def asset_description(self):
        """Gets the asset_description of this CreateDigitalAssetRequestBody.

        资产描述。

        :return: The asset_description of this CreateDigitalAssetRequestBody.
        :rtype: str
        """
        return self._asset_description

    @asset_description.setter
    def asset_description(self, asset_description):
        """Sets the asset_description of this CreateDigitalAssetRequestBody.

        资产描述。

        :param asset_description: The asset_description of this CreateDigitalAssetRequestBody.
        :type asset_description: str
        """
        self._asset_description = asset_description

    @property
    def asset_type(self):
        """Gets the asset_type of this CreateDigitalAssetRequestBody.

        资产类型。  公共资产类型： * VOICE_MODEL：音色模型（仅系统管理员可上传，普通租户仅可查询） * VIDEO：视频文件 * IMAGE：图片文件 * PPT：幻灯片文件 * MUSIC: 音乐 * AUDIO: 音频 * COMMON_FILE：通用文件  分身数字人资产： * HUMAN_MODEL_2D: 分身数字人模型 * BUSINESS_CARD_TEMPLET: 数字人名片模板  3D数字人资产： * HUMAN_MODEL：3D数字人模型 * SCENE：场景模型 * ANIMATION：动作动画 * MATERIAL：风格化素材 * NORMAL_MODEL: 普通模型

        :return: The asset_type of this CreateDigitalAssetRequestBody.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        """Sets the asset_type of this CreateDigitalAssetRequestBody.

        资产类型。  公共资产类型： * VOICE_MODEL：音色模型（仅系统管理员可上传，普通租户仅可查询） * VIDEO：视频文件 * IMAGE：图片文件 * PPT：幻灯片文件 * MUSIC: 音乐 * AUDIO: 音频 * COMMON_FILE：通用文件  分身数字人资产： * HUMAN_MODEL_2D: 分身数字人模型 * BUSINESS_CARD_TEMPLET: 数字人名片模板  3D数字人资产： * HUMAN_MODEL：3D数字人模型 * SCENE：场景模型 * ANIMATION：动作动画 * MATERIAL：风格化素材 * NORMAL_MODEL: 普通模型

        :param asset_type: The asset_type of this CreateDigitalAssetRequestBody.
        :type asset_type: str
        """
        self._asset_type = asset_type

    @property
    def asset_owner(self):
        """Gets the asset_owner of this CreateDigitalAssetRequestBody.

        项目ID。 > * 仅管理员账号可设置此参数。

        :return: The asset_owner of this CreateDigitalAssetRequestBody.
        :rtype: str
        """
        return self._asset_owner

    @asset_owner.setter
    def asset_owner(self, asset_owner):
        """Sets the asset_owner of this CreateDigitalAssetRequestBody.

        项目ID。 > * 仅管理员账号可设置此参数。

        :param asset_owner: The asset_owner of this CreateDigitalAssetRequestBody.
        :type asset_owner: str
        """
        self._asset_owner = asset_owner

    @property
    def review_config(self):
        """Gets the review_config of this CreateDigitalAssetRequestBody.

        :return: The review_config of this CreateDigitalAssetRequestBody.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        return self._review_config

    @review_config.setter
    def review_config(self, review_config):
        """Sets the review_config of this CreateDigitalAssetRequestBody.

        :param review_config: The review_config of this CreateDigitalAssetRequestBody.
        :type review_config: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        self._review_config = review_config

    @property
    def tags(self):
        """Gets the tags of this CreateDigitalAssetRequestBody.

        标签列表。 > 分身形象系统资产的tag定义如下： > - 行业：NEWS,BUSINESS,E-COMMERCE,MARKETING,KNOWLEDGE,EDUCATION,SPORTS > - 性别：MALE,FEMALE > - 姿势：FULL-BODY,HALF-BODY,STANDING,SITTING,WALKING > - 区域：ASIAN,WESTERN,MIDDLE-EASTERNER,AFRICAN,LATINO

        :return: The tags of this CreateDigitalAssetRequestBody.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateDigitalAssetRequestBody.

        标签列表。 > 分身形象系统资产的tag定义如下： > - 行业：NEWS,BUSINESS,E-COMMERCE,MARKETING,KNOWLEDGE,EDUCATION,SPORTS > - 性别：MALE,FEMALE > - 姿势：FULL-BODY,HALF-BODY,STANDING,SITTING,WALKING > - 区域：ASIAN,WESTERN,MIDDLE-EASTERNER,AFRICAN,LATINO

        :param tags: The tags of this CreateDigitalAssetRequestBody.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def asset_extra_meta(self):
        """Gets the asset_extra_meta of this CreateDigitalAssetRequestBody.

        :return: The asset_extra_meta of this CreateDigitalAssetRequestBody.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.AssetExtraMeta`
        """
        return self._asset_extra_meta

    @asset_extra_meta.setter
    def asset_extra_meta(self, asset_extra_meta):
        """Sets the asset_extra_meta of this CreateDigitalAssetRequestBody.

        :param asset_extra_meta: The asset_extra_meta of this CreateDigitalAssetRequestBody.
        :type asset_extra_meta: :class:`huaweicloudsdkmetastudio.v1.AssetExtraMeta`
        """
        self._asset_extra_meta = asset_extra_meta

    @property
    def system_properties(self):
        """Gets the system_properties of this CreateDigitalAssetRequestBody.

        设置系统属性。

        :return: The system_properties of this CreateDigitalAssetRequestBody.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.SystemProperty`]
        """
        return self._system_properties

    @system_properties.setter
    def system_properties(self, system_properties):
        """Sets the system_properties of this CreateDigitalAssetRequestBody.

        设置系统属性。

        :param system_properties: The system_properties of this CreateDigitalAssetRequestBody.
        :type system_properties: list[:class:`huaweicloudsdkmetastudio.v1.SystemProperty`]
        """
        self._system_properties = system_properties

    @property
    def shared_config(self):
        """Gets the shared_config of this CreateDigitalAssetRequestBody.

        :return: The shared_config of this CreateDigitalAssetRequestBody.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.AssetSharedConfig`
        """
        return self._shared_config

    @shared_config.setter
    def shared_config(self, shared_config):
        """Sets the shared_config of this CreateDigitalAssetRequestBody.

        :param shared_config: The shared_config of this CreateDigitalAssetRequestBody.
        :type shared_config: :class:`huaweicloudsdkmetastudio.v1.AssetSharedConfig`
        """
        self._shared_config = shared_config

    @property
    def is_need_generate_cover(self):
        """Gets the is_need_generate_cover of this CreateDigitalAssetRequestBody.

        是否需要生成封面。

        :return: The is_need_generate_cover of this CreateDigitalAssetRequestBody.
        :rtype: bool
        """
        return self._is_need_generate_cover

    @is_need_generate_cover.setter
    def is_need_generate_cover(self, is_need_generate_cover):
        """Sets the is_need_generate_cover of this CreateDigitalAssetRequestBody.

        是否需要生成封面。

        :param is_need_generate_cover: The is_need_generate_cover of this CreateDigitalAssetRequestBody.
        :type is_need_generate_cover: bool
        """
        self._is_need_generate_cover = is_need_generate_cover

    @property
    def asset_order(self):
        """Gets the asset_order of this CreateDigitalAssetRequestBody.

        展示顺序

        :return: The asset_order of this CreateDigitalAssetRequestBody.
        :rtype: int
        """
        return self._asset_order

    @asset_order.setter
    def asset_order(self, asset_order):
        """Sets the asset_order of this CreateDigitalAssetRequestBody.

        展示顺序

        :param asset_order: The asset_order of this CreateDigitalAssetRequestBody.
        :type asset_order: int
        """
        self._asset_order = asset_order

    @property
    def supported_service(self):
        """Gets the supported_service of this CreateDigitalAssetRequestBody.

        支持的业务类型。： * VIDEO_2D：分身数字人视频制作 * LIVE_2D：分身数字人直播 * CHAT_2D：分身数字人智能交互

        :return: The supported_service of this CreateDigitalAssetRequestBody.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.SupportedServiceEnum`]
        """
        return self._supported_service

    @supported_service.setter
    def supported_service(self, supported_service):
        """Sets the supported_service of this CreateDigitalAssetRequestBody.

        支持的业务类型。： * VIDEO_2D：分身数字人视频制作 * LIVE_2D：分身数字人直播 * CHAT_2D：分身数字人智能交互

        :param supported_service: The supported_service of this CreateDigitalAssetRequestBody.
        :type supported_service: list[:class:`huaweicloudsdkmetastudio.v1.SupportedServiceEnum`]
        """
        self._supported_service = supported_service

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
        if not isinstance(other, CreateDigitalAssetRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
