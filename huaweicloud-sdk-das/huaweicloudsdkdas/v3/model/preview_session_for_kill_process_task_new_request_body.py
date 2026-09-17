# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PreviewSessionForKillProcessTaskNewRequestBody:

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
        'command': 'str',
        'time': 'int',
        'info': 'str',
        'task_duration': 'int',
        'task_type': 'str'
    }

    attribute_map = {
        'user': 'user',
        'host': 'host',
        'db': 'db',
        'command': 'command',
        'time': 'time',
        'info': 'info',
        'task_duration': 'task_duration',
        'task_type': 'task_type'
    }

    def __init__(self, user=None, host=None, db=None, command=None, time=None, info=None, task_duration=None, task_type=None):
        r"""PreviewSessionForKillProcessTaskNewRequestBody

        The model defined in huaweicloud sdk

        :param user: 数据库用户
        :type user: str
        :param host: 数据库主机
        :type host: str
        :param db: 数据库名称
        :type db: str
        :param command: 命令类型
        :type command: str
        :param time: 会话执行时间
        :type time: int
        :param info: SQL信息
        :type info: str
        :param task_duration: 任务持续时间
        :type task_duration: int
        :param task_type: 任务类型
        :type task_type: str
        """
        
        

        self._user = None
        self._host = None
        self._db = None
        self._command = None
        self._time = None
        self._info = None
        self._task_duration = None
        self._task_type = None
        self.discriminator = None

        if user is not None:
            self.user = user
        if host is not None:
            self.host = host
        if db is not None:
            self.db = db
        if command is not None:
            self.command = command
        self.time = time
        if info is not None:
            self.info = info
        self.task_duration = task_duration
        self.task_type = task_type

    @property
    def user(self):
        r"""Gets the user of this PreviewSessionForKillProcessTaskNewRequestBody.

        数据库用户

        :return: The user of this PreviewSessionForKillProcessTaskNewRequestBody.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this PreviewSessionForKillProcessTaskNewRequestBody.

        数据库用户

        :param user: The user of this PreviewSessionForKillProcessTaskNewRequestBody.
        :type user: str
        """
        self._user = user

    @property
    def host(self):
        r"""Gets the host of this PreviewSessionForKillProcessTaskNewRequestBody.

        数据库主机

        :return: The host of this PreviewSessionForKillProcessTaskNewRequestBody.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this PreviewSessionForKillProcessTaskNewRequestBody.

        数据库主机

        :param host: The host of this PreviewSessionForKillProcessTaskNewRequestBody.
        :type host: str
        """
        self._host = host

    @property
    def db(self):
        r"""Gets the db of this PreviewSessionForKillProcessTaskNewRequestBody.

        数据库名称

        :return: The db of this PreviewSessionForKillProcessTaskNewRequestBody.
        :rtype: str
        """
        return self._db

    @db.setter
    def db(self, db):
        r"""Sets the db of this PreviewSessionForKillProcessTaskNewRequestBody.

        数据库名称

        :param db: The db of this PreviewSessionForKillProcessTaskNewRequestBody.
        :type db: str
        """
        self._db = db

    @property
    def command(self):
        r"""Gets the command of this PreviewSessionForKillProcessTaskNewRequestBody.

        命令类型

        :return: The command of this PreviewSessionForKillProcessTaskNewRequestBody.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this PreviewSessionForKillProcessTaskNewRequestBody.

        命令类型

        :param command: The command of this PreviewSessionForKillProcessTaskNewRequestBody.
        :type command: str
        """
        self._command = command

    @property
    def time(self):
        r"""Gets the time of this PreviewSessionForKillProcessTaskNewRequestBody.

        会话执行时间

        :return: The time of this PreviewSessionForKillProcessTaskNewRequestBody.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this PreviewSessionForKillProcessTaskNewRequestBody.

        会话执行时间

        :param time: The time of this PreviewSessionForKillProcessTaskNewRequestBody.
        :type time: int
        """
        self._time = time

    @property
    def info(self):
        r"""Gets the info of this PreviewSessionForKillProcessTaskNewRequestBody.

        SQL信息

        :return: The info of this PreviewSessionForKillProcessTaskNewRequestBody.
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        r"""Sets the info of this PreviewSessionForKillProcessTaskNewRequestBody.

        SQL信息

        :param info: The info of this PreviewSessionForKillProcessTaskNewRequestBody.
        :type info: str
        """
        self._info = info

    @property
    def task_duration(self):
        r"""Gets the task_duration of this PreviewSessionForKillProcessTaskNewRequestBody.

        任务持续时间

        :return: The task_duration of this PreviewSessionForKillProcessTaskNewRequestBody.
        :rtype: int
        """
        return self._task_duration

    @task_duration.setter
    def task_duration(self, task_duration):
        r"""Sets the task_duration of this PreviewSessionForKillProcessTaskNewRequestBody.

        任务持续时间

        :param task_duration: The task_duration of this PreviewSessionForKillProcessTaskNewRequestBody.
        :type task_duration: int
        """
        self._task_duration = task_duration

    @property
    def task_type(self):
        r"""Gets the task_type of this PreviewSessionForKillProcessTaskNewRequestBody.

        任务类型

        :return: The task_type of this PreviewSessionForKillProcessTaskNewRequestBody.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this PreviewSessionForKillProcessTaskNewRequestBody.

        任务类型

        :param task_type: The task_type of this PreviewSessionForKillProcessTaskNewRequestBody.
        :type task_type: str
        """
        self._task_type = task_type

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
        if not isinstance(other, PreviewSessionForKillProcessTaskNewRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
