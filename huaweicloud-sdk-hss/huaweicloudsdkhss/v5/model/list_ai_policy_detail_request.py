# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAiPolicyDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_id': 'str',
        'policy_name': 'str'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'policy_name': 'policy_name'
    }

    def __init__(self, policy_id=None, policy_name=None):
        r"""ListAiPolicyDetailRequest

        The model defined in huaweicloud sdk

        :param policy_id: **参数解释**： 策略组ID **约束限制**： 必填 **取值范围**： 最小值0，最大值9223372036854775807 **默认取值**： 不涉及 
        :type policy_id: str
        :param policy_name: **参数解释**： 策略名称 **约束限制**： 必填 **取值范围**： - 0: 意图行为一致性检测 - 1: 命令执行控制 - 2: 文件访问控制 - 3: 敏感信息检测 - 4: 角色限定  **默认取值**： 不涉及 
        :type policy_name: str
        """
        
        

        self._policy_id = None
        self._policy_name = None
        self.discriminator = None

        self.policy_id = policy_id
        self.policy_name = policy_name

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ListAiPolicyDetailRequest.

        **参数解释**： 策略组ID **约束限制**： 必填 **取值范围**： 最小值0，最大值9223372036854775807 **默认取值**： 不涉及 

        :return: The policy_id of this ListAiPolicyDetailRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ListAiPolicyDetailRequest.

        **参数解释**： 策略组ID **约束限制**： 必填 **取值范围**： 最小值0，最大值9223372036854775807 **默认取值**： 不涉及 

        :param policy_id: The policy_id of this ListAiPolicyDetailRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def policy_name(self):
        r"""Gets the policy_name of this ListAiPolicyDetailRequest.

        **参数解释**： 策略名称 **约束限制**： 必填 **取值范围**： - 0: 意图行为一致性检测 - 1: 命令执行控制 - 2: 文件访问控制 - 3: 敏感信息检测 - 4: 角色限定  **默认取值**： 不涉及 

        :return: The policy_name of this ListAiPolicyDetailRequest.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this ListAiPolicyDetailRequest.

        **参数解释**： 策略名称 **约束限制**： 必填 **取值范围**： - 0: 意图行为一致性检测 - 1: 命令执行控制 - 2: 文件访问控制 - 3: 敏感信息检测 - 4: 角色限定  **默认取值**： 不涉及 

        :param policy_name: The policy_name of this ListAiPolicyDetailRequest.
        :type policy_name: str
        """
        self._policy_name = policy_name

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
        if not isinstance(other, ListAiPolicyDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
