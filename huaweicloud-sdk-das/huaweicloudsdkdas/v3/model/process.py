# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Process:

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
        'database': 'str',
        'command': 'str',
        'time': 'str',
        'state': 'str',
        'sql': 'str',
        'trx_executed_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'user': 'user',
        'host': 'host',
        'database': 'database',
        'command': 'command',
        'time': 'time',
        'state': 'state',
        'sql': 'sql',
        'trx_executed_time': 'trx_executed_time'
    }

    def __init__(self, id=None, user=None, host=None, database=None, command=None, time=None, state=None, sql=None, trx_executed_time=None):
        r"""Process

        The model defined in huaweicloud sdk

        :param id: 会话ID
        :type id: str
        :param user: 用户
        :type user: str
        :param host: 主机
        :type host: str
        :param database: 数据库
        :type database: str
        :param command: 命令
        :type command: str
        :param time: 会话持续时间
        :type time: str
        :param state: 状态
        :type state: str
        :param sql: SQL语句
        :type sql: str
        :param trx_executed_time: 事务持续时间
        :type trx_executed_time: str
        """
        
        

        self._id = None
        self._user = None
        self._host = None
        self._database = None
        self._command = None
        self._time = None
        self._state = None
        self._sql = None
        self._trx_executed_time = None
        self.discriminator = None

        self.id = id
        self.user = user
        self.host = host
        self.database = database
        self.command = command
        self.time = time
        self.state = state
        self.sql = sql
        self.trx_executed_time = trx_executed_time

    @property
    def id(self):
        r"""Gets the id of this Process.

        会话ID

        :return: The id of this Process.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Process.

        会话ID

        :param id: The id of this Process.
        :type id: str
        """
        self._id = id

    @property
    def user(self):
        r"""Gets the user of this Process.

        用户

        :return: The user of this Process.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this Process.

        用户

        :param user: The user of this Process.
        :type user: str
        """
        self._user = user

    @property
    def host(self):
        r"""Gets the host of this Process.

        主机

        :return: The host of this Process.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this Process.

        主机

        :param host: The host of this Process.
        :type host: str
        """
        self._host = host

    @property
    def database(self):
        r"""Gets the database of this Process.

        数据库

        :return: The database of this Process.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this Process.

        数据库

        :param database: The database of this Process.
        :type database: str
        """
        self._database = database

    @property
    def command(self):
        r"""Gets the command of this Process.

        命令

        :return: The command of this Process.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this Process.

        命令

        :param command: The command of this Process.
        :type command: str
        """
        self._command = command

    @property
    def time(self):
        r"""Gets the time of this Process.

        会话持续时间

        :return: The time of this Process.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this Process.

        会话持续时间

        :param time: The time of this Process.
        :type time: str
        """
        self._time = time

    @property
    def state(self):
        r"""Gets the state of this Process.

        状态

        :return: The state of this Process.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this Process.

        状态

        :param state: The state of this Process.
        :type state: str
        """
        self._state = state

    @property
    def sql(self):
        r"""Gets the sql of this Process.

        SQL语句

        :return: The sql of this Process.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this Process.

        SQL语句

        :param sql: The sql of this Process.
        :type sql: str
        """
        self._sql = sql

    @property
    def trx_executed_time(self):
        r"""Gets the trx_executed_time of this Process.

        事务持续时间

        :return: The trx_executed_time of this Process.
        :rtype: str
        """
        return self._trx_executed_time

    @trx_executed_time.setter
    def trx_executed_time(self, trx_executed_time):
        r"""Sets the trx_executed_time of this Process.

        事务持续时间

        :param trx_executed_time: The trx_executed_time of this Process.
        :type trx_executed_time: str
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
        if not isinstance(other, Process):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
