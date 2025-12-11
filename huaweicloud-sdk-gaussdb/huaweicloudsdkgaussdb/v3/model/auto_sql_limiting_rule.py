# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoSqlLimitingRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'condition': 'str',
        'cpu_usage': 'int',
        'active_sessions': 'int',
        'clear_time': 'int',
        'duration': 'int',
        'max_concurrency': 'int',
        'retain_sql_rule': 'bool'
    }

    attribute_map = {
        'node_id': 'node_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'condition': 'condition',
        'cpu_usage': 'cpu_usage',
        'active_sessions': 'active_sessions',
        'clear_time': 'clear_time',
        'duration': 'duration',
        'max_concurrency': 'max_concurrency',
        'retain_sql_rule': 'retain_sql_rule'
    }

    def __init__(self, node_id=None, start_time=None, end_time=None, condition=None, cpu_usage=None, active_sessions=None, clear_time=None, duration=None, max_concurrency=None, retain_sql_rule=None):
        r"""AutoSqlLimitingRule

        The model defined in huaweicloud sdk

        :param node_id: **参数解释**：  节点ID。  获取方法请参见[查询实例详情](https://support.huaweicloud.com/api-taurusdb/ShowGaussMySqlInstanceInfoUnifyStatus.html)。  **约束限制**：  节点角色必须为主节点。  **取值范围**：  只能由英文字母、数字组成，前面为UUID，后缀为no07，长度为36个字符。  **默认取值**：  不涉及。
        :type node_id: str
        :param start_time: **参数解释**：  自治限流规则每天生效开始时间。  **约束限制**：  格式为 \&quot;hh:mm\&quot;。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type start_time: str
        :param end_time: **参数解释**：  自治限流规则每天生效结束时间。  **约束限制**：  格式为 \&quot;hh:mm\&quot;。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type end_time: str
        :param condition: **参数解释**：  限流策略CPU利用率和活跃会话数的关联关系。  **约束限制**：  不涉及。  **取值范围**：    - and：且。   - or：或。  **默认取值**：  不涉及。
        :type condition: str
        :param cpu_usage: **参数解释**：  限流策略CPU利用率。  **约束限制**：  不涉及。  **取值范围**：  [70~100]。  **默认取值**：  不涉及。
        :type cpu_usage: int
        :param active_sessions: **参数解释**：  限流策略活跃会话数。  **约束限制**：  不涉及。  **取值范围**：  [1~5000]。  **默认取值**：  不涉及。
        :type active_sessions: int
        :param clear_time: **参数解释**：  每次最大限流时长（分钟）。  **约束限制**：  不涉及。  **取值范围**：  [1~1440]。  **默认取值**：  不涉及。
        :type clear_time: int
        :param duration: **参数解释**：  限流策略满足限流条件的事件持续时间（分钟）。  **约束限制**：  不涉及。  **取值范围**：  [2~60]。  **默认取值**：  不涉及。
        :type duration: int
        :param max_concurrency: **参数解释**：  最大并发数。  **约束限制**：  不涉及。  **取值范围**：  [0~1000000000]。  **默认取值**：  不涉及。
        :type max_concurrency: int
        :param retain_sql_rule: **参数解释**：  是否保留已有的SQL限流规则。  **约束限制**：  不涉及。  **取值范围**：    - true：保留已有的SQL限流规则。   - false：清理已有的SQL限流规则。  **默认取值**：  不涉及。
        :type retain_sql_rule: bool
        """
        
        

        self._node_id = None
        self._start_time = None
        self._end_time = None
        self._condition = None
        self._cpu_usage = None
        self._active_sessions = None
        self._clear_time = None
        self._duration = None
        self._max_concurrency = None
        self._retain_sql_rule = None
        self.discriminator = None

        self.node_id = node_id
        self.start_time = start_time
        self.end_time = end_time
        self.condition = condition
        self.cpu_usage = cpu_usage
        self.active_sessions = active_sessions
        self.clear_time = clear_time
        self.duration = duration
        self.max_concurrency = max_concurrency
        self.retain_sql_rule = retain_sql_rule

    @property
    def node_id(self):
        r"""Gets the node_id of this AutoSqlLimitingRule.

        **参数解释**：  节点ID。  获取方法请参见[查询实例详情](https://support.huaweicloud.com/api-taurusdb/ShowGaussMySqlInstanceInfoUnifyStatus.html)。  **约束限制**：  节点角色必须为主节点。  **取值范围**：  只能由英文字母、数字组成，前面为UUID，后缀为no07，长度为36个字符。  **默认取值**：  不涉及。

        :return: The node_id of this AutoSqlLimitingRule.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this AutoSqlLimitingRule.

        **参数解释**：  节点ID。  获取方法请参见[查询实例详情](https://support.huaweicloud.com/api-taurusdb/ShowGaussMySqlInstanceInfoUnifyStatus.html)。  **约束限制**：  节点角色必须为主节点。  **取值范围**：  只能由英文字母、数字组成，前面为UUID，后缀为no07，长度为36个字符。  **默认取值**：  不涉及。

        :param node_id: The node_id of this AutoSqlLimitingRule.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def start_time(self):
        r"""Gets the start_time of this AutoSqlLimitingRule.

        **参数解释**：  自治限流规则每天生效开始时间。  **约束限制**：  格式为 \"hh:mm\"。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The start_time of this AutoSqlLimitingRule.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this AutoSqlLimitingRule.

        **参数解释**：  自治限流规则每天生效开始时间。  **约束限制**：  格式为 \"hh:mm\"。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param start_time: The start_time of this AutoSqlLimitingRule.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this AutoSqlLimitingRule.

        **参数解释**：  自治限流规则每天生效结束时间。  **约束限制**：  格式为 \"hh:mm\"。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The end_time of this AutoSqlLimitingRule.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this AutoSqlLimitingRule.

        **参数解释**：  自治限流规则每天生效结束时间。  **约束限制**：  格式为 \"hh:mm\"。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param end_time: The end_time of this AutoSqlLimitingRule.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def condition(self):
        r"""Gets the condition of this AutoSqlLimitingRule.

        **参数解释**：  限流策略CPU利用率和活跃会话数的关联关系。  **约束限制**：  不涉及。  **取值范围**：    - and：且。   - or：或。  **默认取值**：  不涉及。

        :return: The condition of this AutoSqlLimitingRule.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this AutoSqlLimitingRule.

        **参数解释**：  限流策略CPU利用率和活跃会话数的关联关系。  **约束限制**：  不涉及。  **取值范围**：    - and：且。   - or：或。  **默认取值**：  不涉及。

        :param condition: The condition of this AutoSqlLimitingRule.
        :type condition: str
        """
        self._condition = condition

    @property
    def cpu_usage(self):
        r"""Gets the cpu_usage of this AutoSqlLimitingRule.

        **参数解释**：  限流策略CPU利用率。  **约束限制**：  不涉及。  **取值范围**：  [70~100]。  **默认取值**：  不涉及。

        :return: The cpu_usage of this AutoSqlLimitingRule.
        :rtype: int
        """
        return self._cpu_usage

    @cpu_usage.setter
    def cpu_usage(self, cpu_usage):
        r"""Sets the cpu_usage of this AutoSqlLimitingRule.

        **参数解释**：  限流策略CPU利用率。  **约束限制**：  不涉及。  **取值范围**：  [70~100]。  **默认取值**：  不涉及。

        :param cpu_usage: The cpu_usage of this AutoSqlLimitingRule.
        :type cpu_usage: int
        """
        self._cpu_usage = cpu_usage

    @property
    def active_sessions(self):
        r"""Gets the active_sessions of this AutoSqlLimitingRule.

        **参数解释**：  限流策略活跃会话数。  **约束限制**：  不涉及。  **取值范围**：  [1~5000]。  **默认取值**：  不涉及。

        :return: The active_sessions of this AutoSqlLimitingRule.
        :rtype: int
        """
        return self._active_sessions

    @active_sessions.setter
    def active_sessions(self, active_sessions):
        r"""Sets the active_sessions of this AutoSqlLimitingRule.

        **参数解释**：  限流策略活跃会话数。  **约束限制**：  不涉及。  **取值范围**：  [1~5000]。  **默认取值**：  不涉及。

        :param active_sessions: The active_sessions of this AutoSqlLimitingRule.
        :type active_sessions: int
        """
        self._active_sessions = active_sessions

    @property
    def clear_time(self):
        r"""Gets the clear_time of this AutoSqlLimitingRule.

        **参数解释**：  每次最大限流时长（分钟）。  **约束限制**：  不涉及。  **取值范围**：  [1~1440]。  **默认取值**：  不涉及。

        :return: The clear_time of this AutoSqlLimitingRule.
        :rtype: int
        """
        return self._clear_time

    @clear_time.setter
    def clear_time(self, clear_time):
        r"""Sets the clear_time of this AutoSqlLimitingRule.

        **参数解释**：  每次最大限流时长（分钟）。  **约束限制**：  不涉及。  **取值范围**：  [1~1440]。  **默认取值**：  不涉及。

        :param clear_time: The clear_time of this AutoSqlLimitingRule.
        :type clear_time: int
        """
        self._clear_time = clear_time

    @property
    def duration(self):
        r"""Gets the duration of this AutoSqlLimitingRule.

        **参数解释**：  限流策略满足限流条件的事件持续时间（分钟）。  **约束限制**：  不涉及。  **取值范围**：  [2~60]。  **默认取值**：  不涉及。

        :return: The duration of this AutoSqlLimitingRule.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this AutoSqlLimitingRule.

        **参数解释**：  限流策略满足限流条件的事件持续时间（分钟）。  **约束限制**：  不涉及。  **取值范围**：  [2~60]。  **默认取值**：  不涉及。

        :param duration: The duration of this AutoSqlLimitingRule.
        :type duration: int
        """
        self._duration = duration

    @property
    def max_concurrency(self):
        r"""Gets the max_concurrency of this AutoSqlLimitingRule.

        **参数解释**：  最大并发数。  **约束限制**：  不涉及。  **取值范围**：  [0~1000000000]。  **默认取值**：  不涉及。

        :return: The max_concurrency of this AutoSqlLimitingRule.
        :rtype: int
        """
        return self._max_concurrency

    @max_concurrency.setter
    def max_concurrency(self, max_concurrency):
        r"""Sets the max_concurrency of this AutoSqlLimitingRule.

        **参数解释**：  最大并发数。  **约束限制**：  不涉及。  **取值范围**：  [0~1000000000]。  **默认取值**：  不涉及。

        :param max_concurrency: The max_concurrency of this AutoSqlLimitingRule.
        :type max_concurrency: int
        """
        self._max_concurrency = max_concurrency

    @property
    def retain_sql_rule(self):
        r"""Gets the retain_sql_rule of this AutoSqlLimitingRule.

        **参数解释**：  是否保留已有的SQL限流规则。  **约束限制**：  不涉及。  **取值范围**：    - true：保留已有的SQL限流规则。   - false：清理已有的SQL限流规则。  **默认取值**：  不涉及。

        :return: The retain_sql_rule of this AutoSqlLimitingRule.
        :rtype: bool
        """
        return self._retain_sql_rule

    @retain_sql_rule.setter
    def retain_sql_rule(self, retain_sql_rule):
        r"""Sets the retain_sql_rule of this AutoSqlLimitingRule.

        **参数解释**：  是否保留已有的SQL限流规则。  **约束限制**：  不涉及。  **取值范围**：    - true：保留已有的SQL限流规则。   - false：清理已有的SQL限流规则。  **默认取值**：  不涉及。

        :param retain_sql_rule: The retain_sql_rule of this AutoSqlLimitingRule.
        :type retain_sql_rule: bool
        """
        self._retain_sql_rule = retain_sql_rule

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
        if not isinstance(other, AutoSqlLimitingRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
