# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHttpAccessControlRuleRequestBody:

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
        'status': 'int',
        'time': 'bool',
        'start': 'int',
        'terminal': 'int',
        'priority': 'int',
        'conditions': 'list[HttpAccessControlRuleCondition]',
        'action': 'HttpRuleAction'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'time': 'time',
        'start': 'start',
        'terminal': 'terminal',
        'priority': 'priority',
        'conditions': 'conditions',
        'action': 'action'
    }

    def __init__(self, name=None, description=None, status=None, time=None, start=None, terminal=None, priority=None, conditions=None, action=None):
        r"""UpdateHttpAccessControlRuleRequestBody

        The model defined in huaweicloud sdk

        :param name: 规则名称
        :type name: str
        :param description: 规则描述，最长512字符
        :type description: str
        :param status: 规则开关状态
        :type status: int
        :param time: 是否设定生效时间
        :type time: bool
        :param start: 生效时间
        :type start: int
        :param terminal: 失效时间
        :type terminal: int
        :param priority: 优先级
        :type priority: int
        :param conditions: 命中条件
        :type conditions: list[:class:`huaweicloudsdkedgesec.v2.HttpAccessControlRuleCondition`]
        :param action: 
        :type action: :class:`huaweicloudsdkedgesec.v2.HttpRuleAction`
        """
        
        

        self._name = None
        self._description = None
        self._status = None
        self._time = None
        self._start = None
        self._terminal = None
        self._priority = None
        self._conditions = None
        self._action = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        self.time = time
        if start is not None:
            self.start = start
        if terminal is not None:
            self.terminal = terminal
        self.priority = priority
        self.conditions = conditions
        self.action = action

    @property
    def name(self):
        r"""Gets the name of this UpdateHttpAccessControlRuleRequestBody.

        规则名称

        :return: The name of this UpdateHttpAccessControlRuleRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateHttpAccessControlRuleRequestBody.

        规则名称

        :param name: The name of this UpdateHttpAccessControlRuleRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateHttpAccessControlRuleRequestBody.

        规则描述，最长512字符

        :return: The description of this UpdateHttpAccessControlRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateHttpAccessControlRuleRequestBody.

        规则描述，最长512字符

        :param description: The description of this UpdateHttpAccessControlRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this UpdateHttpAccessControlRuleRequestBody.

        规则开关状态

        :return: The status of this UpdateHttpAccessControlRuleRequestBody.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateHttpAccessControlRuleRequestBody.

        规则开关状态

        :param status: The status of this UpdateHttpAccessControlRuleRequestBody.
        :type status: int
        """
        self._status = status

    @property
    def time(self):
        r"""Gets the time of this UpdateHttpAccessControlRuleRequestBody.

        是否设定生效时间

        :return: The time of this UpdateHttpAccessControlRuleRequestBody.
        :rtype: bool
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this UpdateHttpAccessControlRuleRequestBody.

        是否设定生效时间

        :param time: The time of this UpdateHttpAccessControlRuleRequestBody.
        :type time: bool
        """
        self._time = time

    @property
    def start(self):
        r"""Gets the start of this UpdateHttpAccessControlRuleRequestBody.

        生效时间

        :return: The start of this UpdateHttpAccessControlRuleRequestBody.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this UpdateHttpAccessControlRuleRequestBody.

        生效时间

        :param start: The start of this UpdateHttpAccessControlRuleRequestBody.
        :type start: int
        """
        self._start = start

    @property
    def terminal(self):
        r"""Gets the terminal of this UpdateHttpAccessControlRuleRequestBody.

        失效时间

        :return: The terminal of this UpdateHttpAccessControlRuleRequestBody.
        :rtype: int
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        r"""Sets the terminal of this UpdateHttpAccessControlRuleRequestBody.

        失效时间

        :param terminal: The terminal of this UpdateHttpAccessControlRuleRequestBody.
        :type terminal: int
        """
        self._terminal = terminal

    @property
    def priority(self):
        r"""Gets the priority of this UpdateHttpAccessControlRuleRequestBody.

        优先级

        :return: The priority of this UpdateHttpAccessControlRuleRequestBody.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this UpdateHttpAccessControlRuleRequestBody.

        优先级

        :param priority: The priority of this UpdateHttpAccessControlRuleRequestBody.
        :type priority: int
        """
        self._priority = priority

    @property
    def conditions(self):
        r"""Gets the conditions of this UpdateHttpAccessControlRuleRequestBody.

        命中条件

        :return: The conditions of this UpdateHttpAccessControlRuleRequestBody.
        :rtype: list[:class:`huaweicloudsdkedgesec.v2.HttpAccessControlRuleCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this UpdateHttpAccessControlRuleRequestBody.

        命中条件

        :param conditions: The conditions of this UpdateHttpAccessControlRuleRequestBody.
        :type conditions: list[:class:`huaweicloudsdkedgesec.v2.HttpAccessControlRuleCondition`]
        """
        self._conditions = conditions

    @property
    def action(self):
        r"""Gets the action of this UpdateHttpAccessControlRuleRequestBody.

        :return: The action of this UpdateHttpAccessControlRuleRequestBody.
        :rtype: :class:`huaweicloudsdkedgesec.v2.HttpRuleAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this UpdateHttpAccessControlRuleRequestBody.

        :param action: The action of this UpdateHttpAccessControlRuleRequestBody.
        :type action: :class:`huaweicloudsdkedgesec.v2.HttpRuleAction`
        """
        self._action = action

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
        if not isinstance(other, UpdateHttpAccessControlRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
