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
        'review_config': 'ReviewConfig',
        'tags': 'list[str]',
        'asset_extra_meta': 'AssetExtraMeta',
        'system_properties': 'list[SystemProperty]',
        'shared_config': 'AssetSharedConfig',
        'asset_order': 'int',
        'supported_service': 'list[SupportedServiceEnum]',
        'auto_operation_config': 'list[AutoOperationConfig]'
    }

    attribute_map = {
        'asset_name': 'asset_name',
        'asset_description': 'asset_description',
        'asset_type': 'asset_type',
        'asset_state': 'asset_state',
        'review_config': 'review_config',
        'tags': 'tags',
        'asset_extra_meta': 'asset_extra_meta',
        'system_properties': 'system_properties',
        'shared_config': 'shared_config',
        'asset_order': 'asset_order',
        'supported_service': 'supported_service',
        'auto_operation_config': 'auto_operation_config'
    }

    def __init__(self, asset_name=None, asset_description=None, asset_type=None, asset_state=None, review_config=None, tags=None, asset_extra_meta=None, system_properties=None, shared_config=None, asset_order=None, supported_service=None, auto_operation_config=None):
        r"""UpdateDigitalAssetRequestBody

        The model defined in huaweicloud sdk

        :param asset_name: **参数解释**： 资产名称。 **约束限制**： 不涉及。 **取值范围**： 只能使用中英文字符，字符长度0-256位。 **默认取值**： 不涉及。
        :type asset_name: str
        :param asset_description: **参数解释**： 资产描述。 **约束限制**： 不涉及。 **取值范围**： 只能使用中英文字符，字符长度0-4096位。 **默认取值**： 不涉及。
        :type asset_description: str
        :param asset_type: **参数解释**： 资产类型。 **约束限制**： VOICE_MODEL，HUMAN_MODEL_2D 普通用户均无法上传。 **取值范围**： 公共资产类型： * VOICE_MODEL：音色模型 * VIDEO：视频文件 * IMAGE：图片文件 * PPT：幻灯片文件 * MUSIC: 音乐 * AUDIO: 音频 * COMMON_FILE：通用文件  分身数字人资产： * HUMAN_MODEL_2D: 分身数字人模型 * BUSINESS_CARD_TEMPLET: 数字人名片模板  **默认取值**： 不涉及。
        :type asset_type: str
        :param asset_state: **参数解释**： 资产状态。 **约束限制**： 租户仅能激活或取消激活资产，其他状态由系统自动更新。 **取值范围**： * UNACTIVED：取消激活。未激活的资产不可用于其他业务 * ACTIVED：激活。激活后的资产可用于其他业务 * WAITING_DELETE：资产将被下线(激活状态资产可用、管理员可用)  **默认取值**： 不涉及。
        :type asset_state: str
        :param review_config: 
        :type review_config: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        :param tags: **参数解释**： 标签列表。 &gt; 分身形象系统资产的tag定义如下： &gt; - 行业：NEWS,BUSINESS,E-COMMERCE,MARKETING,KNOWLEDGE,EDUCATION,SPORTS &gt; - 性别：MALE,FEMALE &gt; - 姿势：FULL-BODY,HALF-BODY,STANDING,SITTING,WALKING &gt; - 区域：ASIAN,WESTERN,MIDDLE-EASTERNER,AFRICAN,LATINO  **约束限制**： 不涉及 **取值范围**： 标签个数最大为50个。 标签内容为中英文，字符长度0-128位。 **默认取值**： 不涉及
        :type tags: list[str]
        :param asset_extra_meta: 
        :type asset_extra_meta: :class:`huaweicloudsdkmetastudio.v1.AssetExtraMeta`
        :param system_properties: 设置系统属性。
        :type system_properties: list[:class:`huaweicloudsdkmetastudio.v1.SystemProperty`]
        :param shared_config: 
        :type shared_config: :class:`huaweicloudsdkmetastudio.v1.AssetSharedConfig`
        :param asset_order: **参数解释**： 用于console控制台展示顺序。 如果取值相同，则默认最新的排在前面。 **约束限制**： 不涉及 **默认取值**： 不涉及
        :type asset_order: int
        :param supported_service: 支持的业务类型。： * VIDEO_2D：分身数字人视频制作 * LIVE_2D：分身数字人直播 * CHAT_2D：分身数字人智能交互
        :type supported_service: list[:class:`huaweicloudsdkmetastudio.v1.SupportedServiceEnum`]
        :param auto_operation_config: 资产自动处理任务。
        :type auto_operation_config: list[:class:`huaweicloudsdkmetastudio.v1.AutoOperationConfig`]
        """
        
        

        self._asset_name = None
        self._asset_description = None
        self._asset_type = None
        self._asset_state = None
        self._review_config = None
        self._tags = None
        self._asset_extra_meta = None
        self._system_properties = None
        self._shared_config = None
        self._asset_order = None
        self._supported_service = None
        self._auto_operation_config = None
        self.discriminator = None

        if asset_name is not None:
            self.asset_name = asset_name
        if asset_description is not None:
            self.asset_description = asset_description
        if asset_type is not None:
            self.asset_type = asset_type
        if asset_state is not None:
            self.asset_state = asset_state
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
        if asset_order is not None:
            self.asset_order = asset_order
        if supported_service is not None:
            self.supported_service = supported_service
        if auto_operation_config is not None:
            self.auto_operation_config = auto_operation_config

    @property
    def asset_name(self):
        r"""Gets the asset_name of this UpdateDigitalAssetRequestBody.

        **参数解释**： 资产名称。 **约束限制**： 不涉及。 **取值范围**： 只能使用中英文字符，字符长度0-256位。 **默认取值**： 不涉及。

        :return: The asset_name of this UpdateDigitalAssetRequestBody.
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        r"""Sets the asset_name of this UpdateDigitalAssetRequestBody.

        **参数解释**： 资产名称。 **约束限制**： 不涉及。 **取值范围**： 只能使用中英文字符，字符长度0-256位。 **默认取值**： 不涉及。

        :param asset_name: The asset_name of this UpdateDigitalAssetRequestBody.
        :type asset_name: str
        """
        self._asset_name = asset_name

    @property
    def asset_description(self):
        r"""Gets the asset_description of this UpdateDigitalAssetRequestBody.

        **参数解释**： 资产描述。 **约束限制**： 不涉及。 **取值范围**： 只能使用中英文字符，字符长度0-4096位。 **默认取值**： 不涉及。

        :return: The asset_description of this UpdateDigitalAssetRequestBody.
        :rtype: str
        """
        return self._asset_description

    @asset_description.setter
    def asset_description(self, asset_description):
        r"""Sets the asset_description of this UpdateDigitalAssetRequestBody.

        **参数解释**： 资产描述。 **约束限制**： 不涉及。 **取值范围**： 只能使用中英文字符，字符长度0-4096位。 **默认取值**： 不涉及。

        :param asset_description: The asset_description of this UpdateDigitalAssetRequestBody.
        :type asset_description: str
        """
        self._asset_description = asset_description

    @property
    def asset_type(self):
        r"""Gets the asset_type of this UpdateDigitalAssetRequestBody.

        **参数解释**： 资产类型。 **约束限制**： VOICE_MODEL，HUMAN_MODEL_2D 普通用户均无法上传。 **取值范围**： 公共资产类型： * VOICE_MODEL：音色模型 * VIDEO：视频文件 * IMAGE：图片文件 * PPT：幻灯片文件 * MUSIC: 音乐 * AUDIO: 音频 * COMMON_FILE：通用文件  分身数字人资产： * HUMAN_MODEL_2D: 分身数字人模型 * BUSINESS_CARD_TEMPLET: 数字人名片模板  **默认取值**： 不涉及。

        :return: The asset_type of this UpdateDigitalAssetRequestBody.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        r"""Sets the asset_type of this UpdateDigitalAssetRequestBody.

        **参数解释**： 资产类型。 **约束限制**： VOICE_MODEL，HUMAN_MODEL_2D 普通用户均无法上传。 **取值范围**： 公共资产类型： * VOICE_MODEL：音色模型 * VIDEO：视频文件 * IMAGE：图片文件 * PPT：幻灯片文件 * MUSIC: 音乐 * AUDIO: 音频 * COMMON_FILE：通用文件  分身数字人资产： * HUMAN_MODEL_2D: 分身数字人模型 * BUSINESS_CARD_TEMPLET: 数字人名片模板  **默认取值**： 不涉及。

        :param asset_type: The asset_type of this UpdateDigitalAssetRequestBody.
        :type asset_type: str
        """
        self._asset_type = asset_type

    @property
    def asset_state(self):
        r"""Gets the asset_state of this UpdateDigitalAssetRequestBody.

        **参数解释**： 资产状态。 **约束限制**： 租户仅能激活或取消激活资产，其他状态由系统自动更新。 **取值范围**： * UNACTIVED：取消激活。未激活的资产不可用于其他业务 * ACTIVED：激活。激活后的资产可用于其他业务 * WAITING_DELETE：资产将被下线(激活状态资产可用、管理员可用)  **默认取值**： 不涉及。

        :return: The asset_state of this UpdateDigitalAssetRequestBody.
        :rtype: str
        """
        return self._asset_state

    @asset_state.setter
    def asset_state(self, asset_state):
        r"""Sets the asset_state of this UpdateDigitalAssetRequestBody.

        **参数解释**： 资产状态。 **约束限制**： 租户仅能激活或取消激活资产，其他状态由系统自动更新。 **取值范围**： * UNACTIVED：取消激活。未激活的资产不可用于其他业务 * ACTIVED：激活。激活后的资产可用于其他业务 * WAITING_DELETE：资产将被下线(激活状态资产可用、管理员可用)  **默认取值**： 不涉及。

        :param asset_state: The asset_state of this UpdateDigitalAssetRequestBody.
        :type asset_state: str
        """
        self._asset_state = asset_state

    @property
    def review_config(self):
        r"""Gets the review_config of this UpdateDigitalAssetRequestBody.

        :return: The review_config of this UpdateDigitalAssetRequestBody.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        return self._review_config

    @review_config.setter
    def review_config(self, review_config):
        r"""Sets the review_config of this UpdateDigitalAssetRequestBody.

        :param review_config: The review_config of this UpdateDigitalAssetRequestBody.
        :type review_config: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        self._review_config = review_config

    @property
    def tags(self):
        r"""Gets the tags of this UpdateDigitalAssetRequestBody.

        **参数解释**： 标签列表。 > 分身形象系统资产的tag定义如下： > - 行业：NEWS,BUSINESS,E-COMMERCE,MARKETING,KNOWLEDGE,EDUCATION,SPORTS > - 性别：MALE,FEMALE > - 姿势：FULL-BODY,HALF-BODY,STANDING,SITTING,WALKING > - 区域：ASIAN,WESTERN,MIDDLE-EASTERNER,AFRICAN,LATINO  **约束限制**： 不涉及 **取值范围**： 标签个数最大为50个。 标签内容为中英文，字符长度0-128位。 **默认取值**： 不涉及

        :return: The tags of this UpdateDigitalAssetRequestBody.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this UpdateDigitalAssetRequestBody.

        **参数解释**： 标签列表。 > 分身形象系统资产的tag定义如下： > - 行业：NEWS,BUSINESS,E-COMMERCE,MARKETING,KNOWLEDGE,EDUCATION,SPORTS > - 性别：MALE,FEMALE > - 姿势：FULL-BODY,HALF-BODY,STANDING,SITTING,WALKING > - 区域：ASIAN,WESTERN,MIDDLE-EASTERNER,AFRICAN,LATINO  **约束限制**： 不涉及 **取值范围**： 标签个数最大为50个。 标签内容为中英文，字符长度0-128位。 **默认取值**： 不涉及

        :param tags: The tags of this UpdateDigitalAssetRequestBody.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def asset_extra_meta(self):
        r"""Gets the asset_extra_meta of this UpdateDigitalAssetRequestBody.

        :return: The asset_extra_meta of this UpdateDigitalAssetRequestBody.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.AssetExtraMeta`
        """
        return self._asset_extra_meta

    @asset_extra_meta.setter
    def asset_extra_meta(self, asset_extra_meta):
        r"""Sets the asset_extra_meta of this UpdateDigitalAssetRequestBody.

        :param asset_extra_meta: The asset_extra_meta of this UpdateDigitalAssetRequestBody.
        :type asset_extra_meta: :class:`huaweicloudsdkmetastudio.v1.AssetExtraMeta`
        """
        self._asset_extra_meta = asset_extra_meta

    @property
    def system_properties(self):
        r"""Gets the system_properties of this UpdateDigitalAssetRequestBody.

        设置系统属性。

        :return: The system_properties of this UpdateDigitalAssetRequestBody.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.SystemProperty`]
        """
        return self._system_properties

    @system_properties.setter
    def system_properties(self, system_properties):
        r"""Sets the system_properties of this UpdateDigitalAssetRequestBody.

        设置系统属性。

        :param system_properties: The system_properties of this UpdateDigitalAssetRequestBody.
        :type system_properties: list[:class:`huaweicloudsdkmetastudio.v1.SystemProperty`]
        """
        self._system_properties = system_properties

    @property
    def shared_config(self):
        r"""Gets the shared_config of this UpdateDigitalAssetRequestBody.

        :return: The shared_config of this UpdateDigitalAssetRequestBody.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.AssetSharedConfig`
        """
        return self._shared_config

    @shared_config.setter
    def shared_config(self, shared_config):
        r"""Sets the shared_config of this UpdateDigitalAssetRequestBody.

        :param shared_config: The shared_config of this UpdateDigitalAssetRequestBody.
        :type shared_config: :class:`huaweicloudsdkmetastudio.v1.AssetSharedConfig`
        """
        self._shared_config = shared_config

    @property
    def asset_order(self):
        r"""Gets the asset_order of this UpdateDigitalAssetRequestBody.

        **参数解释**： 用于console控制台展示顺序。 如果取值相同，则默认最新的排在前面。 **约束限制**： 不涉及 **默认取值**： 不涉及

        :return: The asset_order of this UpdateDigitalAssetRequestBody.
        :rtype: int
        """
        return self._asset_order

    @asset_order.setter
    def asset_order(self, asset_order):
        r"""Sets the asset_order of this UpdateDigitalAssetRequestBody.

        **参数解释**： 用于console控制台展示顺序。 如果取值相同，则默认最新的排在前面。 **约束限制**： 不涉及 **默认取值**： 不涉及

        :param asset_order: The asset_order of this UpdateDigitalAssetRequestBody.
        :type asset_order: int
        """
        self._asset_order = asset_order

    @property
    def supported_service(self):
        r"""Gets the supported_service of this UpdateDigitalAssetRequestBody.

        支持的业务类型。： * VIDEO_2D：分身数字人视频制作 * LIVE_2D：分身数字人直播 * CHAT_2D：分身数字人智能交互

        :return: The supported_service of this UpdateDigitalAssetRequestBody.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.SupportedServiceEnum`]
        """
        return self._supported_service

    @supported_service.setter
    def supported_service(self, supported_service):
        r"""Sets the supported_service of this UpdateDigitalAssetRequestBody.

        支持的业务类型。： * VIDEO_2D：分身数字人视频制作 * LIVE_2D：分身数字人直播 * CHAT_2D：分身数字人智能交互

        :param supported_service: The supported_service of this UpdateDigitalAssetRequestBody.
        :type supported_service: list[:class:`huaweicloudsdkmetastudio.v1.SupportedServiceEnum`]
        """
        self._supported_service = supported_service

    @property
    def auto_operation_config(self):
        r"""Gets the auto_operation_config of this UpdateDigitalAssetRequestBody.

        资产自动处理任务。

        :return: The auto_operation_config of this UpdateDigitalAssetRequestBody.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.AutoOperationConfig`]
        """
        return self._auto_operation_config

    @auto_operation_config.setter
    def auto_operation_config(self, auto_operation_config):
        r"""Sets the auto_operation_config of this UpdateDigitalAssetRequestBody.

        资产自动处理任务。

        :param auto_operation_config: The auto_operation_config of this UpdateDigitalAssetRequestBody.
        :type auto_operation_config: list[:class:`huaweicloudsdkmetastudio.v1.AutoOperationConfig`]
        """
        self._auto_operation_config = auto_operation_config

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
