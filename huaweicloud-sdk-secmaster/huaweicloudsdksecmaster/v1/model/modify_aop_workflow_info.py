# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyAopWorkflowInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'enabled': 'bool',
        'version_id': 'str',
        'labels': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'enabled': 'enabled',
        'version_id': 'version_id',
        'labels': 'labels'
    }

    def __init__(self, name=None, description=None, enabled=None, version_id=None, labels=None):
        r"""ModifyAopWorkflowInfo

        The model defined in huaweicloud sdk

        :param name: **参数解释**: 流程名称 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及
        :type name: str
        :param description: **参数解释**: 流程的描述 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及
        :type description: str
        :param enabled: **参数解释**: 启用或者禁用流程 **约束限制**: 不涉及         **取值范围**: - true  启用流程 - false 禁用流程  **默认值**:  不涉及
        :type enabled: bool
        :param version_id: **参数解释**: 流程版本ID **约束限制**: 当前流程下已经激活的流程版本ID，当启用流程时为必填参数
        :type version_id: str
        :param labels: **参数解释**: 流程实体类型 - IP IP - ACCOUNT 账号 - DOMAIN 域名  **约束限制**: 不涉及         **取值范围**: - IP - ACCOUNT - DOMAIN  **默认值**:  不涉及
        :type labels: str
        """
        
        

        self._name = None
        self._description = None
        self._enabled = None
        self._version_id = None
        self._labels = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if enabled is not None:
            self.enabled = enabled
        if version_id is not None:
            self.version_id = version_id
        if labels is not None:
            self.labels = labels

    @property
    def name(self):
        r"""Gets the name of this ModifyAopWorkflowInfo.

        **参数解释**: 流程名称 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The name of this ModifyAopWorkflowInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ModifyAopWorkflowInfo.

        **参数解释**: 流程名称 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :param name: The name of this ModifyAopWorkflowInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ModifyAopWorkflowInfo.

        **参数解释**: 流程的描述 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The description of this ModifyAopWorkflowInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ModifyAopWorkflowInfo.

        **参数解释**: 流程的描述 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :param description: The description of this ModifyAopWorkflowInfo.
        :type description: str
        """
        self._description = description

    @property
    def enabled(self):
        r"""Gets the enabled of this ModifyAopWorkflowInfo.

        **参数解释**: 启用或者禁用流程 **约束限制**: 不涉及         **取值范围**: - true  启用流程 - false 禁用流程  **默认值**:  不涉及

        :return: The enabled of this ModifyAopWorkflowInfo.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ModifyAopWorkflowInfo.

        **参数解释**: 启用或者禁用流程 **约束限制**: 不涉及         **取值范围**: - true  启用流程 - false 禁用流程  **默认值**:  不涉及

        :param enabled: The enabled of this ModifyAopWorkflowInfo.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def version_id(self):
        r"""Gets the version_id of this ModifyAopWorkflowInfo.

        **参数解释**: 流程版本ID **约束限制**: 当前流程下已经激活的流程版本ID，当启用流程时为必填参数

        :return: The version_id of this ModifyAopWorkflowInfo.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this ModifyAopWorkflowInfo.

        **参数解释**: 流程版本ID **约束限制**: 当前流程下已经激活的流程版本ID，当启用流程时为必填参数

        :param version_id: The version_id of this ModifyAopWorkflowInfo.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def labels(self):
        r"""Gets the labels of this ModifyAopWorkflowInfo.

        **参数解释**: 流程实体类型 - IP IP - ACCOUNT 账号 - DOMAIN 域名  **约束限制**: 不涉及         **取值范围**: - IP - ACCOUNT - DOMAIN  **默认值**:  不涉及

        :return: The labels of this ModifyAopWorkflowInfo.
        :rtype: str
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ModifyAopWorkflowInfo.

        **参数解释**: 流程实体类型 - IP IP - ACCOUNT 账号 - DOMAIN 域名  **约束限制**: 不涉及         **取值范围**: - IP - ACCOUNT - DOMAIN  **默认值**:  不涉及

        :param labels: The labels of this ModifyAopWorkflowInfo.
        :type labels: str
        """
        self._labels = labels

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
        if not isinstance(other, ModifyAopWorkflowInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
