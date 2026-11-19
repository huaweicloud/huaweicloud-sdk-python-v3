# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AiAgentPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_group_name': 'str',
        'policy_group_id': 'str',
        'policy_group_type': 'int',
        'policy_group_enabled': 'bool',
        'is_default': 'bool'
    }

    attribute_map = {
        'policy_group_name': 'policy_group_name',
        'policy_group_id': 'policy_group_id',
        'policy_group_type': 'policy_group_type',
        'policy_group_enabled': 'policy_group_enabled',
        'is_default': 'is_default'
    }

    def __init__(self, policy_group_name=None, policy_group_id=None, policy_group_type=None, policy_group_enabled=None, is_default=None):
        r"""AiAgentPolicy

        The model defined in huaweicloud sdk

        :param policy_group_name: **参数解释**: 策略组名称 **取值范围**: 字符长度1-128位 
        :type policy_group_name: str
        :param policy_group_id: **参数解释**： 策略组ID **取值范围**： 字符长度1-20位 
        :type policy_group_id: str
        :param policy_group_type: **参数解释**： 策略组类型 **取值范围**： - 0：Agent运行时防护-OfficeAce - 1：Agent行为轨迹检测-OfficeAce - 2：Agent角色限定 - 3：Agent运行时防护-AgentArts - 4：Agent行为轨迹检测-AgentArts - 5：Agent运行时防护-OpenClaw - 6：Agent运行时防护-其他三方Claw 
        :type policy_group_type: int
        :param policy_group_enabled: **参数解释**: 策略组是否启用 **取值范围**: - true：已启用 - false：未启用 
        :type policy_group_enabled: bool
        :param is_default: **参数解释**: 是否是默认策略 **取值范围**: - false：否 - true：是 
        :type is_default: bool
        """
        
        

        self._policy_group_name = None
        self._policy_group_id = None
        self._policy_group_type = None
        self._policy_group_enabled = None
        self._is_default = None
        self.discriminator = None

        if policy_group_name is not None:
            self.policy_group_name = policy_group_name
        if policy_group_id is not None:
            self.policy_group_id = policy_group_id
        if policy_group_type is not None:
            self.policy_group_type = policy_group_type
        if policy_group_enabled is not None:
            self.policy_group_enabled = policy_group_enabled
        if is_default is not None:
            self.is_default = is_default

    @property
    def policy_group_name(self):
        r"""Gets the policy_group_name of this AiAgentPolicy.

        **参数解释**: 策略组名称 **取值范围**: 字符长度1-128位 

        :return: The policy_group_name of this AiAgentPolicy.
        :rtype: str
        """
        return self._policy_group_name

    @policy_group_name.setter
    def policy_group_name(self, policy_group_name):
        r"""Sets the policy_group_name of this AiAgentPolicy.

        **参数解释**: 策略组名称 **取值范围**: 字符长度1-128位 

        :param policy_group_name: The policy_group_name of this AiAgentPolicy.
        :type policy_group_name: str
        """
        self._policy_group_name = policy_group_name

    @property
    def policy_group_id(self):
        r"""Gets the policy_group_id of this AiAgentPolicy.

        **参数解释**： 策略组ID **取值范围**： 字符长度1-20位 

        :return: The policy_group_id of this AiAgentPolicy.
        :rtype: str
        """
        return self._policy_group_id

    @policy_group_id.setter
    def policy_group_id(self, policy_group_id):
        r"""Sets the policy_group_id of this AiAgentPolicy.

        **参数解释**： 策略组ID **取值范围**： 字符长度1-20位 

        :param policy_group_id: The policy_group_id of this AiAgentPolicy.
        :type policy_group_id: str
        """
        self._policy_group_id = policy_group_id

    @property
    def policy_group_type(self):
        r"""Gets the policy_group_type of this AiAgentPolicy.

        **参数解释**： 策略组类型 **取值范围**： - 0：Agent运行时防护-OfficeAce - 1：Agent行为轨迹检测-OfficeAce - 2：Agent角色限定 - 3：Agent运行时防护-AgentArts - 4：Agent行为轨迹检测-AgentArts - 5：Agent运行时防护-OpenClaw - 6：Agent运行时防护-其他三方Claw 

        :return: The policy_group_type of this AiAgentPolicy.
        :rtype: int
        """
        return self._policy_group_type

    @policy_group_type.setter
    def policy_group_type(self, policy_group_type):
        r"""Sets the policy_group_type of this AiAgentPolicy.

        **参数解释**： 策略组类型 **取值范围**： - 0：Agent运行时防护-OfficeAce - 1：Agent行为轨迹检测-OfficeAce - 2：Agent角色限定 - 3：Agent运行时防护-AgentArts - 4：Agent行为轨迹检测-AgentArts - 5：Agent运行时防护-OpenClaw - 6：Agent运行时防护-其他三方Claw 

        :param policy_group_type: The policy_group_type of this AiAgentPolicy.
        :type policy_group_type: int
        """
        self._policy_group_type = policy_group_type

    @property
    def policy_group_enabled(self):
        r"""Gets the policy_group_enabled of this AiAgentPolicy.

        **参数解释**: 策略组是否启用 **取值范围**: - true：已启用 - false：未启用 

        :return: The policy_group_enabled of this AiAgentPolicy.
        :rtype: bool
        """
        return self._policy_group_enabled

    @policy_group_enabled.setter
    def policy_group_enabled(self, policy_group_enabled):
        r"""Sets the policy_group_enabled of this AiAgentPolicy.

        **参数解释**: 策略组是否启用 **取值范围**: - true：已启用 - false：未启用 

        :param policy_group_enabled: The policy_group_enabled of this AiAgentPolicy.
        :type policy_group_enabled: bool
        """
        self._policy_group_enabled = policy_group_enabled

    @property
    def is_default(self):
        r"""Gets the is_default of this AiAgentPolicy.

        **参数解释**: 是否是默认策略 **取值范围**: - false：否 - true：是 

        :return: The is_default of this AiAgentPolicy.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        r"""Sets the is_default of this AiAgentPolicy.

        **参数解释**: 是否是默认策略 **取值范围**: - false：否 - true：是 

        :param is_default: The is_default of this AiAgentPolicy.
        :type is_default: bool
        """
        self._is_default = is_default

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
        if not isinstance(other, AiAgentPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
