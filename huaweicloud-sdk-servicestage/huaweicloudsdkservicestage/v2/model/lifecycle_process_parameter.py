# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LifecycleProcessParameter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'command': 'list[str]',
        'host': 'str',
        'port': 'int',
        'path': 'str'
    }

    attribute_map = {
        'command': 'command',
        'host': 'host',
        'port': 'port',
        'path': 'path'
    }

    def __init__(self, command=None, host=None, port=None, path=None):
        """LifecycleProcessParameter

        The model defined in huaweicloud sdk

        :param command: 命令参数，适用于command类型
        :type command: list[str]
        :param host: 默认为POD实例的IP地址。也可以自己指定。适用于http类型。
        :type host: str
        :param port: 端口号，适用于http类型。
        :type port: int
        :param path: 请求url，适用于http类型。
        :type path: str
        """
        
        

        self._command = None
        self._host = None
        self._port = None
        self._path = None
        self.discriminator = None

        if command is not None:
            self.command = command
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if path is not None:
            self.path = path

    @property
    def command(self):
        """Gets the command of this LifecycleProcessParameter.

        命令参数，适用于command类型

        :return: The command of this LifecycleProcessParameter.
        :rtype: list[str]
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this LifecycleProcessParameter.

        命令参数，适用于command类型

        :param command: The command of this LifecycleProcessParameter.
        :type command: list[str]
        """
        self._command = command

    @property
    def host(self):
        """Gets the host of this LifecycleProcessParameter.

        默认为POD实例的IP地址。也可以自己指定。适用于http类型。

        :return: The host of this LifecycleProcessParameter.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this LifecycleProcessParameter.

        默认为POD实例的IP地址。也可以自己指定。适用于http类型。

        :param host: The host of this LifecycleProcessParameter.
        :type host: str
        """
        self._host = host

    @property
    def port(self):
        """Gets the port of this LifecycleProcessParameter.

        端口号，适用于http类型。

        :return: The port of this LifecycleProcessParameter.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this LifecycleProcessParameter.

        端口号，适用于http类型。

        :param port: The port of this LifecycleProcessParameter.
        :type port: int
        """
        self._port = port

    @property
    def path(self):
        """Gets the path of this LifecycleProcessParameter.

        请求url，适用于http类型。

        :return: The path of this LifecycleProcessParameter.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this LifecycleProcessParameter.

        请求url，适用于http类型。

        :param path: The path of this LifecycleProcessParameter.
        :type path: str
        """
        self._path = path

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
        if not isinstance(other, LifecycleProcessParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
