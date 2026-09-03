# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MySQLTransaction:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'session_id': 'str',
        'thread_id': 'str',
        'request_type': 'str',
        'transaction_id': 'str',
        'table': 'str',
        'waiting_lock': 'str',
        'waiting_lock_index': 'str',
        'waiting_lock_type': 'str',
        'holding_lock': 'str',
        'holding_lock_index': 'str',
        'holding_lock_type': 'str',
        'sql': 'str'
    }

    attribute_map = {
        'session_id': 'session_id',
        'thread_id': 'thread_id',
        'request_type': 'request_type',
        'transaction_id': 'transaction_id',
        'table': 'table',
        'waiting_lock': 'waiting_lock',
        'waiting_lock_index': 'waiting_lock_index',
        'waiting_lock_type': 'waiting_lock_type',
        'holding_lock': 'holding_lock',
        'holding_lock_index': 'holding_lock_index',
        'holding_lock_type': 'holding_lock_type',
        'sql': 'sql'
    }

    def __init__(self, session_id=None, thread_id=None, request_type=None, transaction_id=None, table=None, waiting_lock=None, waiting_lock_index=None, waiting_lock_type=None, holding_lock=None, holding_lock_index=None, holding_lock_type=None, sql=None):
        r"""MySQLTransaction

        The model defined in huaweicloud sdk

        :param session_id: 会话ID
        :type session_id: str
        :param thread_id: 线程ID
        :type thread_id: str
        :param request_type: 请求类型
        :type request_type: str
        :param transaction_id: 事务ID
        :type transaction_id: str
        :param table: 涉及表
        :type table: str
        :param waiting_lock: 等待锁
        :type waiting_lock: str
        :param waiting_lock_index: 等待锁索引名
        :type waiting_lock_index: str
        :param waiting_lock_type: 等待锁索引类型
        :type waiting_lock_type: str
        :param holding_lock: 持有锁
        :type holding_lock: str
        :param holding_lock_index: 持有锁索引
        :type holding_lock_index: str
        :param holding_lock_type: 持有锁索引类型
        :type holding_lock_type: str
        :param sql: SQL语句
        :type sql: str
        """
        
        

        self._session_id = None
        self._thread_id = None
        self._request_type = None
        self._transaction_id = None
        self._table = None
        self._waiting_lock = None
        self._waiting_lock_index = None
        self._waiting_lock_type = None
        self._holding_lock = None
        self._holding_lock_index = None
        self._holding_lock_type = None
        self._sql = None
        self.discriminator = None

        if session_id is not None:
            self.session_id = session_id
        if thread_id is not None:
            self.thread_id = thread_id
        if request_type is not None:
            self.request_type = request_type
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if table is not None:
            self.table = table
        if waiting_lock is not None:
            self.waiting_lock = waiting_lock
        if waiting_lock_index is not None:
            self.waiting_lock_index = waiting_lock_index
        if waiting_lock_type is not None:
            self.waiting_lock_type = waiting_lock_type
        if holding_lock is not None:
            self.holding_lock = holding_lock
        if holding_lock_index is not None:
            self.holding_lock_index = holding_lock_index
        if holding_lock_type is not None:
            self.holding_lock_type = holding_lock_type
        if sql is not None:
            self.sql = sql

    @property
    def session_id(self):
        r"""Gets the session_id of this MySQLTransaction.

        会话ID

        :return: The session_id of this MySQLTransaction.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this MySQLTransaction.

        会话ID

        :param session_id: The session_id of this MySQLTransaction.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def thread_id(self):
        r"""Gets the thread_id of this MySQLTransaction.

        线程ID

        :return: The thread_id of this MySQLTransaction.
        :rtype: str
        """
        return self._thread_id

    @thread_id.setter
    def thread_id(self, thread_id):
        r"""Sets the thread_id of this MySQLTransaction.

        线程ID

        :param thread_id: The thread_id of this MySQLTransaction.
        :type thread_id: str
        """
        self._thread_id = thread_id

    @property
    def request_type(self):
        r"""Gets the request_type of this MySQLTransaction.

        请求类型

        :return: The request_type of this MySQLTransaction.
        :rtype: str
        """
        return self._request_type

    @request_type.setter
    def request_type(self, request_type):
        r"""Sets the request_type of this MySQLTransaction.

        请求类型

        :param request_type: The request_type of this MySQLTransaction.
        :type request_type: str
        """
        self._request_type = request_type

    @property
    def transaction_id(self):
        r"""Gets the transaction_id of this MySQLTransaction.

        事务ID

        :return: The transaction_id of this MySQLTransaction.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        r"""Sets the transaction_id of this MySQLTransaction.

        事务ID

        :param transaction_id: The transaction_id of this MySQLTransaction.
        :type transaction_id: str
        """
        self._transaction_id = transaction_id

    @property
    def table(self):
        r"""Gets the table of this MySQLTransaction.

        涉及表

        :return: The table of this MySQLTransaction.
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        r"""Sets the table of this MySQLTransaction.

        涉及表

        :param table: The table of this MySQLTransaction.
        :type table: str
        """
        self._table = table

    @property
    def waiting_lock(self):
        r"""Gets the waiting_lock of this MySQLTransaction.

        等待锁

        :return: The waiting_lock of this MySQLTransaction.
        :rtype: str
        """
        return self._waiting_lock

    @waiting_lock.setter
    def waiting_lock(self, waiting_lock):
        r"""Sets the waiting_lock of this MySQLTransaction.

        等待锁

        :param waiting_lock: The waiting_lock of this MySQLTransaction.
        :type waiting_lock: str
        """
        self._waiting_lock = waiting_lock

    @property
    def waiting_lock_index(self):
        r"""Gets the waiting_lock_index of this MySQLTransaction.

        等待锁索引名

        :return: The waiting_lock_index of this MySQLTransaction.
        :rtype: str
        """
        return self._waiting_lock_index

    @waiting_lock_index.setter
    def waiting_lock_index(self, waiting_lock_index):
        r"""Sets the waiting_lock_index of this MySQLTransaction.

        等待锁索引名

        :param waiting_lock_index: The waiting_lock_index of this MySQLTransaction.
        :type waiting_lock_index: str
        """
        self._waiting_lock_index = waiting_lock_index

    @property
    def waiting_lock_type(self):
        r"""Gets the waiting_lock_type of this MySQLTransaction.

        等待锁索引类型

        :return: The waiting_lock_type of this MySQLTransaction.
        :rtype: str
        """
        return self._waiting_lock_type

    @waiting_lock_type.setter
    def waiting_lock_type(self, waiting_lock_type):
        r"""Sets the waiting_lock_type of this MySQLTransaction.

        等待锁索引类型

        :param waiting_lock_type: The waiting_lock_type of this MySQLTransaction.
        :type waiting_lock_type: str
        """
        self._waiting_lock_type = waiting_lock_type

    @property
    def holding_lock(self):
        r"""Gets the holding_lock of this MySQLTransaction.

        持有锁

        :return: The holding_lock of this MySQLTransaction.
        :rtype: str
        """
        return self._holding_lock

    @holding_lock.setter
    def holding_lock(self, holding_lock):
        r"""Sets the holding_lock of this MySQLTransaction.

        持有锁

        :param holding_lock: The holding_lock of this MySQLTransaction.
        :type holding_lock: str
        """
        self._holding_lock = holding_lock

    @property
    def holding_lock_index(self):
        r"""Gets the holding_lock_index of this MySQLTransaction.

        持有锁索引

        :return: The holding_lock_index of this MySQLTransaction.
        :rtype: str
        """
        return self._holding_lock_index

    @holding_lock_index.setter
    def holding_lock_index(self, holding_lock_index):
        r"""Sets the holding_lock_index of this MySQLTransaction.

        持有锁索引

        :param holding_lock_index: The holding_lock_index of this MySQLTransaction.
        :type holding_lock_index: str
        """
        self._holding_lock_index = holding_lock_index

    @property
    def holding_lock_type(self):
        r"""Gets the holding_lock_type of this MySQLTransaction.

        持有锁索引类型

        :return: The holding_lock_type of this MySQLTransaction.
        :rtype: str
        """
        return self._holding_lock_type

    @holding_lock_type.setter
    def holding_lock_type(self, holding_lock_type):
        r"""Sets the holding_lock_type of this MySQLTransaction.

        持有锁索引类型

        :param holding_lock_type: The holding_lock_type of this MySQLTransaction.
        :type holding_lock_type: str
        """
        self._holding_lock_type = holding_lock_type

    @property
    def sql(self):
        r"""Gets the sql of this MySQLTransaction.

        SQL语句

        :return: The sql of this MySQLTransaction.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this MySQLTransaction.

        SQL语句

        :param sql: The sql of this MySQLTransaction.
        :type sql: str
        """
        self._sql = sql

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
        if not isinstance(other, MySQLTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
