# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keep_day': 'int',
        'backup_strategies': 'BackupStrategyDetail',
        'device_name': 'str',
        'server_port': 'str',
        'backup_param': 'str',
        'server_ips': 'list[str]'
    }

    attribute_map = {
        'keep_day': 'keep_day',
        'backup_strategies': 'backup_strategies',
        'device_name': 'device_name',
        'server_port': 'server_port',
        'backup_param': 'backup_param',
        'server_ips': 'server_ips'
    }

    def __init__(self, keep_day=None, backup_strategies=None, device_name=None, server_port=None, backup_param=None, server_ips=None):
        """BackupPolicy

        The model defined in huaweicloud sdk

        :param keep_day: 保留天数。
        :type keep_day: int
        :param backup_strategies: 
        :type backup_strategies: :class:`huaweicloudsdkdws.v2.BackupStrategyDetail`
        :param device_name: 备份设备。
        :type device_name: str
        :param server_port: 端口。
        :type server_port: str
        :param backup_param: 参数。
        :type backup_param: str
        :param server_ips: 备份介质服务IP。
        :type server_ips: list[str]
        """
        
        

        self._keep_day = None
        self._backup_strategies = None
        self._device_name = None
        self._server_port = None
        self._backup_param = None
        self._server_ips = None
        self.discriminator = None

        if keep_day is not None:
            self.keep_day = keep_day
        if backup_strategies is not None:
            self.backup_strategies = backup_strategies
        if device_name is not None:
            self.device_name = device_name
        if server_port is not None:
            self.server_port = server_port
        if backup_param is not None:
            self.backup_param = backup_param
        if server_ips is not None:
            self.server_ips = server_ips

    @property
    def keep_day(self):
        """Gets the keep_day of this BackupPolicy.

        保留天数。

        :return: The keep_day of this BackupPolicy.
        :rtype: int
        """
        return self._keep_day

    @keep_day.setter
    def keep_day(self, keep_day):
        """Sets the keep_day of this BackupPolicy.

        保留天数。

        :param keep_day: The keep_day of this BackupPolicy.
        :type keep_day: int
        """
        self._keep_day = keep_day

    @property
    def backup_strategies(self):
        """Gets the backup_strategies of this BackupPolicy.

        :return: The backup_strategies of this BackupPolicy.
        :rtype: :class:`huaweicloudsdkdws.v2.BackupStrategyDetail`
        """
        return self._backup_strategies

    @backup_strategies.setter
    def backup_strategies(self, backup_strategies):
        """Sets the backup_strategies of this BackupPolicy.

        :param backup_strategies: The backup_strategies of this BackupPolicy.
        :type backup_strategies: :class:`huaweicloudsdkdws.v2.BackupStrategyDetail`
        """
        self._backup_strategies = backup_strategies

    @property
    def device_name(self):
        """Gets the device_name of this BackupPolicy.

        备份设备。

        :return: The device_name of this BackupPolicy.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this BackupPolicy.

        备份设备。

        :param device_name: The device_name of this BackupPolicy.
        :type device_name: str
        """
        self._device_name = device_name

    @property
    def server_port(self):
        """Gets the server_port of this BackupPolicy.

        端口。

        :return: The server_port of this BackupPolicy.
        :rtype: str
        """
        return self._server_port

    @server_port.setter
    def server_port(self, server_port):
        """Sets the server_port of this BackupPolicy.

        端口。

        :param server_port: The server_port of this BackupPolicy.
        :type server_port: str
        """
        self._server_port = server_port

    @property
    def backup_param(self):
        """Gets the backup_param of this BackupPolicy.

        参数。

        :return: The backup_param of this BackupPolicy.
        :rtype: str
        """
        return self._backup_param

    @backup_param.setter
    def backup_param(self, backup_param):
        """Sets the backup_param of this BackupPolicy.

        参数。

        :param backup_param: The backup_param of this BackupPolicy.
        :type backup_param: str
        """
        self._backup_param = backup_param

    @property
    def server_ips(self):
        """Gets the server_ips of this BackupPolicy.

        备份介质服务IP。

        :return: The server_ips of this BackupPolicy.
        :rtype: list[str]
        """
        return self._server_ips

    @server_ips.setter
    def server_ips(self, server_ips):
        """Sets the server_ips of this BackupPolicy.

        备份介质服务IP。

        :param server_ips: The server_ips of this BackupPolicy.
        :type server_ips: list[str]
        """
        self._server_ips = server_ips

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
        if not isinstance(other, BackupPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
