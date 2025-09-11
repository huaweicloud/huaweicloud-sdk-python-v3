# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopSQLInfoResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_id': 'str',
        'user_name': 'str',
        'sql_text': 'str',
        'calls_percent': 'str',
        'cpu_percent': 'str',
        'io_percent': 'str',
        'calls': 'str',
        'returned_rows': 'str',
        'tuple_read': 'str',
        'avg_elapse_time': 'str',
        'total_elapse_time': 'str',
        'cpu_time': 'str',
        'io_time': 'str',
        'min_elapse_time': 'str',
        'max_elapse_time': 'str',
        'sql_hit_ratio': 'str',
        'node_id': 'str',
        'db_name': 'str',
        'node_name': 'str'
    }

    attribute_map = {
        'sql_id': 'sql_id',
        'user_name': 'user_name',
        'sql_text': 'sql_text',
        'calls_percent': 'calls_percent',
        'cpu_percent': 'cpu_percent',
        'io_percent': 'io_percent',
        'calls': 'calls',
        'returned_rows': 'returned_rows',
        'tuple_read': 'tuple_read',
        'avg_elapse_time': 'avg_elapse_time',
        'total_elapse_time': 'total_elapse_time',
        'cpu_time': 'cpu_time',
        'io_time': 'io_time',
        'min_elapse_time': 'min_elapse_time',
        'max_elapse_time': 'max_elapse_time',
        'sql_hit_ratio': 'sql_hit_ratio',
        'node_id': 'node_id',
        'db_name': 'db_name',
        'node_name': 'node_name'
    }

    def __init__(self, sql_id=None, user_name=None, sql_text=None, calls_percent=None, cpu_percent=None, io_percent=None, calls=None, returned_rows=None, tuple_read=None, avg_elapse_time=None, total_elapse_time=None, cpu_time=None, io_time=None, min_elapse_time=None, max_elapse_time=None, sql_hit_ratio=None, node_id=None, db_name=None, node_name=None):
        r"""TopSQLInfoResult

        The model defined in huaweicloud sdk

        :param sql_id: **参数解释**: Top SQL的归一化SQL ID。 **取值范围**: 不涉及。
        :type sql_id: str
        :param user_name: **参数解释**: Top SQL的用户名。 **取值范围**: 不涉及。
        :type user_name: str
        :param sql_text: **参数解释**: Top SQL的SQL文本。 **取值范围**: 不涉及。
        :type sql_text: str
        :param calls_percent: **参数解释**: Top SQL的调用频率占比（%）。 **取值范围**: 0-100。
        :type calls_percent: str
        :param cpu_percent: **参数解释**: Top SQL的调用频率占比。 **取值范围**: 0-100。
        :type cpu_percent: str
        :param io_percent: **参数解释**: Top SQL的IO开销占比。 **取值范围**: 0-100。
        :type io_percent: str
        :param calls: **参数解释** Top SQL的调用次数。 **取值范围** 大于等于0。
        :type calls: str
        :param returned_rows: **参数解释** Top SQL的返回元组数。 **取值范围** 大于等于0。
        :type returned_rows: str
        :param tuple_read: **参数解释** Top SQL的读取元组数。 **取值范围** 大于等于0。
        :type tuple_read: str
        :param avg_elapse_time: **参数解释** Top SQL的平均时间开销。单位ms。 **取值范围** 大于等于0。
        :type avg_elapse_time: str
        :param total_elapse_time: **参数解释** Top SQL的总时间开销。单位ms。 **取值范围** 大于等于0。
        :type total_elapse_time: str
        :param cpu_time: **参数解释**: Top SQL的CPU开销。单位ms。 **取值范围**: 不涉及。
        :type cpu_time: str
        :param io_time: **参数解释**: Top SQL的IO开销。单位ms。 **取值范围**: 不涉及。
        :type io_time: str
        :param min_elapse_time: **参数解释**: Top SQL的最小执行时间。单位ms。 **取值范围**: 不涉及。
        :type min_elapse_time: str
        :param max_elapse_time: **参数解释**: Top SQL最大执行时间。单位ms。 **取值范围**: 不涉及。
        :type max_elapse_time: str
        :param sql_hit_ratio: **参数解释** Top SQL的SQL命中率。 **取值范围** 大于等于0。
        :type sql_hit_ratio: str
        :param node_id: **参数解释**: Top SQL的节点ID。 **取值范围**: 不涉及。
        :type node_id: str
        :param db_name: **参数解释**: Top SQL的数据库名（引擎版本8.200及以上支持）。 **取值范围**: 不涉及。
        :type db_name: str
        :param node_name: **参数解释**: Top SQL的节点名称。 **取值范围**: 不涉及。
        :type node_name: str
        """
        
        

        self._sql_id = None
        self._user_name = None
        self._sql_text = None
        self._calls_percent = None
        self._cpu_percent = None
        self._io_percent = None
        self._calls = None
        self._returned_rows = None
        self._tuple_read = None
        self._avg_elapse_time = None
        self._total_elapse_time = None
        self._cpu_time = None
        self._io_time = None
        self._min_elapse_time = None
        self._max_elapse_time = None
        self._sql_hit_ratio = None
        self._node_id = None
        self._db_name = None
        self._node_name = None
        self.discriminator = None

        if sql_id is not None:
            self.sql_id = sql_id
        if user_name is not None:
            self.user_name = user_name
        if sql_text is not None:
            self.sql_text = sql_text
        if calls_percent is not None:
            self.calls_percent = calls_percent
        if cpu_percent is not None:
            self.cpu_percent = cpu_percent
        if io_percent is not None:
            self.io_percent = io_percent
        if calls is not None:
            self.calls = calls
        if returned_rows is not None:
            self.returned_rows = returned_rows
        if tuple_read is not None:
            self.tuple_read = tuple_read
        if avg_elapse_time is not None:
            self.avg_elapse_time = avg_elapse_time
        if total_elapse_time is not None:
            self.total_elapse_time = total_elapse_time
        if cpu_time is not None:
            self.cpu_time = cpu_time
        if io_time is not None:
            self.io_time = io_time
        if min_elapse_time is not None:
            self.min_elapse_time = min_elapse_time
        if max_elapse_time is not None:
            self.max_elapse_time = max_elapse_time
        if sql_hit_ratio is not None:
            self.sql_hit_ratio = sql_hit_ratio
        if node_id is not None:
            self.node_id = node_id
        if db_name is not None:
            self.db_name = db_name
        if node_name is not None:
            self.node_name = node_name

    @property
    def sql_id(self):
        r"""Gets the sql_id of this TopSQLInfoResult.

        **参数解释**: Top SQL的归一化SQL ID。 **取值范围**: 不涉及。

        :return: The sql_id of this TopSQLInfoResult.
        :rtype: str
        """
        return self._sql_id

    @sql_id.setter
    def sql_id(self, sql_id):
        r"""Sets the sql_id of this TopSQLInfoResult.

        **参数解释**: Top SQL的归一化SQL ID。 **取值范围**: 不涉及。

        :param sql_id: The sql_id of this TopSQLInfoResult.
        :type sql_id: str
        """
        self._sql_id = sql_id

    @property
    def user_name(self):
        r"""Gets the user_name of this TopSQLInfoResult.

        **参数解释**: Top SQL的用户名。 **取值范围**: 不涉及。

        :return: The user_name of this TopSQLInfoResult.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this TopSQLInfoResult.

        **参数解释**: Top SQL的用户名。 **取值范围**: 不涉及。

        :param user_name: The user_name of this TopSQLInfoResult.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def sql_text(self):
        r"""Gets the sql_text of this TopSQLInfoResult.

        **参数解释**: Top SQL的SQL文本。 **取值范围**: 不涉及。

        :return: The sql_text of this TopSQLInfoResult.
        :rtype: str
        """
        return self._sql_text

    @sql_text.setter
    def sql_text(self, sql_text):
        r"""Sets the sql_text of this TopSQLInfoResult.

        **参数解释**: Top SQL的SQL文本。 **取值范围**: 不涉及。

        :param sql_text: The sql_text of this TopSQLInfoResult.
        :type sql_text: str
        """
        self._sql_text = sql_text

    @property
    def calls_percent(self):
        r"""Gets the calls_percent of this TopSQLInfoResult.

        **参数解释**: Top SQL的调用频率占比（%）。 **取值范围**: 0-100。

        :return: The calls_percent of this TopSQLInfoResult.
        :rtype: str
        """
        return self._calls_percent

    @calls_percent.setter
    def calls_percent(self, calls_percent):
        r"""Sets the calls_percent of this TopSQLInfoResult.

        **参数解释**: Top SQL的调用频率占比（%）。 **取值范围**: 0-100。

        :param calls_percent: The calls_percent of this TopSQLInfoResult.
        :type calls_percent: str
        """
        self._calls_percent = calls_percent

    @property
    def cpu_percent(self):
        r"""Gets the cpu_percent of this TopSQLInfoResult.

        **参数解释**: Top SQL的调用频率占比。 **取值范围**: 0-100。

        :return: The cpu_percent of this TopSQLInfoResult.
        :rtype: str
        """
        return self._cpu_percent

    @cpu_percent.setter
    def cpu_percent(self, cpu_percent):
        r"""Sets the cpu_percent of this TopSQLInfoResult.

        **参数解释**: Top SQL的调用频率占比。 **取值范围**: 0-100。

        :param cpu_percent: The cpu_percent of this TopSQLInfoResult.
        :type cpu_percent: str
        """
        self._cpu_percent = cpu_percent

    @property
    def io_percent(self):
        r"""Gets the io_percent of this TopSQLInfoResult.

        **参数解释**: Top SQL的IO开销占比。 **取值范围**: 0-100。

        :return: The io_percent of this TopSQLInfoResult.
        :rtype: str
        """
        return self._io_percent

    @io_percent.setter
    def io_percent(self, io_percent):
        r"""Sets the io_percent of this TopSQLInfoResult.

        **参数解释**: Top SQL的IO开销占比。 **取值范围**: 0-100。

        :param io_percent: The io_percent of this TopSQLInfoResult.
        :type io_percent: str
        """
        self._io_percent = io_percent

    @property
    def calls(self):
        r"""Gets the calls of this TopSQLInfoResult.

        **参数解释** Top SQL的调用次数。 **取值范围** 大于等于0。

        :return: The calls of this TopSQLInfoResult.
        :rtype: str
        """
        return self._calls

    @calls.setter
    def calls(self, calls):
        r"""Sets the calls of this TopSQLInfoResult.

        **参数解释** Top SQL的调用次数。 **取值范围** 大于等于0。

        :param calls: The calls of this TopSQLInfoResult.
        :type calls: str
        """
        self._calls = calls

    @property
    def returned_rows(self):
        r"""Gets the returned_rows of this TopSQLInfoResult.

        **参数解释** Top SQL的返回元组数。 **取值范围** 大于等于0。

        :return: The returned_rows of this TopSQLInfoResult.
        :rtype: str
        """
        return self._returned_rows

    @returned_rows.setter
    def returned_rows(self, returned_rows):
        r"""Sets the returned_rows of this TopSQLInfoResult.

        **参数解释** Top SQL的返回元组数。 **取值范围** 大于等于0。

        :param returned_rows: The returned_rows of this TopSQLInfoResult.
        :type returned_rows: str
        """
        self._returned_rows = returned_rows

    @property
    def tuple_read(self):
        r"""Gets the tuple_read of this TopSQLInfoResult.

        **参数解释** Top SQL的读取元组数。 **取值范围** 大于等于0。

        :return: The tuple_read of this TopSQLInfoResult.
        :rtype: str
        """
        return self._tuple_read

    @tuple_read.setter
    def tuple_read(self, tuple_read):
        r"""Sets the tuple_read of this TopSQLInfoResult.

        **参数解释** Top SQL的读取元组数。 **取值范围** 大于等于0。

        :param tuple_read: The tuple_read of this TopSQLInfoResult.
        :type tuple_read: str
        """
        self._tuple_read = tuple_read

    @property
    def avg_elapse_time(self):
        r"""Gets the avg_elapse_time of this TopSQLInfoResult.

        **参数解释** Top SQL的平均时间开销。单位ms。 **取值范围** 大于等于0。

        :return: The avg_elapse_time of this TopSQLInfoResult.
        :rtype: str
        """
        return self._avg_elapse_time

    @avg_elapse_time.setter
    def avg_elapse_time(self, avg_elapse_time):
        r"""Sets the avg_elapse_time of this TopSQLInfoResult.

        **参数解释** Top SQL的平均时间开销。单位ms。 **取值范围** 大于等于0。

        :param avg_elapse_time: The avg_elapse_time of this TopSQLInfoResult.
        :type avg_elapse_time: str
        """
        self._avg_elapse_time = avg_elapse_time

    @property
    def total_elapse_time(self):
        r"""Gets the total_elapse_time of this TopSQLInfoResult.

        **参数解释** Top SQL的总时间开销。单位ms。 **取值范围** 大于等于0。

        :return: The total_elapse_time of this TopSQLInfoResult.
        :rtype: str
        """
        return self._total_elapse_time

    @total_elapse_time.setter
    def total_elapse_time(self, total_elapse_time):
        r"""Sets the total_elapse_time of this TopSQLInfoResult.

        **参数解释** Top SQL的总时间开销。单位ms。 **取值范围** 大于等于0。

        :param total_elapse_time: The total_elapse_time of this TopSQLInfoResult.
        :type total_elapse_time: str
        """
        self._total_elapse_time = total_elapse_time

    @property
    def cpu_time(self):
        r"""Gets the cpu_time of this TopSQLInfoResult.

        **参数解释**: Top SQL的CPU开销。单位ms。 **取值范围**: 不涉及。

        :return: The cpu_time of this TopSQLInfoResult.
        :rtype: str
        """
        return self._cpu_time

    @cpu_time.setter
    def cpu_time(self, cpu_time):
        r"""Sets the cpu_time of this TopSQLInfoResult.

        **参数解释**: Top SQL的CPU开销。单位ms。 **取值范围**: 不涉及。

        :param cpu_time: The cpu_time of this TopSQLInfoResult.
        :type cpu_time: str
        """
        self._cpu_time = cpu_time

    @property
    def io_time(self):
        r"""Gets the io_time of this TopSQLInfoResult.

        **参数解释**: Top SQL的IO开销。单位ms。 **取值范围**: 不涉及。

        :return: The io_time of this TopSQLInfoResult.
        :rtype: str
        """
        return self._io_time

    @io_time.setter
    def io_time(self, io_time):
        r"""Sets the io_time of this TopSQLInfoResult.

        **参数解释**: Top SQL的IO开销。单位ms。 **取值范围**: 不涉及。

        :param io_time: The io_time of this TopSQLInfoResult.
        :type io_time: str
        """
        self._io_time = io_time

    @property
    def min_elapse_time(self):
        r"""Gets the min_elapse_time of this TopSQLInfoResult.

        **参数解释**: Top SQL的最小执行时间。单位ms。 **取值范围**: 不涉及。

        :return: The min_elapse_time of this TopSQLInfoResult.
        :rtype: str
        """
        return self._min_elapse_time

    @min_elapse_time.setter
    def min_elapse_time(self, min_elapse_time):
        r"""Sets the min_elapse_time of this TopSQLInfoResult.

        **参数解释**: Top SQL的最小执行时间。单位ms。 **取值范围**: 不涉及。

        :param min_elapse_time: The min_elapse_time of this TopSQLInfoResult.
        :type min_elapse_time: str
        """
        self._min_elapse_time = min_elapse_time

    @property
    def max_elapse_time(self):
        r"""Gets the max_elapse_time of this TopSQLInfoResult.

        **参数解释**: Top SQL最大执行时间。单位ms。 **取值范围**: 不涉及。

        :return: The max_elapse_time of this TopSQLInfoResult.
        :rtype: str
        """
        return self._max_elapse_time

    @max_elapse_time.setter
    def max_elapse_time(self, max_elapse_time):
        r"""Sets the max_elapse_time of this TopSQLInfoResult.

        **参数解释**: Top SQL最大执行时间。单位ms。 **取值范围**: 不涉及。

        :param max_elapse_time: The max_elapse_time of this TopSQLInfoResult.
        :type max_elapse_time: str
        """
        self._max_elapse_time = max_elapse_time

    @property
    def sql_hit_ratio(self):
        r"""Gets the sql_hit_ratio of this TopSQLInfoResult.

        **参数解释** Top SQL的SQL命中率。 **取值范围** 大于等于0。

        :return: The sql_hit_ratio of this TopSQLInfoResult.
        :rtype: str
        """
        return self._sql_hit_ratio

    @sql_hit_ratio.setter
    def sql_hit_ratio(self, sql_hit_ratio):
        r"""Sets the sql_hit_ratio of this TopSQLInfoResult.

        **参数解释** Top SQL的SQL命中率。 **取值范围** 大于等于0。

        :param sql_hit_ratio: The sql_hit_ratio of this TopSQLInfoResult.
        :type sql_hit_ratio: str
        """
        self._sql_hit_ratio = sql_hit_ratio

    @property
    def node_id(self):
        r"""Gets the node_id of this TopSQLInfoResult.

        **参数解释**: Top SQL的节点ID。 **取值范围**: 不涉及。

        :return: The node_id of this TopSQLInfoResult.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this TopSQLInfoResult.

        **参数解释**: Top SQL的节点ID。 **取值范围**: 不涉及。

        :param node_id: The node_id of this TopSQLInfoResult.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def db_name(self):
        r"""Gets the db_name of this TopSQLInfoResult.

        **参数解释**: Top SQL的数据库名（引擎版本8.200及以上支持）。 **取值范围**: 不涉及。

        :return: The db_name of this TopSQLInfoResult.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this TopSQLInfoResult.

        **参数解释**: Top SQL的数据库名（引擎版本8.200及以上支持）。 **取值范围**: 不涉及。

        :param db_name: The db_name of this TopSQLInfoResult.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def node_name(self):
        r"""Gets the node_name of this TopSQLInfoResult.

        **参数解释**: Top SQL的节点名称。 **取值范围**: 不涉及。

        :return: The node_name of this TopSQLInfoResult.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this TopSQLInfoResult.

        **参数解释**: Top SQL的节点名称。 **取值范围**: 不涉及。

        :param node_name: The node_name of this TopSQLInfoResult.
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
        if not isinstance(other, TopSQLInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
