# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyDefinition:

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
        'name': 'str',
        'display_name': 'str',
        'policy_type': 'str',
        'description': 'str',
        'policy_rule_type': 'str',
        'policy_rule': 'object',
        'trigger_type': 'str',
        'keywords': 'list[str]',
        'default_resource_types': 'list[PolicyDefinitionDefaultResourceTypes]',
        'parameters': 'dict(str, PolicyParameterDefinition)'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'display_name': 'display_name',
        'policy_type': 'policy_type',
        'description': 'description',
        'policy_rule_type': 'policy_rule_type',
        'policy_rule': 'policy_rule',
        'trigger_type': 'trigger_type',
        'keywords': 'keywords',
        'default_resource_types': 'default_resource_types',
        'parameters': 'parameters'
    }

    def __init__(self, id=None, name=None, display_name=None, policy_type=None, description=None, policy_rule_type=None, policy_rule=None, trigger_type=None, keywords=None, default_resource_types=None, parameters=None):
        r"""PolicyDefinition

        The model defined in huaweicloud sdk

        :param id: 策略id
        :type id: str
        :param name: 策略名字
        :type name: str
        :param display_name: 策略展示名
        :type display_name: str
        :param policy_type: 策略类型
        :type policy_type: str
        :param description: 策略描述
        :type description: str
        :param policy_rule_type: 策略语法类型
        :type policy_rule_type: str
        :param policy_rule: 策略规则
        :type policy_rule: object
        :param trigger_type: 触发器类型，可选值：resource, period
        :type trigger_type: str
        :param keywords: 关键词列表
        :type keywords: list[str]
        :param default_resource_types: 默认资源类型列表
        :type default_resource_types: list[:class:`huaweicloudsdkconfig.v1.PolicyDefinitionDefaultResourceTypes`]
        :param parameters: 策略参数
        :type parameters: dict(str, PolicyParameterDefinition)
        """
        
        

        self._id = None
        self._name = None
        self._display_name = None
        self._policy_type = None
        self._description = None
        self._policy_rule_type = None
        self._policy_rule = None
        self._trigger_type = None
        self._keywords = None
        self._default_resource_types = None
        self._parameters = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if policy_type is not None:
            self.policy_type = policy_type
        if description is not None:
            self.description = description
        if policy_rule_type is not None:
            self.policy_rule_type = policy_rule_type
        if policy_rule is not None:
            self.policy_rule = policy_rule
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if keywords is not None:
            self.keywords = keywords
        if default_resource_types is not None:
            self.default_resource_types = default_resource_types
        if parameters is not None:
            self.parameters = parameters

    @property
    def id(self):
        r"""Gets the id of this PolicyDefinition.

        策略id

        :return: The id of this PolicyDefinition.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PolicyDefinition.

        策略id

        :param id: The id of this PolicyDefinition.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this PolicyDefinition.

        策略名字

        :return: The name of this PolicyDefinition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PolicyDefinition.

        策略名字

        :param name: The name of this PolicyDefinition.
        :type name: str
        """
        self._name = name

    @property
    def display_name(self):
        r"""Gets the display_name of this PolicyDefinition.

        策略展示名

        :return: The display_name of this PolicyDefinition.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this PolicyDefinition.

        策略展示名

        :param display_name: The display_name of this PolicyDefinition.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def policy_type(self):
        r"""Gets the policy_type of this PolicyDefinition.

        策略类型

        :return: The policy_type of this PolicyDefinition.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        r"""Sets the policy_type of this PolicyDefinition.

        策略类型

        :param policy_type: The policy_type of this PolicyDefinition.
        :type policy_type: str
        """
        self._policy_type = policy_type

    @property
    def description(self):
        r"""Gets the description of this PolicyDefinition.

        策略描述

        :return: The description of this PolicyDefinition.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PolicyDefinition.

        策略描述

        :param description: The description of this PolicyDefinition.
        :type description: str
        """
        self._description = description

    @property
    def policy_rule_type(self):
        r"""Gets the policy_rule_type of this PolicyDefinition.

        策略语法类型

        :return: The policy_rule_type of this PolicyDefinition.
        :rtype: str
        """
        return self._policy_rule_type

    @policy_rule_type.setter
    def policy_rule_type(self, policy_rule_type):
        r"""Sets the policy_rule_type of this PolicyDefinition.

        策略语法类型

        :param policy_rule_type: The policy_rule_type of this PolicyDefinition.
        :type policy_rule_type: str
        """
        self._policy_rule_type = policy_rule_type

    @property
    def policy_rule(self):
        r"""Gets the policy_rule of this PolicyDefinition.

        策略规则

        :return: The policy_rule of this PolicyDefinition.
        :rtype: object
        """
        return self._policy_rule

    @policy_rule.setter
    def policy_rule(self, policy_rule):
        r"""Sets the policy_rule of this PolicyDefinition.

        策略规则

        :param policy_rule: The policy_rule of this PolicyDefinition.
        :type policy_rule: object
        """
        self._policy_rule = policy_rule

    @property
    def trigger_type(self):
        r"""Gets the trigger_type of this PolicyDefinition.

        触发器类型，可选值：resource, period

        :return: The trigger_type of this PolicyDefinition.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        r"""Sets the trigger_type of this PolicyDefinition.

        触发器类型，可选值：resource, period

        :param trigger_type: The trigger_type of this PolicyDefinition.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def keywords(self):
        r"""Gets the keywords of this PolicyDefinition.

        关键词列表

        :return: The keywords of this PolicyDefinition.
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        r"""Sets the keywords of this PolicyDefinition.

        关键词列表

        :param keywords: The keywords of this PolicyDefinition.
        :type keywords: list[str]
        """
        self._keywords = keywords

    @property
    def default_resource_types(self):
        r"""Gets the default_resource_types of this PolicyDefinition.

        默认资源类型列表

        :return: The default_resource_types of this PolicyDefinition.
        :rtype: list[:class:`huaweicloudsdkconfig.v1.PolicyDefinitionDefaultResourceTypes`]
        """
        return self._default_resource_types

    @default_resource_types.setter
    def default_resource_types(self, default_resource_types):
        r"""Sets the default_resource_types of this PolicyDefinition.

        默认资源类型列表

        :param default_resource_types: The default_resource_types of this PolicyDefinition.
        :type default_resource_types: list[:class:`huaweicloudsdkconfig.v1.PolicyDefinitionDefaultResourceTypes`]
        """
        self._default_resource_types = default_resource_types

    @property
    def parameters(self):
        r"""Gets the parameters of this PolicyDefinition.

        策略参数

        :return: The parameters of this PolicyDefinition.
        :rtype: dict(str, PolicyParameterDefinition)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this PolicyDefinition.

        策略参数

        :param parameters: The parameters of this PolicyDefinition.
        :type parameters: dict(str, PolicyParameterDefinition)
        """
        self._parameters = parameters

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
        if not isinstance(other, PolicyDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
