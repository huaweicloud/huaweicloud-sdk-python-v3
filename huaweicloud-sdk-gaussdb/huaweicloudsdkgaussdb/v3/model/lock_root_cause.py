# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LockRootCause:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'locked_pid': 'int',
        'locked_sql': 'str',
        'wait_seconds': 'int',
        'lock_db': 'str',
        'lock_table': 'str',
        'lock_index': 'str',
        'lock_mode': 'str',
        'lock_data': 'str',
        'blocker_pid': 'int',
        'blocker_state': 'str',
        'blocker_age': 'int',
        'blocker_rows_locked': 'int',
        'blocker_rows_modified': 'int',
        'blocker_current_sql': 'list[str]',
        'blocker_host': 'str',
        'blocker_command': 'str',
        'blocker_thread_id': 'int'
    }

    attribute_map = {
        'locked_pid': 'locked_pid',
        'locked_sql': 'locked_sql',
        'wait_seconds': 'wait_seconds',
        'lock_db': 'lock_db',
        'lock_table': 'lock_table',
        'lock_index': 'lock_index',
        'lock_mode': 'lock_mode',
        'lock_data': 'lock_data',
        'blocker_pid': 'blocker_pid',
        'blocker_state': 'blocker_state',
        'blocker_age': 'blocker_age',
        'blocker_rows_locked': 'blocker_rows_locked',
        'blocker_rows_modified': 'blocker_rows_modified',
        'blocker_current_sql': 'blocker_current_sql',
        'blocker_host': 'blocker_host',
        'blocker_command': 'blocker_command',
        'blocker_thread_id': 'blocker_thread_id'
    }

    def __init__(self, locked_pid=None, locked_sql=None, wait_seconds=None, lock_db=None, lock_table=None, lock_index=None, lock_mode=None, lock_data=None, blocker_pid=None, blocker_state=None, blocker_age=None, blocker_rows_locked=None, blocker_rows_modified=None, blocker_current_sql=None, blocker_host=None, blocker_command=None, blocker_thread_id=None):
        r"""LockRootCause

        The model defined in huaweicloud sdk

        :param locked_pid: **参数解释**： 被锁会话ID。 **取值范围**： 不涉及。 
        :type locked_pid: int
        :param locked_sql: **参数解释**： 被锁会话当前执行的SQL。 **取值范围**： 不涉及。 
        :type locked_sql: str
        :param wait_seconds: **参数解释**： 等待持续时间（秒）。 **取值范围**： 不涉及。 
        :type wait_seconds: int
        :param lock_db: **参数解释**： 锁所在数据库。 **取值范围**： 不涉及。 
        :type lock_db: str
        :param lock_table: **参数解释**： 锁所在表。 **取值范围**： 不涉及。 
        :type lock_table: str
        :param lock_index: **参数解释**： 锁所在索引。 **取值范围**： 不涉及。 
        :type lock_index: str
        :param lock_mode: **参数解释**： 锁模式。 **取值范围**： - IX：表级排他锁。 - X,REC_NOT_GAP：排他记录锁。 - X,GAP：间隙锁。 - X：行级排他锁。 
        :type lock_mode: str
        :param lock_data: **参数解释**： 锁住的具体数据行的标识。 **取值范围**： 不涉及。 
        :type lock_data: str
        :param blocker_pid: **参数解释**： 阻塞源会话ID。 **取值范围**： 不涉及。 
        :type blocker_pid: int
        :param blocker_state: **参数解释**： 阻塞源事务状态。 **取值范围**： - RUNNING：运行中。 - LOCK WAIT：锁等待。 - ROLLING BACK：回滚中。 - COMMITTING：提交中。 
        :type blocker_state: str
        :param blocker_age: **参数解释**： 阻塞源事务持续时间（秒）。 **取值范围**： 不涉及。 
        :type blocker_age: int
        :param blocker_rows_locked: **参数解释**： 阻塞源锁定的行数。 **取值范围**： 不涉及。 
        :type blocker_rows_locked: int
        :param blocker_rows_modified: **参数解释**： 阻塞源修改的行数。 **取值范围**： 不涉及。 
        :type blocker_rows_modified: int
        :param blocker_current_sql: **参数解释**： 阻塞源当前执行的SQL列表。 
        :type blocker_current_sql: list[str]
        :param blocker_host: **参数解释**： 阻塞源主机。 **取值范围**： 不涉及。 
        :type blocker_host: str
        :param blocker_command: **参数解释**： 阻塞源命令。 **取值范围**： 不涉及。 
        :type blocker_command: str
        :param blocker_thread_id: **参数解释**： 阻塞源线程ID。 **取值范围**： 不涉及。 
        :type blocker_thread_id: int
        """
        
        

        self._locked_pid = None
        self._locked_sql = None
        self._wait_seconds = None
        self._lock_db = None
        self._lock_table = None
        self._lock_index = None
        self._lock_mode = None
        self._lock_data = None
        self._blocker_pid = None
        self._blocker_state = None
        self._blocker_age = None
        self._blocker_rows_locked = None
        self._blocker_rows_modified = None
        self._blocker_current_sql = None
        self._blocker_host = None
        self._blocker_command = None
        self._blocker_thread_id = None
        self.discriminator = None

        if locked_pid is not None:
            self.locked_pid = locked_pid
        if locked_sql is not None:
            self.locked_sql = locked_sql
        if wait_seconds is not None:
            self.wait_seconds = wait_seconds
        if lock_db is not None:
            self.lock_db = lock_db
        if lock_table is not None:
            self.lock_table = lock_table
        if lock_index is not None:
            self.lock_index = lock_index
        if lock_mode is not None:
            self.lock_mode = lock_mode
        if lock_data is not None:
            self.lock_data = lock_data
        if blocker_pid is not None:
            self.blocker_pid = blocker_pid
        if blocker_state is not None:
            self.blocker_state = blocker_state
        if blocker_age is not None:
            self.blocker_age = blocker_age
        if blocker_rows_locked is not None:
            self.blocker_rows_locked = blocker_rows_locked
        if blocker_rows_modified is not None:
            self.blocker_rows_modified = blocker_rows_modified
        if blocker_current_sql is not None:
            self.blocker_current_sql = blocker_current_sql
        if blocker_host is not None:
            self.blocker_host = blocker_host
        if blocker_command is not None:
            self.blocker_command = blocker_command
        if blocker_thread_id is not None:
            self.blocker_thread_id = blocker_thread_id

    @property
    def locked_pid(self):
        r"""Gets the locked_pid of this LockRootCause.

        **参数解释**： 被锁会话ID。 **取值范围**： 不涉及。 

        :return: The locked_pid of this LockRootCause.
        :rtype: int
        """
        return self._locked_pid

    @locked_pid.setter
    def locked_pid(self, locked_pid):
        r"""Sets the locked_pid of this LockRootCause.

        **参数解释**： 被锁会话ID。 **取值范围**： 不涉及。 

        :param locked_pid: The locked_pid of this LockRootCause.
        :type locked_pid: int
        """
        self._locked_pid = locked_pid

    @property
    def locked_sql(self):
        r"""Gets the locked_sql of this LockRootCause.

        **参数解释**： 被锁会话当前执行的SQL。 **取值范围**： 不涉及。 

        :return: The locked_sql of this LockRootCause.
        :rtype: str
        """
        return self._locked_sql

    @locked_sql.setter
    def locked_sql(self, locked_sql):
        r"""Sets the locked_sql of this LockRootCause.

        **参数解释**： 被锁会话当前执行的SQL。 **取值范围**： 不涉及。 

        :param locked_sql: The locked_sql of this LockRootCause.
        :type locked_sql: str
        """
        self._locked_sql = locked_sql

    @property
    def wait_seconds(self):
        r"""Gets the wait_seconds of this LockRootCause.

        **参数解释**： 等待持续时间（秒）。 **取值范围**： 不涉及。 

        :return: The wait_seconds of this LockRootCause.
        :rtype: int
        """
        return self._wait_seconds

    @wait_seconds.setter
    def wait_seconds(self, wait_seconds):
        r"""Sets the wait_seconds of this LockRootCause.

        **参数解释**： 等待持续时间（秒）。 **取值范围**： 不涉及。 

        :param wait_seconds: The wait_seconds of this LockRootCause.
        :type wait_seconds: int
        """
        self._wait_seconds = wait_seconds

    @property
    def lock_db(self):
        r"""Gets the lock_db of this LockRootCause.

        **参数解释**： 锁所在数据库。 **取值范围**： 不涉及。 

        :return: The lock_db of this LockRootCause.
        :rtype: str
        """
        return self._lock_db

    @lock_db.setter
    def lock_db(self, lock_db):
        r"""Sets the lock_db of this LockRootCause.

        **参数解释**： 锁所在数据库。 **取值范围**： 不涉及。 

        :param lock_db: The lock_db of this LockRootCause.
        :type lock_db: str
        """
        self._lock_db = lock_db

    @property
    def lock_table(self):
        r"""Gets the lock_table of this LockRootCause.

        **参数解释**： 锁所在表。 **取值范围**： 不涉及。 

        :return: The lock_table of this LockRootCause.
        :rtype: str
        """
        return self._lock_table

    @lock_table.setter
    def lock_table(self, lock_table):
        r"""Sets the lock_table of this LockRootCause.

        **参数解释**： 锁所在表。 **取值范围**： 不涉及。 

        :param lock_table: The lock_table of this LockRootCause.
        :type lock_table: str
        """
        self._lock_table = lock_table

    @property
    def lock_index(self):
        r"""Gets the lock_index of this LockRootCause.

        **参数解释**： 锁所在索引。 **取值范围**： 不涉及。 

        :return: The lock_index of this LockRootCause.
        :rtype: str
        """
        return self._lock_index

    @lock_index.setter
    def lock_index(self, lock_index):
        r"""Sets the lock_index of this LockRootCause.

        **参数解释**： 锁所在索引。 **取值范围**： 不涉及。 

        :param lock_index: The lock_index of this LockRootCause.
        :type lock_index: str
        """
        self._lock_index = lock_index

    @property
    def lock_mode(self):
        r"""Gets the lock_mode of this LockRootCause.

        **参数解释**： 锁模式。 **取值范围**： - IX：表级排他锁。 - X,REC_NOT_GAP：排他记录锁。 - X,GAP：间隙锁。 - X：行级排他锁。 

        :return: The lock_mode of this LockRootCause.
        :rtype: str
        """
        return self._lock_mode

    @lock_mode.setter
    def lock_mode(self, lock_mode):
        r"""Sets the lock_mode of this LockRootCause.

        **参数解释**： 锁模式。 **取值范围**： - IX：表级排他锁。 - X,REC_NOT_GAP：排他记录锁。 - X,GAP：间隙锁。 - X：行级排他锁。 

        :param lock_mode: The lock_mode of this LockRootCause.
        :type lock_mode: str
        """
        self._lock_mode = lock_mode

    @property
    def lock_data(self):
        r"""Gets the lock_data of this LockRootCause.

        **参数解释**： 锁住的具体数据行的标识。 **取值范围**： 不涉及。 

        :return: The lock_data of this LockRootCause.
        :rtype: str
        """
        return self._lock_data

    @lock_data.setter
    def lock_data(self, lock_data):
        r"""Sets the lock_data of this LockRootCause.

        **参数解释**： 锁住的具体数据行的标识。 **取值范围**： 不涉及。 

        :param lock_data: The lock_data of this LockRootCause.
        :type lock_data: str
        """
        self._lock_data = lock_data

    @property
    def blocker_pid(self):
        r"""Gets the blocker_pid of this LockRootCause.

        **参数解释**： 阻塞源会话ID。 **取值范围**： 不涉及。 

        :return: The blocker_pid of this LockRootCause.
        :rtype: int
        """
        return self._blocker_pid

    @blocker_pid.setter
    def blocker_pid(self, blocker_pid):
        r"""Sets the blocker_pid of this LockRootCause.

        **参数解释**： 阻塞源会话ID。 **取值范围**： 不涉及。 

        :param blocker_pid: The blocker_pid of this LockRootCause.
        :type blocker_pid: int
        """
        self._blocker_pid = blocker_pid

    @property
    def blocker_state(self):
        r"""Gets the blocker_state of this LockRootCause.

        **参数解释**： 阻塞源事务状态。 **取值范围**： - RUNNING：运行中。 - LOCK WAIT：锁等待。 - ROLLING BACK：回滚中。 - COMMITTING：提交中。 

        :return: The blocker_state of this LockRootCause.
        :rtype: str
        """
        return self._blocker_state

    @blocker_state.setter
    def blocker_state(self, blocker_state):
        r"""Sets the blocker_state of this LockRootCause.

        **参数解释**： 阻塞源事务状态。 **取值范围**： - RUNNING：运行中。 - LOCK WAIT：锁等待。 - ROLLING BACK：回滚中。 - COMMITTING：提交中。 

        :param blocker_state: The blocker_state of this LockRootCause.
        :type blocker_state: str
        """
        self._blocker_state = blocker_state

    @property
    def blocker_age(self):
        r"""Gets the blocker_age of this LockRootCause.

        **参数解释**： 阻塞源事务持续时间（秒）。 **取值范围**： 不涉及。 

        :return: The blocker_age of this LockRootCause.
        :rtype: int
        """
        return self._blocker_age

    @blocker_age.setter
    def blocker_age(self, blocker_age):
        r"""Sets the blocker_age of this LockRootCause.

        **参数解释**： 阻塞源事务持续时间（秒）。 **取值范围**： 不涉及。 

        :param blocker_age: The blocker_age of this LockRootCause.
        :type blocker_age: int
        """
        self._blocker_age = blocker_age

    @property
    def blocker_rows_locked(self):
        r"""Gets the blocker_rows_locked of this LockRootCause.

        **参数解释**： 阻塞源锁定的行数。 **取值范围**： 不涉及。 

        :return: The blocker_rows_locked of this LockRootCause.
        :rtype: int
        """
        return self._blocker_rows_locked

    @blocker_rows_locked.setter
    def blocker_rows_locked(self, blocker_rows_locked):
        r"""Sets the blocker_rows_locked of this LockRootCause.

        **参数解释**： 阻塞源锁定的行数。 **取值范围**： 不涉及。 

        :param blocker_rows_locked: The blocker_rows_locked of this LockRootCause.
        :type blocker_rows_locked: int
        """
        self._blocker_rows_locked = blocker_rows_locked

    @property
    def blocker_rows_modified(self):
        r"""Gets the blocker_rows_modified of this LockRootCause.

        **参数解释**： 阻塞源修改的行数。 **取值范围**： 不涉及。 

        :return: The blocker_rows_modified of this LockRootCause.
        :rtype: int
        """
        return self._blocker_rows_modified

    @blocker_rows_modified.setter
    def blocker_rows_modified(self, blocker_rows_modified):
        r"""Sets the blocker_rows_modified of this LockRootCause.

        **参数解释**： 阻塞源修改的行数。 **取值范围**： 不涉及。 

        :param blocker_rows_modified: The blocker_rows_modified of this LockRootCause.
        :type blocker_rows_modified: int
        """
        self._blocker_rows_modified = blocker_rows_modified

    @property
    def blocker_current_sql(self):
        r"""Gets the blocker_current_sql of this LockRootCause.

        **参数解释**： 阻塞源当前执行的SQL列表。 

        :return: The blocker_current_sql of this LockRootCause.
        :rtype: list[str]
        """
        return self._blocker_current_sql

    @blocker_current_sql.setter
    def blocker_current_sql(self, blocker_current_sql):
        r"""Sets the blocker_current_sql of this LockRootCause.

        **参数解释**： 阻塞源当前执行的SQL列表。 

        :param blocker_current_sql: The blocker_current_sql of this LockRootCause.
        :type blocker_current_sql: list[str]
        """
        self._blocker_current_sql = blocker_current_sql

    @property
    def blocker_host(self):
        r"""Gets the blocker_host of this LockRootCause.

        **参数解释**： 阻塞源主机。 **取值范围**： 不涉及。 

        :return: The blocker_host of this LockRootCause.
        :rtype: str
        """
        return self._blocker_host

    @blocker_host.setter
    def blocker_host(self, blocker_host):
        r"""Sets the blocker_host of this LockRootCause.

        **参数解释**： 阻塞源主机。 **取值范围**： 不涉及。 

        :param blocker_host: The blocker_host of this LockRootCause.
        :type blocker_host: str
        """
        self._blocker_host = blocker_host

    @property
    def blocker_command(self):
        r"""Gets the blocker_command of this LockRootCause.

        **参数解释**： 阻塞源命令。 **取值范围**： 不涉及。 

        :return: The blocker_command of this LockRootCause.
        :rtype: str
        """
        return self._blocker_command

    @blocker_command.setter
    def blocker_command(self, blocker_command):
        r"""Sets the blocker_command of this LockRootCause.

        **参数解释**： 阻塞源命令。 **取值范围**： 不涉及。 

        :param blocker_command: The blocker_command of this LockRootCause.
        :type blocker_command: str
        """
        self._blocker_command = blocker_command

    @property
    def blocker_thread_id(self):
        r"""Gets the blocker_thread_id of this LockRootCause.

        **参数解释**： 阻塞源线程ID。 **取值范围**： 不涉及。 

        :return: The blocker_thread_id of this LockRootCause.
        :rtype: int
        """
        return self._blocker_thread_id

    @blocker_thread_id.setter
    def blocker_thread_id(self, blocker_thread_id):
        r"""Sets the blocker_thread_id of this LockRootCause.

        **参数解释**： 阻塞源线程ID。 **取值范围**： 不涉及。 

        :param blocker_thread_id: The blocker_thread_id of this LockRootCause.
        :type blocker_thread_id: int
        """
        self._blocker_thread_id = blocker_thread_id

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
        if not isinstance(other, LockRootCause):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
