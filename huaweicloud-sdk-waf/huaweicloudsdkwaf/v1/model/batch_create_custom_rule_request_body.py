# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateCustomRuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time': 'bool',
        'start': 'int',
        'terminal': 'int',
        'description': 'str',
        'conditions': 'list[CustomConditions]',
        'action': 'CustomAction',
        'priority': 'int',
        'name': 'str',
        'policy_ids': 'list[str]'
    }

    attribute_map = {
        'time': 'time',
        'start': 'start',
        'terminal': 'terminal',
        'description': 'description',
        'conditions': 'conditions',
        'action': 'action',
        'priority': 'priority',
        'name': 'name',
        'policy_ids': 'policy_ids'
    }

    def __init__(self, time=None, start=None, terminal=None, description=None, conditions=None, action=None, priority=None, name=None, policy_ids=None):
        r"""BatchCreateCustomRuleRequestBody

        The model defined in huaweicloud sdk

        :param time: 精准防护规则生效时间:  - “false”：表示该规则立即生效。   - “true”：表示自定义生效时间。
        :type time: bool
        :param start: 精准防护规则生效的起始时间戳（秒）。当time&#x3D;true，才需要填写该参数。
        :type start: int
        :param terminal: 精准防护规则生效的终止时间戳（秒）。当time&#x3D;true，才需要填写该参数。
        :type terminal: int
        :param description: 规则描述
        :type description: str
        :param conditions: 匹配条件列表
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.CustomConditions`]
        :param action: 
        :type action: :class:`huaweicloudsdkwaf.v1.CustomAction`
        :param priority: 执行该规则的优先级，值越小，优先级越高，值相同时，规则创建时间早，优先级越高。取值范围：0到65535。
        :type priority: int
        :param name: 规则名称
        :type name: str
        :param policy_ids: 策略id
        :type policy_ids: list[str]
        """
        
        

        self._time = None
        self._start = None
        self._terminal = None
        self._description = None
        self._conditions = None
        self._action = None
        self._priority = None
        self._name = None
        self._policy_ids = None
        self.discriminator = None

        self.time = time
        if start is not None:
            self.start = start
        if terminal is not None:
            self.terminal = terminal
        if description is not None:
            self.description = description
        self.conditions = conditions
        self.action = action
        self.priority = priority
        self.name = name
        if policy_ids is not None:
            self.policy_ids = policy_ids

    @property
    def time(self):
        r"""Gets the time of this BatchCreateCustomRuleRequestBody.

        精准防护规则生效时间:  - “false”：表示该规则立即生效。   - “true”：表示自定义生效时间。

        :return: The time of this BatchCreateCustomRuleRequestBody.
        :rtype: bool
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this BatchCreateCustomRuleRequestBody.

        精准防护规则生效时间:  - “false”：表示该规则立即生效。   - “true”：表示自定义生效时间。

        :param time: The time of this BatchCreateCustomRuleRequestBody.
        :type time: bool
        """
        self._time = time

    @property
    def start(self):
        r"""Gets the start of this BatchCreateCustomRuleRequestBody.

        精准防护规则生效的起始时间戳（秒）。当time=true，才需要填写该参数。

        :return: The start of this BatchCreateCustomRuleRequestBody.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this BatchCreateCustomRuleRequestBody.

        精准防护规则生效的起始时间戳（秒）。当time=true，才需要填写该参数。

        :param start: The start of this BatchCreateCustomRuleRequestBody.
        :type start: int
        """
        self._start = start

    @property
    def terminal(self):
        r"""Gets the terminal of this BatchCreateCustomRuleRequestBody.

        精准防护规则生效的终止时间戳（秒）。当time=true，才需要填写该参数。

        :return: The terminal of this BatchCreateCustomRuleRequestBody.
        :rtype: int
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        r"""Sets the terminal of this BatchCreateCustomRuleRequestBody.

        精准防护规则生效的终止时间戳（秒）。当time=true，才需要填写该参数。

        :param terminal: The terminal of this BatchCreateCustomRuleRequestBody.
        :type terminal: int
        """
        self._terminal = terminal

    @property
    def description(self):
        r"""Gets the description of this BatchCreateCustomRuleRequestBody.

        规则描述

        :return: The description of this BatchCreateCustomRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BatchCreateCustomRuleRequestBody.

        规则描述

        :param description: The description of this BatchCreateCustomRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def conditions(self):
        r"""Gets the conditions of this BatchCreateCustomRuleRequestBody.

        匹配条件列表

        :return: The conditions of this BatchCreateCustomRuleRequestBody.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.CustomConditions`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this BatchCreateCustomRuleRequestBody.

        匹配条件列表

        :param conditions: The conditions of this BatchCreateCustomRuleRequestBody.
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.CustomConditions`]
        """
        self._conditions = conditions

    @property
    def action(self):
        r"""Gets the action of this BatchCreateCustomRuleRequestBody.

        :return: The action of this BatchCreateCustomRuleRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.CustomAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this BatchCreateCustomRuleRequestBody.

        :param action: The action of this BatchCreateCustomRuleRequestBody.
        :type action: :class:`huaweicloudsdkwaf.v1.CustomAction`
        """
        self._action = action

    @property
    def priority(self):
        r"""Gets the priority of this BatchCreateCustomRuleRequestBody.

        执行该规则的优先级，值越小，优先级越高，值相同时，规则创建时间早，优先级越高。取值范围：0到65535。

        :return: The priority of this BatchCreateCustomRuleRequestBody.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this BatchCreateCustomRuleRequestBody.

        执行该规则的优先级，值越小，优先级越高，值相同时，规则创建时间早，优先级越高。取值范围：0到65535。

        :param priority: The priority of this BatchCreateCustomRuleRequestBody.
        :type priority: int
        """
        self._priority = priority

    @property
    def name(self):
        r"""Gets the name of this BatchCreateCustomRuleRequestBody.

        规则名称

        :return: The name of this BatchCreateCustomRuleRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BatchCreateCustomRuleRequestBody.

        规则名称

        :param name: The name of this BatchCreateCustomRuleRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def policy_ids(self):
        r"""Gets the policy_ids of this BatchCreateCustomRuleRequestBody.

        策略id

        :return: The policy_ids of this BatchCreateCustomRuleRequestBody.
        :rtype: list[str]
        """
        return self._policy_ids

    @policy_ids.setter
    def policy_ids(self, policy_ids):
        r"""Sets the policy_ids of this BatchCreateCustomRuleRequestBody.

        策略id

        :param policy_ids: The policy_ids of this BatchCreateCustomRuleRequestBody.
        :type policy_ids: list[str]
        """
        self._policy_ids = policy_ids

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
        if not isinstance(other, BatchCreateCustomRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
