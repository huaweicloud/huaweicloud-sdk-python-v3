# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlowsInfoVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'name': 'str',
        'description': 'str',
        'extra_config': 'list[dict(str, object)]',
        'from_code': 'str',
        'to_code': 'str',
        'before_rule_configs': 'list[WorkItemFlowRuleConfigVO]',
        'before_rule_validator': 'list[str]',
        'after_rule_configs': 'list[WorkItemFlowRuleConfigVO]'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name',
        'description': 'description',
        'extra_config': 'extra_config',
        'from_code': 'from_code',
        'to_code': 'to_code',
        'before_rule_configs': 'before_rule_configs',
        'before_rule_validator': 'before_rule_validator',
        'after_rule_configs': 'after_rule_configs'
    }

    def __init__(self, code=None, name=None, description=None, extra_config=None, from_code=None, to_code=None, before_rule_configs=None, before_rule_validator=None, after_rule_configs=None):
        r"""FlowsInfoVO

        The model defined in huaweicloud sdk

        :param code: **参数解释**： 流转线code。 **取值范围**： 不涉及。
        :type code: str
        :param name: **参数解释**： 流转线名称。 **取值范围**： 不涉及。
        :type name: str
        :param description: **参数解释**： 流转线描述信息。 **取值范围**： 不涉及。
        :type description: str
        :param extra_config: **参数解释**： 流转线扩展配置。 **取值范围**： 不涉及。
        :type extra_config: list[dict(str, object)]
        :param from_code: **参数解释**： 当前工作流节点code。 **取值范围**： 不涉及。
        :type from_code: str
        :param to_code: **参数解释**： 目标工作流节点code。 **取值范围**： 不涉及。
        :type to_code: str
        :param before_rule_configs: **参数解释**： 流转前规则配置。 **取值范围**： 不涉及。
        :type before_rule_configs: list[:class:`huaweicloudsdkprojectman.v4.WorkItemFlowRuleConfigVO`]
        :param before_rule_validator: **参数解释**： 流转前校验规则。 **取值范围**： 不涉及。
        :type before_rule_validator: list[str]
        :param after_rule_configs: **参数解释**： 流转后规则配置。 **取值范围**： 不涉及。
        :type after_rule_configs: list[:class:`huaweicloudsdkprojectman.v4.WorkItemFlowRuleConfigVO`]
        """
        
        

        self._code = None
        self._name = None
        self._description = None
        self._extra_config = None
        self._from_code = None
        self._to_code = None
        self._before_rule_configs = None
        self._before_rule_validator = None
        self._after_rule_configs = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if extra_config is not None:
            self.extra_config = extra_config
        if from_code is not None:
            self.from_code = from_code
        if to_code is not None:
            self.to_code = to_code
        if before_rule_configs is not None:
            self.before_rule_configs = before_rule_configs
        if before_rule_validator is not None:
            self.before_rule_validator = before_rule_validator
        if after_rule_configs is not None:
            self.after_rule_configs = after_rule_configs

    @property
    def code(self):
        r"""Gets the code of this FlowsInfoVO.

        **参数解释**： 流转线code。 **取值范围**： 不涉及。

        :return: The code of this FlowsInfoVO.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this FlowsInfoVO.

        **参数解释**： 流转线code。 **取值范围**： 不涉及。

        :param code: The code of this FlowsInfoVO.
        :type code: str
        """
        self._code = code

    @property
    def name(self):
        r"""Gets the name of this FlowsInfoVO.

        **参数解释**： 流转线名称。 **取值范围**： 不涉及。

        :return: The name of this FlowsInfoVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this FlowsInfoVO.

        **参数解释**： 流转线名称。 **取值范围**： 不涉及。

        :param name: The name of this FlowsInfoVO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this FlowsInfoVO.

        **参数解释**： 流转线描述信息。 **取值范围**： 不涉及。

        :return: The description of this FlowsInfoVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this FlowsInfoVO.

        **参数解释**： 流转线描述信息。 **取值范围**： 不涉及。

        :param description: The description of this FlowsInfoVO.
        :type description: str
        """
        self._description = description

    @property
    def extra_config(self):
        r"""Gets the extra_config of this FlowsInfoVO.

        **参数解释**： 流转线扩展配置。 **取值范围**： 不涉及。

        :return: The extra_config of this FlowsInfoVO.
        :rtype: list[dict(str, object)]
        """
        return self._extra_config

    @extra_config.setter
    def extra_config(self, extra_config):
        r"""Sets the extra_config of this FlowsInfoVO.

        **参数解释**： 流转线扩展配置。 **取值范围**： 不涉及。

        :param extra_config: The extra_config of this FlowsInfoVO.
        :type extra_config: list[dict(str, object)]
        """
        self._extra_config = extra_config

    @property
    def from_code(self):
        r"""Gets the from_code of this FlowsInfoVO.

        **参数解释**： 当前工作流节点code。 **取值范围**： 不涉及。

        :return: The from_code of this FlowsInfoVO.
        :rtype: str
        """
        return self._from_code

    @from_code.setter
    def from_code(self, from_code):
        r"""Sets the from_code of this FlowsInfoVO.

        **参数解释**： 当前工作流节点code。 **取值范围**： 不涉及。

        :param from_code: The from_code of this FlowsInfoVO.
        :type from_code: str
        """
        self._from_code = from_code

    @property
    def to_code(self):
        r"""Gets the to_code of this FlowsInfoVO.

        **参数解释**： 目标工作流节点code。 **取值范围**： 不涉及。

        :return: The to_code of this FlowsInfoVO.
        :rtype: str
        """
        return self._to_code

    @to_code.setter
    def to_code(self, to_code):
        r"""Sets the to_code of this FlowsInfoVO.

        **参数解释**： 目标工作流节点code。 **取值范围**： 不涉及。

        :param to_code: The to_code of this FlowsInfoVO.
        :type to_code: str
        """
        self._to_code = to_code

    @property
    def before_rule_configs(self):
        r"""Gets the before_rule_configs of this FlowsInfoVO.

        **参数解释**： 流转前规则配置。 **取值范围**： 不涉及。

        :return: The before_rule_configs of this FlowsInfoVO.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.WorkItemFlowRuleConfigVO`]
        """
        return self._before_rule_configs

    @before_rule_configs.setter
    def before_rule_configs(self, before_rule_configs):
        r"""Sets the before_rule_configs of this FlowsInfoVO.

        **参数解释**： 流转前规则配置。 **取值范围**： 不涉及。

        :param before_rule_configs: The before_rule_configs of this FlowsInfoVO.
        :type before_rule_configs: list[:class:`huaweicloudsdkprojectman.v4.WorkItemFlowRuleConfigVO`]
        """
        self._before_rule_configs = before_rule_configs

    @property
    def before_rule_validator(self):
        r"""Gets the before_rule_validator of this FlowsInfoVO.

        **参数解释**： 流转前校验规则。 **取值范围**： 不涉及。

        :return: The before_rule_validator of this FlowsInfoVO.
        :rtype: list[str]
        """
        return self._before_rule_validator

    @before_rule_validator.setter
    def before_rule_validator(self, before_rule_validator):
        r"""Sets the before_rule_validator of this FlowsInfoVO.

        **参数解释**： 流转前校验规则。 **取值范围**： 不涉及。

        :param before_rule_validator: The before_rule_validator of this FlowsInfoVO.
        :type before_rule_validator: list[str]
        """
        self._before_rule_validator = before_rule_validator

    @property
    def after_rule_configs(self):
        r"""Gets the after_rule_configs of this FlowsInfoVO.

        **参数解释**： 流转后规则配置。 **取值范围**： 不涉及。

        :return: The after_rule_configs of this FlowsInfoVO.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.WorkItemFlowRuleConfigVO`]
        """
        return self._after_rule_configs

    @after_rule_configs.setter
    def after_rule_configs(self, after_rule_configs):
        r"""Sets the after_rule_configs of this FlowsInfoVO.

        **参数解释**： 流转后规则配置。 **取值范围**： 不涉及。

        :param after_rule_configs: The after_rule_configs of this FlowsInfoVO.
        :type after_rule_configs: list[:class:`huaweicloudsdkprojectman.v4.WorkItemFlowRuleConfigVO`]
        """
        self._after_rule_configs = after_rule_configs

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
        if not isinstance(other, FlowsInfoVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
