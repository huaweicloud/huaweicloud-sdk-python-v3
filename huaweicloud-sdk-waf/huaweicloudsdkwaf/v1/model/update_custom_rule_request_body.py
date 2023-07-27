# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCustomRuleRequestBody:

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
        'time': 'bool',
        'start': 'int',
        'terminal': 'int',
        'description': 'str',
        'conditions': 'list[CustomConditions]',
        'action': 'CustomAction',
        'priority': 'int'
    }

    attribute_map = {
        'name': 'name',
        'time': 'time',
        'start': 'start',
        'terminal': 'terminal',
        'description': 'description',
        'conditions': 'conditions',
        'action': 'action',
        'priority': 'priority'
    }

    def __init__(self, name=None, time=None, start=None, terminal=None, description=None, conditions=None, action=None, priority=None):
        """UpdateCustomRuleRequestBody

        The model defined in huaweicloud sdk

        :param name: 规则名称
        :type name: str
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
        :param priority: 执行该规则的优先级，值越小，优先级越高，值相同时，规则创建时间早，优先级越高。取值范围：0到1000。
        :type priority: int
        """
        
        

        self._name = None
        self._time = None
        self._start = None
        self._terminal = None
        self._description = None
        self._conditions = None
        self._action = None
        self._priority = None
        self.discriminator = None

        self.name = name
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

    @property
    def name(self):
        """Gets the name of this UpdateCustomRuleRequestBody.

        规则名称

        :return: The name of this UpdateCustomRuleRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateCustomRuleRequestBody.

        规则名称

        :param name: The name of this UpdateCustomRuleRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def time(self):
        """Gets the time of this UpdateCustomRuleRequestBody.

        精准防护规则生效时间:  - “false”：表示该规则立即生效。   - “true”：表示自定义生效时间。

        :return: The time of this UpdateCustomRuleRequestBody.
        :rtype: bool
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this UpdateCustomRuleRequestBody.

        精准防护规则生效时间:  - “false”：表示该规则立即生效。   - “true”：表示自定义生效时间。

        :param time: The time of this UpdateCustomRuleRequestBody.
        :type time: bool
        """
        self._time = time

    @property
    def start(self):
        """Gets the start of this UpdateCustomRuleRequestBody.

        精准防护规则生效的起始时间戳（秒）。当time=true，才需要填写该参数。

        :return: The start of this UpdateCustomRuleRequestBody.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this UpdateCustomRuleRequestBody.

        精准防护规则生效的起始时间戳（秒）。当time=true，才需要填写该参数。

        :param start: The start of this UpdateCustomRuleRequestBody.
        :type start: int
        """
        self._start = start

    @property
    def terminal(self):
        """Gets the terminal of this UpdateCustomRuleRequestBody.

        精准防护规则生效的终止时间戳（秒）。当time=true，才需要填写该参数。

        :return: The terminal of this UpdateCustomRuleRequestBody.
        :rtype: int
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """Sets the terminal of this UpdateCustomRuleRequestBody.

        精准防护规则生效的终止时间戳（秒）。当time=true，才需要填写该参数。

        :param terminal: The terminal of this UpdateCustomRuleRequestBody.
        :type terminal: int
        """
        self._terminal = terminal

    @property
    def description(self):
        """Gets the description of this UpdateCustomRuleRequestBody.

        规则描述

        :return: The description of this UpdateCustomRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateCustomRuleRequestBody.

        规则描述

        :param description: The description of this UpdateCustomRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def conditions(self):
        """Gets the conditions of this UpdateCustomRuleRequestBody.

        匹配条件列表

        :return: The conditions of this UpdateCustomRuleRequestBody.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.CustomConditions`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this UpdateCustomRuleRequestBody.

        匹配条件列表

        :param conditions: The conditions of this UpdateCustomRuleRequestBody.
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.CustomConditions`]
        """
        self._conditions = conditions

    @property
    def action(self):
        """Gets the action of this UpdateCustomRuleRequestBody.

        :return: The action of this UpdateCustomRuleRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.CustomAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this UpdateCustomRuleRequestBody.

        :param action: The action of this UpdateCustomRuleRequestBody.
        :type action: :class:`huaweicloudsdkwaf.v1.CustomAction`
        """
        self._action = action

    @property
    def priority(self):
        """Gets the priority of this UpdateCustomRuleRequestBody.

        执行该规则的优先级，值越小，优先级越高，值相同时，规则创建时间早，优先级越高。取值范围：0到1000。

        :return: The priority of this UpdateCustomRuleRequestBody.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this UpdateCustomRuleRequestBody.

        执行该规则的优先级，值越小，优先级越高，值相同时，规则创建时间早，优先级越高。取值范围：0到1000。

        :param priority: The priority of this UpdateCustomRuleRequestBody.
        :type priority: int
        """
        self._priority = priority

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
        if not isinstance(other, UpdateCustomRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
