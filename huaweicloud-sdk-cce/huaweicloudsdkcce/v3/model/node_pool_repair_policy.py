# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodePoolRepairPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'policy': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'policy': 'policy'
    }

    def __init__(self, enable=None, policy=None):
        r"""NodePoolRepairPolicy

        The model defined in huaweicloud sdk

        :param enable: **参数解释**： 系统与 K8s 组件异常时是否启用policy中配置的自愈策略。 **约束限制**： 不涉及 **取值范围**： - false：使用基础自愈策略 - true：使用policy中配置的自愈策略  **默认取值**： false
        :type enable: bool
        :param policy: **参数解释**： 节点自愈的恢复策略 **约束限制**： - 当 enable 为 true 时，此字段必填。 - 当 enable 为 false 时，此字段无效，用户填写任意值均不会生效，系统使用基础自愈策略。  **取值范围**： - restartNode：系统与 K8s 组件异常时允许通过重启节点自愈  **默认取值**： 不涉及
        :type policy: str
        """
        
        

        self._enable = None
        self._policy = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if policy is not None:
            self.policy = policy

    @property
    def enable(self):
        r"""Gets the enable of this NodePoolRepairPolicy.

        **参数解释**： 系统与 K8s 组件异常时是否启用policy中配置的自愈策略。 **约束限制**： 不涉及 **取值范围**： - false：使用基础自愈策略 - true：使用policy中配置的自愈策略  **默认取值**： false

        :return: The enable of this NodePoolRepairPolicy.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this NodePoolRepairPolicy.

        **参数解释**： 系统与 K8s 组件异常时是否启用policy中配置的自愈策略。 **约束限制**： 不涉及 **取值范围**： - false：使用基础自愈策略 - true：使用policy中配置的自愈策略  **默认取值**： false

        :param enable: The enable of this NodePoolRepairPolicy.
        :type enable: bool
        """
        self._enable = enable

    @property
    def policy(self):
        r"""Gets the policy of this NodePoolRepairPolicy.

        **参数解释**： 节点自愈的恢复策略 **约束限制**： - 当 enable 为 true 时，此字段必填。 - 当 enable 为 false 时，此字段无效，用户填写任意值均不会生效，系统使用基础自愈策略。  **取值范围**： - restartNode：系统与 K8s 组件异常时允许通过重启节点自愈  **默认取值**： 不涉及

        :return: The policy of this NodePoolRepairPolicy.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this NodePoolRepairPolicy.

        **参数解释**： 节点自愈的恢复策略 **约束限制**： - 当 enable 为 true 时，此字段必填。 - 当 enable 为 false 时，此字段无效，用户填写任意值均不会生效，系统使用基础自愈策略。  **取值范围**： - restartNode：系统与 K8s 组件异常时允许通过重启节点自愈  **默认取值**： 不涉及

        :param policy: The policy of this NodePoolRepairPolicy.
        :type policy: str
        """
        self._policy = policy

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
        if not isinstance(other, NodePoolRepairPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
