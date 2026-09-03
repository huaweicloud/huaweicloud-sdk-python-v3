# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProcessInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'user': 'str',
        'host': 'str',
        'db': 'str',
        'command': 'str',
        'time': 'str',
        'state': 'str',
        'info': 'str',
        'trx_duration': 'str'
    }

    attribute_map = {
        'id': 'id',
        'user': 'user',
        'host': 'host',
        'db': 'db',
        'command': 'command',
        'time': 'time',
        'state': 'state',
        'info': 'info',
        'trx_duration': 'trx_duration'
    }

    def __init__(self, id=None, user=None, host=None, db=None, command=None, time=None, state=None, info=None, trx_duration=None):
        r"""ProcessInfo

        The model defined in huaweicloud sdk

        :param id: 会话ID
        :type id: str
        :param user: 用户
        :type user: str
        :param host: 连接库的IP和port
        :type host: str
        :param db: 数据库
        :type db: str
        :param command: 当前执行的命令
        :type command: str
        :param time: 会话运行时间
        :type time: str
        :param state: 执行状态
        :type state: str
        :param info: 执行的SQL
        :type info: str
        :param trx_duration: 事务持续时间
        :type trx_duration: str
        """
        
        

        self._id = None
        self._user = None
        self._host = None
        self._db = None
        self._command = None
        self._time = None
        self._state = None
        self._info = None
        self._trx_duration = None
        self.discriminator = None

        if id is not None:
            self.id = id
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
        if trx_duration is not None:
            self.trx_duration = trx_duration

    @property
    def id(self):
        r"""Gets the id of this ProcessInfo.

        会话ID

        :return: The id of this ProcessInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ProcessInfo.

        会话ID

        :param id: The id of this ProcessInfo.
        :type id: str
        """
        self._id = id

    @property
    def user(self):
        r"""Gets the user of this ProcessInfo.

        用户

        :return: The user of this ProcessInfo.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this ProcessInfo.

        用户

        :param user: The user of this ProcessInfo.
        :type user: str
        """
        self._user = user

    @property
    def host(self):
        r"""Gets the host of this ProcessInfo.

        连接库的IP和port

        :return: The host of this ProcessInfo.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this ProcessInfo.

        连接库的IP和port

        :param host: The host of this ProcessInfo.
        :type host: str
        """
        self._host = host

    @property
    def db(self):
        r"""Gets the db of this ProcessInfo.

        数据库

        :return: The db of this ProcessInfo.
        :rtype: str
        """
        return self._db

    @db.setter
    def db(self, db):
        r"""Sets the db of this ProcessInfo.

        数据库

        :param db: The db of this ProcessInfo.
        :type db: str
        """
        self._db = db

    @property
    def command(self):
        r"""Gets the command of this ProcessInfo.

        当前执行的命令

        :return: The command of this ProcessInfo.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this ProcessInfo.

        当前执行的命令

        :param command: The command of this ProcessInfo.
        :type command: str
        """
        self._command = command

    @property
    def time(self):
        r"""Gets the time of this ProcessInfo.

        会话运行时间

        :return: The time of this ProcessInfo.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this ProcessInfo.

        会话运行时间

        :param time: The time of this ProcessInfo.
        :type time: str
        """
        self._time = time

    @property
    def state(self):
        r"""Gets the state of this ProcessInfo.

        执行状态

        :return: The state of this ProcessInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ProcessInfo.

        执行状态

        :param state: The state of this ProcessInfo.
        :type state: str
        """
        self._state = state

    @property
    def info(self):
        r"""Gets the info of this ProcessInfo.

        执行的SQL

        :return: The info of this ProcessInfo.
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        r"""Sets the info of this ProcessInfo.

        执行的SQL

        :param info: The info of this ProcessInfo.
        :type info: str
        """
        self._info = info

    @property
    def trx_duration(self):
        r"""Gets the trx_duration of this ProcessInfo.

        事务持续时间

        :return: The trx_duration of this ProcessInfo.
        :rtype: str
        """
        return self._trx_duration

    @trx_duration.setter
    def trx_duration(self, trx_duration):
        r"""Sets the trx_duration of this ProcessInfo.

        事务持续时间

        :param trx_duration: The trx_duration of this ProcessInfo.
        :type trx_duration: str
        """
        self._trx_duration = trx_duration

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
        if not isinstance(other, ProcessInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
