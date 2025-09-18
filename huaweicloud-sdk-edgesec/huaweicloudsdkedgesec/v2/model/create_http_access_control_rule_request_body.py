# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateHttpAccessControlRuleRequestBody:

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
        'start': 'int',
        'terminal': 'int',
        'time_mode': 'str',
        'period_type': 'str',
        'time_range': 'list[TimeRangeItem]',
        'time_zone': 'str',
        'priority': 'int',
        'conditions': 'list[HttpAccessControlRuleCondition]',
        'action': 'HttpRuleAction'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'start': 'start',
        'terminal': 'terminal',
        'time_mode': 'time_mode',
        'period_type': 'period_type',
        'time_range': 'time_range',
        'time_zone': 'time_zone',
        'priority': 'priority',
        'conditions': 'conditions',
        'action': 'action'
    }

    def __init__(self, name=None, description=None, start=None, terminal=None, time_mode=None, period_type=None, time_range=None, time_zone=None, priority=None, conditions=None, action=None):
        r"""CreateHttpAccessControlRuleRequestBody

        The model defined in huaweicloud sdk

        :param name: 规则名称
        :type name: str
        :param description: 规则描述，最长512字符
        :type description: str
        :param start: 精准防护规则生效的起始时间戳（秒）。当time&#x3D;true，才需要填写该参数。
        :type start: int
        :param terminal: 精准防护规则生效的终止时间戳（秒）。当time&#x3D;true，才需要填写该参数。
        :type terminal: int
        :param time_mode: 生效模式
        :type time_mode: str
        :param period_type: time_mode为period时必传，每日生效时间类型，目前只有day
        :type period_type: str
        :param time_range: time_mode为period时必传，每日生效时间区间
        :type time_range: list[:class:`huaweicloudsdkedgesec.v2.TimeRangeItem`]
        :param time_zone: time_mode为period时必传，时区，例如：UTC+8
        :type time_zone: str
        :param priority: 执行该规则的优先级，值越小，优先级越高，值相同时，规则创建时间早，优先级越高。取值范围：1到100。
        :type priority: int
        :param conditions: 命中条件
        :type conditions: list[:class:`huaweicloudsdkedgesec.v2.HttpAccessControlRuleCondition`]
        :param action: 
        :type action: :class:`huaweicloudsdkedgesec.v2.HttpRuleAction`
        """
        
        

        self._name = None
        self._description = None
        self._start = None
        self._terminal = None
        self._time_mode = None
        self._period_type = None
        self._time_range = None
        self._time_zone = None
        self._priority = None
        self._conditions = None
        self._action = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if start is not None:
            self.start = start
        if terminal is not None:
            self.terminal = terminal
        self.time_mode = time_mode
        if period_type is not None:
            self.period_type = period_type
        if time_range is not None:
            self.time_range = time_range
        if time_zone is not None:
            self.time_zone = time_zone
        self.priority = priority
        self.conditions = conditions
        self.action = action

    @property
    def name(self):
        r"""Gets the name of this CreateHttpAccessControlRuleRequestBody.

        规则名称

        :return: The name of this CreateHttpAccessControlRuleRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateHttpAccessControlRuleRequestBody.

        规则名称

        :param name: The name of this CreateHttpAccessControlRuleRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateHttpAccessControlRuleRequestBody.

        规则描述，最长512字符

        :return: The description of this CreateHttpAccessControlRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateHttpAccessControlRuleRequestBody.

        规则描述，最长512字符

        :param description: The description of this CreateHttpAccessControlRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def start(self):
        r"""Gets the start of this CreateHttpAccessControlRuleRequestBody.

        精准防护规则生效的起始时间戳（秒）。当time=true，才需要填写该参数。

        :return: The start of this CreateHttpAccessControlRuleRequestBody.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this CreateHttpAccessControlRuleRequestBody.

        精准防护规则生效的起始时间戳（秒）。当time=true，才需要填写该参数。

        :param start: The start of this CreateHttpAccessControlRuleRequestBody.
        :type start: int
        """
        self._start = start

    @property
    def terminal(self):
        r"""Gets the terminal of this CreateHttpAccessControlRuleRequestBody.

        精准防护规则生效的终止时间戳（秒）。当time=true，才需要填写该参数。

        :return: The terminal of this CreateHttpAccessControlRuleRequestBody.
        :rtype: int
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        r"""Sets the terminal of this CreateHttpAccessControlRuleRequestBody.

        精准防护规则生效的终止时间戳（秒）。当time=true，才需要填写该参数。

        :param terminal: The terminal of this CreateHttpAccessControlRuleRequestBody.
        :type terminal: int
        """
        self._terminal = terminal

    @property
    def time_mode(self):
        r"""Gets the time_mode of this CreateHttpAccessControlRuleRequestBody.

        生效模式

        :return: The time_mode of this CreateHttpAccessControlRuleRequestBody.
        :rtype: str
        """
        return self._time_mode

    @time_mode.setter
    def time_mode(self, time_mode):
        r"""Sets the time_mode of this CreateHttpAccessControlRuleRequestBody.

        生效模式

        :param time_mode: The time_mode of this CreateHttpAccessControlRuleRequestBody.
        :type time_mode: str
        """
        self._time_mode = time_mode

    @property
    def period_type(self):
        r"""Gets the period_type of this CreateHttpAccessControlRuleRequestBody.

        time_mode为period时必传，每日生效时间类型，目前只有day

        :return: The period_type of this CreateHttpAccessControlRuleRequestBody.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this CreateHttpAccessControlRuleRequestBody.

        time_mode为period时必传，每日生效时间类型，目前只有day

        :param period_type: The period_type of this CreateHttpAccessControlRuleRequestBody.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def time_range(self):
        r"""Gets the time_range of this CreateHttpAccessControlRuleRequestBody.

        time_mode为period时必传，每日生效时间区间

        :return: The time_range of this CreateHttpAccessControlRuleRequestBody.
        :rtype: list[:class:`huaweicloudsdkedgesec.v2.TimeRangeItem`]
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        r"""Sets the time_range of this CreateHttpAccessControlRuleRequestBody.

        time_mode为period时必传，每日生效时间区间

        :param time_range: The time_range of this CreateHttpAccessControlRuleRequestBody.
        :type time_range: list[:class:`huaweicloudsdkedgesec.v2.TimeRangeItem`]
        """
        self._time_range = time_range

    @property
    def time_zone(self):
        r"""Gets the time_zone of this CreateHttpAccessControlRuleRequestBody.

        time_mode为period时必传，时区，例如：UTC+8

        :return: The time_zone of this CreateHttpAccessControlRuleRequestBody.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this CreateHttpAccessControlRuleRequestBody.

        time_mode为period时必传，时区，例如：UTC+8

        :param time_zone: The time_zone of this CreateHttpAccessControlRuleRequestBody.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def priority(self):
        r"""Gets the priority of this CreateHttpAccessControlRuleRequestBody.

        执行该规则的优先级，值越小，优先级越高，值相同时，规则创建时间早，优先级越高。取值范围：1到100。

        :return: The priority of this CreateHttpAccessControlRuleRequestBody.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this CreateHttpAccessControlRuleRequestBody.

        执行该规则的优先级，值越小，优先级越高，值相同时，规则创建时间早，优先级越高。取值范围：1到100。

        :param priority: The priority of this CreateHttpAccessControlRuleRequestBody.
        :type priority: int
        """
        self._priority = priority

    @property
    def conditions(self):
        r"""Gets the conditions of this CreateHttpAccessControlRuleRequestBody.

        命中条件

        :return: The conditions of this CreateHttpAccessControlRuleRequestBody.
        :rtype: list[:class:`huaweicloudsdkedgesec.v2.HttpAccessControlRuleCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this CreateHttpAccessControlRuleRequestBody.

        命中条件

        :param conditions: The conditions of this CreateHttpAccessControlRuleRequestBody.
        :type conditions: list[:class:`huaweicloudsdkedgesec.v2.HttpAccessControlRuleCondition`]
        """
        self._conditions = conditions

    @property
    def action(self):
        r"""Gets the action of this CreateHttpAccessControlRuleRequestBody.

        :return: The action of this CreateHttpAccessControlRuleRequestBody.
        :rtype: :class:`huaweicloudsdkedgesec.v2.HttpRuleAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this CreateHttpAccessControlRuleRequestBody.

        :param action: The action of this CreateHttpAccessControlRuleRequestBody.
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
        if not isinstance(other, CreateHttpAccessControlRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
