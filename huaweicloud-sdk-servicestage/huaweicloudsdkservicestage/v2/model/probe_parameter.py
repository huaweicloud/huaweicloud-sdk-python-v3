# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProbeParameter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scheme': 'str',
        'host': 'str',
        'port': 'int',
        'path': 'str',
        'command': 'list[str]'
    }

    attribute_map = {
        'scheme': 'scheme',
        'host': 'host',
        'port': 'port',
        'path': 'path',
        'command': 'command'
    }

    def __init__(self, scheme=None, host=None, port=None, path=None, command=None):
        """ProbeParameter

        The model defined in huaweicloud sdk

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
        
        

        self._scheme = None
        self._host = None
        self._port = None
        self._path = None
        self._command = None
        self.discriminator = None

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
    def scheme(self):
        """Gets the scheme of this ProbeParameter.

        type为http类型时生效

        :return: The scheme of this ProbeParameter.
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """Sets the scheme of this ProbeParameter.

        type为http类型时生效

        :param scheme: The scheme of this ProbeParameter.
        :type scheme: str
        """
        self._scheme = scheme

    @property
    def host(self):
        """Gets the host of this ProbeParameter.

        type为http类型时生效。默认为POD的IP, 可以指定自定义的IP

        :return: The host of this ProbeParameter.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ProbeParameter.

        type为http类型时生效。默认为POD的IP, 可以指定自定义的IP

        :param host: The host of this ProbeParameter.
        :type host: str
        """
        self._host = host

    @property
    def port(self):
        """Gets the port of this ProbeParameter.

        type为http和tcp类型时生效。

        :return: The port of this ProbeParameter.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ProbeParameter.

        type为http和tcp类型时生效。

        :param port: The port of this ProbeParameter.
        :type port: int
        """
        self._port = port

    @property
    def path(self):
        """Gets the path of this ProbeParameter.

        type为http类型时生效。请求路径。

        :return: The path of this ProbeParameter.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ProbeParameter.

        type为http类型时生效。请求路径。

        :param path: The path of this ProbeParameter.
        :type path: str
        """
        self._path = path

    @property
    def command(self):
        """Gets the command of this ProbeParameter.

        type为command类型时生效。命令列表

        :return: The command of this ProbeParameter.
        :rtype: list[str]
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this ProbeParameter.

        type为command类型时生效。命令列表

        :param command: The command of this ProbeParameter.
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
        if not isinstance(other, ProbeParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
