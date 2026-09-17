# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KillProcessHistoryInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'node_id': 'str',
        'task_id': 'int',
        'session_id': 'int',
        'user': 'str',
        'host': 'str',
        'db': 'str',
        'command': 'str',
        'time': 'int',
        'state': 'str',
        'info': 'str',
        'kill_time': 'int',
        'killed_source': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'node_id': 'node_id',
        'task_id': 'task_id',
        'session_id': 'session_id',
        'user': 'user',
        'host': 'host',
        'db': 'db',
        'command': 'command',
        'time': 'time',
        'state': 'state',
        'info': 'info',
        'kill_time': 'kill_time',
        'killed_source': 'killed_source'
    }

    def __init__(self, instance_id=None, node_id=None, task_id=None, session_id=None, user=None, host=None, db=None, command=None, time=None, state=None, info=None, kill_time=None, killed_source=None):
        r"""KillProcessHistoryInfo

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param node_id: 节点ID
        :type node_id: str
        :param task_id: 任务ID
        :type task_id: int
        :param session_id: 会话ID
        :type session_id: int
        :param user: 数据库用户
        :type user: str
        :param host: 数据库主机
        :type host: str
        :param db: 数据库名称
        :type db: str
        :param command: 命令类型
        :type command: str
        :param time: 执行时间
        :type time: int
        :param state: 状态
        :type state: str
        :param info: 信息
        :type info: str
        :param kill_time: Kill时间
        :type kill_time: int
        :param killed_source: 会话被查杀的来源
        :type killed_source: str
        """
        
        

        self._instance_id = None
        self._node_id = None
        self._task_id = None
        self._session_id = None
        self._user = None
        self._host = None
        self._db = None
        self._command = None
        self._time = None
        self._state = None
        self._info = None
        self._kill_time = None
        self._killed_source = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if node_id is not None:
            self.node_id = node_id
        if task_id is not None:
            self.task_id = task_id
        if session_id is not None:
            self.session_id = session_id
        if user is not None:
            self.user = user
        if host is not None:
            self.host = host
        if db is not None:
            self.db = db
        if command is not None:
            self.command = command
        if time is not None:
            self.time = time
        if state is not None:
            self.state = state
        if info is not None:
            self.info = info
        if kill_time is not None:
            self.kill_time = kill_time
        if killed_source is not None:
            self.killed_source = killed_source

    @property
    def instance_id(self):
        r"""Gets the instance_id of this KillProcessHistoryInfo.

        实例ID

        :return: The instance_id of this KillProcessHistoryInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this KillProcessHistoryInfo.

        实例ID

        :param instance_id: The instance_id of this KillProcessHistoryInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_id(self):
        r"""Gets the node_id of this KillProcessHistoryInfo.

        节点ID

        :return: The node_id of this KillProcessHistoryInfo.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this KillProcessHistoryInfo.

        节点ID

        :param node_id: The node_id of this KillProcessHistoryInfo.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def task_id(self):
        r"""Gets the task_id of this KillProcessHistoryInfo.

        任务ID

        :return: The task_id of this KillProcessHistoryInfo.
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this KillProcessHistoryInfo.

        任务ID

        :param task_id: The task_id of this KillProcessHistoryInfo.
        :type task_id: int
        """
        self._task_id = task_id

    @property
    def session_id(self):
        r"""Gets the session_id of this KillProcessHistoryInfo.

        会话ID

        :return: The session_id of this KillProcessHistoryInfo.
        :rtype: int
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this KillProcessHistoryInfo.

        会话ID

        :param session_id: The session_id of this KillProcessHistoryInfo.
        :type session_id: int
        """
        self._session_id = session_id

    @property
    def user(self):
        r"""Gets the user of this KillProcessHistoryInfo.

        数据库用户

        :return: The user of this KillProcessHistoryInfo.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this KillProcessHistoryInfo.

        数据库用户

        :param user: The user of this KillProcessHistoryInfo.
        :type user: str
        """
        self._user = user

    @property
    def host(self):
        r"""Gets the host of this KillProcessHistoryInfo.

        数据库主机

        :return: The host of this KillProcessHistoryInfo.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this KillProcessHistoryInfo.

        数据库主机

        :param host: The host of this KillProcessHistoryInfo.
        :type host: str
        """
        self._host = host

    @property
    def db(self):
        r"""Gets the db of this KillProcessHistoryInfo.

        数据库名称

        :return: The db of this KillProcessHistoryInfo.
        :rtype: str
        """
        return self._db

    @db.setter
    def db(self, db):
        r"""Sets the db of this KillProcessHistoryInfo.

        数据库名称

        :param db: The db of this KillProcessHistoryInfo.
        :type db: str
        """
        self._db = db

    @property
    def command(self):
        r"""Gets the command of this KillProcessHistoryInfo.

        命令类型

        :return: The command of this KillProcessHistoryInfo.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this KillProcessHistoryInfo.

        命令类型

        :param command: The command of this KillProcessHistoryInfo.
        :type command: str
        """
        self._command = command

    @property
    def time(self):
        r"""Gets the time of this KillProcessHistoryInfo.

        执行时间

        :return: The time of this KillProcessHistoryInfo.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this KillProcessHistoryInfo.

        执行时间

        :param time: The time of this KillProcessHistoryInfo.
        :type time: int
        """
        self._time = time

    @property
    def state(self):
        r"""Gets the state of this KillProcessHistoryInfo.

        状态

        :return: The state of this KillProcessHistoryInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this KillProcessHistoryInfo.

        状态

        :param state: The state of this KillProcessHistoryInfo.
        :type state: str
        """
        self._state = state

    @property
    def info(self):
        r"""Gets the info of this KillProcessHistoryInfo.

        信息

        :return: The info of this KillProcessHistoryInfo.
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        r"""Sets the info of this KillProcessHistoryInfo.

        信息

        :param info: The info of this KillProcessHistoryInfo.
        :type info: str
        """
        self._info = info

    @property
    def kill_time(self):
        r"""Gets the kill_time of this KillProcessHistoryInfo.

        Kill时间

        :return: The kill_time of this KillProcessHistoryInfo.
        :rtype: int
        """
        return self._kill_time

    @kill_time.setter
    def kill_time(self, kill_time):
        r"""Sets the kill_time of this KillProcessHistoryInfo.

        Kill时间

        :param kill_time: The kill_time of this KillProcessHistoryInfo.
        :type kill_time: int
        """
        self._kill_time = kill_time

    @property
    def killed_source(self):
        r"""Gets the killed_source of this KillProcessHistoryInfo.

        会话被查杀的来源

        :return: The killed_source of this KillProcessHistoryInfo.
        :rtype: str
        """
        return self._killed_source

    @killed_source.setter
    def killed_source(self, killed_source):
        r"""Sets the killed_source of this KillProcessHistoryInfo.

        会话被查杀的来源

        :param killed_source: The killed_source of this KillProcessHistoryInfo.
        :type killed_source: str
        """
        self._killed_source = killed_source

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
        if not isinstance(other, KillProcessHistoryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
