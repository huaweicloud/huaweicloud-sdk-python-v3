# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetadataLock:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'thread_id': 'str',
        'lock_status': 'str',
        'lock_mode': 'str',
        'lock_type': 'str',
        'lock_duration': 'str',
        'table_schema': 'str',
        'table_name': 'str',
        'user': 'str',
        'time': 'str',
        'host': 'str',
        'database': 'str',
        'command': 'str',
        'state': 'str',
        'sql': 'str',
        'trx_exec_time': 'str',
        'block_process': 'list[Process]',
        'wait_process': 'list[Process]'
    }

    attribute_map = {
        'thread_id': 'thread_id',
        'lock_status': 'lock_status',
        'lock_mode': 'lock_mode',
        'lock_type': 'lock_type',
        'lock_duration': 'lock_duration',
        'table_schema': 'table_schema',
        'table_name': 'table_name',
        'user': 'user',
        'time': 'time',
        'host': 'host',
        'database': 'database',
        'command': 'command',
        'state': 'state',
        'sql': 'sql',
        'trx_exec_time': 'trx_exec_time',
        'block_process': 'block_process',
        'wait_process': 'wait_process'
    }

    def __init__(self, thread_id=None, lock_status=None, lock_mode=None, lock_type=None, lock_duration=None, table_schema=None, table_name=None, user=None, time=None, host=None, database=None, command=None, state=None, sql=None, trx_exec_time=None, block_process=None, wait_process=None):
        r"""MetadataLock

        The model defined in huaweicloud sdk

        :param thread_id: 会话ID
        :type thread_id: str
        :param lock_status: 锁状态，取值为PENDING和GRANTED，分别表示等待锁和持有锁。
        :type lock_status: str
        :param lock_mode: 加锁模式，取值为MDL_SHARED 、MDL_EXCLUSIVE 、MDL_SHARED_READ、MDL_SHARED_WRITE等。
        :type lock_mode: str
        :param lock_type: 锁类型，取值为Table metadata lock、Schema metadata lock、Tablespace lock、Global read lock，分别表示表元数据锁、库元数据锁、表空间锁、全局读锁。
        :type lock_type: str
        :param lock_duration: 锁范围，取值为MDL_STATEMENT、MDL_TRANSACTION、MDL_EXPLICIT，分别表示语句级别、事务级别、global级别
        :type lock_duration: str
        :param table_schema: 锁所在的数据库，对于部分Global read lock级别的元数据锁，该值为空。
        :type table_schema: str
        :param table_name: 表名
        :type table_name: str
        :param user: 用户
        :type user: str
        :param time: 时间
        :type time: str
        :param host: 主机
        :type host: str
        :param database: 会话所在的数据库
        :type database: str
        :param command: 命令
        :type command: str
        :param state: 状态
        :type state: str
        :param sql: SQL语句
        :type sql: str
        :param trx_exec_time: 事务执行时间
        :type trx_exec_time: str
        :param block_process: 阻塞会话列表
        :type block_process: list[:class:`huaweicloudsdkdas.v3.Process`]
        :param wait_process: 等待会话列表
        :type wait_process: list[:class:`huaweicloudsdkdas.v3.Process`]
        """
        
        

        self._thread_id = None
        self._lock_status = None
        self._lock_mode = None
        self._lock_type = None
        self._lock_duration = None
        self._table_schema = None
        self._table_name = None
        self._user = None
        self._time = None
        self._host = None
        self._database = None
        self._command = None
        self._state = None
        self._sql = None
        self._trx_exec_time = None
        self._block_process = None
        self._wait_process = None
        self.discriminator = None

        self.thread_id = thread_id
        self.lock_status = lock_status
        self.lock_mode = lock_mode
        self.lock_type = lock_type
        self.lock_duration = lock_duration
        self.table_schema = table_schema
        self.table_name = table_name
        self.user = user
        self.time = time
        self.host = host
        self.database = database
        self.command = command
        self.state = state
        self.sql = sql
        self.trx_exec_time = trx_exec_time
        self.block_process = block_process
        self.wait_process = wait_process

    @property
    def thread_id(self):
        r"""Gets the thread_id of this MetadataLock.

        会话ID

        :return: The thread_id of this MetadataLock.
        :rtype: str
        """
        return self._thread_id

    @thread_id.setter
    def thread_id(self, thread_id):
        r"""Sets the thread_id of this MetadataLock.

        会话ID

        :param thread_id: The thread_id of this MetadataLock.
        :type thread_id: str
        """
        self._thread_id = thread_id

    @property
    def lock_status(self):
        r"""Gets the lock_status of this MetadataLock.

        锁状态，取值为PENDING和GRANTED，分别表示等待锁和持有锁。

        :return: The lock_status of this MetadataLock.
        :rtype: str
        """
        return self._lock_status

    @lock_status.setter
    def lock_status(self, lock_status):
        r"""Sets the lock_status of this MetadataLock.

        锁状态，取值为PENDING和GRANTED，分别表示等待锁和持有锁。

        :param lock_status: The lock_status of this MetadataLock.
        :type lock_status: str
        """
        self._lock_status = lock_status

    @property
    def lock_mode(self):
        r"""Gets the lock_mode of this MetadataLock.

        加锁模式，取值为MDL_SHARED 、MDL_EXCLUSIVE 、MDL_SHARED_READ、MDL_SHARED_WRITE等。

        :return: The lock_mode of this MetadataLock.
        :rtype: str
        """
        return self._lock_mode

    @lock_mode.setter
    def lock_mode(self, lock_mode):
        r"""Sets the lock_mode of this MetadataLock.

        加锁模式，取值为MDL_SHARED 、MDL_EXCLUSIVE 、MDL_SHARED_READ、MDL_SHARED_WRITE等。

        :param lock_mode: The lock_mode of this MetadataLock.
        :type lock_mode: str
        """
        self._lock_mode = lock_mode

    @property
    def lock_type(self):
        r"""Gets the lock_type of this MetadataLock.

        锁类型，取值为Table metadata lock、Schema metadata lock、Tablespace lock、Global read lock，分别表示表元数据锁、库元数据锁、表空间锁、全局读锁。

        :return: The lock_type of this MetadataLock.
        :rtype: str
        """
        return self._lock_type

    @lock_type.setter
    def lock_type(self, lock_type):
        r"""Sets the lock_type of this MetadataLock.

        锁类型，取值为Table metadata lock、Schema metadata lock、Tablespace lock、Global read lock，分别表示表元数据锁、库元数据锁、表空间锁、全局读锁。

        :param lock_type: The lock_type of this MetadataLock.
        :type lock_type: str
        """
        self._lock_type = lock_type

    @property
    def lock_duration(self):
        r"""Gets the lock_duration of this MetadataLock.

        锁范围，取值为MDL_STATEMENT、MDL_TRANSACTION、MDL_EXPLICIT，分别表示语句级别、事务级别、global级别

        :return: The lock_duration of this MetadataLock.
        :rtype: str
        """
        return self._lock_duration

    @lock_duration.setter
    def lock_duration(self, lock_duration):
        r"""Sets the lock_duration of this MetadataLock.

        锁范围，取值为MDL_STATEMENT、MDL_TRANSACTION、MDL_EXPLICIT，分别表示语句级别、事务级别、global级别

        :param lock_duration: The lock_duration of this MetadataLock.
        :type lock_duration: str
        """
        self._lock_duration = lock_duration

    @property
    def table_schema(self):
        r"""Gets the table_schema of this MetadataLock.

        锁所在的数据库，对于部分Global read lock级别的元数据锁，该值为空。

        :return: The table_schema of this MetadataLock.
        :rtype: str
        """
        return self._table_schema

    @table_schema.setter
    def table_schema(self, table_schema):
        r"""Sets the table_schema of this MetadataLock.

        锁所在的数据库，对于部分Global read lock级别的元数据锁，该值为空。

        :param table_schema: The table_schema of this MetadataLock.
        :type table_schema: str
        """
        self._table_schema = table_schema

    @property
    def table_name(self):
        r"""Gets the table_name of this MetadataLock.

        表名

        :return: The table_name of this MetadataLock.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this MetadataLock.

        表名

        :param table_name: The table_name of this MetadataLock.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def user(self):
        r"""Gets the user of this MetadataLock.

        用户

        :return: The user of this MetadataLock.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this MetadataLock.

        用户

        :param user: The user of this MetadataLock.
        :type user: str
        """
        self._user = user

    @property
    def time(self):
        r"""Gets the time of this MetadataLock.

        时间

        :return: The time of this MetadataLock.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this MetadataLock.

        时间

        :param time: The time of this MetadataLock.
        :type time: str
        """
        self._time = time

    @property
    def host(self):
        r"""Gets the host of this MetadataLock.

        主机

        :return: The host of this MetadataLock.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this MetadataLock.

        主机

        :param host: The host of this MetadataLock.
        :type host: str
        """
        self._host = host

    @property
    def database(self):
        r"""Gets the database of this MetadataLock.

        会话所在的数据库

        :return: The database of this MetadataLock.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this MetadataLock.

        会话所在的数据库

        :param database: The database of this MetadataLock.
        :type database: str
        """
        self._database = database

    @property
    def command(self):
        r"""Gets the command of this MetadataLock.

        命令

        :return: The command of this MetadataLock.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this MetadataLock.

        命令

        :param command: The command of this MetadataLock.
        :type command: str
        """
        self._command = command

    @property
    def state(self):
        r"""Gets the state of this MetadataLock.

        状态

        :return: The state of this MetadataLock.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this MetadataLock.

        状态

        :param state: The state of this MetadataLock.
        :type state: str
        """
        self._state = state

    @property
    def sql(self):
        r"""Gets the sql of this MetadataLock.

        SQL语句

        :return: The sql of this MetadataLock.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this MetadataLock.

        SQL语句

        :param sql: The sql of this MetadataLock.
        :type sql: str
        """
        self._sql = sql

    @property
    def trx_exec_time(self):
        r"""Gets the trx_exec_time of this MetadataLock.

        事务执行时间

        :return: The trx_exec_time of this MetadataLock.
        :rtype: str
        """
        return self._trx_exec_time

    @trx_exec_time.setter
    def trx_exec_time(self, trx_exec_time):
        r"""Sets the trx_exec_time of this MetadataLock.

        事务执行时间

        :param trx_exec_time: The trx_exec_time of this MetadataLock.
        :type trx_exec_time: str
        """
        self._trx_exec_time = trx_exec_time

    @property
    def block_process(self):
        r"""Gets the block_process of this MetadataLock.

        阻塞会话列表

        :return: The block_process of this MetadataLock.
        :rtype: list[:class:`huaweicloudsdkdas.v3.Process`]
        """
        return self._block_process

    @block_process.setter
    def block_process(self, block_process):
        r"""Sets the block_process of this MetadataLock.

        阻塞会话列表

        :param block_process: The block_process of this MetadataLock.
        :type block_process: list[:class:`huaweicloudsdkdas.v3.Process`]
        """
        self._block_process = block_process

    @property
    def wait_process(self):
        r"""Gets the wait_process of this MetadataLock.

        等待会话列表

        :return: The wait_process of this MetadataLock.
        :rtype: list[:class:`huaweicloudsdkdas.v3.Process`]
        """
        return self._wait_process

    @wait_process.setter
    def wait_process(self, wait_process):
        r"""Sets the wait_process of this MetadataLock.

        等待会话列表

        :param wait_process: The wait_process of this MetadataLock.
        :type wait_process: list[:class:`huaweicloudsdkdas.v3.Process`]
        """
        self._wait_process = wait_process

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
        if not isinstance(other, MetadataLock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
