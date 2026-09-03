# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InnodbTrxInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trx_id': 'str',
        'trx_state': 'str',
        'trx_started': 'str',
        'trx_started_timestamp': 'int',
        'trx_requested_lock_id': 'str',
        'trx_wait_started': 'str',
        'trx_wait_started_timestamp': 'int',
        'trx_weight': 'str',
        'trx_mysql_thread_id': 'str',
        'trx_query': 'str',
        'trx_operation_state': 'str',
        'trx_tables_in_use': 'str',
        'trx_tables_locked': 'str',
        'trx_lock_structs': 'str',
        'trx_lock_memory_bytes': 'str',
        'trx_rows_locked': 'str',
        'trx_rows_modified': 'str',
        'trx_concurrency_tickets': 'str',
        'trx_isolation_level': 'str'
    }

    attribute_map = {
        'trx_id': 'trx_id',
        'trx_state': 'trx_state',
        'trx_started': 'trx_started',
        'trx_started_timestamp': 'trx_started_timestamp',
        'trx_requested_lock_id': 'trx_requested_lock_id',
        'trx_wait_started': 'trx_wait_started',
        'trx_wait_started_timestamp': 'trx_wait_started_timestamp',
        'trx_weight': 'trx_weight',
        'trx_mysql_thread_id': 'trx_mysql_thread_id',
        'trx_query': 'trx_query',
        'trx_operation_state': 'trx_operation_state',
        'trx_tables_in_use': 'trx_tables_in_use',
        'trx_tables_locked': 'trx_tables_locked',
        'trx_lock_structs': 'trx_lock_structs',
        'trx_lock_memory_bytes': 'trx_lock_memory_bytes',
        'trx_rows_locked': 'trx_rows_locked',
        'trx_rows_modified': 'trx_rows_modified',
        'trx_concurrency_tickets': 'trx_concurrency_tickets',
        'trx_isolation_level': 'trx_isolation_level'
    }

    def __init__(self, trx_id=None, trx_state=None, trx_started=None, trx_started_timestamp=None, trx_requested_lock_id=None, trx_wait_started=None, trx_wait_started_timestamp=None, trx_weight=None, trx_mysql_thread_id=None, trx_query=None, trx_operation_state=None, trx_tables_in_use=None, trx_tables_locked=None, trx_lock_structs=None, trx_lock_memory_bytes=None, trx_rows_locked=None, trx_rows_modified=None, trx_concurrency_tickets=None, trx_isolation_level=None):
        r"""InnodbTrxInfo

        The model defined in huaweicloud sdk

        :param trx_id: 事务ID
        :type trx_id: str
        :param trx_state: 事务状态
        :type trx_state: str
        :param trx_started: 事务开始时间
        :type trx_started: str
        :param trx_started_timestamp: 事务开始时间戳
        :type trx_started_timestamp: int
        :param trx_requested_lock_id: 事务当前正在等待锁的Id
        :type trx_requested_lock_id: str
        :param trx_wait_started: 事务开始等待时间
        :type trx_wait_started: str
        :param trx_wait_started_timestamp: 事务开始等待时间戳
        :type trx_wait_started_timestamp: int
        :param trx_weight: 事务权重
        :type trx_weight: str
        :param trx_mysql_thread_id: 会话ID
        :type trx_mysql_thread_id: str
        :param trx_query: 事务正在执行的SQL语句
        :type trx_query: str
        :param trx_operation_state: 事务当前操作状态
        :type trx_operation_state: str
        :param trx_tables_in_use: 当前事务执行的SQL中使用的表个数
        :type trx_tables_in_use: str
        :param trx_tables_locked: 当前执行SQL的行锁数量
        :type trx_tables_locked: str
        :param trx_lock_structs: 事务保留的锁数量
        :type trx_lock_structs: str
        :param trx_lock_memory_bytes: 事务锁住的内存大小
        :type trx_lock_memory_bytes: str
        :param trx_rows_locked: 事务锁住的行记录数
        :type trx_rows_locked: str
        :param trx_rows_modified: 事务更改的行数
        :type trx_rows_modified: str
        :param trx_concurrency_tickets: 事务并发票数
        :type trx_concurrency_tickets: str
        :param trx_isolation_level: 事务隔离级别
        :type trx_isolation_level: str
        """
        
        

        self._trx_id = None
        self._trx_state = None
        self._trx_started = None
        self._trx_started_timestamp = None
        self._trx_requested_lock_id = None
        self._trx_wait_started = None
        self._trx_wait_started_timestamp = None
        self._trx_weight = None
        self._trx_mysql_thread_id = None
        self._trx_query = None
        self._trx_operation_state = None
        self._trx_tables_in_use = None
        self._trx_tables_locked = None
        self._trx_lock_structs = None
        self._trx_lock_memory_bytes = None
        self._trx_rows_locked = None
        self._trx_rows_modified = None
        self._trx_concurrency_tickets = None
        self._trx_isolation_level = None
        self.discriminator = None

        if trx_id is not None:
            self.trx_id = trx_id
        if trx_state is not None:
            self.trx_state = trx_state
        if trx_started is not None:
            self.trx_started = trx_started
        if trx_started_timestamp is not None:
            self.trx_started_timestamp = trx_started_timestamp
        if trx_requested_lock_id is not None:
            self.trx_requested_lock_id = trx_requested_lock_id
        if trx_wait_started is not None:
            self.trx_wait_started = trx_wait_started
        if trx_wait_started_timestamp is not None:
            self.trx_wait_started_timestamp = trx_wait_started_timestamp
        if trx_weight is not None:
            self.trx_weight = trx_weight
        if trx_mysql_thread_id is not None:
            self.trx_mysql_thread_id = trx_mysql_thread_id
        if trx_query is not None:
            self.trx_query = trx_query
        if trx_operation_state is not None:
            self.trx_operation_state = trx_operation_state
        if trx_tables_in_use is not None:
            self.trx_tables_in_use = trx_tables_in_use
        if trx_tables_locked is not None:
            self.trx_tables_locked = trx_tables_locked
        if trx_lock_structs is not None:
            self.trx_lock_structs = trx_lock_structs
        if trx_lock_memory_bytes is not None:
            self.trx_lock_memory_bytes = trx_lock_memory_bytes
        if trx_rows_locked is not None:
            self.trx_rows_locked = trx_rows_locked
        if trx_rows_modified is not None:
            self.trx_rows_modified = trx_rows_modified
        if trx_concurrency_tickets is not None:
            self.trx_concurrency_tickets = trx_concurrency_tickets
        if trx_isolation_level is not None:
            self.trx_isolation_level = trx_isolation_level

    @property
    def trx_id(self):
        r"""Gets the trx_id of this InnodbTrxInfo.

        事务ID

        :return: The trx_id of this InnodbTrxInfo.
        :rtype: str
        """
        return self._trx_id

    @trx_id.setter
    def trx_id(self, trx_id):
        r"""Sets the trx_id of this InnodbTrxInfo.

        事务ID

        :param trx_id: The trx_id of this InnodbTrxInfo.
        :type trx_id: str
        """
        self._trx_id = trx_id

    @property
    def trx_state(self):
        r"""Gets the trx_state of this InnodbTrxInfo.

        事务状态

        :return: The trx_state of this InnodbTrxInfo.
        :rtype: str
        """
        return self._trx_state

    @trx_state.setter
    def trx_state(self, trx_state):
        r"""Sets the trx_state of this InnodbTrxInfo.

        事务状态

        :param trx_state: The trx_state of this InnodbTrxInfo.
        :type trx_state: str
        """
        self._trx_state = trx_state

    @property
    def trx_started(self):
        r"""Gets the trx_started of this InnodbTrxInfo.

        事务开始时间

        :return: The trx_started of this InnodbTrxInfo.
        :rtype: str
        """
        return self._trx_started

    @trx_started.setter
    def trx_started(self, trx_started):
        r"""Sets the trx_started of this InnodbTrxInfo.

        事务开始时间

        :param trx_started: The trx_started of this InnodbTrxInfo.
        :type trx_started: str
        """
        self._trx_started = trx_started

    @property
    def trx_started_timestamp(self):
        r"""Gets the trx_started_timestamp of this InnodbTrxInfo.

        事务开始时间戳

        :return: The trx_started_timestamp of this InnodbTrxInfo.
        :rtype: int
        """
        return self._trx_started_timestamp

    @trx_started_timestamp.setter
    def trx_started_timestamp(self, trx_started_timestamp):
        r"""Sets the trx_started_timestamp of this InnodbTrxInfo.

        事务开始时间戳

        :param trx_started_timestamp: The trx_started_timestamp of this InnodbTrxInfo.
        :type trx_started_timestamp: int
        """
        self._trx_started_timestamp = trx_started_timestamp

    @property
    def trx_requested_lock_id(self):
        r"""Gets the trx_requested_lock_id of this InnodbTrxInfo.

        事务当前正在等待锁的Id

        :return: The trx_requested_lock_id of this InnodbTrxInfo.
        :rtype: str
        """
        return self._trx_requested_lock_id

    @trx_requested_lock_id.setter
    def trx_requested_lock_id(self, trx_requested_lock_id):
        r"""Sets the trx_requested_lock_id of this InnodbTrxInfo.

        事务当前正在等待锁的Id

        :param trx_requested_lock_id: The trx_requested_lock_id of this InnodbTrxInfo.
        :type trx_requested_lock_id: str
        """
        self._trx_requested_lock_id = trx_requested_lock_id

    @property
    def trx_wait_started(self):
        r"""Gets the trx_wait_started of this InnodbTrxInfo.

        事务开始等待时间

        :return: The trx_wait_started of this InnodbTrxInfo.
        :rtype: str
        """
        return self._trx_wait_started

    @trx_wait_started.setter
    def trx_wait_started(self, trx_wait_started):
        r"""Sets the trx_wait_started of this InnodbTrxInfo.

        事务开始等待时间

        :param trx_wait_started: The trx_wait_started of this InnodbTrxInfo.
        :type trx_wait_started: str
        """
        self._trx_wait_started = trx_wait_started

    @property
    def trx_wait_started_timestamp(self):
        r"""Gets the trx_wait_started_timestamp of this InnodbTrxInfo.

        事务开始等待时间戳

        :return: The trx_wait_started_timestamp of this InnodbTrxInfo.
        :rtype: int
        """
        return self._trx_wait_started_timestamp

    @trx_wait_started_timestamp.setter
    def trx_wait_started_timestamp(self, trx_wait_started_timestamp):
        r"""Sets the trx_wait_started_timestamp of this InnodbTrxInfo.

        事务开始等待时间戳

        :param trx_wait_started_timestamp: The trx_wait_started_timestamp of this InnodbTrxInfo.
        :type trx_wait_started_timestamp: int
        """
        self._trx_wait_started_timestamp = trx_wait_started_timestamp

    @property
    def trx_weight(self):
        r"""Gets the trx_weight of this InnodbTrxInfo.

        事务权重

        :return: The trx_weight of this InnodbTrxInfo.
        :rtype: str
        """
        return self._trx_weight

    @trx_weight.setter
    def trx_weight(self, trx_weight):
        r"""Sets the trx_weight of this InnodbTrxInfo.

        事务权重

        :param trx_weight: The trx_weight of this InnodbTrxInfo.
        :type trx_weight: str
        """
        self._trx_weight = trx_weight

    @property
    def trx_mysql_thread_id(self):
        r"""Gets the trx_mysql_thread_id of this InnodbTrxInfo.

        会话ID

        :return: The trx_mysql_thread_id of this InnodbTrxInfo.
        :rtype: str
        """
        return self._trx_mysql_thread_id

    @trx_mysql_thread_id.setter
    def trx_mysql_thread_id(self, trx_mysql_thread_id):
        r"""Sets the trx_mysql_thread_id of this InnodbTrxInfo.

        会话ID

        :param trx_mysql_thread_id: The trx_mysql_thread_id of this InnodbTrxInfo.
        :type trx_mysql_thread_id: str
        """
        self._trx_mysql_thread_id = trx_mysql_thread_id

    @property
    def trx_query(self):
        r"""Gets the trx_query of this InnodbTrxInfo.

        事务正在执行的SQL语句

        :return: The trx_query of this InnodbTrxInfo.
        :rtype: str
        """
        return self._trx_query

    @trx_query.setter
    def trx_query(self, trx_query):
        r"""Sets the trx_query of this InnodbTrxInfo.

        事务正在执行的SQL语句

        :param trx_query: The trx_query of this InnodbTrxInfo.
        :type trx_query: str
        """
        self._trx_query = trx_query

    @property
    def trx_operation_state(self):
        r"""Gets the trx_operation_state of this InnodbTrxInfo.

        事务当前操作状态

        :return: The trx_operation_state of this InnodbTrxInfo.
        :rtype: str
        """
        return self._trx_operation_state

    @trx_operation_state.setter
    def trx_operation_state(self, trx_operation_state):
        r"""Sets the trx_operation_state of this InnodbTrxInfo.

        事务当前操作状态

        :param trx_operation_state: The trx_operation_state of this InnodbTrxInfo.
        :type trx_operation_state: str
        """
        self._trx_operation_state = trx_operation_state

    @property
    def trx_tables_in_use(self):
        r"""Gets the trx_tables_in_use of this InnodbTrxInfo.

        当前事务执行的SQL中使用的表个数

        :return: The trx_tables_in_use of this InnodbTrxInfo.
        :rtype: str
        """
        return self._trx_tables_in_use

    @trx_tables_in_use.setter
    def trx_tables_in_use(self, trx_tables_in_use):
        r"""Sets the trx_tables_in_use of this InnodbTrxInfo.

        当前事务执行的SQL中使用的表个数

        :param trx_tables_in_use: The trx_tables_in_use of this InnodbTrxInfo.
        :type trx_tables_in_use: str
        """
        self._trx_tables_in_use = trx_tables_in_use

    @property
    def trx_tables_locked(self):
        r"""Gets the trx_tables_locked of this InnodbTrxInfo.

        当前执行SQL的行锁数量

        :return: The trx_tables_locked of this InnodbTrxInfo.
        :rtype: str
        """
        return self._trx_tables_locked

    @trx_tables_locked.setter
    def trx_tables_locked(self, trx_tables_locked):
        r"""Sets the trx_tables_locked of this InnodbTrxInfo.

        当前执行SQL的行锁数量

        :param trx_tables_locked: The trx_tables_locked of this InnodbTrxInfo.
        :type trx_tables_locked: str
        """
        self._trx_tables_locked = trx_tables_locked

    @property
    def trx_lock_structs(self):
        r"""Gets the trx_lock_structs of this InnodbTrxInfo.

        事务保留的锁数量

        :return: The trx_lock_structs of this InnodbTrxInfo.
        :rtype: str
        """
        return self._trx_lock_structs

    @trx_lock_structs.setter
    def trx_lock_structs(self, trx_lock_structs):
        r"""Sets the trx_lock_structs of this InnodbTrxInfo.

        事务保留的锁数量

        :param trx_lock_structs: The trx_lock_structs of this InnodbTrxInfo.
        :type trx_lock_structs: str
        """
        self._trx_lock_structs = trx_lock_structs

    @property
    def trx_lock_memory_bytes(self):
        r"""Gets the trx_lock_memory_bytes of this InnodbTrxInfo.

        事务锁住的内存大小

        :return: The trx_lock_memory_bytes of this InnodbTrxInfo.
        :rtype: str
        """
        return self._trx_lock_memory_bytes

    @trx_lock_memory_bytes.setter
    def trx_lock_memory_bytes(self, trx_lock_memory_bytes):
        r"""Sets the trx_lock_memory_bytes of this InnodbTrxInfo.

        事务锁住的内存大小

        :param trx_lock_memory_bytes: The trx_lock_memory_bytes of this InnodbTrxInfo.
        :type trx_lock_memory_bytes: str
        """
        self._trx_lock_memory_bytes = trx_lock_memory_bytes

    @property
    def trx_rows_locked(self):
        r"""Gets the trx_rows_locked of this InnodbTrxInfo.

        事务锁住的行记录数

        :return: The trx_rows_locked of this InnodbTrxInfo.
        :rtype: str
        """
        return self._trx_rows_locked

    @trx_rows_locked.setter
    def trx_rows_locked(self, trx_rows_locked):
        r"""Sets the trx_rows_locked of this InnodbTrxInfo.

        事务锁住的行记录数

        :param trx_rows_locked: The trx_rows_locked of this InnodbTrxInfo.
        :type trx_rows_locked: str
        """
        self._trx_rows_locked = trx_rows_locked

    @property
    def trx_rows_modified(self):
        r"""Gets the trx_rows_modified of this InnodbTrxInfo.

        事务更改的行数

        :return: The trx_rows_modified of this InnodbTrxInfo.
        :rtype: str
        """
        return self._trx_rows_modified

    @trx_rows_modified.setter
    def trx_rows_modified(self, trx_rows_modified):
        r"""Sets the trx_rows_modified of this InnodbTrxInfo.

        事务更改的行数

        :param trx_rows_modified: The trx_rows_modified of this InnodbTrxInfo.
        :type trx_rows_modified: str
        """
        self._trx_rows_modified = trx_rows_modified

    @property
    def trx_concurrency_tickets(self):
        r"""Gets the trx_concurrency_tickets of this InnodbTrxInfo.

        事务并发票数

        :return: The trx_concurrency_tickets of this InnodbTrxInfo.
        :rtype: str
        """
        return self._trx_concurrency_tickets

    @trx_concurrency_tickets.setter
    def trx_concurrency_tickets(self, trx_concurrency_tickets):
        r"""Sets the trx_concurrency_tickets of this InnodbTrxInfo.

        事务并发票数

        :param trx_concurrency_tickets: The trx_concurrency_tickets of this InnodbTrxInfo.
        :type trx_concurrency_tickets: str
        """
        self._trx_concurrency_tickets = trx_concurrency_tickets

    @property
    def trx_isolation_level(self):
        r"""Gets the trx_isolation_level of this InnodbTrxInfo.

        事务隔离级别

        :return: The trx_isolation_level of this InnodbTrxInfo.
        :rtype: str
        """
        return self._trx_isolation_level

    @trx_isolation_level.setter
    def trx_isolation_level(self, trx_isolation_level):
        r"""Sets the trx_isolation_level of this InnodbTrxInfo.

        事务隔离级别

        :param trx_isolation_level: The trx_isolation_level of this InnodbTrxInfo.
        :type trx_isolation_level: str
        """
        self._trx_isolation_level = trx_isolation_level

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
        if not isinstance(other, InnodbTrxInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
