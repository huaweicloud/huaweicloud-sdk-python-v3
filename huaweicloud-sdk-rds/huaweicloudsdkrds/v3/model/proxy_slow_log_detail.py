# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProxySlowLogDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_ip': 'str',
        'desc_ip': 'str',
        'user': 'str',
        'reaction_time': 'str',
        'trace_id': 'str',
        'sql': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'line_num': 'str',
        'database': 'str',
        'log_time': 'str'
    }

    attribute_map = {
        'source_ip': 'source_ip',
        'desc_ip': 'desc_ip',
        'user': 'user',
        'reaction_time': 'reaction_time',
        'trace_id': 'trace_id',
        'sql': 'sql',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'line_num': 'line_num',
        'database': 'database',
        'log_time': 'log_time'
    }

    def __init__(self, source_ip=None, desc_ip=None, user=None, reaction_time=None, trace_id=None, sql=None, start_time=None, end_time=None, line_num=None, database=None, log_time=None):
        r"""ProxySlowLogDetail

        The model defined in huaweicloud sdk

        :param source_ip: **参数解释**：  客户端IP。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type source_ip: str
        :param desc_ip: **参数解释**：  后端数据库IP。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type desc_ip: str
        :param user: **参数解释**：  数据库用户。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type user: str
        :param reaction_time: **参数解释**：  响应时长，单位ms。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type reaction_time: str
        :param trace_id: **参数解释**：  SQL执行跟踪ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type trace_id: str
        :param sql: **参数解释**：  执行语句。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type sql: str
        :param start_time: **参数解释**：  SQL语句执行开始时间，毫秒级时间戳。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type start_time: str
        :param end_time: **参数解释**：  SQL语句执行结束时间，毫秒级时间戳。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type end_time: str
        :param line_num: **参数解释**：  每次查询起始记录ID，用于获取后续数据时在请求中传入。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type line_num: str
        :param database: **参数解释**：  数据库名称。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type database: str
        :param log_time: **参数解释**：  日志上报时间，毫秒级时间戳。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type log_time: str
        """
        
        

        self._source_ip = None
        self._desc_ip = None
        self._user = None
        self._reaction_time = None
        self._trace_id = None
        self._sql = None
        self._start_time = None
        self._end_time = None
        self._line_num = None
        self._database = None
        self._log_time = None
        self.discriminator = None

        if source_ip is not None:
            self.source_ip = source_ip
        if desc_ip is not None:
            self.desc_ip = desc_ip
        if user is not None:
            self.user = user
        if reaction_time is not None:
            self.reaction_time = reaction_time
        if trace_id is not None:
            self.trace_id = trace_id
        if sql is not None:
            self.sql = sql
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if line_num is not None:
            self.line_num = line_num
        if database is not None:
            self.database = database
        if log_time is not None:
            self.log_time = log_time

    @property
    def source_ip(self):
        r"""Gets the source_ip of this ProxySlowLogDetail.

        **参数解释**：  客户端IP。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The source_ip of this ProxySlowLogDetail.
        :rtype: str
        """
        return self._source_ip

    @source_ip.setter
    def source_ip(self, source_ip):
        r"""Sets the source_ip of this ProxySlowLogDetail.

        **参数解释**：  客户端IP。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param source_ip: The source_ip of this ProxySlowLogDetail.
        :type source_ip: str
        """
        self._source_ip = source_ip

    @property
    def desc_ip(self):
        r"""Gets the desc_ip of this ProxySlowLogDetail.

        **参数解释**：  后端数据库IP。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The desc_ip of this ProxySlowLogDetail.
        :rtype: str
        """
        return self._desc_ip

    @desc_ip.setter
    def desc_ip(self, desc_ip):
        r"""Sets the desc_ip of this ProxySlowLogDetail.

        **参数解释**：  后端数据库IP。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param desc_ip: The desc_ip of this ProxySlowLogDetail.
        :type desc_ip: str
        """
        self._desc_ip = desc_ip

    @property
    def user(self):
        r"""Gets the user of this ProxySlowLogDetail.

        **参数解释**：  数据库用户。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The user of this ProxySlowLogDetail.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this ProxySlowLogDetail.

        **参数解释**：  数据库用户。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param user: The user of this ProxySlowLogDetail.
        :type user: str
        """
        self._user = user

    @property
    def reaction_time(self):
        r"""Gets the reaction_time of this ProxySlowLogDetail.

        **参数解释**：  响应时长，单位ms。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The reaction_time of this ProxySlowLogDetail.
        :rtype: str
        """
        return self._reaction_time

    @reaction_time.setter
    def reaction_time(self, reaction_time):
        r"""Sets the reaction_time of this ProxySlowLogDetail.

        **参数解释**：  响应时长，单位ms。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param reaction_time: The reaction_time of this ProxySlowLogDetail.
        :type reaction_time: str
        """
        self._reaction_time = reaction_time

    @property
    def trace_id(self):
        r"""Gets the trace_id of this ProxySlowLogDetail.

        **参数解释**：  SQL执行跟踪ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The trace_id of this ProxySlowLogDetail.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        r"""Sets the trace_id of this ProxySlowLogDetail.

        **参数解释**：  SQL执行跟踪ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param trace_id: The trace_id of this ProxySlowLogDetail.
        :type trace_id: str
        """
        self._trace_id = trace_id

    @property
    def sql(self):
        r"""Gets the sql of this ProxySlowLogDetail.

        **参数解释**：  执行语句。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The sql of this ProxySlowLogDetail.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this ProxySlowLogDetail.

        **参数解释**：  执行语句。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param sql: The sql of this ProxySlowLogDetail.
        :type sql: str
        """
        self._sql = sql

    @property
    def start_time(self):
        r"""Gets the start_time of this ProxySlowLogDetail.

        **参数解释**：  SQL语句执行开始时间，毫秒级时间戳。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The start_time of this ProxySlowLogDetail.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ProxySlowLogDetail.

        **参数解释**：  SQL语句执行开始时间，毫秒级时间戳。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param start_time: The start_time of this ProxySlowLogDetail.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ProxySlowLogDetail.

        **参数解释**：  SQL语句执行结束时间，毫秒级时间戳。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The end_time of this ProxySlowLogDetail.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ProxySlowLogDetail.

        **参数解释**：  SQL语句执行结束时间，毫秒级时间戳。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param end_time: The end_time of this ProxySlowLogDetail.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def line_num(self):
        r"""Gets the line_num of this ProxySlowLogDetail.

        **参数解释**：  每次查询起始记录ID，用于获取后续数据时在请求中传入。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The line_num of this ProxySlowLogDetail.
        :rtype: str
        """
        return self._line_num

    @line_num.setter
    def line_num(self, line_num):
        r"""Sets the line_num of this ProxySlowLogDetail.

        **参数解释**：  每次查询起始记录ID，用于获取后续数据时在请求中传入。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param line_num: The line_num of this ProxySlowLogDetail.
        :type line_num: str
        """
        self._line_num = line_num

    @property
    def database(self):
        r"""Gets the database of this ProxySlowLogDetail.

        **参数解释**：  数据库名称。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The database of this ProxySlowLogDetail.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this ProxySlowLogDetail.

        **参数解释**：  数据库名称。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param database: The database of this ProxySlowLogDetail.
        :type database: str
        """
        self._database = database

    @property
    def log_time(self):
        r"""Gets the log_time of this ProxySlowLogDetail.

        **参数解释**：  日志上报时间，毫秒级时间戳。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The log_time of this ProxySlowLogDetail.
        :rtype: str
        """
        return self._log_time

    @log_time.setter
    def log_time(self, log_time):
        r"""Sets the log_time of this ProxySlowLogDetail.

        **参数解释**：  日志上报时间，毫秒级时间戳。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param log_time: The log_time of this ProxySlowLogDetail.
        :type log_time: str
        """
        self._log_time = log_time

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
        if not isinstance(other, ProxySlowLogDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
