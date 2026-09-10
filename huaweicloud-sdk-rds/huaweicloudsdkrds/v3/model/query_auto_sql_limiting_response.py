# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryAutoSqlLimitingResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cpu_usage': 'int',
        'active_sessions': 'int',
        'condition': 'str',
        'duration': 'int',
        'start_time': 'str',
        'end_time': 'str',
        'session_allow': 'int',
        'user': 'list[str]',
        'db': 'list[str]',
        'clear_time': 'int',
        'enable': 'bool',
        'is_keyword': 'bool',
        'max_concurrency': 'int',
        'retain_sql_rule': 'bool',
        'kill_session_switch': 'bool'
    }

    attribute_map = {
        'cpu_usage': 'cpu_usage',
        'active_sessions': 'active_sessions',
        'condition': 'condition',
        'duration': 'duration',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'session_allow': 'session_allow',
        'user': 'user',
        'db': 'db',
        'clear_time': 'clear_time',
        'enable': 'enable',
        'is_keyword': 'is_keyword',
        'max_concurrency': 'max_concurrency',
        'retain_sql_rule': 'retain_sql_rule',
        'kill_session_switch': 'kill_session_switch'
    }

    def __init__(self, cpu_usage=None, active_sessions=None, condition=None, duration=None, start_time=None, end_time=None, session_allow=None, user=None, db=None, clear_time=None, enable=None, is_keyword=None, max_concurrency=None, retain_sql_rule=None, kill_session_switch=None):
        r"""QueryAutoSqlLimitingResponse

        The model defined in huaweicloud sdk

        :param cpu_usage: 限流策略CPU利用率。
        :type cpu_usage: int
        :param active_sessions: 限流策略活跃会话数。
        :type active_sessions: int
        :param condition: 限流策略CPU利用率和活跃会话数的关联关系。取值范围：and、or。
        :type condition: str
        :param duration: 限流策略满足限流条件的事件持续时间（分钟）。
        :type duration: int
        :param start_time: 自治限流规则每天生效开始时间。
        :type start_time: str
        :param end_time: 自治限流规则每天生效结束时间。
        :type end_time: str
        :param session_allow: 允许的会话数。
        :type session_allow: int
        :param user: 限流规则适用的用户列表。
        :type user: list[str]
        :param db: 限流规则适用的数据库列表。
        :type db: list[str]
        :param clear_time: 每次最大限流时长（分钟）。
        :type clear_time: int
        :param enable: 是否启用自治限流规则。
        :type enable: bool
        :param is_keyword: 是否为关键字限流。
        :type is_keyword: bool
        :param max_concurrency: 最大并发数。
        :type max_concurrency: int
        :param retain_sql_rule: 是否保留SQL限流规则。
        :type retain_sql_rule: bool
        :param kill_session_switch: 是否开启kill会话开关。
        :type kill_session_switch: bool
        """
        
        super().__init__()

        self._cpu_usage = None
        self._active_sessions = None
        self._condition = None
        self._duration = None
        self._start_time = None
        self._end_time = None
        self._session_allow = None
        self._user = None
        self._db = None
        self._clear_time = None
        self._enable = None
        self._is_keyword = None
        self._max_concurrency = None
        self._retain_sql_rule = None
        self._kill_session_switch = None
        self.discriminator = None

        if cpu_usage is not None:
            self.cpu_usage = cpu_usage
        if active_sessions is not None:
            self.active_sessions = active_sessions
        if condition is not None:
            self.condition = condition
        if duration is not None:
            self.duration = duration
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if session_allow is not None:
            self.session_allow = session_allow
        if user is not None:
            self.user = user
        if db is not None:
            self.db = db
        if clear_time is not None:
            self.clear_time = clear_time
        if enable is not None:
            self.enable = enable
        if is_keyword is not None:
            self.is_keyword = is_keyword
        if max_concurrency is not None:
            self.max_concurrency = max_concurrency
        if retain_sql_rule is not None:
            self.retain_sql_rule = retain_sql_rule
        if kill_session_switch is not None:
            self.kill_session_switch = kill_session_switch

    @property
    def cpu_usage(self):
        r"""Gets the cpu_usage of this QueryAutoSqlLimitingResponse.

        限流策略CPU利用率。

        :return: The cpu_usage of this QueryAutoSqlLimitingResponse.
        :rtype: int
        """
        return self._cpu_usage

    @cpu_usage.setter
    def cpu_usage(self, cpu_usage):
        r"""Sets the cpu_usage of this QueryAutoSqlLimitingResponse.

        限流策略CPU利用率。

        :param cpu_usage: The cpu_usage of this QueryAutoSqlLimitingResponse.
        :type cpu_usage: int
        """
        self._cpu_usage = cpu_usage

    @property
    def active_sessions(self):
        r"""Gets the active_sessions of this QueryAutoSqlLimitingResponse.

        限流策略活跃会话数。

        :return: The active_sessions of this QueryAutoSqlLimitingResponse.
        :rtype: int
        """
        return self._active_sessions

    @active_sessions.setter
    def active_sessions(self, active_sessions):
        r"""Sets the active_sessions of this QueryAutoSqlLimitingResponse.

        限流策略活跃会话数。

        :param active_sessions: The active_sessions of this QueryAutoSqlLimitingResponse.
        :type active_sessions: int
        """
        self._active_sessions = active_sessions

    @property
    def condition(self):
        r"""Gets the condition of this QueryAutoSqlLimitingResponse.

        限流策略CPU利用率和活跃会话数的关联关系。取值范围：and、or。

        :return: The condition of this QueryAutoSqlLimitingResponse.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this QueryAutoSqlLimitingResponse.

        限流策略CPU利用率和活跃会话数的关联关系。取值范围：and、or。

        :param condition: The condition of this QueryAutoSqlLimitingResponse.
        :type condition: str
        """
        self._condition = condition

    @property
    def duration(self):
        r"""Gets the duration of this QueryAutoSqlLimitingResponse.

        限流策略满足限流条件的事件持续时间（分钟）。

        :return: The duration of this QueryAutoSqlLimitingResponse.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this QueryAutoSqlLimitingResponse.

        限流策略满足限流条件的事件持续时间（分钟）。

        :param duration: The duration of this QueryAutoSqlLimitingResponse.
        :type duration: int
        """
        self._duration = duration

    @property
    def start_time(self):
        r"""Gets the start_time of this QueryAutoSqlLimitingResponse.

        自治限流规则每天生效开始时间。

        :return: The start_time of this QueryAutoSqlLimitingResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this QueryAutoSqlLimitingResponse.

        自治限流规则每天生效开始时间。

        :param start_time: The start_time of this QueryAutoSqlLimitingResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this QueryAutoSqlLimitingResponse.

        自治限流规则每天生效结束时间。

        :return: The end_time of this QueryAutoSqlLimitingResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this QueryAutoSqlLimitingResponse.

        自治限流规则每天生效结束时间。

        :param end_time: The end_time of this QueryAutoSqlLimitingResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def session_allow(self):
        r"""Gets the session_allow of this QueryAutoSqlLimitingResponse.

        允许的会话数。

        :return: The session_allow of this QueryAutoSqlLimitingResponse.
        :rtype: int
        """
        return self._session_allow

    @session_allow.setter
    def session_allow(self, session_allow):
        r"""Sets the session_allow of this QueryAutoSqlLimitingResponse.

        允许的会话数。

        :param session_allow: The session_allow of this QueryAutoSqlLimitingResponse.
        :type session_allow: int
        """
        self._session_allow = session_allow

    @property
    def user(self):
        r"""Gets the user of this QueryAutoSqlLimitingResponse.

        限流规则适用的用户列表。

        :return: The user of this QueryAutoSqlLimitingResponse.
        :rtype: list[str]
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this QueryAutoSqlLimitingResponse.

        限流规则适用的用户列表。

        :param user: The user of this QueryAutoSqlLimitingResponse.
        :type user: list[str]
        """
        self._user = user

    @property
    def db(self):
        r"""Gets the db of this QueryAutoSqlLimitingResponse.

        限流规则适用的数据库列表。

        :return: The db of this QueryAutoSqlLimitingResponse.
        :rtype: list[str]
        """
        return self._db

    @db.setter
    def db(self, db):
        r"""Sets the db of this QueryAutoSqlLimitingResponse.

        限流规则适用的数据库列表。

        :param db: The db of this QueryAutoSqlLimitingResponse.
        :type db: list[str]
        """
        self._db = db

    @property
    def clear_time(self):
        r"""Gets the clear_time of this QueryAutoSqlLimitingResponse.

        每次最大限流时长（分钟）。

        :return: The clear_time of this QueryAutoSqlLimitingResponse.
        :rtype: int
        """
        return self._clear_time

    @clear_time.setter
    def clear_time(self, clear_time):
        r"""Sets the clear_time of this QueryAutoSqlLimitingResponse.

        每次最大限流时长（分钟）。

        :param clear_time: The clear_time of this QueryAutoSqlLimitingResponse.
        :type clear_time: int
        """
        self._clear_time = clear_time

    @property
    def enable(self):
        r"""Gets the enable of this QueryAutoSqlLimitingResponse.

        是否启用自治限流规则。

        :return: The enable of this QueryAutoSqlLimitingResponse.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this QueryAutoSqlLimitingResponse.

        是否启用自治限流规则。

        :param enable: The enable of this QueryAutoSqlLimitingResponse.
        :type enable: bool
        """
        self._enable = enable

    @property
    def is_keyword(self):
        r"""Gets the is_keyword of this QueryAutoSqlLimitingResponse.

        是否为关键字限流。

        :return: The is_keyword of this QueryAutoSqlLimitingResponse.
        :rtype: bool
        """
        return self._is_keyword

    @is_keyword.setter
    def is_keyword(self, is_keyword):
        r"""Sets the is_keyword of this QueryAutoSqlLimitingResponse.

        是否为关键字限流。

        :param is_keyword: The is_keyword of this QueryAutoSqlLimitingResponse.
        :type is_keyword: bool
        """
        self._is_keyword = is_keyword

    @property
    def max_concurrency(self):
        r"""Gets the max_concurrency of this QueryAutoSqlLimitingResponse.

        最大并发数。

        :return: The max_concurrency of this QueryAutoSqlLimitingResponse.
        :rtype: int
        """
        return self._max_concurrency

    @max_concurrency.setter
    def max_concurrency(self, max_concurrency):
        r"""Sets the max_concurrency of this QueryAutoSqlLimitingResponse.

        最大并发数。

        :param max_concurrency: The max_concurrency of this QueryAutoSqlLimitingResponse.
        :type max_concurrency: int
        """
        self._max_concurrency = max_concurrency

    @property
    def retain_sql_rule(self):
        r"""Gets the retain_sql_rule of this QueryAutoSqlLimitingResponse.

        是否保留SQL限流规则。

        :return: The retain_sql_rule of this QueryAutoSqlLimitingResponse.
        :rtype: bool
        """
        return self._retain_sql_rule

    @retain_sql_rule.setter
    def retain_sql_rule(self, retain_sql_rule):
        r"""Sets the retain_sql_rule of this QueryAutoSqlLimitingResponse.

        是否保留SQL限流规则。

        :param retain_sql_rule: The retain_sql_rule of this QueryAutoSqlLimitingResponse.
        :type retain_sql_rule: bool
        """
        self._retain_sql_rule = retain_sql_rule

    @property
    def kill_session_switch(self):
        r"""Gets the kill_session_switch of this QueryAutoSqlLimitingResponse.

        是否开启kill会话开关。

        :return: The kill_session_switch of this QueryAutoSqlLimitingResponse.
        :rtype: bool
        """
        return self._kill_session_switch

    @kill_session_switch.setter
    def kill_session_switch(self, kill_session_switch):
        r"""Sets the kill_session_switch of this QueryAutoSqlLimitingResponse.

        是否开启kill会话开关。

        :param kill_session_switch: The kill_session_switch of this QueryAutoSqlLimitingResponse.
        :type kill_session_switch: bool
        """
        self._kill_session_switch = kill_session_switch

    def to_dict(self):
        import warnings
        warnings.warn("QueryAutoSqlLimitingResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, QueryAutoSqlLimitingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
