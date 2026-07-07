# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDeadLockTopologyGraphRespTransactions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'transaction_id': 'str',
        'thread_id': 'int',
        'rollback_target': 'bool',
        'sql': 'str',
        'table': 'str',
        'operator': 'str',
        'row_lock_count': 'int',
        'undo_log_entries': 'int'
    }

    attribute_map = {
        'transaction_id': 'transaction_id',
        'thread_id': 'thread_id',
        'rollback_target': 'rollback_target',
        'sql': 'sql',
        'table': 'table',
        'operator': 'operator',
        'row_lock_count': 'row_lock_count',
        'undo_log_entries': 'undo_log_entries'
    }

    def __init__(self, transaction_id=None, thread_id=None, rollback_target=None, sql=None, table=None, operator=None, row_lock_count=None, undo_log_entries=None):
        r"""ShowDeadLockTopologyGraphRespTransactions

        The model defined in huaweicloud sdk

        :param transaction_id: 事务ID
        :type transaction_id: str
        :param thread_id: 线程ID
        :type thread_id: int
        :param rollback_target: 是否被回滚
        :type rollback_target: bool
        :param sql: SQL语句
        :type sql: str
        :param table: 操作的表名
        :type table: str
        :param operator: 操作类型
        :type operator: str
        :param row_lock_count: 行锁数量
        :type row_lock_count: int
        :param undo_log_entries: Undo日志条数
        :type undo_log_entries: int
        """
        
        

        self._transaction_id = None
        self._thread_id = None
        self._rollback_target = None
        self._sql = None
        self._table = None
        self._operator = None
        self._row_lock_count = None
        self._undo_log_entries = None
        self.discriminator = None

        self.transaction_id = transaction_id
        self.thread_id = thread_id
        self.rollback_target = rollback_target
        self.sql = sql
        self.table = table
        self.operator = operator
        self.row_lock_count = row_lock_count
        self.undo_log_entries = undo_log_entries

    @property
    def transaction_id(self):
        r"""Gets the transaction_id of this ShowDeadLockTopologyGraphRespTransactions.

        事务ID

        :return: The transaction_id of this ShowDeadLockTopologyGraphRespTransactions.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        r"""Sets the transaction_id of this ShowDeadLockTopologyGraphRespTransactions.

        事务ID

        :param transaction_id: The transaction_id of this ShowDeadLockTopologyGraphRespTransactions.
        :type transaction_id: str
        """
        self._transaction_id = transaction_id

    @property
    def thread_id(self):
        r"""Gets the thread_id of this ShowDeadLockTopologyGraphRespTransactions.

        线程ID

        :return: The thread_id of this ShowDeadLockTopologyGraphRespTransactions.
        :rtype: int
        """
        return self._thread_id

    @thread_id.setter
    def thread_id(self, thread_id):
        r"""Sets the thread_id of this ShowDeadLockTopologyGraphRespTransactions.

        线程ID

        :param thread_id: The thread_id of this ShowDeadLockTopologyGraphRespTransactions.
        :type thread_id: int
        """
        self._thread_id = thread_id

    @property
    def rollback_target(self):
        r"""Gets the rollback_target of this ShowDeadLockTopologyGraphRespTransactions.

        是否被回滚

        :return: The rollback_target of this ShowDeadLockTopologyGraphRespTransactions.
        :rtype: bool
        """
        return self._rollback_target

    @rollback_target.setter
    def rollback_target(self, rollback_target):
        r"""Sets the rollback_target of this ShowDeadLockTopologyGraphRespTransactions.

        是否被回滚

        :param rollback_target: The rollback_target of this ShowDeadLockTopologyGraphRespTransactions.
        :type rollback_target: bool
        """
        self._rollback_target = rollback_target

    @property
    def sql(self):
        r"""Gets the sql of this ShowDeadLockTopologyGraphRespTransactions.

        SQL语句

        :return: The sql of this ShowDeadLockTopologyGraphRespTransactions.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this ShowDeadLockTopologyGraphRespTransactions.

        SQL语句

        :param sql: The sql of this ShowDeadLockTopologyGraphRespTransactions.
        :type sql: str
        """
        self._sql = sql

    @property
    def table(self):
        r"""Gets the table of this ShowDeadLockTopologyGraphRespTransactions.

        操作的表名

        :return: The table of this ShowDeadLockTopologyGraphRespTransactions.
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        r"""Sets the table of this ShowDeadLockTopologyGraphRespTransactions.

        操作的表名

        :param table: The table of this ShowDeadLockTopologyGraphRespTransactions.
        :type table: str
        """
        self._table = table

    @property
    def operator(self):
        r"""Gets the operator of this ShowDeadLockTopologyGraphRespTransactions.

        操作类型

        :return: The operator of this ShowDeadLockTopologyGraphRespTransactions.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this ShowDeadLockTopologyGraphRespTransactions.

        操作类型

        :param operator: The operator of this ShowDeadLockTopologyGraphRespTransactions.
        :type operator: str
        """
        self._operator = operator

    @property
    def row_lock_count(self):
        r"""Gets the row_lock_count of this ShowDeadLockTopologyGraphRespTransactions.

        行锁数量

        :return: The row_lock_count of this ShowDeadLockTopologyGraphRespTransactions.
        :rtype: int
        """
        return self._row_lock_count

    @row_lock_count.setter
    def row_lock_count(self, row_lock_count):
        r"""Sets the row_lock_count of this ShowDeadLockTopologyGraphRespTransactions.

        行锁数量

        :param row_lock_count: The row_lock_count of this ShowDeadLockTopologyGraphRespTransactions.
        :type row_lock_count: int
        """
        self._row_lock_count = row_lock_count

    @property
    def undo_log_entries(self):
        r"""Gets the undo_log_entries of this ShowDeadLockTopologyGraphRespTransactions.

        Undo日志条数

        :return: The undo_log_entries of this ShowDeadLockTopologyGraphRespTransactions.
        :rtype: int
        """
        return self._undo_log_entries

    @undo_log_entries.setter
    def undo_log_entries(self, undo_log_entries):
        r"""Sets the undo_log_entries of this ShowDeadLockTopologyGraphRespTransactions.

        Undo日志条数

        :param undo_log_entries: The undo_log_entries of this ShowDeadLockTopologyGraphRespTransactions.
        :type undo_log_entries: int
        """
        self._undo_log_entries = undo_log_entries

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
        if not isinstance(other, ShowDeadLockTopologyGraphRespTransactions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
