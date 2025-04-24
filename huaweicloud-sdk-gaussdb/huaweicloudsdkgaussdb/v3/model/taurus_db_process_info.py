# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaurusDbProcessInfo:

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
        'time': 'int',
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
        r"""TaurusDbProcessInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释**：  用户会话线程ID。
        :type id: int
        :param user: **参数解释**：  启动用户会话线程的用户。 
        :type user: str
        :param host: **参数解释**：  发送请求的主机和端口。 
        :type host: str
        :param db: **参数解释**：  当前访问的数据库名。 
        :type db: str
        :param command: **参数解释**：  当前执行的命令。 
        :type command: str
        :param time: **参数解释**：  用户会话线程处于当前状态的持续时间，单位为秒。 
        :type time: int
        :param state: **参数解释**：  正在执行的SQL语句的当前状态。 
        :type state: str
        :param info: **参数解释**：  额外信息，通常是正在执行的语句。 
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

        self.id = id
        self.user = user
        self.host = host
        self.db = db
        self.command = command
        self.time = time
        self.state = state
        self.info = info

    @property
    def id(self):
        r"""Gets the id of this TaurusDbProcessInfo.

        **参数解释**：  用户会话线程ID。

        :return: The id of this TaurusDbProcessInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TaurusDbProcessInfo.

        **参数解释**：  用户会话线程ID。

        :param id: The id of this TaurusDbProcessInfo.
        :type id: int
        """
        self._id = id

    @property
    def user(self):
        r"""Gets the user of this TaurusDbProcessInfo.

        **参数解释**：  启动用户会话线程的用户。 

        :return: The user of this TaurusDbProcessInfo.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this TaurusDbProcessInfo.

        **参数解释**：  启动用户会话线程的用户。 

        :param user: The user of this TaurusDbProcessInfo.
        :type user: str
        """
        self._user = user

    @property
    def host(self):
        r"""Gets the host of this TaurusDbProcessInfo.

        **参数解释**：  发送请求的主机和端口。 

        :return: The host of this TaurusDbProcessInfo.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this TaurusDbProcessInfo.

        **参数解释**：  发送请求的主机和端口。 

        :param host: The host of this TaurusDbProcessInfo.
        :type host: str
        """
        self._host = host

    @property
    def db(self):
        r"""Gets the db of this TaurusDbProcessInfo.

        **参数解释**：  当前访问的数据库名。 

        :return: The db of this TaurusDbProcessInfo.
        :rtype: str
        """
        return self._db

    @db.setter
    def db(self, db):
        r"""Sets the db of this TaurusDbProcessInfo.

        **参数解释**：  当前访问的数据库名。 

        :param db: The db of this TaurusDbProcessInfo.
        :type db: str
        """
        self._db = db

    @property
    def command(self):
        r"""Gets the command of this TaurusDbProcessInfo.

        **参数解释**：  当前执行的命令。 

        :return: The command of this TaurusDbProcessInfo.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this TaurusDbProcessInfo.

        **参数解释**：  当前执行的命令。 

        :param command: The command of this TaurusDbProcessInfo.
        :type command: str
        """
        self._command = command

    @property
    def time(self):
        r"""Gets the time of this TaurusDbProcessInfo.

        **参数解释**：  用户会话线程处于当前状态的持续时间，单位为秒。 

        :return: The time of this TaurusDbProcessInfo.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this TaurusDbProcessInfo.

        **参数解释**：  用户会话线程处于当前状态的持续时间，单位为秒。 

        :param time: The time of this TaurusDbProcessInfo.
        :type time: int
        """
        self._time = time

    @property
    def state(self):
        r"""Gets the state of this TaurusDbProcessInfo.

        **参数解释**：  正在执行的SQL语句的当前状态。 

        :return: The state of this TaurusDbProcessInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this TaurusDbProcessInfo.

        **参数解释**：  正在执行的SQL语句的当前状态。 

        :param state: The state of this TaurusDbProcessInfo.
        :type state: str
        """
        self._state = state

    @property
    def info(self):
        r"""Gets the info of this TaurusDbProcessInfo.

        **参数解释**：  额外信息，通常是正在执行的语句。 

        :return: The info of this TaurusDbProcessInfo.
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        r"""Sets the info of this TaurusDbProcessInfo.

        **参数解释**：  额外信息，通常是正在执行的语句。 

        :param info: The info of this TaurusDbProcessInfo.
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
        if not isinstance(other, TaurusDbProcessInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
