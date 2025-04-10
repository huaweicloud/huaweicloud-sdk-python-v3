# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PhysicalProcessInfo:

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
        'state': 'str',
        'command': 'str',
        'info': 'str',
        'time': 'int',
        'trx_executed_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'user': 'user',
        'host': 'host',
        'db': 'db',
        'state': 'state',
        'command': 'command',
        'info': 'info',
        'time': 'time',
        'trx_executed_time': 'trx_executed_time'
    }

    def __init__(self, id=None, user=None, host=None, db=None, state=None, command=None, info=None, time=None, trx_executed_time=None):
        r"""PhysicalProcessInfo

        The model defined in huaweicloud sdk

        :param id: 会话id
        :type id: int
        :param user: 用户
        :type user: str
        :param host: 主机
        :type host: str
        :param db: 数据库
        :type db: str
        :param state: 状态
        :type state: str
        :param command: 连接状态，一般是休眠（sleep），查询（query），连接（connect）
        :type command: str
        :param info: 线程执行的 sql 语句
        :type info: str
        :param time: 会话持续时间，单位秒
        :type time: int
        :param trx_executed_time: 事务持续时间，单位秒
        :type trx_executed_time: int
        """
        
        

        self._id = None
        self._user = None
        self._host = None
        self._db = None
        self._state = None
        self._command = None
        self._info = None
        self._time = None
        self._trx_executed_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user is not None:
            self.user = user
        if host is not None:
            self.host = host
        if db is not None:
            self.db = db
        if state is not None:
            self.state = state
        if command is not None:
            self.command = command
        if info is not None:
            self.info = info
        if time is not None:
            self.time = time
        if trx_executed_time is not None:
            self.trx_executed_time = trx_executed_time

    @property
    def id(self):
        r"""Gets the id of this PhysicalProcessInfo.

        会话id

        :return: The id of this PhysicalProcessInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PhysicalProcessInfo.

        会话id

        :param id: The id of this PhysicalProcessInfo.
        :type id: int
        """
        self._id = id

    @property
    def user(self):
        r"""Gets the user of this PhysicalProcessInfo.

        用户

        :return: The user of this PhysicalProcessInfo.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this PhysicalProcessInfo.

        用户

        :param user: The user of this PhysicalProcessInfo.
        :type user: str
        """
        self._user = user

    @property
    def host(self):
        r"""Gets the host of this PhysicalProcessInfo.

        主机

        :return: The host of this PhysicalProcessInfo.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this PhysicalProcessInfo.

        主机

        :param host: The host of this PhysicalProcessInfo.
        :type host: str
        """
        self._host = host

    @property
    def db(self):
        r"""Gets the db of this PhysicalProcessInfo.

        数据库

        :return: The db of this PhysicalProcessInfo.
        :rtype: str
        """
        return self._db

    @db.setter
    def db(self, db):
        r"""Sets the db of this PhysicalProcessInfo.

        数据库

        :param db: The db of this PhysicalProcessInfo.
        :type db: str
        """
        self._db = db

    @property
    def state(self):
        r"""Gets the state of this PhysicalProcessInfo.

        状态

        :return: The state of this PhysicalProcessInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this PhysicalProcessInfo.

        状态

        :param state: The state of this PhysicalProcessInfo.
        :type state: str
        """
        self._state = state

    @property
    def command(self):
        r"""Gets the command of this PhysicalProcessInfo.

        连接状态，一般是休眠（sleep），查询（query），连接（connect）

        :return: The command of this PhysicalProcessInfo.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this PhysicalProcessInfo.

        连接状态，一般是休眠（sleep），查询（query），连接（connect）

        :param command: The command of this PhysicalProcessInfo.
        :type command: str
        """
        self._command = command

    @property
    def info(self):
        r"""Gets the info of this PhysicalProcessInfo.

        线程执行的 sql 语句

        :return: The info of this PhysicalProcessInfo.
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        r"""Sets the info of this PhysicalProcessInfo.

        线程执行的 sql 语句

        :param info: The info of this PhysicalProcessInfo.
        :type info: str
        """
        self._info = info

    @property
    def time(self):
        r"""Gets the time of this PhysicalProcessInfo.

        会话持续时间，单位秒

        :return: The time of this PhysicalProcessInfo.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this PhysicalProcessInfo.

        会话持续时间，单位秒

        :param time: The time of this PhysicalProcessInfo.
        :type time: int
        """
        self._time = time

    @property
    def trx_executed_time(self):
        r"""Gets the trx_executed_time of this PhysicalProcessInfo.

        事务持续时间，单位秒

        :return: The trx_executed_time of this PhysicalProcessInfo.
        :rtype: int
        """
        return self._trx_executed_time

    @trx_executed_time.setter
    def trx_executed_time(self, trx_executed_time):
        r"""Sets the trx_executed_time of this PhysicalProcessInfo.

        事务持续时间，单位秒

        :param trx_executed_time: The trx_executed_time of this PhysicalProcessInfo.
        :type trx_executed_time: int
        """
        self._trx_executed_time = trx_executed_time

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
        if not isinstance(other, PhysicalProcessInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
