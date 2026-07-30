# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAlarmWhiteListRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_id': 'str',
        'scope': 'bool',
        'agent_ids': 'list[str]',
        'instance_ids': 'list[str]'
    }

    attribute_map = {
        'rule_id': 'rule_id',
        'scope': 'scope',
        'agent_ids': 'agent_ids',
        'instance_ids': 'instance_ids'
    }

    def __init__(self, rule_id=None, scope=None, agent_ids=None, instance_ids=None):
        r"""UpdateAlarmWhiteListRequestInfo

        The model defined in huaweicloud sdk

        :param rule_id: **参数解释**： 规则ID **约束限制**： 必填 **取值范围**： 字符长度1-36位 **默认取值**： 不涉及 
        :type rule_id: str
        :param scope: **参数解释**: 是否选择所有主机 **约束限制**: 不涉及 **取值范围**: - true：是 - false：否 **默认取值**: false 
        :type scope: bool
        :param agent_ids: **参数解释**: agent列表 **约束限制**: 不涉及 **取值范围**: 1-1000个agentID **默认取值**: 不涉及 
        :type agent_ids: list[str]
        :param instance_ids: **参数解释**: 实例ID列表 **约束限制**: 当需要为serverless配置规则时，传入此字段 **取值范围**: 1-1000个实例ID **默认取值**: 不涉及 
        :type instance_ids: list[str]
        """
        
        

        self._rule_id = None
        self._scope = None
        self._agent_ids = None
        self._instance_ids = None
        self.discriminator = None

        self.rule_id = rule_id
        if scope is not None:
            self.scope = scope
        if agent_ids is not None:
            self.agent_ids = agent_ids
        if instance_ids is not None:
            self.instance_ids = instance_ids

    @property
    def rule_id(self):
        r"""Gets the rule_id of this UpdateAlarmWhiteListRequestInfo.

        **参数解释**： 规则ID **约束限制**： 必填 **取值范围**： 字符长度1-36位 **默认取值**： 不涉及 

        :return: The rule_id of this UpdateAlarmWhiteListRequestInfo.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this UpdateAlarmWhiteListRequestInfo.

        **参数解释**： 规则ID **约束限制**： 必填 **取值范围**： 字符长度1-36位 **默认取值**： 不涉及 

        :param rule_id: The rule_id of this UpdateAlarmWhiteListRequestInfo.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def scope(self):
        r"""Gets the scope of this UpdateAlarmWhiteListRequestInfo.

        **参数解释**: 是否选择所有主机 **约束限制**: 不涉及 **取值范围**: - true：是 - false：否 **默认取值**: false 

        :return: The scope of this UpdateAlarmWhiteListRequestInfo.
        :rtype: bool
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this UpdateAlarmWhiteListRequestInfo.

        **参数解释**: 是否选择所有主机 **约束限制**: 不涉及 **取值范围**: - true：是 - false：否 **默认取值**: false 

        :param scope: The scope of this UpdateAlarmWhiteListRequestInfo.
        :type scope: bool
        """
        self._scope = scope

    @property
    def agent_ids(self):
        r"""Gets the agent_ids of this UpdateAlarmWhiteListRequestInfo.

        **参数解释**: agent列表 **约束限制**: 不涉及 **取值范围**: 1-1000个agentID **默认取值**: 不涉及 

        :return: The agent_ids of this UpdateAlarmWhiteListRequestInfo.
        :rtype: list[str]
        """
        return self._agent_ids

    @agent_ids.setter
    def agent_ids(self, agent_ids):
        r"""Sets the agent_ids of this UpdateAlarmWhiteListRequestInfo.

        **参数解释**: agent列表 **约束限制**: 不涉及 **取值范围**: 1-1000个agentID **默认取值**: 不涉及 

        :param agent_ids: The agent_ids of this UpdateAlarmWhiteListRequestInfo.
        :type agent_ids: list[str]
        """
        self._agent_ids = agent_ids

    @property
    def instance_ids(self):
        r"""Gets the instance_ids of this UpdateAlarmWhiteListRequestInfo.

        **参数解释**: 实例ID列表 **约束限制**: 当需要为serverless配置规则时，传入此字段 **取值范围**: 1-1000个实例ID **默认取值**: 不涉及 

        :return: The instance_ids of this UpdateAlarmWhiteListRequestInfo.
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        r"""Sets the instance_ids of this UpdateAlarmWhiteListRequestInfo.

        **参数解释**: 实例ID列表 **约束限制**: 当需要为serverless配置规则时，传入此字段 **取值范围**: 1-1000个实例ID **默认取值**: 不涉及 

        :param instance_ids: The instance_ids of this UpdateAlarmWhiteListRequestInfo.
        :type instance_ids: list[str]
        """
        self._instance_ids = instance_ids

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
        if not isinstance(other, UpdateAlarmWhiteListRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
