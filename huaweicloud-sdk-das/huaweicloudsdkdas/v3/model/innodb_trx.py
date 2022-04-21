# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InnodbTrx:

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
        'trx_wait_started': 'str',
        'trx_mysql_thread_id': 'str',
        'trx_query': 'str',
        'trx_tables_locked': 'str',
        'trx_rows_locked': 'str',
        'trx_rows_modified': 'str',
        'trx_isolation_level': 'str',
        'innodb_wait_locks': 'list[InnodbLock]',
        'innodb_hold_locks': 'list[InnodbLock]'
    }

    attribute_map = {
        'trx_id': 'trx_id',
        'trx_state': 'trx_state',
        'trx_started': 'trx_started',
        'trx_wait_started': 'trx_wait_started',
        'trx_mysql_thread_id': 'trx_mysql_thread_id',
        'trx_query': 'trx_query',
        'trx_tables_locked': 'trx_tables_locked',
        'trx_rows_locked': 'trx_rows_locked',
        'trx_rows_modified': 'trx_rows_modified',
        'trx_isolation_level': 'trx_isolation_level',
        'innodb_wait_locks': 'innodb_wait_locks',
        'innodb_hold_locks': 'innodb_hold_locks'
    }

    def __init__(self, trx_id=None, trx_state=None, trx_started=None, trx_wait_started=None, trx_mysql_thread_id=None, trx_query=None, trx_tables_locked=None, trx_rows_locked=None, trx_rows_modified=None, trx_isolation_level=None, innodb_wait_locks=None, innodb_hold_locks=None):
        """InnodbTrx

        The model defined in huaweicloud sdk

        :param trx_id: 事务ID
        :type trx_id: str
        :param trx_state: 事务状态
        :type trx_state: str
        :param trx_started: 事务开始时间
        :type trx_started: str
        :param trx_wait_started: 事务等待开始时间
        :type trx_wait_started: str
        :param trx_mysql_thread_id: 会话ID，同ListProcesses接口返回的id。
        :type trx_mysql_thread_id: str
        :param trx_query: 事务运行的SQL语句
        :type trx_query: str
        :param trx_tables_locked: 加行锁的表数量
        :type trx_tables_locked: str
        :param trx_rows_locked: 锁定的行数量（近似值）
        :type trx_rows_locked: str
        :param trx_rows_modified: 事务插入或者修改的行数
        :type trx_rows_modified: str
        :param trx_isolation_level: 隔离级别
        :type trx_isolation_level: str
        :param innodb_wait_locks: 等待锁信息
        :type innodb_wait_locks: list[:class:`huaweicloudsdkdas.v3.InnodbLock`]
        :param innodb_hold_locks: 持有锁信息
        :type innodb_hold_locks: list[:class:`huaweicloudsdkdas.v3.InnodbLock`]
        """
        
        

        self._trx_id = None
        self._trx_state = None
        self._trx_started = None
        self._trx_wait_started = None
        self._trx_mysql_thread_id = None
        self._trx_query = None
        self._trx_tables_locked = None
        self._trx_rows_locked = None
        self._trx_rows_modified = None
        self._trx_isolation_level = None
        self._innodb_wait_locks = None
        self._innodb_hold_locks = None
        self.discriminator = None

        self.trx_id = trx_id
        self.trx_state = trx_state
        self.trx_started = trx_started
        self.trx_wait_started = trx_wait_started
        self.trx_mysql_thread_id = trx_mysql_thread_id
        self.trx_query = trx_query
        self.trx_tables_locked = trx_tables_locked
        self.trx_rows_locked = trx_rows_locked
        self.trx_rows_modified = trx_rows_modified
        self.trx_isolation_level = trx_isolation_level
        self.innodb_wait_locks = innodb_wait_locks
        self.innodb_hold_locks = innodb_hold_locks

    @property
    def trx_id(self):
        """Gets the trx_id of this InnodbTrx.

        事务ID

        :return: The trx_id of this InnodbTrx.
        :rtype: str
        """
        return self._trx_id

    @trx_id.setter
    def trx_id(self, trx_id):
        """Sets the trx_id of this InnodbTrx.

        事务ID

        :param trx_id: The trx_id of this InnodbTrx.
        :type trx_id: str
        """
        self._trx_id = trx_id

    @property
    def trx_state(self):
        """Gets the trx_state of this InnodbTrx.

        事务状态

        :return: The trx_state of this InnodbTrx.
        :rtype: str
        """
        return self._trx_state

    @trx_state.setter
    def trx_state(self, trx_state):
        """Sets the trx_state of this InnodbTrx.

        事务状态

        :param trx_state: The trx_state of this InnodbTrx.
        :type trx_state: str
        """
        self._trx_state = trx_state

    @property
    def trx_started(self):
        """Gets the trx_started of this InnodbTrx.

        事务开始时间

        :return: The trx_started of this InnodbTrx.
        :rtype: str
        """
        return self._trx_started

    @trx_started.setter
    def trx_started(self, trx_started):
        """Sets the trx_started of this InnodbTrx.

        事务开始时间

        :param trx_started: The trx_started of this InnodbTrx.
        :type trx_started: str
        """
        self._trx_started = trx_started

    @property
    def trx_wait_started(self):
        """Gets the trx_wait_started of this InnodbTrx.

        事务等待开始时间

        :return: The trx_wait_started of this InnodbTrx.
        :rtype: str
        """
        return self._trx_wait_started

    @trx_wait_started.setter
    def trx_wait_started(self, trx_wait_started):
        """Sets the trx_wait_started of this InnodbTrx.

        事务等待开始时间

        :param trx_wait_started: The trx_wait_started of this InnodbTrx.
        :type trx_wait_started: str
        """
        self._trx_wait_started = trx_wait_started

    @property
    def trx_mysql_thread_id(self):
        """Gets the trx_mysql_thread_id of this InnodbTrx.

        会话ID，同ListProcesses接口返回的id。

        :return: The trx_mysql_thread_id of this InnodbTrx.
        :rtype: str
        """
        return self._trx_mysql_thread_id

    @trx_mysql_thread_id.setter
    def trx_mysql_thread_id(self, trx_mysql_thread_id):
        """Sets the trx_mysql_thread_id of this InnodbTrx.

        会话ID，同ListProcesses接口返回的id。

        :param trx_mysql_thread_id: The trx_mysql_thread_id of this InnodbTrx.
        :type trx_mysql_thread_id: str
        """
        self._trx_mysql_thread_id = trx_mysql_thread_id

    @property
    def trx_query(self):
        """Gets the trx_query of this InnodbTrx.

        事务运行的SQL语句

        :return: The trx_query of this InnodbTrx.
        :rtype: str
        """
        return self._trx_query

    @trx_query.setter
    def trx_query(self, trx_query):
        """Sets the trx_query of this InnodbTrx.

        事务运行的SQL语句

        :param trx_query: The trx_query of this InnodbTrx.
        :type trx_query: str
        """
        self._trx_query = trx_query

    @property
    def trx_tables_locked(self):
        """Gets the trx_tables_locked of this InnodbTrx.

        加行锁的表数量

        :return: The trx_tables_locked of this InnodbTrx.
        :rtype: str
        """
        return self._trx_tables_locked

    @trx_tables_locked.setter
    def trx_tables_locked(self, trx_tables_locked):
        """Sets the trx_tables_locked of this InnodbTrx.

        加行锁的表数量

        :param trx_tables_locked: The trx_tables_locked of this InnodbTrx.
        :type trx_tables_locked: str
        """
        self._trx_tables_locked = trx_tables_locked

    @property
    def trx_rows_locked(self):
        """Gets the trx_rows_locked of this InnodbTrx.

        锁定的行数量（近似值）

        :return: The trx_rows_locked of this InnodbTrx.
        :rtype: str
        """
        return self._trx_rows_locked

    @trx_rows_locked.setter
    def trx_rows_locked(self, trx_rows_locked):
        """Sets the trx_rows_locked of this InnodbTrx.

        锁定的行数量（近似值）

        :param trx_rows_locked: The trx_rows_locked of this InnodbTrx.
        :type trx_rows_locked: str
        """
        self._trx_rows_locked = trx_rows_locked

    @property
    def trx_rows_modified(self):
        """Gets the trx_rows_modified of this InnodbTrx.

        事务插入或者修改的行数

        :return: The trx_rows_modified of this InnodbTrx.
        :rtype: str
        """
        return self._trx_rows_modified

    @trx_rows_modified.setter
    def trx_rows_modified(self, trx_rows_modified):
        """Sets the trx_rows_modified of this InnodbTrx.

        事务插入或者修改的行数

        :param trx_rows_modified: The trx_rows_modified of this InnodbTrx.
        :type trx_rows_modified: str
        """
        self._trx_rows_modified = trx_rows_modified

    @property
    def trx_isolation_level(self):
        """Gets the trx_isolation_level of this InnodbTrx.

        隔离级别

        :return: The trx_isolation_level of this InnodbTrx.
        :rtype: str
        """
        return self._trx_isolation_level

    @trx_isolation_level.setter
    def trx_isolation_level(self, trx_isolation_level):
        """Sets the trx_isolation_level of this InnodbTrx.

        隔离级别

        :param trx_isolation_level: The trx_isolation_level of this InnodbTrx.
        :type trx_isolation_level: str
        """
        self._trx_isolation_level = trx_isolation_level

    @property
    def innodb_wait_locks(self):
        """Gets the innodb_wait_locks of this InnodbTrx.

        等待锁信息

        :return: The innodb_wait_locks of this InnodbTrx.
        :rtype: list[:class:`huaweicloudsdkdas.v3.InnodbLock`]
        """
        return self._innodb_wait_locks

    @innodb_wait_locks.setter
    def innodb_wait_locks(self, innodb_wait_locks):
        """Sets the innodb_wait_locks of this InnodbTrx.

        等待锁信息

        :param innodb_wait_locks: The innodb_wait_locks of this InnodbTrx.
        :type innodb_wait_locks: list[:class:`huaweicloudsdkdas.v3.InnodbLock`]
        """
        self._innodb_wait_locks = innodb_wait_locks

    @property
    def innodb_hold_locks(self):
        """Gets the innodb_hold_locks of this InnodbTrx.

        持有锁信息

        :return: The innodb_hold_locks of this InnodbTrx.
        :rtype: list[:class:`huaweicloudsdkdas.v3.InnodbLock`]
        """
        return self._innodb_hold_locks

    @innodb_hold_locks.setter
    def innodb_hold_locks(self, innodb_hold_locks):
        """Sets the innodb_hold_locks of this InnodbTrx.

        持有锁信息

        :param innodb_hold_locks: The innodb_hold_locks of this InnodbTrx.
        :type innodb_hold_locks: list[:class:`huaweicloudsdkdas.v3.InnodbLock`]
        """
        self._innodb_hold_locks = innodb_hold_locks

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
        if not isinstance(other, InnodbTrx):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
