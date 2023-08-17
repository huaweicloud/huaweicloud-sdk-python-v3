# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentProbe:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'delay': 'int',
        'timeout': 'int',
        'scheme': 'str',
        'host': 'str',
        'port': 'int',
        'path': 'str',
        'command': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'delay': 'delay',
        'timeout': 'timeout',
        'scheme': 'scheme',
        'host': 'host',
        'port': 'port',
        'path': 'path',
        'command': 'command'
    }

    def __init__(self, type=None, delay=None, timeout=None, scheme=None, host=None, port=None, path=None, command=None):
        """ComponentProbe

        The model defined in huaweicloud sdk

        :param type: 
        :type type: str
        :param delay: 表示启动后多久开始探测
        :type delay: int
        :param timeout: 表示探测超时时间
        :type timeout: int
        :param scheme: type为http类型时生效
        :type scheme: str
        :param host: type为http类型时生效。默认为POD的IP, 可以指定自定义的IP
        :type host: str
        :param port: type为http和tcp类型时生效。
        :type port: int
        :param path: type为http类型时生效。请求路径。
        :type path: str
        :param command: type为command类型时生效。命令列表
        :type command: list[str]
        """
        
        

        self._type = None
        self._delay = None
        self._timeout = None
        self._scheme = None
        self._host = None
        self._port = None
        self._path = None
        self._command = None
        self.discriminator = None

        self.type = type
        self.delay = delay
        self.timeout = timeout
        if scheme is not None:
            self.scheme = scheme
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if path is not None:
            self.path = path
        if command is not None:
            self.command = command

    @property
    def type(self):
        """Gets the type of this ComponentProbe.

        :return: The type of this ComponentProbe.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ComponentProbe.

        :param type: The type of this ComponentProbe.
        :type type: str
        """
        self._type = type

    @property
    def delay(self):
        """Gets the delay of this ComponentProbe.

        表示启动后多久开始探测

        :return: The delay of this ComponentProbe.
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this ComponentProbe.

        表示启动后多久开始探测

        :param delay: The delay of this ComponentProbe.
        :type delay: int
        """
        self._delay = delay

    @property
    def timeout(self):
        """Gets the timeout of this ComponentProbe.

        表示探测超时时间

        :return: The timeout of this ComponentProbe.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this ComponentProbe.

        表示探测超时时间

        :param timeout: The timeout of this ComponentProbe.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def scheme(self):
        """Gets the scheme of this ComponentProbe.

        type为http类型时生效

        :return: The scheme of this ComponentProbe.
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """Sets the scheme of this ComponentProbe.

        type为http类型时生效

        :param scheme: The scheme of this ComponentProbe.
        :type scheme: str
        """
        self._scheme = scheme

    @property
    def host(self):
        """Gets the host of this ComponentProbe.

        type为http类型时生效。默认为POD的IP, 可以指定自定义的IP

        :return: The host of this ComponentProbe.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ComponentProbe.

        type为http类型时生效。默认为POD的IP, 可以指定自定义的IP

        :param host: The host of this ComponentProbe.
        :type host: str
        """
        self._host = host

    @property
    def port(self):
        """Gets the port of this ComponentProbe.

        type为http和tcp类型时生效。

        :return: The port of this ComponentProbe.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ComponentProbe.

        type为http和tcp类型时生效。

        :param port: The port of this ComponentProbe.
        :type port: int
        """
        self._port = port

    @property
    def path(self):
        """Gets the path of this ComponentProbe.

        type为http类型时生效。请求路径。

        :return: The path of this ComponentProbe.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ComponentProbe.

        type为http类型时生效。请求路径。

        :param path: The path of this ComponentProbe.
        :type path: str
        """
        self._path = path

    @property
    def command(self):
        """Gets the command of this ComponentProbe.

        type为command类型时生效。命令列表

        :return: The command of this ComponentProbe.
        :rtype: list[str]
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this ComponentProbe.

        type为command类型时生效。命令列表

        :param command: The command of this ComponentProbe.
        :type command: list[str]
        """
        self._command = command

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
        if not isinstance(other, ComponentProbe):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
