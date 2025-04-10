# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WafCustomRule:

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
        'time': 'bool',
        'start': 'int',
        'terminal': 'int',
        'priority': 'int',
        'conditions': 'list[WafCustomCondition]',
        'action': 'WafCustomRuleAction',
        'domain_name': 'str',
        'overseas_type': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'time': 'time',
        'start': 'start',
        'terminal': 'terminal',
        'priority': 'priority',
        'conditions': 'conditions',
        'action': 'action',
        'domain_name': 'domain_name',
        'overseas_type': 'overseas_type'
    }

    def __init__(self, id=None, name=None, time=None, start=None, terminal=None, priority=None, conditions=None, action=None, domain_name=None, overseas_type=None):
        r"""WafCustomRule

        The model defined in huaweicloud sdk

        :param id: id
        :type id: str
        :param name: name
        :type name: str
        :param time: 精准防护规则生效时间。true-自定义生效时间，false-立即生效
        :type time: bool
        :param start: 精准防护规则生效的起始时间戳（秒）
        :type start: int
        :param terminal: 精准防护规则生效的终止时间戳（秒）
        :type terminal: int
        :param priority: 执行该规则的优先级，值越小，优先级越高。取值范围：0到1000。
        :type priority: int
        :param conditions: condition
        :type conditions: list[:class:`huaweicloudsdkaad.v2.WafCustomCondition`]
        :param action: 
        :type action: :class:`huaweicloudsdkaad.v2.WafCustomRuleAction`
        :param domain_name: 域名
        :type domain_name: str
        :param overseas_type: 防护区域，0-大陆，1-海外
        :type overseas_type: int
        """
        
        

        self._id = None
        self._name = None
        self._time = None
        self._start = None
        self._terminal = None
        self._priority = None
        self._conditions = None
        self._action = None
        self._domain_name = None
        self._overseas_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        self.time = time
        if start is not None:
            self.start = start
        if terminal is not None:
            self.terminal = terminal
        self.priority = priority
        if conditions is not None:
            self.conditions = conditions
        if action is not None:
            self.action = action
        if domain_name is not None:
            self.domain_name = domain_name
        if overseas_type is not None:
            self.overseas_type = overseas_type

    @property
    def id(self):
        r"""Gets the id of this WafCustomRule.

        id

        :return: The id of this WafCustomRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this WafCustomRule.

        id

        :param id: The id of this WafCustomRule.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this WafCustomRule.

        name

        :return: The name of this WafCustomRule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this WafCustomRule.

        name

        :param name: The name of this WafCustomRule.
        :type name: str
        """
        self._name = name

    @property
    def time(self):
        r"""Gets the time of this WafCustomRule.

        精准防护规则生效时间。true-自定义生效时间，false-立即生效

        :return: The time of this WafCustomRule.
        :rtype: bool
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this WafCustomRule.

        精准防护规则生效时间。true-自定义生效时间，false-立即生效

        :param time: The time of this WafCustomRule.
        :type time: bool
        """
        self._time = time

    @property
    def start(self):
        r"""Gets the start of this WafCustomRule.

        精准防护规则生效的起始时间戳（秒）

        :return: The start of this WafCustomRule.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this WafCustomRule.

        精准防护规则生效的起始时间戳（秒）

        :param start: The start of this WafCustomRule.
        :type start: int
        """
        self._start = start

    @property
    def terminal(self):
        r"""Gets the terminal of this WafCustomRule.

        精准防护规则生效的终止时间戳（秒）

        :return: The terminal of this WafCustomRule.
        :rtype: int
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        r"""Sets the terminal of this WafCustomRule.

        精准防护规则生效的终止时间戳（秒）

        :param terminal: The terminal of this WafCustomRule.
        :type terminal: int
        """
        self._terminal = terminal

    @property
    def priority(self):
        r"""Gets the priority of this WafCustomRule.

        执行该规则的优先级，值越小，优先级越高。取值范围：0到1000。

        :return: The priority of this WafCustomRule.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this WafCustomRule.

        执行该规则的优先级，值越小，优先级越高。取值范围：0到1000。

        :param priority: The priority of this WafCustomRule.
        :type priority: int
        """
        self._priority = priority

    @property
    def conditions(self):
        r"""Gets the conditions of this WafCustomRule.

        condition

        :return: The conditions of this WafCustomRule.
        :rtype: list[:class:`huaweicloudsdkaad.v2.WafCustomCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this WafCustomRule.

        condition

        :param conditions: The conditions of this WafCustomRule.
        :type conditions: list[:class:`huaweicloudsdkaad.v2.WafCustomCondition`]
        """
        self._conditions = conditions

    @property
    def action(self):
        r"""Gets the action of this WafCustomRule.

        :return: The action of this WafCustomRule.
        :rtype: :class:`huaweicloudsdkaad.v2.WafCustomRuleAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this WafCustomRule.

        :param action: The action of this WafCustomRule.
        :type action: :class:`huaweicloudsdkaad.v2.WafCustomRuleAction`
        """
        self._action = action

    @property
    def domain_name(self):
        r"""Gets the domain_name of this WafCustomRule.

        域名

        :return: The domain_name of this WafCustomRule.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this WafCustomRule.

        域名

        :param domain_name: The domain_name of this WafCustomRule.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def overseas_type(self):
        r"""Gets the overseas_type of this WafCustomRule.

        防护区域，0-大陆，1-海外

        :return: The overseas_type of this WafCustomRule.
        :rtype: int
        """
        return self._overseas_type

    @overseas_type.setter
    def overseas_type(self, overseas_type):
        r"""Sets the overseas_type of this WafCustomRule.

        防护区域，0-大陆，1-海外

        :param overseas_type: The overseas_type of this WafCustomRule.
        :type overseas_type: int
        """
        self._overseas_type = overseas_type

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
        if not isinstance(other, WafCustomRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
