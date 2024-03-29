# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSnapshotPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keep_day': 'str',
        'backup_strategies': 'list[BackupStrategyDetail]',
        'device_name': 'str',
        'server_ips': 'list[str]',
        'server_port': 'str',
        'backup_param': 'str'
    }

    attribute_map = {
        'keep_day': 'keep_day',
        'backup_strategies': 'backup_strategies',
        'device_name': 'device_name',
        'server_ips': 'server_ips',
        'server_port': 'server_port',
        'backup_param': 'backup_param'
    }

    def __init__(self, keep_day=None, backup_strategies=None, device_name=None, server_ips=None, server_port=None, backup_param=None):
        """ListSnapshotPolicyResponse

        The model defined in huaweicloud sdk

        :param keep_day: 保留天数。
        :type keep_day: str
        :param backup_strategies: 备份策略。
        :type backup_strategies: list[:class:`huaweicloudsdkdws.v2.BackupStrategyDetail`]
        :param device_name: 备份设备。
        :type device_name: str
        :param server_ips: 服务IP。
        :type server_ips: list[str]
        :param server_port: 服务端口。
        :type server_port: str
        :param backup_param: 参数。
        :type backup_param: str
        """
        
        super(ListSnapshotPolicyResponse, self).__init__()

        self._keep_day = None
        self._backup_strategies = None
        self._device_name = None
        self._server_ips = None
        self._server_port = None
        self._backup_param = None
        self.discriminator = None

        if keep_day is not None:
            self.keep_day = keep_day
        if backup_strategies is not None:
            self.backup_strategies = backup_strategies
        if device_name is not None:
            self.device_name = device_name
        if server_ips is not None:
            self.server_ips = server_ips
        if server_port is not None:
            self.server_port = server_port
        if backup_param is not None:
            self.backup_param = backup_param

    @property
    def keep_day(self):
        """Gets the keep_day of this ListSnapshotPolicyResponse.

        保留天数。

        :return: The keep_day of this ListSnapshotPolicyResponse.
        :rtype: str
        """
        return self._keep_day

    @keep_day.setter
    def keep_day(self, keep_day):
        """Sets the keep_day of this ListSnapshotPolicyResponse.

        保留天数。

        :param keep_day: The keep_day of this ListSnapshotPolicyResponse.
        :type keep_day: str
        """
        self._keep_day = keep_day

    @property
    def backup_strategies(self):
        """Gets the backup_strategies of this ListSnapshotPolicyResponse.

        备份策略。

        :return: The backup_strategies of this ListSnapshotPolicyResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.BackupStrategyDetail`]
        """
        return self._backup_strategies

    @backup_strategies.setter
    def backup_strategies(self, backup_strategies):
        """Sets the backup_strategies of this ListSnapshotPolicyResponse.

        备份策略。

        :param backup_strategies: The backup_strategies of this ListSnapshotPolicyResponse.
        :type backup_strategies: list[:class:`huaweicloudsdkdws.v2.BackupStrategyDetail`]
        """
        self._backup_strategies = backup_strategies

    @property
    def device_name(self):
        """Gets the device_name of this ListSnapshotPolicyResponse.

        备份设备。

        :return: The device_name of this ListSnapshotPolicyResponse.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this ListSnapshotPolicyResponse.

        备份设备。

        :param device_name: The device_name of this ListSnapshotPolicyResponse.
        :type device_name: str
        """
        self._device_name = device_name

    @property
    def server_ips(self):
        """Gets the server_ips of this ListSnapshotPolicyResponse.

        服务IP。

        :return: The server_ips of this ListSnapshotPolicyResponse.
        :rtype: list[str]
        """
        return self._server_ips

    @server_ips.setter
    def server_ips(self, server_ips):
        """Sets the server_ips of this ListSnapshotPolicyResponse.

        服务IP。

        :param server_ips: The server_ips of this ListSnapshotPolicyResponse.
        :type server_ips: list[str]
        """
        self._server_ips = server_ips

    @property
    def server_port(self):
        """Gets the server_port of this ListSnapshotPolicyResponse.

        服务端口。

        :return: The server_port of this ListSnapshotPolicyResponse.
        :rtype: str
        """
        return self._server_port

    @server_port.setter
    def server_port(self, server_port):
        """Sets the server_port of this ListSnapshotPolicyResponse.

        服务端口。

        :param server_port: The server_port of this ListSnapshotPolicyResponse.
        :type server_port: str
        """
        self._server_port = server_port

    @property
    def backup_param(self):
        """Gets the backup_param of this ListSnapshotPolicyResponse.

        参数。

        :return: The backup_param of this ListSnapshotPolicyResponse.
        :rtype: str
        """
        return self._backup_param

    @backup_param.setter
    def backup_param(self, backup_param):
        """Sets the backup_param of this ListSnapshotPolicyResponse.

        参数。

        :param backup_param: The backup_param of this ListSnapshotPolicyResponse.
        :type backup_param: str
        """
        self._backup_param = backup_param

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
        if not isinstance(other, ListSnapshotPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
