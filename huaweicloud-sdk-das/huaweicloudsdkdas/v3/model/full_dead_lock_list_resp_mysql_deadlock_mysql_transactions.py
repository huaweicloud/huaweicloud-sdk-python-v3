# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FullDeadLockListRespMysqlDeadlockMysqlTransactions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table': 'str',
        'sql': 'str',
        'session_id': 'str',
        'thread_id': 'str',
        'request_type': 'str',
        'transaction_id': 'str',
        'waiting_lock': 'str',
        'waiting_lock_index': 'str',
        'waiting_lock_type': 'str'
    }

    attribute_map = {
        'table': 'table',
        'sql': 'sql',
        'session_id': 'session_id',
        'thread_id': 'thread_id',
        'request_type': 'request_type',
        'transaction_id': 'transaction_id',
        'waiting_lock': 'waiting_lock',
        'waiting_lock_index': 'waiting_lock_index',
        'waiting_lock_type': 'waiting_lock_type'
    }

    def __init__(self, table=None, sql=None, session_id=None, thread_id=None, request_type=None, transaction_id=None, waiting_lock=None, waiting_lock_index=None, waiting_lock_type=None):
        r"""FullDeadLockListRespMysqlDeadlockMysqlTransactions

        The model defined in huaweicloud sdk

        :param table: 表
        :type table: str
        :param sql: 具体sql
        :type sql: str
        :param session_id: 会话id
        :type session_id: str
        :param thread_id: 线程id
        :type thread_id: str
        :param request_type: 请求类型
        :type request_type: str
        :param transaction_id: 内部事务id
        :type transaction_id: str
        :param waiting_lock: 事务正在等待的锁的描述
        :type waiting_lock: str
        :param waiting_lock_index: 锁针对的索引
        :type waiting_lock_index: str
        :param waiting_lock_type: 锁类型
        :type waiting_lock_type: str
        """
        
        

        self._table = None
        self._sql = None
        self._session_id = None
        self._thread_id = None
        self._request_type = None
        self._transaction_id = None
        self._waiting_lock = None
        self._waiting_lock_index = None
        self._waiting_lock_type = None
        self.discriminator = None

        if table is not None:
            self.table = table
        if sql is not None:
            self.sql = sql
        if session_id is not None:
            self.session_id = session_id
        if thread_id is not None:
            self.thread_id = thread_id
        if request_type is not None:
            self.request_type = request_type
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if waiting_lock is not None:
            self.waiting_lock = waiting_lock
        if waiting_lock_index is not None:
            self.waiting_lock_index = waiting_lock_index
        if waiting_lock_type is not None:
            self.waiting_lock_type = waiting_lock_type

    @property
    def table(self):
        r"""Gets the table of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.

        表

        :return: The table of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        r"""Sets the table of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.

        表

        :param table: The table of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.
        :type table: str
        """
        self._table = table

    @property
    def sql(self):
        r"""Gets the sql of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.

        具体sql

        :return: The sql of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.

        具体sql

        :param sql: The sql of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.
        :type sql: str
        """
        self._sql = sql

    @property
    def session_id(self):
        r"""Gets the session_id of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.

        会话id

        :return: The session_id of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.

        会话id

        :param session_id: The session_id of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def thread_id(self):
        r"""Gets the thread_id of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.

        线程id

        :return: The thread_id of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.
        :rtype: str
        """
        return self._thread_id

    @thread_id.setter
    def thread_id(self, thread_id):
        r"""Sets the thread_id of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.

        线程id

        :param thread_id: The thread_id of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.
        :type thread_id: str
        """
        self._thread_id = thread_id

    @property
    def request_type(self):
        r"""Gets the request_type of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.

        请求类型

        :return: The request_type of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.
        :rtype: str
        """
        return self._request_type

    @request_type.setter
    def request_type(self, request_type):
        r"""Sets the request_type of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.

        请求类型

        :param request_type: The request_type of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.
        :type request_type: str
        """
        self._request_type = request_type

    @property
    def transaction_id(self):
        r"""Gets the transaction_id of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.

        内部事务id

        :return: The transaction_id of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        r"""Sets the transaction_id of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.

        内部事务id

        :param transaction_id: The transaction_id of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.
        :type transaction_id: str
        """
        self._transaction_id = transaction_id

    @property
    def waiting_lock(self):
        r"""Gets the waiting_lock of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.

        事务正在等待的锁的描述

        :return: The waiting_lock of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.
        :rtype: str
        """
        return self._waiting_lock

    @waiting_lock.setter
    def waiting_lock(self, waiting_lock):
        r"""Sets the waiting_lock of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.

        事务正在等待的锁的描述

        :param waiting_lock: The waiting_lock of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.
        :type waiting_lock: str
        """
        self._waiting_lock = waiting_lock

    @property
    def waiting_lock_index(self):
        r"""Gets the waiting_lock_index of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.

        锁针对的索引

        :return: The waiting_lock_index of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.
        :rtype: str
        """
        return self._waiting_lock_index

    @waiting_lock_index.setter
    def waiting_lock_index(self, waiting_lock_index):
        r"""Sets the waiting_lock_index of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.

        锁针对的索引

        :param waiting_lock_index: The waiting_lock_index of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.
        :type waiting_lock_index: str
        """
        self._waiting_lock_index = waiting_lock_index

    @property
    def waiting_lock_type(self):
        r"""Gets the waiting_lock_type of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.

        锁类型

        :return: The waiting_lock_type of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.
        :rtype: str
        """
        return self._waiting_lock_type

    @waiting_lock_type.setter
    def waiting_lock_type(self, waiting_lock_type):
        r"""Sets the waiting_lock_type of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.

        锁类型

        :param waiting_lock_type: The waiting_lock_type of this FullDeadLockListRespMysqlDeadlockMysqlTransactions.
        :type waiting_lock_type: str
        """
        self._waiting_lock_type = waiting_lock_type

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
        if not isinstance(other, FullDeadLockListRespMysqlDeadlockMysqlTransactions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
