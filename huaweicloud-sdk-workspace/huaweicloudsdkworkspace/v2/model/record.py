# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Record:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'computer_name': 'str',
        'user_name': 'str',
        'terminal_mac': 'str',
        'terminal_name': 'str',
        'terminal_ip': 'str',
        'client_version': 'str',
        'terminal_type': 'str',
        'agent_version': 'str',
        'desktop_ip': 'str',
        'connection_start_time': 'str',
        'connection_setup_time': 'str',
        'connection_end_time': 'str',
        'is_reconnect': 'bool',
        'connection_failure_reason': 'str'
    }

    attribute_map = {
        'computer_name': 'computer_name',
        'user_name': 'user_name',
        'terminal_mac': 'terminal_mac',
        'terminal_name': 'terminal_name',
        'terminal_ip': 'terminal_ip',
        'client_version': 'client_version',
        'terminal_type': 'terminal_type',
        'agent_version': 'agent_version',
        'desktop_ip': 'desktop_ip',
        'connection_start_time': 'connection_start_time',
        'connection_setup_time': 'connection_setup_time',
        'connection_end_time': 'connection_end_time',
        'is_reconnect': 'is_reconnect',
        'connection_failure_reason': 'connection_failure_reason'
    }

    def __init__(self, computer_name=None, user_name=None, terminal_mac=None, terminal_name=None, terminal_ip=None, client_version=None, terminal_type=None, agent_version=None, desktop_ip=None, connection_start_time=None, connection_setup_time=None, connection_end_time=None, is_reconnect=None, connection_failure_reason=None):
        """Record

        The model defined in huaweicloud sdk

        :param computer_name: 计算机名。
        :type computer_name: str
        :param user_name: 用户名。
        :type user_name: str
        :param terminal_mac: 终端MAC地址。
        :type terminal_mac: str
        :param terminal_name: 终端名称。
        :type terminal_name: str
        :param terminal_ip: 终端IP。
        :type terminal_ip: str
        :param client_version: AccessClient版本。
        :type client_version: str
        :param terminal_type: 终端系统类型。
        :type terminal_type: str
        :param agent_version: AccessAgent版本。
        :type agent_version: str
        :param desktop_ip: 桌面IP。
        :type desktop_ip: str
        :param connection_start_time: 开始连接时间。
        :type connection_start_time: str
        :param connection_setup_time: 建立连接时间。
        :type connection_setup_time: str
        :param connection_end_time: 结束连接时间。
        :type connection_end_time: str
        :param is_reconnect: 是否重连。
        :type is_reconnect: bool
        :param connection_failure_reason: 连接失败原因。
        :type connection_failure_reason: str
        """
        
        

        self._computer_name = None
        self._user_name = None
        self._terminal_mac = None
        self._terminal_name = None
        self._terminal_ip = None
        self._client_version = None
        self._terminal_type = None
        self._agent_version = None
        self._desktop_ip = None
        self._connection_start_time = None
        self._connection_setup_time = None
        self._connection_end_time = None
        self._is_reconnect = None
        self._connection_failure_reason = None
        self.discriminator = None

        if computer_name is not None:
            self.computer_name = computer_name
        if user_name is not None:
            self.user_name = user_name
        if terminal_mac is not None:
            self.terminal_mac = terminal_mac
        if terminal_name is not None:
            self.terminal_name = terminal_name
        if terminal_ip is not None:
            self.terminal_ip = terminal_ip
        if client_version is not None:
            self.client_version = client_version
        if terminal_type is not None:
            self.terminal_type = terminal_type
        if agent_version is not None:
            self.agent_version = agent_version
        if desktop_ip is not None:
            self.desktop_ip = desktop_ip
        if connection_start_time is not None:
            self.connection_start_time = connection_start_time
        if connection_setup_time is not None:
            self.connection_setup_time = connection_setup_time
        if connection_end_time is not None:
            self.connection_end_time = connection_end_time
        if is_reconnect is not None:
            self.is_reconnect = is_reconnect
        if connection_failure_reason is not None:
            self.connection_failure_reason = connection_failure_reason

    @property
    def computer_name(self):
        """Gets the computer_name of this Record.

        计算机名。

        :return: The computer_name of this Record.
        :rtype: str
        """
        return self._computer_name

    @computer_name.setter
    def computer_name(self, computer_name):
        """Sets the computer_name of this Record.

        计算机名。

        :param computer_name: The computer_name of this Record.
        :type computer_name: str
        """
        self._computer_name = computer_name

    @property
    def user_name(self):
        """Gets the user_name of this Record.

        用户名。

        :return: The user_name of this Record.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this Record.

        用户名。

        :param user_name: The user_name of this Record.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def terminal_mac(self):
        """Gets the terminal_mac of this Record.

        终端MAC地址。

        :return: The terminal_mac of this Record.
        :rtype: str
        """
        return self._terminal_mac

    @terminal_mac.setter
    def terminal_mac(self, terminal_mac):
        """Sets the terminal_mac of this Record.

        终端MAC地址。

        :param terminal_mac: The terminal_mac of this Record.
        :type terminal_mac: str
        """
        self._terminal_mac = terminal_mac

    @property
    def terminal_name(self):
        """Gets the terminal_name of this Record.

        终端名称。

        :return: The terminal_name of this Record.
        :rtype: str
        """
        return self._terminal_name

    @terminal_name.setter
    def terminal_name(self, terminal_name):
        """Sets the terminal_name of this Record.

        终端名称。

        :param terminal_name: The terminal_name of this Record.
        :type terminal_name: str
        """
        self._terminal_name = terminal_name

    @property
    def terminal_ip(self):
        """Gets the terminal_ip of this Record.

        终端IP。

        :return: The terminal_ip of this Record.
        :rtype: str
        """
        return self._terminal_ip

    @terminal_ip.setter
    def terminal_ip(self, terminal_ip):
        """Sets the terminal_ip of this Record.

        终端IP。

        :param terminal_ip: The terminal_ip of this Record.
        :type terminal_ip: str
        """
        self._terminal_ip = terminal_ip

    @property
    def client_version(self):
        """Gets the client_version of this Record.

        AccessClient版本。

        :return: The client_version of this Record.
        :rtype: str
        """
        return self._client_version

    @client_version.setter
    def client_version(self, client_version):
        """Sets the client_version of this Record.

        AccessClient版本。

        :param client_version: The client_version of this Record.
        :type client_version: str
        """
        self._client_version = client_version

    @property
    def terminal_type(self):
        """Gets the terminal_type of this Record.

        终端系统类型。

        :return: The terminal_type of this Record.
        :rtype: str
        """
        return self._terminal_type

    @terminal_type.setter
    def terminal_type(self, terminal_type):
        """Sets the terminal_type of this Record.

        终端系统类型。

        :param terminal_type: The terminal_type of this Record.
        :type terminal_type: str
        """
        self._terminal_type = terminal_type

    @property
    def agent_version(self):
        """Gets the agent_version of this Record.

        AccessAgent版本。

        :return: The agent_version of this Record.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        """Sets the agent_version of this Record.

        AccessAgent版本。

        :param agent_version: The agent_version of this Record.
        :type agent_version: str
        """
        self._agent_version = agent_version

    @property
    def desktop_ip(self):
        """Gets the desktop_ip of this Record.

        桌面IP。

        :return: The desktop_ip of this Record.
        :rtype: str
        """
        return self._desktop_ip

    @desktop_ip.setter
    def desktop_ip(self, desktop_ip):
        """Sets the desktop_ip of this Record.

        桌面IP。

        :param desktop_ip: The desktop_ip of this Record.
        :type desktop_ip: str
        """
        self._desktop_ip = desktop_ip

    @property
    def connection_start_time(self):
        """Gets the connection_start_time of this Record.

        开始连接时间。

        :return: The connection_start_time of this Record.
        :rtype: str
        """
        return self._connection_start_time

    @connection_start_time.setter
    def connection_start_time(self, connection_start_time):
        """Sets the connection_start_time of this Record.

        开始连接时间。

        :param connection_start_time: The connection_start_time of this Record.
        :type connection_start_time: str
        """
        self._connection_start_time = connection_start_time

    @property
    def connection_setup_time(self):
        """Gets the connection_setup_time of this Record.

        建立连接时间。

        :return: The connection_setup_time of this Record.
        :rtype: str
        """
        return self._connection_setup_time

    @connection_setup_time.setter
    def connection_setup_time(self, connection_setup_time):
        """Sets the connection_setup_time of this Record.

        建立连接时间。

        :param connection_setup_time: The connection_setup_time of this Record.
        :type connection_setup_time: str
        """
        self._connection_setup_time = connection_setup_time

    @property
    def connection_end_time(self):
        """Gets the connection_end_time of this Record.

        结束连接时间。

        :return: The connection_end_time of this Record.
        :rtype: str
        """
        return self._connection_end_time

    @connection_end_time.setter
    def connection_end_time(self, connection_end_time):
        """Sets the connection_end_time of this Record.

        结束连接时间。

        :param connection_end_time: The connection_end_time of this Record.
        :type connection_end_time: str
        """
        self._connection_end_time = connection_end_time

    @property
    def is_reconnect(self):
        """Gets the is_reconnect of this Record.

        是否重连。

        :return: The is_reconnect of this Record.
        :rtype: bool
        """
        return self._is_reconnect

    @is_reconnect.setter
    def is_reconnect(self, is_reconnect):
        """Sets the is_reconnect of this Record.

        是否重连。

        :param is_reconnect: The is_reconnect of this Record.
        :type is_reconnect: bool
        """
        self._is_reconnect = is_reconnect

    @property
    def connection_failure_reason(self):
        """Gets the connection_failure_reason of this Record.

        连接失败原因。

        :return: The connection_failure_reason of this Record.
        :rtype: str
        """
        return self._connection_failure_reason

    @connection_failure_reason.setter
    def connection_failure_reason(self, connection_failure_reason):
        """Sets the connection_failure_reason of this Record.

        连接失败原因。

        :param connection_failure_reason: The connection_failure_reason of this Record.
        :type connection_failure_reason: str
        """
        self._connection_failure_reason = connection_failure_reason

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
        if not isinstance(other, Record):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
