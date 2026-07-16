# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHpaRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'hpa_rules': 'list[HpaRules]',
        'workspace_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'hpa_rules': 'hpa_rules',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, id=None, hpa_rules=None, workspace_id=None):
        r"""UpdateHpaRequestBody

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 自动扩缩容策略绑定的目标ID **取值范围：** 实例组ID **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type id: str
        :param hpa_rules: **参数解释：** 自动扩缩容规则。 **约束限制：** 不涉及。
        :type hpa_rules: list[:class:`huaweicloudsdkmodelarts.v1.HpaRules`]
        :param workspace_id: **参数解释：** 工作空间ID。 **取值范围：** - 0：默认空间ID - 由数字和小写字母组成的32位字符：其他空间ID，可参考[工作空间创建](CreateWorkspace.xml) **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type workspace_id: str
        """
        
        

        self._id = None
        self._hpa_rules = None
        self._workspace_id = None
        self.discriminator = None

        self.id = id
        if hpa_rules is not None:
            self.hpa_rules = hpa_rules
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def id(self):
        r"""Gets the id of this UpdateHpaRequestBody.

        **参数解释：** 自动扩缩容策略绑定的目标ID **取值范围：** 实例组ID **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The id of this UpdateHpaRequestBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateHpaRequestBody.

        **参数解释：** 自动扩缩容策略绑定的目标ID **取值范围：** 实例组ID **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param id: The id of this UpdateHpaRequestBody.
        :type id: str
        """
        self._id = id

    @property
    def hpa_rules(self):
        r"""Gets the hpa_rules of this UpdateHpaRequestBody.

        **参数解释：** 自动扩缩容规则。 **约束限制：** 不涉及。

        :return: The hpa_rules of this UpdateHpaRequestBody.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.HpaRules`]
        """
        return self._hpa_rules

    @hpa_rules.setter
    def hpa_rules(self, hpa_rules):
        r"""Sets the hpa_rules of this UpdateHpaRequestBody.

        **参数解释：** 自动扩缩容规则。 **约束限制：** 不涉及。

        :param hpa_rules: The hpa_rules of this UpdateHpaRequestBody.
        :type hpa_rules: list[:class:`huaweicloudsdkmodelarts.v1.HpaRules`]
        """
        self._hpa_rules = hpa_rules

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this UpdateHpaRequestBody.

        **参数解释：** 工作空间ID。 **取值范围：** - 0：默认空间ID - 由数字和小写字母组成的32位字符：其他空间ID，可参考[工作空间创建](CreateWorkspace.xml) **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The workspace_id of this UpdateHpaRequestBody.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this UpdateHpaRequestBody.

        **参数解释：** 工作空间ID。 **取值范围：** - 0：默认空间ID - 由数字和小写字母组成的32位字符：其他空间ID，可参考[工作空间创建](CreateWorkspace.xml) **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param workspace_id: The workspace_id of this UpdateHpaRequestBody.
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
        if not isinstance(other, UpdateHpaRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
