# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetaLockInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'lock_id': 'str',
        'thread_id': 'str',
        'lock_status': 'str',
        'lock_mode': 'str',
        'lock_type': 'str',
        'lock_duration': 'str',
        'table_schema': 'str',
        'table_name': 'str',
        'user': 'str',
        'time': 'str',
        'block_number': 'int',
        'wait_number': 'int',
        'host': 'str',
        'db_name': 'str',
        'command': 'str',
        'state': 'str',
        'info': 'str',
        'sql_limit_rule': 'str',
        'trx_exec_time': 'str',
        'block_process_info': 'list[ProcessInfo]',
        'wait_process_info': 'list[ProcessInfo]'
    }

    attribute_map = {
        'lock_id': 'lock_id',
        'thread_id': 'thread_id',
        'lock_status': 'lock_status',
        'lock_mode': 'lock_mode',
        'lock_type': 'lock_type',
        'lock_duration': 'lock_duration',
        'table_schema': 'table_schema',
        'table_name': 'table_name',
        'user': 'user',
        'time': 'time',
        'block_number': 'block_number',
        'wait_number': 'wait_number',
        'host': 'host',
        'db_name': 'db_name',
        'command': 'command',
        'state': 'state',
        'info': 'info',
        'sql_limit_rule': 'sql_limit_rule',
        'trx_exec_time': 'trx_exec_time',
        'block_process_info': 'block_process_info',
        'wait_process_info': 'wait_process_info'
    }

    def __init__(self, lock_id=None, thread_id=None, lock_status=None, lock_mode=None, lock_type=None, lock_duration=None, table_schema=None, table_name=None, user=None, time=None, block_number=None, wait_number=None, host=None, db_name=None, command=None, state=None, info=None, sql_limit_rule=None, trx_exec_time=None, block_process_info=None, wait_process_info=None):
        r"""MetaLockInfo

        The model defined in huaweicloud sdk

        :param lock_id: MDL锁ID
        :type lock_id: str
        :param thread_id: 线程ID
        :type thread_id: str
        :param lock_status: MDL锁状态
        :type lock_status: str
        :param lock_mode: MDL锁等待模式
        :type lock_mode: str
        :param lock_type: MDL锁等待信息
        :type lock_type: str
        :param lock_duration: MDL锁等待持续时间
        :type lock_duration: str
        :param table_schema: 库表schema信息
        :type table_schema: str
        :param table_name: 表名称
        :type table_name: str
        :param user: 用户名称
        :type user: str
        :param time: MDL锁等待时间
        :type time: str
        :param block_number: MDL锁等待阻塞数量
        :type block_number: int
        :param wait_number: MDL锁等待数量
        :type wait_number: int
        :param host: 主机
        :type host: str
        :param db_name: 数据库名称
        :type db_name: str
        :param command: MDL锁等待SQL语句
        :type command: str
        :param state: MDL锁等待状态
        :type state: str
        :param info: MDL锁等待额外信息
        :type info: str
        :param sql_limit_rule: 关联的SQL限流规则
        :type sql_limit_rule: str
        :param trx_exec_time: 事务执行时间
        :type trx_exec_time: str
        :param block_process_info: 阻塞的事务信息列表
        :type block_process_info: list[:class:`huaweicloudsdkdas.v3.ProcessInfo`]
        :param wait_process_info: 等待的事务信息列表
        :type wait_process_info: list[:class:`huaweicloudsdkdas.v3.ProcessInfo`]
        """
        
        

        self._lock_id = None
        self._thread_id = None
        self._lock_status = None
        self._lock_mode = None
        self._lock_type = None
        self._lock_duration = None
        self._table_schema = None
        self._table_name = None
        self._user = None
        self._time = None
        self._block_number = None
        self._wait_number = None
        self._host = None
        self._db_name = None
        self._command = None
        self._state = None
        self._info = None
        self._sql_limit_rule = None
        self._trx_exec_time = None
        self._block_process_info = None
        self._wait_process_info = None
        self.discriminator = None

        if lock_id is not None:
            self.lock_id = lock_id
        if thread_id is not None:
            self.thread_id = thread_id
        if lock_status is not None:
            self.lock_status = lock_status
        if lock_mode is not None:
            self.lock_mode = lock_mode
        if lock_type is not None:
            self.lock_type = lock_type
        if lock_duration is not None:
            self.lock_duration = lock_duration
        if table_schema is not None:
            self.table_schema = table_schema
        if table_name is not None:
            self.table_name = table_name
        if user is not None:
            self.user = user
        if time is not None:
            self.time = time
        if block_number is not None:
            self.block_number = block_number
        if wait_number is not None:
            self.wait_number = wait_number
        if host is not None:
            self.host = host
        if db_name is not None:
            self.db_name = db_name
        if command is not None:
            self.command = command
        if state is not None:
            self.state = state
        if info is not None:
            self.info = info
        if sql_limit_rule is not None:
            self.sql_limit_rule = sql_limit_rule
        if trx_exec_time is not None:
            self.trx_exec_time = trx_exec_time
        if block_process_info is not None:
            self.block_process_info = block_process_info
        if wait_process_info is not None:
            self.wait_process_info = wait_process_info

    @property
    def lock_id(self):
        r"""Gets the lock_id of this MetaLockInfo.

        MDL锁ID

        :return: The lock_id of this MetaLockInfo.
        :rtype: str
        """
        return self._lock_id

    @lock_id.setter
    def lock_id(self, lock_id):
        r"""Sets the lock_id of this MetaLockInfo.

        MDL锁ID

        :param lock_id: The lock_id of this MetaLockInfo.
        :type lock_id: str
        """
        self._lock_id = lock_id

    @property
    def thread_id(self):
        r"""Gets the thread_id of this MetaLockInfo.

        线程ID

        :return: The thread_id of this MetaLockInfo.
        :rtype: str
        """
        return self._thread_id

    @thread_id.setter
    def thread_id(self, thread_id):
        r"""Sets the thread_id of this MetaLockInfo.

        线程ID

        :param thread_id: The thread_id of this MetaLockInfo.
        :type thread_id: str
        """
        self._thread_id = thread_id

    @property
    def lock_status(self):
        r"""Gets the lock_status of this MetaLockInfo.

        MDL锁状态

        :return: The lock_status of this MetaLockInfo.
        :rtype: str
        """
        return self._lock_status

    @lock_status.setter
    def lock_status(self, lock_status):
        r"""Sets the lock_status of this MetaLockInfo.

        MDL锁状态

        :param lock_status: The lock_status of this MetaLockInfo.
        :type lock_status: str
        """
        self._lock_status = lock_status

    @property
    def lock_mode(self):
        r"""Gets the lock_mode of this MetaLockInfo.

        MDL锁等待模式

        :return: The lock_mode of this MetaLockInfo.
        :rtype: str
        """
        return self._lock_mode

    @lock_mode.setter
    def lock_mode(self, lock_mode):
        r"""Sets the lock_mode of this MetaLockInfo.

        MDL锁等待模式

        :param lock_mode: The lock_mode of this MetaLockInfo.
        :type lock_mode: str
        """
        self._lock_mode = lock_mode

    @property
    def lock_type(self):
        r"""Gets the lock_type of this MetaLockInfo.

        MDL锁等待信息

        :return: The lock_type of this MetaLockInfo.
        :rtype: str
        """
        return self._lock_type

    @lock_type.setter
    def lock_type(self, lock_type):
        r"""Sets the lock_type of this MetaLockInfo.

        MDL锁等待信息

        :param lock_type: The lock_type of this MetaLockInfo.
        :type lock_type: str
        """
        self._lock_type = lock_type

    @property
    def lock_duration(self):
        r"""Gets the lock_duration of this MetaLockInfo.

        MDL锁等待持续时间

        :return: The lock_duration of this MetaLockInfo.
        :rtype: str
        """
        return self._lock_duration

    @lock_duration.setter
    def lock_duration(self, lock_duration):
        r"""Sets the lock_duration of this MetaLockInfo.

        MDL锁等待持续时间

        :param lock_duration: The lock_duration of this MetaLockInfo.
        :type lock_duration: str
        """
        self._lock_duration = lock_duration

    @property
    def table_schema(self):
        r"""Gets the table_schema of this MetaLockInfo.

        库表schema信息

        :return: The table_schema of this MetaLockInfo.
        :rtype: str
        """
        return self._table_schema

    @table_schema.setter
    def table_schema(self, table_schema):
        r"""Sets the table_schema of this MetaLockInfo.

        库表schema信息

        :param table_schema: The table_schema of this MetaLockInfo.
        :type table_schema: str
        """
        self._table_schema = table_schema

    @property
    def table_name(self):
        r"""Gets the table_name of this MetaLockInfo.

        表名称

        :return: The table_name of this MetaLockInfo.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this MetaLockInfo.

        表名称

        :param table_name: The table_name of this MetaLockInfo.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def user(self):
        r"""Gets the user of this MetaLockInfo.

        用户名称

        :return: The user of this MetaLockInfo.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this MetaLockInfo.

        用户名称

        :param user: The user of this MetaLockInfo.
        :type user: str
        """
        self._user = user

    @property
    def time(self):
        r"""Gets the time of this MetaLockInfo.

        MDL锁等待时间

        :return: The time of this MetaLockInfo.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this MetaLockInfo.

        MDL锁等待时间

        :param time: The time of this MetaLockInfo.
        :type time: str
        """
        self._time = time

    @property
    def block_number(self):
        r"""Gets the block_number of this MetaLockInfo.

        MDL锁等待阻塞数量

        :return: The block_number of this MetaLockInfo.
        :rtype: int
        """
        return self._block_number

    @block_number.setter
    def block_number(self, block_number):
        r"""Sets the block_number of this MetaLockInfo.

        MDL锁等待阻塞数量

        :param block_number: The block_number of this MetaLockInfo.
        :type block_number: int
        """
        self._block_number = block_number

    @property
    def wait_number(self):
        r"""Gets the wait_number of this MetaLockInfo.

        MDL锁等待数量

        :return: The wait_number of this MetaLockInfo.
        :rtype: int
        """
        return self._wait_number

    @wait_number.setter
    def wait_number(self, wait_number):
        r"""Sets the wait_number of this MetaLockInfo.

        MDL锁等待数量

        :param wait_number: The wait_number of this MetaLockInfo.
        :type wait_number: int
        """
        self._wait_number = wait_number

    @property
    def host(self):
        r"""Gets the host of this MetaLockInfo.

        主机

        :return: The host of this MetaLockInfo.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this MetaLockInfo.

        主机

        :param host: The host of this MetaLockInfo.
        :type host: str
        """
        self._host = host

    @property
    def db_name(self):
        r"""Gets the db_name of this MetaLockInfo.

        数据库名称

        :return: The db_name of this MetaLockInfo.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this MetaLockInfo.

        数据库名称

        :param db_name: The db_name of this MetaLockInfo.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def command(self):
        r"""Gets the command of this MetaLockInfo.

        MDL锁等待SQL语句

        :return: The command of this MetaLockInfo.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this MetaLockInfo.

        MDL锁等待SQL语句

        :param command: The command of this MetaLockInfo.
        :type command: str
        """
        self._command = command

    @property
    def state(self):
        r"""Gets the state of this MetaLockInfo.

        MDL锁等待状态

        :return: The state of this MetaLockInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this MetaLockInfo.

        MDL锁等待状态

        :param state: The state of this MetaLockInfo.
        :type state: str
        """
        self._state = state

    @property
    def info(self):
        r"""Gets the info of this MetaLockInfo.

        MDL锁等待额外信息

        :return: The info of this MetaLockInfo.
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        r"""Sets the info of this MetaLockInfo.

        MDL锁等待额外信息

        :param info: The info of this MetaLockInfo.
        :type info: str
        """
        self._info = info

    @property
    def sql_limit_rule(self):
        r"""Gets the sql_limit_rule of this MetaLockInfo.

        关联的SQL限流规则

        :return: The sql_limit_rule of this MetaLockInfo.
        :rtype: str
        """
        return self._sql_limit_rule

    @sql_limit_rule.setter
    def sql_limit_rule(self, sql_limit_rule):
        r"""Sets the sql_limit_rule of this MetaLockInfo.

        关联的SQL限流规则

        :param sql_limit_rule: The sql_limit_rule of this MetaLockInfo.
        :type sql_limit_rule: str
        """
        self._sql_limit_rule = sql_limit_rule

    @property
    def trx_exec_time(self):
        r"""Gets the trx_exec_time of this MetaLockInfo.

        事务执行时间

        :return: The trx_exec_time of this MetaLockInfo.
        :rtype: str
        """
        return self._trx_exec_time

    @trx_exec_time.setter
    def trx_exec_time(self, trx_exec_time):
        r"""Sets the trx_exec_time of this MetaLockInfo.

        事务执行时间

        :param trx_exec_time: The trx_exec_time of this MetaLockInfo.
        :type trx_exec_time: str
        """
        self._trx_exec_time = trx_exec_time

    @property
    def block_process_info(self):
        r"""Gets the block_process_info of this MetaLockInfo.

        阻塞的事务信息列表

        :return: The block_process_info of this MetaLockInfo.
        :rtype: list[:class:`huaweicloudsdkdas.v3.ProcessInfo`]
        """
        return self._block_process_info

    @block_process_info.setter
    def block_process_info(self, block_process_info):
        r"""Sets the block_process_info of this MetaLockInfo.

        阻塞的事务信息列表

        :param block_process_info: The block_process_info of this MetaLockInfo.
        :type block_process_info: list[:class:`huaweicloudsdkdas.v3.ProcessInfo`]
        """
        self._block_process_info = block_process_info

    @property
    def wait_process_info(self):
        r"""Gets the wait_process_info of this MetaLockInfo.

        等待的事务信息列表

        :return: The wait_process_info of this MetaLockInfo.
        :rtype: list[:class:`huaweicloudsdkdas.v3.ProcessInfo`]
        """
        return self._wait_process_info

    @wait_process_info.setter
    def wait_process_info(self, wait_process_info):
        r"""Sets the wait_process_info of this MetaLockInfo.

        等待的事务信息列表

        :param wait_process_info: The wait_process_info of this MetaLockInfo.
        :type wait_process_info: list[:class:`huaweicloudsdkdas.v3.ProcessInfo`]
        """
        self._wait_process_info = wait_process_info

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
        if not isinstance(other, MetaLockInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
