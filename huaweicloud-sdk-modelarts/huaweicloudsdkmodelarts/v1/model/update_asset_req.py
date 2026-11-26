# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAssetReq:

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
        'asset_desc': 'str',
        'asset_group_desc': 'str',
        'asset_series': 'str',
        'asset_capabilities': 'list[str]',
        'status': 'str',
        'enabled': 'bool',
        'is_deleted': 'bool',
        'tags': 'dict(str, list[str])',
        'properties': 'Properties'
    }

    attribute_map = {
        'asset_name': 'asset_name',
        'asset_desc': 'asset_desc',
        'asset_group_desc': 'asset_group_desc',
        'asset_series': 'asset_series',
        'asset_capabilities': 'asset_capabilities',
        'status': 'status',
        'enabled': 'enabled',
        'is_deleted': 'is_deleted',
        'tags': 'tags',
        'properties': 'properties'
    }

    def __init__(self, asset_name=None, asset_desc=None, asset_group_desc=None, asset_series=None, asset_capabilities=None, status=None, enabled=None, is_deleted=None, tags=None, properties=None):
        r"""UpdateAssetReq

        The model defined in huaweicloud sdk

        :param asset_name: **参数解释**：资产名称。 **约束限制**：1-128位字符，只包含中文、字母、数字、中划线、下划线。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type asset_name: str
        :param asset_desc: **参数解释**：资产描述。 **约束限制**：0-512位字符，不能包含英文尖括号（即 &lt; 或 &gt;）。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type asset_desc: str
        :param asset_group_desc: **参数解释**：资产组描述。 **约束限制**：0-512位字符，不能包含英文尖括号（即 &lt; 或 &gt;）。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type asset_group_desc: str
        :param asset_series: **参数解释**：资产品牌，例如DeepSeek,Qwen,Wan,GPT,Llama,GLM,ERNIE,Mistral,Kimi,Other。 **约束限制**：1-40位字符，仅支持英文字母、数字、下划线和中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type asset_series: str
        :param asset_capabilities: **参数解释**：资产能力，为自由文本字符串列表(非严格枚举)。推荐使用以下约定值：例如TextGeneration,ImageUnderstanding,ImageGeneration,VideoGeneration,AgenticRL,Other。 **约束限制**：每个元素1-40位字符，仅支持英文字母、数字、下划线和中划线；最多10个元素。
        :type asset_capabilities: list[str]
        :param status: **参数解释**：数据集资产的上下线状态。 **约束限制**：不涉及。 **取值范围**：枚举值： - online：上线 - offline：下线 - waiting: 等待中 **默认取值**：不涉及。
        :type status: str
        :param enabled: **参数解释**：资产是否可用。 **约束限制**：不涉及。 **取值范围**： - true：可用 - false：不可用 **默认取值**：不涉及。
        :type enabled: bool
        :param is_deleted: **参数解释**：数据集资产是否被软删除。 **约束限制**：不涉及。 **取值范围**： - true：已删除 - false：未删除 **默认取值**：不涉及。
        :type is_deleted: bool
        :param tags: **参数解释**：资产tag。 **约束限制**：不涉及。
        :type tags: dict(str, list[str])
        :param properties: 
        :type properties: :class:`huaweicloudsdkmodelarts.v1.Properties`
        """
        
        

        self._asset_name = None
        self._asset_desc = None
        self._asset_group_desc = None
        self._asset_series = None
        self._asset_capabilities = None
        self._status = None
        self._enabled = None
        self._is_deleted = None
        self._tags = None
        self._properties = None
        self.discriminator = None

        if asset_name is not None:
            self.asset_name = asset_name
        if asset_desc is not None:
            self.asset_desc = asset_desc
        if asset_group_desc is not None:
            self.asset_group_desc = asset_group_desc
        if asset_series is not None:
            self.asset_series = asset_series
        if asset_capabilities is not None:
            self.asset_capabilities = asset_capabilities
        if status is not None:
            self.status = status
        if enabled is not None:
            self.enabled = enabled
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if tags is not None:
            self.tags = tags
        if properties is not None:
            self.properties = properties

    @property
    def asset_name(self):
        r"""Gets the asset_name of this UpdateAssetReq.

        **参数解释**：资产名称。 **约束限制**：1-128位字符，只包含中文、字母、数字、中划线、下划线。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The asset_name of this UpdateAssetReq.
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        r"""Sets the asset_name of this UpdateAssetReq.

        **参数解释**：资产名称。 **约束限制**：1-128位字符，只包含中文、字母、数字、中划线、下划线。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param asset_name: The asset_name of this UpdateAssetReq.
        :type asset_name: str
        """
        self._asset_name = asset_name

    @property
    def asset_desc(self):
        r"""Gets the asset_desc of this UpdateAssetReq.

        **参数解释**：资产描述。 **约束限制**：0-512位字符，不能包含英文尖括号（即 < 或 >）。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The asset_desc of this UpdateAssetReq.
        :rtype: str
        """
        return self._asset_desc

    @asset_desc.setter
    def asset_desc(self, asset_desc):
        r"""Sets the asset_desc of this UpdateAssetReq.

        **参数解释**：资产描述。 **约束限制**：0-512位字符，不能包含英文尖括号（即 < 或 >）。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param asset_desc: The asset_desc of this UpdateAssetReq.
        :type asset_desc: str
        """
        self._asset_desc = asset_desc

    @property
    def asset_group_desc(self):
        r"""Gets the asset_group_desc of this UpdateAssetReq.

        **参数解释**：资产组描述。 **约束限制**：0-512位字符，不能包含英文尖括号（即 < 或 >）。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The asset_group_desc of this UpdateAssetReq.
        :rtype: str
        """
        return self._asset_group_desc

    @asset_group_desc.setter
    def asset_group_desc(self, asset_group_desc):
        r"""Sets the asset_group_desc of this UpdateAssetReq.

        **参数解释**：资产组描述。 **约束限制**：0-512位字符，不能包含英文尖括号（即 < 或 >）。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param asset_group_desc: The asset_group_desc of this UpdateAssetReq.
        :type asset_group_desc: str
        """
        self._asset_group_desc = asset_group_desc

    @property
    def asset_series(self):
        r"""Gets the asset_series of this UpdateAssetReq.

        **参数解释**：资产品牌，例如DeepSeek,Qwen,Wan,GPT,Llama,GLM,ERNIE,Mistral,Kimi,Other。 **约束限制**：1-40位字符，仅支持英文字母、数字、下划线和中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The asset_series of this UpdateAssetReq.
        :rtype: str
        """
        return self._asset_series

    @asset_series.setter
    def asset_series(self, asset_series):
        r"""Sets the asset_series of this UpdateAssetReq.

        **参数解释**：资产品牌，例如DeepSeek,Qwen,Wan,GPT,Llama,GLM,ERNIE,Mistral,Kimi,Other。 **约束限制**：1-40位字符，仅支持英文字母、数字、下划线和中划线。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param asset_series: The asset_series of this UpdateAssetReq.
        :type asset_series: str
        """
        self._asset_series = asset_series

    @property
    def asset_capabilities(self):
        r"""Gets the asset_capabilities of this UpdateAssetReq.

        **参数解释**：资产能力，为自由文本字符串列表(非严格枚举)。推荐使用以下约定值：例如TextGeneration,ImageUnderstanding,ImageGeneration,VideoGeneration,AgenticRL,Other。 **约束限制**：每个元素1-40位字符，仅支持英文字母、数字、下划线和中划线；最多10个元素。

        :return: The asset_capabilities of this UpdateAssetReq.
        :rtype: list[str]
        """
        return self._asset_capabilities

    @asset_capabilities.setter
    def asset_capabilities(self, asset_capabilities):
        r"""Sets the asset_capabilities of this UpdateAssetReq.

        **参数解释**：资产能力，为自由文本字符串列表(非严格枚举)。推荐使用以下约定值：例如TextGeneration,ImageUnderstanding,ImageGeneration,VideoGeneration,AgenticRL,Other。 **约束限制**：每个元素1-40位字符，仅支持英文字母、数字、下划线和中划线；最多10个元素。

        :param asset_capabilities: The asset_capabilities of this UpdateAssetReq.
        :type asset_capabilities: list[str]
        """
        self._asset_capabilities = asset_capabilities

    @property
    def status(self):
        r"""Gets the status of this UpdateAssetReq.

        **参数解释**：数据集资产的上下线状态。 **约束限制**：不涉及。 **取值范围**：枚举值： - online：上线 - offline：下线 - waiting: 等待中 **默认取值**：不涉及。

        :return: The status of this UpdateAssetReq.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateAssetReq.

        **参数解释**：数据集资产的上下线状态。 **约束限制**：不涉及。 **取值范围**：枚举值： - online：上线 - offline：下线 - waiting: 等待中 **默认取值**：不涉及。

        :param status: The status of this UpdateAssetReq.
        :type status: str
        """
        self._status = status

    @property
    def enabled(self):
        r"""Gets the enabled of this UpdateAssetReq.

        **参数解释**：资产是否可用。 **约束限制**：不涉及。 **取值范围**： - true：可用 - false：不可用 **默认取值**：不涉及。

        :return: The enabled of this UpdateAssetReq.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this UpdateAssetReq.

        **参数解释**：资产是否可用。 **约束限制**：不涉及。 **取值范围**： - true：可用 - false：不可用 **默认取值**：不涉及。

        :param enabled: The enabled of this UpdateAssetReq.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def is_deleted(self):
        r"""Gets the is_deleted of this UpdateAssetReq.

        **参数解释**：数据集资产是否被软删除。 **约束限制**：不涉及。 **取值范围**： - true：已删除 - false：未删除 **默认取值**：不涉及。

        :return: The is_deleted of this UpdateAssetReq.
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        r"""Sets the is_deleted of this UpdateAssetReq.

        **参数解释**：数据集资产是否被软删除。 **约束限制**：不涉及。 **取值范围**： - true：已删除 - false：未删除 **默认取值**：不涉及。

        :param is_deleted: The is_deleted of this UpdateAssetReq.
        :type is_deleted: bool
        """
        self._is_deleted = is_deleted

    @property
    def tags(self):
        r"""Gets the tags of this UpdateAssetReq.

        **参数解释**：资产tag。 **约束限制**：不涉及。

        :return: The tags of this UpdateAssetReq.
        :rtype: dict(str, list[str])
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this UpdateAssetReq.

        **参数解释**：资产tag。 **约束限制**：不涉及。

        :param tags: The tags of this UpdateAssetReq.
        :type tags: dict(str, list[str])
        """
        self._tags = tags

    @property
    def properties(self):
        r"""Gets the properties of this UpdateAssetReq.

        :return: The properties of this UpdateAssetReq.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Properties`
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this UpdateAssetReq.

        :param properties: The properties of this UpdateAssetReq.
        :type properties: :class:`huaweicloudsdkmodelarts.v1.Properties`
        """
        self._properties = properties

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateAssetReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
