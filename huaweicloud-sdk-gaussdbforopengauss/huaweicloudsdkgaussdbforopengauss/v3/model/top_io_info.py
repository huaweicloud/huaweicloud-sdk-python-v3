# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopIoInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'thread_id': 'str',
        'thread_type': 'str',
        'disk_read_rate': 'int',
        'disk_write_rate': 'int',
        'session_id': 'str',
        'unique_sql_id': 'str',
        'database_name': 'str',
        'client_ip': 'str',
        'user_name': 'str',
        'state': 'str',
        'sql_start': 'int'
    }

    attribute_map = {
        'thread_id': 'thread_id',
        'thread_type': 'thread_type',
        'disk_read_rate': 'disk_read_rate',
        'disk_write_rate': 'disk_write_rate',
        'session_id': 'session_id',
        'unique_sql_id': 'unique_sql_id',
        'database_name': 'database_name',
        'client_ip': 'client_ip',
        'user_name': 'user_name',
        'state': 'state',
        'sql_start': 'sql_start'
    }

    def __init__(self, thread_id=None, thread_type=None, disk_read_rate=None, disk_write_rate=None, session_id=None, unique_sql_id=None, database_name=None, client_ip=None, user_name=None, state=None, sql_start=None):
        """TopIoInfo

        The model defined in huaweicloud sdk

        :param thread_id: 线程ID
        :type thread_id: str
        :param thread_type: 线程分类标识，取值：业务（worker）和后台（background）。需将GUC参数\&quot;enable_thread_pool\&quot;设置为on
        :type thread_type: str
        :param disk_read_rate: 从磁盘读取数据速率, 单位：KB/s
        :type disk_read_rate: int
        :param disk_write_rate: 写入磁盘数据速率, 单位：KB/s
        :type disk_write_rate: int
        :param session_id: 会话ID
        :type session_id: str
        :param unique_sql_id: SQL ID
        :type unique_sql_id: str
        :param database_name: 数据库
        :type database_name: str
        :param client_ip: 客户端IP
        :type client_ip: str
        :param user_name: 用户名
        :type user_name: str
        :param state: 状态
        :type state: str
        :param sql_start: 语句开始时间
        :type sql_start: int
        """
        
        

        self._thread_id = None
        self._thread_type = None
        self._disk_read_rate = None
        self._disk_write_rate = None
        self._session_id = None
        self._unique_sql_id = None
        self._database_name = None
        self._client_ip = None
        self._user_name = None
        self._state = None
        self._sql_start = None
        self.discriminator = None

        if thread_id is not None:
            self.thread_id = thread_id
        if thread_type is not None:
            self.thread_type = thread_type
        if disk_read_rate is not None:
            self.disk_read_rate = disk_read_rate
        if disk_write_rate is not None:
            self.disk_write_rate = disk_write_rate
        if session_id is not None:
            self.session_id = session_id
        if unique_sql_id is not None:
            self.unique_sql_id = unique_sql_id
        if database_name is not None:
            self.database_name = database_name
        if client_ip is not None:
            self.client_ip = client_ip
        if user_name is not None:
            self.user_name = user_name
        if state is not None:
            self.state = state
        if sql_start is not None:
            self.sql_start = sql_start

    @property
    def thread_id(self):
        """Gets the thread_id of this TopIoInfo.

        线程ID

        :return: The thread_id of this TopIoInfo.
        :rtype: str
        """
        return self._thread_id

    @thread_id.setter
    def thread_id(self, thread_id):
        """Sets the thread_id of this TopIoInfo.

        线程ID

        :param thread_id: The thread_id of this TopIoInfo.
        :type thread_id: str
        """
        self._thread_id = thread_id

    @property
    def thread_type(self):
        """Gets the thread_type of this TopIoInfo.

        线程分类标识，取值：业务（worker）和后台（background）。需将GUC参数\"enable_thread_pool\"设置为on

        :return: The thread_type of this TopIoInfo.
        :rtype: str
        """
        return self._thread_type

    @thread_type.setter
    def thread_type(self, thread_type):
        """Sets the thread_type of this TopIoInfo.

        线程分类标识，取值：业务（worker）和后台（background）。需将GUC参数\"enable_thread_pool\"设置为on

        :param thread_type: The thread_type of this TopIoInfo.
        :type thread_type: str
        """
        self._thread_type = thread_type

    @property
    def disk_read_rate(self):
        """Gets the disk_read_rate of this TopIoInfo.

        从磁盘读取数据速率, 单位：KB/s

        :return: The disk_read_rate of this TopIoInfo.
        :rtype: int
        """
        return self._disk_read_rate

    @disk_read_rate.setter
    def disk_read_rate(self, disk_read_rate):
        """Sets the disk_read_rate of this TopIoInfo.

        从磁盘读取数据速率, 单位：KB/s

        :param disk_read_rate: The disk_read_rate of this TopIoInfo.
        :type disk_read_rate: int
        """
        self._disk_read_rate = disk_read_rate

    @property
    def disk_write_rate(self):
        """Gets the disk_write_rate of this TopIoInfo.

        写入磁盘数据速率, 单位：KB/s

        :return: The disk_write_rate of this TopIoInfo.
        :rtype: int
        """
        return self._disk_write_rate

    @disk_write_rate.setter
    def disk_write_rate(self, disk_write_rate):
        """Sets the disk_write_rate of this TopIoInfo.

        写入磁盘数据速率, 单位：KB/s

        :param disk_write_rate: The disk_write_rate of this TopIoInfo.
        :type disk_write_rate: int
        """
        self._disk_write_rate = disk_write_rate

    @property
    def session_id(self):
        """Gets the session_id of this TopIoInfo.

        会话ID

        :return: The session_id of this TopIoInfo.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this TopIoInfo.

        会话ID

        :param session_id: The session_id of this TopIoInfo.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def unique_sql_id(self):
        """Gets the unique_sql_id of this TopIoInfo.

        SQL ID

        :return: The unique_sql_id of this TopIoInfo.
        :rtype: str
        """
        return self._unique_sql_id

    @unique_sql_id.setter
    def unique_sql_id(self, unique_sql_id):
        """Sets the unique_sql_id of this TopIoInfo.

        SQL ID

        :param unique_sql_id: The unique_sql_id of this TopIoInfo.
        :type unique_sql_id: str
        """
        self._unique_sql_id = unique_sql_id

    @property
    def database_name(self):
        """Gets the database_name of this TopIoInfo.

        数据库

        :return: The database_name of this TopIoInfo.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this TopIoInfo.

        数据库

        :param database_name: The database_name of this TopIoInfo.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def client_ip(self):
        """Gets the client_ip of this TopIoInfo.

        客户端IP

        :return: The client_ip of this TopIoInfo.
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        """Sets the client_ip of this TopIoInfo.

        客户端IP

        :param client_ip: The client_ip of this TopIoInfo.
        :type client_ip: str
        """
        self._client_ip = client_ip

    @property
    def user_name(self):
        """Gets the user_name of this TopIoInfo.

        用户名

        :return: The user_name of this TopIoInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this TopIoInfo.

        用户名

        :param user_name: The user_name of this TopIoInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def state(self):
        """Gets the state of this TopIoInfo.

        状态

        :return: The state of this TopIoInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TopIoInfo.

        状态

        :param state: The state of this TopIoInfo.
        :type state: str
        """
        self._state = state

    @property
    def sql_start(self):
        """Gets the sql_start of this TopIoInfo.

        语句开始时间

        :return: The sql_start of this TopIoInfo.
        :rtype: int
        """
        return self._sql_start

    @sql_start.setter
    def sql_start(self, sql_start):
        """Sets the sql_start of this TopIoInfo.

        语句开始时间

        :param sql_start: The sql_start of this TopIoInfo.
        :type sql_start: int
        """
        self._sql_start = sql_start

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
        if not isinstance(other, TopIoInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
