# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlowSQLInfoResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql': 'str',
        'sql_id': 'str',
        'user_name': 'str',
        'sql_text': 'str',
        'query_plan': 'str',
        'calls': 'int',
        'avg_exec_time': 'str',
        'avg_cpu_time': 'str',
        'avg_io_time': 'str',
        'avg_returned_rows': 'int',
        'avg_fetched_rows': 'int',
        'buffer_hit_ratio': 'str',
        'sql_hit_ratio': 'str',
        'node_id': 'str',
        'node_name': 'str'
    }

    attribute_map = {
        'sql': 'sql',
        'sql_id': 'sql_id',
        'user_name': 'user_name',
        'sql_text': 'sql_text',
        'query_plan': 'query_plan',
        'calls': 'calls',
        'avg_exec_time': 'avg_exec_time',
        'avg_cpu_time': 'avg_cpu_time',
        'avg_io_time': 'avg_io_time',
        'avg_returned_rows': 'avg_returned_rows',
        'avg_fetched_rows': 'avg_fetched_rows',
        'buffer_hit_ratio': 'buffer_hit_ratio',
        'sql_hit_ratio': 'sql_hit_ratio',
        'node_id': 'node_id',
        'node_name': 'node_name'
    }

    def __init__(self, sql=None, sql_id=None, user_name=None, sql_text=None, query_plan=None, calls=None, avg_exec_time=None, avg_cpu_time=None, avg_io_time=None, avg_returned_rows=None, avg_fetched_rows=None, buffer_hit_ratio=None, sql_hit_ratio=None, node_id=None, node_name=None):
        r"""SlowSQLInfoResult

        The model defined in huaweicloud sdk

        :param sql: **参数解释**: 变量替换后的完整SQL。当sql_text不返回变量值时，sql返回空字符串。 **取值范围**: 不涉及。
        :type sql: str
        :param sql_id: **参数解释**: SQL ID。 **取值范围**: 不涉及。
        :type sql_id: str
        :param user_name: **参数解释**: 用户名称。 **取值范围**: 不涉及。
        :type user_name: str
        :param sql_text: **参数解释**: SQL文本。 **取值范围**: 不涉及。
        :type sql_text: str
        :param query_plan: **参数解释**: SQL计划。 **取值范围**: 不涉及。
        :type query_plan: str
        :param calls: **参数解释**: 执行次数（次）。 **取值范围**: 不涉及。
        :type calls: int
        :param avg_exec_time: **参数解释**: 平均执行时间（us）。 **取值范围**: 不涉及。
        :type avg_exec_time: str
        :param avg_cpu_time: **参数解释**: 平均CPU耗时（us）。 **取值范围**: 不涉及。
        :type avg_cpu_time: str
        :param avg_io_time: **参数解释**: 平均IO耗时（us）。 **取值范围**: 不涉及。
        :type avg_io_time: str
        :param avg_returned_rows: **参数解释**: 平均返回行数（行）。 **取值范围**: 不涉及。
        :type avg_returned_rows: int
        :param avg_fetched_rows: **参数解释**: 平均扫描行数（行）。 **取值范围**: 不涉及。
        :type avg_fetched_rows: int
        :param buffer_hit_ratio: **参数解释**: buffer命中率。 **取值范围**: 不涉及。
        :type buffer_hit_ratio: str
        :param sql_hit_ratio: **参数解释**: SQL命中率。 **取值范围**: 不涉及。
        :type sql_hit_ratio: str
        :param node_id: **参数解释**: 节点ID。 **取值范围**: 不涉及。
        :type node_id: str
        :param node_name: **参数解释**: 节点名称。 **取值范围**: 不涉及。
        :type node_name: str
        """
        
        

        self._sql = None
        self._sql_id = None
        self._user_name = None
        self._sql_text = None
        self._query_plan = None
        self._calls = None
        self._avg_exec_time = None
        self._avg_cpu_time = None
        self._avg_io_time = None
        self._avg_returned_rows = None
        self._avg_fetched_rows = None
        self._buffer_hit_ratio = None
        self._sql_hit_ratio = None
        self._node_id = None
        self._node_name = None
        self.discriminator = None

        if sql is not None:
            self.sql = sql
        if sql_id is not None:
            self.sql_id = sql_id
        if user_name is not None:
            self.user_name = user_name
        if sql_text is not None:
            self.sql_text = sql_text
        if query_plan is not None:
            self.query_plan = query_plan
        if calls is not None:
            self.calls = calls
        if avg_exec_time is not None:
            self.avg_exec_time = avg_exec_time
        if avg_cpu_time is not None:
            self.avg_cpu_time = avg_cpu_time
        if avg_io_time is not None:
            self.avg_io_time = avg_io_time
        if avg_returned_rows is not None:
            self.avg_returned_rows = avg_returned_rows
        if avg_fetched_rows is not None:
            self.avg_fetched_rows = avg_fetched_rows
        if buffer_hit_ratio is not None:
            self.buffer_hit_ratio = buffer_hit_ratio
        if sql_hit_ratio is not None:
            self.sql_hit_ratio = sql_hit_ratio
        if node_id is not None:
            self.node_id = node_id
        if node_name is not None:
            self.node_name = node_name

    @property
    def sql(self):
        r"""Gets the sql of this SlowSQLInfoResult.

        **参数解释**: 变量替换后的完整SQL。当sql_text不返回变量值时，sql返回空字符串。 **取值范围**: 不涉及。

        :return: The sql of this SlowSQLInfoResult.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this SlowSQLInfoResult.

        **参数解释**: 变量替换后的完整SQL。当sql_text不返回变量值时，sql返回空字符串。 **取值范围**: 不涉及。

        :param sql: The sql of this SlowSQLInfoResult.
        :type sql: str
        """
        self._sql = sql

    @property
    def sql_id(self):
        r"""Gets the sql_id of this SlowSQLInfoResult.

        **参数解释**: SQL ID。 **取值范围**: 不涉及。

        :return: The sql_id of this SlowSQLInfoResult.
        :rtype: str
        """
        return self._sql_id

    @sql_id.setter
    def sql_id(self, sql_id):
        r"""Sets the sql_id of this SlowSQLInfoResult.

        **参数解释**: SQL ID。 **取值范围**: 不涉及。

        :param sql_id: The sql_id of this SlowSQLInfoResult.
        :type sql_id: str
        """
        self._sql_id = sql_id

    @property
    def user_name(self):
        r"""Gets the user_name of this SlowSQLInfoResult.

        **参数解释**: 用户名称。 **取值范围**: 不涉及。

        :return: The user_name of this SlowSQLInfoResult.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this SlowSQLInfoResult.

        **参数解释**: 用户名称。 **取值范围**: 不涉及。

        :param user_name: The user_name of this SlowSQLInfoResult.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def sql_text(self):
        r"""Gets the sql_text of this SlowSQLInfoResult.

        **参数解释**: SQL文本。 **取值范围**: 不涉及。

        :return: The sql_text of this SlowSQLInfoResult.
        :rtype: str
        """
        return self._sql_text

    @sql_text.setter
    def sql_text(self, sql_text):
        r"""Sets the sql_text of this SlowSQLInfoResult.

        **参数解释**: SQL文本。 **取值范围**: 不涉及。

        :param sql_text: The sql_text of this SlowSQLInfoResult.
        :type sql_text: str
        """
        self._sql_text = sql_text

    @property
    def query_plan(self):
        r"""Gets the query_plan of this SlowSQLInfoResult.

        **参数解释**: SQL计划。 **取值范围**: 不涉及。

        :return: The query_plan of this SlowSQLInfoResult.
        :rtype: str
        """
        return self._query_plan

    @query_plan.setter
    def query_plan(self, query_plan):
        r"""Sets the query_plan of this SlowSQLInfoResult.

        **参数解释**: SQL计划。 **取值范围**: 不涉及。

        :param query_plan: The query_plan of this SlowSQLInfoResult.
        :type query_plan: str
        """
        self._query_plan = query_plan

    @property
    def calls(self):
        r"""Gets the calls of this SlowSQLInfoResult.

        **参数解释**: 执行次数（次）。 **取值范围**: 不涉及。

        :return: The calls of this SlowSQLInfoResult.
        :rtype: int
        """
        return self._calls

    @calls.setter
    def calls(self, calls):
        r"""Sets the calls of this SlowSQLInfoResult.

        **参数解释**: 执行次数（次）。 **取值范围**: 不涉及。

        :param calls: The calls of this SlowSQLInfoResult.
        :type calls: int
        """
        self._calls = calls

    @property
    def avg_exec_time(self):
        r"""Gets the avg_exec_time of this SlowSQLInfoResult.

        **参数解释**: 平均执行时间（us）。 **取值范围**: 不涉及。

        :return: The avg_exec_time of this SlowSQLInfoResult.
        :rtype: str
        """
        return self._avg_exec_time

    @avg_exec_time.setter
    def avg_exec_time(self, avg_exec_time):
        r"""Sets the avg_exec_time of this SlowSQLInfoResult.

        **参数解释**: 平均执行时间（us）。 **取值范围**: 不涉及。

        :param avg_exec_time: The avg_exec_time of this SlowSQLInfoResult.
        :type avg_exec_time: str
        """
        self._avg_exec_time = avg_exec_time

    @property
    def avg_cpu_time(self):
        r"""Gets the avg_cpu_time of this SlowSQLInfoResult.

        **参数解释**: 平均CPU耗时（us）。 **取值范围**: 不涉及。

        :return: The avg_cpu_time of this SlowSQLInfoResult.
        :rtype: str
        """
        return self._avg_cpu_time

    @avg_cpu_time.setter
    def avg_cpu_time(self, avg_cpu_time):
        r"""Sets the avg_cpu_time of this SlowSQLInfoResult.

        **参数解释**: 平均CPU耗时（us）。 **取值范围**: 不涉及。

        :param avg_cpu_time: The avg_cpu_time of this SlowSQLInfoResult.
        :type avg_cpu_time: str
        """
        self._avg_cpu_time = avg_cpu_time

    @property
    def avg_io_time(self):
        r"""Gets the avg_io_time of this SlowSQLInfoResult.

        **参数解释**: 平均IO耗时（us）。 **取值范围**: 不涉及。

        :return: The avg_io_time of this SlowSQLInfoResult.
        :rtype: str
        """
        return self._avg_io_time

    @avg_io_time.setter
    def avg_io_time(self, avg_io_time):
        r"""Sets the avg_io_time of this SlowSQLInfoResult.

        **参数解释**: 平均IO耗时（us）。 **取值范围**: 不涉及。

        :param avg_io_time: The avg_io_time of this SlowSQLInfoResult.
        :type avg_io_time: str
        """
        self._avg_io_time = avg_io_time

    @property
    def avg_returned_rows(self):
        r"""Gets the avg_returned_rows of this SlowSQLInfoResult.

        **参数解释**: 平均返回行数（行）。 **取值范围**: 不涉及。

        :return: The avg_returned_rows of this SlowSQLInfoResult.
        :rtype: int
        """
        return self._avg_returned_rows

    @avg_returned_rows.setter
    def avg_returned_rows(self, avg_returned_rows):
        r"""Sets the avg_returned_rows of this SlowSQLInfoResult.

        **参数解释**: 平均返回行数（行）。 **取值范围**: 不涉及。

        :param avg_returned_rows: The avg_returned_rows of this SlowSQLInfoResult.
        :type avg_returned_rows: int
        """
        self._avg_returned_rows = avg_returned_rows

    @property
    def avg_fetched_rows(self):
        r"""Gets the avg_fetched_rows of this SlowSQLInfoResult.

        **参数解释**: 平均扫描行数（行）。 **取值范围**: 不涉及。

        :return: The avg_fetched_rows of this SlowSQLInfoResult.
        :rtype: int
        """
        return self._avg_fetched_rows

    @avg_fetched_rows.setter
    def avg_fetched_rows(self, avg_fetched_rows):
        r"""Sets the avg_fetched_rows of this SlowSQLInfoResult.

        **参数解释**: 平均扫描行数（行）。 **取值范围**: 不涉及。

        :param avg_fetched_rows: The avg_fetched_rows of this SlowSQLInfoResult.
        :type avg_fetched_rows: int
        """
        self._avg_fetched_rows = avg_fetched_rows

    @property
    def buffer_hit_ratio(self):
        r"""Gets the buffer_hit_ratio of this SlowSQLInfoResult.

        **参数解释**: buffer命中率。 **取值范围**: 不涉及。

        :return: The buffer_hit_ratio of this SlowSQLInfoResult.
        :rtype: str
        """
        return self._buffer_hit_ratio

    @buffer_hit_ratio.setter
    def buffer_hit_ratio(self, buffer_hit_ratio):
        r"""Sets the buffer_hit_ratio of this SlowSQLInfoResult.

        **参数解释**: buffer命中率。 **取值范围**: 不涉及。

        :param buffer_hit_ratio: The buffer_hit_ratio of this SlowSQLInfoResult.
        :type buffer_hit_ratio: str
        """
        self._buffer_hit_ratio = buffer_hit_ratio

    @property
    def sql_hit_ratio(self):
        r"""Gets the sql_hit_ratio of this SlowSQLInfoResult.

        **参数解释**: SQL命中率。 **取值范围**: 不涉及。

        :return: The sql_hit_ratio of this SlowSQLInfoResult.
        :rtype: str
        """
        return self._sql_hit_ratio

    @sql_hit_ratio.setter
    def sql_hit_ratio(self, sql_hit_ratio):
        r"""Sets the sql_hit_ratio of this SlowSQLInfoResult.

        **参数解释**: SQL命中率。 **取值范围**: 不涉及。

        :param sql_hit_ratio: The sql_hit_ratio of this SlowSQLInfoResult.
        :type sql_hit_ratio: str
        """
        self._sql_hit_ratio = sql_hit_ratio

    @property
    def node_id(self):
        r"""Gets the node_id of this SlowSQLInfoResult.

        **参数解释**: 节点ID。 **取值范围**: 不涉及。

        :return: The node_id of this SlowSQLInfoResult.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this SlowSQLInfoResult.

        **参数解释**: 节点ID。 **取值范围**: 不涉及。

        :param node_id: The node_id of this SlowSQLInfoResult.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_name(self):
        r"""Gets the node_name of this SlowSQLInfoResult.

        **参数解释**: 节点名称。 **取值范围**: 不涉及。

        :return: The node_name of this SlowSQLInfoResult.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this SlowSQLInfoResult.

        **参数解释**: 节点名称。 **取值范围**: 不涉及。

        :param node_name: The node_name of this SlowSQLInfoResult.
        :type node_name: str
        """
        self._node_name = node_name

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
        if not isinstance(other, SlowSQLInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
