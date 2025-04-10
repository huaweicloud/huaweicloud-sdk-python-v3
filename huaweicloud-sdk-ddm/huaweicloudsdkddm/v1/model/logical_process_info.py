# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogicalProcessInfo:

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
        'info': 'str'
    }

    attribute_map = {
        'id': 'id',
        'user': 'user',
        'host': 'host',
        'db': 'db',
        'command': 'command',
        'time': 'time',
        'state': 'state',
        'info': 'info'
    }

    def __init__(self, id=None, user=None, host=None, db=None, command=None, time=None, state=None, info=None):
        r"""LogicalProcessInfo

        The model defined in huaweicloud sdk

        :param id: 会话id
        :type id: str
        :param user: 当前连接用户
        :type user: str
        :param host: 所属的 IP 和端口
        :type host: str
        :param db: 数据库名
        :type db: str
        :param command: 连接状态，一般是休眠（sleep），查询（query），连接（connect）
        :type command: str
        :param time: 连接状态持续的时间，单位是秒（s）
        :type time: str
        :param state: 当前 SQL 语句的状态
        :type state: str
        :param info: 当前所执行的 SQL 语句
        :type info: str
        """
        
        

        self._id = None
        self._user = None
        self._host = None
        self._db = None
        self._command = None
        self._time = None
        self._state = None
        self._info = None
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

    @property
    def id(self):
        r"""Gets the id of this LogicalProcessInfo.

        会话id

        :return: The id of this LogicalProcessInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this LogicalProcessInfo.

        会话id

        :param id: The id of this LogicalProcessInfo.
        :type id: str
        """
        self._id = id

    @property
    def user(self):
        r"""Gets the user of this LogicalProcessInfo.

        当前连接用户

        :return: The user of this LogicalProcessInfo.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this LogicalProcessInfo.

        当前连接用户

        :param user: The user of this LogicalProcessInfo.
        :type user: str
        """
        self._user = user

    @property
    def host(self):
        r"""Gets the host of this LogicalProcessInfo.

        所属的 IP 和端口

        :return: The host of this LogicalProcessInfo.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this LogicalProcessInfo.

        所属的 IP 和端口

        :param host: The host of this LogicalProcessInfo.
        :type host: str
        """
        self._host = host

    @property
    def db(self):
        r"""Gets the db of this LogicalProcessInfo.

        数据库名

        :return: The db of this LogicalProcessInfo.
        :rtype: str
        """
        return self._db

    @db.setter
    def db(self, db):
        r"""Sets the db of this LogicalProcessInfo.

        数据库名

        :param db: The db of this LogicalProcessInfo.
        :type db: str
        """
        self._db = db

    @property
    def command(self):
        r"""Gets the command of this LogicalProcessInfo.

        连接状态，一般是休眠（sleep），查询（query），连接（connect）

        :return: The command of this LogicalProcessInfo.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this LogicalProcessInfo.

        连接状态，一般是休眠（sleep），查询（query），连接（connect）

        :param command: The command of this LogicalProcessInfo.
        :type command: str
        """
        self._command = command

    @property
    def time(self):
        r"""Gets the time of this LogicalProcessInfo.

        连接状态持续的时间，单位是秒（s）

        :return: The time of this LogicalProcessInfo.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this LogicalProcessInfo.

        连接状态持续的时间，单位是秒（s）

        :param time: The time of this LogicalProcessInfo.
        :type time: str
        """
        self._time = time

    @property
    def state(self):
        r"""Gets the state of this LogicalProcessInfo.

        当前 SQL 语句的状态

        :return: The state of this LogicalProcessInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this LogicalProcessInfo.

        当前 SQL 语句的状态

        :param state: The state of this LogicalProcessInfo.
        :type state: str
        """
        self._state = state

    @property
    def info(self):
        r"""Gets the info of this LogicalProcessInfo.

        当前所执行的 SQL 语句

        :return: The info of this LogicalProcessInfo.
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        r"""Sets the info of this LogicalProcessInfo.

        当前所执行的 SQL 语句

        :param info: The info of this LogicalProcessInfo.
        :type info: str
        """
        self._info = info

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
        if not isinstance(other, LogicalProcessInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
