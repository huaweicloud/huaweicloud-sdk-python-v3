# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlKillingTaskResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user': 'str',
        'host': 'str',
        'db': 'str',
        'info': 'str',
        'command': 'str',
        'time': 'int',
        'task_id': 'int',
        'task_type': 'str',
        'task_duration': 'int',
        'task_state': 'int',
        'start_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'user': 'user',
        'host': 'host',
        'db': 'db',
        'info': 'info',
        'command': 'command',
        'time': 'time',
        'task_id': 'task_id',
        'task_type': 'task_type',
        'task_duration': 'task_duration',
        'task_state': 'task_state',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, user=None, host=None, db=None, info=None, command=None, time=None, task_id=None, task_type=None, task_duration=None, task_state=None, start_time=None, end_time=None):
        r"""SqlKillingTaskResp

        The model defined in huaweicloud sdk

        :param user: 用户名
        :type user: str
        :param host: host地址
        :type host: str
        :param db: 数据库
        :type db: str
        :param info: 信息
        :type info: str
        :param command: 命令行
        :type command: str
        :param time: 次数
        :type time: int
        :param task_id: 任务ID
        :type task_id: int
        :param task_type: 任务类型
        :type task_type: str
        :param task_duration: 任务耗时
        :type task_duration: int
        :param task_state: 任务状态
        :type task_state: int
        :param start_time: 开始时间
        :type start_time: int
        :param end_time: 结束时间
        :type end_time: int
        """
        
        

        self._user = None
        self._host = None
        self._db = None
        self._info = None
        self._command = None
        self._time = None
        self._task_id = None
        self._task_type = None
        self._task_duration = None
        self._task_state = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if user is not None:
            self.user = user
        if host is not None:
            self.host = host
        if db is not None:
            self.db = db
        if info is not None:
            self.info = info
        if command is not None:
            self.command = command
        if time is not None:
            self.time = time
        if task_id is not None:
            self.task_id = task_id
        if task_type is not None:
            self.task_type = task_type
        if task_duration is not None:
            self.task_duration = task_duration
        if task_state is not None:
            self.task_state = task_state
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def user(self):
        r"""Gets the user of this SqlKillingTaskResp.

        用户名

        :return: The user of this SqlKillingTaskResp.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this SqlKillingTaskResp.

        用户名

        :param user: The user of this SqlKillingTaskResp.
        :type user: str
        """
        self._user = user

    @property
    def host(self):
        r"""Gets the host of this SqlKillingTaskResp.

        host地址

        :return: The host of this SqlKillingTaskResp.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this SqlKillingTaskResp.

        host地址

        :param host: The host of this SqlKillingTaskResp.
        :type host: str
        """
        self._host = host

    @property
    def db(self):
        r"""Gets the db of this SqlKillingTaskResp.

        数据库

        :return: The db of this SqlKillingTaskResp.
        :rtype: str
        """
        return self._db

    @db.setter
    def db(self, db):
        r"""Sets the db of this SqlKillingTaskResp.

        数据库

        :param db: The db of this SqlKillingTaskResp.
        :type db: str
        """
        self._db = db

    @property
    def info(self):
        r"""Gets the info of this SqlKillingTaskResp.

        信息

        :return: The info of this SqlKillingTaskResp.
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        r"""Sets the info of this SqlKillingTaskResp.

        信息

        :param info: The info of this SqlKillingTaskResp.
        :type info: str
        """
        self._info = info

    @property
    def command(self):
        r"""Gets the command of this SqlKillingTaskResp.

        命令行

        :return: The command of this SqlKillingTaskResp.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this SqlKillingTaskResp.

        命令行

        :param command: The command of this SqlKillingTaskResp.
        :type command: str
        """
        self._command = command

    @property
    def time(self):
        r"""Gets the time of this SqlKillingTaskResp.

        次数

        :return: The time of this SqlKillingTaskResp.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this SqlKillingTaskResp.

        次数

        :param time: The time of this SqlKillingTaskResp.
        :type time: int
        """
        self._time = time

    @property
    def task_id(self):
        r"""Gets the task_id of this SqlKillingTaskResp.

        任务ID

        :return: The task_id of this SqlKillingTaskResp.
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this SqlKillingTaskResp.

        任务ID

        :param task_id: The task_id of this SqlKillingTaskResp.
        :type task_id: int
        """
        self._task_id = task_id

    @property
    def task_type(self):
        r"""Gets the task_type of this SqlKillingTaskResp.

        任务类型

        :return: The task_type of this SqlKillingTaskResp.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this SqlKillingTaskResp.

        任务类型

        :param task_type: The task_type of this SqlKillingTaskResp.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def task_duration(self):
        r"""Gets the task_duration of this SqlKillingTaskResp.

        任务耗时

        :return: The task_duration of this SqlKillingTaskResp.
        :rtype: int
        """
        return self._task_duration

    @task_duration.setter
    def task_duration(self, task_duration):
        r"""Sets the task_duration of this SqlKillingTaskResp.

        任务耗时

        :param task_duration: The task_duration of this SqlKillingTaskResp.
        :type task_duration: int
        """
        self._task_duration = task_duration

    @property
    def task_state(self):
        r"""Gets the task_state of this SqlKillingTaskResp.

        任务状态

        :return: The task_state of this SqlKillingTaskResp.
        :rtype: int
        """
        return self._task_state

    @task_state.setter
    def task_state(self, task_state):
        r"""Sets the task_state of this SqlKillingTaskResp.

        任务状态

        :param task_state: The task_state of this SqlKillingTaskResp.
        :type task_state: int
        """
        self._task_state = task_state

    @property
    def start_time(self):
        r"""Gets the start_time of this SqlKillingTaskResp.

        开始时间

        :return: The start_time of this SqlKillingTaskResp.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this SqlKillingTaskResp.

        开始时间

        :param start_time: The start_time of this SqlKillingTaskResp.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this SqlKillingTaskResp.

        结束时间

        :return: The end_time of this SqlKillingTaskResp.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this SqlKillingTaskResp.

        结束时间

        :param end_time: The end_time of this SqlKillingTaskResp.
        :type end_time: int
        """
        self._end_time = end_time

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
        if not isinstance(other, SqlKillingTaskResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
