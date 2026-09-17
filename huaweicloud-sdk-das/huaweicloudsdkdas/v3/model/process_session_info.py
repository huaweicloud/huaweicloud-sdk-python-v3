# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProcessSessionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'user': 'str',
        'host': 'str',
        'db': 'str',
        'command': 'str',
        'sql_info': 'str',
        'state_duration': 'int',
        'state': 'str'
    }

    attribute_map = {
        'id': 'id',
        'user': 'user',
        'host': 'host',
        'db': 'db',
        'command': 'command',
        'sql_info': 'sql_info',
        'state_duration': 'state_duration',
        'state': 'state'
    }

    def __init__(self, id=None, user=None, host=None, db=None, command=None, sql_info=None, state_duration=None, state=None):
        r"""ProcessSessionInfo

        The model defined in huaweicloud sdk

        :param id: 会话ID
        :type id: int
        :param user: 数据库用户
        :type user: str
        :param host: 数据库主机
        :type host: str
        :param db: 数据库名称
        :type db: str
        :param command: 命令类型
        :type command: str
        :param sql_info: SQL信息
        :type sql_info: str
        :param state_duration: 当前状态持续时间
        :type state_duration: int
        :param state: 当前状态
        :type state: str
        """
        
        

        self._id = None
        self._user = None
        self._host = None
        self._db = None
        self._command = None
        self._sql_info = None
        self._state_duration = None
        self._state = None
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
        if sql_info is not None:
            self.sql_info = sql_info
        if state_duration is not None:
            self.state_duration = state_duration
        if state is not None:
            self.state = state

    @property
    def id(self):
        r"""Gets the id of this ProcessSessionInfo.

        会话ID

        :return: The id of this ProcessSessionInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ProcessSessionInfo.

        会话ID

        :param id: The id of this ProcessSessionInfo.
        :type id: int
        """
        self._id = id

    @property
    def user(self):
        r"""Gets the user of this ProcessSessionInfo.

        数据库用户

        :return: The user of this ProcessSessionInfo.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this ProcessSessionInfo.

        数据库用户

        :param user: The user of this ProcessSessionInfo.
        :type user: str
        """
        self._user = user

    @property
    def host(self):
        r"""Gets the host of this ProcessSessionInfo.

        数据库主机

        :return: The host of this ProcessSessionInfo.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this ProcessSessionInfo.

        数据库主机

        :param host: The host of this ProcessSessionInfo.
        :type host: str
        """
        self._host = host

    @property
    def db(self):
        r"""Gets the db of this ProcessSessionInfo.

        数据库名称

        :return: The db of this ProcessSessionInfo.
        :rtype: str
        """
        return self._db

    @db.setter
    def db(self, db):
        r"""Sets the db of this ProcessSessionInfo.

        数据库名称

        :param db: The db of this ProcessSessionInfo.
        :type db: str
        """
        self._db = db

    @property
    def command(self):
        r"""Gets the command of this ProcessSessionInfo.

        命令类型

        :return: The command of this ProcessSessionInfo.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this ProcessSessionInfo.

        命令类型

        :param command: The command of this ProcessSessionInfo.
        :type command: str
        """
        self._command = command

    @property
    def sql_info(self):
        r"""Gets the sql_info of this ProcessSessionInfo.

        SQL信息

        :return: The sql_info of this ProcessSessionInfo.
        :rtype: str
        """
        return self._sql_info

    @sql_info.setter
    def sql_info(self, sql_info):
        r"""Sets the sql_info of this ProcessSessionInfo.

        SQL信息

        :param sql_info: The sql_info of this ProcessSessionInfo.
        :type sql_info: str
        """
        self._sql_info = sql_info

    @property
    def state_duration(self):
        r"""Gets the state_duration of this ProcessSessionInfo.

        当前状态持续时间

        :return: The state_duration of this ProcessSessionInfo.
        :rtype: int
        """
        return self._state_duration

    @state_duration.setter
    def state_duration(self, state_duration):
        r"""Sets the state_duration of this ProcessSessionInfo.

        当前状态持续时间

        :param state_duration: The state_duration of this ProcessSessionInfo.
        :type state_duration: int
        """
        self._state_duration = state_duration

    @property
    def state(self):
        r"""Gets the state of this ProcessSessionInfo.

        当前状态

        :return: The state of this ProcessSessionInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ProcessSessionInfo.

        当前状态

        :param state: The state of this ProcessSessionInfo.
        :type state: str
        """
        self._state = state

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
        if not isinstance(other, ProcessSessionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
