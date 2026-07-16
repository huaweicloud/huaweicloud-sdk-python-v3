# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateHpaRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'target_resource_id': 'str',
        'target_resource_type': 'str',
        'hpa_rules': 'list[HpaRules]',
        'workspace_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'target_resource_id': 'target_resource_id',
        'target_resource_type': 'target_resource_type',
        'hpa_rules': 'hpa_rules',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, type=None, target_resource_id=None, target_resource_type=None, hpa_rules=None, workspace_id=None):
        r"""CreateHpaRequestBody

        The model defined in huaweicloud sdk

        :param type: **参数解释：** 自动扩缩容类型。 **取值范围：** - CRON_HPA：定时扩缩容策略 - METRIC_HPA：指标扩缩容策略 **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type type: str
        :param target_resource_id: **参数解释：** 自动扩缩容策略绑定的目标ID **取值范围：** 实例组ID **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type target_resource_id: str
        :param target_resource_type: **参数解释：** 自动扩缩容策略绑定的目标类型。 **取值范围：** - GROUP：实例组 **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type target_resource_type: str
        :param hpa_rules: **参数解释：** 自动扩缩容规则。 **约束限制：** 不涉及。
        :type hpa_rules: list[:class:`huaweicloudsdkmodelarts.v1.HpaRules`]
        :param workspace_id: **参数解释：** 工作空间ID。 **取值范围：** - 0：默认空间ID - 由数字和小写字母组成的32位字符：其他空间ID，可参考[工作空间创建](CreateWorkspace.xml) **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type workspace_id: str
        """
        
        

        self._type = None
        self._target_resource_id = None
        self._target_resource_type = None
        self._hpa_rules = None
        self._workspace_id = None
        self.discriminator = None

        self.type = type
        self.target_resource_id = target_resource_id
        self.target_resource_type = target_resource_type
        self.hpa_rules = hpa_rules
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def type(self):
        r"""Gets the type of this CreateHpaRequestBody.

        **参数解释：** 自动扩缩容类型。 **取值范围：** - CRON_HPA：定时扩缩容策略 - METRIC_HPA：指标扩缩容策略 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The type of this CreateHpaRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateHpaRequestBody.

        **参数解释：** 自动扩缩容类型。 **取值范围：** - CRON_HPA：定时扩缩容策略 - METRIC_HPA：指标扩缩容策略 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param type: The type of this CreateHpaRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def target_resource_id(self):
        r"""Gets the target_resource_id of this CreateHpaRequestBody.

        **参数解释：** 自动扩缩容策略绑定的目标ID **取值范围：** 实例组ID **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The target_resource_id of this CreateHpaRequestBody.
        :rtype: str
        """
        return self._target_resource_id

    @target_resource_id.setter
    def target_resource_id(self, target_resource_id):
        r"""Sets the target_resource_id of this CreateHpaRequestBody.

        **参数解释：** 自动扩缩容策略绑定的目标ID **取值范围：** 实例组ID **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param target_resource_id: The target_resource_id of this CreateHpaRequestBody.
        :type target_resource_id: str
        """
        self._target_resource_id = target_resource_id

    @property
    def target_resource_type(self):
        r"""Gets the target_resource_type of this CreateHpaRequestBody.

        **参数解释：** 自动扩缩容策略绑定的目标类型。 **取值范围：** - GROUP：实例组 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The target_resource_type of this CreateHpaRequestBody.
        :rtype: str
        """
        return self._target_resource_type

    @target_resource_type.setter
    def target_resource_type(self, target_resource_type):
        r"""Sets the target_resource_type of this CreateHpaRequestBody.

        **参数解释：** 自动扩缩容策略绑定的目标类型。 **取值范围：** - GROUP：实例组 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param target_resource_type: The target_resource_type of this CreateHpaRequestBody.
        :type target_resource_type: str
        """
        self._target_resource_type = target_resource_type

    @property
    def hpa_rules(self):
        r"""Gets the hpa_rules of this CreateHpaRequestBody.

        **参数解释：** 自动扩缩容规则。 **约束限制：** 不涉及。

        :return: The hpa_rules of this CreateHpaRequestBody.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.HpaRules`]
        """
        return self._hpa_rules

    @hpa_rules.setter
    def hpa_rules(self, hpa_rules):
        r"""Sets the hpa_rules of this CreateHpaRequestBody.

        **参数解释：** 自动扩缩容规则。 **约束限制：** 不涉及。

        :param hpa_rules: The hpa_rules of this CreateHpaRequestBody.
        :type hpa_rules: list[:class:`huaweicloudsdkmodelarts.v1.HpaRules`]
        """
        self._hpa_rules = hpa_rules

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this CreateHpaRequestBody.

        **参数解释：** 工作空间ID。 **取值范围：** - 0：默认空间ID - 由数字和小写字母组成的32位字符：其他空间ID，可参考[工作空间创建](CreateWorkspace.xml) **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The workspace_id of this CreateHpaRequestBody.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this CreateHpaRequestBody.

        **参数解释：** 工作空间ID。 **取值范围：** - 0：默认空间ID - 由数字和小写字母组成的32位字符：其他空间ID，可参考[工作空间创建](CreateWorkspace.xml) **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param workspace_id: The workspace_id of this CreateHpaRequestBody.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

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
        if not isinstance(other, CreateHpaRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
