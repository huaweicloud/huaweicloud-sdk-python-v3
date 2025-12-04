# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateCustomRuleRequestBody:

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
        'policyid': 'str',
        'description': 'str',
        'status': 'int',
        'conditions': 'list[CustomRuleConditions]',
        'action': 'CustomAction',
        'action_mode': 'bool',
        'priority': 'int',
        'time': 'bool',
        'start': 'int',
        'terminal': 'int',
        'producer': 'int',
        'policy_rule_ids': 'list[PolicyRuleIdRequestBodyPolicyRuleIds]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'policyid': 'policyid',
        'description': 'description',
        'status': 'status',
        'conditions': 'conditions',
        'action': 'action',
        'action_mode': 'action_mode',
        'priority': 'priority',
        'time': 'time',
        'start': 'start',
        'terminal': 'terminal',
        'producer': 'producer',
        'policy_rule_ids': 'policy_rule_ids'
    }

    def __init__(self, id=None, name=None, policyid=None, description=None, status=None, conditions=None, action=None, action_mode=None, priority=None, time=None, start=None, terminal=None, producer=None, policy_rule_ids=None):
        r"""BatchUpdateCustomRuleRequestBody

        The model defined in huaweicloud sdk

        :param id: 规则id
        :type id: str
        :param name: 规则名称
        :type name: str
        :param policyid: 策略id
        :type policyid: str
        :param description: 规则描述
        :type description: str
        :param status: **参数解释：** 规则状态标识，用于指定规则的启用或关闭状态 **约束限制：** 不涉及 **取值范围：**  - 0：关闭  - 1：开启 **默认取值：** 不涉及
        :type status: int
        :param conditions: 匹配条件列表，匹配条件必须同时满足。
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.CustomRuleConditions`]
        :param action: 
        :type action: :class:`huaweicloudsdkwaf.v1.CustomAction`
        :param action_mode: 预留参数，可忽略。
        :type action_mode: bool
        :param priority: 执行该规则的优先级，值越小，优先级越高，值相同时，规则创建时间早，优先级越高。取值范围：0到65535。
        :type priority: int
        :param time: 精准防护规则生效时间:  - “false”：表示该规则立即生效。   - “true”：表示自定义生效时间。
        :type time: bool
        :param start: 精准防护规则生效的起始时间戳（秒）。当time&#x3D;true，才会返回该参数。
        :type start: int
        :param terminal: 精准防护规则生效的终止时间戳（秒）。当time&#x3D;true，才会返回该参数。
        :type terminal: int
        :param producer: 规则创建对象，该参数为预留参数，用于后续功能扩展，当前请用户忽略该参数
        :type producer: int
        :param policy_rule_ids: **参数解释：** 策略和规则id数组，关联防护策略与对应的规则集合 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type policy_rule_ids: list[:class:`huaweicloudsdkwaf.v1.PolicyRuleIdRequestBodyPolicyRuleIds`]
        """
        
        

        self._id = None
        self._name = None
        self._policyid = None
        self._description = None
        self._status = None
        self._conditions = None
        self._action = None
        self._action_mode = None
        self._priority = None
        self._time = None
        self._start = None
        self._terminal = None
        self._producer = None
        self._policy_rule_ids = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if policyid is not None:
            self.policyid = policyid
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if conditions is not None:
            self.conditions = conditions
        if action is not None:
            self.action = action
        if action_mode is not None:
            self.action_mode = action_mode
        if priority is not None:
            self.priority = priority
        if time is not None:
            self.time = time
        if start is not None:
            self.start = start
        if terminal is not None:
            self.terminal = terminal
        if producer is not None:
            self.producer = producer
        if policy_rule_ids is not None:
            self.policy_rule_ids = policy_rule_ids

    @property
    def id(self):
        r"""Gets the id of this BatchUpdateCustomRuleRequestBody.

        规则id

        :return: The id of this BatchUpdateCustomRuleRequestBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BatchUpdateCustomRuleRequestBody.

        规则id

        :param id: The id of this BatchUpdateCustomRuleRequestBody.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this BatchUpdateCustomRuleRequestBody.

        规则名称

        :return: The name of this BatchUpdateCustomRuleRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BatchUpdateCustomRuleRequestBody.

        规则名称

        :param name: The name of this BatchUpdateCustomRuleRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def policyid(self):
        r"""Gets the policyid of this BatchUpdateCustomRuleRequestBody.

        策略id

        :return: The policyid of this BatchUpdateCustomRuleRequestBody.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        r"""Sets the policyid of this BatchUpdateCustomRuleRequestBody.

        策略id

        :param policyid: The policyid of this BatchUpdateCustomRuleRequestBody.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def description(self):
        r"""Gets the description of this BatchUpdateCustomRuleRequestBody.

        规则描述

        :return: The description of this BatchUpdateCustomRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BatchUpdateCustomRuleRequestBody.

        规则描述

        :param description: The description of this BatchUpdateCustomRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this BatchUpdateCustomRuleRequestBody.

        **参数解释：** 规则状态标识，用于指定规则的启用或关闭状态 **约束限制：** 不涉及 **取值范围：**  - 0：关闭  - 1：开启 **默认取值：** 不涉及

        :return: The status of this BatchUpdateCustomRuleRequestBody.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BatchUpdateCustomRuleRequestBody.

        **参数解释：** 规则状态标识，用于指定规则的启用或关闭状态 **约束限制：** 不涉及 **取值范围：**  - 0：关闭  - 1：开启 **默认取值：** 不涉及

        :param status: The status of this BatchUpdateCustomRuleRequestBody.
        :type status: int
        """
        self._status = status

    @property
    def conditions(self):
        r"""Gets the conditions of this BatchUpdateCustomRuleRequestBody.

        匹配条件列表，匹配条件必须同时满足。

        :return: The conditions of this BatchUpdateCustomRuleRequestBody.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.CustomRuleConditions`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this BatchUpdateCustomRuleRequestBody.

        匹配条件列表，匹配条件必须同时满足。

        :param conditions: The conditions of this BatchUpdateCustomRuleRequestBody.
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.CustomRuleConditions`]
        """
        self._conditions = conditions

    @property
    def action(self):
        r"""Gets the action of this BatchUpdateCustomRuleRequestBody.

        :return: The action of this BatchUpdateCustomRuleRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.CustomAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this BatchUpdateCustomRuleRequestBody.

        :param action: The action of this BatchUpdateCustomRuleRequestBody.
        :type action: :class:`huaweicloudsdkwaf.v1.CustomAction`
        """
        self._action = action

    @property
    def action_mode(self):
        r"""Gets the action_mode of this BatchUpdateCustomRuleRequestBody.

        预留参数，可忽略。

        :return: The action_mode of this BatchUpdateCustomRuleRequestBody.
        :rtype: bool
        """
        return self._action_mode

    @action_mode.setter
    def action_mode(self, action_mode):
        r"""Sets the action_mode of this BatchUpdateCustomRuleRequestBody.

        预留参数，可忽略。

        :param action_mode: The action_mode of this BatchUpdateCustomRuleRequestBody.
        :type action_mode: bool
        """
        self._action_mode = action_mode

    @property
    def priority(self):
        r"""Gets the priority of this BatchUpdateCustomRuleRequestBody.

        执行该规则的优先级，值越小，优先级越高，值相同时，规则创建时间早，优先级越高。取值范围：0到65535。

        :return: The priority of this BatchUpdateCustomRuleRequestBody.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this BatchUpdateCustomRuleRequestBody.

        执行该规则的优先级，值越小，优先级越高，值相同时，规则创建时间早，优先级越高。取值范围：0到65535。

        :param priority: The priority of this BatchUpdateCustomRuleRequestBody.
        :type priority: int
        """
        self._priority = priority

    @property
    def time(self):
        r"""Gets the time of this BatchUpdateCustomRuleRequestBody.

        精准防护规则生效时间:  - “false”：表示该规则立即生效。   - “true”：表示自定义生效时间。

        :return: The time of this BatchUpdateCustomRuleRequestBody.
        :rtype: bool
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this BatchUpdateCustomRuleRequestBody.

        精准防护规则生效时间:  - “false”：表示该规则立即生效。   - “true”：表示自定义生效时间。

        :param time: The time of this BatchUpdateCustomRuleRequestBody.
        :type time: bool
        """
        self._time = time

    @property
    def start(self):
        r"""Gets the start of this BatchUpdateCustomRuleRequestBody.

        精准防护规则生效的起始时间戳（秒）。当time=true，才会返回该参数。

        :return: The start of this BatchUpdateCustomRuleRequestBody.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this BatchUpdateCustomRuleRequestBody.

        精准防护规则生效的起始时间戳（秒）。当time=true，才会返回该参数。

        :param start: The start of this BatchUpdateCustomRuleRequestBody.
        :type start: int
        """
        self._start = start

    @property
    def terminal(self):
        r"""Gets the terminal of this BatchUpdateCustomRuleRequestBody.

        精准防护规则生效的终止时间戳（秒）。当time=true，才会返回该参数。

        :return: The terminal of this BatchUpdateCustomRuleRequestBody.
        :rtype: int
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        r"""Sets the terminal of this BatchUpdateCustomRuleRequestBody.

        精准防护规则生效的终止时间戳（秒）。当time=true，才会返回该参数。

        :param terminal: The terminal of this BatchUpdateCustomRuleRequestBody.
        :type terminal: int
        """
        self._terminal = terminal

    @property
    def producer(self):
        r"""Gets the producer of this BatchUpdateCustomRuleRequestBody.

        规则创建对象，该参数为预留参数，用于后续功能扩展，当前请用户忽略该参数

        :return: The producer of this BatchUpdateCustomRuleRequestBody.
        :rtype: int
        """
        return self._producer

    @producer.setter
    def producer(self, producer):
        r"""Sets the producer of this BatchUpdateCustomRuleRequestBody.

        规则创建对象，该参数为预留参数，用于后续功能扩展，当前请用户忽略该参数

        :param producer: The producer of this BatchUpdateCustomRuleRequestBody.
        :type producer: int
        """
        self._producer = producer

    @property
    def policy_rule_ids(self):
        r"""Gets the policy_rule_ids of this BatchUpdateCustomRuleRequestBody.

        **参数解释：** 策略和规则id数组，关联防护策略与对应的规则集合 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The policy_rule_ids of this BatchUpdateCustomRuleRequestBody.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.PolicyRuleIdRequestBodyPolicyRuleIds`]
        """
        return self._policy_rule_ids

    @policy_rule_ids.setter
    def policy_rule_ids(self, policy_rule_ids):
        r"""Sets the policy_rule_ids of this BatchUpdateCustomRuleRequestBody.

        **参数解释：** 策略和规则id数组，关联防护策略与对应的规则集合 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param policy_rule_ids: The policy_rule_ids of this BatchUpdateCustomRuleRequestBody.
        :type policy_rule_ids: list[:class:`huaweicloudsdkwaf.v1.PolicyRuleIdRequestBodyPolicyRuleIds`]
        """
        self._policy_rule_ids = policy_rule_ids

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
        if not isinstance(other, BatchUpdateCustomRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
